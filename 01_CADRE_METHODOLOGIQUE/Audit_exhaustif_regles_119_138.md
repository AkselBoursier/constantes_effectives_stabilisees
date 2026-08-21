# Audit exhaustif et étude des règles et régimes — fenêtre de départ #119 à #138

## Fonction

Cette pièce est l’ancrage courant de la PR #139. Elle porte l’état récupérable de l’audit des règles explicites et implicites du dépôt, de leurs régimes, effets, contre-cas et récursivités.

La fenêtre #119–#138 était un point de départ, pas une frontière. L’étude a remonté les antécédents nécessaires, suivi les conséquences pertinentes, exécuté une passe indépendante repo-led, une étude exhaustive de second ordre du matériau empirique conversationnel fourni, puis un prototype 2D local, une Phase I aveugle répliquée à n=2 par condition et une Phase II écologique désormais complète.

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
NON_INFERIORITE_D17_PHASE_I = REPRODUITE
COMPRESSION_ENTREE_D17 = ENVIRON_28.1_POURCENT
SUPERIORITE_D17 = NON_ETABLIE

PHASE_II_ECOLOGIQUE = COMPLETE
BASE_COMMUNE_PHASE_II = main@c9deaf1fe86b742d9227f0385e975809f64dc9bd
D61_SHA = c9deaf657ff15b8395aa54dd63e313561a58b7c6
D61_FIDELITE = 48/48
D61_NAVIGATION = 20/20
D17_SHA = 267a894ad75c3d90e3c83fe1c9bb819c3038ca1b
D17_FIDELITE = 48/48
D17_NAVIGATION = 20/20
ERREURS_CRITIQUES_PHASE_II = 0_DANS_LES_2_REPONSES
CONTAMINATION_PHASE_II = NON
FICHIERS_CONSULTES_D61 = 9
FICHIERS_CONSULTES_D17 = 9
ISSUES_CONSULTEES = 0_DANS_LES_2_CONDITIONS
NON_INFERIORITE_D17_PHASE_II = ETABLIE_SUR_CETTE_PAIRE
GAIN_NAVIGATION_NOMBRE_FICHIERS = NON_DEMONTRE
GAIN_EFFICACITE_DOCUMENTAIRE = SOUTENU

PROMOTION_NORMATIVE = NON_EFFECTUEE
AGENTS_MODIFIE = NON
INSTALLATION_OUTIL = NON
MERGE_#139 = NON_AUTORISE
```

## Résultat du second ordre empirique

Trois fonctions ont résisté à l’ablation contre la matrice antérieure :

### R-040 — intégrité des transformations de représentation
`justesse locale != suffisance pour l’usage aval`.

### R-041 — statut probatoire d’une règle
`formulée != appliquée != observée != testée != soutenue/falsifiée != ratifiée != promue`.

### R-042 — remontée de résolution
`solution locale != connaissance causale != apprentissage transférable`.

Le régime d’une règle reste une dimension de la matrice ; le cycle de vie d’une candidate reste une trajectoire/processus.

## Prototype 2D et Phase I

```text
D17 = 42/48 puis 42/48 = 84/96
D61 = 42/48 puis 40/48 = 82/96
ERREURS_CRITIQUES = 0/4
```

La supériorité générale de D17 n’est pas établie ; sa non-infériorité avec environ 28,1 % de matière d’entrée en moins est reproduite.

## Phase II écologique — complète

Base commune : `main@c9deaf1fe86b742d9227f0385e975809f64dc9bd`.

Branche séquentielle : `reprise/controle-20260821`.

Les deux incarnations avaient le même point d’entrée, les mêmes quatre cas, la même consigne externe et les mêmes fichiers du dépôt principal. Une seule pièce variait : `00_REPRISE/guide_reprise.md`.

### Condition D61 — fiches + relations

```text
SHA = c9deaf657ff15b8395aa54dd63e313561a58b7c6
FIDELITE = 48/48
NAVIGATION = 20/20
ERREURS_CRITIQUES = 0
CONTAMINATION = NON
FICHIERS_CONSULTES = 9
ISSUES_CONSULTEES = 0
REPONSE = 2098_MOTS
```

### Condition D17 — organisation fonctionnelle

```text
SHA = 267a894ad75c3d90e3c83fe1c9bb819c3038ca1b
FIDELITE = 48/48
NAVIGATION = 20/20
ERREURS_CRITIQUES = 0
CONTAMINATION = NON
FICHIERS_CONSULTES = 9
ISSUES_CONSULTEES = 0
REPONSE = 1898_MOTS
```

Les cinq fichiers communs avaient exactement les mêmes blob SHA dans les deux incarnations. Le guide D17 contenait environ 28,1 % de mots en moins que D61.

Il n’existe donc aucun gain de score brut ni de nombre de fichiers consultés pour D17 sur cette paire. Le résultat soutenu est plus étroit : D17 conserve la qualité décisionnelle et la discipline de navigation de D61 avec une surface de guide sensiblement plus compacte, sans augmentation observée des erreurs critiques.

L’opérateur humain a en outre déclaré, après gel de la seconde réponse, n’avoir lu ni modifié les réponses, ni cherché des informations sur l’état du dépôt ou les conditions pendant les tests. Cette déclaration est conservée comme attestation procédurale humaine, non comme mesure indépendante du résultat.

Rapport final : `Resultats_phaseII_ecologique_final.md`.

## Condition de réouverture générale

Réouvrir l’archéologie historique ou l’étude empirique seulement sur signal discriminant : épisode oublié, nouvelle version du matériau, famille sans rattachement, contre-cas renversant un statut, relation empêchant une fusion, provenance changeant une autorité ou nouvelle interaction réelle produisant une fonction absente.

## Prochaine décision de portée

Une nouvelle répétition des mêmes quatre cas avec le même modèle aurait désormais un faible gain marginal.

La décision suivante doit porter sur le régime d’usage du prototype, sans promotion automatique :

1. essai réel local et ablable de reprise avec la surface fonctionnelle dérivée ;
2. test sur un autre sous-système avant toute sédimentation transverse ;
3. refus de sédimentation si le coût d’une surface dérivée supplémentaire est jugé supérieur au gain de compression.

Aucune de ces options n’est autorisée par le seul succès des tests. Une décision humaine explicite de portée est requise.