# C2 — Instruction à un agent local pour l’extraction et l’analyse DESI DR2 v0.1

## 0. Fonction et statut

```text
fonction : permettre à Codex, Cowork ou un autre agent local d’achever l’ingestion
           contrôlée des produits officiels DESI DR2 déjà téléchargés ;
racine locale annoncée : data_external/desi_dr2 ;
entrée suivie par Git : manifest_produits_officiels_c2.json et scripts C2 ;
sorties suivies par Git : manifestes locaux, contrôles, tableaux et rapports dérivés ;
interdit : versionner l’archive, les chaînes brutes, les caches ou les environnements ;
ne vaut pas : nouvel ajustement cosmologique, reproduction depuis les spectres ou
              conclusion de nouvelle physique.
```

`data_external/` est ignoré par `.gitignore`. L’agent doit interrompre le travail si
les fichiers volumineux apparaissent dans `git status` ou dans l’index Git.

## 1. Règles scientifiques non négociables

1. Ne jamais remplacer une chaîne manquante par le substitut gaussien de `C1`.
2. Ne jamais déduire un résultat depuis le nom d’un dossier.
3. Distinguer strictement :
   - `base_mnu` : somme libre, frontière à zéro ;
   - `base_mnu059` : plancher scalaire à `0,059 eV` ;
   - `base_mnu_binary_3` : construction physique des ordres avec information
     oscillatoire ;
   - `base_mnu_w_wa` : extension `w0waCDM`.
4. Un résultat n’est marqué `reproduit` que s’il provient de la lecture effective
   des échantillons et de leurs poids.
5. Un maximum de posterior (`MAP`) n’est pas un maximum de vraisemblance.
6. Un fichier `iminuit` isolé ne constitue pas, à lui seul, un profil de
   vraisemblance.
7. Toute absence, différence de taille, somme de contrôle incorrecte, colonne
   ambiguë ou convergence insuffisante doit produire un statut explicite et non
   une valeur de remplacement.

## 2. État Git initial

Depuis la racine du dépôt :

```bash
git status --short
git branch --show-current
git rev-parse HEAD
```

Conserver ces trois sorties dans le rapport d’exécution. Ne pas lancer de
réorganisation générale du dépôt. Ne modifier que le chantier `C2` et les fichiers
de navigation explicitement nécessaires.

Vérifier que les données sont ignorées :

```bash
git check-ignore -v data_external/desi_dr2
```

Si la commande ne confirme pas une règle `.gitignore`, arrêter avant toute suite.

## 3. Identifier ce qui a été téléchargé

Examiner récursivement `data_external/desi_dr2` et déterminer lequel de ces cas est
présent :

```text
A. archive dr2-bao-zenodo.zip non extraite ;
B. archive et répertoire extrait ;
C. répertoire extrait seulement ;
D. sélection manuelle de sous-répertoires.
```

Produire localement :

```text
data_external/desi_dr2/_controle/inventaire_initial.txt
data_external/desi_dr2/_controle/arborescence_niveau_4.txt
```

Ne pas les ajouter à Git.

## 4. Contrôler l’archive externe

Lorsque `dr2-bao-zenodo.zip` est présent, calculer son MD5 et le comparer à :

```text
425623648b4b12515fa1943a5857fd46
```

Sous PowerShell :

```powershell
Get-FileHash .\data_external\desi_dr2\dr2-bao-zenodo.zip -Algorithm MD5
```

Sous Bash :

```bash
md5sum data_external/desi_dr2/dr2-bao-zenodo.zip
```

Refuser l’extraction ou l’analyse si la somme diffère. Enregistrer le résultat dans
le manifeste local dérivé.

Extraire, si nécessaire, dans :

```text
data_external/desi_dr2/extracted/
```

Ne pas déplacer les fichiers extraits dans un répertoire suivi par Git.

## 5. Découvrir la véritable racine des produits

Ne pas supposer que l’archive ajoute ou non un répertoire de tête. Rechercher le
répertoire qui contient simultanément, directement ou sous un niveau intermédiaire :

```text
SHA256SUMS
cobaya/
iminuit/
README.html ou documentation équivalente
```

Nommer cette racine locale `DESI_DATA_ROOT` dans les scripts ou commandes. Conserver
son chemin relatif depuis la racine Git ; ne jamais enregistrer un chemin absolu
propre à la machine dans un fichier versionné.

## 6. Vérifier les sommes internes

Lire `SHA256SUMS` depuis `DESI_DATA_ROOT`. Vérifier au minimum tous les fichiers
utilisés par `C2` ; préférer une vérification complète de l’archive si le coût reste
raisonnable.

Produire dans le dossier suivi par Git :

```text
checksums_desi_dr2_c2.sha256
```

Ce fichier doit contenir uniquement les chemins relatifs des produits effectivement
analysés et leurs SHA-256 calculés localement. Ajouter une colonne ou un fichier JSON
associé indiquant :

```text
expected_sha256 ; actual_sha256 ; match ; size_bytes.
```

Ne pas recopier aveuglément `SHA256SUMS` : le but est d’attester ce qui a réellement
été lu sur cette machine.

## 7. Jeu CMB directeur

Le jeu directeur est exactement :

```text
desi-bao-all_planck2018-lowl-TT-clik_planck2018-lowl-EE-clik_
planck-NPIPE-highl-CamSpec-TTTEEE_planck-act-dr6-lensing
```

La chaîne ci-dessus est écrite sur deux lignes pour la lisibilité ; le nom du
répertoire réel ne contient aucun retour à la ligne.

Pour les trois modèles déjà inscrits dans le manifeste, les répertoires attendus
sont :

```text
cobaya/base_mnu/<JEU_CMB_DIRECTEUR>/
cobaya/base_mnu059/<JEU_CMB_DIRECTEUR>/
cobaya/base_mnu_w_wa/<JEU_CMB_DIRECTEUR>/
```

Pour `base_mnu_binary_3`, rechercher le répertoire réel dans l’archive et enregistrer
son chemin exact. Ne pas inventer un chemin si ce produit se trouve dans une archive,
un sous-dossier ou une combinaison de données différente.

Faire la même recherche sous `iminuit/`.

## 8. Fichiers à inventorier par modèle

Pour chacun des quatre modèles, inventorier lorsqu’ils existent :

```text
chain.1.txt
chain.2.txt
chain.3.txt
chain.4.txt
chain.checkpoint
chain.covmat
chain.input.yaml
chain.updated.yaml
chain.margestats
chain.progress
```

Inventorier également tout fichier post-traité :

```text
chain.post.*.txt
chain.post.*.yaml
```

Ne pas mélanger chaînes natives et chaînes post-traitées. Si un résultat publié
repose sur importance sampling, l’identifier dans les YAML et traiter le jeu
post-traité comme un produit distinct.

Sous `iminuit/<MODELE>/<JEU_DE_DONNEES>/`, inventorier :

```text
bestfit.minimum.txt
bestfit.minimum
bestfit.bestfit.txt
bestfit.bestfit
```

ainsi que tout fichier de scan ou de profil réellement présent. L’absence d’un
`bestfit.bestfit*` doit être conservée comme absence ; elle n’autorise pas à appeler
le MAP « maximum de vraisemblance ».

## 9. Produire un manifeste local versionnable

Créer ou mettre à jour :

```text
manifest_local_desi_dr2_c2.json
inventaire_produits_desi_dr2_c2.csv
```

Le manifeste JSON doit contenir au minimum :

```text
version de l’instruction ;
date et heure UTC d’exécution ;
commit Git de départ ;
chemin relatif de DESI_DATA_ROOT ;
MD5 de l’archive et résultat du contrôle ;
SHA-256 de chaque fichier utilisé ;
taille de chaque fichier ;
modèle ; jeu de données ; type natif ou post-traité ;
noms exacts des paramètres et colonnes ;
présence des métadonnées et produits iminuit ;
statut d’ingestion par modèle ;
avertissements et absences.
```

Ne jamais enregistrer le nom d’utilisateur Windows ou un chemin absolu.

## 10. Première ingestion avec le lecteur existant

Depuis la racine du dépôt :

```bash
python 02_CYCLES_PHYSIQUES/03_Cycle_neutrinos/01_REPRISE_COMPUTATIONNELLE_N1_N3/analyse_produits_officiels_desi_c2.py \
  --manifest 02_CYCLES_PHYSIQUES/03_Cycle_neutrinos/01_REPRISE_COMPUTATIONNELLE_N1_N3/manifest_produits_officiels_c2.json \
  --data-root data_external/desi_dr2/extracted \
  --output-dir 02_CYCLES_PHYSIQUES/03_Cycle_neutrinos/01_REPRISE_COMPUTATIONNELLE_N1_N3/sorties_locales_c2 \
  --hash-files
```

Adapter `--data-root` à la racine réellement découverte. Ne pas adapter le manifeste
pour masquer une mauvaise racine.

Exécuter aussi le test interne :

```bash
python 02_CYCLES_PHYSIQUES/03_Cycle_neutrinos/01_REPRISE_COMPUTATIONNELLE_N1_N3/analyse_produits_officiels_desi_c2.py \
  --manifest 02_CYCLES_PHYSIQUES/03_Cycle_neutrinos/01_REPRISE_COMPUTATIONNELLE_N1_N3/manifest_produits_officiels_c2.json \
  --output-dir data_external/desi_dr2/_controle/self_test_c2 \
  --self-test \
  --allow-missing
```

## 11. Contrôles des chaînes réelles

Pour chaque chaîne :

1. lire l’en-tête et enregistrer les noms de colonnes exacts ;
2. identifier la colonne de poids et la définition de la colonne de masse ;
3. vérifier la finitude et la positivité des poids ;
4. vérifier le support du paramètre de masse ;
5. comparer les quatre chaînes séparément avant concaténation ;
6. lire `chain.checkpoint` et `chain.progress` ;
7. calculer une taille effective pondérée ;
8. utiliser GetDist, si disponible, pour comparer les statistiques et diagnostics
   avec `chain.margestats` ;
9. signaler tout écart dû au burn-in, à l’importance sampling ou à une convention de
   quantile.

Ne pas déclarer une convergence satisfaisante sur la seule base de la présence de
quatre fichiers.

## 12. Résultats numériques à reproduire

### 12.1 `base_mnu`

Calculer depuis les poids :

```text
moyenne ; écart-type ; médiane ; quantile supérieur 95 % ; support observé ;
taille effective ; statistiques par chaîne et combinées.
```

Tests de régression publiés :

```text
quantile supérieur 95 % : 0,0642 eV ;
écart-type marginal : environ 0,020 eV.
```

Comparer le résultat calculé au fichier `chain.margestats` et à l’ancrage publié.
Un écart doit être expliqué ; ne pas écraser l’ancrage.

### 12.2 `base_mnu059`

Calculer les mêmes statistiques. Vérifier que le support respecte le plancher réel
encodé dans le YAML et dans les échantillons. Publier son quantile à 95 %, qui ne
doit pas être déduit de `C1`.

### 12.3 `base_mnu_w_wa`

Calculer les mêmes statistiques et tester l’ancrage publié :

```text
quantile supérieur 95 % : 0,163 eV.
```

Calculer les corrélations pondérées entre la masse et, selon les noms réellement
présents :

```text
H0 ; Omega_m ; w0 ; wa ; A_s ou logA ; tau.
```

Ne pas substituer une colonne dérivée à une colonne échantillonnée sans le signaler.

### 12.4 `base_mnu_binary_3`

Lire d’abord les YAML et la documentation locale. Déterminer :

```text
comment les deux ordres sont encodés ;
quel paramètre représente la masse la plus légère ou la somme ;
quels profils ou priors NuFIT sont utilisés ;
comment les poids des ordres sont normalisés ;
si les échantillons sont natifs, combinés ou post-traités.
```

Reproduire uniquement les quantités effectivement définies par ce produit. L’ancrage
publié sur la masse légère (`< 0,023 eV`) est un test, non une valeur à injecter.
Ne pas assimiler une préférence d’ordre à un facteur de Bayes sans normalisation
d’évidence explicitement justifiée.

## 13. Maxima et profils

Pour chaque modèle disposant de produits `iminuit` :

1. extraire séparément le MAP et le maximum de vraisemblance lorsqu’ils existent ;
2. conserver les valeurs de `-logpost`, `-loglike` ou `chi2` avec leurs noms exacts ;
3. comparer la masse au mode marginal des chaînes ;
4. enregistrer les autres paramètres pertinents ;
5. rechercher des scans ou grilles de profil.

Si seuls des maxima ponctuels sont disponibles, écrire :

```text
profil de vraisemblance : non reconstruit ; maxima ponctuels seulement.
```

## 14. Sorties suivies par Git

Produire ou mettre à jour dans le dossier `C2` :

```text
manifest_local_desi_dr2_c2.json
checksums_desi_dr2_c2.sha256
inventaire_produits_desi_dr2_c2.csv
resultats_c2.json
quantiles_c2.csv
diagnostics_convergence_c2.csv
correlations_c2.csv
maxima_iminuit_c2.csv
C2_Resultats_ingestion_locale_DESI_DR2_v0_2.md
```

Les tableaux doivent distinguer :

```text
publié ; reproduit ; calcul dérivé ; non disponible ; non acquis.
```

Les sorties volumineuses, caches GetDist, figures intermédiaires et copies de chaînes
restent sous `data_external/`.

## 15. Rapport scientifique v0.2

Le rapport doit répondre sans extrapolation à ces questions :

1. `0,0642 eV` est-il reproduit depuis les poids ?
2. Quel est le résultat effectif de `base_mnu059` ?
3. Quel déplacement vient du support et quel déplacement vient de la
   paramétrisation physique des ordres ?
4. `0,163 eV` est-il reproduit sous `w0waCDM` ?
5. Quelles corrélations expliquent l’élargissement ?
6. Les maxima ponctuels se situent-ils sur, au-dessus ou sous la frontière ?
7. Un profil numérique est-il réellement disponible ?
8. Quels diagnostics de convergence limitent l’interprétation ?
9. Qu’est-ce qui reste nécessaire pour remplacer NuFIT 6.0 par NuFIT 6.1 ?

Ne pas conclure à une anomalie physique tant que les effets du support, des priors,
du modèle d’expansion et des likelihoods ne sont pas séparés.

## 16. Contrôles du dépôt

Avant commit :

```bash
git status --short
git diff --stat
git diff -- .gitignore 02_CYCLES_PHYSIQUES/03_Cycle_neutrinos/01_REPRISE_COMPUTATIONNELLE_N1_N3
python audit/audit_structure_corpus.py
bash audit/audit_liens.sh
bash audit/audit_encodage.sh
bash audit/audit_placeholders.sh
```

Vérifier explicitement qu’aucun chemin sous `data_external/` n’est suivi :

```bash
git ls-files data_external
```

La sortie doit être vide.

## 17. Commit attendu

Un seul commit thématique est préférable après validation de toutes les sorties :

```text
Clore C2 par ingestion locale des produits DESI DR2
```

Le message de synthèse doit déclarer :

```text
modèles effectivement ingérés ;
ancrages reproduits ou non ;
présence ou absence des maxima et profils ;
audit du corpus ;
absence de données brutes dans Git.
```

Ne pas fusionner dans `main` et ne pas fermer la PR de consolidation sans instruction
explicite de l’auteur.
