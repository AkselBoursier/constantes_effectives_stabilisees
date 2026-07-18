# Protocole de réécriture historique ciblée des PDF de la PR nº 14 v0.1

## 0. Statut et finalité

```text
date : 18 juillet 2026 ;
dépôt : AkselBoursier/constantes_effectives_stabilisees ;
visibilité : privée ;
branche à réécrire : agent/contribution-q1-information-chemin ;
base à ne pas réécrire : main ;
fonction : retirer deux PDF de tous les commits de la branche cumulative sans
           aplatir l'histoire intellectuelle et documentaire ;
outil : git-filter-repo ;
méthode de fusion après contrôle : fusion normale avec commit de fusion ;
ne vaut pas : purge garantie des caches, clones ou anciennes vues serveur.
```

Le dépôt privé reste accessible au connecteur GitHub autorisé. Le passage en privé
réduit l'exposition ordinaire des anciens commits, mais ne remplace pas le nettoyage
de l'histoire avant l'intégration à `main`.

## 1. Décision de méthode

La fusion par squash est abandonnée parce qu'elle réduirait les centaines de commits
de la branche à un seul commit dans l'histoire de `main`.

La méthode retenue est :

```text
sauvegarde privée complète ;
réécriture ciblée de la seule branche cumulative ;
retrait des deux chemins PDF avant et après le renommage du laboratoire ;
conservation de la chronologie, des messages, des auteurs et de la topologie ;
production d'une table ancien SHA -> nouveau SHA ;
comparaison stricte de l'arbre final ;
force-push avec lease de la seule branche ;
audit GitHub ;
fusion normale après validation.
```

Les SHA changent à partir du premier commit affecté, parce qu'un SHA identifie le
contenu et l'ascendance exacts d'un commit. La continuité intelligible est préservée
par les messages, dates, auteurs, ordre, topologie et table de correspondance.

## 2. Chemins à retirer de toute l'histoire de la branche

Les quatre chemins suivants couvrent la présence des deux fichiers avant et après le
renommage de `93_RENDU_PUBLIC` :

```text
93_RENDU_PUBLIC/ESSAI_tentative/sources/Eran_Tal_2022_1-s2.0-S0263224117305730-main.pdf
93_RENDU_PUBLIC/ESSAI_tentative/sources/N_de_Courtenay_SI_2022posc_a_00397.pdf
93_LABORATOIRE_EDITORIAL_EXPERIMENTAL/ESSAI_tentative/sources/Eran_Tal_2022_1-s2.0-S0263224117305730-main.pdf
93_LABORATOIRE_EDITORIAL_EXPERIMENTAL/ESSAI_tentative/sources/N_de_Courtenay_SI_2022posc_a_00397.pdf
```

Aucun autre PDF, document, fichier binaire ou chemin ne doit être filtré par cette
opération.

## 3. Contraintes absolues

1. Ne pas exécuter la réécriture dans le clone quotidien situé sous OneDrive.
2. Travailler dans un clone temporaire placé hors OneDrive.
3. Ne jamais réécrire `main`.
4. Ne jamais pousser `--all`, `--mirror` ou des tags réécrits.
5. Ne pousser que `agent/contribution-q1-information-chemin`.
6. Ne pas utiliser `git push --force` simple ; utiliser un lease explicite portant
   l'ancien SHA de tête.
7. Ne pas supprimer la sauvegarde privée après réussite.
8. Ne pas reprendre le travail depuis l'ancien clone après le force-push.
9. Arrêter l'opération si l'arbre final, le nombre de commits ou la séquence des
   messages diffèrent hors effet explicitement prévu.

## 4. Prérequis

Dans PowerShell :

```powershell
python --version
git --version
python -m pip install --upgrade git-filter-repo
git filter-repo --version
```

`git-filter-repo` doit être installé par la distribution Python réellement utilisée
par Git.

## 5. Variables de travail

Adapter seulement `$Source` si le chemin local diffère :

```powershell
$Source = "C:\Users\admin\OneDrive\Documents\constantes_effectives_stabilisees"
$Branch = "agent/contribution-q1-information-chemin"
$RepoUrl = "https://github.com/AkselBoursier/constantes_effectives_stabilisees.git"
$Stamp = Get-Date -Format "yyyyMMdd-HHmmss"
$Root = "C:\git-rewrite\constantes_effectives_stabilisees-$Stamp"
$Backup = Join-Path $Root "backup"
$Rewrite = Join-Path $Root "rewrite"
New-Item -ItemType Directory -Force -Path $Backup | Out-Null
```

## 6. Contrôle du clone source

```powershell
Set-Location $Source

git status --short
if ($LASTEXITCODE -ne 0) { throw "git status a échoué" }
if ((git status --porcelain).Length -ne 0) { throw "Arbre de travail non propre" }

$currentBranch = git branch --show-current
if ($currentBranch -ne $Branch) { throw "Branche active incorrecte : $currentBranch" }

git fetch origin
$OldHead = git rev-parse $Branch
$RemoteHead = git rev-parse "origin/$Branch"
if ($OldHead -ne $RemoteHead) { throw "La branche locale et la branche distante divergent" }

$OldTree = git rev-parse "$OldHead^{tree}"
$OldCount = [int](git rev-list --count "main..$Branch")
$OldMergeCount = [int](git rev-list --min-parents=2 --count "main..$Branch")

$OldHead | Set-Content -Encoding utf8 (Join-Path $Backup "old_head.txt")
$OldTree | Set-Content -Encoding utf8 (Join-Path $Backup "old_tree.txt")
$OldCount | Set-Content -Encoding utf8 (Join-Path $Backup "old_commit_count.txt")
$OldMergeCount | Set-Content -Encoding utf8 (Join-Path $Backup "old_merge_count.txt")

git log --reverse --date=iso-strict `
  --pretty=format:"%H`t%P`t%ad`t%an`t%ae`t%s" `
  "main..$Branch" |
  Set-Content -Encoding utf8 (Join-Path $Backup "commits_avant.tsv")

git log --all --date=iso-strict --decorate=full --oneline |
  Set-Content -Encoding utf8 (Join-Path $Backup "refs_et_commits_avant.txt")
```

## 7. Sauvegarde privée complète

Créer un bundle contenant toutes les références atteignables depuis le clone source :

```powershell
$Bundle = Join-Path $Backup "constantes_effectives_stabilisees_avant_recriture.bundle"
git bundle create $Bundle --all
if ($LASTEXITCODE -ne 0) { throw "Création du bundle échouée" }
git bundle verify $Bundle
if ($LASTEXITCODE -ne 0) { throw "Vérification du bundle échouée" }
```

Ce bundle contient l'histoire originale, y compris les PDF. Il doit rester privé,
hors du dépôt GitHub et hors de tout dossier partagé publiquement.

## 8. Clone temporaire hors OneDrive

```powershell
git clone --no-hardlinks $Bundle $Rewrite
Set-Location $Rewrite

git remote remove origin 2>$null
git remote add origin $RepoUrl

git checkout $Branch
if ($LASTEXITCODE -ne 0) { throw "Checkout de la branche échoué" }

$CheckHead = git rev-parse HEAD
if ($CheckHead -ne $OldHead) { throw "Le clone temporaire ne part pas de l'ancienne tête" }
```

## 9. Réécriture ciblée

Exécuter exactement :

```powershell
git filter-repo --force `
  --refs "refs/heads/$Branch" `
  --invert-paths `
  --path "93_RENDU_PUBLIC/ESSAI_tentative/sources/Eran_Tal_2022_1-s2.0-S0263224117305730-main.pdf" `
  --path "93_RENDU_PUBLIC/ESSAI_tentative/sources/N_de_Courtenay_SI_2022posc_a_00397.pdf" `
  --path "93_LABORATOIRE_EDITORIAL_EXPERIMENTAL/ESSAI_tentative/sources/Eran_Tal_2022_1-s2.0-S0263224117305730-main.pdf" `
  --path "93_LABORATOIRE_EDITORIAL_EXPERIMENTAL/ESSAI_tentative/sources/N_de_Courtenay_SI_2022posc_a_00397.pdf" `
  --prune-empty never

if ($LASTEXITCODE -ne 0) { throw "Réécriture git-filter-repo échouée" }
```

`--prune-empty never` conserve le jalon administratif de retrait même s'il devient
un commit sans différence de contenu. La granularité du parcours reste ainsi maximale.

`git-filter-repo` peut retirer le remote `origin` par sécurité. Le rétablir avant le
push :

```powershell
if (-not (git remote | Select-String -SimpleMatch "origin")) {
  git remote add origin $RepoUrl
}
```

## 10. Contrôles d'identité du résultat

```powershell
$NewHead = git rev-parse $Branch
$NewTree = git rev-parse "$NewHead^{tree}"
$NewCount = [int](git rev-list --count "main..$Branch")
$NewMergeCount = [int](git rev-list --min-parents=2 --count "main..$Branch")

if ($NewHead -eq $OldHead) { throw "La tête n'a pas changé : le filtre n'a pas agi" }
if ($NewTree -ne $OldTree) { throw "L'arbre final a changé" }
if ($NewCount -ne $OldCount) { throw "Le nombre de commits a changé" }
if ($NewMergeCount -ne $OldMergeCount) { throw "Le nombre de commits de fusion a changé" }
```

Le SHA de l'arbre final doit être strictement identique : les PDF avaient déjà été
retirés du dernier état, donc seule l'ascendance doit changer.

Comparer la séquence sémantique des commits sans leurs SHA et parents :

```powershell
git log --reverse --date=iso-strict `
  --pretty=format:"%ad`t%an`t%ae`t%s" `
  "main..$Branch" |
  Set-Content -Encoding utf8 (Join-Path $Backup "commits_apres_semantique.tsv")

Get-Content (Join-Path $Backup "commits_avant.tsv") |
  ForEach-Object { ($_ -split "`t", 3)[2] } |
  Set-Content -Encoding utf8 (Join-Path $Backup "commits_avant_semantique.tsv")

$SemanticDiff = Compare-Object `
  (Get-Content (Join-Path $Backup "commits_avant_semantique.tsv")) `
  (Get-Content (Join-Path $Backup "commits_apres_semantique.tsv"))
if ($SemanticDiff) {
  $SemanticDiff | Format-Table | Out-String | Write-Host
  throw "La séquence sémantique des commits a changé"
}
```

Vérifier l'absence totale des quatre chemins dans l'ascendance de la branche :

```powershell
$Forbidden = @(
  "Eran_Tal_2022_1-s2.0-S0263224117305730-main.pdf",
  "N_de_Courtenay_SI_2022posc_a_00397.pdf"
)
$Objects = git rev-list --objects $Branch
foreach ($name in $Forbidden) {
  if ($Objects | Select-String -SimpleMatch $name) {
    throw "Objet interdit encore atteignable dans la branche : $name"
  }
}
```

## 11. Table de correspondance des SHA

`git-filter-repo` produit :

```text
.git/filter-repo/commit-map
```

Copier cette table dans le corpus propre :

```powershell
$MapSource = Join-Path $Rewrite ".git\filter-repo\commit-map"
$MapTarget = Join-Path $Rewrite "05_CARTES_ET_SYNTHESES\Mapping_SHA_recriture_PDF_PR14_2026-07-18.tsv"
Copy-Item $MapSource $MapTarget
```

Ajouter ensuite un rapport :

```text
05_CARTES_ET_SYNTHESES/Rapport_recriture_historique_PDF_PR14_v0_1.md
```

Le rapport doit consigner :

- ancien et nouveau SHA de tête ;
- ancien et nouveau SHA d'arbre final ;
- nombres de commits et de commits de fusion ;
- quatre chemins filtrés ;
- résultat des recherches d'objets interdits ;
- emplacement du bundle privé ;
- résultats des audits ;
- limite : absence de garantie de purge des caches, clones ou anciennes vues GitHub.

Créer un commit thématique pour la table et le rapport :

```powershell
git add 05_CARTES_ET_SYNTHESES/Mapping_SHA_recriture_PDF_PR14_2026-07-18.tsv
git add 05_CARTES_ET_SYNTHESES/Rapport_recriture_historique_PDF_PR14_v0_1.md
git commit -m "Documenter la réécriture historique ciblée des PDF"
```

Ce commit documentaire est nécessairement postérieur à la table produite par le filtre.

## 12. Audits avant push

```powershell
git diff --check main...HEAD
python audit/audit_structure_corpus.py
bash audit/audit_liens.sh
bash audit/audit_encodage.sh
node audit/sanitize_conversation_exports.mjs
python -m compileall -q `
  "02_CYCLES_PHYSIQUES/03_Cycle_neutrinos/01_REPRISE_COMPUTATIONNELLE_N1_N3" `
  "02_CYCLES_PHYSIQUES/10_Cycle_fixite_electrofaible_dynamique/calculs" `
  "audit"
```

Exécuter aussi le test synthétique `C2` selon le workflow GitHub. Aucune sortie ne doit
être qualifiée de DESI reproduite.

## 13. Push réécrit avec lease explicite

Le push ne doit viser qu'une branche :

```powershell
git push `
  --force-with-lease="refs/heads/$Branch`:$OldHead" `
  origin `
  "HEAD:refs/heads/$Branch"

if ($LASTEXITCODE -ne 0) { throw "Force-push avec lease refusé ou échoué" }
```

Le lease protège contre toute modification distante intervenue depuis la capture de
`$OldHead`.

Ne pousser ni `main`, ni les tags, ni les autres branches.

## 14. Après le push

1. Vérifier que la PR nº 14 reste ouverte et pointe vers la nouvelle tête.
2. Vérifier que le diff final contre `main` est inchangé hors table et rapport.
3. Attendre la réussite du workflow renforcé.
4. Mettre à jour l'audit de pré-fusion et la description de la PR.
5. Ne plus utiliser l'ancien clone comme source de push.
6. Renommer l'ancien clone en archive privée ou le conserver déconnecté de `origin`.
7. Créer un clone quotidien neuf depuis le dépôt nettoyé.
8. Replacer `data_external/desi_dr2` dans ce clone neuf ou créer un lien local ; ne
   jamais l'ajouter à Git.

## 15. Fusion après réécriture

Après validation du rapport et du workflow :

```text
méthode autorisée : Create a merge commit ;
méthode également techniquement possible : Rebase and merge ;
méthode recommandée : Create a merge commit, afin de préserver explicitement la
                       branche cumulative comme lignée intégrée ;
méthode non nécessaire : Squash and merge.
```

La décision de fusion reste explicite. La réécriture nettoie l'histoire candidate ; elle
ne fusionne pas automatiquement la PR nº 14.
