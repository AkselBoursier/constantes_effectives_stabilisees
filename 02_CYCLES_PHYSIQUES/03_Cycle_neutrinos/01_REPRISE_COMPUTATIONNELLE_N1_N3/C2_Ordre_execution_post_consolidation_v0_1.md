# C2 — Ordre d’exécution post-consolidation v0.1

## 0. Fonction et statut

```text
fonction : ouvrir la phase P1 depuis le main consolidé ;
branche : agent/c2-ingestion-locale-desi-dr2 ;
entrée locale : data_external/desi_dr2 ;
données brutes : hors Git ;
sorties dérivées : versionnables après contrôle ;
objectif : clore ou suspendre proprement C2, sans extrapolation physique.
```

La consolidation de la PR nº 14 est close. Le chantier reprend désormais sur une
branche thématique neuve. Le présent document fixe l’ordre d’exécution ; il ne
remplace ni l’instruction détaillée v0.1 ni le rapport scientifique final v0.2.

## 1. Point de départ réel

Le lecteur actuel `analyse_produits_officiels_desi_c2.py` constitue un premier
lecteur de chaînes. Il vérifie les tailles déclarées, peut calculer les SHA-256 et
produit des statistiques pondérées combinées.

Il ne suffit pas encore à clore C2, car l’état versionné ne couvre pas entièrement :

```text
base_mnu_binary_3 ;
chaînes natives contre chaînes post-traitées ;
statistiques séparées par chaîne ;
lecture de chain.margestats ;
diagnostics de convergence ;
corrélations pondérées ;
produits iminuit ;
MAP contre maximum de vraisemblance ;
profils ou scans effectivement disponibles.
```

Le manifeste officiel versionné contient actuellement les trois modèles
`base_mnu`, `base_mnu059` et `base_mnu_w_wa`. Le quatrième modèle doit être
découvert depuis l’archive réelle ; aucun chemin ne doit être inventé.

## 2. Porte A — État Git et protection des données

Avant toute analyse :

```bash
git status --short
git branch --show-current
git rev-parse HEAD
git check-ignore -v data_external/desi_dr2
git ls-files data_external
```

Résultats requis :

```text
branche active : agent/c2-ingestion-locale-desi-dr2 ;
arbre de travail propre au départ ;
data_external/desi_dr2 explicitement ignoré ;
aucun fichier sous data_external suivi par Git.
```

Toute apparition de chaînes, archives, caches ou environnements dans l’index Git
est bloquante.

## 3. Porte B — Intégrité et racine des produits

1. Inventorier récursivement `data_external/desi_dr2`.
2. Vérifier, si l’archive est présente :

```text
MD5 attendu de dr2-bao-zenodo.zip :
425623648b4b12515fa1943a5857fd46
```

3. Découvrir la véritable racine contenant `SHA256SUMS`, `cobaya/`, `iminuit/`
et la documentation locale.
4. Vérifier les SHA-256 de tous les fichiers effectivement utilisés.
5. N’enregistrer dans les sorties versionnées que des chemins relatifs au dépôt.

Une somme incorrecte ou une racine ambiguë arrête l’analyse numérique.

## 4. Porte C — Inventaire positif des quatre modèles

Pour chaque modèle, produire un statut explicite :

```text
présent et natif ;
présent mais post-traité ;
présent sous une autre combinaison de données ;
partiel ;
absent ;
ambigu.
```

Modèles :

```text
base_mnu ;
base_mnu059 ;
base_mnu_binary_3 ;
base_mnu_w_wa.
```

Le jeu CMB directeur pour les trois modèles déjà inscrits au manifeste reste :

```text
desi-bao-all_planck2018-lowl-TT-clik_planck2018-lowl-EE-clik_planck-NPIPE-highl-CamSpec-TTTEEE_planck-act-dr6-lensing
```

`base_mnu059` ne doit jamais être assimilé à `base_mnu_binary_3`.

## 5. Porte D — Extension minimale du lecteur avant verdict

Le lecteur doit être étendu ou accompagné de contrôles séparés pour produire :

```text
statistiques par chaîne et combinées ;
poids, support, taille effective et quantiles ;
comparaison avec chain.margestats ;
lecture de chain.checkpoint et chain.progress ;
diagnostics de convergence disponibles ;
corrélations pondérées avec les paramètres cosmologiques présents ;
inventaire des produits iminuit ;
qualification exacte des maxima ;
présence ou absence de scans et profils.
```

Un maximum ponctuel ne doit pas être nommé « profil ». Un MAP ne doit pas être
nommé « maximum de vraisemblance ».

## 6. Porte E — Tests numériques directeurs

Les ancrages publiés restent des tests de régression, non des valeurs à injecter :

```text
base_mnu : quantile supérieur 95 % = 0,0642 eV ;
base_mnu059 : quantile à calculer effectivement ;
base_mnu_w_wa : quantile supérieur 95 % = 0,163 eV ;
base_mnu_binary_3 : masse légère < 0,023 eV, seulement si la quantité et
                    la construction présentes correspondent réellement.
```

Chaque résultat doit porter l’un des statuts suivants :

```text
publié ;
reproduit ;
calcul dérivé ;
non disponible ;
non acquis.
```

Tout écart doit être expliqué par une convention identifiable — burn-in,
importance sampling, définition du quantile, support, prior, modèle ou produit —
et non corrigé silencieusement.

## 7. Porte F — Sorties attendues

Les sorties versionnables restent :

```text
manifest_local_desi_dr2_c2.json ;
checksums_desi_dr2_c2.sha256 ;
inventaire_produits_desi_dr2_c2.csv ;
resultats_c2.json ;
quantiles_c2.csv ;
diagnostics_convergence_c2.csv ;
correlations_c2.csv ;
maxima_iminuit_c2.csv ;
C2_Resultats_ingestion_locale_DESI_DR2_v0_2.md.
```

Les fichiers doivent exclure les chemins absolus, les noms d’utilisateur, les
chaînes brutes, les caches et les sorties volumineuses.

## 8. Critère de décision

C2 est close seulement si les ancrages utiles sont reproduits ou si leurs écarts
sont expliqués, si `base_mnu059` est effectivement calculé, si
`base_mnu_binary_3` est traité comme produit distinct, et si maxima, profils et
convergence sont qualifiés correctement.

Si un produit indispensable manque, C2 est suspendue proprement avec un manifeste
positif des absences. Une absence documentée ne doit pas bloquer indéfiniment
l’ouverture du cycle 1.

## 9. Discipline Git

Le travail reste sur cette branche jusqu’au verdict C2. Une pull request ne sera
ouverte qu’après production des sorties contrôlées ou d’un rapport de suspension
scientifiquement suffisant.

Avant tout commit :

```bash
python audit/audit_structure_corpus.py
bash audit/audit_liens.sh
bash audit/audit_encodage.sh
node audit/sanitize_conversation_exports.mjs
python -m compileall -q audit 02_CYCLES_PHYSIQUES
git ls-files data_external
```

Le commit final visé demeure :

```text
Clore C2 par ingestion locale des produits DESI DR2
```
