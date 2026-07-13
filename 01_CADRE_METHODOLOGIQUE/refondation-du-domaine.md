# Refondation du domaine

## Statut

Ce document est le cadre canonique actif de la refondation.

Son historique est désormais porté par Git. Aucun numéro de version n’est ajouté à son nom.

Document de synthèse associé :

- [Synthèse de la refondation des cycles](../05_CARTES_ET_SYNTHESES/synthese-refondation-des-cycles.md)

## 1. Question directrice

> Qu’est-ce qu’une constante physique ?

Cette question n’est pas posée dans l’attente nécessaire d’une définition ontologique unique. Elle sert d’instruction d’enquête pour distinguer :

- les objets ;
- les types de fixité ;
- les transformations pertinentes ;
- les régimes de validité ;
- les voies d’accès ;
- les opérations de représentation, de définition et d’inférence.

## 2. Hypothèse pluraliste

Les tests conduisent à l’hypothèse suivante :

> `Constante physique` fonctionne comme un concept pluraliste à noyau méthodologique, plutôt que comme le nom d’une espèce naturelle unique.

Le noyau commun est :

```text
attribution de fixité
+ objet identifié
+ régime
+ transformations
+ niveau
+ condition de refus.
```

La fonction commune n’implique pas une nature physique commune.

## 3. Critère provisoire

Notation de travail :

```text
C(g | R, T, epsilon)
```

Une grandeur `g` peut recevoir un statut de constance relativement à un régime `R` lorsque :

1. les transformations ou variables pertinentes `T` sont spécifiées ;
2. la variation de `g` est nulle ou inférieure à une tolérance `epsilon` déclarée ;
3. le domaine de validité est explicite ;
4. le mode d’accès est distingué de la propriété physique ;
5. les conventions de schéma, de base, d’échelle, d’époque, de pivot ou d’unités sont indiquées lorsqu’elles sont pertinentes.

Le mot `stabilisée` désigne le résultat éventuel d’un test. Il ne définit pas circulairement la stabilisation.

## 4. Trois statuts de constance

### 4.1 Constance physique

Invariance d’une grandeur ou d’une relation sous des transformations physiques déclarées, dans un domaine donné.

### 4.2 Constance effective

Coefficient traité comme fixe dans une approximation contrôlée, avec corrections et condition de rupture explicites.

### 4.3 Constance métrologique

Valeur numérique fixée exactement dans un système d’unités, sans assimilation à une mesure parfaite ni à une invariance physique démontrée.

## 5. Axes auxiliaires

Les propriétés suivantes ne constituent pas, à elles seules, des statuts de constance physique :

- robustesse inférentielle ;
- stabilité d’une procédure ;
- choix d’une époque de référence ;
- choix d’un pivot ;
- paramètre fixé dans un ajustement ;
- coordonnée choisie dans une représentation ;
- borne ou intervalle stable.

```text
robustesse de l’accès
≠
constance de l’objet.
```

## 6. Fonction de fixité

Une fonction de fixité désigne provisoirement :

> le rôle local par lequel un objet physiquement ou formellement déterminé maintient une relation stable entre des états, processus, secteurs ou descriptions, dans un régime et sous des transformations explicités.

Cette fonction n’est pas un type ontologique.

Le même objet peut exercer plusieurs fonctions, et plusieurs objets physiquement différents peuvent tenir une fonction similaire.

## 7. Objets exclus du noyau

Le qualificatif de constante est refusé ou suspendu pour :

- une fonction variant sous la transformation examinée ;
- une valeur d’état à une époque particulière ;
- une condition initiale en tant que telle ;
- une coordonnée conventionnelle sans invariant identifié ;
- une borne ou un intervalle ;
- une tension entre inférences ;
- une reconstruction dépendante d’un modèle ;
- un coefficient incomplet sans échelle, schéma ou base ;
- un paramètre rendu fixe seulement par procédure ;
- une valeur numérique dont le système d’unités est omis.

## 8. Test des cinq cas sentinelles

Document :

- [Test des cinq cas sentinelles](test-cas-sentinelles.md)

Résultat :

| Cas | Décision |
|---|---|
| `G_F` | admis comme constante effective à basse énergie |
| `h` dans le SI | admis comme constante métrologique définissante |
| `alpha_s(mu)` | refusé comme constante simpliciter |
| `H_0` | refusé comme constante nomologique |
| borne sur la masse des neutrinos | refusée comme constante |

```text
2 admissions relatives
3 refus.
```

## 9. Résultat des cycles

### 9.1 Higgs–Yukawa

- [Dossier central](../02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/architecture-relationnelle-higgs-yukawa.md)
- [Vérification](../02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/verification-physique-higgs-yukawa.md)
- [Évaluation](../02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/evaluation-gain-explicatif-higgs-yukawa.md)

Verdict : architecture physique et représentationnelle confirmée ; famille unique de constantes refusée.

### 9.2 Basse énergie

- [Dossier central](../02_CYCLES_PHYSIQUES/06_Cycle_effectif_basse_energie/architecture-relationnelle-basse-energie.md)
- [Vérification](../02_CYCLES_PHYSIQUES/06_Cycle_effectif_basse_energie/verification-physique-basse-energie.md)
- [Évaluation](../02_CYCLES_PHYSIQUES/06_Cycle_effectif_basse_energie/evaluation-gain-explicatif-basse-energie.md)

Verdict : architecture méthodologique de validité confirmée ; espèce unique de constantes effectives refusée.

### 9.3 SI

- [Dossier central](../02_CYCLES_PHYSIQUES/08_Cycle_metrologique_SI/architecture-relationnelle-metrologique-si.md)
- [Vérification](../02_CYCLES_PHYSIQUES/08_Cycle_metrologique_SI/verification-metrologique-si.md)
- [Évaluation](../02_CYCLES_PHYSIQUES/08_Cycle_metrologique_SI/evaluation-gain-explicatif-metrologique-si.md)

Verdict : architecture définitionnelle confirmée ; homogénéité physique des constantes définissantes refusée.

### 9.4 Cosmologie

- [Dossier central](../02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/architecture-relationnelle-cosmologique.md)
- [Vérification](../02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/verification-physique-cosmologique.md)
- [Évaluation](../02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/evaluation-gain-explicatif-cosmologique.md)

Verdict : architecture inférentielle confirmée ; architecture de constantes refusée ; `Lambda` seul candidat direct dans un modèle spécifié.

## 10. Distinctions acquises

```text
explication d’une relation
≠
explication de la valeur de ses paramètres
```

```text
fixité d’un coefficient
≠
stabilité d’une prédiction
≠
validité d’une description
```

```text
exactitude définitionnelle
≠
invariance physique
≠
précision empirique
```

```text
fixé dans un modèle
≠
constant physiquement
```

```text
architecture d’un domaine
≠
architecture de constantes
```

## 11. Conditions d’échec

Le cadre échoue si :

1. il ne peut pas préciser le régime ou les transformations ;
2. il confond objet et accès ;
3. il admet tout ce qui est numériquement fixe ;
4. il transforme une borne, une tension ou une reconstruction en constante ;
5. il confond fonction locale et nature de l’objet ;
6. il transforme un paramètre libre en explication ;
7. ses catégories dépendent seulement de son vocabulaire interne ;
8. une carte relationnelle n’ajoute ni dérivation, ni exclusion, ni contrefactuel.

## 12. Statut du corpus antérieur

Les anciennes familles, cartes et architectures restent disponibles comme archives de recherche.

Elles ne commandent plus le noyau actif.

Les éléments réutilisables sont :

- relations physiques ;
- équations ;
- sources ;
- distinctions de régime ;
- voies d’accès ;
- limites explicatives ;
- intuitions philosophiques requalifiées.

## 13. Prochaine phase

La phase conceptuelle minimale est close.

La prochaine phase est documentaire et Git :

1. rendre le `README` navigable depuis ce noyau ;
2. définir les statuts `actif`, `source`, `archive` ;
3. remplacer progressivement les noms versionnés des documents actifs par des noms canoniques ;
4. préserver les états historiques dans Git et dans les archives ;
5. réparer les liens relatifs ;
6. ouvrir une pull request de migration séparée.

## 14. Formule de clôture

> La question « qu’est-ce qu’une constante ? » fournit moins une réponse substantielle unique qu’un opérateur critique : demander à chaque fixité qui la porte, sous quelles transformations elle tient, dans quel régime, par quelle voie nous y accédons et à quel niveau elle doit être refusée.
