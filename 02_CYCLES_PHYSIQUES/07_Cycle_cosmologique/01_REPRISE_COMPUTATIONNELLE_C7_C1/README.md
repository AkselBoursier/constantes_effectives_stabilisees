# 01_REPRISE_COMPUTATIONNELLE_C7_C1

Reprise computationnelle du cycle cosmologique — lot C7-C1 :
comparaison commune `LambdaCDM` / CPL / `X(z)` sous la même vraisemblance
DESI DR2 BAO (13 composantes) et le même ancrage CMB comprimé.

## Gouvernance

```text
issue directrice : #63 (C7-C1) ;
provenance       : #60 — D9 ; #61 — A0–A5 ; #62 — P29 ;
archivage        : décision séparée #64 (rien d'initialisé ici) ;
branche          : comp/c7-c1-comparaison-commune ;
base             : origin/main = 5e088d1 (vérifié G1.0) ;
état G1          : G1.0, G1.2 et G1.3 validées ;
porte suivante   : G2.1 — validation de l'instrument numérique X(z),
                   ouverte dans #63 sur une branche distincte après merge.
```

Les huit chaînes G1.3 ont été produites hors Git. Elles ne sont ni suivies
ni distribuées dans cette PR.

## Portes (résumé de #63)

- G0 — provenance et spécification : **close et ratifiée** (G0.6) ;
- G1.0 — environnement, octets, configurations, tests de point :
  **validée** (commentaire G1.2 de #63) ;
- G1.2 — qualification de la vraisemblance commune : **validée**
  (commentaire G1.4 de #63 ; corrections documentaires en `1ee2b4c`) ;
- G1.3 — reproductions LambdaCDM et CPL sous la vraisemblance commune
  (8 chaînes convergées, T7 passé, minimisations multi-départs,
  contraste) : **validée** (commentaire G1.6 de #63 ;
  `reports/rapport_G1_3.md`) ;
- G2.0 — spécification de `X(z)` : **ratifiée** ;
- G2.1 — invariants et stabilité de `X(z)` : **ouverte pour tests seulement** ;
- G2.2 — pré-enregistrement des priors ; G2.3 — première inférence ;
- G3 — comparaison commune ; G4 — verdict.

## Interdits actifs

```text
données, chaînes, caches, environnements : hors Git ;
data_external : lecture seule, jamais suivi par Git ;
aucun chemin absolu local, secret ou jeton dans les fichiers suivis ;
aucune substitution de fichier voisin à un produit demandé ;
pas de qualification d'un meilleur point de profil de vraisemblance ;
pas de Wilks automatique pour le modèle spline ;
aucun MCMC X(z), aucune minimisation X(z et aucune inférence avant
validation humaine de G2.1 puis pré-enregistrement G2.2.
```

## Contenu

```text
configs/     — transcriptions LambdaCDM et CPL (+ copies officielles de
               référence dans configs/references/) ;
manifests/   — provenance, versions, tailles, SHA-256 ;
scripts/     — vraisemblances transcrites, acquisition et tests G1.0,
               contrôle BAO et repondération G1.2,
               analyse_g1_3.py, run_mcmc_g1_3.py et minimize_g1_3.py ;
reports/     — rapports G1.0, G1.2 et rapport_G1_3.md,
               jamais de chaînes brutes ;
requirements-c7c1.txt — gel de l'environnement isolé.
```

## Exécution des tests G1.0 (depuis cette racine)

```text
C7C1_DATA_DIR = répertoire local hors Git contenant desi_bao_dr2/ ;
python scripts/acquire_bao_data.py            # acquisition vérifiée
python scripts/test_points_g1_0.py configs/c7c1_lcdm_bao_cmbcomp.yaml <dir_chaine_officielle_base>
python scripts/test_points_g1_0.py configs/c7c1_cpl_bao_cmbcomp.yaml  <dir_chaine_officielle_base_w_wa>
```

Les répertoires de chaînes officielles restent sous `data_external/`
(lecture seule) et sont passés en argument à l'exécution.

## Prior CPL ratifié (G0.6)

```text
w0 ~ U[-3, 1] ; wa ~ U[-3, 2] ; w0 + wa < 0 (bloc prior explicite,
testé : un point violant est rejeté avec logprior = -inf).
```
