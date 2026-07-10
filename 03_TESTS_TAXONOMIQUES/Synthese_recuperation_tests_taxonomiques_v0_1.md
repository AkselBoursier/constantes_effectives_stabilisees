# Synthese de recuperation des tests taxonomiques v0.1

## Seuil, Fond, liaison stabilisee et familles fragiles

### 1. Fonction

Cette note accompagne l'ouverture du lot 2 de remontee DOCX.

Elle ne remplace pas les extractions.

Elle sert a transformer les tests historiques en instruments actifs :

```text
diagnostics de fragilite ;
tests de passage vers une famille fonctionnelle ;
tests de retrogradation vers role contextuel ;
tests de rattachement a une architecture ;
tests de non-proliferation lexicale.
```

### 2. Extractions produites

| Source DOCX | Markdown de travail |
|---|---|
| `Test des familles fragiles.docx` | `03_TESTS_TAXONOMIQUES/Source_docx_Test_familles_fragiles_v0_1.md` |
| `Test de la famille Seuil.docx` | `03_TESTS_TAXONOMIQUES/Source_docx_Test_famille_Seuil_v0_1.md` |
| `Test de la famille Fond.docx` | `03_TESTS_TAXONOMIQUES/Source_docx_Test_famille_Fond_v0_1.md` |
| `Test de la famille Relation v0.1.docx` | `03_TESTS_TAXONOMIQUES/Source_docx_Test_famille_Relation_v0_1.md` |

Statut :

```text
extractions textuelles de travail,
non substitutives aux DOCX originaux,
produites pour comparaison et integration.
```

### 3. Resultat general

Les tests taxonomiques confirment la trajectoire actuelle.

Ils ne demandent pas de restaurer les anciennes familles.

Ils montrent plutot pourquoi la methode devait passer :

```text
du nom de famille vers la fonction directrice ;
de la fonction trop large vers le role contextuel ;
de la case fragile vers le test de non-reduction ;
du classement local vers l'architecture ;
du verdict nominal vers une matrice de passage.
```

Decision de recuperation :

```text
les tests sont conserves comme sources primaires,
mais leurs conclusions anciennes ne deviennent actives
que si elles passent la methode v1.3.
```

### 4. Test des familles fragiles

Le test initial posait une bonne question :

```text
une famille classe-t-elle plusieurs cas heterogenes,
ou nomme-t-elle seulement une difficulte locale ?
```

Cette question devient un test actif.

Une fonction directrice peut devenir famille fonctionnelle seulement si :

```text
1. elle classe plusieurs cas heterogenes ;
2. elle conserve une fonction principale claire ;
3. elle ne se reduit pas a une forme logique du rang 0 ;
4. elle ne se decrit pas mieux comme role contextuel ;
5. elle ne designe pas seulement une architecture locale.
```

Recuperation positive :

```text
famille fragile = hypothese de classement a tester,
non case acquise.
```

### 5. Recuperation de Seuil

Le test de Seuil tranche fortement.

Il montre que :

```text
M_W est d'abord une echelle electrofaible,
avec fonction de seuil de validite pour la theorie de Fermi ;
Lambda_QCD est d'abord une echelle dynamique,
avec fonction de seuil perturbatif / non perturbatif ;
la masse absolue des neutrinos est d'abord un ancrage spectral,
avec fonction de borne ou de seuil selon l'acces.
```

Decision active :

```text
Seuil ne doit pas etre une famille fonctionnelle.
```

Reformulation positive :

```text
seuil = role contextuel de borne, ancrage, passage ou limite de validite.
```

Usage autorise :

```text
fonction seuil d'une echelle ;
fonction seuil d'une liaison spectrale ;
fonction seuil d'un raccordement ;
borne d'acces experimental ou observationnel.
```

Interdit :

```text
classer une grandeur comme Seuil
avant d'avoir determine sa forme logique, sa fonction directrice,
son regime physique et son regime d'acces.
```

### 6. Recuperation de Fond

Le test de Fond tranche aussi.

Il montre que :

```text
Lambda peut jouer un role de terme de fond ;
H_0 fixe un taux d'expansion actuel ;
Omega_i sont des densites normalisees ;
w est une relation d'etat ;
A_s et n_s relevent des conditions initiales ou du secteur primordial ;
sigma_8 et S_8 relevent de reconstructions de croissance.
```

Ces objets appartiennent a une architecture cosmologique.

Ils ne confirment pas Fond comme famille autonome.

Decision active :

```text
Fond ne doit pas etre une famille fonctionnelle.
```

Reformulation positive :

```text
fond = role architectural dans une architecture cosmologique,
notamment quand une grandeur structure le cadre global dans lequel
d'autres processus deviennent lisibles.
```

Consequence :

```text
la cosmologie ne doit pas etre rangee dans une case Fond ;
elle doit etre lue comme reseau de dependances, d'acces et de modeles.
```

### 7. Recuperation de Relation comme liaison stabilisee

Le test de Relation est plus delicat.

La source historique conclut que Relation doit survivre comme famille
qualifiee.

La methode v1.3 a depuis durci cette conclusion.

Decision active :

```text
ne pas restaurer Relation comme famille par defaut.
```

Ce qu'il faut recuperer :

```text
les types de liaison stabilisee ;
les frontieres avec echelle, raccordement, convention et orientation ;
la matrice qui empeche le fourre-tout.
```

Les formes utiles deviennent :

| Forme recuperee | Statut v1.3 |
|---|---|
| Liaison stratifiee | A tester : fonction directrice ou role contextuel |
| Composition exacte | Rang 0 composition + convention ou composition |
| Ecart spectral | Rang 0 ecart + fonction physique locale |
| Liaison constitutive | Souvent architecture constitutive, par exemple Saveur-Higgs |
| Densite normalisee | Rapport normalise dans architecture cosmologique |
| Equation d'etat | Rang 0 loi de comportement + role cosmologique |

Test de non-reduction :

```text
une liaison stabilisee ne peut devenir sortie taxonomique faible
que si la liaison est l'objet principal,
qu'elle ne se reduit pas a une forme logique,
et qu'elle n'est pas mieux decrite comme role contextuel ou architecture.
```

Formulation positive :

```text
liaison stabilisee = objet d'analyse qualifie,
jamais etiquette suffisante.
```

### 8. Matrice active issue des tests

Pour toute ancienne famille fragile, appliquer cette matrice.

| Question | Effet |
|---|---|
| Quelle forme logique est stabilisee ? | Evite de classer trop tot |
| Quelle fonction directrice est principale ? | Identifie ce que la grandeur fait |
| La fonction vaut-elle pour plusieurs cas heterogenes ? | Test de famille possible |
| Le role est-il seulement local ou transversal ? | Retrogradation en role contextuel |
| Le role depend-il d'un reseau de grandeurs ? | Rattachement a une architecture |
| L'acces produit-il la fragilite ? | Rattachement au regime d'acces |
| La tension est-elle temporelle ? | Rattachement a la trajectoire de stabilisation |

### 9. Table de decisions recuperees

| Terme historique | Recuperation active | Interdit |
|---|---|---|
| Seuil | Role contextuel : borne, passage, ancrage, limite de validite | Famille fonctionnelle autonome |
| Fond | Role architectural cosmologique | Famille englobant la cosmologie |
| Relation | Liaison stabilisee qualifiee, sous test de non-reduction | Case par defaut pour tout rapport |
| Famille fragile | Hypothese de classement | Statut acquis sans test |

### 10. Consequence pour les architectures

Les tests taxonomiques imposent un garde-fou avant le cercle 2.

Chaque architecture devra verifier :

```text
1. qu'elle n'est pas une ancienne famille agrandie ;
2. qu'elle articule plusieurs fonctions solidaires ;
3. qu'elle explicite les roles contextuels ;
4. qu'elle distingue regime physique et regime d'acces ;
5. qu'elle ne transforme pas une tension locale en categorie ;
6. qu'elle expose sa trajectoire de stabilisation.
```

### 11. Prochaine etape logique

Le lot 2 etant ouvert, la prochaine etape devient :

```text
ouvrir le lot 3 des sources d'architecture,
extraire les sources Saveur-Higgs et effectives basse energie,
puis seulement ensuite ouvrir le cercle 2 des architectures actives.
```

### 12. Formule de cloture

```text
Les tests taxonomiques ne restaurent pas les anciennes familles ;
ils fournissent les epreuves qui expliquent pourquoi certaines distinctions
deviennent fonctions directrices, roles contextuels, formes logiques
ou architectures.
```
