# Contrat public d'environnement et de chemins — lot C7-C1

**Version 1.1 — 2 août 2026 — portes INFRA-1 (issue #80) et CAP-1 (issue #90)**
**Propriétaire : mainteneur du lot C7-C1. Révision : à chaque changement
d'environnement directeur, de racine de calcul ou de politique de secrets.**

Ce document est **public et expurgé**. Il ne contient aucun chemin utilisateur
réel, aucun nom de machine, aucun identifiant, aucun secret. Les chemins
concrets vivent dans un contrat **privé**, hors dépôt (voir
`contrat_local.example.json` pour le schéma).

Notation :

```text
<REPO>      clone directeur du dépôt, hors dossier synchronisé
<DATA>      racine des données d'entrée figées
<RUNS>      racine des sorties de calcul long
<ENV>       environnement Python directeur du lot
<CACHE>     caches réutilisables et régénérables
<TEMP>      temporaires du calcul, distincts du TEMP général
<ARCHIVES>  runs antérieurs figés, en lecture seule
```

## 1. Environnement directeur C7-C1

```text
autorité unique : <ENV>/Scripts/python.exe
  Python  3.12.0
  Cobaya  3.5
  CAMB    1.5.4
  NumPy   1.26.4      (contrainte : NumPy < 2 — exigée par CAMB 1.5.4)
  SciPy   1.13.1
  GetDist 1.7.7
  35 paquets ; empreinte SHA-256 de l'inventaire normalisé publiée au
  rapport de porte et vérifiée par l'enveloppe locale.
```

L'inventaire normalisé est la liste `nom==version`, en minuscules, triée,
une entrée par ligne, terminée par LF.

Un second environnement existe comme **banc de contrôle gelé** : il n'est pas
directeur, il est interdit au lanceur, et il n'est ni mis à jour ni supprimé.

## 2. WSL / CLASS — hors autorité C7-C1

L'environnement WSL fondé sur CLASS est un **environnement distinct et non
substituable**. Il n'exécute pas le lot C7-C1 : il ne contient pas CAMB, et sa
version de NumPy est incompatible avec CAMB 1.5.4. Toute documentation qui
présenterait un moteur WSL comme canonique pour C7-C1 est erronée pour ce lot.

## 3. Politique de chemins privés

```text
- aucun chemin utilisateur réel n'est versionné ;
- les chemins concrets vivent dans un contrat privé hors dépôt ;
- le dépôt ne publie que les symboles <REPO> <DATA> <RUNS> <ENV> <CACHE>
  <TEMP> <ARCHIVES> ;
- <REPO> est un clone complet situé hors de tout dossier synchronisé par un
  client cloud, et hors de toute arborescence portant des attributs de
  fichiers à la demande ;
- <RUNS> est hors de tout dépôt Git : aucun ancêtre du chemin ne contient
  d'entrée .git, y compris vide ;
- <RUNS> est gelée pour la durée d'un lot : aucune migration pendant une
  chaîne ni pendant une reprise ;
- <DATA>, <RUNS>, <CACHE> et <TEMP> sont quatre racines distinctes.
```

## 4. Politique de secrets et de données personnelles

```text
- aucun jeton, clé, mot de passe, URL signée ni identifiant dans le dépôt ;
- aucun nom d'hôte, nom d'utilisateur ni chemin personnel absolu dans un
  fichier versionné : le dépôt est public ;
- les contrats privés, manifestes locaux, fichiers .env et répertoires
  « private » sont exclus par .gitignore ;
- un secret ou une donnée personnelle déjà publié n'est pas corrigé par une
  simple suppression : l'expurgation de la version visible et la réécriture
  éventuelle de l'historique sont deux décisions distinctes.
```

## 5. Politique des états volatils

```text
- espace disque, mémoire libre, processus, durées, caches et états de
  synchronisation ne sont JAMAIS des faits documentaires ;
- ils sont consignés dans un relevé horodaté, jamais dans une consigne ;
- aucune règle opérationnelle ne peut être fondée sur un chiffre volatil
  sans mesure refaite au moment de l'usage.
```

## 6. Politique de manifestes

```text
- toute donnée d'entrée directrice possède un manifeste SHA-256 ;
- tout déplacement ou toute copie d'artefact produit un manifeste ;
- les artefacts de reproduction et de restauration existent en au moins
  deux exemplaires vérifiés, hors répertoire de session d'outil ;
- les manifestes privés peuvent contenir les chemins réels : ils restent
  hors du dépôt public ;
- un manifeste de run réel n'est produit qu'au moment d'une production
  autorisée, et consigne une forme expurgée des chemins.
```

## 7. Contrôle avant calcul long

Sept conditions, toutes bloquantes, vérifiées par l'enveloppe locale privée
avant toute campagne :

```text
1. environnement : versions directrices exactes et empreinte d'inventaire
   conforme ; NumPy < 2 ; interpréteur 64 bits ; site utilisateur désactivé ;
2. variables : les deux variables directrices du lot sont injectées au
   processus courant, jamais persistées aux portées utilisateur ou machine ;
3. plafonds : OMP, OPENBLAS, MKL et NUMEXPR forcés à 1 — refus si absents ;
   OPENBLAS_NUM_THREADS est exigé en plus d'OMP_NUM_THREADS, les
   bibliothèques embarquées n'étant pas compilées avec OpenMP ;
4. frontières : <RUNS> hors Git, hors dossier synchronisé, gelée ;
5. capacité : espace libre mesuré sur le RÉPERTOIRE CIBLE, pas sur la
   racine du volume ; et admission soumise à la politique de capacité
   ratifiée décrite au § 9 ;
6. reprise : identité de chemin stable ; le fichier de manifeste que la
   garde de reprise lit doit être effectivement écrit avant toute reprise ;
7. journal : versions, empreintes, chemins expurgés et variables consignés.
```

## 8. Statut

```text
raccord au lanceur          : QUALIFIÉ (G2.4d), production toujours verrouillée
manifestes réels            : INTERDITS
MCMC / minimisation         : FERMÉES
production                  : FERMÉE
budget de capacité          : RATIFIÉ (CAP-0/CAP-1) — n'ouvre PAS la production
réécriture d'historique Git : hors de cette porte
```

Le présent contrat décrit une **préparation qualifiée**, pas une autorisation
de calcul. L'ouverture de la production reste une décision humaine distincte.

## 9. Politique de capacité ratifiée

Le budget de capacité du premier lot a été **mesuré** (CAP-0) puis **ratifié
par décision humaine** le 2 août 2026, et **matérialisé** dans le contrat privé
et le lanceur (CAP-1). Les valeurs sont publiques ; elles ne dépendent d'aucun
chemin local :

```text
budget_production_requis_Gio  = 20     (enveloppe de capacité du lot de 32 runs)
reserve_reprise_Gio           = 1.15   (croissance d'un run en cours + reprise)
reserve_volume_minimale_Gio   = 40     (doit rester libre sur le support actif)
reference_ratification_budget = CAP0-2026-08-02-issue90-rat1
politique_capacite_version    = cap1-1.0.0
```

Ces valeurs sont comparées **exactement** : 19,999 et 20,001 sont refusés
comme 19 et 21. Le budget est une enveloppe de **stockage** ; il n'est ni un
critère de convergence, ni une borne du nombre de samples, ni une anticipation
de posterior.

### Règle d'admission d'un nouveau run

```text
budget_restant_alloue = max(0, budget_total − budget_deja_consomme
                                            − allocation_run_actif)

admission SI espace_libre >= budget_restant_alloue
                            + allocation_run_actif
                            + reserve_reprise
                            + reserve_volume
```

`allocation_run_actif` est l'enveloppe conservatrice S8 du type de run
courant, recalculée depuis les constantes de mesure CAP-0 (1 755 200 lignes
par run ; borne empirique de 349 octets par ligne pour la grille à cinq nœuds,
331 pour celle à quatre ; enveloppe auxiliaire au pire ratio mesuré de
0,845 %). Au début du lot, la règle exige donc **61,15 Gio** libres.

`budget_deja_consomme` est mesuré sous `<RUNS>`, sans jamais suivre de lien ni
de point d'analyse sortant, en refusant toute identité canonique qui quitte la
racine, et sans compter les sous-arbres temporaires reconnus ni les produits
non attribués à un manifeste de run. En l'absence de run réel, il vaut zéro.

La garde technique de 40 Gio **reste une garde indépendante** : elle n'est ni
remplacée ni relâchée par ce qui précède.

### Surveillance du run actif

Un observateur de capacité, branché en `callback_function` de Cobaya avec
`callback_every = 1000`, lit périodiquement l'espace libre, l'occupation du
lot et celle du run courant. Il **n'écrit rien** : ni paramètres, ni priors,
ni propositions, ni `Rminus1_stop`, ni `Rminus1_cl_stop`, ni poids, ni
samples, ni l'état de convergence. S'il franchit la haute-eau, il lève une
exception dédiée et le run reste

```text
NON_CONVERGE_INTERRUPTION_CAPACITE
```

Positionner `converged = True` est **interdit** : cela ferait passer une
interruption de capacité pour une convergence scientifique.

**Limite bloquante connue.** Cobaya 3.5 n'écrit le checkpoint qu'au cycle
d'apprentissage de la proposition ; il n'existe pas de périodicité de
checkpoint indépendante. Rien ne garantit donc qu'un checkpoint récent existe
au moment d'une interruption de capacité : la reprise automatique peut être
impossible. La garde de reprise le constate et refuse — aucun checkpoint n'est
fabriqué.

### Support actif

Le support actif est qualifié **dynamiquement** avant tout calcul : volume
système, lecteur fixe, NTFS, média SSD, bus NVMe, état sain, hors Git, hors
synchronisation. Seule une identité expurgée est publiée ou consignée — aucun
modèle, aucun numéro de série. Si la qualification matérielle devient
indisponible, le lancement est **refusé** plutôt que supposé.

Le support d'**archive indépendant** reste `NON SATISFAIT` : un seul support
physique existe, et deux répertoires du même disque ne constituent pas deux
copies.
