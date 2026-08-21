# Plan d’action dérivé de l’audit des règles

## Fonction

Ce document est l’état d’action courant de #139 après intégration de l’étude exhaustive de second ordre du matériau empirique. Il ne transforme aucune qualification en promotion normative.

État de référence :

```text
39 unités de base
+ 3 unités de second ordre (R-040 à R-042)
= 42 unités effectives

44 relations de base
+ 8 relations de second ordre
= 52 relations effectives
```

Pièces nouvelles : `Etude_second_ordre_materiau_empirique.md`, `codage_second_ordre_materiau_empirique.csv`, `delta_matrice_second_ordre_materiau_empirique.csv`, `delta_relations_second_ordre_materiau_empirique.csv`.

Aucun statut ci-dessous n’autorise le merge de #139.

## 1. Travaux acquis

```text
audit historique / repo-led                 = FAIT
matrice de base 39                          = FAIT
table de relations de base 44               = FAIT
étude second ordre matériau 71/71           = FAIT
saturation fonctionnelle corpus fixe        = ATTEINTE
delta R-040 à R-042                         = MATÉRIALISÉ
relations second ordre                      = MATÉRIALISÉES
synthèse exécutive                          = RECONSOLIDÉE
cartographie outillage                      = FAIT
comparaison capacités                       = FAIT
installation outil                          = NON JUSTIFIÉE
AGENTS                                      = INCHANGÉ
merge                                       = NON AUTORISÉ
```

L’ancienne conclusion `AUDIT_SUFFISAMMENT_INSTRUIT_POUR_DECISION_P1_P5` est retirée comme état terminal : P1–P5 restent utiles, mais étaient pré-second-ordre empirique.

## 2. Actions sans nouvelle promotion

Continuer à appliquer dans leur régime les noyaux déjà soutenus : rang machine/science, indexation des énoncés, cible/accès/constitution, portée des conclusions, conservation des négatifs, passage inter-domaines, routage documentaire, confinement Git, non-prolifération proportionnée et séparation activité/qualification.

`AUCUNE_ACTION_NOUVELLE` ne signifie pas abandon de la fonction.

Les mécanismes actuels Git/GitHub/CI restent préférés aux nouvelles plateformes pour les propriétés réellement observables par la machine.

## 3. Nouvelles unités issues du second ordre

### R-040 — intégrité des transformations de représentation

**Statut : `CANDIDATE_FORTE / PAS_PROMOTION_IMMEDIATE`.**

Action : conserver dans l’audit et l’éprouver sur le prochain raccord réel où une représentation devient l’entrée d’une phase, décision ou état courant.

Critère : vérifier `conservé / perdu / ajouté / requalifié` et l’effet aval seulement si la transformation change de fonction ou de granularité pertinente.

Ne pas transformer toute reformulation en audit de transmission.

### R-041 — statut probatoire d’une règle

**Statut : `TRES_FORT_DANS_LE_REGIME_AUDIT_PROMOTION / DECISION_DE_SUPPORT_A_INSTRUIRE`.**

Action : utiliser immédiatement dans #139 pour qualifier les règles ; ne pas l’imposer comme protocole expérimental lourd à chaque usage quotidien.

Déclencheur : prétention `testée`, `validée`, `fonctionne`, extension de portée ou promotion.

### R-042 — remontée de résolution

**Statut : `FORTE_COMME_PROCESSUS_VERTICAL / PROMOTION_TRANSVERSE_NON_ETABLIE`.**

Action : lors de la prochaine résolution substantielle hors C7, distinguer explicitement `solution locale / connaissance causale / apprentissage candidat`, puis tester si quelque chose mérite de remonter.

Ne pas créer de registre général ni de post-mortem obligatoire pour les correctifs triviaux.

## 4. Ancien delta P1–P5 requalifié

P1–P5 ne sont plus le delta terminal, mais leurs preuves ne disparaissent pas.

- **P1 / R-033** : ambiguïté structurelle forte ; dommage direct isolé non établi ; portée seulement haute autorité/science/irréversible.
- **P2 / R-034** : très forte ; contre-cas causal #117 ; candidate de non-transitivité des actes.
- **P3 / R-032** : forte scientifiquement ; non-détection seulement si dispositif discriminant.
- **P4 / R-025** : fonction forte, mais amendement du noyau existant préférable à une nouvelle ligne.
- **P5 / R-038** : très forte pour mutations dépendant de l’état courant ; mécanisation partielle possible.

Aucune de ces fonctions n’est promue automatiquement par #139.

## 5. Décisions de portée à réinstruire

La décision humaine post-audit doit maintenant examiner trois classes séparées.

### Classe A — protections déjà fortement instruites pour accès agentique direct

À examiner : R-034, R-032, R-038 et, plus étroitement, R-033/R-025.

La question n’est pas seulement « règle vraie ? », mais « `AGENTS.md` actuel porte-t-il déjà suffisamment son déclencheur et sa borne ? ».

### Classe B — fonctions de second ordre fortement qualifiées mais encore à exposer

- R-040 : futur raccord réel avant promotion agentique générale ;
- R-042 : future résolution substantielle hors C7 avant promotion transverse.

### Classe C — fonction de gouvernance du statut probatoire

R-041 est déjà suffisamment soutenue pour gouverner l’audit et la promotion des règles. Son support quotidien exact — prose agentique, méthodologie locale ou seulement protocole d’audit — reste à décider.

## 6. Vue 2D

**Statut : `PROTOTYPE_LOCAL_JUSTIFIE / NON_SEDIMENTÉ`.**

Le second ordre renforce sa fonction. Le prototype doit être dérivé des unités/relations existantes, non créer une troisième source normative.

Axe horizontal : déclencheur → exposition → observable → qualification → décision → action/silence/révision.

Axe vertical : incident → cause → connaissance → candidate → test/enforcement → contrôle du contrôle → représentation/reprise.

R-040, R-041 et R-042 doivent pouvoir y être placées sans arêtes ambiguës.

## 7. Outillage

Aucune nouvelle installation n’est ouverte.

Conserver : Git/PR/SHA, read-back après état ambigu, routage C2, scripts locaux et distinction signal/sévérité.

Les nouvelles fonctions R-040–R-042 sont principalement sémantiques ; une automatisation peut assister la trace, pas décider leur verdict.

## 8. Prochaine opération non normative recevable

Deux opérations restent possibles sans franchir la promotion :

1. construire un **prototype 2D local et dérivé**, sur un sous-système borné, puis tester son gain de guidage ;
2. contre-tester la proposition de portée actuelle contre l’état 42/52 et produire une proposition humaine finale sans modifier `AGENTS.md`.

Elles peuvent être séquencées ; aucune nouvelle archéologie générale n’est justifiée sans anomalie discriminante.

## Statut courant

```text
AUDIT_GENERAL = ACQUIS
SECOND_ORDRE_EMPIRIQUE = ACQUIS
ETAT_ANALYTIQUE = 42 UNITES / 52 RELATIONS
PROPOSITION_P1_P5 = PRE_SECOND_ORDRE / A_RECONSOLIDER
ACTION_NORMATIVE_AUTOMATIQUE = NON
AGENTS_MODIFIE = NON
INSTALLATION = NON
MERGE_#139 = NON_AUTORISE
```
