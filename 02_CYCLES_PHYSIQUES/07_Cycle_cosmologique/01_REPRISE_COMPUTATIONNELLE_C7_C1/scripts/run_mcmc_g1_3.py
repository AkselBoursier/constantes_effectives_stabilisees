"""Lanceur MCMC contrôlé — porte G1.3 (issue #63).

Reproduit LambdaCDM ou CPL sous la vraisemblance commune (configs/
transcrites, vraisemblances c7c1_likelihoods, prior joint CPL explicite),
avec le bloc sampler officiel transcrit :

    Rminus1_stop = 0.01 ; Rminus1_cl_stop = 0.02.

Règles :
- le préfixe de sortie est fourni à l'exécution et DOIT être hors du
  dépôt : le script s'arrête si un répertoire `.git` est trouvé dans les
  ancêtres du préfixe (chaînes et sorties volumineuses hors Git) ;
- la graine est fournie explicitement par chaîne (traçabilité) ;
- reprise automatique autorisée (resume) après interruption.

Usage :
    python scripts/run_mcmc_g1_3.py <config.yaml> <prefixe_sortie> <graine>
"""

import os
import sys

from cobaya.run import run
from cobaya.yaml import yaml_load_file


def refuser_si_dans_un_depot(prefix):
    d = os.path.abspath(os.path.dirname(prefix))
    while True:
        if os.path.isdir(os.path.join(d, ".git")) or os.path.isfile(
            os.path.join(d, ".git")
        ):
            raise SystemExit(
                f"ARRET: le préfixe de sortie {prefix!r} est dans un dépôt Git "
                "(chaînes et sorties volumineuses interdites dans Git)."
            )
        parent = os.path.dirname(d)
        if parent == d:
            return
        d = parent


def main():
    config, out_prefix, seed = sys.argv[1], sys.argv[2], int(sys.argv[3])
    refuser_si_dans_un_depot(out_prefix)
    os.makedirs(os.path.dirname(out_prefix), exist_ok=True)

    info = yaml_load_file(config)
    info["output"] = out_prefix
    info["sampler"]["mcmc"]["seed"] = seed
    run(info, resume=True)


if __name__ == "__main__":
    main()
