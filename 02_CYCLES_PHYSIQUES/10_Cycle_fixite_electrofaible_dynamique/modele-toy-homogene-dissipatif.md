# Toy model homogène dissipatif — bilan énergétique explicite

## Statut

Ce document définit la phase 4 du cycle de fixité électrofaible dynamique.

Le but n'est pas encore de dériver un taux microscopique de dissipation. Il est de déterminer quel transfert énergétique minimal serait nécessaire pour éviter la relique cohérente qui invalide les modèles conservatifs quadratique et quartique.

Le coefficient de dissipation est donc traité comme une prescription phénoménologique. Il sert à cartographier le besoin physique, non à constituer une explication fondamentale.

## 1. Question testée

> Une dissipation homogène peut-elle convertir l'énergie du condensat en rayonnement assez tôt pour conserver une variation électrofaible ancienne significative, constituer une fixité avant la BBN et éviter une surabondance scalaire ?

Le problème est décomposé en trois opérations :

```text
convergence de v
+
transfert hors du mode homogène
+
compatibilité de l'énergie transférée avec l'histoire thermique
```

## 2. Régime retenu

Le calcul commence après le crossover électrofaible, dans un régime où le condensat scalaire oscille autour de son minimum effectif.

Pour le premier test, on retient un régime quadratique moyen :

```text
<w_phi> = 0
```

Le condensat se comporte comme de la matière en l'absence de transfert.

Le déplacement électrofaible est paramétré par :

```text
q = lambda_Hphi phi² / mu_H²
```

avec :

```text
v²(phi) = v_0² (1 - q)
```

et :

```text
Delta v / v_0 = sqrt(1 - q) - 1.
```

## 3. Équations de bilan

Le modèle moyen emploie :

```text
dot rho_phi + 3 H rho_phi = - Q

dot rho_r + 4 H rho_r = + Q
```

avec :

```text
Q = Gamma_phi rho_phi.
```

Cette forme est l'approximation oscillatoire quadratique d'une équation de champ contenant un terme local de friction. Dans une description microscopique, le noyau dissipatif peut être non local et dépendre du milieu ; le présent modèle ne présuppose pas que `Gamma_phi` soit fondamental.

L'énergie totale est conservée dans le système élargi :

```text
perte du condensat = gain du bain relativiste.
```

## 4. Variables comobiles

On définit :

```text
N = ln(a / a_EW)
P = rho_phi a³ / rho_r,EW
U = rho_r a⁴ / rho_r,EW.
```

Les équations deviennent :

```text
dP/dN = - (Gamma_phi / H) P

dU/dN = (Gamma_phi / H) P exp(N).
```

Les quantités reconstruites sont :

```text
rho_phi / rho_r = P exp(N) / U

q(N) = q_i [P(N) / P_i] exp(-3N)

T(N) = T_EW exp(-N) U^(1/4)
```

sous l'approximation de degrés de liberté relativistes constants.

Le dernier choix sera relâché dans un traitement plus réaliste autour de QCD.

## 5. Énergie initiale

L'excès énergétique associé au déplacement du minimum du Higgs est repris du modèle minimal :

```text
Delta V(q_i) = lambda_H v_0^4 (2 q_i - q_i²) / 4.
```

Le rapport initial au rayonnement est :

```text
r_i = Delta V(q_i) / rho_r(T_EW).
```

Dans le domaine `0 < q_i < 1`, ce rapport reste inférieur au pour cent pour les valeurs de référence employées. Une dissipation précoce peut donc, en principe, transférer toute l'énergie du condensat sans provoquer un réchauffement catastrophique.

## 6. Prescriptions de dissipation

Quatre prescriptions sont comparées.

### A. Largeur physique constante

```text
Gamma_phi = Gamma_0

gamma_EW = Gamma_0 / H_EW.
```

Pendant la domination radiative :

```text
Gamma_phi / H ~ gamma_EW exp(2N).
```

Même une largeur initialement petite devient efficace lorsque `H` diminue.

### B. Taux thermique

```text
Gamma_phi proportional to T
```

avec normalisation :

```text
Gamma_phi(T_EW) / H_EW = gamma_EW.
```

Alors :

```text
Gamma_phi / H ~ gamma_EW exp(N).
```

Cette prescription est un proxy pour un transfert soutenu par le plasma.

### C. Rapport constant au taux d'expansion

```text
Gamma_phi / H = gamma_EW.
```

Cette prescription est purement phénoménologique. Elle teste le niveau de dissipation continue requis par unité d'expansion.

### D. Taux auto-extinguible proportionnel à phi²

```text
Gamma_phi proportional to phi².
```

Dans le régime quadratique :

```text
Gamma_phi / H = gamma_EW s(N) exp(-N)
```

avec :

```text
s(N) = P(N) / P_i
     = 1 / [1 + gamma_EW (1 - exp(-N))].
```

Le transfert s'éteint à mesure que le condensat diminue. Cette prescription sert de contrôle négatif pour les dissipation qui disparaissent avec leur propre source.

## 7. Critères exploratoires

Un point est déclaré acceptable dans ce toy model s'il vérifie :

1. variation initiale significative : `|Delta v_i / v| >= 1 %` ;
2. contrôle de l'approximation radiative : `max(rho_phi / rho_r) < 0.1` ;
3. composante scalaire à la BBN : `rho_phi / rho_r < 0.01` ;
4. composante scalaire à l'égalité : `rho_phi / rho_r < 0.01` ;
5. déplacement électrofaible à la BBN : `|Delta v_BBN / v| < 1 %` ;
6. augmentation d'entropie visible avant la BBN : `Delta S / S < 10 %`.

L'entropie est estimée par :

```text
Delta S / S = U_BBN^(3/4) - 1.
```

Ces seuils servent au tri interne du toy model. Ils ne remplacent ni un calcul BBN ni une borne observationnelle complète.

## 8. Ce que le modèle peut établir

Il peut déterminer :

- l'ordre de grandeur de `Gamma_phi / H` requis ;
- l'époque approximative du transfert ;
- le maximum de la fraction scalaire ;
- l'entropie injectée ;
- la sensibilité au profil temporel de la dissipation ;
- les prescriptions qui s'auto-extinguent trop vite.

## 9. Ce qu'il ne peut pas établir

Il ne dérive pas :

- la particule ou le secteur recevant l'énergie ;
- les largeurs de désintégration depuis un lagrangien ;
- les masses thermiques et blocages cinématiques ;
- la statistique de Bose ou de Fermi ;
- les effets non perturbatifs ;
- la fragmentation du condensat ;
- les variations de `g_*` autour de QCD ;
- la production d'entropie baryonique ou de rayonnement caché ;
- les contraintes sur `Delta N_eff`.

## 10. Critère de gain explicatif

Une fenêtre dissipative constitue un progrès seulement si un mécanisme microscopique raisonnable peut produire le taux requis sans introduire un réglage plus sévère.

```text
fenêtre phénoménologique non vide
!=
explication microscopique acquise.
```

La phase suivante doit donc traduire la fenêtre trouvée vers des couplages, canaux de désintégration ou processus de thermalisation concrets.

## 11. Sources de contrôle

- K. Enqvist et J. Högdahl, *Scalar condensate decay in a fermionic heat bath in the early universe*, arXiv:hep-ph/0405299.
- Alessandro Di Marco et al., *Energy Density, Temperature and Entropy Dynamics in Perturbative Reheating*, arXiv:1907.06084.
- Lev Kofman, Andrei Linde et Alexei Starobinsky, *Reheating after Inflation*, arXiv:hep-th/9405187.
- Shuyang Cao et Daniel Boyanovsky, *Condensate decay in a radiation dominated cosmology*, arXiv:2409.16076.

## 12. Verdict d'ouverture

> Le toy model dissipatif ne cherche plus seulement à amortir une grandeur. Il suit la destination de l'énergie et mesure le coût minimal d'une fixité électrofaible constituée dans un système ouvert.