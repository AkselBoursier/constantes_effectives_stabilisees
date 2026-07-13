# Résultats de phase 3 — régime quartique du portail scalaire–Higgs

## Statut

Cette phase teste l’extension prioritaire identifiée après l’échec du condensat quadratique stable.

La question est :

> Une auto-interaction quartique peut-elle conserver une variation électrofaible ancienne significative tout en évitant la surabondance de matière produite par les oscillations quadratiques ?

Le calcul reste analytique et exploratoire. Il ne comprend ni fragmentation, ni thermalisation, ni résolution complète du potentiel thermique.

## 1. Modèle

On ajoute :

```text
V_phi(phi) = lambda_phi phi^4 / 4
```

au portail :

```text
lambda_Hphi phi^2 H†H.
```

On conserve :

```text
q = lambda_Hphi phi² / mu_H²,
v²(phi) = v_0² (1 - q).
```

Une variation électrofaible initiale supérieure à 1 % exige approximativement :

```text
q_i > 0.02.
```

## 2. Deux régimes de dilution

Lorsque le terme quartique domine :

```text
rho_phi ∝ a^-4,
phi_amplitude ∝ a^-1,
q ∝ a^-2.
```

Le condensat se dilue alors comme le rayonnement.

Après le crossover, le portail induit une masse :

```text
m_eff² = lambda_Hphi v².
```

La transition vers le régime quadratique survient lorsque :

```text
lambda_phi phi² ~ m_eff².
```

En termes de `q` :

```text
q_transition = lambda_Hphi² / (lambda_phi lambda_H).
```

Après cette transition :

```text
rho_phi ∝ a^-3.
```

La surabondance peut donc réapparaître si la transition a lieu trop tôt.

## 3. Tension structurelle

Retarder la transition quadratique demande :

```text
lambda_phi grande relativement à lambda_Hphi².
```

Mais l’énergie quartique initiale vaut :

```text
rho_quartic,i = lambda_phi phi_i^4 / 4.
```

Or :

```text
phi_i² = q_i mu_H² / lambda_Hphi.
```

Donc :

```text
rho_quartic,i
= q_i² mu_H^4 / (4 q_transition lambda_H).
```

À `q_i` fixé, diminuer `q_transition` pour prolonger le régime radiatif augmente donc inversement l’énergie initiale.

Il existe une tension intrinsèque :

```text
transition tardive
<->
énergie quartique initiale élevée.
```

## 4. Domaine exploré

Le scan couvre :

```text
10^-40 <= lambda_Hphi <= 10^-8
10^-40 <= lambda_phi <= 10^4
10^-12 <= q_i <= 0.9
```

soit :

```text
2 077 061 points.
```

Les filtres sont :

1. amplitude sub-planckienne ;
2. régime quartique initial réel ;
3. énergie initiale inférieure au rayonnement ;
4. densité du condensat inférieure au rayonnement à l’égalité ;
5. variation électrofaible initiale supérieure à 1 %.

## 5. Résultat numérique

```text
points satisfaisant tous les critères : 0
```

Le meilleur point du scan parmi ceux ayant une variation supérieure à 1 %, une amplitude sub-planckienne et une domination quartique initiale donne approximativement :

```text
lambda_Hphi = 10^-18
lambda_phi = 10^-33
q_i = 2.04 × 10^-2
T_transition = 98.4 GeV
rho_phi/rho_rad au crossover = 4.88 × 10^-4
rho_phi/rho_rad à l’égalité = 6.00 × 10^7
```

Même le point le moins défavorable surproduit donc la densité admissible de plusieurs ordres de grandeur.

## 6. Pourquoi la dilution quartique ne suffit pas

Le régime quartique corrige bien la loi de dilution pendant une première phase.

Mais le portail qui doit ramener `v` vers sa valeur tardive induit aussi un terme quadratique. Le condensat finit alors par devenir une composante de matière.

Pour retarder suffisamment cette transition, il faut augmenter l’énergie quartique initiale. La réduction de la croissance tardive est compensée par une augmentation du budget énergétique de départ.

Le problème n’est donc plus seulement :

```text
rho_phi ∝ a^-3 trop tôt.
```

Il devient :

```text
retarder le régime a^-3
exige une énergie a^-4 initiale trop grande.
```

## 7. Verdict conditionnel

Dans le modèle homogène, stable et non dissipatif étudié :

```text
régime quartique seul : insuffisant.
```

Il améliore la dilution mais ne produit pas une architecture viable pour une variation électrofaible ancienne supérieure à 1 %.

Le verdict est conditionnel à :

- la stabilité du condensat ;
- l’absence de transfert d’énergie au plasma ;
- l’absence de fragmentation ;
- l’approximation d’une transition nette quartique–quadratique ;
- le fond cosmologique imposé ;
- l’absence d’une phase inflationnaire ou d’une production tardive spécialement organisée.

## 8. Gain conceptuel

La phase distingue désormais trois niveaux :

```text
1. amortissement de la variation de v ;
2. dilution de l’énergie du porteur ;
3. élimination ou redistribution de cette énergie.
```

Le régime quadratique échouait au niveau 2.

Le régime quartique améliore le niveau 2, mais échoue encore au niveau 3 dès qu’il doit rejoindre le régime massif induit par le Higgs.

La fixité ne peut donc pas être évaluée seulement par la convergence de la variable :

> Une fixité dynamiquement constituée exige aussi une histoire acceptable de l’énergie mobilisée pour produire cette convergence.

## 9. Suite prioritaire

La prochaine extension ne doit plus être une simple modification du potentiel conservatif.

Elle doit introduire un mécanisme d’évacuation ou de redistribution :

1. fragmentation du condensat ;
2. annihilation ou thermalisation dans le plasma ;
3. brisure de `Z_2` et désintégration ;
4. couplage dissipatif dépendant de la température ;
5. transition vers un secteur sombre relativiste soumis aux bornes sur `Delta N_eff`.

La priorité méthodologique devient donc :

```text
fixité + bilan énergétique ouvert.
```

## 10. Fichiers reproductibles

```text
calculs/scan_portail_higgs_quartique.py
calculs/resultats_scan_portail_higgs_quartique_resume.csv
```

## 11. Sources de contrôle

- Catarina Cosme, João G. Rosa et O. Bertolami, *Scale-invariant scalar field dark matter through the Higgs portal*, arXiv:1802.09434.
- J. A. R. Cembranos, A. L. Maroto et S. J. Núñez Jareño, *Cosmological perturbations in coherent oscillating scalar field models*, arXiv:1509.08819.
