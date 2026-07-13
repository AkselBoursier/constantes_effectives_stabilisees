# Résultats de phase 2 — modèle scalaire–Higgs minimal

## Statut

Ce document rapporte un premier calcul exploratoire du modèle `Z_2` défini dans :

```text
modele-test-scalaire-higgs-portal.md
```

Le calcul n'est ni un ajustement cosmologique global ni une résolution complète du potentiel thermique. Il sert de test de falsification minimal.

La question testée est :

> Un condensat scalaire stable, couplé quadratiquement au Higgs, peut-il produire une variation électrofaible ancienne significative, se verrouiller avant la BBN et rester cosmologiquement acceptable sans mécanisme supplémentaire de dissipation ?

## 1. Hypothèses du calcul

Le potentiel est :

```text
V(H, phi) =
  - mu_H² H†H
  + lambda_H (H†H)²
  + lambda_Hphi phi² H†H
```

avec, dans ce premier test :

```text
m_phi = 0
lambda_phi = 0
lambda_Hphi > 0
```

Le Higgs est supposé suivre adiabatiquement son minimum après le crossover électrofaible.

On définit :

```text
q = lambda_Hphi phi² / mu_H²
```

Dans la branche brisée :

```text
0 < q < 1
v²(phi) = v_0² (1 - q)
```

La variation initiale est donc :

```text
Delta v / v_0 = sqrt(1 - q_i) - 1
```

Après minimisation du Higgs, l'excès d'énergie potentielle relativement à `phi = 0` est :

```text
Delta V(q) =
lambda_H v_0^4 (2 q - q²) / 4
```

La masse effective locale du scalaire est approximée par :

```text
m_eff² =
lambda_Hphi v_0² (1 - q_i)
```

Le champ est supposé gelé tant que :

```text
H > m_eff
```

puis oscillant dans un régime approximativement quadratique lorsque :

```text
H <= m_eff
```

Dans ce régime :

```text
rho_phi proportional to a^-3
phi_amplitude proportional to a^-3/2
q_envelope proportional to a^-3
```

Le condensat est supposé stable et aucune annihilation, fragmentation, désintégration ou thermalisation n'est incluse.

## 2. Domaine exploré

Le scan emploie :

```text
10^-40 <= lambda_Hphi <= 10^-8
10^-12 <= q_i <= 0.9
```

avec :

```text
129 valeurs de lambda_Hphi
161 valeurs de q_i
20769 points au total
```

Les valeurs de référence sont :

```text
v_0 = 246.22 GeV
m_h = 125.25 GeV
T_EW = 160 GeV
T_BBN = 1 MeV
T_eq = 0.8 eV
```

Les fonctions `g_*(T)` et `g_*s(T)` sont représentées par une interpolation par paliers suffisante pour ce test exploratoire.

## 3. Critères

Un point est déclaré acceptable dans ce premier test s'il vérifie :

1. branche électrofaible brisée : `0 < q_i < 1` ;
2. amplitude initiale sub-planckienne : `phi_i < M_Pl réduit` ;
3. absence de domination avant le début des oscillations : `rho_phi / rho_rad < 1` ;
4. contrainte BBN simplifiée : `|Delta v_BBN / v| < 1 %` ;
5. condensat stable non surabondant à l'égalité : `rho_phi / rho_rad < 1` ;
6. variation ancienne significative : `|Delta v_i / v| > 1 %`.

Le seuil BBN est volontairement plus grossier que les analyses nucléaires publiées. Il sert uniquement de filtre de premier niveau.

## 4. Résultat numérique principal

Résumé du scan :

| Test | Nombre de points |
|---|---:|
| total | 20 769 |
| amplitude sub-planckienne | 19 366 |
| absence de domination avant oscillation | 19 641 |
| filtre BBN | 20 769 |
| condensat non surabondant à l'égalité | 3 034 |
| variation initiale supérieure à 1 % | 2 967 |
| tous les critères sauf la relique | 2 379 |
| tous les critères simultanément | **0** |

Résultat :

```text
aucun point du scan
```

ne produit à la fois :

```text
variation ancienne significative
+
verrouillage avant BBN
+
condensat Z_2 stable cosmologiquement acceptable.
```

## 5. Pourquoi la BBN n'est pas l'obstacle principal

Lorsque les oscillations commencent avant la BBN :

```text
q_BBN =
q_i (a_osc / a_BBN)^3
```

Pour une oscillation déclenchée autour du crossover :

```text
q_BBN / q_i ~ 10^-17
```

La variation de `v` est donc fortement amortie avant la nucléosynthèse.

Dans ce modèle simplifié, le portail peut ainsi constituer rapidement une quasi-fixité électrofaible.

Mais l'amortissement de l'amplitude ne détruit pas l'énergie du condensat.

## 6. Obstacle principal : la relique cohérente

Après le début des oscillations quadratiques :

```text
rho_phi proportional to a^-3
rho_rad proportional to a^-4
```

La fraction relative du scalaire croît donc comme :

```text
rho_phi / rho_rad proportional to a
```

Pour `q_i = 0.1`, les résultats représentatifs sont :

| `lambda_Hphi` | `T_osc` | `phi_i / M_Pl` | `rho_phi/rho_rad` à l'oscillation | `rho_phi/rho_rad` à l'égalité |
|---:|---:|---:|---:|---:|
| `10^-36` | `14.1 GeV` | `11.5` | `23.3` | `1.10 × 10^12` |
| `10^-34` | `44.5 GeV` | `1.15` | `0.233` | `3.47 × 10^10` |
| `10^-33` | `79.2 GeV` | `0.364` | `0.0233` | `6.17 × 10^9` |
| `10^-32` | `129 GeV` | `0.115` | `0.00233` | `1.13 × 10^9` |
| `>= 10^-31` | `160 GeV` | dépend du portail | `9.81 × 10^-4` | `5.91 × 10^8` |

Même lorsque la fraction initiale paraît petite, son comportement de matière la rend catastrophique avant l'égalité.

## 7. Borne analytique dans le régime d'oscillation immédiate

Pour `q_i << 1` et une libération au voisinage de `T_EW` :

```text
Delta V ~ lambda_H v_0^4 q_i / 2
```

puis :

```text
r_eq =
(rho_phi / rho_rad)_eq
~ 6 × 10^9 q_i
```

La condition conservatrice :

```text
r_eq < 1
```

impose donc approximativement :

```text
q_i < 1.6 × 10^-10
```

soit :

```text
|Delta v_i / v| < 8 × 10^-11
```

Le scan numérique retrouve :

```text
q_i,max = 1.47 × 10^-10
|Delta v_i / v|_max = 7.34 × 10^-11
```

pour les points satisfaisant simultanément les filtres sub-planckien, pré-domination, BBN et relique.

Cette amplitude est trop petite pour constituer une histoire électrofaible significative au sens du cycle.

## 8. Verdict physique conditionnel

Le modèle minimal réalise bien :

```text
déplacement initial de v
-> masse induite après le crossover
-> oscillations
-> amortissement de phi
-> quasi-fixité rapide de v
```

Mais il réalise simultanément :

```text
énergie de déplacement
-> condensat scalaire stable
-> composante de matière
-> surabondance cosmologique
```

Le mécanisme ne supprime donc pas le coût de la variation. Il le transfère de la valeur électrofaible vers une abondance relique.

## 9. Interprétation conceptuelle

Ce cas distingue deux sens de la stabilisation.

### Stabilisation cinématique

```text
phi -> 0
Delta v / v -> 0
```

Elle est obtenue.

### Stabilisation cosmologique complète

```text
phi -> 0
+
énergie résiduelle compatible avec l'histoire cosmologique
```

Elle n'est pas obtenue dans le modèle minimal stable.

Le résultat constitue donc un cas de :

```text
fixité locale constituée
+
échec global de l'architecture cosmologique
```

Il montre également une migration du réglage :

```text
variation électrofaible initiale
-> problème d'abondance du condensat
-> nécessité d'un mécanisme de dilution ou de désintégration
```

## 10. Portée et limites

Le verdict est conditionnel aux hypothèses suivantes :

- symétrie `Z_2` exacte ;
- condensat stable ;
- régime quadratique après le crossover ;
- absence de transfert d'énergie vers le plasma ;
- absence de fragmentation ;
- absence d'annihilation efficace ;
- fond cosmologique imposé ;
- potentiel thermique remplacé par une transition simplifiée ;
- perturbations et production de particules négligées.

Il ne constitue donc pas un théorème excluant tous les portails scalaires.

Il exclut comme explication suffisante la version la plus minimale :

> un condensat cohérent stable qui se verrouille seulement par une masse quadratique induite par le Higgs.

## 11. Voies de sortie à instruire

Le résultat indique quatre extensions physiquement distinctes.

### A. Brisure de `Z_2` et désintégration

L'énergie du condensat peut être transférée au plasma, au prix de mélange, de contraintes de durée de vie et d'éventuelles cinquièmes forces.

### B. Régime quartique

Si les oscillations sont dominées par :

```text
lambda_phi phi^4 / 4
```

alors l'équation d'état moyenne est de type radiation :

```text
rho_phi proportional to a^-4
```

La surabondance de matière peut être évitée ou retardée.

### C. Dissipation ou thermalisation

Une interaction suffisamment efficace peut fragmenter ou évaporer le condensat. Un calcul de Boltzmann ou de préchauffage devient alors nécessaire.

### D. Scalaire comme matière noire

Le condensat peut être conservé comme composante de matière noire, mais la borne trouvée impose alors une variation électrofaible initiale de l'ordre de `10^-10` ou moins dans ce modèle minimal.

## 12. Décision de phase 2

```text
Modèle Z_2 minimal, cohérent, stable et quadratique :
écarté comme mécanisme autonome d'une variation électrofaible ancienne significative.
```

La phase est néanmoins concluante méthodologiquement.

Elle a produit :

1. un modèle dimensionnellement explicite ;
2. un code reproductible ;
3. un scan de bassin paramétrique ;
4. un filtre BBN ;
5. un test de rétroaction énergétique ;
6. un cas négatif précis ;
7. une localisation de la migration du réglage.

La prochaine extension prioritaire est le régime quartique, car il modifie directement la loi de dilution responsable de l'échec.

## 13. Fichiers reproductibles

```text
calculs/scan_portail_higgs.py
calculs/resultats_scan_portail_higgs_resume.csv
```

Le script peut également générer le scan complet au format CSV.

## 14. Sources de contrôle

- Anne-Katherine Burns et al., *Constraints on Variation of the Weak Scale from Big Bang Nucleosynthesis*, arXiv:2402.08626.
- Helen Meyer et Ulf-G. Meißner, *Improved Constraints on the Variation of the Weak Scale from Big Bang Nucleosynthesis*, arXiv:2403.09325.
- Catarina Cosme, João G. Rosa et O. Bertolami, *Scale-invariant scalar field dark matter through the Higgs portal*, arXiv:1802.09434.
- J. A. R. Cembranos, A. L. Maroto et S. J. Núñez Jareño, *Cosmological perturbations in coherent oscillating scalar field models*, arXiv:1509.08819.
