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

### 2. Le protocole de commit (a adopter)

```text
1. format : docs: <imperatif anglais, une ligne> ;
2. granularite : un changement logique par commit ;
3. contenu : le message dit ce que le commit fait, non comment ;
4. les commits de contenu et les commits de synchronisation suivent
   le meme format.
note de session : les commits de juillet 2026 ont employe des
prefixes francais (philo:, methodo:, plan:) - ecart assume et
non retroactif ; l'alignement sur "docs:" vaut a partir de la
presente fiche.
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

### 6. Formule de cloture

```text
Le protocole existait dans les gestes ; il manquait a l'ecrit. Un
depot se lit aussi dans son histoire : commits courts, un changement
a la fois, l'arborescence mise a jour par couches, jamais reecrite
d'un bloc.
```
