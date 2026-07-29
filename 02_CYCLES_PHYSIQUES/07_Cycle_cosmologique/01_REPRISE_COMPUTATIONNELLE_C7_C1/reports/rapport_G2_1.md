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

Complément G2.1d intégré : (i) `_dm_scalar` transmet désormais à `quad`
tous les nœuds strictement intérieurs à l'intervalle, y compris z = 2,33
pour les intégrales allant jusqu'à z_star (la rupture de dérivée admise y
est signalée au quadrateur) ; (ii) I6 mesure la stabilité default/tight de
`D_M(z_star)`, `theta_star` et `chi2_CMB` pour des profils non constants,
sous les deux conventions. Le passage --full a été ré-exécuté deux fois
après ces modifications : diff vide entre les deux sorties. Seuls les
planchers CMB de l'identité I1 changent (ils s'améliorent, §3.1) ; les
blocs BAO, I4 et I5 sont inchangés au bit près.

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
|Delta theta_star| (absolu)       1.22e-13   (~1.2e-11 relatif)
|Delta chi2_BAO|                  4.58e-13
|Delta chi2_CMB|                  7.40e-8
```

Avant le complément G2.1d, les planchers `theta_star` et `chi2_CMB`
valaient 4.49e-12 et 2.72e-6 : l'exclusion de z = 2,33 des points de
quadrature pour l'intégrale jusqu'à z_star en était la source dominante
(amélioration d'un facteur ~37 après correction). Le plancher `chi2_CMB`
résiduel reste entièrement expliqué par l'amplification de l'écart
`theta_star` par la covariance CMB inverse ; il ne traduit aucun défaut
supplémentaire. L'identité est indépendante de la convention de spline et
du traitement acoustique, comme attendu pour `X ≡ 1`.

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

### 3.5 Stabilité CMB default/tight pour profils non constants (G2.1d)

Pour `signed_crossing` et `oscillatory`, sous `natural` et `not-a-knot`,
modes `fixed` et `corrected` :

```text
grandeur                              plancher mesuré (max)
D_M(z_star) default vs tight (rel)    1.86e-10
theta_star default vs tight (abs)     1.92e-12
chi2_CMB default vs tight (abs)       2.34e-4
```

Le plancher `chi2_CMB` est proportionnel au résidu CMB standardisé du
profil de stress (très grand pour ces profils) ; au voisinage des données
(résidus d'ordre 1), l'effet attendu est d'ordre 1e-6. Les valeurs
`fixed` et `corrected` de ces stabilités coïncident à ~1e-16 près.

### 3.6 Voie de calcul indépendante (I8) — validation R3

Vérificateur construit sans aucune méthode de `XZBackground` ni
`scipy.interpolate` : spline cubique par résolution directe du système
des moments (`numpy.linalg.solve`, conditions `natural` et `not-a-knot`
explicites) ; `D_M` par Simpson composite en variable `u = sqrt(a)`,
`a = 1/(1+z)`, avec césure explicite à z = 2,33 ; grille fixe et contrôle
de Richardson. Dépendances partagées, déclarées : valeurs nodales du
profil ; objet `H_ref` (CAMB) ; constantes physiques.

```text
étalonnage du vérificateur sur solution analytique exacte (EdS,
  D_M = (2c/H0)(1 - 1/sqrt(1+z))) : erreur <= 3.6e-16 ;

accord voie principale / voie indépendante (max sur les 2 profils
de stress x 2 conventions) :
  X(z) (scipy vs système des moments)      <= 8.9e-15
  H_X(z)                                   <= 5.2e-16
  D_M aux 6 z BAO (quad-z vs Simpson-u)    <= 5.7e-16
  D_M(z_star)                              <= 1.85e-10
    (Richardson du vérificateur : 1.8e-13 — le plancher 1.85e-10 est
     attribuable à la tolérance quad de la voie principale, non au
     vérificateur)
  theta_star (fixed)                       <= 1.92e-12
  chi2_CMB (fixed)                         <= 2.33e-4  (même origine)
```

### 3.7 Tests adversariaux (I9) — fautes injectées et gardes

Chaque faute est injectée dans une variante volontairement défectueuse ;
la garde désignée doit la détecter, le témoin correct restant sous le
seuil. Profil `signed_crossing`, M2a, `natural`.

```text
faute                                garde                   déviation   témoin      détectée
F1 signe inversé dans corr. de H²    I8-H                    5.4e-1      2.0e-16     OUI
F2 facteur de variable omis (D_M)    I8-D_M                  5.3e-1      2.9e-16     OUI
F3 nœud déplacé (1/3 -> 0.35)        I8-X (points sondes)    4.2e-2      8.9e-16     OUI
F4 raccord z=2.33 supprimé           I3 (continuation)       6.4e-1      0           OUI
F5 Omega_X,0 faux (x1.05)            I8-H                    1.7e-2      2.0e-16     OUI
toutes fautes détectées : OUI
```

Aveuglements documentés (et pris en charge par les gardes I8) :
l'identité I1 (X = 1) est **aveugle** à F1 et F5, car la correction
s'annule à X = 1 quel que soit son signe ou son échelle ; le test I2
évalué aux nœuds du profil fautif serait aveugle à F3.

### 3.8 Classification épistémique R1 / R2 / R3 de chaque test

Règle appliquée : un test ne compte comme confirmation externe (R3) que
si sa référence ne dépend ni du même objet logiciel, ni de la même
discrétisation, ni du même chemin algébrique que la quantité testée.

| test | quantité testée | référence | dépendances partagées | statut | démontre | ne démontre pas |
|---|---|---|---|---|---|---|
| double exécution `--full` | sortie complète | seconde exécution | tout | **R1** | déterminisme | justesse |
| I1 : H, r_drag, r_star (X=1) | branchement X=1 | valeurs CAMB | même objet CAMB ; identité par construction | **R2** | câblage correct du cas X=1 | signe/échelle de la correction (aveugle à F1, F5) |
| I1 : D_M, theta, chi2 (X=1) | quadrature en z | distance interne CAMB | même H (CAMB) ; intégrateurs distincts | **R2** (+R3 limité à l'étape d'intégration) | quad-z reproduit l'intégration CAMB | indépendance de la source H |
| I2 : valeurs aux nœuds | interpolant | valeurs imposées | même spline | **R2** | interpolation exacte | position des nœuds (aveugle à F3) |
| I2 : polynômes P<=3 | interpolant | forme analytique exacte | aucune | **R3** (sous-espace P<=3) | justesse sur P<=3 | comportement hors P<=3 |
| I3 : continuation | X(z>=2.33) | valeur nodale | même profil | **R2** | règle appliquée | pertinence physique du raccord |
| I4 : domaine signé / rejet | H_X² | règle déclarée | même objet | **R2** | conformité à la règle | — |
| I5 : sensibilité spline | X, H, D_M, chi2 | autre convention | tout partagé | **caractérisation** (ni R1/R2/R3) | ampleur de la convention | aucune justesse |
| I6 : default/tight, zmax | D_M, BAO, θ★, χ² | mêmes méthodes, tolérances resserrées | même intégrateur et discrétisation | **R2** (stabilité) | insensibilité aux tolérances | justesse (même chemin) |
| I8 : X manuel | X(z) | système des moments (numpy.linalg.solve) | valeurs nodales seulement | **R3** | justesse de l'interpolation principale | — |
| I8 : H_X | H_X(z) | reconstruction algébrique indépendante | H_ref (CAMB) | **R3** (chemin algébrique) | câblage correct de la correction | justesse de H_ref |
| I8 : D_M | D_M | Simpson en u=sqrt(a), césure 2.33, grille fixe | source H | **R3** (variable + intégrateur + discrétisation) | justesse de la quadrature principale | justesse du H partagé |
| I8 : étalonnage EdS | vérificateur D_M | solution analytique exacte | aucune | **R3** | fiabilité du vérificateur | — |
| I9 : F1–F5 | les gardes elles-mêmes | fautes injectées | — | **méta-validation** | les gardes détectent leurs fautes | exhaustivité des fautes |

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

T11 — stabilité quadrature / borne acoustique (COMPLÉTÉ G2.1d) :
     quadrature par défaut vs resserrée : BAO  <= 1e-12 (mesuré <= 9.8e-15) ;
     D_M quad adaptative vs trapèzes           <= 1e-8  (mesuré 6.6e-11) ;
     borne acoustique : zmax = 1e7 retenue ; contrôle 1e7 vs 1e8
       <= 1e-10 Mpc (mesuré 1.4e-12) ; zmax = 1e6 interdite (1.3e-9) ;
     déterminisme : deux passages complets bit à bit identiques exigés ;
     -- planchers CMB ajoutés (profils non constants, 2 conventions) :
     D_M(z_star) default vs tight (rel)        <= 1e-8  (mesuré <= 1.9e-10) ;
     theta_star default vs tight (abs)         <= 1e-10 (mesuré <= 2.0e-12) ;
     chi2_CMB default vs tight (abs), profils
       de stress                               <= 2e-2  (mesuré <= 2.4e-4 ;
       plancher proportionnel au résidu CMB standardisé du profil) ;
     -- voie indépendante et gardes (règle épistémique) :
     à chaque modification de l'instrument, ré-exécuter I8 et I9 :
       X (scipy vs moments)      <= 1e-12 (mesuré <= 8.9e-15) ;
       H_X                       <= 1e-13 (mesuré <= 5.2e-16) ;
       D_M aux z BAO             <= 1e-13 (mesuré <= 5.7e-16) ;
       étalonnage EdS            <= 1e-13 (mesuré <= 3.6e-16) ;
       fautes F1-F5              toutes détectées, sans exception.

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
         RÉÉVALUATION G2.1d : conclusion inchangée — l'équivalence
         fixed/corrected persiste dans le secteur CMB pour les profils
         non constants (stabilités theta/chi2 identiques aux deux modes
         à ~1e-16 près) ; aucun résultat contradictoire.
```

T8, T9, T10 et T12(a) : inchangés, conformément à G2.1d (aucun résultat
contradictoire ; les marges de T8 sur theta_star et chi2_CMB se sont
élargies d'un facteur ~37 après la correction du point de quadrature).

## 5. Verdict final de G2.1 — séparé par niveau épistémique

Conformément à la règle transversale, « validé » n'est jamais employé ici
sans précision du niveau acquis.

```text
reproductibilité R1 :
  ACQUISE — deux exécutions complètes bit à bit identiques, répétées
  après chaque modification de l'instrument (G2.1c, G2.1d) ;

cohérence interne R2 :
  ACQUISE — identité X=1 (planchers 1e-16 à 1e-13 ; chi2_CMB 7.4e-8,
  expliqué), valeurs aux nœuds, continuation constante, domaine signé
  et rejets, stabilité default/tight (BAO et CMB), borne acoustique
  convergée ;

validation indépendante R3 :
  ACQUISE POUR LES QUANTITÉS CENTRALES, avec dépendances partagées
  déclarées :
    - interpolation X(z) : spline par système des moments,
      accord <= 8.9e-15 ;
    - H_X(z) : reconstruction algébrique indépendante,
      accord <= 5.2e-16 ;
    - D_M : Simpson en u=sqrt(a) avec césure z=2.33, étalonné sur
      solution analytique EdS exacte (3.6e-16),
      accord <= 5.7e-16 (z BAO) et <= 1.85e-10 (z_star, borné par la
      tolérance quad de la voie principale) ;
    - interpolant sur P<=3 : référence analytique exacte ;
  et méta-validation des gardes : fautes F1-F5 toutes détectées ;

limites restantes :
  - H_ref (CAMB 1.5.4) demeure une dépendance partagée de toutes les
    voies : aucune validation R3 de CAMB lui-même n'est revendiquée ;
  - r_star, r_drag et la correction acoustique reposent sur les étalons
    CAMB et le sound_speed partagés : leur statut est R2 + stabilité,
    pas R3 ;
  - chi2_CMB hérite du plancher 1.85e-10 de D_M(z_star) : ~2.3e-4 sur
    profils de stress, ~1e-6 attendu au voisinage des données ;
  - la liste de fautes F1-F5 n'est pas exhaustive ;
  - I5 est une caractérisation de convention, pas une validation.

MCMC / minimisation / posterior / priors X_i : absents, conformes ;
G2.1 : clôturable sur la base R1 + R2 + R3 ci-dessus, sous ratification
humaine de T8-T12 ; G2.2 / G2.3 : fermées jusqu'à cette décision.
```

## Annexe — sortie brute du passage directeur final (identique sur les deux exécutions, complément G2.1d inclus)

# Sortie brute G2.1 — mesures I1–I7

Cette sortie ne constitue ni un posterior ni une préférence de modèle.

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
        "BAO_corrected_rel_max": 4.899037428868147e-16,
        "BAO_fixed_rel_max": 4.899037428868147e-16,
        "CMB_corrected_abs_max": 1.6323747908941755e-14,
        "CMB_fixed_abs_max": 1.6323747908941755e-14,
        "DM_rel_max": 4.2438814862380456e-16,
        "H_rel_max": 0.0,
        "chi2_BAO_corrected_abs": 1.900701818158268e-13,
        "chi2_BAO_fixed_abs": 1.900701818158268e-13,
        "chi2_CMB_corrected_abs": 3.726955188909642e-09,
        "chi2_CMB_fixed_abs": 3.726955188909642e-09,
        "rdrag_corrected_abs": 0.0,
        "rdrag_fixed_abs": 0.0,
        "rstar_corrected_abs": 0.0,
        "rstar_fixed_abs": 0.0,
        "theta_corrected_abs": 1.6323747908941755e-14,
        "theta_fixed_abs": 1.6323747908941755e-14
      },
      "g1_lcdm_map_M2a_not-a-knot": {
        "BAO_corrected_rel_max": 4.899037428868147e-16,
        "BAO_fixed_rel_max": 4.899037428868147e-16,
        "CMB_corrected_abs_max": 1.6323747908941755e-14,
        "CMB_fixed_abs_max": 1.6323747908941755e-14,
        "DM_rel_max": 4.2438814862380456e-16,
        "H_rel_max": 0.0,
        "chi2_BAO_corrected_abs": 1.900701818158268e-13,
        "chi2_BAO_fixed_abs": 1.900701818158268e-13,
        "chi2_CMB_corrected_abs": 3.726955188909642e-09,
        "chi2_CMB_fixed_abs": 3.726955188909642e-09,
        "rdrag_corrected_abs": 0.0,
        "rdrag_fixed_abs": 0.0,
        "rstar_corrected_abs": 0.0,
        "rstar_fixed_abs": 0.0,
        "theta_corrected_abs": 1.6323747908941755e-14,
        "theta_fixed_abs": 1.6323747908941755e-14
      },
      "g1_lcdm_map_M2b_natural": {
        "BAO_corrected_rel_max": 4.899037428868147e-16,
        "BAO_fixed_rel_max": 4.899037428868147e-16,
        "CMB_corrected_abs_max": 1.6323747908941755e-14,
        "CMB_fixed_abs_max": 1.6323747908941755e-14,
        "DM_rel_max": 4.2438814862380456e-16,
        "H_rel_max": 0.0,
        "chi2_BAO_corrected_abs": 1.900701818158268e-13,
        "chi2_BAO_fixed_abs": 1.900701818158268e-13,
        "chi2_CMB_corrected_abs": 3.726955188909642e-09,
        "chi2_CMB_fixed_abs": 3.726955188909642e-09,
        "rdrag_corrected_abs": 0.0,
        "rdrag_fixed_abs": 0.0,
        "rstar_corrected_abs": 0.0,
        "rstar_fixed_abs": 0.0,
        "theta_corrected_abs": 1.6323747908941755e-14,
        "theta_fixed_abs": 1.6323747908941755e-14
      },
      "g1_lcdm_map_M2b_not-a-knot": {
        "BAO_corrected_rel_max": 4.899037428868147e-16,
        "BAO_fixed_rel_max": 4.899037428868147e-16,
        "CMB_corrected_abs_max": 1.6323747908941755e-14,
        "CMB_fixed_abs_max": 1.6323747908941755e-14,
        "DM_rel_max": 4.2438814862380456e-16,
        "H_rel_max": 0.0,
        "chi2_BAO_corrected_abs": 1.900701818158268e-13,
        "chi2_BAO_fixed_abs": 1.900701818158268e-13,
        "chi2_CMB_corrected_abs": 3.726955188909642e-09,
        "chi2_CMB_fixed_abs": 3.726955188909642e-09,
        "rdrag_corrected_abs": 0.0,
        "rdrag_fixed_abs": 0.0,
        "rstar_corrected_abs": 0.0,
        "rstar_fixed_abs": 0.0,
        "theta_corrected_abs": 1.6323747908941755e-14,
        "theta_fixed_abs": 1.6323747908941755e-14
      },
      "g1_reference_M2a_natural": {
        "BAO_corrected_rel_max": 4.409610555329156e-16,
        "BAO_fixed_rel_max": 4.409610555329156e-16,
        "CMB_corrected_abs_max": 1.221852480304264e-13,
        "CMB_fixed_abs_max": 1.221852480304264e-13,
        "DM_rel_max": 2.8111216401697903e-16,
        "H_rel_max": 0.0,
        "chi2_BAO_corrected_abs": 4.476419235288631e-13,
        "chi2_BAO_fixed_abs": 4.476419235288631e-13,
        "chi2_CMB_corrected_abs": 7.404621626960761e-08,
        "chi2_CMB_fixed_abs": 7.404621626960761e-08,
        "rdrag_corrected_abs": 0.0,
        "rdrag_fixed_abs": 0.0,
        "rstar_corrected_abs": 0.0,
        "rstar_fixed_abs": 0.0,
        "theta_corrected_abs": 1.221852480304264e-13,
        "theta_fixed_abs": 1.221852480304264e-13
      },
      "g1_reference_M2a_not-a-knot": {
        "BAO_corrected_rel_max": 4.409610555329156e-16,
        "BAO_fixed_rel_max": 4.409610555329156e-16,
        "CMB_corrected_abs_max": 1.221852480304264e-13,
        "CMB_fixed_abs_max": 1.221852480304264e-13,
        "DM_rel_max": 2.8111216401697903e-16,
        "H_rel_max": 0.0,
        "chi2_BAO_corrected_abs": 4.476419235288631e-13,
        "chi2_BAO_fixed_abs": 4.476419235288631e-13,
        "chi2_CMB_corrected_abs": 7.404621626960761e-08,
        "chi2_CMB_fixed_abs": 7.404621626960761e-08,
        "rdrag_corrected_abs": 0.0,
        "rdrag_fixed_abs": 0.0,
        "rstar_corrected_abs": 0.0,
        "rstar_fixed_abs": 0.0,
        "theta_corrected_abs": 1.221852480304264e-13,
        "theta_fixed_abs": 1.221852480304264e-13
      },
      "g1_reference_M2b_natural": {
        "BAO_corrected_rel_max": 4.409610555329156e-16,
        "BAO_fixed_rel_max": 4.409610555329156e-16,
        "CMB_corrected_abs_max": 1.2218177858347445e-13,
        "CMB_fixed_abs_max": 1.2218177858347445e-13,
        "DM_rel_max": 2.8111216401697903e-16,
        "H_rel_max": 0.0,
        "chi2_BAO_corrected_abs": 4.369837824924616e-13,
        "chi2_BAO_fixed_abs": 4.369837824924616e-13,
        "chi2_CMB_corrected_abs": 7.404411350719897e-08,
        "chi2_CMB_fixed_abs": 7.404411350719897e-08,
        "rdrag_corrected_abs": 0.0,
        "rdrag_fixed_abs": 0.0,
        "rstar_corrected_abs": 0.0,
        "rstar_fixed_abs": 0.0,
        "theta_corrected_abs": 1.2218177858347445e-13,
        "theta_fixed_abs": 1.2218177858347445e-13
      },
      "g1_reference_M2b_not-a-knot": {
        "BAO_corrected_rel_max": 4.409610555329156e-16,
        "BAO_fixed_rel_max": 4.409610555329156e-16,
        "CMB_corrected_abs_max": 1.2218177858347445e-13,
        "CMB_fixed_abs_max": 1.2218177858347445e-13,
        "DM_rel_max": 2.8111216401697903e-16,
        "H_rel_max": 0.0,
        "chi2_BAO_corrected_abs": 4.369837824924616e-13,
        "chi2_BAO_fixed_abs": 4.369837824924616e-13,
        "chi2_CMB_corrected_abs": 7.404411350719897e-08,
        "chi2_CMB_fixed_abs": 7.404411350719897e-08,
        "rdrag_corrected_abs": 0.0,
        "rdrag_fixed_abs": 0.0,
        "rstar_corrected_abs": 0.0,
        "rstar_fixed_abs": 0.0,
        "theta_corrected_abs": 1.2218177858347445e-13,
        "theta_fixed_abs": 1.2218177858347445e-13
      }
    },
    "I4_I5_acoustic_and_spline_sensitivity": {
      "oscillatory": {
        "BAO_nat_nak_rel_max": 0.0687067730992424,
        "X_nak_min": -4.014169823509499,
        "X_nat_min": -0.7420852901228724,
        "X_nat_nak_abs_max": 3.7325974330938902,
        "chi2_BAO_nat_minus_nak": -174.78741100164257,
        "natural_BAO_corrected_vs_fixed_rel_max": 1.4527529408734507e-14,
        "natural_chi2_BAO_corrected_minus_fixed": 1.1368683772161603e-11,
        "natural_rdrag_corrected_minus_fixed": -2.1316282072803006e-12,
        "natural_rstar_corrected_minus_fixed": -2.1032064978498966e-12,
        "natural_theta_corrected_minus_fixed": -1.491862189340054e-16,
        "not-a-knot_BAO_corrected_vs_fixed_rel_max": 1.4519302031759727e-14,
        "not-a-knot_chi2_BAO_corrected_minus_fixed": -1.7394086171407253e-11,
        "not-a-knot_rdrag_corrected_minus_fixed": -2.1316282072803006e-12,
        "not-a-knot_rstar_corrected_minus_fixed": -2.1032064978498966e-12,
        "not-a-knot_theta_corrected_minus_fixed": -1.474514954580286e-16
      },
      "positive_gentle": {
        "BAO_nat_nak_rel_max": 0.0022444218967308154,
        "X_nak_min": 0.799899747636211,
        "X_nat_min": 0.7995201594126987,
        "X_nat_nak_abs_max": 0.15522946677287952,
        "chi2_BAO_nat_minus_nak": 3.9867364276775703,
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
        "BAO_nat_nak_rel_max": 0.025070127837649364,
        "X_nak_min": -0.20321357877328486,
        "X_nat_min": -0.20756469747680747,
        "X_nat_nak_abs_max": 0.3396422085447146,
        "chi2_BAO_nat_minus_nak": 188.7168668529598,
        "natural_BAO_corrected_vs_fixed_rel_max": 9.811587615290697e-15,
        "natural_chi2_BAO_corrected_minus_fixed": -3.2605385058559477e-10,
        "natural_rdrag_corrected_minus_fixed": 1.4210854715202004e-12,
        "natural_rstar_corrected_minus_fixed": 1.4210854715202004e-12,
        "natural_theta_corrected_minus_fixed": 9.8879238130678e-17,
        "not-a-knot_BAO_corrected_vs_fixed_rel_max": 9.811587615290697e-15,
        "not-a-knot_chi2_BAO_corrected_minus_fixed": -3.0377123039215803e-10,
        "not-a-knot_rdrag_corrected_minus_fixed": 1.4210854715202004e-12,
        "not-a-knot_rstar_corrected_minus_fixed": 1.4210854715202004e-12,
        "not-a-knot_theta_corrected_minus_fixed": 9.8879238130678e-17
      }
    },
    "I6_numerical_stability": {
      "BAO_default_vs_tight_rel_max": 9.811587615290697e-15,
      "CMB_default_vs_tight": {
        "oscillatory_natural": {
          "DM_zstar_rel": 1.8502327829625374e-10,
          "chi2_CMB_corrected_abs": 4.508283052473416e-05,
          "chi2_CMB_fixed_abs": 4.507931737407489e-05,
          "theta_corrected_abs": 1.914605626818222e-12,
          "theta_fixed_abs": 1.914456440599288e-12
        },
        "oscillatory_not-a-knot": {
          "DM_zstar_rel": 1.825739998129624e-10,
          "chi2_CMB_corrected_abs": 0.00013660925378644606,
          "chi2_CMB_fixed_abs": 0.0001365984498988837,
          "theta_corrected_abs": 1.8642535432045193e-12,
          "theta_fixed_abs": 1.8641060917090613e-12
        },
        "signed_crossing_natural": {
          "DM_zstar_rel": 1.8163685390822352e-10,
          "chi2_CMB_corrected_abs": 0.00023340053303400055,
          "chi2_CMB_fixed_abs": 0.00023341316045843996,
          "theta_corrected_abs": 1.8271946455872268e-12,
          "theta_fixed_abs": 1.8272935248253575e-12
        },
        "signed_crossing_not-a-knot": {
          "DM_zstar_rel": 1.8218932474487737e-10,
          "chi2_CMB_corrected_abs": 0.00021439436750370078,
          "chi2_CMB_fixed_abs": 0.00021440589989651926,
          "theta_corrected_abs": 1.838328100856046e-12,
          "theta_fixed_abs": 1.8384269800941766e-12
        }
      },
      "DM_default_vs_tight_rel_max": 0.0,
      "H_default_vs_tight_rel_max": 0.0,
      "rdrag_zmax_1e6_minus_1e7": 1.3376109109231038e-09,
      "rdrag_zmax_1e7_minus_1e8": 1.4210854715202004e-12,
      "rstar_zmax_1e6_minus_1e7": 1.2491625511756865e-09,
      "rstar_zmax_1e7_minus_1e8": 1.4210854715202004e-12
    },
    "I8_independent_path": {
      "eds_calibration": {
        "z1089.0_rel": 2.189955273610818e-16,
        "z2.33_rel": 3.523685146060914e-16
      },
      "oscillatory_natural": {
        "DM_bao_rel_max": 5.670103170711733e-16,
        "DM_zstar_rel": 1.8461792032578391e-10,
        "DM_zstar_richardson_rel": 1.755037868621818e-13,
        "H_rel_max": 2.1997840575663356e-16,
        "X_scipy_vs_manuel_abs_max": 1.5543122344752192e-15,
        "chi2_CMB_fixed_abs": 4.498054886425962e-05,
        "theta_fixed_abs": 1.910261879234376e-12
      },
      "oscillatory_not-a-knot": {
        "DM_bao_rel_max": 5.646256181840648e-16,
        "DM_zstar_rel": 1.8217400784056816e-10,
        "DM_zstar_richardson_rel": 1.7318052433621293e-13,
        "H_rel_max": 5.130432518293426e-16,
        "X_scipy_vs_manuel_abs_max": 8.881784197001252e-15,
        "chi2_CMB_fixed_abs": 0.00013629921431856928,
        "theta_fixed_abs": 1.860022552646612e-12
      },
      "signed_crossing_natural": {
        "DM_bao_rel_max": 3.9394700618789315e-16,
        "DM_zstar_rel": 1.8124273801474716e-10,
        "DM_zstar_richardson_rel": 1.6975359760732635e-13,
        "H_rel_max": 2.1035056369274808e-16,
        "X_scipy_vs_manuel_abs_max": 8.881784197001252e-16,
        "chi2_CMB_fixed_abs": 0.0002329066082893405,
        "theta_fixed_abs": 1.8233279469592745e-12
      },
      "signed_crossing_not-a-knot": {
        "DM_bao_rel_max": 4.974095439247051e-16,
        "DM_zstar_rel": 1.8179400982494397e-10,
        "DM_zstar_richardson_rel": 1.7027004228272272e-13,
        "H_rel_max": 2.1767788957177584e-16,
        "X_scipy_vs_manuel_abs_max": 1.5543122344752192e-15,
        "chi2_CMB_fixed_abs": 0.0002139407879440114,
        "theta_fixed_abs": 1.834438850822906e-12
      }
    },
    "I9_adversarial": {
      "F1_signe_H2": {
        "aveuglement_documente": "l'identité I1 (X=1) est aveugle à cette faute : la correction s'annule quel que soit son signe.",
        "detecte": true,
        "deviation_faute": 0.5407883261662035,
        "garde": "I8_H_rel_max",
        "temoin_correct": 2.015872465342384e-16
      },
      "F2_facteur_variable_DM": {
        "detecte": true,
        "deviation_faute": 0.5308370565639866,
        "garde": "I8_DM_bao_rel_max",
        "temoin_correct": 2.917319130001695e-16
      },
      "F3_noeud_deplace": {
        "aveuglement_documente": "le test I2 évalué aux nœuds du profil fautif passerait : il ne garde pas la position des nœuds.",
        "detecte": true,
        "deviation_faute": 0.04244438989289562,
        "garde": "I8_X_scipy_vs_manuel_abs_max",
        "temoin_correct": 8.881784197001252e-16
      },
      "F4_raccord_supprime": {
        "detecte": true,
        "deviation_faute": 0.6448472080390781,
        "garde": "I3_constant_extension_abs_max",
        "temoin_correct": 0.0
      },
      "F5_omega_x0_faux": {
        "aveuglement_documente": "l'identité I1 (X=1) est aveugle à cette faute : Omega_X,0 multiplie (X-1)=0.",
        "detecte": true,
        "deviation_faute": 0.017325443827536195,
        "garde": "I8_H_rel_max",
        "temoin_correct": 2.015872465342384e-16
      },
      "toutes_fautes_detectees": true
    }
  }
}
```
