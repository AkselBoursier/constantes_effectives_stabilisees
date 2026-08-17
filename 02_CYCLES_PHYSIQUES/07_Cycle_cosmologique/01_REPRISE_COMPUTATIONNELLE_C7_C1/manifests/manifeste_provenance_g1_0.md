# Manifeste de provenance — C7-C1, porte G1.0

Issue directrice : #63. Ratification : commentaire G0.6.
Aucun chemin absolu local n'est consigné ici (règle #63) ; les
emplacements hors Git sont désignés par variables d'environnement.

## 1. Base Git

```text
branche : comp/c7-c1-comparaison-commune
base    : origin/main = 5e088d13e6cd292656debedccec4b244eba33015
          (« philo-resynchro-provisoire »)
mode    : worktree propre, hors du checkout OneDrive principal
```

## 2. Octets BAO officiels (hors Git, sous %C7C1_DATA_DIR%/desi_bao_dr2/)

Source : dépôt officiel `CobayaSampler/bao_data`, répertoire
`desi_bao_dr2/`, épinglé au commit
`bb0c1c9009dc76d1391300e169e8df38fd1096db` (2025-06-26, branche master).

| fichier | taille | git blob SHA-1 (annoncé API GitHub = recalculé local) | SHA-256 |
|---|---|---|---|
| `desi_gaussian_bao_ALL_GCcomb_mean.txt` | 472 octets | `8aff444fdb42c0946342aa0011ab287eda097c4c` | `9ac154ab583ce759c0f7eef3c978c7c70a6ead2d18774caceadf1a350a640585` |
| `desi_gaussian_bao_ALL_GCcomb_cov.txt` | 2 547 octets | `fd8e5697ab61379b07b52efb781ea6713417a4d9` | `252a143274c8a07c78694c119617d36594f6d7965d00319ca611c6ffb886e509` |

Contenu contrôlé : 13 composantes (1 `DV_over_rs`, 6 `DM_over_rs`,
6 `DH_over_rs`, z de 0,295 à 2,33), covariance 13×13, `rs_fid = 1 Mpc`.

Équivalence avec les bindings historiques DESI
(`desi_y3_cosmo_bindings...bao_likelihoods_v1p2.desi_bao_all`) :
déclarée byte-identique par le support officiel DESI
(help.desi.lbl.gov, question 182 « provenance external cobaya likelihood
public cosmology chains ») ; contrôle empirique supplémentaire par tests
de point de vraisemblance (voir `reports/rapport_G1_0.md`).

Ré-acquisition reproductible : `scripts/acquire_bao_data.py`
(vérifie taille, git blob SHA-1 et SHA-256 avant écriture).

## 3. YAML officiels de référence (copies contrôlées, `configs/references/`)

| copie | SHA-256 | source |
|---|---|---|
| `officiel_base_cmbcomp_chain.input.yaml` | `c497ecc0e43d169aff18ce1a815577554a91d9a987f0322becbddc699b63a309` | Zenodo DESI DR2, `cosmology_chains/cobaya/base/desi-bao-all_CMB-compressed-theta-ombh2-ombch2/chain.input.yaml` (ingestion C2 vérifiée) |
| `officiel_base_w_wa_cmbcomp_chain.input.yaml` | `3ebbe59e2443652e78e3cc6f19b4a7b56f7da0d69f4f22ef62d099fbcc619fb4` | idem, `base_w_wa/...` |
| `officiel_cobaya_v3.6.2_desi_bao_all.yaml` | `fd7e9bf2dcf5ffee90a9a30b18227f4337d6d5c1978782c63513cbe0d8280daa` | `CobayaSampler/cobaya` @ tag `v3.6.2`, `cobaya/likelihoods/bao/desi_dr2/desi_bao_all.yaml` |

Les SHA-256 des deux `chain.input.yaml` sont identiques à ceux consignés
au rapport G0.3 dans #63 : copies byte-identiques aux produits ingérés.

## 4. Compression CMB (transcrite dans `scripts/c7c1_likelihoods.py`)

```text
q  = (theta_star, omega_b h^2, omega_bc h^2)   # ordre publié, G0.1
mu = (0.01041, 0.02223, 0.14208)
C  = 1e-9 * [[ 0.006621,   0.12444,   -1.1929 ],
             [ 0.12444,   21.344,    -94.001  ],
             [-1.1929,   -94.001,   1488.4    ]]
```

Convention contrôlée : première coordonnée `theta_star = 0.01041`
(pas `100 theta_star`) ; CAMB sérialisant `thetastar` comme
`100 theta_star`, la conversion `/100` est explicite dans le code et
contrôlée par les tests de point.

## 5. Environnement isolé (hors Git, hors OneDrive)

```text
python : 3.12 (venv dédié, %C7C1_ENV%)
cible  : cobaya == 3.5, camb == 1.5.4  (versions sérialisées des chaînes)
gel    : requirements-c7c1.txt (pip freeze de l'environnement réel)
```

Note d'environnement : l'emplacement `%LOCALAPPDATA%` proposé en G0.4
s'est révélé virtualisé (redirection MSIX) dans l'environnement d'agent ;
l'environnement et le worktree ont donc été placés sous un répertoire
non virtualisé du profil utilisateur, hors OneDrive et hors Git.
Contrainte respectée : « pas dans le checkout OneDrive ».

## 6. Prior CPL ratifié (G0.6)

```text
w0 ~ U[-3, 1] ; wa ~ U[-3, 2] ; contrainte jointe w0 + wa < 0
```

Encodage : bloc `prior:` explicite dans `configs/c7c1_cpl_bao_cmbcomp.yaml`
(`matter_domination_w0wa`), testé par `scripts/test_points_g1_0.py`
(rejet -inf d'un point violant).

## 7. Hors Git (rappel)

Chaînes, données BAO brutes, caches Cobaya/CAMB, environnements,
sorties MCMC, secrets : jamais versionnés. `data_external/` reste en
lecture seule et ignoré par Git.
