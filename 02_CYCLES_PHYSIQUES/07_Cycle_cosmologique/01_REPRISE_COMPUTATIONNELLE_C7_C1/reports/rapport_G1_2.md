# Rapport G1.2 — qualification de la vraisemblance commune avant échantillonnage

Issue directrice : #63. Autorisation et prescriptions : commentaire G1.2
(arbitrage des deux vraisemblances). Aucun échantillonnage MCMC lancé.
Aucun coefficient CMB ajusté sur les chaînes n'est promu comme donnée
officielle. Aucun chemin absolu local.

## 1. Push et PR brouillon (auditabilité)

```text
branche poussée sans réécriture : comp/c7-c1-comparaison-commune ;
PR brouillon : #65 (base main, liée à #63) — AUCUN MERGE ;
contenu vérifié via l'API au push initial : les 12 fichiers déclarés de
G1.0 ; après le commit G1.2, la PR contient 17 fichiers = 12 (G1.0)
+ 5 ajouts (G1.2) ;
données externes suivies : aucune.
```

## 2. Convention CMB ratifiée et repondération complète

Convention appliquée : `CMB_compressed_public_DR2_rounded` — coefficients
publiés (éq. 35–36, DESI DR2 Results II v3) tels quels, transcrits dans
`scripts/c7c1_likelihoods.py`. Aucune prétention de reproduction
byte-identique de la compression interne DESI.

### 2.1 Méthode de calcul de theta_star par échantillon

Décision de méthode, après deux tentatives d'émulation documentées :

- un émulateur polynomial (deg 4, 600 points) valide à 0,0016 sigma_theta
  en LambdaCDM (3D) mais échoue en CPL (5D) ;
- l'enrichissement (deg 6, 3000 points, étage RBF, queue de Mahalanobis
  exacte à 5 %) plafonne à 0,0165 sigma_theta : le diagnostic aux pires
  points de validation montre que TOUS se situent sur ou près du
  croisement w(a) = -1. Constat borné : l'échec de l'émulation lisse est
  LOCALISÉ près de ce croisement ; le mécanisme précis n'est pas établi
  (CAMB présente PPF comme une approximation destinée à permettre ce
  franchissement de manière lissée — l'attribution d'un « pli » à PPF
  reste donc suspendue) ;
- tests de sensibilité et de convergence numérique de la cible :
  perturbations relatives 1e-9 des entrées → variations ~1e-12 de
  theta_star (sensibilité aux entrées) ; AccuracyBoost=2 → +2,2e-10
  (0,0001 sigma_theta ; contrôle de convergence numérique). Ces tests ne
  constituent pas une mesure directe de répétabilité, mais ils bornent la
  variabilité numérique de la cible très au-dessous des résidus
  d'émulation observés : l'écart venait de l'émulation, pas de la cible.

**Mode directeur retenu : EXACT INTÉGRAL** — un appel CAMB 1.5.4 par
échantillon (107 532 CPL + 46 828 LambdaCDM), aucune émulation, aucune
charge de validation résiduelle. (Le mode hybride reste disponible dans le
script, avec arrêt automatique si sa validation échoue.)

### 2.2 Résultats LambdaCDM (46 828 échantillons, 4 chaînes)

```text
distribution ponderee de Delta chi2_CMB (poids officiels) :
  min=-0.8993 max=+1.0113 moyenne=+0.0841 ecart-type=0.2252
  quantiles 5/50/95 : -0.2873 +0.0816 +0.4552

ESS officiel=28636.9  ESS repondere=28321.3  ratio=0.9890
part des 10 plus gros poids reponderes : 0.1648 %

param   moy_off    moy_pub    d_moy/sig  med_off    med_pub    d_med/sig  d_largeur%
omegam   0.30081    0.30082    +0.0012    0.30070    0.30070    -0.0003    +0.221
H0      68.33840   68.33423    -0.0130   68.34629   68.34263    -0.0114    +0.127

meilleurs echantillons (min chi2 total) :
  officiel 15.1445 ; public 15.2147 ; public au point officiel optimal 15.2220

correlations ponderees de Delta chi2 :
  H0 +0.1151 ; omegam -0.0104 ; rdrag -0.2170 ; H0rdrag +0.0482
```

Contrôle de cohérence : le passage exact intégral reproduit à ~1e-4 près
les statistiques du mode émulé validé (0,0016 sigma_theta) — les deux
méthodes concordent là où l'émulateur était qualifié.

### 2.3 Résultats CPL (107 532 échantillons, 4 chaînes)

```text
distribution ponderee de Delta chi2_CMB (poids officiels) :
  min=-0.8813 max=+1.4595 moyenne=+0.0286 ecart-type=0.2261
  quantiles 5/50/95 : -0.3447 +0.0295 +0.3986

ESS officiel=57065.0  ESS repondere=56645.5  ratio=0.9926
part des 10 plus gros poids reponderes : 0.1082 %

param   moy_off    moy_pub    d_moy/sig  med_off    med_pub    d_med/sig  d_largeur%
omegam   0.35194    0.35203    +0.0041    0.35222    0.35233    +0.0047    -0.120
H0      63.73066   63.72003    -0.0054   63.61770   63.60591    -0.0059    -0.113
w       -0.43328   -0.43203    +0.0056   -0.42822   -0.42673    +0.0067    -0.136
wa      -1.69944   -1.70398    -0.0070   -1.70189   -1.70722    -0.0083    -0.059

meilleurs echantillons (min chi2 total) :
  officiel 7.1791 ; public 7.1806 ; public au point officiel optimal 7.2109

correlations ponderees de Delta chi2 :
  H0 +0.0476 ; omegam -0.0365 ; rdrag -0.1329 ; H0rdrag +0.0402 ;
  w -0.0499 ; wa +0.0622
```

Les moyennes officielles retrouvent les ancrages publiés (G0.1 §4) :
Omega_m = 0,352, H0 = 63,7, w0 = -0,43, wa = -1,70.

### 2.4 Critères provisoires d'acceptation

```text
critere                                    seuil        mesure (pire cas)      verdict
deplacement de chaque parametre directeur  <= 0.10 sig  0.0130 sig (H0, LCDM)  PASSE
variation de chaque largeur 68 %           <= 2 %       +0.221 % (omegam, LCDM) PASSE
variation du contraste Delta chi2 CPL-LCDM <= 0.2       0.069                  PASSE
  (officiel : 7.1791 - 15.1445 = -7.9654 ;
   public   : 7.1806 - 15.2147 = -8.0341)
ESS reponderee / queue de poids            suffisante   ratios 0.9890 et 0.9926 ;
                                                        top-10 poids <= 0.165 % PASSE
```

Les quatre critères provisoires sont satisfaits : l'arrondi de la
compression publique est **négligeable pour le calcul commun** au sens de
l'arbitrage G1.2. Le contraste public (-8.03) reste cohérent avec
l'ancrage déclaré DESI (Delta chi2_MAP = -8.0), sachant que le minimum sur
échantillons n'est pas le minimum de profil.

## 3. Contrôle BAO secondaire (indépendance d'implémentation)

Environnement séparé et épinglé : Cobaya 3.5.7 (première branche publique
avec `bao.desi_dr2`), CAMB 1.5.4, numpy 1.26.4 — gel complet dans
`requirements-c7c1-secondaire.txt`. Données installées par l'installateur
officiel (`cobaya-install bao.desi_dr2.desi_bao_all --upgrade`) dans un
chemin de paquets dédié.

Contrôle de provenance triple : les deux fichiers installés par
l'installateur officiel sont **byte-identiques** (SHA-256) aux octets
épinglés du manifeste (bao_data @ bb0c1c9) et à l'acquisition directe :

```text
mean : 9ac154ab583ce759c0f7eef3c978c7c70a6ead2d18774caceadf1a350a640585
cov  : 252a143274c8a07c78694c119617d36594f6d7965d00319ca611c6ffb886e509
```

Évaluation de la vraisemblance stock sur les MÊMES points fixes que G1.0 :

```text
LCDM   point 0      chi2 chaine 28.138814  stock 28.138816  delta +1.82e-06
LCDM   point 5766   chi2 chaine 11.775298  stock 11.775299  delta +8.40e-07
LCDM   point 11533  chi2 chaine 10.652586  stock 10.652586  delta -2.08e-07
CPL    point 0      chi2 chaine 32.952856  stock 32.952851  delta -4.78e-06
CPL    point 13566  chi2 chaine  8.373108  stock  8.373110  delta +1.76e-06
CPL    point 27132  chi2 chaine  9.598190  stock  9.598190  delta -1.61e-07
```

Le triangle est fermé à ~1e-6 près : bindings historiques (chaînes),
transcription contrôlée (voie primaire) et vraisemblance stock (voie
secondaire) coïncident sur les mêmes points, avec les mêmes octets.

## 4. Prior joint CPL : point accepté et point rejeté

`scripts/test_prior_joint_g1_2.py`, configuration CPL transcrite :

```text
point accepté (chaîne officielle) : w=-1.021781, wa=0.102660 (w+wa=-0.919121)
  contribution du prior joint = 0.0 ; logpost fini (-32.363265) ;
point rejeté : w=0.5, wa=0.5 (w+wa=1.0)
  logpost = -inf.
```

La contrainte `w0 + wa < 0` est encodée explicitement (bloc `prior`) et
vérifiée dans les deux sens.

## 5. Tolérances finales de reproduction proposées

Fondées sur les valeurs mesurées ci-dessus (marges explicites), soumises à
ratification :

```text
T1 — octets BAO : identité SHA-256 stricte au manifeste (aucune tolérance) ;
T2 — chi2_BAO en points fixes, toute implémentation vs chaînes
     officielles : |delta| <= 1e-4   (mesuré <= 5e-6, marge x20) ;
T3 — chi2_BAO voie primaire vs voie stock, points fixes :
     |delta| <= 1e-4                 (mesuré <= 7e-6) ;
T4 — dérivés : rdrag |delta| <= 0.01 Mpc (mesuré <= 1e-4) ;
     omegam |delta| <= 1e-5          (mesuré <= 1e-6) ;
T5 — CMB : chi2 de CMB_compressed_public_DR2_rounded est LA définition du
     lot (aucune tolérance vs compression interne DESI) ; son écart aux
     chaînes historiques est celui mesuré et accepté par la repondération
     (0.013 sig / 0.22 % / 0.069, critères 0.10 sig / 2 % / 0.2) ;
T6 — theta_star : calcul CAMB exact en production (jamais d'émulation) ;
     tests de sensibilité/convergence numérique : ~1e-12 sous
     perturbations 1e-9 des entrées ; 2.2e-10 = 0.0001 sig sous
     AccuracyBoost x2 (bornes numériques, non répétabilité directe) ;
T7 — reproduction des ancrages G0.1 §4 par le futur MCMC G1 :
     déplacement des moyennes <= 0.10 sigma vs valeurs publiées, largeurs
     68 % à ±5 % — à re-ratifier au vu des sorties G1.
```

## 6. Zenodo

Compte Zenodo authentifié et relié à ORCID/GitHub — disponibilité déclarée
par l'utilisateur, non testée par l'agent. Aucune opération d'archivage ;
décision distincte : #64.

## 7. État

```text
push + PR brouillon (#65) : faits ; PR = 12 fichiers G1.0 + 5 ajouts
  G1.2 (17 au total), aucun merge ;
repondération CMB complète : exécutée en exact intégral,
  4 critères d'acceptation PASSÉS ;
contrôle BAO secondaire : triangle bindings/transcription/stock fermé
  à ~1e-6, octets byte-identiques via l'installateur officiel ;
prior joint w0+wa<0 : testé, accepté/rejeté conformes ;
tolérances finales : proposées (§5), à ratifier ;
MCMC : toujours interdit ;
suite : validation humaine du présent rapport G1.2.
```
