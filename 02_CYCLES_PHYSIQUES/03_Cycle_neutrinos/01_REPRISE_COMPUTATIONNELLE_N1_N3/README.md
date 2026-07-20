# Reprise computationnelle N1–N3

Ce sous-dossier approfondit la tension entre les planchers de somme issus des
oscillations (`N1`) et la contrainte cosmologique sur `Sigma m_nu` (`N3`).

## Statut

```text
chantier : ouvert le 17 juillet 2026 ;
phase C1 : reconstruction des planchers et diagnostic substitutif de
           frontière/prior — achevée ;
phase C2 : ingestion contrôlée des produits officiels DESI DR2 distribués — close ;
état C2 : chaînes base_mnu, base_mnu059 et base_mnu_w_wa ingérées ;
          base_mnu_binary_3 non disponible dans la distribution vérifiée ;
          profils exacts non reconstruits ;
portée : calcul scientifique contrôlé depuis les produits distribués ;
ne vaut pas : nouvel ajustement cosmologique, séparation complète de toutes les
              composantes de sensibilité ou conclusion de nouvelle physique.
```

La clôture de `C2` est une clôture propre avec limites positives. Elle n’affirme ni
que tous les produits officiels possibles ont été inspectés, ni que les effets du
support, des priors, du modèle d’expansion et des likelihoods sont déjà factorisés.
Le test borné `T2` porte sur cette discrimination résiduelle et peut être mené sans
bloquer la reprise du cycle 1.

## C1 — diagnostic substitutif

La phase C1 utilise deux composants distincts :

1. une propagation Monte Carlo des incertitudes oscillatoires ;
2. une vraisemblance gaussienne substitutive calibrée sur la borne bayésienne
   publiée par DESI (`0.0642 eV`) et l'écart-type marginalisé (`0.020 eV`).

Le second composant est un diagnostic de la frontière et des priors. Il n'est
pas une substitution silencieuse aux chaînes MCMC officielles.

Fichiers C1 :

- `analyse_tension_n1_n3.py` ;
- `resultats_synthese.json` ;
- `sensibilite_priors.csv` ;
- `diagnostic_tension_n1_n3.svg` produit à l'exécution ;
- `C1_Resultats_planchers_frontiere_priors_v0_1.md`.

## C2 — produits officiels

La phase C2 sépare quatre constructions :

```text
base_mnu          : frontière à zéro ;
base_mnu059       : plancher scalaire 0.059 eV ;
base_mnu_binary_3 : deux ordres avec information NuFIT 6.0 ;
base_mnu_w_wa     : masse libre et énergie noire dynamique.
```

La distribution vérifiée contient les chaînes de `base_mnu`, `base_mnu059` et
`base_mnu_w_wa`. Elle ne contient pas `base_mnu_binary_3`. Cette absence vaut pour
l’archive inspectée et ne doit pas être généralisée à toute distribution officielle.

Résultats principaux :

| Modèle | q95 empirique | Limite `margestats` | Statut |
|---|---:|---:|---|
| `base_mnu` | `0.0649342 eV` | `0.0642 eV` | chaînes ingérées |
| `base_mnu059` | `0.104862 eV` | `0.105 eV` | chaînes ingérées |
| `base_mnu_binary_3` | non disponible | non disponible | absent de la distribution vérifiée |
| `base_mnu_w_wa` | `0.163905 eV` | `0.163 eV` | chaînes ingérées |

Les quantiles empiriques utilisent directement les poids des échantillons. Les
limites `margestats` restent séparées, car les conventions de densité, de lissage
ou d’interpolation peuvent différer.

Fichiers directeurs C2 :

- `manifest_produits_officiels_c2.json` : chemins, tailles et provenance ;
- `analyse_produits_officiels_desi_c2.py` : contrôle, lecture et statistiques pondérées ;
- `resultats_c2.json` : état machine-lisible de l’ingestion et des absences ;
- `quantiles_c2.csv` : comparaison des quantiles empiriques et des limites distribuées ;
- `ancrages_publication_c2.csv` : valeurs publiées utilisées comme tests ;
- `C2_Produits_officiels_quantiles_maxima_profils_v0_1.md` : cadrage antérieur à l’ingestion ;
- `C2_Resultats_ingestion_locale_DESI_DR2_v0_2.md` : rapport de clôture de l’ingestion locale.

## Produits ponctuels et profils

Les répertoires `iminuit` disponibles ne fournissent pas, pour les trois modèles
ingérés, les profils exacts demandés. Un fichier ponctuel `bestfit.*` n’est pas
qualifié de profil et aucun modèle voisin n’est substitué au modèle demandé.

## Dépendances

```bash
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

## Exécution C1

```bash
python analyse_tension_n1_n3.py --output-dir sorties
```

## Exécution C2 avec distribution vérifiée

```bash
python analyse_produits_officiels_desi_c2.py \
  --manifest manifest_produits_officiels_c2.json \
  --data-root /chemin/vers/cosmology_chains \
  --output-dir sorties_c2_officielles \
  --hash-files \
  --self-test
```

Sans `--allow-missing`, le programme retourne un code d'erreur si une chaîne
attendue est absente, si sa taille ne correspond pas au manifeste ou si les
colonnes de poids et de masse ne peuvent pas être identifiées. L’option
`--allow-missing` reste réservée aux diagnostics qui doivent documenter une
absence sans fabriquer de résultat numérique.
