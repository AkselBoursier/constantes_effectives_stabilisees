# C2 — Produits officiels DESI : chaînes, quantiles, maxima et profils v0.1

## 0. Statut et portée

```text
statut : phase C2 active, accomplie au niveau de la provenance et de
         l'infrastructure de reproduction ;
date : 17 juillet 2026 ;
base : C1, N1, N3 et N5 ;
fonction : identifier exactement les produits officiels DESI DR2, empêcher les
           substitutions entre modèles, préparer une ingestion vérifiable et
           séparer les ancrages publiés des quantiles effectivement reproduits ;
ne vaut pas : ingestion achevée des chaînes, reproduction des quantiles DESI,
              profil de vraisemblance reconstruit ou verdict physique nouveau ;
blocage : les index et métadonnées officiels sont accessibles, mais les octets
          des chaînes et de l'archive volumineuse n'ont pas pu être téléchargés
          de manière fiable dans l'environnement courant ;
révision : obligatoire dès que l'archive ou les répertoires officiels sont
           montés localement et contrôlés par sommes de vérification.
```

Cette étape produit une **reproduction partielle des produits officiels**, non
une reproduction partielle des résultats numériques. La distinction est
substantielle : la structure, les modèles, les jeux de données, les fichiers
attendus et les ancrages publiés sont vérifiés ; les quantiles pondérés restent
vides tant que les échantillons et leurs poids ne sont pas lus.

## 1. Corpus officiel identifié

La [documentation DESI DR2](https://data.desi.lbl.gov/public/papers/y3/bao-cosmo-params/README.html)
sépare :

```text
cobaya/  : chaînes MCMC et échantillons postérieurs ;
iminuit/ : maxima du posterior et, lorsqu'ils existent, maxima de vraisemblance.
```

Le jeu de données directeur de `N3` est :

```text
desi-bao-all
+ Planck PR3 bas multipoles TT et EE
+ Planck PR4 NPIPE / CamSpec hauts multipoles TT, TE, EE
+ lentillage Planck PR4 + ACT DR6 v1.2.
```

Son identifiant complet est conservé dans
[`manifest_produits_officiels_c2.json`](manifest_produits_officiels_c2.json).

Un [supplément Zenodo officiel](https://doi.org/10.5281/zenodo.16644577)
publie également l'archive `dr2-bao-zenodo.zip`, annoncée à `1,3 GB`, avec la
somme MD5 :

```text
425623648b4b12515fa1943a5857fd46
```

Cette somme contrôle l'archive externe. Elle ne dispense pas de vérifier les
fichiers extraits contre le manifeste `SHA256SUMS` du dépôt DESI.

## 2. Trois constructions à ne pas confondre

### 2.1 `base_mnu`

```text
modèle : LambdaCDM + Sigma m_nu libre ;
frontière : Sigma m_nu > 0 ;
traitement spectral standard : trois états dégénérés ;
rôle : construction qui produit la borne publiée 0.0642 eV.
```

### 2.2 `base_mnu059`

```text
modèle : même paramétrisation dégénérée ;
frontière : Sigma m_nu > 0.059 eV ;
rôle : test d'un plancher scalaire proche du minimum normal.
```

Il ne contient pas, par son seul nom, les deux ordres ni les profils complets
d'oscillation. Sa comparaison avec `base_mnu` isole principalement un changement
de support et de volume de prior.

### 2.3 `base_mnu_binary_3`

La documentation DR2 définit séparément :

```text
Sigma m_nu libre
+ priors physiques de NuFIT 6.0
+ ordre normal ou inversé.
```

Cette construction porte la comparaison physique des ordres utilisée dans
l'analyse neutrino. Elle ne doit pas être remplacée par `base_mnu059`.

### 2.4 `base_mnu_w_wa`

```text
modèle : w0waCDM + Sigma m_nu libre ;
rôle : ouvrir la dégénérescence entre masse et histoire d'expansion ;
ancrage publié : Sigma m_nu < 0.163 eV à 95 %.
```

Le passage de `0.0642` à `0.163 eV` élargit la borne d'un facteur :

```text
0.163 / 0.0642 = 2.539.
```

Ce facteur ne quantifie pas une incertitude supplémentaire sur une grandeur
inchangée. Il compare deux modèles et deux espaces de paramètres.

## 3. Inventaire des chaînes sélectionnées

Chaque construction comprend quatre chaînes pour la combinaison `desi-bao-all`
avec le CMB directeur.

| Construction | Nombre de chaînes | Volume attendu | Fonction |
|---|---:|---:|---|
| `base_mnu` | 4 | `79 811 100` octets (`76,11 MiB`) | frontière à zéro |
| `base_mnu059` | 4 | `68 224 500` octets (`65,06 MiB`) | plancher scalaire normal |
| `base_mnu_w_wa` | 4 | `171 453 516` octets (`163,51 MiB`) | dégénérescence masse–énergie noire |
| **total** | **12** | **319 489 116 octets (`304,69 MiB`)** | corpus minimal de comparaison |

Les index officiels indiquent aussi, pour chaque modèle :

```text
chain.checkpoint ;
chain.covmat ;
chain.input.yaml ;
chain.updated.yaml ;
chain.margestats ;
chain.progress.
```

Le contrôle ne doit donc pas commencer par concaténer les quatre fichiers. Il
doit d'abord vérifier la configuration, les colonnes, la convergence, la présence
d'un éventuel post-traitement et l'identité du jeu de données.

## 4. Ancrages publiés et non reproduits

[`ancrages_publication_c2.csv`](ancrages_publication_c2.csv) conserve les
résultats utilisés comme tests de régression :

| Construction | Ancrage | Valeur | Statut C2 |
|---|---|---:|---|
| `base_mnu` | quantile supérieur 95 % | `0.0642 eV` | publié, non reproduit |
| `base_mnu` | écart-type marginal | `0.020 eV` | publié, non reproduit |
| `base_mnu_w_wa` | quantile supérieur 95 % | `0.163 eV` | publié, non reproduit |
| `base_mnu_binary_3` | borne sur la masse légère | `0.023 eV` | publiée, non reproduite |
| `base_mnu059` | quantile supérieur 95 % | — | à calculer depuis les poids |

Le tiret de la dernière ligne est un résultat documentaire positif : aucun
nombre n'est reconstruit depuis le nom du répertoire ou transposé depuis `C1`.

## 5. Infrastructure d'ingestion produite

Le script
[`analyse_produits_officiels_desi_c2.py`](analyse_produits_officiels_desi_c2.py)
réalise les opérations suivantes :

1. charge le manifeste officiel local ;
2. résout les répertoires des modèles sans supposer une arborescence unique ;
3. vérifie la présence et la taille des quatre chaînes attendues ;
4. calcule les sommes SHA-256 lorsque l'option est demandée ;
5. lit l'en-tête Cobaya et localise explicitement les colonnes de poids et de masse ;
6. combine les chaînes seulement après ces contrôles ;
7. calcule moyenne, écart-type, médiane et quantile 95 % pondérés ;
8. publie le nombre de lignes, la somme des poids et une taille effective de type Kish ;
9. produit un JSON détaillé et un CSV comparatif ;
10. retourne un état incomplet si un fichier manque ou possède une taille inattendue.

La règle de sûreté centrale est inscrite dans le code :

> Une chaîne officielle absente n'est jamais remplacée par la vraisemblance
> substitutive de `C1`.

Le lecteur a été contrôlé sur deux chaînes synthétiques pondérées et le script a
été compilé avec succès. Ce test valide le mécanisme de lecture ; il ne valide
pas le contenu absent des chaînes DESI.

## 6. Sortie obtenue dans l'environnement courant

[`resultats_c2.json`](resultats_c2.json) porte le statut :

```text
official_metadata_only_chains_not_fully_ingested
```

Les trois modèles sont marqués :

```text
not_inspected_no_data_root
```

Le fichier [`quantiles_c2.csv`](quantiles_c2.csv) conserve les lignes de modèles,
mais laisse toutes les statistiques vides. Cette absence empêche qu'une sortie
de diagnostic soit ultérieurement citée comme reproduction numérique.

## 7. Résultat positif de C2 à ce stade

La tension `N1–N3` doit désormais être décomposée en au moins quatre opérations
cosmologiques distinctes :

```text
A. base_mnu : vraisemblance + frontière Sigma > 0 ;
B. base_mnu059 : même famille de modèle + plancher scalaire ;
C. base_mnu_binary_3 : spectres physiques et deux ordres informés par NuFIT ;
D. base_mnu_w_wa : modification conjointe de l'expansion et de la masse.
```

`C1` avait montré la sensibilité au support dans un substitut minimal. `C2`
montre que les produits officiels eux-mêmes distinguent ces opérations et que
leur nomenclature contient une différence physique : imposer `0.059 eV` n'est
pas intégrer le problème des ordres.

La formulation active devient :

> La tension oscillations–cosmologie ne peut être quantifiée par la seule
> comparaison entre `0.0587` et `0.0642 eV`. Elle exige de distinguer le profil
> cosmologique non borné, la frontière statistique, le plancher scalaire, la
> paramétrisation physique des ordres et l'ouverture du modèle d'expansion.

## 8. Ce qui reste non acquis

Cette phase ne fournit pas encore :

```text
le quantile pondéré reproduit de base_mnu ;
le déplacement réel base_mnu -> base_mnu059 ;
le facteur d'évidence officiel entre les ordres ;
les corrélations mnu-H0-Omega_m-w0-wa ;
les maxima MAP et maximum de vraisemblance issus d'iminuit ;
le profil de vraisemblance en masse effective négative ;
les diagnostics R-1 ou tailles effectives des chaînes réelles ;
les profils numériques NuFIT 6.1.
```

## 9. Conditions de clôture de C2

`C2` ne sera close que lorsque les opérations suivantes auront produit des
sorties versionnées :

1. monter ou extraire l'archive officielle ;
2. contrôler le MD5 externe et les SHA-256 internes ;
3. lire les fichiers YAML et identifier les priors exacts ;
4. reproduire `0.0642 eV` depuis `base_mnu` ;
5. calculer le quantile propre à `base_mnu059` ;
6. analyser `base_mnu_binary_3` séparément et reconstruire la préférence d'ordre ;
7. reproduire `0.163 eV` depuis `base_mnu_w_wa` ;
8. comparer les échantillons aux maxima `iminuit` ;
9. publier les corrélations avec `H_0`, `Omega_m`, `w_0` et `w_a` ;
10. remplacer les Gaussiennes indépendantes de `N1` par des profils oscillatoires
    numériques dont la version et la provenance sont explicites.

## 10. Verdict C2 provisoire

```text
produits officiels localisés : oui ;
modèles et jeu CMB identifiés : oui ;
base_mnu059 distingué de base_mnu_binary_3 : oui ;
archive et somme MD5 documentées : oui ;
lecteur pondéré et contrôles de taille produits : oui ;
ingestion brute dans l'environnement courant : non ;
quantiles officiels reproduits : non ;
fonction positive : rendre la prochaine ingestion falsifiable et empêcher les
                    substitutions entre frontière, plancher et ordre ;
statut : C2 ouverte, infrastructure et provenance stabilisées.
```
