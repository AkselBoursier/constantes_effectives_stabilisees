# Rapport G2.1 — validation de l’instrument numérique `X(z)`

Issue directrice : #63. Branche : `comp/c7-c1-xz-validation`.

## 0. Statut de la porte

```text
statut : exécution partielle ;
G2.1 : non clôturable à ce commit ;
MCMC / minimisation / posterior : interdits et absents ;
priors scientifiques sur X_i : non définis ;
G2.2 : fermée.
```

Ce commit installe l’instrument et sa matrice de tests. Les tests analytiques
indépendants de CAMB ont été exécutés. Les contrôles complets sous
Python 3.12 / CAMB 1.5.4 doivent encore être exécutés dans l’environnement
directeur local avant toute validation humaine de G2.1.

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

## 3. Contrôles complets encore requis

Dans l’environnement directeur gelé :

```text
python scripts/test_xz_g2_1.py --full
```

Préconditions :

```text
Python 3.12 ; CAMB 1.5.4 ; NumPy 1.26.4 ; SciPy 1.13.1 ;
C7C1_DATA_DIR vers les octets BAO officiels hors Git.
```

Le passage complet doit fournir :

1. identité `X_i=1` avec CAMB aux deux points G1 verrouillés ;
2. erreurs sur `H`, `D_M`, `D_H`, `D_V`, `r_drag`, `r_star`, `theta_star` ;
3. identité des 13 prédictions BAO et des `chi²_BAO/CMB` ;
4. comparaison `natural` / `not-a-knot` sur profils fixés ;
5. comparaison acoustique `fixed` / `corrected` ;
6. stabilité des quadratures et de la borne haute acoustique ;
7. toutes les erreurs absolues et relatives nécessaires à T8–T12.

## 4. Tolérances T8–T12

Aucune tolérance finale n’est fixée dans ce commit. Elles doivent être dérivées
des planchers mesurés par le passage complet, puis ratifiées humainement :

```text
T8  — identité LambdaCDM des observables de fond ;
T9  — interpolation, nœuds et continuité interne ;
T10 — frontière z=2.33 et continuation constante ;
T11 — stabilité quadrature / borne acoustique ;
T12 — effet de la convention de spline et du traitement acoustique.
```

T12 ne doit pas transformer une différence de convention en simple « erreur
numérique » : si l’effet est non négligeable, les variantes devront rester
séparées jusqu’au pré-enregistrement G2.2.

## 5. Verdict provisoire

```text
instrument structurel : cohérent sur les tests analytiques ;
identité CAMB G1 : non encore mesurée dans ce commit ;
étalon acoustique : comparaison implémentée, non encore exécutée sous G1 ;
tolérances T8–T12 : suspendues ;
G2.1 : ouverte, non validée ;
G2.2 / G2.3 : fermées.
```
