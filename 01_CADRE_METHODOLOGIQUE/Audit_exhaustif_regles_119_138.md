# Audit exhaustif et étude des règles et régimes — fenêtre de départ #119 à #138

## Fonction

Cette pièce est l’ancrage courant de la PR #139. Elle porte l’état récupérable de l’audit des règles explicites et implicites du dépôt, de leurs régimes, effets, contre-cas et récursivités.

La fenêtre #119–#138 était un point de départ, pas une frontière. L’étude a remonté les antécédents nécessaires, suivi les conséquences pertinentes, exécuté une passe indépendante repo-led et, désormais, une **véritable étude exhaustive de second ordre du matériau empirique conversationnel fourni**.

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

PROMOTION_NORMATIVE = NON_EFFECTUEE
AGENTS_MODIFIE = NON
INSTALLATION_OUTIL = NON
MERGE_#139 = NON_AUTORISE
```

## Sorties courantes

### Base pré-second-ordre

- `matrice_regles_audit.csv` — 39 unités R-001 à R-039 ;
- `relations_regles_audit.csv` — 44 relations REL-001 à REL-044.

### Second ordre empirique

- `Etude_second_ordre_materiau_empirique.md` — méthode, couverture, saturation, ablation et verdicts ;
- `codage_second_ordre_materiau_empirique.csv` — 71 épisodes et 15 familles empiriques finales ;
- `delta_matrice_second_ordre_materiau_empirique.csv` — R-040 à R-042 ;
- `delta_relations_second_ordre_materiau_empirique.csv` — REL-045 à REL-052.

La séparation base/delta conserve explicitement le changement apporté par le second ordre. Elle est comparative et probatoire, non une duplication d’autorité.

### Reconsolidations

- `Synthese_executive_audit_regles.md` — état 42/52 ;
- `Plan_action_post_audit_regles.md` — actions requalifiées ;
- `Proposition_portee_post_audit_regles.md` — proposition humaine post-second-ordre ;
- cartographie des fonctions mécanisables et comparaison d’outillage déjà réalisées.

## Résultat du second ordre empirique

La première passe sur le matériau n’était pas saturée. La saturation a été établie seulement après : lecture ouverte, recherche inverse des phénomènes tardifs, relecture brute complète, compression fonctionnelle et ablation contre la matrice.

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

## Structures volontairement non réifiées

Deux résultats de second ordre ne deviennent pas des lignes supplémentaires :

- le régime d’une règle est déjà porté par les colonnes de la matrice ;
- le cycle de vie d’une candidate est une trajectoire horizontale du dispositif, à représenter dans les relations/vue 2D, pas une règle auto-référentielle.

## Matrice 2D — état conceptuel

Le matériau soutient désormais empiriquement :

**horizontal** : déclencheur → exposition → observable → qualification → décision → action/silence/révision ;

**vertical** : incident → cause → connaissance → candidate → test/enforcement → contrôle du contrôle → représentation/reprise.

R-040 protège les raccords de représentation, R-041 les changements de statut probatoire et R-042 la remontée sélective des résolutions.

Les relations doivent être typées ; proximité graphique ≠ causalité.

## Outillage

La comparaison d’outillage reste négative pour une nouvelle plateforme générale. Les besoins mécaniques utiles sont déjà largement portés par Git/GitHub, les SHA, les PR, le workflow existant et les scripts locaux.

R-040–R-042 sont principalement sémantiques/processuelles : une infrastructure peut aider à tracer ou rappeler, pas automatiser leur verdict.

## Requalification de la portée

Le précédent delta P1–P5 n’est plus terminal. Ses preuves restent valides localement, mais la décision doit intégrer le second ordre.

État de proposition :

- candidats directs les plus forts : R-034, R-032, R-038 ;
- candidat étroit : R-033 ;
- amendement du noyau préférable : R-025 ;
- fonction très forte dans le régime audit/promotion, support agentique à décider : R-041 ;
- exposition supplémentaire avant promotion : R-040, R-042.

Aucune de ces lignes n’est promue automatiquement.

## Condition de réouverture

Réouvrir l’archéologie historique ou l’étude empirique seulement si apparaît un signal discriminant : épisode oublié, nouvelle version du matériau, famille sans rattachement, contre-cas renversant un statut, relation empêchant une fusion, provenance changeant une autorité, ou nouvelle interaction réelle produisant une fonction absente.

En l’absence d’un tel signal, recommencer une lecture générale du même corpus serait du coût sans information nouvelle démontrée.

## Prochaine frontière

La PR #139 est désormais suffisamment instruite pour **réinstruire la décision de portée à partir de l’état 42/52**, sans prétendre que toutes les fonctions fortes doivent être promues.

Deux opérations non normatives restent recevables avant toute écriture dans `AGENTS.md` :

1. prototype 2D local dérivé des unités/relations, avec test de gain réel ;
2. dernier contrôle marginal de couverture sur `main` pour les seules fonctions envisagées à la promotion.

```text
ACTION_NORMATIVE_AUTOMATIQUE = NON
DECISION_HUMAINE_DE_PORTEE = REQUISE_AVANT_PROMOTION
MERGE_#139 = NON_AUTORISE
```
