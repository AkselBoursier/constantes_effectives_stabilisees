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
  oracle = 1.364e-12 ; valeur vraie = 3.549541e-9 (quad resserré,
  erreur estimée 8.7e-16 ; GL indépendante concordante à 3e-16).
  L'écart est physiquement négligeable (< 1e-8 Mpc) mais interdit
  toute équivalence à 1e-10 Mpc contre l'oracle par une quadrature
  propre ;
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

```text
par variante (4 variantes, 331 points au total, 280 valides comparés) :
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
  speedup représentatif : 12.0x / 12.1x (deux passes) vs oracle
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
sorties normalisées bit à bit identiques (diff vide) ;
temps/mémoire et verdicts chronométrés : section séparée, exclue du
diff déterministe (les comptages d'appels CAMB, déterministes, restent
dans la sortie normalisée).
```

## 8. Limites

```text
- l'équivalence bit à bit est démontrée sur l'ensemble gelé (331
  points x 4 variantes) et garantie par construction (mêmes quadratures,
  intégrandes aux valeurs identiques, égalité bitwise de la spline
  vérifiée) — elle n'est pas un théorème sur tout le prior continu ;
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

## 9. Verdict sur G2.4c-iii

```text
équivalence : bit-identique sur l'ensemble gelé, classification
  incluse ; seuils T8-T12 : tous respectés sans relâchement ;
fautes : 14/14 détectées + ordre historique ;
speedup représentatif : 12.0x >= 10x (cible atteinte ;
  ~64x vs coût de production G2.4b) ;
évaluation lente : 0.68x l'oracle (critère <= 1.10x) ;

VERDICT : la porte recommande l'ouverture de G2.4c-iii (raccord au
lanceur G2.4b fusionné), SANS autoriser la production : le premier
lancement réel reste soumis au manifeste à deux clés et à une décision
humaine distincte.
```
