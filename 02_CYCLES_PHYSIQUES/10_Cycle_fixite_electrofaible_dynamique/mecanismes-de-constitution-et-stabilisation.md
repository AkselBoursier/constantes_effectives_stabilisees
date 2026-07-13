# Mécanismes de constitution et de stabilisation électrofaible

## Statut

Cette fiche cartographie les mécanismes par lesquels une quantité électrofaible dépendante d'un champ ou d'un régime pourrait devenir quasi fixe.

Elle ne cherche pas encore à sélectionner un modèle favori.

## 1. Schéma minimal

On introduit un degré de liberté `phi` :

```text
phi(x)
-> fonctions de couplage B_i(phi)
-> paramètres électrofaibles
-> masses et taux
```

Une action schématique est :

```text
S = ∫ d⁴x sqrt(-g) [
    M_Pl² R / 2
  - (∂phi)² / 2
  - V(phi)
  + L_SM(phi)
]
```

avec, par exemple :

```text
L_SM(phi) ⊃
- B_W(phi) W² / 4
- B_Y(phi) B² / 4
- m_H²(phi) H†H
- lambda(phi) (H†H)²
- Y_f(phi) fermions × H
```

Chaque choix produit des corrélations différentes.

## 2. Minimum simple d'un potentiel

### 2.1 Mécanisme

Le champ évolue vers un minimum :

```text
V'(phi_*) = 0
V''(phi_*) > 0
```

La quantité électrofaible devient :

```text
g_eff = g(phi_*)
```

### 2.2 Force explicative

Le mécanisme peut expliquer l'arrêt de l'évolution.

### 2.3 Limite

Il n'explique pas automatiquement :

- pourquoi le minimum se trouve à la valeur observée ;
- pourquoi le champ l'atteint avant la BBN ;
- pourquoi les couplages à la matière sont suffisamment faibles ;
- pourquoi les corrections quantiques ne déplacent pas le minimum.

### 2.4 Test

Comparer la taille du bassin d'attraction à la précision requise sur la valeur tardive.

## 3. Friction cosmologique

### 3.1 Équation

Pour un champ homogène :

```text
phi_ddot + 3 H phi_dot + V'(phi) = source_matière
```

Le terme `3 H phi_dot` ralentit l'évolution.

### 3.2 Effet

À grande expansion, le champ peut être gelé sans se trouver exactement au minimum.

### 3.3 Distinction

```text
gel cinématique
≠
stabilisation au minimum
```

Un champ gelé peut recommencer à évoluer lorsque `H` diminue.

### 3.4 Risque

La quasi-fixité actuelle peut dépendre fortement des conditions initiales.

## 4. Attracteur dynamique

### 4.1 Définition

Un attracteur est une trajectoire ou un point vers lequel converge une famille de conditions initiales.

### 4.2 Critère fort

```text
ensemble étendu de conditions initiales
-> même trajectoire tardive
```

### 4.3 Gain pour le fine-tuning

Un attracteur peut réduire la sensibilité aux conditions initiales.

### 4.4 Limite

Il faut encore expliquer :

- la forme du potentiel ;
- les fonctions de couplage ;
- la valeur de l'attracteur ;
- la stabilité aux corrections quantiques.

## 5. Principe de moindre couplage

### 5.1 Idée

Dans les modèles de type Damour-Polyakov, l'évolution cosmologique peut conduire un dilaton vers une valeur où ses couplages à la matière sont minimisés.

```text
phi(t)
-> minimum commun des fonctions de couplage
-> découplage approximatif de la matière
```

### 5.2 Intérêt

Le même mécanisme peut produire :

- une variation ancienne ;
- une variation résiduelle faible ;
- une compatibilité approximative avec le principe d'équivalence.

### 5.3 Condition forte

Les fonctions de couplage doivent posséder une structure suffisamment universelle ou corrélée.

### 5.4 Risque de migration

Le réglage peut migrer vers l'hypothèse d'un minimum commun.

## 6. Masse élevée du porteur

### 6.1 Mécanisme

Si :

```text
m_phi² = V''(phi_*)
```

est grand, les excitations de `phi` sont de courte portée et l'évolution tardive est fortement supprimée.

### 6.2 Avantage

Les cinquièmes forces sont réduites.

### 6.3 Limite

Un champ lourd peut difficilement évoluer sur des temps cosmologiques tardifs.

Le modèle doit donc organiser une histoire :

```text
champ mobile tôt
-> masse ou minimum modifié
-> champ lourd tard
```

## 7. Écrantage environnemental

### 7.1 Principe

Le milieu modifie le potentiel effectif :

```text
V_eff(phi, rho) = V(phi) + rho A(phi)
```

### 7.2 Conséquence

Le champ peut être :

- léger et mobile dans le vide cosmologique ;
- lourd ou faiblement couplé dans un laboratoire dense.

### 7.3 Types généraux

- chameleon : masse dépendante de la densité ;
- symmetron : couplage dépendant du régime de symétrie ;
- mécanismes de type Vainshtein : suppression non linéaire des gradients.

### 7.4 Prudence

Ces mécanismes sont généraux et ne garantissent pas qu'une variation électrofaible précise soit viable.

Ils doivent être combinés à un couplage explicite au secteur de Higgs ou de jauge.

## 8. Transition de phase et verrouillage

### 8.1 Architecture

Un champ peut passer d'un régime à un autre :

```text
haute température : minimum A
refroidissement : modification de V_eff
basse température : minimum B
```

### 8.2 Effet

Une quantité électrofaible peut être différente avant et après la transition.

### 8.3 Exemple de principe

Le secteur de Higgs lui-même change de régime thermique au crossover électrofaible.

Une extension peut ajouter une transition plus tardive qui modifie les paramètres du Higgs.

### 8.4 Risques

- défauts topologiques ;
- énergie latente ;
- production d'entropie ;
- domaines ;
- signatures dans la BBN ou le CMB ;
- réglage de la température critique.

## 9. Couplage à la courbure

### 9.1 Forme

```text
xi phi² R
```

ou :

```text
xi H†H R
```

### 9.2 Effet

La courbure cosmologique peut déplacer le minimum effectif du champ.

### 9.3 Intérêt

La valeur du champ peut suivre l'histoire de l'expansion.

### 9.4 Limite

Le mécanisme dépend du cadre gravitationnel, du choix de repère et des corrections quantiques.

Il faut distinguer un effet physique invariant d'une simple reparamétrisation entre repères conformes.

## 10. Couplage Higgs-portal

### 10.1 Forme minimale

```text
lambda_Hphi H†H phi²
```

### 10.2 Effet

La valeur de `phi` modifie le terme de masse effectif du Higgs :

```text
m_H,eff² = m_H² + lambda_Hphi phi²
```

et donc potentiellement l'échelle `v`.

### 10.3 Corrélations

Une variation de `v` entraîne :

```text
M_W, M_Z, m_f, G_F
```

à moins que `g`, `g'` ou `Y_f` varient conjointement.

### 10.4 Risque

Le portail peut transmettre de fortes contraintes du secteur visible au champ cosmologique.

## 11. Fonctions de jauge variables

### 11.1 Forme

```text
B_W(phi) W^a_{mu nu} W^{a mu nu}
B_Y(phi) B_{mu nu} B^{mu nu}
```

### 11.2 Effet

Après normalisation canonique, les couplages de jauge dépendent de `phi`.

### 11.3 Difficultés

- préservation de la structure de jauge ;
- corrections quantiques ;
- couplage du dilaton aux masses générées ;
- violation possible du principe d'équivalence ;
- cinquièmes forces.

### 11.4 Source de référence

Les modèles de Shaw et Barrow étendent des scénarios à couplages électrofaibles variables et étudient leurs équations cosmologiques quantiquement corrigées.

## 12. Variation des Yukawa

### 12.1 Forme

```text
Y_f = Y_f(phi)
```

### 12.2 Effets

- masses variables ;
- couplages Higgs-fermions variables ;
- possible variation des angles de mélange ;
- possible apparition de violation de saveur.

### 12.3 Cas commun

Si toutes les Yukawa varient par un facteur commun, les rapports de masses peuvent être partiellement préservés.

### 12.4 Cas générique

Une variation de texture est beaucoup plus fortement contrainte.

## 13. Découplage tardif

### 13.1 Principe

Le porteur dynamique peut perdre son influence lorsque :

- sa masse augmente ;
- son couplage diminue ;
- il tombe dans un minimum ;
- le secteur qui le source devient dilué ;
- une symétrie interdit les interactions résiduelles.

### 13.2 Fonction de fixité

```text
variation ancienne
-> découplage
-> paramètre effectif tardif quasi fixe
```

### 13.3 Test

La durée et la précision de la quasi-fixité doivent être comparées aux horloges, à la spectroscopie et aux tests d'équivalence.

## 14. Matrice des mécanismes

| Mécanisme | Réduit la sensibilité initiale ? | Réduit les cinquièmes forces ? | Risque principal |
|---|---:|---:|---|
| minimum simple | parfois | si champ lourd | valeur du minimum arbitraire |
| friction cosmologique | temporairement | non | dépendance initiale |
| attracteur | oui potentiellement | pas automatiquement | potentiel ajusté |
| moindre couplage | oui | oui potentiellement | universalité supposée |
| masse tardive | non nécessairement | oui | histoire de masse à expliquer |
| écrantage | non nécessairement | localement | complexité et contraintes |
| transition de phase | parfois | selon le modèle | défauts et BBN |
| couplage à la courbure | parfois | non automatiquement | dépendance au cadre |
| Higgs-portal | selon la dynamique | non automatiquement | contraintes visibles |
| fonctions de jauge variables | selon le modèle | non | équivalence et quantique |

## 15. Critère de sélection d'un premier modèle test

Le premier modèle complet devrait :

1. ne faire varier qu'une fonction principale ;
2. préserver clairement la cohérence de jauge ;
3. permettre une intégration cosmologique simple ;
4. produire des observables BBN et tardives calculables ;
5. posséder une limite où la théorie standard est récupérée ;
6. montrer explicitement s'il existe un attracteur ;
7. permettre de quantifier la migration du réglage.

Le candidat le plus lisible pour une première étude est :

```text
scalaire phi
+ couplage Higgs-portal
-> m_H²(phi)
-> v(phi)
-> G_F(phi), masses(phi)
```

avec les Yukawa et les couplages de jauge maintenus fixes dans un premier temps.

Cette coupe est artificielle mais transparente. Elle doit être présentée comme un modèle test, non comme une théorie privilégiée.

## 16. Verdict provisoire

> Plusieurs mécanismes peuvent rendre une grandeur variable presque fixe, mais aucun mot — minimum, attracteur, écrantage ou transition — ne constitue à lui seul une explication. Le gain dépend de la taille du bassin de trajectoires convergentes, de la stabilité quantique et de la compatibilité observationnelle.

## 17. Sources

- T. Damour et A. M. Polyakov, *The String Dilaton and a Least Coupling Principle*, arXiv:hep-th/9401069.
- Douglas J. Shaw et John D. Barrow, *Varying Couplings in Electroweak Theory*, arXiv:gr-qc/0412135.
- Xavier Calmet, *Cosmological Evolution of the Higgs Boson's Vacuum Expectation Value*, arXiv:1707.06922.
- Catarina Cosme, João G. Rosa et O. Bertolami, *Scale-invariant scalar field dark matter through the Higgs portal*, arXiv:1802.09434.