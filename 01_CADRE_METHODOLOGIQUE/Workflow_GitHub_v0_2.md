# Workflow GitHub v0.2

## Branches thematiques ephemeres et branche d'integration

### 1. Fonction

La v0.2 met a jour le workflow v0.1 en y ajoutant un modele de
branches. Elle conserve la regle centrale du v0.1 :

```text
les decisions conceptuelles restent soumises a validation explicite ;
les synchronisations documentaires, controles, commits et pushs
peuvent etre delegues apres stabilisation.
```

Objectif du modele : rendre la validation visible dans Git, avec
trois regles seulement.

### 2. Le modele

```text
main : l'etat valide du corpus. Il recoit des merges, jamais du
travail direct.

branches thematiques : une par chantier ouvert (exemples :
philosophie, methodologie, cycles). Chacune porte les documents de
son chantier, vit le temps du chantier, se merge dans main a la
validation, puis se supprime.

travail : branche d'integration locale, union des chantiers ouverts.
C'est l'etat quotidien du dossier : tout y est visible en meme temps.
Elle se resynchronise depuis main apres chaque merge ; elle reste
locale au flux de travail et main ne recoit jamais rien d'elle
directement.
```

Circuit complet :

```text
chantier -> branche thematique -> validation -> merge dans main ->
suppression de la branche -> resynchronisation de travail.
```

### 3. Les trois regles de sobriete

```text
1. trois branches thematiques vivantes au maximum ; une quatrieme
   attend la cloture d'une des trois.
2. les fichiers partages entre chantiers (README racine, index
   raisonne, cartes consolidees) se modifient sur une seule branche
   a la fois, designee au moment d'ouvrir le chantier.
3. une branche thematique se merge en entier : la validation porte
   sur le chantier, ses commits racontent les etapes.
```

### 4. Etat a la mise en place (juillet 2026)

```text
branche methodologie : reecriture positive v0.2 et v0.3, protocole
de test et copies, present workflow v0.2.
branche philosophie : branche 06_PHILOSOPHIE (README, situations 01
a 04, carte de la philosophie implicite), note d'ouverture
genetique, fiche d'horizon anthropique, plan de preparation de
l'arene.
branche travail : integration des deux, etat courant du dossier.
branche heritee agent/reprise-cycle-cosmologique : a merger ou a
cloturer lors de la reprise du cycle cosmologique.
```

### 5. Commandes de reference

Le shell local est Windows PowerShell : une commande par ligne
(le separateur && appartient a d'autres shells).

Ouvrir un chantier :

```text
git checkout main
git checkout -b <theme>
```

Integrer au quotidien :

```text
git checkout travail
git merge <theme>
```

Valider un chantier :

```text
git checkout main
git merge <theme>
git push
git branch -d <theme>
git checkout travail
```

Resynchroniser et publier les chantiers en cours :

```text
git checkout travail
git merge main
git push origin travail <theme>
```

Regle de lecture : ver