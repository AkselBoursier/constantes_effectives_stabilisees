# Architecture cosmologique - stress test v0.1

## Test prudent d'unite, de sous-reseaux et de limites

### 1. Fonction du document

Ce document applique le stress test d'architecture a l'architecture cosmologique.

Il prolonge :

```text
04_ARCHITECTURES_INTER_FAMILLES/Architecture_cosmologique_notes.md
02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Synthese_cycle_cosmologique_v0_1.md
05_CARTES_ET_SYNTHESES/Carte_dependances_architectures_v0_1.md
05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_2_refonte.md
```

Question directrice :

```text
l'architecture cosmologique doit-elle rester une architecture unique,
ou faut-il la decrire comme un ensemble de sous-architectures ?
```

Ce document ne cherche pas a resoudre les tensions cosmologiques.

Il cherche seulement a classer leur statut methodologique.

### 2. Decision centrale

Decision prudente :

```text
l'architecture cosmologique reste une macro-architecture active,
mais elle doit etre lue comme un reseau de sous-reseaux.
```

Elle ne doit pas etre :

```text
une famille cosmologique,
un simple tableau de parametres,
une collection de tensions,
ou une theorie physique de l'univers.
```

Elle devient :

```text
une architecture inferentielle et reconstructive,
composee de sous-reseaux fonctionnels soumis a acces, modele et tensions.
```

### 3. Corpus soumis au stress test

Le stress test porte sur les six groupes stabilises par le cycle cosmologique.

| Groupe | Fonction stabilisee | Risque |
|---|---|---|
| `Lambda` | Fond | Confondre terme de fond et explication de l'energie noire |
| `H_0` | Parametre d'etat actuel | Traiter une valeur actuelle comme constante fondamentale |
| `Omega_i` | Densite normalisee | Confondre fraction normalisee et densite absolue |
| `w` | Relation d'etat | Confondre parametrisation et microphysique |
| `A_s`, `n_s` | Conditions initiales perturbatives | Absorber le primordial dans Fond |
| `sigma_8`, `S_8` | Observables reconstruites | Transformer une tension d'acces en famille ou verdict physique |

Regle :

```text
aucun de ces groupes ne suffit seul a definir l'architecture cosmologique.
```

### 4. Stress test general

| Question | Resultat |
|---|---|
| Plusieurs roles sont-ils solidaires ? | Oui : fond, etat, normalisation, condition initiale, reconstruction |
| Le regime physique est-il unique ? | Non : fond global, expansion actuelle, primordial, croissance tardive |
| Le regime d'acces est-il unique ? | Non : CMB, BAO, SNe, distance ladder, lensing, amas, combinaisons |
| Le modele conditionne-t-il les valeurs ? | Oui, fortement pour plusieurs grandeurs |
| Le retrait d'un noeud modifie-t-il le reseau ? | Oui, mais pas toujours de la meme maniere |
| Les tensions suffisent-elles a eclater l'architecture ? | Non, pas seules |
| Faut-il nommer des sous-reseaux ? | Oui |

Conclusion :

```text
architecture unique conservee,
mais decomposee en sous-reseaux internes pour la lecture.
```

### 5. Sous-reseaux proposes

La decomposition prudente distingue cinq sous-reseaux.

| Sous-reseau | Grandeurs principales | Type | Statut |
|---|---|---|---|
| Fond / expansion | `Lambda`, `H_0` | Fond et etat | Sous-reseau actif |
| Budget normalise | `Omega_i` | Normalisation globale | Sous-reseau actif |
| Etat de composante | `w` | Relation d'etat | Sous-reseau phenomenologique |
| Primordial | `A_s`, `n_s` | Conditions initiales | Sous-reseau actif |
| Croissance / reconstruction | `sigma_8`, `S_8` | Observables reconstruites | Sous-reseau sous tension |

Ces sous-reseaux ne sont pas des familles.

Ils sont des zones internes de l'architecture cosmologique.

### 6. Sous-reseau fond / expansion

Noeuds :

```text
Lambda
H_0
modele d'expansion
routes d'acces a l'expansion
```

Dependances :

| Noeud | Depend de | Rend possible |
|---|---|---|
| `Lambda` | Modele de fond | Terme de fond dans LambdaCDM |
| `H_0` | Expansion actuelle + acces | Normalisation actuelle du taux d'expansion |
| Routes d'acces | Distance ladder, CMB + modele, BAO, SNe | Comparaison des contraintes |

Test de retrait :

```text
retirer Lambda ne retire pas H_0,
mais modifie fortement le modele de fond ;
retirer H_0 ne retire pas Lambda,
mais detruit la normalisation actuelle de l'expansion.
```

Decision :

```text
sous-reseau actif,
mais pas architecture autonome a ce stade.
```

Limite :

```text
ce sous-reseau ne resout ni la nature de Lambda ni la tension H_0.
```

### 7. Sous-reseau budget normalise

Noeuds :

```text
Omega_i
rho_i
rho_crit
H
modele de decomposition globale
```

Dependances :

```text
Omega_i = rho_i / rho_crit
rho_crit = 3 H^2 / (8 pi G)
```

Lecture :

```text
Omega_i est une relation normalisee dans un budget global,
non une densite absolue et non une constante primitive.
```

Test de retrait :

```text
retirer rho_crit ou H detruit la comparabilite des Omega_i ;
retirer le modele de decomposition rend le budget ambigu.
```

Decision :

```text
sous-reseau actif de normalisation.
```

Limite :

```text
ce sous-reseau depend du modele cosmologique et de ses composantes.
```

### 8. Sous-reseau etat de composante

Noeud principal :

```text
w
```

Lecture :

```text
w = p / rho
```

ou, selon convention :

```text
w = p / (rho c^2)
```

Dependances :

| Noeud | Depend de | Rend possible |
|---|---|---|
| `w` | Hypothese de composante fluide ou phenomenologique | Test d'etat d'une composante |
| `w = -1` | Reference LambdaCDM | Identification phenomenologique a Lambda stricte |
| `w(a)` | Extension phenomenologique | Test de variation effective |

Test de retrait :

```text
retirer w n'empeche pas une architecture LambdaCDM stricte,
mais retire la possibilite de tester phenomenologiquement l'etat d'une composante.
```

Decision :

```text
sous-reseau phenomenologique,
pas architecture autonome.
```

Limite :

```text
w ne donne pas une microphysique de l'energie noire.
```

### 9. Sous-reseau primordial

Noeuds :

```text
A_s
n_s
spectre primordial
point pivot
CMB
modele d'inference
```

Structure :

```text
P_R(k) = A_s (k / k_*)^(n_s - 1)
```

Lecture :

```text
A_s et n_s sont des conditions initiales perturbatives,
non des termes de fond.
```

Test de retrait :

```text
retirer A_s retire l'amplitude des perturbations scalaires ;
retirer n_s retire la forme spectrale ;
retirer le CMB ou le modele d'inference affaiblit leur stabilisation.
```

Decision :

```text
sous-reseau actif primordial.
```

Limite :

```text
ce sous-reseau ne fixe pas une theorie unique de l'inflation
ni une microphysique complete des perturbations.
```

### 10. Sous-reseau croissance / reconstruction

Noeuds :

```text
sigma_8
S_8
Omega_m
croissance tardive
lensing faible
CMB + modele
amas
3x2pt
systematiques
```

Lecture :

```text
sigma_8 et S_8 sont des observables reconstruites,
non des constantes primitives.
```

Dependances :

```text
S_8 combine sigma_8 et Omega_m selon une convention d'analyse.
```

Test de retrait :

```text
retirer le modele d'inference rend sigma_8 et S_8 mal definis ;
retirer les routes d'acces transforme la tension en simple label ;
retirer Omega_m affaiblit la lecture de S_8.
```

Decision :

```text
sous-reseau reconstructif sous tension.
```

Limite :

```text
ce sous-reseau ne transforme pas la tension S_8 en verdict physique direct.
```

### 11. Reseau transversal d'acces

Les sous-reseaux cosmologiques partagent un reseau transversal d'acces.

| Acces | Role |
|---|---|
| CMB | Contraint fond, primordial, lentille et modele |
| BAO | Contraint distances et expansion relative |
| SNe | Contraignent distances et expansion tardive |
| Distance ladder | Contraint H_0 localement |
| Lensing faible | Contraint croissance tardive et S_8 |
| Amas | Contraignent croissance et masse de structure |
| 3x2pt | Combine plusieurs observables de structure |

Regle :

```text
le reseau d'acces traverse les sous-reseaux,
mais ne devient pas une architecture separee.
```

### 12. Reseau transversal des tensions

Les tensions ne sont pas des familles.

Elles ne sont pas non plus des sous-architectures.

Elles sont :

```text
des proprietes d'un reseau d'acces, de modele et d'inference.
```

| Tension | Sous-reseau touche | Statut methodologique |
|---|---|---|
| H_0 | Fond / expansion | Divergence inter-acces |
| S_8 | Croissance / reconstruction | Tension reconstructive |
| w ou w(a) | Etat de composante | Test phenomenologique de modele |
| A_s / sigma_8 | Primordial et croissance | Chaine d'inference entre initial et tardif |

Decision :

```text
une tension persistante oblige a documenter le stress test,
mais ne suffit pas a creer une famille ou une architecture autonome.
```

### 13. Test d'eclatement

Le stress test distingue trois niveaux.

| Niveau | Critere | Decision |
|---|---|---|
| Sous-reseau interne | Fonctions distinctes mais dependantes du meme modele global | Confirme |
| Sous-architecture candidate | Regime, acces, tensions et dependances assez autonomes | A surveiller |
| Architecture separee | Reseau autonome avec test de retrait propre | Non confirme |

Application :

| Zone | Niveau obtenu |
|---|---|
| Fond / expansion | Sous-reseau interne |
| Budget normalise | Sous-reseau interne |
| Etat de composante | Sous-reseau phenomenologique |
| Primordial | Sous-reseau interne fort |
| Croissance / reconstruction | Sous-reseau sous tension, sous-architecture candidate faible |
| Tensions | Reseau transversal, pas sous-architecture |

Conclusion :

```text
aucune sous-architecture cosmologique autonome n'est confirmee en v0.1.
```

### 14. Decision finale du stress test

Decision :

```text
conserver Architecture cosmologique comme macro-architecture unique,
mais toujours la presenter avec ses sous-reseaux internes.
```

Statut :

```text
architecture confirmee,
inferentielle et reconstructive,
sous stress test permanent,
non eclatee a ce stade.
```

Formule :

```text
Cosmologique = macro-architecture d'inference ;
fond, etat, normalisation, primordial et reconstruction = sous-reseaux ;
tensions = proprietes transversales d'acces et de modele.
```

### 15. Consequences pour la carte v1.2

La carte consolidee v1.2 reste valide.

Elle doit toutefois etre lue avec la precision suivante :

```text
Architecture cosmologique ne signifie pas bloc homogene.
```

Elle signifie :

```text
macro-architecture dont les grandeurs sont solidaires
par modele global, regimes d'acces et dependances d'inference.
```

Ajout recommande dans les futures cartes :

```text
Cosmologique : macro-architecture inferentielle / reconstructive,
composee de sous-reseaux fond-expansion, budget, etat, primordial,
croissance-reconstruction et tensions transversales.
```

### 16. Protocole pour futures fiches cosmologiques

Toute nouvelle fiche cosmologique doit indiquer :

```text
1. le sous-reseau concerne ;
2. le role contextuel principal ;
3. le regime physique ;
4. le regime d'acces ;
5. le modele d'inference ;
6. le test de retrait ;
7. la tension eventuelle ;
8. la limite conservee.
```

Elle doit eviter :

```text
famille Cosmologie,
famille Tension,
famille Fond,
classement par parametre de modele seul,
classement par acces seul.
```

### 17. Plan de reprise produit ensuite

Le stress test ne doit pas rester une couche externe au cycle.

Document de reprise :

```text
02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Plan_reprise_cycle_cosmologique_v0_1.md
```

Role :

```text
preparer la clarification interne des fiches cosmologiques,
sans creer d'addendum permanent.
```

Decision :

```text
reprendre le cycle par sous-reseaux
plutot que multiplier les notes superposees.
```

### 18. Documents integres

Documents cosmologiques :

```text
02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Synthese_cycle_cosmologique_v0_1.md
02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Plan_reprise_cycle_cosmologique_v0_1.md
04_ARCHITECTURES_INTER_FAMILLES/Architecture_cosmologique_notes.md
```

Documents methodologiques et cartes :

```text
01_CADRE_METHODOLOGIQUE/Note_synthese_methodologique_v1_3_pre_familial_et_temporalite.md
01_CADRE_METHODOLOGIQUE/Matrice_criblage_taxonomique_v0_1.md
05_CARTES_ET_SYNTHESES/Carte_dependances_architectures_v0_1.md
05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_2_refonte.md
05_CARTES_ET_SYNTHESES/Index_raisonne_du_corpus_v1_0.md
```

Fiches sources du cycle :

```text
02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Cycle_cosmologique_v0_1_cadrage.md
02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Cycle_cosmologique_v0_2_Lambda.md
02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Cycle_cosmologique_v0_3_H0.md
02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Cycle_cosmologique_v0_4_Omega_i.md
02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Cycle_cosmologique_v0_5_w.md
02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Cycle_cosmologique_v0_6_As_ns.md
02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Cycle_cosmologique_v0_7_sigma8_S8.md
```

### 19. Formule de cloture

Le stress test ne fragilise pas l'architecture cosmologique.

Il la rend moins plate.

Formule finale :

> L'architecture cosmologique tient comme macro-architecture si elle accepte de ne pas etre homogene : elle stabilise un reseau de fond, d'etat, de normalisation, de primordial, de reconstruction et de tensions d'acces, sans transformer ce reseau en famille unique.
