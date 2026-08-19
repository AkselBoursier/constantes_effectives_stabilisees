# Programme vivant des audits

## Fonction et rang

Ce document porte la **séquence de contrôle du projet** : types d’audits, dépendances, états, critères d’arrêt, d’approfondissement et de réouverture, ainsi que les conditions d’amendement de cette séquence.

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

Une rubrique inconnue reste `NON_ETABLI` ; elle n’est pas remplie par vraisemblance.

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
CORPUS_DE_REFERENCE_EXACT = A_ETABLIR_PAR_MANIFESTE
```

En conséquence, la **lecture documentaire du corpus de référence est exhaustive**. Tant que son manifeste exact n’est pas établi, aucune pièce ne peut être exclue par pertinence supposée, catégorie, titre, rang, emplacement ou routage. Un audit de surface, un README, une synthèse ou un inventaire de titres ne peuvent remplacer la lecture du contenu pour exclure un document.

Cette exhaustivité documentaire ne signifie pas réauditer scientifiquement, computationnellement, méthodologiquement ou philosophiquement chaque contenu avec la même profondeur. Après lecture intégrale et remontée dans le changelog d’audit, l’approfondissement substantiel reste commandé par les résultats, dépendances, contradictions, dettes et falsificateurs effectivement identifiés.

La réduction progressive du corpus actif est donc autorisée **après remontée**, jamais avant.

### 1.6 Pas d’approfondissement gratuit, pas de fermeture gratuite

La présence d’un matériau impose sa couverture dans la lecture documentaire exhaustive ; elle n’impose pas automatiquement une réinstruction substantielle complète.

Un audit substantiel s’approfondit lorsqu’une conclusion importante dépend d’un élément non qualifié, lorsqu’un résultat remonté exige vérification, lorsqu’un contre-exemple reproduit montre qu’une conclusion est insuffisamment soutenue, ou lorsqu’une résurgence modifie la carte des dépendances.

Réciproquement, aucune lecture achevée ni aucun périmètre courant ne ferme par principe la possibilité de réauditer un cycle ou un volet lorsque le changelog ou un audit ultérieur fait surgir une raison matérielle de le faire.

### 1.7 Méta-règle de cartographie et d’instruction adaptative

La cartographie disponible constitue le point de départ le plus économique de
l’instruction suivante, mais elle ne constitue jamais un filtre exclusif ni une
limite immuable. Toute étape doit garder son but propre et respecter les
contrôles qui lui sont nécessaires ; elle peut toutefois adapter son chemin au
contexte, aux résultats remontés, aux lacunes, aux contradictions, aux
dépendances et aux falsificateurs effectivement rencontrés.

```text
CARTOGRAPHIE_EXISTANTE = POINT_DE_DEPART, NON_EXCLUSION
ETAPE_EN_COURS = BUT_A_PRESERVER, CHEMIN_ADAPTABLE
REGLE_DE_TRAVAIL = NON_EXCLUSIVE, NON_IMMUTABLE, CONTEXTUELLE
RETOUR_CIBLE = AUTORISE_SI_MATERIELLEMENT_JUSTIFIE
RELECTURE_OU_TRIANGULATION = PROPORTIONNEE_A_LA_QUESTION
ARRET = DES_QUE_LA_QUESTION_EST_SUFFISAMMENT_INSTRUITE_DANS_SON_PERIMETRE
```

Cette méta-règle ne remplace aucune étape, aucun critère d’arrêt, aucun
contre-test ni aucune condition de réouverture. Elle interdit seulement de
traiter un point d’entrée, une sentinelle, une séquence initiale ou une
réduction de corpus comme l’unique chemin légitime. Une adaptation doit être
motivée dans le changelog par la question poursuivie, l’élément déclencheur,
ce qui est conservé, ce qui est ajouté ou repris, et la condition d’arrêt.

Elle s’applique transversalement aux étapes `0–9`, aux co-instructions et aux
retours ciblés, sous réserve de la portée propre de chaque audit. Elle ne donne
pas à une étape le pouvoir de promouvoir seule une hypothèse, un résultat ou
une décision relevant d’un autre rang.

### 1.8 Journalisation séquencée par phase

Le changelog vivant peut être réparti en journaux stables correspondant à une
phase complète lorsque la longueur, la continuité de lecture ou la fonction de
contrôle le justifie. Cette répartition est technique et ne doit produire ni
perte, ni résumé substitutif, ni rupture de provenance.

```text
UNITE_DE_JOURNAL = PHASE_COMPLETE_OU_LOT_COHERENT
REGLES_D_ECRITURE = HERITEES_ET_EXPLICITES_DANS_CHAQUE_PHASE
RACCORD_INTER_PHASES = OBLIGATOIRE
DUPLICATION_DES_ENTREES = INTERDITE_SAUF_GAIN_DE_CONTROLE_EXPLICITE
DEPLACEMENT_D_UNE_ENTREE = PROVENANCE_ET_REFERENCE_CONSERVEES
NOM_DU_FICHIER = STABLE_PENDANT_LA_PHASE
```

Un journal de phase conserve les mêmes exigences que le changelog intégral :
résultats positifs et négatifs, limites, dettes, contradictions, bifurcations,
triangulations, incidents, effets sur les décisions et états `NON_ETABLI` ou
`NON_DECIDABLE`. Il peut renvoyer à une entrée antérieure déjà complète au lieu
de la recopier, à condition d'indiquer le fichier, la phase, le point de
raccord et la raison de cette non-duplication.

La création d'un journal de phase ne clôt pas la phase, ne crée pas une
nouvelle autorité et ne rend pas immuable son organisation. Une phase peut
rester dans un journal unique ou être subdivisée seulement si ce choix apporte
un gain réel de contrôlabilité ; le programme et le changelog doivent alors
conserver la généalogie du choix.

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
CORPUS_DE_REFERENCE_A_COUVRIR
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

`CORPUS_DE_REFERENCE_A_COUVRIR` décrit ce qui doit être lu intégralement et ne peut être réduit par pertinence supposée avant lecture. `PERIMETRE_SUBSTANTIEL_INITIAL` décrit seulement où commence la réinstruction approfondie ; il ne constitue jamais un filtre documentaire d’exclusion.

Les contre-tests doivent être adaptés à la nature de l’audit. Leur fonction est d’empêcher qu’une conclusion soit qualifiée sans exposition suffisante à une alternative, un cas négatif, une ablation ou un falsificateur pertinent. Lorsqu’aucun contre-test de ce type n’est applicable, cette absence doit être justifiée plutôt que supposée.

La fiche doit rester aussi courte que le permet la contrôlabilité réelle de l’audit. Les issues peuvent porter son exécution détaillée ; elles ne remplacent pas ce programme comme vue de la séquence générale.

Le changelog vivant `changelog_audit_integral.md` est obligatoire pour les investigations engagées sous cette règle de couverture. Il est mis à jour au minimum après chaque investigation complète d’un cycle et à chaque résurgence significative susceptible de modifier une lecture, une dette, une relation ou une décision.

---

## 4. Séquence provisoire

Cette séquence exprime des dépendances de travail, non une chaîne irréversible. Les retours ciblés de la section 5 en font partie.

| Étape | Audit | Fonction / question principale |
|---|---|---|
| **0** | **Cadrage du programme** | Fixer questions, couverture documentaire, dépendances, sentinelles éventuelles, contre-tests, critères d’arrêt, d’approfondissement et de réouverture. Le présent document est le premier résultat de ce cadrage ; il n’ouvre aucun audit substantiel. |
| **1** | **Documentaire d’orientation et de couverture** | Localiser les pièces, distinguer routes vivantes, rangs revendiqués et états datés, puis établir le manifeste exhaustif du corpus de référence. Des travaux documentaires antérieurs, notamment ceux ayant conduit à #124 et #126, existent comme matériaux candidats ; leur qualification comme réalisation partielle de cette étape reste à établir sous le présent programme. Cet audit ne décide pas de la justesse scientifique, conceptuelle ou philosophique. |
| **2** | **Scientifique des résultats porteurs** | En application de la méta-règle 1.7, partir des résultats, dettes, dépendances et contradictions effectivement remontés par l’étape 1, puis vérifier en profondeur ce que les résultats effectivement porteurs établissent réellement et si leur qualification suffit à l’usage envisagé. Le corpus de l’étape 1 n’est pas relu par défaut, sans que cette économie devienne une exclusion. Une lacune, contradiction ou dépendance non qualifiée déclenche une triangulation ciblée avec les issues, fichiers, commentaires de PR, commits ou autres pièces pertinentes ; son nombre n’est pas plafonné a priori, mais elle s’arrête dès que la question locale est suffisamment instruite. Le caractère « porteur » n’est pas présupposé par la sélection initiale, le rang documentaire ou le routage. |
| **3** | **Conceptuel** | Identifier les questions, distinctions et fonctions intellectuelles réellement portées, puis tester ce qu’elles sont devenues : conservées, partiellement conservées, transformées avec gain ou perte, encore fécondes, dépassées, perdues/non réassimilées ou non décidables. Le test porte sur la fonction discriminante, pas sur la survie d’un mot. Le corpus de référence est couvert intégralement avant toute exclusion documentaire. |
| **4** | **Méthodologique** | Tester si les règles et distinctions actuelles sont justifiées au regard des problèmes, discriminations, risques et supports effectivement établis, ou si elles sont seulement locales, redondantes, trop fortes, mal placées, non justifiées ou non décidables. Une règle n’est ni dérivée automatiquement des résultats scientifiques ni justifiée par sa seule cohérence interne. |
| **5** | **Philosophique** | Distinguer propositions, portées et transferts entre philosophie, science et méthodologie. `COMPATIBLE != DERIVE_DE`. Les matériaux philosophiques, éditoriaux et généalogiques sont repérés à partir de la couverture intégrale du corpus de référence ; aucun emplacement ni rang documentaire ne permet de les filtrer avant lecture. |
| **6** | **Cohérence intellectuelle** | Tester si questions de recherche, résultats retenus, distinctions conceptuelles, choix méthodologiques et propositions philosophiques composent un programme dont les transitions sont justifiées plutôt que reconstruites a posteriori. Rechercher aussi les continuités réelles masquées, les acquis sous-exploités et les tensions fécondes. |
| **7** | **Cohérence générale / transversale** | Après qualification suffisante des couches concernées, contrôler les relations pertinentes : questions ↔ résultats, résultats ↔ concepts, concepts ↔ méthode, science ↔ philosophie, philosophie ↔ méthode, documents/issues ↔ état substantiel réel. La couverture documentaire déjà consignée évite de confondre absence de lecture et absence de relation. |
| **8** | **Contre-audit** | Tenter activement de falsifier les conclusions précédentes de manière bilatérale : surpromotion **et** écrasement, continuité artificielle **et** continuité réelle devenue invisible, concept inutile **et** concept dont l’ablation fait perdre une discrimination, résultat surinterprété **et** sous-exploité. Cette étape complète les contre-tests locaux ; elle ne les remplace pas. |
| **9** | **Normalisation documentaire Human-First** | Seulement lorsque les dépendances substantielles d’une transformation sont suffisamment qualifiées et que la couverture nécessaire est consignée : documents vivants humains, routage agent minimal, noms stables, réécriture positive, réduction de méta-documentation, archivage et suppression exceptionnelle. |

### Règle Human-First : représentation publique et laboratoire

La phase 9 distingue deux fonctions documentaires qui ne doivent pas être
fusionnées :

```text
DOCUMENT_PUBLIC_HUMAN_FIRST = ETAT_COURANT_LISIBLE, LANGAGE_NATUREL, FONCTION_ET_PORTÉE
LABORATOIRE = PROVENANCE, GENEALOGIE, JOURNAUX, DETTES, TUYAUTERIE, ETATS_DATÉS
```

Les documents d’accueil, de distribution et les documents destinés à une
lecture humaine courante décrivent d’abord ce que le projet est, ce qu’il
examine, ce qu’il établit et dans quelles limites. Ils ne racontent pas par
défaut l’histoire de fabrication du dépôt, la séquence des agents, les étapes
de l’audit ou les opérations de maintenance. Une généalogie peut être proposée
dans une annexe ou une route séparée, clairement optionnelle et sans conditionner
la compréhension de l’état courant.

Cette règle ne demande ni un état figé ni l’effacement de l’histoire. Elle impose
une séparation de vues : l’état public courant reste révisable, tandis que la
provenance et la tuyauterie restent récupérables dans les journaux, archives,
issues et Git. Toute suppression ou réduction de contenu doit continuer à
respecter les contrôles de contenu unique, fonction probatoire et récupérabilité.

```text
LANGAGE_PUBLIC = POSITIF, DESCRIPTIF, NATUREL
HISTORICITE_DANS_L_ACCUEIL = OPTIONNELLE, NON_IMPOSEE
TUYAUTERIE_DANS_LA_DISTRIBUTION = A_RELEGUER_HORS_FLUX_PRINCIPAL
ETAT_COURANT = REVISABLE, NON_FIGE
PROVENANCE = CONSERVEE, NON_PROPAGEE_PAR_DEFAUT
```

Test d’ablation : si cette séparation est retirée, la lisibilité publique et la
traçabilité du laboratoire sont mises en concurrence ; si elle est conservée,
les deux fonctions restent accessibles avec des coûts de lecture différents.
La règle est un contrôle de représentation Human-First, non une autorisation
de réécriture ou de suppression immédiate.

### Consolidation éditoriale sémantique

La réduction documentaire de la phase 9 ne désigne ni une compression
quantitative, ni une concaténation mécanique de fichiers, ni une suppression
des versions. Le terme de travail retenu est :

```text
CONSOLIDATION_EDITORIALE_SEMANTIQUE
```

Elle consiste à reconstruire, pour un public et une fonction dominants, un
document plus clair à partir de plusieurs pièces, en faisant remonter leur
contenu intellectuel, scientifique, méthodologique ou éditorial pertinent.
Elle peut réduire le nombre de documents actifs, mais son critère premier est
la conservation et l'amélioration de la structure de sens.

```text
SOURCES_LUES_ET_CARTOGRAPHIEES
-> FONCTION_DOMINANTE_ET_PUBLIC
-> RANGS, RESULTATS, LIMITES ET TRANSITIONS
-> TEXTE_CONTINU_RECOMPOSE
-> CONTROLE_DE_PERTE_ET_DE_PORTEE
-> ROUTE_DE_PROVENANCE
```

Une consolidation réussie conserve les distinctions qui changent un verdict,
rassemble les éléments complémentaires sans fabriquer une cohérence absente,
remplace la juxtaposition par une progression lisible et adapte le ton, la
longueur et le degré de détail à la classe du document. Les généalogies et
états datés restent récupérables sans être imposés au lecteur.

```text
COMPRESSION_QUANTITATIVE_SEULE = INSUFFISANTE
CONCATENATION_MECANIQUE = REFUSEE
CONSOLIDATION_SEMANTIQUE = A_TESTER
FUSION_SANS_MATRICE_DE_PERTE = NON_AUTORISEE
ARCHIVAGE_DES_VERSIONS = DECISION_HUMAINE_SEPAREE
```

Le test d'ablation compare le document consolidé aux sources : contenu unique,
rang, limite, contradiction, bifurcation, résultat négatif et condition de
réouverture doivent rester retrouvables. Une réduction de longueur sans gain de
compréhension ou de contrôle est refusée ; un document trop large est subdivisé
par fonction plutôt que simplement raccourci.

### Co-instruction bornée des étapes 2 et 3

Les étapes 2 et 3 ne forment pas une dérivation simple `2 -> 3`.

La lecture documentaire exhaustive de l’étape 1 peut faire remonter des résultats, questions ou fonctions intellectuelles que les routes courantes ne signalaient pas. L’audit scientifique repart de cette remontée et détermine lesquels exigent une qualification scientifique approfondie ; il ne réouvre pas par défaut la lecture des pièces déjà couvertes, conformément à la méta-règle 1.7, sans transformer cette économie en exclusion. Une lacune, contradiction ou dépendance non qualifiée justifie une triangulation ciblée avec les sources pertinentes ; le recoupement reste sans plafond numérique a priori, mais sans prolifération gratuite et avec arrêt local dès que la question est suffisamment instruite. L’audit conceptuel peut à son tour révéler qu’un résultat omis, une ancienne question ou une fonction intellectuelle impose un retour scientifique ciblé. Inversement, la qualification scientifique peut invalider ou réduire une relation conceptuelle présumée.

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
corpus de reference manifeste
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

CHANGELOGS DE PHASE
= execution sequentielle d'une phase complete, avec raccord sans perte

ISSUES
= executions bornees, preuves, arbitrages, blocages, resultats locaux

PR / GIT
= mutations du corpus et historique exact
```

Un éventuel GitHub Project peut représenter visuellement ces états mais ne devient pas une autorité scientifique, conceptuelle ou méthodologique par lui-même.

Les statuts transitoires de PR, branches ou opérations en cours restent dans GitHub ; ils ne doivent pas être recopiés dans ce document vivant sauf s’ils changent durablement la structure ou l’autorité du programme.

Un changelog de phase peut devenir l'instrument courant de la phase concernée.
Il doit alors rappeler les règles héritées, pointer vers le changelog antérieur,
indiquer son manifeste de départ et maintenir un raccord explicite lors de la
clôture. Le changelog intégral historique n'est pas réécrit pour créer cette
séparation.

---

## 9. État courant du programme après décision d’exhaustivité documentaire

```text
SEQUENCE_D_AUDITS = VALIDEE_COMME_BASE_DE_TRAVAIL
COUVERTURE_DOCUMENTAIRE_EXHAUSTIVE = REQUISE
CORPUS_DE_REFERENCE_EXACT = A_ETABLIR_PAR_MANIFESTE
CHANGELOG_AUDIT_INTEGRAL = REQUIS
AUDITS_SUBSTANTIELS = NON_OUVERTS_PAR_CE_DOCUMENT

TRAVAUX_DOCUMENTAIRES_ANTERIEURS = EXISTENT
QUALIFICATION_DE_CES_TRAVAUX_COMME_ETAPE_1 = NON_ETABLIE
PORTEE_DES_RESULTATS_ANTERIEURS = A_RETESTER_APRES_REMONTEE
```

La première utilisation substantielle de ce programme doit d’abord établir le manifeste exact du corpus de référence sans exclusion préalable par pertinence supposée. Elle ne transforme pas rétrospectivement les travaux antérieurs en preuves qu’ils n’avaient pas pour fonction d’établir.
