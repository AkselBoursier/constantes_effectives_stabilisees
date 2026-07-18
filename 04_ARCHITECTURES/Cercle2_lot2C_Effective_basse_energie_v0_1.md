# Cercle 2 lot 2C - Effective basse energie v0.1

## Reprise positive de l'architecture de validite

### 1. Fonction

Cette note produit le lot 2C du cercle 2.

Elle reprend l'architecture effective basse energie par formulations positives,
a partir des appuis suivants :

```text
04_ARCHITECTURES/Cercle2_architectures_actives_v0_1.md
04_ARCHITECTURES/Architecture_effective_basse_energie_notes.md
02_CYCLES_PHYSIQUES/06_Cycle_effectif_basse_energie/Synthese_cycle_effectif_basse_energie_v0_1.md
02_CYCLES_PHYSIQUES/06_Cycle_effectif_basse_energie/Synthese_comparaison_alphaG_MPl_sources_v0_1.md
```

Le but n'est pas de refaire le cycle effectif.

Le but est de stabiliser une version positive du noyau architectural :

```text
regime limite
+ domaine de validite
+ non-resolution explicite
+ coefficient, couplage ou echelle stabilise
+ raccordement local, distribue ou attendu
+ limites de description.
```

### 2. Formulation positive d'ouverture

Formulation directrice :

```text
L'architecture effective basse energie rend operatoire une description limitee
en indiquant ce qui est condense, non resolu, courant, non perturbatif,
supprime ou attendu au-dela du domaine de validite.
```

Cette formulation place d'abord ce que le reseau fait.

Elle evite de reduire l'effectivite a une approximation vague ou a une seule
image issue de la theorie de Fermi.

### 3. Matrice regime / solidarite / acces / trajectoire

| Champ | Lecture effective basse energie |
|---|---|
| Regime | Domaine ou une description limitee vaut sans resoudre toute la structure plus profonde |
| Solidarite | Coefficients effectifs, echelles de validite, couplages de regime, changements de description |
| Noeuds | `G_F`, `M_W`, `alpha_s(Q^2)`, `Lambda_QCD`, `alpha_G(E)`, `M_Pl` |
| Acces | Mesures faibles, precision electroweak, extractions QCD, construction gravitationnelle par rapports d'echelle |
| Trajectoire | Description plus complete -> regime limite -> non-resolution explicite -> grandeur stabilisee -> domaine de validite |
| Limites | Completion quantique de la gravitation, regimes non perturbatifs, origine des constantes, frontieres non nettes |

Formule :

```text
la stabilisation effective est une validite de description dans un regime determine,
pas une valeur absolue hors domaine.
```

### 4. Trois formes positives d'effectivite

Le cycle stabilise trois formes internes.

#### 4.1 Integration locale

Cas :

```text
G_F / M_W
```

Lecture positive :

```text
un mediateur massif n'est pas resolu explicitement ;
son effet devient un coefficient local dans un regime E << M_W.
```

Forme :

```text
non-resolution d'un degre de liberte lourd
-> coefficient effectif
-> validite locale de la theorie de Fermi.
```

#### 4.2 Flot et changement de regime

Cas :

```text
alpha_s(Q^2) / Lambda_QCD
```

Lecture positive :

```text
le couplage varie avec l'echelle ;
une echelle dynamique marque le changement de description.
```

Forme :

```text
couplage courant
+ echelle dynamique
+ passage perturbatif / non perturbatif
+ degres de liberte adaptes.
```

#### 4.3 Suppression par hierarchie d'echelle

Cas :

```text
alpha_G(E) / M_Pl
```

Lecture positive :

```text
le couplage gravitationnel quantique devient lisible par un rapport d'echelle ;
la basse energie correspond a une suppression forte.
```

Forme :

```text
G_N dimensionne
-> rapport sans dimension
-> suppression pour E << M_Pl
-> validite attendue de la gravitation effective basse energie.
```

### 5. Noeuds et fonctions locales

| Noeud | Fonction positive | Acces ou manifestation |
|---|---|---|
| `G_F` | Coefficient effectif de raccordement faible basse energie | Duree de vie du muon, fits faibles |
| `M_W` | Echelle electrofaible et borne de validite de Fermi | Precision electroweak, mesures du W |
| `alpha_s(Q^2)` | Couplage courant de QCD | Extractions multi-processus |
| `Lambda_QCD` | Echelle dynamique du changement de regime QCD | Definition RG, ajustements QCD |
| `alpha_G(E)` | Couplage gravitationnel effectif construit | Rapport a une echelle d'energie |
| `M_Pl` | Echelle de validite attendue gravitationnelle | Grandeur derivee de `G_N`, `hbar`, `c` |

### 6. Acces et robustesse

L'architecture effective basse energie possede un acces composite.

Elle depend toujours du domaine ou la description vaut.

| Domaine | Robustesse | Prudence |
|---|---|---|
| Faible basse energie | Forte pour `G_F` dans son domaine | Ne remplace pas la theorie electroweak complete |
| Echelle electroweak | Forte, mesuree et ajustee | Fonction seuil seulement dans la lecture Fermi |
| QCD | Robuste mais dependante de l'echelle et du schema | Basse energie non perturbative |
| Gravitation basse energie | Forte comme description classique / EFT | Completion quantique ouverte |
| Planck | Echelle de reference | Pas une frontiere experimentale nette |

Regle de reprise :

```text
aucune grandeur effective ne doit etre presentee sans son domaine de validite.
```

### 7. Formulations a eviter

Le lot 2C recommande de remplacer les formulations defensives par les
formulations positives suivantes.

| Formulation a eviter | Formulation positive |
|---|---|
| `effectif n'est pas une famille superieure` | `effectif decrit un mode de validite dans un regime determine` |
| `basse energie n'est pas toujours simplification` | `la basse energie prend une forme locale, non perturbative ou supprimee selon le secteur` |
| `Seuil n'est pas une famille` | `le seuil est la visibilite locale d'une echelle de validite` |
| `Hierarchie n'est pas une famille` | `la hierarchie qualifie un ecart d'echelle, de couplage ou de validite` |
| `G_N n'est pas comparable directement a alpha` | Le contenu de couplage gravitationnel passe par `alpha_G(E)` ou un rapport sans dimension |
| `M_Pl n'est pas une frontiere nette` | `M_Pl fournit une echelle de validite attendue et de comparaison gravitationnelle` |

Les formulations negatives peuvent rester en garde-fou historique.

Elles ne doivent plus porter le coeur de la note.

### 8. Decision de maintien / deplacement / reformulation

| Element | Decision |
|---|---|
| `G_F` | Maintien comme coefficient de raccordement local faible |
| `M_W` | Maintien comme echelle electroweak a fonction de validite |
| `alpha_s(Q^2)` | Maintien comme couplage courant |
| `Lambda_QCD` | Maintien comme echelle dynamique de changement de regime |
| `alpha_G(E)` | Maintien comme couplage gravitationnel effectif construit |
| `M_Pl` | Maintien comme echelle de validite attendue, non frontiere nette |
| Validite | Reformulation comme fonction transversale centrale |
| Seuil | Reformulation comme manifestation locale d'une echelle |
| Hierarchie | Reformulation comme qualification d'ecarts d'echelle et de couplage |

Decision generale :

```text
la reprise positive conserve le fond de la note active,
mais deplace son centre de gravite vers la pluralite des validites.
```

### 9. Test de retrait positif

Le test de retrait s'ecrit positivement.

| Retrait | Ce qui devient impossible |
|---|---|
| Retirer le domaine de validite | Les grandeurs deviennent des coefficients hors contexte |
| Retirer `G_F` | Perte du raccordement local faible basse energie |
| Retirer `M_W` | Perte de la borne electroweak de la theorie de Fermi |
| Retirer `alpha_s(Q^2)` | Perte de la dependance d'echelle du couplage QCD |
| Retirer `Lambda_QCD` | Perte du marqueur dynamique du changement de regime QCD |
| Retirer `alpha_G(E)` | Perte de la lecture sans dimension du couplage gravitationnel |
| Retirer `M_Pl` | Perte de l'echelle de comparaison et de validite attendue |

Conclusion :

```text
la robustesse de l'architecture effective vient de la solidarite entre
regime limite, grandeur stabilisee et domaine de validite.
```

### 10. Effet sur la note active

La note active `Architecture_effective_basse_energie_notes.md` n'est pas
invalidee.

Elle reste la consolidation locale.

Le lot 2C lui ajoute une consigne de reprise :

```text
faire passer le texte d'une logique de correction de rang
a une logique de description des validites situees.
```

Priorite de reprise future :

```text
1. ouvrir par la notion de validite de description dans un regime determine ;
2. presenter les trois formes d'effectivite comme formes positives ;
3. expliciter le sens variable de basse energie ;
4. placer les garde-fous sur Seuil, Hierarchie et Effectif dans une section dediee ;
5. conserver la prudence gravitationnelle autour de `M_Pl`.
```

### 11. Statut du lot 2C

Statut :

```text
lot 2C produit.
```

Suite logique :

```text
lot 2D : reprise positive prudente de l'architecture cosmologique.
```

Formule de cloture :

```text
L'architecture effective basse energie stabilise une validite : elle rend un
regime descriptible en nommant ce qui est condense, courant, non perturbatif,
supprime ou attendu au-dela de son domaine.
```
