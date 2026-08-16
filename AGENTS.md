# Guide d’amorçage pour agents

Ce fichier décrit **comment travailler dans le dépôt**. Il ne doit pas mémoriser l’état détaillé de chaque cycle ni devenir un second index.

Lire d’abord le [README](README.md), puis le point d’entrée local du cycle ou du volet concerné. Ne charger les documents méthodologiques spécialisés qu’au moment où la tâche les exige.

## 1. Mission et autorité

Le projet examine ce que les sciences peuvent soutenir lorsqu’elles qualifient de constante une grandeur, une relation, une valeur ou une structure.

Deux questions publiques organisent le travail :

1. Comment les sciences établissent-elles, utilisent-elles et déplacent-elles la frontière entre ce qui varie et ce qui tient ?
2. Par quelles structures, opérations et chemins de détermination un maintien devient-il opératoire ou affirmable dans un régime, et que change cette reconstruction pour l’enquête scientifique ?

L’agent peut inspecter, comparer, calculer, falsifier, proposer des corrections et exécuter les opérations techniques autorisées dans le périmètre déclaré. L’autorité humaine reste obligatoire pour les frontières scientifiques ou irréversibles : question de recherche, modèle, données, prior, paramétrisation scientifique, interprétation, seuil d’évidence, promotion durable et merge.

## 2. Parcours minimal

Pour une tâche locale :

1. lire le README ;
2. lire l’[accueil des cycles](02_CYCLES_PHYSIQUES/README.md) si la tâche est physique ou computationnelle ;
3. entrer dans le meilleur document local indiqué pour le cycle ;
4. lire l’issue active ou la décision qui borne la tâche, lorsqu’elle existe ;
5. remonter vers le [cadre canonique](01_CADRE_METHODOLOGIQUE/refondation-du-domaine.md), le [glossaire](GLOSSAIRE.md) ou une décision méthodologique seulement si une ambiguïté de rang, de terme ou de méthode l’exige.

Ne pas précharger l’intégralité du corpus « par sécurité ». La profondeur de lecture doit être proportionnée à la question.

## 3. Invariants human-first

Les noms sémantiques ci-dessous priment sur les anciens identifiants `Pxx`, `Dx`, `Tx` ou autres labels généalogiques.

- **Situer l’énoncé.** Identifier la cible, la transformation, le régime, le modèle ou schéma, la tolérance et la condition de rupture.
- **Séparer cible, accès et constitution.** Une robustesse d’accès n’est pas automatiquement une propriété physique ; une architecture constitutive ne fixe pas automatiquement la valeur de ses paramètres.
- **Séparer résultat, soutien et verdict.** Une borne, une tension ou une non-détection ne devient pas automatiquement un verdict de constance, de variation ou d’existence.
- **Borner la portée.** Ne pas étendre une conclusion au-delà du domaine effectivement instruit.
- **Typer les chemins quand cela change l’argument.** Physique, expérimental, métrologique, computationnel, inférentiel, historique et représentationnel ne sont pas interchangeables.
- **Employer le vocabulaire disciplinaire d’abord.** Une catégorie interne ne doit pas corriger ou écraser le vocabulaire plus précis du domaine.
- **Préserver provenance, temporalité et rang.** Distinguer état historique, décision actuelle, application documentaire et preuve locale.
- **Séparer exploration et ratification.** Un support exploratoire peut être utile sans acquérir d’autorité durable.
- **Exiger un gain net de complexité.** Une couche ou subdivision durable doit protéger une fonction identifiable et simplifier, remplacer ou rendre contrôlable une complexité au moins équivalente.
- **Conserver les sorties négatives et les suspensions.** Ne pas nettoyer un échec, un refus ou une dette pertinente pour obtenir une histoire plus nette.

## 4. Science et computation

Toujours conserver la séparation :

```text
calcul
≠ résultat computationnel
≠ qualification technique
≠ interprétation scientifique
≠ conséquence philosophique
≠ usage éditorial
```

Un changement de représentation, de sampler, d’oracle, de tolérance ou d’infrastructure n’est recevable comme optimisation que si la cible scientifique et les invariants nécessaires sont conservés ou si un amendement scientifique distinct l’autorise.

Les diagnostics mouvants d’un run restent dans ses sorties, journaux ou issue computationnelle. Ne pas recopier des `R-1`, taux d’acceptation, checkpoints ou états transitoires dans les README d’accueil.

## 5. Documents vivants et pièces figées

Choisir le type de document avant de l’écrire.

### Document vivant

Il représente ce qu’il faut comprendre **maintenant**. Le mettre à jour sous un nom stable par défaut ; Git porte son historique.

Ne pas créer automatiquement `v0.2`, `v0.3`, etc. pour chaque changement. Un numéro de version n’est justifié que s’il possède une fonction réelle : publication, format, interface, release, objet cité ou identité explicitement comparable.

### Pièce probatoire figée

Pré-enregistrement, extraction, protocole exécuté, résultat, décision située ou artefact dont l’état doit rester comparable. Ne pas le réécrire pour le rendre actuel ; créer une nouvelle pièce ou un successeur seulement si la fonction probatoire l’exige.

### Héritage documentaire

Ne pas renommer ou supprimer massivement les anciens fichiers versionnés. Avant tout déclassement, vérifier :

```text
contenu unique ?
dépendances ou liens entrants ?
fonction scientifique ou probatoire ?
fonction opérationnelle encore active ?
valeur généalogique réellement utile ?
```

Heuristique supplémentaire : si le fichier n’avait pas été nécessaire pour maintenir le contexte d’un agent avant Git/GitHub, aurait-il été créé pour une raison indépendante ? Si non, il est candidat au déclassement, pas à l’effacement automatique.

## 6. Issues, état du travail et mises à jour

Une issue porte une instruction bornée, des décisions et les étapes qui changent réellement l’état du travail. Elle ne doit pas devenir la copie exhaustive d’une conversation.

Consigner lorsqu’au moins un élément substantiel change : question, périmètre, résultat admis/refusé/suspendu, blocage durable, validation humaine, décision suivante, ouverture, remplacement, clôture ou réouverture.

Ne pas créer une mise à jour documentaire pour chaque action technique.

L’état mouvant du travail doit rester dérivable des issues et, lorsqu’une vue GitHub Project sera matériellement éprouvée, de cette vue. Ne pas copier dans un README un numéro d’issue « actuellement active » si cela crée une synchronisation manuelle permanente.

Une issue successeure est justifiée lorsqu’un vrai changement d’état, de question ou d’autorité rend l’ancien fil cognitivement ou méthodologiquement inadéquat ; pas simplement parce qu’il est long.

## 7. Séparation des volets et passages

Les voies **physique**, **computation**, **méthodologie** et **philosophie** restent séparées par défaut mais ne sont pas exclusives.

Lorsqu’une question, un résultat ou une dette exige un passage :

```text
identifier le besoin de passage
→ lier explicitement les dossiers concernés
→ déclarer ce qui est transféré et ce qui ne l’est pas
→ ré-instruire dans le volet compétent
→ aucune propagation automatique du verdict
```

Ne pas créer une taxonomie supplémentaire de « membranes », « portes » ou « interfaces » si des liens d’issues, des labels multiples et une formulation explicite suffisent.

## 8. Dette, suspension et transfert

Un transfert de dette n’est pas une clôture administrative. Le qualifier comme transfert scientifique seulement si :

1. la dette restante ne modifie plus le verdict courant du cycle d’origine ;
2. le cycle d’accueil offre un accès, un discriminant ou une structure explicative réellement différente ;
3. la question est reformulée, pas copiée ;
4. la provenance et la condition de retour sont conservées ;
5. le transfert n’ouvre rien automatiquement.

Sinon, employer simplement `dette différée` ou `suspendue`.

## 9. Discipline Git et mutations

- Travailler sur une branche ou un worktree dédié pour toute mutation substantielle.
- Ne pas mélanger dans une même PR des modifications scientifiques, documentaires et méthodologiques sans nécessité démontrée.
- Ne pas modifier `main` directement lorsqu’une PR bornée permet l’audit.
- Ne pas réécrire une archive ou un état daté pour simuler une cohérence actuelle.
- Ne pas importer une proposition ancienne sans vérification indépendante si elle redevient active.
- Ne pas transformer une trajectoire de calcul en histoire physique.
- Préférer une correction locale à une restructuration générale.
- Aucun merge sans autorisation humaine explicite et contrôle final du périmètre.

## 10. Rôle des points d’entrée

```text
README.md
= question du projet, navigation stable, doctrine documentaire minimale

AGENTS.md
= règles de travail stables pour humains et agents

02_CYCLES_PHYSIQUES/README.md
= meilleur point d'entrée courant de chaque cycle

issues
= travail en cours, arbitrages, validations, dettes et généalogie

Git
= histoire des documents vivants et des transformations du corpus

pièces figées
= preuves, protocoles, résultats et décisions comparables
```

L’index raisonné et les anciennes cartes restent consultables pour la profondeur généalogique ou documentaire, mais ne doivent pas redevenir des prérequis universels d’entrée.
