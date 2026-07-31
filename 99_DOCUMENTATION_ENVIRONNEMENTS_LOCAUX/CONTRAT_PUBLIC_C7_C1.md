# Contrat public d'environnement et de chemins — lot C7-C1

**Version 1.0 — 31 juillet 2026 — porte INFRA-1 (issue #80)**
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
   racine du volume ;
6. reprise : identité de chemin stable ; le fichier de manifeste que la
   garde de reprise lit doit être effectivement écrit avant toute reprise ;
7. journal : versions, empreintes, chemins expurgés et variables consignés.
```

## 8. Statut

```text
raccord au lanceur          : FERMÉ
manifestes réels            : INTERDITS
MCMC / minimisation         : FERMÉES
production                  : FERMÉE
réécriture d'historique Git : hors de cette porte
```

Le présent contrat décrit une **préparation qualifiée**, pas une autorisation
de calcul. L'ouverture de la production reste une décision humaine distincte,
soumise à un budget de capacité mesuré sur `<RUNS>`.
