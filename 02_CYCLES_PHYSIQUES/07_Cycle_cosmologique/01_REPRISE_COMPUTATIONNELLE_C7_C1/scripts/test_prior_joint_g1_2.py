"""Validation du prior joint w0 + wa < 0 — porte G1.2 (issue #63, §4).

Teste explicitement, sur la configuration CPL transcrite :

1. un point ACCEPTÉ (tiré des chaînes officielles, w0 + wa < 0) :
   le prior externe `matter_domination_w0wa` doit contribuer 0.0 et le
   log-posterior doit être fini ;
2. un point REJETÉ (w0 = 0.5, wa = 0.5, soit w0 + wa = 1.0 >= 0) :
   le log-posterior doit valoir -inf.

Aucun échantillonnage, aucune écriture de fichier.

Usage :
    python scripts/test_prior_joint_g1_2.py <repertoire_chaine_cpl>
"""

import sys

import numpy as np
from cobaya.model import get_model
from cobaya.yaml import yaml_load_file

CONFIG = "configs/c7c1_cpl_bao_cmbcomp.yaml"


def main():
    chain_dir = sys.argv[1]
    info = yaml_load_file(CONFIG)
    info.pop("sampler", None)
    info.pop("output", None)
    model = get_model(info)
    sampled = list(model.parameterization.sampled_params())
    prior_names = list(model.prior)

    path = f"{chain_dir}/chain.1.txt"
    with open(path, encoding="utf-8") as f:
        header = next(line for line in f if line.lstrip().startswith("#"))
    names = header.lstrip().lstrip("#").split()
    row = np.loadtxt(path, max_rows=1)
    col = {n: names.index(n) for n in names}

    accepted = {p: row[col[p]] for p in sampled}
    lp = model.logposterior(accepted)
    print(f"blocs de prior : {prior_names}")
    print(f"point accepté : w={accepted['w']:.6f} wa={accepted['wa']:.6f} "
          f"(w+wa={accepted['w']+accepted['wa']:.6f})")
    print(f"  logpriors par bloc = {dict(zip(prior_names, lp.logpriors))}")
    print(f"  logpost = {lp.logpost:.6f}")
    ext = dict(zip(prior_names, lp.logpriors))["matter_domination_w0wa"]
    if ext != 0.0 or not np.isfinite(lp.logpost):
        raise SystemExit("ARRET: point accepté traité incorrectement")
    print("  -> ACCEPTÉ : contribution du prior joint = 0.0, logpost fini.")

    rejected = dict(accepted, w=0.5, wa=0.5)
    lp_bad = model.logposterior(rejected)
    print(f"point rejeté  : w=0.5 wa=0.5 (w+wa=1.0)")
    print(f"  logpost = {lp_bad.logpost}")
    if not np.isneginf(lp_bad.logpost):
        raise SystemExit("ARRET: point violant non rejeté")
    print("  -> REJETÉ : logpost = -inf, contrainte jointe effective.")


if __name__ == "__main__":
    main()
