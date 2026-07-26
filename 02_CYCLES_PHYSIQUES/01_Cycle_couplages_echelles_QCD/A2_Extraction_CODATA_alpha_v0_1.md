# α2 — Extraction du traitement de `alpha` dans l’ajustement CODATA 2022 v0.1

## 0. Statut

```text
statut : extraction scientifique bornée en cours ;
date : 26 juillet 2026 ;
opération : α2, issue #36 ;
source directrice : Mohr, Newell, Taylor et Tiesinga,
                    CODATA recommended values of the fundamental physical constants: 2022,
                    Rev. Mod. Phys. 97, 025002 (2025) ;
DOI : 10.1103/RevModPhys.97.025002 ;
portée : reconstruire les données, relations et décisions d’ajustement qui déterminent
         la valeur recommandée de basse énergie de alpha ;
autorité : descriptive et préparatoire ;
ne vaut pas : reproduction indépendante de l’ajustement, nouvelle moyenne,
               verdict définitif sur les chaînes, variation physique de alpha,
               ou propagation dans la synthèse active du cycle 1.
```

L’étiquette « CODATA 2022 » désigne un ajustement fondé sur les données théoriques et expérimentales disponibles jusqu’au 31 décembre 2022. Le rapport détaillé a été publié le 30 avril 2025.

## 1. Résultat directeur

La valeur recommandée de `alpha` n’est pas une mesure unique. Elle est la sortie d’un ajustement par moindres carrés qui relie des données expérimentales et théoriques à des constantes ajustées par des équations d’observation.

Pour `alpha`, le sous-ensemble direct est constitué de six données D1–D6 :

```text
D1 : anomalie magnétique expérimentale de l’électron ae(exp) ;
D2 : correction additive portant l’incertitude de la théorie de ae ;
D3 : h/m(87Rb) issu du recul atomique ;
D4 : h/m(133Cs) issu du recul atomique ;
D5 : masse atomique relative Ar(87Rb) ;
D6 : masse atomique relative Ar(133Cs).
```

Ces six données ne constituent pas six déterminations indépendantes de `alpha`. Elles forment trois voies principales :

```text
voie QED / anomalie électronique : D1 + D2 ;
voie recul rubidium : D3 + D5, avec constantes ajustées communes ;
voie recul césium : D4 + D6, avec constantes ajustées communes.
```

## 2. Données D1–D6

Source : rapport CODATA 2022, Table XXV, section consacrée aux données pertinentes pour `alpha` et la masse de l’électron.

| Identifiant | Donnée d’entrée | Valeur utilisée | Incertitude standard relative | Origine | Fonction |
|---|---|---:|---:|---|---|
| D1 | `ae(exp)` | `1.159 652 180 59(13) × 10^-3` | `1.1 × 10^-10` | Fan et al., Northwestern, mesure 2022 publiée en 2023 | observable expérimentale première de la voie QED |
| D2 | `delta_e` | `0.000(16) × 10^-12` | `1.4 × 10^-11` relativement à `ae` | théorie QED | correction additive représentant l’incertitude de l’expression théorique |
| D3 | `h/m(87Rb)` | `4.591 359 258 90(65) × 10^-9 m² s^-2 Hz^-1` | `1.4 × 10^-10` | Morel et al., LKB, 2020 | observable de recul de la voie rubidium |
| D4 | `h/m(133Cs)` | `3.002 369 4721(12) × 10^-9 m² s^-2 Hz^-1` | `4.0 × 10^-10` | Parker et al., Berkeley, 2018 | observable de recul de la voie césium |
| D5 | `Ar(87Rb)` | `86.909 180 5291(65)` | `7.5 × 10^-11` | Atomic Mass Data Center 2020 | entrée auxiliaire nécessaire à la voie rubidium |
| D6 | `Ar(133Cs)` | `132.905 451 9585(86)` | `6.5 × 10^-11` | Atomic Mass Data Center 2020 | entrée auxiliaire nécessaire à la voie césium |

## 3. Équations d’observation

Source : rapport CODATA 2022, Table XXXI et sections V–VI.

### 3.1 Voie anomalie magnétique de l’électron

```text
ae(exp) ≐ ae(th) + delta_th(e)
delta_e ≐ delta_th(e)
```

`ae(th)` est principalement une fonction de `alpha`, mais dépend aussi de coefficients QED, de rapports de masses leptoniques et de contributions hadroniques et électrofaibles. L’ajustement ne traite donc pas D1 comme une mesure directe de `alpha`.

La voie comporte au minimum :

```text
observable mesurée : ae(exp) ;
relation de passage : expression théorique ae(th; alpha, ...) ;
incertitude théorique explicite : delta_th(e), portée par D2 ;
sortie conditionnelle : valeur de alpha obtenue par inversion de la relation.
```

### 3.2 Voies de recul atomique

Pour `X = 87Rb` ou `133Cs`, l’équation d’observation est :

```text
h / m(X) ≐ [Ar(e) / Ar(X)] [c alpha² / (2 R_inf)].
```

Elle peut être réécrite sous la forme :

```text
alpha = sqrt{ [2 h c R_inf / (m(X)c²)] [Ar(X) / Ar(e)] }.
```

Depuis la révision du SI, `h` et `c` sont exacts. La détermination de `alpha` par recul dépend néanmoins de plusieurs éléments qui ne sont pas l’observable de recul elle-même :

```text
h/m(X) ou m(X) ;
Ar(X) ;
Ar(e) ;
R_inf ;
relations de passage et covariances de l’ajustement.
```

La mesure première est une grandeur de recul ou une masse atomique en unités SI ; `alpha` est une sortie inférée par l’équation d’observation.

## 4. Corrélations explicitement déclarées

La Table XXVI ne signale, parmi D1–D6, qu’une corrélation d’entrée supérieure à `0.0001` :

```text
r(D5, D6) = 0.1032.
```

Elle indique également des corrélations de D5 et D6 avec d’autres masses atomiques de l’ajustement :

```text
r(D5, D11) = 0.0678 ;
r(D6, D11) = 0.0630.
```

L’absence de corrélation d’entrée déclarée entre D1, D3 et D4 ne suffit pas à faire de leurs valeurs dérivées de `alpha` des voies totalement indépendantes. Elles partagent des constantes ajustées, des relations théoriques et, pour les deux voies de recul, une architecture métrologique commune.

La distinction à conserver est donc :

```text
corrélation fournie entre données d’entrée
≠
dépendance commune par une équation ou une constante ajustée
≠
indépendance physique complète des chaînes.
```

## 5. Incohérence et facteur d’expansion

### 5.1 Ajustement initial

Avant application des facteurs d’expansion, l’ajustement global des 133 données et 79 constantes ajustées donne :

```text
chi² = 109.6 ;
degrés de liberté = 54 ;
probabilité = 0.001 % ;
rapport de Birge = 1.42.
```

Parmi les huit données dont le résidu normalisé dépasse 2 figurent :

```text
D3 — h/m(87Rb) : résidu normalisé -2.3 ;
D4 — h/m(133Cs) : résidu normalisé 4.7.
```

Le césium est donc le contributeur le plus fortement discordant du sous-dossier `alpha` avant expansion.

### 5.2 Décision CODATA

CODATA applique un facteur d’expansion de `2.5` aux incertitudes des six données D1–D6 :

```text
mesure ae(exp) ;
incertitude de théorie QED ;
recul rubidium ;
recul césium ;
masse relative du rubidium ;
masse relative du césium.
```

Cette décision :

- maintient les trois voies dans l’ajustement ;
- réduit leurs résidus normalisés à 2 ou moins ;
- ne choisit pas une chaîne comme vraie et les autres comme fausses ;
- ne transforme pas l’incohérence en variation physique de `alpha` ;
- élargit l’incertitude attribuée à la valeur recommandée.

Lorsque le même facteur est appliqué aux deux membres d’une paire corrélée, CODATA applique son carré à la covariance, afin de conserver le coefficient de corrélation.

### 5.3 Ajustement final

Après les facteurs d’expansion appliqués aux différents sous-ensembles problématiques du corpus CODATA :

```text
chi² = 44.2 ;
degrés de liberté = 54 ;
probabilité = 0.83 ;
rapport de Birge = 0.90.
```

Le facteur `2.5` constitue donc une décision de traitement de l’incohérence des données dans l’ajustement. Il n’est ni une correction expérimentale propre à une chaîne ni une preuve que les désaccords ont une cause physique commune.

## 6. Trois valeurs dérivées publiées et valeur recommandée

Le rapport CODATA rappelle les valeurs de `alpha^-1` dérivées par les auteurs des trois résultats clés :

| Voie | Valeur dérivée publiée de `alpha^-1` |
|---|---:|
| recul césium, Berkeley-18 | `137.035 999 046(27)` |
| recul rubidium, LKB-20 | `137.035 999 206(11)` |
| anomalie de l’électron, Northwestern-23 | `137.035 999 166(15)` |

Après application du facteur `2.5`, leur moyenne pondérée indicative est :

```text
137.035 999 178(21).
```

La valeur recommandée issue de l’ajustement complet est :

```text
alpha^-1 = 137.035 999 177(21) ;
incertitude standard relative = 1.6 × 10^-10.
```

La quasi-identité entre la moyenne pondérée indicative des trois valeurs dérivées et la valeur recommandée ne rend pas CODATA réductible à cette moyenne. L’ajustement complet emploie les données D1–D6, leurs équations d’observation, les masses relatives, les constantes ajustées communes et leurs covariances.

## 7. Lecture des trois chaînes

### 7.1 Voie rubidium

```text
observable première : h/m(87Rb) ;
entrée auxiliaire directe : Ar(87Rb) ;
relations communes : Ar(e), R_inf, h exact, c exact ;
valeur dérivée : alpha^-1 = 137.035 999 206(11) ;
rang : détermination par recul et propagation métrologique.
```

Le rapport CODATA note que l’expérience LKB 2020 a identifié et réduit plusieurs effets systématiques absents ou moins bien contrôlés dans son expérience de 2011.

### 7.2 Voie césium

```text
observable première : h/m(133Cs) ;
entrée auxiliaire directe : Ar(133Cs) ;
relations communes : Ar(e), R_inf, h exact, c exact ;
valeur dérivée : alpha^-1 = 137.035 999 046(27) ;
rang : détermination par recul et propagation métrologique ;
point critique : résidu normalisé 4.7 avant expansion.
```

CODATA constate que cette voie est moins en accord avec les voies rubidium et anomalie de l’électron que ces deux dernières ne le sont entre elles. Le rapport n’attribue cependant pas une cause démontrée à cette discordance.

### 7.3 Voie anomalie de l’électron

```text
observable première : ae(exp) ;
relation conditionnelle : ae(th; alpha, coefficients QED, rapports de masses, ...) ;
incertitude théorique explicite : D2 ;
valeur dérivée : alpha^-1 = 137.035 999 166(15) ;
rang : inférence conditionnelle par la théorie QED.
```

Cette voie est scientifiquement distincte des deux voies de recul. Elle fournit aussi, lorsqu’une valeur de `alpha` obtenue par recul lui est injectée, un test de la prédiction QED de `ae`. Elle ne peut donc pas être comptée simultanément comme une mesure indépendante de `alpha` et comme un test indépendant de la même relation sans déclarer le sens de l’inférence.

## 8. Verdict préparatoire d’extraction

```text
ce qui est mesuré directement :
  ae(exp), h/m(87Rb), h/m(133Cs), Ar(87Rb), Ar(133Cs) ;

ce qui est théorique :
  expression ae(th), coefficients QED, correction delta_th(e),
  équations de passage et constantes ajustées communes ;

ce qui est inféré :
  les trois valeurs publiées de alpha^-1 ;

ce qui est ajusté :
  la valeur recommandée CODATA et les constantes reliées ;

ce qui est commun aux voies de recul :
  forme de l’équation d’observation, Ar(e), R_inf, h et c,
  architecture de propagation métrologique ;

ce qui demeure discordant :
  principalement la position de la voie césium relativement
  aux voies rubidium et anomalie électronique ;

ce qui demeure suspendu :
  la cause physique ou instrumentale de la discordance,
  l’indépendance effective complète des chaînes,
  et un verdict de cohérence scientifique définitif.
```

## 9. Dettes avant le verdict local α2

1. reconstruire depuis Parker et al. la chaîne expérimentale et le budget d’incertitude du césium ;
2. reconstruire depuis Morel et al. la chaîne expérimentale et le budget d’incertitude du rubidium ;
3. reconstruire depuis Fan et al. l’observable mesurée, puis séparer le calcul QED utilisé pour l’inversion ;
4. identifier dans CODATA la dépendance de `Ar(e)` et de `R_inf` aux autres sous-ensembles de données ;
5. distinguer corrélations numériques fournies et dépendances structurelles communes ;
6. tester si une matrice d’indépendance graduée est justifiée ;
7. ne produire aucun verdict de préférence entre chaînes avant ces reconstructions.

## 10. Références primaires

- Mohr, P. J., Newell, D. B., Taylor, B. N. et Tiesinga, E., « CODATA recommended values of the fundamental physical constants: 2022 », *Reviews of Modern Physics* 97, 025002 (2025), DOI `10.1103/RevModPhys.97.025002`.
- Parker, R. H., Yu, C., Zhong, W., Estey, B. et Müller, H., « Measurement of the fine-structure constant as a test of the Standard Model », *Science* 360, 191–195 (2018), DOI `10.1126/science.aap7706`.
- Morel, L., Yao, Z., Cladé, P. et Guellati-Khélifa, S., « Determination of the fine-structure constant with an accuracy of 81 parts per trillion », *Nature* 588, 61–65 (2020), DOI `10.1038/s41586-020-2964-7`.
- Fan, X., Myers, T. G., Sukra, B. A. D. et Gabrielse, G., « Measurement of the Electron Magnetic Moment », *Physical Review Letters* 130, 071801 (2023), DOI `10.1103/PhysRevLett.130.071801`.
