# Source DOCX - Fiche_Wolfenstein_v0_1

## Statut

```text
lot: 1E - CKM et saveur cible avant cercle 2
source physique: Fiche Wolfenstein v0.1.docx
statut: extraction textuelle de travail
document actif concerne: Synthese Saveur-Higgs ; architecture Saveur-Higgs
controle attendu: Extraction + comparaison
sha256_extraction: 04bb3a88587f4eb1dc5415fff8146db109c61ba1ef06e5be00f76f17f7adf3a6
```

## Limite

```text
Cette extraction ne remplace pas le DOCX source.
Elle rend la matiere lisible en Markdown pour comparaison et integration.
La mise en page Word n'est pas reconstruite.
```

## Extraction

### Fiche Wolfenstein v0.1

#### Paramètres de Wolfenstein, hiérarchie CKM et orientation de saveur compressée

#### 1. Identification

La paramétrisation de Wolfenstein est une manière de représenter la matrice CKM en faisant apparaître sa structure hiérarchique. Elle remplace la lecture directe en trois angles et une phase par quatre paramètres :

[ ,A,{},{} ]

Ces quatre paramètres ne forment pas une nouvelle matrice indépendante. Ils réexpriment la même structure CKM, mais sous une forme adaptée au fait empirique central :

[ s_{13}s_{23}s_{12} ]

Le PDG indique explicitement qu’il est commode d’exhiber cette hiérarchie au moyen de la paramétrisation de Wolfenstein. Il définit notamment :

[ s_{12}= ]

[ s_{23}=A^2 ]

[ s_{13}e{i}=V_{ub}{*}=A^3(+i) ]

avec une formulation moderne en ({},{}), choisie de manière à préserver l’unitarité à tous les ordres en ().

#### 2. Type logique

Les paramètres de Wolfenstein sont des paramètres sans dimension. Ils ne sont pas des constantes dimensionnées, ni des échelles, ni des masses.

Leur type logique est :

[  ]

ou, dans la taxonomie actuelle :

[  ]

Ils décrivent comment l’orientation CKM est organisée.

[  ]

mesure l’ordre principal du mélange entre les deux premières générations.

[ A ]

fixe l’amplitude relative du mélange (2).

[ {},{} ]

localisent le sommet du triangle d’unitarité et portent l’information complexe liée à la phase CP. Le PDG précise que ({}+i{}) est indépendant de la convention de phase, et que le triangle d’unitarité usuel a pour sommets ((0,0)), ((1,0)), et (({},{})).

#### 3. Régime de définition physique

Le régime de définition physique reste le même que pour CKM :

[  ]

[  ]

[  ]

La paramétrisation de Wolfenstein ne crée pas un nouveau régime physique. Elle fournit une carte hiérarchique du mélange CKM.

Son objet n’est donc pas :

[  ]

mais :

[  ]

Dans cette lecture, l’interaction faible chargée n’est pas distribuée également entre générations. Elle est fortement quasi diagonale. Les transitions proches sont favorisées ; les transitions entre générations éloignées sont supprimées par des puissances de ().

À l’ordre dominant :

[ V_{us} ]

[ V_{cb}A^2 ]

[ V_{ub}A^3(-i) ]

La hiérarchie CKM devient donc lisible comme une architecture de puissances.

#### 4. Régime d’accès épistémique

Le régime d’accès épistémique est celui de l’ajustement global CKM.

Les paramètres de Wolfenstein ne sont pas mesurés directement comme quatre objets isolés. Ils sont extraits d’un réseau d’observables : désintégrations faibles, mesures de (|V_{ij}|), mélange de mésons neutres, violation CP, angles du triangle d’unitarité et contraintes d’unitarité.

Le PDG indique que les éléments CKM les plus précisément déterminés proviennent d’un ajustement global à toutes les mesures disponibles, en imposant les contraintes du Modèle standard, notamment l’unitarité à trois générations. Il précise aussi que ces ajustements utilisent des prédictions théoriques d’éléments de matrice hadroniques, parfois avec des incertitudes significatives.

Le régime d’accès est donc :

[  ]

et non :

[  ]

Cette distinction est importante pour notre méthode : Wolfenstein est une paramétrisation stabilisée par un ensemble d’observables et de contraintes théoriques.

#### 5. Valeurs actuelles

Dans le fit global PDG fondé sur la méthode CKMfitter, les paramètres de Wolfenstein sont :

[ = 0{,}22501 00068 ]

[ A = 0{,}826^{+0{,}016}_{-0{,}015} ]

[ {}=0{,}15910094 ]

[ {}=0{,}3523^{+0{,}0073}_{-0{,}0071} ]

Le PDG donne aussi un ajustement de type UTfit très proche :

[ 2249700070 ]

[ A=0{,}839011 ]

[ {}=0{,}15810092 ]

[ {}=0{,}35480072 ]

Le fait que ces approches donnent des résultats proches renforce la stabilisation globale de la structure CKM, même si certaines tensions locales demeurent.

#### 6. Fonction physique

La fonction des paramètres de Wolfenstein est de rendre lisible la hiérarchie de l’orientation CKM.

Ils ne fixent pas une nouvelle interaction. Ils organisent la distribution des amplitudes faibles entre générations.

[  ]

est le petit paramètre d’expansion. Il encode le mélange dominant entre première et deuxième générations.

[ A ]

module l’entrée du troisième secteur générationnel.

[ {},{} ]

localisent la composante complexe de l’orientation, donc la géométrie CP du triangle d’unitarité.

La fonction générale est donc :

[  ]

Cette fonction est plus précise que “mélanger”. Wolfenstein ne dit pas seulement qu’il y a mélange ; il montre que le mélange est ordonné, asymétrique, quasi diagonal et CP-complexe.

#### 7. Triangle d’unitarité

La relation d’unitarité :

[ V_{ud}V_{ub}{}+V_{cd}V_{cb}^{}+V_{td}V_{tb}{*}=0 ]

peut être représentée comme un triangle dans le plan complexe. Après normalisation par (V_{cd}V_{cb}^{*}), le triangle usuel a pour sommets :

[ (0,0),(1,0),({},{}) ]

Le PDG souligne que de nombreuses mesures peuvent être comparées dans le plan (({},{})), et que l’objectif important de la physique de la saveur est de surcontraindre les éléments CKM.

Ce point est taxonomiquement important : ({}) et ({}) ne sont pas de simples coordonnées arbitraires. Elles condensent la géométrie d’unitarité et la composante CP de CKM.

#### 8. Violation CP et invariant de Jarlskog

La violation CP dans CKM peut être mesurée de manière indépendante des conventions de phase par l’invariant de Jarlskog. Le PDG rappelle que l’aire des triangles d’unitarité est égale à la moitié de l’invariant de Jarlskog, et donne dans son fit global :

[ J = 3{,}12^{+0{,}13}_{-0{,}12}^{-5} ]

Il donne également les paramètres de la paramétrisation standard :

[ _{12}=0{,}2250100068 ]

[ {13}=0{,}003732^{+0{,}000090}{-0{,}000085} ]

[ {23}=0{,}04183^{+0{,}00079}{-0{,}00069} ]

[ 147026 ]

Dans la lecture Wolfenstein, la violation CP est principalement portée par ({}). Une valeur non nulle de ({}) signifie que le triangle d’unitarité a une aire non nulle, donc que la structure CKM contient une phase CP physique.

#### 9. Degré de stabilisation

Les paramètres de Wolfenstein sont globalement bien stabilisés dans le cadre du Modèle standard à trois générations.

Cette stabilisation n’est cependant pas homogène.

[  ]

est très fortement stabilisé, car il est lié au secteur (V_{us}), mesuré avec une bonne précision.

[ A ]

est bien stabilisé, mais dépend davantage du secteur (V_{cb}), où les extractions inclusives et exclusives peuvent jouer un rôle dans les discussions de précision.

[ {},{} ]

sont stabilisés par la combinaison des contraintes du triangle d’unitarité, des observables CP, des mélanges de mésons et des fits globaux.

Le PDG signale toutefois une tension de (2{,}3) dans le test d’unitarité de la première ligne :

[ |V_{ud}|2+|V_{us}|2+|V_{ub}|^2 = 0{,}99840007 ]

liée notamment à la baisse récente de (|V_{ud}|).

Le statut correct est donc :

[  ]

mais :

[  ]

#### 10. Dépendance d’échelle

Le PDG précise que la matrice CKM possède une dépendance d’échelle connue au-dessus de l’échelle faible, parce que le lagrangien est renormalisé. En dessous de (=m_W), les éléments CKM peuvent être traités comme constants, l’ensemble de la dépendance en () étant portée par les masses de quarks courantes et les opérateurs de dimension supérieure.

Cela donne une formulation très utile pour notre enquête :

[  ]

La constance de Wolfenstein est donc une constance de régime :

[  ]

et non une immuabilité abstraite.

#### 11. Ce que Wolfenstein ne dit pas

La paramétrisation de Wolfenstein ne résout pas le problème de la saveur. Elle expose la hiérarchie CKM, mais elle n’en explique pas l’origine.

Elle ne dit pas pourquoi :

[ 225 ]

ni pourquoi :

[ s_{13}s_{23}s_{12} ]

ni pourquoi la phase CP a la valeur observée.

Elle ne remplace pas non plus les matrices de Yukawa. Elle en exprime une conséquence phénoménologique après diagonalisation.

Elle ne doit donc pas être traitée comme une explication fondamentale de la hiérarchie des saveurs, mais comme une paramétrisation extrêmement efficace d’une hiérarchie observée.

#### 12. Lecture par la matrice v0.2

| Critère | Lecture pour Wolfenstein |
|---|---|
| Grandeur | (,A,{},{}) |
| Type logique | Paramètres sans dimension d’une matrice unitaire complexe |
| Dimension | Sans dimension |
| Régime de définition physique | Régime électrofaible brisé ; secteur quark ; courants faibles chargés |
| Régime d’accès épistémique | Ajustement global CKM, contraintes d’unitarité, désintégrations faibles, mélanges mésoniques, observables CP |
| Fonction | Hiérarchiser l’orientation CKM |
| Dépendance d’échelle | CKM traitée comme constante sous (m_W) ; dépendance d’échelle au-dessus du faible |
| Stabilisation empirique | Forte globalement ; tensions locales à surveiller |
| Stabilisation conventionnelle | Non concernée |
| Limites | Paramétrise la hiérarchie, mais n’explique pas son origine |
| Famille fonctionnelle | Orientation |
| Sous-type | Paramètres hiérarchiques d’orientation de saveur |

#### 13. Catégorie proposée

Les paramètres de Wolfenstein ne doivent pas produire une nouvelle famille. Ils appartiennent à la famille :

[  ]

Sous-type proposé :

[  ]

Définition provisoire :

Les paramètres hiérarchiques d’orientation de saveur sont des paramètres sans dimension qui organisent, selon une hiérarchie de puissances, le désalignement entre bases de masse et bases d’interaction faible.

Ce sous-type est plus compact que les anciennes catégories issues des neutrinos. Il permet de dire :

[  ]

[  ]

Le mot “oscillatoire” devient donc local, non général.

#### 14. Formulation provisoire

Les paramètres de Wolfenstein peuvent être compris comme des constantes effectives stabilisées d’orientation hiérarchique dans le secteur quark. Leur fonction n’est pas de fixer une échelle ou une intensité d’interaction, mais d’organiser la structure CKM comme une orientation de saveur quasi diagonale, hiérarchisée par puissances de (), et dotée d’une composante complexe responsable de la violation CP.

La question pertinente devient :

À quelles conditions les paramètres de Wolfenstein peuvent-ils être traités comme constantes stabilisées, alors qu’ils ne sont pas mesurés directement, mais reconstruits par ajustement global comme coordonnées hiérarchiques de la matrice CKM ?

#### 15. Fonction dans l’enquête générale

Cette fiche confirme le rôle du cycle CKM : tester la compression de la famille Orientation.

Le résultat est positif. Wolfenstein montre que la famille Orientation peut accueillir des structures très différentes :

[ _W ]

comme orientation de champs de jauge,

[ PMNS ]

comme orientation saveur/masse à manifestation oscillatoire,

[ CKM ]

comme orientation saveur/masse à manifestation transitionnelle,

[ ,A,{},{} ]

comme coordonnées hiérarchiques de cette orientation.

La taxonomie gagne donc en compression. Elle ne crée pas une famille “Wolfenstein”. Elle reconnaît Wolfenstein comme une paramétrisation hiérarchique locale d’une famille déjà disponible : Orientation.

La prochaine étape logique sera une synthèse courte du cycle CKM, afin de formuler précisément ce qu’il impose à la carte : séparation entre orientation, oscillation, transition faible, hiérarchie et reconstruction globale.
