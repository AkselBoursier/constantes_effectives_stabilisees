# T1.2 — Fiche d’extraction de `alpha_s` par formes d’événements `e+e-` v0.1

## 0. Statut

```text
statut : fiche primaire de chaîne d’extraction ;
date de contrôle : 21 juillet 2026 ;
source de référence : JHEP 06 (2025) 200 ;
texte de travail : arXiv:2501.18173v1 ;
fonction : rendre contrôlable une extraction multi-échelles par formes d’événements ;
ne vaut pas : reproduction du fit, arbitrage général sur les corrections de puissance,
               validation indépendante des covariances expérimentales ou moyenne mondiale.
```

## 1. Porteur et transformation

### Porteurs à distinguer

```text
observables principales : thrust T ou tau = 1 - T, paramètre C et résolution trois jets y_23 ;
paramètres ajustés : alpha_s(M_Z) et paramètre non perturbatif alpha_0 ;
relation physique testée : évolution des prédictions avec l’énergie Q ;
objet T1 : cohérence conjointe des distributions, du running perturbatif et des
           corrections de puissance dans le domaine de fit déclaré.
```

Les masses de l’hémisphère lourd et la différence de masses d’hémisphères sont étudiées
séparément, mais ne font pas partie du fit principal en raison du comportement de leurs
corrections non perturbatives dans la limite à deux jets.

### Transformations déclarées

```text
énergie de centre de masse Q : 22 à 207 GeV ;
variation de l’échelle de renormalisation ;
variation des limites de fit ;
variation du schéma de masses hadroniques ;
variation du modèle et des paramètres non perturbatifs ;
variation des effets de masses lourdes ;
passage d’un observable isolé au fit conjoint T-C-y_23.
```

Le fait que les distributions changent avec `Q` ne constitue pas une variation temporelle
de `alpha_s`. Le test porte sur le running et sur la cohérence d’une même paramétrisation
de référence avec plusieurs énergies.

## 2. Données et domaine expérimental

L’analyse utilise des distributions issues de :

```text
ALEPH ;
DELPHI ;
JADE ;
L3 ;
OPAL ;
SLD ;
TRISTAN ;
combinaison JADE–OPAL pour y_23.
```

Les énergies s’étendent de 22 à 207 GeV. Les données sont accessibles dans HEPData. Le
jeu disponible représente environ 1400 points avant sélection ; jusqu’à 915 points sont
retenus selon les domaines de fit. Le fit central conjoint `C-T-y_23` emploie 895 bins.

Les données `y_23` de JADE et OPAL sont omises aux énergies déjà couvertes par la
combinaison JADE–OPAL, afin d’éviter une duplication explicite.

## 3. Domaine des observables et limites de fit

Le domaine inférieur est déterminé par une procédure dépendant de l’énergie et de
l’observable. Elle tient compte :

- de la position du pic de la distribution ;
- de son déplacement avec l’énergie ;
- d’une contrainte imposant que l’échelle dynamique de renormalisation ne descende pas
  sous 4 GeV.

La borne inférieure finale est le maximum des limites produites par ces critères. Pour
`y_23`, la borne est gelée à celle du pôle Z au-dessus de `M_Z` lorsque le pic se déplace
vers des valeurs trop petites.

Les bornes supérieures sont proches des limites cinématiques à trois partons :

```text
C : 0.6 ;
tau : 0.3 ;
y_23 : 0.3.
```

Ces limites font partie de la définition opérationnelle de l’extraction. Leur variation
contribue à l’incertitude théorique.

## 4. Théorie perturbative

```text
processus : e+e- -> 3 jets ;
ordre : NNLO, c’est-à-dire termes jusqu’à alpha_s^3 pour les distributions ;
code : EERAD3 ;
méthode de soustraction : antenna subtraction ;
schéma du couplage : MS-bar ;
échelle de renormalisation : dynamique dans le réglage central.
```

L’échelle dynamique est construite à partir de la valeur moyenne, au premier ordre, du
moment transverse du gluon perturbatif qui produit le troisième jet pour chaque valeur de
l’observable.

Le calcul principal est à ordre fixe. Les auteurs discutent le risque d’utiliser des
prédictions résommées dans une région dominée par trois jets bien séparés, où leur domaine
de validité peut devenir incertain. Pour T1, l’absence de résommation dans la chaîne
centrale est enregistrée comme choix de domaine et d’approximation, non comme verdict
général contre les méthodes résommées.

## 5. Corrections non perturbatives et masses

Les corrections de puissance sont calculées pour la région à trois jets et paramétrées
par `alpha_0`, ajusté simultanément avec `alpha_s`.

L’emploi de plusieurs énergies réduit la dégénérescence entre les contributions
perturbatives et non perturbatives, plus fortement que le seul ajustement conjoint de
plusieurs observables au pôle Z.

Le schéma central pour les masses hadroniques est le schéma `E`. Les schémas `p`, `D` et
standard sont utilisés comme variations. Les effets de masses des quarks lourds sont
corrigés au moyen de simulations Monte-Carlo selon le protocole repris de l’étude
antérieure.

La dépendance au schéma de masse hadronique est une dépendance de représentation de la
chaîne expérimentale et théorique. Elle ne constitue pas une variation de l’objet
`alpha_s`.

## 6. Fit, covariance et optimisation

Tous les bins, observables, expériences et énergies retenus sont indexés dans un même
`chi^2` global.

La covariance contient :

```text
incertitudes statistiques ;
corrélations statistiques disponibles ;
covariance des systématiques ;
traitement symétrisé des erreurs systématiques asymétriques par leur maximum.
```

Contrairement à l’étude précédente, aucune erreur théorique n’est ajoutée directement à
la définition du `chi^2`, car les corrélations bin-à-bin correspondantes ne sont pas
suffisamment spécifiées. Les incertitudes théoriques sont évaluées par variations du
réglage.

Le minimum dans le plan `(alpha_s, alpha_0)` est recherché sur des grilles rectangulaires
adaptatives. Le réglage typique part d’une grille `11 x 11`, centrée vers
`alpha_s = 0.12` et `alpha_0 = 0.5`, puis réduit l’intervalle pendant quatre itérations.

Pour le fit central conjoint :

```text
nombre de bins : 895 ;
chi^2 / N_deg : 1.26.
```

## 7. Résultat

```text
alpha_s(M_Z) = 0.1181
               ^{+0.0002}_{-0.0005}  expérimental
               ^{+0.0018}_{-0.0021}  théorique.
```

L’incertitude théorique agrège les variations d’échelle, les effets de masse, les limites
de fit, les schémas non perturbatifs et les incertitudes non perturbatives.

Le paramètre est rapporté directement à `M_Z`. Les données multi-échelles contraignent
son effet sur les distributions à travers le running, mais l’article ne fournit pas une
collection de mesures indépendantes de `alpha_s(Q)` à chacune des énergies.

## 8. Typage des chemins

```text
chemin physique : running de alpha_s dans les prédictions NNLO selon Q et mu_R ;
chaîne expérimentale : distributions multi-expériences, sélection des bins et covariance ;
chemin inférentiel : fit conjoint alpha_s-alpha_0 et choix des domaines ;
chemin computationnel : EERAD3, grilles adaptatives et variations du réglage ;
chemin de représentation : définitions de formes, schémas de masses hadroniques ;
chemin non perturbatif : corrections de puissance à trois jets et paramètre alpha_0 ;
histoire temporelle : non pertinente.
```

## 9. Test de maintien provisoire

La chaîne teste si une valeur de référence de `alpha_s(M_Z)`, évoluée dans les
prédictions à plusieurs énergies, permet une description cohérente de distributions
différentes lorsque la composante non perturbative est ajustée et que les schémas de
masse sont variés.

Le porteur provisoire du maintien est :

```text
la cohérence multi-échelles du running perturbatif et de la séparation
perturbatif / non perturbatif dans les domaines de fit déclarés.
```

Ce résultat est plus fort qu’une simple proximité numérique avec une moyenne mondiale,
mais plus faible qu’une mesure directe et indépendante du running à chaque énergie.

## 10. Dimensions et portée

```text
dimension objet : coefficient alpha_s(M_Z) et évolution RG des prédictions ;
dimension accès : distributions, covariance, domaines de fit et ajustement alpha_s-alpha_0 ;
dimension constitution : factorisation perturbative / corrections de puissance et
                         définition des observables hadroniques ;
portée physique : compatibilité d’un même paramètre avec des données multi-échelles ;
portée épistémologique : sensibilité aux schémas de masses, limites et modèles NP ;
portée ontologique : non engagée.
```

## 11. Limites et opération suivante

La structure de la chaîne est suffisamment extraite pour T1.4. Une reproduction complète
requiert encore :

1. tableaux numériques de toutes les distributions et covariances retenues ;
2. implémentation et configuration exactes d’EERAD3 ;
3. fonctions de corrections de puissance et valeurs des paramètres auxiliaires ;
4. détail numérique de chacune des variations composant l’enveloppe théorique ;
5. correction Monte-Carlo des masses lourdes ;
6. procédure exacte de construction de l’échelle dynamique pour chaque observable.

Ces éléments ne bloquent pas la sélection et la fiche lattice de T1.3. Ils bloqueront une
reproduction numérique indépendante du résultat final.