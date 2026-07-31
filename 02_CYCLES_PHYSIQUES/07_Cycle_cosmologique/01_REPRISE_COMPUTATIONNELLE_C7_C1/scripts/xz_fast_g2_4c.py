"""Implémentation optimisée O1+O3 de l'évaluation X(z) — porte G2.4c-ii.

CANDIDATE À QUALIFIER contre l'oracle G2.1/G2.3 (`xz_background_g2_1` +
`xz_likelihood_g2_3`), qui reste la référence intouchée. Aucun émulateur,
aucune interpolation de r_drag/r_star/theta_star ou d'une sortie CAMB,
aucune approximation acoustique, aucune table précalculée sur les
paramètres : uniquement des identités algébriques et une quadrature
numérique fixe par lots, qualifiée comme nouvelle implémentation.

O1 — séparation lente/rapide :
  ReferenceLenteXZ (cobaya Theory) dépend exclusivement de H0, ombh2,
  omm et fournit un état lent immuable (produit « etat_lent_xz ») ;
  VraisemblanceRapideXZ (cobaya Likelihood) dépend des seuls X_i et
  consomme l'état via le mécanisme officiel provider/get_result.

O3 — quadrature par lots et cumulative :
  redshifts requis triés ; scission aux nœuds de spline, à z=2.33,
  et (en queue, variable u = 1/sqrt(1+z)) à zstar/zdrag et aux bornes
  acoustiques prédéclarées ; chaque segment commun intégré une seule
  fois ; H_ref et X(z) évalués en tableaux ; cumuls partagés pour tous
  les D_M BAO ; D_M(zstar) = D_M(2.33) + queue(X(2.33)) ; segments
  communs de r_drag / r_star partagés. Pour z >= 2.33, seule l'identité
  pré-enregistrée X(z) = X(2.33) est exploitée : la dépendance rapide de
  la queue passe uniquement par la dernière amplitude nodale.

État lent : valeurs exactes (H0, ombh2, omm), CambReference, identité
variante/convention/descripteur, grilles/poids/structures de quadrature
dépendant du fond, empreinte déterministe. Clés de cache = valeurs
complètes (aucun arrondi, aucun hachage tronqué). Une construction ayant
levé une exception n'entre jamais dans le cache. Les tableaux de l'état
sont verrouillés en écriture.

Le paramètre test-only ``sabotage`` (jamais utilisé par les composants
Cobaya) sert exclusivement aux fautes injectées de la qualification.
"""

from __future__ import annotations

import math
from collections import OrderedDict
from dataclasses import dataclass, field
from typing import Any

import numpy as np

from xz_background_g2_1 import (
    ACOUSTIC_RULES,
    C_KM_S,
    NODES,
    CambReference,
    XZProfile,
    resolve_acoustic_mode,
)
from xz_likelihood_g2_3 import (
    BAO_KINDS,
    BAO_REDSHIFTS,
    CMB_ICOV,
    CMB_MU,
    PRIOR_X,
    PRIORS_FOND,
    PARAMETRES_FIXES,
    VARIANTES,
    load_config,
)

# Ordres de quadrature retenus par l'étude de convergence prédéclarée
# {512, 1024, 2048, 4096} (suite en puissances de deux) de
# qualify_xz_optim_g2_4c.py — intervalles de Simpson composite par
# segment, globaux par classe d'intégrale, jamais ajustés point par
# point. Le choix Simpson (plutôt que Gauss-Legendre) est imposé par les
# plis C² internes de l'interpolant CAMB de H_ref, qui plafonnent la
# convergence spectrale ; c'est la voie déjà validée par I8 (G2.1).
ORDRES_RETENUS = {"principal": 2048, "queue": 2048}

# Corrections acoustiques : PAS de nouvelle quadrature — réutilisation
# bit à bit de la méthode de l'oracle (scipy.integrate.quad, mêmes
# tolérances et même intégrande scalaire), sous les règles de mode de
# l'amendement A1 (ACOUSTIC_RULES de xz_background_g2_1, source unique).
# Mode directeur aligné sur l'oracle : « corrected » -> corrected-v1.1
# (epsabs=1e-15, epsrel=1e-13, limit=800). Le mode corrected-legacy
# reste sélectionnable EXCLUSIVEMENT pour les tests de régression bit à
# bit contre l'ancien oracle — jamais par les composants Cobaya.
MODE_ACOUSTIQUE_DIRECTEUR = "corrected-v1.1"
Z_MAX_ACOUSTIQUE = 1.0e7
Z_RACCORD = 2.33

# Grille de contrôle de validité du fond sur [0, 2.33] (déterministe).
GRILLE_CONTROLE = np.linspace(0.0, Z_RACCORD, 2049)


class GardeIdentiteErreur(RuntimeError):
    """L'état lent ne correspond pas au fond/à la variante demandés."""


class _FondInvalide(Exception):
    """H_X² non fini ou <= 0 rencontré par une quadrature répliquée
    (même sémantique et même ordre de détection que l'oracle)."""


def _gauss_legendre(a: float, b: float, ordre: int) -> tuple[np.ndarray, np.ndarray]:
    x, w = np.polynomial.legendre.leggauss(ordre)
    milieu, demi = 0.5 * (a + b), 0.5 * (b - a)
    return milieu + demi * x, demi * w


def fabrique_eval_spline(spline):
    """Fermeture d'évaluation scalaire d'une CubicSpline, bit à bit
    identique à ``float(spline(zz))`` : mêmes coefficients et MÊME ordre
    d'accumulation que scipy PPoly (_ppoly.evaluate_poly1 :
    res = c3 + c2·t + c1·t² + c0·t³, accumulé à gauche, puissances par
    multiplications successives). Python pur (listes + bisect) pour la
    vitesse. L'égalité bitwise est vérifiée de façon bloquante par la
    qualification sur une grille dense."""
    import bisect

    xs = spline.x.tolist()
    c0 = spline.c[0].tolist()
    c1 = spline.c[1].tolist()
    c2 = spline.c[2].tolist()
    c3 = spline.c[3].tolist()
    n_max = len(xs) - 2

    def evaluer(zz: float) -> float:
        i = bisect.bisect_right(xs, zz) - 1
        if i < 0:
            i = 0
        elif i > n_max:
            i = n_max
        t = zz - xs[i]
        z2 = t * t
        z3 = z2 * t
        return ((c3[i] + c2[i] * t) + c1[i] * z2) + c0[i] * z3

    return evaluer


def _simpson(a: float, b: float, n_intervalles: int) -> tuple[np.ndarray, np.ndarray]:
    """Abscisses et poids de Simpson composite sur [a, b]
    (n_intervalles pair)."""
    if n_intervalles % 2:
        n_intervalles += 1
    x = np.linspace(a, b, n_intervalles + 1)
    pas = (b - a) / n_intervalles
    w = np.full(n_intervalles + 1, 2.0)
    w[1::2] = 4.0
    w[0] = w[-1] = 1.0
    return x, w * pas / 3.0


@dataclass(frozen=True)
class EtatLent:
    """État lent immuable : tout ce qui ne dépend que de (H0, ombh2, omm)
    — plus l'identité de la variante et les structures de quadrature."""

    h0: float
    ombh2: float
    omm: float
    omch2: float
    variante: str
    convention: str
    empreinte: tuple
    reference: CambReference
    c0: float                    # H0^2 * Omega_X,0
    # segments principaux [0, 2.33] : bornes, abscisses/poids aplatis,
    # index de fin par segment, H_ref^2 aux abscisses,
    # index de borne pour chaque z BAO et pour 2.33
    bornes_principales: np.ndarray
    z_gl: np.ndarray
    w_gl: np.ndarray
    fin_segment: np.ndarray
    h2_ref_gl: np.ndarray
    index_borne_bao: np.ndarray
    index_borne_2p33: int
    # queue D_M [2.33, zstar] en u : poids (jacobien inclus) et H_ref^2
    w_queue: np.ndarray
    h2_ref_queue: np.ndarray
    # BAO ponctuel
    h2_ref_bao: np.ndarray

    def verifier(self, variante: str, convention: str,
                 h0: float, ombh2: float, omm: float) -> None:
        attendu = (variante, convention, float(h0), float(ombh2), float(omm))
        if self.empreinte != attendu:
            raise GardeIdentiteErreur(
                f"état lent {self.empreinte} != demandé {attendu}"
            )


def cle_etat(variante: str, convention: str,
             h0: float, ombh2: float, omm: float) -> tuple:
    """Clé de cache : valeurs complètes, sans arrondi ni hachage tronqué."""
    return (variante, convention, float(h0), float(ombh2), float(omm))


def construire_etat_lent(
    variante: str,
    h0: float,
    ombh2: float,
    omm: float,
    ordres: dict[str, int] | None = None,
    sabotage: frozenset = frozenset(),
) -> EtatLent:
    ordres = dict(ORDRES_RETENUS, **(ordres or {}))
    grille, convention = VARIANTES[variante]
    reference = CambReference.from_g1(h0=h0, ombh2=ombh2, omegam=omm)
    c0 = reference.h0**2 * reference.omega_x0

    # --- segments principaux [0, 2.33] --------------------------------
    bornes = sorted(
        {0.0, Z_RACCORD}
        | {float(z) for z in NODES[grille]}
        | {float(z) for z in np.unique(BAO_REDSHIFTS)}
    )
    if "segment_2p33_omis" in sabotage:
        # FAUTE INJECTABLE (test uniquement) : scission à z=2.33 omise —
        # la construction DOIT refuser (l'index de borne 2.33 est requis
        # par la structure cumulée).
        bornes = [b for b in bornes if abs(b - Z_RACCORD) > 1e-12]
    bornes = np.array(bornes)
    z_par_seg, w_par_seg, fins = [], [], []
    total = 0
    for a, b in zip(bornes[:-1], bornes[1:]):
        zg, wg = _simpson(float(a), float(b), ordres["principal"])
        z_par_seg.append(zg)
        w_par_seg.append(wg)
        total += len(zg)
        fins.append(total)
    z_gl = np.concatenate(z_par_seg)
    w_gl = np.concatenate(w_par_seg)
    h_ref_gl = np.asarray(reference.hubble(z_gl), dtype=float)
    index_borne_bao = np.array(
        [int(np.flatnonzero(np.isclose(bornes, z, rtol=0, atol=1e-12))[0])
         for z in BAO_REDSHIFTS]
    )
    index_borne_2p33 = int(
        np.flatnonzero(np.isclose(bornes, Z_RACCORD, rtol=0, atol=1e-12))[0]
    )

    # --- queue D_M [2.33, zstar] en u = 1/sqrt(1+z) --------------------
    u_star = 1.0 / math.sqrt(1.0 + reference.zstar)
    u_2p33 = 1.0 / math.sqrt(1.0 + Z_RACCORD)
    u_q, w_q = _simpson(u_star, u_2p33, ordres["queue"])
    z_q = 1.0 / (u_q * u_q) - 1.0
    w_queue = w_q * 2.0 * C_KM_S / u_q**3
    h2_ref_queue = np.asarray(reference.hubble(z_q), dtype=float) ** 2

    h2_ref_bao = np.asarray(reference.hubble(BAO_REDSHIFTS), dtype=float) ** 2

    omch2 = omm * (h0 / 100.0) ** 2 - PARAMETRES_FIXES["mnu"] / 93.14 - ombh2
    etat = EtatLent(
        h0=float(h0), ombh2=float(ombh2), omm=float(omm), omch2=float(omch2),
        variante=variante, convention=convention,
        empreinte=cle_etat(variante, convention, h0, ombh2, omm),
        reference=reference, c0=float(c0),
        bornes_principales=bornes, z_gl=z_gl, w_gl=w_gl,
        fin_segment=np.array(fins), h2_ref_gl=h_ref_gl**2,
        index_borne_bao=index_borne_bao, index_borne_2p33=index_borne_2p33,
        w_queue=w_queue, h2_ref_queue=h2_ref_queue,
        h2_ref_bao=h2_ref_bao,
    )
    for tableau in (etat.bornes_principales, etat.z_gl, etat.w_gl,
                    etat.fin_segment, etat.h2_ref_gl, etat.index_borne_bao,
                    etat.w_queue, etat.h2_ref_queue, etat.h2_ref_bao):
        tableau.setflags(write=False)
    return etat


class FabriqueEtatsLents:
    """Cache exact borné (FIFO) d'états lents. Clé = valeurs complètes.
    Une construction qui lève une exception n'est jamais insérée."""

    def __init__(self, borne: int = 8, ordres: dict[str, int] | None = None,
                 sabotage: frozenset = frozenset()):
        self._borne = borne
        self._ordres = ordres
        self._sabotage = sabotage
        self._cache: OrderedDict[tuple, EtatLent] = OrderedDict()

    def obtenir(self, variante: str, h0: float, ombh2: float, omm: float) -> EtatLent:
        grille, convention = VARIANTES[variante]
        if "cache_partage_variantes" in self._sabotage:
            cle = ("PARTAGE", float(h0), float(ombh2), float(omm))
        elif "collision_cle" in self._sabotage:
            cle = ("COLLISION",)
        else:
            cle = cle_etat(variante, convention, h0, ombh2, omm)
        if "cache_desactive" not in self._sabotage and cle in self._cache:
            self._cache.move_to_end(cle)
            return self._cache[cle]
        etat = construire_etat_lent(
            variante, h0, ombh2, omm, ordres=self._ordres,
            sabotage=self._sabotage,
        )
        if len(self._cache) >= self._borne:
            self._cache.popitem(last=False)
        self._cache[cle] = etat
        return etat

    @property
    def taille(self) -> int:
        return len(self._cache)

    def memoire_octets(self) -> int:
        total = 0
        for etat in self._cache.values():
            for tableau in (etat.z_gl, etat.w_gl, etat.h2_ref_gl,
                            etat.w_queue, etat.h2_ref_queue,
                            etat.h2_ref_bao):
                total += tableau.nbytes
        return total


# ------------------------------------------------------------ évaluation

def _dans_support(h0, ombh2, omm, xs) -> bool:
    return bool(
        PRIORS_FOND["H0"]["min"] <= h0 <= PRIORS_FOND["H0"]["max"]
        and PRIORS_FOND["ombh2"]["min"] <= ombh2 <= PRIORS_FOND["ombh2"]["max"]
        and PRIORS_FOND["omm"]["min"] <= omm <= PRIORS_FOND["omm"]["max"]
        and all(PRIOR_X["min"] <= x <= PRIOR_X["max"] for x in xs)
    )


class EvaluateurRapide:
    """Évaluation complète d'un point, algébriquement identique à
    l'oracle XZEvaluator, via un état lent + le chemin rapide O3.
    Sortie : même structure que l'oracle (logprior, chi2, vecteurs,
    contraintes)."""

    def __init__(self, config: dict[str, Any], bao_mean: np.ndarray,
                 bao_icov: np.ndarray, fabrique: FabriqueEtatsLents,
                 sabotage: frozenset = frozenset(),
                 mode_acoustique: str = MODE_ACOUSTIQUE_DIRECTEUR):
        self.config = config
        self.variante = config["variante"]
        self.grille, self.convention = VARIANTES[self.variante]
        self.noms_x = [item["nom"] for item in config["parametres_x"]]
        self.bao_mean = bao_mean
        self.bao_icov = bao_icov
        self.fabrique = fabrique
        self.sabotage = sabotage
        # Mode acoustique RÉSOLU (amendement A1) : corrected-v1.1 par
        # défaut (directeur) ; corrected-legacy réservé aux tests de
        # régression bit à bit ; « fixed » n'est pas un mode de ce
        # pipeline (l'oracle XZEvaluator évalue en « corrected »).
        self.mode_acoustique = resolve_acoustic_mode(mode_acoustique)
        if self.mode_acoustique == "fixed":
            raise ValueError(
                "EvaluateurRapide réplique le pipeline « corrected » de "
                "l'oracle ; le mode fixed n'y est pas défini."
            )

    # ---- chemin rapide (dépend des X_i, état lent fourni) -------------
    def _dm_bao_replique_oracle(self, etat: EtatLent,
                                profil: XZProfile) -> np.ndarray:
        """D_M aux 13 z BAO : réplique bit à bit de XZBackground.dm
        (un quad par z UNIQUE, mêmes tolérances et points de scission,
        cache par z comme l'oracle), intégrande réécrite vite."""
        from scipy.integrate import quad

        eval_x = fabrique_eval_spline(profil._spline)
        derniere = float(profil.last_value)
        c0 = etat.c0
        hub = etat.reference.hubble

        def integrande(zz: float) -> float:
            x = derniere if zz >= Z_RACCORD else eval_x(zz)
            href = float(hub(zz))
            h2x = href * href + c0 * (x - 1.0)
            if not math.isfinite(h2x) or h2x <= 0.0:
                raise _FondInvalide()
            return C_KM_S / math.sqrt(h2x)

        cache: dict[float, float] = {}
        valeurs = np.empty(len(BAO_REDSHIFTS))
        noeuds = profil.nodes
        for i, z in enumerate(BAO_REDSHIFTS):
            cle = float(z)
            if cle not in cache:
                points = [p for p in noeuds[1:] if 0.0 < p < cle]
                valeur, _ = quad(
                    integrande, 0.0, cle,
                    epsabs=1e-8, epsrel=1e-10, limit=300, points=points,
                )
                cache[cle] = float(valeur)
            valeurs[i] = cache[cle]
        return valeurs

    def verif_simpson(self, etat: EtatLent, profil: XZProfile) -> dict:
        """Contre-contrôle O3 : D_M par lots Simpson cumulatif (état
        lent), comparé aux répliques oracle — utilisé par l'étude de
        convergence de la qualification, hors chemin de production."""
        x_gl = np.asarray(profil(etat.z_gl), dtype=float)
        h2x = etat.h2_ref_gl + etat.c0 * (x_gl - 1.0)
        if not np.all(np.isfinite(h2x)) or np.any(h2x <= 0.0):
            raise _FondInvalide()
        contributions = C_KM_S * etat.w_gl / np.sqrt(h2x)
        cumuls = np.concatenate(
            [[0.0], np.cumsum(np.add.reduceat(
                contributions,
                np.concatenate([[0], etat.fin_segment[:-1]])))]
        )
        dm_bao_simpson = cumuls[etat.index_borne_bao]
        x5 = float(profil.last_value)
        hx_queue = np.sqrt(etat.h2_ref_queue + etat.c0 * (x5 - 1.0))
        queue_simpson = float(np.sum(etat.w_queue / hx_queue))
        return {"dm_bao": dm_bao_simpson,
                "dm_2p33": float(cumuls[etat.index_borne_2p33]),
                "queue": queue_simpson}

    def _dm_star_replique_oracle(self, etat: EtatLent,
                                 profil: XZProfile) -> float:
        """D_M(z_star) : réplique BIT À BIT de XZBackground._dm_scalar
        (même scipy.quad, mêmes tolérances, mêmes points de scission,
        intégrande aux valeurs strictement identiques) — l'intégrande est
        seulement RÉÉCRITE plus vite (appels scalaires directs à la même
        spline et à la même référence CAMB). Motif : theta_star doit être
        identique à l'oracle pour que les seuils absolus de chi2_CMB
        restent exigibles quel que soit le résidu (le remplacement par
        une quadrature propre laisse sinon un plancher ~bruit quad de
        l'oracle, amplifié par les grands résidus — constat au rapport).
        """
        from scipy.integrate import quad

        reference = etat.reference
        eval_x = fabrique_eval_spline(profil._spline)
        derniere = float(profil.last_value)
        c0 = etat.c0
        hub = reference.hubble

        def integrande(zz: float) -> float:
            x = derniere if zz >= Z_RACCORD else eval_x(zz)
            href = float(hub(zz))
            h2x = href * href + c0 * (x - 1.0)
            if not math.isfinite(h2x) or h2x <= 0.0:
                raise _FondInvalide()
            return C_KM_S / math.sqrt(h2x)

        borne = Z_RACCORD if "queue_dm_omise" in self.sabotage \
            else float(reference.zstar)
        valeur, _ = quad(
            integrande, 0.0, borne,
            epsabs=1e-8, epsrel=1e-10, limit=300,
            points=[p for p in profil.nodes[1:] if 0.0 < p < borne],
        )
        return float(valeur)

    def _correction_acoustique(self, etat: EtatLent, x5: float) -> tuple[float, float]:
        """(correction_rdrag, correction_rstar).

        Réplique BIT À BIT la méthode de l'oracle
        (XZBackground._sound_horizon_correction) : même scipy.quad, même
        intégrande scalaire, et les tolérances du MODE ACOUSTIQUE RÉSOLU
        de l'évaluateur (ACOUSTIC_RULES — amendement A1 ; source unique
        partagée avec l'oracle). Pour z >= 2.33, X(z) = X(2.33) rend
        l'intégrande identique à celle de l'oracle avec
        H_X² = H_ref² + c0·(x5-1). Aucune nouvelle quadrature ici.
        """
        if "queue_acoustique_omise" in self.sabotage:
            return 0.0, 0.0
        from scipy.integrate import quad

        regle = ACOUSTIC_RULES[self.mode_acoustique]
        reference = etat.reference
        ratio0 = reference.baryon_photon_ratio0
        delta = etat.c0 * (x5 - 1.0)

        def integrande(z: float) -> float:
            # ordre des opérations identique à XZBackground.sound_speed
            # puis à h2/hubble (associativité flottante préservée).
            ratio = ratio0 / (1.0 + z)
            cs = C_KM_S / math.sqrt(3.0 * (1.0 + 0.75 * ratio))
            href = float(reference.hubble(z))
            h2x = href * href + delta
            if not math.isfinite(h2x) or h2x <= 0.0:
                raise _FondInvalide()
            hx = math.sqrt(h2x)
            return cs * (1.0 / hx - 1.0 / href)

        corrections = []
        for z_depart in (reference.zdrag, reference.zstar):
            valeur, _ = quad(
                integrande, float(z_depart), Z_MAX_ACOUSTIQUE,
                epsabs=regle["epsabs"], epsrel=regle["epsrel"],
                limit=int(regle["limit"]),
            )
            corrections.append(float(valeur))
        return corrections[0], corrections[1]

    def evaluer_avec_etat(self, etat: EtatLent, xs: list[float]) -> dict[str, Any]:
        etat.verifier(self.variante, self.convention,
                      etat.h0, etat.ombh2, etat.omm)
        if etat.variante != self.variante or etat.convention != self.convention:
            raise GardeIdentiteErreur(
                f"état {etat.variante}/{etat.convention} pour évaluateur "
                f"{self.variante}/{self.convention}"
            )
        profil = XZProfile(self.grille, tuple(xs), self.convention)
        statut = {
            "dans_support_uniforme": _dans_support(
                etat.h0, etat.ombh2, etat.omm, xs),
            "omch2_positive": bool(etat.omch2 > 0.0),
            "fond_valide": None,
        }
        resultat: dict[str, Any] = {
            "variante": self.variante,
            "point": {"H0": etat.h0, "ombh2": etat.ombh2, "omm": etat.omm,
                      **dict(zip(self.noms_x, map(float, xs)))},
            "omch2": etat.omch2,
            "logprior": None, "chi2_BAO": None, "chi2_CMB": None,
            "chi2_total": None, "vecteur_BAO": None, "vecteur_CMB": None,
            "contraintes": statut,
        }
        if not statut["dans_support_uniforme"] or not statut["omch2_positive"]:
            resultat["logprior"] = -math.inf
            return resultat
        # Pipeline RÉPLIQUE ORACLE : mêmes quadratures scipy.quad (mêmes
        # tolérances, mêmes points de scission, intégrandes aux valeurs
        # bit à bit identiques mais réécrites vite), même ORDRE
        # d'évaluation que XZEvaluator/XZBackground — y compris la
        # sémantique d'invalidité (exception à la première quadrature qui
        # rencontre H_X² <= 0). Toutes les sorties publiées sont donc
        # identiques à l'oracle au bit près ; le calcul par lots Simpson
        # (O3) sert de contre-contrôle de qualification (verif_simpson).
        x5 = float(profil.last_value)
        try:
            # 1) rdrag corrigé (comme oracle bao_vector -> rdrag)
            corr_drag, corr_star = self._correction_acoustique(etat, x5)
            rdrag = etat.reference.rdrag + corr_drag
            rstar = etat.reference.rstar + corr_star
            # 2) D_M aux z BAO (quads répliqués, uniques mis en cache)
            dm_bao = self._dm_bao_replique_oracle(etat, profil)
            # 3) D_H vectoriel (mêmes opérations que l'oracle)
            h2_bao = (etat.h2_ref_bao
                      + etat.c0
                      * (np.asarray(profil(BAO_REDSHIFTS), dtype=float) - 1.0))
            if np.any(~np.isfinite(h2_bao)) or np.any(h2_bao <= 0.0):
                raise _FondInvalide()
            dh_bao = C_KM_S / np.sqrt(h2_bao)
            # 4) D_M(z_star) (quad répliqué)
            dm_star = self._dm_star_replique_oracle(etat, profil)
        except _FondInvalide:
            if "classification_sans_grille" in self.sabotage:
                # FAUTE INJECTABLE : invalidité ignorée (divergence de
                # classification, à détecter par la qualification).
                statut["fond_valide"] = True
                resultat["logprior"] = 0.0
                return resultat
            statut["fond_valide"] = False
            resultat["logprior"] = -math.inf
            return resultat
        statut["fond_valide"] = True

        dv = np.cbrt(BAO_REDSHIFTS * dm_bao * dm_bao * dh_bao)
        bao = np.empty(len(BAO_REDSHIFTS))
        for i, kind in enumerate(BAO_KINDS):
            if kind == "DM_over_rs":
                bao[i] = dm_bao[i] / rdrag
            elif kind == "DH_over_rs":
                bao[i] = dh_bao[i] / rdrag
            else:
                bao[i] = dv[i] / rdrag
        theta = rstar / dm_star
        cmb = np.array([theta, etat.ombh2, etat.ombh2 + etat.omch2])
        r_bao = bao - self.bao_mean
        r_cmb = cmb - CMB_MU
        chi2_bao = float(r_bao @ self.bao_icov @ r_bao)
        chi2_cmb = float(r_cmb @ CMB_ICOV @ r_cmb)
        resultat.update(
            logprior=0.0, chi2_BAO=chi2_bao, chi2_CMB=chi2_cmb,
            chi2_total=chi2_bao + chi2_cmb,
            vecteur_BAO=[float(v) for v in bao],
            vecteur_CMB=[float(v) for v in cmb],
        )
        resultat["_interne"] = {
            "dm_bao": dm_bao, "dm_star": dm_star, "rdrag": rdrag,
            "rstar": rstar, "corr_drag": corr_drag, "corr_star": corr_star,
            "h_bao": np.sqrt(h2_bao),
        }
        return resultat

    def evaluate(self, point: dict[str, float]) -> dict[str, Any]:
        h0, ombh2, omm = (float(point["H0"]), float(point["ombh2"]),
                          float(point["omm"]))
        xs = [float(point[nom]) for nom in self.noms_x]
        omch2 = omm * (h0 / 100.0) ** 2 - PARAMETRES_FIXES["mnu"] / 93.14 - ombh2
        if not _dans_support(h0, ombh2, omm, xs) or not omch2 > 0.0:
            # aucun état lent construit hors support (identique à l'oracle)
            return {
                "variante": self.variante,
                "point": {"H0": h0, "ombh2": ombh2, "omm": omm,
                          **dict(zip(self.noms_x, xs))},
                "omch2": omch2, "logprior": -math.inf,
                "chi2_BAO": None, "chi2_CMB": None, "chi2_total": None,
                "vecteur_BAO": None, "vecteur_CMB": None,
                "contraintes": {
                    "dans_support_uniforme": _dans_support(h0, ombh2, omm, xs),
                    "omch2_positive": bool(omch2 > 0.0),
                    "fond_valide": None,
                },
            }
        etat = self.fabrique.obtenir(self.variante, h0, ombh2, omm)
        etat.verifier(self.variante, self.convention, h0, ombh2, omm)
        return self.evaluer_avec_etat(etat, xs)


# ------------------------------------------------------ composants Cobaya

try:
    from cobaya.likelihood import Likelihood
    from cobaya.theory import Theory
except ImportError:  # profil analytique sans cobaya
    Likelihood = object  # type: ignore
    Theory = object  # type: ignore


class ReferenceLenteXZ(Theory):
    """Théorie lente : dépend exclusivement de H0, ombh2, omm ;
    fournit le produit « etat_lent_xz »."""

    descripteur: str = ""

    def initialize(self):
        self._config = load_config(self.descripteur)
        self._variante = self._config["variante"]
        self._fabrique = FabriqueEtatsLents(borne=8)
        self.set_cache_size(8)

    def get_can_provide(self):
        return ["etat_lent_xz"]

    def calculate(self, state, want_derived=True, **params):
        state["etat_lent_xz"] = self._fabrique.obtenir(
            self._variante, params["H0"], params["ombh2"], params["omm"]
        )

    def get_result(self, result_name, **kwargs):
        return self.current_state[result_name]


class VraisemblanceRapideXZ(Likelihood):
    """Vraisemblance rapide : dépend directement des seuls X_i ;
    consomme l'état lent via le provider officiel."""

    descripteur: str = ""

    def initialize(self):
        from xz_likelihood_g2_3 import load_bao_data

        self._config = load_config(self.descripteur)
        self._variante = self._config["variante"]
        bao_mean, bao_icov = load_bao_data()
        self._evaluateur = EvaluateurRapide(
            self._config, bao_mean, bao_icov,
            fabrique=None,  # jamais utilisé : l'état vient du provider
        )
        self._noms_x = [item["nom"] for item in self._config["parametres_x"]]

    def get_requirements(self):
        return {"etat_lent_xz": None}

    def logp(self, _derived=None, **valeurs):
        etat: EtatLent = self.provider.get_result("etat_lent_xz")
        xs = [float(valeurs[nom]) for nom in self._noms_x]
        sortie = self._evaluateur.evaluer_avec_etat(etat, xs)
        if _derived is not None:
            for nom in ("chi2_BAO", "chi2_CMB", "chi2_total"):
                _derived[nom] = (
                    np.nan if sortie[nom] is None else sortie[nom]
                )
        if sortie["logprior"] == -math.inf:
            return -np.inf
        return -0.5 * sortie["chi2_total"]


def build_info_optimisee(descripteur: str, graine: int) -> dict[str, Any]:
    """Information Cobaya O1+O3 : mêmes paramètres, priors, refs,
    propositions et bloc sampler que l'adaptateur G2.4b — seule
    l'organisation likelihood/theory change."""
    import copy

    from xz_cobaya_g2_4 import (
        PROPOSAL_FOND,
        PROPOSAL_X,
        REF_FOND,
        REF_X,
        SAMPLER_G1,
        _LAMBDA_OMCH2,
    )

    config = load_config(descripteur)
    noms_x = [item["nom"] for item in config["parametres_x"]]
    params: dict[str, Any] = {
        "H0": {"prior": {"min": 20.0, "max": 100.0},
               "ref": dict(REF_FOND["H0"]), "proposal": PROPOSAL_FOND["H0"],
               "latex": "H_0"},
        "ombh2": {"prior": {"min": 0.005, "max": 0.1},
                  "ref": dict(REF_FOND["ombh2"]),
                  "proposal": PROPOSAL_FOND["ombh2"],
                  "latex": r"\Omega_\mathrm{b} h^2"},
        "omm": {"prior": {"min": 0.01, "max": 0.99},
                "ref": dict(REF_FOND["omm"]), "proposal": PROPOSAL_FOND["omm"],
                "latex": r"\Omega_\mathrm{m}"},
    }
    for nom in noms_x:
        params[nom] = {"prior": {"min": -2.0, "max": 4.0},
                       "ref": dict(REF_X), "proposal": PROPOSAL_X,
                       "latex": nom}
    params["omch2"] = {"derived": _LAMBDA_OMCH2,
                       "latex": r"\Omega_\mathrm{c} h^2"}
    for nom in ("chi2_BAO", "chi2_CMB", "chi2_total"):
        params[nom] = {"derived": True}
    sampler = copy.deepcopy(SAMPLER_G1)
    sampler["mcmc"]["seed"] = int(graine)
    mnu = PARAMETRES_FIXES["mnu"]
    return {
        "params": params,
        "theory": {
            "reference_lente_xz": {
                "external": ReferenceLenteXZ,
                "input_params": ["H0", "ombh2", "omm"],
                "descripteur": descripteur,
            }
        },
        "likelihood": {
            "xz_rapide": {
                "external": VraisemblanceRapideXZ,
                "input_params": list(noms_x),
                "output_params": ["chi2_BAO", "chi2_CMB", "chi2_total"],
                "descripteur": descripteur,
            }
        },
        "prior": {
            "omch2_positif": (
                f"lambda omm, H0, ombh2: 0.0 if "
                f"(omm*(H0/100)**2 - {mnu}/93.14 - ombh2) > 0.0 else -np.inf"
            )
        },
        "sampler": sampler,
    }
