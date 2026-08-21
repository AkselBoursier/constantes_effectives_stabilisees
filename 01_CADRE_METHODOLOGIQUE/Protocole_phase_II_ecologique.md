# Protocole expérimentateur — Phase II écologique

## Statut

Document réservé à l'expérimentateur. Ne pas le fournir à l'agent testé.

La Phase I fermée a produit deux réponses par condition :
- organisation fonctionnelle D17 : 42/48 puis 42/48 ;
- fiches + relations D61 : 42/48 puis 40/48 ;
- zéro erreur critique dans les quatre réponses ;
- D17 contient environ 28,1 % de matière d'entrée en moins.

Cette Phase II ne reteste donc pas la simple extraction d'un dossier. Elle teste l'intégration d'une surface de guidage dans un dépôt réel, avec navigation bornée.

## Base commune

Dépôt :
`AkselBoursier/constantes_effectives_stabilisees`

Base Git commune :
`main@c9deaf1fe86b742d9227f0385e975809f64dc9bd`

La branche d'audit #139 n'est jamais une base expérimentale.

Branche temporaire réutilisée séquentiellement :
`reprise/controle-20260821`

Entre les deux conditions, le ref de cette branche doit être **forcé de nouveau exactement sur le SHA de main ci-dessus** avant d'injecter la seconde condition. Ainsi, la seconde incarnation n'hérite pas de l'historique visible de la première.

## Assignation pré-enregistrée

Matériau de tirage :
`c9deaf1fe86b742d9227f0385e975809f64dc9bd|af68f350d6d74c584d894e59df5689d4f043e32c|phaseII`

`SHA256 = 55b56379db57a4eff68938dbbc41c0717ef6d0f8473cd8540c2c0da26c3f7550`

Convention pré-déclarée :
- parité 0 → première condition = `FICHES_PLUS_RELATIONS` ;
- parité 1 → première condition = `ORGANISATION_FONCTIONNELLE`.

Résultat :
`PARITE = 0`
`PREMIERE_CONDITION = FICHES_PLUS_RELATIONS`
`SECONDE_CONDITION = ORGANISATION_FONCTIONNELLE`

Cette clé ne doit pas être communiquée à l'agent avant gel de sa réponse.

## Variable expérimentale

Les deux incarnations de la branche ont exactement :
- le même ancêtre `main@c9deaf1fe86b742d9227f0385e975809f64dc9bd` ;
- le même nom de branche ;
- le même point d'entrée `00_REPRISE/README.md` ;
- les mêmes quatre cas ;
- la même consigne externe ;
- les mêmes règles de navigation ;
- les mêmes fichiers du dépôt principal.

Une seule pièce diffère :
`00_REPRISE/guide_reprise.md`.

Condition `FICHES_PLUS_RELATIONS` :
contenu dérivé de `Dossier_61.md`.

Condition `ORGANISATION_FONCTIONNELLE` :
contenu dérivé de `Dossier_17.md`.

Aucun nom de fichier ne révèle la condition.

## Régime de navigation

L'agent doit :
1. rester sur le ref fourni pour les fichiers ;
2. commencer par `00_REPRISE/README.md`, qui lui demande de lire `AGENTS.md`, `README.md` et `00_REPRISE/guide_reprise.md` ;
3. consulter ensuite les cas et les pièces du dépôt utiles ;
4. pouvoir consulter une issue explicitement liée depuis un fichier du ref seulement si cela est nécessaire à la décision ;
5. produire un journal des chemins consultés dans leur ordre.

L'agent ne doit pas :
- consulter une PR ;
- changer de branche ou de tag ;
- consulter l'historique Git ou les commits pour reconstruire l'autre condition ;
- chercher #139, le prototype, D17/D61, le protocole ou la grille ;
- muter le dépôt.

Un accès à #139, à la branche d'audit, à une autre condition ou à un artefact de scoring entraîne `CONTAMINATION = OUI`.

Une consultation d'une issue active explicitement routée par le ref n'est pas une contamination.

## Cas écologiques

Les quatre cas sont homologues aux quatre tâches de Phase I, mais demandent désormais une confrontation au dépôt :

1. une synthèse correcte pour C7-C1 proposée ensuite comme état du Cycle 7 entier ;
2. une pratique de checkpoint utilisée trois fois sans incident et proposée comme obligatoire pour tous les cycles ;
3. la résolution du rouge de persistance C7-C1 proposée comme source d'une règle/outillage générique ;
4. un audit ancien local C7-C1 proposé comme soutien au niveau du Cycle 7 devenu explicitement bifurqué C7-C1 / C7-GAL.

## Mesures

### A. Fidélité décisionnelle
Même logique que la grille Phase I :
score séparé sur 48.

### B. Navigation écologique
10 critères sur 2 points :
score séparé sur 20.

Ne pas fusionner mécaniquement A et B : une réponse peut être correcte tout en naviguant mal, ou inversement.

### C. Mesures descriptives
- nombre de fichiers distincts déclarés comme consultés ;
- nombre d'issues consultées ;
- nombre de détours non nécessaires ;
- présence/absence d'un retour à la source disciplinaire après usage du guide ;
- longueur de la réponse ;
- contamination éventuelle.

## Série minimale

Deux chats éphémères neufs :
- premier agent : première incarnation de la branche ;
- deuxième agent : seconde incarnation.

Même modèle/configuration si possible.
Aucun échange préalable.
Réponse brute gelée avant toute relance.

## Gel de série

Dès que la première réponse est obtenue :
- le contenu de sa branche/commit est figé comme condition A de cette série ;
- aucune correction du prompt, des cas ou de la grille n'est rétroactive ;
- toute correction ouvre une nouvelle série.

Après gel de la première réponse :
1. enregistrer le SHA exact de la première incarnation ;
2. forcer `reprise/controle-20260821` sur `main@c9deaf1fe86b742d9227f0385e975809f64dc9bd` ;
3. recréer exactement les fichiers communs ;
4. remplacer uniquement `guide_reprise.md` par l'autre condition ;
5. enregistrer le SHA exact de la seconde incarnation ;
6. lancer un chat éphémère neuf.

## Interprétation

Phase II soutient un gain écologique de l'organisation fonctionnelle seulement si, à fidélité au moins non inférieure :
- la navigation est plus courte ou plus proportionnée ;
- les changements de niveau sont mieux identifiés ;
- le retour aux sources factuelles est conservé ;
- les conditions de silence/arrêt restent visibles ;
- aucune contamination ou autorité fictive n'augmente.

Un meilleur score final avec davantage de détours n'est pas automatiquement un gain de guidage.
