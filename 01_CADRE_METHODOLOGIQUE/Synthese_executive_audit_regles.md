# Synthèse exécutive — audit des règles, régimes et récursivités

## Statut

Cette synthèse est la troisième sortie de la PR #139, après :

- `matrice_regles_audit.csv` : 39 unités d’étude ;
- `relations_regles_audit.csv` : 44 relations qualifiées entre ces unités.

Elle est **descriptive et qualifiante**, non normative par elle-même. Elle ne promeut aucune nouvelle règle dans `AGENTS.md`, ne modifie aucun état scientifique et n’autorise aucun merge.

```text
PR = #139
MATRICE = 39 UNITES
RELATIONS = 44 ARETES QUALIFIEES
SATURATION_HISTORIQUE_POUR_DECOUVERTE_DE_FAMILLES = ATTEINTE
LECTURE_EXHAUSTIVE_DE_TOUS_LES_COMMENTAIRES = NON
PROMOTION_NORMATIVE = NON_EFFECTUEE
MERGE = NON_AUTORISE
```

La saturation obtenue est fonctionnelle : des lectures supplémentaires ne sont plus justifiées par la seule possibilité abstraite qu’un commentaire ancien contienne encore quelque chose. L’archéologie se réouvre si un nouvel indice est susceptible de modifier une famille, un régime, un contre-cas, une relation, une autorité ou une action.

## 1. Résultat principal : le dépôt n’est pas gouverné par une seule « méthode »

L’audit ne confirme ni un système unique de méta-règles, ni une accumulation arbitraire de précautions. Il montre plusieurs fonctions distinctes qui ont été co-fabriquées à partir d’incidents scientifiques, computationnels, documentaires et agentiques.

Les 39 unités ne doivent donc pas être lues comme 39 commandements de même rang. Elles comprennent notamment :

1. des **contrôles scientifiques et probatoires** ;
2. des **règles de continuité, provenance et reprise** ;
3. des **règles d’audit et de contrôle de sélection** ;
4. des **règles de décision, d’autorité et de mutation** ;
5. des **spécialisations locales ou mécanismes d’enforcement** ;
6. des **principes d’interface** dont le support exact reste à décider.

La principale correction apportée à la matrice initiale de 24 lignes est la remontée d’une strate qui y manquait : les contrôles scientifiques/conceptuels actifs D1–D4, P25–P27, les passages inter-domaines, les négatifs/suspensions et les frontières exactes entre décision, autorisation et mutation.

## 2. Noyau scientifique et probatoire suffisamment différencié

Le noyau scientifique n’est pas réductible à « ne pas surinterpréter un résultat ». Plusieurs fonctions indépendantes résistent aux tests de fusion.

### 2.1 Nature du maintien et indexation de l’énoncé

`R-025` distingue **constance** et **stabilisation**.  
`R-026` impose de situer une attribution par cible, transformation, régime, échelle/schéma/modèle lorsque pertinent, tolérance et rupture.

Ces fonctions ne se remplacent pas : un énoncé peut être correctement indexé tout en confondant constance de l’objet et stabilisation d’un accès ; inversement la distinction conceptuelle peut être correcte mais rester trop peu située pour être falsifiable.

### 2.2 Cible, accès, constitution et chemins

`R-027` distingue la cible, les voies d’accès et les mécanismes/architectures de constitution, sans ordre universel entre eux.

`R-029` qualifie les chemins ou dépendances lorsqu’ils changent l’argument : physique, inférentiel, computationnel, représentationnel, historique/de réalisation, etc.

L’ablation instruite autour de #104 montre que ces deux fonctions sont indépendantes. Savoir **quelles couches** sont en jeu ne suffit pas à savoir **quelle dépendance** relie deux résultats ou deux opérations.

### 2.3 Portée de l’énoncé et rang probatoire

`R-028` borne la portée de la conclusion.  
`R-031` distingue résultat, soutien probatoire et verdict.  
`R-001` est une spécialisation particulièrement exposée de `R-031` pour les sorties machine/CI.

Une conclusion peut être au bon rang probatoire mais porter trop loin ; elle peut aussi être correctement bornée tout en confondant résultat et verdict. Les deux contrôles sont nécessaires.

### 2.4 Non-détection discriminante

`R-032` conserve une fonction propre : une absence de variation ou de signal n’est informative que si le dispositif avait une puissance réelle sur une famille déclarée d’alternatives. Une borne sur une valeur n’est pas automatiquement une borne sur sa variation.

Les dossiers α4/α5 fournissent des applications réelles où une non-détection locale est admise tandis que l’invariance universelle est explicitement refusée.

### 2.5 Négatifs, refus et suspensions

`R-037` ne se confond ni avec `R-031` ni avec la représentation de la science vivante (`R-009`). Sa fonction est la conservation d’une sortie négative à son rang exact.

Le cas M2a-N reste sentinelle : ~120 h soutiennent `strategie_historique = NON_PRODUCTIVE` sans devenir un verdict pour ou contre X(z). La conservation de ce négatif évite sa répétition et sa réinterprétation.

## 3. Couplage entre preuve et dispositif : une règle mieux bornée qu’au départ

`R-003` sort renforcée de l’audit. Elle n’est plus soutenue seulement par des cas C7 ou des proxies conceptuels.

#82 fournit un échec réel de test vacant : `62/62` fautes semblaient détectées alors que cinq contrôles d’autorisation étaient devenus inatteignables. #105–#107 transportent la fonction hors C7 :

- une ablation peut montrer qu’un contrôle est redondant ;
- une heuristique peut signaler à tort une structure normale ;
- un détecteur peut être correct mais produire une sévérité inadéquate au risque réellement protégé.

La bonne abstraction n’est donc pas « tout proxy exige un contre-test supplémentaire ». Elle est :

```text
propriété revendiquée
→ régime effectivement exercé
→ dispositif réellement sensible à cette propriété
→ signal attribué à la bonne cause
→ sévérité compatible avec le risque protégé
```

Le candidat séparé « qualification située dans le régime d’exécution » n’a pas besoin d’une unité autonome : sa fonction est absorbée par `R-026` + `R-003`.

`R-002` — reproduire la cause d’un rouge avant attribution au candidat — reste une heuristique forte mais bornée ; sa nécessité comme règle autonome n’est pas établie. Elle peut être absorbée dans ce noyau causal/probatoire plutôt que promue séparément.

## 4. Science vivante : représenter un programme n’est pas inventorier ses résultats

`R-009` demeure l’une des corrections les plus importantes de l’audit de reprise.

Une représentation qui prétend montrer l’état scientifique doit distinguer au minimum :

- recherche active ;
- question vivante mais dormante ;
- veille conditionnelle ;
- périmètre clos ;
- périmètre suspendu ;
- résultat qualifié ;
- blocage ;
- décision ouverte ;
- condition de reprise ;
- effet attendu sur le programme.

`recherche active != résultat` et `dette != priorité`. Cette séparation est portée explicitement par `R-023` : l’activité d’un chantier ne vaut ni qualification scientifique, ni permission de franchir la porte suivante.

#49/#51 puis #114 permettent en outre de distinguer **clôture locale**, **suspension conditionnelle**, **veille conditionnelle** et **réouverture**. Une réouverture n’est justifiée que si un événement change effectivement un pont, un verdict ou une condition de reprise ; une nouvelle publication ou une nouvelle hypothèse ne suffit pas.

Cette fonction doit être portée par les surfaces de reprise appropriées, mais elle ne justifie pas à elle seule un tableau de bord global permanent.

## 4 bis. Passages entre domaines : transférer exige une réinstruction

`R-016` empêche déjà de propager automatiquement l’état d’un chantier vers un autre : l’effet d’une conclusion sur un autre objet doit être testé, avec `NON_ETABLI` comme sortie recevable.

`R-036` ajoute une exigence plus forte lorsqu’un passage inter-domaines est réellement utile : la question doit être **réinstruite** dans les objets, accès, discriminants et contraintes du domaine d’accueil.

Le transfert `m_e` du cycle 1 vers Saveur–Higgs constitue le cas positif principal. Il n’a été justifié que parce que :

- le résidu ne changeait plus le verdict courant du domaine d’origine ;
- le domaine d’accueil apportait une structure explicative et des accès distincts ;
- la question était reformulée plutôt que copiée ;
- provenance et conditions de réouverture restaient visibles ;
- le transfert n’ouvrait pas automatiquement un nouveau programme.

La même logique borne les passages philosophie → science : une proposition philosophique peut préciser une question, mais elle ne modifie un statut physique qu’après réinstruction dans les discriminants du domaine compétent.

## 5. Continuité documentaire et provenance : plusieurs axes à ne pas fusionner

L’audit confirme quatre questions distinctes :

- `R-004` : où commencer et vers quelle autorité router ;
- `R-005` : un contenu daté peut rester valide sans être l’état courant ;
- `R-007` : document courant sous nom stable par défaut, avec exceptions probatoires ;
- `R-033` : provenance d’une formulation, garantie scientifique, autorité normative et ratification humaine effective sont différentes.

Deux corrections importantes en résultent.

Premièrement, « Git porte l’histoire » est un **principe par défaut**, non une loi d’intangibilité. #14 montre qu’une obligation indépendante — droit, confidentialité, sécurité ou retrait de données — peut justifier une purge contrôlée de l’historique.

Deuxièmement, un commentaire ou commit apparaissant sous le compte `AkselBoursier` ne prouve pas, à lui seul, une ratification humaine lorsqu’un agent peut écrire via le compte connecté. La provenance effective de l’intervention doit être établie lorsque la décision a un effet scientifique, irréversible ou de forte autorité.

## 6. P28 et P29 : fonctions conservées, mécanismes historiques non réactivés littéralement

### P28

La reconstruction historique interdit deux caricatures.

P28 n’est pas un veto général à la création documentaire. Sa forme dure visait la **promotion durable d’artefacts de gouvernement**. L’amendement a explicitement admis des supports exploratoires temporaires lorsqu’ils réduisent la charge ou rendent une épreuve inspectable.

La règle fonctionnelle actuelle (`R-017`) devient :

```text
ne créer ni refuser par principe ou par nombre brut ;
tester la fonction distincte, le support déjà disponible,
le gain discriminant/de contrôle et le coût de maintenance.
```

La capture légère (`R-018`) en est une spécialisation : préserver une idée récupérable ne lui donne ni priorité ni identité documentaire autonome.

### P29

P29 a bien protégé une fonction de traçabilité, mais son mécanisme initial était plus strict que le régime courant : issue pour toute instruction, commentaire séparé pour chaque étape, checklist synchronisée.

La fonction subsiste dans `R-008` :

```text
ancrage principal récupérable
+
transitions substantielles conservées
+
reconsolidation de l’état courant
```

Il ne faut ni réactiver P29 littéralement, ni remplacer l’état courant par une succession illimitée de checkpoints.

## 7. Audit de l’audit : ce qui a réellement résisté

Le dispositif de second ordre doit rester **événementiel et borné**.

`R-010` est déclenchée lorsqu’un angle mort réel, un changement de corpus ou un défaut de sélection remet en cause la capacité de l’audit à voir ce qu’il prétend voir. Elle n’autorise pas une réflexivité continue.

`R-011` ajoute une contrainte spécifique aux audits de portée globale : ne pas seulement falsifier les conclusions reçues, mais chercher indépendamment ce que la sélection d’entrée a pu exclure.

`R-014` protège les audits antérieurs contre les deux réécritures symétriques : un audit ancien n’est ni annulé par principe, ni réputé contextuellement suffisant par ancienneté. Ses preuves locales subsistent ; un réaudit n’est déclenché que si le nouveau contexte touche une prémisse, une exclusion, un critère ou une portée.

`R-015` impose la symétrie critique : une conclusion positive et une critique négative supportent la même charge de preuve. #132 a montré toutefois que cette symétrie ne suffit pas si la **sélection d’entrée** est elle-même asymétrique ; d’où son articulation nécessaire avec `R-011` pour les audits globaux.

#139 a exécuté cette passe : la fenêtre #119–#138 a été dépassée, les issues antérieures ont été parcourues jusqu’à #1 au niveau requis, #118 a fourni une archéologie antérieure vers A1–A3, puis plusieurs zones non sélectionnées ont été contre-échantillonnées. Les dernières lectures n’ont plus produit de nouvelle famille substantielle.

Cela justifie :

```text
SATURATION_HISTORIQUE_POUR_DECOUVERTE_DE_FAMILLES = OUI
RELECTURE_TOTALE_DE_TOUT_COMMENTAIRE = NON_REQUISE
REOUVERTURE = SUR_INDICE_DISCRIMINANT
```

La règle d’exhaustivité documentaire (`R-012`) reste exacte dans son régime : un document appartenant à un corpus auditable défini ne peut être déclaré sans effet avant lecture. Elle ne doit pas être généralisée à toute tâche locale.

La triangulation ciblée (`R-013`) reste bonne localement mais insuffisante, seule, pour une prétention d’exhaustivité globale.

## 8. Autorité : intervention, capacité d’agir et portée d’une décision sont trois questions

`R-019`, `R-020` et `R-034` ne doivent pas être aplaties.

`R-019` type l’intervention humaine lorsque cela change l’action : observation, hypothèse, proposition, préférence, décision et autorisation. Une suggestion n’est pas automatiquement un ordre ; inversement une décision explicite ne doit pas être neutralisée en la requalifiant artificiellement comme simple proposition.

`R-020` et `R-034` résistent ensuite à la fusion.

`R-020` distribue l’autorité selon la nature de l’acte, son observabilité, sa réversibilité, son coût d’erreur et sa portée. Elle permet davantage d’autonomie agentique pour les opérations techniques locales, observables et réversibles, tout en maintenant les frontières scientifiques et irréversibles sous décision humaine.

`R-034` borne l’effet d’une décision précise :

```text
qualification
!= exécution
!= propagation
!= mutation
!= merge
```

Les clôtures α3–α5 sous délégation procédurale sont des cas positifs : la condition d’arrêt autorisait la clôture locale, pas la propagation ni la fusion.

#117 est le contre-cas causal : un diagnostic de déclassement a été converti trop tôt en suppression matérielle.

`R-035` spécialise ce risque pour les mutations destructives : avant suppression, déplacement ou déclassement, vérifier contenu unique, dépendances, fonction scientifique/probatoire et autorisation exacte.

## 9. Mutations et infrastructure : ce qui paraît mécanisable

`R-038` qualifie le confinement versionné de la mutation :

```text
cible/fonction
→ état/SHA relu
→ action de bonne classe
→ éviter no-op/diff vide
→ contrôle terminal
```

`R-021` couvre la phase suivante lorsqu’une écriture retourne un état ambigu : read-back avant toute certitude.

Ces fonctions se prêtent à une mécanisation partielle parce qu’elles portent sur des propriétés machine-observables. Elles ne doivent pas automatiser la décision scientifique ou le merge.

`R-022` constitue un cas positif local : le routage CI C2 par pertinence de changement est techniquement qualifié, avec chemins positifs et négatifs. Il ne justifie pas une généralisation obligatoire à toute CI.

`R-024` reste un critère de sélection d’outillage, pas une autorisation d’installer : usage répétable, périmètre compréhensible et gain net supérieur au coût de maintenance/apprentissage.

## 10. Human-First : principe soutenu, portée à tester par l’usage

`R-039` distingue une fonction d’interface : les surfaces de reprise et de décision doivent porter leur sens en langage humain ; les codes restent secondaires et récupérables.

Elle ne remplace pas `R-030`. `R-030` protège la **fidélité scientifique du vocabulaire** : décrire d’abord le phénomène dans les termes du domaine et n’introduire une catégorie transverse que si elle ajoute un gain discriminant. Une formulation peut donc être très lisible mais scientifiquement inadéquate, ou scientifiquement correcte mais inutilement opaque.

Cette règle ne signifie ni prose maximale, ni interdiction des sigles, ni réécriture de tout l’historique. Un identifiant compact est acceptable lorsqu’il réduit réellement la charge dans un contexte local où son référent est récupérable.

Le test aveugle #137 est partiellement confondu par la mémoire de compte. Il soutient le problème mais ne suffit pas comme preuve expérimentale propre.

La présente synthèse sert donc aussi de test : si l’architecture des règles peut être comprise ici sans lire les 39 IDs comme une taxonomie à mémoriser, Human-First produit un gain réel. Si elle oblige au contraire à retourner constamment aux codes, le mécanisme d’interface doit être corrigé avant toute promotion durable.

## 11. Non-règles, régimes retirés ou non généralisables

L’audit doit conserver explicitement ce qui **ne doit pas** revenir comme règle transverse par simple répétition historique.

Ne sont pas à réactiver comme normes générales :

- « une seule unité substantielle active » : solution locale historique de contexte agentique ;
- `SOURCE_HIERARCHY` et anciens workflows rigides à trois branches : régimes historiques/localisés ;
- P29 littéral et exhaustif : fonction conservée, mécanisme proportionné ;
- P28 lu comme interdiction générale de créer : sur-extension historique ;
- réflexivité continue ou audit automatique de l’audit à chaque tâche ;
- seuil numérique universel de « shadow learning » ;
- automatisation générale du shadow ;
- cycle de vie universel/auto-clôture des PR ;
- datation prospective générale de toute prédiction ;
- nombre brut d’issues/branches comme mesure de complexité ;
- ancienneté d’un document comme dette en soi ;
- « Git est une archive intangible » sans exception ;
- recherche d’originalité comme filtre général de sélection scientifique ;
- `constante effective` comme classe transverse propre au projet ;
- restauration d’une « question génétique » autonome comme centre général ;
- « accès » comme centre universel ou simple contrôle terminal ;
- ordre universel formation → constitution → accès.

### D5 : décision programmatique, pas règle générique

Les deux questions publiques du projet et la conservation de Q3 comme contrôle interne constituent une **décision programmatique active**. Leur fonction est d’organiser le programme scientifique, non de fournir une règle opératoire transposable à d’autres objets.

D5 n’est donc pas ajouté comme règle transverse générique dans la matrice. Il doit être conservé comme décision programmatique dans les supports qui portent la mission du projet.

## 12. Prototype de lecture 2D — utile mais non sédimenté

Les relations montrent deux récursivités différentes qui ne doivent pas partager des arêtes non qualifiées.

### Axe horizontal : transformation d’une situation en décision

```text
déclencheur
→ opération / enquête
→ observable ou preuve
→ qualification
→ décision
→ action / silence / suspension / arrêt
```

### Axe vertical : niveaux sur lesquels la récursivité peut intervenir

```text
objet scientifique
↓
énoncé / règle de qualification
↓
contrôle ou dispositif de preuve
↓
contrôle du contrôle / sélection
↓
synchronisation de l’état / reprise
```

Deux boucles doivent rester typées :

- **récursivité scientifique** : objet ↔ accès ↔ constitution, chemins et requalification ;
- **récursivité méthodologique** : audit → résultat d’audit → contrôle du critère → reprise.

Cette vue est utile pour éviter qu’un contrôle de contrôle soit pris pour une nouvelle strate scientifique. Elle reste un prototype dérivé des deux CSV ; aucune nouvelle information normative ne doit y être créée.

## 13. Actions justifiées par la matrice

La matrice ne commande pas une « grande réparation ». Les actions se répartissent en quatre classes.

### A. Achever proprement #139

1. reconsolider l’ancrage courant de l’audit afin qu’il ne reste pas au statut initial `OUVERT` après la matrice ;
2. exécuter une passe finale de second ordre sur la matrice + la présente synthèse, avec condition d’arrêt explicite ;
3. produire le plan d’action dérivé, sans modifier encore `AGENTS.md`.

### B. Conserver/appliquer sans nouvelle promotion

Plusieurs fonctions sont déjà suffisamment établies ou actives dans leur régime : rang probatoire, routage/autorité, statut documentaire, non-propagation entre chantiers, règles scientifiques D1–D4/P27, conservation des négatifs, pré-vol des mutations.

La présence dans la matrice ne justifie pas de les recopier dans plusieurs supports.

### C. Porter potentiellement par infrastructure après la synthèse

Candidats raisonnables :

- read-back après écriture ambiguë (`R-021`) ;
- pré-vol SHA/état et contrôle terminal (`R-038`) ;
- routage de contrôles coûteux par pertinence (`R-022`) ;
- séparation détection / sévérité lorsque la propriété est machine-observable (`R-003`) ;
- mécanismes réduisant les no-op ou mutations de mauvaise classe.

Toute automatisation devra être comparée à quatre options :

```text
règle interprétée
vs mécanisme infrastructurel
vs combinaison
vs absence de changement
```

### D. Décision humaine post-audit

Restent des décisions humaines de portée :

- quelles unités méritent une formulation directe dans `AGENTS.md` racine ou local ;
- quelles fonctions doivent rester seulement dans les dossiers scientifiques ;
- quelle partie de Human-First doit être promue ;
- quels mécanismes doivent être automatisés ;
- quels supports de reprise doivent être reconsolidés ;
- merge éventuel de #139.

## 14. Condition de réouverture de l’archéologie

L’étude historique n’est pas déclarée « complète pour toujours ». Elle est fermée **pour la découverte générale de familles** tant qu’aucun signal discriminant nouveau n’apparaît.

Réouvrir si un nouvel objet montre au moins l’un des cas suivants :

- famille normative non représentée ;
- transformation de régime qui change un verdict de matrice ;
- contre-cas matériel qui renverse un statut probatoire ;
- mécanisme d’enforcement distinct ;
- sous-application ou sur-application non absorbable par les unités existantes ;
- relation récursive substantielle absente ;
- provenance/ratification susceptible de changer l’autorité attribuée ;
- contradiction entre une règle matricée et un état matériel actuel du dépôt.

En l’absence d’un tel déclencheur, la prochaine opération utile n’est plus l’archéologie générale : c’est la passe finale de second ordre, puis le plan d’action et la cartographie fonctionnelle de l’outillage.
