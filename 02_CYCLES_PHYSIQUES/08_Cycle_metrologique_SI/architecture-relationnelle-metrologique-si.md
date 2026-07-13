# Dossier de transfert — architecture relationnelle métrologique SI

## Statut

Ce document reprend le cycle métrologique SI comme cas contrasté après les cycles Higgs–Yukawa et basse énergie.

Il part des matériaux internes :

- [Cycle_metrologique_SI_v0_1_c_h_e.md](Cycle_metrologique_SI_v0_1_c_h_e.md)
- [Synthese_recuperation_thermo_metrologique_SI_v0_1.md](../04_Cycle_thermo_metrologique/Synthese_recuperation_thermo_metrologique_SI_v0_1.md)

L’ancienne conclusion d’une « architecture inter-familles confirmée » est suspendue. Le dossier teste une hypothèse plus sobre :

> Le SI constitue une architecture définitionnelle qui attribue une fixité numérique exacte à des grandeurs physiquement hétérogènes afin d’engendrer un système cohérent d’unités.

## 1. Question du dossier

> Qu’est-ce qui devient exactement fixe lorsque le SI fixe la valeur numérique de constantes définissantes ?

Question complémentaire :

> Cette fixité métrologique porte-t-elle sur les grandeurs physiques elles-mêmes, sur leur valeur numérique dans un système d’unités, ou sur les règles de réalisation et de comparaison des mesures ?

## 2. Corpus interne repris

Les matériaux existants ont déjà établi plusieurs distinctions solides :

- exactitude définitionnelle et précision empirique ne sont pas identiques ;
- une constante définissante conserve un rôle physique qui n’est pas épuisé par son statut SI ;
- `R = N_A k_B`, `K_J = 2e/h` et `R_K = h/e²` sont exacts par composition dans le SI ;
- `e` ne doit pas être confondu avec le couplage électromagnétique sans dimension `alpha` ;
- les réalisations pratiques conservent des incertitudes.

Ces acquis sont conservés. Les anciens classements en familles sont suspendus.

## 3. Les sept constantes définissantes

Le SI est défini par les valeurs numériques exactes de :

| Constante définissante | Type de grandeur ou référence |
|---|---|
| `Delta nu_Cs` | fréquence de transition hyperfine du césium 133 |
| `c` | vitesse de la lumière dans le vide |
| `h` | constante de Planck |
| `e` | charge élémentaire |
| `k_B` | constante de Boltzmann |
| `N_A` | constante d’Avogadro |
| `K_cd` | efficacité lumineuse d’un rayonnement monochromatique spécifié |

Leur point commun est métrologique :

```text
valeur numérique exacte
+ unité SI associée
-> définition du système d’unités.
```

Leur point commun n’est pas une nature physique unique.

## 4. Chaîne A — histoire empirique et décision définitionnelle

```text
grandeur ou référence physique
        |
        v
déterminations expérimentales historiques
        |
        v
comparaisons et ajustements cohérents
        |
        v
décision institutionnelle de fixer une valeur numérique
        |
        v
redéfinition des unités du SI
```

La fixation n’est pas arbitraire au sens d’une valeur choisie sans rapport avec l’expérience. Elle absorbe une connaissance empirique antérieure dans une définition conventionnelle.

Après la fixation, la valeur numérique n’est plus ré-estimée comme une quantité incertaine du SI.

## 5. Chaîne B — définition des unités

```text
sept valeurs numériques exactes
        |
        v
équations de définition
        |
        v
unités de base et unités dérivées
        |
        v
valeurs numériques des grandeurs mesurées
```

Le produit :

```text
valeur numérique fixée × unité
```

doit égaler la valeur de la constante définissante.

La fixité porte donc sur une relation entre :

- une grandeur ou référence définissante ;
- une valeur numérique ;
- une unité ;
- un système cohérent de dimensions et de dérivations.

## 6. Chaîne C — réalisation pratique

```text
définition idéale du SI
        |
        v
méthode de mise en pratique
        |
        v
instrumentation et étalonnage
        |
        v
comparaison entre laboratoires
        |
        v
résultat avec incertitude
```

Une valeur définissante exacte ne produit pas une réalisation sans incertitude.

Il faut distinguer :

```text
exactitude de la définition
≠
incertitude de réalisation
≠
incertitude de la grandeur mesurée.
```

## 7. Chaîne D — rôle physique conservé

La définition SI n’épuise pas le contenu physique des constantes.

### `c`

`c` intervient dans la structure relativiste et causale. Sa valeur numérique exacte en `m s^-1` relie le mètre à la seconde dans le SI, mais son rôle physique ne se réduit pas à cette conversion.

### `h`

`h` fixe une échelle d’action et intervient dans des relations quantiques telles que :

```math
E=h\nu.
```

Il ne doit pas être qualifié d’« opérateur ». C’est une constante de proportionnalité et une échelle physique dans le formalisme quantique.

### `e`

`e` est la valeur absolue de la charge de l’électron et un paramètre du secteur électromagnétique. L’expression « quantum de charge » exige une qualification : les quarks portent des charges fractionnaires en unités de `e`, même s’ils ne sont pas observés isolément.

La force du couplage électromagnétique se lit plus proprement par la constante sans dimension `alpha`.

### `k_B`

`k_B` relie l’échelle de température thermodynamique à l’énergie et intervient dans les relations statistiques et entropiques. Sa fixation définit le kelvin, mais n’explique pas la thermodynamique statistique.

### `N_A`

`N_A` fixe le nombre d’entités par mole. Son rôle est principalement de relier le comptage microscopique à la quantité de matière définie par le SI.

### `Delta nu_Cs`

La fréquence du césium fournit la référence définissant la seconde. Elle est liée à une transition particulière d’un système atomique, non à une constante fondamentale universelle de la dynamique.

### `K_cd`

`K_cd` relie une grandeur radiométrique à une grandeur photométrique pour un rayonnement spécifié. Son statut montre particulièrement que « constante définissante du SI » ne signifie pas « constante fondamentale de la nature ».

## 8. Exactitude par composition

Lorsque des valeurs définissantes sont exactes, certaines combinaisons le deviennent numériquement dans le SI :

```math
K_J=\frac{2e}{h},
\qquad
R_K=\frac{h}{e^2},
\qquad
R=N_Ak_B.
```

Il faut distinguer trois propositions :

1. la combinaison algébrique des constantes définissantes est exacte dans le SI ;
2. une relation théorique associe cette combinaison à un phénomène physique ;
3. une réalisation expérimentale du phénomène possède une incertitude et doit être contrôlée.

L’exactitude de la composition ne démontre pas automatiquement l’exactitude universelle de toute loi phénoménologique utilisée pour la réaliser.

## 9. Contraste avec le cycle basse énergie

| Cycle EFT | Cycle SI |
|---|---|
| coefficient défini dans un régime de validité | valeur numérique fixée dans un système d’unités |
| dépendance possible à l’échelle, au schéma et à la base | exactitude numérique par définition |
| erreur de troncature | incertitude de réalisation |
| invariance recherchée dans l’observable | cohérence recherchée dans le système de mesure |
| rupture lorsque la hiérarchie disparaît | révision institutionnelle possible du système de définition |

Les deux cycles parlent de fixité, mais à des niveaux différents.

## 10. Objets et fonctions provisoires

| Objet | Fonction métrologique | Rôle physique ou institutionnel distinct |
|---|---|---|
| `Delta nu_Cs` | définit la seconde | fréquence d’une transition atomique choisie |
| `c` | relie mètre et seconde | invariant relativiste / structure causale |
| `h` | participe à la définition du kilogramme | échelle d’action quantique |
| `e` | participe à la définition de l’ampère | charge élémentaire et paramètre électromagnétique |
| `k_B` | définit le kelvin | conversion température-énergie |
| `N_A` | définit la mole | convention de comptage d’entités |
| `K_cd` | définit la candela | convention photométrique physiologiquement et historiquement située |

Ce tableau interdit d’assimiler « définissante » à « fondamentale ».

## 11. Contrefactuels initiaux

### 11.1 Si une valeur définissante était modifiée tout en conservant les mêmes phénomènes

Les valeurs numériques de certaines unités et grandeurs changeraient, mais les rapports sans dimension et les prédictions physiques invariantes resteraient inchangés.

### 11.2 Si la réalisation pratique était imparfaite

La définition resterait exacte ; seul le résultat de la réalisation porterait une incertitude accrue.

### 11.3 Si `alpha` était réévaluée

La valeur définissante de `e` ne changerait pas. Dans le SI révisé, l’incertitude se reporterait sur d’autres constantes dérivées, notamment `epsilon_0` et `mu_0`.

### 11.4 Si une transition atomique plus performante remplaçait un jour le césium

La définition de la seconde pourrait être révisée sans que le temps physique ou les lois dynamiques aient changé.

### 11.5 Si `K_cd` n’était pas retenue

La photométrie SI serait organisée différemment, sans modification de la propagation électromagnétique elle-même.

## 12. Première décision sur la fonction de fixité

Le SI confirme une fonction de fixité réelle, mais elle est :

```text
définitionnelle
+ institutionnelle
+ opératoire
```

plutôt que dynamique.

Elle maintient la comparabilité des mesures en fixant des valeurs numériques et des règles de dérivation.

Elle ne doit pas être projetée rétroactivement sur la nature physique des grandeurs comme si celles-ci étaient devenues constantes par décision.

## 13. Conditions d’échec du dossier

Le dossier échoue si :

- les sept constantes sont traitées comme une espèce physique homogène ;
- exactitude numérique et invariance physique sont confondues ;
- les incertitudes de réalisation sont supprimées par définition ;
- `h` est décrit comme un opérateur ;
- `e` est présenté sans nuance comme l’unique quantum universel de toute charge ;
- `K_cd` est assimilée à une constante fondamentale de la nature ;
- les compositions exactes sont prises pour des validations empiriques automatiques des phénomènes utilisés en métrologie.

## 14. Travail de vérification

La phase suivante devra :

1. contrôler les sept définitions et leurs valeurs exactes auprès du BIPM ;
2. distinguer définition, mise en pratique et mesure ;
3. préciser le statut de `c`, `h`, `e`, `k_B`, `N_A`, `Delta nu_Cs` et `K_cd` ;
4. vérifier le transfert des incertitudes vers les constantes dérivées ;
5. contrôler le statut de `K_J`, `R_K` et `R` ;
6. évaluer si « architecture définitionnelle » produit un gain explicatif réel.

## 15. Décision provisoire

```text
Cycle SI : matière interne solide sur les distinctions essentielles ;
élargissement nécessaire aux sept constantes définissantes ;
architecture définitionnelle à vérifier.
```

> Le SI ne transforme pas sept constantes physiques semblables en étalons. Il sélectionne des références hétérogènes et fixe leurs valeurs numériques afin de construire une grammaire commune de la mesure.
