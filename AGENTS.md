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

Un protocole exécuté, une extraction, un pré-enregistrement, un résultat ou une décision dont l’état doit rester comparable est conservé comme pièce distincte.

Avant de supprimer, déplacer ou déclasser un document existant, vérifier au minimum son contenu unique, ses dépendances et sa fonction scientifique ou probatoire.

Ne pas créer de registre central supplémentaire lorsqu’un README local, une issue active ou Git porte déjà la fonction nécessaire. Ne créer un `AGENTS.md` local que si des règles locales diffèrent réellement du noyau racine ; un fichier local affine le parent, il ne doit pas le recopier intégralement.

Pour un chantier long ou complexe susceptible de perdre son état de reprise, conserver un **checkpoint unique et traçable** dans l’ancrage opérationnel déjà utilisé par ce chantier : commentaire de PR lorsqu’une PR porte effectivement le travail, commentaire d’issue lorsqu’une issue en est l’ancrage, ou autre support existant approprié.

Un checkpoint n’est pas un journal exhaustif. Il conserve seulement ce qui est nécessaire à une reprise sûre :

- objet travaillé, en langage naturel ;
- acquis établis et limites de portée ;
- questions, blocages ou décisions encore ouverts ;
- inférences explicitement interdites ou non établies lorsqu’elles comptent ;
- prochaine opération réellement retenue ;
- quelques ancres de provenance suffisantes pour retrouver les preuves.

Mettre à jour le même checkpoint lorsqu’un changement modifie réellement l’état de reprise. Ne pas dupliquer automatiquement le même état dans plusieurs supports.

## 8. Issues, interventions humaines et état du travail

Une issue porte une instruction bornée, ses décisions et les étapes qui changent réellement l’état du travail. Elle ne doit pas devenir une copie exhaustive de la conversation.

Pour un chantier borné, préférer un ancrage opérationnel unique. Consigner un changement lorsqu’il modifie substantiellement la question, le périmètre, un résultat, un blocage durable, une validation, la décision suivante, l’ouverture, le remplacement, la suspension, la clôture ou la réouverture du travail.

Ne pas créer de mise à jour documentaire pour chaque action technique. Ne pas inférer automatiquement l’issue active depuis un numéro, une date ou un label.

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
