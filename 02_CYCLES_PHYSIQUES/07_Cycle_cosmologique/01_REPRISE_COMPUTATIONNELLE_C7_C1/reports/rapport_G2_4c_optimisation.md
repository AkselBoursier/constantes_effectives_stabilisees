# Rapport G2.4c-ii — implémentation optimisée O1+O3 qualifiée, sans MCMC

Issue directrice : #63 (G2.4c-i validée ; ouverture bornée G2.4c-ii).
Branche : `comp/c7-c1-xz-computational-optimization`, base
`5697323dc19d30c33f06b7dacb8e1a86a701732c`. Oracle intouché :
`xz_background_g2_1.py` + `xz_likelihood_g2_3.py`. Fichiers créés :
`scripts/xz_fast_g2_4c.py`, `scripts/qualify_xz_optim_g2_4c.py`, le
présent rapport — rien d'autre.

```text
MCMC / minimisation / posterior : ABSENTS ;
lanceur G2.4b : NON modifié ; manifeste réel : AUCUN ;
aucun chi2 interprété (seuls des écarts |candidat - oracle| publiés) ;
aucun émulateur, aucune interpolation de r_drag/r_star/theta_star ou
d'une sortie CAMB, aucune approximation acoustique, aucune table
précalculée sur les paramètres.
```

## 1. Architecture Theory/likelihood (O1)

```text
ReferenceLenteXZ (cobaya Theory)  : dépend exclusivement de H0, ombh2,
  omm ; fournit le produit « etat_lent_xz » ; cache d'états Cobaya
  (taille 8) + fabrique interne exacte bornée (8, FIFO) ;
VraisemblanceRapideXZ (Likelihood) : dépend directement des seuls X_i ;
  consomme l'état par provider.get_result (mécanisme officiel) ;
état lent immuable : (H0, ombh2, omm) exacts, CambReference, identité
  variante/convention, empreinte déterministe, grilles/poids Simpson et
  H_ref² pré-évalués (tableaux verrouillés en écriture) ;
clés de cache = valeurs complètes, sans arrondi ni hachage tronqué ;
une construction levant une exception n'entre jamais dans un cache
  (garanti aussi par Cobaya : theory.py l.246-270).
```

Démonstrations par appels déterministes au modèle Cobaya (aucune MCMC) :

```text
variation d'un X_i seul            : 0 nouvel appel CambReference.from_g1 ;
variation de H0                    : exactement 1 nouvel état lent ;
retour à un triplet encore caché   : 0 nouvel appel (réutilisation exacte) ;
graphe de blocs (split_fast_slow, oversample_power 0.4) :
  bloc lent  = [H0, ombh2, omm] ;
  bloc rapide = [X1..X5] — exactement le graphe déclaré ;
séquence représentative            : 4 appels CAMB pour 4 cycles (exact).
```

O2 (blocage manuel) reste une réserve de réglage : le graphe mesuré par
Cobaya correspond déjà exactement aux dépendances déclarées.

## 2. Méthode de calcul (O3 requalifiée) et CONSTATS sur l'oracle

La qualification a établi deux constats numériques sur l'oracle,
déterminants pour l'architecture retenue :

```text
C1 — corrections acoustiques : quad(epsabs=1e-8) SOUS-RÉSOUT ces
  intégrales minuscules. Exemple mesuré (profil P2, M2a-N) :
  oracle = 1.364e-12 ; référence resserrée = 3.549541e-9 (quad
  epsabs=1e-15/epsrel=1e-13, erreur estimée 8.7e-16, corroborée par
  une quadrature indépendante Gauss-Legendre concordante à 3e-16).
  L'écart est petit en valeur absolue (< 1e-8 Mpc) mais interdit
  toute équivalence à 1e-10 Mpc contre l'oracle par une quadrature
  propre (son évaluation aux seuils T12(b) : voir §8 bis) ;
C2 — D_M : le bruit propre des quads adaptatifs de l'oracle vaut
  ~5.7e-13 rel aux z BAO et ~4.8e-10 rel sur l'annulation
  D_M(z_star)-D_M(2.33), INDÉPENDANT de l'ordre Simpson opposé —
  amplifié par les grands résidus, il rend les seuils absolus de chi2
  inatteignables contre l'oracle pour toute implémentation « plus
  vraie » que lui.
```

Architecture retenue en conséquence — RÉPLIQUE ORACLE INTÉGRALE :

```text
toutes les quadratures publiées (D_M aux 13 z BAO, D_M(z_star),
  corrections r_drag/r_star) sont les MÊMES scipy.quad que l'oracle
  (tolérances, bornes, points de scission aux nœuds et à z=2.33
  identiques), avec des intégrandes RÉÉCRITES rapides aux valeurs
  bit à bit identiques :
  - évaluation scalaire de la spline par le schéma de Horner exact de
    scipy PPoly (égalité bitwise vérifiée de façon bloquante sur 4097
    points) ;
  - H_ref scalaire par le même appel CAMB ; associativité flottante
    préservée à l'identique ;
  - sémantique d'invalidité identique : H_X² <= 0 détecté au même
    point d'échantillonnage, dans le même ordre d'évaluation
    (rdrag -> D_M BAO -> D_H -> D_M(z_star)) ;
la queue z >= 2.33 n'exploite que l'identité pré-enregistrée
  X(z) = X(2.33) : la dépendance rapide passe par la seule dernière
  amplitude nodale ;
le calcul PAR LOTS ET CUMULATIF (Simpson composite par segments
  scindés aux nœuds, aux z BAO et à z=2.33 ; H_ref et X évalués en
  tableaux ; cumuls partagés pour tous les D_M) est conservé comme
  CONTRE-CONTRÔLE de qualification (verif_simpson), hors chemin de
  production.
```

Toutes les sorties publiées sont donc identiques à l'oracle AU BIT PRÈS
— l'accélération vient du coût des intégrandes (~10x) et de la
réutilisation de l'état CAMB (O1), pas d'un changement de méthode.

## 3. Étude de convergence du contre-contrôle Simpson

```text
règle : Simpson composite ; variable : z sur [0, 2.33] (scission aux
  nœuds, z BAO, 2.33), u = 1/sqrt(1+z) sur [2.33, z_star] ;
suite prédéclarée (puissances de deux) : 2048, 4096, 8192, 16384, 32768
  intervalles par segment ; choix global par classe, jamais par point ;
seuils croisés (vs répliques ; ~20x au-dessus des planchers C2) :
  principal <= 1e-11 rel ; queue <= 1e-8 rel à D_M(z_star) ;
ordre retenu : principal 2048 ; queue 2048
  (pire rapport écart/seuil : 0.057) ;
doublement (4096/4096) : PASSE (pire rapport 0.048) ;
coût : contre-contrôle seulement — absent du chemin de production ;
une faute d'ordre volontairement insuffisant (8) dépasse les seuils
  de >= 1e5x : DÉTECTÉE.
```

## 4. Ensemble d'équivalence gelé et résultats

Couverture G2.4c-ii-a : TOUT point oracle-valide entre dans les
comparaisons numériques, sans exclusion (ni étiquette de couche
frontière, ni boîte de fonds, ni taille de résidu CMB, ni proximité de
H_X² = 0) ; les points oracle-invalides sont contrôlés en
classification. Condition bloquante : nombre numériquement comparé ==
nombre oracle-valide (un auto-test de retrait d'un point oracle-valide
produit un code non nul).

```text
COMPTES DE COUVERTURE (par variante : total / oracle-valide /
oracle-invalide / numériquement comparé / classification-only) :
  M2a-N :  82 / 77 / 5 / 77 / 5
  M2a-K :  85 / 79 / 6 / 79 / 6
  M2b-N :  81 / 74 / 7 / 74 / 7
  M2b-K :  83 / 76 / 7 / 76 / 7
  TOTAL : 331 / 306 / 25 / 306 / 25
condition nominale : numériquement comparé == oracle-valide : VÉRIFIÉE
  (306 == 306) ; auto-test : le retrait artificiel d'un point
  oracle-valide (C7C1_TEST_RETRAIT_POINT) produit exit 1 — VÉRIFIÉ.

composition par variante (331 points au total sur quatre variantes) :
  P0, P1 (X_i = 1) ; P2 signé ; P3 oscillatoire ;
  bords exacts de P_WS (tous X = 4 ; alternance -2/4) ;
  voisinage H_X² -> 0+ (bissection déterministe sur le statut oracle,
    marges ±10 %) et sonde rejetée correspondante ;
  sondes invalides (fond et X) ;
  64 tirages valides (8 fonds x 8 profils, graine NumPy 642401,
    acceptation par le seul statut valide/invalide de l'oracle) ;
  sondes plein-priors et couche frontière : classification seulement ;
  sondes H : nœuds, 2.33 ± 1e-9, 2.33, zdrag, zstar ;

classification valide/invalide : STRICTEMENT IDENTIQUE (331/331) ;

pires écarts (seuils T8-T12 inchangés, aucun relâché) :
  H relatif        0.0   (<= 1e-13)     BAO relatif      0.0 (<= 1e-13)
  theta_star abs   0.0   (<= 1e-9)      chi2_BAO abs     0.0 (<= 1e-10)
  chi2_CMB abs     0.0   (<= 1e-3)      rdrag abs        0.0 (<= 1e-10)
  rstar abs        0.0   (<= 1e-10)     D_M(z_star) rel  0.0 (<= 1e-8)
  correction acoustique abs 1.41e-14    (<= 1e-13)
```

Historique de mise au point consigné : les seuils absolus de chi2 sont
inatteignables contre cet oracle par toute quadrature indépendante sur
les points à très grands résidus (constat C2) — c'est ce qui a imposé la
réplique bit à bit, qui les rend triviaux (0.0) sur tout le domaine,
couche frontière incluse.

## 5. Tests adversariaux (14/14 détectées, code non nul)

```text
état lent d'un autre triplet ; état lent périmé après changement lent ;
descripteur d'une autre variante ; natural/not-a-knot croisés ;
cache partagé entre variantes ; collision artificielle de clé ;
construction lente échouée puis réutilisée (rien en cache après échec) ;
segment z=2.33 omis (la construction de l'état REFUSE) ;
queue de D_M(z_star) omise ; queue acoustique omise ;
ordre de quadrature volontairement insuffisant ;
classification valide/invalide divergente (invalidité ignorée) ;
graphe Cobaya restant en un seul bloc (architecture G2.4b : détecté) ;
nouvel appel CAMB lors d'une variation X_i seule (cache désactivé).

ordre historique : parcours A,B,C,A et C,A,B,A — sorties identiques
point à point (chi2_BAO/CMB/total) : PASSE.
```

## 6. Performance (mesures séparées du diff déterministe)

```text
état lent neuf                     : 0.042 s (CAMB compris) ;
état lent en cache                 : ~1 µs ;
évaluation rapide (X_i seuls)      : 4.1 ms  (17.5x l'oracle réchauffé) ;
évaluation lente complète          : 49 ms = 0.68x l'oracle réchauffé
                                     (critère <= 1.10x : dépassé en mieux) ;
séquence représentative (4 cycles x [1 lent + 25 rapides],
  facteur de suréchantillonnage prédéclaré 5) :
  5.95 ms par évaluation ; 4 appels CAMB pour 104 évaluations ;
  speedup représentatif : 12.0x à 13.6x selon les passes vs oracle
  réchauffé — mesure CONSERVATRICE : contre le coût de production
  mesuré en G2.4b (~0.38 s/éval, CAMB froid à chaque pas dans le bloc
  unique), le même mélange vaut ~64x ;
mémoire du cache d'états (8 états) : 4.6 Mo ; caches bornés partout.

nouvelle projection de faisabilité (32 chaînes, longueurs G2.4b-i,
acceptation ~0.2, 5.95 ms/éval) :
  basse 153k    : ~41 h CPU  (~5 h à 8 chaînes parallèles) ;
  centrale 330k : ~87 h CPU  (~11 h) ;
  haute 880k    : ~233 h CPU (~29 h).
Le lot passe de semaines-mois à heures-jours sur la machine locale.
```

## 7. Déterminisme

```text
qualification complète exécutée DEUX FOIS : exit 0 et exit 0 ;
sorties normalisées bit à bit identiques (diff vide) — couverture
  complète et diagnostic acoustique inclus dans la sortie normalisée ;
temps/mémoire et verdicts chronométrés : section séparée, exclue du
diff déterministe (les comptages d'appels CAMB, déterministes, restent
dans la sortie normalisée) ;
auto-test d'échec : un point oracle-valide artificiellement retiré de
la comparaison (C7C1_TEST_RETRAIT_POINT) produit exit 1 — VÉRIFIÉ.
```

## 8. Limites

```text
- l'équivalence bit à bit est démontrée sur l'ensemble gelé (331
  points au total sur quatre variantes, tous les points oracle-valides
  comparés) et étayée par construction (mêmes quadratures, intégrandes
  aux valeurs identiques, égalité bitwise de la spline vérifiée) —
  elle n'est pas un théorème sur tout le prior continu ;
- les constats C1/C2 documentent un bruit numérique PROPRE À L'ORACLE
  (sous-résolution des corrections acoustiques ; ~5e-13/5e-10 rel sur
  D_M) : hérité tel quel par la réplique, par fidélité — tout
  raffinement relèverait d'un amendement d'oracle, porte distincte ;
- le facteur de suréchantillonnage de la séquence représentative (5)
  est prédéclaré (justifié par (rapport de vitesses)^0.4) ; le facteur
  effectif en production sera fixé par Cobaya ;
- speedup mesuré sur cette machine ; les valeurs absolues varient, les
  comptages d'appels CAMB (déterministes) non ;
- couche frontière H_X²->0+ et sondes plein-priors : classification
  strictement identique vérifiée ; devenues non contraignantes pour les
  seuils depuis la réplique (écarts 0.0).
```

## 8 bis. Diagnostic acoustique non productif (G2.4c-ii-a/-b)

Sans modification de l'oracle ni de la candidate de production. Règle
numérique fixée avant exécution et appliquée aux quatre variantes sur
P0–P3 :

```text
resserrée : scipy.quad, variable z, bornes [z_depart, 1e7],
  epsabs = 1e-15, epsrel = 1e-13, limit = 800 ;
contrôle indépendant : Gauss-Legendre, variable u = 1/sqrt(1+z),
  segments [z_depart, z_star], [z_star, 1e4], [1e4, 1e6], [1e6, 1e7],
  512 points par segment ; contrôle de convergence : 1024 points ;
  appliqué SÉPARÉMENT aux deux corrections, règle IDENTIQUE hormis la
  borne initiale (z_drag pour r_drag, z_star pour r_star) ;
concordance BLOQUANTE resserrée vs GL512, pour CHACUNE des deux
  corrections : seuil 1e-13 Mpc (absolu), déclaré avant exécution,
  fondé sur les planchers observés en G2.4c-ii-a, maxima mesurés sur
  les 16 points de la sortie conservée de la passe 1 : concordance
  resserrée-GL512 2.333e-15 Mpc (point M2a-K:P3), convergence GL
  512/1024 7.027e-16 Mpc ; seuil fixé ~43x au-dessus, GLOBAL —
  identique pour les deux corrections et tous les points, sans
  ajustement point par point ; les maxima de concordance et de
  convergence sont désormais PUBLIÉS dans la sortie normalisée
  (concordance_GL_max, convergence_GL_max), rendant les planchers
  traçables dans le dépôt ;
garantie de compte : les 16 points (4 variantes x P0-P3) doivent tous
  entrer au diagnostic — tout point manquant est un échec bloquant ;
grandeurs publiées par point : corr_rdrag_resserree,
  corr_rstar_resserree, controle_GL512_rdrag, controle_GL1024_rdrag,
  convergence_GL_rdrag, controle_GL512_rstar, controle_GL1024_rstar,
  convergence_GL_rstar, concordances resserrée-GL, corrections de
  l'oracle courant, écart oracle–resserré, Δtheta_star, écart max du
  vecteur BAO, Δchi2_BAO, Δchi2_CMB.
```

Résultats (aucune interprétation cosmologique ; valeurs complètes dans
la sortie normalisée de la qualification) :

```text
exemple (M2a-N : P2) :
  corr r_drag : oracle 1.364242e-12 ; resserrée 3.549540e-9 ;
    GL512 3.549542e-9 ; GL1024 3.549542e-9 ;
    convergence GL 1.13e-16 ; concordance resserrée-GL 1.80e-15 ;
  corr r_star : oracle 1.335820e-12 ; resserrée 3.195187e-9 ;
    GL512 3.195188e-9 ; GL1024 3.195188e-9 ;
    convergence GL 1.01e-16 ; concordance resserrée-GL 5.83e-16 ;
  écart oracle-resserré : 3.548e-9 (r_drag) / 3.194e-9 (r_star) ;
  Δtheta_star 2.23e-13 ; écart BAO max 1.02e-9 ;
  Δchi2_BAO -8.4e-7 ; Δchi2_CMB -2.7e-5 ;

maxima absolus sur les 16 points (4 variantes x P0-P3) :
  corr oracle                 <= 2.02e-12 Mpc (r_drag et r_star) ;
  corr resserrée              <= 5.32e-9 (r_drag) / 4.79e-9 (r_star) ;
  écart oracle-resserré       <= 5.32e-9 (r_drag) / 4.79e-9 (r_star) ;
  concordance resserrée-GL512 : 2.33e-15 (r_drag) / 7.34e-16 (r_star)
    — BLOQUANTE, seuil 1e-13 : PASSÉE pour les deux corrections ;
  convergence GL 512/1024     : 7.03e-16 (r_drag) / 6.96e-16 (r_star) ;
  Δtheta_star                 <= 3.57e-13 ;
  écart vecteur BAO           <= 1.48e-9 (absolu) ;
  Δchi2_BAO                   <= 8.47e-7 ;  Δchi2_CMB <= 4.45e-5.
```

Rapports aux seuils de contrôle T12(b), publiés tels quels :

```text
max |correction resserrée| / 1e-10 : 5.324313e-9  / 1e-10 = 53.24 ;
max |Δchi2_BAO|            / 1e-8  : 8.463585e-7  / 1e-8  = 84.64 ;
max |Δchi2_CMB|            / 1e-3  : 4.447887e-5  / 1e-3  = 0.04448 ;
max |Δtheta_star|          / 1e-9  : 3.566753e-13 / 1e-9  = 3.567e-4.
```

Les effets restent petits en valeur absolue, mais la correction
acoustique et Δchi2_BAO dépassent les seuils de contrôle T12(b).
Cette rupture impose un amendement explicite ; aucune conclusion
cosmologique n'est tirée.

## 8 ter. Proposition d'amendement D3-H (PROPOSÉE, NON APPLIQUÉE)

```text
date proposée      : 30 juillet 2026 ;
version proposée   : amendement A1 du mode « corrected » (v1.1) ;

clause ancienne exacte (implémentation actuelle de l'oracle,
xz_background_g2_1.XZBackground._sound_horizon_correction) :
  quad(integrande, z_depart, acoustic_zmax,
       epsabs=self.epsabs=1e-8, epsrel=self.epsrel=1e-10,
       limit=self.quad_limit=300)
  — le mode « corrected » ratifié en T12(b) repose sur cette règle ;

anomalie démontrée : sur des intégrales de correction d'ordre
  1e-12..1e-8 Mpc, epsabs=1e-8 autorise un arrêt prématuré ; valeurs
  rendues non convergées (ex. 1.364e-12 rendu contre 3.549541e-9 en
  référence resserrée corroborée indépendamment) — défaut numérique
  RÉEL du mode corrected ; les effets mesurés restent petits en valeur
  absolue, mais la correction acoustique et Δchi2_BAO dépassent les
  seuils de contrôle T12(b) (voir §8 bis) — cette rupture impose le
  présent amendement explicite ; aucune conclusion cosmologique n'est
  tirée ;

résultats déjà visibles avant amendement : G2.1 (I1-I9, T8-T12),
  G2.3a (C1-C8), G2.4b (banc, aucune chaîne), G2.4c-i/ii (profilage,
  qualification, diagnostic §8 bis) — AUCUNE chaîne MCMC X(z) n'a été
  produite ; aucun posterior n'existe ;

règle candidate UNIQUE (A1) :
  corrected-v1.1 :
    scipy.quad en variable z ;
    bornes inchangées ;
    epsabs = 1e-15 ;
    epsrel = 1e-13 ;
    limit = 800.
  la quadrature Gauss-Legendre en u = 1/sqrt(1+z) reste EXCLUSIVEMENT
  un contrôle indépendant (jamais une règle de production candidate) ;

maintien du mode historique : l'ancienne règle est conservée sous
  « corrected-legacy » à des fins de régression et de traçabilité
  (aucune suppression) ;

fichiers affectés si ratifié : scripts/xz_background_g2_1.py (oracle),
  scripts/xz_fast_g2_4c.py (réplique alignée), rapports G2.1/G2.4c ;

contrôles à rejouer : suite I1-I9 complète, T8-T12, qualification
  G2.3a (C1-C8), qualification G2.4c-ii (double passe) ;

modèles/sensibilités à réexécuter : aucun résultat d'inférence
  n'existe ; T12(b) devra être re-ratifiée ; S5 (corrected vs fixed)
  reste la sensibilité de contrôle au moment de la production ;

statut de l'amendement : PROPOSÉ ; NON APPLIQUÉ ; soumis à validation
  humaine explicite ;

condition de validation : décision humaine explicite dans #63, datée
  et versionnée conformément à D3-H — la présente section est une
  PROPOSITION ; aucune clause D3-A..H n'est modifiée par ce commit.
```

### Addendum §8 ter-A1 — statut postérieur (G2.4c-iii)

La condition de validation ci-dessus a été satisfaite : **l'amendement
A1 a été ratifié humainement le 30 juillet 2026** (#63, ouverture de la
porte G2.4c-iii) puis **appliqué explicitement** en G2.4c-iii — modes
`corrected-v1.1` (directeur, alias du nom nu `corrected`) et
`corrected-legacy` (ancienne règle, bit à bit), chemin rapide aligné,
suites I1-I9 / T8-T12 / C1-C8 / G2.4c-ii rejouées. Le texte des §8 bis
et §8 ter ci-dessus est conservé tel quel à titre de trace : les
valeurs « oracle » y sont désormais à lire comme `corrected-legacy`.
Résultats complets : `reports/rapport_G2_4c_iii_amendement_A1.md`.

## 9. Verdict sur G2.4c-iii

```text
équivalence : bit-identique sur l'ensemble gelé, classification
  incluse ; seuils T8-T12 : tous respectés sans relâchement ;
fautes : 14/14 détectées + ordre historique ;
speedup représentatif : 12.0x à 13.6x selon les passes, >= 10x
  (cible atteinte ; ~64x vs coût de production G2.4b) ;
évaluation lente : 0.68x l'oracle (critère <= 1.10x) ;

VERDICT : la porte recommande l'ouverture de G2.4c-iii (raccord au
lanceur G2.4b fusionné), SANS autoriser la production : le premier
lancement réel reste soumis au manifeste à deux clés et à une décision
humaine distincte.
```
