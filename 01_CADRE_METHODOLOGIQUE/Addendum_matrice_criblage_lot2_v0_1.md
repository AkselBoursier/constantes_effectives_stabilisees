# Addendum a la matrice de criblage - lot 2 v0.1

## Couche decisionnelle issue des cinq critiques supplementaires

### 0. Statut documentaire

```text
statut : addendum actif ;
document complete : 01_CADRE_METHODOLOGIQUE/Matrice_criblage_taxonomique_v0_1.md ;
source : 01_CADRE_METHODOLOGIQUE/Fiche_criblage_critiques_lot2_v0_1.md ;
fonction : transformer la prudence methodologique en seuils de decision.
```

Cet addendum ne cree pas une nouvelle taxonomie.

Il ajoute une couche de sortie.

Formule directrice :

```text
la classification ne doit pas ouvrir la fiche ;
elle doit sortir du criblage.
```

### 1. Decision integree depuis le lot 2

Les cinq critiques supplementaires convergent vers un point simple :

```text
une methode prudente ne suffit pas si elle ne dit jamais quand conclure,
quand tester, quand differer et quand refuser.
```

La matrice v0.1 conserve donc son ordre :

```text
forme -> fonction -> role -> acces -> architecture -> trajectoire.
```

L'addendum ajoute le passage suivant avant la decision finale :

```text
diagnostic -> verrou -> test eventuel -> sortie taxonomique.
```

### 2. Sortie taxonomique en fin de fiche

Une fiche ne doit annoncer une famille fonctionnelle qu'apres avoir documente :

| Point controle | Question minimale |
|---|---|
| Forme stabilisee | Quelle forme est stabilisee avant le classement ? |
| Regime physique | Dans quel domaine la grandeur opere-t-elle ? |
| Regime d'acces | Par quelle route la grandeur devient-elle connue ? |
| Role contextuel | Quel role local ou architectural prend-elle ? |
| Architecture | Un reseau de dependances est-il requis ? |
| Temporalite | Le statut se constitue-t-il, se reconstruit-il ou se tend-il dans le temps ? |

La sortie taxonomique vient ensuite.

Elle peut etre :

```text
classement confirme ;
classement confirme avec role contextuel explicite ;
classement conserve sous audit ;
classement deplace vers rang 0 ;
classement deplace vers role contextuel ;
classement deplace vers architecture ;
classement differe par tension ou degenerescence ;
classement refuse.
```

### 3. Champs decisionnels a ajouter aux cas litigieux

| Champ | Question | Effet |
|---|---|---|
| Sortie taxonomique | Quelle classification reste apres les rangs de criblage ? | Met le classement en conclusion |
| Contrainte transversale active | Une borne, validite ou limite prime-t-elle localement sur la fonction ? | Evite de forcer une famille |
| Couplage fort regime-acces | Le mode d'acces participe-t-il a la definition effective de la grandeur ? | Oblige a qualifier l'acces |
| Degre de tension | S'agit-il d'une divergence locale, d'une tension persistante ou d'un point de bascule ? | Oriente vers simple note, stress test ou dossier autonome |
| Test de degradation | Que devient le regime quand le seuil, l'echelle ou le noeud varie ? | Observe la dissolution progressive |
| Test de substitution | Quelle alternative controlee remplace le noeud ou le modele teste ? | Compare la robustesse du reseau |
| Verrou d'options | Quelles interpretations deviennent incompatibles apres le diagnostic ? | Empeche les sorties simultanees faibles |
| Temporalite scindee | Faut-il separer constitution physique et acces epistemique ? | Prepare la matrice temporelle v0.2 |

### 4. Verrous d'options

Un verrou n'est pas une interdiction abstraite.

Il enregistre une incompatibilite locale.

Exemples de verrous :

| Diagnostic | Verrou |
|---|---|
| Couplage fort regime-acces sans controle inter-acces | Pas de classement robuste sans qualifier la route d'acces |
| Contrainte transversale dominante | Ne pas reduire la grandeur a une fonction locale simple |
| Architecture requise pour comprendre la grandeur | Ne pas conclure avant test de dependance |
| Tension persistante entre routes d'acces | Ne pas transformer la tension en anomalie sans passerelle d'escalade |
| Degenerescence cosmologique active | Ne pas isoler une constante hors du reseau modele-donnees |
| Temporalite physique et temporalite d'acces divergentes | Scinder constitution et reconstruction avant decision |

### 5. Test de retrait elargi

Le test de retrait reste valide.

Il est complete par deux epreuves :

```text
test de degradation ;
test de substitution.
```

Usage :

| Epreuve | Question | Sortie utile |
|---|---|---|
| Retrait | Que perd-on si la grandeur disparait ? | Fonction locale, articulation, domaine ou architecture |
| Degradation | Comment le regime se dissout-il si le seuil ou l'echelle varie ? | Sensibilite progressive |
| Substitution | Que devient le reseau avec une alternative controlee ? | Robustesse ou dependance au modele |

### 6. Bloc additif pour les futures fiches

A ajouter apres le rang 5 lorsque le cas est litigieux :

```text
Contrainte transversale active :
Couplage fort regime-acces :
Degre de tension :
Test de degradation :
Test de substitution :
Verrous d'options :

Sortie taxonomique proposee :
Decision de classement :
Reserve conservee :
```

Tous les champs ne doivent pas etre remplis artificiellement.

Ils deviennent obligatoires seulement lorsque le cas presente :

```text
une tension persistante ;
une reconstruction modele-dependante ;
une contrainte transversale ;
une architecture active ;
ou un risque de classement premature.
```

### 7. Articulation avec les prochaines etapes

Cet addendum appelle trois suites, dans cet ordre :

```text
1. matrice temporelle v0.2 scindant constitution physique et acces epistemique ;
2. passerelle d'escalade des tensions cosmologiques ;
3. cas traversant pour verifier que la couche decisionnelle produit mieux
   qu'une simple liste de reserves.
```

La carte consolidee ne doit etre modifiee qu'apres ces controles.

Etat du premier point :

```text
01_CADRE_METHODOLOGIQUE/Matrice_temporelle_v0_2.md
```

Etat du deuxieme point :

```text
01_CADRE_METHODOLOGIQUE/Passerelle_escalade_tensions_cosmologiques_v0_1.md
```

Etat du troisieme point :

```text
03_TESTS_TAXONOMIQUES/Test_traversant_H0_passerelle_tensions_v0_1.md
```

### 8. Formule de cloture

```text
Le criblage ne gagne pas en rigueur en retardant indefiniment la decision.
Il gagne en rigueur lorsque la decision devient la sortie explicite d'un
diagnostic documente.
```
