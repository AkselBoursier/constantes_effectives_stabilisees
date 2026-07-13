# Source DOCX - Cycle_effectif_basse_energie_v0_3

## Statut

```text
lot: 3 - sources d'architecture
source physique: Cycle effectif basse énergie v0.3.docx
statut: extraction textuelle de travail
document actif concerne: Architecture effective basse energie
controle attendu: Extraction + comparaison
```

## Limite

```text
Cette extraction ne remplace pas le DOCX source.
Elle rend la matiere lisible en Markdown pour comparaison et integration.
La mise en page Word n'est pas reconstruite.
```

## Avertissement d'extraction

> Ce fichier contient des placeholders `[  ]` (et variants comme `[ X= ]`) correspondant
> a des passages incomplets dans le DOCX source : formules non rendues, tableaux mal convertis,
> elements graphiques ou equations complexes.
> Ne pas interpreter ces placeholders comme du contenu valide.
> Verifier le DOCX source avant toute reprise scientifique.
> Convention : [CONVENTION_PLACEHOLDERS.md](../../CONVENTION_PLACEHOLDERS.md)

## Extraction

### Cycle effectif basse énergie v0.3

#### Fiche 3 : (s(Q^2)) et ({})

#### 1. Fonction de la fiche

Les deux fiches précédentes ont testé le cas faible :

[ G_F ]

comme coefficient de raccordement effectif,

et :

[ M_W ]

comme échelle de validité de la théorie de Fermi.

Le cas QCD est différent.

Il ne s’agit pas seulement d’une interaction médiée par une particule massive que l’on intégrerait à basse énergie. Il s’agit d’une théorie de jauge non abélienne dont le couplage varie avec l’échelle et produit une séparation de régimes :

[  ]

[  ]

La question directrice devient donc :

[  ]

Le couple :

[ s(Q^2),{} ]

teste une autre forme d’effectivité : non plus seulement le raccordement entre théorie de Fermi et théorie électrofaible, mais l’articulation entre couplage courant, échelle dynamique et changement de régime.

#### 2. Identification

Grandeurs :

[ _s(Q^2) ]

[ _{} ]

Noms :

[  ]

[  ]

Types logiques :

[ _s(Q^2) :  ]

[ _{} :  ]

Familles principales :

[ _s(Q^2) :  ]

[ _{} :  ]

Sous-types :

[ _s(Q^2) :  ]

[ _{} :  ]

Fonctions transversales :

[  ]

[  ]

[  ]

Architecture :

[  ]

#### 3. Régime de définition physique

QCD est la théorie de jauge des interactions fortes, associée au groupe :

[ SU(3) ]

Son couplage est généralement noté :

[ g_s ]

ou :

[ _s= ]

Le PDG décrit (_s) comme le paramètre fondamental de QCD, en dehors des masses de quarks, et rappelle que les quarks et les gluons ne sont pas observés comme particules libres : les hadrons sont des combinaisons singlets de couleur.

Le régime physique de (_s(Q^2)) n’est donc pas un régime unique. La même théorie présente deux comportements :

[  ]

[  ]

Cette dualité de régime est au cœur de la fiche.

#### 4. Régime d’accès épistémique

Le régime d’accès de (_s) est multiple.

On ne mesure pas (_s) comme une valeur unique détachée de tout contexte. On l’extrait de nombreux processus, puis on la ramène généralement à une échelle de référence, typiquement :

[ M_Z ]

Le PDG 2025 donne comme moyenne mondiale :

[ _s(M_Z^2)=0.1180 ]

et souligne que cette moyenne combine plusieurs sous-domaines expérimentaux et théoriques.

Cela montre immédiatement que le régime d’accès est composite :

[  ]

[  ]

[  ]

[  ]

[  ]

[  ]

La valeur de référence à (M_Z) n’est donc pas “la” valeur naturelle du couplage fort. C’est une convention de comparaison physique et phénoménologique.

#### 5. (_s(Q^2)) comme couplage courant

La fonction principale de :

[ _s(Q^2) ]

est de paramétrer l’intensité effective de l’interaction forte à une échelle donnée.

Dans la QCD perturbative, les prédictions s’expriment en termes d’un couplage renormalisé :

[ _s(_R^2) ]

où (_R) est une échelle de renormalisation. Lorsque (_R) est choisi proche du transfert d’impulsion (Q), (_s(_R2Q2)) indique la force effective de l’interaction forte dans le processus considéré.

La famille principale est donc :

[  ]

Sous-type :

[  ]

Formulation :

**(_s(Q^2)) est une constante seulement au sens local : elle est stabilisée à une échelle donnée, dans un schéma donné, pour un régime de processus donné.**

Ce point est important pour la notion de constante effective stabilisée. Ici, la constance n’est pas l’absence de variation. Elle est la comparabilité contrôlée d’un couplage qui varie.

#### 6. Liberté asymptotique

La fonction bêta de QCD porte un signe qui produit la liberté asymptotique : le couplage fort devient faible à grand transfert d’impulsion. Le PDG indique qu’autour de (0.1) à (1 ), (_s) est de l’ordre de (0.1), tandis que la théorie devient fortement couplée autour et au-dessous de (1 ).

La structure est donc :

[ Q   _s(Q^2)    ]

[ Q   _s(Q^2)    ]

Ce n’est pas une simple dépendance paramétrique. C’est un changement de régime.

La fonction transversale associée est :

[  ]

car la valeur du couplage indique le domaine où certaines méthodes restent applicables.

#### 7. (_{}) comme échelle dynamique

Dans une approximation simple de l’équation du groupe de renormalisation, une constante :

[  ]

apparaît comme constante d’intégration. Elle correspond à l’échelle où le couplage défini perturbativement divergerait. Le PDG précise que cette valeur indique la région d’énergie où dominent les dynamiques non perturbatives. Il rappelle aussi qu’en pratique, il est devenu standard de citer (_s) à une échelle donnée, typiquement (M_Z), plutôt que de citer directement (), parce que la signification de () dépend de la manière de résoudre ou d’approximer l’équation de renormalisation.

La famille principale de :

[ _{} ]

est donc :

[  ]

Sous-type :

[  ]

Formulation :

**(_{}) n’est pas une masse de particule ; c’est une échelle produite par le flot du couplage fort.**

Elle condense la transition entre un régime où les degrés de liberté partoniques et les méthodes perturbatives sont adaptés, et un régime où les degrés de liberté hadroniques et les méthodes non perturbatives deviennent nécessaires.

#### 8. Fonction seuil de (_{})

(_{}) joue aussi une fonction seuil.

Elle marque approximativement :

[  ]

[  ]

[  ]

Mais ce seuil n’est pas une frontière nette. Ce n’est pas une porte mathématique à une valeur unique. C’est une région de changement de régime.

La classification correcte est donc :

[ _{} :  ]

avec :

[  ]

Formulation :

**(_{}) est d’abord une échelle dynamique ; elle devient seuil lorsqu’elle sert à marquer le passage vers le régime non perturbatif.**

Ce résultat confirme la rétrogradation de Seuil : le seuil est un rôle, non une famille.

#### 9. Différence avec (M_W)

Le contraste avec (M_W) est instructif.

Dans le cas faible :

[ M_W ]

est la masse d’un médiateur massif. À basse énergie, l’échange du boson (W) est remplacé par un coefficient local :

[ G_F ]

Dans le cas QCD :

[ _{} ]

n’est pas la masse d’un médiateur que l’on intègre. Elle est une échelle générée par le flot du couplage.

La structure faible est :

[    ]

La structure QCD est :

[      ]

Cela montre que l’architecture effective basse énergie ne se réduit pas à l’intégration d’une particule massive.

#### 10. Raccordement ou non ?

Le cas QCD oblige à préciser la famille Raccordement.

[ G_F ]

est un raccordement clair : il relie la théorie de Fermi à la théorie électrofaible.

[ _s(Q^2) ]

n’est pas un raccordement. C’est un couplage courant.

[ _{} ]

n’est pas non plus un raccordement. C’est une échelle dynamique.

Cependant, le couple :

[ s(Q^2),{} ]

participe à une architecture effective, parce qu’il organise le passage entre descriptions :

[  ]

[  ]

[  ]

[  ]

Le raccordement n’est donc pas ici porté par une seule constante. Il est architectural.

Formulation :

Dans le cas QCD, l’effectivité n’est pas concentrée dans un coefficient de raccordement unique ; elle est distribuée entre un couplage courant, une échelle dynamique et des méthodes de description adaptées au régime.

#### 11. Régime basse énergie en QCD

L’expression “basse énergie” n’a pas le même sens en QCD que dans la théorie de Fermi.

Dans le cas de Fermi, basse énergie signifie :

[ EM_W ]

et la description devient plus simple : une interaction locale.

Dans le cas de QCD, basse énergie signifie plutôt :

[ Q_{} ]

et la description devient plus difficile : le couplage devient fort, la perturbation échoue, le confinement impose des degrés de liberté hadroniques.

Donc :

[  =  ]

[  =  ]

Ce contraste est important. Il empêche de définir l’architecture effective basse énergie comme simple réduction de complexité.

Formulation :

Le régime effectif basse énergie peut simplifier une description, mais il peut aussi signaler l’entrée dans un domaine où la description perturbative cesse d’être suffisante.

#### 12. Fonction de validité

Dans cette fiche, la fonction de validité est centrale.

[ _s(Q^2) ]

indique la force effective du couplage à l’échelle considérée.

[ _{} ]

indique la région où la dynamique non perturbative domine.

Ensemble, ils permettent de cartographier la validité relative des descriptions :

[ Q_{} ]

description perturbative adaptée,

[ Q_{} ]

régime de transition,

[ Q_{} ]

description non perturbative ou hadronique nécessaire.

La fonction transversale :

[  ]

est donc confirmée.

#### 13. Fonction de hiérarchie

Le couple :

[ s(Q^2),{} ]

stabilise aussi une hiérarchie de régimes.

Il distingue :

[  ]

[  ]

[  ]

d’un côté,

et :

[  ]

[  ]

[  ]

de l’autre.

La fonction hiérarchique est donc :

[  ]

et non seulement :

[  ]

Cela enrichit la fonction transversale Hiérarchie.

#### 14. Stabilisation empirique

(_s) est fortement stabilisée comme couplage courant de QCD, mais sa stabilisation passe par des déterminations multiples, dépendantes des observables, des ordres perturbatifs, des incertitudes théoriques et des évolutions vers une échelle commune.

La moyenne mondiale à (M_Z) donne une valeur très précise :

[ _s(M_Z^2)=0.1180 ]

mais cette précision repose sur la cohérence de nombreux domaines et sur une comparaison par évolution de renormalisation.

(_{}), en revanche, est plus délicate à citer comme valeur unique, parce que sa signification dépend du schéma, du nombre de saveurs actives et de la méthode utilisée pour résoudre l’équation de renormalisation. C’est pourquoi la pratique standard privilégie souvent la citation de (_s) à une échelle de référence.

Stabilisation :

[ _s(M_Z^2) :  ]

[ _{} :  ]

#### 15. Stabilisation conventionnelle

Ni :

[ _s(Q^2) ]

ni :

[ _{} ]

ne sont des constantes définissantes du SI.

Elles ne sont pas fixées par convention métrologique.

Stabilisation conventionnelle :

[  ]

Elles relèvent d’une stabilisation théorique, phénoménologique et expérimentale, non d’une exactitude conventionnelle.

#### 16. Lecture par la matrice v0.8

| Critère | Lecture pour (_s(Q^2)) | Lecture pour (_{}) |
|---|---|---|
| Grandeur | (_s(Q^2)) | (_{}) |
| Type logique | Couplage sans dimension dépendant de l’échelle | Échelle dynamique dimensionnée |
| Dimension | Sans dimension | ([E]) |
| Famille principale | Couplage | Échelle |
| Sous-type local | Couplage courant | Échelle dynamique |
| Fonction transversale | Validité, hiérarchie | Seuil, validité, hiérarchie |
| Régime de définition physique | QCD perturbative selon l’échelle | Régime QCD, transition perturbatif/non perturbatif |
| Régime d’accès épistémique | Extractions multi-processus, évolution RG, valeur de référence à (M_Z) | Définition par RG, schéma, nombre de saveurs, relation à (_s) |
| Dépendance d’échelle | Essentielle | Schéma-dépendante |
| Stabilisation empirique | Forte globale à (M_Z) | Indirecte / schéma-dépendante |
| Stabilisation conventionnelle | Non concernée | Non concernée |
| Architecture | Effective basse énergie / QCD | Effective basse énergie / QCD |
| Limite | N’est pas constante hors échelle | N’est pas un seuil net ni une masse de particule |

#### 17. Ce que le cas QCD confirme

Le cas :

[ s(Q^2),{} ]

confirme que l’architecture effective basse énergie doit être élargie.

Après (G_F/M_W), elle pouvait encore sembler centrée sur :

[

]

Avec QCD, elle devient :

[

]

Le cas QCD confirme donc l’architecture, mais en la transformant.

Formule enrichie :

[  =

]

#### 18. Ce que le cas QCD corrige

Le cas QCD corrige une vision trop simple de l’effectivité.

Dans le cas faible, le régime basse énergie permet de simplifier :

[ W   G_F ]

Dans le cas QCD, le régime basse énergie rend la description perturbative insuffisante :

[ _s    ]

Il ne faut donc pas identifier :

[  ]

avec :

[  ]

La bonne formulation est :

Une description effective est adaptée à un régime ; elle peut être plus simple formellement ou plus complexe dynamiquement selon les degrés de liberté pertinents.

#### 19. Décision provisoire après QCD

Après :

[ G_F ]

[ M_W ]

[ s(Q^2),{} ]

l’architecture effective basse énergie est nettement renforcée.

Elle ne repose plus sur un seul type de cas.

Elle inclut désormais deux formes d’effectivité :

[  ]

et :

[  ]

La première est illustrée par :

[ G_F/M_W ]

La seconde par :

[ s/{} ]

La formulation provisoire devient :

Une architecture effective basse énergie stabilise les grandeurs qui permettent de décrire ce qu’un régime donné rend accessible, intégrable, courant, non résolu ou non perturbatif.

#### 20. Prochaine fiche du cycle

La prochaine fiche doit porter sur :

[ G(E),M{} ]

Ce cas testera une troisième forme d’effectivité :

[  ]

et :

[  ]

La question deviendra :

[  ]
