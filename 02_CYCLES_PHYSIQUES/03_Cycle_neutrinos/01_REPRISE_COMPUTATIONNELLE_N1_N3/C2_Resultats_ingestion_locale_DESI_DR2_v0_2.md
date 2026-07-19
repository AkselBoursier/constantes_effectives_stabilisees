# C2 — Résultats de l’ingestion locale DESI DR2 v0.2

## Statut

- exécution UTC : `2026-07-19T08:28:18.566635+00:00` ;
- commit de départ : `08195e97af3530ae24c19e0edb464eace51cf714` ;
- racine relative : `data_external/desi_dr2/cosmology_chains_verified/cosmology_chains` ;
- données brutes : hors Git ;
- portée : reproduction depuis les chaînes distribuées, sans nouvel ajustement cosmologique.

## Quantiles et convergence

| Modèle | Statut | q95 empirique (eV) | limite officielle `margestats` (eV) | écart (eV) | R−1 final |
|---|---|---:|---:|---:|---:|
| `base_mnu` | chains_ingested | 0.0649342 | 0.0642 | 0.000734183 | 0.00914719 |
| `base_mnu059` | chains_ingested | 0.104862 | 0.105 | -0.000137913 | 0.00836159 |
| `base_mnu_binary_3` | not_available_in_verified_distribution | non disponible | non disponible | non disponible | non disponible |
| `base_mnu_w_wa` | chains_ingested | 0.163905 | 0.163 | 0.000904566 | 0.00669579 |

Les quantiles empiriques utilisent directement les poids des échantillons. Les limites de `chain.margestats` restent séparées, car GetDist peut appliquer une convention de densité, de lissage ou d’interpolation différente.

## Produits `iminuit`

| Modèle | Produit exact même modèle/même jeu | Profil |
|---|---|---|
| `base_mnu` | directory_without_bestfit_files | not_reconstructed_point_products_only |
| `base_mnu059` | directory_without_bestfit_files | not_reconstructed_point_products_only |
| `base_mnu_binary_3` | non applicable | non reconstruit |
| `base_mnu_w_wa` | exact_product_not_available | non reconstruit |

Un fichier ponctuel `bestfit.*` n’est pas qualifié de profil. Aucun modèle voisin n’est substitué au modèle demandé.

## Limites

- `base_mnu_binary_3` n’est qualifié qu’au niveau de la distribution inspectée ;
- l’absence dans cette archive ne vaut pas absence de toute distribution officielle ;
- aucune conclusion de nouvelle physique n’est tirée avant séparation du support, des priors, du modèle d’expansion et des likelihoods.
