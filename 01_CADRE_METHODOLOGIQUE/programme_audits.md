# Programme vivant des audits

## Statut et fonction

Ce document porte la **séquence de contrôle du projet** : types d’audits, dépendances entre eux, états, critères d’arrêt et de réouverture, ainsi que les conditions d’amendement de cette séquence.

Il ne contient pas les résultats des audits et n’autorise par lui-même aucune réinstruction scientifique, computationnelle, méthodologique ou philosophique. Les issues restent les unités d’exécution bornées ; les PR et Git portent les mutations et leur historique.

La séquence ci-dessous est **validée comme base de travail mais reste amendable**. Sa numérotation est provisoire et n’a aucune valeur conceptuelle. Ajouter, scinder, fusionner ou déplacer une étape exige un gain discriminant démontré selon la section « Amendement de la séquence ».

Ce document est vivant et conserve un nom stable ; Git porte son historique.

---

## 1. Contrat épistémique

### 1.1 Aucune supposition promue en état

Une hypothèse peut orienter une recherche, choisir une source à consulter ou motiver un test. Elle ne devient ni fait, ni verdict, ni dépendance, ni autorisation sans support explicite.

```text
HYPOTHESE != RESULTAT
PLAUSIBILITE != ETAT
ABSENCE_DE_CONTRE_EXEMPLE != PREUVE_POSITIVE
```

Lorsqu’une relation nécessaire n’a pas été testée :

```text
DEPENDANCE = NON_ETABLIE
```

### 1.2 Même charge de preuve pour inflation et écrasement

L’audit n’est orienté par défaut ni vers la validation ni vers la démolition.

Une conclusion positive, une conclusion négative, une suspension, un déclassement ou une réhabilitation doivent être soutenus par des éléments identifiés et bornés au périmètre réellement instruit.

```text
PAS_D_INFLATION_SANS_SUPPORT
PAS_DE_DEFLATION_SANS_SUPPORT
```

Un audit doit pouvoir établir aussi bien :

- un résultat robuste ;
- une distinction discriminante ;
- un gain explicatif réel ;
- une question féconde ;
- une fonction conceptuelle conservée ;
- une compatibilité établie dans un périmètre ;
- une tension féconde ;
- un résultat négatif scientifiquement informatif ;

que :

- une erreur ;
- une surinterprétation ;
- une dette ;
- une perte ;
- une incohérence ;
- une dépendance non établie ;
- une conclusion non décidable dans l’état des matériaux.

### 1.3 Tout verdict est borné

Aucune conclusion ne vaut au-delà des matériaux, transformations, régimes, documents, résultats ou relations effectivement contrôlés.

`QUALIFIE_DANS_LE_PERIMETRE` signifie que les conditions sont suffisantes pour avancer dans le périmètre déclaré. Il ne signifie ni vérité définitive ni interdiction de réouverture.

### 1.4 L’inachevé peut rester inachevé

Un chantier ne doit pas être artificiellement clos pour permettre à un autre d’avancer.

Une suspension conserve :

- la raison exacte de la suspension ;
- ce qui reste non qualifié ;
- la condition de reprise si elle est identifiable ;
- l’effet sur les autres chantiers uniquement lorsqu’il a été testé séparément.

### 1.5 Pas d’extension gratuite

Aucun audit ne s’étend simplement parce qu’un matériau existe ou qu’un autre cycle pourrait être vérifié.

L’extension est justifiée lorsqu’une conclusion importante dépend d’un élément non qualifié, ou lorsqu’un contre-exemple reproduit montre que le périmètre initial est insuffisant.

Réciproquement, un périmètre initial borné ne ferme jamais par principe la possibilité de réauditer d’autres cycles.

---

## 2. Deux axes indépendants : état et effet sur les dépendances

### 2.1 État d’un audit

```text
NON_OUVERT
EN_COURS
SUSPENDU
QUALIFIE_DANS_LE_PERIMETRE
A_REOUVRIR_SUR_CONDITION
```

Ces états décrivent uniquement le chantier lui-même.

### 2.2 Effet sur un autre chantier ou une décision

Pour une relation `X -> Y` :

```text
EFFET_SUR_Y = NON_ETABLI
               BLOQUANT_POUR_Y
               NON_BLOQUANT_POUR_Y
               CONDITIONNEL_POUR_Y
```

La valeur par défaut est `NON_ETABLI`.

En particulier :

```text
SUSPENDU != NON_BLOQUANT
```

Déclarer `NON_BLOQUANT_POUR_Y` exige au minimum que la dépendance de `Y` envers `X` ait été testée et que les éléments restant non qualifiés dans `X` ne soutiennent aucune prémisse nécessaire de la décision `Y` dans le périmètre examiné.

L’absence momentanée de contre-exemple ne suffit pas à établir un non-blocage général.

---

## 3. Fiche minimale d’un audit

Avant ouverture substantielle, chaque audit doit expliciter seulement ce qui est nécessaire pour rendre ses décisions contrôlables :

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

Une rubrique inconnue reste `NON_ETABLIE` ; elle n’est pas remplie par supposition.

Les issues peuvent porter l’exécution détaillée de cette fiche. Elles ne remplacent pas le présent programme comme vue de la séquence générale.

---

## 4. Séquence provisoire des audits

Cette séquence exprime des **dépendances de travail**, non une chaîne irréversible. Les boucles de retour prévues à la section suivante font partie du programme.

### 0 — Cadrage du programme d’audits

Fonction : fixer les questions de chaque audit, leurs dépendances, sentinelles initiales, critères d’arrêt, d’extension et de réouverture.

Ce document constitue le premier résultat de ce cadrage. Il ne lance pas encore les audits substantiels.

### 1 — Audit documentaire minimal d’orientation

Question : où sont les pièces pertinentes, quel rang revendiquent-elles, quelles sont les routes vivantes, quels états sont datés ?

Fonction : rendre les matériaux localisables et leurs statuts documentaires lisibles avant comparaison substantielle.

Les travaux de reprise ayant conduit notamment à #124 et #126 en constituent une partie déjà réalisée. Leur portée et leurs conclusions restent elles-mêmes réauditables.

Cet audit ne décide pas qu’un contenu est conceptuellement, scientifiquement ou philosophiquement juste.

### 2 — Audit scientifique des résultats porteurs

Question : quels résultats scientifiques soutiennent réellement l’architecture intellectuelle actuelle, et leur qualification est-elle suffisante pour cet usage ?

Chaîne minimale à préserver lorsque pertinente :

```text
calcul
-> resultat machine
-> qualification technique
-> soutien probatoire
-> resultat scientifique
-> verdict
-> portee
```

Le périmètre initial doit être borné à des résultats porteurs ou sentinelles. D’autres cycles restent réauditables si une dépendance ou un contre-exemple justifie l’extension.

### 3 — Audit conceptuel

Question : quelles questions, distinctions et fonctions intellectuelles sont effectivement portées par le projet actuel, et que sont devenues celles qui ont structuré sa refondation ?

Sorties recevables, à adapter au cas :

```text
FONCTION_CONSERVEE_ET_MIEUX_FORMULEE
FONCTION_PARTIELLEMENT_CONSERVEE
FONCTION_TRANSFORMEE_AVEC_GAIN
FONCTION_TRANSFORMEE_AVEC_PERTE
FONCTION_ENCORE_FECONDE
FONCTION_DEPASSEE
PERDUE_OU_NON_REASSIMILEE
NON_DECIDABLE
```

Le vocabulaire historique n’est ni restauré ni déclassé automatiquement. L’objet du test est la fonction discriminante, pas la survie d’un mot.

### 4 — Audit méthodologique

Question : les règles et distinctions méthodologiques actuelles sont-elles réellement justifiées par les résultats et discriminations qualifiés, ou certaines sont-elles trop fortes, redondantes, locales ou mal placées ?

Sorties possibles :

```text
NECESSAIRE
UTILE_MAIS_LOCALE
REDONDANTE
TROP_FORTE
MAL_PLACEE
NON_JUSTIFIEE
NON_DECIDABLE
```

La cohérence interne d’une règle ne suffit pas à démontrer sa nécessité.

### 5 — Audit philosophique

Question : quelles propositions sont philosophiques, quelles portées revendiquent-elles, quelles relations entretiennent-elles avec les résultats scientifiques et la méthodologie, et quelles transformations du programme ont-elles effectivement contribué à produire ?

L’audit distingue au minimum :

```text
COMPATIBLE != DERIVE_DE
```

Une conséquence philosophique n’est jamais déduite automatiquement d’un résultat scientifique. Une proposition philosophique n’a pas à être démontrée par la physique pour être recevable, mais elle ne peut pas présenter une extrapolation comme résultat physique.

La généalogie éditoriale ou conversationnelle n’est consultée que lorsqu’elle est nécessaire pour qualifier une transformation intellectuelle déterminée.

### 6 — Audit de cohérence intellectuelle

Question : les questions de recherche, résultats retenus, distinctions conceptuelles, choix méthodologiques et propositions philosophiques forment-ils un programme intelligible dont les transitions sont justifiées ?

Cet audit recherche aussi bien :

- les raccords artificiellement reconstruits a posteriori ;
- les continuités réelles rendues invisibles par la fragmentation documentaire ;
- les acquis intellectuels sous-exploités ;
- les simplifications ayant fait perdre un degré de liberté de la question ;
- les tensions réellement fécondes qu’une normalisation trop rapide pourrait effacer.

Une cohérence documentaire ou une élégance conceptuelle ne suffisent pas à établir une cohérence intellectuelle.

### 7 — Audit de cohérence générale et transversale

Question : après qualification des couches précédentes, leurs relations sont-elles compatibles avec les portées effectivement établies ?

Relations initiales à contrôler lorsque pertinentes :

```text
questions de recherche <-> resultats
resultats <-> concepts
concepts <-> methodologie
science <-> philosophie
philosophie <-> methodologie
documents/issues <-> etat substantiel reel
```

Cette liste n’est pas une obligation d’exhaustivité ; chaque relation doit avoir une fonction démontrée dans la décision examinée.

### 8 — Contre-audit

Fonction : tenter activement de falsifier les conclusions et déclassements produits par les audits précédents.

Le contre-audit est bilatéral. Il cherche :

```text
ce qui a ete trop promu
ET ce qui a ete trop declasse

les continuites artificielles
ET les continuites reelles devenues invisibles

les concepts inutiles
ET ceux dont l'ablation fait perdre une discrimination

les resultats surinterpretes
ET les resultats sous-exploites
```

Une critique non étayée reçoit elle aussi `NON_ETABLIE`.

### 9 — Normalisation documentaire Human-First

Cette étape ne devient admissible qu’après qualification suffisante des couches dont dépend une transformation documentaire donnée.

Elle peut alors instruire, séparément et sans automatisme :

- architecture documentaire destinée aux humains ;
- routage minimal destiné aux agents ;
- noms stables des documents vivants ;
- réécriture positive des corps courants ;
- réduction de la méta-documentation ;
- archivage ;
- suppression exceptionnelle.

L’historique Git est une condition utile de réauditabilité mais ne suffit pas à autoriser une suppression.

Une suppression exige au minimum que soient qualifiés :

```text
CONTENU_UNIQUE
FONCTION_PROBATOIRE_ACTIVE
DEPENDANCES_VIVANTES
GENEALOGIE_REPRESENTEE
RECUPERABILITE_GIT
```

La conservation d’un résultat négatif, d’une limite, d’un refus ou d’une dette pertinente n’est pas contraire à une réécriture positive.

---

## 5. Boucles de retour et réouverture

La séquence n’est pas strictement linéaire.

Exemples de retours légitimes :

- l’audit conceptuel révèle qu’une distinction dépend d’un résultat physique insuffisamment qualifié -> retour ciblé vers l’audit scientifique du dossier concerné ;
- l’audit méthodologique montre qu’une règle change la lecture d’un résultat -> réaudit scientifique ciblé ;
- l’audit philosophique révèle une portée méthodologique importée sans qualification -> retour ciblé vers l’audit méthodologique ;
- l’audit de cohérence intellectuelle révèle une transformation historique inexpliquée -> généalogie ciblée, sans réouverture automatique de toute l’archéologie ;
- le contre-audit reproduit un faux déclassement, une fausse promotion ou un faux raccord -> réouverture du seul chantier nécessaire pour qualifier ce contre-exemple.

Une réouverture doit identifier :

```text
DECLENCHEUR
CONCLUSION_PRECEDENTE_A_RETESTER
NOUVEAU_PERIMETRE_MINIMAL
POURQUOI_LE_PERIMETRE_PRECEDENT_NE_SUFFIT_PLUS
```

Aucun audit qualifié n’est irrévocable. Aucun audit n’est rouvert seulement parce qu’une possibilité abstraite de doute existe.

---

## 6. Critères d’arrêt et de profondeur

La profondeur est commandée par les dépendances de la décision, pas par le nombre de niveaux documentaires disponibles.

Forme générale :

```text
question examinee
-> premisses necessaires
-> supports de ces premisses
-> approfondissement seulement si une premisse reste non qualifiee
-> STOP local lorsque la decision devient qualifiable dans le perimetre declare
```

L’apparition d’une dette extérieure au raisonnement ne force pas son instruction immédiate.

Un audit peut s’arrêter avec `NON_DECIDABLE` si les matériaux suffisants ne sont pas accessibles ou si l’extension nécessaire dépasserait le périmètre autorisé. Ce résultat doit être conservé comme tel.

---

## 7. Amendement de la séquence

La séquence n’est pas canonisée par sa numérotation actuelle.

Ajouter une étape, scinder ou fusionner un audit, modifier l’ordre ou introduire un nouvel état n’est recevable que si l’amendement établit :

1. une confusion, une dépendance ou un risque concret que la séquence actuelle ne contrôle pas suffisamment ;
2. la conséquence possible de cette insuffisance ;
3. la discrimination ou décision nouvelle rendue possible par l’amendement ;
4. pourquoi une simple précision d’une étape existante ne suffit pas.

Test d’ablation :

> Si retirer l’amendement ne change aucune décision possible, aucune protection ou aucune capacité de falsification, l’amendement n’est pas justifié.

Principe transverse :

```text
PAS_DE_NOUVELLE_COUCHE
PAS_DE_NOUVELLE_CATEGORIE
PAS_DE_NOUVEL_ETAT
PAS_DE_NOUVEL_AUDIT
PAS_DE_NOUVELLE_DEPENDANCE
```

sans gain discriminant ou de contrôle démontré.

---

## 8. Architecture de gouvernance

```text
PROGRAMME VIVANT DES AUDITS
= sequence, dependances, etats, criteres

ISSUES
= executions bornees, preuves, arbitrages, blocages, resultats locaux

PR / GIT
= mutations du corpus et historique exact
```

Un éventuel tableau de bord ou GitHub Project peut représenter visuellement ces états, mais ne devient pas une autorité scientifique, conceptuelle ou méthodologique par lui-même.

---

## 9. État initial au moment de création

```text
SEQUENCE_D_AUDITS = VALIDEE_COMME_BASE_DE_TRAVAIL
CONTRAT_EPISTEMIQUE = INSCRIT_COMME_CANDIDAT_A_PROMOTION
AUDITS_SUBSTANTIELS = NON_OUVERTS_PAR_CE_DOCUMENT

AUDIT_DOCUMENTAIRE_MINIMAL = PARTIELLEMENT_REALISE_AVANT_CREATION
PORTEE_DES_RESULTATS_ANTERIEURS = A_RETESTER_SELON_DEPENDANCES

PR_#128 = CANDIDATE_DOCUMENTAIRE_DISTINCTE / NON_PROMUE_A_CE_STADE
```

La première utilisation de ce programme devra consister à cadrer explicitement l’audit substantiel initial avant de l’ouvrir. Elle ne doit pas transformer rétrospectivement les travaux antérieurs en preuves qu’ils n’avaient pas pour fonction d’établir.
