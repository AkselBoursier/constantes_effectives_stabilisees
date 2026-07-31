# Synthèse exécutive de l’environnement local

**État consolidé au 30 juillet 2026 — machine `DESKTOP-94HCGG9`**

Ce document est la fiche de référence unique à fournir à tout agent appelé à travailler localement avec Codex, Claude Code, ChatGPT, un MCP filesystem, VS Code ou une session distante. Il remplace, pour l’orientation courante, la lecture préalable de tous les rapports d’audit. Les rapports sources restent conservés pour les preuves, détails et procédures de restauration.

## Résumé décisionnel

- Le moteur scientifique canonique est **Ubuntu 22.04 sous WSL**, avec l’environnement Python isolé `/home/akselboursier/.venvs/cosmo-mcmc`.
- L’unique clone CLASS canonique est `/home/akselboursier/class_public`, compilé et relié à Cobaya.
- Pour les calculs scientifiques Windows qui ne nécessitent pas WSL, utiliser explicitement Python 3.11 : `C:\Program Files\Python311\python.exe`. Ne pas employer le `python` par défaut sans vérifier sa version : il pointe actuellement vers Python 3.14, moins complet.
- Julia n’est volontairement pas globale. La reproduction ALPHA/QCD possède son runtime Julia 1.11.5 figé et son propre dépôt de paquets ; il faut utiliser le lanceur dédié.
- Pour 32 chaînes MCMC, exécuter de préférence **4 chaînes simultanées**, éventuellement 8 après mesure, avec toutes les bibliothèques numériques limitées à un thread. Ne pas lancer 32 processus actifs simultanément sur cette machine.
- L’espace libre est passé de **17,47 Gio à 98,21 Gio**, soit un gain net observé d’environ **80,74 Gio** entre les relevés extrêmes. Une partie provient de suppressions précisément mesurées et une autre de la déshydratation OneDrive et des changements intervenus entre redémarrages.
- OneDrive reste provisoirement la racine de plusieurs projets, mais ses fichiers à la demande compliquent les parcours MCP et les hachages. La cible adoptée est un stockage local ordinaire sur SSD, sauvegardé par **restic vers Backblaze B2**.
- Docker, CUDA, un SDK .NET et une Julia globale ne doivent pas être installés sans cas d’usage explicite. Ils ne sont pas requis par la pile cosmologique validée.

## Bloc de contexte court à donner à un agent

```text
Machine Windows avec Intel i7-8550U, 4 cœurs/8 threads, 15,9 Gio de RAM.
Calcul canonique : WSL Ubuntu-22.04, utilisateur akselboursier.
Python canonique MCMC : /home/akselboursier/.venvs/cosmo-mcmc/bin/python.
CLASS canonique : /home/akselboursier/class_public, commit d60de3f4.
Pile validée : Cobaya, CLASS/classy, OpenMPI/mpi4py, emcee, ArviZ,
GetDist, Astropy, Healpy, HDF5/NetCDF/xarray, NumPy/SciPy.
Lancer 4 chaînes en parallèle, éventuellement 8, avec OMP/BLAS/MKL=1.
Python Windows scientifique : C:\Program Files\Python311\python.exe.
Julia ALPHA : uniquement via run-alpha-julia.ps1 ; ne pas la mettre dans PATH.
Ne jamais supprimer un dataset sur son nom ou sa taille : vérifier SHA-256.
Ne pas parcourir/hacher aveuglément les placeholders OneDrive.
Ne pas supprimer ext4.vhdx ni recréer CLASS ou un environnement lourd sans besoin.
Stockage cible en préparation : SSD local + restic + Backblaze B2.
```

## Configuration matérielle et limites de calcul

| Élément | État utile |
|---|---|
| Processeur | Intel Core i7-8550U, 4 cœurs physiques, 8 processeurs logiques |
| Mémoire vive | environ 15,9 Gio |
| GPU dédié | NVIDIA GeForce 930MX, 2 Gio, ancien pilote 516.69 |
| GPU intégré | Intel UHD Graphics 620 |
| CUDA | aucun `nvcc` ni `nvidia-smi` exploitable détecté |
| Disque système | C: 455,94 Gio formatés ; dernier relevé documenté : 98,21 Gio libres |

La GeForce 930MX n’est pas une cible raisonnable pour accélérer CLASS/Cobaya. Les calculs validés sont CPU. Pour éviter la surallocation, fixer systématiquement :

```bash
export OMP_NUM_THREADS=1
export OPENBLAS_NUM_THREADS=1
export MKL_NUM_THREADS=1
export NUMEXPR_NUM_THREADS=1
```

## Bilan du nettoyage et de l’espace récupéré

### Relevés fiables

| Étape | Espace libre |
|---|---:|
| Départ, 29 juillet | 17,47 Gio |
| Après le nettoyage principal | 59,35 Gio |
| Avant la passe démarrages/Docker/npm | 94,92 Gio |
| Après cette dernière passe | 98,21 Gio |
| Gain net entre le premier et le dernier relevé | 80,74 Gio |

Le nettoyage principal a produit un gain directement mesuré de **41,87 Gio**. La dernière passe a ajouté **3,29 Gio**. Le compactage administratif du VHDX WSL a réduit celui-ci d’environ **498 Mio**. La différence restante entre les relevés extrêmes n’est pas attribuée artificiellement à une suppression unique : elle inclut notamment la déshydratation OneDrive, le nettoyage interne de WSL et les effets des redémarrages/mises à jour.

### Suppressions et optimisations confirmées

- 22 copies FITS supprimées après double vérification SHA-256 : 3,62 Gio.
- 63 anciens installateurs supprimés de Téléchargements : 10,24 Gio.
- Modèles Ollama retirés : 12,99 Gio ; aucun modèle local restant.
- Caches npm, pip, mises à jour et temporaires recréables : 10,16 Gio lors de la passe principale.
- Anciens environnements Conda `chronosim` et `lenstronomy-env` supprimés après export de leurs recettes de recréation.
- Modèles Docker AI, Docker Scout et paquet npm `clawdbot` retirés : passe finale de 3,29 Gio.
- Démarrages automatiques retirés pour Claude, Evernote, Notion, Perplexity, Comet et Google Drive.
- Démarrages conservés : OneDrive pendant la transition, Wispr Flow et « Envoyer à OneNote ».

### Éléments volontairement protégés

- Mémoires, sessions, bases et stockages locaux de Claude, ChatGPT/OpenAI et Codex.
- VHDX et données Cowork/Claude en activité.
- Sauvegarde Wispr Flow du 28 juillet 2026.
- Données visibles via CrossDevice/OnePlus, non démontrées comme cache supprimable.
- Clone CLASS canonique, environnement cosmo-MCMC et paquet Julia ALPHA.
- Jeux de données canoniques ou difficiles à remplacer décrits ci-dessous.

## Environnement cosmologie/MCMC canonique

### Chemins

| Fonction | Chemin |
|---|---|
| WSL | `C:\Windows\System32\wsl.exe`, version relevée 2.5.7.0 |
| Distribution | `Ubuntu-22.04` |
| Utilisateur | `akselboursier` |
| Dossier personnel | `/home/akselboursier` |
| Python canonique | `/home/akselboursier/.venvs/cosmo-mcmc/bin/python` |
| Environnement | `/home/akselboursier/.venvs/cosmo-mcmc` ; environ 723 Mio |
| CLASS canonique | `/home/akselboursier/class_public` |
| Exécutable CLASS | `/home/akselboursier/class_public/class` |
| Miniconda conservé | `/home/akselboursier/miniconda3` ; environnement `base` seulement |
| Verrou de versions | `cosmo-mcmc-requirements-lock.txt` dans le dossier de cette synthèse |
| Noyau Jupyter | `Python (cosmo-mcmc WSL)` |

CLASS provient de `https://github.com/lesgourg/class_public.git`, branche `master`, commit relevé `d60de3f475b46dd8621e9344c8df6ffa6cfd095e`. L’environnement Python est isolé avec `include-system-site-packages = false`.

### Pile validée le 30 juillet

CLASS/classy 3.3.2.0, Cobaya 3.6.2, OpenMPI 4.1.2, mpi4py 4.1.2, emcee 3.1.6, ArviZ 1.2.0, GetDist 1.7.7, NumPy 2.5.1, SciPy 1.18.0, pandas 3.0.5, Matplotlib 3.11.1, Astropy 8.0.1, Healpy 1.20.0, HDF5/h5py, NetCDF4, xarray, Jupyter/IPython et pytest.

Sont également disponibles dans WSL : GCC, G++, GFortran, Make, Git, SSH, rsync, OpenBLAS/LAPACK, FFTW, GSL, CMake, Ninja, ccache, `rg`, `jq`, curl, wget et tmux.

### Activation et lancement

```bash
source /home/akselboursier/.venvs/cosmo-mcmc/bin/activate
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 NUMEXPR_NUM_THREADS=1
python -m pip check
```

Depuis PowerShell :

```powershell
wsl.exe -d Ubuntu-22.04 -u akselboursier -- env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 NUMEXPR_NUM_THREADS=1 /home/akselboursier/.venvs/cosmo-mcmc/bin/python /chemin/du/script.py
```

Exécution MPI conseillée :

```bash
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 NUMEXPR_NUM_THREADS=1 \
  mpirun -n 4 /home/akselboursier/.venvs/cosmo-mcmc/bin/cobaya-run analyse.yaml
```

Pour plusieurs jours, utiliser `tmux`. Lancer les 32 chaînes en 8 lots de 4, ou 4 lots de 8 seulement si la mémoire mesurée reste sûre.

### Tests réussis

- `pip check` sans dépendance cassée.
- Imports de la pile scientifique.
- Calcul CLASS Lambda-CDM avec `mPk`.
- Chaîne emcee de test.
- Vraisemblance externe Cobaya.
- HDF5, NetCDF4, xarray/ArviZ et Healpy.
- OpenMPI + mpi4py avec deux rangs.
- Limitation OpenBLAS/OpenMP à un thread.

Les scripts `smoke_test_cosmo.py`, `smoke_test_cosmo_arviz12.py` et `mpi_smoke.py` sont conservés avec ce document.

## Routage des outils selon l’action

| Action locale | Outil et chemin à privilégier |
|---|---|
| Cosmologie, CLASS, Cobaya, MPI | WSL + `/home/akselboursier/.venvs/cosmo-mcmc` |
| Modifier/compiler CLASS | VS Code Remote WSL + `/home/akselboursier/class_public` |
| Analyse scientifique Windows | `C:\Program Files\Python311\python.exe` |
| Reproduction ALPHA/QCD | `run-alpha-julia.ps1`, sans Julia globale |
| Compilation native Windows GNU | `C:\msys64\mingw64\bin\gcc.exe` / `g++.exe` |
| Compilation MSVC ancienne | Visual Studio Build Tools 2019 |
| Dépôts et automatisation GitHub | Git 2.51 + `C:\Program Files\GitHub CLI\gh.exe` |
| Édition et notebooks | VS Code 1.131 + Python/Pylance/Jupyter/WSL |
| Markdown/LaTeX/PDF | Pandoc 3.6.3 + MiKTeX/pdfLaTeX/XeLaTeX/BibTeX |
| Accès distant | OpenSSH, SCP et curl Windows ; SSH/rsync dans WSL |
| MCP fichiers | un seul serveur filesystem avec racines explicites, jamais tout C: |

Commande VS Code pour CLASS :

```powershell
code --remote wsl+Ubuntu-22.04 /home/akselboursier/class_public
```

## Julia ALPHA/QCD reproductible

Julia 1.11.5 est encapsulée dans le paquet ALPHA :

```text
C:\Users\admin\OneDrive\Documents\constantes_effectives_stabilisees\data_external\QCD\work_t1_5_ALPHA_2026\runtime\julia-1.11.5\bin\julia.exe
```

Le projet et son manifeste sont sous `package\julia_env`, et le dépôt isolé sous `julia_depot`. Le runtime et le dépôt représentent environ 3,81 Gio. Ils ont reproduit `Lambda_MSbar` et `alpha_s` et doivent rester figés.

Lanceur :

```powershell
& 'C:\Users\admin\.codex\visualizations\2026\07\29\019faebe-360d-72e1-8cb3-b48f1ce2fc8d\run-alpha-julia.ps1' -e 'import Pkg; Pkg.status()'
```

Ne pas ajouter ce runtime au `PATH` et ne pas mettre à jour son manifeste. Pour un futur projet Julia indépendant, Juliaup pourra être évalué séparément.

## Jeux de données et résultats à protéger

### Collections canoniques identifiées

- Projet actif : `C:\Users\admin\OneDrive\Documents\constantes_effectives_stabilisees\data_external`
  - `desi_dr2` : environ 8,44 Gio logiques.
  - `QCD` : environ 3,82 Gio logiques, incluant la reproduction Julia.
- Archive multi-relevés : `C:\Users\admin\OneDrive\Documents\OBSERVATIONS_COSMOLOGIQUES\data`
  - DESI, Euclid, Planck, Pantheon+SH0ES et SDSS.
- Collection difficile à remplacer : `C:\Users\admin\OneDrive\Documents\Epistemologie_cosmologie\data_observations`
  - BOSS/eBOSS DR16, Planck, Pantheon+SH0ES, eROSITA, TDCOSMO, sirènes, lentilles et GWOSC.

### Règle de conservation demandée

Conserver au moins un exemplaire validé de DESI, BOSS/eBOSS, SH0ES, Planck et Euclid, ainsi que le clone CLASS propre. Pour les résultats, privilégier les branches/dossiers les plus récents de :

- `couples_effectifs_stabilises` ;
- `constantes_effectives_stabilisees` ;
- le dossier cosmologique récent contenant les données encore actives.

Les anciennes arborescences et datasets pollués peuvent être retirés seulement après identification de l’exemplaire canonique, hydratation complète si OneDrive est impliqué, vérification SHA-256 et validation de la nouvelle sauvegarde.

## Outils présents, incomplets ou volontairement absents

### Présents et exploitables

- PowerShell 7.6.3, Git, GitHub CLI, VS Code, Node.js 24/npm/pnpm, MSYS2/GCC, Visual Studio Build Tools 2019.
- Python Windows 3.11, 3.12, 3.13 et 3.14 ; Python 3.11 est le choix scientifique Windows.
- Pandoc, MiKTeX, Calibre, OpenSSH, SQL Server LocalDB.
- Codex/ChatGPT Desktop, Claude Desktop/Claude Code, GitHub Copilot, Gemini CLI, Codex CLI et MCP filesystem.

### Présents sous forme spécialisée

- Julia : uniquement portable dans ALPHA/QCD.
- Miniconda : conservé sous WSL, base seulement.
- CLASS : clone unique sous WSL.

### Incomplets, retirés ou à ne pas supposer disponibles

- .NET : runtimes présents, **aucun SDK** ; ne pas supposer que `dotnet build` fonctionne.
- Docker Desktop : désinstallé ; modèles Docker AI et Docker Scout retirés.
- Ollama : aucun modèle et aucun exécutable fonctionnel confirmé ; une inscription orpheline peut subsister.
- CUDA : non installé et non recommandé sur ce GPU.
- Julia globale, R/Rscript, Podman, Terraform, kubectl et Azure CLI : non disponibles au dernier audit.
- Cursor : non installé et non nécessaire à la pile actuelle.

## Consignes impératives pour les agents

1. Lire cette synthèse avant toute découverte récursive du disque.
2. Utiliser des chemins explicites et limiter les racines MCP aux projets concernés.
3. Ne jamais supprimer un fichier scientifique sur la seule base du nom, de la date ou de la taille.
4. Pour un doublon, exiger une égalité SHA-256 entre la copie retirée et la copie canonique, puis vérifier de nouveau immédiatement avant suppression.
5. Une taille OneDrive est souvent logique et non physique ; hydrater les fichiers avant hachage ou copie.
6. Ne jamais supprimer directement `ext4.vhdx`. Utiliser uniquement WSL puis un compactage VHDX validé, distribution arrêtée.
7. Ne pas modifier le dépôt Julia ALPHA ni son manifeste ; ne pas ajouter son Julia au `PATH`.
8. Ne pas dupliquer CLASS ni créer un nouveau gestionnaire d’environnements sans insuffisance démontrée.
9. Pendant un calcul MCMC lourd, fermer les applications Electron non nécessaires et limiter BLAS/OpenMP à un thread.
10. Ne pas produire 150–200 Gio de chaînes sur C: dans son état actuel. Attendre le SSD et écrire les sorties lourdes sur celui-ci.
11. Sauvegarder code, configurations, manifestes, journaux et résultats finaux ; les caches et environnements reconstruisibles ne sont pas des données canoniques.
12. La future sauvegarde B2/restic ne remplace pas une restauration testée. Tout chantier de migration se termine par un essai de restauration.

## Artefacts de reproduction et restauration

Tous sont sous :

```text
C:\Users\admin\.codex\visualizations\2026\07\29\019faebe-360d-72e1-8cb3-b48f1ce2fc8d
```

- `cosmo-mcmc-requirements-lock.txt` : versions Python canoniques.
- `chronosim-recreation.yml` et `lenstronomy-env-recreation.yml` : recettes des environnements retirés.
- `smoke_test_cosmo.py`, `smoke_test_cosmo_arviz12.py`, `mpi_smoke.py` : diagnostics.
- `run-alpha-julia.ps1` : lanceur Julia ALPHA isolé.
- `safe_remove_verified_fits.ps1` : suppression contrôlée après vérification de doublons.
- `compact_wsl_vhdx_admin.ps1` et son journal : compactage contrôlé WSL.
- `startup_backup_2026-07-30\HKCU_Run_before_2026-07-30.reg` : restauration des démarrages utilisateur.
- `startup_backup_2026-07-30\Comet.lnk.disabled` : raccourci Comet désactivé et récupérable.

## Rapports sources conservés

- `RESULTATS_NETTOYAGE_2026-07-29.md`
- `NETTOYAGE_DISQUE_2026-07-29.md`
- `REPERTOIRE_OUTILS_COMPUTATIONNELS_2026-07-29.md`
- `ENVIRONNEMENT_COSMO_MCMC_2026-07-30.md`
- `CARTOGRAPHIE_LOGICIELLE_ET_ERGONOMIE_2026-07-30.md`
- `CARTOGRAPHIE_DATASETS_2026-07-29.md`
- `startup_backup_2026-07-30\RESTAURATION_ET_RAPPORT.md`

En cas de contradiction, la validation la plus récente prévaut : MPI, CMake, Ninja et les outils scientifiques WSL ont été installés et testés le 30 juillet ; Julia a été retrouvée comme environnement portable spécialisé ; les restes Docker AI et `clawdbot` ont ensuite été supprimés.
