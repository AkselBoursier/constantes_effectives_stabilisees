# Cartographie sélective des transitions conversationnelles v0.1

## 0. Statut

```text
type : extraction sélective de provenance ;
corpus : trois archives conversationnelles assainies, 278 messages au total ;
période couverte : 8 au 16 juillet 2026 ;
fonction : restituer les bifurcations, continuités, abandons, ajournements et
           non-décisions qui éclairent l'état actuel du projet ;
rang : consolidation de provenance, subordonnée aux décisions et documents actifs ;
validation : reconstruction générale non exhaustive validée le 16 juillet 2026
             pour instruire un premier essai réflexif borné ;
effet immédiat : aucun changement de doctrine, de rang documentaire ou de
                 résultat scientifique.
```

Cette cartographie ne résume pas intégralement les conversations. Elle extrait
les passages où la direction de recherche, la méthode, le périmètre ou le mode
de travail changent de manière suffisamment nette pour expliquer un document
ou une décision ultérieurs.

Elle ne cherche pas à répartir la propriété intellectuelle. Les rôles affichés
dans l'interface renseignent la provenance textuelle d'une formulation, non la
distribution complète des intuitions antérieures, de l'orientation, de la
recherche, de la rédaction, de la sélection et de la validation.

## 1. Corpus et mode de lecture

### 1.1 Références stables

Les trois fichiers structurés au format JavaScript Object Notation (JSON) sont
désignés ainsi :

| Référence | Archive | Messages | Période |
|---|---|---:|---|
| `A1` | *Recherche sur les constantes* | 112 | 8–9 juillet 2026 |
| `A2` | *Analyse cohérence projet* | 99 | 12–14 juillet 2026 |
| `A3` | *Travail collaboratif projet GitHub* | 67 | 14–16 juillet 2026 |

`A2-M56` désigne le cinquante-sixième message du tableau `messages` de la
deuxième archive. Une plage telle que `A3-M7–M10` comprend tous les tours de
cette séquence, quels que soient leurs rôles affichés.

Cette numérotation commence à 1 et reste liée aux copies assainies dont les
empreintes sont consignées dans l'[accueil des archives
conversationnelles](../92_ARCHIVES_CONVERSATIONNELLES/README.md). Elle évite de
confondre l'ordre de lecture avec une hiérarchie d'autorité.

L'ancienne [extraction détaillée des questions des cycles 1 à
3](Extraction_questions_conversation_cycles_1_a_3_v0_1.md) emploie les indices
techniques commençant à 0. Son `message 62` correspond donc ici à `A1-M63`.

### 1.2 Trois degrés de certitude

| Qualification | Usage dans cette carte |
|---|---|
| **Explicite** | la correction, la validation, l'abandon ou l'ajournement est formulé directement dans l'échange |
| **Fortement étayé** | plusieurs tours convergent et la transition est matérialisée par des documents ou des opérations ultérieures |
| **Reconstruction prudente** | le rapprochement éclaire la séquence, mais aucune formulation unique ne suffit à l'établir |

Ces degrés qualifient la reconstruction documentaire. Ils ne mesurent ni la
vérité scientifique d'une réponse ni la part intellectuelle d'un participant.

### 1.3 Limites de l'extraction

- Les questions physiques locales de la première archive sont déjà traitées en
  détail dans l'extraction des cycles 1 à 3 ; elles ne sont pas répétées ici.
- Les lignées longues du projet sont déjà décrites dans la [cartographie
  généalogique](Cartographie_genealogique_lignees_projet_v0_1.md) ; la présente
  carte suit seulement leurs déplacements visibles pendant huit jours.
- Les recherches rapportées dans les réponses ne sont pas revérifiées par cette
  opération.
- L'archive 3 s'arrête à `A3-M67`. La décision ultérieure d'archiver les trois
  conversations, la politique des micro-paragraphes de transition et la
  reconstruction finale de la branche ne figurent donc pas dans son contenu.
  Elles ne doivent pas lui être attribuées rétrospectivement.

## 2. Première phase — entrer par les cas

### 2.1 De la question cosmologique générale à une enquête située

| Traces | Déplacement | Qualification |
|---|---|---|
| `A1-M1–M12` | La question initiale associe stabilité tardive, définition antérieure et histoire physique. Oklo passe rapidement du rôle d'entrée possible à celui de jalon empirique latéral, puis sort du cadrage. La littérature récente doit encadrer la question. Le terme « émergence », improvisé lors de la dictée, est retiré jusque dans les formulations négatives qui continuaient à le maintenir actif. | Explicite |

Le premier geste durable n'est donc pas un programme sur Oklo ni une doctrine
de l'émergence. C'est une méthode « par la petite porte » : prendre des objets
déterminés et demander à quelles conditions ils sont définissables,
mesurables, comparables et stables.

### 2.2 Des fiches autonomes avant la comparaison

| Traces | Déplacement | Qualification |
|---|---|---|
| `A1-M13–M61`, surtout `A1-M33–M36` | Les cas sont instruits successivement. Chaque fiche doit tenir par son propre objet ; les comparaisons avec les fiches précédentes sont reportées jusqu'au moment où elles modifient réellement l'argument. | Explicite |

Cette décision explique pourquoi les premiers cycles peuvent paraître
foisonnants : leur fonction initiale est de produire des différences locales,
non de remplir immédiatement une grille comparative uniforme.

### 2.3 La méthode devient elle-même un objet d'épreuve

| Traces | Déplacement | Qualification |
|---|---|---|
| `A1-M62–M106`, surtout `A1-M63–M64` et `A1-M105–M106` | La première méthode est jugée insuffisamment compressive. La distinction entre régime physique et régime d'accès devient nécessaire avant le cycle métrologique. La fixation conventionnelle ne tient pas sur la même échelle que la maturité empirique. Le cycle effectif de basse énergie est ensuite choisi pour tester l'architecture encore provisoire avant de réécrire la méthode. | Explicite et fortement étayé |

Le mouvement important n'est pas la succession des versions. Les objets
forcent la méthode à se différencier : le Système international d'unités (SI)
rend visible la fixation conventionnelle ; les théories effectives obligent à
distinguer dépendance à l'échelle, changement de régime et domaine de validité.

### 2.4 De la limite du clavardage à une infrastructure versionnée

| Traces | Déplacement | Qualification |
|---|---|---|
| `A1-M111–M112` | La saturation de la conversation conduit à demander une architecture de répertoires, un état du projet, une généalogie courte et un ordre de lecture pour un agent local. | Explicite |

GitHub apparaît ici comme une réponse à un problème de continuité et de
navigabilité. Cette transition ne fait pas du dépôt l'auteur de la recherche ;
elle montre qu'une infrastructure documentaire conditionne ce qui peut être
retrouvé, comparé et contrôlé.

## 3. Deuxième phase — auditer, rouvrir, éprouver

### 3.1 L'audit systémique ouvre une seconde question

| Traces | Déplacement | Qualification |
|---|---|---|
| `A2-M1–M14` | La demande porte explicitement sur les tautologies, trivialités et défauts de cohérence. À la question de qualification s'ajoute la formation des constances et son pouvoir explicatif. L'idée d'une « fonction de fixité » est envisagée, mais la définition générale des constantes n'est déjà plus une fin suffisante. | Explicite |

Cette réouverture ne remplace pas immédiatement la première question. Elle
sépare plutôt deux opérations : contrôler ce qui est tenu fixe et instruire,
lorsque le cas le permet, comment cette fixité se constitue.

### 3.2 Le corpus est repris, non recommencé

| Traces | Déplacement | Qualification |
|---|---|---|
| `A2-M15–M23` | L'hypothèse d'un redémarrage complet est refusée. Les matériaux existants sont relus pour distinguer les acquis physiques, les anciennes grammaires taxonomiques et les formulations à requalifier. L'exécution peut s'enchaîner sans validation répétée tant qu'aucun nouvel arbitrage conceptuel n'est requis. | Explicite |

Une règle de travail se stabilise : conserver le matériau, changer la question
qu'on lui pose et arrêter l'exécution lorsqu'une décision de fond dépasse ce
qui a déjà été validé.

### 3.3 La recherche interne se distingue de la sortie soutenable

| Traces | Déplacement | Qualification |
|---|---|---|
| `A2-M24–M47` | La différence entre l'étendue du travail de recherche et l'étroitesse légitime d'un énoncé public devient explicite. Le réglage fin (*fine-tuning*) est déplacé d'une liste de nombres isolés vers un réseau de dépendances et de contingences résiduelles. Un cycle dynamique est ouvert, puis plusieurs modèles simplifiés sont testés avec leurs échecs et leurs limites. | Explicite et fortement étayé |

La séquence ne conclut pas que les mécanismes dissolvent le fine-tuning. Elle
apprend à séparer possibilité, mécanisme local, bilan énergétique et histoire
cosmologique réalisée.

### 3.4 Le dépôt devient aussi une condition d'accès épistémique

| Traces | Déplacement | Qualification |
|---|---|---|
| `A2-M48–M54` | La cohérence du workflow, l'accès aux branches et la consolidation sont discutés comme des conditions de reprise du raisonnement. Ce qui reste enfoui dans une branche ou mal classé peut être matériellement présent tout en demeurant difficilement disponible à l'enquête. | Fortement étayé |

Il s'agit d'un élargissement du mot « accès » : non d'un centre philosophique
universel, mais d'une condition concrète de contrôle documentaire et
computationnel.

### 3.5 La hiérarchie rigide est corrigée, puis l'accès réouvert

| Traces | Déplacement | Qualification |
|---|---|---|
| `A2-M56–M85`, complété par `A3-M5–M6` | L'ordre objet–constitution–accès sert d'abord à corriger l'envahissement de la métrologie et de l'accès. Il est ensuite assoupli : l'ordre dépend du cas, et l'accès peut intervenir dans la préparation, l'individuation, l'inférence ou la preuve. Le terme général « fixité dynamique » est rétrogradé au profit de trajectoires locales explicitement définies. L'analogie de la toupie, d'abord bornée, est finalement retirée des documents actifs. | Explicite |

La doctrine durable n'est donc ni la priorité universelle de l'accès, ni son
rejet, ni une hiérarchie fixe. C'est la distinction des niveaux avec un ordre
local imposé par l'objet et la question.

### 3.6 De la nouveauté revendiquée à la contribution située

| Traces | Déplacement | Qualification |
|---|---|---|
| `A2-M86–M99`, surtout `A2-M94–M99` | Le chantier quantique est reconnu comme calibratoire lorsqu'il reconstruit des distinctions déjà présentes dans la discipline. Le standard d'« originalité » est remplacé par l'évaluation d'une contribution située à des conversations existantes, avec recouvrement, différenciation et limites explicites. | Explicite |

Cette correction ne dévalorise pas les tests précédents. Elle change le critère
auquel ils répondent et prépare la [note active d'évaluation d'une
contribution](../01_CADRE_METHODOLOGIQUE/Note_standard_evaluation_contribution_v0_1.md).

## 4. Troisième phase — resynchroniser l'orientation

### 4.1 L'autorité documentaire passe par la comparaison des états

| Traces | Déplacement | Qualification |
|---|---|---|
| `A3-M1–M6` | Une vue d'ensemble externe et la branche spécialisée apparaissent désynchronisées. Ni l'une ni l'autre n'est déclarée autorité par défaut. La date erronée de novembre 2026 est traitée comme un bug. La reprise compare les énoncés, leurs rangs et leurs traces avant d'actualiser la navigation. | Explicite |

La resynchronisation devient ainsi une opération probatoire : déterminer ce
qui est actuel, historique, anticipé ou encore indécidable, au lieu de choisir
le document le plus récent ou le plus synthétique.

### 4.2 Le centre passe de la police du mot à la mobilité des frontières

| Traces | Déplacement | Qualification |
|---|---|---|
| `A3-M7–M10` | Le projet cesse d'être décrit principalement comme une méthode décidant quelles grandeurs méritent le nom de constante. Deux questions sont reformulées : comment les sciences établissent et déplacent la frontière entre ce qui varie et ce qui tient ; comment l'enquête change lorsqu'elle étudie les constances par leurs régimes, constitutions, accès et transformations possibles. Le pan philosophique passe en quarantaine sélective parce qu'il colorait trop l'enquête interne. | Explicite |

Ce déplacement est matérialisé par la [vue d'ensemble
v0.3](Vue_ensemble_une_page_v0_3.md). Il conserve la qualification comme test
local, mais lui retire le statut de finalité générale.

### 4.3 Dix portraits différenciés, une pratique sous condition

| Traces | Déplacement | Qualification |
|---|---|---|
| `A3-M11–M18` | La cartographie des dix cycles reçoit une ossature commune sans devenir dix formulaires identiques. Le mode de recherche doit varier selon l'objet et rester ouvert à la surprise. La dimension pratique n'est conservée que lorsqu'elle change l'accès, les données, l'inférence ou le statut du résultat. Le test de retrait reste une heuristique réversible, non une règle magique de suppression. | Explicite |

La même séquence conserve un futur chantier sur la mesure, de la microphysique
à la cosmologie, mais refuse de le promouvoir avant d'avoir instruit sa
littérature et vérifié qu'il ne présuppose pas un problème unique.

### 4.4 Les archives améliorent la provenance sans résoudre l'attribution

| Traces | Déplacement | Qualification |
|---|---|---|
| `A3-M20–M29` | La première conversation source est récupérée pour retrouver les questions et corrections disparues des fiches. L'alternance `Prompt` / `Response` est explicitement jugée insuffisante pour répartir intuition, orientation et rigueur. Le dossier des travaux antérieurs devient témoin de trajectoire, non réservoir à réinjecter. Une condition d'arrêt ferme la recherche de propriété lorsqu'elle n'éclaire plus une décision déterminée. | Explicite |
| `A3-M30–M48` | L'assainissement devient une règle d'infrastructure : un contenu nettoyé ne suffit pas si une fusion Git rend de nouveau accessible un historique sensible. Un clone propre et la distinction entre fichiers suivis et doublons locaux permettent de reprendre sans réunir les histoires incompatibles. | Explicite |

Cette transition fonde le présent chantier : archiver permet de mieux
reconstruire les décisions, mais ne transforme pas une conversation en preuve
de propriété intellectuelle ni en autorité scientifique.

### 4.5 Les cinq contrastes précèdent une correction ciblée

| Traces | Déplacement | Qualification |
|---|---|---|
| `A3-M49–M64` | Les dix cycles sont éprouvés par cinq contrastes. À leur terme, une resynchronisation générale est explicitement écartée. Un contrôle transversal distingue acquis, formulations provisoires, contradictions actives et dettes locales, puis un lot ciblé corrige les portes d'entrée et quelques avis de rang sans réécrire sources, archives, calculs ou résultats physiques. | Explicite |

Le résultat consolidé se trouve dans le [contrôle des cinq
contrastes](Controle_consolidation_cinq_contrastes_v0_1.md). La séquence montre
qu'une synthèse intermédiaire peut éviter à la fois la propagation prématurée
et l'immobilisme documentaire.

### 4.6 La réflexivité est instruite avant d'être exécutée

| Traces | Déplacement | Qualification |
|---|---|---|
| `A3-M65–M67` | Deux ouvertures sont proposées : examiner l'incidence du nouvel état sur les sources, archives, calculs et résultats physiques ; appliquer au projet ses propres recommandations. La réponse distingue les couches, recommande un audit réflexif borné et asymétrique, puis sépare son instruction, son essai et sa propagation. | Explicite |

L'archive ne contient pas l'exécution de cet audit. Elle établit seulement que
les sources ne sont pas transformées par une décision conceptuelle, que les
calculs peuvent être réinterrogés dans leurs hypothèses et que les résultats
peuvent être requalifiés sans être réécrits.

## 5. Continuités qui traversent les trois phases

| Continuité | Traces principales | Portée actuelle |
|---|---|---|
| Partir de cas qui résistent aux grilles | `A1-M7–M106`, `A3-M11–M18` | comparer les cycles sans les rendre identiques |
| Conserver les limites comme résultats | `A1-M13–M16`, `A2-M32–M47`, `A3-M49–M64` | une borne, un échec de modèle ou une dette locale fixe la portée d'un énoncé |
| Encadrer la question par la littérature | `A1-M5–M10`, `A2-M94–M99` | situer une contribution plutôt que revendiquer une nouveauté isolée |
| Requalifier sans effacer | `A2-M15–M23`, `A3-M1–M6`, `A3-M59–M64` | préserver les documents historiques et corriger leur rang ou leur fonction |
| Déléguer l'exécution sous condition d'arrêt | `A2-M21–M23`, `A3-M13–M18` | enchaîner les opérations validées, suspendre devant un nouvel arbitrage conceptuel |
| Retirer les mots ou images qui commandent indûment l'enquête | `A1-M7–M12`, `A2-M56–M85` | ne pas laisser « émergence », « fixité dynamique » ou une analogie imposer un résultat |

Ces continuités ne prouvent pas qu'une méthode définitive était présente dès le
départ. Elles montrent des exigences récurrentes qui changent de formulation et
de portée au contact des objets.

## 6. Abandons, ajournements et non-décisions

| Élément | Statut dans les archives | Traces |
|---|---|---|
| Oklo comme entrée centrale | abandonné ; repère empirique latéral seulement | `A1-M5–M12` |
| « émergence » comme mot directeur | abandonné, y compris sous forme de garde-fou négatif | `A1-M7–M12` |
| comparaison dans chaque fiche | refusée ; comparaison différée jusqu'à un gain argumentatif réel | `A1-M33–M36` |
| taxonomie comme système final | non validée ; instrument historique soumis à des tests de compression | `A1-M62–M106` |
| percolation dans le modèle immédiat | ajournée ; intuition conservée pour un modèle spatial plus épais | `A2-M42–M46` |
| analogie de la toupie | d'abord bornée, puis retirée entièrement des documents actifs | `A2-M82–M85` |
| « fixité dynamique » comme principe général | abandonnée ; seules des trajectoires locales définies restent possibles | `A2-M56–M85` |
| ordre universel objet–constitution–accès | abandonné ; distinction conservée, ordre local | `A2-M56–M85`, `A3-M5–M6` |
| qualification comme centre exclusif | reclassée comme instrument local | `A3-M7–M10` |
| chantier sur la mesure | conservé, non promu ; paysage contemporain encore à instruire | `A3-M11–M18` |
| resynchronisation générale après les contrastes | écartée au profit d'un contrôle puis d'un lot ciblé | `A3-M59–M64` |
| révision immédiate des sources et calculs | non lancée ; audit d'incidence à instruire d'abord | `A3-M65–M67` |

La distinction est importante : un élément ajourné n'est ni validé ni rejeté.
Une non-décision doit rester disponible sans être présentée comme prochaine
étape acquise.

## 7. Ce que cette extraction change — et ne change pas

### 7.1 Gains documentaires

Cette lecture rend visibles quatre enchaînements que les documents finaux
compressent fortement :

1. la méthode actuelle provient de corrections imposées par les cas, non d'une
   grille restée identique depuis l'ouverture ;
2. les deux questions directrices résultent d'un déplacement progressif de la
   qualification vers la formation, puis vers la mobilité des frontières et
   les effets sur l'enquête ;
3. GitHub agit comme infrastructure de continuité, de contrôle et d'accès au
   corpus, sans devenir une source d'autorité intellectuelle ;
4. la réflexivité a été instruite sous une forme bornée avant l'ouverture du
   présent chantier conversationnel.

### 7.2 Absence d'effet doctrinal automatique

Cette cartographie :

- ne remplace pas la vue d'ensemble v0.3 ;
- ne modifie pas les deux questions directrices ;
- ne réactive pas les anciennes taxonomies ou doctrines ;
- ne tranche aucune attribution juridique, éditoriale ou propriétaire ;
- n'autorise pas une révision globale des sources, calculs ou interprétations ;
- ne valide pas par elle-même le futur chantier sur la mesure.

## 8. Décision après lecture

La lecture humaine du 16 juillet 2026 valide cette carte comme reconstruction
fidèle de l'évolution générale visible dans les trois archives, tout en
maintenant deux limites : la sélection n'est pas exhaustive et le pan
philosophique n'y est pas reconstruit. Cette seconde dimension pourra être
ajoutée si les premiers résultats en montrent le besoin ; elle n'est pas
requise pour le premier essai.

La carte peut donc instruire un [essai réflexif borné sur trois
objets](Cadrage_essai_reflexif_borne_v0_1.md). Cette validation ne déclenche ni
resynchronisation générale, ni modification des documents mis à l'épreuve, ni
promotion de la carte en nouveau centre du projet.

## 9. Continuation postérieure aux archives

Cette section prolonge la carte jusqu'au jalon du micro-pilote sans prétendre
constituer une nouvelle archive de conversation.

### 9.1 Régime de preuve distinct

Les trois exports s'arrêtent au message `A3-M67`. La continuation ci-dessous
ne reçoit donc pas de repères `A`–`M`, qui désignent exclusivement des messages
présents dans les copies JSON assainies.

Elle retient seulement :

- les décisions explicitement formulées dans la conversation encore
  accessible lors de l'écriture ;
- les documents et événements Git qui en matérialisent l'exécution ;
- les limites et non-décisions nécessaires à la reprise du chantier.

Ce régime est moins riche qu'une archive intégrale. Il ne permet ni citation
exhaustive, ni reconstruction de toutes les inflexions, ni attribution fine des
intuitions. Il suffit ici à documenter les bifurcations sans installer un
journal permanent du clavardage.

### 9.2 De la limite du clavardage à une extraction unique

Après `A3-M67`, la limite produite par l'absence d'archives conversationnelles
est reconnue. Deux solutions sont distinguées : une récupération exceptionnelle
des conversations déjà accumulées et, pour l'avenir, de courts paragraphes
naturels dans les documents qui portent une orientation, une réorientation ou
une continuité importante.

Le journal exhaustif et l'export systématique de chaque conversation sont
écartés. La règle future consiste à rendre une décision reconstructible, non à
conserver chaque tour de dialogue.

### 9.3 Assainissement, reconstruction et nouveau clone

L'auteur fournit trois conversations, autorise explicitement l'assainissement
de leurs données personnelles et techniques, puis autorise la reconstruction
de la branche et sa publication distante. Après confirmation du jalon, il
reclone la branche reconstruite.

Le commit distant `1279975` matérialise l'assainissement et l'indexation des
six copies, sous les deux formats JSON et Markdown. L'opération améliore la
provenance sans promouvoir les archives au rang de preuve scientifique ou
d'autorité doctrinale.

### 9.4 Extraction des transitions et validation de sa portée

Une lecture sélective des 278 messages produit la présente carte. Le commit
distant `642f592` la publie sans modifier les archives ni les documents actifs
qu'elle met en relation.

La lecture humaine la valide comme reconstruction fidèle de l'évolution
générale physique et méthodologique, avec deux réserves : elle n'est pas
exhaustive et elle ne reconstruit pas le pan philosophique. Cette absence est
acceptée pour le premier essai ; elle ne devient ni preuve d'incompatibilité ni
décision d'abandon.

### 9.5 Instruction du micro-pilote

La carte sert ensuite à borner un essai réflexif sur trois objets : la vue
d'ensemble v0.3, le contraste des cycles 9 et 10 et le workflow GitHub confronté
à l'opération d'extraction. Le commit distant `55370fc` publie ce cadrage.

L'instruction sépare explicitement trois gestes : cadrage, passage unique et
propagation éventuelle. Elle interdit de modifier les objets pendant le test,
de rouvrir tout le corpus ou de transformer l'essai en attribution de propriété
intellectuelle.

### 9.6 Autorisation d'exécution et limite des limites

La lecture humaine valide ensuite le cadrage et autorise l'exécution. Elle
ajoute deux exigences :

1. consigner tout jalon postérieur à la dernière archive qui serait nécessaire
   à la reprise, y compris cette demande elle-même ;
2. déclarer les limites du micro-pilote, ainsi que le risque que ses exclusions
   empêchent de voir un problème situé hors de l'échantillon.

Ces exigences sont intégrées aux [résultats de l'essai réflexif
borné v0.2](Resultats_essai_reflexif_borne_v0_2.md). La seconde ne commande pas un
audit de l'audit : lorsqu'une couche exclue devient nécessaire, elle est
consignée comme dette, puis le passage borné s'arrête.

### 9.7 État atteint

Le micro-pilote est exécuté une fois sur les trois objets. Il ne modifie aucun
d'eux. Ses constats, limites et propositions sont restitués séparément et
attendent une validation humaine avant tout lot de correction.

Cette continuation ferme la lacune conversationnelle connue jusqu'à ce jalon.
Elle n'affirme pas que tout le clavardage intermédiaire est désormais archivé.

### 9.8 Retour de lecture — complétude informative

La lecture humaine des premiers résultats accepte le fond du micro-pilote et
signale une perte d'information dans sa formulation : plusieurs limites disent
clairement ce que l'essai, Git ou les résultats physiques n'établissent pas,
mais laissent parfois au lecteur la charge de reconstruire leur fonction
positive.

La règle de réécriture positive v0.3 contient déjà le principe « dire d'abord
ce que le cas est ». Son test contrôlait surtout le rang, la structure et la
conservation des refus. Le retour d'usage ajoute un contrôle de complétude :
chaque limite importante doit borner un résultat, une fonction, un appui, un
rang ou une opération explicitement nommés.

La première restitution v0.1 est reprise sous ce contrôle dans les [résultats
v0.2](Resultats_essai_reflexif_borne_v0_2.md). Les refus et les dettes gardent
leur force ; l'information positive qu'ils délimitent devient directement
lisible. Cette correction porte sur la restitution du micro-pilote et sur la
règle d'écriture ; elle laisse les trois objets éprouvés dans leur état pendant
la décision formelle des propositions A à D.

### 9.9 GitHub comme composante de l'architecture distribuée

Le retour suivant attribue à GitHub un rôle plus fort que celui de support :
son infrastructure versionnée contribue à la mémoire, à la sélection du
contexte pertinent, à la réversibilité et à la cohésion méthodologique du
projet. Les outils employés par les modèles rendent cette infrastructure
consultable, modifiable et vérifiable.

La [note sur l'architecture
distribuée](../01_CADRE_METHODOLOGIQUE/Note_architecture_distribuee_auteur_modeles_GitHub_v0_1.md)
place donc l'auteur, les modèles, GitHub et les outils sur un même plan
d'analyse causale. Elle distingue quatre contributions et deux registres de
responsabilité : scientifique et décisionnel pour l'auteur ; fonctionnel et
traçable pour les modèles, l'infrastructure et les outils.

Cette architecture fournit une explication positive de la fluidité observée :
les validations humaines deviennent des contraintes durables du dépôt, les
modèles retrouvent ces contraintes par les routes documentaires et les outils,
puis GitHub conserve le nouvel état pour l'itération suivante. L'accord fréquent
peut ainsi manifester une convergence cumulative sous mémoire structurée.

La même propriété ouvre un risque de dépendance au chemin. Les clauses de
révision, les alternatives archivées, la littérature extérieure et les tests
de réception restent les contrepoids actifs de cette cohésion.

### 9.10 Instruction d'une cartographie des rôles

La discussion suivante propose de déterminer les rôles de l'auteur, des
modèles, de GitHub et des outils sans produire de hiérarchie entre eux. La
comparaison reste autorisée : elle porte sur l'orientation, la proposition,
l'appui, la transformation, la contrainte, l'arbitrage, l'inscription, la
vérification et la relance propres à une transition.

La structure reçoit une validation humaine, avec trois règles : aucun
pourcentage d'attribution, aucun ordre général entre les composantes et une
sortie explicite « contribution distribuée ou indéterminable » lorsque les
traces le demandent. Les objets, sources, calculs et expériences de lecture
sont ajoutés comme pôle d'appui et de résistance, sans être transformés en
acteur homogène.

La [cartographie des rôles dans trois
transitions](Cartographie_roles_trois_transitions_v0_1.md) applique la grille à
la reformulation des deux questions, au contraste des cycles 9 et 10 et à la
réécriture positive avec l'architecture distribuée. Elle reste un micro-pilote
soumis à validation avant toute intégration dans les règles courantes.

### 9.11 Clarification de la micro-défaillance informationnelle

Avant de valider les trois portraits, la lecture humaine demande que le
troisième intègre la première réécriture positive insuffisante. Elle se demande
si sa cause relève de la méthode, de l'architecture documentaire, de
l'infrastructure ou d'un mélange de ces couches.

La reconstruction confirme que le diagnostic humain portait déjà
explicitement sur une perte de contenu informatif et de précision. La formule
« complétude informative » est la traduction opératoire ultérieure de ce
diagnostic. La forme négative constitue le symptôme visible ; le défaut
sémantique réside dans un contenu positif encore dépendant de l'inférence du
lecteur.

La [cartographie des rôles](Cartographie_roles_trois_transitions_v0_1.md#43-diagnostic-causal-de-la-micro-défaillance)
distingue ensuite trois temps : une règle initialement centrée sur le rang, une
première application de la règle corrigée encore trop proche du texte source,
puis une ambiguïté de version dans le visualiseur. GitHub a conservé les états
et permis leur comparaison ; il n'est pas identifié comme origine du défaut
informationnel. L'hypothèse précise d'un cache d'interface reste non démontrée.

La [note sur l'architecture
distribuée](../01_CADRE_METHODOLOGIQUE/Note_architecture_distribuee_auteur_modeles_GitHub_v0_1.md#10-complémentarité-révélée-par-une-micro-défaillance)
formalise la complémentarité : la méthode définit la propriété, l'architecture
la rend récupérable, GitHub conserve les états, les outils vérifient leur
périmètre et la lecture humaine éprouve l'effet sémantique.

### 9.12 Validation des portraits et correction de représentativité

La lecture humaine valide ensuite le diagnostic causal, les cinq composantes,
les trois portraits, la comparaison sans classement et le micro-paragraphe de
continuité. Cette validation clôt le micro-pilote dans son périmètre propre.

Elle ajoute une objection à toute généralisation de ses exemples. Les trois
transitions ont été choisies pour éprouver la grille, non pour représenter les
contributions les plus fortes de chaque composante. Le contraste 9–10 ne peut
donc pas devenir, à lui seul, la mesure des apports des modèles de langage ou de
GitHub.

La [cartographie des rôles](Cartographie_roles_trois_transitions_v0_1.md#51-limite-de-représentativité-de-léchantillon)
sépare désormais deux résultats : les portraits situés restent bornés à leur
échantillon ; une synthèse transversale, révisable et non exhaustive recherche
les apports saillants dans plusieurs phases des archives, dans les documents
actifs et dans les transitions Git. Elle retient la récurrence, la force
causale et le caractère distinctif sans produire de score, de classement ou
d'attribution propriétaire.

### 9.13 Clôture du chantier et mise en réserve

La lecture suivante reconnaît à l'analyse des rôles une valeur possible, mais
réduite dans le projet présent. La clarification rétablit un cadre de travail
où les considérations propres aux systèmes informatiques et langagiers ne
dominent plus la place de l'auteur ni l'objet scientifique. Ce résultat de
relation de travail motive une clôture, et non l'ouverture d'un nouveau centre
de recherche.

Le cadrage, les résultats, la note d'architecture distribuée et la cartographie
des rôles sont donc conservés comme outils réflexifs en réserve. Ils sortent du
parcours minimal et de la séquence immédiate sans être supprimés ni déplacés.
Leur réouverture exige désormais une question déterminée de provenance, de
responsabilité, de collaboration, de publication ou d'effet infrastructurel.

Les consignes d'agent appliquent la même limite : le travail scientifique
ordinaire utilise l'infrastructure et les outils sans produire de commentaire
routinier sur la répartition des contributions. La prochaine décision redevient
le choix explicite d'une orientation scientifique ou éditoriale.
