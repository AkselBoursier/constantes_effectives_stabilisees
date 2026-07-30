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

PROPOSITION B1 (PROPOSÉE, NON APPLIQUÉE — décision humaine requise ;
ni test_xz_g2_1.py ni les seuils T11 ne sont dans le périmètre autorisé
de la présente porte) :

```text
option privilégiée (i) : amender le contrôle I6 dans une porte
  documentaire distincte — remplacer la variante d'instance
  acoustic_zmax=1e8 par le contrôle de queue GL/borne d'intégrande
  ([1e7, 1e8] < 1e-20), puis re-ratifier T11_BAO_default_tight,
  T11_rdrag_zmax, T11_rstar_zmax sous A1 sur planchers re-mesurés ;
option écartée (ii) : relever les trois seuils T11 aux niveaux mesurés
  (~1e-8) — écartée car l'écart mesuré ÉGALE la correction entière :
  le seuil ainsi relevé ne contrôlerait plus rien ;
dans l'attente : la porte G2.4c-iii publie l'échec T11 tel quel
  (exit 1 de G2.3a, cause unique documentée), sans relèvement
  silencieux d'aucun seuil.
```

Mise à jour documentaire T12(b) appliquée (déclarée avant
réexécution) : `T12_rdrag_corr_fixed` et `T12_rstar_corr_fixed`
1e-10 -> 1e-7 ; `T12_chi2_BAO_corr_fixed` 1e-8 -> 1e-5 — fondée sur les
maxima publiés du diagnostic G2.4c-ii-b sous la règle A1 (5.33e-9 /
4.80e-9 / 8.5e-7), seuils globaux, sans ajustement point par point.
Les autres seuils T8-T11 et T12(a) sont INCHANGÉS. Anciennes valeurs
conservées et traçables sous corrected-legacy (rapport G2.1, addendum
§4-A1).

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

## 8. Comparaison corrected-v1.1 / corrected-legacy / fixed

Maxima absolus sur les 16 points P0-P3 (4 variantes), sans
interprétation cosmologique :

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
     contrôle physique simplifié  : fixed.
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
qualification optimisation : DEUX passes complètes, exit 0 / exit 0 ;
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
```
