# Audit exhaustif et étude des règles et régimes — fenêtre de départ #119 à #138

## Fonction

Cette pièce est l’ancrage courant de la PR #139. Elle porte l’état récupérable de l’audit des règles explicites et implicites du dépôt, de leurs régimes, effets, contre-cas et récursivités.

La fenêtre #119–#138 était un point de départ, pas une frontière. L’étude a remonté les antécédents nécessaires, suivi les conséquences pertinentes, exécuté une passe indépendante repo-led, une étude exhaustive de second ordre du matériau empirique conversationnel fourni, puis un prototype 2D local et une Phase I aveugle par agents neufs désormais répliquée à `n=2` par condition.

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

BLIND_TEST_AGENT_NEUF_PHASE_I = REPLIQUE_N2_PAR_CONDITION
D17_S1 = 42/48
D17_S2 = 42/48
D17_TOTAL = 84/96
D61_S1 = 42/48
D61_S2 = 40/48
D61_TOTAL = 82/96
ERREURS_CRITIQUES = 0_DANS_LES_4_REPONSES
REDUCTION_VOLUME_ENTREE_D17 = ENVIRON_28.1_POURCENT
GAIN_EXACTITUDE_GLOBAL = NON_DEMONTRE
SUPERIORITE_D17 = NON_ETABLIE
NON_INFERIORITE_D17 = REPRODUITE
GAIN_EFFICACITE_DOCUMENTAIRE = SOUTENU_PLUS_FORTEMENT
PHASE_II_ECOLOGIQUE = JUSTIFIEE_COMME_PROCHAIN_DISCRIMINANT
SEDIMENTATION_DURABLE_PROTO_2D = NON_ETABLIE

PROMOTION_NORMATIVE = NON_EFFECTUEE
AGENTS_MODIFIE = NON
INSTALLATION_OUTIL = NON
MERGE_#139 = NON_AUTORISE
```

## Base analytique

- `matrice_regles_audit.csv` — R-001 à R-039 ;
- `relations_regles_audit.csv` — REL-001 à REL-044 ;
- `Etude_second_ordre_materiau_empirique.md` + `codage_second_ordre_materiau_empirique.csv` ;
- `delta_matrice_second_ordre_materiau_empirique.csv` — R-040 à R-042 ;
- `delta_relations_second_ordre_materiau_empirique.csv` — REL-045 à REL-052.

Trois fonctions ont résisté au second ordre :

- `R-040` — intégrité des transformations de représentation ;
- `R-041` — statut probatoire d’une règle/pratique ;
- `R-042` — remontée de résolution.

Le régime d’une règle reste une dimension de la matrice et le cycle de vie d’une candidate une trajectoire/processus, pas une règle supplémentaire.

## Prototype 2D local

Le prototype organise localement le sous-système reprise/audit/apprentissage :

- horizontal : déclencheur → objet → contrôle → qualification → retour → silence/arrêt ;
- vertical : reprise ↕ raccord de représentation ↕ audit de second ordre ↕ statut probatoire ↕ remontée de résolution.

Le test contrôlé a montré un gain de navigation local ; le contre-test de silence a donné 4/4 PASS. Ces passes n’étaient pas aveugles.

## Blind test agent neuf — Phase I complète à n=2

Le protocole a gelé avant toute réponse : consigne commune silencieuse sur l’objet comparatif, deux dossiers neutres, clé d’assignation séparée et grille de scoring ex ante.

Les quatre réponses ont été conservées verbatim avant scoring.

| Condition | Série 1 | Série 2 | Total | Erreurs critiques | Entrée |
|---|---:|---:|---:|---:|---:|
| D17 — organisation fonctionnelle | 42/48 | 42/48 | 84/96 | 0 | 1065 mots |
| D61 — fiches + relations | 42/48 | 40/48 | 82/96 | 0 | 1482 mots |

Le résultat ne démontre pas une supériorité générale de D17 : l’écart moyen est seulement de +1 point sur 48. En revanche, deux propriétés sont désormais reproduites :

1. D17 n’est inférieur à D61 dans aucune des deux séries ;
2. D17 conserve cette qualité avec environ 28,1 % de matière d’entrée en moins.

Le gain soutenu est donc actuellement **documentaire et de guidage**, pas une hausse démontrée de l’exactitude globale.

### Profil récurrent

- D17 rend plus régulièrement visibles les changements de niveau, retours et arrêt global ;
- D61 expose davantage de détail atomique, mais cet avantage ne produit pas un meilleur score moyen ;
- le point faible commun reste la transition d’un problème local vers une portée globale, notamment la nécessité d’un contrôle indépendant/contre-échantillon.

Sorties de la réplication :

- `Reponse_brute_agent_Dossier_17_replication.md` ;
- `Reponse_brute_agent_Dossier_61_replication.md` ;
- `Scoring_blind_test_agent_neuf_replication.csv` ;
- `Resultats_blind_test_agent_neuf_phase_I_n2.md`.

## Portée

Le précédent delta P1–P5 n’est plus terminal. État de proposition :

- candidats directs forts : R-034, R-032, R-038 ;
- candidat étroit : R-033 ;
- amendement du noyau préférable : R-025 ;
- fonction très forte dans audit/promotion, support agentique à décider : R-041 ;
- exposition supplémentaire avant promotion : R-040, R-042.

Aucune de ces qualifications ne vaut décision humaine de promotion.

## Prochaine opération

Une troisième répétition du même test fermé apporterait désormais peu d’information marginale. Le prochain discriminant doit changer le régime d’usage : **Phase II écologique avec dépôt contrôlé**.

Contraintes déjà acquises pour cette Phase II :

1. partir d’un même SHA propre de `main`, pas de #139 ;
2. une seule condition expérimentale visible par agent ;
3. même chemin et même point d’entrée dans les deux environnements ;
4. navigation réelle dans le dépôt autorisée ;
5. conserver les tâches, réponses brutes, chemins/sources consultés et erreurs de raccord ;
6. ne pas exposer protocole, clé, scoring ni condition concurrente ;
7. aucune promotion dans `AGENTS.md`, migration d’outil ou fusion ne découle automatiquement du test.

```text
PHASE_I = SUFFISAMMENT_INSTRUITE
PHASE_II_ECOLOGIQUE = PROCHAINE_OPERATION
ACTION_NORMATIVE_AUTOMATIQUE = NON
MERGE_#139 = NON_AUTORISE
```
