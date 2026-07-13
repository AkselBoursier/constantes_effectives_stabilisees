# Source DOCX - Fiche_Delta_m2_v0_1

## Statut

```text
lot: 1C - neutrinos
source physique: Fiche Delta m^2.docx
source physique path: 02_CYCLES_PHYSIQUES/03_Cycle_neutrinos/00_Sources_docx/Fiche Delta m^2.docx
sha256_source: 77bc17cfdabc259f899eed42a37d429c834a4bee95b49e67f8acae494126b65d
statut: extraction DOCX de travail
document actif concerne: Cycle Saveur-Higgs; PMNS / oscillations
controle attendu: Extraction
```

## Limite

```text
Cette extraction ne remplace pas la source originale.
Elle rend la matiere lisible en Markdown pour comparaison et integration.
La mise en page Word, les equations, tableaux et elements graphiques
peuvent etre restitues de maniere incomplete.
```

> Verifier la source originale avant toute reprise scientifique.
> Convention : [CONVENTION_PLACEHOLDERS.md](../../../CONVENTION_PLACEHOLDERS.md)

## Extraction

## Fiche (m^2) v0.1

## Différences de masses au carré et constantes de phase oscillatoire

## 1. Identification

Les différences de masses au carré des neutrinos sont définies par :

\[ m<sup>2\_{ij}=m_i</sup>2-m_j^2 \]

où (m_i) et (m_j) sont les masses des états propres de masse (\_i) et (\_j). Dans le cadre à trois neutrinos, les oscillations ne dépendent pas des trois masses absolues prises séparément, mais principalement de deux différences indépendantes de masses au carré.

Les deux grandeurs centrales sont :

\[ m^2\_{21} \]

et

\[ m^2\_{3} \]

avec une convention dépendant de l’ordre des masses :

\[ m^2\_{3}\>0 \]

pour l’ordre normal, et :

\[ m^2\_{3}\<0 \]

pour l’ordre inversé. NuFIT 6.0 utilise explicitement cette convention dans son analyse globale des données d’oscillation disponibles jusqu’en septembre 2024.

Les valeurs typiques sont de deux ordres de grandeur différents :

\[ m<sup>2\_{21}7{,}5</sup>{-5} ^2 \]

et :

\[ \|m<sup>2\_{3}\|2{,}5</sup>{-3} ^2 \]

NuFIT 6.0 donne, dans la variante incluant les cartes atmosphériques IC24 et Super-Kamiokande, pour l’ordre normal :

\[ m<sup>2\_{21}=7{,}49</sup>{+0{,}19}\_{-0{,}19}<sup>{-5} </sup>2 \]

et :

\[ m<sup>2\_{31}=+2{,}513</sup>{+0{,}021}\_{-0{,}019}<sup>{-3} </sup>2 \]

Pour l’ordre inversé, la même analyse donne :

\[ m<sup>2\_{32}=-2{,}484</sup>{+0{,}020}\_{-0{,}020}<sup>{-3} </sup>2 \]

avec le même (m^2\_{21}).

## 2. Statut physique

Les (m^2) ne sont pas des masses absolues. Ce sont des différences entre carrés de masses. Leur statut est donc relationnel dès le départ.

Les oscillations de neutrinos ne mesurent pas directement :

\[ m_1,m_2,m_3 \]

Elles mesurent les phases relatives accumulées entre états de masse au cours de la propagation. Dans une approximation à deux états, la probabilité d’oscillation contient un terme du type :

\[ ^2() \]

où (L) est la distance de propagation et (E) l’énergie du neutrino.

Le point essentiel est que (m^2) entre dans une phase sans dimension :

\[ \]

Une grandeur dimensionnée, (m^2), devient observable par son inscription dans une combinaison de propagation. Elle n’est pas mesurée comme une masse posée sur une balance conceptuelle, mais comme un motif d’interférence.

## 3. Deux échelles oscillatoires

Le secteur neutrino présente deux échelles principales.

La première est l’échelle solaire :

\[ m^2\_{21} \]

Elle gouverne principalement les oscillations solaires et une partie des oscillations de réacteurs à longue distance.

La seconde est l’échelle atmosphérique :

\[ \|m^2\_{3}\| \]

Elle gouverne principalement les oscillations atmosphériques, les expériences à longue ligne de base et les expériences de réacteurs à courte ou moyenne distance.

Le rapport d’ordre de grandeur entre les deux est :

\[ 33 \]

Cette hiérarchie structure toute la phénoménologie oscillatoire. Elle permet de séparer approximativement des régimes expérimentaux : solaire, atmosphérique, réacteur, longue ligne de base.

## 4. Différences de masses et ordre des masses

Les (m^2) permettent de connaître les écarts entre masses, mais pas directement l’ordre complet avec certitude absolue.

Deux ordres restent distingués :

\[ m_1\<m_2\<m_3 \]

\[ m_3\<m_1\<m_2 \]

Le signe de la grande différence de masses au carré est donc central. Si :

\[ m^2\_{31}\>0 \]

on est dans l’ordre normal. Si :

\[ m^2\_{32}\<0 \]

on est dans l’ordre inversé.

NuFIT 6.0 indique que les données actuelles ont en principe une sensibilité de l’ordre de (2{,}5) à (3) à l’ordre des masses, mais que des tensions entre différents jeux de données réduisent la discrimination effective. Avec certaines données atmosphériques Super-Kamiokande ajoutées, l’ordre normal est préféré avec (^2=6{,}1), mais le statut reste à formuler prudemment.

## 5. Ce que les (m^2) ne disent pas

Les différences de masses au carré ne donnent pas la masse absolue des neutrinos. Si l’on ajoute une même contribution commune aux trois masses, les oscillations ne suffisent pas à déterminer cette contribution.

Autrement dit, les oscillations sont sensibles aux écarts :

\[ m_i<sup>2-m_j</sup>2 \]

mais pas directement à l’échelle absolue :

\[ m_1+m_2+m_3 \]

ni à la masse du plus léger neutrino.

C’est pourquoi la masse absolue doit être contrainte par d’autres voies : cinématique de la désintégration bêta, cosmologie, ou double désintégration bêta sans neutrino si les neutrinos sont de Majorana. Les (m^2) donnent donc l’architecture relative du spectre, pas son ancrage absolu.

## 6. Régime de manifestation

Les (m^2) deviennent physiquement lisibles dans un régime oscillatoire.

Ce régime exige plusieurs conditions :

les neutrinos doivent être produits dans des états de saveur ;

ils doivent se propager comme superpositions cohérentes d’états de masse ;

les différences de phase doivent rester observables sur une distance (L) et une énergie (E) données ;

la détection doit projeter à nouveau l’état propagé sur une saveur observable.

La grandeur (m^2) est donc une constante de propagation relative. Elle ne décrit pas une intensité d’interaction. Elle décrit la vitesse à laquelle deux composantes de masse se déphasent l’une par rapport à l’autre.

## 7. Effets de matière

En matière, les oscillations peuvent être modifiées par les interactions cohérentes des neutrinos avec les électrons du milieu. C’est l’effet MSW. Dans ce cas, les paramètres effectifs de propagation ne sont plus exactement ceux du vide.

Il faut donc distinguer :

\[ m^2\_{} \]

et les paramètres effectifs en matière.

Cette distinction est importante pour la cartographie. Les (m^2) du vide peuvent être traités comme constantes du secteur neutrino, tandis que les grandeurs effectives en matière dépendent du milieu, de la densité électronique et de l’énergie.

La constance de (m^2) est donc celle d’un paramètre de propagation dans le vide, ou d’un paramètre fondamental reconstruit à travers des analyses qui corrigent les effets de matière.

## 8. Lecture par la grille des constantes effectives stabilisées

| Critère                | Lecture pour (m^2)                              |
|------------------------|-------------------------------------------------|
| Type de grandeur       | Différence de masses au carré                   |
| Dimension              | (^2)                                            |
| Grandeurs principales  | (m^2\_{21}), (m^2\_{3})                         |
| Valeur solaire         | (7{,}5<sup>{-5} </sup>2)                        |
| Valeur atmosphérique   | (2{,}5<sup>{-3} </sup>2)                        |
| Observable direct      | Phase d’oscillation dépendant de (m^2 L/E)      |
| Statut                 | Grandeur relationnelle de propagation           |
| Ce qu’elle fixe        | Écart entre états de masse                      |
| Ce qu’elle ne fixe pas | Masse absolue des neutrinos                     |
| Régime requis          | Propagation cohérente et oscillations de saveur |
| Catégorie proposée     | Constante de phase oscillatoire                 |

## 9. Catégorie proposée

Les différences de masses au carré introduisent la catégorie de **constantes de phase oscillatoire**.

Une constante de phase oscillatoire désigne une grandeur qui ne se manifeste pas principalement comme valeur absolue d’une propriété, mais comme rythme de déphasage entre composantes d’un état quantique. Sa constance se lit dans la stabilité des motifs d’oscillation selon (L/E).

Cette catégorie est plus précise que la catégorie générale de “masse”. Les (m^2) ne sont pas des masses ; elles sont des écarts de masses au carré rendus visibles par des interférences.

## 10. Formulation provisoire

Les différences de masses au carré des neutrinos peuvent être comprises comme des constantes effectives stabilisées du régime oscillatoire. Elles ne déterminent pas l’échelle absolue des masses, mais elles stabilisent les phases relatives qui rendent possible la transformation observable des saveurs.

La question pertinente devient donc :

**À quelles conditions les différences de masses au carré peuvent-elles être traitées comme constantes stabilisées, alors qu’elles ne sont accessibles qu’à travers des phases de propagation et ne fixent pas les masses absolues des neutrinos ?**

## 11. Fonction dans l’enquête générale

Cette fiche précise le cœur du secteur neutrino. Elle montre qu’une constante physique peut être essentiellement différentielle : elle ne donne pas une valeur absolue, mais une structure d’écarts.

Avec (m^2), la constance n’est pas celle d’un objet isolé. Elle est celle d’un rythme relatif. La stabilité observée est celle d’un motif d’interférence, d’un rapport entre distance, énergie et différence de masse.

Ce cas enrichit la cartographie en ajoutant une forme spécifique de constance :

\[ \]

La prochaine fiche pourra traiter les angles de mélange leptoniques (*{12}), (*{23}), (\_{13}), qui déterminent non plus le rythme des oscillations, mais leur amplitude et leur structure de projection entre saveur et masse.
