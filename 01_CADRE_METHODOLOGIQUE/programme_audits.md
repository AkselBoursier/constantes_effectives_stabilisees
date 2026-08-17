# Programme vivant des audits

## Fonction et rang

Ce document porte la **séquence de contrôle du projet** : types d’audits, dépendances, états, critères d’arrêt, d’extension et de réouverture, ainsi que les conditions d’amendement de cette séquence.

Il ne contient pas les résultats des audits et n’autorise par lui-même aucune réinstruction scientifique, computationnelle, méthodologique ou philosophique. Les issues restent les unités d’exécution bornées ; les PR et Git portent les mutations et leur historique.

La séquence ci-dessous est **validée comme base de travail mais reste amendable**. Sa numérotation `0–9` est provisoire et n’a aucune valeur conceptuelle. Toute modification de cette structure doit satisfaire le test d’amendement défini plus bas.

Ce document est vivant et conserve un nom stable ; Git porte son historique.

---

## 1. Contrat épistémique

### 1.1 Aucune supposition promue en état

Une hypothèse peut orienter une recherche, choisir une source ou motiver un test. Elle ne devient ni fait, ni verdict, ni dépendance, ni autorisation sans support explicite.

```text
HYPOTHESE != RESULTAT
PLAUSIBILITE != ETAT
ABSENCE_DE_CONTRE_EXEMPLE != PREUVE_POSITIVE
DEPENDANCE_NON_TESTEE = NON_ETABLIE
```

Une rubrique inconnue reste `NON_ETABLIE` ou `NON_DECIDABLE` selon le cas ; elle n’est pas remplie par vraisemblance.

### 1.2 Symétrie critique

L’audit n’est orienté par défaut ni vers la validation ni vers la démolition.

```text
PAS_D_INFLATION_SANS_SUPPORT
PAS_DE_DEFLATION_SANS_SUPPORT
```

Une conclusion positive et une critique négative supportent la même charge de preuve. L’audit doit pouvoir nommer et préserver les acquis réels — résultat robuste, distinction discriminante, gain explicatif, question féconde, fonction conceptuelle conservée, compatibilité ou tension féconde — autant que les erreurs, surinterprétations, pertes, dettes et incohérences réelles.

Un résultat négatif scientifiquement informatif est un acquis lorsqu’il réduit effectivement l’espace des possibilités ou modifie une décision.

### 1.3 Tout verdict est borné

Aucune conclusion ne vaut au-delà des matériaux, transformations, régimes, documents, résultats ou relations effectivement contrôlés.

`QUALIFIE_DANS_LE_PERIMETRE` signifie : conditions suffisantes pour avancer dans le périmètre déclaré. Il ne signifie ni vérité définitive ni interdiction de réouverture.

### 1.4 L’inachevé peut rester inachevé

Un chantier ne doit pas être artificiellement clos pour permettre à un autre d’avancer. Une suspension conserve la raison exacte, ce qui reste non qualifié et, si elle est établie, la condition de reprise.

L’effet de cette suspension sur un autre chantier doit être testé séparément.

### 1.5 Pas d’extension gratuite, pas de fermeture gratuite

Un audit ne s’étend pas simplement parce qu’un matériau existe. Il s’étend lorsqu’une conclusion importante dépend d’un élément non qualifié ou lorsqu’un contre-exemple reproduit montre que le périmètre initial est insuffisant.

Réciproquement, un périmètre initial borné ne ferme jamais par principe la possibilité de réauditer d’autres cycles ou volets.

---

## 2. Deux axes indépendants : état et effet sur une dépendance

### État d’un audit

```text
NON_OUVERT
EN_COURS
SUSPENDU
QUALIFIE_DANS_LE_PERIMETRE
A_REOUVRIR_SUR_CONDITION
```

### Effet de `X` sur un autre chantier ou une décision `Y`

```text
EFFET_SUR_Y = NON_ETABLI
               BLOQUANT_POUR_Y
               NON_BLOQUANT_POUR_Y
               CONDITIONNEL_POUR_Y
```

La valeur par défaut est `NON_ETABLI`.

```text
SUSPENDU != NON_BLOQUANT
```

Déclarer `NON_BLOQUANT_POUR_Y` exige que la dépendance de `Y` envers `X` ait été testée et que les éléments restant non qualifiés dans `X` ne soutiennent aucune prémisse nécessaire de `Y` dans le périmètre examiné. L’absence momentanée de contre-exemple ne suffit pas.

---

## 3. Fiche minimale avant ouverture d’un audit

```text
QUESTION
PERIMETRE_INITIAL
DEPENDANCES_CONNUES
HYPOTHESES_A_TESTER
MATERIAUX_OU_RESULTATS_SENTINELLES
CRITERES_D_ARRET
CRITERES_D_EXTENSION
CRITERES_DE_REOUVERTURE
SORTIES_RECEVABLES
```

La fiche doit rester aussi courte que le permet la contrôlabilité réelle de l’audit. Les issues peuvent porter son exécution détaillée ; elles ne remplacent pas ce programme comme vue de la séquence générale.

---

## 4. Séquence provisoire

Cette séquence exprime des dépendances de travail, non une chaîne irréversible. Les retours ciblés de la section 5 en font partie.

| Étape | Audit | Fonction / question principale |
|---|---|---|
| **0** | **Cadrage du programme** | Fixer questions, dépendances, sentinelles, critères d’arrêt, d’extension et de réouverture. Le présent document est le premier résultat de ce cadrage ; il n’ouvre aucun audit substantiel. |
| **1** | **Documentaire minimal d’orientation** | Localiser les pièces, distinguer routes vivantes, rangs revendiqués et états datés. Les travaux ayant conduit notamment à #124 et #126 en constituent une partie déjà réalisée, elle-même réauditable. Cet audit ne décide pas de la justesse scientifique, conceptuelle ou philosophique. |
| **2** | **Scientifique des résultats porteurs** | Identifier les résultats qui soutiennent réellement l’architecture intellectuelle actuelle et vérifier si leur qualification suffit à cet usage. Le périmètre initial reste borné ; d’autres cycles sont réaudités si une dépendance ou un contre-exemple le justifie. |
| **3** | **Conceptuel** | Identifier les questions, distinctions et fonctions intellectuelles réellement portées, puis tester ce qu’elles sont devenues : conservées, partiellement conservées, transformées avec gain ou perte, encore fécondes, dépassées, perdues/non réassimilées ou non décidables. Le test porte sur la fonction discriminante, pas sur la survie d’un mot. |
| **4** | **Méthodologique** | Tester si les règles et distinctions actuelles sont justifiées par les résultats et discriminations qualifiés, ou si elles sont seulement locales, redondantes, trop fortes, mal placées, non justifiées ou non décidables. La cohérence interne d’une règle ne prouve pas sa nécessité. |
| **5** | **Philosophique** | Distinguer propositions, portées et transferts entre philosophie, science et méthodologie. `COMPATIBLE != DERIVE_DE`. La généalogie éditoriale ou conversationnelle n’est consultée que si une transformation intellectuelle déterminée l’exige. |
| **6** | **Cohérence intellectuelle** | Tester si questions de recherche, résultats retenus, distinctions conceptuelles, choix méthodologiques et propositions philosophiques composent un programme dont les transitions sont justifiées plutôt que reconstruites a posteriori. Rechercher aussi les continuités réelles masquées, les acquis sous-exploités et les tensions fécondes. |
| **7** | **Cohérence générale / transversale** | Après qualification suffisante des couches concernées, contrôler les relations pertinentes : questions ↔ résultats, résultats ↔ concepts, concepts ↔ méthode, science ↔ philosophie, philosophie ↔ méthode, documents/issues ↔ état substantiel réel. Aucune relation n’est auditée par simple souci d’exhaustivité. |
| **8** | **Contre-audit** | Tenter activement de falsifier les conclusions précédentes de manière bilatérale : surpromotion **et** écrasement, continuité artificielle **et** continuité réelle devenue invisible, concept inutile **et** concept dont l’ablation fait perdre une discrimination, résultat surinterprété **et** sous-exploité. |
| **9** | **Normalisation documentaire Human-First** | Seulement lorsque les dépendances substantielles d’une transformation sont suffisamment qualifiées : documents vivants humains, routage agent minimal, noms stables, réécriture positive, réduction de méta-documentation, archivage et suppression exceptionnelle. |

Pour l’audit scientifique, préserver lorsque pertinent la séparation :

```text
calcul
-> resultat machine
-> qualification technique
-> soutien probatoire
-> resultat scientifique
-> verdict
-> portee
```

Pour l’étape 9, l’historique Git améliore la réauditabilité mais ne suffit jamais seul à autoriser une suppression. Une suppression exige au minimum la qualification du contenu unique, de la fonction probatoire active, des dépendances vivantes, de la représentation généalogique et de la récupérabilité Git.

---

## 5. Retours ciblés et réouverture

La séquence n’est pas strictement linéaire. Un audit peut rouvrir une couche antérieure lorsque sa propre conclusion en dépend réellement.

Exemples :

- un problème conceptuel dépend d’un résultat physique insuffisamment qualifié → retour scientifique ciblé ;
- une règle méthodologique change la lecture d’un résultat → réaudit scientifique ciblé ;
- une portée philosophique a été importée dans la méthode sans qualification → retour méthodologique ciblé ;
- une transformation intellectuelle reste inexpliquée → généalogie ciblée, sans réouverture automatique de toute l’archéologie ;
- le contre-audit reproduit un faux déclassement, une fausse promotion ou un faux raccord → réouverture du seul chantier nécessaire.

Toute réouverture identifie :

```text
DECLENCHEUR
CONCLUSION_PRECEDENTE_A_RETESTER
NOUVEAU_PERIMETRE_MINIMAL
POURQUOI_LE_PERIMETRE_PRECEDENT_NE_SUFFIT_PLUS
```

Aucun audit qualifié n’est irrévocable. Aucun audit n’est rouvert pour la seule possibilité abstraite d’un doute.

---

## 6. Profondeur et arrêt

La profondeur est commandée par les dépendances de la décision, pas par le nombre de niveaux documentaires disponibles.

```text
question examinee
-> premisses necessaires
-> supports de ces premisses
-> approfondissement si une premisse reste non qualifiee
-> STOP local lorsque la decision devient qualifiable dans le perimetre declare
```

Une dette extérieure à ce raisonnement ne force pas son instruction immédiate.

Un audit peut s’arrêter avec `NON_DECIDABLE` si les matériaux suffisants sont inaccessibles ou si l’extension nécessaire dépasse le périmètre autorisé. Ce résultat reste visible comme tel.

---

## 7. Amendement de la séquence

Ajouter une étape, scinder ou fusionner un audit, modifier l’ordre ou introduire un nouvel état exige d’établir :

1. la confusion, dépendance ou risque concret insuffisamment contrôlé par la structure actuelle ;
2. la conséquence possible de cette insuffisance ;
3. la discrimination, protection ou décision nouvelle rendue possible par l’amendement ;
4. pourquoi une simple précision d’une étape existante ne suffit pas.

Test d’ablation : si retirer l’amendement ne change aucune décision possible, aucune protection ou aucune capacité de falsification, l’amendement n’est pas justifié.

```text
PAS_DE_NOUVELLE_COUCHE
PAS_DE_NOUVELLE_CATEGORIE
PAS_DE_NOUVEL_ETAT
PAS_DE_NOUVEL_AUDIT
PAS_DE_NOUVELLE_DEPENDANCE
```

sans gain discriminant ou de contrôle démontré.

---

## 8. Gouvernance

```text
PROGRAMME VIVANT DES AUDITS
= sequence, dependances, etats, criteres

ISSUES
= executions bornees, preuves, arbitrages, blocages, resultats locaux

PR / GIT
= mutations du corpus et historique exact
```

Un éventuel GitHub Project peut représenter visuellement ces états mais ne devient pas une autorité scientifique, conceptuelle ou méthodologique par lui-même.

---

## 9. État initial de ce programme

```text
SEQUENCE_D_AUDITS = VALIDEE_COMME_BASE_DE_TRAVAIL
CONTRAT_EPISTEMIQUE = CANDIDAT_A_PROMOTION
AUDITS_SUBSTANTIELS = NON_OUVERTS_PAR_CE_DOCUMENT

AUDIT_DOCUMENTAIRE_MINIMAL = PARTIELLEMENT_REALISE_AVANT_CREATION
PORTEE_DES_RESULTATS_ANTERIEURS = A_RETESTER_SELON_DEPENDANCES

PR_#128 = CANDIDATE_DOCUMENTAIRE_DISTINCTE / NON_PROMUE
```

La première utilisation de ce programme devra cadrer explicitement l’audit substantiel initial avant de l’ouvrir. Elle ne transformera pas rétrospectivement les travaux antérieurs en preuves qu’ils n’avaient pas pour fonction d’établir.
