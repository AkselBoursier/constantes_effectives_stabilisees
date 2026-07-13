# Résultats de phase 4 — toy model homogène dissipatif

## Statut

Cette phase ajoute un bilan énergétique ouvert au condensat scalaire homogène.

Le calcul reste phénoménologique. Il ne dérive pas `Gamma_phi` depuis un lagrangien et ne constitue ni un calcul de thermalisation complet ni une analyse BBN.

La question testée est :

> Existe-t-il une fenêtre de dissipation permettant une variation électrofaible ancienne significative, une quasi-fixité avant la BBN et une relique scalaire acceptable, sans injection excessive d'entropie ?

## 1. Équations retenues

Dans le régime quadratique moyen :

```text
dot rho_phi + 3 H rho_phi = - Gamma_phi rho_phi

dot rho_r + 4 H rho_r = + Gamma_phi rho_phi.
```

Le second membre est conservatif pour le système élargi : l'énergie perdue par le condensat est versée au bain relativiste.

Les variables comobiles :

```text
P = rho_phi a³ / rho_r,EW
U = rho_r a⁴ / rho_r,EW
```

vérifient :

```text
dP/dN = - (Gamma_phi / H) P

dU/dN = (Gamma_phi / H) P exp(N).
```

La fraction scalaire et le déplacement électrofaible sont reconstruits par :

```text
rho_phi / rho_r = P exp(N) / U

q(N) = q_i [P(N) / P_i] exp(-3N)

v²(N) = v_0² [1 - q(N)].
```

## 2. Critères de tri

Le scan impose simultanément :

1. `|Delta v_i / v| >= 1 %` ;
2. `max(rho_phi / rho_r) < 0.1` ;
3. `rho_phi / rho_r < 0.01` à la BBN ;
4. `rho_phi / rho_r < 0.01` à l'égalité ;
5. `|Delta v_BBN / v| < 1 %` ;
6. `Delta S / S < 10 %` avant la BBN.

Ces seuils sont des filtres de contrôle du toy model. Le seuil de dix pour cent sur l'entropie est volontairement conservateur et devient souvent le critère actif pour une désintégration tardive.

## 3. Quatre prescriptions comparées

### 3.1 Largeur physique constante

```text
Gamma_phi = Gamma_0

gamma_EW = Gamma_0 / H_EW.
```

Sous domination radiative :

```text
Gamma_phi / H ~ gamma_EW exp(2N).
```

Une largeur initialement petite devient donc efficace à mesure que l'expansion ralentit.

### 3.2 Taux thermique

```text
Gamma_phi proportional to T
```

et :

```text
Gamma_phi / H ~ gamma_EW exp(N).
```

Le taux relatif croît moins vite que pour une largeur constante.

### 3.3 Taux suivant l'expansion

```text
Gamma_phi / H = gamma_EW.
```

La dissipation agit de façon continue par unité de facteur d'échelle.

### 3.4 Taux proportionnel à phi²

```text
Gamma_phi proportional to phi².
```

La dissipation diminue avec le condensat. Elle constitue un test d'auto-extinction.

## 4. Résultat numérique principal

Le tableau donne le plus petit `gamma_EW` trouvé sur la grille pour quatre déplacements initiaux représentatifs.

| Prescription | `q_i` | `|Delta v_i/v|` | `gamma_EW,min` |
|---|---:|---:|---:|
| largeur constante | 0.0199 | 1.0 % | `3.71 × 10^-6` |
| largeur constante | 0.1 | 5.13 % | `8.55 × 10^-5` |
| largeur constante | 0.5 | 29.3 % | `1.30 × 10^-3` |
| largeur constante | 0.9 | 68.4 % | `2.26 × 10^-3` |
| taux thermique | 0.0199 | 1.0 % | `1.51 × 10^-3` |
| taux thermique | 0.1 | 5.13 % | `7.37 × 10^-3` |
| taux thermique | 0.5 | 29.3 % | `3.00 × 10^-2` |
| taux thermique | 0.9 | 68.4 % | `4.03 × 10^-2` |
| `Gamma/H` constant | 0.0199 | 1.0 % | `0.851` |
| `Gamma/H` constant | 0.1 | 5.13 % | `0.912` |
| `Gamma/H` constant | 0.5 | 29.3 % | `0.964` |
| `Gamma/H` constant | 0.9 | 68.4 % | `0.977` |
| taux `proportional to phi²` | 0.0199 | 1.0 % | `4.09 × 10^9` |
| taux `proportional to phi²` | 0.1 | 5.13 % | `2.05 × 10^10` |
| taux `proportional to phi²` | 0.5 | 29.3 % | `7.83 × 10^10` |
| taux `proportional to phi²` | 0.9 | 68.4 % | `1.03 × 10^11` |

Une région phénoménologique acceptable existe donc pour les trois premières prescriptions.

La prescription `phi²` n'est pas exclue algébriquement, mais elle exige une valeur initiale de `Gamma/H` si grande qu'elle cesse d'être un candidat naturel dans ce toy model local.

## 5. Lecture physique de la largeur constante

Avec :

```text
H_EW approximativement égal à 3.6 × 10^-14 GeV
```

le cas `q_i = 0.1` demande :

```text
gamma_EW approximativement égal à 8.5 × 10^-5

Gamma_0 approximativement égal à 3.1 × 10^-18 GeV.
```

Cela correspond à une durée caractéristique :

```text
tau approximativement égal à 2.1 × 10^-7 s.
```

La condition `H ~ Gamma_0` est atteinte vers :

```text
T_dec approximativement égal à T_EW sqrt(gamma_EW)
      approximativement égal à 1.5 GeV.
```

Pour les quatre déplacements testés, les températures indicatives de transfert sont approximativement :

| `q_i` | `T_dec` largeur constante |
|---:|---:|
| 0.0199 | 0.31 GeV |
| 0.1 | 1.48 GeV |
| 0.5 | 5.77 GeV |
| 0.9 | 7.61 GeV |

Ces valeurs sont antérieures à la BBN, mais les plus basses approchent la région QCD, où l'approximation de `g_*` constant doit être abandonnée.

## 6. Lecture physique du taux thermique

Pour :

```text
Gamma_phi proportional to T
```

l'efficacité relative croît seulement comme `a`, au lieu de `a²` pour une largeur constante.

Le taux normalisé requis à `T_EW` est donc plus grand. Les températures indicatives `Gamma/H ~ 1` sont néanmoins du même ordre :

| `q_i` | `T_dec` taux thermique |
|---:|---:|
| 0.0199 | 0.24 GeV |
| 0.1 | 1.18 GeV |
| 0.5 | 4.80 GeV |
| 0.9 | 6.45 GeV |

La fenêtre viable correspond encore à un transfert terminé bien avant la BBN.

## 7. Pourquoi une fenêtre apparaît

L'énergie initiale liée au déplacement du minimum du Higgs reste modeste relativement au rayonnement :

| `q_i` | `rho_phi/rho_r` initial |
|---:|---:|
| 0.0199 | `2.04 × 10^-4` |
| 0.1 | `9.81 × 10^-4` |
| 0.5 | `3.87 × 10^-3` |
| 0.9 | `5.11 × 10^-3` |

Si cette énergie est transférée assez tôt, elle n'a pas le temps de bénéficier de la croissance relative `rho_phi/rho_r proportional to a` qui produisait la catastrophe du modèle stable.

Le bilan devient :

```text
énergie initiale sous-percentuelle
+
transfert avant domination
->
réchauffement modeste
+
absence de relique cohérente.
```

## 8. Rôle du filtre d'entropie

Les points minimaux des prescriptions constante et thermique atteignent typiquement :

```text
max(rho_phi / rho_r) approximativement égal à 0.05 à 0.06

Delta S / S approximativement égal à 0.10.
```

La borne de taux n'est donc pas seulement déterminée par la disparition de la relique. Elle exige que le condensat ne survive pas assez longtemps pour devenir une composante significative avant sa conversion.

Une exigence plus faible, limitée à l'absence de domination, autoriserait des taux plus petits mais conduirait à une injection d'entropie plus importante.

## 9. Contrôle négatif : dissipation auto-extinguible

Pour `Gamma_phi proportional to phi²`, la solution comobile tend vers :

```text
P_final / P_i = 1 / (1 + gamma_EW).
```

L'intégrale totale de dissipation est donc finie. Le taux disparaît précisément lorsque le champ diminue.

Éviter la relique impose alors :

```text
gamma_EW de l'ordre de 10^10 à 10^11
```

pour les déplacements testés.

Ce résultat ne prouve pas qu'aucun couplage dépendant du champ ne fonctionne. Il montre qu'une prescription qui s'éteint comme `phi²` sans autre canal ne fournit pas naturellement une relaxation tardive complète.

## 10. Verdict de phase 4

Contrairement aux phases 2 et 3, le toy model dissipatif possède une fenêtre non vide.

```text
variation ancienne significative
+
transfert énergétique assez précoce
->
fixité avant BBN
+
relique supprimée
+
entropie contrôlée.
```

Le verdict reste cependant phénoménologique :

> La difficulté n'est plus de savoir si un bilan énergétique ouvert peut sauver le toy model. Elle est de déterminer si un mécanisme microscopique peut produire le profil de dissipation requis sans réintroduire un réglage, une instabilité ou une nouvelle contrainte plus sévère.

## 11. Déplacement du problème explicatif

Les phases précédentes donnaient :

```text
fixité cinématique
+
échec du devenir énergétique.
```

La phase 4 donne :

```text
fixité cinématique
+
bilan énergétique viable dans une paramétrisation effective
+
origine microscopique du taux encore ouverte.
```

Le réglage éventuel se situe désormais dans :

- la valeur et le profil temporel de `Gamma_phi` ;
- l'identité du secteur récepteur ;
- les seuils cinématiques ;
- la thermalisation ;
- les contraintes de mélange, de cinquième force ou de rayonnement caché.

## 12. Étape suivante

La prochaine phase doit sélectionner une réalisation microscopique minimale parmi :

1. légère brisure de `Z_2` et mélange scalaire-Higgs ;
2. couplage de Yukawa à des fermions légers ;
3. couplage à un second scalaire relativiste ;
4. annihilation ou évaporation thermique du condensat.

Le premier candidat doit être choisi en comparant le taux calculable aux fenêtres de `gamma_EW` obtenues ici.

## 13. Fichiers reproductibles

```text
modele-toy-homogene-dissipatif.md
calculs/scan_dissipation_homogene.py
calculs/resultats_scan_dissipation_homogene_resume.csv
```

## 14. Limites principales

- domination radiative imposée ;
- degrés de liberté relativistes constants ;
- transfert instantanément thermalise dans le secteur visible ;
- aucune masse thermique ;
- aucune rétroaction microscopique ;
- aucune statistique quantique ;
- oscillations moyennées ;
- validité limitée du terme de friction local ;
- seuils BBN et entropie seulement exploratoires.

## 15. Sources de contrôle

- K. Enqvist et J. Högdahl, *Scalar condensate decay in a fermionic heat bath in the early universe*, arXiv:hep-ph/0405299.
- Alessandro Di Marco et al., *Energy Density, Temperature and Entropy Dynamics in Perturbative Reheating*, arXiv:1907.06084.
- Lev Kofman, Andrei Linde et Alexei Starobinsky, *Reheating after Inflation*, arXiv:hep-th/9405187.
- Shuyang Cao et Daniel Boyanovsky, *Condensate decay in a radiation dominated cosmology*, arXiv:2409.16076.

## 16. Décision

```text
Toy model homogène dissipatif : fenêtre phénoménologique non vide.
```

La phase suivante n'a pas à complexifier arbitrairement le potentiel. Elle doit tester si un canal microscopique concret peut occuper cette fenêtre.