# T1.5 — Manifeste local du paquet ALPHA 2026 v0.1

## 0. Statut

```text
statut : manifeste local de provenance et d'exécution ;
date du contrôle : 21 juillet 2026 ;
fonction : identifier le paquet, son environnement et la couche de calcul
           effectivement reproductible ;
ne vaut pas : audit du code de simulation, preuve d'identité avec un commit Git,
              validation indépendante des données réduites ou résultat physique
              nouveau.
```

Le présent manifeste lève le blocage d'acquisition décrit dans le
[rapport historique](T1_5_Rapport_blocage_reproduction_lattice_ALPHA_2026_v0_1.md).
Ce rapport antérieur n'est pas modifié.

## 1. Provenance locale

```text
paquet extrait témoin :
  C:\Users\admin\OneDrive\Documents\constantes_effectives_stabilisees\
  data_external\QCD\replication-package-2501.06633

archive locale :
  C:\Users\admin\OneDrive\Documents\constantes_effectives_stabilisees\
  data_external\QCD\replication-package-2501.06633-main.zip

copie d'exécution :
  C:\Users\admin\OneDrive\Documents\constantes_effectives_stabilisees\
  data_external\QCD\work_t1_5_ALPHA_2026\package
```

L'archive et les deux arborescences sont ignorées par Git au titre de la règle
`data_external/`.

| Champ | Contrôle local |
|---|---|
| origine déclarée | projet `alramos/replication-package-2501.06633` sur `https://igit.ific.uv.es`, associé à arXiv:2501.06633 |
| article de référence | Mattia Dalla Brida et al., « High-precision calculation of the quark–gluon coupling from lattice QCD », *Nature* 652, 328–334 (2026) |
| racine de l'archive | `replication-package-2501.06633-main/` |
| branche d'origine | `main`, indiquée par l'archive et par le projet déjà contrôlé ; aucune métadonnée Git locale ne permet de la certifier davantage |
| commit ou révision du paquet | **non établi** : ni l'archive ni les fichiers extraits ne contiennent un identifiant de commit |
| SHA-256 de l'archive | `9509ac9297af375f97706c68c7c3fc25ebd6d05c8c988143f2a9fa07f96b0aa6` |
| SHA-256 du manifeste Julia | `b807da7d286fa68567c792be5018e984abb4b6f7e34124e21dd2c7e1e26293ae` |
| taille des données réduites | 236 558 octets dans six fichiers BDIO |

L'empreinte de l'archive identifie exactement le matériau local utilisé. Elle ne
remplace pas l'identifiant de commit absent et ne prouve pas, à elle seule, que cette
archive est la dernière révision du projet distant.

## 2. Arborescence fonctionnelle

```text
replication-package-2501.06633/
├── README.md                         documentation et séquence d'entrée
├── data/                             données réduites BDIO
│   ├── gsqz.bdio                     couplages massifs, route découplage
│   ├── L0xLam3.bdio                  entrée Lambda^(3)/mu0, route directe
│   ├── nf0_parameters.bdio           paramètres corrélés de la théorie N_f=0
│   ├── refovhad.bdio                 rapport d'échelles basse énergie
│   ├── sqrt0.bdio                    entrées de fixation de sqrt(t0)
│   └── ssfgf.bdio                    step scaling GF à trois saveurs
├── julia_env/
│   ├── Project.toml                  dépendances directes
│   └── Manifest.toml                 environnement verrouillé Julia 1.11.5
├── main/                              scripts d'entrée, à exécuter dans l'ordre
│   ├── scale.jl                      fixation de t0 et mu_ref
│   ├── running_le.jl                 running GF basse énergie et échelles
│   ├── lam_nf3.jl                    route directe N_f=3
│   ├── lam_dec.jl                    route de découplage
│   ├── alphas.jl                     combinaison et transport vers m_Z
│   └── nf0_parameters.jl             contrôle facultatif des entrées N_f=0
├── results/
│   └── README.md                     description du format de sortie ALPHAio
└── src/                               auxiliaires d'ajustement et d'erreur
    ├── ana_utils.jl
    ├── AUFits.jl
    ├── AUSSF.jl
    ├── AUsys.jl
    └── AUTypes.jl
```

### 2.1 Classement par fonction

| Fonction | Fichiers |
|---|---|
| documentation | `README.md`, `results/README.md`, commentaires d'en-tête des scripts |
| données | six fichiers `data/*.bdio` |
| code d'analyse | `src/*.jl` et calculs contenus dans `main/*.jl` |
| code de simulation | absent du paquet ; aucune nouvelle génération de configurations lattice n'est prévue |
| configuration | paramètres codés dans les scripts et métadonnées BDIO |
| environnement et dépendances | `julia_env/Project.toml`, `julia_env/Manifest.toml` |
| résultats de référence | aucun nombre pré-calculé dans `results/` ; seulement son README avant exécution |
| scripts d'entrée | les six fichiers `main/*.jl` |

## 3. Licence et limites de réutilisation

Aucun fichier `LICENSE`, `COPYING` ou avis de licence général n'est fourni à la
racine. Les cinq fichiers `src/*.jl` portent individuellement une notice dite
« Beer-Ware License » attribuée à Alberto Ramos. Le statut de licence du README,
des scripts `main/*.jl` et des données BDIO n'est pas déclaré dans les matériaux
locaux. Il ne faut donc pas étendre la notice des auxiliaires à l'ensemble du paquet
sans information supplémentaire.

```text
licence générale du paquet : non établie.
```

## 4. Langages, formats et dépendances

```text
langage d'analyse : Julia ;
version demandée et testée par les auteurs : 1.11.5 ;
formats textuels : Markdown et TOML ;
format de données et de résultats : BDIO / ALPHAio ;
notebook : aucun ;
compilation de code du paquet : aucune ;
gestionnaire : Pkg de Julia.
```

Les dépendances directes verrouillées sont :

| Paquet | Version | Révision ou empreinte utile |
|---|---:|---|
| `ADerrors` | 0.1.0 | branche `dev-bin`, arbre `55867fb077aa683a3e0e57d52d1205ebbc6fd8fb` |
| `ALPHAio` | 0.4.0 | branche `main`, arbre `ef2b76ec5650bab78cba39314b9b31ebf7d2d1b2` |
| `ArgParse` | 1.2.0 | manifeste Julia |
| `BDIO` | 0.1.0 | branche `master`, arbre `6e36bf54b3f2f5e9ab4fd3590035b56f606eb4b3` |
| `DelimitedFiles` | 1.9.1 | manifeste Julia |
| `FastGaussQuadrature` | 1.0.2 | manifeste Julia |
| `FromFile` | 0.1.6 | manifeste Julia |
| `LaTeXStrings` | 1.4.0 | manifeste Julia |
| `LeastSquaresOptim` | 0.8.7 | manifeste Julia |
| `PGFPlotsX` | 1.6.2 | manifeste Julia |
| `Plots` | 1.40.14 | manifeste Julia |
| `Roots` | 2.2.8 | manifeste Julia |
| `Utils` | 0.1.0 | branche `main`, arbre `4cdc2cc0704eb5d984b6ccf31951c1706e961300` |

Les valeurs `git-tree-sha1` fixent le contenu des dépendances concernées dans le
manifeste ; elles ne sont pas présentées comme les commits du paquet principal.

## 5. Environnement local isolé

```text
système : Microsoft Windows 11 Professionnel 64 bits, version 10.0.26200 ;
terminal : PowerShell Core 7.5.8 ;
Julia : 1.11.5, commit de distribution 760b2e5b73 ;
plateforme Julia : x86_64-w64-mingw32 ;
processeur déclaré : Intel Core i7-8550U, 8 cœurs virtuels ;
threads Julia : 1 thread par défaut ;
compilateur externe : non requis pour l'analyse exécutée ;
dépôt de paquets : data_external/QCD/work_t1_5_ALPHA_2026/julia_depot ;
distribution portable : data_external/QCD/work_t1_5_ALPHA_2026/runtime/julia-1.11.5.
```

La distribution officielle Windows a été téléchargée sous forme ZIP. Son SHA-256,
contrôlé avant utilisation, est
`580ecaf458e273568bdd6ebcb7126392cd1e71f9b9500e0156769334774c595b`.
L'environnement natif Windows suffit ; Windows Subsystem for Linux (WSL) n'a pas été
utilisé.

## 6. Commandes d'entrée

Depuis la racine de la copie du paquet :

```powershell
$env:JULIA_DEPOT_PATH = '<...>\data_external\QCD\work_t1_5_ALPHA_2026\julia_depot'
$env:JULIA_PKG_PRECOMPILE_AUTO = '0'
<...>\runtime\julia-1.11.5\bin\julia.exe --startup-file=no --project=julia_env -e "import Pkg; Pkg.instantiate(); Pkg.status()"
```

Depuis `main/`, la séquence prescrite est :

```powershell
<...>\runtime\julia-1.11.5\bin\julia.exe --startup-file=no nf0_parameters.jl
<...>\runtime\julia-1.11.5\bin\julia.exe --startup-file=no scale.jl
<...>\runtime\julia-1.11.5\bin\julia.exe --startup-file=no running_le.jl
<...>\runtime\julia-1.11.5\bin\julia.exe --startup-file=no lam_nf3.jl
<...>\runtime\julia-1.11.5\bin\julia.exe --startup-file=no lam_dec.jl
<...>\runtime\julia-1.11.5\bin\julia.exe --startup-file=no alphas.jl
```

`nf0_parameters.jl` est un contrôle facultatif sans sortie écrite. Les cinq autres
scripts constituent la chaîne ordonnée. Les fichiers de résultat existants ne sont
pas écrasés ; la copie de travail était vide de ces sorties avant l'exécution. Le
paquet extrait témoin est resté inchangé ; les sorties locales ont été écrites
uniquement dans `data_external/QCD/work_t1_5_ALPHA_2026/package/results/`.

## 7. Données réduites et simulations complètes

Le paquet réduit plusieurs millions d'heures-cœur de simulation à des observables et
paramètres BDIO suffisants pour réexécuter les ajustements distribués et les nombres
finaux. Il permet :

- de refaire la fixation d'échelle à partir des entrées distribuées ;
- de réajuster le step scaling de flot de gradient (GF) basse énergie ;
- de reconstruire la route directe à partir d'une entrée condensée de haute énergie ;
- d'ajuster les couplages massifs, le continuum et la limite de découplage ;
- de combiner les deux routes avec leur covariance propagée ;
- d'effectuer les raccordements vers quatre puis cinq saveurs.

Il ne permet pas, à lui seul :

- de régénérer les configurations lattice avec `openQCD` ;
- de refaire la détermination non perturbative de `b_g` à partir des configurations ;
- de recomputer depuis les configurations le running Schrödinger fonctionnel (SF) à
  haute énergie, condensé dans `L0xLam3.bdio` ;
- de reconstruire depuis les configurations les paramètres de jauge pure contenus
  dans `nf0_parameters.bdio` ;
- de produire indépendamment les données condensées distribuées ;
- d'établir le commit exact du paquet principal.

La reproduction documentée porte donc sur le pipeline d'analyse à partir des produits
condensés fournis, pas sur une nouvelle simulation lattice ni sur une nouvelle mesure.
