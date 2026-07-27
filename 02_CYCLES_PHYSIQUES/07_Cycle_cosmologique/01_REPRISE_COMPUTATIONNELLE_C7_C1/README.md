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
porte courante   : G1.2 — qualification de la vraisemblance commune.
                   AUCUN échantillonnage.
```

## Portes (résumé de #63)

- G0 — provenance et spécification : **close et ratifiée** (G0.6) ;
- G1.0 — environnement, octets, configurations, tests de point :
  **validée** (commentaire G1.2 de #63) ;
- G1.2 — qualification de la vraisemblance commune (repondération CMB
  publique, contrôle BAO stock, prior joint, tolérances) : **exécutée,
  rapport soumis à validation humaine** (`reports/rapport_G1_2.md`) ;
- G1 — contrôles officiels (reproduction LambdaCDM et CPL) : non ouverte ;
- G2 — validation de X(z) ; G3 — comparaison commune ; G4 — verdict.

## Interdits actifs

```text
aucune chaîne MCMC avant validation humaine du rapport G1.0 ;
données, chaînes, caches, environnements : hors Git ;
data_external : lecture seule, jamais suivi par Git ;
aucun chemin absolu local, secret ou jeton dans les fichiers suivis ;
aucune substitution de fichier voisin à un produit demandé ;
pas de qualification d'un meilleur point de profil de vraisemblance ;
pas de Wilks automatique pour le modèle spline.
```

## Contenu

```text
configs/     — transcriptions LambdaCDM et CPL (+ copies officielles de
               référence dans configs/references/) ;
manifests/   — provenance, versions, tailles, SHA-256 ;
scripts/     — vraisemblances transcrites, acquisition vérifiée des
               octets BAO, tests de point G1.0 ;
reports/     — comptes rendus légers (jamais de chaînes brutes) ;
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
