# Dossier documentaire — reprise et audit

## Périmètre

Ce dossier décrit un sous-système méthodologique portant sur la reprise d’un chantier, les transformations de représentation, l’audit de second ordre, le statut probatoire d’une pratique et la remontée d’une résolution.

Les identifiants `R-xxx` servent de pointeurs. Ils ne constituent pas à eux seuls le sens des éléments.

## Convention de lecture

### Déroulement fonctionnel

`déclencheur → objet → opération/contrôle → qualification/décision → retour/synchronisation → silence/arrêt`

### Changements de niveau possibles

`reprise courante ↕ raccord de représentation ↕ audit de second ordre ↕ statut probatoire d’une pratique ↕ remontée de résolution`

Un changement de niveau n’est jamais automatique.

### Types de relations

- **déclenche** : un état ouvre légitimement un contrôle supplémentaire ;
- **contrôle** : une opération vérifie ou borne une autre ;
- **supporte** : une information est utile ou nécessaire à une autre fonction ;
- **requalifie** : une information change le statut ou la représentation sans prétention causale physique ;
- **transport conditionnel** : un transfert n’est recevable qu’après épreuve de portée ;
- **indépendant** : deux fonctions proches ne se remplacent pas.

La proximité de deux éléments ne vaut ni causalité, ni autorisation, ni promotion.

## Organisation fonctionnelle

| Niveau | Déclencheur | Objet à examiner | Opération / contrôle | Qualification ou décision permise | Retour possible | Silence / arrêt |
|---|---|---|---|---|---|---|
| **Reprise courante** (`R-008`, `R-009`) | Chantier long, reprise, ou surface prétendant représenter l’état réel | Ancrage courant + état scientifique vivant : question, investigation, acquis, négatifs, blocages, décision ouverte, condition de reprise | Reconsolider l’état courant sans journal exhaustif ; distinguer actif, dormant, veille, clos, suspendu | La surface est suffisante pour la reprise ou incomplète pour la fonction qu’elle revendique | Si la surface provient d’une réduction ou synthèse, examiner `R-040` | Arrêt lorsque l’état courant est récupérable et non contradictoire ; pas de checkpoint à chaque action |
| **Raccord de représentation** (`R-040`) | Une synthèse, réduction, traduction ou sortie devient entrée d’une étape aval ou prétend être l’état courant | Delta `source → représentation` : dimensions conservées, perdues, ajoutées, requalifiées | Comparer fonction de la source et de la sortie ; tester si une différence change l’usage aval | `localement juste` peut coexister avec `insuffisant pour l’aval` | Si le delta touche prémisse, sélection ou capacité de détection : déclencher `R-010`; sinon retour vers reprise | Silence si aucune perte pertinente pour l’usage aval ; arrêt quand delta et effets aval sont qualifiés |
| **Audit de second ordre** (`R-010`, `R-011`, `R-014`, `R-015`) | Angle mort réel, changement de corpus/régime, ancien audit dont une prémisse est touchée, ou audit global à clore | Critères, exclusions, sélection d’entrée, preuves locales conservées, contre-échantillon | Réauditer ce que le dispositif pouvait manquer ; chercher aussi ce qui n’a pas été sélectionné ; appliquer la même charge de preuve aux conclusions positives et critiques négatives | Conserver, requalifier ou borner un audit ; ne pas annuler automatiquement ses preuves locales | Si la question devient « cette pratique a-t-elle réellement été testée ? », passer à `R-041`. Si l’état courant change, reconsolider `R-008/R-009` | Pas de réflexivité continue ; réaudit seulement si prémisse/exclusion/critère/portée change. Pour un audit global : arrêt après contre-échantillon indépendant et absence de nouvelle famille discriminante |
| **Statut probatoire d’une pratique** (`R-041`) | Affirmation qu’une pratique fonctionne, est testée/validée, ou projet d’extension/promotion | Statut : formulée, appliquée, observée, mise à l’épreuve, soutenue/falsifiée, ratifiée, promue | Expliciter effet attendu, échec/coût, contre-cas ou comparaison et observation discriminante | Une application sans incident ne devient pas un test ; le statut peut monter, descendre ou rester indécis | Retour vers audit si les preuves révèlent un biais de sélection ; la promotion reste une décision extérieure | Silence lors d’un usage ordinaire sans prétention probatoire ; arrêt lorsque statut et preuves disponibles sont explicites |
| **Remontée de résolution** (`R-042`) | Résolution substantielle, coûteuse, récurrente ou causalement informative | Trois sorties : solution locale / connaissance causale / apprentissage candidat | Séparer les trois ; tester le transport ; choisir la surface existante la moins coûteuse où la connaissance utile pourra réapparaître | Rester local, rendre récupérable la connaissance causale, ou conserver un candidat à tester ailleurs | Vers `R-008` si connaissance nécessaire à la reprise ; vers `R-024` si mécanisme/outillage envisagé ; rester distinct de `R-018` si simple idée à capturer | Arrêt si aucune valeur de reprise distincte ou si la connaissance est déjà portée ; ne pas transformer chaque correctif en règle |
| **Interface de lecture** (`R-039`) | Nouvelle surface de reprise/décision destinée à un lecteur ou agent neuf | Sens humain, nom de l’objet, codes/IDs secondaires | Vérifier que la compacité ne supprime ni référent ni distinction nécessaire | Lisible n’implique pas complet ; complet n’implique pas lisible | `R-039` et `R-040` restent indépendants | Compacité locale permise si le référent est récupérable et la fonction comprise |

## Boucles admises

### Représentation → audit → reprise

`R-008/R-009 → R-040 → (si perte matérielle) R-010/R-011/R-015 → requalification → R-008/R-009`

Cette boucle est opérationnelle et requalifiante ; elle ne constitue pas une causalité scientifique.

### Pratique → épreuve → statut

`pratique formulée/appliquée → R-041 → (si biais/angle mort) R-010/R-015 → nouveau statut`

Une éventuelle promotion reste distincte. La boucle s’arrête si aucun nouveau discriminant n’apparaît.

### Résolution → connaissance → reprise

`incident résolu → R-042 → (si valeur de reprise) R-008`

L’apprentissage éventuel ne devient pas automatiquement une règle.

## Repères complémentaires

- `R-008 → R-009` : un ancrage de reprise scientifique doit porter l’état vivant nécessaire.
- `R-009 → R-010` : une perte d’état vivant peut déclencher un second ordre.
- `R-010 → R-011` : pour un audit global, contrôler aussi la sélection d’entrée.
- `R-014 → R-010` : un ancien audit n’est réaudité que si le nouveau contexte touche réellement prémisse, exclusion, critère ou portée.
- `R-015 → R-011` : la symétrie critique ne suffit pas lorsque le corpus d’entrée lui-même est asymétrique.
- `R-040 → R-039` : intelligibilité et intégrité du contenu transmis sont deux fonctions indépendantes.
- `R-041 → R-015` : succès, mauvais cas et coûts contribuent au statut probatoire sans auto-promotion.
- `R-042 → R-018` : capturer une possibilité n’est pas la même chose que remonter une connaissance causale.
- `R-042 → R-024` : règle, outil ou mécanisme transverse seulement après test de transport et comparaison du support.
