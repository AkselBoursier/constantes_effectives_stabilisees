# Refondation du domaine

## 1. Statut du document

Ce document ouvre une refondation du projet.

Il ne supprime pas le corpus antérieur. Il suspend provisoirement l’autorité de ses taxonomies, architectures et trajectoires afin de resserrer l’objet étudié et de rendre le cadre réellement discriminant.

La question directrice redevient la question première :

> Qu’est-ce qu’une constante physique ?

Cette question n’est pas posée dans l’attente nécessaire d’une définition ontologique unique. Elle sert d’instruction d’enquête pour distinguer les objets, les fonctions de fixité, les processus, les régimes et les voies d’accès que le vocabulaire ordinaire de la constance tend à réunir.

Une première question méthodologique lui est subordonnée :

> Dans quelles conditions précises le qualificatif de constante est-il légitime pour une grandeur physique ?

Une seconde question porte sur l’architecture des processus :

> Que devient la description d’un domaine physique lorsque les constantes ne sont plus présentées comme des valeurs isolées, mais comme des éléments exerçant des fonctions de fixité différenciées entre des processus ?

## 2. Motif du resserrement

Le cadre antérieur pouvait accueillir des objets trop hétérogènes : constantes, paramètres d’état, conditions initiales, observables reconstruites, bornes et tensions de données.

Cette extension affaiblissait son pouvoir d’exclusion. Un cadre qui peut qualifier presque tout ne distingue plus suffisamment ce qui relève réellement de la constance.

La refondation impose donc une règle :

> Le projet doit pouvoir refuser le statut de constante à certains objets et refuser le statut d’explication à certaines descriptions relationnelles.

## 3. Critère provisoire de constance

Une grandeur `g` peut recevoir un statut de constance relativement à un régime `R` lorsque :

1. les transformations ou variables pertinentes `T` sont explicitement spécifiées ;
2. la variation de `g` sous ces transformations est nulle ou inférieure à un seuil déclaré `epsilon` ;
3. le domaine de validité de cette attribution est explicite ;
4. le mode d’accès justifie l’attribution sans être confondu avec la propriété physique elle-même.

Notation de travail :

```text
C(g | R, T, epsilon)
```

Cette notation signifie : `g` est tenue pour constante dans le régime `R`, relativement aux transformations `T`, à la précision ou tolérance `epsilon`.

Le mot `stabilisée` désigne alors le résultat éventuel d’un test. Il ne sert plus à définir circulairement la stabilisation.

## 4. Hypothèse de fonction de fixité

Le projet examine l’hypothèse suivante :

> « Constante physique » ne désigne peut-être pas une espèce naturelle unique, mais une fonction de fixité tenue par différents types d’objets dans différentes architectures théoriques et dans différentes relations entre processus.

Une fonction de fixité désigne provisoirement le rôle par lequel une grandeur, un coefficient ou une structure maintient déterminée une relation dans un régime donné.

Cette hypothèse ne doit pas devenir une nouvelle définition absorbante. Elle doit permettre des distinctions, des refus et des cas d’échec.

## 5. Critère d’entrée dans le domaine principal

Une grandeur entre dans le domaine principal seulement si elle est candidate à l’un des statuts suivants :

- invariance physique dans un régime spécifié ;
- coefficient traité comme fixe dans une approximation effective contrôlée ;
- valeur fixée par définition dans un système métrologique ;
- paramètre dont la robustesse inférentielle peut être comparée à un statut physique sans lui être assimilée.

Une grandeur n’entre pas dans le domaine principal uniquement parce qu’elle est mesurée avec précision, reconstruite de manière stable ou soumise à une borne robuste.

## 6. Quatre statuts à distinguer

### 6.1 Constance physique

La grandeur est invariante, ou supposée telle, relativement à des transformations physiques déclarées dans un domaine donné.

### 6.2 Constance effective

La grandeur peut être traitée comme un coefficient fixe dans un régime où les dépendances ou corrections négligées restent sous contrôle.

### 6.3 Constance métrologique

La valeur numérique de la grandeur est fixée exactement par définition dans un système d’unités. Cette exactitude ne constitue ni une mesure parfaite ni une explication physique.

### 6.4 Robustesse inférentielle

Une estimation reste stable entre plusieurs analyses, modèles, jeux de données ou procédures. Ce statut est épistémique et auxiliaire. Il ne suffit pas à établir une constance physique.

## 7. Objets exclus du noyau

Les objets suivants ne sont plus traités comme des modes de constance :

- tension de données ;
- borne expérimentale ou observationnelle ;
- intervalle admissible ;
- observable reconstruite en tant que telle ;
- condition initiale en tant que telle ;
- paramètre d’état explicitement dépendant du temps ;
- fonction explicitement dépendante de l’échelle prise dans sa totalité ;
- paramètre de nuisance ou artefact de paramétrisation.

Ils peuvent intervenir comme accès, contraintes, comparateurs ou contre-exemples.

## 8. Deux protocoles complémentaires

### 8.1 Test discriminant par cas sentinelles

| Cas | Décision provisoire | Fonction du test |
|---|---|---|
| `G_F` | Admis comme constante effective dans le régime basse énergie | Tester la constance locale d’un coefficient effectif |
| `h` dans le SI | Admis comme constante métrologique ; rôle physique à distinguer | Tester l’exactitude définitionnelle |
| `alpha_s(Q)` | Refusé comme constante simpliciter ; valeur spécifiable à une échelle donnée | Tester la dépendance explicite à l’échelle |
| `H_0` | Exclu du noyau comme paramètre d’état actuel ; robustesse inférentielle analysable | Tester la différence entre paramètre et constante |
| borne sur la masse des neutrinos | Refusée comme constante | Tester la différence entre grandeur et état de connaissance |

Le cadre n’est considéré comme discriminant que s’il maintient ces différences sans les réabsorber dans une catégorie plus large.

### 8.2 Dossier pilote relationnel

Le cycle Saveur–Higgs sert de premier cas expérimental pour tester la description processus à processus.

Document actif :

```text
02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/architecture-relationnelle-higgs-yukawa.md
```

Le pilote doit distinguer au minimum :

- constitution théorique ;
- histoire thermique ;
- opérations de diagonalisation et de représentation ;
- voies d’accès expérimentales et inférentielles ;
- fonctions locales de `v`, des Yukawa, des masses, de CKM et de `G_F` ;
- limites explicatives du Modèle standard.

Il ne sera pas généralisé aux autres cycles avant vérification de son gain explicatif.

## 9. Conditions d’échec du cadre

Le cadre échoue si :

1. il ne peut pas spécifier le régime, les transformations ou la tolérance pertinentes ;
2. il confond stabilité de la grandeur et robustesse de son estimation ;
3. il transforme une borne ou une tension en propriété de constance ;
4. il ne distingue pas une constante d’un paramètre simplement fixé dans un modèle ;
5. il admet tous les cas examinés ;
6. sa décision dépend uniquement de son propre vocabulaire interne ;
7. un changement arbitraire de paramétrisation suffit à créer ou supprimer le statut sans contenu invariant identifiable ;
8. une carte relationnelle ne fait que redessiner des équations connues sans produire de distinction, de dérivation ou de contrefactuel supplémentaire ;
9. un paramètre libre est présenté comme expliqué parce qu’il intervient dans un mécanisme.

## 10. Effet sur le corpus antérieur

Sont provisoirement suspendus comme principes directeurs :

- les familles fonctionnelles ;
- les architectures inter-familles déclarées confirmées par les seuls tests de retrait ;
- la théorie générale des trajectoires de stabilisation ;
- l’extension des modes de constance aux bornes et reconstructions.

Ces éléments ne sont pas invalidés. Ils sont rétrogradés au rang de matériaux historiques ou d’hypothèses à réintroduire seulement si les tests minimaux en montrent la nécessité.

Les relations physiques, sources, distinctions de régime, voies d’accès et limites explicatives déjà documentées restent pleinement réutilisables après contrôle.

## 11. Ordre de travail actuel

Le travail se poursuit dans l’ordre suivant :

1. extraction et requalification du corpus Saveur–Higgs ;
2. correction des chaînes physiques et séparation des temporalités ;
3. vérification externe ciblée des propositions physiques ;
4. évaluation du gain explicatif du pilote ;
5. application complète du test des cas sentinelles ;
6. décision sur l’extension éventuelle aux cycles basse énergie, SI et cosmologie.

Aucune nouvelle taxonomie générale ne doit être créée avant la clôture du pilote et des cas sentinelles.

## 12. Formule de clôture

> Le projet prend la question « qu’est-ce qu’une constante physique ? » comme une instruction d’enquête. Il cherche à distinguer les formes de fixité, les processus qu’elles articulent, les régimes dans lesquels elles opèrent, les voies par lesquelles nous y accédons et les limites de ce qu’elles permettent d’expliquer.
