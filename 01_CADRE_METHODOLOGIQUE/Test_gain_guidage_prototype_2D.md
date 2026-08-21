# Test de gain de guidage — prototype 2D local

## Objet

Comparer la surface source actuelle — matrice `42 unités` + graphe `52 relations` — au prototype 2D local, sans traiter ce dernier comme autorité.

Le test porte sur un **gain de guidage** : retrouver le chemin pertinent, ses conditions de silence, ses retours et son arrêt sans inventer de propagation.

## Limite du test

Le test effectué ici est **contrôlé mais non aveugle** : il est exécuté dans la même session qui a construit le prototype. Il mesure fidélité, charge de navigation et complétude du chemin, mais ne démontre pas encore qu’un agent neuf sans contexte se comportera mieux.

Un blind test séparé reste nécessaire avant toute sédimentation durable.

## Rubrique

Pour chaque tâche :

- **fidélité** aux distinctions sources ;
- **chemin** des contrôles et retours ;
- **silence/arrêt** visibles ;
- **non-surpropagation** : aucune causalité, autorisation ou promotion inventée ;
- **charge de navigation** : unités/relations à reconstruire dans les CSV versus zones du prototype.

Le nombre de lectures est un indicateur documentaire, pas une mesure cognitive universelle.

## T1 — synthèse localement juste mais incomplète pour l’aval

Situation : une synthèse répond correctement à sa question locale mais devient le substrat d’une phase suivante ; une recherche scientifique vivante n’a pas été transportée.

Chemin source : `R-040 → R-010 → R-011/R-015 → R-009 → R-008`.

À préserver : ne pas déclarer la synthèse localement fausse ; qualifier le delta source→sortie ; second ordre seulement si effet aval ; contrôler la sélection d’entrée ; reconsolider l’état vivant ; arrêter après qualification du delta et absence de nouvelle famille discriminante.

Le prototype expose ce chemin dans deux lignes et la boucle A.

**Verdict T1 : gain fort.**

## T2 — règle appliquée plusieurs fois sans incident

Situation : une règle a été utilisée trois fois sans erreur visible. Peut-on la déclarer testée puis la promouvoir ?

Chemin source : `R-041 → R-015`, avec `R-010` seulement si anomalie de sélection/protocole.

À préserver : application ≠ test ; effet attendu ; critère d’échec/coût ; contre-cas/comparaison ; observation discriminante ; statut explicite ; promotion distincte et humaine ; silence pour usage ordinaire sans prétention probatoire.

Le prototype porte directement ces éléments et évite de déclencher automatiquement le second ordre.

**Verdict T2 : gain fort, surtout sur la condition de silence.**

## T3 — résolution coûteuse et causalement informative

Situation : un incident difficile est résolu ; la cause est comprise et pourrait être utile ailleurs.

Chemin source : `R-042 → R-008`, avec ports conditionnels vers `R-018` ou `R-024`.

À préserver : solution locale ≠ connaissance causale ≠ apprentissage transférable ; transport testé avant généralisation ; connaissance récupérable si valeur de reprise ; outil seulement après choix fonctionnel ; capture légère si simple possibilité ; arrêt si rien de distinct ne mérite de remonter.

La ligne « remontée de résolution » et la boucle C rendent ces niveaux et sorties directement visibles.

**Verdict T3 : gain très fort de guidage vertical.**

## T4 — ancien audit confronté à un nouveau contexte

Situation : un ancien audit possède des preuves locales valides, mais un nouveau contexte pourrait affecter une prémisse.

Chemin source : `R-014 → R-010`, puis `R-011/R-015` seulement si la portée du réaudit le requiert.

À préserver : ne pas annuler l’ancien audit ; ne pas le déclarer automatiquement suffisant ; identifier la prémisse/exclusion/critère/portée touchée ; réaudit ciblé ; pas de récursivité permanente.

Le prototype regroupe ces conditions sans effacer les différences entre audit ancien, second ordre, contre-audit global et symétrie critique.

**Verdict T4 : gain modéré à fort.**

## Charge de navigation

| Tâche | Unités sources minimales | Relations minimales | Éléments de navigation source | Zones du prototype |
|---|---:|---:|---:|---:|
| T1 | 6 | 6 | 12 | 3 |
| T2 | 3 | 2 | 5 | 2 |
| T3 | 4 | 3 | 7 | 2 |
| T4 | 4 | 3 | 7 | 2 |
| **Total** | — | — | **31** | **9** |

Cette mesure n’implique pas qu’un agent lise toujours 31 lignes complètes : un filtrage peut réduire le coût. Elle montre que la vue 2D précompose des chaînes distribuées entre unités et arêtes.

Réduction documentaire indicative : `31 → 9` zones de navigation, environ **71 %** sur cet échantillon.

## Fidélité et pertes

### Conservé

- déclencheurs ;
- conditions de silence ;
- conditions d’arrêt ;
- différence local/global ;
- non-transitivité vers promotion ;
- auditabilité ≠ intégrité de transmission ;
- solution ≠ connaissance ≠ apprentissage ;
- types de rétroaction.

### Non transporté volontairement

- sources historiques détaillées ;
- épisodes complets ;
- statut probatoire détaillé de chaque unité ;
- actions documentaires spécifiques de toutes les lignes ;
- contre-cas complets.

Ces éléments restent dans les CSV sources : le prototype sert au guidage, pas à la qualification finale.

### Fausse causalité

Aucune relation du prototype n’est présentée comme causalité physique. Les boucles A–C sont qualifiées comme opérationnelles, requalifiantes ou conditionnelles.

### Sur-déclenchement

Aucun scénario n’exige automatiquement un audit général :

- T1 seulement si perte pertinente pour l’aval ;
- T2 pas de second ordre sans anomalie de protocole/sélection ;
- T3 arrêt possible sans remontée ;
- T4 réaudit ciblé seulement si une prémisse réelle est touchée.

## Verdict contrôlé

```text
FIDELITE_AUX_SOURCES = PASS
CONDITIONS_DE_SILENCE_ET_ARRET = PASS
FAUSSE_CAUSALITE = NON_DETECTEE
SURPROPAGATION_AUTOMATIQUE = NON_DETECTEE
GAIN_DE_NAVIGATION = POSITIF
GAIN_LE_PLUS_FORT = GUIDAGE_VERTICAL_R-042 + RACCORDEMENT_R-040
SEDIMENTATION_DURABLE = NON_ETABLIE
BLIND_TEST_AGENT_NEUF = ENCORE_REQUIS
```

Le prototype apporte donc un **gain réel dans ce test documentaire contrôlé** : il réduit les sauts entre unités et relations tout en conservant les distinctions qui déterminent action et arrêt.

Ce résultat ne suffit pas à le promouvoir comme surface durable.

## Épreuve suivante discriminante

Blind test : fournir soit les CSV sources, soit le prototype à un agent neuf sur des tâches équivalentes, sans annoncer l’hypothèse testée, puis comparer omissions, faux déclenchements, lectures/retours aux sources et besoin de clarification.

Conserver durablement le prototype seulement si l’agent neuf :

1. reconstruit au moins aussi fidèlement les chemins ;
2. manque moins de conditions de silence/arrêt ;
3. ne crée pas davantage de causalités ou autorisations fictives ;
4. réduit réellement les retours aux CSV ;
5. explique en langage naturel ce qui déclenche un changement de niveau ;
6. sait revenir aux sources lorsque le prototype ne suffit pas.

Sinon : réduire, amender ou supprimer le prototype sans perte normative.
