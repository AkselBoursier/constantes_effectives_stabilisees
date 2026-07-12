# Refondation du domaine

## 1. Statut du document

Ce document ouvre une refondation du projet.

Il ne supprime pas le corpus antérieur. Il suspend provisoirement l’autorité de ses taxonomies, architectures et trajectoires afin de resserrer l’objet étudié et de rendre le cadre réellement discriminant.

La question n’est plus de savoir comment intégrer toutes les formes de stabilisation rencontrées en physique. Elle devient :

> Dans quelles conditions précises le qualificatif de constante est-il légitime pour une grandeur physique ?

## 2. Motif du resserrement

Le cadre antérieur pouvait accueillir des objets trop hétérogènes : constantes, paramètres d’état, conditions initiales, observables reconstruites, bornes et tensions de données.

Cette extension affaiblissait son pouvoir d’exclusion. Un cadre qui peut qualifier presque tout ne distingue plus suffisamment ce qui relève réellement de la constance.

La refondation impose donc une règle :

> Le projet doit pouvoir refuser le statut de constante effective stabilisée à certains objets.

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

Le mot `stabilisée` désigne alors le résultat d’un test. Il ne sert plus à définir circulairement la stabilisation.

## 4. Critère d’entrée dans le domaine principal

Une grandeur entre dans le domaine principal seulement si elle est candidate à l’un des statuts suivants :

- invariance physique dans un régime spécifié ;
- coefficient traité comme fixe dans une approximation effective contrôlée ;
- valeur fixée par définition dans un système métrologique ;
- paramètre dont la robustesse inférentielle peut être comparée à un statut physique sans lui être assimilée.

Une grandeur n’entre pas dans le domaine principal uniquement parce qu’elle est mesurée avec précision, reconstruite de manière stable ou soumise à une borne robuste.

## 5. Quatre statuts à distinguer

### 5.1 Constance physique

La grandeur est invariante, ou supposée telle, relativement à des transformations physiques déclarées dans un domaine donné.

### 5.2 Constance effective

La grandeur peut être traitée comme un coefficient fixe dans un régime où les dépendances ou corrections négligées restent sous contrôle.

### 5.3 Constance métrologique

La valeur numérique de la grandeur est fixée exactement par définition dans un système d’unités. Cette exactitude ne constitue ni une mesure parfaite ni une explication physique.

### 5.4 Robustesse inférentielle

Une estimation reste stable entre plusieurs analyses, modèles, jeux de données ou procédures. Ce statut est épistémique et auxiliaire. Il ne suffit pas à établir une constance physique.

## 6. Objets exclus du noyau

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

## 7. Cinq cas sentinelles

| Cas | Décision provisoire | Fonction du test |
|---|---|---|
| `G_F` | Admis comme constante effective dans le régime basse énergie | Tester la constance locale d’un coefficient effectif |
| `h` dans le SI | Admis comme constante métrologique ; rôle physique à distinguer | Tester l’exactitude définitionnelle |
| `alpha_s(Q)` | Refusé comme constante simpliciter ; valeur spécifiable à une échelle donnée | Tester la dépendance explicite à l’échelle |
| `H_0` | Exclu du noyau comme paramètre d’état actuel ; robustesse inférentielle analysable | Tester la différence entre paramètre et constante |
| borne sur la masse des neutrinos | Refusée comme constante | Tester la différence entre grandeur et état de connaissance |

Le cadre n’est considéré comme discriminant que s’il maintient ces différences sans les réabsorber dans une catégorie plus large.

## 8. Conditions d’échec du cadre

Le cadre échoue si :

1. il ne peut pas spécifier le régime, les transformations ou la tolérance pertinentes ;
2. il confond stabilité de la grandeur et robustesse de son estimation ;
3. il transforme une borne ou une tension en propriété de constance ;
4. il ne distingue pas une constante d’un paramètre simplement fixé dans un modèle ;
5. il admet tous les cas examinés ;
6. sa décision dépend uniquement de son propre vocabulaire interne ;
7. un changement arbitraire de paramétrisation suffit à créer ou supprimer le statut sans contenu invariant identifiable.

## 9. Effet sur le corpus antérieur

Sont provisoirement suspendus comme principes directeurs :

- les familles fonctionnelles ;
- les architectures inter-familles ;
- la théorie générale des trajectoires de stabilisation ;
- l’extension des modes de constance aux bornes et reconstructions.

Ces éléments ne sont pas invalidés. Ils sont rétrogradés au rang de matériaux historiques ou d’hypothèses à réintroduire seulement si les tests minimaux en montrent la nécessité.

## 10. Prochaine étape

La prochaine étape consiste à appliquer le critère provisoire aux cinq cas sentinelles, avec pour chacun :

```text
objet exact
régime
transformations pertinentes
tolérance ou niveau de contrôle
statut admis ou refusé
justification physique
statut de l’accès
condition d’échec
```

Aucune nouvelle taxonomie ne doit être créée avant la clôture de ce test.

## 11. Formule de clôture

> Le projet n’étudie plus toute stabilisation scientifique. Il étudie les conditions sous lesquelles une grandeur peut légitimement être tenue pour constante, et les conditions sous lesquelles ce qualificatif doit être refusé.
