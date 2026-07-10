# Source DOCX - Fiche_k_B_v0_1

## Statut

```text
lot: 1D - thermo-metrologie SI ciblee avant cercle 2
source physique: Fiche k_B v0.1.docx
statut: extraction textuelle de travail
document actif concerne: Cycle metrologique SI ; architecture metrologique SI
controle attendu: Extraction + comparaison
sha256_extraction: 71d84997e189e01bf792f38827970eb7dcb39c3bfdca8b04d494c37a30dd8ee9
```

## Limite

```text
Cette extraction ne remplace pas le DOCX source.
Elle rend la matiere lisible en Markdown pour comparaison et integration.
La mise en page Word n'est pas reconstruite.
```

## Extraction

### Fiche (k_B) v0.1

#### Constante de Boltzmann, passage micro/macro et fixation conventionnelle du kelvin

#### 1. Identification

La constante de Boltzmann, notée (k_B) ou parfois simplement (k), relie la température thermodynamique à une échelle d’énergie. Elle intervient dans la physique statistique, la thermodynamique, la théorie cinétique des gaz, l’entropie statistique et les distributions d’équilibre.

Sa valeur exacte dans le SI est :

[ k_B = 1{,}380,649 ^{-23}  ]

Depuis la révision du SI entrée en vigueur en 2019, cette valeur n’a pas d’incertitude : elle est fixée par définition. Le BIPM liste (k) parmi les sept constantes définissantes du SI et donne explicitement sa valeur exacte ; il précise aussi que les valeurs numériques de ces sept constantes définissantes n’ont pas d’incertitude.

Le point décisif pour cette fiche est donc double :

[ k_B ]

est physiquement une constante de passage entre température et énergie,

mais métrologiquement, dans le SI actuel,

[ k_B ]

est une constante définissante du kelvin.

#### 2. Type logique

(k_B) est une grandeur dimensionnée. Son unité SI est :

[  ]

ou, en unités de base :

[  ]

Elle n’est donc pas directement comparable à une constante sans dimension comme (), (m_p/m_e) ou un angle de mélange. Sa valeur numérique dépend du système d’unités.

Son contenu physique apparaît dans des expressions comme :

[ k_B T ]

qui donne une énergie thermique caractéristique associée à une température (T), ou encore :

[ S = k_B W ]

dans la forme statistique de l’entropie.

Le type logique de (k_B) est donc :

[  ]

et, depuis le SI révisé :

[  ]

Ces deux statuts doivent être distingués. Le premier est physique ; le second est métrologique.

#### 3. Régime de définition physique

Le régime de définition physique de (k_B) est le passage entre description microscopique et description macroscopique.

Au niveau microscopique, les systèmes sont décrits par des états, des degrés de liberté, des distributions d’énergie et des probabilités.

Au niveau macroscopique, ils sont décrits par des grandeurs comme :

[ T,S,U,P,V ]

La constante de Boltzmann relie ces niveaux. Elle permet d’exprimer une température comme une mesure d’énergie par degré de liberté ou comme un paramètre de distribution statistique.

Dans une distribution de Boltzmann, par exemple, les probabilités relatives d’états d’énergie (E_i) dépendent du facteur :

[ e^{-E_i/(k_B T)} ]

Le produit (k_B T) fixe donc l’échelle énergétique du régime thermique.

Le régime physique de (k_B) peut ainsi être formulé comme :

[  ]

ou plus précisément :

[  ]

#### 4. Régime d’accès épistémique

Le régime d’accès épistémique de (k_B) a changé avec la réforme du SI.

Avant la révision du SI, (k_B) était une grandeur mesurée expérimentalement. Sa détermination passait par des méthodes comme la thermométrie acoustique des gaz, la thermométrie par bruit Johnson, ou d’autres techniques de métrologie thermique.

Depuis le SI révisé, la situation est inversée. (k_B) n’est plus mesuré pour définir le kelvin ; sa valeur numérique exacte sert à définir l’unité de température thermodynamique. Le BIPM indique que les définitions de quatre unités de base — kilogramme, ampère, kelvin et mole — ont été modifiées dans la révision de 2018, et que leurs nouvelles définitions reposent sur les valeurs numériques fixées de (h), (e), (k) et (N_A), respectivement.

Le régime d’accès épistémique actuel est donc :

[  ]

et non :

[  k_B ]

Ce déplacement est central pour la méthode. Il montre qu’une constante peut être physiquement significative tout en étant numériquement stabilisée par convention.

#### 5. Fonction physique

La fonction physique principale de (k_B) est de convertir une température en énergie.

[ T ]

est une grandeur thermodynamique macroscopique.

[ k_B T ]

est une énergie thermique caractéristique.

Cette conversion n’est pas une simple commodité d’unité. Elle exprime le fait que la température peut être lue comme une grandeur statistique liée à la distribution des énergies microscopiques.

Dans l’entropie statistique :

[ S = k_B W ]

(k_B) fixe l’échelle entre une quantité informationnelle ou combinatoire, (W), et une grandeur thermodynamique dimensionnée, (S).

Dans la loi des gaz parfaits sous forme microscopique :

[ PV = N k_B T ]

(k_B) relie le nombre de particules (N) à la température et à l’énergie macroscopique du gaz.

La fonction générale de (k_B) est donc :

[  ]

Elle transforme une structure statistique en grandeur thermodynamique mesurable.

#### 6. Stabilisation empirique

La stabilisation empirique de (k_B) appartient à l’histoire pré-2019 de la métrologie. Avant que sa valeur soit fixée par définition, il fallait mesurer (k_B) avec une incertitude suffisamment faible pour rendre possible la redéfinition du kelvin sans rupture avec les pratiques antérieures.

Ce point est important : la fixation conventionnelle de 2019 n’efface pas l’histoire empirique de (k_B). Elle la clôt métrologiquement.

On peut donc dire :

[  k_B  ]

[  k_B  ]

La stabilisation empirique est donc historiquement forte, mais le statut actuel de la valeur numérique est conventionnel.

#### 7. Stabilisation conventionnelle

La stabilisation conventionnelle de (k_B) est maximale dans le SI actuel.

Le BIPM donne :

[ k = 1{,}380,649 ^{-23}  ]

comme l’une des sept constantes définissantes du SI, et précise que les valeurs numériques de ces constantes n’ont pas d’incertitude.

Cela signifie que l’exactitude numérique de (k_B) n’est pas une mesure infiniment précise. Elle est une stipulation métrologique.

La bonne formulation est donc :

[ k_B  ]

et non :

[ k_B  ]

Cette distinction est le test principal du quatrième cycle.

#### 8. Ce que (k_B) ne dit pas

(k_B) ne donne pas une constante sans dimension fondamentale. Sa valeur dépend du choix des unités d’énergie et de température.

(k_B) ne dit pas non plus que la température est “réductible simplement” à l’énergie microscopique. Il donne le facteur de conversion dans les formalismes où température, énergie, entropie et probabilité sont articulées.

Enfin, le fait que (k_B) soit exact dans le SI ne signifie pas que toutes les mesures de température sont exactes. Les réalisations pratiques du kelvin gardent leurs incertitudes expérimentales. Le BIPM précise que les unités du SI sont définies par les constantes fixées, mais que des mises en pratique sont nécessaires pour expliquer la réalisation pratique des définitions des unités de base.

La constante est donc exacte dans le système ; les mesures concrètes ne le sont pas.

#### 9. Lecture par la matrice v0.2

| Critère | Lecture pour (k_B) |
|---|---|
| Grandeur | Constante de Boltzmann |
| Type logique | Constante dimensionnée de conversion physique |
| Dimension | () |
| Régime de définition physique | Thermodynamique statistique, passage micro/macro |
| Régime d’accès épistémique | Définition SI par valeur numérique fixée |
| Fonction | Convertir température en énergie ; relier entropie statistique et entropie thermodynamique |
| Dépendance d’échelle | Non pertinente au sens renormalisation ; dépendance aux unités |
| Stabilisation empirique | Historiquement mesurée ; empiriquement consolidée avant 2019 |
| Stabilisation conventionnelle | Fixée exactement dans le SI |
| Limites | Exactitude conventionnelle ≠ mesure sans incertitude ; grandeur dimensionnée ≠ rapport fondamental |
| Famille fonctionnelle | Convention + passage micro/macro |
| Sous-type | Constante définissante d’un système d’unités ; constante de conversion thermodynamique |

#### 10. Catégorie proposée

(k_B) appartient à deux catégories, situées sur deux axes différents.

Sur l’axe physique :

constante de passage micro/macro.

Définition provisoire :

Une constante de passage micro/macro est une grandeur qui relie une description statistique microscopique à une grandeur thermodynamique macroscopique.

Sur l’axe d’accès épistémique :

constante définissante d’un système d’unités.

Définition provisoire :

Une constante définissante d’un système d’unités est une grandeur à laquelle un système métrologique attribue une valeur numérique exacte afin de définir une ou plusieurs unités.

Le point crucial est que ces deux catégories ne sont pas concurrentes. Elles répondent à deux questions différentes :

[  k_B  ]

et :

[  ]

#### 11. Formulation provisoire

La constante de Boltzmann peut être comprise comme une constante effective stabilisée de passage micro/macro, dont la fonction physique est de relier température, énergie et entropie dans le régime thermodynamique-statistique.

Dans le SI actuel, elle est aussi une constante définissante du kelvin : sa valeur numérique est exacte par convention métrologique. Sa stabilisation actuelle n’est donc pas seulement empirique ; elle est conventionnelle.

La question pertinente devient :

À quelles conditions (k_B) peut-elle être traitée comme constante stabilisée, alors qu’elle est à la fois un facteur physique de passage entre microphysique et thermodynamique, et une constante définissante exacte du système SI ?

#### 12. Fonction dans l’enquête générale

La fiche (k_B) confirme la nécessité de la matrice v0.2.

Avec (k_B), il devient impossible de maintenir un seul axe de stabilisation. Il faut distinguer :

[  ]

et :

[  ]

Il devient aussi nécessaire de distinguer :

[  ]

et :

[  ]

Physiquement, (k_B) appartient au raccordement micro/macro. Métrologiquement, il appartient au système des constantes définissantes du SI.

Cette fiche réussit donc le premier test du quatrième cycle : elle ne crée pas une catégorie isolée pour (k_B), mais montre que la même grandeur doit être classée selon deux axes distincts.
