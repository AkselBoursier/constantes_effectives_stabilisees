# Cercle 2 lot 2A - Saveur-Higgs v0.1

## Reprise positive de l'architecture constitutive

### 1. Fonction

Cette note produit le lot 2A du cercle 2.

Elle reprend l'architecture Saveur-Higgs par formulations positives, a partir
des appuis suivants :

```text
04_ARCHITECTURES/Cercle2_architectures_actives_v0_1.md
04_ARCHITECTURES/Architecture_saveur_Higgs_notes.md
02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/Synthese_cycle_saveur_Higgs_v0_1.md
02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/Synthese_recuperation_sources_saveur_Higgs_cible_v0_1.md
```

Le but n'est pas de corriger toute la note active ligne par ligne.

Le but est de stabiliser une version positive du noyau architectural :

```text
regime electrofaible brise
+ echelle constitutive
+ textures de couplage
+ diagonalisation
+ spectres de masses
+ orientations observables
+ acces phenomenologiques heterogenes.
```

### 2. Formulation positive d'ouverture

Formulation directrice :

```text
Saveur-Higgs est l'architecture constitutive du regime electrofaible brise :
elle decrit comment une echelle commune, des textures de couplage,
des operations de diagonalisation, des spectres de masse et des orientations
observables deviennent solidaires.
```

Cette formulation place d'abord ce que le reseau fait.

Elle permet de reserver les corrections de rang aux sections de controle.

### 3. Matrice regime / solidarite / acces / trajectoire

| Champ | Lecture Saveur-Higgs |
|---|---|
| Regime | Regime electrofaible brise, avec extension prudente au secteur neutrino massif |
| Solidarite | `v`, matrices de Yukawa, matrices de masse, diagonalisation, spectres et orientations |
| Noeuds | `v`, `Y_f`, `M_f`, rotations gauches, `m_f`, CKM, PMNS, `Delta m^2`, masse absolue neutrino |
| Acces | `G_F`, masses faibles, Higgs, masses fermioniques, decays faibles, melanges de mesons, oscillations neutrino, bornes directes et cosmologiques |
| Trajectoire | Brisure electroweak -> matrices de masse -> diagonalisation -> spectres -> orientations -> manifestations |
| Limites | Origine des Yukawa, hierarchies de saveur, contraste CKM / PMNS, nature neutrino, ancrage absolu du spectre neutrino |

Formule :

```text
la stabilisation Saveur-Higgs est une constitution de regime,
pas une juxtaposition de valeurs.
```

### 4. Chaine constitutive

La chaine positive est :

```text
1. `v` fixe l'echelle du regime electrofaible brise.
2. Les matrices `Y_f` distribuent cette echelle entre secteurs fermioniques.
3. Les matrices de masse deviennent lisibles apres couplage au champ de Higgs.
4. La diagonalisation produit les bases physiques.
5. Les valeurs `m_f` stabilisent les spectres accessibles.
6. CKM et PMNS stabilisent des orientations entre bases.
7. Les transitions, oscillations et phases rendent ces orientations observables.
```

Le role de la diagonalisation est central.

Sans elle, la note retombe dans une lecture trop pauvre :

```text
echelle + couplage = masse.
```

La lecture complete est :

```text
echelle + textures + diagonalisation = spectres + orientations.
```

### 5. Noeuds et fonctions locales

| Noeud | Fonction positive | Acces ou manifestation |
|---|---|---|
| `v` | Echelle constitutive du regime brise | `G_F`, ajustements electroweak, masses faibles |
| `Y_f` | Texture de couplage au champ de Higgs | Masses, couplages Higgs, schema de renormalisation |
| `M_f` | Matrice de masse de regime | Construction apres brisure |
| Diagonalisation | Passage aux bases physiques | Spectres de masse et orientations |
| `m_f` | Spectre stabilise | Mesures directes, reconstructions, schemas pour quarks |
| CKM | Orientation transitionnelle du secteur quark | Decays faibles, melanges de mesons, CP |
| Wolfenstein | Coordonnees hierarchiques de CKM | Parametrisation locale de l'orientation |
| PMNS | Orientation oscillatoire du secteur neutrino massif | Oscillations neutrino |
| `Delta m^2` | Ecart spectral de dephasage | Oscillations, sans ancrage absolu |
| Masse absolue neutrino | Ancrage spectral borne | Beta decay, cosmologie, double beta selon hypotheses |

### 6. Acces et robustesse

L'architecture Saveur-Higgs a un acces intermediaire.

Elle n'est ni purement directe, ni aussi reconstructive que la cosmologie.

| Domaine | Robustesse | Prudence |
|---|---|---|
| `v` et secteur faible | Forte dans le cadre standard | Depend de l'inference electroweak |
| Leptons charges | Forte | Faible dette d'acces |
| Quarks | Robuste mais scheme-dependent | Masses et Yukawa dependent du schema |
| CKM | Forte globalement | Tensions locales et dependance aux fits |
| PMNS | Forte pour plusieurs angles et ecarts | Phases et ordre de masse encore incomplets |
| Masse absolue neutrino | Bornee | Acces heterogenes et modele-dependants |

Regle de reprise :

```text
aucune grandeur Saveur-Higgs ne doit etre presentee sans son regime d'acces.
```

### 7. Formulations a eviter

Le lot 2A recommande de remplacer les formulations defensives par les
formulations positives suivantes.

| Formulation a eviter | Formulation positive |
|---|---|
| `Saveur-Higgs n'est pas une famille` | `Saveur-Higgs solidarise echelle, textures, spectres et orientations dans le regime brise` |
| `m_f n'est pas seulement une relation` | `m_f est une valeur spectrale issue de l'echelle, des textures et de la diagonalisation` |
| `CKM n'est pas une constante de saveur autonome` | `CKM est l'orientation transitionnelle observable du desalignement quark` |
| `Wolfenstein n'est pas une nouvelle famille` | `Wolfenstein fournit des coordonnees hierarchiques locales de CKM` |
| `Delta m^2 n'est pas une famille oscillatoire` | `Delta m^2 stabilise l'ecart spectral qui porte le dephasage oscillatoire` |
| `Relation intervient mais ne suffit pas` | `la forme locale doit etre nommee : spectrale, constitutive, orientationnelle ou dephasante` |

Les formulations negatives peuvent rester en garde-fou historique.

Elles ne doivent plus porter le coeur de la note.

### 8. Decision de maintien / deplacement / reformulation

| Element | Decision |
|---|---|
| `v` | Maintien comme echelle constitutive |
| `Y_f` | Maintien comme texture de couplage |
| `m_f` | Deplacement vers spectre stabilise dans l'architecture constitutive |
| CKM | Maintien comme orientation transitionnelle |
| Wolfenstein | Reformulation comme coordonnees hierarchiques de CKM |
| PMNS | Maintien prudent comme orientation oscillatoire du secteur neutrino massif |
| `Delta m^2` | Reformulation comme ecart spectral de dephasage |
| Masse absolue neutrino | Maintien comme ancrage spectral borne et interface cosmologique |

Decision generale :

```text
la reprise positive conserve le fond de la note active,
mais deplace son centre de gravite vers la chaine constitutive.
```

### 9. Test de retrait positif

Le test de retrait s'ecrit positivement.

| Retrait | Ce qui devient impossible |
|---|---|
| Retirer `v` | Perte de l'echelle commune du regime brise |
| Retirer `Y_f` | Perte de la distribution fermionique de l'echelle |
| Retirer la diagonalisation | Perte des bases physiques, des spectres et des orientations |
| Retirer CKM | Perte de l'orientation transitionnelle quark |
| Retirer PMNS | Perte de l'orientation oscillatoire neutrino |
| Retirer les regimes d'acces | Transformation des grandeurs en nombres sans statut |

Conclusion :

```text
la robustesse de Saveur-Higgs vient du reseau,
pas d'un nom de classement.
```

### 10. Effet sur la note active

La note active `Architecture_saveur_Higgs_notes.md` n'est pas invalidee.

Elle reste la consolidation locale.

Le lot 2A lui ajoute une consigne de reprise :

```text
faire passer le texte d'une logique de correction de rang
a une logique de description constitutive.
```

Priorite de reprise future :

```text
1. remplacer les ouvertures negatives par la formulation positive ;
2. reduire les occurrences defensives de `relation` ;
3. expliciter la diagonalisation comme noeud central ;
4. garder les garde-fous dans une section dediee ;
5. conserver les limites ouvertes.
```

### 11. Statut du lot 2A

Statut :

```text
lot 2A produit.
```

Suite logique :

```text
lot 2B : reprise positive de l'architecture metrologique SI.
```

Formule de cloture :

```text
Saveur-Higgs stabilise une constitution : une echelle devient distribuee par
des textures, rendue spectrale par diagonalisation, puis observable comme
orientation et transition dans des regimes d'acces determines.
```
