# Rapport G2.3a — qualification des configurations X(z), sans inférence

Issue directrice : #63 (commentaires G2.3a et G2.3b). Branche :
`comp/c7-c1-xz-config-qualification`, depuis le merge G2.2
`f498086d07c8f971dfa104f5ad71b5e3a8e45d8e`. Pré-enregistrement directeur :
`reports/rapport_G2_2a_preregistration.md` (D3-A à D3-H, gelées).

```text
MCMC / échantillonnage / minimisation / optimisation : ABSENTS ;
posterior / préférence de modèle / interprétation cosmologique : ABSENTS ;
les chi2 rapportés aux points fixes sont des valeurs de contrôle
d'instrument, pas des résultats d'inférence.
```

## 1. Livrables (7 fichiers autorisés, aucun autre)

```text
configs/xz/g2_3_m2a_n.yaml   — M2a, natural,     graine 6301 ;
configs/xz/g2_3_m2a_k.yaml   — M2a, not-a-knot,  graine 6302 ;
configs/xz/g2_3_m2b_n.yaml   — M2b, natural,     graine 6303 ;
configs/xz/g2_3_m2b_k.yaml   — M2b, not-a-knot,  graine 6304 ;
scripts/xz_likelihood_g2_3.py      — évaluateur déterministe ;
scripts/qualify_xz_configs_g2_3.py — qualification, mode unique ;
reports/rapport_G2_3a.md           — le présent rapport.
```

Chaque YAML porte : le prior directeur `P_WS` (`X_i ~ U[-2,4]` pour chaque
amplitude libre, `X(0)=1` fixé), les priors de fond G1
(`H0 ~ U[20,100]`, `ombh2 ~ U[0.005,0.1]`, `omm ~ U[0.01,0.99]`), la
contrainte dure `omch2 > 0`, le traitement acoustique `corrected`, la
continuation `X(z>=2.33)=X(2.33)`, une graine explicite distincte, la
règle de sorties hors Git et la garde `inference.autorisee: false`.

L'évaluateur réutilise `CambReference`, `XZProfile` et `XZBackground` de
G2.1 sans réimplémentation du fond, et retourne : `logprior`, `chi2_BAO`,
`chi2_CMB`, `chi2_total`, vecteur BAO (13), vecteur CMB (3) et statut des
contraintes. `logprior = 0` à l'intérieur du support uniforme valide ;
`-inf` hors support, si `omch2 <= 0`, si le fond est non fini ou si
`H_X² <= 0`.

Le qualificateur ne possède qu'un mode. Les options `--mcmc`, `--sample`,
`--minimize`, `--optimize`, `--fit`, `--posterior`, `--chain` (et
variantes) sont refusées à l'entrée avec arrêt explicite ; aucun code
d'échantillonnage ou d'optimisation n'existe dans le module.

### Durcissement G2.3d — porte auto-bloquante et contrat YAML intégral

`validate_config` vérifie désormais TOUTE la configuration : `lot`,
`contraintes_dures` (liste exacte), `continuation` (chaîne exacte),
structure exacte des blocs `parametres_x` (clés nom/noeud/prior),
`prior`, `priors_fond`, `sorties` (`regle == hors_git`,
`variable_environnement == C7C1_XZ_OUT_DIR`, note non vide) et
`inference` (`autorisee is false`, note non vide) — sans clé manquante ni
supplémentaire — et la graine attendue par variante (M2a-N 6301,
M2a-K 6302, M2b-N 6303, M2b-K 6304).

La garde de répertoire de sortie `refuser_sortie_sous_git` LÈVE
`SortieSousGitError` pour tout chemin sous un ancêtre Git.

La qualification est une PORTE AUTO-BLOQUANTE : chaque condition
échouée est accumulée et la commande se termine par un code de sortie
NON NUL (`SystemExit(1)`) après impression du JSON — un `false` inscrit
dans la sortie ne suffit jamais. Conditions bloquantes : quatre
variantes exactes présentes une fois chacune ; graines exactes et
distinctes ; `logprior == 0.0` sur P0–P3 ; `logprior == -inf` sur
toutes les sondes invalides ; huit identités P0/P1 aux seuils T8 ;
T8–T12 tous vrais dans la ré-exécution I1–I9 (un verdict faux dans le
JSON du sous-processus est un échec même à code retour nul) ; C6 dans
ses tolérances ; FQ1–FQ4 détectées ; racine Git rejetée par exception ;
chemin externe accepté.

## 2. Environnement directeur et commandes

```text
Python 3.12.0 ; CAMB 1.5.4 ; NumPy 1.26.4 ; SciPy 1.13.1 ;
C7C1_DATA_DIR vers les octets BAO officiels hors Git ;

commande (exécutée DEUX FOIS, depuis la racine C7-C1) :
  python scripts/qualify_xz_configs_g2_3.py

diff entre les deux sorties : VIDE — bit à bit identiques.
```

## 3. Points fixes prédéclarés

Gelés dans le code avant la première exécution ; identiques entre
`natural` et `not-a-knot` d'une même grille :

```text
P0 : fond G1 de référence (H0=67.36, ombh2=0.02237, omm=0.3152), X_i=1 ;
P1 : MAP LambdaCDM G1 (H0=68.3526, ombh2=0.022410, omm=0.300539), X_i=1 ;
P2 : profil signé G2.1 — M2a : (0.6, -0.2, 0.4, 1.2, 0.8) ;
     adaptation M2b par suppression de l'amplitude du nœud 4/3 :
     (0.6, -0.2, 0.4, 0.8) ;
P3 : profil oscillatoire G2.1 — M2a : (1.4, 0.2, 1.6, 0.1, 1.3) ;
     M2b : (1.4, 0.2, 1.6, 1.3).
```

## 4. Résultats des contrôles

### C1/C2 — schéma strict et ordre exact (4/4 valides)

Clés exactes ; nœuds strictement croissants et identiques au verrou
`NODES` de G2.1 (représentations flottantes exactes de 1/3, 2/3, 4/3) ;
noms `X1..Xn` en bijection ordonnée avec les nœuds libres ; priors
`P_WS` exacts ; graines distinctes (6301–6304) ; garde d'inférence
présente dans chaque fichier.

### C3 — logprior sur points fixes et sondes (4 variantes × 8 points)

```text
                     M2a-N   M2a-K   M2b-N   M2b-K
P0, P1, P2, P3        0.0     0.0     0.0     0.0
X1 = 4.5 (haut)      -inf    -inf    -inf    -inf
X1 = -2.5 (bas)      -inf    -inf    -inf    -inf
omch2 <= 0           -inf    -inf    -inf    -inf
fond invalide        -inf    -inf    -inf    -inf
```

Valeurs de contrôle d'instrument aux points de stress (sans aucune
interprétation) : chi2_total(P2) = 22589.26 (M2a-N), 18889.54 (M2a-K),
24521.70 (M2b-N), 12442.77 (M2b-K) ; chi2_total(P3) = 858.60, 6014.08,
4445.14, 22055.99 respectivement. Leur dispersion entre conventions
illustre T12(a) ; aucune valeur n'est comparée à un modèle.

### C4 — identité P0/P1 avec LambdaCDM aux seuils T8 (8/8 PASSE)

Pire mesure sur les 4 variantes × 2 points : 7.40e-8 (chi2_CMB, seuil
T8 = 1e-3) ; BAO rel <= 4.4e-16 (seuil 1e-13) ; theta_star <= 1.7e-14
(seuil 1e-9) ; chi2_BAO <= 4.6e-13 (seuil 1e-10).

### C5 — ré-exécution complète de T8–T12 (suite I1–I9)

```text
T8  : PASSE   T9 : PASSE   T10 : PASSE   T11 : PASSE   T12 : PASSE
I9 (fautes G2.1 F1–F5) : toutes détectées.
```

Mesures maximales contrôlées contre les seuils ratifiés (détail dans la
sortie JSON) — aucune régression par rapport à G2.1.

### C6 — assemblage indépendant (sans bao_vector / cmb_vector)

Tolérances d'ingénierie fixées avant exécution (gardes d'assemblage,
pas des seuils scientifiques) : BAO abs <= 1e-12 ; CMB abs <= 1e-14.

```text
P0 : BAO abs max 1.8e-15 ; CMB abs max 0.0 — dans les tolérances ;
P2 : BAO abs max 3.6e-15 ; CMB abs max 0.0 — dans les tolérances.
```

### C7 — fautes injectées (4/4 détectées)

```text
FQ1 — nœuds 1/3 et 2/3 permutés dans une configuration en mémoire :
      REJETÉE par la validation stricte du schéma (nœuds non identiques
      au verrou / non croissants) — détectée ;
FQ2 — suppression de la division thetastar/100 dans le vecteur CMB :
      chi2_CMB passe de 2.20 à 1.93e11 — écart >> seuil T8 (1e-3) —
      détectée ;
FQ3 — continuation altérée (« extrapolation cubique ») :
      REJETÉE par validate_config — détectée ;
FQ4 — variable de sortie altérée (TMPDIR) :
      REJETÉE par validate_config — détectée.
```

### C8 — sorties hors Git (par exception)

```text
racine du dépôt : SortieSousGitError levée — REFUSÉE ;
répertoire externe hors Git : accepté sans exception.
```

### Preuve du chemin d'échec (code de sortie non nul)

```text
passes nominales (deux)                    : exit 0, sorties identiques ;
échec synthétique (C7C1_QUALIF_TEST_ECHEC) : exit 1,
  porte.passe = false, échec listé dans porte.echecs ;
option interdite (--mcmc)                  : exit 2, arrêt explicite.
```

Une régression de n'importe quelle condition bloquante produit donc un
code non nul, pas seulement un `false` dans le JSON.

## 5. Classification épistémique

```text
R1 — reproductibilité :
  ACQUISE — deux exécutions complètes de la qualification bit à bit
  identiques (diff vide) ; aucune source d'aléa dans le chemin de
  qualification (les graines des YAML ne servent qu'à l'inférence
  future, non lancée) ;

R2 — cohérence interne et stabilité :
  ACQUISE — schéma strict (C1/C2), grille de logprior conforme (C3),
  identité P0/P1 aux seuils T8 (C4), ré-exécution T8–T12 sans
  régression (C5), assemblage indépendant cohérent (C6), refus des
  sorties sous ancêtre Git (C8) ;

R3 — validation indépendante :
  HÉRITÉE DE G2.1 pour l'instrument (voie indépendante I8, étalonnage
  analytique EdS, fautes F1–F5), ré-exécutée ici via C5 ;
  APPORT PROPRE de cette porte : détection des fautes FQ1–FQ4 (C7) et
  preuve du chemin d'échec à code non nul — méta-validation des gardes
  de configuration et de la porte elle-même ; l'assemblage C6 partage
  les briques dm/dh/rdrag de l'instrument : il est classé R2
  (contrôle d'assemblage sous tolérances d'ingénierie), pas R3 ;

limites restantes :
  - les chi2 aux points P2/P3 ne sont validés par aucune voie
    indépendante complète (seuls leurs ingrédients le sont via I8) ;
  - la liste de fautes FQ1–FQ4 n'est pas exhaustive ;
  - H_ref (CAMB 1.5.4) demeure partagé par toutes les voies ;
  - l'auto-test du chemin d'échec repose sur un échec synthétique :
    il prouve le mécanisme de blocage, pas l'exhaustivité des causes ;
  - aucune qualification de performance (temps d'évaluation par point)
    n'est fournie : hors périmètre G2.3a.
```

## 6. État et suite

```text
G2.3a : contrôles C1–C8 exécutés, tous PASSÉS ; porte auto-bloquante
  en place (G2.3d) : toute régression produit un code de sortie non
  nul ; passes nominales : exit 0, deux sorties bit à bit identiques ;
PR : brouillon, aucun merge ;
première inférence réelle (MCMC/minimisation) : FERMÉE — exige une
nouvelle validation humaine explicite ;
G2.2a : gel inchangé ; aucune clause amendée (aucune valeur
  scientifique, prior ou point P0–P3 modifié par G2.3d).
```
