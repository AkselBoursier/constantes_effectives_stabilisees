# Dossier de transfert — architecture relationnelle cosmologique

## Statut

Ce document ouvre la reprise du cycle cosmologique.

Il part principalement de :

- [Synthese_cycle_cosmologique_v0_1.md](Synthese_cycle_cosmologique_v0_1.md)

L’ancienne conclusion d’une macro-architecture cosmologique confirmée est suspendue. La cosmologie sert ici de test critique : le cadre doit probablement exclure du noyau des constantes la majorité des objets étudiés.

## 1. Question du dossier

> Parmi les grandeurs couramment appelées constantes ou paramètres cosmologiques, lesquelles peuvent réellement recevoir un statut de constance, et lesquelles appartiennent à l’état du cosmos, à son histoire, aux conditions initiales ou à la reconstruction des observations ?

Question complémentaire :

> Que gagne-t-on à décrire séparément la dynamique cosmique, le modèle paramétrique et le réseau d’accès observationnel ?

## 2. Corpus repris

Le cycle antérieur traitait :

```text
Lambda
H_0
Omega_i
w
A_s, n_s
sigma_8, S_8
```

Il avait déjà établi plusieurs distinctions robustes :

- `H_0` est la valeur actuelle de `H(t)` ;
- `Omega_i` est un rapport normalisé ;
- `w` est une relation ou paramétrisation d’état ;
- `A_s` et `n_s` paramètrent le spectre primordial ;
- `sigma_8` et `S_8` sont des amplitudes reconstruites ;
- les tensions appartiennent au réseau d’accès et de modèles.

Ces distinctions sont conservées. Leur classement comme fonctions d’une architecture générale n’est pas présupposé.

## 3. Règle d’entrée

Chaque objet sera soumis à cinq questions :

1. appartient-il aux équations de loi ou à une solution particulière ?
2. varie-t-il avec le temps, le facteur d’échelle ou la position ?
3. dépend-il d’une normalisation, d’un pivot ou d’une paramétrisation ?
4. est-il observé directement ou reconstruit dans un modèle ?
5. que faudrait-il changer pour que son statut ou sa valeur change ?

## 4. Chaîne A — dynamique du fond cosmologique

Dans un modèle FLRW, l’expansion est décrite par :

```math
H(t)=\frac{\dot a(t)}{a(t)}.
```

L’équation de Friedmann s’écrit schématiquement :

```math
H^2(t)=\frac{8\pi G}{3}\rho(t)
-\frac{k c^2}{a^2(t)}
+\frac{\Lambda c^2}{3}.
```

Chaîne relationnelle :

```text
lois gravitationnelles
+ contenu matériel et énergétique
+ courbure
+ conditions initiales
        |
        v
solution a(t)
        |
        v
H(t), distances et histoire d’expansion
        |
        v
valeurs à une époque donnée, dont H_0
```

Cette chaîne sépare immédiatement :

```text
paramètres de loi
≠
conditions de solution
≠
valeurs d’état actuelles.
```

## 5. `Lambda` — seul candidat direct du noyau

Dans la relativité générale avec constante cosmologique :

```math
G_{\mu\nu}+\Lambda g_{\mu\nu}
=\frac{8\pi G}{c^4}T_{\mu\nu}.
```

`Lambda` est un paramètre du terme géométrique et est traité comme constant dans ce modèle.

On peut lui associer une densité :

```math
\rho_\Lambda=\frac{\Lambda c^2}{8\pi G}
```

selon les conventions d’unités.

### Distinctions obligatoires

```text
Lambda
≠
rho_Lambda
≠
Omega_Lambda(t)
≠
w.
```

`Omega_Lambda(t)` dépend de la densité critique, donc de `H(t)`, même si `rho_Lambda` est constante dans le modèle.

### Décision provisoire

```text
Lambda : candidat à la constance nomologique dans GR + Lambda.
```

Cette décision reste relative au modèle. Une composante d’énergie noire dynamique n’est pas une constante cosmologique.

## 6. `H_0` — valeur d’état actuelle

```math
H_0=H(t_0).
```

`H_0` caractérise l’expansion à l’époque présente. Il n’est pas invariant sous :

```text
t_0 -> t.
```

### Décision

```text
H_0 : exclu du noyau des constantes.
```

Le terme historique « constante de Hubble » ne suffit pas à lui conférer un statut nomologique.

Les tensions sur `H_0` concernent :

- les voies d’accès ;
- les calibrations ;
- les hypothèses de modèle ;
- d’éventuelles insuffisances physiques.

Elles ne constituent pas une variation temporelle observée de `H_0`.

## 7. `Omega_i` — rapports d’état normalisés

```math
\Omega_i(t)=\frac{\rho_i(t)}{\rho_{\mathrm{crit}}(t)},
\qquad
\rho_{\mathrm{crit}}(t)=\frac{3H^2(t)}{8\pi G}.
```

Les `Omega_i` dépendent :

- des densités des composantes ;
- de l’époque ;
- de `H(t)` ;
- du modèle de décomposition.

### Décision

```text
Omega_i : exclus comme constantes primitives.
```

Les valeurs `Omega_{i0}` sont des paramètres d’état actuels normalisés.

## 8. `w` — relation d’état ou paramétrisation

```math
w=\frac{p}{\rho c^2}
```

selon les conventions.

Pour une constante cosmologique stricte :

```math
w=-1.
```

Mais :

```text
w = -1
≠
identité de w avec Lambda.
```

Dans `wCDM`, `w` est supposé constant comme paramètre phénoménologique. Dans `w_0w_aCDM`, il varie selon une forme choisie.

### Décision provisoire

```text
w : relation d’état ;
constance éventuelle = hypothèse de modèle, non statut universel.
```

## 9. `A_s` et `n_s` — paramétrisation primordiale

Le spectre primordial est souvent écrit :

```math
\mathcal P_\mathcal R(k)
=A_s\left(\frac{k}{k_*}\right)^{n_s-1}
```

à un pivot `k_*`.

`A_s` dépend de la convention de normalisation et du pivot ; `n_s` décrit une pente locale dans une paramétrisation sans running ou avec running négligé.

### Décision

```text
A_s, n_s : paramètres du spectre primordial,
non constantes physiques universelles.
```

Ils peuvent être les paramètres d’entrée d’un modèle inflationnaire ou phénoménologique sans constituer des constantes de loi.

## 10. `sigma_8` et `S_8` — reconstructions tardives

`σ_8` mesure l’amplitude rms des fluctuations de matière lissées à l’échelle conventionnelle `8 h^-1 Mpc`.

```math
S_8=\sigma_8\sqrt{\frac{\Omega_m}{0.3}}.
```

Ces grandeurs dépendent :

- du spectre de matière ;
- de l’histoire de croissance ;
- de `h` et `Omega_m` ;
- du modèle reliant les observables aux perturbations ;
- des conventions de lissage et de combinaison.

### Décision

```text
sigma_8, S_8 : observables ou paramètres reconstruits,
exclus comme constantes primitives.
```

Une tension `S_8` est une propriété comparative des inférences, non une grandeur physique autonome.

## 11. Trois chaînes à séparer

### 11.1 Chaîne physique

```text
lois + contenu + conditions initiales
-> évolution du fond et des perturbations
-> observables possibles.
```

### 11.2 Chaîne paramétrique

```text
choix du modèle
-> paramètres libres
-> solution numérique
-> prédictions.
```

### 11.3 Chaîne inférentielle

```text
données brutes
+ calibration
+ fonctions de vraisemblance
+ modèles astrophysiques
+ modèle cosmologique
-> distributions postérieures des paramètres.
```

La valeur reconstruite d’un paramètre ne doit pas être confondue avec un accès direct à un objet isolé.

## 12. Tableau provisoire

| Objet | Type après reprise | Statut de constance provisoire |
|---|---|---|
| `Lambda` | paramètre de loi dans GR + Lambda | candidat relatif au modèle |
| `H_0` | valeur d’état actuelle | refusé |
| `Omega_i0` | rapports d’état normalisés | refusés |
| `w` | relation / paramétrisation d’état | hypothèse locale, non universelle |
| `A_s`, `n_s` | paramètres primordiaux à pivot donné | refusés comme constantes universelles |
| `sigma_8`, `S_8` | reconstructions tardives | refusés |
| tension `H_0` ou `S_8` | relation entre inférences | refusée comme objet constant |

## 13. Contrefactuels initiaux

### 13.1 Changement d’époque

`H_0`, `Omega_i0` et les amplitudes de croissance changent de statut ou de valeur lorsque `t_0` est remplacé par une autre époque.

### 13.2 Changement de pivot

Les valeurs numériques de `A_s` et des paramètres spectraux peuvent être transformées lorsque `k_*` change, sans changement du spectre physique représenté.

### 13.3 Changement de paramétrisation de l’énergie noire

Une même expansion approchée peut être représentée par `Lambda`, `w` constant ou `w(a)` dans des plages de données limitées, avec des interprétations physiques différentes.

### 13.4 Changement de modèle cosmologique

Les valeurs postérieures de `H_0`, `Omega_m`, `S_8` ou `sum m_nu` peuvent se déplacer lorsque le modèle est étendu, même si les données brutes ne changent pas.

### 13.5 Si `Lambda` variait

Une dépendance spatio-temporelle ne serait plus une constante cosmologique stricte ; elle devrait être décrite par un champ, une fonction ou un secteur dynamique supplémentaire.

## 14. Fonction de fixité

La cosmologie révèle plusieurs fixités procédurales :

- pivot fixé ;
- époque de référence fixée ;
- paramètre tenu constant dans un modèle ;
- géométrie ou contenu fixé pendant un ajustement ;
- combinaison choisie pour réduire une dégénérescence.

Ces fixités rendent l’inférence possible, mais ne transforment pas automatiquement leurs objets en constantes physiques.

### Décision provisoire

```text
la cosmologie est le domaine où la fonction de fixité
risque le plus de devenir une propriété de la procédure
plutôt qu’une propriété de l’objet.
```

## 15. Conditions d’échec du dossier

Le dossier échoue si :

- `H_0` est restauré comme constante fondamentale ;
- les `Omega_i` sont traités comme composition fixe intemporelle ;
- `w=-1` est pris comme explication de l’énergie noire ;
- les paramètres primordiaux sont confondus avec des observables directes ;
- `S_8` est transformé en constante physique ;
- une tension devient une famille ou un objet physique autonome ;
- la dépendance au modèle est décrite comme une simple incertitude instrumentale ;
- `Lambda` est déclaré expliqué parce qu’il ajuste l’accélération.

## 16. Travail de vérification

La phase suivante devra :

1. contrôler les définitions auprès du PDG et de sources cosmologiques de référence ;
2. préciser le statut de `Lambda` dans les équations et dans l’action ;
3. distinguer `Lambda`, densité du vide et énergie noire phénoménologique ;
4. contrôler les dépendances temporelles de `H`, `Omega_i` et de la croissance ;
5. préciser pivot, normalisation et dépendances de `A_s`, `n_s`, `sigma_8`, `S_8` ;
6. produire une évaluation du pouvoir explicatif indépendante des tensions actuelles.

## 17. Décision provisoire

```text
Cycle cosmologique : très bon corpus de distinctions ;
ancienne macro-architecture non reprise ;
un seul candidat direct à la constance, Lambda, sous modèle spécifié.
```

> La cosmologie ne réunit pas une famille de constantes. Elle organise une inférence sur une histoire dynamique au moyen de paramètres hétérogènes dont la plupart ne sont constants que parce qu’une époque, un pivot ou un modèle ont été fixés.
