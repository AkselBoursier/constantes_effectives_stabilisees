# C1 — Résultats computationnels : planchers, frontière et priors v0.1

## 0. Statut et portée

```text
statut : première reprise computationnelle active de la tension N1–N3 ;
date : 17 juillet 2026 ;
base : N1 oscillations, N3 cosmologie et N5 matrice comparative ;
fonction : quantifier les planchers oscillatoires et isoler l'effet de la
           frontière et des priors sur l'énoncé cosmologique ;
ne vaut pas : reproduction des chaînes DESI, profil Feldman–Cousins exact,
              nouvel ajustement de Boltzmann ou preuve de nouvelle physique ;
révision : requise après ingestion des chaînes officielles DESI DR2 et des
           profils numériques complets de NuFIT 6.1.
```

Le calcul est produit par
[`analyse_tension_n1_n3.py`](analyse_tension_n1_n3.py). Les sorties numériques
sont conservées dans [`resultats_synthese.json`](resultats_synthese.json) et
[`sensibilite_priors.csv`](sensibilite_priors.csv).

## 1. Question computationnelle

La tension documentaire de `N5` peut provenir de plusieurs opérations qu'il faut
séparer :

```text
A. incertitude sur les écarts de masses mesurés par oscillation ;
B. choix de l'ordre normal ou inversé ;
C. vraisemblance cosmologique préférant une direction sous la frontière ;
D. prior Sigma m_nu >= 0 ou prior imposant un plancher oscillatoire ;
E. paramétrisation uniforme en Sigma m_nu ou en masse la plus légère ;
F. modèle cosmologique LambdaCDM ou extension de l'expansion.
```

La phase `C1` traite directement `A–E` dans un modèle substitutif. Le point `F`
reste documenté par le contraste publié `0.0642 eV` sous `LambdaCDM` contre
`0.163 eV` sous `w_0w_aCDM`, sans reconstruire sa likelihood.

## 2. Entrées oscillatoires

Les entrées centrales sont prises dans les résultats primaires déjà instruits par
`N1` :

```text
Delta m^2_21 = (7.50 +/- 0.12) x 10^-5 eV^2 ;
Delta m^2_32 (NO) = (2.43 +/- 0.035) x 10^-3 eV^2 ;
|Delta m^2_32| (IO) = (2.48 +/- 0.035) x 10^-3 eV^2.
```

La première valeur vient du premier résultat JUNO ; les deux valeurs atmosphériques
sont une symétrisation conservatrice des intervalles de l'analyse conjointe
T2K–NOvA. Le calcul tient compte de la convention :

```math
\Delta m^2_{31}=\Delta m^2_{32}+\Delta m^2_{21}
```

pour l'ordre normal.

Cinq cent mille tirages gaussiens indépendants sont effectués. Cette indépendance
est une approximation de `C1` : les profils et corrélations de NuFIT 6.1 seront
nécessaires en `C2`.

## 3. Planchers reconstruits

Pour une masse la plus légère nulle, le calcul obtient :

| Ordre | Moyenne du plancher | Écart-type propagé | Intervalle central 95 % |
|---|---:|---:|---:|
| normal | `0.058709 eV` | `0.000359 eV` | `[0.058000 ; 0.059408] eV` |
| inversé | `0.098840 eV` | `0.000708 eV` | `[0.097449 ; 0.100217] eV` |

Le premier résultat positif est donc :

> L'épaisseur actuelle des planchers oscillatoires est petite devant l'échelle
> marginale cosmologique publiée de `0.020 eV`.

La tension ne peut pas être supprimée en élargissant simplement les incertitudes
actuelles de `Delta m^2`. Une reprise exacte des corrélations peut déplacer les
dernières décimales, mais non transformer une incertitude de quelques `10^-4 eV`
en une largeur de plusieurs `10^-2 eV`.

## 4. Construction du substitut cosmologique

DESI publie sous `LambdaCDM`, trois masses dégénérées et un prior uniforme
`Sigma m_nu >= 0` :

```text
quantile supérieur 95 % : 0.0642 eV ;
écart-type marginalisé du posterior : 0.020 eV.
```

Pour isoler la frontière, `C1` suppose une vraisemblance marginale gaussienne non
bornée :

```math
L(\Sigma) \propto
\exp\left[-\frac{(\Sigma-\mu)^2}{2\sigma^2}\right],
```

puis la tronque à `Sigma >= 0`. Les deux paramètres sont déterminés en imposant
simultanément le quantile et l'écart-type publiés. On obtient :

```text
mu = -0.015165 eV ;
sigma = 0.037497 eV.
```

Cette valeur négative n'est pas une masse physique. Elle reconstruit la direction
dans laquelle un modèle gaussien minimal placerait le maximum avant application
de la frontière.

Le substitut ne reproduit ni les non-gaussianités multidimensionnelles, ni la
construction Feldman–Cousins, ni le paramètre effectif négatif de l'article DESI.
Sa fonction est uniquement de montrer ce que la frontière suffit déjà à produire.

## 5. Masse postérieure au-dessus des planchers

Sous le posterior substitutif tronqué à zéro :

```text
P(Sigma m_nu >= plancher NO | données, substitut) = 0.0712 ;
P(Sigma m_nu >= plancher IO | données, substitut) = 0.00344.
```

Relativement au centre non borné du substitut, les planchers se trouvent à :

```text
NO : 1.97 sigma ;
IO : 3.04 sigma.
```

Ces nombres ne doivent pas être identifiés au `3 sigma` de l'analyse DESI en masse
effective : ils proviennent d'une reconstruction à deux contraintes seulement.
Ils montrent néanmoins une asymétrie robuste : l'ordre inversé est beaucoup plus
fortement comprimé que l'ordre normal par la combinaison cosmologique de base.

## 6. Effet d'un changement de frontière

La même vraisemblance substitutive donne les quantiles suivants :

| Prior ou paramétrisation | Médiane de `Sigma m_nu` | Quantile 95 % |
|---|---:|---:|
| uniforme, `Sigma >= 0` | `0.02040 eV` | `0.06420 eV` |
| uniforme, `Sigma >= plancher NO` | `0.06923 eV` | `0.09847 eV` |
| uniforme, `Sigma >= plancher IO` | `0.10645 eV` | `0.12920 eV` |
| uniforme en `m_lightest`, NO | `0.06923 eV` | `0.09847 eV` |
| uniforme en `m_lightest`, IO | `0.10645 eV` | `0.12920 eV` |

Le déplacement ne signifie pas que les données ont changé. Il signifie que
l'énoncé postérieur a changé parce que son domaine et sa mesure de volume ont
changé.

La borne `0.0642 eV` ne peut donc pas être transportée dans un modèle qui impose
le plancher normal sans recalcul. Réciproquement, imposer le plancher ne résout pas
la préférence du maximum cosmologique : cela redistribue le posterior dans la
région physique restante.

## 7. Préférence d'ordre dans le substitut

Avec des probabilités antérieures égales pour les deux ordres et un prior uniforme
sur la masse la plus légère entre `0` et `1 eV`, l'intégration du substitut donne :

```text
facteur de Bayes NO / IO = 15.9.
```

Sous le même choix :

```text
NO : m_lightest < 0.01945 eV à 95 % ;
IO : m_lightest < 0.01946 eV à 95 %.
```

Le facteur de Bayes est un diagnostic conditionnel au substitut, au prior et à
l'égalité initiale des probabilités d'ordre. Il ne remplace pas le calcul DESI
utilisant les profils d'oscillation.

## 8. Résultat scientifique de C1

La tension `N1–N3` se décompose maintenant en trois résultats distincts :

1. **le plancher oscillatoire est numériquement étroit** ; son incertitude n'est pas
   la source principale du frottement ;
2. **la likelihood cosmologique de base pointe vers la frontière ou au-dessous** ;
   la troncature transforme cette direction en borne supérieure serrée ;
3. **la préférence d'ordre et la borne dépendent de la mesure de prior** ; elles
   ne sont pas des observables brutes de DESI.

La formulation « la cosmologie exclut la masse minimale des oscillations » reste
trop forte. La formulation recevable après `C1` est :

> Sous la combinaison DESI DR2 BAO + CMB et `LambdaCDM`, la direction préférée de
> la reconstruction marginale est suffisamment basse pour que l'imposition du
> domaine physique oscillatoire crée une tension de frontière, faible à modérée
> pour l'ordre normal et forte pour l'ordre inversé dans le substitut minimal.

## 9. Ce que C1 ne décide pas

`C1` ne détermine pas :

```text
la forme exacte du profil de vraisemblance DESI ;
la statistique Feldman–Cousins exacte ;
la contribution séparée de chaque likelihood CMB ou point BAO ;
les corrélations avec H_0, Omega_m, A_s, tau, w_0 et w_a ;
la préférence d'ordre après profils NuFIT 6.1 complets ;
l'origine physique ou systématique de la direction négative.
```

## 10. Phase C2 requise

Les produits officiels DESI DR2 publient les chaînes Cobaya et les maxima de
posterior pour plusieurs modèles et priors. La reprise suivante doit :

1. ingérer le jeu `base_mnu` avec CMB de référence ;
2. vérifier le quantile `0.0642 eV` depuis les poids de chaîne ;
3. comparer au jeu à plancher oscillatoire et reconstruire le changement de
   normalisation ;
4. ingérer `base_mnu_w_wa` et mesurer le déplacement conjoint avec `w_0`, `w_a`,
   `H_0` et `Omega_m` ;
5. confronter posterior marginal, profil de likelihood et maxima `iminuit` ;
6. remplacer les Gaussiennes indépendantes de `N1` par les profils numériques de
   NuFIT 6.1 ;
7. publier les scripts, sommes de contrôle des fichiers et diagnostics de
   convergence.

Le script de `C1` comprend déjà un lecteur optionnel des chaînes Cobaya lorsque
leurs fichiers sont disponibles localement. Les sorties officielles ne sont pas
incluses dans le dépôt afin d'éviter de dupliquer plusieurs dizaines de mégaoctets
sans manifeste ni contrôle de provenance.

## 11. Sources primaires et produits officiels

- [JUNO, premier résultat sur le secteur solaire, Nature 654 (2026)](https://doi.org/10.1038/s41586-026-10538-z) ;
- [T2K–NOvA, analyse conjointe, Nature 646 (2025)](https://doi.org/10.1038/s41586-025-09599-3) ;
- [DESI, contraintes neutrino DR2, arXiv:2503.14744 v3](https://arxiv.org/abs/2503.14744) ;
- [documentation officielle des chaînes DESI DR2](https://data.desi.lbl.gov/public/papers/y3/bao-cosmo-params/README.html) ;
- [NuFIT 6.1](https://www.nu-fit.org/?q=node%2F309).

## 12. Verdict C1

```text
plancher NO : 0.058709 +/- 0.000359 eV ;
plancher IO : 0.098840 +/- 0.000708 eV ;
incertitude N1 insuffisante pour absorber le frottement : oui ;
origine immédiate du frottement : direction basse de la reconstruction N3
                                  + frontière + prior ;
ordre inversé plus fortement comprimé : oui ;
reproduction des chaînes officielles : non encore ;
statut : première passe computationnelle concluante comme diagnostic,
         chantier ouvert pour C2.
```
