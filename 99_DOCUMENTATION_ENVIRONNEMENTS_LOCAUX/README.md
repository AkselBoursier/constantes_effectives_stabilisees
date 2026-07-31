# 99_DOCUMENTATION_ENVIRONNEMENTS_LOCAUX

Documentation **publique et expurgée** des environnements et chemins locaux.

## Ce que contient ce dossier

| Fichier | Rôle |
|---|---|
| `SYNTHESE_EXECUTIVE_ENVIRONNEMENT_LOCAL_2026-07-30.md` | notice publique de sécurité et de routage ; principe d'autorité par lot |
| `CONTRAT_PUBLIC_C7_C1.md` | contrat d'environnement, de chemins et de contrôle du lot C7-C1 |
| `contrat_local.example.json` | **modèle** de contrat privé — aucune valeur réelle |

## Ce que ce dossier ne contient pas, volontairement

```text
- aucun chemin utilisateur réel, nom de machine, identifiant ni UUID ;
- aucun inventaire volatil de la machine (espace disque, processus, durées) ;
- aucun verrou de versions, script de diagnostic ni sauvegarde de restauration :
  ces artefacts sont privés, conservés hors dépôt en exemplaires vérifiés
  et couverts par un manifeste SHA-256 ;
- aucun secret, jeton, clé ni URL signée.
```

Ce dossier ne renvoie donc jamais à des « fichiers joints » qui n'y seraient
pas : tout document publié ici est autoportant. Cette règle corrige un défaut
constaté à la porte INFRA-0, où un document renvoyait à des annexes absentes.

## Comment obtenir un contrat local utilisable

1. copier `contrat_local.example.json` **hors du dépôt** ;
2. y inscrire les chemins réels, les empreintes et les seuils ;
3. ne jamais versionner la copie remplie — `.gitignore` l'exclut déjà
   (`contrat_local*.json`, `*.private.*`, `private/`, `.env`) ;
4. exécuter l'enveloppe locale privée, qui vérifie environnement, données,
   frontières et capacité avant tout calcul long.

## Autorité

Pour le lot C7-C1, l'autorité scientifique reste l'issue #63 et ses rapports
qualifiés ; l'autorité d'infrastructure est l'issue #80. En cas de divergence
entre un document local et un rapport de porte, le rapport de porte prévaut.
