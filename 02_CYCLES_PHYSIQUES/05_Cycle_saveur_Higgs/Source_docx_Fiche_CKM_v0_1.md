# Source DOCX - Fiche_CKM_v0_1

## Statut

```text
lot: 1E - CKM et saveur cible avant cercle 2
source physique: Fiche CKM v0.1.docx
statut: extraction textuelle de travail
document actif concerne: Synthese Saveur-Higgs ; architecture Saveur-Higgs
controle attendu: Extraction + comparaison
sha256_extraction: 4c3223b10db3adb14ff3f65ceb5757d115c722568b1b21d72ab8f2c7b79ba93c
```

## Limite

```text
Cette extraction ne remplace pas le DOCX source.
Elle rend la matiere lisible en Markdown pour comparaison et integration.
La mise en page Word n'est pas reconstruite.
```

## Extraction

### Fiche CKM v0.1

#### Matrice CKM, mélange des quarks et orientation faible dans le secteur quark

#### 1. Identification

La matrice CKM, pour Cabibbo-Kobayashi-Maskawa, est la matrice de mélange des quarks dans le Modèle standard. Elle décrit la manière dont les quarks de type up :

[ u,c,t ]

se couplent, par interaction faible chargée, aux quarks de type down :

[ d,s,b ]

via les bosons (W^).

Dans le Modèle standard, les masses et les mélanges des quarks ont une origine commune : les interactions de Yukawa avec le champ de Higgs. Lorsque le champ de Higgs acquiert sa valeur moyenne dans le vide, les matrices de Yukawa donnent des termes de masse pour les quarks ; la diagonalisation de ces matrices fait apparaître la matrice CKM dans les courants faibles chargés. Le PDG formule explicitement :

[ V_{} = V_L^u V_L^{d} ]

et l’insère dans le couplage des quarks physiques au boson (W^+).

La matrice CKM est une matrice unitaire (3) :

[ V_{}=

]

Elle est paramétrable par trois angles de mélange et une phase complexe responsable de la violation CP dans les processus de changement de saveur du Modèle standard.

#### 2. Type logique

La matrice CKM n’est pas une constante numérique simple. C’est une matrice unitaire complexe sans dimension.

Elle contient neuf éléments complexes, mais l’unitarité et les redéfinitions de phase des champs de quarks réduisent le nombre de paramètres physiques à quatre :

[ {12},{23},_{13}, ]

c’est-à-dire trois angles de mélange et une phase CP.

Son type logique est donc :

[  ]

ou plus précisément :

[  ]

Mais dans la taxonomie v0.3, il vaut mieux ne pas créer une nouvelle famille. CKM relève d’abord de la famille supérieure :

[  ]

avec un sous-type local :

[  ]

#### 3. Régime de définition physique

Le régime de définition physique de CKM est le régime électrofaible brisé, après diagonalisation des matrices de masse des quarks.

Avant diagonalisation, les quarks apparaissent dans une base de saveur faible. Après diagonalisation des matrices de Yukawa, on obtient les états physiques de masse. La matrice CKM exprime le désalignement entre ces bases dans le secteur des courants faibles chargés.

Le point essentiel est donc :

[  ]

Cela la rapproche de PMNS, mais sans l’identifier à PMNS. Dans le secteur neutrino, le mélange se manifeste par des oscillations de particules libres propagées sur de longues distances. Dans le secteur quark, les quarks ne sont pas observés comme particules libres isolées ; le mélange CKM se manifeste principalement dans des transitions faibles et des désintégrations de hadrons.

Le régime de définition physique est donc :

[  ]

#### 4. Régime d’accès épistémique

Le régime d’accès épistémique de CKM est expérimentalement indirect.

Les éléments CKM sont extraits de nombreux processus :

[  ]

[  ]

[  ]

[  B ]

[  ]

[  ]

Le PDG indique par exemple que (|V_{ud}|) est déterminé très précisément à partir des transitions nucléaires superpermises (0++), avec :

[ |V_{ud}| = 0{,}97367 00032 ]

et que (|V_{us}|) est extrait notamment des désintégrations semi-leptoniques de kaons avec des facteurs de forme hadroniques.

Le régime d’accès est donc :

[  ]

et non :

[  ]

Le PDG souligne que les éléments CKM les plus précisément déterminés le sont par ajustement global à toutes les mesures disponibles en imposant les contraintes du Modèle standard, notamment l’unitarité à trois générations ; ces ajustements utilisent aussi des prédictions théoriques pour des éléments de matrice hadroniques, parfois avec des incertitudes significatives.

#### 5. Fonction physique

La fonction physique de CKM est d’orienter les transitions faibles entre saveurs de quarks.

Elle ne fixe pas une masse, ni une échelle, ni un couplage global. Elle distribue l’interaction faible chargée entre les différentes générations de quarks.

Les éléments proches de la diagonale sont grands :

[ |V_{ud}|,|V_{cs}|,|V_{tb}| ]

tandis que les transitions entre générations éloignées sont fortement supprimées :

[ |V_{ub}|,|V_{td}| ]

Le fit global cité par le PDG donne une matrice de modules fortement hiérarchisée, par exemple :

[ |V_{}|

]

avec les incertitudes indiquées dans l’ajustement global.

La fonction de CKM est donc :

[  ]

#### 6. Paramétrisation standard

Dans la paramétrisation standard, CKM est écrite comme un produit de trois rotations, avec une phase complexe dans le secteur (1-3) :

[ V_{} = R_{23}({23}) ,U{13}({13},) ,R{12}(_{12}) ]

où :

[ s_{ij}=_{ij} ]

[ c_{ij}=_{ij} ]

La phase () est responsable des phénomènes de violation CP dans les processus de changement de saveur du Modèle standard.

Le PDG donne, dans son fit global :

[ _{12}=0{,}2250100068 ]

[ {13}=0{,}003732^{+0{,}000090}{-0{,}000085} ]

[ {23}=0{,}04183^{+0{,}00079}{-0{,}00069} ]

[ 147026 ]

La hiérarchie est donc très marquée :

[ s_{13}s_{23}s_{12} ]

et le PDG souligne que cette hiérarchie motive l’usage de la paramétrisation de Wolfenstein.

#### 7. Paramétrisation de Wolfenstein

La paramétrisation de Wolfenstein rend visible la hiérarchie de CKM à partir de quatre paramètres :

[ ,A,{},{} ]

avec :

[ s_{12}= ]

[ s_{23}=A^2 ]

[ s_{13}e{i}=A3(+i) ]

Le PDG donne, dans son fit global :

[ 2250100068 ]

[ A=0{,}826^{+0{,}016}_{-0{,}015} ]

[ {}=0{,}15910094 ]

[ {}=0{,}3523^{+0{,}0073}_{-0{,}0071} ]

et précise que différentes approches d’ajustement global, notamment CKMfitter et UTfit, donnent des résultats désormais très proches.

Cette paramétrisation est importante pour notre grille : elle montre que CKM n’est pas seulement une matrice de mélange ; c’est une structure hiérarchique de mélange.

#### 8. Violation CP

CKM contient une phase complexe qui rend possible la violation CP dans le secteur quark.

Cette violation CP est mesurée par des observables comme :

[  ]

dans les désintégrations de mésons (B), par les angles du triangle d’unitarité, par les observables kaoniques comme (_K), et par plusieurs processus de saveur.

Le PDG donne par exemple :

[ = 0{,}709011 ]

pour la moyenne mondiale correspondante.

L’invariant de Jarlskog associé à CKM mesure la violation CP de manière indépendante des conventions de phase. Le PDG donne :

[ J = 3{,}12^{+0{,}13}_{-0{,}12}^{-5} ]

dans le fit global.

Ce point confirme que la phase CKM ne doit pas être traitée comme une simple décoration mathématique : elle a des effets physiques observables.

#### 9. Unitarité et tensions

Dans le Modèle standard à trois générations, CKM est unitaire. L’unitarité impose des relations entre les lignes et les colonnes de la matrice.

Le PDG indique que les tests d’unitarité donnent notamment :

[ |V_{ud}|2+|V_{us}|2+|V_{ub}|^2 = 0{,}99840007 ]

pour la première ligne, avec une tension de (2{,}3) liée notamment à la diminution récente de la valeur de (|V_{ud}|).

Il faut donc distinguer deux niveaux.

Au niveau théorique du Modèle standard :

[ V_{}  ]

Au niveau expérimental :

[  ]

Cette distinction est importante pour notre méthode : l’unitarité est une contrainte structurelle du modèle, mais sa vérification empirique passe par des protocoles et des corrections très spécifiques.

#### 10. Différence avec PMNS

CKM teste directement la compression de la famille “Orientation”.

Avec PMNS, les angles et phases apparaissaient dans un régime oscillatoire : les neutrinos sont produits dans une saveur, se propagent comme superpositions d’états de masse, puis sont détectés dans une saveur.

Avec CKM, il n’y a pas d’oscillation libre analogue des quarks. Les quarks sont confinés dans des hadrons, et le mélange se manifeste dans les amplitudes de transitions faibles et dans les désintégrations.

La catégorie générale ne doit donc pas être :

[  ]

mais :

[  ]

Les oscillations neutrino deviennent un sous-type local de l’orientation quantique, non la famille générale.

#### 11. Ce que CKM ne dit pas

CKM ne donne pas l’origine profonde des masses et mélanges des quarks. Dans le Modèle standard, les matrices de Yukawa sont des paramètres. CKM résulte de leur diagonalisation, mais le Modèle standard n’explique pas pourquoi les angles et la phase ont les valeurs observées.

CKM ne décrit pas non plus toute la physique de la saveur. Les observables mesurées dépendent de facteurs de forme, d’éléments de matrice hadroniques, de corrections radiatives et parfois de calculs QCD non perturbatifs.

CKM ne doit donc pas être confondu avec les observables de désintégration elles-mêmes. Elle est une structure reconstruite à partir d’un ensemble d’observables.

Enfin, CKM n’est pas une constante conventionnelle au sens du SI. Elle n’est pas fixée par définition ; elle est reconstruite expérimentalement dans le cadre du Modèle standard.

#### 12. Lecture par la matrice v0.2

| Critère | Lecture pour CKM |
|---|---|
| Grandeur | Matrice CKM (V_{}) |
| Type logique | Matrice unitaire complexe sans dimension |
| Dimension | Sans dimension |
| Régime de définition physique | Régime électrofaible brisé ; diagonalisation des Yukawa quark ; courants faibles chargés |
| Régime d’accès épistémique | Reconstruction multi-processus : désintégrations faibles, oscillations de mésons, violation CP, fits globaux |
| Fonction | Orienter et hiérarchiser les transitions faibles entre saveurs de quarks |
| Dépendance d’échelle | Les éléments CKM sont traités comme constantes dans le SM ; les extractions dépendent de corrections, schémas et éléments hadroniques |
| Stabilisation empirique | Globalement forte, mais avec tensions locales, notamment sur l’unitarité de première ligne |
| Stabilisation conventionnelle | Non concernée |
| Limites | N’explique pas l’origine des Yukawa ; reconstruction indirecte ; dépend de calculs hadroniques |
| Famille fonctionnelle | Orientation |
| Sous-type | Orientation de saveur dans les courants faibles chargés |

#### 13. Catégorie proposée

CKM doit être classée dans la famille supérieure :

[  ]

et non dans une famille nouvelle.

Sous-type proposé :

[  ]

Définition provisoire :

Une constante matricielle d’orientation de saveur est une structure sans dimension qui fixe la manière dont les états de masse et les états d’interaction faible se désalignent, et qui distribue les amplitudes de transition entre générations.

Ce sous-type peut accueillir CKM et, avec prudence, PMNS, mais sous des régimes d’accès différents :

[  ]

[  ]

#### 14. Formulation provisoire

La matrice CKM peut être comprise comme une constante effective stabilisée d’orientation de saveur dans le secteur quark. Sa fonction n’est pas de fixer une échelle ou une intensité globale, mais de distribuer les transitions faibles chargées entre générations de quarks selon une structure unitaire, hiérarchique et complexe.

La question pertinente devient :

À quelles conditions la matrice CKM peut-elle être traitée comme constante stabilisée, alors qu’elle est reconstruite indirectement à partir de désintégrations faibles, de phénomènes de mélange mésonique et d’observables de violation CP, plutôt que mesurée comme une grandeur isolée ?

#### 15. Fonction dans l’enquête générale

Cette fiche réussit le premier test du cycle CKM.

Elle montre que la famille “Orientation” peut être généralisée au-delà des oscillations neutrino. CKM confirme que l’orientation entre bases physiques peut être une fonction de constance indépendante du régime oscillatoire.

Le résultat taxonomique est donc :

[  ]

est une famille supérieure valide,

tandis que :

[  ]

est un régime d’accès et de manifestation propre au secteur neutrino, non une famille générale.

La prochaine fiche naturelle devra porter sur les paramètres CKM eux-mêmes :

[ {12}{q},{23}^{q},{13}{q},{} ]

ou, de manière plus compacte, sur les paramètres de Wolfenstein :

[ ,A,{},{} ]

Le choix le plus utile pour la taxonomie sera probablement la fiche Wolfenstein, car elle teste la hiérarchie interne du mélange CKM sans créer une catégorie par angle.
