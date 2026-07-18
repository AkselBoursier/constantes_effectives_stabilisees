# Reprise computationnelle N1–N3

Ce sous-dossier approfondit la tension entre les planchers de somme issus des
oscillations (`N1`) et la contrainte cosmologique sur `Sigma m_nu` (`N3`).

## Statut

```text
chantier : ouvert le 17 juillet 2026 ;
phase C1 : reconstruction des planchers et diagnostic substitutif de
           frontière/prior — achevée ;
phase C2 : produits officiels DESI, ingestion pondérée, maxima et profils —
           ouverte ;
état C2 : provenance et infrastructure stabilisées ; chaînes brutes non encore
          ingérées dans l'environnement courant ;
portée : calcul scientifique contrôlé ;
ne vaut pas : reproduction complète DESI, nouvel ajustement cosmologique ou
              conclusion de nouvelle physique.
```

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

Le code ne produit aucun quantile lorsque les chaînes officielles sont absentes.
Les fichiers C2 sont :

- `manifest_produits_officiels_c2.json` : chemins, tailles et provenance ;
- `analyse_produits_officiels_desi_c2.py` : contrôle, lecture et statistiques
  pondérées ;
- `resultats_c2.json` : état machine-lisible de l'ingestion ;
- `quantiles_c2.csv` : tableau volontairement vide tant que les chaînes manquent ;
- `ancrages_publication_c2.csv` : valeurs publiées utilisées comme tests, non
  présentées comme reproductions ;
- `C2_Produits_officiels_quantiles_maxima_profils_v0_1.md` : rapport borné.

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

## Exécution C2 sans chaînes

Cette commande contrôle le manifeste et produit un statut incomplet explicite :

```bash
python analyse_produits_officiels_desi_c2.py \
  --manifest manifest_produits_officiels_c2.json \
  --output-dir sorties_c2 \
  --allow-missing \
  --self-test
```

## Exécution C2 avec archive extraite

```bash
python analyse_produits_officiels_desi_c2.py \
  --manifest manifest_produits_officiels_c2.json \
  --data-root /chemin/vers/bao-cosmo-params \
  --output-dir sorties_c2_officielles \
  --hash-files \
  --self-test
```

Sans `--allow-missing`, le programme retourne un code d'erreur si une chaîne est
absente, si sa taille ne correspond pas à l'index officiel ou si les colonnes de
poids et de masse ne peuvent pas être identifiées.
