"""Contrôle BAO secondaire — porte G1.2 (issue #63, §3, voie secondaire).

Évalue la vraisemblance stock `bao.desi_dr2.desi_bao_all` (introduite dans
Cobaya >= 3.5.6) sur les MÊMES points fixes que les tests G1.0, dans un
environnement séparé et épinglé (Cobaya 3.5.7 attendu). Les fichiers de
données sont les octets vérifiés du manifeste (bao_data @ bb0c1c9), placés
sous <packages_path>/data/bao_data/desi_bao_dr2/.

Rôle : contrôle d'indépendance d'implémentation uniquement. Ce script ne
remplace pas la voie primaire et ne lance aucun MCMC.

Usage :
    python scripts/control_bao_stock_g1_2.py <packages_path> <racine_chaines>

<racine_chaines> : répertoire cobaya/ des chaînes officielles (lecture
seule), contenant base/... et base_w_wa/... ; passé à l'exécution, jamais
stocké dans le dépôt.
"""

import sys

import cobaya
import numpy as np
from cobaya.model import get_model
from cobaya.yaml import yaml_load_file

CASES = [
    (
        "configs/c7c1_lcdm_bao_cmbcomp.yaml",
        "base/desi-bao-all_CMB-compressed-theta-ombh2-ombch2",
        "LCDM",
    ),
    (
        "configs/c7c1_cpl_bao_cmbcomp.yaml",
        "base_w_wa/desi-bao-all_CMB-compressed-theta-ombh2-ombch2",
        "CPL",
    ),
]

STOCK = "bao.desi_dr2.desi_bao_all"


def chain_points(chain_dir, n_points=3):
    path = f"{chain_dir}/chain.1.txt"
    with open(path, encoding="utf-8") as f:
        header = next(line for line in f if line.lstrip().startswith("#"))
    names = header.lstrip().lstrip("#").split()
    data = np.loadtxt(path)
    idx = np.linspace(0, len(data) - 1, n_points, dtype=int)
    return names, data[idx], idx


def main():
    packages_path, chains_root = sys.argv[1], sys.argv[2]
    print(f"cobaya {cobaya.__version__} (contrôle secondaire épinglé)")

    for config, sub, label in CASES:
        info = yaml_load_file(config)
        info.pop("sampler", None)
        info.pop("output", None)
        info.pop("prior", None)
        info["likelihood"] = {STOCK: None}
        info["packages_path"] = packages_path
        model = get_model(info)
        sampled = list(model.parameterization.sampled_params())

        names, rows, idx = chain_points(f"{chains_root}/{sub}")
        col = {n: names.index(n) for n in names}
        print(f"\n=== {label} — points fixes identiques à G1.0 ===")
        print("point   chi2_BAO(chaine)  chi2_BAO(stock)   delta")
        for k, row in enumerate(rows):
            point = {p: row[col[p]] for p in sampled}
            lp = model.logposterior(point)
            chi2_stock = -2.0 * lp.loglikes[0]
            chi2_off = row[col["chi2__BAO"]]
            print(
                f"{idx[k]:>6d}  {chi2_off:16.6f}  {chi2_stock:15.6f}  "
                f"{chi2_stock - chi2_off:+.2e}"
            )


if __name__ == "__main__":
    main()
