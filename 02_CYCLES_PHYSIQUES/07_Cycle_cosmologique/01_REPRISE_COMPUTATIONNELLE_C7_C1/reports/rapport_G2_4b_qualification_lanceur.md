# Rapport G2.4b — qualification du lanceur MCMC X(z), sans MCMC réelle

Issue directrice : #63 (G2.4a ratifiée D4-A..H ; G2.4b-i inventaire ;
G2.4b-ii gel de la capacité). Branche :
`comp/c7-c1-xz-mcmc-launch-qualification`, base
`ae1e84ac0aae74c8a8e6c79a9741c587d7056160`.

```text
MCMC réelle : AUCUNE — le lanceur est resté verrouillé pendant toute la
  qualification ; le chemin de production se termine par un refus
  explicite avant cobaya.run tant que G2.4b n'est pas validée ;
minimisation / posterior / lecture cosmologique : ABSENTS ;
vrai manifeste d'autorisation : JAMAIS créé (fictifs refusés) ;
les chi2 du banc ne sont ni publiés ni utilisés (embargo D4-F).
```

## 1. Architecture (D4-A)

```text
scripts/xz_cobaya_g2_4.py      — information Cobaya construite EN MÉMOIRE
  depuis un descripteur G2.3 immuable, après validate_config strict ;
  vraisemblance externe = XZEvaluator (corrected), logp = -chi2_total/2 ;
  chi2_BAO, chi2_CMB, chi2_total exposés comme dérivés auditables ;
  omch2 exposé en dérivé (formule G1) ; contrainte omch2>0 en prior
  explicite ; cache CAMB borné (8 entrées) pour l'échantillonnage futur ;
scripts/run_mcmc_xz_g2_4.py    — lanceur verrouillé : gardes de pré-vol,
  matrice gelée, capacité, autorisation à deux clés, qualification
  adversariale orchestrée (mode unique --qualification) ;
scripts/diagnose_mcmc_xz_g2_4.py — diagnostics techniques qualifiés sur
  cas synthétiques exclusivement.
Aucun YAML créé ; les quatre descripteurs G2.3 sont restés intacts.
```

## 2. Contrats vérifiés

### 2.1 Encodage exact (adaptateur)

`H0 ~ U[20,100]`, `ombh2 ~ U[0.005,0.1]`, `omm ~ U[0.01,0.99]`,
`X_i ~ U[-2,4]`, `omch2 = omm*(H0/100)^2 - mnu/93.14 - ombh2` (dérivé),
`omch2 > 0` (prior explicite + ré-application par l'évaluateur),
traitement acoustique `corrected` (imposé par le descripteur validé).
Refs/proposals : paramètres d'efficacité (règle G2.4a §10 : refs de fond
G1 ; `X_i` : normale centrée en 1, contenue dans `P_WS` ; proposition
identique pour tous les nœuds d'une grille) — pas des priors.

### 2.2 Bloc sampler G1 et clé exacte Cobaya 3.5

```text
drag: false ; oversample_power: 0.4 ; proposal_scale: 1.9 ;
covmat: null ; temperature: 1 ; Rminus1_stop: 0.01 ;
Rminus1_cl_stop: 0.02 ; max_tries: 1000 ; (+ graine par chaîne)

vérification double, sans correction silencieuse :
  clé correcte « oversample_power »   : ACCEPTÉE (run test=True) ;
  clé fautive  « over_sample_power »  : REJETÉE par Cobaya avec erreur
    explicite (« does not recognize some options ») — conforme.
```

Deux contraintes d'API Cobaya 3.5 ont été établies pendant la
qualification et sont encodées : un paramètre dérivé sans consommateur
doit être déclaré via `derived:` (et non `value:`) ; une fonction externe
avec `output_params` doit retourner le tuple `(logp, {dérivés})`.

## 3. Matrice des graines (D4-B, gelée)

```text
M2a-N : 630101–630108 ;  M2a-K : 630201–630208 ;
M2b-N : 630301–630308 ;  M2b-K : 630401–630408 ;
règle : 100 x graine_G2.3 + index de chaîne ; 4 x 8 = 32 chaînes.
```

## 4. Garde de capacité gelée (G2.4b-ii)

```text
seuil de production : espace libre du volume de C7C1_XZ_OUT_DIR
  >= 40 Gio, mesuré en octets réels (shutil.disk_usage) ;
< 40 Gio : arrêt non nul, aucun répertoire créé, aucune reprise,
  aucun fichier existant modifié ;
< 15 Gio : alerte technique, tout lancement/reprise interdit ;
aucune suppression ni libération automatique ;
tests par INJECTION (C7C1_TEST_ESPACE_LIBRE_GIO), jamais en remplissant
  le disque ; toute injection C7C1_TEST_* présente en mode production
  est elle-même une faute et entraîne le refus.
```

## 5. Tests nominaux (tous conformes, exit 0)

```text
préflight M2a-N/630101, espace simulé 41 Gio : PASSE ;
préflight, espace simulé exactement 40 Gio   : PASSE (>= 40) ;
clé sampler correcte                          : ACCEPTÉE ;
clé sampler fautive                           : REJET détecté (exit 0 du
                                                vérificateur = conformité) ;
diagnostic synthétique convergé               : certifié (exit 0) ;
self-test diagnostique complet                : PASSE (exit 0).
```

## 6. Tests adversariaux (tous refusés, code non nul)

```text
variante inconnue (M2c-N)                       : refus ;
graine hors matrice (999999)                    : refus ;
graine d'une autre variante (630201 sous M2a-N) : refus ;
YAML altéré (copie hors Git, prior élargi)      : refus (validate_config) ;
SHA de descripteur incorrect                    : refus ;
SHA de données incorrect (octets BAO altérés,
  copie hors Git)                               : refus ;
environnement incorrect (version numpy forgée)  : refus ;
sortie sous un ancêtre Git                      : refus (SortieSousGitError) ;
collision de préfixe (répertoire occupé)        : refus, fichier occupant
                                                  intact après la passe ;
reprise avec manifeste incompatible             : refus ;
autorisation absente                            : refus ;
autorisation factice (SHA lanceur faux)         : refus ;
production sans confirmation explicite          : refus ;
espace simulé 39 Gio                            : refus ;
espace simulé 14 Gio                            : alerte + refus ;
diagnostic synthétique non convergé             : certification refusée ;
poids non entier / négatif / non fini           : refus (3 scénarios) ;
segments de reprise désordonnés                 : refus.
```

Incident environnemental documenté : pendant la qualification, un
répertoire `C:\.git` VIDE (artefact d'un chantier de nettoyage disque
mené en parallèle par l'utilisateur, hors périmètre) a déclenché la
garde « hors Git » sur tout le volume — preuve en conditions réelles que
la garde bloque, avec code non nul, sans créer ni modifier aucun
fichier. Le résidu (vide, invalide pour Git) a été supprimé avec
l'accord explicite de l'utilisateur, en dehors des produits du lot.

## 7. Diagnostics : implémentation et bibliothèque de référence figée

Implémentés : reconstruction chronologique par poids (finis, positifs,
entiers à 1e-9), concaténation ordonnée des segments de reprise, burn-in
30 %, aucun amincissement, R-hat scindé normalisé par rang (max bulk /
replié), ESS bulk (rangs normalisés, ex aequo moyennés), ESS tail
(indicatrices des quantiles 5 %/95 %, sans normalisation par rang),
exigence des 8 chaînes contributrices. Seuils gelés : R-hat <= 1.01 ;
ESS bulk/tail >= 1000.

```text
bibliothèque de référence FIGÉE : GetDist 1.7.7 (présente dans
  l'environnement directeur gelé) — concordance vérifiée :
  R-1 GetDist = 0.0001 (cas convergé) / 23.64 (cas non convergé) ;
ancrages analytiques fermés :
  iid : ESS mesurée 22 400 = N total (attendu ~N) ;
  AR(1) rho=0.9 : ESS mesurée 2 225 vs ancrage N/19 = 2 358
    (rapport 0.944) ;
arviz : ABSENT localement ; son installation modifierait
  l'environnement directeur gelé — écarté pour cette porte et consigné
  comme limite.
AUCUNE chaîne physique G2 lue ; aucune moyenne de paramètre produite.
```

## 8. Banc de performance (points prédéclarés P0–P3, 4 variantes)

Chi2 ni publiés ni utilisés. Mesures non déterministes consignées
séparément de la sortie normalisée (le contrôle de déterminisme porte
sur la sortie normalisée seule).

```text
validité (déterministe, graine 6300) :
  P0–P3 : 4/4 points valides pour chacune des 4 variantes ;
  taux omch2>0 sous les priors de fond P_WS      : 74.9 % ;
  taux de fond H_X² valide sous P_WS (fond P0)   : M2a 77.0 % ;
                                                   M2b 84.0 % ;
temps d'évaluation (indicatif, cette machine)    : ~0.28 à 0.88 s,
  médiane ~0.38 s par évaluation (une construction CAMB complète par
  point : get_background avec thermodynamique) ;
mémoire Python (tracemalloc, pic)                : <= ~1.3 Mo par série
  d'évaluations (n'inclut pas les allocations internes CAMB — psutil
  absent, limite consignée) ;

projection de charge pour 32 chaînes (longueurs G2.4b-i, acceptation
~0.2 héritée de G1) :
  basse    (153k lignes/chaîne) :  2 570 heures CPU ;
  centrale (330k)               :  5 544 heures CPU ;
  haute    (880k)               : 14 784 heures CPU ;
soit, à 8 chaînes en parallèle sur cette machine : ~13 j / ~29 j / ~77 j
de temps mur.
```

CONSTAT DE FAISABILITÉ (G2.4a §9) : cette charge rend le plan
difficilement réalisable en l'état sur la machine locale. La cause
dominante est identifiée et purement computationnelle : l'évaluateur
reconstruit une référence CAMB complète (avec thermodynamique) à chaque
point. Conformément à la spécification, la suite relève d'une décision
humaine : suspension pour optimisation computationnelle (sans
changement scientifique), exécution partielle par rondes, ou moyens de
calcul supplémentaires. Aucun résultat partiel n'existe ni ne peut être
interprété.

## 9. Déterminisme

```text
qualification complète exécutée DEUX FOIS :
  exit 0 et exit 0 ;
  sorties normalisées bit à bit identiques (diff vide) ;
mesures de temps/mémoire : consignées dans une section séparée,
  exclue par construction du contrôle de déterminisme.
```

## 10. Limites

```text
- la charge projetée (§8) conditionne la faisabilité : décision humaine
  requise avant tout lancement ;
- la mémoire mesurée exclut les allocations internes CAMB (psutil absent) ;
- arviz absent : la référence rang-normalisée est validée contre GetDist
  (R-1 classique) et des ancrages analytiques, pas contre une
  implémentation rang-normalisée indépendante ;
- les scénarios adversariaux couvrent les 19 fautes prescrites ; la
  liste n'est pas exhaustive ;
- l'autorisation à deux clés est qualifiée en refus (absente, factice) ;
  son acceptation nominale ne sera exercée qu'avec le vrai manifeste,
  interdit avant validation humaine de G2.4b.
```

## 11. Statut de la première MCMC

```text
PREMIÈRE MCMC RÉELLE : FERMÉE.
Le lanceur reste verrouillé : sans manifeste d'autorisation à deux clés
valide ET confirmation explicite en ligne de commande, tout chemin de
production se termine par un refus à code non nul. Le vrai manifeste ne
peut être créé qu'après validation humaine du présent rapport, et la
décision de faisabilité (§8) doit être tranchée avant tout lancement.
```
