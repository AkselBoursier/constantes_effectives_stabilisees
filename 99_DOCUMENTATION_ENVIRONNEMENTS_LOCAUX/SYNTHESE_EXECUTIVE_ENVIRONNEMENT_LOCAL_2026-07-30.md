# Environnements locaux — notice publique expurgée

**Statut : document de sécurité et de routage.**

Cette version publique ne contient volontairement aucun nom de machine, identifiant local, chemin utilisateur absolu, UUID de session, inventaire personnel, état volatil du disque ni emplacement de secret.

La version antérieure de ce fichier ne doit plus être utilisée comme fiche de référence : elle mélangeait plusieurs projets scientifiques, décrivait des chemins propres à une machine et attribuait à tort un environnement canonique unique à l’ensemble du dépôt.

## Principe d’autorité

Il n’existe pas d’environnement local universel pour tous les travaux du dépôt. Chaque lot computationnel possède son propre contrat versionné : versions logicielles, données, chemins abstraits, commandes de qualification et interdictions.

Les informations locales détaillées restent hors Git. Elles peuvent être matérialisées dans des manifestes privés, expurgés avant toute publication.

## Lot C7-C1

Pour C7-C1, l’autorité demeure l’issue #63 et ses rapports qualifiés.

```text
environnement directeur : Windows, Python 3.12.0
Cobaya                 : 3.5
CAMB                   : 1.5.4
NumPy                  : 1.26.4
SciPy                  : 1.13.1
mode acoustique        : corrected-v1.1
```

Un environnement WSL/CLASS distinct peut exister pour d’autres travaux, mais il n’est pas une substitution autorisée à l’environnement C7-C1.

## Chemins et stockage

Les documents publics emploient uniquement les symboles suivants :

```text
<REPO>       dépôt Git
<DATA>       données externes vérifiées, hors Git
<RUNS>       sorties de calcul, hors Git et hors synchronisation active
<ENV>        environnement Python qualifié
<CACHE>      caches recréables
<TEMP>       temporaires scientifiques
<ARCHIVES>   produits arrêtés et vérifiés
```

Les valeurs réelles de `C7C1_DATA_DIR` et `C7C1_XZ_OUT_DIR` ne sont jamais inscrites dans le dépôt. Elles doivent être contrôlées avant chaque calcul long et consignées sous forme expurgée dans le manifeste du run.

## Données sensibles

Sont interdits dans Git :

- noms d’hôte et identifiants locaux ;
- chemins personnels absolus ;
- UUID ou chemins de sessions d’agents ;
- jetons, secrets, identifiants et URL signées ;
- inventaires volatils détaillés de la machine ;
- sorties, caches, environnements et données volumineuses.

## État opérationnel

L’audit d’infrastructure est conduit dans l’issue #80. Jusqu’à sa clôture :

```text
raccord au lanceur G2.4b : fermé
manifestes réels          : interdits
MCMC et production        : fermées
```

Une documentation publique plus complète ne pourra être ajoutée qu’après séparation explicite entre faits stables, contrats reproductibles, états volatils et informations sensibles.
