# Reprise computationnelle N1–N3

Ce sous-dossier approfondit la tension entre les planchers de somme issus des
oscillations (`N1`) et la contrainte cosmologique sur `Sigma m_nu` (`N3`).

## Statut

```text
chantier : ouvert le 17 juillet 2026 ;
phase C1 : reconstruction des planchers et diagnostic de frontière/prior ;
phase C2 : ingestion et réanalyse des chaînes officielles DESI DR2 ;
portée : calcul scientifique contrôlé ;
ne vaut pas : reproduction complète DESI, nouvel ajustement cosmologique ou
              conclusion de nouvelle physique.
```

La phase C1 utilise deux composants distincts :

1. une propagation Monte Carlo des incertitudes oscillatoires ;
2. une vraisemblance gaussienne substitutive calibrée sur la borne bayésienne
   publiée par DESI (`0.0642 eV`) et l'écart-type marginalisé (`0.020 eV`).

Le second composant est un diagnostic de la frontière et des priors. Il n'est
pas une substitution silencieuse aux chaînes MCMC officielles.

## Fichiers

- `analyse_tension_n1_n3.py` : calcul reproductible et lecteur optionnel de
  chaînes Cobaya locales ;
- `resultats_synthese.json` : entrées, planchers et diagnostics numériques ;
- `sensibilite_priors.csv` : quantiles obtenus sous plusieurs paramétrisations ;
- `diagnostic_tension_n1_n3.svg` : représentation produite à l'exécution ;
- `C1_Resultats_planchers_frontiere_priors_v0_1.md` : interprétation scientifique
  bornée de la première passe ;
- `requirements.txt` : dépendances minimales.

## Exécution

```bash
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python analyse_tension_n1_n3.py --output-dir sorties
```

Pour une chaîne Cobaya dont l'en-tête contient `weight`, `minuslogpost` et le
paramètre de masse :

```bash
python analyse_tension_n1_n3.py \
  --output-dir sorties_chain \
  --chains-glob '/chemin/chain.*.txt' \
  --chain-parameter mnu
```

La phase C2 devra appliquer ce mode séparément aux jeux officiels `base_mnu`,
`base_mnu059` et `base_mnu_w_wa`, après contrôle des fichiers YAML et des noms
de colonnes.
