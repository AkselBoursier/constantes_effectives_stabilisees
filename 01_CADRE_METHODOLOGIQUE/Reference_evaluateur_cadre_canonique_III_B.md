# Référence évaluateur — cadre canonique pour la Phase III-B

## 0. Statut expérimental

Cette pièce est une **clé d'évaluation** de la tâche scientifique III-B. Elle reconstruit le cadre courant à partir des surfaces actives de `main` et de leurs décisions de rang.

Elle ne doit pas être fournie aux agents testés, ni copiée dans leur bootstrap, ni utilisée pour leur indiquer les chemins qu'ils doivent découvrir.

```text
FONCTION = REFERENCE_EVALUATEUR
VISIBLE_AGENT_TESTE = NON
AUTORITE_NORMATIVE_NOUVELLE = NON
SOURCE = DOCUMENTS_ACTIFS_ET_DECISIONS_DE_MAIN
PHASE_III_B = NON_LANCEE
```

Cette référence n'affirme pas qu'un fichier unique du dépôt constitue « le cadre ». Elle gèle pour le scoring les distinctions dont le rang courant est suffisamment établi pour juger une réinstruction du cycle 10.

## 1. Hiérarchie minimale des surfaces à reconstruire

Un agent performant doit retrouver un ensemble cohérent de surfaces actuelles et distinguer leur fonction.

### Orientation publique courante

- `README.md` : deux questions actuelles, distinction minimale constance/stabilisation et routage.
- `05_CARTES_ET_SYNTHESES/Vue_ensemble_une_page_v0_3.md` : vue humaine issue des cinq contrastes ; trois dimensions couplées sans ordre universel.
- `05_CARTES_ET_SYNTHESES/Controle_consolidation_cinq_contrastes_v0_1.md` : contrôle du changement de centre et des désynchronisations documentaires.

### Noyau conceptuel et décisions actives

- `01_CADRE_METHODOLOGIQUE/refondation-du-domaine.md` : déclaré noyau canonique actif de la refondation.
- `01_CADRE_METHODOLOGIQUE/Decision_statuts_constance_acces_constitution_v0_1.md` : décision canonique active sur objet / accès / constitution.
- `GLOSSAIRE.md` : référence rapide explicitement subordonnée aux décisions actives.
- `05_CARTES_ET_SYNTHESES/Verdict_final_audit_portee_regimes_constance_v0_1.md` : verdict validé le 20 juillet 2026 sur les ajustements de portée.

### Pan philosophique et strates antérieures

Les documents de `06_PHILOSOPHIE` et plusieurs synthèses anciennes constituent une partie importante de la genèse du cadre. Ils n'acquièrent pas pour autant une autorité présente uniforme.

La branche Git `philosophie` elle-même est un état antérieur : sa tête observée est le commit `18a193d0984580db3d07a4d34dcafbb09ea810e0` du 11 juillet 2026. Plusieurs formulations qui y figurent ont ensuite été intégrées, corrigées, bornées ou déclassées sur `main`.

Un agent qui traite « branche philosophie = canon courant » sans contrôler les décisions ultérieures échoue au test de rang documentaire.

## 2. Centre actuel du projet

Le projet ne cherche plus principalement à déterminer quelles grandeurs « méritent » le nom de constante, ni à défendre une classe de « constantes effectives stabilisées ».

Deux questions publiques organisent le travail :

1. **Frontière** — comment les sciences établissent-elles, utilisent-elles et déplacent-elles la frontière entre ce qui varie et ce qui tient ?
2. **Détermination et enquête** — par quelles structures, opérations et chemins de détermination un maintien devient-il opératoire ou affirmable dans un régime, et que change cette reconstruction pour l'enquête scientifique ?

La question de qualification d'une grandeur comme constante reste un contrôle local nécessaire lorsqu'une attribution de constance est réellement formulée. Elle n'est plus le centre exclusif du projet.

La question de formation reste légitime et active : comment un statut, un régime ou une relation se forme, se maintient, se transforme ou se défait ? Elle ne possède pas de priorité universelle sur l'objet ou l'accès.

## 3. Constance et stabilisation

### Constance

La constance est une **attribution conditionnée d'un maintien à une cible explicitement identifiée**.

Un énoncé de constance doit être indexé par les éléments pertinents du cas :

```text
porteur / cible
+ transformation
+ régime / domaine
+ échelle, schéma ou modèle lorsque pertinents
+ tolérance / ordre
+ condition de rupture, refus ou suspension
```

La notation historique de travail `C(P | R, T, epsilon)` reste recevable comme contrôle d'indexation, non comme loi physique.

### Stabilisation

La stabilisation est un terme méthodologique de second ordre : établissement, consolidation ou maintien des conditions grâce auxquelles un état, un régime, une réalisation, une estimation, une chaîne probatoire ou une attribution devient opératoire ou soutenable selon un critère déclaré.

```text
STABILISATION != CONSTANCE_DE_LA_CIBLE
STABILISATION != CONSTITUTION
STABILISATION != EXPLICATION_PAR_ELLE_MEME
```

Une dynamique qui fait tendre une variable vers une valeur peut donc constituer un mécanisme ou une quasi-stationnarité sans établir automatiquement un statut de constance de l'objet.

## 4. Trois statuts canoniques de constance

Le noyau actif conserve trois statuts analytiques :

1. **constance physique** : maintien ou invariance physique d'une grandeur, relation ou structure sous transformations déclarées dans un domaine ;
2. **constance effective** : énoncé dans lequel un coefficient ou une relation est traité comme fixe dans une approximation contrôlée, avec ordre, tolérance, corrections et rupture explicites ;
3. **constance métrologique** : énoncé portant sur une valeur numérique fixée exactement dans un système d'unités, sans assimilation à une mesure parfaite ni à une invariance physique démontrée.

`Constante effective` n'est plus une espèce transverse d'objets propre au projet. Une reconstruction, une borne, une quasi-stationnarité, un paramètre fixé dans un ajustement ou un coefficient générique ne reçoit pas automatiquement le statut de constance effective.

## 5. Objet, accès et constitution

Distinction canonique :

```text
constance de l'objet ou de la cible
!=
stabilisation de l'accès ou de l'estimation
!=
mode de constitution ou d'organisation
```

### Objet

Ce qui est effectivement qualifié : grandeur, relation, observable, coefficient, secteur, prédiction ou structure, selon la question.

### Accès

Opérations par lesquelles une valeur, une borne ou un domaine admissible deviennent attribuables : mesure, reconstruction, ajustement, inférence, comparaison, réalisation, etc.

L'accès participe à la qualification mais ne devient ni essence de la grandeur ni producteur universel de l'objet.

### Constitution

Structures ou mécanismes par lesquels une relation, un secteur ou un régime deviennent opératoires : symétrie, seuil, architecture, dynamique, couplage, organisation.

Une constitution peut produire ou canaliser une fixité, mais il faut encore établir la grandeur concernée, le bassin, la durée, la tolérance, les corrections, les coûts en paramètres/énergie et les conditions d'échec avant toute conclusion sur la constance de l'objet.

### Non-linéarité

Les trois dimensions peuvent se contraindre mutuellement : une difficulté d'accès peut reformuler l'objet ; un mécanisme constitutif peut révéler la transformation pertinente ; une différence d'objet peut interdire une comparaison d'accès.

Aucun ordre universel n'est canonique.

## 6. Transformation, chemin et portée

La transformation pertinente doit être déclarée avant une affirmation de constance ou de variation. Temps, énergie, échelle de renormalisation, changement de régime, convention, accès, paramétrisation et contrefactuel ne sont pas substituables.

Lorsque cela change l'argument, le chemin doit être typé : physique, historique, expérimental/métrologique, computationnel, inférentiel, représentationnel ou autre catégorie disciplinaire justifiée.

Explorer formation, constitution, accès, histoire ou mécanisme ne donne pas automatiquement le droit d'élargir la portée de l'énoncé.

La portée physique, épistémologique ou ontologique demande des arguments distincts. Une portée non engagée est une sortie recevable.

## 7. Discipline probatoire

Le cadre courant exige de maintenir séparés :

```text
calcul
!= sortie machine
!= qualification technique
!= résultat scientifique
!= soutien probatoire
!= verdict scientifique
!= interprétation
!= décision programmatique ou éditoriale
```

Un résultat négatif, une borne, une non-détection, un blocage ou une stratégie non productive peuvent être fortement informatifs sans devenir verdict positif sur l'objet.

Une non-détection n'est discriminante que pour les familles d'alternatives auxquelles le dispositif possède effectivement une puissance déclarée.

## 8. Vocabulaire disciplinaire et vocabulaire du projet

Le vocabulaire disciplinaire local est premier. Les termes transversaux du projet n'ont droit d'usage que s'ils ajoutent un gain discriminant et n'écrasent pas les notions du domaine.

Le nom historique `constantes_effectives_stabilisees` ne constitue plus une thèse ni une taxonomie.

Les anciennes catégories telles que `reconstruit`, `borné`, `constitutif` ou certains « modes de constance » peuvent rester utiles comme descriptions locales ou généalogiques ; elles ne doivent pas être réactivées comme statuts canoniques de constance de l'objet.

## 9. Place du pan philosophique

Le pan philosophique fournit des instruments, des voisinages, des contrôles de rang et des questions. Il ne constitue pas une doctrine qui commande par défaut les dossiers physiques.

L'état consolidé a placé les développements philosophiques antérieurs en **quarantaine sélective** : non supprimés, disponibles comme matériau, réactivables sur question précise, mais non directeurs par défaut pour l'enquête physique.

La philosophie peut modifier le cadre actif lorsqu'un élément a passé les circuits de validation et de rang correspondants ; sa simple présence dans la branche ou dans une synthèse ne suffit pas.

## 10. Supersessions que l'agent devrait être capable de reconnaître

### Ancien centre de qualification

Des documents antérieurs organisaient l'ensemble du projet autour de :

```text
Q-qual : dans quelle mesure une grandeur peut-elle être qualifiée de constante ?
```

Cette question reste utile localement, mais les cinq contrastes ont déplacé le centre vers les deux questions actuelles de frontière et de transformation de l'enquête.

### Ancien T0 et anciens modes

La formule de `stabilisation effective située` et la matrice historique `T1–T10` ont été fécondes. Elles ne doivent pas être restaurées comme canon intégral.

Le cadre actuel a séparé :

```text
constance de l'objet
stabilisation de l'accès / attribution
constitution
portée
```

et requalifié les anciennes catégories `reconstruit`, `borné`, `constitutif`, etc.

### Question de formation

Une ancienne séquence pouvait suggérer « droit d'abord, genèse ensuite ». L'état courant conserve la distinction droit/genèse mais refuse un ordre universel de recherche : le terrain peut exiger de commencer par la constitution, l'objet ou l'accès.

## 11. Référence de réinstruction du cycle 10

Le scoring ne présuppose pas une réécriture unique, mais une réponse solide doit au minimum examiner les points suivants.

### 11.1 Cible et transformations

Identifier ce que les documents calculent effectivement : champ scalaire, déplacement de `v`, énergie du condensat, taux de dissipation, abondance/relique et observables/contraintes associées.

Distinguer l'axe temporel d'une solution, l'axe de scan paramétrique et une histoire physique réellement établie.

### 11.2 Résultats des phases 2 et 3

Les scans négatifs restent des **résultats conditionnels informatifs** dans les modèles étudiés.

Ils soutiennent l'échec des architectures conservatrices testées sous leurs hypothèses. Ils n'excluent pas tous les portails scalaires ni toute dynamique électrofaible.

Le fait que `v` converge ou devienne quasi stationnaire appartient d'abord au mécanisme/à la constitution et à la trajectoire calculée ; il ne suffit pas à établir une constance effective de `v`.

### 11.3 Résultat de phase 4

La fenêtre dissipative non vide reste un résultat computationnel/physique conditionnel du toy model phénoménologique : certains profils prescrits de dissipation rendent compatibles, dans les approximations déclarées, variation ancienne, transfert d'énergie, quasi-fixité avant BBN, relique limitée et entropie contrôlée.

Elle n'établit pas :

- un mécanisme microscopique réalisé ;
- l'existence d'un canal concret satisfaisant le profil ;
- l'histoire réelle de notre univers ;
- une probabilité physique tirée de la densité des points du scan ;
- une explication achevée de la valeur électrofaible.

### 11.4 Ce qui reste ouvert

La dette principale est la réalisation microscopique de la dissipation et son coût complet : couplages, seuils, thermalisation, contraintes de mélange/cinquième force/rayonnement caché, robustesse et prise empirique.

Cette dette n'est pas automatiquement autorisée comme nouveau calcul par la réinstruction III-B.

### 11.5 Conservation non destructive

La réinstruction ne doit pas réécrire rétroactivement les calculs, scans ou résultats pour leur faire parler le vocabulaire actuel.

Sorties attendues :

```text
CONSERVER_COMME_RESULTAT_LOCAL
REQUALIFIER_LE_RANG_OU_LA_PORTEE
DECLASSER_COMME_FORMULATION_HISTORIQUE
MAINTENIR_OUVERT
NON_ETABLI
```

Une conclusion « aucune modification substantielle de ce résultat » est recevable si elle est argumentée.

## 12. Critère de réussite de récupération canonique

Un agent n'a pas besoin de reproduire mot pour mot cette référence ni de lire tous les documents listés.

La récupération est réussie s'il :

1. retrouve une route courante suffisante ;
2. distingue cette route de strates historiquement fécondes mais requalifiées ;
3. reconstruit les distinctions nécessaires au cycle 10 ;
4. montre les conséquences de ces distinctions sur les résultats réels ;
5. déclare honnêtement ce qui resterait non établi.

Une réponse qui récite le vocabulaire actuel sans retrouver l'autorité ni modifier correctement les qualifications du cycle n'obtient pas le niveau maximal.
