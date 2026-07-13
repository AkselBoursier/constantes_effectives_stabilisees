# Typologie des variations électrofaibles

## Statut

Cette fiche établit les distinctions minimales nécessaires avant toute affirmation selon laquelle « l'interaction faible varie ».

## 1. Principe général

Une même notation variable peut recouvrir des phénomènes différents :

```text
g(mu)     : dépendance à l'échelle de renormalisation
g(T)      : quantité effective dans un milieu thermique
g(phi(x)) : variation spatio-temporelle portée par un champ
ĝ(data)   : estimation reconstruite à partir de données
```

Ces quatre écritures ne doivent pas être interprétées comme quatre versions équivalentes d'une constante qui changerait.

## 2. Dépendance à l'échelle de renormalisation

### 2.1 Nature

Les paramètres renormalisés évoluent avec l'échelle de résolution `mu` selon des équations de groupe de renormalisation.

```text
mu d g / d mu = beta_g
mu d y_f / d mu = beta_yf
mu d lambda / d mu = beta_lambda
```

### 2.2 Ce qui varie

Ce sont les paramètres d'une description renormalisée lorsqu'on change d'échelle de calcul.

### 2.3 Ce qui ne suit pas

On ne peut pas conclure directement :

```text
le couplage change avec le temps cosmique
```

Le passage de `mu` à `t` exige une relation physique supplémentaire, par exemple une échelle caractéristique dépendant de la température ou de l'énergie du processus.

### 2.4 Statut pour le projet

```text
variation RG = variation de description contrôlée
```

Elle constitue un cas de dépendance de régime, non une preuve de variation d'une loi dans l'espace-temps.

## 3. Dépendance thermique

### 3.1 Nature

À température finie, le potentiel effectif, les masses thermiques et les taux de réaction dépendent de l'état du plasma.

Forme schématique :

```text
V_eff(H, T)
```

Le minimum pertinent et les observables thermodynamiques évoluent avec `T`.

### 3.2 Crossover électrofaible

Dans le Modèle standard pour les masses mesurées, la transition électrofaible est un crossover plutôt qu'une transition de phase du premier ordre.

La description doit privilégier des observables thermodynamiques et des quantités invariantes de jauge.

### 3.3 Ce qui varie

- masses effectives dans le plasma ;
- condensats ou observables associées au secteur de Higgs ;
- taux sphalérons et taux de réaction ;
- contenu pertinent des degrés de liberté.

### 3.4 Ce qui ne suit pas

La dépendance thermique ne prouve pas que les paramètres nus ou renormalisés du lagrangien sont des champs cosmologiques variables.

### 3.5 Statut pour le projet

```text
variation thermique = même théorie, état physique différent
```

Elle offre néanmoins un premier exemple de constitution historique d'un régime où certaines relations deviennent opératoires.

## 4. Variation dynamique dans l'espace-temps

### 4.1 Nature

Une quantité du Modèle standard dépend d'un champ additionnel `phi(x)` :

```text
g -> g(phi)
g' -> g'(phi)
m_H² -> m_H²(phi)
lambda -> lambda(phi)
Y_f -> Y_f(phi)
```

### 4.2 Conséquence

La valeur locale du champ `phi` modifie les masses, les couplages ou les taux :

```text
phi(x)
-> secteur électrofaible local
-> observables locales
```

### 4.3 Conditions de cohérence

Il faut spécifier :

- la covariance de la théorie ;
- les identités de jauge ;
- la conservation de l'énergie-impulsion totale ;
- les termes cinétiques et le potentiel de `phi` ;
- les corrections quantiques ;
- les couplages induits aux autres secteurs.

### 4.4 Statut pour le projet

```text
variation dynamique = nouvelle physique testable
```

Elle n'appartient pas au Modèle standard minimal sans extension.

## 5. Variation spatiale par domaines

### 5.1 Nature

Un champ peut prendre différentes valeurs dans des régions séparées :

```text
phi = phi_1 dans un domaine
phi = phi_2 dans un autre domaine
```

### 5.2 Origines possibles

- brisure spontanée avec minima multiples ;
- transition de phase ;
- défauts topologiques ;
- conditions initiales inflationnaires ;
- paysage de vides.

### 5.3 Difficultés

- énergie des parois ;
- stabilité des domaines ;
- causalité de leur formation ;
- signatures observationnelles ;
- définition d'une mesure sur les domaines.

### 5.4 Statut pour le projet

Ce cas relie variation intra-univers et comparaison de domaines, mais ne doit pas être assimilé automatiquement à un multivers statistique.

## 6. Variation oscillante

### 6.1 Nature

Un champ ultraléger cohérent peut osciller :

```text
phi(t) ≈ phi_0 cos(m_phi t)
```

et induire :

```text
delta alpha / alpha

delta mu / mu

delta m_f / m_f
```

oscillants.

### 6.2 Accès

Les horloges atomiques et la spectroscopie cherchent des modulations périodiques ou transitoires.

### 6.3 Statut

La moyenne temporelle peut paraître fixe alors qu'une petite variation périodique subsiste.

Cela oblige à inclure la résolution temporelle dans toute attribution de constance.

## 7. Variation environnementale et écrantage

### 7.1 Nature

La valeur ou la masse effective du porteur dépend de la densité locale :

```text
V_eff(phi) = V(phi) + rho A(phi)
```

### 7.2 Conséquence

Le champ peut évoluer cosmologiquement mais être presque immobilisé dans les environnements denses où les expériences sont réalisées.

### 7.3 Risque méthodologique

Une absence de variation locale ne prouve pas nécessairement une absence de variation cosmologique.

Inversement, un modèle d'écrantage doit être calculé et ne peut servir d'excuse générale contre toutes les contraintes.

## 8. Variation inférentielle

### 8.1 Nature

Une analyse peut reconstruire une valeur différente lorsque changent :

- le modèle cosmologique ;
- les jeux de données ;
- les calibrations ;
- les hypothèses nucléaires ;
- les paramètres corrélés.

### 8.2 Exemple de structure

```text
données spectroscopiques
+ modèle moléculaire
+ étalonnage
-> contrainte sur Delta mu / mu
```

### 8.3 Statut

```text
robustesse ou tension de l'estimation
≠
variation physique démontrée
```

## 9. Matrice de distinction

| Forme | Variable indépendante | Porteur physique nouveau ? | Signification |
|---|---|---:|---|
| RG | échelle `mu` | non | changement de résolution |
| thermique | température / état du milieu | non nécessairement | même théorie dans un autre régime |
| dynamique temporelle | champ `phi(t)` | généralement oui | nouvelle physique cosmologique |
| dynamique spatiale | champ `phi(x)` | généralement oui | inhomogénéité ou domaines |
| oscillante | phase d'un champ cohérent | oui | modulation périodique |
| environnementale | densité / courbure locale | oui | valeur effective dépendante du milieu |
| inférentielle | données et modèle | non | changement de reconstruction |

## 10. Application aux objets électrofaibles

### 10.1 Couplages `g` et `g'`

Ils courent avec l'échelle. Une variation spatio-temporelle demande des fonctions de jauge dépendant d'un champ et une formulation cohérente de la théorie de jauge.

### 10.2 Valeur `v`

`v` peut désigner :

- une échelle dérivée de `G_F` dans un schéma donné ;
- un paramètre du vide au niveau arbre ;
- une quantité effective thermique ;
- une valeur dépendante d'un autre champ dans une extension.

Ces usages ne sont pas interchangeables.

### 10.3 `G_F`

`G_F` est un coefficient effectif basse énergie. Sa variation peut résulter de variations de `v`, de corrections radiatives, de nouvelles interactions ou d'une mauvaise réduction effective.

### 10.4 Yukawa

Une variation de `Y_f` modifie les masses et les couplages Higgs-fermions. Elle peut aussi induire des changements de saveur si les textures varient, ce qui est beaucoup plus contraignant qu'une variation commune de toutes les masses.

## 11. Test décisionnel

Avant d'utiliser le mot variation, une fiche doit répondre :

```text
1. variable de variation ?
2. objet qui varie ?
3. porteur dynamique ?
4. équation d'évolution ?
5. corrélations induites ?
6. observable ?
7. régime et résolution ?
```

## 12. Conclusion

> Une grandeur peut être dépendante de l'échelle, de la température, d'un champ cosmologique, du milieu ou de la procédure d'inférence. Le mot « variation » n'est physiquement informatif qu'après identification de cette architecture.

## 13. Sources de contrôle

- Douglas J. Shaw et John D. Barrow, *Varying Couplings in Electroweak Theory*, arXiv:gr-qc/0412135.
- T. Damour et A. M. Polyakov, *The String Dilaton and a Least Coupling Principle*, arXiv:hep-th/9401069.
- Nathaniel Sherrill et al., *Analysis of atomic-clock data to constrain variations of fundamental constants*, arXiv:2302.04565.
- A. C. O. Leite et C. J. A. P. Martins, *Current and future constraints on Bekenstein-type models for varying couplings*, arXiv:1607.01677.