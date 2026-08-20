# Audit exhaustif des règles et régimes — #119 à #138

## Fonction

Cette pièce est l’ancrage de l’inventaire exhaustif des règles explicites et implicites présentes, appliquées, modifiées, testées, contredites ou perdues dans les objets GitHub #119 à #138 et dans les surfaces empiriques directement pertinentes pour leur interprétation.

Elle précède toute nouvelle promotion normative dans `AGENTS.md`, toute migration vers l’infrastructure et toute sélection d’outil.

La conversation fournie par l’auteur pendant la reprise du 20 août 2026 est traitée comme une **expérience empirique / surface d’observation des trajectoires et de l’application réelle des règles**. Elle n’est pas une autorité normative. Elle sert notamment à observer les règles effectivement déclenchées, non déclenchées, sur-appliquées, sous-appliquées, corrigées ou oubliées.

## Règles d’audit déjà applicables

L’audit applique notamment les exigences déjà établies dans le dépôt :

- distinguer règle formulée, régime déclaré, régime humainement ratifié, régime appliqué de facto et régime justifié après audit ;
- rechercher symétriquement sur-extension et sous-application ;
- distinguer application, observation, test, qualification, promotion et extension de périmètre ;
- ne pas reconstruire rétroactivement une portée depuis la répétition, l’ancienneté ou la seule présence dans un document ;
- rechercher les pratiques normatives implicites sans confondre répétition, contrainte technique, habitude d’agent, décision locale et norme de facto ;
- localiser le niveau causal/fonctionnel avant de proposer une correction ;
- conserver les contre-cas, résultats négatifs, exceptions, conditions de silence et coûts ;
- distinguer utilité d’une fonction et nécessité de la conserver sous forme de règle ;
- ne pas réparer les règles pendant la phase d’inventaire ;
- ne pas attribuer une ratification humaine sur la seule identité du compte GitHub auteur lorsqu’un agent peut écrire via le compte connecté.

## Condition d’exhaustivité

La première passe n’est pas terminée tant que :

1. chaque objet #119–#138 a été lu avec son corps et tous ses commentaires/checkpoints pertinents ;
2. chaque formulation normative ou pratique normative identifiable a soit une entrée de matrice, soit une justification explicite de non-règle ;
3. les relations récursives entre règles, règles de contrôle, règles de contrôle des règles et mécanismes d’enforcement ont été reliées ;
4. les règles explicitement locales sont séparées des extensions historiques ou supposées ;
5. les règles implicites détectées dans les comportements réels sont distinguées des simples habitudes ;
6. la surface empirique conversationnelle fournie a été confrontée aux règles du dépôt pour observer application, oubli, sous-application, sur-application et correction ;
7. aucune grande famille de fonction rencontrée dans #119–#138 n’est exclue par convention.

## Couverture des objets

| Objet | Nature | Corps | Commentaires/checkpoints | Règles extraites | Relations/récursivités | Statut couverture |
|---|---|---|---|---|---|---|
| #119 | issue | lu | à lire exhaustivement | en cours | en cours | OUVERT |
| #120 | issue | lu | à lire exhaustivement | en cours | en cours | OUVERT |
| #121 | PR | lu | à lire exhaustivement | en cours | en cours | OUVERT |
| #122 | PR | lu | à lire exhaustivement | en cours | en cours | OUVERT |
| #123 | issue | lu | à lire exhaustivement | en cours | en cours | OUVERT |
| #124 | PR | lu | à lire exhaustivement | en cours | en cours | OUVERT |
| #125 | issue | lu | à lire exhaustivement | en cours | en cours | OUVERT |
| #126 | PR | lu | à lire exhaustivement | en cours | en cours | OUVERT |
| #127 | issue | lu | à lire exhaustivement | en cours | en cours | OUVERT |
| #128 | PR | lu | aucun commentaire d’ouverture signalé | en cours | en cours | OUVERT |
| #129 | PR | lu | à lire exhaustivement | en cours | en cours | OUVERT |
| #130 | issue | lu | à lire exhaustivement | en cours | en cours | OUVERT |
| #131 | PR | lu | à lire exhaustivement | en cours | en cours | OUVERT |
| #132 | PR | lu/état déjà partiellement reconstruit | à relire exhaustivement | en cours | en cours | OUVERT |
| #133 | PR | lu/état courant connu | à relire exhaustivement | en cours | en cours | OUVERT |
| #134 | issue | lu | à relire exhaustivement | en cours | en cours | OUVERT |
| #135 | issue | lu | à relire exhaustivement | en cours | en cours | OUVERT |
| #136 | issue | lu | à lire exhaustivement | en cours | en cours | OUVERT |
| #137 | PR | lu | aucun commentaire au dernier contrôle | en cours | en cours | OUVERT |
| #138 | PR gelée | lu | checkpoint/tentative à intégrer comme contre-cas | en cours | en cours | OUVERT |

## Sorties attendues après inventaire

Après couverture exhaustive, l’audit produira séparément :

1. une matrice exhaustive des règles et régimes, sur un support choisi selon son rôle réel de filtrage, comparaison, maintenance et future automatisation ;
2. une carte des récursivités et dépendances entre règles ;
3. une synthèse exécutive indiquant ce qui paraît applicable, testable, promouvable, local, à restreindre, à contre-tester, à déplacer vers l’infrastructure ou à laisser en observation ;
4. une cartographie fonctionnelle des besoins d’outillage, puis une recherche ciblée de capacités natives, API/MCP et outils open source gratuits, sans choisir un outil avant d’avoir établi la fonction à porter.

## Statut

```text
INVENTAIRE_119_138 = OUVERT / EXHAUSTIF
PROMOTION_NORMATIVE = SUSPENDUE
MATRICE = SUPPORT_A_DECIDER_APRES_OBSERVATION_STRUCTURELLE
OUTILLAGE = APRES_MATRICE_ET_FONCTIONS
MERGE = NON_AUTORISE_PAR_CE_DOCUMENT
```
