# Plan d’action dérivé de l’audit des règles

## Fonction

Ce document est l’**état d’action courant** dérivé de la matrice, de la table de relations, de la synthèse, de la cartographie d’outillage et du contre-test empirique final.

Il ne transforme pas automatiquement une qualification en promotion normative.

Sources courantes :

- `matrice_regles_audit.csv` — 39 unités ;
- `relations_regles_audit.csv` — 44 relations ;
- `Synthese_executive_audit_regles.md` ;
- `Cartographie_fonctions_mecanisables.md` ;
- `Comparaison_capacites_outillage_post_audit.md` ;
- `Contre_test_empirique_delta_P1_P5.md` ;
- `Proposition_portee_post_audit_regles.md`.

Les statuts sont :

```text
FAIT
AUCUNE_ACTION_NOUVELLE
A_DECIDER_HUMAINEMENT
CONDITIONNEL
LOCAL_SANS_PROMOTION
RETIRE_OU_ABSORBE
MECANISATION_PARTIELLE_SEULEMENT
```

Aucun statut n’autorise le merge de #139.

## 1. Travaux de #139 déjà exécutés

### Audit historique et matrice

```text
inventaire/étude = FAIT
39 unités = MATRICÉES
44 relations = RELIÉES
saturation fonctionnelle de découverte de familles = ATTEINTE
lecture de tout commentaire historique = NON REVENDIQUÉE
archéologie = RÉOUVRABLE SUR INDICE DISCRIMINANT
```

### Audit de second ordre

**Statut : FAIT dans le régime de #139.**

La synthèse a reçu une passe de contrôle qui a détecté plusieurs omissions de niveau puis s’est stabilisée sans nouvelle famille. La réflexivité continue reste refusée.

### Reconsolidation de reprise

**Statut : FAIT.**

L’ancrage courant a été mis à jour pour que la reprise ne dépende pas de la lecture de tous les checkpoints historiques.

### Cartographie d’outillage

**Statut : FAIT pour la tranche issue de #139.**

Les fonctions mécanisables et non mécanisables ont été distinguées avant recherche d’outil.

### Comparaison native / externe

**Statut : FAIT.**

Aucune nouvelle plateforme ou installation externe n’est justifiée pour les fonctions prioritaires. Git/GitHub, le workflow existant et les scripts locaux portent déjà l’essentiel des protections mécaniques utiles.

### Contre-test empirique P1–P5

**Statut : FAIT.**

Le matériau empirique conversationnel et les pièces scientifiques/techniques du dépôt ont requalifié le delta : cinq fonctions utiles, mais quatre nouvelles unités textuelles autonomes au plus ; `R-025/P4` doit être fusionnée dans le noyau scientifique existant si elle est promue.

## 2. Conserver et appliquer sans nouvelle couche

Aucune nouvelle inscription n’est justifiée actuellement pour :

- `R-001` — rang machine/science ;
- `R-002` — localisation causale, absorbable dans le noyau causal/probatoire ;
- `R-003` — couplage probatoire ;
- `R-004` — routage/autorité documentaire ;
- `R-005` — statut documentaire ;
- `R-006` — double contre-factuel, local seulement ;
- `R-007` — courant + généalogie, avec exceptions ;
- `R-008` — ancrage + transitions substantielles ;
- `R-010` à `R-015` — outils d’audit dans leurs régimes bornés ;
- `R-016` — effet inter-chantiers ;
- `R-017` — non-prolifération proportionnée ;
- `R-018` — capture légère ;
- `R-020` — distribution actuelle de l’autorité technique ;
- `R-022` — routage CI C2 local ;
- `R-023` — activité ≠ qualification ;
- `R-024` — outil par fonction ;
- `R-026` à `R-031` — noyau scientifique déjà largement porté ;
- `R-035` à `R-037` — mutation destructive, réinstruction inter-domaines, conservation des négatifs.

`AUCUNE_ACTION_NOUVELLE` signifie ici : **continuer à appliquer dans le bon régime**, pas abandonner la fonction.

## 3. Décision normative réellement restante

Le contre-test réduit le delta soumis à décision humaine à cinq fonctions, dont quatre ajouts autonomes au plus.

### P1 / R-033 — provenance apparente et ratification humaine

```text
STATUT = A_DECIDER_HUMAINEMENT
PREUVE = AMBIGUITE_STRUCTURELLE_FORTE
DOMMAGE_DIRECT_ISOLE = NON_ETABLI
PORTEE_PROPOSEE = DECISIONS_SCIENTIFIQUES_IRREVERSIBLES_OU_HAUTE_AUTORITE
```

Action candidate : une phrase courte au point d’autorité agentique ; pas d’archéologie de provenance pour chaque commentaire.

### P2 / R-034 — portée exacte des décisions

```text
STATUT = A_DECIDER_HUMAINEMENT
PREUVE = TRES_FORTE
CONTRE_CAS_CAUSAL = #117
CAS_POSITIFS = alpha3-alpha5 + autres portes
```

Action candidate : promouvoir une règle courte de non-transitivité des actes.

### P3 / R-032 — non-détection discriminante

```text
STATUT = A_DECIDER_HUMAINEMENT
PREUVE_SCIENTIFIQUE = FORTE
CAS = alpha4 / alpha5
```

Action candidate : promouvoir une phrase scientifique courte précisant qu’une absence de signal n’est probante que pour les alternatives effectivement testables.

### P4 / R-025 — constance ≠ stabilisation

```text
STATUT = A_DECIDER_HUMAINEMENT
FONCTION = FORTE
NOUVELLE_LIGNE_AUTONOME = NON_RECOMMANDEE
```

Action candidate : si promotion décidée, **amender une formulation scientifique existante** plutôt qu’ajouter une unité supplémentaire.

### P5 / R-038 — pré-vol des mutations dépendant de l’état courant

```text
STATUT = A_DECIDER_HUMAINEMENT
PREUVE = TRES_FORTE
INCIDENTS = __invalid__ + répétitions 409 de #139
PORTAGE = TEXTE_COURT + MECANISATION_PARTIELLE_SI_DISPONIBLE
```

Action candidate : borner le pré-vol aux mutations de fichier/ref ou objets dont l’écriture dépend de l’état courant ; ne pas l’imposer à tout appel API append-only.

## 4. Décisions secondaires non urgentes

### R-009 — science vivante

**Statut : `CONDITIONNEL / SUPPORT_LOCAL_A_DECIDER`.**

Ne pas créer de tableau de bord global par principe. Lorsqu’une surface prétend représenter l’état scientifique d’un domaine, elle doit porter l’état vivant nécessaire à la reprise.

### R-019 — interventions humaines typées

**Statut : `CONDITIONNEL`.**

Fonction soutenue, mais risque symétrique de sur-interpréter une instruction claire. Une éventuelle formulation doit être courte et ne se déclencher que lorsque le type d’intervention change l’action.

### R-039 — Human-First

**Statut : `CONDITIONNEL / TEST_PAR_USAGE`.**

Continuer à l’éprouver sur les nouvelles surfaces et le prototype 2D. Pas de réécriture massive.

### Vue 2D des récursivités

**Statut : `PROTOTYPE_LOCAL_JUSTIFIE / NON_SEDIMENTÉ`.**

Construire seulement un prototype dérivé des CSV, sur un sous-système borné, si l’on veut tester le gain de guidage agentique. Ne pas créer une troisième source normative.

## 5. Mécanisation : verdict actuel

### À conserver dans l’existant

- routage C2 dans GitHub Actions ;
- `audit_structure_corpus.py` et distinction ERROR/WARNING ;
- branches/PR/SHAs pour confinement et provenance ;
- contrôle humain du merge.

### Mécanisation partielle possible si l’interface le permet

- read-back après réponse d’écriture ambiguë (`R-021`) ;
- lecture SHA/état avant remplacement d’un fichier/ref (`R-038`) ;
- détection de no-op/diff vide ;
- contrôle terminal après mutation ;
- instrumentation de couverture de branches uniquement pour un harnais Python complexe lorsque cette observation manque réellement.

### Non justifié actuellement

- nouvelle plateforme de gouvernance ;
- installation générale de `pre-commit` pour protéger les écritures API ;
- Coverage.py généralisé ;
- Vale bloquant ;
- système ADR/MADR complet ;
- Log4brains ;
- automatisation générale du shadow learning ;
- auto-clôture temporelle des issues/PR.

L’état réel des protections/rulesets de `main` n’a pas pu être observé avec le connecteur disponible. Il reste `ETAT_NON_OBSERVE`, pas `ABSENT`.

## 6. Régimes historiques à ne pas réactiver

Ne pas restaurer comme normes générales :

- une seule unité substantielle active ;
- P29 littéral ;
- P28 comme veto général à la création ;
- limite brute de branches ;
- réflexivité continue ;
- seuil numérique universel de shadow ;
- ancienneté = dette ;
- nombre brut d’issues/branches = complexité ;
- Git comme historique intangible sans exception ;
- originalité comme filtre scientifique général ;
- `constante effective` comme classe transverse propre ;
- accès comme centre universel ;
- ordre universel formation → constitution → accès.

D5 reste une décision programmatique active, pas une règle générique.

## 7. État de séquence

La séquence décidée par #139 a été exécutée jusqu’à la frontière normative :

```text
matrice                          = FAIT
relations                        = FAIT
synthèse exécutive               = FAIT
contre-audit synthèse            = FAIT
plan d’action                    = FAIT / RECONSOLIDE
cartographie fonctions/outillage = FAIT
comparaison capacités            = FAIT
contre-test empirique P1-P5      = FAIT
proposition de portée            = REQUALIFIEE

promotion AGENTS                 = NON EFFECTUEE
migration/infrastructure         = NON OUVERTE
installation outil               = NON
merge #139                       = NON AUTORISE
```

## 8. Prochaine frontière

La prochaine opération **normative** serait une décision humaine sur le delta requalifié :

```text
P1 + P2 + P3 + P5 = ajouts autonomes candidats
P4 = amendement du noyau existant
```

Sans cette décision, il n’existe plus de tâche d’audit générale justifiant de continuer à produire de nouvelles règles ou de nouveaux supports.

L’archéologie se réouvre seulement si une anomalie discriminante apparaît : nouvelle famille, contradiction de portée, contre-cas matériel, mécanisme d’enforcement absent ou filiation nécessaire à une décision.

## Statut terminal courant

```text
AUDIT_GENERAL = SUFFISAMMENT_INSTRUIT_POUR_DECISION_DE_PORTEE
DELTA = REQUALIFIE_EMPIRIQUEMENT
ACTION_NORMATIVE_AUTOMATIQUE = NON
AGENTS_MODIFIE = NON
OUTIL_NOUVEAU = NON_JUSTIFIE
DECISION_HUMAINE_DE_PROMOTION = REQUISE
MERGE_#139 = NON_AUTORISE
```
