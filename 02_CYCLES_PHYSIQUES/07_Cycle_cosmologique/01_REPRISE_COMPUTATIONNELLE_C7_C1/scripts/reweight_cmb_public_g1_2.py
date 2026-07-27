"""Repondération CMB publique arrondie — porte G1.2 (issue #63, §2.3).

Pour chaque échantillon des chaînes officielles comprimées (LambdaCDM ou
CPL), calcule :

    Delta chi2_CMB = chi2_public_arrondi - chi2_officiel_stocke
    poids_public   = poids_officiel * exp(-Delta chi2_CMB / 2)

où chi2_public_arrondi est le chi2 de la convention ratifiée
CMB_compressed_public_DR2_rounded (coefficients publiés, transcrits dans
c7c1_likelihoods.CmbCompressedPR4 ; mêmes mu et C ici).

theta_star est évalué selon le mode choisi :
- degree=0 : MODE EXACT INTÉGRAL — un appel CAMB par échantillon, aucune
  émulation. Mode directeur retenu pour G1.2 : l'implémentation PPF
  introduit un pli non-analytique de theta_star le long de la surface de
  croisement w(a) = -1, que les émulateurs lisses (polynôme, RBF) ne
  suivent pas au niveau requis (diagnostic consigné dans reports/).
- degree>0 : mode hybride historique (émulateur polynomial + étage RBF
  conditionnel, validé sur points CAMB tenus à l'écart, queue Mahalanobis
  exacte) ; le script S'ARRETE si la validation du coeur dépasse le seuil.

Publie : distribution pondérée de Delta chi2 (min/max/moyenne/écart-type,
quantiles 5/50/95), tailles effectives avant/après, déplacements des
moyennes/médianes/intervalles 68 % (Omega_m, H0, w0, wa) en fraction de
l'écart-type officiel, variation des largeurs, meilleurs échantillons,
corrélations de Delta chi2 avec les paramètres tardifs.

AUCUN échantillonnage MCMC ; aucune écriture de fichier : sortie stdout
uniquement (rapport léger repris dans reports/).

Usage :
    python scripts/reweight_cmb_public_g1_2.py <repertoire_chaines> lcdm|cpl \
        [n_train] [n_val] [degree] [nproc] [tail_frac]

Defauts : n_train=600, n_val=150, degree=4, nproc=1, tail_frac=0.01
(reproduisent le run LambdaCDM). L'espace CPL (5 dimensions, priors larges
sur w0/wa, degenerescences) exige un emulateur plus riche ET une queue
exacte plus large : degree=6, n_train=3000, tail_frac=0.05 valides
empiriquement.
"""

import multiprocessing
import sys

import camb
import numpy as np

MU = np.array([0.01041, 0.02223, 0.14208])
COV = 1e-9 * np.array(
    [
        [0.006621, 0.12444, -1.1929],
        [0.12444, 21.344, -94.001],
        [-1.1929, -94.001, 1488.4],
    ]
)
ICOV = np.linalg.inv(COV)
SIGMA_THETA = float(np.sqrt(COV[0, 0]))

SEUIL_VAL_SIGMA = 0.005  # residu max admis sur points de validation (coeur)
CHUNK = 20000  # taille de bloc pour les matrices de monomes

FIXED = dict(
    mnu=0.06,
    nnu=3.044,
    num_massive_neutrinos=1,
    bbn_predictor="PArthENoPE_880.2_standard.dat",
    dark_energy_model="ppf",
    tau=0.0544,
    ns=0.9649,
    As=1e-10 * np.exp(3.036),
)


def theta_star_camb(H0, ombh2, omch2, w=None, wa=None):
    kw = dict(FIXED, H0=H0, ombh2=ombh2, omch2=omch2)
    if w is not None:
        kw.update(w=w, wa=wa)
    pars = camb.set_params(**kw)
    res = camb.get_background(pars)
    return res.get_derived_params()["thetastar"] / 100.0


def _worker(args):
    return theta_star_camb(*args)


def monomials(x, degree):
    n, d = x.shape
    cols = [np.ones(n)]
    idx = [np.zeros(d, dtype=int)]

    def rec(start, left, cur):
        for j in range(start, d):
            nxt = cur.copy()
            nxt[j] += 1
            cols.append(np.prod(x**nxt, axis=1))
            idx.append(nxt)
            if left > 1:
                rec(j, left - 1, nxt)

    rec(0, degree, np.zeros(len(x[0]), dtype=int))
    return np.column_stack(cols)


def wq(x, w, q):
    order = np.argsort(x)
    cw = np.cumsum(w[order])
    return float(np.interp(q * cw[-1], cw, x[order]))


def ess(w):
    return float(w.sum() ** 2 / (w**2).sum())


def main():
    root, model = sys.argv[1], sys.argv[2]
    n_train = int(sys.argv[3]) if len(sys.argv) > 3 else 600
    n_val = int(sys.argv[4]) if len(sys.argv) > 4 else 150
    degree = int(sys.argv[5]) if len(sys.argv) > 5 else 4
    nproc = int(sys.argv[6]) if len(sys.argv) > 6 else 1
    tail_frac = float(sys.argv[7]) if len(sys.argv) > 7 else 0.01
    is_cpl = model == "cpl"

    names = None
    blocks = []
    for i in (1, 2, 3, 4):
        path = f"{root}/chain.{i}.txt"
        with open(path, encoding="utf-8") as f:
            header = next(line for line in f if line.lstrip().startswith("#"))
        n = header.lstrip().lstrip("#").split()
        if names is None:
            names = n
        elif n != names:
            raise SystemExit("ARRET: en-têtes hétérogènes entre chaînes")
        blocks.append(np.loadtxt(path))
    data = np.vstack(blocks)
    col = {n: i for i, n in enumerate(names)}
    print(f"modele={model}  echantillons={len(data)}  (4 chaines)")

    feats = ["H0", "ombh2", "omch2"] + (["w", "wa"] if is_cpl else [])
    X = np.column_stack([data[:, col[f]] for f in feats])
    xm, xs = X.mean(axis=0), X.std(axis=0)
    Xs = (X - xm) / xs

    def exact(rows):
        tasks = [tuple(X[r]) + ((None, None) if not is_cpl else ()) for r in rows]
        tasks = [t[:5] for t in tasks]
        if nproc > 1:
            with multiprocessing.Pool(nproc) as pool:
                return np.array(pool.map(_worker, tasks, chunksize=8))
        return np.array([_worker(t) for t in tasks])

    def theta_hybride():
        rng = np.random.default_rng(63)
        pick = rng.choice(len(data), size=n_train + n_val, replace=False)
        tr, va = pick[:n_train], pick[n_train:]
        y_tr, y_va = exact(tr), exact(va)
        y0 = y_tr.mean()
        A = monomials(Xs[tr], degree)
        coef, *_ = np.linalg.lstsq(A, (y_tr - y0) * 1e6, rcond=None)

        def emul(rows):
            out = np.empty(len(rows))
            for a in range(0, len(rows), CHUNK):
                sl = rows[a : a + CHUNK]
                out[a : a + CHUNK] = y0 + monomials(Xs[sl], degree) @ coef * 1e-6
            return out

        # coeur/queue : distance de Mahalanobis des traits standardises
        sinv = np.linalg.inv(np.cov(Xs.T))
        dist2 = np.einsum("ij,jk,ik->i", Xs, sinv, Xs)
        cut = np.quantile(dist2, 1.0 - tail_frac)
        tail = np.flatnonzero(dist2 > cut)
        core = np.flatnonzero(dist2 <= cut)

        mask_va = dist2[va] <= cut
        va_core, y_va_core = va[mask_va], y_va[mask_va]

        def bilan(resid, etage):
            print(
                f"emulateur theta_star (etage {etage}) : deg={degree} "
                f"train={n_train} val_coeur={len(va_core)}/{n_val} ; "
                f"residu val max={np.abs(resid).max():.3e} "
                f"({np.abs(resid).max()/SIGMA_THETA:.4f} sigma_theta) "
                f"rms={np.sqrt((resid**2).mean()):.3e}"
            )

        emul_final = emul
        resid = emul(va_core) - y_va_core
        bilan(resid, 1)
        if np.abs(resid).max() > SEUIL_VAL_SIGMA * SIGMA_THETA:
            from scipy.interpolate import RBFInterpolator

            rbf = RBFInterpolator(
                Xs[tr], (y_tr - emul(tr)) * 1e6, kernel="thin_plate_spline"
            )

            def emul2(rows):
                out = np.empty(len(rows))
                for a in range(0, len(rows), CHUNK):
                    sl = rows[a : a + CHUNK]
                    out[a : a + CHUNK] = emul(sl) + rbf(Xs[sl]) * 1e-6
                return out

            emul_final = emul2
            resid = emul2(va_core) - y_va_core
            bilan(resid, 2)

        print(
            f"hybride : coeur emule={len(core)} ; queue CAMB exact={len(tail)} "
            f"({len(tail)/len(data):.2%})"
        )
        if np.abs(resid).max() > SEUIL_VAL_SIGMA * SIGMA_THETA:
            raise SystemExit(
                "ARRET: emulateur theta_star hors tolerance de validation (coeur)"
            )

        th = np.empty(len(data))
        th[core] = emul_final(core)
        th[tail] = exact(tail)
        return th

    if degree == 0:
        print("mode EXACT INTEGRAL : un appel CAMB par echantillon, aucune emulation")
        theta = exact(np.arange(len(data)))
    else:
        theta = theta_hybride()
    ombh2 = data[:, col["ombh2"]]
    ombch2 = ombh2 + data[:, col["omch2"]]
    R = np.column_stack([theta, ombh2, ombch2]) - MU
    chi2_pub = np.einsum("ij,jk,ik->i", R, ICOV, R)
    chi2_off = data[:, col["chi2__CMB_compressed"]]
    dchi2 = chi2_pub - chi2_off

    w_off = data[:, col["weight"]]
    w_pub = w_off * np.exp(-(dchi2 - np.median(dchi2)) / 2.0)

    print("\n--- distribution ponderee de Delta chi2_CMB (poids officiels) ---")
    m = np.average(dchi2, weights=w_off)
    sd = np.sqrt(np.average((dchi2 - m) ** 2, weights=w_off))
    print(f"min={dchi2.min():+.4f} max={dchi2.max():+.4f} moyenne={m:+.4f} ecart-type={sd:.4f}")
    print(
        "quantiles 5/50/95 : "
        + " ".join(f"{wq(dchi2, w_off, q):+.4f}" for q in (0.05, 0.50, 0.95))
    )

    e0, e1 = ess(w_off), ess(w_pub)
    print(f"\nESS officiel={e0:.1f}  ESS repondere={e1:.1f}  ratio={e1/e0:.4f}")
    top = np.sort(w_pub)[::-1]
    print(f"part des 10 plus gros poids reponderes : {top[:10].sum()/w_pub.sum():.4%}")

    print("\n--- parametres directeurs (officiel -> repondere) ---")
    params = ["omegam", "H0"] + (["w", "wa"] if is_cpl else [])
    print("param   moy_off    moy_pub    d_moy/sig  med_off    med_pub    d_med/sig  "
          "q16_off   q84_off   q16_pub   q84_pub   d_largeur%")
    for p in params:
        x = data[:, col[p]]
        mo = np.average(x, weights=w_off)
        so = np.sqrt(np.average((x - mo) ** 2, weights=w_off))
        mp = np.average(x, weights=w_pub)
        do, dp = wq(x, w_off, 0.5), wq(x, w_pub, 0.5)
        a0, b0 = wq(x, w_off, 0.16), wq(x, w_off, 0.84)
        a1, b1 = wq(x, w_pub, 0.16), wq(x, w_pub, 0.84)
        print(
            f"{p:<7} {mo:9.5f}  {mp:9.5f}  {(mp-mo)/so:+9.4f}  "
            f"{do:9.5f}  {dp:9.5f}  {(dp-do)/so:+9.4f}  "
            f"{a0:8.5f}  {b0:8.5f}  {a1:8.5f}  {b1:8.5f}  "
            f"{((b1-a1)/(b0-a0)-1)*100:+8.3f}"
        )

    chi2_tot_off = data[:, col["chi2"]]
    chi2_tot_pub = chi2_tot_off - chi2_off + chi2_pub
    i0, i1 = np.argmin(chi2_tot_off), np.argmin(chi2_tot_pub)
    print("\n--- meilleurs echantillons disponibles (min chi2 total) ---")
    print(f"officiel : chi2={chi2_tot_off[i0]:.4f} (echantillon {i0})")
    print(f"public   : chi2={chi2_tot_pub[i1]:.4f} (echantillon {i1})")
    print(f"min chi2_public au point officiel optimal : {chi2_tot_pub[i0]:.4f}")

    print("\n--- correlations ponderees de Delta chi2 avec parametres tardifs ---")
    for p in ["H0", "omegam", "rdrag", "H0rdrag"] + (["w", "wa"] if is_cpl else []):
        x = data[:, col[p]]
        mx = np.average(x, weights=w_off)
        md = np.average(dchi2, weights=w_off)
        cxy = np.average((x - mx) * (dchi2 - md), weights=w_off)
        cxx = np.average((x - mx) ** 2, weights=w_off)
        cyy = np.average((dchi2 - md) ** 2, weights=w_off)
        print(f"corr(Delta chi2, {p:<8}) = {cxy/np.sqrt(cxx*cyy):+.4f}")


if __name__ == "__main__":
    main()
