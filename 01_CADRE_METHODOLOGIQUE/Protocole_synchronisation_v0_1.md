# Protocole de synchronisation v0.1

## Retro-ingenierie des pratiques du depot, rendues explicites

### 0. Statut documentaire

```text
statut : fiche methodologique (01_CADRE_METHODOLOGIQUE), soumise a
validation ; elle rend explicite un protocole reste implicite -
reconstitue par retro-ingenierie de l'historique Git du depot.
elle complete le Workflow_GitHub_v0_2 (branches) sans le remplacer :
v0.2 organise les chantiers, la presente fiche fixe le format des
commits et la discipline de mise a jour de l'arborescence.
```

### 1. Ce que l'historique revele

```text
convention des commits, observee sur main (40 commits anterieurs a
la session de juillet 2026) :
- prefixe unique : "docs:" ;
- verbe a l'imperatif, en anglais, une ligne ;
- un changement logique par commit (une fiche, une synthese, un lot);
- historique lineaire sur main ; branches reservees au travail
  d'agent (agent/reprise-cycle-cosmologique).
exemples : "docs: add first thesis statement", "docs: recenter
theoretical matrix on constants", "docs: open architecture circle
two".
```

### 2. Le protocole de commit et de push (a adopter)

```text
1. format : docs: <imperatif anglais, une ligne> ;
2. granularite : un cycle de travail coherent par commit, sauf besoin de
   sauvegarde ;
3. contenu : le message dit ce que le commit fait, non comment ;
4. les commits de contenu et les commits de synchronisation suivent
   le meme format.
5. push distant seulement aux jalons substantiels ou sur demande explicite.
note de session : les commits de juillet 2026 ont employe des
prefixes francais (philo:, methodo:, plan:) - ecart assume et
non retroactif ; l'alignement sur "docs:" vaut a partir de la
presente fiche.
```

Distinction active :

```text
commit local = sauvegarde fine et lisibilite du travail ;
push GitHub = publication d'un jalon, d'une branche partagee ou d'un etat a
securiser avant pause.
```

La granularite fine reste possible dans les commits locaux, mais elle n'est
plus automatique.

La granularite des pushs devient plus large.

Regle de rythme :

```text
1. ne pas ajouter une section Git a chaque reponse ;
2. attendre la fin d'un lot coherent lorsque plusieurs documents doivent etre
   modifies ensemble ;
3. mentionner Git seulement si une action Git a ete faite, si une decision de
   versionnage est requise, ou si l'etat du depot affecte la suite ;
4. preferer amender un commit local non pousse lorsque la correction appartient
   au meme changement logique.
```

Regle de regroupement economique :

```text
si le geste de commit est deja necessaire, regarder les autres modifications
pretes avant de le faire ;
committer ensemble ce qui appartient au meme cycle coherent ;
ne pas laisser en attente un changement pret seulement pour creer un commit
ulterieur ;
ne jamais inclure un changement non relu, ambigu, externe ou non lie au cycle.
```

### 3. Le modele de branches (rappel v0.2)

```text
main : etat valide, recoit des merges, jamais de travail direct.
branches thematiques ephemeres : une par chantier, trois vivantes
au maximum, mergees dans main a la validation puis supprimees.
travail : branche d'integration, union des chantiers ouverts, etat
quotidien du dossier.
regle des fichiers partages : README, index et cartes se modifient
sur une seule branche a la fois - un chantier "arborescence" dedie
lorsqu'ils doivent bouger ensemble.
```

### 4. Discipline de mise a jour de l'arborescence

Reprise des regles de l'index raisonne (section 16), appliquees a
toute mise a jour de navigation :

```text
avant de produire ou mettre a jour une synthese ou un index :
1. dire quels documents elle integre ;
2. dire quel rang elle stabilise ;
3. dire quels documents elle prolonge ou remplace ;
4. dire quelles limites elle conserve.
avant de deplacer ou renommer un fichier :
1. inventorier les references internes ;
2. distinguer actifs et archives ;
3. creer une table de correspondance ;
4. ne rien deplacer sans raison documentaire explicite.
regle de rang : un document recent corrige le rang, le vocabulaire
ou la fonction d'un ancien, il ne l'efface pas.
```

### 5. Procedure de mise a jour additive (economie)

```text
plutot que reecrire un index long, on produit un supplement additif
qui pointe vers les nouveaux documents et corrige les rangs, en
renvoyant a l'index precedent pour le reste. L'index precedent
reste la couche stable ; le supplement est la couche recente.
c'est la methode retenue pour la mise a jour de juillet 2026 :
Index_supplement_pan_philosophique_v0_1.md complete
Index_raisonne_du_corpus_v1_0.md sans le reecrire.
```

### 6. Controle proportionne

Les controles suivent maintenant une regle de proportion.

```text
1. controle courant : git status, revue du diff, git diff --check ;
2. controle cible : rg sur les termes sensibles lorsqu'ils sont en jeu ;
3. controle lourd : avant jalon, publication, fusion de branche, ou demande
   explicite.
```

Le balayage ASCII general n'est pas une exigence courante du corpus.

Il reste utile seulement pour :

```text
code ;
export technique ;
document deja strictement ASCII ;
preparation de publication ;
controle demande explicitement.
```

### 7. Formule de cloture

```text
Le protocole existait dans les gestes ; il manquait a l'ecrit. Un
depot se lit aussi dans son histoire : commits sobres, cycles coherents,
pushs aux jalons, arborescence mise a jour par couches, jamais reecrite
d'un bloc.
```
