# Guide de travail pour les agents

Ce fichier décrit comment intervenir dans le dépôt sans confondre état scientifique, calcul, documentation et décision. Lire d’abord le [README](README.md), puis le point d’entrée du cycle ou du volet concerné.

## 1. Mission et autorité

Le projet étudie ce que les sciences peuvent soutenir lorsqu’elles qualifient de constante une grandeur, une relation, une valeur ou une structure.

Deux questions publiques organisent le travail :

1. Comment les sciences établissent-elles, utilisent-elles et déplacent-elles la frontière entre ce qui varie et ce qui tient ?
2. Par quelles structures, opérations et chemins de détermination un maintien devient-il opératoire ou affirmable dans un régime, et que change cette reconstruction pour l’enquête scientifique ?

L’agent peut inspecter, comparer, calculer, falsifier, proposer des corrections et exécuter les opérations techniques autorisées dans son périmètre. Une décision humaine reste obligatoire pour les frontières scientifiques ou irréversibles : question de recherche, modèle, données, prior, paramétrisation scientifique, interprétation, seuil d’évidence, promotion durable et merge.

## 2. Parcours minimal

Pour une tâche locale :

1. lire le [README](README.md) ;
2. pour une tâche physique ou computationnelle, lire l’[accueil des cycles](02_CYCLES_PHYSIQUES/README.md) ;
3. entrer dans le README ou document local indiqué ;
4. lire l’issue ou la décision qui borne la tâche, lorsqu’elle existe ;
5. consulter le [cadre méthodologique](01_CADRE_METHODOLOGIQUE/refondation-du-domaine.md) ou le [glossaire](GLOSSAIRE.md) seulement si la tâche l’exige.

Ne pas précharger l’intégralité du corpus par défaut. La provenance détaillée se consulte lorsqu’une décision, une contradiction ou une révision l’exige.

### 2.1 Intelligibilité humaine suffisante

Une prose grammaticalement claire ne suffit pas si les objets auxquels elle se réfère ne sont pas identifiables par le lecteur humain.

Lorsqu’une proposition, une synthèse, un état ou une décision doit être compris, contrôlé ou validé humainement :

- nommer d’abord l’objet en langage naturel ;
- introduire ensuite, si utile, son code, sigle ou identifiant local comme référence secondaire ;
- ré-expliciter le référent aux frontières de contexte lorsque plusieurs codes, phases, cycles ou sous-objets peuvent être confondus ;
- ne pas présumer qu’une syntaxe fluide établit à elle seule la compréhension du référent.

Cette règle n’interdit pas la notation compacte dans le travail effectif. Une notation locale peut être utilisée si elle apporte un gain réel de précision ou de charge cognitive et si son référent reste récupérable sans dépendre de la mémoire implicite de l’agent ou de l’auteur.

La distinction entre vue publique, vue de synthèse et travail effectif est utile mais non rigide : la quantité de prose n’est pas le critère ; l’auditabilité sémantique l’est.

## 3. Routage et autorité documentaire

Ne pas confondre l’endroit où l’on commence avec ce qui fait autorité. Un point d’entrée vivant local route vers l’autorité applicable ; il ne l’acquiert pas par sa seule fonction d’accueil.

Avant d’agir, distinguer :

- les autorités transverses : cadre canonique et décisions de rang encore applicables ;
- l’autorité locale courante : décision humaine, protocole, spécification ou issue explicitement identifiée par le point d’entrée vivant du chantier ;
- les résultats qualifiés et synthèses validées, qui établissent ce qu’ils portent dans leur périmètre sans devenir automatiquement une autorisation d’action ;
- les explorations et états datés ;
- les archives et la provenance historique.

Une décision humaine plus récente explicitement applicable peut amender une règle ou une décision antérieure. Ni la date, ni le numéro d’issue, ni le nom du fichier ne suffisent à établir ce rang.

Ne pas modifier une archive ou un état daté pour simuler une cohérence actuelle. Corriger la porte d’entrée vivante et conserver la généalogie.

### 3.1 Archives conversationnelles comme corpus empirique

Une archive conversationnelle n’est pas une autorité scientifique, doctrinale ou opérationnelle par sa seule existence. Elle peut néanmoins constituer un **corpus empirique de trajectoires** : apparition d’un problème, hypothèses successives, décisions, corrections, erreurs de portée, effets observés, contre-cas et déplacements de question.

Lorsqu’une archive conversationnelle est utilisée pour instruire une règle, une décision ou une reprise :

- distinguer ce qui y est seulement proposé de ce qui a été décidé ou effectivement appliqué ;
- confronter les affirmations pertinentes à l’état matériel et aux autorités courantes du dépôt lorsque cette confrontation est possible ;
- utiliser la conversation pour étudier les transformations du raisonnement et les effets d’une règle, pas pour contourner les qualifications présentes ;
- ne pas exclure une promotion au seul motif que l’observation provient d’une conversation, mais ne pas promouvoir non plus une règle sur la seule force rhétorique ou la répétition de cette conversation.

Une archive peut donc soutenir une promotion lorsqu’elle fournit une trajectoire suffisamment discriminante et que la portée proposée reste compatible avec les effets observables et l’état courant du dépôt.

## 4. Règles scientifiques et méthodologiques

- Identifier ce qui est effectivement testé, sous quelle transformation, dans quel régime et avec quelles limites.
- Pour un énoncé de constance ou de stabilisation, rendre explicites au minimum la cible, la transformation, le régime, l’échelle / le schéma / le modèle pertinents, la tolérance et la condition de rupture.
- Ne pas confondre propriété de la cible, qualité de l’accès et mode de constitution.
- Distinguer résultat, soutien probatoire et verdict.
- Borner toute conclusion au domaine réellement instruit.
- Employer d’abord le vocabulaire standard du domaine ; les catégories internes restent secondaires.
- Distinguer chemin physique, expérimental, métrologique, computationnel, inférentiel, historique ou représentationnel lorsque cette différence change l’argument.
- Préserver provenance, temporalité et statut des résultats.
- Conserver les résultats négatifs, refus, suspensions, blocages et limites lorsqu’ils sont pertinents.
- Une exploration peut proposer ; elle ne devient pas une règle durable sans qualification et validation.
- N’ajouter une couche, une subdivision ou un document durable que s’il apporte un gain discriminant ou de contrôle supérieur à son coût de maintenance.

### 4.1 Localiser avant d’intervenir

Lorsqu’une correction est envisagée mais que la cause ou le niveau fonctionnel du défaut n’est pas encore établi, identifier d’abord **le niveau qui produit réellement le comportement** par le contrôle discriminant le moins coûteux, puis redescendre vers l’intervention minimale.

Ne pas dézoomer par principe. S’arrêter dès qu’un discriminant local relie suffisamment le défaut, sa portée et la correction minimale, notamment lorsque la cause est déjà reproduite, localisée et réversible sans modifier la cible scientifique, le contrat probatoire ou une ressource protégée.

Le raisonnement systémique sert à choisir le bon niveau d’analyse ; il ne remplace pas le test local une fois ce niveau identifié.

### 4.2 Couplage probatoire des représentations indirectes

Lorsqu’une propriété d’un objet réel est inférée à partir d’un toy, mock, proxy, fallback, harnais, conversion, extraction ou autre représentation indirecte, vérifier que le dispositif **exerce effectivement la propriété qu’il prétend qualifier** avant de généraliser son résultat.

Cette vérification doit être proportionnée. Elle n’impose pas un contre-test supplémentaire pour une propriété directement observable ni lorsqu’une équivalence pertinente est déjà établie sans ambiguïté. Elle ne justifie pas non plus de consommer une ressource rare lorsqu’une source, une trace ou un contrôle moins coûteux possède déjà le pouvoir discriminant nécessaire.

### 4.3 Portée et prudence de promotion

Promouvoir une règle et étendre son périmètre sont deux décisions distinctes. Une règle peut être suffisamment soutenue pour un régime local, réversible et observable sans être qualifiée pour un autre domaine.

La charge de preuve avant promotion ou extension doit être proportionnée notamment à :

- l’autorité supplémentaire accordée à la règle ;
- l’élargissement de domaine ou de portée demandé ;
- la gravité d’un faux positif ou d’un faux négatif ;
- la réversibilité de ses effets ;
- sa capacité à modifier une décision scientifique, méthodologique ou humaine plutôt qu’à seulement améliorer une représentation.

Ne pas appliquer une retenue uniforme à toutes les règles : une pratique locale, informative et facilement réversible peut être essayée plus tôt qu’une règle transversale, bloquante ou susceptible de modifier un verdict.

## 5. Science, machine et interprétation

Toujours conserver la séparation :

```text
calcul
≠ résultat machine
≠ qualification technique
≠ résultat scientifique
≠ interprétation scientifique
≠ conséquence philosophique
≠ usage éditorial
```

Un vert machine établit au plus ce que le contrôle a effectivement observé. Il ne valide pas un résultat scientifique. Un rouge machine peut provenir du harness, de la spécification ou de l’environnement ; reproduire sa cause avant de l’attribuer au candidat scientifique.

Un changement de sampler, d’oracle, de tolérance, de représentation ou d’infrastructure ne constitue pas par lui-même une modification scientifique. S’il peut changer la cible, le posterior, les données, le prior ou l’interprétation, il doit être traité comme un amendement scientifique distinct.

Les diagnostics transitoires d’un run restent dans ses sorties, journaux ou issue computationnelle ; ne pas les recopier dans les README d’accueil.

## 6. Route active du cycle 7

Le [README du cycle 7](02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/README.md) est la porte locale avant toute reprise cosmologique.

Deux lignes sont actuellement indépendantes :

- `C7-C1 / X(z) / SCI-1` → ancrage opérationnel actif : [issue #119](https://github.com/AkselBoursier/constantes_effectives_stabilisees/issues/119) ;
- `C7-GAL / C0` → ancrage opérationnel actif : [issue #120](https://github.com/AkselBoursier/constantes_effectives_stabilisees/issues/120).

Ne jamais appeler `C7-GAL` « C7-C1 GAL ». Aucun état MCMC, aucune porte B1/SCI-1 et aucune autorisation de calcul ne se transfèrent de C7-C1 vers C7-GAL. Réciproquement, une dette matérielle ou une porte G2 de C7-GAL ne modifie pas SCI-1.

Les permissions, blocages et états mouvants ne sont pas recopiés ici : les lire dans le README du cycle 7 puis dans l’issue active de la ligne. Ne pas reconstituer l’autorité depuis les anciennes issues seules.

## 7. Documents, preuves et checkpoints de reprise

Un document destiné à représenter l’état courant est mis à jour sous un nom stable par défaut. Git porte son historique. Ne pas créer une nouvelle version de fichier pour chaque changement sans raison propre.

### 7.1 État courant et généalogie

Un document courant parle d’abord de son objet tel qu’il doit être compris dans l’état présent du travail. Il n’a pas à raconter ses anciennes formulations pour justifier la formulation actuelle.

Par défaut, ne pas écrire dans un document courant des phrases du type « auparavant X, maintenant Y » ou des négations d’un état antérieur absent du document. Si une ancienne formulation n’est plus nécessaire à la compréhension de l’objet présent, la retirer du document courant plutôt que la conserver comme pseudo-historique.

La généalogie des transformations appartient par défaut à Git, aux diffs, aux commits, aux PR, aux issues, aux checkpoints, aux archives ou aux documents dont la fonction est explicitement historique, comparative ou décisionnelle. Ces supports conservent le passé ; le document courant conserve l’état présent.

Préférer la mise à jour d’un document existant sous identité stable lorsque sa fonction reste la même. Créer un nouveau document seulement lorsqu’une fonction, une pièce probatoire, un état comparable ou un objet réellement nouveau exige une identité propre.

Cette règle ne s’applique pas aux pièces dont l’objet est précisément temporel ou comparatif : changelog, rapport de décision, pré-enregistrement, protocole exécuté, état daté, archive, généalogie ou comparaison explicite.

Un protocole exécuté, une extraction, un pré-enregistrement, un résultat ou une décision dont l’état doit rester comparable est conservé comme pièce distincte.

Avant de supprimer, déplacer ou déclasser un document existant, vérifier au minimum son contenu unique, ses dépendances et sa fonction scientifique ou probatoire.

Ne pas créer de registre central supplémentaire lorsqu’un README local, une issue active ou Git porte déjà la fonction nécessaire. Ne créer un `AGENTS.md` local que si des règles locales diffèrent réellement du noyau racine ; un fichier local affine le parent, il ne doit pas le recopier intégralement.

Pour un chantier long ou complexe susceptible de perdre son état de reprise, conserver un **ancrage opérationnel principal identifiable** : PR lorsqu’une PR porte effectivement le travail, issue lorsqu’une issue en est l’ancrage, ou autre support existant approprié.

À l’intérieur de cet ancrage, créer des **checkpoints successifs et traçables** lorsqu’un changement modifie réellement l’état de reprise. Un checkpoint représente un état daté du chantier ; il n’est pas réécrit pour représenter un état ultérieur, sauf correction factuelle explicitement signalée.

Un checkpoint n’est pas un journal exhaustif. Il conserve seulement ce qui est nécessaire à une reprise sûre :

- objet travaillé, en langage naturel ;
- acquis établis et limites de portée ;
- questions, blocages ou décisions encore ouverts ;
- inférences explicitement interdites ou non établies lorsqu’elles comptent ;
- prochaine opération réellement retenue ;
- quelques ancres de provenance suffisantes pour retrouver les preuves.

Créer un nouveau checkpoint seulement lorsqu’un changement substantiel justifie un nouvel état de reprise. Ne pas dupliquer automatiquement le même checkpoint dans plusieurs supports. La non-prolifération porte sur la multiplication des ancrages, des supports redondants et des checkpoints sans changement d’état ; elle ne justifie pas l’écrasement d’états antérieurs nécessaires à la traçabilité.

## 8. Issues, interventions humaines et état du travail

Une issue porte une instruction bornée, ses décisions et les étapes qui changent réellement l’état du travail. Elle ne doit pas devenir une copie exhaustive de la conversation.

Pour un chantier borné, préférer un ancrage opérationnel principal identifiable. Consigner un changement lorsqu’il modifie substantiellement la question, le périmètre, un résultat, un blocage durable, une validation, la décision suivante, l’ouverture, le remplacement, la suspension, la clôture ou la réouverture du travail.

Ne pas créer de mise à jour documentaire pour chaque action technique. Ne pas inférer automatiquement l’issue active depuis un numéro, une date ou un label.

### 8.1 Idées pertinentes hors périmètre

Lorsqu’une idée mérite une attention ultérieure mais déborde du chantier courant, ne pas la poursuivre automatiquement et ne pas la laisser dépendre de la mémoire de la conversation.

Avant de reprendre le chantier principal, **matérialiser sa capture** dans le support le plus léger qui permette un suivi réel : issue distincte si elle constitue une question ou une dette autonome, checkpoint si elle modifie l’état du chantier courant, ou simple pointeur si un ancrage existe déjà.

La capture doit préciser au minimum : ce qui mérite d’être repris, pourquoi ce n’est pas traité maintenant, et sous quelle condition ou à quel palier la question doit être réouverte.

**Capture = bloquante avant reprise si l’idée serait autrement perdue. Résolution = conditionnellement bloquante.** Résoudre immédiatement seulement si la question conditionne la validité, la traçabilité ou la prochaine action du chantier courant, ou si sa résolution est strictement bornée, rapide et n’ouvre pas un nouveau chantier. Sinon, la différer explicitement avec suivi.

Ne pas transformer chaque pensée latérale en issue : la matérialisation est justifiée lorsqu’il existe une valeur de reprise identifiable, pas par la seule apparition d’une idée.

Une intervention humaine ne doit pas être transformée automatiquement en ordre. Lorsque cela change l’action, distinguer au moins : observation, hypothèse, proposition, préférence, décision et autorisation. Une proposition reste à évaluer intellectuellement et méthodologiquement ; une décision ou autorisation explicite s’applique dans le périmètre qu’elle établit.

Avant d’engager une tâche longue, vérifier qu’un point de reprise suffisamment consolidé existe si la perte de contexte serait coûteuse. À un palier de consolidation ou avant de clore une longue séquence, effectuer un autocontrôle borné portant sur : intelligibilité des objets, traçabilité suffisante, respect du périmètre et absence de nouvel artefact injustifié. Ne pas maintenir par défaut une boucle d’auto-réflexivité permanente parallèle au travail principal.

## 9. Passages entre volets ou cycles

Physique, computation, méthodologie et philosophie sont séparées par défaut sans être hermétiques.

Lorsqu’un passage est nécessaire :

```text
identifier la question qui le justifie
→ relier les dossiers concernés
→ préciser ce qui est transféré et ce qui ne l’est pas
→ ré-instruire dans le domaine compétent
→ ne jamais propager automatiquement le verdict
```

Une dette n’est transférée scientifiquement que si le nouveau terrain offre un accès, un discriminant ou une structure explicative réellement différente. Sinon, la qualifier simplement de différérée ou suspendue.

## 10. Git et mutations

- Utiliser une branche ou un worktree dédié pour toute mutation substantielle.
- Garder une PR bornée ; ne pas mélanger des modifications indépendantes sans nécessité.
- Ne pas modifier `main` directement lorsqu’une PR permet l’audit.
- Ne pas réécrire un état historique pour simuler une cohérence actuelle.
- Vérifier indépendamment une proposition ancienne avant de la réactiver.
- Préférer une correction locale à une restructuration générale.
- Une CI verte est un contrôle technique borné, pas une autorisation de merge ni une validation scientifique.
- Aucun merge sans autorisation humaine explicite et contrôle final du périmètre.
