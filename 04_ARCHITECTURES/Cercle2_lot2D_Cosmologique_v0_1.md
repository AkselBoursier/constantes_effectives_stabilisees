# Cercle 2 lot 2D - Cosmologique v0.1

## Reprise positive prudente de l'architecture inferentielle et reconstructive

### 1. Fonction

Cette note produit le lot 2D du cercle 2.

Elle reprend l'architecture cosmologique par formulations positives prudentes,
a partir des appuis suivants :

```text
04_ARCHITECTURES/Cercle2_architectures_actives_v0_1.md
04_ARCHITECTURES/Architecture_cosmologique_notes.md
04_ARCHITECTURES/Architecture_cosmologique_stress_test_v0_1.md
02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Synthese_cycle_cosmologique_v0_1.md
02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Plan_reprise_cycle_cosmologique_v0_1.md
```

Le but n'est pas de refaire le cycle cosmologique.

Le but est de stabiliser une version positive du noyau architectural :

```text
modele cosmologique global
+ fonctions de fond, d'etat, de normalisation, de condition initiale
+ observables reconstruites
+ sous-reseaux fonctionnels
+ regimes d'acces
+ dependances de modele
+ tensions transversales
+ limites conservees.
```

### 2. Formulation positive d'ouverture

Formulation directrice :

```text
L'architecture cosmologique rend operatoire un modele d'univers en articulant
des roles de fond, d'etat, de normalisation, de condition initiale et de
reconstruction, toujours avec leurs regimes d'acces, leurs dependances de
modele et leurs tensions eventuelles.
```

Cette formulation place d'abord ce que le reseau fait.

Elle evite de reduire la cosmologie a une liste de parametres, a une classe
autonome ou a une collection de tensions.

### 3. Matrice regime / solidarite / acces / trajectoire

| Champ | Lecture cosmologique |
|---|---|
| Regime | Modele cosmologique global, avec sous-reseaux de fond, expansion, budget, etat, primordial et croissance |
| Solidarite | Fonctions architecturales, inference de modele, observables, acces heterogenes et comparaisons de donnees |
| Noeuds | `Lambda`, `H_0`, `Omega_i`, `w`, `A_s`, `n_s`, `sigma_8`, `S_8` |
| Acces | CMB, BAO, supernovae, echelle locale des distances, lentillage faible, amas, 3x2pt, calibrations |
| Trajectoire | Modele -> inference -> reconstruction -> comparaison des acces -> convergences et tensions |
| Limites | Nature de l'energie noire, origine de `Lambda`, tensions `H_0` et `S_8`, microphysique inflationnaire, validite ultime de LambdaCDM |

Formule :

```text
la stabilisation cosmologique est une inference reconstructive situee,
pas une lecture directe d'une constante isolee.
```

### 4. Sous-reseaux positifs

Le stress test confirme une macro-architecture active, lisible par
sous-reseaux fonctionnels.

Ces sous-reseaux ne sont pas des architectures autonomes confirmees.

Ils servent a distribuer les roles internes sans perdre l'unite du modele.

#### 4.1 Fond et expansion

Cas :

```text
Lambda / H_0
```

Lecture positive :

```text
Lambda stabilise un terme de fond du modele ;
H_0 stabilise l'etat actuel du taux d'expansion.
```

Forme :

```text
fond cosmologique
+ etat d'expansion actuel
+ acces par routes cosmologiques et locales
+ comparaison des determinations.
```

#### 4.2 Budget normalise

Cas :

```text
Omega_i
```

Lecture positive :

```text
les Omega_i organisent le budget relatif du modele en rapportant chaque
composante a la densite critique.
```

Forme :

```text
densites physiques
-> normalisation par rho_crit
-> budget relatif
-> dependance au modele d'arriere-plan.
```

#### 4.3 Etat de composante

Cas :

```text
w
```

Lecture positive :

```text
w decrit une relation d'etat phenomenologique entre pression et densite.
```

Forme :

```text
composante cosmologique
+ relation d'etat
+ test de l'ecart a Lambda
+ prudence sur l'interpretation microphysique.
```

#### 4.4 Primordial

Cas :

```text
A_s / n_s
```

Lecture positive :

```text
A_s et n_s stabilisent l'entree primordiale du modele, telle qu'elle est
inferee par les signatures statistiques des fluctuations.
```

Forme :

```text
conditions initiales statistiques
+ spectre primordial
+ acces CMB et grandes structures
+ limite sur le modele inflationnaire sous-jacent.
```

#### 4.5 Croissance et reconstruction

Cas :

```text
sigma_8 / S_8
```

Lecture positive :

```text
sigma_8 et S_8 stabilisent des reconstructions tardives de l'amplitude de
croissance, selon des routes d'acces et des hypotheses de modele.
```

Forme :

```text
conditions initiales
-> evolution gravitationnelle
-> croissance des structures
-> observable reconstruite
-> comparaison des acces.
```

#### 4.6 Tensions transversales

Les tensions sont des proprietes transversales du reseau.

Elles qualifient la compatibilite entre acces, modeles et calibrations.

Elles ne constituent pas un sous-reseau autonome.

### 5. Noeuds et fonctions locales

| Noeud | Fonction positive | Acces ou manifestation |
|---|---|---|
| `Lambda` | Terme de fond du modele cosmologique | Dynamique d'expansion, fits LambdaCDM |
| `H_0` | Parametre d'etat actuel du taux d'expansion | CMB-inference, echelle locale des distances, BAO, supernovae |
| `Omega_i` | Budget normalise des composantes | CMB, BAO, supernovae, modele de fond |
| `w` | Relation d'etat phenomenologique | Contraintes energie noire, extensions de LambdaCDM |
| `A_s` | Amplitude statistique primordiale | CMB, grandes structures apres evolution |
| `n_s` | Inclinaison du spectre primordial | CMB, tests de forme spectrale |
| `sigma_8` | Amplitude reconstruite de croissance tardive | Lensing, amas, grandes structures |
| `S_8` | Combinaison reconstruite adaptee aux degenerescences | Lensing faible, 3x2pt, comparaisons de croissance |
| Tensions | Diagnostic transversal d'acces et de modele | Tensions `H_0`, `S_8`, dependances aux calibrations |

### 6. Acces et robustesse

L'architecture cosmologique possede un acces fortement reconstructif.

Sa robustesse ne vient pas d'une observation directe unique.

Elle vient de la capacite du reseau a faire converger des routes d'inference
heterogenes, tout en rendant visibles les zones de tension.

| Domaine | Robustesse | Prudence |
|---|---|---|
| Fond et expansion | Forte dans LambdaCDM et ses tests proches | Tension `H_0`, dependance aux calibrations et au modele |
| Budget normalise | Forte comme decomposition interne du modele | Depend du choix de modele et de `rho_crit` |
| Etat de composante | Utile pour tester l'energie noire | Relation phenomenologique, microphysique non fixee |
| Primordial | Fortement contraint par le CMB | Ne selectionne pas seul une theorie inflationnaire unique |
| Croissance reconstruite | Informative et multi-acces | Degenerescences, systematiques et tension `S_8` |
| Tensions | Diagnostic methodologique central | Ne sont ni un verdict immediat ni une nouvelle classe de grandeurs |

Regle de reprise :

```text
aucune grandeur cosmologique ne doit etre presentee sans son modele,
son sous-reseau fonctionnel, son regime d'acces et sa limite conservee.
```

### 7. Formulations a eviter

Le lot 2D recommande de remplacer les formulations defensives par les
formulations positives suivantes.

| Formulation a eviter | Formulation positive |
|---|---|
| `La cosmologie n'est pas une famille` | `La cosmologie solidarise des fonctions architecturales dans un modele et des regimes d'acces` |
| `H_0 n'est pas une constante fondamentale` | `H_0 est un parametre d'etat actuel du taux d'expansion, pluralement accessible` |
| `Une tension n'est pas une famille` | `Une tension qualifie la compatibilite entre acces, modeles et calibrations` |
| `S_8 n'est pas un verdict cosmologique` | `S_8 est une observable reconstruite, utile pour comparer les routes de croissance` |
| `w n'est pas Lambda` | `w decrit une relation d'etat phenomenologique et teste l'ecart a Lambda` |
| `A_s n'est pas sigma_8` | `A_s et n_s appartiennent a l'entree primordiale ; sigma_8 et S_8 appartiennent a la reconstruction tardive` |

Les formulations negatives peuvent rester en garde-fou historique.

Elles ne doivent plus porter le coeur de la note.

### 8. Decision de maintien / deplacement / reformulation

| Element | Decision |
|---|---|
| `Lambda` | Maintien comme terme de fond du modele cosmologique |
| `H_0` | Maintien comme parametre d'etat actuel de l'expansion |
| `Omega_i` | Reformulation comme budget normalise des composantes |
| `w` | Maintien comme relation d'etat phenomenologique |
| `A_s` | Maintien comme amplitude statistique primordiale |
| `n_s` | Maintien comme inclinaison du spectre primordial |
| `sigma_8` | Maintien comme amplitude reconstruite de croissance |
| `S_8` | Reformulation comme combinaison reconstruite adaptee aux degenerescences |
| Tensions | Maintien comme diagnostic transversal d'acces et de modele |
| Sous-reseaux | Maintien comme organisation interne, non comme architectures autonomes confirmees |

Decision generale :

```text
la reprise positive conserve le fond de la note active,
mais deplace son centre de gravite vers la chaine inferentielle et
reconstructive.
```

### 9. Test de retrait positif

Le test de retrait s'ecrit positivement.

| Retrait | Ce qui devient impossible |
|---|---|
| Retirer le modele global | Les grandeurs perdent leur regime commun d'interpretation |
| Retirer les regimes d'acces | Les parametres deviennent des nombres sans statut empirique |
| Retirer `Lambda` | Perte du terme de fond de LambdaCDM |
| Retirer `H_0` | Perte de l'etat actuel du taux d'expansion |
| Retirer `Omega_i` | Perte du budget normalise des composantes |
| Retirer `w` | Perte du test phenomenologique de relation d'etat |
| Retirer `A_s` et `n_s` | Perte de l'entree statistique primordiale |
| Retirer `sigma_8` et `S_8` | Perte de la reconstruction de croissance tardive |
| Retirer les tensions | Perte du diagnostic de compatibilite entre acces |

Conclusion :

```text
la robustesse de l'architecture cosmologique vient de la solidarite entre
modele, sous-reseaux, acces, reconstruction et controle des tensions.
```

### 10. Effet sur la note active

La note active `Architecture_cosmologique_notes.md` n'est pas invalidee.

Elle reste la consolidation locale.

Le lot 2D lui ajoute une consigne de reprise :

```text
faire passer le texte d'une logique de correction de rang
a une logique de description inferentielle et reconstructive prudente.
```

Priorite de reprise future :

```text
1. ouvrir par la macro-architecture inferentielle et reconstructive ;
2. presenter les sous-reseaux comme organisation interne, non comme classes ;
3. associer chaque grandeur a son modele et a son regime d'acces ;
4. placer les tensions dans une section transversale d'acces et de modele ;
5. conserver les limites sur l'energie noire, l'inflation et les tensions.
```

### 11. Statut du lot 2D

Statut :

```text
lot 2D produit.
```

Suite logique :

```text
lot 2E : reprise de la synthese transverse des architectures.
```

Formule de cloture :

```text
L'architecture cosmologique stabilise une inference : un modele d'univers
rend solidaires des fonctions de fond, d'etat, de normalisation, de conditions
initiales et de reconstruction, puis les expose a des acces multiples dont
les convergences et tensions font partie du statut methodologique.
```
