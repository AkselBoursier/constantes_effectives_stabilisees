# Clé des conditions et ordre — Phase III-B

## Statut

**Ne pas fournir aux agents testés. Ne pas révéler avant gel des quatre réponses brutes.**

La clé est pré-enregistrée avant lancement des chats prospectifs afin d'empêcher toute attribution post hoc des conditions.

## Base de dérivation

Commit de sélection des tâches avant construction des paquets :

`e08d15ef5492e614de4d6deff1ce7b9b67b8bd45`

Empreintes déterministes :

```text
SHA256("e08d15ef5492e614de4d6deff1ce7b9b67b8bd45|III-B|S")
= aad84dc7c9eef27a2c9dcd49bee5cd97c98535615ac647ca6caad3d52ae9b4ed

SHA256("e08d15ef5492e614de4d6deff1ce7b9b67b8bd45|III-B|M")
= 71459ecb96d44f34b080f2cfda4b60a51119ef7596220fb6d586e33e04683eb3

SHA256("e08d15ef5492e614de4d6deff1ce7b9b67b8bd45|III-B|ORDER")
= c025e584a86267f377bd7a7d898c540cff0e2bf53a35042db38a4959fea92ebe
```

## Clé documentaire

```text
CONDITION_7A = présentation par unités/fiches + relations explicites
CONDITION_9C = présentation fonctionnelle composée / parcours et boucles
```

Correspondance historique de l'hypothèse expérimentale, à ne pas exposer aux agents :

```text
7A ~ famille D61
9C ~ famille D17
```

La comparaison porte sur organisation/compression, pas sur un corpus fonctionnel différent.

## Ordre de lancement pré-enregistré

Permutation déterministe obtenue depuis l'empreinte `ORDER` :

```text
1. M_9C
2. S_7A
3. M_7A
4. S_9C
```

L'ordre n'est pas une variable scientifique ; il sert seulement à éviter un choix opportuniste après observation d'une première réponse.

## Gel

```text
CLE = GELEE
ORDRE = GELE
REVELATION_AUX_AGENTS = INTERDITE
REVELATION_AVANT_4_REPONSES_BRUTES = INTERDITE
```
