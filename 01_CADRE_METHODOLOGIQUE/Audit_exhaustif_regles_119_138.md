# Audit exhaustif et étude des règles et régimes — fenêtre de départ #119 à #138

## Fonction

Cette pièce est l’ancrage courant de la PR #139. Elle porte l’état récupérable de l’audit des règles explicites et implicites du dépôt, de leurs régimes, effets, contre-cas et récursivités.

La fenêtre #119–#138 était un point de départ, pas une frontière. L’étude a remonté les antécédents nécessaires, suivi les conséquences pertinentes, exécuté une passe indépendante repo-led, une étude exhaustive de second ordre du matériau empirique conversationnel fourni, puis un prototype 2D local et sa première épreuve aveugle par agents neufs.

Aucune sortie de cette PR n’est une autorité normative par simple présence. `AGENTS.md` n’est pas modifié et le merge n’est pas autorisé.

## État courant — 21 août 2026

```text
AUDIT_HISTORIQUE_REPO_LED = EFFECTUE
SATURATION_HISTORIQUE_POUR_DECOUVERTE_GENERALE = ATTEINTE

ETUDE_SECOND_ORDRE_MATERIAU_EMPIRIQUE = EFFECTUEE
COUVERTURE_MATERIAU = 71/71 EPISODES
LECTURE_BRUTE_CONTINUE = OUI
PASSE_INDEPENDANTE_MATERIAU→PHENOMENES = OUI
PASSE_INVERSE = OUI
CONTRE_PASSE_AVEC_#139 = OUI
ABLATION_DES_LACUNES = OUI
SATURATION_DANS_CE_CORPUS_FIXE = ATTEINTE
SATURATION_UNIVERSELLE = NON_REVENDIQUEE

MATRICE_BASE = 39 UNITES
DELTA_SECOND_ORDRE = 3 UNITES (R-040 à R-042)
ETAT_ANALYTIQUE_EFFECTIF = 42 UNITES
RELATIONS_BASE = 44
DELTA_RELATIONS = 8
ETAT_RELATIONNEL_EFFECTIF = 52

PROTOTYPE_2D_LOCAL = CONSTRUIT
TEST_GUIDAGE_CONTROLE = POSITIF
CONTRE_TEST_SILENCE = PASS_4_SUR_4

BLIND_TEST_AGENT_NEUF_PHASE_I = PILOTE_EXECUTE
N_PAR_CONDITION = 1
SCORE_D17 = 42/48
SCORE_D61 = 42/48
ERREURS_CRITIQUES = 0_VS_0
D17 = ORGANISATION_FONCTIONNELLE
D61 = FICHES_PLUS_RELATIONS
REDUCTION_VOLUME_ENTREE_D17 = ENVIRON_28.1_POURCENT
GAIN_EXACTITUDE = NON_ETABLI
NON_INFERIORITE_FONCTIONNELLE = SOUTENUE_DANS_CE_PILOTE
GAIN_EFFICACITE_DOCUMENTAIRE = CANDIDAT_SOUTENU
REPLICATION_N2_PAR_CONDITION = REQUISE_AVANT_PHASE_II
SEDIMENTATION_DURABLE_PROTO_2D = NON_ETABLIE

PROMOTION_NORMATIVE = NON_EFFECTUEE
AGENTS_MODIFIE = NON
INSTALLATION_OUTIL = NON
MERGE_#139 = NON_AUTORISE
```

## Sorties courantes

### Base et second ordre

- `matrice_regles_audit.csv` — 39 unités R-001 à R-039 ;
- `relations_regles_audit.csv` — 44 relations REL-001 à REL-044 ;
- `Etude_second_ordre_materiau_empirique.md` — méthode, couverture, saturation, ablation et verdicts ;
- `codage_second_ordre_materiau_empirique.csv` — 71 épisodes et 15 familles empiriques finales ;
- `delta_matrice_second_ordre_materiau_empirique.csv` — R-040 à R-042 ;
- `delta_relations_second_ordre_materiau_empirique.csv` — REL-045 à REL-052.

La séparation base/delta conserve explicitement le changement apporté par le second ordre. Elle est comparative et probatoire, non une duplication d’autorité.

### Prototype et tests

- `Prototype_2D_local_reprise_audit.md` ;
- `Test_gain_guidage_prototype_2D.md` ;
- `Contre_test_silence_prototype_2D.md` ;
- `Consigne_exercice_reprise_agent_neuf.md` ;
- `Dossier_17.md` ;
- `Dossier_61.md` ;
- `Protocole_experimentateur_agent_neuf.md` ;
- `Grille_scoring_agent_neuf.csv` ;
- `Reponse_brute_agent_Dossier_17.md` ;
- `Reponse_brute_agent_Dossier_61.md` ;
- `Scoring_blind_test_agent_neuf_pilote.csv` ;
- `Resultats_blind_test_agent_neuf_pilote.md`.

### Reconsolidations

- `Synthese_executive_audit_regles.md` ;
- `Plan_action_post_audit_regles.md` ;
- `Proposition_portee_post_audit_regles.md` ;
- cartographie des fonctions mécanisables et comparaison d’outillage déjà réalisées.

## Résultat du second ordre empirique

La saturation a été établie seulement après lecture ouverte, recherche inverse des phénomènes tardifs, relecture brute complète, compression fonctionnelle et ablation contre la matrice.

Quinze familles empiriques finales couvrent les 71 épisodes. Douze sont déjà absorbées ou distribuées dans R-001–R-039. Trois fonctions indépendantes restent :

### R-040 — intégrité des transformations de représentation

Lorsqu’une représentation devient l’entrée d’une étape suivante, vérifier ce qui a été conservé, perdu, ajouté ou requalifié.

`justesse locale != suffisance pour l’usage aval`.

### R-041 — statut probatoire d’une règle

`formulée != appliquée != observée != testée != soutenue/falsifiée != ratifiée != promue`.

Une application sans incident n’est pas une preuve d’efficacité.

### R-042 — remontée de résolution

`solution locale != connaissance causale != apprentissage transférable`.

Une résolution ne remonte que si sa valeur de transport est réelle et si elle peut être rendue récupérable sans créer de méta-travail disproportionné.

Deux résultats ne sont volontairement pas réifiés comme règles supplémentaires : le régime d’une règle, déjà porté par la matrice, et le cycle de vie d’une candidate, qui est une trajectoire/processus.

## Prototype 2D local

Le prototype organise localement un sous-système récursif selon :

**horizontal** : déclencheur → objet → contrôle → qualification → retour → silence/arrêt ;

**vertical** : reprise ↕ raccord de représentation ↕ audit de second ordre ↕ statut probatoire ↕ remontée de résolution.

Les relations sont typées ; proximité graphique ≠ causalité, autorisation ou promotion.

Le test contrôlé a montré un gain de navigation local et le contre-test de silence a donné 4/4 PASS. Ces deux passes n’étaient pas aveugles.

## Blind test agent neuf — Phase I

La série a été pré-enregistrée avant toute réponse : consigne commune silencieuse sur l’objet comparatif, deux dossiers neutres, clé d’assignation séparée et grille de scoring ex ante.

Deux chats éphémères neufs ont fourni les premières réponses, conservées verbatim avant scoring.

Résultat pilote :

```text
D17 = 42/48
D61 = 42/48
ERREURS_CRITIQUES = 0/0
```

Révélation après gel du score :

- `Dossier_17` = organisation fonctionnelle dérivée du prototype 2D ;
- `Dossier_61` = fiches + relations.

Le pilote ne montre **aucun gain d’exactitude globale** : égalité 42/48. Il montre en revanche une non-infériorité provisoire de l’organisation fonctionnelle avec environ 28,1 % de mots d’entrée en moins : 1065 contre 1482, pour des réponses de longueur presque identique : 963 contre 986 mots.

Le profil des omissions diffère :

- D17 rend davantage visibles certains retours et changements de niveau ;
- D61 conserve mieux certains détails atomiques locaux.

Ce contraste doit être reproduit avant d’être interprété comme effet stable.

```text
VERSION_FORTE_HYPOTHESE = NON_SOUTENUE_PAR_CE_PILOTE
# pas de gain de score global

VERSION_ETROITE = SOUTENUE_PROVISOIREMENT
# même score global + zéro erreur critique avec moins de matériau d'entrée
```

## Outillage et portée

La comparaison d’outillage reste négative pour une nouvelle plateforme générale. Les besoins mécaniques utiles sont déjà largement portés par Git/GitHub, les SHA, les PR, le workflow existant et les scripts locaux.

Le précédent delta P1–P5 n’est plus terminal. État de proposition :

- candidats directs les plus forts : R-034, R-032, R-038 ;
- candidat étroit : R-033 ;
- amendement du noyau préférable : R-025 ;
- fonction très forte dans le régime audit/promotion, support agentique à décider : R-041 ;
- exposition supplémentaire avant promotion : R-040, R-042.

Aucune de ces lignes n’est promue automatiquement.

## Condition de réouverture

Réouvrir l’archéologie historique ou l’étude empirique seulement si apparaît un signal discriminant : épisode oublié, nouvelle version du matériau, famille sans rattachement, contre-cas renversant un statut, relation empêchant une fusion, provenance changeant une autorité, ou nouvelle interaction réelle produisant une fonction absente.

En l’absence d’un tel signal, recommencer une lecture générale du même corpus serait du coût sans information nouvelle démontrée.

## Prochaine opération

1. répéter le blind test Phase I une fois par condition avec les **mêmes fichiers gelés** ;
2. scorer les deux nouvelles réponses avec la **même grille** avant toute modification ;
3. seulement après cette réplication, décider si le signal justifie une Phase II écologique avec dépôt contrôlé ;
4. aucune promotion dans `AGENTS.md`, migration d’outil ou fusion ne découle automatiquement du test.
