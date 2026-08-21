# Diagnostic de l’incident 409 et correction opérationnelle

## Objet

Documenter l’origine des conflits HTTP 409 rencontrés pendant les mutations GitHub de la PR #139 et vérifier une correction reproductible.

## Symptôme observé

Plusieurs appels `update_file` ont renvoyé `409 Conflict` avec un message du type « le fichier ne correspond pas au SHA fourni ».

Deux mécanismes distincts ont été observés derrière le même code :

1. **SHA de blob périmé** : `update_file` applique un verrouillage optimiste ; le SHA fourni doit être le blob courant du fichier. Une lecture ancienne, suivie d’une autre mutation du même fichier, rend le SHA précédent invalide.
2. **Mauvaise classe d’action** : certaines opérations visant à déplacer/réinitialiser une branche ont été envoyées à `update_file` au lieu de `update_ref`, parfois avec un SHA factice. Le conflit était alors déterministe et ne signalait pas une anomalie de GitHub.

## Cause racine

Le problème n’est donc pas un défaut unique du dépôt ou de GitHub. Il provient d’une combinaison de :

- réutilisation d’état mutable mis en cache pour des écritures dépendantes du contenu ;
- confusion entre deux primitives de mutation qui n’ont pas le même contrat :
  - fichier dépendant de son blob courant → `fetch_file` puis `update_file` avec le SHA fraîchement lu ;
  - déplacement de branche/ref → `update_ref` avec le commit SHA cible.

## Procédure corrective

### Mutation de fichier existant

1. lire le fichier immédiatement avant écriture ;
2. utiliser le blob SHA renvoyé par cette lecture ;
3. si une deuxième écriture séquentielle sur le même fichier est nécessaire, utiliser le `content_sha` renvoyé par la première écriture ou relire le fichier ;
4. ne jamais réutiliser un SHA stocké avant une mutation intermédiaire ;
5. en cas de 409, considérer l’état comme inconnu, relire et ne pas réessayer avec la même précondition.

### Mutation de branche/ref

Utiliser uniquement `update_ref`. Ne jamais employer `update_file` pour remettre une branche sur un commit.

## Vérification de la correction

La branche expérimentale `reprise/controle-20260821` a été déplacée avec `update_ref(force=true)` vers :

`c9deaf1fe86b742d9227f0385e975809f64dc9bd`

Une comparaison immédiate avec ce même SHA de `main` a retourné :

```text
status = identical
ahead_by = 0
behind_by = 0
total_commits = 0
files = []
```

Le symptôme original de neutralisation impossible est donc corrigé par la bonne primitive.

## Portée

Cette correction ne supprime pas les 409 légitimes : un 409 doit continuer à apparaître lorsqu’une précondition de blob est réellement périmée. Le but est d’éliminer les 409 produits par une mauvaise discipline d’écriture ou une mauvaise classe d’action.

```text
409_LEGITIME_SUR_SHA_PERIME = A_CONSERVER
REUTILISATION_SHA_PERIME = A_EVITER
BRANCH_RESET_PAR_UPDATE_FILE = INTERDIT_PAR_PROCEDURE
BRANCH_RESET_PAR_UPDATE_REF = VERIFIE
```

Ce diagnostic renforce fonctionnellement R-038 sans constituer par lui-même une décision de promotion normative dans `AGENTS.md`.
