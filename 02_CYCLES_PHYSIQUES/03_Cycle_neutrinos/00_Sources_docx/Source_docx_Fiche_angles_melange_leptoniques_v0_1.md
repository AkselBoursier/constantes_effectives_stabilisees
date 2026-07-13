# Source DOCX - Fiche_angles_melange_leptoniques_v0_1

## Statut

```text
lot: 1C - neutrinos
source physique: Fiche Angles de Mélange Leptoniques.docx
source physique path: 02_CYCLES_PHYSIQUES/03_Cycle_neutrinos/00_Sources_docx/Fiche Angles de Mélange Leptoniques.docx
sha256_source: 6262f9f5738091e07156571f2a7ace73070e838d02bc0eaf8bdf8600feca30b9
statut: extraction DOCX de travail
document actif concerne: Cycle Saveur-Higgs; PMNS
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

## Fiche (*{12},* {23}, \_{13}) v0.1

## Angles de mélange leptoniques et constantes de projection oscillatoire

## 1. Identification

Les angles de mélange leptoniques (*{12}), (*{23}) et (\_{13}) sont les trois angles qui paramètrent la matrice PMNS dans le cadre standard à trois neutrinos. Cette matrice relie les états de saveur produits et détectés par interaction faible :

\[ *e,*,\_ \]

aux états de masse qui se propagent :

\[ \_1,\_2,\_3 \]

On écrit généralement :

\[ \|\_= *i U*{i}^\* \|\_i \]

où (=e,,), (i=1,2,3), et (U) est la matrice PMNS.

Le PDG rappelle que la matrice de mélange leptonique organise la relation entre états de saveur et états de masse, et que les oscillations de neutrinos résultent précisément de cette non-coïncidence entre base d’interaction et base de propagation. Le même chapitre indique aussi que, dans le Modèle standard minimal, les neutrinos sont sans masse, et qu’il faut étendre le modèle pour introduire des masses de neutrinos.

## 2. Statut physique

Les angles PMNS ne sont pas des masses et ne sont pas des couplages d’intensité. Ce sont des paramètres d’orientation entre deux bases physiques :

\[ \]

et

\[ \]

Ils déterminent comment un neutrino produit comme (*e), (*) ou (\_) se décompose en états de masse (\_1,\_2,\_3). Pendant la propagation, ces états de masse accumulent des phases différentes ; à la détection, la recomposition donne une probabilité de trouver une autre saveur.

Les (m^2) fixent le rythme de déphasage. Les angles (*{12},*{23},\_{13}) fixent la géométrie de projection. Ils contrôlent donc les amplitudes relatives des canaux d’oscillation.

La catégorie pertinente est donc :

**constantes de projection oscillatoire.**

## 3. Paramétrisation standard

Dans la convention standard, la matrice PMNS peut être écrite comme un produit de trois rotations, avec une phase CP :

\[ U = R\_{23}(*{23}) ,U*{13}(*{13},*{}) ,R\_{12}(\_{12}) \]

Les trois angles jouent des rôles différents.

\[ \_{12} \]

est principalement associé au secteur solaire.

\[ \_{23} \]

est principalement associé au secteur atmosphérique.

\[ \_{13} \]

couple le secteur électronique au troisième état de masse et rend possible l’accès expérimental à la violation CP dans les expériences à longue ligne de base.

Cette séparation n’est pas absolue, car le système complet est tridimensionnel. Mais elle donne une lecture physique utile des trois angles.

## 4. Valeurs actuelles et niveau de stabilisation

NuFIT 6.0, publié en 2024 à partir des données disponibles jusqu’en septembre 2024, indique que (*{12}), (*{13}), (m^2\_{21}) et (\|m^2\_{3}\|) sont bien déterminés. En revanche, (\_{23}) souffre encore de l’ambiguïté d’octant : les données ne tranchent pas clairement entre une valeur inférieure ou supérieure à (45^).

Dans une notation usuelle en (^2), les valeurs typiques du fit global sont approximativement :

\[ ^2\_{12} 31 \]

\[ ^2\_{13} 022 \]

\[ ^2\_{23} 45 - 0{,}58 \]

selon l’ordre des masses, les jeux de données et les minima locaux. Le point important n’est pas seulement la valeur centrale ; c’est le degré de stabilisation différent de chaque angle. (*{12}) et (*{13}) sont relativement bien contraints. (\_{23}), lui, reste structurellement plus ambigu.

## 5. (\_{12}) : angle solaire

(\_{12}) contrôle principalement le mélange entre les deux premiers états de masse. Il est fortement lié aux oscillations solaires et aux expériences de réacteurs à longue distance.

Sa valeur est grande, mais non maximale :

\[ \_{12}33^ \]

Cela signifie que (\_e) possède une forte composante sur les deux premiers états de masse. Le mélange solaire n’est donc pas une petite correction ; il est une structure majeure du secteur leptonique.

Pour la cartographie, (\_{12}) est un bon exemple de constante de projection bien stabilisée. Il détermine une composante géométrique robuste de la matrice PMNS.

## 6. (\_{23}) : angle atmosphérique et ambiguïté d’octant

(*{23}) contrôle principalement le mélange entre les secteurs (*) et (\_). Il est lié aux oscillations atmosphériques et aux expériences à longue ligne de base.

Sa valeur est proche de :

\[ 45^ \]

mais la question décisive est de savoir s’il est exactement maximal, inférieur à (45^), ou supérieur à (45^). On parle d’ambiguïté d’octant.

Si :

\[ \_{23}\<45^ \]

on est dans le premier octant. Si :

\[ \_{23}\>45^ \]

on est dans le second octant.

NuFIT 6.0 indique que (\_{23}) reste soumis à cette ambiguïté, sans indication claire et stable de l’octant.

Pour notre grille, (\_{23}) est donc une constante partiellement stabilisée : elle est connue comme grande et proche de la maximalité, mais son statut fin reste ouvert.

## 7. (\_{13}) : petit angle non nul

(\_{13}) est plus petit que les deux autres angles, mais il est non nul :

\[ \_{13}8{,}5^ \]

ou :

\[ ^2\_{13}022 \]

Ce résultat est crucial. Si (*{13}) était nul, certains canaux d’oscillation seraient fortement simplifiés, et la phase (*{}) serait beaucoup moins accessible expérimentalement dans les oscillations à trois saveurs.

Le fait que (*{13}) soit non nul ouvre la possibilité d’étudier la violation CP leptonique dans les expériences à longue ligne de base. (*{13}) est donc une petite constante de projection, mais à grande conséquence phénoménologique. Le cas est presque une leçon de sobriété cosmique : petit angle, grosses emmerdes expérimentales.

## 8. Angles et amplitudes d’oscillation

Les angles PMNS entrent dans les probabilités d’oscillation via les modules et produits des éléments de la matrice (U). Dans une approximation à deux saveurs, l’amplitude d’oscillation est contrôlée par :

\[ ^2(2) \]

tandis que la phase est contrôlée par :

\[ \]

Cette distinction est importante.

\[ m^2 \]

fixe le rythme de l’oscillation.

\[ \]

fixe l’amplitude du mélange.

Dans le système à trois saveurs, cette image devient plus riche, mais le principe reste valable : les angles ne donnent pas les fréquences d’oscillation ; ils déterminent les projections et les poids des composantes de masse dans chaque saveur.

## 9. Différence avec les angles de mélange de jauge

Les angles PMNS ne doivent pas être confondus avec un angle de mélange de champs de jauge. Ici, l’angle ne transforme pas des champs de jauge neutres en bosons physiques. Il transforme des états de saveur en états de masse.

La structure est donc :

\[ \]

et non :

\[ \]

Cette différence justifie une catégorie propre. Les angles PMNS sont des constantes de projection entre états quantiques, mesurées par des phénomènes d’oscillation.

## 10. Lecture par la grille des constantes effectives stabilisées

| Critère | Lecture pour les angles PMNS |
|----|----|
| Type de grandeur | Angles sans dimension |
| Grandeurs | (*{12}), (*{23}), (\_{13}) |
| Matrice associée | PMNS |
| Bases reliées | Saveur et masse |
| Rôle principal | Projection entre états produits/détectés et états propagés |
| Observable | Probabilités d’oscillation |
| Rôle de (\_{12}) | Mélange solaire |
| Rôle de (\_{23}) | Mélange atmosphérique, ambiguïté d’octant |
| Rôle de (\_{13}) | Couplage au troisième état, accès à (\_{}) |
| Niveau de stabilisation | (*{12}), (*{13}) bien contraints ; (\_{23}) plus ouvert |
| Catégorie proposée | Constantes de projection oscillatoire |

## 11. Catégorie proposée

Les angles PMNS introduisent la catégorie de **constantes de projection oscillatoire**.

Une constante de projection oscillatoire désigne un paramètre sans dimension qui stabilise la relation entre états de saveur et états de masse. Elle ne mesure pas une force, ne fixe pas une masse et ne détermine pas directement une fréquence. Elle fixe la géométrie de composition des états.

Cette catégorie inclut :

\[ *{12},*{23},\_{13} \]

avec des degrés de stabilisation différents. (*{12}) et (*{13}) sont relativement bien déterminés ; (\_{23}) reste plus problématique à cause de la question de la maximalité et de l’octant.

## 12. Formulation provisoire

Les angles de mélange leptoniques peuvent être compris comme des constantes effectives stabilisées du régime oscillatoire. Leur constance se manifeste dans la stabilité des probabilités de transition entre saveurs, non comme masse absolue ou intensité de couplage, mais comme géométrie de projection entre bases quantiques.

La question pertinente devient donc :

**À quelles conditions les angles PMNS peuvent-ils être traités comme constantes stabilisées, alors qu’ils déterminent non le rythme des oscillations, mais la structure de projection entre saveur et masse ?**

## 13. Fonction dans l’enquête générale

Cette fiche complète la fiche (m^2). Les différences de masses au carré donnent les phases relatives ; les angles PMNS donnent la géométrie du mélange.

Le secteur neutrino révèle ainsi deux formes complémentaires de constance :

\[ \]

et

\[ \]

Cette distinction est importante pour la cartographie générale. Elle montre qu’une constante peut stabiliser non seulement une valeur, une échelle ou un couplage, mais aussi une architecture de transition entre états quantiques.
