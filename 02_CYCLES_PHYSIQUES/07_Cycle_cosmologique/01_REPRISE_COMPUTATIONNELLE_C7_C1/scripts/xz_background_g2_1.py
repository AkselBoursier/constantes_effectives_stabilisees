"""Fond cosmologique direct en X(z) — porte G2.1 (issue #63).

Ce module valide l'instrument numérique seulement. Il ne définit aucun prior
scientifique sur les amplitudes X_i, ne lance aucun MCMC et ne convertit pas
X(z) en w(z).

Architecture ratifiée G2.0 :

    H_X(z)^2 = H_ref(z)^2 + H0^2 * Omega_X,0 * (X(z) - 1)

Le fond de référence est LambdaCDM calculé par CAMB 1.5.4 sous les conventions
G1. Les distances tardives sont recalculées directement avec H_X. Deux
traitements de l'étalon acoustique sont exposés :

- ``fixed`` : r_star et r_drag CAMB conservés ;
- ``corrected`` : correction différentielle de leurs intégrales par H_X.

Les valeurs négatives de X sont admises pendant les tests. Un profil n'est
rejeté que si une valeur non finie apparaît ou si H_X^2 <= 0 sur un point
évalué du domaine requis.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable, Literal, Protocol, Sequence

import numpy as np
from scipy.integrate import quad
from scipy.interpolate import CubicSpline

C_KM_S = 299_792.458
Z_MAX_NODE = 2.33

Variant = Literal["M2a", "M2b"]
SplineConvention = Literal["natural", "not-a-knot"]
AcousticMode = Literal["fixed", "corrected"]

NODES: dict[Variant, np.ndarray] = {
    "M2a": np.array([0.0, 1.0 / 3.0, 2.0 / 3.0, 1.0, 4.0 / 3.0, 2.33]),
    "M2b": np.array([0.0, 1.0 / 3.0, 2.0 / 3.0, 1.0, 2.33]),
}


class InvalidBackgroundError(ValueError):
    """Le profil produit un fond non fini ou H_X^2 <= 0."""


@dataclass(frozen=True)
class XZProfile:
    """Spline cubique directe de X(z), avec X(0)=1 imposé par définition."""

    variant: Variant
    free_values: tuple[float, ...]
    convention: SplineConvention = "not-a-knot"

    def __post_init__(self) -> None:
        nodes = NODES[self.variant]
        expected = len(nodes) - 1
        if len(self.free_values) != expected:
            raise ValueError(
                f"{self.variant} attend {expected} amplitudes libres, "
                f"{len(self.free_values)} reçues."
            )
        values = np.array((1.0, *self.free_values), dtype=float)
        if not np.all(np.isfinite(values)):
            raise ValueError("Les amplitudes X_i doivent être finies.")
        object.__setattr__(self, "_nodes", nodes.copy())
        object.__setattr__(self, "_values", values)
        object.__setattr__(
            self,
            "_spline",
            CubicSpline(nodes, values, bc_type=self.convention, extrapolate=False),
        )

    @classmethod
    def constant(
        cls,
        variant: Variant = "M2a",
        value: float = 1.0,
        convention: SplineConvention = "not-a-knot",
    ) -> "XZProfile":
        """Construit notamment la limite LambdaCDM avec ``value=1``."""

        return cls(variant, tuple([float(value)] * (len(NODES[variant]) - 1)), convention)

    @property
    def nodes(self) -> np.ndarray:
        return self._nodes.copy()

    @property
    def values(self) -> np.ndarray:
        return self._values.copy()

    @property
    def last_value(self) -> float:
        return float(self._values[-1])

    def __call__(self, z: float | Sequence[float] | np.ndarray) -> float | np.ndarray:
        arr = np.asarray(z, dtype=float)
        if np.any(~np.isfinite(arr)):
            raise ValueError("Le redshift doit être fini.")
        if np.any(arr < 0.0):
            raise ValueError("G2.1 est défini pour z >= 0.")
        clipped = np.minimum(arr, Z_MAX_NODE)
        out = np.asarray(self._spline(clipped), dtype=float)
        out = np.where(arr >= Z_MAX_NODE, self.last_value, out)
        if arr.ndim == 0:
            return float(out)
        return out

    def derivative(self, z: float | Sequence[float] | np.ndarray, order: int = 1) -> float | np.ndarray:
        """Dérivée à gauche dans la spline, nulle au-delà de 2.33."""

        if order not in (1, 2):
            raise ValueError("Seules les dérivées d'ordre 1 et 2 sont exposées.")
        arr = np.asarray(z, dtype=float)
        if np.any(arr < 0.0) or np.any(~np.isfinite(arr)):
            raise ValueError("Le redshift doit être fini et >= 0.")
        left = np.asarray(self._spline(np.minimum(arr, Z_MAX_NODE), nu=order), dtype=float)
        out = np.where(arr > Z_MAX_NODE, 0.0, left)
        if arr.ndim == 0:
            return float(out)
        return out


class ReferenceBackground(Protocol):
    h0: float
    omega_x0: float
    ombh2: float
    omch2: float
    zstar: float
    zdrag: float
    rstar: float
    rdrag: float
    theta_star: float
    baryon_photon_ratio0: float

    def hubble(self, z: float | np.ndarray) -> float | np.ndarray: ...
    def comoving_distance(self, z: float | np.ndarray) -> float | np.ndarray: ...


@dataclass
class CambReference:
    """Adaptateur d'un résultat CAMB 1.5.4 sous les paramètres G1."""

    results: object
    h0: float
    omega_x0: float
    ombh2: float
    omch2: float
    zstar: float
    zdrag: float
    rstar: float
    rdrag: float
    theta_star: float
    baryon_photon_ratio0: float

    @classmethod
    def from_g1(
        cls,
        *,
        h0: float,
        ombh2: float,
        omegam: float,
        mnu: float = 0.06,
        nnu: float = 3.044,
        loga: float = 3.036,
        ns: float = 0.9649,
        tau: float = 0.0544,
    ) -> "CambReference":
        try:
            import camb
        except ImportError as exc:
            raise RuntimeError(
                "CAMB est requis pour les tests complets G2.1. Utiliser "
                "l'environnement directeur gelé (CAMB 1.5.4)."
            ) from exc

        omch2 = omegam * (h0 / 100.0) ** 2 - mnu / 93.14 - ombh2
        if omch2 <= 0.0:
            raise ValueError(f"omch2 non positif sous les coordonnées G1 : {omch2}")

        pars = camb.set_params(
            H0=h0,
            ombh2=ombh2,
            omch2=omch2,
            mnu=mnu,
            nnu=nnu,
            omk=0.0,
            num_massive_neutrinos=1,
            tau=tau,
            As=1e-10 * np.exp(loga),
            ns=ns,
            w=-1.0,
            wa=0.0,
            dark_energy_model="ppf",
            bbn_predictor="PArthENoPE_880.2_standard.dat",
        )
        results = camb.get_background(pars, no_thermo=False)
        derived = results.get_derived_params()
        densities0 = results.get_background_densities(
            np.array([1.0]), vars=["baryon", "photon"], format="dict"
        )
        rho_b0 = float(np.asarray(densities0["baryon"]).reshape(-1)[0])
        rho_g0 = float(np.asarray(densities0["photon"]).reshape(-1)[0])
        if rho_b0 <= 0.0 or rho_g0 <= 0.0:
            raise RuntimeError("Densités baryon/photon CAMB non positives.")

        return cls(
            results=results,
            h0=float(h0),
            omega_x0=float(results.omega_de),
            ombh2=float(ombh2),
            omch2=float(omch2),
            zstar=float(derived["zstar"]),
            zdrag=float(derived["zdrag"]),
            rstar=float(derived["rstar"]),
            rdrag=float(derived["rdrag"]),
            theta_star=float(derived["thetastar"]) / 100.0,
            baryon_photon_ratio0=rho_b0 / rho_g0,
        )

    def hubble(self, z: float | np.ndarray) -> float | np.ndarray:
        arr = np.asarray(z, dtype=float)
        arg = float(arr) if arr.ndim == 0 else arr
        out = self.results.hubble_parameter(arg)
        return float(out) if arr.ndim == 0 else np.asarray(out, dtype=float)

    def comoving_distance(self, z: float | np.ndarray) -> float | np.ndarray:
        arr = np.asarray(z, dtype=float)
        arg = float(arr) if arr.ndim == 0 else arr
        out = self.results.comoving_radial_distance(arg)
        return float(out) if arr.ndim == 0 else np.asarray(out, dtype=float)


@dataclass
class XZBackground:
    """Fond tardif direct construit à partir d'un profil X(z)."""

    reference: ReferenceBackground
    profile: XZProfile
    epsabs: float = 1e-8
    epsrel: float = 1e-10
    quad_limit: int = 300
    acoustic_zmax: float = 1e7
    _dm_cache: dict[float, float] = field(default_factory=dict, init=False, repr=False)

    def h2(self, z: float | Sequence[float] | np.ndarray) -> float | np.ndarray:
        arr = np.asarray(z, dtype=float)
        arg = float(arr) if arr.ndim == 0 else arr
        href = np.asarray(self.reference.hubble(arg), dtype=float)
        x = np.asarray(self.profile(arg), dtype=float)
        h2 = href * href + self.reference.h0**2 * self.reference.omega_x0 * (x - 1.0)
        if np.any(~np.isfinite(h2)) or np.any(h2 <= 0.0):
            raise InvalidBackgroundError("Fond invalide : H_X^2 non positif ou non fini.")
        return float(h2) if arr.ndim == 0 else h2

    def hubble(self, z: float | Sequence[float] | np.ndarray) -> float | np.ndarray:
        out = np.sqrt(self.h2(z))
        return float(out) if np.asarray(z).ndim == 0 else np.asarray(out, dtype=float)

    def dh(self, z: float | Sequence[float] | np.ndarray) -> float | np.ndarray:
        out = C_KM_S / np.asarray(self.hubble(z), dtype=float)
        return float(out) if np.asarray(z).ndim == 0 else out

    def _dm_scalar(self, z: float) -> float:
        if z < 0.0 or not np.isfinite(z):
            raise ValueError("Le redshift doit être fini et >= 0.")
        if z == 0.0:
            return 0.0
        key = float(z)
        if key in self._dm_cache:
            return self._dm_cache[key]
        value, _ = quad(
            lambda zz: C_KM_S / float(self.hubble(zz)),
            0.0,
            key,
            epsabs=self.epsabs,
            epsrel=self.epsrel,
            limit=self.quad_limit,
            points=[p for p in self.profile.nodes[1:-1] if 0.0 < p < key],
        )
        result = float(value)
        if len(self._dm_cache) >= 2048:
            self._dm_cache.clear()
        self._dm_cache[key] = result
        return result

    def dm(self, z: float | Sequence[float] | np.ndarray) -> float | np.ndarray:
        arr = np.asarray(z, dtype=float)
        out = np.array(
            [self._dm_scalar(float(v)) for v in arr.reshape(-1)], dtype=float
        ).reshape(arr.shape)
        return float(out) if arr.ndim == 0 else out

    def da(self, z: float | Sequence[float] | np.ndarray) -> float | np.ndarray:
        arr = np.asarray(z, dtype=float)
        out = np.asarray(self.dm(arr), dtype=float) / (1.0 + arr)
        return float(out) if arr.ndim == 0 else out

    def dv(self, z: float | Sequence[float] | np.ndarray) -> float | np.ndarray:
        arr = np.asarray(z, dtype=float)
        dm = np.asarray(self.dm(arr), dtype=float)
        dh = np.asarray(self.dh(arr), dtype=float)
        out = np.cbrt(arr * dm * dm * dh)
        return float(out) if arr.ndim == 0 else out

    def sound_speed(self, z: float | np.ndarray) -> float | np.ndarray:
        arr = np.asarray(z, dtype=float)
        ratio = self.reference.baryon_photon_ratio0 / (1.0 + arr)
        out = C_KM_S / np.sqrt(3.0 * (1.0 + 0.75 * ratio))
        return float(out) if arr.ndim == 0 else out

    def _sound_horizon_correction(self, z_start: float) -> float:
        if self.acoustic_zmax <= z_start:
            raise ValueError("acoustic_zmax doit dépasser le redshift de départ.")

        def integrand(z: float) -> float:
            cs = float(self.sound_speed(z))
            return cs * (
                1.0 / float(self.hubble(z)) - 1.0 / float(self.reference.hubble(z))
            )

        value, _ = quad(
            integrand,
            float(z_start),
            float(self.acoustic_zmax),
            epsabs=self.epsabs,
            epsrel=self.epsrel,
            limit=self.quad_limit,
        )
        return float(value)

    def rstar(self, mode: AcousticMode = "fixed") -> float:
        if mode == "fixed":
            return self.reference.rstar
        if mode == "corrected":
            return self.reference.rstar + self._sound_horizon_correction(self.reference.zstar)
        raise ValueError(f"Mode acoustique inconnu : {mode}")

    def rdrag(self, mode: AcousticMode = "fixed") -> float:
        if mode == "fixed":
            return self.reference.rdrag
        if mode == "corrected":
            return self.reference.rdrag + self._sound_horizon_correction(self.reference.zdrag)
        raise ValueError(f"Mode acoustique inconnu : {mode}")

    def theta_star(self, mode: AcousticMode = "fixed") -> float:
        return self.rstar(mode) / float(self.dm(self.reference.zstar))

    def bao_vector(
        self,
        redshifts: Iterable[float],
        kinds: Iterable[str],
        mode: AcousticMode = "fixed",
    ) -> np.ndarray:
        z = np.asarray(tuple(redshifts), dtype=float)
        kinds_tuple = tuple(kinds)
        if len(z) != len(kinds_tuple):
            raise ValueError("redshifts et kinds doivent avoir la même longueur.")
        rd = self.rdrag(mode)
        dm = np.asarray(self.dm(z), dtype=float)
        dh = np.asarray(self.dh(z), dtype=float)
        dv = np.cbrt(z * dm * dm * dh)
        out = np.empty(len(z), dtype=float)
        for i, kind in enumerate(kinds_tuple):
            if kind == "DV_over_rs":
                out[i] = dv[i] / rd
            elif kind == "DM_over_rs":
                out[i] = dm[i] / rd
            elif kind == "DH_over_rs":
                out[i] = dh[i] / rd
            else:
                raise ValueError(f"Quantité BAO inconnue : {kind}")
        return out

    def cmb_vector(self, mode: AcousticMode = "fixed") -> np.ndarray:
        return np.array(
            [
                self.theta_star(mode),
                self.reference.ombh2,
                self.reference.ombh2 + self.reference.omch2,
            ],
            dtype=float,
        )
