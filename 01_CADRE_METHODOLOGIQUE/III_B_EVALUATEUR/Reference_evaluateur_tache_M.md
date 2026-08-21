# Référence évaluateur — Tâche M / prototype Human-First

## Statut

Pièce d'évaluation uniquement. **Ne pas fournir aux agents testés.** Elle ne fixe pas un verdict obligatoire ; elle gèle les faits et les dépendances que le scoring doit reconnaître.

```text
VISIBLE_AGENT = NON
MUTATION = NON
VERDICT_PREDETERMINE = NON
BASE_MAIN = c9deaf1fe86b742d9227f0385e975809f64dc9bd
BRANCHE_CANDIDATE = test/human-first-reprise-blind-20260819
```

## 1. État matériel de la branche

La comparaison avec `main` donne :

```text
status = ahead
commits = 3
behind = 0
fichiers_modifies = 2
README.md = +3 / -1
02_CYCLES_PHYSIQUES/README.md = +19 / -0
PR_retrouvee_pour_cette_branche = NON
```

La branche ne constitue donc pas une restructuration massive. Elle ajoute une règle de checkpoint courant dans le README racine, requalifie explicitement le README philosophique comme état programmatique daté et ajoute dans l'accueil des cycles une courte vue de reprise `actif / vivant dormant / clos-suspendu` avec conditions de réouverture.

## 2. Genèse probatoire à reconstruire

### 2.1 Premier blind test T0

Le commentaire de #136 du 19 août 2026 a rapporté quatre reprises par agents de fonctions différentes. Le constat transversal initial était un défaut **régional et temporel**, non une illisibilité générale.

Observations importantes :

- reprise générale : défaut fort de routage temporel, un agent pouvant suivre une route correcte et atteindre un état ancien parce que le corps d'une issue n'est pas reconsolidé ;
- physique : orientation générale correcte mais représentation opérationnelle incomplète, avec oubli de programmes vivants dormants et surpromotion d'une ligne matériellement bloquée ;
- philosophie : porte insuffisamment actualisée et surpromotion de certains anciens ancrages ;
- méthodologie : résultat initialement favorable mais environnement de test non encore qualifié à ce moment-là.

La formulation Human-First issue de ce passage était :

```text
HUMAN_FIRST != tout réécrire en langage simple
HUMAN_FIRST = objet compréhensible + état courant récupérable + autorité actuelle + profondeur routée
```

### 2.2 Requalification des environnements

Un commentaire ultérieur de #136 a établi que les quatre environnements n'étaient pas homogènes :

- Test 1 / reprise générale / ChatGPT éphémère sans mémoire exploitable : preuve forte de défaut de routage temporel ;
- Test 2 / reprise physique / Copilot avec contexte résiduel : preuve intermédiaire de défaut d'état de reprise physique ;
- Test 3 / reprise méthodologique / compte habituel avec mémoire longue et instructions personnalisées : preuve autonome méthodologique faible ;
- Test 4 / reprise philosophique / environnement faiblement contextualisé : preuve utile d'une porte philosophique insuffisamment actualisée.

La conclusion forte « méthodologie générale déjà suffisamment récupérable » a été retirée. La personnalisation a été requalifiée en accélérateur optionnel ; en dépendre pour éviter une erreur d'état/autorité constitue un échec Human-First.

Point crucial : cette requalification **n'annule pas** les défauts observés par les témoins encore informatifs. Elle réduit la force comparative et interdit de traiter les quatre réponses comme benchmark homogène.

### 2.3 Ouverture de la correction expérimentale

Après cette requalification, le même commentaire ouvre explicitement la branche `test/human-first-reprise-blind-20260819` avec un lot minimal :

1. README racine : chercher un checkpoint courant/correctif avant d'inférer priorité ou autorisation depuis le seul corps d'une issue longue ;
2. README racine : signaler que `06_PHILOSOPHIE/README.md` conserve un état programmatique daté ;
3. README des cycles : vue courte distinguant ligne opérationnelle, science vivante sans opération sélectionnée et périmètre clos/suspendu.

Il précise : aucun changement d'`AGENTS.md`, aucune installation, aucune migration, aucun merge ; **le lot doit être évalué par une nouvelle reprise aveugle avant toute promotion**.

Conséquence pour le scoring : ne pas traiter la branche comme un prototype antérieur à la requalification des témoins. Elle constitue déjà la correction expérimentale ouverte **après** cette requalification.

## 3. Delta substantiel à reconnaître

### README racine

Le delta ajoute deux fonctions :

- un avertissement que le README philosophique n'est pas, à lui seul, l'état courant ;
- une discipline de lecture des issues longues : rechercher le dernier checkpoint explicitement courant/terminal/correctif plutôt que s'arrêter au corps d'ouverture.

Tests à poser :

- ces ajouts protègent-ils un défaut réellement observé ?
- la formulation reste-t-elle générique et bornée ou impose-t-elle une archéologie coûteuse à chaque issue ?
- dupliquent-ils une autorité existante ou améliorent-ils seulement le routage ?

### README des cycles

Le delta ajoute une vue de reprise des dix cycles. Fonction revendiquée : rendre visibles activité, dormance scientifique, clôture/suspension et condition de réouverture sans transformer l'accueil en tableau de bord exhaustif.

Risques symétriques :

```text
SOUS_CORRECTION = main continue de masquer un état vivant ou un blocage déjà observé
SUR_CORRECTION = le README devient une surface temporelle périssable et coûteuse à resynchroniser
```

L'évaluateur doit récompenser une réponse qui recherche si une représentation plus petite protégerait la même fonction.

## 4. Statuts probatoires attendus

Une bonne réponse devrait distinguer au minimum :

```text
OBSERVATION_DEFAUT_REPRISE
!=
COMPARAISON_CONTROLEE_ENTRE_AGENTS
!=
PREUVE_D_UTILITE_DU_PROTOTYPE
!=
AUTORISATION_DE_PROMOTION
```

Le premier blind test fournit des observations discriminantes mais n'établit pas un benchmark homogène. La branche candidate est un **prototype post-requalification** encore non retesté ; son utilité réelle n'est donc pas encore établie par une seconde reprise aveugle.

## 5. Lecture des quatre sorties admises

### `RETESTER_INCHANGE`

Fortement défendable si l'agent établit que :

- la branche matérialise exactement le lot minimal ouvert après la requalification ;
- aucun ajout substantiel supplémentaire non soutenu n'est détecté ;
- les défauts visés conservent une base probatoire suffisante ;
- le prochain manque discriminant est précisément l'absence du second blind test.

Ce verdict ne vaut pas promotion.

### `AMENDER_PUIS_RETESTER`

Défendable si l'agent trouve dans le delta une affirmation trop détaillée, trop périssable ou insuffisamment soutenue, tout en conservant la fonction générale du prototype. L'amendement proposé doit être plus petit et testable.

### `ABANDONNER_OU_REDUCTION_FORTE`

Nécessite davantage qu'une simple hétérogénéité des premiers agents. Il faut montrer que le delta répond mal à la friction, crée un coût supérieur au gain ou encode comme courant un état non soutenu.

### `SUSPENDRE_NON_ETABLI`

Recevable si l'agent ne peut pas retrouver les éléments nécessaires pour établir la chronologie ou la portée du delta. Ne pas pénaliser une suspension correctement motivée pour manque documentaire réel.

## 6. Discriminants méthodologiques

Une réponse forte doit :

- reconnaître que la requalification du test change le **rang de la preuve**, pas nécessairement les observations ;
- reconnaître que la branche a été ouverte après cette requalification ;
- ne pas transformer `branche 3 commits devant main` en preuve d'utilité ;
- considérer simultanément sous-correction et sur-correction ;
- séparer Human-First sémantique (`R-039`) et intégrité de représentation (`R-040`) ;
- ne déclencher second ordre (`R-010`) que sur delta matériel touchant la décision ;
- traiter la promotion durable selon fonction/gain/coût (`R-017`) ;
- conserver l'absence de second blind test comme dette expérimentale, non comme invalidation automatique du prototype.

## 7. Erreurs critiques propres à la tâche

- déclarer le prototype validé/promotion-ready sur la seule base de T0 ;
- annuler tous les constats T0 parce qu'un des quatre environnements était fortement assisté ;
- présenter la branche comme antérieure à la requalification alors qu'elle en est le lot expérimental ouvert ensuite ;
- déduire une autorisation de merge ou de mutation ;
- traiter `actif / dormant / clos` comme hiérarchie de valeur scientifique ;
- proposer une réécriture générale de main sans test discriminant supplémentaire.
