# Cercle 2 lot 2B - Metrologique SI v0.1

## Reprise positive de l'architecture definitionnelle et operationnelle

### 1. Fonction

Cette note produit le lot 2B du cercle 2.

Elle reprend l'architecture metrologique SI par formulations positives, a
partir des appuis suivants :

```text
04_ARCHITECTURES/Cercle2_architectures_actives_v0_1.md
04_ARCHITECTURES/Architecture_metrologique_SI_notes.md
02_CYCLES_PHYSIQUES/04_Cycle_thermo_metrologique/Synthese_recuperation_thermo_metrologique_SI_v0_1.md
02_CYCLES_PHYSIQUES/08_Cycle_metrologique_SI/Cycle_metrologique_SI_v0_1_c_h_e.md
01_CADRE_METHODOLOGIQUE/Note_situation_effective_et_equilibrage_SI_v0_1.md
```

Le but n'est pas de refaire le cycle SI.

Le but est de stabiliser une version positive du noyau architectural :

```text
systeme SI
+ constantes definissantes primaires
+ compositions exactes
+ definitions d'unites
+ realisations pratiques
+ roles physiques conserves
+ distinction entre exactitude et acces.
```

### 2. Formulation positive d'ouverture

Formulation directrice :

```text
L'architecture metrologique SI rend un systeme d'unites operatoire en fixant
des valeurs definissantes, en produisant des compositions exactes et en
organisant leurs realisations pratiques, sans effacer les roles physiques
des grandeurs concernees.
```

Cette formulation place d'abord ce que le reseau fait.

Elle evite de reduire l'architecture SI a une liste de constantes exactes ou
a une simple convention.

### 3. Matrice regime / solidarite / acces / trajectoire

| Champ | Lecture metrologique SI |
|---|---|
| Regime | Systeme SI revise, avec roles physiques conserves dans leurs regimes propres |
| Solidarite | Constantes definissantes, compositions exactes, definitions d'unites, realisations pratiques |
| Noeuds | `k_B`, `N_A`, `c`, `h`, `e`, `R`, `K_J`, `R_K` |
| Acces | Definitions SI, realisations thermometriques, chimiques, atomiques, longueur-temps, balances de Kibble, effets Josephson et Hall quantique |
| Trajectoire | Mesure historique -> stabilisation empirique -> absorption definitionnelle -> realisation pratique continue |
| Limites | Exactitude de definition, incertitudes de realisation, roles physiques non epuises, distinction `e` / `alpha` |

Formule :

```text
la stabilisation SI est une operation de definition et de realisation,
pas une mesure parfaite ni un effacement physique.
```

### 4. Chaine definitionnelle et operationnelle

La chaine positive est :

```text
1. Une histoire empirique rend certaines grandeurs assez stabilisees pour
   devenir definissantes.
2. Le SI fixe leurs valeurs numeriques dans un systeme coherent d'unites.
3. Ces valeurs definissantes produisent des compositions exactes.
4. Les realisations pratiques rendent les definitions utilisables.
5. Les regimes physiques conservent le contenu propre des grandeurs.
6. Les incertitudes se deplacent vers les realisations et les grandeurs non
   definissantes.
```

Le point central est la distinction entre trois niveaux.

```text
valeur definissante
composition exacte
realisation pratique
```

La lecture complete est :

```text
definition + composition + realisation = architecture metrologique operatoire.
```

### 5. Noeuds et fonctions locales

| Noeud | Fonction positive | Acces ou manifestation |
|---|---|---|
| `k_B` | Constante definissante du kelvin ; passage energie / temperature | Realisations thermometriques |
| `N_A` | Constante definissante de la mole ; comptage entites / quantite de matiere | Realisations chimiques et atomiques |
| `c` | Constante definissante ; echelle causale espace-temps | Realisations longueur-temps |
| `h` | Constante definissante ; quantum d'action | Kilogramme, balance de Kibble, spectroscopie |
| `e` | Constante definissante ; quantum de charge | Ampere, comptage de charge |
| `R` | Composition exacte `N_A k_B` | Thermodynamique macroscopique |
| `K_J` | Composition exacte `2 e / h` | Effet Josephson |
| `R_K` | Composition exacte `h / e^2` | Effet Hall quantique |
| `alpha` | Couplage sans dimension distinct de `e` | Determination experimentale |

### 6. Acces et robustesse

L'architecture metrologique SI possede un acces definitionnel fort, mais elle
ne transforme pas tout acces en certitude pratique.

| Domaine | Robustesse | Prudence |
|---|---|---|
| Valeurs definissantes | Exactes dans le SI | Exactitude de definition, non mesure parfaite |
| Realisations pratiques | Operationnelles et controlees | Incertitudes experimentales persistantes |
| Compositions exactes | Exactes par heritages definissants | Ne sont pas des constantes definissantes primaires |
| Roles physiques | Conserves hors du seul SI | Ne sont pas expliques par l'exactitude numerique |
| `e` / `alpha` | Distinction robuste | `alpha` reste determine experimentalement |

Regle de reprise :

```text
aucune grandeur SI ne doit etre presentee sans distinguer valeur
definissante, realisation pratique et contenu physique.
```

Regle de proportion :

```text
le poids de l'acces dans le SI est normal pour une architecture
definitionnelle ; il devient excessif s'il sert a definir toutes les formes
de constance.
```

Le SI doit donc rester un cas local :

```text
cas de definition et de realisation,
modele local d'une constance fixee et mise en oeuvre dans un systeme d'unites.
```

### 7. Formulations a eviter

Le lot 2B recommande de remplacer les formulations defensives par les
formulations positives suivantes.

| Formulation a eviter | Formulation positive |
|---|---|
| `SI n'est pas une famille superieure` | `SI organise une architecture definitionnelle et operationnelle d'unites` |
| `R n'est pas une constante definissante primaire` | `R` est une composition exacte heritee de `N_A` et `k_B` |
| `K_J et R_K ne sont pas des relations par defaut` | `K_J et R_K sont des compositions exactes utiles aux realisations electriques quantiques` |
| `c n'est pas seulement une convention` | `c est valeur definissante dans le SI et echelle causale en relativite` |
| `h n'est pas seulement une convention` | `h est valeur definissante dans le SI et quantum d'action en physique quantique` |
| `e ne doit pas etre confondu avec alpha` | `e` fixe le quantum de charge ; `alpha` porte le couplage electromagnetique sans dimension |
| `exactitude SI n'est pas precision empirique` | `exactitude SI fixe la valeur ; les realisations gardent leurs incertitudes` |

Les formulations negatives peuvent rester en garde-fou historique.

Elles ne doivent plus porter le coeur de la note.

### 8. Decision de maintien / deplacement / reformulation

| Element | Decision |
|---|---|
| `k_B` | Maintien comme constante definissante avec role energie / temperature |
| `N_A` | Maintien comme constante definissante avec role de comptage |
| `c` | Maintien comme constante definissante et echelle causale |
| `h` | Maintien comme constante definissante et quantum d'action |
| `e` | Maintien comme constante definissante et quantum de charge |
| `R` | Reformulation comme composition exacte thermodynamique |
| `K_J` | Reformulation comme composition exacte de realisation electrique |
| `R_K` | Reformulation comme composition exacte de realisation electrique |
| `alpha` | Maintien hors exactitude SI comme couplage sans dimension determine experimentalement |

Decision generale :

```text
la reprise positive conserve le fond de la note active,
mais deplace son centre de gravite vers la chaine definitionnelle et
operationnelle.
```

### 9. Test de retrait positif

Le test de retrait s'ecrit positivement.

| Retrait | Ce qui devient impossible |
|---|---|
| Retirer les constantes definissantes | Perte du socle numerique exact du SI revise |
| Retirer les compositions exactes | Perte de grandeurs derivees exactes comme `R`, `K_J`, `R_K` |
| Retirer les realisations pratiques | Definitions exactes sans mise en oeuvre operationnelle |
| Retirer les roles physiques | Reduction du SI a une notation d'unites |
| Retirer la distinction `e` / `alpha` | Confusion entre charge dimensionnee exacte et couplage sans dimension |
| Retirer l'histoire empirique | Perte de la trajectoire qui rend l'absorption definitionnelle intelligible |

Conclusion :

```text
la robustesse de l'architecture SI vient de la solidarite entre definition,
composition, realisation et contenu physique conserve.
```

### 10. Effet sur la note active

La note active `Architecture_metrologique_SI_notes.md` n'est pas invalidee.

Elle reste la consolidation locale.

Le lot 2B lui ajoute une consigne de reprise :

```text
faire passer le texte d'une logique de correction de rang
a une logique de description definitionnelle et operationnelle.
```

Priorite de reprise future :

```text
1. ouvrir par la chaine definition / composition / realisation ;
2. presenter `R`, `K_J` et `R_K` comme compositions exactes ;
3. expliciter les realisations pratiques comme noeud d'acces ;
4. placer les garde-fous dans une section dediee ;
5. conserver les limites sur l'origine physique et l'interpretation.
```

### 11. Statut du lot 2B

Statut :

```text
lot 2B produit.
```

Suite logique :

```text
lot 2C : reprise positive de l'architecture effective basse energie.
```

Formule de cloture :

```text
L'architecture SI stabilise une operation : des valeurs definissantes rendent
un systeme d'unites coherent, des compositions exactes en prolongent les
effets, des realisations le rendent praticable, et les roles physiques des
grandeurs restent lisibles hors de la seule convention.
```
