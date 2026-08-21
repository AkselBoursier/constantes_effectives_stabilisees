# Prototype 2D local — reprise, audit et apprentissage du dispositif

## Statut

Vue **dérivée** de l’état analytique `42 unités / 52 relations` de la PR #139. Elle n’est ni une nouvelle autorité normative, ni une troisième matrice source.

Fonction : tester si une représentation 2D locale permet à un agent de reconstruire plus directement les déclencheurs, retours, conditions de silence et arrêts d’un sous-système récursif.

Sous-système : `R-008`, `R-009`, `R-010`, `R-011`, `R-014`, `R-015`, `R-039`, `R-040`, `R-041`, `R-042`. Deux ports externes restent visibles : `R-018` et `R-024`.

## Axes

**Horizontal** : `déclencheur → objet → opération/contrôle → qualification/décision → retour/synchronisation → silence/arrêt`.

**Vertical** : `reprise courante ↕ raccord de représentation ↕ audit de second ordre ↕ statut probatoire de la règle ↕ remontée de résolution`.

Types de relation : **D** déclenche ; **C** contrôle ; **S** supporte ; **R** requalifie ; **T** transport conditionnel ; **I** fonctions indépendantes. Aucune proximité graphique ne vaut causalité, autorisation ou promotion.

## Vue 2D

| Niveau | Déclencheur | Objet | Opération / contrôle | Qualification / décision permise | Retour vertical | Silence / arrêt |
|---|---|---|---|---|---|---|
| **Reprise courante** (`R-008`, `R-009`) | Chantier long, reprise, ou surface prétendant représenter l’état réel | Ancrage courant + science vivante : question, investigation, acquis, négatifs, blocages, décision ouverte, condition de reprise | Reconsolider l’état courant sans journal exhaustif | Surface suffisante pour la reprise, ou incomplète pour la fonction revendiquée | Si la surface résulte d’une réduction/synthèse : descendre vers `R-040` | Arrêt lorsque l’état courant est récupérable et non contradictoire ; pas de checkpoint à chaque action |
| **Raccord de représentation** (`R-040`) | Synthèse, réduction, traduction ou sortie devenant entrée aval ou état courant | Delta `source → représentation` : conservé, perdu, ajouté, requalifié | Comparer fonction de la source et de la sortie ; tester l’effet aval | `localement juste` peut coexister avec `insuffisant pour l’aval` | Si le delta touche prémisse, sélection ou capacité de détection : **D → R-010** ; sinon retour vers reprise | Silence si aucune perte pertinente ; arrêt quand delta et effets aval sont qualifiés |
| **Audit de second ordre** (`R-010`, `R-011`, `R-014`, `R-015`) | Angle mort réel, changement de corpus/régime, ancien audit dont une prémisse est touchée, ou audit global à clore | Critères, exclusions, sélection d’entrée, preuves locales, contre-échantillon | Réauditer ce que le dispositif pouvait manquer ; chercher aussi ce qui n’a pas été sélectionné ; même charge de preuve aux conclusions positives et critiques négatives | Conserver, requalifier ou borner un audit sans annuler automatiquement ses preuves locales | Si la question devient « la règle a-t-elle réellement été testée ? » : **C → R-041**. Si l’état courant change : **R → R-008/R-009** | Pas de réflexivité continue ; réaudit seulement si prémisse/exclusion/critère/portée change ; audit global arrêté après contre-échantillon et absence de nouvelle famille discriminante |
| **Statut probatoire d’une règle** (`R-041`) | Affirmation qu’une règle fonctionne, est testée/validée, ou projet d’extension/promotion | Formulée, appliquée, observée, mise à l’épreuve, soutenue/falsifiée, ratifiée, promue | Effet attendu, échec/coût, contre-cas/comparaison, observation discriminante | Application sans incident ≠ test ; le statut peut monter, descendre ou rester indécis | **R → audit** si les preuves révèlent un biais de sélection ; promotion reste extérieure et humaine | Silence lors d’un usage ordinaire sans prétention probatoire ; arrêt lorsque statut et preuves sont explicites |
| **Remontée de résolution** (`R-042`) | Résolution substantielle, coûteuse, récurrente ou causalement informative | Solution locale / connaissance causale / apprentissage candidat | Séparer les trois ; tester le transport ; choisir la surface existante la moins coûteuse | Rester local, rendre récupérable la connaissance, ou conserver un candidat à tester ailleurs | **S → R-008** si nécessaire à la reprise ; **T → R-024** si mécanisme envisagé ; **I → R-018** si simple idée à capturer | Arrêt si aucune valeur de reprise distincte ou si la connaissance est déjà portée ; pas de règle issue automatiquement de chaque correctif |
| **Interface Human-First** (`R-039`, transversal) | Nouvelle surface de reprise/décision destinée à un lecteur ou agent neuf | Sens humain primaire ; codes/IDs comme pointeurs secondaires | Vérifier que la compacité ne supprime ni référent ni distinction nécessaire | Lisible n’implique pas complet ; complet n’implique pas lisible | **I ↔ R-040** : auditabilité sémantique et intégrité de transmission restent deux contrôles différents | Compacité locale permise si référent récupérable et fonction comprise |

## Boucles admises

### A — représentation → audit → reprise

`R-008/R-009 → R-040 → [si perte matérielle] R-010/R-011/R-015 → requalification → R-008/R-009`.

Boucle requalifiante et opérationnelle, pas causalité scientifique.

### B — règle → épreuve → statut

`règle candidate/appliquée → R-041 → [si angle mort] R-010/R-015 → nouveau statut R-041 → décision humaine éventuelle`.

Arrêt si aucun nouveau discriminant n’apparaît.

### C — résolution → connaissance → reprise

`incident résolu → R-042 → [si valeur de reprise] R-008 → épisode ultérieur`.

La boucle ne transforme pas automatiquement l’apprentissage en règle.

## Relations sources principales

Le prototype ne crée aucune relation nouvelle. Il compose notamment :

- `R-008 → R-009` ; `R-009 → R-010` ; `R-010 → R-011` ;
- `R-014 → R-010` ; `R-015 → R-011` ;
- `R-040 → R-009` ; `R-040 → R-039` ; `R-040 → R-010` ;
- `R-041 → R-010` ; `R-041 → R-015` ;
- `R-042 → R-008` ; ports `R-042 → R-018` et `R-042 → R-024`.

## Conditions d’échec

Rejeter, réduire ou amender le prototype s’il :

1. fait inventer une causalité par simple proximité ;
2. fait croire que toute transformation déclenche un audit de second ordre ;
3. transforme toute résolution en règle ou post-mortem ;
4. remplace les CSV sources au lieu de les rendre plus navigables ;
5. nécessite autant de lecture que matrice + relations ;
6. masque une condition de silence ou d’arrêt ;
7. exige une nouvelle taxonomie pour être compris.

```text
PORTEE = LOCALE
SOURCE_AUTORITATIVE = NON
DERIVATION = 42 UNITES / 52 RELATIONS
NOUVELLE_REGLE = NON
NOUVELLE_RELATION = NON
PROMOTION = NON
```
