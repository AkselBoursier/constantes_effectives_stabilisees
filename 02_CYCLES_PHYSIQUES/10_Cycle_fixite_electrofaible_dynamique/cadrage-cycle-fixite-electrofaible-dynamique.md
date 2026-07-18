# Cycle — fixité électrofaible dynamique

## Statut

Ce cycle prolonge le cycle fine-tuning en changeant le type de contrefactuel étudié.

Les modèles weakless et les variations anthropiques usuelles comparent généralement plusieurs univers-modèles, chacun doté d'un jeu de paramètres globalement fixe. Le présent cycle demande au contraire :

> Une grandeur électrofaible susceptible de varier peut-elle évoluer au cours d'un même univers, puis devenir pratiquement fixe dans un régime tardif ?

L'objet n'est donc plus seulement la variation **entre** univers possibles, mais la variation **dans** l'histoire d'un univers.

## 1. Question directrice

> Comment une structure électrofaible capable de varier devient-elle suffisamment fixe pour soutenir des relations physiques reproductibles dans un régime donné ?

Cette question se décompose en quatre sous-questions :

1. qu'est-ce qui varie exactement ;
2. quel degré de liberté porte cette variation ;
3. quel mécanisme produit, ralentit ou arrête l'évolution ;
4. quelles observations permettent de distinguer variation réelle, dépendance de régime et simple dépendance de représentation ?

## 2. Hypothèse de travail

Le cycle examine l'hypothèse suivante :

> Une partie de ce qui est appelé « constante électrofaible » pourrait être comprise comme la valeur tardive, locale ou effective d'une architecture dynamique devenue quasi stationnaire.

Cette hypothèse n'est pas un résultat acquis. Elle doit pouvoir échouer.

Elle échoue notamment si :

- aucune extension cohérente ne permet la variation considérée ;
- la variation contredit les observations ;
- la stabilisation exige un réglage équivalent ou plus sévère ;
- le langage dynamique ne fait que réécrire une constante fixe sous une forme plus compliquée ;
- aucune observable ne distingue la dynamique proposée d'un paramètre simplement choisi.

## 3. Pourquoi « la force faible » n'est pas un bouton unique

À basse énergie, l'intensité des processus faibles est souvent résumée par la constante de Fermi :

```text
G_F / sqrt(2) = 1 / (2 v^2)
```

au niveau arbre.

Mais le secteur électrofaible complet comporte au minimum :

```text
g, g'        : couplages de jauge
v            : échelle du régime électrofaible brisé
lambda, m²   : paramètres du potentiel du Higgs
Y_f          : matrices de Yukawa
M_W, M_Z     : masses dérivées des bosons de jauge
m_f          : masses fermioniques dérivées
G_F          : coefficient effectif basse énergie
```

Les relations au niveau arbre incluent :

```text
M_W = g v / 2
M_Z = sqrt(g² + g'²) v / 2
m_f = y_f v / sqrt(2)
G_F = 1 / (sqrt(2) v²)
```

Une variation de `g`, de `v`, des paramètres du potentiel ou des Yukawa ne produit donc pas la même histoire physique.

Le cycle refuse l'expression non qualifiée :

```text
la force faible varie
```

Elle doit être remplacée par une proposition explicite :

```text
quel objet varie ?
selon quelle variable ?
dans quelle théorie ?
avec quelles corrélations ?
```

## 4. Quatre formes de variation à distinguer

### 4.1 Dépendance à l'échelle de renormalisation

Les couplages renormalisés dépendent de l'échelle `mu` :

```text
g = g(mu)
g' = g'(mu)
y_f = y_f(mu)
lambda = lambda(mu)
```

Cette dépendance ne signifie pas qu'une constante change spontanément avec le temps cosmique. Elle exprime la manière dont une même théorie relie des descriptions à différentes échelles de résolution.

### 4.2 Dépendance thermique ou environnementale

Dans le plasma primordial, les masses effectives, le potentiel effectif et l'état du secteur de Higgs dépendent de la température.

```text
même lagrangien
+ état thermique différent
-> propriétés électrofaibles effectives différentes
```

Le crossover électrofaible appartient à cette catégorie.

### 4.3 Variation dynamique dans l'espace-temps

Une variation réelle exige en général un degré de liberté supplémentaire : dilaton, module, champ scalaire cosmologique ou autre secteur dynamique.

Forme schématique :

```text
phi(x)
-> g(phi), g'(phi), m²_H(phi), lambda(phi), Y_f(phi)
-> v(phi)
-> masses et taux faibles variables
```

Dans ce cas, les quantités électrofaibles suivent l'évolution de `phi(x)`.

### 4.4 Variation apparente ou inférentielle

Une variation reconstruite peut provenir :

- d'une dégénérescence entre paramètres ;
- d'un changement de modèle ;
- d'une dépendance mal séparée entre QCD, électromagnétisme et secteur de Higgs ;
- d'une erreur systématique ;
- d'une mauvaise identification de la grandeur réellement mesurée.

Le cycle doit donc toujours distinguer :

```text
variation de l'objet
≠
variation de l'estimation
```

## 5. Architecture minimale d'une théorie de variation

Une théorie ne peut pas se limiter à prescrire arbitrairement `G_F(t)`.

Elle doit fournir :

1. un porteur dynamique `phi` ;
2. une action ou des équations de mouvement ;
3. un potentiel `V(phi)` ;
4. des fonctions de couplage aux secteurs du Modèle standard ;
5. les conditions initiales ;
6. la rétroaction sur la matière et l'expansion ;
7. un mécanisme de stabilisation ou une raison de l'absence de stabilisation ;
8. des observables distinctives.

Forme de travail :

```text
S = S_gravitation
  + S_phi
  + S_SM[g(phi), g'(phi), m²_H(phi), lambda(phi), Y_f(phi)]
```

Cette écriture est seulement architecturale. Chaque modèle particulier doit préciser quelles fonctions varient réellement.

## 6. Constitution dynamique d'une fixité

Le terme central du cycle est :

> **constitution dynamique d'une fixité**

Il désigne un processus par lequel une grandeur variable devient quasi stationnaire relativement à un régime, une précision et une durée spécifiés.

Notation exploratoire :

```text
F_dyn(g | R, T, epsilon, Delta t)
```

avec :

- `g` : grandeur considérée ;
- `R` : régime ;
- `T` : transformations ou variables pertinentes ;
- `epsilon` : tolérance ;
- `Delta t` : durée sur laquelle la quasi-fixité est testée.

La fixité dynamique peut résulter de plusieurs mécanismes :

- minimum d'un potentiel ;
- friction cosmologique ;
- attracteur ;
- découplage ;
- masse élevée du porteur ;
- écrantage environnemental ;
- transition de phase ;
- principe de moindre couplage ;
- verrouillage par une symétrie.

## 7. Critère de réussite explicative

Une dynamique explique mieux une fixité qu'un paramètre choisi si elle montre qu'une région non négligeable de conditions initiales conduit au même régime tardif.

Le test doit donc comparer :

```text
largeur des conditions initiales
-> convergence ou divergence des trajectoires
-> valeur tardive
-> vitesse résiduelle de variation
```

Un attracteur est explicativement plus fort qu'une trajectoire unique ajustée à la main.

Mais une convergence tardive ne suffit pas si :

- le potentiel est lui-même finement réglé ;
- la valeur du minimum est arbitraire ;
- les couplages au Modèle standard sont ajustés ;
- le champ introduit une cinquième force exclue ;
- la stabilisation survient trop tard pour la nucléosynthèse ou la chimie.

## 8. Trois époques minimales

Le cycle séparera au moins :

### 8.1 Régime électrofaible primordial

Températures proches ou supérieures au crossover électrofaible. Les propriétés effectives du secteur de Higgs diffèrent de celles du vide tardif.

### 8.2 Nucléosynthèse primordiale

La valeur de `v`, les masses fermioniques, les taux faibles et les seuils QCD influencent les abondances légères.

Les travaux récents contraignent des écarts relatifs de `v` à l'époque de la BBN à un niveau typiquement percentuel, avec une dépendance aux abondances retenues et au traitement nucléaire.

### 8.3 Univers tardif

Les horloges atomiques, la spectroscopie astrophysique, les tests du principe d'équivalence et les recherches de cinquième force imposent des limites fortes à toute évolution résiduelle.

Le mécanisme recherché doit donc souvent produire :

```text
variation possible ou forte très tôt
-> ralentissement / stabilisation avant ou pendant la BBN
-> variation résiduelle extrêmement faible aujourd'hui
```

## 9. Relation avec le fine-tuning

Le cycle teste quatre effets possibles.

### 9.1 Dissolution partielle

Une valeur fixe supposée primitive devient la valeur tardive d'une dynamique.

### 9.2 Réduction

Un attracteur rend la valeur tardive peu sensible aux conditions initiales.

### 9.3 Déplacement

Le réglage migre vers le potentiel, les couplages ou le choix du porteur.

### 9.4 Aggravation

Le modèle ajoute de nouveaux paramètres et de nouvelles contraintes sans expliquer la valeur observée.

La question pertinente n'est donc pas :

```text
la constante est-elle devenue dynamique ?
```

mais :

```text
la dynamique réduit-elle réellement la contingence résiduelle ?
```

## 10. Premier programme de travail

### Dossier A — typologie des variations

Séparer RG, thermique, dynamique spatio-temporelle et variation inférentielle.

### Dossier B — mécanismes porteurs

Examiner :

- modèles de type Bekenstein pour les couplages de jauge ;
- dilatons et modules ;
- couplages entre un scalaire cosmologique et le secteur de Higgs ;
- mécanismes d'attracteur ou de moindre couplage ;
- écrantage et gel tardif.

### Dossier C — contraintes

Cartographier :

- BBN ;
- CMB et recombinaison ;
- spectres moléculaires ;
- horloges atomiques ;
- principe d'équivalence ;
- cinquièmes forces ;
- collisions et précision électrofaible.

### Dossier D — cas test complet

Construire un modèle minimal où un champ `phi` modifie un seul secteur, puis suivre :

```text
phi(t)
-> paramètre électrofaible
-> masses / taux
-> BBN
-> évolution tardive
-> contraintes locales
```

## 11. Conditions d'échec du cycle

Le cycle échoue si :

1. il confond évolution RG et variation temporelle ;
2. il traite le crossover thermique comme variation d'une loi fondamentale sans qualification ;
3. il écrit une fonction temporelle sans porteur dynamique ;
4. il varie `G_F` sans préciser `g`, `v`, masses et Yukawa ;
5. il ignore les corrélations induites dans QCD et les masses ;
6. il appelle attracteur une trajectoire unique ;
7. il néglige les contraintes de BBN et d'horloges ;
8. il présente une possibilité de modèle comme une propriété du Modèle standard ;
9. il déplace le réglage sans le reconnaître ;
10. il conclut à la variabilité réelle à partir d'une simple robustesse inférentielle.

## 12. Sources de départ

- Douglas J. Shaw et John D. Barrow, *Varying Couplings in Electroweak Theory*, arXiv:gr-qc/0412135.
- T. Damour et A. M. Polyakov, *The String Dilaton and a Least Coupling Principle*, arXiv:hep-th/9401069.
- Xavier Calmet, *Cosmological Evolution of the Higgs Boson's Vacuum Expectation Value*, arXiv:1707.06922.
- Anne-Katherine Burns et al., *Constraints on Variation of the Weak Scale from Big Bang Nucleosynthesis*, arXiv:2402.08626.
- Helen Meyer et Ulf-G. Meißner, *Improved Constraints on the Variation of the Weak Scale from Big Bang Nucleosynthesis*, arXiv:2403.09325.
- Nathaniel Sherrill et al., *Analysis of atomic-clock data to constrain variations of fundamental constants*, arXiv:2302.04565.
- A. C. O. Leite et C. J. A. P. Martins, *Current and future constraints on Bekenstein-type models for varying couplings*, arXiv:1607.01677.

## 13. Décision d'ouverture

Le cycle est ouvert comme enquête distincte.

> La question n'est plus seulement de savoir quelles valeurs pourraient être différentes, mais comment une histoire physique peut produire, modifier puis immobiliser les relations qui deviennent nos constantes effectives de régime.