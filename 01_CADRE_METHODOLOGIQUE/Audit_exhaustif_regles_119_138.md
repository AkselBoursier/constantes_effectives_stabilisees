# Audit exhaustif et étude des règles et régimes — fenêtre de départ #119 à #138

## Fonction

Cette pièce est l’ancrage courant de la PR #139. Elle porte l’état récupérable de l’audit des règles explicites et implicites du dépôt, de leurs régimes, effets, contre-cas et récursivités.

La fenêtre #119–#138 était un point de départ, pas une frontière. L’étude a remonté les antécédents nécessaires, suivi les conséquences pertinentes, exécuté une passe indépendante repo-led, une étude exhaustive de second ordre du matériau empirique conversationnel fourni, puis un prototype 2D local, une Phase I aveugle répliquée à n=2 par condition et désormais une Phase II écologique pré-enregistrée.

Aucune sortie de cette PR n’est une autorité normative par simple présence. `AGENTS.md` n’est pas modifié et le merge n’est pas autorisé.

## État courant — 21 août 2026

```text
AUDIT_HISTORIQUE_REPO_LED = EFFECTUE
SATURATION_HISTORIQUE_POUR_DECOUVERTE_GENERALE = ATTEINTE

ETUDE_SECOND_ORDRE_MATERIAU_EMPIRIQUE = EFFECTUEE
COUVERTURE_MATERIAU = 71/71 EPISODES
SATURATION_DANS_CE_CORPUS_FIXE = ATTEINTE
SATURATION_UNIVERSELLE = NON_REVENDIQUEE

ETAT_ANALYTIQUE_EFFECTIF = 42 UNITES
ETAT_RELATIONNEL_EFFECTIF = 52 RELATIONS

PROTOTYPE_2D_LOCAL = CONSTRUIT
TEST_GUIDAGE_CONTROLE = POSITIF
CONTRE_TEST_SILENCE = PASS_4_SUR_4

PHASE_I_AGENT_NEUF = REPLIQUEE_N2_PAR_CONDITION
D17_TOTAL = 84/96
D61_TOTAL = 82/96
ERREURS_CRITIQUES_PHASE_I = 0_DANS_LES_4_REPONSES
NON_INFERIORITE_D17 = REPRODUITE
COMPRESSION_ENTREE_D17 = ENVIRON_28.1_POURCENT
SUPERIORITE_D17 = NON_ETABLIE

PHASE_II_ECOLOGIQUE = PRE_ENREGISTREE
BASE_COMMUNE = main@c9deaf1fe86b742d9227f0385e975809f64dc9bd
BRANCHE_TEMPORAIRE = reprise/controle-20260821
CONDITION_1 = PRETE
REPONSE_CONDITION_1 = NON_ENCORE_OBTENUE
SCORING_PHASE_II = GELE_AVANT_REPONSE

PROMOTION_NORMATIVE = NON_EFFECTUEE
AGENTS_MODIFIE = NON
INSTALLATION_OUTIL = NON
MERGE_#139 = NON_AUTORISE
```

## Second ordre empirique

Trois fonctions ont résisté à l’ablation :

- `R-040` — intégrité des transformations de représentation : `justesse locale != suffisance pour l’usage aval` ;
- `R-041` — statut probatoire d’une règle : `formulée != appliquée != observée != testée != soutenue/falsifiée != ratifiée != promue` ;
- `R-042` — remontée de résolution : `solution locale != connaissance causale != apprentissage transférable`.

Le régime d’une règle reste une dimension de la matrice et le cycle de vie d’une candidate une trajectoire/processus, non une nouvelle unité normative.

## Prototype 2D et Phase I

Le prototype organise localement un sous-système récursif selon :

**horizontal** : déclencheur → objet → contrôle → qualification → retour → silence/arrêt ;

**vertical** : reprise ↕ raccord de représentation ↕ audit de second ordre ↕ statut probatoire ↕ remontée de résolution.

Phase I fermée :

```text
D17_S1 = 42/48
D17_S2 = 42/48
D17_TOTAL = 84/96
D61_S1 = 42/48
D61_S2 = 40/48
D61_TOTAL = 82/96
ERREURS_CRITIQUES = 0_DANS_LES_4_REPONSES
GAIN_EXACTITUDE_GLOBAL = NON_DEMONTRE
NON_INFERIORITE_D17 = REPRODUITE
GAIN_EFFICACITE_DOCUMENTAIRE = SOUTENU_PLUS_FORTEMENT
```

Une troisième répétition fermée identique aurait peu de valeur marginale.

## Phase II écologique

La Phase II teste désormais le régime d’usage, pas seulement l’extraction depuis un dossier fermé.

Pièces pré-enregistrées avant toute réponse :

- `Protocole_phase_II_ecologique.md` — réservé à l’expérimentateur ;
- `Consigne_phase_II_agent_neuf.md` — consigne neutre ;
- `Grille_scoring_phase_II_ecologique.csv` — score décisionnel séparé du score de navigation.

Architecture :

- même ancêtre Git pour les deux conditions : `main@c9deaf1f…` ;
- une seule branche temporaire visible par agent : `reprise/controle-20260821` ;
- même point d’entrée : `00_REPRISE/README.md` ;
- mêmes quatre cas écologiques ;
- une seule pièce varie : `00_REPRISE/guide_reprise.md` ;
- la seconde incarnation sera reconstruite après retour forcé de la branche sur le SHA de `main`, afin de ne pas exposer l’historique visible de la première condition.

La première incarnation diffère de `main` uniquement par six fichiers sous `00_REPRISE/` : point d’entrée, quatre cas et guide. Aucune PR expérimentale n’est ouverte.

L’agent peut consulter les fichiers du ref et, si réellement nécessaire, une issue explicitement routée par ces fichiers. Consulter #139, une autre branche, une PR, l’historique Git ou un artefact de scoring contamine l’essai.

## Portée

Le précédent delta P1–P5 reste un état pré-second-ordre, non un verdict terminal. Aucune qualification de règle ne vaut décision humaine de promotion.

La comparaison d’outillage reste négative pour une nouvelle plateforme générale. Les besoins mécaniques utiles sont largement portés par Git/GitHub, les SHA, les PR, le workflow existant et les scripts locaux.

## Condition de réouverture

Réouvrir l’archéologie historique ou l’étude empirique seulement sur signal discriminant : épisode oublié, nouvelle version du matériau, famille sans rattachement, contre-cas renversant un statut, relation empêchant une fusion, provenance changeant une autorité, ou nouvelle interaction réelle produisant une fonction absente.

## Prochaine opération

Obtenir la réponse brute de l’agent neuf sur la première incarnation Phase II, la geler sans relance, puis seulement :

1. scorer fidélité et navigation avec la grille pré-enregistrée ;
2. enregistrer le SHA exact de cette incarnation ;
3. forcer la branche temporaire sur le SHA commun de `main` ;
4. reconstruire les mêmes fichiers communs avec l’autre organisation de guide ;
5. lancer un second chat éphémère neuf.

```text
ACTION_NORMATIVE_AUTOMATIQUE = NON
SEDIMENTATION_DURABLE_PROTO_2D = NON_ETABLIE
MERGE_#139 = NON_AUTORISE
```
