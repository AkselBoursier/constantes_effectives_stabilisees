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

> Que devient la description d’un domaine physique lorsque les constantes ne sont plus présentées comme des valeurs isolées, mais comme des éléments exerçant des fonctions de fixité différenciées entre des états, processus, secteurs ou descriptions ?

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

> « Constante physique » ne désigne peut-être pas une espèce naturelle unique, mais une fonction de fixité tenue par différents types d’objets dans différentes architectures théoriques et dans différentes relations.

Après le pilote Higgs–Yukawa, une fonction de fixité désigne provisoirement :

> le rôle local par lequel un objet physiquement ou formellement déterminé maintient une relation stable entre des états, processus, secteurs ou descriptions, dans un régime et sous des transformations explicités.

Cette hypothèse ne doit pas devenir une nouvelle définition absorbante. Elle doit permettre des distinctions, des refus et des cas d’échec.

Le pilote a aussi montré qu’une fonction n’est pas un type ontologique : le même objet peut exercer plusieurs fonctions selon le régime et la question posée.

## 5. Critère d’entrée révisé

Une grandeur entre dans le noyau seulement si elle est candidate à l’un des trois statuts suivants :

1. invariance physique dans un régime et sous des transformations spécifiés ;
2. coefficient traité comme fixe dans une approximation effective contrôlée ;
3. valeur numérique fixée par définition dans une architecture métrologique, avec distinction du rôle physique.

Une grandeur n’entre pas dans le noyau uniquement parce qu’elle est mesurée avec précision, reconstruite de manière stable ou soumise à une borne robuste.

## 6. Trois statuts de constance et un axe auxiliaire

### 6.1 Constance physique

La grandeur est invariante, ou supposée telle, relativement à des transformations physiques déclarées dans un domaine donné.

### 6.2 Constance effective

La grandeur peut être traitée comme un coefficient fixe dans un régime où les dépendances ou corrections négligées restent sous contrôle.

### 6.3 Constance métrologique

La valeur numérique de la grandeur est fixée exactement par définition dans un système d’unités. Cette exactitude ne constitue ni une mesure parfaite ni une explication physique.

### 6.4 Robustesse inférentielle — axe transversal

Une estimation, une attribution ou une contrainte peut rester stable entre plusieurs analyses, modèles, jeux de données ou procédures.

Le test des cas sentinelles a établi que cette robustesse n’est pas un quatrième statut de constance. Elle porte sur la solidité de l’accès ou de l’inférence.

```text
robustesse de l’estimation
≠
constance de l’objet
```

## 7. Objets exclus du noyau

Les objets suivants ne sont pas traités comme des modes de constance :

- tension de données ;
- borne expérimentale ou observationnelle ;
- intervalle admissible ;
- observable reconstruite en tant que telle ;
- condition initiale en tant que telle ;
- paramètre d’état explicitement dépendant du temps ;
- fonction explicitement dépendante de l’échelle prise dans sa totalité ;
- paramètre de nuisance ou artefact de paramétrisation ;
- coordonnée conventionnelle dépourvue d’un invariant physique identifié.

Ils peuvent intervenir comme accès, contraintes, comparateurs ou contre-exemples.

## 8. Résultats des deux protocoles minimaux

### 8.1 Test discriminant par cas sentinelles

Document actif :

```text
01_CADRE_METHODOLOGIQUE/test-cas-sentinelles.md
```

Résultat :

| Cas | Décision |
|---|---|
| `G_F` | admis comme constante effective dans le régime basse énergie |
| `h` dans le SI | admis comme constante métrologique définissante |
| `alpha_s(mu)` | refusé comme constante simpliciter |
| `H_0` | refusé du noyau comme paramètre d’état actuel |
| borne sur la masse des neutrinos | refusée comme constante |

```text
2 admissions relatives
3 refus comme constantes simpliciter
```

Le test confirme un pouvoir d’exclusion minimal et sépare définitivement la robustesse inférentielle du statut physique de l’objet.

### 8.2 Dossier pilote relationnel Higgs–Yukawa

Documents actifs :

```text
02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/architecture-relationnelle-higgs-yukawa.md
02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/verification-physique-higgs-yukawa.md
02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/evaluation-gain-explicatif-higgs-yukawa.md
```

Résultat :

```text
Pilote concluant sous conditions.
```

Le pilote a distingué :

- constitution théorique ;
- histoire thermique ;
- opérations de diagonalisation et de représentation ;
- voies d’accès expérimentales et inférentielles ;
- fonctions locales de `v`, des Yukawa, des masses, de CKM et de `G_F` ;
- limites explicatives du Modèle standard.

Il a produit des contrefactuels et montré que le gain le plus robuste réside dans les relations typées et dans la localisation des arrêts de l’explication, non dans la création d’une nouvelle taxonomie.

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
9. un paramètre libre est présenté comme expliqué parce qu’il intervient dans un mécanisme ;
10. une fonction locale est confondue avec le type ontologique de son porteur.

## 10. Effet sur le corpus antérieur

Sont provisoirement suspendus comme principes directeurs :

- les familles fonctionnelles ;
- les architectures inter-familles déclarées confirmées par les seuls tests de retrait ;
- la théorie générale des trajectoires de stabilisation ;
- l’extension des modes de constance aux bornes et reconstructions.

Ces éléments ne sont pas invalidés en bloc. Ils sont rétrogradés au rang de matériaux historiques ou d’hypothèses à réintroduire seulement si les tests en montrent la nécessité.

Les relations physiques, sources, distinctions de régime, voies d’accès et limites explicatives déjà documentées restent pleinement réutilisables après contrôle.

## 11. Critères de transfert aux autres cycles

Une extension est admise seulement si le cycle suivant permet :

1. d’identifier au moins deux chaînes auparavant confondues ;
2. de typer les relations sans les transformer en nouvelles familles automatiques ;
3. de produire au moins un contrefactuel ;
4. de distinguer ce qui est expliqué, inféré, défini ou simplement paramétré ;
5. de fournir un cas où le qualificatif de constante doit être refusé ;
6. de montrer un gain qui ne dépend pas du vocabulaire propre au projet.

## 12. Ordre de travail actuel

Les étapes minimales de la refondation sont closes :

```text
[x] extraction et requalification du corpus Saveur–Higgs
[x] correction des chaînes physiques
[x] vérification externe ciblée
[x] évaluation du gain explicatif
[x] test des cinq cas sentinelles
```

L’ordre de transfert est désormais :

```text
1. cycle effectif basse énergie ;
2. cycle métrologique SI comme cas contrasté ;
3. cosmologie seulement après ces deux tests.
```

Aucune nouvelle taxonomie générale ne doit être créée pendant ce transfert.

## 13. Formule de clôture

> Le projet prend la question « qu’est-ce qu’une constante physique ? » comme une instruction d’enquête. Il cherche à distinguer les formes de fixité, les objets qui les portent, les relations qu’elles maintiennent, les régimes dans lesquels elles opèrent, les voies par lesquelles nous y accédons et les limites de ce qu’elles permettent d’expliquer.
