# Rapport G2.1 — validation de l’instrument numérique `X(z)`

Issue directrice : #63. Branche : `comp/c7-c1-xz-validation`.

## 0. Statut de la porte

```text
statut : exécution complète — passage directeur exécuté ;
G2.1 : clôturable, soumise à validation humaine ;
MCMC / minimisation / posterior : interdits et absents ;
priors scientifiques sur X_i : non définis ;
G2.2 : fermée.
```

Ce rapport consigne l’installation de l’instrument, les tests analytiques,
puis le passage directeur complet exécuté dans l’environnement G1 gelé :

```text
Python 3.12.0 ; CAMB 1.5.4 ; NumPy 1.26.4 ; SciPy 1.13.1 ;
C7C1_DATA_DIR vers les octets BAO officiels hors Git ;
commande : python scripts/test_xz_g2_1.py --full ;
exécutée DEUX FOIS : sorties strictement identiques (diff vide) —
déterminisme bit à bit établi.
```

## 1. Périmètre implémenté

```text
scripts/xz_background_g2_1.py
  - nœuds M2a et M2b, avec X(0)=1 ;
  - splines `natural` et `not-a-knot` séparées ;
  - continuation strictement constante pour z >= 2.33 ;
  - fond direct H_X² = H_ref² + H0² Omega_X,0 [X(z)-1] ;
  - rejet limité aux valeurs non finies ou H_X² <= 0 ;
  - D_H, D_M, D_A et D_V par quadrature ;
  - étalon acoustique `fixed` ou correction différentielle `corrected` ;
  - theta_star et vecteurs BAO/CMB.

scripts/test_xz_g2_1.py
  - tests I1–I7 ;
  - mode analytique sans CAMB ;
  - mode complet sous CAMB 1.5.4 et octets BAO G1 ;
  - sortie JSON/Markdown dans le terminal, sans produit volumineux.
```

L’implémentation ne calcule jamais `w(z)` depuis `X(z)`, n’appelle pas PPF
pour représenter la reconstruction et n’impose pas `X(z)>0`.

## 2. Résultats analytiques déjà exécutés

Commande :

```text
python scripts/test_xz_g2_1.py --analytic-only
```

Environnement auxiliaire du contrôle : Python 3.13.5, NumPy 2.3.5,
SciPy 1.17.0. Ce passage contrôle la structure Python/SciPy ; il ne remplace
pas le passage directeur sous les versions G1.

### I1 / I6 — identité et quadrature sur fond analytique

```text
max |H_X/H_ref - 1|, X=1                    : 0
D_M, quadrature par défaut vs resserrée      : 0
D_M, quad adaptative vs trapèzes 100001 pts  : 6.59e-11 relatif
```

### I2 — interpolation

```text
valeur aux nœuds, M2a/M2b, deux conventions : erreur max 0
not-a-knot, polynômes degré <= 3              : <= 6.67e-16 absolu
natural, constante et linéaire                : <= 4.45e-16 absolu
natural, quadratique/cubique                  : écarts mesurés, attendus
                                                car les conditions naturelles
                                                ne reproduisent pas en général
                                                ces polynômes aux bords
```

Écarts maximaux mesurés pour `natural` :

```text
M2a quadratique : 3.41e-3 ; cubique : 4.38e-4
M2b quadratique : 5.83e-3 ; cubique : 6.93e-4
```

Ces écarts ne sont pas des erreurs d’implémentation : ils documentent l’effet
de la condition aux extrémités, précisément l’objet du contrôle comparatif.

### I3 — frontière haute

```text
X(z>=2.33) - X(2.33), erreur max : 0
```

La dérivée gauche n’est généralement pas nulle ; la continuation constante
crée donc potentiellement une rupture de dérivée, admise et explicitement
rapportée plutôt que masquée.

### I4 — espace signé et fonds invalides

```text
profil test : min X = -0.2041 ; fond fini et H_X²>0
profil fortement négatif : rejet explicite par InvalidBackgroundError
```

### I5 — sensibilité à la convention de spline

Sur un profil signé et oscillant fixé avant calcul :

```text
max |X_natural - X_not-a-knot| : 0.2876
max écart relatif sur H         : 1.18e-2
max écart relatif sur D_M       : 3.29e-2
```

Ce résultat confirme que la convention de spline est une décision
scientifiquement active ; aucune des deux conventions ne peut être attribuée
aux auteurs ou choisie après inspection d’un posterior.

## 3. Passage directeur complet — résultats

Le bloc analytique ré-exécuté sous l’environnement directeur reproduit à
l’identique les valeurs du §2 (obtenues sous l’environnement auxiliaire
Python 3.13.5 / NumPy 2.3.5 / SciPy 1.17.0) : la structure de l’instrument
est insensible au changement d’environnement Python/SciPy testé.

### 3.1 Identité complète `X_i = 1 ≡ LambdaCDM` (I1, CAMB)

Aux deux points G1 verrouillés (`g1_reference` : H0 = 67.36,
ombh2 = 0.02237, Omega_m = 0.3152 ; `g1_lcdm_map` : H0 = 68.3526,
ombh2 = 0.022410, Omega_m = 0.300539), pour M2a et M2b, `natural` et
`not-a-knot`, en modes `fixed` et `corrected` (8 combinaisons par point) :

```text
grandeur                          plancher mesuré (max sur tout)
|H_X/H_ref - 1|                   0 (exact)
|D_M/D_M_ref - 1|                 4.24e-16
13 prédictions BAO (relatif)      4.41e-16
  (D_V, D_M, D_H sur r_drag : couvertes par le vecteur BAO)
|Delta r_drag|                    0 (exact)
|Delta r_star|                    0 (exact)
|Delta theta_star| (absolu)       4.49e-12   (~4.3e-10 relatif)
|Delta chi2_BAO|                  4.58e-13
|Delta chi2_CMB|                  2.72e-6
```

Le plancher `chi2_CMB` est entièrement expliqué par l’amplification de
l’écart `theta_star` (~1.7e-6 sigma_theta) par la covariance CMB inverse ;
il ne traduit aucun défaut supplémentaire. L’identité est indépendante de
la convention de spline et du traitement acoustique, comme attendu pour
`X ≡ 1`.

### 3.2 Sensibilité à la convention de spline (I5, profils fixés a priori)

```text
profil              max|dX|   BAO rel.   Delta chi2_BAO (nat - nak)
positive_gentle     0.1552    2.24e-3        +3.99
signed_crossing     0.3396    2.51e-2      +188.72
oscillatory         3.7326    6.87e-2      -174.79
```

Confirmation quantitative sous CAMB du constat analytique : la convention
d’extrémités est une décision scientifiquement active — sur profils de
stress, elle déplace `chi2_BAO` de valeurs comparables au signal
cosmologique lui-même. Elle ne peut être ni réduite à un détail numérique
ni choisie après inspection d’un posterior.

### 3.3 Traitement acoustique `fixed` / `corrected` (I4)

Sur les trois profils testés, sous les deux conventions :

```text
|Delta r_drag|  (corrected - fixed)   <= 2.14e-12 Mpc
|Delta r_star|  (corrected - fixed)   <= 2.11e-12 Mpc
|Delta theta_star|                    <= 1.51e-16
BAO (relatif)                         <= 1.46e-14
|Delta chi2_BAO|                      <= 3.28e-10
```

Constat borné aux profils testés : sous la continuation constante
`X(z >= 2.33) = X(2.33)`, la contribution de `X` à l’époque acoustique est
noyée par la densité de matière-rayonnement ; `fixed` et `corrected` sont
opérationnellement équivalents aux planchers ci-dessus. Un profil futur qui
briserait cette équivalence signalerait une influence pré-recombinaison de
`X` et devrait être signalé, non absorbé.

### 3.4 Stabilité numérique (I6)

```text
quadrature par défaut vs resserrée : H et D_M : 0 ; BAO <= 9.71e-15 ;
r_drag : zmax 1e6 -> 1e7 : 1.34e-9 Mpc ; 1e7 -> 1e8 : 1.42e-12 Mpc ;
r_star : zmax 1e6 -> 1e7 : 1.25e-9 Mpc ; 1e7 -> 1e8 : 1.42e-12 Mpc ;
reproductibilité : deux passages complets bit à bit identiques.
```

La borne haute acoustique `zmax = 1e7` est convergée (sa variation vers
`1e8` est au niveau 1e-12 Mpc) ; `1e6` est insuffisante (1e-9 Mpc).

## 4. Tolérances T8–T12 — proposition fondée sur les planchers mesurés

Marges d’un facteur >= 100 sur chaque plancher, sauf mention. Soumises à
ratification humaine.

```text
T8 — identité LambdaCDM des observables de fond (à ré-exécuter à chaque
     modification de l'instrument, aux deux points G1, 8 combinaisons) :
     |H_X/H_ref - 1| et |D_M/D_M_ref - 1|   <= 1e-13  (mesuré <= 4.3e-16) ;
     13 prédictions BAO (relatif)           <= 1e-13  (mesuré <= 4.5e-16) ;
     |Delta r_drag|, |Delta r_star|         <= 1e-10 Mpc (mesuré 0) ;
     |Delta theta_star| (absolu)            <= 1e-9   (mesuré <= 4.5e-12) ;
     |Delta chi2_BAO|                       <= 1e-10  (mesuré <= 4.6e-13) ;
     |Delta chi2_CMB|                       <= 1e-3   (mesuré <= 2.8e-6 ;
       plancher dominé par l'amplification C^-1 de theta_star).

T9 — interpolation et nœuds :
     valeurs aux nœuds (M2a/M2b, 2 conventions) <= 1e-14 (mesuré 0) ;
     not-a-knot sur polynômes degré <= 3        <= 1e-13 (mesuré <= 6.7e-16) ;
     natural sur constante/linéaire             <= 1e-13 (mesuré <= 4.5e-16) ;
     natural sur quadratique/cubique : PROPRIÉTÉ de la convention
       (écarts 4.4e-4 à 5.8e-3 documentés), pas une tolérance.

T10 — frontière z = 2.33 :
     |X(z>=2.33) - X(2.33)|                  <= 1e-14 (mesuré 0) ;
     la rupture de dérivée gauche à 2.33 est une propriété déclarée de la
     continuation ratifiée : rapportée (ex. -4.49 natural, -20.67
     not-a-knot sur profil test), jamais lissée silencieusement.

T11 — stabilité quadrature / borne acoustique :
     quadrature par défaut vs resserrée : BAO  <= 1e-12 (mesuré <= 9.8e-15) ;
     D_M quad adaptative vs trapèzes           <= 1e-8  (mesuré 6.6e-11) ;
     borne acoustique : zmax = 1e7 retenue ; contrôle 1e7 vs 1e8
       <= 1e-10 Mpc (mesuré 1.4e-12) ; zmax = 1e6 interdite (1.3e-9) ;
     déterminisme : deux passages complets bit à bit identiques exigés.

T12 — convention de spline et traitement acoustique :
     (a) spline : natural et not-a-knot sont deux VARIANTES SCIENTIFIQUES
         déclarées, portées séparément dans tout produit G2.2+ ; aucun
         choix post-hoc ; effets mesurés sur profils de stress :
         Delta chi2_BAO de +3.99 à ±189 — jamais requalifiables en
         « erreur numérique » ;
     (b) acoustique : corrected par défaut, fixed en contrôle ;
         équivalence sous continuation constante exigée à
         |Delta chi2_BAO| <= 1e-8 (mesuré <= 3.3e-10) et
         |Delta r_drag,star| <= 1e-10 Mpc (mesuré <= 2.2e-12) ;
         toute rupture d'équivalence est un signalement obligatoire.
```

## 5. Verdict final de G2.1

```text
instrument structurel : cohérent (analytique + directeur, deux
  environnements Python concordants) ;
identité CAMB X_i=1 ≡ LambdaCDM : établie aux deux points G1,
  8 combinaisons par point, planchers 1e-16 à 1e-12 (chi2_CMB 2.8e-6,
  expliqué) ;
étalon acoustique : fixed ≡ corrected sous continuation constante,
  aux planchers mesurés, sur les profils testés ;
convention de spline : scientifiquement active — deux variantes
  déclarées à porter séparément (T12a) ;
stabilité : quadratures convergées, zmax=1e7 convergée,
  déterminisme bit à bit établi (deux passages identiques) ;
tolérances T8–T12 : proposées (§4), à ratifier ;
MCMC / minimisation / priors X_i : absents, conformes à l'interdit ;

verdict proposé : VALIDÉ — G2.1 clôturable après ratification humaine
  de T8–T12 ; G2.2 / G2.3 : fermées jusqu'à cette décision.
```

## Annexe — sortie brute du passage directeur (identique sur les deux exécutions)

# Sortie brute G2.1 � mesures I1�I7

Cette sortie ne constitue ni un posterior ni une pr�f�rence de mod�le.

```json
{
  "analytic": {
    "I1_I6_analytic_identity_stability": {
      "DM_default_vs_tight_rel_max": 0.0,
      "DM_quad_vs_trapezoid_rel_max": 6.590911006302019e-11,
      "H_rel_max": 0.0
    },
    "I2_interpolation": {
      "M2a_natural": {
        "node_abs_max": 0.0
      },
      "M2a_not-a-knot": {
        "node_abs_max": 0.0
      },
      "M2b_natural": {
        "node_abs_max": 0.0
      },
      "M2b_not-a-knot": {
        "node_abs_max": 0.0
      },
      "polynomials_abs_max": {
        "M2a_natural_constant": 0.0,
        "M2a_natural_cubic": 0.00043829996474598065,
        "M2a_natural_linear": 1.1102230246251565e-16,
        "M2a_natural_quadratic": 0.003405257851459953,
        "M2a_not-a-knot_constant": 0.0,
        "M2a_not-a-knot_cubic": 4.440892098500626e-16,
        "M2a_not-a-knot_linear": 2.220446049250313e-16,
        "M2a_not-a-knot_quadratic": 2.220446049250313e-16,
        "M2b_natural_constant": 0.0,
        "M2b_natural_cubic": 0.0006927199309572085,
        "M2b_natural_linear": 2.220446049250313e-16,
        "M2b_natural_quadratic": 0.005828159368054142,
        "M2b_not-a-knot_constant": 0.0,
        "M2b_not-a-knot_cubic": 6.661338147750939e-16,
        "M2b_not-a-knot_linear": 4.440892098500626e-16,
        "M2b_not-a-knot_quadratic": 3.3306690738754696e-16
      }
    },
    "I3_boundary": {
      "natural": {
        "constant_extension_abs_max": 0.0,
        "left_derivative_at_2p33": -4.489716927128587,
        "right_derivative_defined": 0.0
      },
      "not-a-knot": {
        "constant_extension_abs_max": 0.0,
        "left_derivative_at_2p33": -20.674891224072546,
        "right_derivative_defined": 0.0
      }
    },
    "I4_signed_domain": {
      "invalid_profile_rejected": true,
      "signed_profile_min_H2": 4900.0,
      "signed_profile_min_X": -0.20411265739572057
    },
    "I5_spline_sensitivity_analytic": {
      "DM_rel_max": 0.032911648969112,
      "H_rel_max": 0.011837884044818453,
      "X_abs_max": 0.28763603776737323
    }
  },
  "camb_full": {
    "I1_CAMB_identity": {
      "g1_lcdm_map_M2a_natural": {
        "BAO_corrected_rel_max": 3.266024952578764e-16,
        "BAO_fixed_rel_max": 3.266024952578764e-16,
        "CMB_corrected_abs_max": 3.1112994125503945e-12,
        "CMB_fixed_abs_max": 3.1112994125503945e-12,
        "DM_rel_max": 4.2438814862380456e-16,
        "H_rel_max": 0.0,
        "chi2_BAO_corrected_abs": 1.474376176702208e-13,
        "chi2_BAO_fixed_abs": 1.474376176702208e-13,
        "chi2_CMB_corrected_abs": 7.103578005818179e-07,
        "chi2_CMB_fixed_abs": 7.103578005818179e-07,
        "rdrag_corrected_abs": 0.0,
        "rdrag_fixed_abs": 0.0,
        "rstar_corrected_abs": 0.0,
        "rstar_fixed_abs": 0.0,
        "theta_corrected_abs": 3.1112994125503945e-12,
        "theta_fixed_abs": 3.1112994125503945e-12
      },
      "g1_lcdm_map_M2a_not-a-knot": {
        "BAO_corrected_rel_max": 3.266024952578764e-16,
        "BAO_fixed_rel_max": 3.266024952578764e-16,
        "CMB_corrected_abs_max": 3.1112994125503945e-12,
        "CMB_fixed_abs_max": 3.1112994125503945e-12,
        "DM_rel_max": 4.2438814862380456e-16,
        "H_rel_max": 0.0,
        "chi2_BAO_corrected_abs": 1.474376176702208e-13,
        "chi2_BAO_fixed_abs": 1.474376176702208e-13,
        "chi2_CMB_corrected_abs": 7.103578005818179e-07,
        "chi2_CMB_fixed_abs": 7.103578005818179e-07,
        "rdrag_corrected_abs": 0.0,
        "rdrag_fixed_abs": 0.0,
        "rstar_corrected_abs": 0.0,
        "rstar_fixed_abs": 0.0,
        "theta_corrected_abs": 3.1112994125503945e-12,
        "theta_fixed_abs": 3.1112994125503945e-12
      },
      "g1_lcdm_map_M2b_natural": {
        "BAO_corrected_rel_max": 3.266024952578764e-16,
        "BAO_fixed_rel_max": 3.266024952578764e-16,
        "CMB_corrected_abs_max": 2.195238782420894e-12,
        "CMB_fixed_abs_max": 2.195238782420894e-12,
        "DM_rel_max": 4.2438814862380456e-16,
        "H_rel_max": 0.0,
        "chi2_BAO_corrected_abs": 1.474376176702208e-13,
        "chi2_BAO_fixed_abs": 1.474376176702208e-13,
        "chi2_CMB_corrected_abs": 5.01206618874761e-07,
        "chi2_CMB_fixed_abs": 5.01206618874761e-07,
        "rdrag_corrected_abs": 0.0,
        "rdrag_fixed_abs": 0.0,
        "rstar_corrected_abs": 0.0,
        "rstar_fixed_abs": 0.0,
        "theta_corrected_abs": 2.195238782420894e-12,
        "theta_fixed_abs": 2.195238782420894e-12
      },
      "g1_lcdm_map_M2b_not-a-knot": {
        "BAO_corrected_rel_max": 3.266024952578764e-16,
        "BAO_fixed_rel_max": 3.266024952578764e-16,
        "CMB_corrected_abs_max": 2.195238782420894e-12,
        "CMB_fixed_abs_max": 2.195238782420894e-12,
        "DM_rel_max": 4.2438814862380456e-16,
        "H_rel_max": 0.0,
        "chi2_BAO_corrected_abs": 1.474376176702208e-13,
        "chi2_BAO_fixed_abs": 1.474376176702208e-13,
        "chi2_CMB_corrected_abs": 5.01206618874761e-07,
        "chi2_CMB_fixed_abs": 5.01206618874761e-07,
        "rdrag_corrected_abs": 0.0,
        "rdrag_fixed_abs": 0.0,
        "rstar_corrected_abs": 0.0,
        "rstar_fixed_abs": 0.0,
        "theta_corrected_abs": 2.195238782420894e-12,
        "theta_fixed_abs": 2.195238782420894e-12
      },
      "g1_reference_M2a_natural": {
        "BAO_corrected_rel_max": 4.409610555329086e-16,
        "BAO_fixed_rel_max": 4.409610555329086e-16,
        "CMB_corrected_abs_max": 3.1528720606521787e-12,
        "CMB_fixed_abs_max": 3.1528720606521787e-12,
        "DM_rel_max": 2.8111216401697903e-16,
        "H_rel_max": 0.0,
        "chi2_BAO_corrected_abs": 4.583000645652646e-13,
        "chi2_BAO_fixed_abs": 4.583000645652646e-13,
        "chi2_CMB_corrected_abs": 1.9106926760770193e-06,
        "chi2_CMB_fixed_abs": 1.9106926760770193e-06,
        "rdrag_corrected_abs": 0.0,
        "rdrag_fixed_abs": 0.0,
        "rstar_corrected_abs": 0.0,
        "rstar_fixed_abs": 0.0,
        "theta_corrected_abs": 3.1528720606521787e-12,
        "theta_fixed_abs": 3.1528720606521787e-12
      },
      "g1_reference_M2a_not-a-knot": {
        "BAO_corrected_rel_max": 4.409610555329086e-16,
        "BAO_fixed_rel_max": 4.409610555329086e-16,
        "CMB_corrected_abs_max": 3.1528720606521787e-12,
        "CMB_fixed_abs_max": 3.1528720606521787e-12,
        "DM_rel_max": 2.8111216401697903e-16,
        "H_rel_max": 0.0,
        "chi2_BAO_corrected_abs": 4.583000645652646e-13,
        "chi2_BAO_fixed_abs": 4.583000645652646e-13,
        "chi2_CMB_corrected_abs": 1.9106926760770193e-06,
        "chi2_CMB_fixed_abs": 1.9106926760770193e-06,
        "rdrag_corrected_abs": 0.0,
        "rdrag_fixed_abs": 0.0,
        "rstar_corrected_abs": 0.0,
        "rstar_fixed_abs": 0.0,
        "theta_corrected_abs": 3.1528720606521787e-12,
        "theta_fixed_abs": 3.1528720606521787e-12
      },
      "g1_reference_M2b_natural": {
        "BAO_corrected_rel_max": 4.409610555329086e-16,
        "BAO_fixed_rel_max": 4.409610555329086e-16,
        "CMB_corrected_abs_max": 4.493320646115073e-12,
        "CMB_fixed_abs_max": 4.493320646115073e-12,
        "DM_rel_max": 2.8111216401697903e-16,
        "H_rel_max": 0.0,
        "chi2_BAO_corrected_abs": 4.476419235288631e-13,
        "chi2_BAO_fixed_abs": 4.476419235288631e-13,
        "chi2_CMB_corrected_abs": 2.7230278081269432e-06,
        "chi2_CMB_fixed_abs": 2.7230278081269432e-06,
        "rdrag_corrected_abs": 0.0,
        "rdrag_fixed_abs": 0.0,
        "rstar_corrected_abs": 0.0,
        "rstar_fixed_abs": 0.0,
        "theta_corrected_abs": 4.493320646115073e-12,
        "theta_fixed_abs": 4.493320646115073e-12
      },
      "g1_reference_M2b_not-a-knot": {
        "BAO_corrected_rel_max": 4.409610555329086e-16,
        "BAO_fixed_rel_max": 4.409610555329086e-16,
        "CMB_corrected_abs_max": 4.493320646115073e-12,
        "CMB_fixed_abs_max": 4.493320646115073e-12,
        "DM_rel_max": 2.8111216401697903e-16,
        "H_rel_max": 0.0,
        "chi2_BAO_corrected_abs": 4.476419235288631e-13,
        "chi2_BAO_fixed_abs": 4.476419235288631e-13,
        "chi2_CMB_corrected_abs": 2.7230278081269432e-06,
        "chi2_CMB_fixed_abs": 2.7230278081269432e-06,
        "rdrag_corrected_abs": 0.0,
        "rdrag_fixed_abs": 0.0,
        "rstar_corrected_abs": 0.0,
        "rstar_fixed_abs": 0.0,
        "theta_corrected_abs": 4.493320646115073e-12,
        "theta_fixed_abs": 4.493320646115073e-12
      }
    },
    "I4_I5_acoustic_and_spline_sensitivity": {
      "oscillatory": {
        "BAO_nat_nak_rel_max": 0.06870677309924239,
        "X_nak_min": -4.014169823509499,
        "X_nat_min": -0.7420852901228724,
        "X_nat_nak_abs_max": 3.7325974330938902,
        "chi2_BAO_nat_minus_nak": -174.78741100164183,
        "natural_BAO_corrected_vs_fixed_rel_max": 1.4527529408734504e-14,
        "natural_chi2_BAO_corrected_minus_fixed": 1.1141310096718371e-11,
        "natural_rdrag_corrected_minus_fixed": -2.1316282072803006e-12,
        "natural_rstar_corrected_minus_fixed": -2.1032064978498966e-12,
        "natural_theta_corrected_minus_fixed": -1.5092094240998222e-16,
        "not-a-knot_BAO_corrected_vs_fixed_rel_max": 1.451930203175972e-14,
        "not-a-knot_chi2_BAO_corrected_minus_fixed": -1.7564616427989677e-11,
        "not-a-knot_rdrag_corrected_minus_fixed": -2.1316282072803006e-12,
        "not-a-knot_rstar_corrected_minus_fixed": -2.1032064978498966e-12,
        "not-a-knot_theta_corrected_minus_fixed": -1.474514954580286e-16
      },
      "positive_gentle": {
        "BAO_nat_nak_rel_max": 0.0022444218967308145,
        "X_nak_min": 0.799899747636211,
        "X_nat_min": 0.7995201594126987,
        "X_nat_nak_abs_max": 0.15522946677287952,
        "chi2_BAO_nat_minus_nak": 3.9867364276772292,
        "natural_BAO_corrected_vs_fixed_rel_max": 0.0,
        "natural_chi2_BAO_corrected_minus_fixed": 0.0,
        "natural_rdrag_corrected_minus_fixed": 0.0,
        "natural_rstar_corrected_minus_fixed": 0.0,
        "natural_theta_corrected_minus_fixed": 0.0,
        "not-a-knot_BAO_corrected_vs_fixed_rel_max": 0.0,
        "not-a-knot_chi2_BAO_corrected_minus_fixed": 0.0,
        "not-a-knot_rdrag_corrected_minus_fixed": 0.0,
        "not-a-knot_rstar_corrected_minus_fixed": 0.0,
        "not-a-knot_theta_corrected_minus_fixed": 0.0
      },
      "signed_crossing": {
        "BAO_nat_nak_rel_max": 0.025070127837649354,
        "X_nak_min": -0.20321357877328486,
        "X_nat_min": -0.20756469747680747,
        "X_nat_nak_abs_max": 0.3396422085447146,
        "chi2_BAO_nat_minus_nak": 188.71686685296072,
        "natural_BAO_corrected_vs_fixed_rel_max": 9.738516380009375e-15,
        "natural_chi2_BAO_corrected_minus_fixed": -3.2741809263825417e-10,
        "natural_rdrag_corrected_minus_fixed": 1.4210854715202004e-12,
        "natural_rstar_corrected_minus_fixed": 1.4210854715202004e-12,
        "natural_theta_corrected_minus_fixed": 9.8879238130678e-17,
        "not-a-knot_BAO_corrected_vs_fixed_rel_max": 9.714599081866318e-15,
        "not-a-knot_chi2_BAO_corrected_minus_fixed": -3.042259777430445e-10,
        "not-a-knot_rdrag_corrected_minus_fixed": 1.4210854715202004e-12,
        "not-a-knot_rstar_corrected_minus_fixed": 1.4210854715202004e-12,
        "not-a-knot_theta_corrected_minus_fixed": 9.8879238130678e-17
      }
    },
    "I6_numerical_stability": {
      "BAO_default_vs_tight_rel_max": 9.714599081866318e-15,
      "DM_default_vs_tight_rel_max": 0.0,
      "H_default_vs_tight_rel_max": 0.0,
      "rdrag_zmax_1e6_minus_1e7": 1.3376109109231038e-09,
      "rdrag_zmax_1e7_minus_1e8": 1.4210854715202004e-12,
      "rstar_zmax_1e6_minus_1e7": 1.2491625511756865e-09,
      "rstar_zmax_1e7_minus_1e8": 1.4210854715202004e-12
    }
  }
}
```
