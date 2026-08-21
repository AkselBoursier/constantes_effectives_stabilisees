# Matrice assignée — Tâche S — condition 7A

## Statut

Surface expérimentale de contrôle. Les identifiants servent de pointeurs ; ils ne sont pas des autorités scientifiques et ne donnent aucune réponse sur le Cycle 10.

## Unités fonctionnelles

### R-004 — routage et autorité

**Fonction.** Empêcher confusion entre accueil, provenance, visibilité et autorité applicable.  
**Déclencheur.** Toute reprise où plusieurs documents ou états peuvent prétendre gouverner la tâche.  
**Contrôle.** Un point d'entrée route vers l'autorité ; date, titre, numéro ou visibilité ne suffisent pas à conférer l'autorité.  
**Silence/arrêt.** Si le point d'entrée est explicitement aussi la décision qui gouverne le cas, aucun détour supplémentaire n'est requis.  
**Décision permise.** Justifier quelle surface gouverne effectivement la qualification courante.

### R-005 — statut documentaire

**Fonction.** Préserver à la fois validité locale d'une pièce ancienne et état courant récupérable.  
**Déclencheur.** Une pièce datée ou ancienne peut être prise pour l'état courant.  
**Contrôle.** Un document peut rester scientifiquement/probatoirement valide sans représenter l'état courant ; ne pas réécrire rétroactivement son corps pour le rendre contemporain.  
**Silence/arrêt.** Document clairement historique sans risque de lecture courante.  
**Décision permise.** Conserver le résultat local et requalifier seulement son rang ou son rôle actuel si nécessaire.

### R-001 — signal machine et science

**Fonction.** Empêcher qu'un signal technique soit promu en conclusion scientifique.  
**Déclencheur.** Sortie machine, vert CI, scan, convergence numérique ou contrôle technique utilisé pour soutenir une propriété scientifique.  
**Contrôle.** Un signal technique n'établit que ce que le dispositif a réellement observé.  
**Silence/arrêt.** Aucune prétention au-delà de la propriété directement observée.  
**Décision permise.** Distinguer sortie machine, qualification technique et éventuel résultat scientifique.

### R-025 — constance et stabilisation

**Fonction.** Empêcher qu'un maintien produit par un mécanisme, une robustesse d'accès ou une stabilisation d'estimation devienne automatiquement constance de la cible.  
**Déclencheur.** Un vocabulaire de stabilité, maintien, quasi-fixité ou stabilisation est utilisé pour parler de constance.  
**Contrôle.** Distinguer constance de la cible, stabilisation d'accès/estimateur/régime et maintien produit par constitution/mécanisme.  
**Silence/arrêt.** Le vocabulaire disciplinaire sépare déjà sans ambiguïté les niveaux.  
**Décision permise.** Qualifier explicitement lequel des maintiens est réellement établi.

### R-026 — énoncé indexé de maintien

**Fonction.** Rendre bornée et réfutable toute attribution de constance, stabilité ou variation.  
**Déclencheur.** Une proposition affirme qu'une cible tient, varie ou ne varie pas.  
**Contrôle.** Indexer par cible, transformation pertinente, régime/domaine, échelle-schéma-modèle si pertinent, tolérance/ordre et condition de rupture/refus.  
**Silence/arrêt.** Ne pas remplir mécaniquement un champ sans sens disciplinaire ; certaines coordonnées peuvent être implicites et non ambiguës.  
**Décision permise.** Énoncé local dont le domaine et la rupture sont explicitables.

### R-027 — cible, accès, constitution

**Fonction.** Empêcher l'attribution directe à l'objet d'une propriété de l'accès ou d'un mécanisme de constitution, sans perdre leurs rétroactions réelles.  
**Déclencheur.** Objet/cible, mesure/reconstruction et mécanisme explicatif sont reliés dans l'argument.  
**Contrôle.** Les trois dimensions sont distinctes ; elles peuvent se contraindre et se reformuler mutuellement ; aucun ordre universel n'est imposé.  
**Silence/arrêt.** Une seule couche est matériellement en jeu.  
**Décision permise.** Dire exactement quelle dimension le résultat modifie et quelles transitions exigent un argument supplémentaire.

### R-028 — dimension de l'enquête et portée

**Fonction.** Empêcher qu'une enquête riche devienne une thèse plus large que les preuves.  
**Déclencheur.** Formation, constitution, accès, histoire, mécanisme ou comparaison servent de base à une conclusion.  
**Contrôle.** Distinguer ce qui est étudié de la portée physique, épistémique, interprétative ou éventuellement non engagée de l'énoncé final.  
**Silence/arrêt.** Aucune extrapolation au-delà de l'opération locale.  
**Décision permise.** Une portée plus étroite peut conserver intégralement un résultat local.

### R-029 — typage des chemins et dépendances

**Fonction.** Rendre visibles les dépendances qui changent causalité, comparabilité ou portée.  
**Déclencheur.** Le type de chemin qui produit/relie une conclusion modifie l'argument.  
**Contrôle.** Typer selon le domaine : physique, inférentiel, computationnel, représentationnel, historique/de réalisation ou autre catégorie disciplinaire justifiée.  
**Silence/arrêt.** Si le type de chemin ne change pas l'argument : `NON_PERTINENT`; s'il ne peut être établi : `NON_ETABLI`.  
**Décision permise.** Ne pas convertir un chemin de scan, de représentation ou d'inférence en trajectoire physique sans argument.

### R-030 — vocabulaire disciplinaire premier

**Fonction.** Éviter redescription interne, faux concept transverse et circularité explicative.  
**Déclencheur.** Un terme transversal du projet est utilisé pour qualifier un phénomène disciplinaire.  
**Contrôle.** Décrire d'abord le phénomène dans le vocabulaire du domaine ; conserver le terme transverse seulement s'il ajoute un gain discriminant.  
**Silence/arrêt.** Le terme interne n'ajoute aucune fonction ou écrase une notion disciplinaire plus précise.  
**Décision permise.** Retirer un ancien label sans effacer le phénomène ou le résultat qu'il décrivait.

### R-031 — résultat, soutien, verdict

**Fonction.** Empêcher qu'un nombre, une reproduction, une borne, une concordance ou un résultat conditionnel soit automatiquement promu en verdict.  
**Déclencheur.** Toute synthèse de résultat ou transition entre niveaux probatoires.  
**Contrôle.** Conserver séparés : résultat/constat ; soutien probatoire sous conditions ; verdict scientifique autorisé ; interprétation/décision programmatique.  
**Silence/arrêt.** Un seul niveau est explicitement revendiqué et aucun transfert n'est effectué.  
**Décision permise.** Un résultat peut rester solide tout en soutenant un verdict plus étroit qu'auparavant.

### R-034 — portée exacte des décisions et autorisations

**Fonction.** Empêcher la transitivité implicite entre qualifier, décider, exécuter et propager.  
**Déclencheur.** Changement de nature d'acte ou de portée : qualifier→calculer, dette→opération, clôturer→propager, proposer→exécuter.  
**Contrôle.** Une décision n'autorise que l'acte, l'objet et la portée explicitement couverts.  
**Silence/arrêt.** La même autorisation couvre explicitement l'enchaînement technique borné.  
**Décision permise.** Une dette scientifique ou un mécanisme restant à instruire ne vaut pas autorisation de lancer la prochaine opération.

### R-037 — négatifs, refus et suspensions

**Fonction.** Préserver l'information acquise par échec, limite ou refus sans la transformer en verdict sur l'objet.  
**Déclencheur.** Un résultat négatif, une voie non productive, une suspension ou une limite modifie le choix futur ou borne une prétention.  
**Contrôle.** Conserver le négatif à son rang exact avec ses hypothèses et sa provenance.  
**Silence/arrêt.** Incident technique trivial sans valeur discriminante pour la reprise.  
**Décision permise.** Refuser de répéter une stratégie localement non productive sans conclure contre toute la famille de modèles.

### R-040 — intégrité des transformations de représentation

**Fonction.** Empêcher qu'une représentation localement correcte devienne une entrée aval incomplète ou contaminée.  
**Déclencheur.** Synthèse, réduction, traduction ou ancien cadrage devient l'entrée d'une nouvelle qualification ou prétend représenter l'état courant.  
**Contrôle.** Examiner le delta source→représentation : conservé, perdu, ajouté, requalifié ; tester si le delta change une prémisse, une sélection ou la portée aval.  
**Silence/arrêt.** Différence sans perte pertinente pour l'usage aval ; arrêt lorsque delta et effet aval sont qualifiés.  
**Décision permise.** `localement juste` peut coexister avec `insuffisant ou trop large pour l'usage actuel` sans réécriture destructive.

## Relations à conserver

- `R-004 → R-005` — **composition** : autorité courante et validité d'une pièce datée sont deux questions différentes.
- `R-025 → R-026` — **complément** : nature du maintien et domaine indexé sont indépendamment nécessaires.
- `R-027 ↔ R-029` — **indépendance fonctionnelle** : distinguer les couches de l'enquête ne remplace pas le typage du chemin qui les relie.
- `R-028 → R-031` — **complément** : portée de l'énoncé et rang probatoire peuvent chacun être corrects ou erronés indépendamment.
- `R-031 → R-001` — **spécialisation** : machine→science est un cas particulièrement exposé de résultat→soutien→verdict.
- `R-031 ↔ R-037` — **indépendance fonctionnelle** : qualifier correctement un négatif ne garantit pas qu'il reste récupérable ; le conserver ne lui donne pas plus de portée.

## Garde générale

Aucune unité n'impose de trouver une conclusion positive. `NON_ETABLI`, maintien local d'un résultat, réduction de portée et absence d'autorisation nouvelle sont des sorties recevables.
