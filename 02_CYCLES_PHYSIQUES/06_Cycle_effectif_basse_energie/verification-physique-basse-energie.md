# Vérification physique — cycle effectif basse énergie

## Statut

Ce document contrôle la phase 2 du dossier :

- [architecture-relationnelle-basse-energie.md](architecture-relationnelle-basse-energie.md)

Il vérifie le cas de Fermi, la logique de raccordement et d’évolution des coefficients, le contraste avec la QCD basse énergie et le statut de la gravitation comme théorie effective.

## 1. Sources de contrôle

1. A. V. Manohar, *Introduction to Effective Field Theories* :
   <https://arxiv.org/abs/1804.05863>
2. C. P. Burgess, *Introduction to Effective Field Theory* :
   <https://arxiv.org/abs/hep-th/0701053>
3. Particle Data Group, *Electroweak Model and Constraints on New Physics*, mise à jour 2025–2026 :
   <https://pdg.lbl.gov/2025/reviews/rpp2025-rev-standard-model.pdf>
4. Particle Data Group, *Quantum Chromodynamics*, mise à jour 2025 :
   <https://pdg.lbl.gov/2025/reviews/rpp2025-rev-qcd.pdf>
5. J. F. Donoghue, *General Relativity as an Effective Field Theory: The Leading Quantum Corrections* :
   <https://arxiv.org/abs/gr-qc/9405057>
6. J. F. Donoghue, *The Quantum Theory of General Relativity at Low Energies* :
   <https://arxiv.org/abs/gr-qc/9607039>

## 2. Ce qu’est une théorie effective dans ce dossier

Une théorie effective n’est pas définie par le seul fait qu’elle serait approximative ou moins fondamentale.

Elle organise une description selon :

```text
degrés de liberté pertinents
+ symétries
+ séparation d’échelles
+ opérateurs classés par puissance
+ coefficients de Wilson
+ règle d’estimation des corrections
```

La prédictivité provient du comptage en puissances : à une précision donnée, seul un nombre fini d’opérateurs contribue.

### Décision

Le noyau commun aux cas recevables est une organisation contrôlée des erreurs et des échelles, non la simple présence d’une « constante effective ».

## 3. Théorie de Fermi comme EFT du secteur faible

### 3.1 Développement du propagateur

Pour une impulsion transférée `q` telle que :

```text
|q²| << M_W²,
```

le propagateur du `W` se développe :

```math
\frac{1}{q^2-M_W^2}
=-\frac{1}{M_W^2}
\left[1+\frac{q^2}{M_W^2}+O\!\left(\frac{q^4}{M_W^4}\right)\right].
```

Le premier terme conduit à un opérateur local de dimension six.

Dans les conventions usuelles :

```math
\mathcal L_F
=-\frac{G_F}{\sqrt2}
\bigl[\bar\psi\gamma^\mu(1-\gamma_5)\psi\bigr]
\bigl[\bar\chi\gamma_\mu(1-\gamma_5)\chi\bigr]
+\cdots
```

et, au niveau arbre :

```math
\frac{G_F}{\sqrt2}=\frac{g^2}{8M_W^2}.
```

### 3.2 Pouvoir explicatif

Le raccordement explique simultanément :

- la localité apparente de l’interaction à basse énergie ;
- la dimension de `G_F` ;
- la suppression des corrections par `q²/M_W²` ;
- le domaine de rupture de l’approximation.

### 3.3 Correction

`G_F` ne remplace pas toute la théorie électrofaible. Il pondère le terme dominant d’une expansion dont les termes suivants restent physiquement définis.

## 4. Matching, running et mélange d’opérateurs

Une EFT ne se réduit pas à retirer un champ lourd.

### 4.1 Raccordement

À une échelle `mu_M` proche de la masse lourde, les amplitudes de la théorie plus complète et de l’EFT sont rendues égales à l’ordre de précision choisi.

Schématiquement :

```math
\mathcal A_{\mathrm{UV}}(\mu_M)
=
\sum_i C_i(\mu_M)\,
\langle O_i(\mu_M)\rangle.
```

Le matching détermine les coefficients `C_i` à cette échelle.

### 4.2 Évolution

Les coefficients satisfont une équation de groupe de renormalisation :

```math
\mu\frac{d C_i}{d\mu}
=\gamma_{ji}C_j,
```

avec mélange possible des opérateurs.

Les coefficients et les éléments de matrice évoluent de manière complémentaire afin que l’observable physique soit indépendante de l’échelle de renormalisation à l’ordre calculé.

### 4.3 Dépendance de base

Une redéfinition de champs, une intégration par parties ou l’usage des équations du mouvement peut modifier la base d’opérateurs et les coefficients individuels sans changer les amplitudes physiques.

### Décision

```text
coefficient de Wilson individuel
≠
invariant physique autonome.
```

Le porteur de contenu physique est la combinaison donnant l’amplitude ou l’observable, dans une précision déclarée.

## 5. Seuils et découplage

Lorsqu’une échelle de calcul franchit la masse d’un degré de liberté lourd, on peut changer d’EFT et effectuer un nouveau raccordement.

Le découplage n’est pas toujours automatique dans n’importe quel schéma de soustraction. Il doit être mis en œuvre par les relations de matching et par le choix des degrés de liberté actifs.

### Correction de vocabulaire

Un seuil n’est généralement pas un point physique où un objet disparaît brutalement.

Il désigne une région dans laquelle :

- le contenu explicite de la description change ;
- une expansion devient moins efficace ;
- un raccordement entre théories est requis.

## 6. QCD : couplage courant et `Lambda_QCD`

### 6.1 Couplage courant

Le PDG écrit les prédictions perturbatives en fonction du couplage renormalisé :

```math
\alpha_s(\mu_R),
```

qui satisfait :

```math
\mu_R^2\frac{d\alpha_s}{d\mu_R^2}
=\beta(\alpha_s).
```

La liberté asymptotique implique que le couplage diminue aux hautes énergies.

### 6.2 Paramètre `Lambda`

La solution de l’équation de groupe peut être paramétrée par une échelle `Lambda`, par exemple `Lambda_{\overline{MS}}`.

Cette échelle dépend :

- du schéma de renormalisation ;
- du nombre de saveurs actives ;
- de l’ordre perturbatif ;
- des conventions de raccordement aux seuils.

Elle ne doit pas être identifiée sans qualification à une observable unique de confinement.

Les masses hadroniques et autres observables sont physiques ; le paramètre `Lambda_{\overline{MS}}` est un moyen de paramétrer la trajectoire du couplage dans un schéma donné.

### 6.3 Basse énergie QCD

Lorsque `Q` approche les échelles hadroniques :

- `alpha_s(Q)` augmente ;
- l’expansion perturbative perd son contrôle ;
- des degrés de liberté composites et des méthodes non perturbatives deviennent appropriés.

### Décision

La QCD confirme que :

```text
basse énergie
≠
simple suppression de degrés lourds
≠
simplification uniforme.
```

Elle constitue un cas de changement de régime et de description.

## 7. Gravitation comme EFT

L’action effective gravitationnelle s’organise comme une expansion en opérateurs de courbure :

```math
S=\int d^4x\sqrt{-g}
\left[
\frac{M_{\mathrm{Pl}}^2}{2}R
+c_1R^2
+c_2R_{\mu\nu}R^{\mu\nu}
+\cdots
\right].
```

À basse énergie ou faible courbure, les opérateurs contenant davantage de dérivées sont supprimés par des rapports d’échelle.

Schématiquement :

```math
\frac{E^2}{M_{\mathrm{Pl}}^2}\ll1.
```

### 7.1 Ce qui est prédictif

Les contributions non analytiques à basse énergie produites par les degrés de liberté sans masse peuvent être indépendantes des détails de la complétion ultraviolette et donner des prédictions quantiques de basse énergie.

### 7.2 Ce qui reste ouvert

Les coefficients locaux d’opérateurs d’ordre supérieur contiennent des informations sur la physique ultraviolette et doivent être déterminés ou bornés.

La théorie effective ne fournit pas une description contrôlée lorsque les rapports d’échelle cessent d’être petits.

### 7.3 Correction

`M_Pl` est une échelle d’organisation du comptage de puissances. Elle n’est pas démontrée comme une frontière nette et universelle où une théorie unique prendrait brusquement le relais.

### Décision

La gravitation basse énergie confirme qu’une EFT peut avoir un pouvoir prédictif sans disposer d’une complétion UV connue.

## 8. Les trois cas ont-ils un noyau physique commun ?

### Cas faible

```text
un médiateur massif est non résolu ;
un opérateur local et ses corrections sont dérivés.
```

### Cas QCD

```text
le couplage évolue ;
la perturbation perd son contrôle ;
les degrés de liberté adaptés changent.
```

### Cas gravitationnel

```text
les corrections de dérivées supérieures sont supprimées ;
la complétion UV reste inconnue.
```

### Verdict

Le noyau commun est principalement méthodologique et structurel :

```text
séparation d’échelles
+ degrés de liberté adaptés
+ symétries
+ expansion ou organisation contrôlée
+ estimation de l’erreur
+ domaine de rupture.
```

Il n’existe pas une même opération physique de « formation d’une constante » dans les trois cas.

## 9. Registre de décisions

| Proposition | Verdict | Qualification |
|---|---|---|
| `G_F` résume l’échange du `W` à basse énergie | confirmé | terme dominant d’une EFT |
| `G_F` est universel sans domaine | refusé | `|q²| << M_W²` et cadre requis |
| tout coefficient de Wilson est une constante physique | refusé | base, échelle, schéma et ordre requis |
| le matching suffit sans running | refusé | logarithmes et mélange d’opérateurs possibles |
| `alpha_s(Q)` est constant en `Q` | refusé | couplage courant |
| `Lambda_MSbar` est une observable de confinement | refusé | paramètre de schéma |
| basse énergie signifie toujours simplification | refusé | QCD fournit un contre-exemple |
| GR est prédictive comme EFT à basse énergie | confirmé | expansion de faible énergie / courbure |
| `M_Pl` est une frontière physique nette | non établi | échelle de comptage et de perte attendue de contrôle |

## 10. Contrefactuels contrôlés

### 10.1 Absence de séparation `q²/M_W²`

Sans petit rapport, la théorie locale de Fermi ne possède plus de paramètre d’expansion et le propagateur doit être conservé.

### 10.2 Annulation de la fonction bêta QCD

Si la fonction bêta pertinente s’annulait identiquement, la trajectoire de `alpha_s` et l’apparition d’une échelle dynamique seraient radicalement modifiées. Le passage de régime ne pourrait plus être décrit de la même manière.

### 10.3 Changement de base d’opérateurs

Les `C_i` changent tandis que l’amplitude demeure. Une attribution de constance physique à un coefficient isolé est donc rejetée.

### 10.4 Absence de hiérarchie gravitationnelle

Si `E/M_Pl` n’était pas petit, le classement des opérateurs ne permettrait plus de tronquer l’action avec une erreur contrôlée.

## 11. Résultat pour la notion de fonction de fixité

La notion est utile pour `G_F` à condition de viser :

```text
la stabilité du terme dominant dans un domaine et une convention donnés.
```

Elle devient trompeuse si elle est étendue aux coefficients de Wilson comme s’ils étaient tous invariants.

En QCD, la structure pertinente est une trajectoire de couplage et un changement de régime, non une fixité sous variation de l’échelle.

En gravitation, la structure pertinente est une hiérarchie de suppression et une organisation des corrections.

### Décision

Le cycle ne confirme pas une classe ontologique de constantes effectives basse énergie.

Il confirme une pluralité de fonctions dans des descriptions gouvernées par une structure EFT commune.

## 12. Conclusion de phase 2

La matière interne est largement récupérable, avec quatre corrections :

1. l’unité du cycle est méthodologique avant d’être physique ;
2. un coefficient de Wilson individuel n’est pas un invariant autonome ;
3. `Lambda_QCD` doit être distinguée d’une échelle physique unique de confinement ;
4. `M_Pl` organise un comptage de puissances sans constituer une frontière nette démontrée.

> L’effectivité ne stabilise pas nécessairement une valeur. Elle organise ce qui peut être calculé, avec quels degrés de liberté, à quelle précision et jusqu’à quelle limite.
