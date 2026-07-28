# Rapport G1.3 — reproductions LambdaCDM et CPL sous la vraisemblance commune

Issue directrice : #63. Autorisation : commentaire G1.4 (validation G1.2,
ouverture G1.3 sous condition du commit correctif — intégré en `1ee2b4c`).
Chaînes et sorties volumineuses : hors Git. Aucun travail sur X(z).

## 1. Dispositif

```text
vraisemblance commune : c7c1_likelihoods (BAO DR2 13 composantes,
  octets épinglés bb0c1c9 ; CMB_compressed_public_DR2_rounded) ;
configs : transcriptions ratifiées (blocs theory/params/sampler
  identiques aux officiels ; prior joint w0+wa<0 explicite en CPL) ;
environnement directeur : Cobaya 3.5, CAMB 1.5.4, numpy 1.26.4 ;
échantillonnage : 4 chaînes indépendantes par modèle, graines
  explicites (LCDM 101-104 ; CPL 201-204), Rminus1_stop=0.01,
  Rminus1_cl_stop=0.02, covmat null (transcription fidèle) ;
lanceur : scripts/run_mcmc_g1_3.py (garde-fou : sorties refusées si un
  dépôt Git est détecté dans les ancêtres du préfixe) ;
burn-in d'analyse : 30 % par chaîne ; R-1 de Gelman-Rubin multi-chaînes.
```

## 2. LambdaCDM (M0)

### 2.1 Convergence

```text
convergence interne cobaya : les 4 chaînes ont convergé
  (20 640 à 38 640 pas acceptés ; R-1 bornes 0.0191-0.0199 <= 0.02) ;
R-1 multi-chaînes (burn-in 30 %) :
  omegam 0.00038 ; H0 0.00044 ; rdrag 0.00005 ;
échantillons post burn-in : 27 048 / 14 700 / 14 448 / 18 144 ;
ESS pondérée combinée : 45 001.
```

### 2.2 Posterior combiné

```text
param    moyenne    mediane    q16        q84        largeur68
omegam    0.30064    0.30061    0.29683    0.30446    0.00763
H0       68.34784   68.34803   68.04826   68.64619    0.59792
```

### 2.3 Contrôle T7 (vs chaînes officielles compressées)

```text
param    d_moyenne/sigma_off   largeur_ours/largeur_off   verdict
omegam        -0.0418                 0.9816               PASSE
H0            +0.0295                 0.9862               PASSE
T7 global : PASSE (seuils : <= 0.10 sigma ; largeurs ±5 %)
```

### 2.4 Minimum rencontré dans les chaînes (statistique d'échantillon)

```text
min chi2 total = 15.2140  (chi2_BAO = 11.5171 ; chi2_CMB = 3.6968)
point : H0 = 68.3471 ; ombh2 = 0.0224096 ; omm = 0.3005969
cohérence interne : contributions recalculées au point = colonnes de
chaîne (11.5171 / 3.6968) ;
cohérence externe : min repondéré G1.2 sur chaînes officielles = 15.2147.
```

À ne pas confondre avec le MAP ni le maximum de vraisemblance (§2.5).

### 2.5 Minimisations à départs multiples

```text
MAP, 5 départs (graines 1000-1004) :
  -logpost : 9.614145 à 9.614684 ; dispersion 5.4e-04 ;
  meilleur : chi2_total = 15.2124
    (H0 = 68.3526 ; ombh2 = 0.022410 ; omm = 0.300539) ;

maximum de vraisemblance, 5 départs (graines 1100-1104) :
  3/5 départs convergent au même point : chi2 = 15.2124 ;
  2 départs piégés (chi2 = 15.2451 et 26.4346), écartés par la
  comparaison multi-départs — rôle exact du protocole ;
  meilleur : chi2 = 15.2124 (H0 = 68.3527 ; omm = 0.300537) ;

lecture : priors uniformes constants => MAP et maximum de vraisemblance
coïncident numériquement (écart < 1e-4 en chi2) ; le minimum optimisé
(15.2124) est inférieur au minimum rencontré dans les chaînes (15.2140),
comme attendu.
```

### 2.6 Résidus BAO par composante au meilleur échantillon

```text
z        quantite     donnee      theorie     residu    residu/sigma
0.295    DV_over_rs       7.9417      7.9381   -0.0036    -0.047
0.510    DM_over_rs      13.5876     13.3137   -0.2739    -1.627
0.510    DH_over_rs      21.8629     22.5391   +0.6762    +1.577
0.706    DM_over_rs      17.3507     17.4829   +0.1322    +0.735
0.706    DH_over_rs      19.4553     20.0482   +0.5928    +1.776
0.934    DM_over_rs      21.5756     21.7567   +0.1811    +1.119
0.934    DH_over_rs      17.6415     17.5079   -0.1336    -0.664
1.321    DM_over_rs      27.6009     27.8317   +0.2309    +0.711
1.321    DH_over_rs      14.1760     14.0565   -0.1196    -0.532
1.484    DM_over_rs      30.5119     30.0253   -0.4866    -0.637
1.484    DH_over_rs      12.8170     12.8830   +0.0660    +0.127
2.330    DH_over_rs       8.6315      8.6386   +0.0071    +0.070
2.330    DM_over_rs      38.9890     38.9461   -0.0429    -0.081
```

## 3. CPL (M1)

### 3.1 Convergence

```text
convergence interne cobaya : les 4 chaînes ont convergé
  (56 400 / 142 400 / 193 200 / 219 400 pas acceptés ;
   R-1 bornes finales 0.0174-0.0198 <= 0.02) ;
R-1 multi-chaînes (burn-in 30 %) :
  omegam 0.00035 ; H0 0.00035 ; w 0.00027 ; wa 0.00026 ; rdrag 0.00017 ;
échantillons post burn-in : 153 580 / 135 240 / 39 480 / 99 680 ;
ESS pondérée combinée : 229 072.
```

### 3.2 Posterior combiné

```text
param    moyenne    mediane    q16        q84        largeur68
omegam    0.35245    0.35271    0.33013    0.37512    0.04499
H0       63.67567   63.56979   61.72647   65.61747    3.89100
w        -0.42725   -0.42286   -0.64999   -0.19873    0.45126
wa       -1.71697   -1.72065   -2.39217   -1.06402    1.32815
```

Cohérence avec les ancrages publiés (G0.1 §4) : Omega_m = 0,353 ± 0,022 ;
H0 = 63,7 ; w0 = -0,43 ± 0,22 ; wa = -1,72 ± 0,64 — tous retrouvés.

### 3.3 Contrôle T7 (vs chaînes officielles compressées)

```text
param    d_moyenne/sigma_off   largeur_ours/largeur_off   verdict
omegam        +0.0228                 0.9697               PASSE
H0            -0.0277                 0.9672               PASSE
w             +0.0271                 0.9702               PASSE
wa            -0.0271                 0.9737               PASSE
T7 global : PASSE (seuils : <= 0.10 sigma ; largeurs ±5 %)
```

### 3.4 Minimum rencontré dans les chaînes

```text
min chi2 total = 7.1633  (chi2_BAO = 7.1128 ; chi2_CMB = 0.0505)
point : H0 = 63.6603 ; ombh2 = 0.0222423 ; omm = 0.3515119 ;
        w = -0.4432219 ; wa = -1.6474341
cohérence interne : contributions recalculées au point = colonnes de
chaîne (7.1128 / 0.0505) ;
cohérence externe : min repondéré G1.2 sur chaînes officielles = 7.1806.
```

À ne pas confondre avec le MAP ni le maximum de vraisemblance (§3.5).

### 3.5 Minimisations à départs multiples

Constat de méthode (consigné) : les 5 départs NAÏFS tirés des
distributions de référence des configs (concentrées vers w = -1,
wa = 0) échouent tous — meilleur chi2 : 10.098 (MAP), 11.418 (maxlike),
dispersions 5.4 et 3.7 — la vallée de dégénérescence w0-wa piège
l'optimiseur loin du minimum. Le protocole multi-départs a joué son rôle
de détection. Les minimisations retenues utilisent des DÉPARTS INFORMÉS :
les meilleurs échantillons des 4 chaînes comme points de départ
(chi2 initiaux 7.1633 à 7.1759).

```text
MAP, 5 départs informés (graines 3000-3004) :
  chi2_total : 7.1641 à 7.2430 ; dispersion (objectif) 3.9e-02 ;
  meilleur : chi2 = 7.1641
    (H0 = 63.7277 ; ombh2 = 0.022255 ; omm = 0.350445 ;
     w = -0.450176 ; wa = -1.619265) ;

maximum de vraisemblance, 5 départs informés (graines 3100-3104) :
  chi2_total : 7.1545 à 7.2742 ; dispersion (objectif) 6.0e-02 ;
  meilleur : chi2 = 7.1545
    (H0 = 63.7279 ; ombh2 = 0.022253 ; omm = 0.350574 ;
     w = -0.451261 ; wa = -1.617966) ;

lecture : priors uniformes + contrainte jointe inactive à l'optimum
=> MAP et maximum de vraisemblance coïncident à la tolérance de
l'optimiseur près (écart 0.010, dispersions 0.04-0.06) ; le minimum
optimisé (7.1545) est inférieur au minimum rencontré dans les chaînes
(7.1633), comme attendu.
```

### 3.6 Résidus BAO par composante au meilleur échantillon

```text
z        quantite     donnee      theorie     residu    residu/sigma
0.295    DV_over_rs       7.9417      7.9845   +0.0429    +0.563
0.510    DM_over_rs      13.5876     13.3433   -0.2443    -1.451
0.510    DH_over_rs      21.8629     22.0299   +0.1669    +0.389
0.706    DM_over_rs      17.3507     17.4319   +0.0812    +0.451
0.706    DH_over_rs      19.4553     19.7465   +0.2912    +0.872
0.934    DM_over_rs      21.5756     21.6648   +0.0891    +0.551
0.934    DH_over_rs      17.6415     17.4369   -0.2046    -1.018
1.321    DM_over_rs      27.6009     27.7561   +0.1552    +0.478
1.321    DH_over_rs      14.1760     14.1723   -0.0037    -0.017
1.484    DM_over_rs      30.5119     29.9707   -0.5412    -0.709
1.484    DH_over_rs      12.8170     13.0209   +0.2039    +0.394
2.330    DH_over_rs       8.6315      8.7324   +0.1009    +0.998
2.330    DM_over_rs      38.9890     38.9974   +0.0084    +0.016
```

Constat descriptif : la paire tendue à z = 0,51 sous LambdaCDM
(±1,6 sigma) est réduite sous CPL (DM -1,45 ; DH +0,39) ; la
contribution CMB au meilleur échantillon passe de 3,70 (LCDM) à 0,05.

## 4. Contraste CPL - LambdaCDM

```text
niveau                                   LCDM       CPL       contraste
minimum optimisé (multi-départs)         15.2124    7.1545    -8.058
minimum rencontré dans les chaînes       15.2140    7.1633    -8.051
rappel G1.2 (chaînes officielles
  repondérées, minima d'échantillon)     15.2147    7.1806    -8.034
ancrage déclaré DESI (Delta chi2_MAP)                          -8.0
```

Les trois niveaux calculés ici et l'ancrage déclaré concordent autour de
-8.0 à -8.06 ; la dispersion des minimisations (0.04-0.06) borne la
précision du contraste optimisé à ± ~0.05. Chaque niveau reste étiqueté
comme tel — aucun minimum d'échantillon n'est qualifié de meilleur point
de profil (interdit #63).

## 5. Distinctions strictes tenues

```text
posterior : moyennes/médianes/intervalles 68 % pondérés (§2.2, §3.2) ;
MAP : minimum de -log(posterior), minimisations multi-départs ;
maximum de vraisemblance : minimum de -log(vraisemblance), prior ignoré ;
minimum rencontré dans les chaînes : statistique d'échantillon, jamais
  qualifiée de meilleur point de profil (interdit #63).
```

## 6. Zenodo

Compte Zenodo authentifié et relié à ORCID/GitHub — disponibilité déclarée
par l'utilisateur, non testée par l'agent. Aucune opération d'archivage ;
décision distincte : #64.

## 7. État

```text
chaînes : 4 LCDM + 4 CPL, toutes convergées sous la règle d'arrêt
  transcrite (R-1 0.01 / bornes 0.02) ; multi-chaînes R-1 <= 4.4e-4 ;
T7 : PASSE pour les deux modèles
  (déplacement max 0.042 sigma ; largeurs entre -3.3 % et -1.4 %) ;
minimisations : LCDM — départs de référence suffisants ;
  CPL — départs informés par les chaînes nécessaires (échec documenté
  des départs naïfs dans la vallée w0-wa) ;
contraste CPL-LCDM : -8.058 (optimisé) / -8.051 (rencontré) /
  -8.034 (repondéré G1.2) / -8.0 (déclaré DESI) ;
chaînes et sorties : hors Git ; PR #65 : brouillon, aucun merge ;
X(z) : toujours fermé ;
suite : validation humaine du présent rapport, re-ratification de T7,
  puis décision d'ouverture de G2.
```
