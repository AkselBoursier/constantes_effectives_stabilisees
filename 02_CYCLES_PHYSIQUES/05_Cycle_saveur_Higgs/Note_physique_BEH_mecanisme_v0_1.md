# Note physique BEH - mecanisme v0.1

## Brout-Englert-Higgs comme seuil physique du regime electrofaible brise

### 0. Statut documentaire

```text
statut : note physique preparatoire ;
position : amont du cycle Saveur-Higgs, preparation du cycle du
seuil electrofaible ;
fonction : decrire le mecanisme BEH, ses grandeurs et ses acces ;
registre : froid, descriptif, verifiable sur sources ;
statut probatoire : P2/P3 interne, a controler sur primaires avant publication.
```

Cette note donne au cadrage BEH son support physique minimal.

Elle decrit le mecanisme par lequel le secteur electrofaible du
Modele standard se lit, a basse energie, comme un regime avec :

```text
une echelle `v` ;
des bosons faibles massifs ;
un photon sans masse ;
un boson de Higgs scalaire ;
des masses fermioniques lisibles via les Yukawa ;
un acces experimental par `G_F`, masses faibles, Higgs et fits
electrofaibles.
```

Elle garde le rang d'une note de mecanisme.

Le cycle du seuil electrofaible s'ouvre ensuite avec un objet plus
precis :

```text
`v`, regime d'echelle, masses faibles, potentiel de Higgs,
ou seuil electroweak comme architecture d'entree.
```

### 1. Point de depart physique

Le Modele standard organise le secteur electrofaible par la symetrie :

```text
SU(2)_L x U(1)_Y
```

Le mecanisme BEH rend lisible le regime basse energie par la reduction
effective vers :

```text
U(1)_em
```

La lecture physique active pour le corpus est la suivante :

```text
un champ scalaire de Higgs porte un etat fondamental structure ;
cet etat introduit une echelle `v` ;
les champs de jauge faibles se recombinent en `W+`, `W-`, `Z` et photon ;
les masses faibles et les masses fermioniques deviennent lisibles ;
le photon conserve le role du champ de jauge electromagnetique.
```

Cette sequence place BEH avant l'architecture Saveur-Higgs :

```text
BEH -> regime electrofaible brise -> `v`
-> Yukawa -> matrices de masse -> diagonalisation
-> spectres et orientations.
```

### 2. Champ de Higgs et potentiel minimal

Dans le Modele standard minimal, le champ de Higgs est un doublet
complexe :

```text
Phi
```

Le potentiel scalaire s'ecrit usuellement, selon les conventions :

```text
V(Phi) = - mu^2 Phi^\dagger Phi
       + lambda (Phi^\dagger Phi)^2
```

avec :

```text
mu^2 > 0 ;
lambda > 0.
```

Cette forme donne un etat fondamental a valeur non nulle du champ.

En jauge unitaire, la fluctuation physique autour de cet etat se lit :

```text
Phi(x) = 1/sqrt(2) * (0, v + h(x))^T
```

ou :

```text
`v` : echelle du fond electroweak ;
`h(x)` : excitation scalaire physique, associee au boson de Higgs.
```

Au niveau arbre, les relations usuelles donnent :

```text
v^2 = mu^2 / lambda
m_h^2 = 2 lambda v^2
```

Lecture pour le corpus :

```text
le potentiel fournit une structure de stabilisation autour de
laquelle le regime electrofaible brise devient formulable.
```

### 3. Masses faibles

Le terme cinetique covariant du champ de Higgs contient :

```text
(D_mu Phi)^\dagger (D^mu Phi)
```

Quand `Phi` est developpe autour de son etat fondamental, ce terme
produit les masses des bosons faibles.

Au niveau arbre :

```text
M_W = g v / 2
M_Z = sqrt(g^2 + g'^2) v / 2
M_gamma = 0
```

Les couplages de jauge sont :

```text
g   : couplage de SU(2)_L ;
g'  : couplage de U(1)_Y.
```

La combinaison electromagnetique reste sans masse.

La combinaison neutre orthogonale devient le boson `Z`.

Lecture pour le corpus :

```text
`v` joue ici le role d'echelle commune ;
les couplages de jauge distribuent cette echelle vers les masses
faibles ;
le photon fixe le residu electromagnetique du regime.
```

### 4. Relation avec `G_F`

Le regime d'acces principal de `v` passe par la constante de Fermi.

Au niveau arbre :

```text
G_F / sqrt(2) = g^2 / (8 M_W^2)
              = 1 / (2 v^2)
```

d'ou :

```text
v = (sqrt(2) G_F)^(-1/2)
```

Cette relation donne a `v` un statut charniere :

```text
grandeur du regime electroweak ;
grandeur reconstruite par phenomenologie basse energie ;
point d'entree des masses faibles et des masses fermioniques.
```

Lecture pour le corpus :

```text
`v` cumule une fonction theorique de valeur de fond et une route
d'acces phenomenologique robuste.
```

### 5. Masses fermioniques et Yukawa

Le mecanisme BEH devient l'amont de Saveur-Higgs quand il rencontre
les couplages de Yukawa.

Pour un fermion charge, la relation diagonale usuelle est :

```text
m_f = y_f v / sqrt(2)
```

Dans l'ecriture matricielle :

```text
M_f = Y_f v / sqrt(2)
```

La diagonalisation des matrices `M_f` donne :

```text
spectres de masses ;
bases physiques ;
orientations CKM et PMNS selon les secteurs et les extensions.
```

Lecture pour le corpus :

```text
BEH fournit l'echelle commune ;
les Yukawa fournissent les textures de differenciation ;
la diagonalisation rend les spectres et les orientations lisibles.
```

La note Saveur-Higgs commence donc juste apres ce seuil :

```text
`v` disponible -> textures `Y_f` -> masses et orientations.
```

### 6. Boson de Higgs

Le champ scalaire laisse une excitation physique :

```text
h(x)
```

Cette excitation correspond au boson de Higgs.

Son role dans la note presente est double :

```text
1. trace physique du secteur scalaire ;
2. acces experimental aux couplages du mecanisme.
```

Les acces experimentaux passent notamment par :

```text
production du Higgs ;
desintegrations du Higgs ;
couplages aux bosons faibles ;
couplages aux fermions ;
masse du Higgs ;
contraintes sur l'auto-couplage.
```

Lecture pour le corpus :

```text
le Higgs observable donne un acces au secteur qui stabilise `v`,
mais `v`, `m_h`, `lambda` et les Yukawa portent des fonctions
distinctes dans le reseau.
```

### 7. Regimes a distinguer

La note de cadrage BEH imposait une separation entre regime physique,
regime d'acces et regime de description.

La note physique la precise ainsi :

| Regime | Fonction | Objets principaux |
|---|---|---|
| Regime physique | etat electroweak a basse energie | `v`, masses faibles, Higgs, masses fermioniques |
| Regime d'acces | mesures et reconstructions | `G_F`, `M_W`, `M_Z`, `m_h`, couplages Higgs, fits |
| Regime de description | formulation perturbative et choix de jauge | jauge unitaire, jauges renormalisables, formulations gauge-invariant |
| Regime cosmologique | histoire thermique du changement electroweak | crossover, temperature caracteristique, plasma primordial |

Le regime cosmologique reste ici en reserve.

Il deviendra pertinent si le cycle du seuil rejoint la jonction
d'historicite cosmique.

### 8. Prudence de jauge

Le vocabulaire courant parle de brisure spontanee de la symetrie
electrofaible.

Dans les theories de jauge, cette formule porte une dette de
description.

Pour le corpus, la formulation operatoire est :

```text
la description en jauge fixee rend visible une valeur de fond `v`
et des termes de masse ;
les enonces physiques robustes portent sur les masses, les
couplages, les etats accessibles et les observables ;
le debat jauge / invariant sert de controle de formulation.
```

Le point methodologique est simple :

```text
la brisure sert de nom de seuil ;
le travail de qualification porte sur les objets stabilises par ce
seuil.
```

### 9. Carte des grandeurs

| Grandeur | Fonction physique | Regime d'acces | Fonction dans le corpus |
|---|---|---|---|
| `v` | echelle du regime electroweak brise | `G_F`, masses faibles, fits | candidat principal de constance de regime |
| `mu^2` | parametre quadratique du potentiel | reconstruit dans le cadre du modele | condition du profil scalaire |
| `lambda` | auto-couplage scalaire | masse du Higgs, auto-couplage, fits | lien avec le chantier scalaire et stabilite du vide |
| `m_h` | masse du boson de Higgs | collisions, canaux Higgs | acces au secteur scalaire |
| `g`, `g'` | couplages de jauge | electroweak precision, fits | distribution de `v` vers `W`, `Z`, photon |
| `M_W`, `M_Z` | masses faibles | mesures directes et fits | valeurs de regime issues de `v` |
| `y_f`, `Y_f` | couplages de Yukawa | masses, couplages Higgs | differenciation fermionique |
| `m_f`, `M_f` | masses fermioniques | mesures, reconstructions, schemas | spectres apres BEH et diagonalisation |

Cette carte donne au cycle du seuil plusieurs objets possibles.

Elle favorise provisoirement la lecture suivante :

```text
BEH stabilise un seuil de regime ;
`v` en est le noeud d'echelle ;
les masses faibles et fermioniques en sont les effets lisibles ;
le potentiel et le Higgs ouvrent le chantier du secteur scalaire.
```

### 10. Conditions de qualification du cycle du seuil

La note physique BEH rend possible le cycle du seuil avec trois
options structurantes.

| Option | Objet du cycle | Gain | Dette |
|---|---|---|---|
| A | `v` comme constance de regime | continuite avec Saveur-Higgs | controle jauge / invariant requis |
| B | seuil electroweak comme architecture d'entree | relie mecanisme, acces et temporalite | objet plus large, a tenir froidement |
| C | masses faibles comme effets stabilises | acces experimental direct | discipline d'ordre entre effet et seuil |

Decision de travail :

```text
seuil electroweak comme architecture d'entree est l'option la plus
englobante pour la prochaine ouverture ;
`v` comme constance de regime fournit le noyau de qualification ;
masses faibles comme effets stabilises reste un controle
phenomenologique.
```

### 11. Relation avec le chantier scalaire

La note distingue le seuil BEH du dossier Higgs proprement dit.

Le chantier du secteur scalaire de Higgs pourra porter sur :

```text
masse du Higgs ;
potentiel scalaire ;
auto-couplage `lambda` ;
stabilite du vide ;
hierarchie ou naturalite, si le corpus decide d'ouvrir ce niveau.
```

Le chantier scalaire enrichit le secteur scalaire.

Le cycle du seuil qualifie d'abord le seuil par lequel le regime
electrofaible brise devient disponible pour Saveur-Higgs.

### 12. Formules prudentes

Formules utilisables dans les prochaines pieces :

```text
BEH installe le seuil physique a partir duquel l'echelle `v`,
les masses faibles et les masses fermioniques deviennent lisibles
dans le regime electrofaible brise.

`v` fonctionne comme noeud d'echelle du regime electroweak ; son
statut de constance depend a la fois de sa fonction theorique et de
ses routes d'acces phenomenologiques.

La brisure nomme le seuil ; la qualification porte sur les objets
qui deviennent stabilises a ce seuil.
```

Formules reservees a une verification primaire :

| Formule forte | Verification requise |
|---|---|
| statut exact de la brisure de jauge | sources FMS, Elitzur, Struyve, Strocchi, physique de jauge |
| valeur numerique de `v`, `M_W`, `M_Z`, `m_h` | PDG / CODATA / publications experimentales |
| statut cosmologique du crossover electroweak | litterature reseau et cosmologie thermique |
| stabilite du vide | calculs RG, masse du top, `m_h`, `alpha_s`, sources specialisees |

### 13. Conclusion operative

```text
BEH donne au corpus un seuil physique precis :
le passage vers un regime ou une echelle `v`, des masses faibles,
des masses fermioniques et un Higgs observable forment un reseau
stabilise.
```

Le cycle du seuil electrofaible est ouvert par :

```text
02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/Cycle_CP1_seuil_electrofaible_v0_1.md
```
