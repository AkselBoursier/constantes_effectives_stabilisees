# α2 — Matrice des chaînes de détermination de la valeur de basse énergie de `alpha` v0.1

## 0. Statut

```text
statut : matrice exploratoire de dépendance ;
date : 26 juillet 2026 ;
opération : α2, issue #36 ;
appui : A2_Extraction_CODATA_alpha_v0_1.md ;
fonction : séparer mesure première, relation de passage, dépendances communes,
           valeur inférée et insertion dans l’ajustement CODATA ;
autorité : descriptive et préparatoire ;
ne vaut pas : verdict final de cohérence, préférence entre chaînes,
               calcul indépendant ou nouvelle valeur recommandée.
```

## 1. Matrice principale

| Voie | Mesure ou donnée première | Relation de passage vers `alpha` | Entrées auxiliaires | Sortie publiée | Insertion CODATA | Limite principale |
|---|---|---|---|---|---|---|
| anomalie magnétique de l’électron | `ae(exp)` mesuré sur un électron unique en piège de Penning | inversion de `ae(th; alpha, rapports de masses, coefficients QED, contributions hadroniques et électrofaibles)` | correction théorique `delta_th(e)` ; rapports de masses leptoniques ; coefficients QED | `alpha^-1 = 137.035 999 166(15)` | D1 + D2 ; ajustement conjoint avec les autres voies | valeur conditionnelle à l’expression QED ; circularité possible si la même voie est présentée à la fois comme détermination et test indépendant |
| recul atomique du rubidium | `h/m(87Rb)` par interférométrie atomique | `h/m(X) ≐ [Ar(e)/Ar(X)] [c alpha²/(2R_inf)]` | `Ar(87Rb)` ; `Ar(e)` ; `R_inf` ; `h` et `c` exacts ; corrections expérimentales | `alpha^-1 = 137.035 999 206(11)` | D3 + D5 ; D5 corrélée à D6 et D11 | résultat dépendant de la chaîne métrologique et du budget de systématiques ; non indépendant de toutes les autres données de masse et de spectroscopie |
| recul atomique du césium | `h/m(133Cs)` par interférométrie atomique | même équation d’observation que pour le rubidium | `Ar(133Cs)` ; `Ar(e)` ; `R_inf` ; `h` et `c` exacts ; corrections expérimentales | `alpha^-1 = 137.035 999 046(27)` | D4 + D6 ; D6 corrélée à D5 et D11 | résidu normalisé `4.7` avant expansion ; cause de la discordance non établie |
| valeur recommandée CODATA | aucune mesure première unique | ajustement par moindres carrés des équations d’observation | D1–D6 ; constantes ajustées ; covariances ; facteurs d’expansion | `alpha^-1 = 137.035 999 177(21)` | sortie de l’ajustement complet | ne doit pas être décrite comme une quatrième mesure indépendante |

## 2. Niveaux de production de l’énoncé numérique

### 2.1 Niveau expérimental

```text
Fan et al. : ae(exp) ;
Morel et al. : h/m(87Rb) ;
Parker et al. : h/m(133Cs) ;
AMDC : Ar(87Rb), Ar(133Cs).
```

Ces données n’ont pas toutes `alpha` pour observable première.

### 2.2 Niveau relationnel

```text
voie QED : ae(exp) confronté à ae(th; alpha, ...) ;
voies de recul : h/m(X) relié à alpha par Ar(e), Ar(X) et R_inf.
```

Le niveau relationnel transforme des observables hétérogènes en valeurs comparables de `alpha^-1`.

### 2.3 Niveau d’ajustement

```text
entrée : données, équations, incertitudes et covariances ;
opération : ajustement global par moindres carrés ;
traitement de l’incohérence : facteur d’expansion 2.5 sur D1–D6 ;
sortie : valeur recommandée et covariance avec d’autres constantes.
```

## 3. Dépendances communes

### 3.1 Commun aux deux voies de recul

```text
forme de l’équation d’observation ;
Ar(e) ;
R_inf ;
h exact ;
c exact ;
architecture de propagation des incertitudes ;
connaissance des masses atomiques relatives.
```

### 3.2 Commun à toutes les voies dans CODATA

```text
ajustement global ;
critère de résidu normalisé ;
facteur d’expansion 2.5 ;
constantes ajustées communes ;
convention de basse énergie de la sortie alpha.
```

### 3.3 Spécifique à la voie QED

```text
mesure de ae ;
coefficients perturbatifs QED ;
terme d’ordre dix ;
contributions de boucles leptoniques ;
contributions hadroniques et électrofaibles ;
incertitude théorique additive.
```

### 3.4 Spécifique aux voies de recul

```text
interféromètre atomique ;
transferts d’impulsion photonique ;
alignement des faisceaux ;
fronts d’onde et phase de Gouy ;
rotation terrestre ;
interactions atomiques et indice de réfraction ;
mesure de fréquence et masses atomiques.
```

## 4. Corrélations et indépendances

| Relation | Statut actuel |
|---|---|
| D5–D6 | corrélation d’entrée explicite `0.1032` |
| D5–D11 | corrélation d’entrée explicite `0.0678` |
| D6–D11 | corrélation d’entrée explicite `0.0630` |
| D1–D3–D4 | aucune corrélation d’entrée supérieure à `0.0001` déclarée dans la Table XXVI |
| rubidium–césium | méthodes proches et équation commune, mais appareils, espèces et budgets de systématiques distincts |
| recul–QED | observables et relations principales distinctes ; dépendances communes indirectes dans l’ajustement |
| valeurs dérivées–CODATA | non indépendantes : CODATA utilise les données dont elles sont dérivées |

La matrice n’autorise pas encore un classement binaire `indépendant / non indépendant`. L’indépendance doit être qualifiée selon au moins quatre dimensions :

```text
indépendance de l’appareil ;
indépendance de l’observable ;
indépendance de la théorie de passage ;
indépendance des données auxiliaires.
```

## 5. Discordance et traitement

Avant expansion :

```text
résidu normalisé D3 — rubidium : -2.3 ;
résidu normalisé D4 — césium : 4.7.
```

Après expansion commune de `2.5` sur D1–D6 :

```text
toutes les valeurs se trouvent à moins de deux incertitudes élargies
par rapport à la valeur recommandée.
```

Ce traitement soutient l’énoncé suivant :

> Le dossier CODATA conserve des voies discordantes dans une sortie cohérente au sens de l’ajustement, en élargissant les incertitudes déclarées.

Il ne soutient pas encore :

```text
une cause commune des écarts ;
la supériorité d’une voie ;
la compatibilité physique parfaite des chaînes ;
une variation de alpha ;
une invariance de alpha.
```

## 6. Formes d’attribution autorisées

### A. Mesure

```text
Une expérience mesure une observable première avec un budget d’incertitude déclaré.
```

### B. Détermination

```text
Une chaîne détermine une valeur de alpha par une relation de passage et des entrées auxiliaires.
```

### C. Ajustement

```text
CODATA recommande une valeur issue d’un ajustement global qui conserve les dépendances et traite l’incohérence par expansion des incertitudes.
```

### D. Comparaison

```text
Les valeurs dérivées peuvent être comparées sous une convention commune sans que les chaînes deviennent équivalentes ni indépendantes.
```

## 7. Questions à instruire dans les fiches locales

### Césium

1. quelle grandeur est effectivement estimée par l’interféromètre ;
2. quelles corrections dominent le budget d’incertitude ;
3. quelles corrélations internes sont publiées ;
4. quelle partie de l’écart avec les autres voies peut être reliée à des systématiques identifiées ;
5. quelle portée donner au résidu CODATA `4.7`.

### Rubidium

1. quelles améliorations distinguent la mesure 2020 de la mesure 2011 ;
2. quels effets systématiques nouveaux ont été identifiés ;
3. comment les données brutes et simulations entrent dans le budget ;
4. quelles dépendances aux masses atomiques et à `R_inf` sont significatives ;
5. quelle portée donner au résidu CODATA `-2.3`.

### Anomalie de l’électron

1. quelle fréquence ou quel rapport est effectivement mesuré ;
2. comment la mesure produit `ae(exp)` ;
3. quelle expression QED est inversée ;
4. comment l’incertitude du coefficient d’ordre dix est traitée ;
5. quelles contributions non QED sont conservées ;
6. dans quel sens la voie détermine `alpha` et dans quel sens elle teste la QED.

## 8. Décision préparatoire

```text
mesures premières : séparées ;
relations de passage : séparées ;
données auxiliaires : identifiées au premier ordre ;
corrélations explicites : identifiées ;
dépendances structurelles : partiellement identifiées ;
traitement CODATA de l’incohérence : identifié ;
préférence entre chaînes : non ouverte ;
verdict local α2 : non ouvert ;
prochaine opération : fiches locales césium, rubidium et anomalie électronique.
```
