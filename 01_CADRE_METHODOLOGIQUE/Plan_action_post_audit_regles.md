# Plan d’action dérivé de l’audit des règles

## Fonction

Ce document transforme les verdicts et `ACTION_A_REALISER` de `matrice_regles_audit.csv` en séquence opératoire **sans transformer automatiquement une qualification en promotion normative**.

Il s’appuie sur :

- `matrice_regles_audit.csv` — 39 unités ;
- `relations_regles_audit.csv` — 44 relations ;
- `Synthese_executive_audit_regles.md` ;
- l’ancrage reconsolidé `Audit_exhaustif_regles_119_138.md`.

Les statuts d’action employés ici sont :

```text
FAIT
= action de #139 déjà exécutée et contrôlée ;

AUCUNE_ACTION_NOUVELLE
= fonction à conserver/appliquer dans son régime sans nouvelle couche ;

A_DECIDER_HUMAINEMENT
= qualification suffisante pour soumettre une décision de portée, pas pour l’anticiper ;

A_MECANISER_OU_PROTOTYPER
= fonction suffisamment observable pour instruire un mécanisme technique ;

CONDITIONNEL
= aucune action maintenant ; déclencheur explicite requis ;

LOCAL_SANS_PROMOTION
= instrument ou mécanisme utile dans un régime borné, à ne pas généraliser ;

RETIRE_OU_ABSORBE
= ne pas conserver comme règle autonome ; fonction absorbée ou régime historique retiré.
```

Aucun de ces statuts n’autorise le merge de #139.

## 1. Actions déjà réalisées dans #139

### R-008 — ancrage et checkpoints

**Statut : FAIT.**

L’ancrage `Audit_exhaustif_regles_119_138.md` a été reconsolidé après matrice et synthèse. Il expose désormais le courant sans obliger un agent neuf à reconstruire l’état depuis toute la chaîne de checkpoints.

La fonction P29 est conservée sous forme proportionnée : ancrage principal + transitions substantielles + reconsolidation, sans journal exhaustif.

### R-010 — audit de second ordre

**Statut : FAIT dans le régime de #139.**

Une passe finale a été exécutée sur la synthèse. Elle a trouvé des omissions réelles de niveau, les a corrigées, puis n’a pas produit de nouvelle famille lors du contrôle suivant.

La réflexivité continue reste refusée. Réouverture seulement sur anomalie discriminante.

### R-011 / R-015 — sélection indépendante et symétrie critique

**Statut : FAIT pour #139 / AUCUNE_ACTION_NOUVELLE immédiate.**

La passe indépendante repo→règles a été exécutée ; elle a découvert des familles absentes de la matrice initiale. Le contrôle négatif ultérieur a atteint une saturation fonctionnelle.

Pour tout futur audit de portée globale, conserver la combinaison : symétrie positif/négatif + contre-échantillon indépendant de la sélection d’entrée.

### R-013 — triangulation ciblée

**Statut : FAIT comme restriction de portée.**

La synthèse distingue désormais explicitement : triangulation locale efficace ≠ preuve d’exhaustivité globale.

## 2. Conserver et appliquer sans nouvelle promotion

Ces unités ont une fonction suffisamment soutenue et déjà portée par les pratiques/documents existants. Leur présence dans la matrice **n’appelle pas une duplication**.

| Unité | Action |
|---|---|
| R-001 — rang probatoire machine/science | `AUCUNE_ACTION_NOUVELLE` ; vérifier seulement une contradiction reproduite dans une surface active |
| R-004 — routage et autorité | `AUCUNE_ACTION_NOUVELLE` ; resynchronisation ciblée seulement si erreur de routage reproduite |
| R-005 — statut documentaire | `AUCUNE_ACTION_NOUVELLE` ; utiliser le double contre-factuel dans son régime documentaire |
| R-007 — courant et généalogie | `AUCUNE_MIGRATION_MASSIVE` ; contre-tester avant toute conversion de snapshots |
| R-012 — exhaustivité documentaire | `AUCUNE_ACTION_NOUVELLE` hors corpus auditable explicitement défini |
| R-014 — audit antérieur et contexte | `AUCUNE_ACTION_NOUVELLE` ; réaudit ciblé seulement si une dépendance matérielle apparaît |
| R-016 — effet sur dépendance | `AUCUNE_ACTION_NOUVELLE` ; tester seulement lorsqu’un chantier est utilisé pour décider un autre |
| R-017 — non-prolifération par fonction | `AUCUNE_COUCHE_NOUVELLE` ; appliquer proportionnellement lors d’une création/promotion envisagée |
| R-023 — activité ≠ qualification | `AUCUNE_ACTION_NOUVELLE` ; conserver comme garde de rang dans les surfaces scientifiques actives |
| R-031 — résultat / soutien / verdict | `AUCUNE_ACTION_NOUVELLE` ; fonction centrale déjà active dans les dossiers scientifiques |
| R-032 — non-détection discriminante | `AUCUNE_ACTION_NOUVELLE` ; appliquer dans les dossiers concernés |
| R-036 — passage inter-domaines | `AUCUNE_ACTION_NOUVELLE` tant qu’aucun passage réel n’est envisagé |
| R-037 — négatifs/refus/suspensions | `AUCUNE_ACTION_NOUVELLE` ; conserver dans les dossiers et états de reprise pertinents |

## 3. Unités à ne pas promouvoir comme règles autonomes transverses

### R-002 — cause d’un rouge

**Statut : RETIRE_OU_ABSORBE comme règle autonome.**

La localisation de la cause est une heuristique forte mais sa nécessité comme règle indépendante n’est pas établie. L’absorber dans le noyau causal/probatoire existant est préférable à une nouvelle inscription.

### R-006 — double contre-factuel documentaire

**Statut : LOCAL_SANS_PROMOTION.**

Instrument robuste pour les resynchronisations de statut documentaire ; ne pas le transformer en formule transverse de toute correction.

### R-018 — capture hors périmètre

**Statut : LOCAL_SANS_PROMOTION / pratique légère.**

Capturer dans le support existant le plus léger lorsque valeur de reprise + risque de perte sont réels. Ne pas créer une obligation d’issue/document et ne pas transformer la capture en priorité.

### R-022 — routage CI par pertinence

**Statut : LOCAL_SANS_PROMOTION.**

Le mécanisme C2 est techniquement qualifié ; il sert de cas positif pour l’outillage, pas de règle imposant un routeur à toute CI.

## 4. Décisions de portée à soumettre après l’audit

Les unités suivantes sont suffisamment soutenues pour qu’une **décision de support et de portée** soit légitime. Elles ne sont pas promues par ce plan.

### 4.1 Noyau d’interaction et de gouvernance agentique

Candidats à examiner ensemble :

- `R-019` — interventions humaines typées ;
- `R-020` — autorité technique distribuée ;
- `R-033` — provenance / garantie / autorité / ratification ;
- `R-034` — portée exacte des décisions et autorisations ;
- `R-035` — mutation destructive ;
- `R-038` — mutation versionnée confinée ;
- `R-039` — intelligibilité sémantique Human-First.

**Décision à prendre :** quelles formulations doivent être directement accessibles aux agents, à quel niveau — racine, méthodologie, science ou Git — sans recopier les mêmes fonctions dans plusieurs surfaces.

**Critère :** une promotion n’est justifiée que si le support courant ne porte pas déjà suffisamment la fonction ou si l’expérience de reprise montre un défaut d’accès réel.

### 4.2 Noyau scientifique/conceptuel

Candidats à examiner comme **règles scientifiques actives**, non comme méta-règles génériques :

- `R-025` — constance ≠ stabilisation ;
- `R-026` — énoncé indexé ;
- `R-027` — cible / accès / constitution ;
- `R-028` — dimensions de l’enquête ≠ portée ;
- `R-029` — typage des chemins lorsque discriminant ;
- `R-030` — vocabulaire disciplinaire prioritaire ;
- `R-031` — résultat / soutien / verdict ;
- `R-032` — non-détection discriminante ;
- `R-036` — réinstruction inter-domaines ;
- `R-037` — conservation des négatifs.

**Décision à prendre :** vérifier si le cadre scientifique courant et l’`AGENTS.md` déjà sur `main` suffisent ou si certaines fonctions ont besoin d’un portage local plus direct. Aucun besoin de nouvelle taxonomie n’est établi.

### 4.3 Représentation de la science vivante

`R-009` est suffisamment soutenue, mais son **support exact** reste une décision de conception.

Options à comparer ultérieurement :

1. points d’entrée vivants locaux ;
2. état porté principalement par les issues actives ;
3. vue dérivée légère ;
4. combinaison minimale.

Refuser par défaut un tableau de bord global supplémentaire tant qu’un gain distinct n’est pas démontré.

## 5. Fonctions à instruire pour mécanisation

La mécanisation n’est justifiée que pour des propriétés effectivement observables par la machine. Elle ne doit ni inventer un verdict scientifique ni automatiser une décision humaine de portée.

### M1 — intégrité d’écriture / read-back

Source : `R-021`.

Fonction : après une réponse d’écriture 5xx ou ambiguë, relecture obligatoire avant de considérer l’état connu.

Propriété mécanisable : réponse d’écriture ambiguë + état du fichier/ref après l’appel.

Candidat : wrapper/connecteur Git qui impose un read-back et suspend la séquence si l’état est contradictoire ou illisible.

### M2 — pré-vol de mutation versionnée

Source : `R-038`.

Fonction : cible/fonction → lecture état/SHA → action de bonne classe → refus du no-op/diff vide → contrôle terminal.

Propriétés mécanisables : SHA courant, existence du chemin, diff vide, branche cible, résultat terminal.

Limite : la **fonction scientifique** ou la légitimité d’une mutation destructive ne sont pas calculables par ce mécanisme ; `R-035` reste un contrôle sémantique.

### M3 — pertinence de contrôles coûteux

Source : `R-022` comme cas local.

Fonction : exécuter un contrôle spécifique uniquement lorsque les changements peuvent réellement toucher sa propriété protégée.

Propriétés mécanisables : chemins modifiés, dépendances déclarées, prédicat positif/négatif.

Condition : ne généraliser qu’après test d’un faux négatif de routage possible.

### M4 — détection, attribution et sévérité

Source : `R-003` + cas #82/#105–#107.

Fonction : distinguer :

```text
propriété recherchée
→ contrôle effectivement traversé
→ cause exacte du signal
→ sévérité correspondant au risque protégé
```

Propriétés mécanisables : couverture du contrôle, classes d’erreur, cause détectée, niveau de sortie.

Limite : la signification scientifique de la propriété et la suffisance probatoire restent hors de l’automatisation.

### M5 — protection contre mutation de mauvaise classe

Sources : `R-034`, `R-035`, `R-038`.

Fonction : empêcher qu’une action explicitement qualifiée comme lecture/diagnostic soit matérialisée par erreur comme suppression ou mutation destructive.

Mécanisation possible seulement lorsque le type d’acte est explicitement disponible dans le contexte/outillage. Ne pas inférer automatiquement l’autorisation scientifique depuis un label.

## 6. Fonctions à ne pas automatiser comme verdicts

Même si une infrastructure peut assister leur application, ne pas automatiser la décision elle-même pour :

- validité scientifique d’une cible, d’un modèle, d’un prior ou d’une paramétrisation ;
- seuil d’évidence scientifique ;
- interprétation scientifique ou philosophique ;
- décision de réouverture d’un programme scientifique ;
- passage inter-domaines et reformulation de la question ;
- promotion durable d’une règle ou d’un document de gouvernement ;
- décision de merge ;
- qualification d’une intervention comme ratification humaine lorsque la provenance effective n’est pas établie.

## 7. Régimes historiques à laisser retirés

Ne pas ouvrir d’action de restauration pour :

- une seule unité substantielle active comme règle générale ;
- `SOURCE_HIERARCHY` ou workflows rigides à trois branches ;
- P29 littéral exhaustif ;
- P28 comme veto général à la création ;
- réflexivité continue ;
- seuil numérique universel de shadow learning ;
- automatisation générale du shadow ;
- auto-clôture / cycle de vie universel des PR ;
- datation prospective générale ;
- nombre brut d’issues/branches comme mesure de complexité ;
- ancienneté = dette ;
- Git comme archive intangible sans exception ;
- originalité comme filtre scientifique général ;
- `constante effective` comme classe transverse propre au projet ;
- question génétique autonome comme centre général ;
- accès comme centre universel ;
- ordre universel formation → constitution → accès.

D5 reste une **décision programmatique active**, pas une règle générique à promouvoir.

## 8. Séquence d’exécution post-audit

### Étape 1 — acquise

```text
matrice
→ relations
→ synthèse exécutive
→ contre-audit de la synthèse
→ reconsolidation de l’ancrage
```

### Étape 2 — présente sortie

```text
plan d’action dérivé = PRESENT
```

### Étape 3 — suivante

Construire la **cartographie fonctionnelle des besoins mécanisables** en partant de M1–M5 et des fonctions de reprise, sans choisir encore d’outil.

### Étape 4

Comparer pour chaque fonction :

```text
règle interprétée
vs mécanisme infrastructurel
vs combinaison des deux
vs absence de changement
```

### Étape 5

Seulement ensuite rechercher :

- capacités natives Git/GitHub ;
- capacités des connecteurs/API/MCP réellement disponibles ;
- outils open source gratuits et maintenus ;
- coût d’intégration, de maintenance, d’apprentissage et de réversibilité.

### Étape 6 — frontière humaine

Présenter séparément les décisions de portée : promotion agentique, localisation des règles, mécanisation, éventuelle migration et merge.

## 9. Déclencheurs de révision du plan

Réviser ce plan seulement si :

- la matrice change matériellement ;
- une nouvelle relation invalide une fusion ou une séparation ;
- un contre-cas renverse un statut probatoire ;
- un mécanisme d’outillage montre qu’une règle prose est inutile ou au contraire nécessaire ;
- une décision humaine modifie la portée autorisée ;
- l’état du dépôt rend un support choisi obsolète.

En l’absence de l’un de ces déclencheurs, la prochaine opération est la cartographie fonctionnelle, non une nouvelle archéologie ou une promotion immédiate dans `AGENTS.md`.

## Statut

```text
PLAN_ACTION = DERIVE_DE_LA_MATRICE
PROMOTION_AGENTS = NON_EFFECTUEE
MIGRATION_INFRASTRUCTURE = NON_EFFECTUEE
OUTIL_CHOISI = AUCUN
PROCHAINE_OPERATION = CARTOGRAPHIE_FONCTIONNELLE_MECANISABLE
MERGE_#139 = NON_AUTORISE
```
