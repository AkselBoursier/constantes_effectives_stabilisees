# Rapport G1.0 — environnement, octets, configurations, tests de chargement

Issue directrice : #63. Autorisation : commentaire G0.6. Aucun échantillonnage
MCMC n'a été lancé. Aucun chemin absolu local n'est consigné ici.

## 1. Base Git et worktree

```text
branche        : comp/c7-c1-comparaison-commune ;
base vérifiée  : origin/main = 5e088d13e6cd292656debedccec4b244eba33015
                 (« philo-resynchro-provisoire » — contient désormais,
                 commises, les 17 modifications autrefois flottantes) ;
mode           : worktree propre, hors du checkout OneDrive ;
état initial   : worktree propre (aucune modification, aucun objet suivi
                 sous data_external) ;
état final     : seule la racine 01_REPRISE_COMPUTATIONNELLE_C7_C1/ ajoutée.
```

Correction d'implantation : l'emplacement `%LOCALAPPDATA%` proposé en G0.4
s'est révélé **virtualisé** (redirection MSIX de l'application hébergeant
l'agent) — un environnement y serait invisible hors de l'agent. Worktree,
environnement et données sont donc implantés dans un répertoire utilisateur
non virtualisé, hors OneDrive et hors Git (contrainte respectée : « pas dans
le checkout OneDrive » ; chemins consignés localement seulement).

## 2. Environnement isolé

```text
python  : 3.12 (venv dédié) ;
cibles  : cobaya 3.5 ; camb 1.5.4  — installées à l'identique ;
annexes : getdist 1.7.7 ;
gel     : requirements-c7c1.txt (pip freeze complet, pip check propre).
```

Ajustement contrôlé : camb 1.5.4 est incompatible avec numpy >= 2
(`TypeError` dans `set_cosmology`) ; épinglage cohérent d'époque :
`numpy 1.26.4`, `scipy 1.13.1`, `pandas 2.2.3`.

Constat de version : cobaya 3.5 **ne contient pas** `bao.desi_dr2`
(vraisemblance ajoutée après DR2). C'est cohérent avec la pratique
historique DESI (cobaya 3.5 + bindings externes). La voie « stock »
exigerait un cobaya plus récent — admissible seulement comme contrôle
secondaire clairement séparé (G0.6 §3), à ratifier.

## 3. Octets BAO officiels — acquis et vérifiés

```text
source épinglée : CobayaSampler/bao_data @ bb0c1c9009dc76d1391300e169e8df38fd1096db
desi_gaussian_bao_ALL_GCcomb_mean.txt : 472 octets
  sha256 9ac154ab583ce759c0f7eef3c978c7c70a6ead2d18774caceadf1a350a640585
desi_gaussian_bao_ALL_GCcomb_cov.txt  : 2547 octets
  sha256 252a143274c8a07c78694c119617d36594f6d7965d00319ca611c6ffb886e509
git blob SHA-1 recalculés localement = annoncés par l'API GitHub (identité
au commit épinglé). 13 composantes (1 DV, 6 DM, 6 DH ; z 0,295 à 2,33),
covariance 13x13, rs_fid = 1 Mpc. Stockage hors Git (C7C1_DATA_DIR).
```

Ré-acquisition : `scripts/acquire_bao_data.py` (arrêt sur toute discordance
de taille, de blob SHA-1 ou de SHA-256).

## 4. Configurations transcrites

Diff structuré contre les YAML officiels (copies de référence dans
`configs/references/`, SHA-256 identiques à ceux consignés en G0.3) :

```text
blocs theory / params / sampler : strictement identiques ;
adaptations (toutes tracées) :
  1. vraisemblances bindings NERSC -> transcription contrôlée
     scripts/c7c1_likelihoods.py ;
  2. output supprimé (G1.0 : aucun produit d'échantillonnage) ;
  3. CPL : bloc prior explicite matter_domination_w0wa (w0 + wa < 0),
     ratifié G0.6.
```

## 5. Tests de chargement et de points de vraisemblance (aucun MCMC)

Chargement : réussi pour les deux modèles ; paramètres échantillonnés
conformes aux chaînes officielles — `(H0, ombh2, omm)` et `(+ w, wa)`.

Six points tirés des chaînes officielles (3 ΛCDM + 3 CPL, lecture seule) :

```text
chi2__BAO            : reproduit à |delta| <= 5e-6 sur les 6 points ;
rdrag                : identique à 1e-4 près ;
omegam               : identique à 1e-6 près ;
chi2__CMB_compressed : écarts de -0,28 à +1,00 selon le point.
```

Le résultat BAO établit **empiriquement** l'équivalence entre les octets
officiels acquis + transcription et les bindings historiques DESI
(en sus de la déclaration officielle du support DESI), et la cohérence
de camb 1.5.4.

Diagnostic des écarts CMB : un unique décalage `delta` du vecteur `mu`
(trois composantes, au plus 0,11 sigma chacune — ordre de l'arrondi des
valeurs publiées à 4-5 chiffres) ramène les six écarts à un résidu
RMS ~ 1,6e-3. La reproduction est donc limitée par la **précision des
coefficients publiés**, non par la transcription. Le vecteur effectif
ajusté est un diagnostic ; il n'est **pas** proposé comme convention
(interdit « ne pas fabriquer de compression »).

Contrainte jointe CPL : un point violant (w = 0,5 ; wa = 0,5) est rejeté
avec `logpost = -inf`. La condition est encodée explicitement et testée.

## 6. Points soumis à ratification avant G1

1. **Convention de compression CMB** :
   (a) coefficients publiés arrondis = définition du lot (alors les χ²
   CMB point à point diffèrent des chaînes historiques de O(<=1) et les
   tolérances G1 doivent l'admettre), ou
   (b) obtention des coefficients pleine précision (source bindings DESI
   ou auteurs) avant reproduction fine.
2. **Voie BAO pour l'échantillonnage G1** : transcription contrôlée sous
   cobaya 3.5 (reproduction historique), et/ou vraisemblance stock
   `bao.desi_dr2.desi_bao_all` sous cobaya récent en contrôle secondaire
   séparé.

## 7. Zenodo

Compte Zenodo authentifié et relié à ORCID/GitHub — disponibilité déclarée
par l'utilisateur, non testée par l'agent. Aucune opération d'archivage ;
décision distincte : #64.

## 8. État

```text
G1.0 : périmètre exécuté (worktree, branche, environnement, octets,
       configurations, tests de chargement et de point) ;
MCMC : toujours interdit ;
suite : validation humaine du présent rapport, ratification des points
        du §6, puis ouverture éventuelle de G1.
```
