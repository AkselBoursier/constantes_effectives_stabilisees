# Vérification physique — cycle cosmologique

## Statut

Ce document contrôle :

- [architecture-relationnelle-cosmologique.md](architecture-relationnelle-cosmologique.md)

Il ne vise pas à arbitrer les tensions observationnelles actuelles. Il vérifie le type des objets, leurs dépendances temporelles, leur statut de modèle et leurs voies d’accès.

## 1. Sources de contrôle

1. Particle Data Group, *Cosmological Parameters*, mise à jour 2025 :
   <https://pdg.lbl.gov/2025/reviews/rpp2025-rev-cosmological-parameters.pdf>
2. Particle Data Group, *Big-Bang Cosmology*, mise à jour 2025 :
   <https://pdg.lbl.gov/2025/reviews/rpp2025-rev-bbang-cosmology.pdf>
3. Particle Data Group, *Dark Energy*, mise à jour 2025 :
   <https://pdg.lbl.gov/2025/reviews/rpp2025-rev-dark-energy.pdf>
4. Planck Collaboration, *Planck 2018 results. VI. Cosmological parameters* :
   <https://arxiv.org/abs/1807.06209>

## 2. Portée du terme « paramètre cosmologique »

Le PDG souligne que l’expression couvre aujourd’hui :

- des nombres décrivant l’état global présent ;
- des fractions de densité ;
- des paramètres de fonctions ;
- des descripteurs statistiques des perturbations ;
- des paramètres dérivés ;
- des paramètres astrophysiques ou de nuisance.

### Décision

```text
paramètre cosmologique
≠
constante cosmologique
≠
constante physique.
```

L’appartenance à un vecteur d’ajustement ne fournit aucun statut ontologique commun.

## 3. `Lambda` dans l’action et les équations

L’action gravitationnelle avec constante cosmologique s’écrit :

```math
S=\frac{c^3}{16\pi G}
\int d^4x\sqrt{-g}\,(R-2\Lambda)+S_m.
```

Les équations sont :

```math
G_{\mu\nu}+\Lambda g_{\mu\nu}
=\frac{8\pi G}{c^4}T_{\mu\nu}.
```

Dans ce cadre, `Lambda` est un paramètre constant de la loi.

Il peut être déplacé au second membre et représenté comme un fluide effectif :

```math
\rho_\Lambda=\frac{\Lambda c^2}{8\pi G},
\qquad
p_\Lambda=-\rho_\Lambda c^2,
\qquad
w_\Lambda=-1.
```

### Limites de l’identification

Les formulations suivantes ne sont pas équivalentes sans hypothèses :

```text
terme géométrique Lambda
énergie du vide quantique
composante phénoménologique avec w = -1
accélération observée.
```

Une observation compatible avec `w=-1` ne détermine pas à elle seule l’interprétation ontologique de la composante.

### Décision

```text
Lambda : constante nomologique dans GR + Lambda ;
statut physique profond et valeur : non expliqués par le modèle.
```

## 4. `H(t)` et `H_0`

```math
H(t)=\frac{\dot a(t)}{a(t)},
\qquad
H_0=H(t_0).
```

Le PDG décrit `H_0` comme le paramètre de Hubble à l’époque présente.

### Décision

`H_0` est une condition d’état présente ou une valeur dérivée d’une solution cosmologique.

Il ne satisfait pas le test d’invariance sous évolution temporelle :

```math
H(t)\neq H_0
```

en général.

Le nom historique « constante de Hubble » n’est donc pas un classement physique suffisant.

## 5. Densités et paramètres `Omega_i`

Pour une composante `i` :

```math
\Omega_i(t)=\frac{\rho_i(t)}{\rho_{\mathrm{crit}}(t)},
\qquad
\rho_{\mathrm{crit}}(t)=\frac{3H^2(t)}{8\pi G}.
```

Les densités évoluent selon leur équation de conservation. Pour une composante non couplée avec `w_i` constant :

```math
\rho_i(a)\propto a^{-3(1+w_i)}.
```

Même si `rho_Lambda` est constante, `Omega_Lambda(a)` évolue parce que `rho_crit(a)` évolue.

### Décision

```text
Omega_i : rapports dynamiques et normalisés ;
Omega_i0 : valeurs d’état actuelles.
```

Ils ne sont pas des fractions intemporelles fixant une composition absolue de l’Univers.

## 6. `w`, `w_0` et `w_a`

L’équation d’état est :

```math
w(a)=\frac{p(a)}{\rho(a)c^2}.
```

Les modèles courants incluent :

```text
LambdaCDM : w = -1 par construction ;
wCDM      : w constant et libre ;
w0waCDM   : w(a) = w0 + wa(1-a).
```

### Décision

- `w=-1` est une conséquence du modèle de constante cosmologique ;
- `w` constant dans `wCDM` est une hypothèse paramétrique ;
- `w_0` et `w_a` sont les coordonnées d’une forme phénoménologique choisie.

Aucun de ces paramètres n’explique à lui seul la microphysique de l’énergie noire.

## 7. Spectre primordial, pivot et running

Une paramétrisation de puissance écrit :

```math
\mathcal P_\mathcal R(k)
=A_s
\left(\frac{k}{k_*}\right)^{n_s-1}.
```

Le pivot `k_*` est choisi conventionnellement, généralement près de la région où les paramètres sont le mieux contraints.

Si le spectre n’est pas une puissance exacte, on ajoute le running :

```math
\alpha_s^{\mathrm{prim}}
=\frac{dn_s}{d\ln k}
```

à ne pas confondre avec le couplage fort.

### Conséquences

- `A_s` est défini à un pivot ;
- `n_s` représente une pente locale ou approximée ;
- leurs valeurs et corrélations se transforment avec le pivot lorsque le modèle spectral est étendu ;
- ils paramètrent des conditions initiales statistiques plutôt qu’une constante de loi universelle.

### Décision

```text
A_s, n_s : paramètres primordiaux de modèle,
avec pivot et forme spectrale explicités.
```

## 8. `sigma_8` et `S_8`

`σ_8` est la dispersion linéaire actuelle du champ de densité de matière lissé par une fenêtre de rayon :

```text
8 h^-1 Mpc.
```

Il est dérivé du spectre de matière après évolution depuis les conditions initiales.

`S_8` est une combinaison construite, souvent :

```math
S_8=\sigma_8\sqrt{\frac{\Omega_m}{0.3}},
```

choisie parce que certaines observations de lentillage faible contraignent mieux cette direction dégénérée.

### Décision

```text
sigma_8 : paramètre dérivé / amplitude reconstruite à l’époque présente ;
S_8     : combinaison de paramètres adaptée à une dégénérescence observationnelle.
```

Ni l’un ni l’autre n’est une constante primitive de la dynamique.

## 9. Paramètres de base, paramètres dérivés et paramètres fixés

Le PDG rappelle qu’une paramétrisation cosmologique n’est pas unique.

Une même information physique peut être exprimée par :

- `Omega_i` ou `Omega_i h²` ;
- `H_0` ou `h` ;
- amplitude primordiale ou amplitude tardive ;
- âge de l’Univers ou combinaison de paramètres de base.

Certains paramètres sont fixés dans un ajustement parce que les données actuelles ne nécessitent pas leur variation ou parce qu’une hypothèse de référence est adoptée.

### Décision

```text
fixé dans un fit
≠
constant physiquement.
```

## 10. Chaîne inférentielle

La chaîne complète est :

```text
signal instrumental
        |
        v
réduction et calibration
        |
        v
observable astrophysique
        |
        v
modèle des sources et effets systématiques
        |
        v
prédiction cosmologique
        |
        v
vraisemblance
        |
        v
distribution postérieure des paramètres
        |
        v
paramètres dérivés et tensions comparatives.
```

### Décision

La cosmologie est fortement reconstructive. Les paramètres ne sont pas lus un à un directement dans les données.

Cette dépendance ne rend pas l’inférence arbitraire ; elle oblige à distinguer la robustesse des résultats de la nature des objets inférés.

## 11. Tensions

Une tension est une mesure de discordance entre distributions inférées sous des hypothèses spécifiées.

Elle dépend :

- des jeux de données ;
- des modèles ;
- du traitement des erreurs ;
- de la métrique statistique ;
- des paramètres comparés.

### Décision

```text
tension H_0 ou S_8 : propriété comparative des inférences,
non grandeur physique autonome.
```

## 12. Registre des décisions

| Proposition | Verdict |
|---|---|
| `Lambda` est constante dans GR + Lambda | confirmé relativement au modèle |
| `Lambda` explique sa propre valeur | refusé |
| `w=-1` prouve une interprétation unique en énergie du vide | refusé |
| `H_0` est une constante nomologique | refusé |
| `Omega_i` sont des fractions intemporelles | refusé |
| `A_s` et `n_s` sont indépendants du pivot et de la paramétrisation | refusé |
| `sigma_8` est une observable directe élémentaire | refusé |
| `S_8` est une constante physique | refusé |
| un paramètre fixé dans un fit est physiquement constant | refusé |
| une tension est un objet physique autonome | refusé |

## 13. Contrefactuels contrôlés

### 13.1 Autre époque de référence

Les valeurs de `H`, `Omega_i` et de la croissance changent. Le suffixe `0` sélectionne l’époque actuelle, il ne produit pas une invariance.

### 13.2 Autre pivot

Les paramètres du spectre sont recoordonnés. Le spectre représenté peut rester identique tandis que les nombres attribués à l’amplitude, la pente et le running changent.

### 13.3 Modèle étendu

Libérer `sum m_nu`, la courbure, `w` ou d’autres paramètres peut déplacer les distributions de `H_0`, `Omega_m` et `S_8` par dégénérescence.

### 13.4 Composante dynamique

Si la densité responsable de l’accélération évolue, `Lambda` ne décrit plus exactement cette composante ; un champ ou une fonction dynamique est requis.

## 14. Statut de l’architecture cosmologique

Le cycle confirme une architecture, mais pas une architecture de constantes.

La structure confirmée est :

```text
architecture inférentielle de modèles dynamiques
=
lois
+ conditions initiales
+ paramètres d’état
+ paramétrisations
+ évolution
+ observables reconstruites
+ voies d’accès
+ comparaisons de modèles.
```

### Décision

```text
architecture cosmologique inférentielle : confirmée ;
macro-architecture de constantes : refusée.
```

## 15. Résultat pour la fonction de fixité

La cosmologie fournit le principal cas négatif du projet.

Une grande partie des « fixités » y sont des opérations de méthode :

- fixer une époque ;
- fixer un pivot ;
- fixer un paramètre pendant un ajustement ;
- fixer une géométrie de référence ;
- choisir une combinaison adaptée à une dégénérescence.

Ces fixités sont nécessaires au calcul et à l’inférence. Elles ne sont pas des constances physiques.

### Correction

La fonction de fixité doit toujours indiquer son niveau :

```text
physique
nomologique
paramétrique
référentiel
statistique
procédural
métrologique.
```

## 16. Conclusion de vérification

Le corpus cosmologique est l’un des plus solides quant à la différenciation des objets. Sa faiblesse ancienne venait de leur réintégration finale dans une macro-architecture de stabilisation trop générale.

La refonte conserve les distinctions et retire cette réabsorption.

> Dans le cycle examiné, `Lambda` est le seul candidat direct à la constance physique, et seulement dans un modèle spécifié. Tous les autres objets étudiés décrivent un état, une fonction, une condition initiale, une reconstruction ou une relation entre inférences.
