# Workflow GitHub v0.1

## Versionnement prudent du corpus

### 1. Fonction

Ce document fixe un workflow provisoire pour utiliser GitHub comme journal de versions du corpus.

Il ne modifie pas la methode theorique.

Il encadre seulement le passage entre :

```text
travail local,
stabilisation documentaire,
commit,
push GitHub,
et eventuelle relecture par branche ou pull request.
```

### 2. Principe central

Le workflow repose maintenant sur deux niveaux.

```text
niveau conceptuel : validation explicite requise ;
niveau documentaire et technique : delegation operative apres stabilisation controlee.
```

Quand une etape engage une decision theorique, taxonomique ou methodologique nouvelle, l'assistant signale :

```text
point de decision conceptuelle
```

et attend validation.

Quand une etape consiste seulement a synchroniser, nettoyer, indexer, committer ou pousser un etat documentaire deja stabilise, l'assistant peut agir directement et donner ensuite le resume exact.

### 3. Cycle normal de travail

Le cycle ordinaire est le suivant.

```text
1. Travailler localement dans les fichiers du corpus.
2. Controler la coherence documentaire.
3. Verifier les references croisees utiles.
4. Verifier l'etat Git local.
5. Identifier si le palier est conceptuel ou seulement documentaire.
6. Demander validation seulement si le palier est conceptuel.
7. Stager seulement les fichiers concernes.
8. Creer un commit avec message explicite.
9. Pousser vers la branche active ou vers origin/main selon le chantier.
10. Donner le resume exact du commit.
```

### 4. Criteres pour proposer un commit

Un commit devient pertinent quand au moins une unite documentaire est stabilisee.

Exemples :

```text
creation d'une fiche,
production d'une synthese,
synchronisation d'une carte,
mise a jour methodologique coherente,
correction d'une incoherence transversale,
ajout d'un protocole de travail.
```

Un commit n'est pas recommande pour :

```text
une idee encore ouverte,
une lecture exploratoire,
une correction non controlee,
ou une transition encore contradictoire.
```

### 5. Messages de commit

Les messages suivent une forme simple.

```text
docs: add cosmological stress test
docs: update active corpus index
chore: add github workflow note
```

Le prefixe `docs:` convient a la majorite du corpus.

Le prefixe `chore:` convient aux regles de travail, au depot ou aux fichiers techniques.

### 6. Branches et pull requests

Le travail peut rester sur `main` pour les petites etapes documentaires controlees.

Une branche dediee devient preferable pour :

```text
refonte de structure,
renommage massif,
reorganisation de dossiers,
revision longue de plusieurs familles,
ou modification risquant de rendre l'index temporairement instable.
```

Dans ce cas, la pull request sert d'espace de relecture.

Elle n'est pas obligatoire pour chaque petite correction.

### 7. Issues GitHub

Les issues peuvent servir plus tard de carnet de chantiers.

Pour l'instant, elles ne sont pas obligatoires.

Regle provisoire :

```text
ne pas transformer chaque idee en issue ;
ne creer une issue que si le chantier doit rester ouvert plusieurs sessions.
```

### 8. Discipline de versionnement

Le depot GitHub doit rester un outil de clarification.

Il ne doit pas remplacer la methode interne du corpus.

Regles :

```text
ne pas reecrire l'historique sans raison explicite ;
ne pas melanger plusieurs chantiers independants dans un commit ;
ne pas deplacer les archives sans table de correspondance ;
ne pas pousser une decision conceptuelle que l'utilisateur n'a pas validee.
```

### 9. Formule operative

```text
travailler localement,
stabiliser documentairement,
qualifier le palier,
valider si conceptuel,
committer si documentairement stable,
pousser,
resumer.
```
