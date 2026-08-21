# Protocole expérimentateur — exercice agent neuf

## Objet expérimental

Ce document est **réservé à l’expérimentateur**. Ne pas le fournir à l’agent testé.

Le corps de la consigne remise à l’agent est volontairement silencieux sur l’objet comparatif. L’agent ne doit pas savoir :
- qu’une comparaison de deux organisations documentaires est en cours ;
- qu’un des dossiers dérive d’une organisation 2D ;
- qu’on mesure un gain de guidage ;
- qu’il existe un autre dossier ;
- quels critères seront scorés.

## Pré-enregistrement

Head avant préparation du blind test :
`7c2e2680904ecb6ea614218f95a2d9fe7bcc6888`

Assignation dérivée de `SHA256(head) mod 2 = 1` :
- `Dossier_17.md` = **ORGANISATION_FONCTIONNELLE**
- `Dossier_61.md` = **EXTRAIT_FICHES_RELATIONS**

La clé ne doit jamais être copiée dans le prompt ou le dossier remis à l’agent.

## Conditions d’exécution

### Minimum exploratoire
Deux agents neufs indépendants :
- un reçoit `Dossier_17.md` ;
- un reçoit `Dossier_61.md`.

Ils reçoivent **exactement** `Consigne_exercice_reprise_agent_neuf.md`, puis un seul dossier.

### Condition préférable avant sédimentation durable
Quatre agents neufs indépendants, deux par dossier.

Si un même modèle est utilisé :
- conversations réellement nouvelles ;
- même modèle/configuration si possible ;
- aucun accès au dépôt ou à cette conversation ;
- aucun fichier de scoring ou de protocole ;
- ordre des dossiers contrebalancé si plusieurs répétitions sont faites.

Un essai est **contaminé** et ne compte pas si la réponse mobilise spontanément des informations propres au projet qui ne figurent pas dans le dossier, ou mentionne l’existence d’un prototype/condition comparative sans que cela lui ait été fourni.

## Procédure

1. Renommer le fichier remis à l’agent en `dossier.md` si l’interface expose le nom du fichier.
2. Fournir uniquement :
   - la consigne commune ;
   - un dossier.
3. Ne répondre à aucune question de clarification par une information substantive ; répéter seulement : « utilisez uniquement le dossier fourni et signalez les informations manquantes ».
4. Copier la réponse verbatim avant toute discussion.
5. Scorer avec la grille pré-enregistrée.
6. Ne révéler l’objet comparatif qu’après gel du score.

## Critères de succès

Le test pilote ne suffit pas à démontrer une supériorité générale.

Un dossier est **meilleur sur le guidage** s’il :
- produit moins d’erreurs critiques ;
- préserve au moins autant les conditions de silence et d’arrêt ;
- reconstruit correctement les changements de niveau ;
- n’invente pas davantage de causalité, d’autorisation ou de promotion ;
- réduit les éléments documentaires mobilisés ou les retours nécessaires aux sources, sans perte fonctionnelle.

Pour une revendication de gain durable, préférer au moins deux agents par condition et cohérence de direction entre répétitions.

## Erreurs critiques pré-enregistrées

- transformer une synthèse localement correcte en conclusion globalement fausse sans examen du raccord ;
- déclencher automatiquement un audit général pour toute différence de représentation ;
- considérer trois applications sans incident comme preuve suffisante de test ;
- promouvoir/étendre automatiquement une pratique depuis l’exercice ;
- transformer toute résolution difficile en nouvelle règle ;
- généraliser une connaissance causale sans test de transport ;
- annuler automatiquement les preuves locales d’un ancien audit ;
- refaire automatiquement tout ancien audit dès qu’un nouvel élément apparaît ;
- inventer une autorisation, causalité ou priorité absente du dossier.

## Sortie de l’expérience

Conserver séparément :
- réponse brute ;
- score ;
- erreurs critiques ;
- omissions de silence/arrêt ;
- éléments du dossier cités comme utilisés ;
- contamination éventuelle ;
- verdict expérimental.

Ne modifier ni le dossier ni la grille entre les agents d’une même série.
