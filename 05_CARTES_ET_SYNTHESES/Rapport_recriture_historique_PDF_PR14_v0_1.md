# Rapport de réécriture historique ciblée des PDF de la PR nº 14 v0.1

## 0. Statut

```text
date : 18 juillet 2026 ;
dépôt : AkselBoursier/constantes_effectives_stabilisees, privé ;
branche : agent/contribution-q1-information-chemin ;
base non réécrite : main ;
outil : git-filter-repo ;
statut du rapport : contrôles locaux préalables au push.
```

L'opération retire deux PDF de toute l'ascendance de la branche cumulative tout
en conservant sa granularité. Elle ne fusionne pas la pull request (PR) nº 14 et
ne vaut pas garantie de purge des copies extérieures à la branche distante.

## 1. Sauvegarde privée

Le bundle complet, créé et vérifié avant la réécriture, est conservé hors
OneDrive et hors du dépôt GitHub :

```text
C:\git-rewrite\constantes_effectives_stabilisees-20260718-202059\backup\constantes_effectives_stabilisees_avant_recriture.bundle
```

Ce bundle contient l'histoire originale et les PDF retirés. Il doit rester
privé.

## 2. Périmètre strict du filtre

Les quatre chemins filtrés sont :

```text
93_RENDU_PUBLIC/ESSAI_tentative/sources/Eran_Tal_2022_1-s2.0-S0263224117305730-main.pdf
93_RENDU_PUBLIC/ESSAI_tentative/sources/N_de_Courtenay_SI_2022posc_a_00397.pdf
93_LABORATOIRE_EDITORIAL_EXPERIMENTAL/ESSAI_tentative/sources/Eran_Tal_2022_1-s2.0-S0263224117305730-main.pdf
93_LABORATOIRE_EDITORIAL_EXPERIMENTAL/ESSAI_tentative/sources/N_de_Courtenay_SI_2022posc_a_00397.pdf
```

Le filtre a été exécuté exclusivement sur
`refs/heads/agent/contribution-q1-information-chemin`, avec inversion des quatre
chemins et conservation des commits vides par `--prune-empty never`.

## 3. Identité et continuité de l'histoire

| Contrôle | Avant | Après réécriture | Verdict |
|---|---:|---:|---|
| SHA de tête | `7b2d33085c01f6007862b861a3594722c9649c4f` | `e5452336957a5c44118c7f409f2fd021a91a2cf2` | changement attendu |
| SHA de l'arbre final | `c5c02a52c5d72d8fc5edf3f6a915eabe4be3701b` | `c5c02a52c5d72d8fc5edf3f6a915eabe4be3701b` | identique |
| Commits dans `main..branche` | 333 | 333 | identique |
| Commits de fusion dans `main..branche` | 44 | 44 | identique |

La comparaison ordonnée des dates au format ISO strict, noms d'auteurs,
adresses d'auteurs et messages de commits est identique avant et après. Les
commits vides sont conservés. La table ancien SHA vers nouveau SHA est
versionnée dans
`05_CARTES_ET_SYNTHESES/Mapping_SHA_recriture_PDF_PR14_2026-07-18.tsv`.

## 4. Recherche des objets interdits

La sortie de `git rev-list --objects agent/contribution-q1-information-chemin`
ne contient plus aucun des deux noms suivants :

```text
Eran_Tal_2022_1-s2.0-S0263224117305730-main.pdf
N_de_Courtenay_SI_2022posc_a_00397.pdf
```

Les deux PDF ne sont donc plus atteignables depuis la branche réécrite.

## 5. Audits avant push

Le contrôle absolu `git diff --check main...HEAD` a retrouvé des anomalies
d'espacement antérieures à la réécriture. Aucun nettoyage opportuniste du
corpus historique n'a été effectué.

Le contrôle a été remplacé par une comparaison des sorties avant et après
filtrage. Les deux commandes ont produit le code de sortie `2`, correspondant
aux anomalies historiques déjà présentes. Les deux inventaires sont
strictement identiques : `Compare-Object` ne produit aucune différence.

Les inventaires sont conservés hors du dépôt dans :

```text
C:\git-rewrite\constantes_effectives_stabilisees-20260718-202059\backup\git_diff_check_avant.txt
C:\git-rewrite\constantes_effectives_stabilisees-20260718-202059\backup\git_diff_check_apres_filtrage.txt
```

Le commit documentaire postérieur au filtrage a été contrôlé séparément par
`git diff --check e5452336957a5c44118c7f409f2fd021a91a2cf2..HEAD` et
n'introduit aucune anomalie.

### 5.1. Assainissement et fins de ligne Windows

Le contrôle d'assainissement exécuté dans le clone Windows signalait cinq
JSON comme `would-change`, alors que `git ls-files --eol` établissait pour ces
fichiers le statut `i/lf w/crlf attr/text=auto` : leurs blobs Git étaient
enregistrés en LF et leur copie de travail était matérialisée en CRLF.

La tentative de rematérialisation physique en LF n'a pas été retenue : elle
créait des différences Git sans portée documentaire. Une extraction
diagnostique directe des blobs confirmait par ailleurs que les JSON
effectivement extraits étaient propres ; deux chemins accentués n'ont pas été
matérialisés correctement par l'outil d'extraction Windows.

Le contrôleur `audit/sanitize_conversation_exports.mjs` a donc été corrigé
pour normaliser CRLF et LF en mémoire avant comparaison. Cette correction ne
modifie ni les JSON, ni les blobs historiques, ni les 333 commits réécrits.
Après correction, le contrôle sans `--write` déclare tous les fichiers propres
et retourne le code `0`. Le diff ciblé sur les cinq JSON est vide et
`git status` ne signale que le contrôleur et le présent rapport avant
amendement.

Les journaux avant et après correction sont conservés hors du dépôt :

```text
C:\git-rewrite\constantes_effectives_stabilisees-20260718-202059\backup\audit_assainissement.txt
C:\git-rewrite\constantes_effectives_stabilisees-20260718-202059\backup\audit_assainissement_normalise_EOL.txt
```

### 5.2. Résultats des contrôles documentaires et techniques

Les contrôles bloquants donnent les résultats suivants :

```text
audit structurel : réussi, 436 fichiers Markdown, 0 erreur et 1669 avertissements ;
audit des liens : réussi, aucun lien brisé signalé ;
audit de l'encodage : réussi, aucun fichier Markdown non UTF-8 ;
assainissement conversationnel : réussi, tous les fichiers propres, code 0 ;
compilation Python : réussie, code 0 ;
fichiers suivis sous data_external : aucun ;
PDF suivi dans le laboratoire éditorial : aucun.
```

Les avertissements structurels et les titres dupliqués inventoriés par l'audit
d'encodage appartiennent au corpus historique et aux exports bruts ; ils ne
constituent pas des erreurs bloquantes. L'inventaire informatif des placeholders
recense 21 extractions de sources contenant des lacunes déjà conventionnées ;
aucun placeholder n'a été supprimé ou modifié par l'opération.

### 5.3. Test synthétique C2 dans un environnement isolé

L'installation locale du fichier complet `requirements.txt` a échoué à deux
reprises dans l'environnement Python préexistant, Matplotlib restant
indisponible. Cette difficulté relève de l'environnement local de paquets et
non de la réécriture Git.

Le lecteur `analyse_produits_officiels_desi_c2.py` n'importe que NumPy parmi
les dépendances externes. Un environnement virtuel Python 3.12 isolé a donc été
créé hors du dépôt, NumPy y a été installé, puis le test synthétique C2 a été
exécuté avec succès :

```text
interpréteur : C:\git-rewrite\constantes_effectives_stabilisees-20260718-202059\backup\venv-c2-python312\Scripts\python.exe ;
Python : 3.12.0 ;
NumPy : 2.5.1 ;
code de sortie du test synthétique C2 : 0 ;
journal : C:\git-rewrite\constantes_effectives_stabilisees-20260718-202059\backup\audit_c2_self_test_venv.txt ;
sorties : C:\git-rewrite\constantes_effectives_stabilisees-20260718-202059\backup\c2-self-test-venv.
```

Le test établit le bon fonctionnement du chemin synthétique interne avec des
chaînes générées pour l'autocontrôle. Il ne reproduit aucun résultat réel de
DESI. SciPy et Matplotlib n'ont pas été retirés du fichier de dépendances ; leur
installation complète demeure contrôlée par GitHub Actions après le push de la
branche réécrite. Le venv, ses sorties et les journaux restent hors du dépôt et
n'ont modifié ni le corpus ni les JSON.

## 6. Portée du push et limites résiduelles

Le push autorisé vise seulement
`HEAD:refs/heads/agent/contribution-q1-information-chemin`, avec un lease
explicite fixé à l'ancienne tête
`7b2d33085c01f6007862b861a3594722c9649c4f`. `main`, les autres branches et les
tags ne doivent pas être poussés.

La réécriture remplace l'histoire atteignable depuis la branche distante, mais
elle ne supprime pas automatiquement les objets présents dans d'anciens clones,
dans des caches locaux ou serveurs, dans le bundle privé, ni dans d'anciennes
vues ou références conservées par GitHub. Cette limite résiduelle est compatible
avec la fonction de l'opération : empêcher l'intégration des PDF dans l'histoire
candidate à `main` tout en conservant la lignée détaillée de la branche.
