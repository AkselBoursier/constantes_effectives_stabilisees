# Source DOCX - Fiche_R_v0_1

## Statut

```text
lot: 1D - thermo-metrologie SI ciblee avant cercle 2
source physique: Fiche R v0.1.docx
statut: extraction textuelle de travail
document actif concerne: Cycle metrologique SI ; architecture metrologique SI
controle attendu: Extraction + controle positif
sha256_extraction: b9e5b9490b8078f2a46aa3a27a9dab9b36120794a9f6bdb36ec49e9f38996fca
```

## Limite

```text
Cette extraction ne remplace pas le DOCX source.
Elle rend la matiere lisible en Markdown pour comparaison et integration.
La mise en page Word n'est pas reconstruite.
```

## Extraction

### Fiche (R) v0.1

#### Constante molaire des gaz, composition (N_A k_B) et exactitude dérivée

#### 1. Identification

La constante molaire des gaz, notée (R), intervient notamment dans l’équation des gaz parfaits :

[ PV = nRT ]

Elle relie la pression (P), le volume (V), la quantité de matière (n) et la température thermodynamique (T).

Depuis la révision du SI entrée en vigueur en 2019, (R) possède une valeur exacte par composition :

[ R = N_A k_B ]

avec :

[ N_A = 6{,}022,140,76 ^{23}  ]

et :

[ k_B = 1{,}380,649 ^{-23}  ]

Le BIPM liste (N_A) et (k) parmi les sept constantes définissantes du SI, avec des valeurs numériques exactes et sans incertitude.

Il en résulte :

[ R = 8{,}314,462,618,153,24  ]

Cette valeur est exacte dans le SI actuel parce qu’elle résulte du produit de deux constantes définissantes exactes.

#### 2. Type logique

(R) est une grandeur dimensionnée. Son unité SI est :

[  ]

Elle combine deux dimensions conceptuellement distinctes :

[  ]

liée à la température thermodynamique,

et :

[  ]

liée à la quantité de matière.

Le type logique de (R) est donc :

[  ]

mais, depuis le SI 2019, son statut métrologique exact vient de :

[ R=N_Ak_B ]

Elle est donc aussi :

[  ]

Ce point la distingue de (k_B) et de (N_A). (k_B) et (N_A) sont des constantes définissantes du SI ; (R), elle, est exacte parce qu’elle est dérivée de deux constantes définissantes.

#### 3. Régime de définition physique

Le régime de définition physique de (R) est la thermodynamique molaire.

Là où (k_B) relie température et énergie par particule :

[ E_{} k_B T ]

et où (N_A) relie nombre d’entités et quantité de matière :

[ N=nN_A ]

(R) relie température et énergie par mole :

[ RT = N_A k_B T ]

Ainsi, (R) est la version molaire de (k_B). Elle transporte le passage micro/macro vers le langage de la quantité de matière.

Dans la loi des gaz parfaits, on peut écrire soit :

[ PV = Nk_B T ]

avec (N) le nombre de particules, soit :

[ PV = nRT ]

avec (n) la quantité de matière en moles.

La relation :

[ N=nN_A ]

transforme l’une en l’autre. Le régime physique de (R) est donc :

[  ]

ou :

[  ]

#### 4. Régime d’accès épistémique

Le régime d’accès épistémique de (R) a changé avec la réforme du SI.

Avant 2019, (R) pouvait être déterminée expérimentalement, notamment par des mesures thermodynamiques et acoustiques de gaz. Des déterminations de (R) par mesures de vitesse du son dans des gaz ont historiquement contribué à la métrologie thermique et à la détermination de (k_B).

Depuis le SI révisé, (R) n’est plus une constante à mesurer pour fixer l’échelle thermodynamique. Sa valeur découle exactement de deux constantes définissantes :

[ R=N_A k_B ]

Le BIPM précise que les sept constantes définissantes ont des valeurs numériques exactes et que toutes les unités du SI peuvent s’écrire à partir de constantes définissantes, de leurs produits ou de leurs quotients.

Le régime d’accès actuel est donc :

[  ]

et non :

[  R ]

Le statut de (R) est ainsi légèrement différent de celui de (k_B) et de (N_A) : il est conventionnel, mais par dérivation.

#### 5. Fonction physique

La fonction physique principale de (R) est de relier la température à une énergie molaire.

[ RT ]

est l’énergie thermique caractéristique par mole.

Dans l’équation des gaz parfaits :

[ PV=nRT ]

(R) donne la constante de proportionnalité entre les variables macroscopiques du gaz.

Dans la relation entre entropie molaire et entropie par particule, (R) joue aussi le rôle de facteur molaire :

[ R=N_Ak_B ]

Cela signifie que (R) transporte au niveau molaire la fonction de (k_B). Là où (k_B) relie énergie et température par entité, (R) relie énergie et température par mole d’entités.

La fonction générale de (R) est donc :

[  ]

ou plus précisément :

[  ]

#### 6. Stabilisation empirique

Historiquement, (R) était déterminée expérimentalement. Des mesures récentes peuvent encore déterminer une valeur expérimentale de (R) à des fins de comparaison, de validation instrumentale ou de métrologie thermique historique. Par exemple, une détermination acoustique publiée en 2024 rapporte :

[ R = (8{,}314,449 000,056)  ]

avec une incertitude relative de (6{,}7) parties par million, dans un dispositif acoustique sur argon.

Mais dans le SI actuel, ce type de mesure ne définit plus (R). Il teste une réalisation expérimentale, une méthode, un dispositif ou une cohérence historique. La valeur SI de (R) est fixée par composition à partir de (N_A) et (k_B).

La stabilisation empirique de (R) est donc historiquement réelle, mais métrologiquement secondaire depuis 2019.

#### 7. Stabilisation conventionnelle

La stabilisation conventionnelle de (R) est dérivée.

Elle n’est pas une constante définissante primaire du SI. Le BIPM ne la liste pas parmi les sept constantes définissantes. Les constantes définissantes incluent notamment (k) et (N_A), dont les valeurs numériques sont exactes.

Mais comme :

[ R=N_Ak_B ]

et que (N_A) et (k_B) sont exactes dans le SI, alors (R) est exacte par composition.

La bonne formulation est donc :

[ R  ]

et non :

[ R  ]

Cette nuance est importante. Elle permet d’éviter de placer toutes les constantes exactes dans la même case.

#### 8. Ce que (R) ne dit pas

(R) ne donne pas une constante fondamentale indépendante. Elle est le produit de deux constantes :

[ N_A ]

et :

[ k_B ]

Elle ne fournit donc pas une information physique nouvelle par rapport à ces deux constantes prises ensemble.

(R) ne dit pas non plus que tous les gaz sont parfaits. Dans l’équation :

[ PV=nRT ]

(R) appartient au modèle du gaz parfait. Les gaz réels exigent des corrections : interactions moléculaires, volume propre, coefficients du viriel, effets quantiques ou transitions de phase.

Enfin, le fait que (R) soit exacte dans le SI ne signifie pas que les mesures de pression, volume, température ou quantité de matière sont exactes. L’exactitude conventionnelle de la constante n’efface pas les incertitudes expérimentales des grandeurs mesurées.

#### 9. Lecture par la matrice v0.2

| Critère | Lecture pour (R) |
|---|---|
| Grandeur | Constante molaire des gaz |
| Type logique | Constante dimensionnée thermodynamique molaire |
| Dimension | () |
| Régime de définition physique | Thermodynamique molaire ; passage particulaire/molaire |
| Régime d’accès épistémique | Déduction algébrique depuis (N_A) et (k_B) fixées dans le SI |
| Fonction | Relier température, énergie molaire et quantité de matière |
| Dépendance d’échelle | Non pertinente au sens renormalisation ; dépendance au système d’unités |
| Stabilisation empirique | Historiquement mesurée ; aujourd’hui secondaire pour la définition SI |
| Stabilisation conventionnelle | Exacte par composition |
| Limites | Exactitude de (R) ≠ exactitude des mesures thermodynamiques ; gaz parfait ≠ gaz réel |
| Famille fonctionnelle | Convention + passage micro/macro molaire |
| Sous-type | Constante exacte par composition ; constante thermodynamique molaire |

#### 10. Catégorie proposée

(R) appartient à deux axes distincts.

Sur l’axe physique :

constante de passage micro/macro molaire.

Définition provisoire :

Une constante de passage micro/macro molaire est une grandeur qui transpose au niveau de la mole une relation entre énergie, température et nombre d’entités.

Sur l’axe d’accès épistémique :

constante exacte par composition.

Définition provisoire :

Une constante exacte par composition est une grandeur dont la valeur numérique est exacte parce qu’elle résulte algébriquement de constantes définissantes exactes.

Ces deux classements répondent à deux questions différentes :

[  R  ]

et :

[  ]

#### 11. Formulation provisoire

La constante molaire des gaz peut être comprise comme une constante effective stabilisée de passage micro/macro en version molaire. Elle relie température, énergie et quantité de matière dans le régime thermodynamique molaire.

Dans le SI actuel, (R) n’est pas une constante définissante primaire. Elle est exacte par composition, parce qu’elle est le produit de deux constantes définissantes exactes :

[ R=N_Ak_B ]

Sa stabilisation actuelle est donc conventionnelle-dérivée.

La question pertinente devient :

À quelles conditions (R) peut-elle être traitée comme constante stabilisée, alors qu’elle est à la fois une constante thermodynamique molaire et une grandeur exacte par composition dans le SI actuel ?

#### 12. Fonction dans l’enquête générale

La fiche (R) confirme le succès du quatrième cycle sur le plan taxonomique.

Elle ne crée pas une nouvelle famille générale. Elle confirme une sous-catégorie précise :

[  ]

Elle montre aussi que la famille “Convention” doit être structurée en au moins deux sous-types :

[  ]

et :

[  ]

Le cycle (k_B), (N_A), (R) montre donc que la méthode v0.2 compresse mieux que la v0.1. Trois grandeurs différentes peuvent être classées dans la même grande famille conventionnelle, tout en conservant leurs fonctions physiques distinctes :

[ k_B ]

comme passage température/énergie,

[ N_A ]

comme passage comptage/mole,

[ R ]

comme passage énergie/température/quantité de matière en version molaire.

Cette fiche remplit le test prévu : (R) modifie la taxonomie sans l’éparpiller.
