# Archives conversationnelles

Ce dossier conserve les exports conversationnels retenus pour la provenance du
projet, dans un régime archivistique distinct du corpus actif.

## Statut

```text
fonction : conserver trois séquences conversationnelles ayant accompagné le projet
rang : archive de provenance, sans autorité scientifique ou doctrinale active
ordre : chronologique, de la plus ancienne à la plus récente
formats : JSON archivistique et Markdown de lecture humaine
assainissement : accompli le 16 juillet 2026
extraction des transitions : non commencée ; décision séparée requise
```

Ces archives documentent une partie du travail conversationnel associé au
projet. Elles ne rendent pas accessibles les intuitions non formulées, les
travaux extérieurs aux échanges ni toutes les conditions ayant orienté les
décisions. Elles améliorent la provenance sans établir à elles seules une
généalogie complète, une attribution de propriété intellectuelle ou une preuve
scientifique.

## 1. Organisation

La numérotation suit l'ordre généalogique :

1. conversation la plus ancienne ;
2. conversation intermédiaire ;
3. conversation la plus récente.

Deux parcours restent possibles :

- **reconstruction historique** : lire de 1 vers 3 ;
- **reprise depuis l'état actuel** : lire de 3 vers 1.

L'ordre des fichiers ne constitue pas une hiérarchie d'autorité.

## 2. Formats conservés

Pour chaque conversation :

- le fichier `JSON` conserve la structure d'export, les rôles, les horodatages
  et le contenu des messages après assainissement ;
- le fichier Markdown fournit une version parallèle destinée à la lecture
  humaine.

Les deux fichiers proviennent du même export, mais leurs mises en forme sont
différentes. Le Markdown ne doit donc pas être traité comme une seconde source
indépendante.

## 3. Inventaire

| Nº | Titre d'export | Période couverte | Messages | Fichiers |
|---:|---|---|---:|---|
| 1 | Recherche sur les constantes | 8–9 juillet 2026 | 112 | `1-ChatGPT-Recherche sur les constantes.json` et `.md` |
| 2 | Analyse cohérence projet | 12–14 juillet 2026 | 99 | `2-ChatGPT-Analyse cohérence projet.json` et `.md` |
| 3 | Travail collaboratif projet GitHub | 14–16 juillet 2026 | 67 | `3-ChatGPT-Travail collaboratif projet GitHub.json` et `.md` |

Les titres et périodes proviennent des métadonnées d'export. L'inventaire ne
préjuge pas du contenu intellectuel de chaque séquence.

## 4. Assainissement

L'assainissement retire :

- l'identité personnelle et l'adresse électronique de l'en-tête d'export ;
- les liens privés de conversation ;
- les URL internes ou signées de pièces jointes ;
- les racines de chemins locaux et les chemins techniques temporaires.

Les messages, leurs rôles et leurs horodatages sont conservés. Les retraits
sont signalés par des marqueurs explicites. Le contrôle est intégré au script
[`audit/sanitize_conversation_exports.mjs`](../audit/sanitize_conversation_exports.mjs),
qui doit rester propre lors de chaque audit du corpus.

## 5. Empreintes des copies assainies

```text
45ab83d1d3663465068e048db86f5de125c34c2782f2be8c55bb5942afa04fba  1-ChatGPT-Recherche sur les constantes.json
d4213a56daade50586d31fc046b0ea85491a2b424ecd0878d1a4c8c5b4c49326  1-ChatGPT-Recherche sur les constantes.md
abc5a351e372cf60e748e0ba786c09a033755f2add3b1340657f5a391d7e3137  2-ChatGPT-Analyse cohérence projet.json
a7952f256ace90fbaaa1b580f4b7a9617b633d70313568b0e1383ab70cdcde20  2-ChatGPT-Analyse cohérence projet.md
16c70cdcee0d0272444d3013e3595f5ad4996694b67c4180cdc9e5e2e9669ec4  3-ChatGPT-Travail collaboratif projet GitHub.json
aac92480939f92998b5cdfa59efa5b0e96160cfbb6604b969e85d0b766ba3525  3-ChatGPT-Travail collaboratif projet GitHub.md
```

Ces empreintes décrivent les copies présentes après l'assainissement initial.
Toute correction ultérieure devra les mettre à jour.

## 6. Rapport au corpus actif

Ces archives pourront servir à une cartographie sélective des transitions :

- changements de question ;
- réorientations méthodologiques ;
- décisions et non-décisions ;
- alternatives abandonnées ;
- continuités importantes.

Cette extraction n'est pas automatique. Elle devra distinguer ce qui est
explicite, fortement impliqué ou seulement reconstruit rétrospectivement. Aucun
résultat physique, verdict philosophique ou attribution de contribution n'est
importé dans le corpus actif par le seul archivage.

## 7. Régime futur

L'export intégral des conversations n'est pas une obligation courante. Les
documents enregistrant une bifurcation importante devraient plutôt indiquer,
en quelques phrases naturelles, le constat de départ, le déplacement accompli
et ce qui reste hors décision.

Un nouvel export complet peut néanmoins être justifié :

- avant une remise à zéro importante du contexte ;
- après une bifurcation que les documents produits ne permettent pas de
  reconstruire correctement.

Cette règle conserve les transitions utiles sans transformer le corpus en
journal permanent du clavardage.
