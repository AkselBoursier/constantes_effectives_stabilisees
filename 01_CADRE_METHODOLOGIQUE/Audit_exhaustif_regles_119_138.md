# Audit exhaustif et étude des règles et régimes — fenêtre de départ #119 à #138

## Fonction

Cette pièce est l’ancrage d’un audit **exhaustif et qualifiant** des règles explicites et implicites présentes, appliquées, modifiées, testées, contredites, sous-appliquées, sur-appliquées ou perdues dans le dépôt.

Les objets GitHub **#119 à #138 constituent la fenêtre de départ obligatoire**, non une frontière. L’investigation est ouverte dans les deux sens :

- **vers l’amont**, en remontant aux issues, PR, documents, commits, décisions, protocoles ou épisodes antérieurs dès qu’ils sont nécessaires pour reconstruire la naissance, le régime, la fonction, l’effectivité ou les contre-cas d’une règle ;
- **vers l’aval et les objets adjacents**, en suivant les conséquences, matérialisations, corrections, essais, retraits ou nouvelles formulations postérieures dès qu’ils changent l’interprétation de la règle étudiée.

L’audit peut donc conduire à lire une part très importante, voire la totalité pertinente, des issues antérieures. Il ne doit toutefois pas lire mécaniquement tout le dépôt si l’investigation atteint une saturation démontrable.

L’audit ne se limite pas à observer ou recenser. Il doit **étudier** chaque règle suffisamment identifiée : reconstruire sa fonction, son régime, son effectivité, ses mécanismes, ses coûts, ses contre-cas, ses relations récursives et son statut probatoire. Lorsque l’observation existante ne suffit pas à discriminer entre plusieurs qualifications, l’audit doit concevoir puis, si son régime l’autorise, exécuter un contre-test, une ablation, une comparaison ou une vérification ciblée.

Cette étude précède toute nouvelle promotion normative dans `AGENTS.md`, toute migration vers l’infrastructure et toute sélection d’outil.

L’expérience empirique conversationnelle fournie par l’auteur pendant la reprise du 20 août 2026 est traitée comme une **surface d’étude des trajectoires et de l’application réelle des règles**. Elle n’est pas une autorité normative. Elle sert notamment à confronter les règles disponibles au comportement effectif : déclenchement, oubli, sous-application, sur-application, correction, bénéfice, coût, récursivité et effet sur la décision suivante.

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
- ne pas attribuer une ratification humaine sur la seule identité du compte GitHub auteur lorsqu’un agent peut écrire via le compte connecté ;
- ne pas appeler `test` une simple application favorable : chercher effet attendu, critère d’échec/coût, comparaison/ablation/contre-exemple et observation discriminante ;
- lorsque plusieurs règles se gouvernent mutuellement, étudier la récursivité elle-même : règle, contrôle de la règle, contrôle du contrôle, trace de ce contrôle, synchronisation et condition d’arrêt.

## Unité d’étude d’une règle

Pour chaque règle ou pratique normative candidate, l’audit cherche, lorsqu’elles sont pertinentes :

1. formulation(s) et transformations ;
2. fonction protégée ou améliorée ;
3. sujet : agent, humain, automatisation ou combinaison ;
4. portée, déclencheur, durée, exceptions, priorité, héritage et condition de retrait ;
5. autorité et ratification réellement retrouvées ;
6. régime appliqué de facto et écarts avec le régime déclaré ;
7. mécanisme d’enforcement réel : convention, document, Git, CI, script, workflow, validation humaine, etc. ;
8. épisodes d’application, de silence, d’oubli, de sous-application et de sur-application ;
9. effets observés sur information, erreur, décision, charge cognitive/documentaire/technique et réversibilité ;
10. contre-cas, falsificateurs, ablations ou comparaisons déjà disponibles ;
11. tests supplémentaires réellement discriminants, s’ils sont nécessaires et autorisés ;
12. contradictions, redondances, absorptions possibles et relations récursives avec d’autres règles ;
13. dépendance au domaine ou au régime ;
14. statut probatoire et verdict provisoire, sans promotion automatique ;
15. **action à réaliser**, si l’étude en justifie une ;
16. **condition de déclenchement / régime de cette action**, afin qu’une action locale ou conditionnelle ne soit pas lue comme une instruction générale.

Une règle peut donc être abondamment observée sans être encore suffisamment étudiée pour être qualifiée. Elle peut aussi être suffisamment qualifiée sans appeler de nouvelle action.

## Condition d’exhaustivité et de suffisance de la première étude

La première passe n’est pas terminée tant que :

1. chaque objet #119–#138 a été lu avec son corps et tous ses commentaires/checkpoints pertinents ;
2. pour les PR qui matérialisent ou testent une règle, les diffs/contrôles nécessaires ont été inspectés afin de distinguer intention et application réelle ;
3. chaque formulation normative ou pratique normative identifiable a soit une entrée de matrice, soit une justification explicite de non-règle ;
4. chaque règle entrée dans la matrice a été étudiée au moins jusqu’au niveau nécessaire pour distinguer fonction, régime, effectivité et statut probatoire ;
5. les relations récursives entre règles, règles de contrôle, règles de contrôle des règles et mécanismes d’enforcement ont été reliées ;
6. les règles explicitement locales sont séparées des extensions historiques ou supposées ;
7. les règles implicites détectées dans les comportements réels sont distinguées des simples habitudes ;
8. l’expérience empirique conversationnelle fournie a été confrontée aux règles du dépôt pour étudier application, oubli, sous-application, sur-application, correction, coût et effet décisionnel ;
9. les règles à fort impact ou au statut ambigu ont reçu un contre-test/une comparaison lorsqu’une observation seule ne permet pas de les qualifier et que le test est autorisé ;
10. aucune grande famille de fonction rencontrée dans la fenêtre de départ ou découverte par remontée/extension n’est exclue par convention ;
11. les antécédents nécessaires ont été suivis vers l’amont et les conséquences nécessaires vers l’aval ;
12. une passe indépendante du dépôt a cherché les pratiques/règles que la fenêtre #119–#138 n’aurait pas rendues saillantes.

L’exhaustivité documentaire n’implique pas une profondeur identique pour toutes les règles : l’approfondissement est commandé par la dépendance réelle et le pouvoir discriminant attendu. Mais une règle ne peut être tenue pour sans effet ou qualifiée uniquement parce que son intitulé paraît clair.

## Condition d’arrêt de l’exploration historique

L’arrêt avant lecture de toutes les issues n’est admissible que s’il est **positivement justifié par saturation**, et non par commodité ou par numéro d’issue.

Une saturation raisonnable exige au minimum que :

- les chaînes de dépendance et antécédents encore ouverts aient été résolues ou explicitement bornées ;
- plusieurs objets successifs ou adjacents supplémentaires n’apportent plus de nouvelle famille de règle, nouvelle transformation de régime, nouveau mécanisme d’enforcement, nouveau contre-cas discriminant, nouvelle sous-application/sur-application ou nouvelle relation récursive substantielle ;
- les règles déjà identifiées aient un contexte de naissance suffisamment reconstruit pour tester leur portée ;
- aucun renvoi encore non suivi ne soit susceptible de modifier un verdict, une action, une autorité ou une condition de silence ;
- la passe indépendante repo→règles n’indique plus de famille substantielle absente du corpus étudié.

La décision d’arrêt doit laisser une trace auditable précisant :

```text
DERNIERES_ZONES_LUES
OBJETS_NON_LUS_OU_NON_APPROFONDIS
RAISON_DE_LEUR_NON_PERTINENCE_PRESUMEE
INDICES_DE_SATURATION_OBSERVES
DEPENDANCES_RESTANTES_EVENTUELLES
CONDITION_DE_REOUVERTURE_DE_L_ARCHEOLOGIE
```

Si ces conditions ne sont pas remplies, l’audit continue à remonter ou à élargir son corpus.

## Couverture des objets

| Objet | Nature | Corps | Commentaires/checkpoints | Diffs/application réelle | Règles étudiées | Relations/récursivités | Statut couverture |
|---|---|---|---|---|---|---|---|
| #119 | issue | lu | lecture en cours | n/a + objets liés si nécessaires | en cours | en cours | OUVERT |
| #120 | issue | lu | lecture en cours | n/a + objets liés si nécessaires | en cours | en cours | OUVERT |
| #121 | PR | lu | lu | à contrôler | en cours | en cours | OUVERT |
| #122 | PR | lu | lu | à contrôler | en cours | en cours | OUVERT |
| #123 | issue | lu | lu | #124 lié | en cours | en cours | OUVERT |
| #124 | PR | lu | lu | à contrôler | en cours | en cours | OUVERT |
| #125 | issue | lu | lu | #126 lié | en cours | en cours | OUVERT |
| #126 | PR | lu | lu | à contrôler | en cours | en cours | OUVERT |
| #127 | issue | lu | lu | #128 + mutations issues | en cours | en cours | OUVERT |
| #128 | PR | lu | aucun commentaire | à contrôler | en cours | en cours | OUVERT |
| #129 | PR | lu | lu | à contrôler | en cours | en cours | OUVERT |
| #130 | issue | lu | lecture exhaustive en cours | objets liés selon dépendance | en cours | en cours | OUVERT |
| #131 | PR | lu | lu | à contrôler | en cours | en cours | OUVERT |
| #132 | PR | état partiellement reconstruit | à relire exhaustivement | à contrôler | en cours | en cours | OUVERT |
| #133 | PR | état courant connu | à relire exhaustivement | à contrôler | en cours | en cours | OUVERT |
| #134 | issue | lu | lecture substantielle effectuée | mécanismes/outils liés | en cours | en cours | OUVERT |
| #135 | issue | lu | lecture exhaustive effectuée | épisodes/diffs liés | en cours | en cours | OUVERT |
| #136 | issue | lu | lecture exhaustive effectuée | mécanismes/outils liés | en cours | en cours | OUVERT |
| #137 | PR | lu | aucun commentaire | diff lu | en cours | en cours | OUVERT |
| #138 | PR gelée | lu | checkpoints lus | diff lu comme contre-cas | en cours | en cours | OUVERT |

Cette table ne constitue pas la liste complète du corpus final. Les objets antérieurs/postérieurs ajoutés par dépendance seront consignés au fur et à mesure dans les supports de couverture et de matrice.

## Schéma minimal attendu de la matrice finale

La structure observée justifie deux tables CSV versionnées : une matrice des règles et une table des relations/récursivités. Chaque entrée de règle devra pouvoir porter au minimum :

```text
ID_REGLE
FORMULATION_COURANTE
FONCTION
SUJET
SOURCE(S)_ET_ANTECEDENT(S)
REGIME_DECLARE
REGIME_RATIFIE
REGIME_DE_FACTO
PORTEE / DECLENCHEUR / EXCEPTIONS / ARRET
MECANISME_D_ENFORCEMENT
EPISODES_D_APPLICATION
EPISODES_DE_SILENCE
SOUS_APPLICATIONS
SUR_APPLICATIONS
EFFETS_BENEFIQUES
COUTS / EFFETS_ADVERSES
CONTRE_CAS / ABLATIONS / TESTS
STATUT_PROBATOIRE
VERDICT_PROVISOIRE
ACTION_A_REALISER
CONDITION_DE_DECLENCHEMENT_DE_L_ACTION
SUPPORT_CIBLE_EVENTUEL
```

Les dépendances, contradictions, absorptions, règles de contrôle et récursivités sont portées séparément dans la table des relations afin de ne pas les aplatir dans une seule cellule.

`ACTION_A_REALISER` n’est pas synonyme de promotion. Les sorties admissibles incluent notamment : `AUCUNE`, `APPLIQUER_DANS_REGIME_X`, `CONTRE_TESTER`, `RESTREINDRE`, `REFORMULER`, `RETIRER`, `INSCRIRE_AGENTS_LOCAL`, `INSCRIRE_AGENTS_TRANSVERSE`, `PORTER_PAR_INFRASTRUCTURE`, `AUTOMATISER_MECANIQUEMENT`, `CONSERVER_EN_SHADOW`, `DOCUMENTER_ET_NE_PAS_ACTIVER`, ou une action plus spécifique justifiée par l’étude.

## Sorties attendues après étude

Après couverture exhaustive et étude suffisante, l’audit produira séparément :

1. une matrice exhaustive des règles et régimes en CSV ;
2. une table CSV des récursivités, contradictions, dépendances, recouvrements et mécanismes d’enforcement entre règles ;
3. une synthèse exécutive Markdown distinguant ce qui est suffisamment soutenu pour être appliqué/promu dans un régime donné, ce qui doit rester local ou en shadow, ce qui exige un contre-test, ce qui doit être restreint/retiré et ce qui paraît mieux porté par l’infrastructure ;
4. un plan d’action dérivé de la matrice, où chaque action conserve son régime, son déclencheur, son support cible et son niveau d’autorité ;
5. seulement après cette synthèse, une cartographie fonctionnelle des besoins d’outillage, puis une recherche ciblée de capacités natives, API/MCP et outils open source gratuits, sans choisir un outil avant d’avoir établi la fonction à porter ;
6. pour toute migration ou automatisation candidate, une comparaison entre règle interprétée, mécanisme infrastructurel, combinaison des deux et absence de changement.

## Statut

```text
AUDIT = OUVERT / EXHAUSTIF / QUALIFIANT
FENETRE_DE_DEPART = #119-#138 / NON_FERMEE
EXPLORATION_AMONT_AVAL = OUVERTE_SELON_PERTINENCE
ARRET_AVANT_LECTURE_TOTALE = UNIQUEMENT_SUR_SATURATION_JUSTIFIEE
OBSERVATION_SEULE = INSUFFISANTE
PROMOTION_NORMATIVE = SUSPENDUE
MATRICE = CSV_REGLES + CSV_RELATIONS
ACTION_A_REALISER = SORTIE_OBLIGATOIRE_DE_L_ETUDE / PEUT_ETRE_AUCUNE
OUTILLAGE = APRES_MATRICE_ET_SYNTHESE_FONCTIONNELLE
MERGE = NON_AUTORISE_PAR_CE_DOCUMENT
```
