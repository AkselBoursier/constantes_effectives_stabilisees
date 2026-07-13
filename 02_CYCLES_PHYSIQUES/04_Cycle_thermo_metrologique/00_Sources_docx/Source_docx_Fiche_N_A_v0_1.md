# Source DOCX - Fiche_N_A_v0_1

## Statut

```text
lot: 1D - thermo-metrologie SI ciblee avant cercle 2
source physique: Fiche N_A v0.1.docx
source physique path: 02_CYCLES_PHYSIQUES/04_Cycle_thermo_metrologique/00_Sources_docx/Fiche N_A v0.1.docx
sha256_source: 43ad6f114f50df9aa6ed6f8cd04c072cbd0acef8fa227f55b1534d5058832a6c
statut: extraction textuelle de travail
document actif concerne: Cycle metrologique SI ; architecture metrologique SI
controle attendu: Extraction + comparaison
sha256_extraction: b6d7de492dbc1d1f07a9258c6547e5e650d77e122e03d0b35cbdb3e21b7451f5
```

## Limite

```text
Cette extraction ne remplace pas le DOCX source.
Elle rend la matiere lisible en Markdown pour comparaison et integration.
La mise en page Word n'est pas reconstruite.
```

## Extraction

### Fiche (N_A) v0.1

#### Constante d’Avogadro, mole et passage entre comptage microscopique et quantité de matière

#### 1. Identification

La constante d’Avogadro, notée (N_A), relie le nombre d’entités élémentaires à la quantité de matière. Sa valeur exacte dans le SI est :

[ N_A = 6{,}022,140,76 ^{23}  ]

Depuis la révision du SI entrée en vigueur en 2019, cette valeur est fixée par définition. Le BIPM liste (N_A) parmi les sept constantes définissantes du SI et précise que les valeurs numériques de ces constantes définissantes n’ont pas d’incertitude.

Le rôle immédiat de (N_A) est de définir la mole. Une mole contient exactement :

[ 6{,}022,140,76 ^{23} ]

entités élémentaires spécifiées. Ces entités peuvent être des atomes, molécules, ions, électrons, autres particules ou groupes spécifiés de particules.

Le point central de cette fiche est donc double :

[ N_A ]

est physiquement une constante de comptage et de passage entre micro-entités et quantité macroscopique de matière,

mais métrologiquement, dans le SI actuel,

[ N_A ]

est une constante définissante de la mole.

#### 2. Type logique

(N_A) est une grandeur dimensionnée. Son unité SI est :

[  ]

Elle n’est pas un nombre pur dans son statut de constante physique : elle convertit une quantité de matière exprimée en moles en un nombre d’entités.

Si (n) désigne la quantité de matière et (N) le nombre d’entités, on a :

[ N = nN_A ]

ou inversement :

[ n =  ]

Le type logique de (N_A) est donc :

[  ]

et, depuis le SI révisé :

[  ]

Ces deux statuts sont distincts. Le premier concerne la fonction physique et chimique de (N_A). Le second concerne son rôle métrologique dans la définition de la mole.

#### 3. Régime de définition physique

Le régime de définition physique de (N_A) est le passage entre le niveau microscopique des entités discrètes et le niveau macroscopique de la quantité de matière.

Au niveau microscopique, on compte des entités :

[ ,,, ]

Au niveau macroscopique, on manipule une quantité de matière :

[ n ]

exprimée en moles.

La constante d’Avogadro relie ces deux niveaux :

[ N = nN_A ]

Elle permet donc de traiter des ensembles énormes d’entités discrètes comme des quantités macroscopiques utilisables en chimie, thermodynamique, physique statistique et métrologie.

Son régime physique peut être formulé comme :

[  ]

ou :

[  ]

#### 4. Régime d’accès épistémique

Le régime d’accès épistémique de (N_A) a changé avec la réforme du SI.

Avant 2019, la mole était liée à la masse de (12 ) de carbone-12. La constante d’Avogadro devait être déterminée expérimentalement à partir de relations entre masse molaire, masse atomique et unités de masse.

Depuis le 20 mai 2019, le SI définit la mole en fixant exactement la valeur numérique de (N_A). La réforme du SI a redéfini quatre unités de base — kilogramme, ampère, kelvin et mole — en fixant respectivement les valeurs numériques de (h), (e), (k_B) et (N_A).

Le régime d’accès actuel est donc :

[  ]

et non :

[  N_A ]

Cette transformation est méthodologiquement importante : (N_A) n’est plus mesuré pour définir la mole ; il définit la mole.

#### 5. Fonction physique

La fonction physique principale de (N_A) est de relier le comptage discret et la quantité de matière.

Dans la loi des gaz parfaits, on peut écrire :

[ PV = Nk_BT ]

où (N) est le nombre de particules, ou :

[ PV = nRT ]

où (n) est la quantité de matière. Le passage entre les deux formes repose sur :

[ N = nN_A ]

et :

[ R = N_A k_B ]

(N_A) permet donc de passer d’une description particulaire à une description molaire.

En chimie, il permet de relier la formule microscopique d’une substance à des quantités manipulables en laboratoire. En physique statistique, il sert à relier les nombres de particules aux grandeurs extensives macroscopiques.

La fonction générale de (N_A) est donc :

[  ]

ou :

[  ]

#### 6. Stabilisation empirique

Avant 2019, (N_A) était une constante mesurée. Sa détermination faisait partie des efforts de métrologie fondamentale liés notamment à la définition du kilogramme, à la masse atomique et aux expériences de comptage d’atomes.

La fixation de (N_A) en 2019 n’annule pas cette histoire empirique. Elle la convertit en base conventionnelle pour le système d’unités. Pour fixer une constante définissante, il fallait que les mesures préalables soient suffisamment concordantes et précises afin d’assurer la continuité des unités.

On peut donc distinguer :

[  N_A  ]

[  N_A  ]

Cette distinction est exactement celle que la matrice v0.2 cherche à rendre visible.

#### 7. Stabilisation conventionnelle

La stabilisation conventionnelle de (N_A) est maximale dans le SI actuel.

La valeur :

[ N_A = 6{,}022,140,76 ^{23}  ]

est exacte par définition. Le BIPM indique que les sept constantes définissantes du SI ont des valeurs numériques fixées et sans incertitude.

La formulation correcte est donc :

[ N_A  ]

et non :

[ N_A  ]

Ce point confirme que la stabilisation conventionnelle doit rester séparée de la stabilisation empirique.

#### 8. Ce que (N_A) ne dit pas

(N_A) ne donne pas une constante sans dimension fondamentale du même type qu’un rapport pur. Sa valeur numérique dépend de la définition de la mole.

(N_A) ne dit pas non plus qu’un système macroscopique est simplement une collection sans structure. Il permet de compter ou de convertir, mais il ne décrit pas à lui seul les interactions, les phases, les corrélations, l’entropie ou les propriétés émergentes d’un système matériel.

Enfin, le fait que (N_A) soit exact dans le SI ne signifie pas que toutes les mesures de quantité de matière sont exactes. Les réalisations pratiques, les pesées, les puretés d’échantillons et les mesures chimiques gardent leurs incertitudes.

L’exactitude porte sur la définition de la constante dans le système d’unités, pas sur toutes les opérations expérimentales utilisant la mole.

#### 9. Lecture par la matrice v0.2

| Critère | Lecture pour (N_A) |
|---|---|
| Grandeur | Constante d’Avogadro |
| Type logique | Constante dimensionnée de comptage |
| Dimension | () |
| Régime de définition physique | Passage entre entités microscopiques et quantité macroscopique de matière |
| Régime d’accès épistémique | Définition SI par valeur numérique fixée |
| Fonction | Relier nombre d’entités et quantité de matière |
| Dépendance d’échelle | Non pertinente au sens renormalisation ; dépendance au système d’unités |
| Stabilisation empirique | Historiquement mesurée ; consolidée avant 2019 |
| Stabilisation conventionnelle | Fixée exactement dans le SI |
| Limites | Exactitude conventionnelle ≠ absence d’incertitude dans les mesures de quantité de matière |
| Famille fonctionnelle | Convention + passage discret/macroscopique |
| Sous-type | Constante définissante d’un système d’unités ; constante de comptage molaire |

#### 10. Catégorie proposée

(N_A) appartient à deux axes distincts.

Sur l’axe physique :

constante de passage discret/macroscopique.

Définition provisoire :

Une constante de passage discret/macroscopique est une grandeur qui relie un nombre d’entités élémentaires à une grandeur macroscopique manipulable dans un régime thermodynamique, chimique ou statistique.

Sur l’axe d’accès épistémique :

constante définissante d’un système d’unités.

Définition provisoire :

Une constante définissante d’un système d’unités est une grandeur à laquelle un système métrologique attribue une valeur numérique exacte afin de définir une ou plusieurs unités.

Ces deux classements ne sont pas concurrents. Ils répondent à deux questions différentes :

[  N_A  ]

et :

[  ]

#### 11. Formulation provisoire

La constante d’Avogadro peut être comprise comme une constante effective stabilisée de passage discret/macroscopique. Sa fonction physique est de relier le nombre d’entités élémentaires à la quantité de matière exprimée en moles.

Dans le SI actuel, elle est aussi une constante définissante de la mole : sa valeur numérique est exacte par convention métrologique. Sa stabilisation actuelle est donc conventionnelle, même si elle repose historiquement sur une consolidation empirique préalable.

La question pertinente devient :

À quelles conditions (N_A) peut-elle être traitée comme constante stabilisée, alors qu’elle est à la fois une constante de passage entre comptage microscopique et quantité macroscopique de matière, et une constante définissante exacte du système SI ?

#### 12. Fonction dans l’enquête générale

La fiche (N_A) confirme le résultat obtenu avec (k_B), mais sans le dupliquer.

Comme (k_B), (N_A) impose de distinguer :

[  ]

et :

[  ]

Comme (k_B), il impose aussi de distinguer :

[  ]

et :

[  ]

Mais sa fonction physique est différente. (k_B) relie température et énergie ; (N_A) relie nombre d’entités et quantité de matière.

La compression taxonomique commence donc à fonctionner : (k_B) et (N_A) appartiennent à la même famille conventionnelle, mais à deux sous-types physiques distincts de passage micro/macro.
