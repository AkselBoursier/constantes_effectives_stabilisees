# Rapport G2.4c-iii — application et qualification de l'amendement A1

Porte G2.4c-iii (issue #63). Aucune MCMC, aucune minimisation, aucun
posterior, aucun manifeste réel, aucun raccord au lanceur dans cette
porte, aucune interprétation cosmologique.

## 1. Ratification humaine

```text
décision : « Je ratifie l'amendement A1 du mode corrected-v1.1. »
auteur   : Aksel (validation humaine, #63) ;
date     : 30 juillet 2026 ;
cadre    : condition de validation explicite prévue par D3-H,
           satisfaite APRÈS le signalement obligatoire de la rupture
           d'équivalence exigé par T12(b) (diagnostic G2.4c-ii-a/-b)
           et AVANT toute inférence (aucune chaîne MCMC X(z), aucun
           posterior, aucune minimisation X(z) n'existe).
```

## 2. Ancienne clause et nouvelle clause

```text
ANCIENNE (au moment de la ratification de T8-T12, G2.1) :
  correction acoustique par scipy.quad en z, bornes [z_depart, 1e7],
  epsabs = self.epsabs = 1e-8, epsrel = self.epsrel = 1e-10,
  limit = self.quad_limit = 300 — tolérances PARTAGÉES avec les
  quadratures de distance de l'instance ;

NOUVELLE (A1, mode directeur « corrected-v1.1 ») :
  scipy.quad en variable z ;
  bornes inchangées ;
  epsabs = 1e-15 ;
  epsrel = 1e-13 ;
  limit  = 800 ;
  tolérances acoustiques PROPRES aux modes (ACOUSTIC_RULES),
  découplées des tolérances de distance (qui ne gouvernent plus que
  D_M) ;

CONSERVÉE : « corrected-legacy » reproduit bit à bit l'ancienne règle
  (epsabs = 1e-8, epsrel = 1e-10, limit = 300) ; la quadrature
  Gauss-Legendre en u = 1/sqrt(1+z) reste EXCLUSIVEMENT un contrôle
  indépendant, jamais une règle de production.
```

## 3. Compatibilité de nom (mapping des modes)

```text
corrected         -> corrected-v1.1   (alias explicite, unique,
                                       documenté, testé : égalité
                                       EXACTE exigée et vérifiée) ;
fixed             -> fixed            (inchangé) ;
corrected-legacy  -> ancienne règle   (bit à bit) ;
mode inconnu      -> ValueError       (aucune acceptation silencieuse).

AUCUN résultat historique n'est réétiqueté : toutes les sorties
antérieures à l'amendement (G2.1 I1-I9 et planchers T8-T12, G2.3a,
G2.4b, G2.4c-i/ii) restent décrites comme « corrected-legacy ».
```

## 4. Fichiers modifiés

```text
scripts/xz_background_g2_1.py        oracle : trois modes, règles
                                     ACOUSTIC_RULES, alias, résolution
                                     stricte, découplage des tolérances ;
scripts/xz_fast_g2_4c.py             chemin rapide aligné sur
                                     corrected-v1.1 (mode paramétrable,
                                     legacy réservé à la régression) ;
scripts/qualify_xz_optim_g2_4c.py    audit bloquant des règles, contrôle
                                     acoustique A1 (modes séparés, alias,
                                     bit-identité legacy, GL séparé
                                     r_drag/r_star, comparaisons de
                                     modes), régression rapide-legacy,
                                     9 fautes A1 ;
scripts/qualify_xz_configs_g2_3.py   mise à jour documentaire T12(b) ;
reports/rapport_G2_1.md              addendum §4-A1 (traçabilité) ;
reports/rapport_G2_4c_optimisation.md addendum §8 ter-A1 (statut) ;
reports/rapport_G2_4c_iii_amendement_A1.md  le présent rapport.

NON MODIFIÉS : les quatre YAML G2.3, les priors, les grilles, les
conventions de spline, le lanceur G2.4b, les graines, les données
BAO/CMB.
```

## 5. Résultats déjà visibles avant amendement

```text
G2.1 : I1-I9 et T8-T12 (sous l'ancienne règle -> corrected-legacy) ;
G2.3a : qualification des quatre configurations ;
G2.4b : qualification du lanceur, aucune chaîne réelle ;
G2.4c-i : profilage ; G2.4c-ii : optimisation qualifiée bit-identique
et diagnostic acoustique (constat C1 : sous-résolution) ;
aucune chaîne MCMC X(z), aucun posterior, aucune minimisation X(z).
La ratification ne dépend d'aucun résultat cosmologique.
```

## 6. Suites rejouées sous l'oracle amendé

### 6.1 G2.3a C1-C8 (inclut la ré-exécution I1-I9 et T8-T12 en C5)

#### 6.1.a Rejeu du 30 juillet 2026 — PRÉ-correctif B1 (HISTORIQUE)

Résultat conservé tel quel, sous les anciens contrôles T11 (jamais
réétiqueté) :

```text
double exécution : exit 1 / exit 1 ; sorties stdout bit à bit
  identiques ; auto-test d'échec (C7C1_QUALIF_TEST_ECHEC) : exit 1 ;
C1/C2 (schéma strict)            : PASSE ;
C3 (points fixes, sondes)        : PASSE ;
C4 (identité T8 P0/P1)           : PASSE (4 variantes x 2 points) ;
C6 (assemblage indépendant)      : PASSE ;
C7 (FQ1-FQ4)                     : 4/4 détectées ;
C8 (sorties hors Git)            : PASSE ;
C5 : T8 PASSE (rdrag/rstar_abs 0.0 ; BAO_rel 4.41e-16 ;
       chi2_BAO 4.58e-13 ; chi2_CMB 7.40e-8 ; theta 1.22e-13) ;
     T9 PASSE (noeuds 0.0 ; polynômes 6.66e-16) ;
     T10 PASSE (0.0) ;
     T12 PASSE sous la mise à jour documentaire pré-déclarée :
       rdrag corr-fixed 5.711e-9 <= 1e-7 ; rstar 5.143e-9 <= 1e-7 ;
       chi2_BAO 8.745e-7 <= 1e-5 (marges >= 11x) ;
     T11 : 11 entrées sur 14 PASSENT (I8 : X 8.9e-15, H 5.1e-16,
       D_M 5.7e-16, EdS 3.5e-16 ; D_M quad/trapèzes 6.6e-11 ;
       D_M z_star 1.85e-10 ; theta 2.28e-12 ; chi2_CMB stress 2.0e-4 ;
       I9 5/5) — TROIS entrées DÉPASSENT :
       T11_BAO_default_tight 2.577e-11 > 1e-12 ;
       T11_rdrag_zmax        3.807e-9  > 1e-10 ;
       T11_rstar_zmax        3.429e-9  > 1e-10.
VERDICT G2.3a : exit 1, CAUSE UNIQUE (voir constat B1 ci-dessous).
```

CONSTAT B1 — le contrôle de borne acoustique zmax=1e8 est NUMÉRIQUEMENT
VIDE (découverte de cette porte, cause unique des trois dépassements) :

```text
mesures (fond g1_lcdm_map, profil signed_crossing, intégrande de
correction, règles telles qu'indiquées) :
  quad v1.1  [zdrag, 1e6]  = 3.807304e-9  (err. estimée 2.1e-14) ;
  quad v1.1  [zdrag, 1e7]  = 3.807304e-9  (err. estimée 2.3e-14) ;
  quad v1.1  [zdrag, 1e8]  = 0.0          (err. estimée 0.0) ;
  quad legacy[zdrag, 1e7]  = 1.432978e-12 (sous-résolu, constat C1) ;
  quad legacy[zdrag, 1e8]  = 0.0          (err. estimée 0.0) ;
  contrôle GL indépendant [zdrag, 1e7]    = 3.807305e-9 ;
  contrôle GL queue [1e7, 1e8]            = 0.0 (< 1e-20 par borne
    d'intégrande : l'intégrande y est sous le plus petit double
    représentable utile) ;

mécanisme : sur [z_depart, 1e8], les 21 noeuds de Gauss-Kronrod du
  premier niveau tombent tous à z >~ 2e5, où l'intégrande s'arrondit
  exactement à 0.0 -> estimation 0, erreur estimée 0, « convergence »
  immédiate vers 0.0 — SOUS TOUTE RÈGLE (legacy comme v1.1) ;

conséquence historique : la ratification de T11_rdrag_zmax <= 1e-10
  (mesuré 1.4e-12 sous legacy) comparait deux valeurs toutes deux non
  résolues (1.43e-12 vs 0.0) — le contrôle passait par coïncidence de
  deux échecs ; l'amendement A1, en RÉSOLVANT la valeur à zmax=1e7
  (3.807e-9, corroborée par GL à ~1e-15 près), rend la vacuité du
  contrôle visible ;

les trois dépassements ont cette cause unique : l'instance de stress
  I6 « tight » porte acoustic_zmax=1e8 -> sa correction vaut 0.0 ->
  |default - tight| = la correction entière (rdrag/rstar_zmax), et le
  même écart propagé à r_d contamine BAO_default_tight
  (3.807e-9 / r_d ~ 2.6e-11) ;

la CONCLUSION scientifique du contrôle (zmax = 1e7 convergée) reste
  POSITIVEMENT établie, mais par le contrôle GL indépendant :
  quad v1.1 [zdrag,1e7] vs GL : accord ~1e-15 ; queue [1e7,1e8]
  bornée < 1e-20 ; et sous v1.1, [zdrag,1e6] et [zdrag,1e7] rendent la
  même valeur 3.807304e-9 à la précision du plancher d'arrondi
  (l'« interdiction » historique de zmax=1e6, fondée sur un écart
  legacy de 1.3e-9, relevait du même artefact de sous-résolution).
```

Le diagnostic B1 a été CONFIRMÉ par l'audit de la PR #79 (30 juillet
2026), qui a retenu l'option d'amendement du contrôle I6 et l'a bornée
à la porte G2.4c-iii-a (commentaire directeur #63).

#### 6.1.b Correctif B1 appliqué (G2.4c-iii-a)

Nouvelle construction I6 (`test_xz_g2_1.py`), conforme au commentaire
directeur et à l'audit :

```text
découplage : instances « default » (epsabs=1e-8, epsrel=1e-10,
  quad_limit=300, acoustic_zmax=1e7) et « tight_distance »
  (epsabs=1e-10, epsrel=1e-12, quad_limit=500, acoustic_zmax=1e7) —
  la borne acoustique est IDENTIQUE (1e7) des deux côtés : le contrôle
  BAO_distance_default_vs_tight (corrected-v1.1 des deux côtés) ne
  teste plus que les quadratures de DISTANCE ;
retrait de la porte : quad(z_depart, 1e8) et les métriques
  rdrag/rstar_zmax_1e7_minus_1e8 ne servent plus ni de référence ni de
  seuil ; la quadrature 1e8 subsiste uniquement comme démonstration
  adversariale historique de la vacuité (B1_adversarial_quad_1e8) ;
  l'instance CMB resserrée passe aussi à acoustic_zmax=1e7 (aucune
  quadrature directe 1e8 dans aucun contrôle d'acceptation) ;
voie acoustique INDÉPENDANTE (distincte de
  _sound_horizon_correction) : u = 1/sqrt(1+z), Gauss-Legendre
  512 points par segment, convergence contrôlée à 1024, segments
  explicites [z_depart, zstar], [zstar, 1e4], [1e4, 1e6], [1e6, 1e7] ;
  r_drag et r_star séparés ; produit rdrag/rstar_v11_vs_GL_abs et
  rdrag/rstar_GL_512_vs_1024_abs ;
queue [1e7, 1e8] évaluée séparément par correction (même changement
  de variable indépendant) : rdrag/rstar_tail_1e7_1e8_abs ; MAJORATION
  analytique conservatrice documentée et publiée :
  |intégrande(z)| <= (c/sqrt(3))·|delta| / (2·h_min(z)^3), décroissante
  en z ; borne = valeur en 1e7 x largeur, calculée par l'expression
  analytique (jamais par la différence catastrophiquement annulée) —
  un flottant exactement nul ne suffit pas, à lui seul, comme preuve ;
  la mesure de porte gate le MAX(queue GL, majoration) ;
seuils PRÉ-DÉCLARÉS avant rejeu (aucun ajustement après lecture) :
  corrected-v1.1 vs GL <= 1e-13 Mpc ; GL512 vs GL1024 <= 1e-13 Mpc ;
  queue <= 1e-18 Mpc ; BAO distance <= 1e-12 (INCHANGÉ, aucune hausse).
```

Rejeu G2.3a post-correctif (nouvelle porte T11, double passe) :

```text
double exécution : exit 0 / exit 0 ; sorties stdout bit à bit
  identiques ; auto-test d'échec (C7C1_QUALIF_TEST_ECHEC) : exit 1 ;
C1-C8 : PASSENT ; I1-I9 : PASSENT ; porte : PASSE (echecs vides) ;
T8  PASSE (rdrag/rstar_abs 0.0 ; BAO_rel 4.41e-16 ; theta 1.22e-13) ;
T9  PASSE (0.0 ; 6.66e-16) ;  T10 PASSE (0.0) ;
T11 PASSE — nouvelles entrées (seuils pré-déclarés) :
  BAO_distance_default_tight : 0.0           <= 1e-12 (INCHANGÉ) ;
  rdrag_v11_vs_GL            : 1.022296e-14  <= 1e-13 ;
  rstar_v11_vs_GL            : 1.181600e-14  <= 1e-13 ;
  rdrag_GL_convergence       : 3.964915e-16  <= 1e-13 ;
  rstar_GL_convergence       : 3.906756e-16  <= 1e-13 ;
  rdrag_tail_1e7_1e8         : 1.880802e-26  <= 1e-18 ;
  rstar_tail_1e7_1e8         : 1.880802e-26  <= 1e-18
  (queue = max(GL indépendante, majoration analytique) — la valeur
  publiée EST la majoration analytique, le flottant GL valant 0.0) ;
  entrées distances inchangées : DM_quad_trapezes 6.59e-11 ;
  DM_zstar 1.85e-10 ; theta 1.91e-12 ; chi2_CMB_stress 2.33e-4 ;
  I8 : X 8.88e-15, H 5.13e-16, D_M 5.67e-16, EdS 3.52e-16 ; I9 5/5 ;
T12 PASSE, séparé :
  T12-legacy-régression : rdrag 2.131628e-12 <= 1e-10 ;
    rstar 2.103206e-12 <= 1e-10 ; chi2_BAO 3.274181e-10 <= 1e-8 ;
  T12-A1-numérique : rdrag_v11_vs_GL 1.022296e-14 <= 1e-13 ;
    rstar_v11_vs_GL 1.181600e-14 <= 1e-13 ; alias corrected EXACT.
```

#### 6.1.c Séparation T12 / S5 (G2.4c-iii-a)

La présentation initiale de G2.4c-iii (seuils 1e-7 Mpc et 1e-5
« T12(b) mis à jour ») était TROP FORTE : la ratification humaine
portait sur A1, pas sur ces valeurs (audit PR #79). Elle est remplacée
par trois objets distincts :

```text
T12-legacy-régression (verdict) : corrected-legacy reproduit l'ancien
  oracle ; anciens seuils conservés :
  |Delta r_drag| <= 1e-10 (mesuré 2.131628e-12) ;
  |Delta r_star| <= 1e-10 (mesuré 2.103206e-12) ;
  |Delta chi2_BAO| <= 1e-8 (mesuré 3.274181e-10) ;

T12-A1-numérique (verdict) :
  corrected-v1.1 vs GL : r_drag <= 1e-13 (mesuré 1.022296e-14) ;
                         r_star <= 1e-13 (mesuré 1.181600e-14) ;
  alias corrected == corrected-v1.1 : EXACT ;
  oracle amendé == chemin rapide : porté par la double passe de
  qualify_xz_optim_g2_4c.py (§6.2, §7) ;

S5-sensibilité (PUBLICATION SANS VERDICT) :
  primaire corrected-v1.1 ; contrôle historique corrected-legacy ;
  contrôle physique simplifié fixed ; écarts rdrag, rstar, theta_star,
  BAO, CMB, chi2 publiés (§8) ; les enveloppes 1e-7 Mpc (corrections)
  et 1e-5 (chi2_BAO) sont des NIVEAUX D'ALERTE PROPOSÉS POUR S5, NON
  RATIFIÉS — elles ne contribuent à AUCUN verdict automatique.
```

Les autres seuils T8-T10, T11 (hors entrées B1 re-proposées ci-dessus)
et T12(a) sont INCHANGÉS. Anciennes valeurs legacy conservées et
traçables (rapport G2.1, addendum §4-A1).

### 6.2 G2.4c-ii (qualification de l'optimisation, double passe)

```text
double passe complète : exit 0 / exit 0 ; sorties normalisées bit à
  bit identiques (diff vide ; temps/mémoire hors diff) ;
auto-test de retrait d'un point oracle-valide : exit 1 — VÉRIFIÉ ;
audit des règles acoustiques : CONFORME (aucune violation) ;
étude de convergence : retenus principal 2048 / queue 2048 ;
  doublement : PASSE (0.048) ; ordre historique : identique ;
spline scalaire : bitwise identique ; porte : PASSE (echecs vides).
```

REJEU G2.4c-iii-a (code de l'optimisation INCHANGÉ par le correctif —
xz_background_g2_1.py, xz_fast_g2_4c.py et qualify_xz_optim_g2_4c.py
non modifiés en iii-a ; la double passe est rejouée pour attester que
le correctif du contrôle I6 ne perturbe rien) :

```text
double passe : exit 0 / exit 0 ; diff normalisé VIDE ;
auto-test de retrait : exit 1 ; porte : PASSE (echecs vides) ;
couverture 331/306/25 inchangée ; classification 331/331 identique ;
contrôle acoustique A1 : 16/16 points, alias exact partout,
  legacy bit-identique partout ; concordance GL max r_drag 1.345e-14 /
  r_star 9.313e-15 ; convergence GL 7.027e-16 / 6.957e-16 ;
fautes : 23/23 détectées ; convergence 2048/2048, doublement 0.048 ;
Cobaya : 0 / 1 / 0 et deux blocs — inchangés.
```

## 7. Équivalence oracle amendé / chemin rapide

```text
ensemble gelé : 331 points au total sur quatre variantes ;
couverture (total / oracle-valide / oracle-invalide / comparé /
classification-only) :
  M2a-N 82/77/5/77/5 ; M2a-K 85/79/6/79/6 ;
  M2b-N 81/74/7/74/7 ; M2b-K 83/76/7/76/7 ;
  TOTAL 331/306/25/306/25 — 306 oracle-valides TOUS comparés
  numériquement, 25 invalides contrôlés en classification ;
classification valide/invalide : STRICTEMENT IDENTIQUE (331/331),
  INCHANGÉE par l'amendement (mêmes comptes qu'en G2.4c-ii-b) ;
pires écarts (aucun seuil relâché) :
  H rel 0.0 ; BAO rel 0.0 ; theta_star abs 0.0 ; chi2_BAO abs 0.0 ;
  chi2_CMB abs 0.0 ; rdrag abs 0.0 ; rstar abs 0.0 ; D_M(z*) rel 0.0 ;
  correction acoustique abs 1.416e-14 (seuil 1e-13 ; borne
  structurelle : requantification ulp(r)/2 ~ 1.4e-14 — les corrections
  BRUTES rapide/oracle sont bit-identiques, vérifié au smoke test et
  verrouillé par rdrag_abs = rstar_abs = 0.0 sur les valeurs publiées).
```

Régression SÉPARÉE en mode corrected-legacy (les anciens tests bit à
bit restent disponibles) :

```text
16 points P0-P3 (4 variantes), évaluateur rapide en mode
corrected-legacy vs oracle amendé en mode corrected-legacy :
  rdrag abs 0.0 ; rstar abs 0.0 ; theta abs 0.0 ; BAO rel 0.0 ;
  chi2_BAO abs 0.0 ; chi2_CMB abs 0.0 ;
  correction acoustique abs 1.262e-14 (seuil 1e-13, requantification).
```

Optimisation lent/rapide inchangée (démonstrations Cobaya sans MCMC) :

```text
variation d'un X_i seul          : 0 appel CAMB ;
variation de H0                  : exactement 1 nouvel état lent ;
retour à un triplet encore caché : 0 appel (réutilisation exacte) ;
graphe de blocs                  : [H0, ombh2, omm] + [X1..X5] — deux
                                   blocs Cobaya distincts, exacts.
```

## 8. S5-sensibilité — comparaison corrected-v1.1 / corrected-legacy / fixed

PUBLICATION SANS VERDICT (G2.4c-iii-a) : aucun de ces écarts n'est
qualifié d'erreur numérique ni d'équivalence. Maxima absolus sur les
16 points P0-P3 (4 variantes), sans interprétation cosmologique :

```text
grandeur        v1.1 - legacy   v1.1 - fixed    legacy - fixed
r_drag          5.322306e-09    5.324324e-09    2.017941e-12
r_star          4.790763e-09    4.792781e-09    2.017941e-12
theta_star      3.566748e-13    3.568257e-13    1.509209e-16
vecteur BAO     1.479130e-09    1.479691e-09    5.613288e-13
vecteur CMB     3.566748e-13    3.568257e-13    1.509209e-16
chi2_BAO        8.463603e-07    8.466855e-07    3.251444e-10
chi2_CMB        4.447887e-05    4.449769e-05    1.882290e-08
chi2_total      4.468016e-05    4.469906e-05    1.889930e-08
(vecteurs : max abs par composante ; points dominants P2/P3)
```

Rapports aux seuils de contrôle T12(b) HISTORIQUES (dénominateurs de
G2.4c-ii-b, conservés pour la continuité de lecture ; les seuils de
PORTE re-ratifiés sont en §6.1) :

```text
max |correction v1.1|      / 1e-10 : 5.324324e-9  / 1e-10 = 53.24 ;
max |Δchi2_BAO| (v1.1-leg) / 1e-8  : 8.463603e-7  / 1e-8  = 84.64 ;
max |Δchi2_CMB| (v1.1-leg) / 1e-3  : 4.447887e-5  / 1e-3  = 0.04448 ;
max |Δtheta_star|          / 1e-9  : 3.566748e-13 / 1e-9  = 3.567e-4 ;
(chi2_total et vecteurs BAO/CMB : aucun seuil T12 déclaré pour ces
grandeurs — maxima publiés tels quels ci-dessus, sans rapport.)
```

Redéfinition de la sensibilité S5 (documentaire) :

```text
S5 : primaire                     : corrected-v1.1 ;
     contrôle historique          : corrected-legacy ;
     contrôle physique simplifié  : fixed ;
     niveaux d'alerte PROPOSÉS, NON RATIFIÉS (hors de tout verdict
     automatique) : correction acoustique <= 1e-7 Mpc ;
                    |Delta chi2_BAO| <= 1e-5.
```

## 9. Contrôles GL indépendants (r_drag et r_star séparés)

```text
16 points (4 variantes x P0-P3), garde de compte 16/16 : VÉRIFIÉE ;
garde de complétude des clés par point : VÉRIFIÉE ;
alias « corrected » == corrected-v1.1 : EXACT sur les 16 points ;
corrected-legacy == ancien oracle : BIT-IDENTIQUE sur les 16 points
  (valeurs publiées r_ref + correction vs reconstruction verbatim de
  l'ancienne règle) ;
concordance corrected-v1.1 vs GL512 (BLOQUANTE, seuil 1e-13 Mpc) :
  r_drag <= 1.345e-14 ; r_star <= 9.313e-15 — PASSÉE partout ;
convergence GL 512 vs 1024 : r_drag <= 7.027e-16 ; r_star <= 6.957e-16 ;
exemple (M2a-N : P2) :
  corr r_drag : v1.1 3.549530e-9 (publié, requantifié) ;
    legacy 1.364242e-12 ; GL512 3.549542e-9 ; GL1024 3.549542e-9 ;
  corr r_star : v1.1 3.195197e-9 ; legacy 1.335820e-12 ;
    GL512 3.195188e-9 ; GL1024 3.195188e-9.
```

Constat numérique consigné (sans interprétation) : sous la règle A1,
scipy.quad signale la détection d'arrondi (IntegrationWarning) — la
quadrature raffine jusqu'au plancher de bruit de l'intégrande ; la
justesse est bornée par le contrôle GL indépendant ci-dessus. La
concordance est mesurée sur la correction requantifiée
(r(mode) - r_ref), qui porte une borne structurelle ulp(r)/2 ≈ 1.4e-14
(r ~ 147 Mpc) incluse dans le seuil déclaré 1e-13.

## 10. Fautes adversariales

```text
23/23 détectées (code non nul), en sous-processus :
14 existantes (G2.4c-ii) : état d'un autre triplet ; état périmé ;
  descripteur d'une autre variante ; conventions croisées ; cache
  partagé entre variantes ; collision de clé ; construction échouée
  réutilisée ; segment 2.33 omis ; queue D_M omise ; queue acoustique
  omise ; ordre insuffisant ; classification divergente ; graphe en un
  bloc ; CAMB sur variation X_i ;
9 nouvelles (A1) :
  v11_avec_tolerances_legacy         (garde : concordance GL) ;
  legacy_avec_tolerances_v11         (garde : bit-identité ancienne
                                      règle, valeurs publiées) ;
  alias_corrected_vers_legacy        (garde : égalité exacte alias) ;
  mode_inconnu_accepte               (garde : refus ValueError exigé) ;
  limit_v11_altere                   (garde DÉSIGNÉE : audit déclaratif
                                      des règles — la garde numérique
                                      peut être aveugle si quad
                                      n'atteint pas la limite,
                                      aveuglement documenté) ;
  epsabs_epsrel_altere               (gardes : audit + concordance GL) ;
  controle_GL_rstar_omis             (garde : complétude des clés) ;
  resultat_historique_reetiquete_v11 (garde : revalidation GL de toute
                                      valeur revendiquant v1.1) ;
  cache_partage_modes_acoustiques    (garde : régression bit à bit
                                      legacy vs ancienne règle).
```

## 11. Déterminisme

```text
G2.4c-iii-a : G2.3a DEUX exécutions exit 0 / exit 0, sorties stdout
  bit à bit identiques (auto-test d'échec : exit 1) ; optimisation
  DEUX passes exit 0 / exit 0, diff normalisé vide, auto-test de
  retrait exit 1 ;
qualification optimisation (G2.4c-iii) : DEUX passes complètes, exit 0 / exit 0 ;
  sorties normalisées bit à bit identiques (diff vide) — audit des
  règles, couverture, contrôle acoustique A1, comparaisons de modes,
  régression legacy et comptages CAMB inclus au diff ; temps/mémoire
  et verdicts chronométrés : section séparée, hors diff ;
  auto-test de retrait : exit 1 — VÉRIFIÉ ;
G2.3a : DEUX exécutions, sorties stdout bit à bit identiques (exit 1
  déterministe, cause unique B1) ; auto-test d'échec : exit 1 ;
IntegrationWarning scipy (règle A1) : émis sur stderr, hors sortie
  normalisée — sans effet sur le contrôle de déterminisme.
```

## 12. Performance

```text
mesures indicatives (hors diff déterministe) de cette passe :
  coût acoustique par paire de corrections :
    corrected-v1.1   : 43.65 ms ;
    corrected-legacy : 0.72 ms ;
    rapport v1.1/legacy : 60.9x — mesuré SANS modification des
    critères scientifiques (différence de coût de la règle ratifiée) ;
  évaluation rapide complète : 43.1 ms (dominée par les quads
    acoustiques v1.1 ; ~5 ms en G2.4c-ii sous legacy) ;
  oracle amendé (réchauffé)   : 0.921 s/éval ;
  évaluation lente complète   : 0.12x l'oracle (critère <= 1.10x) ;
  SPEEDUP REPRÉSENTATIF : 18.8x vs oracle amendé réchauffé
    (obligatoire >= 5x : ATTEINT ; cible >= 10x : ATTEINTE) ;
  aucune régression du graphe lent/rapide (démonstrations Cobaya §7) ;
conséquence déclarée : le coût ABSOLU par évaluation rapide est ~9x
  celui mesuré en G2.4c-ii — les projections de capacité G2.4b-i
  devront être relues à la porte de raccord (hors périmètre présent).

rejeu G2.4c-iii-a (machine chargée : agents de vérification et
  seconde qualification concurrents — les valeurs ABSOLUES sont donc
  dilatées d'un facteur ~3 par rapport au rejeu iii ci-dessus ; seuls
  les RAPPORTS sont comparables, et les comptages d'appels CAMB,
  déterministes, sont inchangés) :
  coût acoustique par paire : v1.1 207.08 ms vs legacy 3.65 ms —
    rapport 56.7x (56.7x à 60.9x selon la charge) ;
  éval rapide complète 132.4 ms ; oracle réchauffé 3.350 s/éval ;
  éval lente 0.081x l'oracle (critère <= 1.10x) ;
  SPEEDUP REPRÉSENTATIF : 22.9x (obligatoire >= 5x : ATTEINT ;
    cible >= 10x : ATTEINTE).
```

## 13. Limites

```text
- la règle A1 appliquée à l'intégrande de l'oracle raffine jusqu'au
  plancher d'arrondi (IntegrationWarning scipy) : coût acoustique par
  paire fortement accru (mesuré §12) — propriété de la règle ratifiée,
  déclarée telle quelle ; la justesse est verrouillée par le contrôle
  GL indépendant ;
- la bit-identité corrected-legacy == ancien oracle est démontrée au
  niveau des valeurs publiées (r_ref + correction), sur les instances
  aux tolérances de distance par défaut (les seules qualifiées en
  production) ; les instances de stress de test_xz_g2_1 (epsabs
  resserrés) relevaient l'ancienne règle d'instance, désormais
  découplée — comportement I6 documenté, non régressif ;
- l'équivalence oracle/rapide est démontrée sur l'ensemble gelé (331
  points au total), pas un théorème sur le prior continu ;
- les projections de coût de production (G2.4b-i) doivent être relues
  avec le coût acoustique v1.1 (§12) : elles seront réévaluées à la
  porte de raccord, hors du périmètre présent.
```

## 14. Statut du raccord au lanceur

```text
AUCUN raccord au lanceur G2.4b dans cette porte (interdit par la
directive) : run_mcmc_xz_g2_4.py et xz_cobaya_g2_4.py sont INTOUCHÉS et
continuent d'utiliser l'oracle via le nom nu « corrected » (donc
corrected-v1.1 après amendement, par l'alias, sans modification du
lanceur). Le raccord du chemin optimisé au lanceur reste une porte
distincte ; le premier lancement réel demeure soumis au manifeste à
deux clés et à une décision humaine distincte. PR : brouillon, aucun
merge.

Statut après le correctif G2.4c-iii-a :
  A1 : implémenté, pré-validé par l'audit (PR #79) — intouché par le
    correctif (xz_background_g2_1.py, xz_fast_g2_4c.py,
    qualify_xz_optim_g2_4c.py non modifiés en iii-a) ;
  B1 : diagnostic confirmé ; correctif appliqué (nouvelle construction
    I6, nouveaux contrôles T11 pré-déclarés) ; échec historique
    conservé en §6.1.a ;
  T12 : séparé (legacy-régression / A1-numérique / S5 publication) ;
    enveloppes S5 explicitement NON RATIFIÉES ;
  PR #79 : brouillon, NON marquée prête, NON fusionnée ;
  production / manifeste / MCMC : FERMÉS ;
  clôture de G2.4c-iii : soumise à la décision humaine sur la base du
    présent rapport et des doubles passes publiées dans #63.
```
