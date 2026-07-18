# Refondation du domaine

## Statut

Ce document est le cadre canonique actif de la refondation.

Son historique est désormais porté par Git. Aucun numéro de version n’est ajouté à son nom.

Décision de rang associée :

- [Constance de l’objet, stabilisation de l’accès et mode de constitution](Decision_statuts_constance_acces_constitution_v0_1.md)

Carte de jonction associée :

- [Carte des frottements entre chantiers](../05_CARTES_ET_SYNTHESES/Carte_frottements_chantiers_v0_1.md)

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

## 4. Trois statuts de constance de l’objet

### 4.1 Constance physique

Invariance d’une grandeur ou d’une relation sous des transformations physiques déclarées, dans un domaine donné.

### 4.2 Constance effective

Coefficient traité comme fixe dans une approximation contrôlée, avec corrections et condition de rupture explicites.

### 4.3 Constance métrologique

Valeur numérique fixée exactement dans un système d’unités, sans assimilation à une mesure parfaite ni à une invariance physique démontrée.

## 5. Niveaux à ne pas confondre

Le corpus distingue désormais explicitement :

```text
constance de l’objet
≠
stabilisation de l’accès ou de l’estimation
≠
mode de constitution ou d’organisation.
```

Une borne, une reconstruction ou une tension peuvent stabiliser un domaine admissible, une estimation ou un niveau de maturité sans constituer une constance de l’objet.

Une architecture, une composition ou une dynamique peuvent constituer une relation ou canaliser une fixité sans expliquer automatiquement la valeur de leurs paramètres libres.

La décision détaillée est portée par :

- [Décision de rang — constance, accès et constitution](Decision_statuts_constance_acces_constitution_v0_1.md)

## 6. Axes auxiliaires

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

## 7. Fonction de fixité

Une fonction de fixité désigne provisoirement :

> le rôle local par lequel un objet physiquement ou formellement déterminé maintient une relation stable entre des états, processus, secteurs ou descriptions, dans un régime et sous des transformations explicités.

Cette fonction n’est pas un type ontologique.

Le même objet peut exercer plusieurs fonctions, et plusieurs objets physiquement différents peuvent tenir une fonction similaire.

## 8. Objets exclus du noyau

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

Le refus du mot `constante` ne retire pas à ces objets leur intérêt scientifique. Il les requalifie comme paramètres d’état, conditions, bornes, reconstructions ou éléments d’une architecture d’inférence.

## 9. Test des cinq cas sentinelles

Document :

- [Test des cinq cas sentinelles](test-cas-sentinelles.md)

Résultat :

| Cas | Décision |
|---|---|
| `G_F` | admis comme constante effective à basse énergie |
| `h` dans le SI | admis comme constante métrologique définissante |
| `alpha_s(mu)` | refusé comme constante simpliciter |
| `H_0` | refusé comme constante nomologique ; conservé comme paramètre d’état reconstruit |
| borne sur la masse des neutrinos | refusée comme constante ; conservée comme domaine admissible borné |

```text
2 admissions relatives
3 refus.
```

## 10. Résultat des cycles

### 10.1 Higgs–Yukawa

- [Dossier central](../02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/architecture-relationnelle-higgs-yukawa.md)
- [Vérification](../02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/verification-physique-higgs-yukawa.md)
- [Évaluation](../02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/evaluation-gain-explicatif-higgs-yukawa.md)

Verdict : architecture physique et représentationnelle confirmée ; famille unique de constantes refusée.

### 10.2 Basse énergie

- [Dossier central](../02_CYCLES_PHYSIQUES/06_Cycle_effectif_basse_energie/architecture-relationnelle-basse-energie.md)
- [Vérification](../02_CYCLES_PHYSIQUES/06_Cycle_effectif_basse_energie/verification-physique-basse-energie.md)
- [Évaluation](../02_CYCLES_PHYSIQUES/06_Cycle_effectif_basse_energie/evaluation-gain-explicatif-basse-energie.md)

Verdict : architecture méthodologique de validité confirmée ; espèce unique de constantes effectives refusée.

### 10.3 SI

- [Dossier central](../02_CYCLES_PHYSIQUES/08_Cycle_metrologique_SI/architecture-relationnelle-metrologique-si.md)
- [Vérification](../02_CYCLES_PHYSIQUES/08_Cycle_metrologique_SI/verification-metrologique-si.md)
- [Évaluation](../02_CYCLES_PHYSIQUES/08_Cycle_metrologique_SI/evaluation-gain-explicatif-metrologique-si.md)

Verdict : architecture définitionnelle confirmée ; homogénéité physique des constantes définissantes refusée.

### 10.4 Cosmologie

- [Dossier central](../02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/architecture-relationnelle-cosmologique.md)
- [Vérification](../02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/verification-physique-cosmologique.md)
- [Évaluation](../02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/evaluation-gain-explicatif-cosmologique.md)

Verdict : architecture inférentielle confirmée ; architecture de constantes refusée ; `Lambda` seul candidat direct dans un modèle spécifié.

### 10.5 Fine-tuning

- [Cadrage](../02_CYCLES_PHYSIQUES/09_Cycle_fine_tuning/cadrage-cycle-fine-tuning.md)
- [Synthèse du premier lot](../02_CYCLES_PHYSIQUES/09_Cycle_fine_tuning/synthese-premier-lot-fine-tuning.md)

Verdict : le fine-tuning doit être audité comme relation entre espace de paramètres, carte vers des observables, critère de viabilité et mesure éventuelle. Les dépendances et corrélations dissolvent ou réduisent certains réglages ; des contingences résiduelles subsistent, notamment pour la constante cosmologique.

### 10.6 Fixité électrofaible dynamique

- [Cadrage](../02_CYCLES_PHYSIQUES/10_Cycle_fixite_electrofaible_dynamique/cadrage-cycle-fixite-electrofaible-dynamique.md)
- [Phase 2 — modèle minimal](../02_CYCLES_PHYSIQUES/10_Cycle_fixite_electrofaible_dynamique/resultats-phase2-modele-minimal.md)
- [Phase 3 — régime quartique](../02_CYCLES_PHYSIQUES/10_Cycle_fixite_electrofaible_dynamique/resultats-phase3-regime-quartique.md)
- [Phase 4 — toy model dissipatif](../02_CYCLES_PHYSIQUES/10_Cycle_fixite_electrofaible_dynamique/resultats-phase4-toy-model-dissipatif.md)

Verdict : rendre une grandeur dynamique ne constitue pas une explication. Les modèles conservatifs testés stabilisent `v` mais échouent sur le devenir énergétique ; un bilan ouvert possède une fenêtre phénoménologique, dont la réalisation microscopique reste à établir.

## 11. Distinctions acquises

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

```text
constitution d’une fixité
≠
qualification de cette fixité
≠
interprétation ontologique de sa constitution
```

## 12. Conditions d’échec

Le cadre échoue si :

1. il ne peut pas préciser le régime ou les transformations ;
2. il confond objet et accès ;
3. il admet tout ce qui est numériquement fixe ;
4. il transforme une borne, une tension ou une reconstruction en constante ;
5. il confond fonction locale et nature de l’objet ;
6. il transforme un paramètre libre en explication ;
7. ses catégories dépendent seulement de son vocabulaire interne ;
8. une carte relationnelle n’ajoute ni dérivation, ni exclusion, ni contrefactuel ;
9. une dynamique déplace le réglage sans en comptabiliser le coût ;
10. une interprétation philosophique est présentée comme résultat physique acquis.

## 13. Statut du corpus antérieur

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

Les documents philosophiques actifs conservent leur fonction d’exploration, de test, de voisinage et de préparation des livrables. Leur intégration au noyau passe par une décision de rang, non par leur seule présence dans le même dépôt.

## 14. Phase actuelle

La migration documentaire, la réunion des branches historiques et l’ouverture des cycles fine-tuning et fixité dynamique ont été réalisées dans une branche de récupération.

La phase actuelle est une resynchronisation bornée avant validation :

1. appliquer la distinction entre constance de l’objet, accès et constitution ;
2. réparer les références actives et les versions déclarées courantes ;
3. rendre visibles les frottements entre les chantiers ;
4. maintenir les documents exploratoires sans leur attribuer un rang canonique implicite ;
5. contrôler les liens, terminaisons, placeholders et fichiers annoncés ;
6. soumettre la consolidation corrigée à revue avant toute fusion dans `main`.

Après cette validation, les nouveaux chantiers devront partir du nouveau `main` et les branches thématiques rester bornées et temporaires.

## 15. Formule de clôture

> La question « qu’est-ce qu’une constante ? » fournit moins une réponse substantielle unique qu’un opérateur critique : demander à chaque fixité qui la porte, sous quelles transformations elle tient, dans quel régime, par quelle voie nous y accédons, par quelle histoire elle se constitue et à quel niveau elle doit être refusée.
