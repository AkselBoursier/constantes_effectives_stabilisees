"""Tests de chargement et de points de vraisemblance — porte G1.0 (issue #63).

Charge une configuration C7-C1 (sans sampler ni output), évalue le
log-posterior sur quelques points tirés des chaînes officielles DESI DR2,
et confronte les chi2 recalculés aux colonnes chi2__BAO et
chi2__CMB_compressed enregistrées dans ces chaînes.

Pour la configuration CPL, vérifie aussi explicitement que le prior joint
w0 + wa < 0 rejette un point violant (logprior = -inf).

AUCUN échantillonnage n'est lancé ; aucun fichier n'est produit.

Usage :
    python scripts/test_points_g1_0.py <config.yaml> <repertoire_chaine> [n_points]

<repertoire_chaine> : répertoire officiel contenant chain.1.txt (lecture
seule) ; passé en argument à l'exécution, jamais stocké dans le dépôt.
"""

import sys

import numpy as np
from cobaya.model import get_model
from cobaya.yaml import yaml_load_file


def load_chain(chain_dir, n_points):
    path = f"{chain_dir}/chain.1.txt"
    with open(path, encoding="utf-8") as f:
        header = next(line for line in f if line.lstrip().startswith("#"))
    names = header.lstrip().lstrip("#").split()
    data = np.loadtxt(path)
    if data.shape[1] != len(names):
        raise SystemExit(f"ARRET: colonnes ambiguës dans {path}")
    idx = np.linspace(0, len(data) - 1, n_points, dtype=int)
    return names, data[idx], idx


def main():
    config, chain_dir = sys.argv[1], sys.argv[2]
    n_points = int(sys.argv[3]) if len(sys.argv) > 3 else 3

    info = yaml_load_file(config)
    info.pop("sampler", None)
    info.pop("output", None)
    model = get_model(info)

    sampled = list(model.parameterization.sampled_params())
    derived = list(model.parameterization.derived_params())
    like_names = list(model.likelihood)
    print(f"config             : {config}")
    print(f"parametres echantillonnes : {sampled}")
    print(f"vraisemblances     : {like_names}")

    names, rows, idx = load_chain(chain_dir, n_points)
    col = {n: names.index(n) for n in names}

    print("\npoint  " + "  ".join(f"{p}" for p in sampled)
          + "  chi2_BAO(off)  chi2_BAO(ici)  d_BAO"
          + "  chi2_CMB(off)  chi2_CMB(ici)  d_CMB"
          + "  rdrag(off)  rdrag(ici)  omegam(off)  omegam(ici)")
    for k, row in enumerate(rows):
        point = {p: row[col[p]] for p in sampled}
        lp = model.logposterior(point)
        loglikes = dict(zip(like_names, lp.loglikes))
        der = dict(zip(derived, lp.derived))
        chi2_bao = -2.0 * loglikes["c7c1_likelihoods.DesiBaoAll"]
        chi2_cmb = -2.0 * loglikes["c7c1_likelihoods.CmbCompressedPR4"]
        chi2_bao_off = row[col["chi2__BAO"]]
        chi2_cmb_off = row[col["chi2__CMB_compressed"]]
        print(
            f"{idx[k]:>6d}  "
            + "  ".join(f"{point[p]:.6f}" for p in sampled)
            + f"  {chi2_bao_off:.6f}  {chi2_bao:.6f}  {chi2_bao - chi2_bao_off:+.2e}"
            + f"  {chi2_cmb_off:.6f}  {chi2_cmb:.6f}  {chi2_cmb - chi2_cmb_off:+.2e}"
            + f"  {row[col['rdrag']]:.4f}  {der['rdrag']:.4f}"
            + f"  {row[col['omegam']]:.6f}  {der['omegam']:.6f}"
        )

    if "w" in sampled and "wa" in sampled:
        good = {p: rows[0][col[p]] for p in sampled}
        bad = dict(good, w=0.5, wa=0.5)
        lp_bad = model.logposterior(bad)
        print("\ncontrole prior joint w0+wa<0 :")
        print(f"  point violant (w=0.5, wa=0.5) -> logpost = {lp_bad.logpost}")
        if not np.isneginf(lp_bad.logpost):
            raise SystemExit("ARRET: la contrainte w0+wa<0 n'a pas rejete le point violant")
        print("  contrainte jointe effective : point violant rejete (-inf).")


if __name__ == "__main__":
    main()
