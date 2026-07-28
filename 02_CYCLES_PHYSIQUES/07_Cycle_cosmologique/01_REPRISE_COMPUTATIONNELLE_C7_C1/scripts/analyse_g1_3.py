"""Analyse des reproductions G1.3 — porte G1.3 (issue #63).

Charge les 4 chaînes indépendantes d'un modèle (LambdaCDM ou CPL)
produites par run_mcmc_g1_3.py et publie, sans écrire de fichier :

1. diagnostics de convergence : Gelman-Rubin R-1 multi-chaînes (burn-in
   30 % retiré), taille effective pondérée par chaîne et combinée ;
2. moyennes, médianes, intervalles 68 % pondérés des paramètres
   directeurs ;
3. contrôle T7 : comparaison aux chaînes officielles compressées
   (déplacement des moyennes en fraction de l'écart-type officiel
   <= 0.10 ; largeurs 68 % à ±5 %) ;
4. minimum de chi2 RENCONTRÉ dans les chaînes (statistique d'échantillon,
   à ne pas confondre avec le MAP ni le maximum de vraisemblance, produits
   séparément par minimize_g1_3.py) ;
5. résidus BAO par composante et contribution CMB au meilleur échantillon.

Usage :
    python scripts/analyse_g1_3.py <config.yaml> <racine_runs> \
        <graines ex: 101,102,103,104> <repertoire_chaines_officielles>
"""

import sys

import numpy as np

BURN = 0.30
C_KM_S = 299792.458


def wq(x, w, q):
    order = np.argsort(x)
    cw = np.cumsum(w[order])
    return float(np.interp(q * cw[-1], cw, x[order]))


def charge(prefix):
    path = f"{prefix}.1.txt"
    with open(path, encoding="utf-8") as f:
        header = next(line for line in f if line.lstrip().startswith("#"))
    names = header.lstrip().lstrip("#").split()
    data = np.loadtxt(path)
    n0 = int(BURN * len(data))
    return names, data[n0:]


def gelman_rubin(chains_x, chains_w):
    means = np.array(
        [np.average(x, weights=w) for x, w in zip(chains_x, chains_w)]
    )
    variances = np.array(
        [
            np.average((x - m) ** 2, weights=w)
            for x, w, m in zip(chains_x, chains_w, means)
        ]
    )
    B = means.var(ddof=1)
    W = variances.mean()
    return B / W if W > 0 else np.inf


def main():
    config, root, seeds_arg, off_root = sys.argv[1:5]
    seeds = [int(s) for s in seeds_arg.split(",")]

    names = None
    per_chain = []
    for s in seeds:
        n, d = charge(f"{root}/s{s}/chain")
        names = names or n
        if n != names:
            raise SystemExit("ARRET: en-têtes hétérogènes entre chaînes G1.3")
        per_chain.append(d)
    col = {n: i for i, n in enumerate(names)}
    allo = np.vstack(per_chain)
    w_all = allo[:, col["weight"]]

    params = ["omegam", "H0"] + (["w", "wa"] if "wa" in col else [])

    print(f"=== convergence (burn-in {BURN:.0%} retiré, {len(seeds)} chaînes) ===")
    print(f"echantillons post burn-in par chaîne : {[len(d) for d in per_chain]}")
    for p in params + ["rdrag"]:
        r1 = gelman_rubin(
            [d[:, col[p]] for d in per_chain],
            [d[:, col["weight"]] for d in per_chain],
        )
        print(f"R-1 ({p:<7}) = {r1:.5f}")
    ess = float(w_all.sum() ** 2 / (w_all**2).sum())
    print(f"ESS ponderee combinee = {ess:.1f}")

    print("\n=== posterior combiné (pondéré) ===")
    print("param    moyenne    mediane    q16        q84        largeur68")
    stats = {}
    for p in params:
        x = allo[:, col[p]]
        m = np.average(x, weights=w_all)
        sd = np.sqrt(np.average((x - m) ** 2, weights=w_all))
        med = wq(x, w_all, 0.5)
        a, b = wq(x, w_all, 0.16), wq(x, w_all, 0.84)
        stats[p] = (m, sd, a, b)
        print(f"{p:<7} {m:10.5f} {med:10.5f} {a:10.5f} {b:10.5f} {b - a:10.5f}")

    print("\n=== contrôle T7 vs chaînes officielles compressées ===")
    onames = None
    oblocks = []
    for i in (1, 2, 3, 4):
        path = f"{off_root}/chain.{i}.txt"
        with open(path, encoding="utf-8") as f:
            header = next(line for line in f if line.lstrip().startswith("#"))
        onames = header.lstrip().lstrip("#").split()
        oblocks.append(np.loadtxt(path))
    odata = np.vstack(oblocks)
    ocol = {n: i for i, n in enumerate(onames)}
    ow = odata[:, ocol["weight"]]
    print("param    d_moyenne/sig_off   largeur_ours/largeur_off   verdict T7")
    t7_ok = True
    for p in params:
        x = odata[:, ocol[p]]
        mo = np.average(x, weights=ow)
        so = np.sqrt(np.average((x - mo) ** 2, weights=ow))
        ao, bo = wq(x, ow, 0.16), wq(x, ow, 0.84)
        m, sd, a, b = stats[p]
        dshift = (m - mo) / so
        rlarg = (b - a) / (bo - ao)
        ok = abs(dshift) <= 0.10 and abs(rlarg - 1) <= 0.05
        t7_ok &= ok
        print(
            f"{p:<7} {dshift:+18.4f} {rlarg:26.4f}   "
            + ("PASSE" if ok else "ECHEC")
        )
    print(f"T7 global : {'PASSE' if t7_ok else 'ECHEC'}")

    print("\n=== minimum de chi2 RENCONTRÉ dans les chaînes ===")
    print("(statistique d'échantillon ; distinct du MAP et du maximum de")
    print(" vraisemblance produits par minimize_g1_3.py)")
    def col_chi2(fragment, fallback):
        for n in names:
            if n.startswith("chi2__") and fragment in n:
                return col[n]
        return col[fallback]

    c_bao = col_chi2("DesiBaoAll", "chi2__BAO")
    c_cmb = col_chi2("CmbCompressed", "chi2__CMB_compressed")
    chi2 = allo[:, col["chi2"]]
    i0 = int(np.argmin(chi2))
    print(f"min chi2 total = {chi2[i0]:.4f}")
    print(
        f"  chi2_BAO = {allo[i0, c_bao]:.4f} ; "
        f"chi2_CMB = {allo[i0, c_cmb]:.4f}"
    )
    best_point = {p: float(allo[i0, col[p]]) for p in ["H0", "ombh2", "omm"]
                  + (["w", "wa"] if "wa" in col else [])}
    print(f"  point : {best_point}")

    print("\n=== résidus BAO par composante au meilleur échantillon ===")
    import os
    from cobaya.model import get_model
    from cobaya.yaml import yaml_load_file

    info = yaml_load_file(config)
    info.pop("sampler", None)
    info.pop("output", None)
    model = get_model(info)
    lp = model.logposterior(best_point)
    like = model.likelihood["c7c1_likelihoods.DesiBaoAll"]
    rd = model.provider.get_param("rdrag") / like.rs_fid
    d_a = model.provider.get_angular_diameter_distance(like.z)
    hub = model.provider.get_Hubble(like.z, units="km/s/Mpc")
    d_m = d_a * (1.0 + like.z)
    d_h = C_KM_S / hub
    print("z        quantite     donnee      theorie     residu    residu/sigma")
    cov = np.linalg.inv(like.icov)
    for i, kind in enumerate(like.kind):
        if kind == "DV_over_rs":
            th = (like.z[i] * d_m[i] ** 2 * d_h[i]) ** (1.0 / 3.0) / rd
        elif kind == "DM_over_rs":
            th = d_m[i] / rd
        else:
            th = d_h[i] / rd
        r = th - like.mean[i]
        sig = np.sqrt(cov[i, i])
        print(
            f"{like.z[i]:<8.3f} {kind:<12} {like.mean[i]:10.4f} {th:11.4f} "
            f"{r:+9.4f} {r / sig:+9.3f}"
        )
    loglikes = dict(zip(list(model.likelihood), lp.loglikes))
    print(
        f"\ncontributions au meilleur échantillon : "
        f"chi2_BAO = {-2 * loglikes['c7c1_likelihoods.DesiBaoAll']:.4f} ; "
        f"chi2_CMB = {-2 * loglikes['c7c1_likelihoods.CmbCompressedPR4']:.4f}"
    )


if __name__ == "__main__":
    main()
