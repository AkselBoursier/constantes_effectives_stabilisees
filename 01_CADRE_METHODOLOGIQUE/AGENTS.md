# Règles locales — méthodologie, méta-règles et shadow learning

Ce fichier complète le `AGENTS.md` racine pour tout travail sur la méthodologie, les règles, la gouvernance documentaire, la reprise entre agents et le shadow learning.

Sa fonction est de rendre l'état méthodologique vivant récupérable sans refaire l'archéologie. Il ne remplace pas les pièces probatoires détaillées.

## 1. Route courante

Pour une tâche relevant de ce domaine, lire dans cet ordre :

1. le `AGENTS.md` racine ;
2. le présent fichier ;
3. l'issue #135 pour l'audit historique et les contre-tests des méta-règles ;
4. la PR #133 seulement lorsqu'une candidate, son checkpoint ou son essai est concerné ;
5. l'issue #134 lorsqu'une fonction pourrait être portée en tout ou partie par Git, GitHub, CI, workflows ou autre infrastructure ;
6. les protocoles historiques précis seulement lorsqu'ils sont nécessaires à l'objet étudié.

Ne pas repartir de zéro. Ne pas traiter une règle comme nouvelle simplement parce qu'elle est nouvelle pour l'agent courant.

## 2. État méthodologique à connaître avant d'agir

L'audit #135 a déjà établi qu'une règle doit être reconstruite selon plusieurs plans qui ne se confondent pas :

```text
REGLE_FORMULEE
!= REGIME_DECLARE
!= REGIME_HUMAINEMENT_RATIFIE
!= REGIME_APPLIQUE_DE_FACTO
!= REGIME_JUSTIFIE_APRES_AUDIT
```

Pour les pratiques implicites, distinguer également : pratique répétée, contrainte technique, habitude d'agent, décision humaine locale et norme de facto.

La répétition, l'ancienneté, l'inscription dans un document d'autorité ou l'usage ultérieur ne suffisent pas à reconstruire rétroactivement la portée d'une règle.

## 3. Application, test et promotion

Une application n'est pas automatiquement un test. Une règle n'est pas qualifiée comme testée seulement parce qu'elle paraît raisonnable, répond à un incident réel, a été appliquée plusieurs fois, a été acceptée localement ou n'a pas produit d'échec visible.

Lorsqu'un test probant est revendiqué, rechercher autant que possible :

```text
effet attendu avant observation
+ critère d'échec ou coût excessif
+ contre-exemple / ablation / comparaison
+ observation réellement discriminante
```

Une qualification locale ne peut pas être promue lorsqu'un contexte matériellement accessible et manifestement pertinent reste non instruit.

La promotion d'une règle et l'extension de son périmètre sont deux questions distinctes. Une règle peut être suffisamment soutenue dans un régime et rester non qualifiée ailleurs.

## 4. Sur-extension et sous-extension

Chercher symétriquement :

- les règles appliquées trop largement, trop longtemps ou hors contexte ;
- les règles comprises trop localement, sous-appliquées ou retirées trop tôt ;
- les occasions manquées où une règle déjà disponible aurait pu prévenir une perte, une confusion, une duplication ou un blocage ;
- les garde-fous perdus lors d'une reformulation ou d'une propagation.

Le bon régime n'est ni global ni local par défaut : il est à reconstruire et à tester.

## 5. Dézoom systémique borné

Lorsqu'un défaut local se répète, qu'une correction locale ne tient pas ou que plusieurs règles produisent la même friction, remonter jusqu'au premier niveau causal testable : objet, relation, sous-système ou architecture.

Ne pas dézoomer par principe. S'arrêter lorsqu'un discriminant suffisant relie le défaut, sa portée et une intervention minimale, puis revenir au niveau local pour vérifier l'effet.

Ne pas ouvrir un audit de l'audit supplémentaire sans anomalie précise ou gain attendu identifiable.

## 6. Autoréflexion — état probatoire actuel

Le micro-pilote réflexif du 16 juillet 2026 constitue une mise à l'épreuve réelle et localement valide de réflexivité bornée sur trois objets, avec passage unique, critères de réussite, critères de boucle stérile et conditions d'arrêt.

En revanche :

```text
AUTORÉFLEXION_CONTINUE = NON_QUALIFIEE
AUTORÉFLEXION_AUTO_DECLENCHEE_A_CHAQUE_TACHE = NON_QUALIFIEE
SUPERIORITE_GENERALE_DU_MODE_BORNE = NON_ETABLIE
BON_DECLENCHEUR_GENERAL = ENCORE_A_INSTRUIRE
```

Utiliser une passe réflexive lorsqu'un déclencheur réel la justifie ; ne pas installer par défaut une boucle permanente parallèle au travail principal.

## 7. Intelligibilité et reprise

Lorsque l'objet doit être compris, contrôlé ou validé humainement :

- nommer d'abord l'objet en langage naturel ;
- utiliser codes et sigles comme repères secondaires ;
- ré-expliciter le référent aux changements de domaine, aux reprises ou lorsque plusieurs objets proches peuvent être confondus ;
- ne pas imposer l'historique d'un objet à un lecteur qui n'en a pas besoin ;
- réintroduire au contraire l'état antérieur lorsqu'une comparaison, une réinstruction, une généalogie ou une décision exige précisément cette temporalité.

## 8. État courant et checkpoints

L'ancrage principal d'un chantier doit permettre de connaître l'état courant suffisamment vite. Les checkpoints successifs conservent les transitions qui ont une valeur réelle de reprise ou de généalogie.

Ne pas écraser un checkpoint ancien pour représenter un état nouveau. Ne pas faire non plus des checkpoints le seul moyen de reconstruire l'état courant.

Créer ou mettre à jour un checkpoint lorsqu'un changement modifie substantiellement le statut, le régime, la portée, le soutien probatoire, un contre-cas, une décision ou la prochaine opération de reprise. Une simple répétition sans changement d'état n'exige pas automatiquement un nouveau checkpoint.

## 9. Non-prolifération proportionnée

La non-prolifération n'est pas un veto à la création.

Créer un document, une issue, une PR, un checkpoint ou une autre couche lorsqu'une fonction identifiable le justifie : récupération de contexte, identité propre d'un objet, comparaison, preuve, décision, traçabilité, contrôle ou réduction réelle de charge.

Ne pas créer un artefact seulement parce qu'une idée existe. Ne pas refuser un artefact utile seulement parce qu'un support existant pourrait théoriquement contenir davantage d'information.

Le critère est fonctionnel : ce que l'objet permet de récupérer, distinguer, contrôler ou reprendre doit justifier son coût de maintien.

## 10. Interventions humaines

Une intervention humaine n'est pas automatiquement un ordre. Lorsque cela change l'action, distinguer observation, hypothèse, proposition, préférence, décision et autorisation.

Une proposition doit être confrontée au dépôt et aux preuves applicables avant d'être transformée en règle ou en mutation. Une décision ou autorisation explicite s'applique dans son périmètre sans être neutralisée au prétexte qu'une nouvelle évaluation serait possible, et sans être généralisée silencieusement au-delà de ce périmètre.

## 11. Surface probatoire actuelle

Les éléments suivants doivent être considérés comme déjà instruits à des degrés différents et ne doivent pas être requalifiés depuis zéro :

- contre-tests CT1–CT5 de #135 ;
- micro-pilote réflexif du 16 juillet ;
- essais Human-First et checkpoints de #133 ;
- lignée d'ablation/contrôles #104–#108 ;
- pilote Issues–Project E0/#19 ;
- épisodes de validation dense puis délégation/autonomie technique dans #63/#102 ;
- antécédents de synchronisation, versionnage et règles implicites documentés dans #135.

Le statut exact de chacun doit être lu dans sa pièce de qualification avant promotion durable.
