# Workflow GitHub v0.2

## Branches thematiques ephemeres et branche d'integration

### 1. Fonction

La v0.2 met a jour le workflow v0.1 en y ajoutant un modele de
branches. Elle conserve la regle centrale du v0.1 :

```text
les decisions conceptuelles restent soumises a validation explicite ;
les synchronisations documentaires, controles et commits locaux
peuvent etre delegues apres stabilisation ;
les pushs distants sont reserves aux jalons ou demandes explicites.
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

### 5. Frequence des commits et des pushs

Le workflow distingue maintenant deux gestes.

```text
commit local : point de sauvegarde et de lisibilite dans le depot local ;
push distant : publication du point de travail sur GitHub.
```

Il distingue aussi deux tailles de travail.

```text
micro-etape : correction locale, raccord ponctuel, ajustement de formulation ;
cycle de travail : ensemble coherent de modifications appele a toucher
plusieurs documents avant de produire un etat lisible.
```

Regle active :

```text
1. ne pas committer automatiquement chaque micro-etape ;
2. committer localement lorsque le cycle de travail en cours devient
   coherent et relisible ;
3. pousser sur GitHub seulement lorsqu'un jalon substantiel est atteint ;
4. grouper plusieurs commits locaux dans un meme push lorsque le chantier
   reste en cours ;
5. pousser immediatement si le travail risque d'etre perdu, si une branche
   doit etre partagee, si une validation de jalon l'exige, ou si l'auteur le
   demande explicitement.
```

Exemples de commit differe :

```text
une serie de corrections terminologiques dans plusieurs documents actifs ;
une reprise de cycle qui modifie fiche, synthese et carte ;
un audit en cours dont les corrections ne sont pas encore stabilisees ;
une sequence de raccords d'index avant cloture du lot.
```

Exemples de commit local immediat :

```text
fin d'un audit ou d'un lot coherent ;
changement de protocole stabilise ;
avant de basculer vers un autre chantier ;
avant une interruption longue ;
sur demande explicite de l'auteur.
```

Regle de regroupement :

```text
si un commit devient necessaire, verifier s'il existe d'autres changements
deja prets, relus et coherents avec le meme cycle de travail ;
les inclure dans le meme commit ou dans le meme geste local si cela evite une
nouvelle sequence de verification ;
laisser hors commit les changements ambigus, non relus, non lies au cycle, ou
manifestement produits par un etat externe comme OneDrive.
```

Exemples de jalon substantiel :

```text
audit transversal clos ;
carte ou synthese stabilisee ;
cycle ou lot documentaire termine ;
changement de protocole majeur a partager immediatement ;
avant une pause longue ou une bascule de branche importante.
```

Exemples de push differe :

```text
micro-correction terminologique ;
commit local de travail encore integre a un cycle ouvert ;
raccord README / index leger ;
correction de coquille ;
ajustement local sans effet de rang.
```

Regle budgetaire :

```text
le travail conceptuel et documentaire prime ;
les commits locaux restent disponibles mais ne doivent pas interrompre chaque
reponse ;
les operations Git distantes restent regulieres mais moins frequentes.
```

### 6. Controle editorial et verification

Les controles doivent suivre le risque.

```text
controle minimal courant : git status, git diff --check, revue du diff ;
controle renforce : recherche ciblee par rg lorsqu'un terme, un rang ou une
formulation sensible est modifie ;
controle lourd : seulement avant jalon, publication, fusion de branche, ou
sur demande.
```

Le controle ASCII systematique n'est plus une obligation de projet.

Regle active :

```text
1. conserver la coherence locale du fichier modifie ;
2. eviter le bruit typographique accidentel ;
3. ne pas lancer de balayage ASCII general sauf besoin explicite :
   code, formule technique, fichier deja strictement ASCII, export
   publication, ou demande de l'auteur.
```

### 7. Commandes de reference

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

Note :

```text
ces commandes de push valent pour les jalons ; elles ne sont plus executees
apres chaque micro-etape.
```

Regle de lecture : verifier la sortie de chaque ligne avant de
lancer la suivante ; PowerShell enchaine sans controler les echecs.

### 8. Formule de cloture

```text
main dit ce qui est valide, les branches disent ce qui est en
chantier, travail dit ou en est le dossier. Les commits locaux marquent les
cycles coherents ; les pushs distants marquent les jalons.
```
