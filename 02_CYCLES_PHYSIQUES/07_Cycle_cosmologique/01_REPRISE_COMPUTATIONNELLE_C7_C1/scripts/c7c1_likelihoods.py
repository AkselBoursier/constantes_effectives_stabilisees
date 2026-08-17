"""Vraisemblances contrôlées C7-C1 — porte G1.0 (issue #63).

Transcription contrôlée des deux vraisemblances des chaînes officielles
DESI DR2 « BAO + CMB comprimé » (G0.1, G0.6) :

- DesiBaoAll : BAO DESI DR2, 13 composantes, gaussienne sur
  (DV/rs, DM/rs, DH/rs). Fichiers officiels
  desi_gaussian_bao_ALL_GCcomb_{mean,cov}.txt, provenance
  CobayaSampler/bao_data @ bb0c1c9009dc76d1391300e169e8df38fd1096db,
  rs_fid = 1 Mpc (cf. manifests/).
- CmbCompressedPR4 : prior gaussien corrélé DESI DR2 sur le vecteur
  q = (theta_star, omega_b h^2, omega_bc h^2), dans l'ordre publié.

Les octets BAO restent hors Git : leur répertoire est fourni à l'exécution
par la variable d'environnement C7C1_DATA_DIR (aucun chemin absolu ici).

Porte G1.0 : chargement et points de vraisemblance seulement — aucun
échantillonnage n'est lancé par ce module.
"""

import os

import numpy as np
from cobaya.likelihood import Likelihood

_C_KM_S = 299792.458


def _data_dir():
    root = os.environ.get("C7C1_DATA_DIR")
    if not root or not os.path.isdir(root):
        raise ValueError(
            "C7C1_DATA_DIR doit désigner le répertoire local (hors Git) "
            "contenant desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_*.txt"
        )
    return root


class DesiBaoAll(Likelihood):
    """BAO DESI DR2, toutes traceurs, 13 composantes (équivalent déclaré
    de bao.desi_dr2.desi_bao_all et des bindings historiques DESI)."""

    measurements_file = os.path.join(
        "desi_bao_dr2", "desi_gaussian_bao_ALL_GCcomb_mean.txt"
    )
    cov_file = os.path.join(
        "desi_bao_dr2", "desi_gaussian_bao_ALL_GCcomb_cov.txt"
    )
    rs_fid = 1.0  # Mpc, convention du yaml officiel Cobaya

    def initialize(self):
        root = _data_dir()
        rows = []
        with open(os.path.join(root, self.measurements_file), encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                z, value, kind = line.split()
                rows.append((float(z), float(value), kind))
        if len(rows) != 13:
            raise ValueError(
                f"13 composantes BAO attendues, {len(rows)} lues : "
                "fichier de mesures non conforme au produit verrouillé."
            )
        self.z = np.array([r[0] for r in rows])
        self.mean = np.array([r[1] for r in rows])
        self.kind = [r[2] for r in rows]
        cov = np.loadtxt(os.path.join(root, self.cov_file))
        if cov.shape != (13, 13):
            raise ValueError(f"covariance 13x13 attendue, forme lue : {cov.shape}")
        self.icov = np.linalg.inv(cov)
        self._z_req = np.unique(self.z)

    def get_requirements(self):
        return {
            "angular_diameter_distance": {"z": self._z_req},
            "Hubble": {"z": self._z_req, "units": "km/s/Mpc"},
            "rdrag": None,
        }

    def logp(self, **params_values):
        rd = self.provider.get_param("rdrag") / self.rs_fid
        d_a = self.provider.get_angular_diameter_distance(self.z)
        hubble = self.provider.get_Hubble(self.z, units="km/s/Mpc")
        d_m = d_a * (1.0 + self.z)
        d_h = _C_KM_S / hubble
        theory = np.empty_like(self.mean)
        for i, kind in enumerate(self.kind):
            if kind == "DV_over_rs":
                theory[i] = (self.z[i] * d_m[i] ** 2 * d_h[i]) ** (1.0 / 3.0) / rd
            elif kind == "DM_over_rs":
                theory[i] = d_m[i] / rd
            elif kind == "DH_over_rs":
                theory[i] = d_h[i] / rd
            else:
                raise ValueError(f"quantité BAO inconnue : {kind}")
        residual = theory - self.mean
        return -0.5 * residual @ self.icov @ residual


class CmbCompressedPR4(Likelihood):
    """Prior gaussien corrélé DESI DR2 sur q = (theta_star, ombh2, ombch2).

    Ordre du vecteur et de la matrice : celui de l'équation publiée (G0.1).
    Point de sûreté : la première coordonnée est theta_star = 0.01041,
    pas 100*theta_star. CAMB/Cobaya sérialisent « thetastar » comme
    100*theta_star (~1.041) : la conversion /100 est donc explicite
    ci-dessous et contrôlée par les tests de point de G1.0.
    """

    def initialize(self):
        self.mu = np.array([0.01041, 0.02223, 0.14208])
        cov = 1e-9 * np.array(
            [
                [0.006621, 0.12444, -1.1929],
                [0.12444, 21.344, -94.001],
                [-1.1929, -94.001, 1488.4],
            ]
        )
        self.icov = np.linalg.inv(cov)

    def get_requirements(self):
        return {"thetastar": None, "ombh2": None, "omch2": None}

    def logp(self, **params_values):
        theta_star = self.provider.get_param("thetastar") / 100.0
        ombh2 = self.provider.get_param("ombh2")
        ombch2 = ombh2 + self.provider.get_param("omch2")
        q = np.array([theta_star, ombh2, ombch2])
        residual = q - self.mu
        return -0.5 * residual @ self.icov @ residual
