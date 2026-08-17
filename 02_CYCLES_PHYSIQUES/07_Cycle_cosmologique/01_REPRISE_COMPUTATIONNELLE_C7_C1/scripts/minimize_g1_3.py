"""Minimisations à départs multiples — porte G1.3 (issue #63).

Pour une configuration donnée (LambdaCDM ou CPL transcrite), exécute N
minimisations indépendantes (graines distinctes, départs tirés des
distributions de référence) dans deux objectifs distincts :

- mode map     : minimum de -log(posterior)  (MAP) ;
- mode maxlike : minimum de -log(vraisemblance), prior ignoré
                 (maximum de vraisemblance).

La distinction stricte MAP / maximum de vraisemblance / minimum rencontré
dans les chaînes est tenue dans le rapport : ce script ne produit que les
deux premiers. Sorties légères vers un répertoire HORS Git (garde-fou).

Usage :
    python scripts/minimize_g1_3.py <config.yaml> <repertoire_sortie> \
        map|maxlike [n_departs=5] [graine_base=1000] \
        [racine_chaines graines_ex:201,202,203,204]

Sans racine de chaînes : départs tirés des distributions de référence des
configs (suffisant en LambdaCDM). Avec racine de chaînes : départs
informés — les meilleurs échantillons (chi2 minimal) des chaînes fournies
servent de points de départ (ref resserrées autour de chacun). Nécessaire
en CPL : la vallée de dégénérescence w0-wa piège les départs naïfs loin du
minimum (constat consigné au rapport G1.3).
"""

import os
import sys

import numpy as np
from cobaya.run import run
from cobaya.yaml import yaml_load_file


def refuser_si_dans_un_depot(path):
    d = os.path.abspath(path)
    while True:
        if os.path.isdir(os.path.join(d, ".git")) or os.path.isfile(
            os.path.join(d, ".git")
        ):
            raise SystemExit(
                f"ARRET: {path!r} est dans un dépôt Git (sorties interdites dans Git)."
            )
        parent = os.path.dirname(d)
        if parent == d:
            return
        d = parent


def main():
    config, out_dir, mode = sys.argv[1], sys.argv[2], sys.argv[3]
    n_starts = int(sys.argv[4]) if len(sys.argv) > 4 else 5
    seed0 = int(sys.argv[5]) if len(sys.argv) > 5 else 1000
    chain_root = sys.argv[6] if len(sys.argv) > 6 else None
    chain_seeds = (
        [int(s) for s in sys.argv[7].split(",")] if len(sys.argv) > 7 else []
    )
    if mode not in ("map", "maxlike"):
        raise SystemExit("ARRET: mode inconnu (map|maxlike)")
    refuser_si_dans_un_depot(out_dir)
    os.makedirs(out_dir, exist_ok=True)

    departs = [None] * n_starts
    if chain_root:
        rows = []
        for cs in chain_seeds:
            path = f"{chain_root}/s{cs}/chain.1.txt"
            with open(path, encoding="utf-8") as f:
                header = next(
                    line for line in f if line.lstrip().startswith("#")
                )
            names = header.lstrip().lstrip("#").split()
            d = np.loadtxt(path)
            k = int(np.argmin(d[:, names.index("chi2")]))
            rows.append((float(d[k, names.index("chi2")]), names, d[k]))
        rows.sort(key=lambda r: r[0])
        departs = [rows[i % len(rows)] for i in range(n_starts)]
        print(
            "départs informés par les chaînes (chi2 des points de départ) : "
            + " ".join(f"{r[0]:.4f}" for r in departs)
        )

    results = []
    for i in range(n_starts):
        seed = seed0 + i
        info = yaml_load_file(config)
        info.pop("output", None)
        if departs[i] is not None:
            chi2_0, names, row = departs[i]
            for p, spec in info["params"].items():
                if isinstance(spec, dict) and "prior" in spec and p in names:
                    scale = float(spec.get("proposal", 0.001)) / 5.0
                    spec["ref"] = {
                        "dist": "norm",
                        "loc": float(row[names.index(p)]),
                        "scale": scale,
                    }
        info["sampler"] = {
            "minimize": {
                "ignore_prior": mode == "maxlike",
                "seed": seed,
                "best_of": 1,
            }
        }
        info["output"] = os.path.join(out_dir, f"min_{mode}_s{seed}", "min")
        upd, sampler = run(info, force=True)
        prod = sampler.products()
        point = prod["minimum"]
        results.append((seed, point))

    sampled = [p for p in results[0][1].sampled_params]
    print(f"\n=== minimisations {mode} : {n_starts} départs ===")
    objectif = "-logpost (MAP)" if mode == "map" else "-loglike (max vraisemblance)"
    print(f"objectif : {objectif}")
    print("graine  valeur_objectif  chi2_total  " + "  ".join(sampled))
    best = None
    for seed, pt in results:
        val = float(pt["minuslogpost"])
        try:
            chi2 = float(pt["chi2"])
        except Exception:
            chi2 = float("nan")
        vals = "  ".join(f"{float(pt[p]):.6f}" for p in sampled)
        print(f"{seed}  {val:.6f}  {chi2:.6f}  {vals}")
        if best is None or val < best[1]:
            best = (seed, val, pt)
    print(f"\nmeilleur départ : graine {best[0]}, objectif {best[1]:.6f}")
    spread = max(float(p["minuslogpost"]) for _, p in results) - min(
        float(p["minuslogpost"]) for _, p in results
    )
    print(f"dispersion entre départs (objectif) : {spread:.2e}")


if __name__ == "__main__":
    main()
