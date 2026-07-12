# Vérification — cycle métrologique SI

## Statut

Ce document contrôle :

- [architecture-relationnelle-metrologique-si.md](architecture-relationnelle-metrologique-si.md)

La source normative principale est le Bureau international des poids et mesures.

## 1. Sources de contrôle

1. BIPM, *SI defining constants* :
   <https://www.bipm.org/en/measurement-units/si-defining-constants>
2. BIPM, *The International System of Units (SI Brochure)* :
   <https://www.bipm.org/en/publications/si-brochure>
3. BIPM, *Practical realizations* :
   <https://www.bipm.org/en/measurement-units/practical-realizations>
4. CGPM, Résolution 1 de la 26e CGPM, 2018 :
   <https://www.bipm.org/en/committees/cg/cgpm/26-2018/resolution-1>

## 2. Définition générale du SI

Le BIPM définit le SI à partir de sept constantes définissantes dont les valeurs numériques, exprimées dans les unités correspondantes, sont fixées exactement.

| Constante | Valeur numérique exacte | Unité |
|---|---:|---|
| `Delta nu_Cs` | `9 192 631 770` | `Hz` |
| `c` | `299 792 458` | `m s^-1` |
| `h` | `6.626 070 15 × 10^-34` | `J s` |
| `e` | `1.602 176 634 × 10^-19` | `C` |
| `k_B` | `1.380 649 × 10^-23` | `J K^-1` |
| `N_A` | `6.022 140 76 × 10^23` | `mol^-1` |
| `K_cd` | `683` | `lm W^-1` |

Le système complet des unités peut être dérivé de ces valeurs fixées.

### Décision

L’exactitude porte sur les valeurs numériques dans le SI. Elle n’est pas une propriété empirique nouvelle acquise par les grandeurs au moment de la redéfinition.

## 3. Valeur d’une grandeur et valeur numérique

Une grandeur physique ne se réduit pas à son nombre.

Schématiquement :

```text
valeur d’une grandeur = valeur numérique × unité.
```

Un changement cohérent d’unités modifie la valeur numérique d’une grandeur dimensionnée sans modifier le phénomène physique.

### Conséquence

L’énoncé :

```text
h possède exactement la valeur 6.626... × 10^-34
```

est incomplet sans :

```text
dans le SI, exprimée en J s.
```

La fixité numérique est relative au système d’unités défini.

## 4. Définition, réalisation et mesure

Trois niveaux doivent être séparés.

### 4.1 Définition

La définition fixe exactement la valeur numérique de la constante.

### 4.2 Mise en pratique

Une mise en pratique décrit une procédure permettant de réaliser une unité conformément à sa définition.

### 4.3 Résultat de mesure

Un résultat de mesure comporte une valeur et une incertitude évaluée.

### Décision

```text
exactitude définitionnelle
≠
réalisation parfaite
≠
mesure sans incertitude.
```

## 5. Hétérogénéité des sept constantes

### `Delta nu_Cs`

La seconde est définie à partir de la fréquence de la transition hyperfine de l’état fondamental non perturbé de l’atome de césium 133.

Cette référence dépend d’un système atomique particulier choisi pour sa reproductibilité. Elle n’est pas un paramètre universel des équations fondamentales.

### `c`

`c` a un rôle physique dans la structure relativiste. La valeur fixée relie le mètre à la seconde.

La valeur exacte de `c` dans le SI ne signifie pas que toute vitesse de propagation mesurée dans un milieu est exacte ou égale à `c`.

### `h`

`h` intervient comme constante de proportionnalité et échelle d’action dans le formalisme quantique.

La formulation :

```text
h est un opérateur de relation quantique
```

est rejetée. `h` est une constante, non un opérateur agissant sur un espace d’états.

### `e`

`e` fixe l’unité de charge dans la définition de l’ampère.

Le vocabulaire de « quantum de charge » doit être qualifié : les charges des quarks sont fractionnaires en unités de `e`. Le contenu physique du couplage électromagnétique est mieux caractérisé par la constante sans dimension `alpha`.

### `k_B`

`k_B` relie température thermodynamique et énergie. Sa valeur fixée définit le kelvin.

La convention métrologique ne produit ni l’agitation thermique ni les lois de la mécanique statistique.

### `N_A`

`N_A` fixe exactement le nombre d’entités spécifiées dans une mole.

Son statut est fortement lié à la définition de la quantité de matière et au comptage. Il ne joue pas le même rôle théorique que `c`, `h` ou `k_B`.

### `K_cd`

`K_cd` fixe l’efficacité lumineuse d’un rayonnement monochromatique de fréquence `540 × 10^12 Hz`.

Cette constante relie radiométrie et photométrie. Son choix inclut une convention propre à la mesure photométrique et ne constitue pas une constante fondamentale de la dynamique électromagnétique.

### Décision

Les sept constantes ne forment pas une espèce naturelle physique. Leur unité est fonctionnelle et institutionnelle : elles engendrent le SI.

## 6. Constantes exactes par composition

Puisque `h`, `e`, `k_B` et `N_A` sont exactes dans le SI :

```math
K_J=\frac{2e}{h},
\qquad
R_K=\frac{h}{e^2},
\qquad
R=N_Ak_B
```

ont des valeurs numériques exactes dans les unités SI correspondantes.

### Limite

Il faut distinguer :

- exactitude de la combinaison de constantes ;
- validité d’une relation théorique reliant cette combinaison à un effet physique ;
- incertitude de la réalisation expérimentale.

L’exactitude de `R_K` comme combinaison ne signifie pas qu’un dispositif Hall réel est exempt de corrections, de défauts ou d’incertitude de mesure.

## 7. Report des incertitudes après 2019

Avant la révision, certaines constantes électriques comme `mu_0` avaient une valeur numérique exacte par définition.

Dans le SI révisé, `e`, `h` et `c` sont exacts tandis que `alpha` reste déterminée expérimentalement.

Avec :

```math
\alpha=\frac{e^2}{2\epsilon_0hc},
```

on obtient :

```math
\epsilon_0=\frac{e^2}{2\alpha hc},
\qquad
\mu_0=\frac{2\alpha h}{e^2c}.
```

L’incertitude de `alpha` se reporte donc sur `epsilon_0` et `mu_0`.

### Décision

Une redéfinition ne supprime pas l’incertitude du monde mesuré ; elle redistribue quels nombres sont exacts et quels nombres sont déterminés expérimentalement.

## 8. Contrefactuels contrôlés

### 8.1 Changement de système d’unités

Si l’on adopte des unités naturelles avec :

```text
c = hbar = 1,
```

les valeurs numériques et dimensions conventionnelles changent, mais les prédictions physiques sans dimension restent.

### 8.2 Révision future de la seconde

Une autre transition atomique pourrait être choisie pour une future définition de la seconde. Le système métrologique changerait ; la dynamique du temps physique ne serait pas modifiée par la décision.

### 8.3 Mauvaise réalisation

Une réalisation biaisée du kilogramme ne change pas la valeur exacte de `h`. Elle produit une réalisation incorrecte ou une incertitude plus grande.

### 8.4 Variation mesurée de `alpha`

Une éventuelle variation physique de `alpha` ne pourrait pas être éliminée en invoquant l’exactitude SI de `e`, `h` ou `c`. Elle se manifesterait dans les relations entre grandeurs et constantes dérivées.

## 9. Registre des décisions

| Proposition | Verdict |
|---|---|
| les sept valeurs numériques définissantes sont exactes dans le SI | confirmé |
| les sept grandeurs ont la même nature physique | refusé |
| une valeur définissante exacte est une mesure infiniment précise | refusé |
| une réalisation d’unité est sans incertitude | refusé |
| `h` est un opérateur | refusé |
| `e` est identique au couplage `alpha` | refusé |
| `K_cd` est une constante fondamentale de la nature | refusé |
| `K_J`, `R_K` et `R` sont exacts par composition dans le SI | confirmé |
| l’exactitude d’une composition valide automatiquement toute réalisation physique | refusé |
| la révision redistribue certaines incertitudes | confirmé |

## 10. Statut de l’architecture définitionnelle

Le SI forme bien une architecture au sens minimal suivant :

```text
ensemble coordonné de valeurs numériques exactes
+ relations dimensionnelles
+ règles de dérivation
+ mises en pratique
+ réseau international de comparabilité.
```

Cette architecture est réelle et opératoire.

Elle n’est pas une architecture physique au même sens que le secteur Higgs–Yukawa, ni une architecture de validité au sens des EFT.

### Décision

```text
architecture métrologique définitionnelle : confirmée ;
unification ontologique des constantes : refusée.
```

## 11. Résultat pour la fonction de fixité

Le SI montre une fonction de fixité distincte :

> assurer la stabilité intersubjective et internationale des valeurs numériques, des unités et des comparaisons de mesure.

Cette fonction porte sur une architecture normative appuyée sur des grandeurs physiques.

Elle ne rend pas les grandeurs physiquement invariantes par convention.

## 12. Conclusion de vérification

Le corpus interne avait correctement distingué exactitude SI, rôle physique et réalisation pratique.

La refonte ajoute quatre corrections :

1. les sept constantes doivent être considérées ensemble pour comprendre la fonction du système ;
2. elles ne constituent pas une espèce physique homogène ;
3. `h` n’est pas un opérateur et `e` exige une qualification comme unité de charge ;
4. l’exactitude définitionnelle redistribue les incertitudes plutôt qu’elle ne les abolit.

> Le SI fixe des nombres pour stabiliser la mesure. Il ne fixe pas conventionnellement les lois de la nature ni les valeurs des rapports sans dimension qui expriment leurs relations.
