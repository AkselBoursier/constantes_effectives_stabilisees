# Plan d'action post-audit — état reconsolidé

## Statut

Ce plan dérive de l'état analytique `42 unités / 52 relations`, de l'étude exhaustive de second ordre du matériau empirique, du prototype 2D local, de la Phase I aveugle répliquée et de la Phase II écologique complète.

Il ne constitue ni une autorisation de promotion dans `AGENTS.md`, ni une décision d'installation d'outil, ni une autorisation de merge.

## Ce qui est fait

- audit historique repo-led et saturation fonctionnelle pour la découverte générale ;
- étude exhaustive de second ordre du matériau empirique : 71/71 épisodes, saturation dans ce corpus fixe ;
- matrice 39 + delta R-040–R-042 = 42 unités effectives ;
- relations 44 + delta REL-045–REL-052 = 52 relations effectives ;
- synthèse exécutive, cartographie fonctionnelle et comparaison d'outillage ;
- prototype 2D local dérivé ;
- test contrôlé de guidage positif ;
- contre-test de silence 4/4 PASS ;
- Phase I agent neuf répliquée à `n=2` par condition : D17 84/96, D61 82/96, zéro erreur critique ;
- Phase II écologique complète : D17 48/48 + 20/20, D61 48/48 + 20/20, zéro erreur critique, zéro contamination ;
- D17 conserve la qualité décisionnelle/navigation observée avec environ 28,1 % de guide en moins ;
- aucun gain de nombre de fichiers consultés démontré en Phase II.

## Actions restantes — ordre recommandé

### A1 — réplication Phase I

**État : FAIT**

Résultat : non-infériorité D17 reproduite ; supériorité générale non établie.

### A2 — Phase II écologique

**État : FAIT**

Résultat : égalité de plafond sur cette paire écologique.

```text
D61_FIDELITE = 48/48
D61_NAVIGATION = 20/20
D17_FIDELITE = 48/48
D17_NAVIGATION = 20/20
ERREURS_CRITIQUES = 0
CONTAMINATION = NON
FICHIERS_CONSULTES = 9_DANS_CHAQUE_CONDITION
```

Le gain soutenu est un gain de **compression documentaire sous qualité conservée**, non une supériorité d'exactitude ni une réduction du nombre de sources consultées.

### A3 — décision de portée du prototype 2D

**État : OUVERTE / DECISION HUMAINE REQUISE**

Trois options restent compatibles avec les preuves :

1. **ESSAI_REEL_LOCAL_ABLABLE** — conserver la surface fonctionnelle comme guide local dérivé sur un chantier réel, avec retour aux sources et possibilité de suppression sans perte normative ;
2. **SECOND_SOUS_SYSTEME_AVANT_SEDIMENTATION** — tester le principe sur un autre sous-système pour vérifier qu'il ne dépend pas du cluster reprise/audit ;
3. **NE_PAS_SEDIMENTER** — considérer que le gain de compression ne compense pas le coût d'une surface dérivée supplémentaire.

Le résultat empirique actuel soutient les options 1 ou 2 plus fortement que l'option 3 sur le seul critère de guidage/compression, mais ne les autorise pas automatiquement.

### A4 — portée normative R-025/R-032/R-033/R-034/R-038/R-041/R-040/R-042

**État : À DÉCIDER HUMAINE**

L'audit fournit des qualifications, pas une autorisation de modification d'`AGENTS.md`.

La décision sur le prototype 2D est distincte de la promotion normative de ces règles.

### A5 — outillage

**État : AUCUNE INSTALLATION**

Les primitives Git/GitHub et scripts existants restent suffisants pour la tranche mécanique actuelle. Toute nouvelle capacité doit repartir d'une fonction observée, non d'un catalogue d'outils.

## Sorties sans action nouvelle

La majorité des 42 unités restent dans `AUCUNE` ou `CONSERVER_REGIME_EXISTANT`. Leur force probatoire n'implique pas un nouvel artefact documentaire.

## Garde-fous

```text
RESULTAT_TEST != PROMOTION
NON_INFERIORITE != SUPERIORITE_ROBUSTE
REDUCTION_VOLUME != GAIN_COGNITIF_UNIVERSEL
EGALITE_DE_SCORE != EGALITE_DE_COUT_DOCUMENTAIRE
CI_VERTE != VERDICT_SCIENTIFIQUE
PR_AUDIT != AUTORISATION_MERGE
```