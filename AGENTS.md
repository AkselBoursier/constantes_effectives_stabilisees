# Guide de travail pour les agents

Ce fichier décrit comment intervenir dans le dépôt sans confondre état scientifique, calcul, documentation et décision. Lire d’abord le présent fichier, puis le point d’entrée du domaine ou du cycle concerné.

## 1. Mission et autorité

Le projet étudie ce que les sciences peuvent soutenir lorsqu’elles qualifient de constante une grandeur, une relation, une valeur ou une structure.

Deux questions publiques organisent le travail :

1. Comment les sciences établissent-elles, utilisent-elles et déplacent-elles la frontière entre ce qui varie et ce qui tient ?
2. Par quelles structures, opérations et chemins de détermination un maintien devient-il opératoire ou affirmable dans un régime, et que change cette reconstruction pour l’enquête scientifique ?

L’agent peut inspecter, comparer, calculer, falsifier, proposer des corrections et exécuter les opérations techniques autorisées dans son périmètre. Une décision humaine reste obligatoire pour les frontières scientifiques ou irréversibles : question de recherche, modèle, données, prior, paramétrisation scientifique, interprétation, seuil d’évidence, promotion durable et merge.

Une intervention humaine n’est pas automatiquement un ordre. Lorsque cela change l’action, distinguer observation, hypothèse, proposition, préférence, décision et autorisation. Une proposition doit être confrontée au dépôt et aux preuves applicables avant d’être transformée en règle ou en mutation. Une décision ou autorisation explicite s’applique dans son périmètre sans être neutralisée par cette règle et sans être généralisée silencieusement au-delà de ce périmètre.

## 2. Parcours minimal et règles locales

Pour une tâche locale :

1. lire le présent `AGENTS.md` ;
2. si le répertoire cible contient un `AGENTS.md`, le lire avant d’agir : il affine le parent pour cette région ;
3. lire le point d’entrée humain du domaine ou du cycle ;
4. entrer dans le README ou document local indiqué ;
5. lire l’issue ou la décision qui borne la tâche, lorsqu’elle existe ;
6. consulter le [cadre méthodologique](01_CADRE_METHODOLOGIQUE/refondation-du-domaine.md) ou le [glossaire](GLOSSAIRE.md) seulement si la tâche l’exige.

Routage local actuellement matérialisé :

- [méthodologie, méta-règles et shadow learning](01_CADRE_METHODOLOGIQUE/AGENTS.md) ;
- [cycles physiques](02_CYCLES_PHYSIQUES/AGENTS.md) ;
- [philosophie](06_PHILOSOPHIE/AGENTS.md).

Un `AGENTS.md` local hérite du noyau parent et précise un régime de travail ; il ne transforme pas automatiquement une règle locale en règle générale. Inversement, le fait qu’une règle soit née localement ne prouve pas qu’elle doive y rester : toute extension de portée doit être instruite séparément.

Ne pas précharger l’intégralité du corpus par défaut. La provenance détaillée se consulte lorsqu’une décision, une contradiction, une révision ou une promotion de règle l’exige.

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
- N’ajouter une couche, une subdivision ou un document durable que s’il apporte un gain discriminant ou de contrôle supérieur à son coût de maintenance. Cette règle n’est pas un veto à la création d’un objet qui porte une fonction réelle non couverte ailleurs.

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

Le [README du cycle 7](02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/README.md) est la porte locale avant toute reprise cosmologique, après lecture du [AGENTS des cycles physiques](02_CYCLES_PHYSIQUES/AGENTS.md).

Deux lignes sont actuellement indépendantes :

- `C7-C1 / X(z) / SCI-1` → ancrage opérationnel actif : [issue #119](https://github.com/AkselBoursier/constantes_effectives_stabilisees/issues/119) ;
- `C7-GAL / C0` → ancrage opérationnel actif : [issue #120](https://github.com/AkselBoursier/constantes_effectives_stabilisees/issues/120).

Ne jamais appeler `C7-GAL` « C7-C1 GAL ». Aucun état MCMC, aucune porte B1/SCI-1 et aucune autorisation de calcul ne se transfèrent de C7-C1 vers C7-GAL. Réciproquement, une dette matérielle ou une porte G2 de C7-GAL ne modifie pas SCI-1.

Les permissions, blocages et états mouvants ne sont pas recopiés ici : les lire dans le README du cycle 7 puis dans l’issue active de la ligne. Ne pas reconstituer l’autorité depuis les anciennes issues seules.

## 7. Documents et preuves

Un document destiné à représenter l’état courant est mis à jour sous un nom stable par défaut. Git porte son historique. Ne pas créer une nouvelle version de fichier pour chaque changement sans raison propre.

Un protocole exécuté, une extraction, un pré-enregistrement, un résultat ou une décision dont l’état doit rester comparable est conservé comme pièce distincte.

Avant de supprimer, déplacer ou déclasser un document existant, vérifier au minimum son contenu unique, ses dépendances et sa fonction scientifique ou probatoire.

Ne pas créer de registre central supplémentaire lorsqu’un README local, une issue active, un `AGENTS.md` local ou Git porte déjà la fonction nécessaire. Créer un `AGENTS.md` local lorsqu’une région possède réellement des règles, routes ou régimes de travail qu’un agent doit connaître avant d’agir et qui ne doivent pas encombrer ou généraliser le noyau racine.

## 8. Issues et état du travail

Une issue porte une instruction bornée, ses décisions et les étapes qui changent réellement l’état du travail. Elle ne doit pas devenir une copie exhaustive de la conversation.

Pour un chantier borné, préférer un ancrage opérationnel principal identifiable. Consigner un changement lorsqu’il modifie substantiellement la question, le périmètre, un résultat, un blocage durable, une validation, la décision suivante, l’ouverture, le remplacement, la suspension, la clôture ou la réouverture du travail.

Ne pas créer de mise à jour documentaire pour chaque action technique. Ne pas inférer automatiquement l’issue active depuis un numéro, une date ou un label.

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
- Préférer une correction locale à une restructuration générale lorsque le niveau causal est réellement local ; dézoomer si les répétitions indiquent un défaut de niveau supérieur.
- Une CI verte est un contrôle technique borné, pas une autorisation de merge ni une validation scientifique.
- Aucun merge sans autorisation humaine explicite et contrôle final du périmètre.
