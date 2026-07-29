"""Acquisition contrôlée des octets BAO officiels — porte G1.0 (issue #63).

Télécharge les deux fichiers de la vraisemblance BAO DESI DR2 depuis le
dépôt officiel CobayaSampler/bao_data, épinglé au commit
bb0c1c9009dc76d1391300e169e8df38fd1096db, puis vérifie :

1. la taille exacte ;
2. le SHA-1 « git blob » annoncé par l'API GitHub pour ce commit ;
3. le SHA-256 attendu, consigné dans manifests/.

Toute discordance est un arrêt. La destination est hors Git, fournie par
la variable d'environnement C7C1_DATA_DIR (sous-répertoire desi_bao_dr2/).

Usage :
    python scripts/acquire_bao_data.py
"""

import hashlib
import os
import sys
import urllib.request

PIN = "bb0c1c9009dc76d1391300e169e8df38fd1096db"
BASE = f"https://raw.githubusercontent.com/CobayaSampler/bao_data/{PIN}/desi_bao_dr2"

EXPECTED = {
    "desi_gaussian_bao_ALL_GCcomb_mean.txt": {
        "size": 472,
        "git_blob_sha1": "8aff444fdb42c0946342aa0011ab287eda097c4c",
        "sha256": "9ac154ab583ce759c0f7eef3c978c7c70a6ead2d18774caceadf1a350a640585",
    },
    "desi_gaussian_bao_ALL_GCcomb_cov.txt": {
        "size": 2547,
        "git_blob_sha1": "fd8e5697ab61379b07b52efb781ea6713417a4d9",
        "sha256": "252a143274c8a07c78694c119617d36594f6d7965d00319ca611c6ffb886e509",
    },
}


def main():
    root = os.environ.get("C7C1_DATA_DIR")
    if not root:
        sys.exit("ARRET: C7C1_DATA_DIR non défini (destination hors Git requise).")
    dest = os.path.join(root, "desi_bao_dr2")
    os.makedirs(dest, exist_ok=True)

    for name, exp in EXPECTED.items():
        data = urllib.request.urlopen(f"{BASE}/{name}").read()
        if len(data) != exp["size"]:
            sys.exit(f"ARRET: taille inattendue pour {name}: {len(data)}")
        blob = hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()
        if blob != exp["git_blob_sha1"]:
            sys.exit(f"ARRET: git blob SHA-1 inattendu pour {name}: {blob}")
        sha256 = hashlib.sha256(data).hexdigest()
        if sha256 != exp["sha256"]:
            sys.exit(f"ARRET: SHA-256 inattendu pour {name}: {sha256}")
        with open(os.path.join(dest, name), "wb") as f:
            f.write(data)
        print(f"OK {name}  {len(data)} octets  sha256={sha256}")

    print("Acquisition vérifiée : octets identiques au commit épinglé.")


if __name__ == "__main__":
    main()
