# Modèle test — scalaire cosmologique couplé au Higgs

## Statut

Cette fiche définit un modèle minimal destiné à tester la constitution dynamique d'une fixité électrofaible.

Il ne s'agit pas d'une théorie privilégiée ni d'une proposition phénoménologique déjà validée.

## 1. But du modèle

Construire le cas le plus simple où :

```text
champ cosmologique phi(t)
-> terme quadratique effectif du Higgs
-> valeur v(phi)
-> masses et G_F
-> contraintes BBN et tardives
```

Le modèle doit permettre de répondre :

> Une dynamique de `phi` peut-elle conduire une large gamme de conditions initiales vers une valeur tardive de `v` suffisamment fixe, sans réintroduire un réglage équivalent dans le portail ou le potentiel ?

## 2. Potentiel minimal

On considère un singulet réel `phi` avec une symétrie `Z_2` :

```text
phi -> -phi
```

Potentiel au niveau arbre :

```text
V(H, phi) =
  - mu_H² H†H
  + lambda_H (H†H)²
  + V_phi(phi)
  + lambda_Hphi phi² H†H
```

avec, dans le modèle le plus simple :

```text
V_phi(phi) = m_phi² phi² / 2 + lambda_phi phi⁴ / 4
```

## 3. Échelle électrofaible dépendante de phi

Dans une approximation homogène et au niveau arbre, le terme quadratique effectif du Higgs est :

```text
mu_eff²(phi) = mu_H² - lambda_Hphi phi²
```

Lorsque `mu_eff² > 0`, le minimum brisé vérifie :

```text
v²(phi) = [mu_H² - lambda_Hphi phi²] / lambda_H
```

sous les conventions de cette fiche.

Le modèle récupère la valeur standard lorsque :

```text
lambda_Hphi phi² << mu_H²
```

## 4. Quantités dérivées

En maintenant provisoirement fixes les couplages de jauge et les Yukawa :

```text
M_W(phi) = g v(phi) / 2
M_Z(phi) = sqrt(g² + g'²) v(phi) / 2
m_f(phi) = y_f v(phi) / sqrt(2)
G_F(phi) = 1 / [sqrt(2) v²(phi)]
```

Cette coupe produit une variation corrélée de toutes les masses électrofaibles.

Elle ne permet pas de varier `G_F` tout en conservant arbitrairement toutes les masses constantes.

## 5. Équation cosmologique de phi

Pour un champ homogène dans un espace FLRW :

```text
phi_ddot + 3 H phi_dot + d V_eff(phi, T) / d phi = 0
```

avec :

```text
V_eff(phi, T) = V_phi(phi) + lambda_Hphi phi² <H†H>_T + corrections thermiques
```

La valeur thermique de `<H†H>_T` modifie la masse effective de `phi`.

Le secteur de Higgs et `phi` doivent donc être résolus conjointement autour du crossover.

## 6. Trois régimes qualitatifs

### 6.1 Avant le crossover électrofaible

```text
<H†H>_T faible ou différent du vide tardif
```

Le champ évolue principalement sous `V_phi` et les corrections thermiques.

### 6.2 Après le crossover

Le condensat électrofaible contribue au potentiel effectif de `phi` :

```text
m_phi,eff² ≈ m_phi² + lambda_Hphi v²
```

Le champ peut devenir plus lourd et se stabiliser plus rapidement.

### 6.3 Univers tardif

Si `phi` est proche d'un minimum et suffisamment massif :

```text
phi_dot -> 0
v_dot / v -> 0
```

La quasi-fixité tardive devient testable par les horloges et la spectroscopie.

## 7. Scénarios à comparer

### Scénario A — minimum unique lourd

`phi` tombe rapidement vers zéro après le crossover.

Avantage : stabilisation simple.

Risque : peu de variation cosmologique et absence de gain sur l'origine de `mu_H²`.

### Scénario B — champ gelé puis libéré

La friction cosmologique maintient `phi` loin du minimum, puis `H` devient comparable à sa masse.

Avantage : histoire non triviale.

Risque : forte dépendance aux conditions initiales.

### Scénario C — attracteur de suivi

Un potentiel non quadratique produit une trajectoire de suivi avant la stabilisation.

Avantage : réduction possible de la sensibilité initiale.

Risque : choix du potentiel et stabilité quantique.

### Scénario D — transition induite par le Higgs

Le changement de `<H†H>_T` modifie le potentiel de `phi` et déclenche son verrouillage.

Avantage : lien constitutif direct entre histoire thermique et fixité tardive.

Risque : paramètres du portail ajustés pour obtenir la bonne époque.

## 8. Quantités à calculer

### 8.1 Dynamique de fond

```text
phi(t)
phi_dot(t)
H(t)
rho_phi(t)
```

### 8.2 Secteur électrofaible

```text
v(t)
G_F(t)
M_W(t)
M_Z(t)
m_e(t), m_q(t)
```

### 8.3 Sensibilités

```text
d ln v / d ln phi
d ln G_F / d ln phi
```

### 8.4 Observables

- taux neutron-proton ;
- durée de vie du neutron ;
- abondances BBN ;
- masse de l'électron à la recombinaison ;
- dérive tardive de rapports de fréquences ;
- cinquième force induite par le mélange Higgs-phi ;
- contribution de `phi` à la densité cosmologique.

## 9. Premier test d'attracteur

Échantillonner un ensemble de conditions initiales :

```text
{phi_i, phi_dot_i}
```

et mesurer la dispersion tardive :

```text
Delta v_final / v_final
```

Le mécanisme est attractif si une région étendue de conditions initiales conduit à :

```text
|Delta v_final / v_final| < epsilon
```

avec `epsilon` déterminé par les contraintes observationnelles.

## 10. Mesure de migration du réglage

Comparer deux descriptions.

### Description standard

```text
mu_H² choisi
-> v observé
```

### Description dynamique

```text
{mu_H², lambda_Hphi, m_phi, lambda_phi, phi_i, phi_dot_i}
-> v observé
```

La dynamique réduit le réglage seulement si :

- le bassin de conditions initiales est large ;
- les paramètres du portail ne doivent pas être choisis dans une région plus étroite ;
- la valeur finale n'est pas seulement imposée par `mu_H²` ;
- les contraintes ne forcent pas `lambda_Hphi` vers zéro au point de rendre le mécanisme inopérant.

## 11. Corrections et complications nécessaires

Le modèle complet devra intégrer :

- potentiel effectif thermique ;
- corrections radiatives au portail ;
- mélange scalaire après brisure ;
- stabilité du potentiel ;
- seuils QCD lorsque les masses des quarks varient ;
- dépendance de la durée de vie du neutron ;
- contraintes de cinquième force ;
- éventuelle production de `phi`.

## 12. Cas négatifs

Le modèle échoue comme explication de la fixité si :

1. `lambda_Hphi` doit être pratiquement nul ;
2. la valeur finale dépend directement de `phi_i` ;
3. la BBN exclut toute variation utile ;
4. `phi` domine l'énergie cosmologique au mauvais moment ;
5. le mélange scalaire est exclu ;
6. les corrections quantiques déstabilisent la hiérarchie ;
7. le nombre de paramètres libres augmente sans réduction mesurable de sensibilité.

## 13. Extension ultérieure

Après ce cas minimal, on pourra comparer :

- variation de `g` par fonction de jauge ;
- variation commune des Yukawa ;
- moindre couplage de type dilaton ;
- écrantage environnemental ;
- domaines spatiaux ;
- dynamique couplée à la courbure.

## 14. Verdict d'ouverture

> Le portail scalaire-Higgs fournit un laboratoire calculable pour tester la différence entre une valeur simplement choisie et une fixité constituée par une histoire dynamique. Il ne constitue une amélioration explicative que si la convergence des trajectoires compense réellement le coût en paramètres et en contraintes nouvelles.