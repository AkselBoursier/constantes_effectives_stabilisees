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

`NON_ETABLI` signifie qu’une proposition, relation ou dépendance n’a pas encore été démontrée dans le périmètre considéré.

`NON_DECIDABLE` est plus fort et ne doit pas servir de synonyme : il suppose qu’une instruction pertinente a été tentée et qu’une limite explicitée des matériaux, des accès ou du périmètre autorisé empêche actuellement de trancher.

Une rubrique inconnue reste `NON_ETABLIE` ; elle n’est pas remplie par vraisemblance.

### 1.2 Symétrie critique

L’audit n’est orienté par défaut ni vers la validation ni vers la démolition.

```text
PAS_D_INFLATION_SANS_SUPPORT
PAS_DE_DEFLATION_SANS_SUPPORT
```

Une conclusion positive et une critique négative supportent la même charge de preuve. L’audit doit pouvoir nommer et préserver les acquis réels — résultat robuste, distinction discriminante, gain explicatif, question féconde, fonction conceptuelle conservée, compatibilité ou tension féconde — autant que les erreurs, surinterprétations, pertes, dettes et incohérences réelles.

Un résultat négatif scientifiquement informatif est un acquis lorsqu’il borne, exclut ou réduit effectivement un espace de possibilités, révèle une limitation pertinente, ou modifie ce qu’une décision ou une interprétation peut légitimement soutenir.

### 1.3 Tout verdict est borné

Aucune conclusion ne vaut au-delà des matériaux, transformations, régimes, documents, résultats ou relations effectivement contrôlés.

`QUALIFIE_DANS_LE_PERIMETRE` signifie seulement que la **conclusion propre de l’audit** est suffisamment instruite dans le périmètre déclaré. Cet état ne vaut ni vérité définitive, ni non-blocage, ni autorisation automatique pour un autre chantier.

L’effet sur un autre chantier reste toujours qualifié sur l’axe séparé défini en section 2.

### 1.4 L’inachevé peut rester inachevé

Un chantier ne doit pas être artificiellement clos pour permettre à un autre d’avancer. Une suspension conserve la raison exacte, ce qui reste non qualifié et, si elle est établie, la condition de reprise.

L’effet de cette suspension sur un autre chantier doit être testé séparément.

### 1.5 Couverture documentaire exhaustive, approfondissement substantiel discriminant

La trajectoire documentaire du projet n’est pas présumée refléter fidèlement sa trajectoire intellectuelle. Un résultat, une question, une dette, un refus, un incident ou une bifurcation peut se trouver dans un document dont le titre, le rang ou le routage vivant ne signale plus sa fonction réelle.

```text
TOPOLOGIE_DOCUMENTAIRE ~= TOPOLOGIE_INTELLECTUELLE = NON_PRESUME
RANG_APPARENT_D_UN_DOCUMENT -> IMPORTANCE_INTELLECTUELLE = NON_ETABLI
ROUTAGE_VIVANT -> EXHAUSTIVITE_DES_ACQUIS = NON_ETABLI
```

En conséquence, la **lecture documentaire du corpus auditable est exhaustive**. Un audit de surface, un README, une synthèse, un inventaire de titres ou une route vivante ne peuvent remplacer cette lecture pour exclure un document.

Cette exhaustivité documentaire ne signifie pas réauditer scientifiquement, computationnellement, méthodologiquement ou philosophiquement chaque contenu avec la même profondeur. Après lecture intégrale et remontée dans le changelog d’audit, l’approfondissement substantiel reste commandé par les résultats, dépendances, contradictions, dettes et falsificateurs effectivement identifiés.

La réduction progressive du corpus actif est donc autorisée **après remontée**, jamais avant.

### 1.6 Pas d’approfondissement gratuit, pas de fermeture gratuite

La présence d’un matériau impose sa lecture dans le corpus documentaire exhaustif ; elle n’impose pas automatiquement une réinstruction substantielle complète.

Un audit substantiel s’approfondit lorsqu’une conclusion importante dépend d’un élément non qualifié, lorsqu’un résultat remonté exige vérification, lorsqu’un contre-exemple reproduit montre qu’une conclusion est insuffisamment soutenue, ou lorsqu’une résurgence modifie la carte des dépendances.

Réciproquement, aucune lecture achevée ni aucun périmètre courant ne ferme par principe la possibilité de réauditer un cycle ou un volet lorsque le changelog ou un audit ultérieur fait surgir une raison matérielle de le faire.

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

- `NON_OUVERT` : aucune instruction substantielle n’a encore été engagée sous ce programme.
- `EN_COURS` : l’instruction est active et aucune conclusion terminale n’est encore qualifiée.
- `SUSPENDU` : l’instruction reste incomplète ; la raison de suspension et le reste non qualifié doivent être explicites.
- `QUALIFIE_DANS_LE_PERIMETRE` : la conclusion propre de l’audit est suffisamment instruite dans son périmètre, sans effet automatique sur un autre chantier.
- `A_REOUVRIR_SUR_CONDITION` : une condition future explicite a été identifiée comme déclencheur de réexamen. Tant qu’elle n’est pas satisfaite, elle ne constitue pas une réouverture active ; si elle devient vraie, la conclusion affectée doit être retestée avant d’être réutilisée au-delà de ce que permet encore son ancien périmètre.

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
QUALIFIE_DANS_LE_PERIMETRE != NON_BLOQUANT
```

Déclarer `NON_BLOQUANT_POUR_Y` exige que la dépendance de `Y` envers `X` ait été testée et que les éléments restant non qualifiés dans `X` ne soutiennent aucune prémisse nécessaire de `Y` dans le périmètre examiné. L’absence momentanée de contre-exemple ne suffit pas.

---

## 3. Fiche minimale avant ouverture d’un audit

```text
QUESTION
CORPUS_DOCUMENTAIRE_A_COUVRIR
PERIMETRE_SUBSTANTIEL_INITIAL
DEPENDANCES_CONNUES
HYPOTHESES_A_TESTER
MATERIAUX_OU_RESULTATS_SENTINELLES
CONTRE_TESTS_OU_FALSIFICATEURS
CRITERES_D_ARRET
CRITERES_D_APPROFONDISSEMENT
CRITERES_DE_REOUVERTURE
SORTIES_RECEVABLES
```

`CORPUS_DOCUMENTAIRE_A_COUVRIR` décrit ce qui doit être lu intégralement. `PERIMETRE_SUBSTANTIEL_INITIAL` décrit seulement où commence la réinstruction approfondie ; il ne constitue jamais un filtre documentaire d’exclusion.

Les contre-tests doivent être adaptés à la nature de l’audit. Leur fonction est d’empêcher qu’une conclusion soit qualifiée sans exposition suffisante à une alternative, un cas négatif, une ablation ou un falsificateur pertinent. Lorsqu’aucun contre-test de ce type n’est applicable, cette absence doit être justifiée plutôt que supposée.

La fiche doit rester aussi courte que le permet la contrôlabilité réelle de l’audit. Les issues peuvent porter son exécution détaillée ; elles ne remplacent pas ce programme comme vue de la séquence générale.

Le changelog vivant `changelog_audit_integral.md` est obligatoire pour les investigations engagées sous cette règle de couverture. Il est mis à jour au minimum après chaque investigation complète d’un cycle et à chaque résurgence significative susceptible de modifier une lecture, une dette, une relation ou une décision.

---

## 4. Séquence provisoire

Cette séquence exprime des dépendances de travail, non une chaîne irréversible. Les retours ciblés de la section 5 en font partie.

| Étape | Audit | Fonction / question principale |
|---|---|---|
| **0** | **Cadrage du programme** | Fixer questions, couverture documentaire, dépendances, sentinelles éventuelles, contre-tests, critères d’arrêt, d’approfondissement et de réouverture. Le présent document est le premier résultat de ce cadrage ; il n’ouvre aucun audit substantiel. |
| **1** | **Documentaire d’orientation et de couverture** | Localiser les pièces, distinguer routes vivantes, rangs revendiqués et états datés, puis établir la couverture exhaustive nécessaire aux audits. Des travaux documentaires antérieurs, notamment ceux ayant conduit à #124 et #126, existent comme matériaux candidats ; leur qualification comme réalisation partielle de cette étape reste à établir sous le présent programme. Cet audit ne décide pas de la justesse scientifique, conceptuelle ou philosophique. |
| **2** | **Scientifique des résultats porteurs** | Lire le corpus documentaire pertinent de manière exhaustive, remonter les résultats et dépendances dans le changelog, puis vérifier en profondeur ce que les résultats effectivement porteurs établissent réellement et si leur qualification suffit à l’usage envisagé. Le caractère « porteur » n’est pas présupposé par la sélection initiale, le rang documentaire ou le routage. |
| **3** | **Conceptuel** | Identifier les questions, distinctions et fonctions intellectuelles réellement portées, puis tester ce qu’elles sont devenues : conservées, partiellement conservées, transformées avec gain ou perte, encore fécondes, dépassées, perdues/non réassimilées ou non décidables. Le test porte sur la fonction discriminante, pas sur la survie d’un mot. La couverture documentaire nécessaire à cette instruction reste exhaustive avant exclusion. |
| **4** | **Méthodologique** | Tester si les règles et distinctions actuelles sont justifiées au regard des problèmes, discriminations, risques et supports effectivement établis, ou si elles sont seulement locales, redondantes, trop fortes, mal placées, non justifiées ou non décidables. Une règle n’est ni dérivée automatiquement des résultats scientifiques ni justifiée par sa seule cohérence interne. |
| **5** | **Philosophique** | Distinguer propositions, portées et transferts entre philosophie, science et méthodologie. `COMPATIBLE != DERIVE_DE`. Les matériaux philosophiques, éditoriaux et généalogiques qui appartiennent au corpus retenu pour cet audit sont lus intégralement avant exclusion ; leur rang n’est pas présumé par leur emplacement. |
| **6** | **Cohérence intellectuelle** | Tester si questions de recherche, résultats retenus, distinctions conceptuelles, choix méthodologiques et propositions philosophiques composent un programme dont les transitions sont justifiées plutôt que reconstruites a posteriori. Rechercher aussi les continuités réelles masquées, les acquis sous-exploités et les tensions fécondes. |
| **7** | **Cohérence générale / transversale** | Après qualification suffisante des couches concernées, contrôler les relations pertinentes : questions ↔ résultats, résultats ↔ concepts, concepts ↔ méthode, science ↔ philosophie, philosophie ↔ méthode, documents/issues ↔ état substantiel réel. La couverture documentaire déjà consignée évite de confondre absence de lecture et absence de relation. |
| **8** | **Contre-audit** | Tenter activement de falsifier les conclusions précédentes de manière bilatérale : surpromotion **et** écrasement, continuité artificielle **et** continuité réelle devenue invisible, concept inutile **et** concept dont l’ablation fait perdre une discrimination, résultat surinterprété **et** sous-exploité. Cette étape complète les contre-tests locaux ; elle ne les remplace pas. |
| **9** | **Normalisation documentaire Human-First** | Seulement lorsque les dépendances substantielles d’une transformation sont suffisamment qualifiées et que la couverture nécessaire est consignée : documents vivants humains, routage agent minimal, noms stables, réécriture positive, réduction de méta-documentation, archivage et suppression exceptionnelle. |

### Co-instruction bornée des étapes 2 et 3

Les étapes 2 et 3 ne forment pas une dérivation simple `2 -> 3`.

La lecture documentaire exhaustive peut faire remonter des résultats, questions ou fonctions intellectuelles que les routes courantes ne signalaient pas. L’audit scientifique détermine ensuite lesquels exigent une qualification scientifique approfondie ; l’audit conceptuel peut à son tour révéler qu’un résultat omis, une ancienne question ou une fonction intellectuelle impose un retour scientifique ciblé. Inversement, la qualification scientifique peut invalider ou réduire une relation conceptuelle présumée.

L’exhaustivité porte donc sur la **lecture et la remontée**, non sur la répétition automatique de toute opération scientifique.

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

## 5. Retours ciblés, résurgences et réouverture

La séquence n’est pas strictement linéaire. Un audit peut rouvrir une couche antérieure lorsque sa propre conclusion en dépend réellement.

Exemples :

- un document lu fait resurgir un résultat scientifique oublié ou déplacé → inscription immédiate au changelog puis qualification de son effet ;
- un problème conceptuel dépend d’un résultat physique insuffisamment qualifié → retour scientifique ciblé ;
- une règle méthodologique change la lecture d’un résultat → réaudit scientifique ciblé ;
- une portée philosophique a été importée dans la méthode sans qualification → retour méthodologique ciblé ;
- une transformation intellectuelle reste inexpliquée → remontée des matériaux généalogiques pertinents ;
- le contre-audit reproduit un faux déclassement, une fausse promotion ou un faux raccord → réouverture du chantier nécessaire.

Toute réouverture identifie :

```text
DECLENCHEUR
CONCLUSION_PRECEDENTE_A_RETESTER
NOUVEAU_PERIMETRE_SUBSTANTIEL_MINIMAL
POURQUOI_LA_QUALIFICATION_PRECEDENTE_NE_SUFFIT_PLUS
```

Aucun audit qualifié n’est irrévocable. Une résurgence significative est enregistrée avant de décider si elle exige ou non une réouverture substantielle.

---

## 6. Profondeur, couverture et arrêt

Deux dimensions sont désormais séparées.

### Couverture documentaire

```text
corpus auditable
-> lecture integrale des documents
-> remontee dans le changelog
-> aucune exclusion avant lecture
```

La couverture ne s’arrête pas parce qu’un README, un titre ou une synthèse paraît suffisant.

### Profondeur substantielle

```text
element remonte
-> question examinee
-> premisses necessaires
-> supports de ces premisses
-> approfondissement si une premisse reste non qualifiee
-> STOP local lorsque la conclusion propre de l'audit devient qualifiable dans le perimetre declare
```

Ce `STOP` substantiel ne transforme pas un document non lu en document sans effet et ne qualifie pas automatiquement l’effet de l’audit sur un autre chantier.

Un audit peut s’arrêter avec `NON_DECIDABLE` seulement après avoir explicité l’instruction tentée et la limite qui empêche de trancher avec les matériaux, accès ou périmètre autorisés. Ce résultat reste visible comme tel.

---

## 7. Amendement de la séquence

Ajouter une étape, scinder ou fusionner un audit, modifier l’ordre ou introduire un nouvel état exige d’établir :

1. la confusion, dépendance ou risque concret insuffisamment contrôlé par la structure actuelle ;
2. la conséquence possible de cette insuffisance ;
3. la discrimination, protection ou décision nouvelle rendue possible par l’amendement ;
4. pourquoi une simple précision d’une étape existante ne suffit pas.

Test d’ablation : si retirer l’amendement ne change aucune décision possible, aucune protection ou aucune capacité de falsification, l’amendement n’est pas justifié.

La règle d’exhaustivité documentaire introduite le 17 août 2026 constitue une **précision transversale de couverture**, pas une nouvelle étape : son apport a été reproduit par des cas où le routage vivant masquait des matériaux pertinents (notamment C7 et C3), puis étendu par décision humaine en raison de la non-linéarité possible du projet.

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

CHANGELOG VIVANT DE L'AUDIT INTEGRAL
= couverture lue, remontees, resurgences, dettes et reductions justifiees

ISSUES
= executions bornees, preuves, arbitrages, blocages, resultats locaux

PR / GIT
= mutations du corpus et historique exact
```

Un éventuel GitHub Project peut représenter visuellement ces états mais ne devient pas une autorité scientifique, conceptuelle ou méthodologique par lui-même.

Les statuts transitoires de PR, branches ou opérations en cours restent dans GitHub ; ils ne doivent pas être recopiés dans ce document vivant sauf s’ils changent durablement la structure ou l’autorité du programme.

---

## 9. État courant du programme après décision d’exhaustivité documentaire

```text
SEQUENCE_D_AUDITS = VALIDEE_COMME_BASE_DE_TRAVAIL
COUVERTURE_DOCUMENTAIRE_EXHAUSTIVE = REQUISE
CHANGELOG_AUDIT_INTEGRAL = REQUIS
AUDITS_SUBSTANTIELS = NON_OUVERTS_PAR_CE_DOCUMENT

TRAVAUX_DOCUMENTAIRES_ANTERIEURS = EXISTENT
QUALIFICATION_DE_CES_TRAVAUX_COMME_ETAPE_1 = NON_ETABLIE
PORTEE_DES_RESULTATS_ANTERIEURS = A_RETESTER_APRES_REMONTEE
```

La première utilisation substantielle de ce programme doit d’abord établir le corpus auditable et son manifeste de couverture. Elle ne transforme pas rétrospectivement les travaux antérieurs en preuves qu’ils n’avaient pas pour fonction d’établir.