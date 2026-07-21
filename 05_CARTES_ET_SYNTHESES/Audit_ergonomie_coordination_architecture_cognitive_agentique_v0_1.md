# Audit d'ergonomie, de coordination et d'architecture cognitive-agentique v0.1

## 0. Statut

```text
statut : audit préparatoire de refonte ergonomique ;
date : 21 juillet 2026 ;
branche : agent/crise-fondatrice-audit-fondations ;
fonction : évaluer la navigabilité humaine et agentique du dépôt, la coordination des
           chantiers, le cloisonnement et l'usage des fonctions GitHub ;
ne vaut pas : nouvelle architecture canonique, migration immédiate, fermeture de PR,
              modification de règles GitHub ni réécriture des points d'entrée.
```

Cet audit part de la refonte fondationnelle en cours. Il ne cherche pas à rendre le dépôt
plus élégant pour lui-même, mais à réduire quatre risques :

```text
1. promotion silencieuse d'une question ou d'un document ;
2. contexte global excessif fourni aux agents ;
3. confusion entre état actif, histoire et planification ;
4. multiplication de documents de coordination qui doivent eux-mêmes être coordonnés.
```

---

## 1. Diagnostic général

### 1.1 Une architecture documentaire riche, mais un état actif dispersé

L'état courant doit aujourd'hui être reconstruit depuis plusieurs objets :

```text
README racine ;
AGENTS.md ;
index raisonné ;
accueil des dix cycles ;
verdicts et clôtures ;
registre des branches ;
corps et descriptions de pull requests ;
registre court des arbitrages ;
branches locales et distantes.
```

Ces documents ne répondent pas à la même fonction, mais ils contiennent tous des éléments
de priorité, de méthode ou de statut. Lorsqu'une décision change, plusieurs couches deviennent
partiellement périmées sans être factuellement fausses.

### 1.2 Les points d'entrée mêlent trois temporalités

Le README, le guide des agents et l'index mêlent actuellement :

```text
règles durables ;
état scientifique daté ;
prochaine opération contingente.
```

Exemple structurel : les deux questions publiques et D1-D5 sont présentées à la fois comme
mission, parcours obligatoire, contrôles intellectuels et état courant. Après la crise
fondationnelle, leur rang doit être réévalué. Tant que cette réévaluation n'est pas intégrée,
un nouvel agent est orienté vers une architecture qui fait précisément l'objet de l'audit.

### 1.3 AGENTS.md fournit trop de doctrine globale

Le fichier racine est utile pour les règles de sécurité documentaire et Git. Il contient
aussi :

```text
la mission intellectuelle ;
les deux questions publiques ;
D1-D5 ;
la prochaine phase scientifique ;
une hiérarchie de documents ;
les règles de provenance ;
l'archivage ;
les branches ;
les commandes et contrôles.
```

Cette densité produit un ancrage puissant : un agent qui lit correctement le guide tend à
reproduire le cadre avant même d'avoir instruit son objet. Le problème n'est pas que les
règles soient mauvaises. Il est qu'elles ne sont ni toutes universelles ni toutes stables.

### 1.4 Le registre manuel des branches dérive

`Registre_branches_corpus_v0_1.md` décrit une consolidation historique et une branche
`travail` comme espace d'intégration quotidien. Après PR 14 et les chantiers suivants, il
ne constitue plus un tableau fiable de l'état Git actuel.

Le registre est valable comme généalogie. Il est fragile comme outil opérationnel : GitHub
possède déjà l'état des branches et des pull requests, et toute copie manuelle crée une dette
de synchronisation.

### 1.5 Les pull requests cumulent trop de fonctions

Les pull requests ont servi successivement à :

```text
ouvrir une question ;
porter un chantier ;
conserver une généalogie ;
annoncer une suite ;
organiser des dépendances empilées ;
valider des décisions ;
intégrer du contenu.
```

Plusieurs PR brouillons anciennes restent ouvertes alors que leur contenu a été intégré
indirectement par la consolidation PR 14. Elles demeurent utiles comme traces, mais leur état
`open` les fait apparaître comme travail actif pour un humain ou un agent.

À la date de l'audit, aucune issue de recherche active n'est utilisée. Les PR portent donc
une planification que GitHub Issues et Projects pourraient représenter plus clairement.

### 1.6 Le workflow d'audit est monolithique

Le workflow `Audit du corpus` exécute sur toute pull request :

```text
structure ;
liens ;
encodage ;
assainissement des conversations ;
contrôle des données et PDF ;
compilation Python ;
installation des dépendances du cycle neutrino C2 ;
test synthétique C2 ;
inventaire des placeholders.
```

Les contrôles globaux sont pertinents. Le test C2 ne l'est pas nécessairement pour toute
modification philosophique, métrologique ou éditoriale. Cette structure fait du cycle 3 le
modèle implicite de toute vérification computationnelle et allonge les PR sans information
scientifique supplémentaire.

### 1.7 La recherche de code est disponible mais sous-utilisée

Le dépôt privé est indexé pour la recherche de code. Une partie des index Markdown et des
registres manuels compense donc une difficulté de navigation qui peut désormais être prise
en charge par une combinaison de :

```text
recherche GitHub ;
statuts normalisés ;
liens depuis les issues ;
manifestes courts ;
instructions locales.
```

---

## 2. Principe de refonte ergonomique

La refonte doit séparer cinq fonctions qui sont actuellement superposées.

### Couche 1 — orientation humaine

```text
fonction : comprendre rapidement ce qu'est le dépôt et où entrer ;
outil : README racine court ;
contenu : nature fédérée du corpus, grandes lignées, règles de prudence, liens vers l'état
          courant et les archives ;
ne contient pas : prochaine tâche détaillée, doctrine non stabilisée, historique des branches.
```

### Couche 2 — état opérationnel

```text
fonction : savoir ce qui est actif, bloqué, en revue ou clos ;
outils : GitHub Issues + Project ;
unité : dossier, test, audit ou décision ;
ne contient pas : argument scientifique complet.
```

### Couche 3 — contexte agentique

```text
fonction : donner à un agent seulement les règles nécessaires à son périmètre ;
outils : AGENTS.md minimal + instructions GitHub Copilot globales et spécifiques par chemin ;
ne contient pas : portrait de l'auteur, théorie du projet, priorité datée répétée partout.
```

### Couche 4 — preuve et recherche

```text
fonction : conserver sources, calculs, résultats, limites et décisions locales ;
outils : dossiers scientifiques et philosophiques, scripts, manifestes et sorties ;
autorité : locale et proportionnée au résultat.
```

### Couche 5 — généalogie et archives

```text
fonction : comprendre comment les questions et documents se sont transformés ;
outils : 91_TRAVAUX_ANTERIEURS, 92_ARCHIVES_CONVERSATIONNELLES, PR closes et tags ;
ne commande pas : la tâche courante sans reprise explicite.
```

---

## 3. Cloisonnement : passer des murs aux membranes

### 3.1 Cloisonnement dur à conserver

Un cloisonnement strict reste nécessaire pour :

```text
données externes volumineuses hors Git ;
sources historiques à ne pas réécrire ;
archives contenant une provenance sensible ;
documents éditeurs et questions de droit ;
résultats reproduits versus seulement rapportés ;
main versus travail non validé.
```

Ces séparations protègent une propriété réelle : intégrité, confidentialité, provenance ou
rang de preuve.

### 3.2 Cloisonnement souple pour les lignées intellectuelles

Physique, philosophie, mesure, fine-tuning, méthodologie et éditorial ne doivent pas être
fusionnés. Ils ne doivent pas non plus être rendus incapables d'interagir.

Leur relation correcte est :

```text
dossier autonome
-> question de jonction explicite
-> test borné
-> résultat de jonction ou absence de gain
-> retour à l'autonomie.
```

Une jonction devient donc une unité de travail visible — idéalement une issue — et non une
circulation diffuse de vocabulaire entre dossiers.

### 3.3 Une branche ne doit pas représenter une discipline

Les branches thématiques longues ont aidé pendant la consolidation. Dans le nouvel état,
une branche doit représenter un paquet modifiable et révisable :

```text
un test ;
un audit ;
une correction ;
un livrable borné.
```

La discipline ou la lignée reste un champ de classement dans le Project et dans les
métadonnées, non une branche durable.

---

## 4. Architecture cognitive cible

### 4.1 Une source unique de l'état actif

Le Project GitHub devient la source opérationnelle principale. Un fichier court peut en
fournir une vue hors ligne, mais il doit être dérivé ou mis à jour seulement aux jalons.

Champs minimaux proposés :

| Champ | Valeurs ou fonction |
|---|---|
| Lignée | physique, mesure, microphysique, philosophie historique, fine-tuning, méthode, éditorial |
| Type | dossier, test, audit, décision, maintenance |
| Statut | candidat, prêt, actif, bloqué, en revue, clos, archivé |
| Priorité | maintenant, ensuite, veille, différé |
| Effort | faible, moyen, élevé |
| État de preuve | rapporté, reconstruit, reproduit, vérifié indépendamment |
| Porte suivante | opération exacte permettant le changement de statut |
| Sortie | fiche, code, note technique, revue, article, archive |

Aucun score total n'est calculé.

### 4.2 Une issue par unité cognitive

Une issue de recherche doit contenir seulement :

```text
question située ;
statut Q / H / R attendu ;
matériaux nécessaires ;
opération non verbale ;
discriminant ;
condition d'arrêt ;
sortie attendue ;
liens vers les documents de preuve.
```

Les sous-issues et dépendances représentent les portes successives des cycles 9 et 10,
plutôt qu'une branche contenant dès l'origine toute la trajectoire supposée.

### 4.3 Une pull request par paquet de preuve

La PR ne doit plus être le lieu où une question est stockée pendant des semaines. Elle
intervient lorsqu'un paquet concret existe :

```text
issue liée ;
modifications délimitées ;
preuve ou résultat ;
statut avant / après ;
limites ;
contrôles exécutés ;
décision demandée.
```

Une PR peut rester brouillon pendant l'exécution, mais elle ne doit pas servir de tableau
général de programme.

### 4.4 Trois unités actives au maximum

La règle antérieure de trois branches devient une limite cognitive :

```text
1. refonte ou ergonomie ;
2. test scientifique exécuté ;
3. audit hors-cycle ou porte de sélection difficile.
```

Les autres éléments restent candidats, bloqués ou en veille dans le Project. Ils n'exigent
ni branche ni document de progression supplémentaire.

---

## 5. Navigation des agents

### 5.1 Réduire AGENTS.md à des invariants

Le fichier racine devrait conserver uniquement :

```text
sécurité des sources et archives ;
main et validation humaine ;
absence de promotion silencieuse ;
distinction résultat / hypothèse / question ;
règles sur data_external ;
obligation de lire l'issue liée et le README local ;
contrôles Git minimaux.
```

Il ne devrait plus contenir :

```text
les deux questions comme mission obligatoire ;
la prochaine priorité scientifique ;
la description complète des dix cycles ;
D1-D5 comme grille universelle ;
la généalogie des branches ;
les plans éditoriaux.
```

### 5.2 Instructions spécifiques par chemin

GitHub Copilot permet des instructions globales de dépôt et des instructions spécifiques
à des chemins. La cible proposée est :

```text
.github/copilot-instructions.md
  règles globales très courtes ;

.github/instructions/physique.instructions.md
  applyTo: 02_CYCLES_PHYSIQUES/** ;
  sources primaires, unités, calculs, reproduction, limites ;

.github/instructions/philosophie.instructions.md
  applyTo: 06_PHILOSOPHIE/** ;
  rang des propositions, voisinages, aucune migration vers la physique ;

.github/instructions/archives.instructions.md
  applyTo: 91_TRAVAUX_ANTERIEURS/**, 92_ARCHIVES_CONVERSATIONNELLES/** ;
  lecture prudente, aucune normalisation ni reprise automatique ;

.github/instructions/editorial.instructions.md
  applyTo: 93_LABORATOIRE_EDITORIAL_EXPERIMENTAL/** ;
  brouillon, aucune promotion de résultat ;

.github/instructions/code-audit.instructions.md
  applyTo: audit/**, .github/**, scripts et données dérivées ;
  tests, chemins, reproductibilité et sécurité.
```

Le format exact doit être testé sur une branche d'ergonomie. `AGENTS.md` reste utile pour
les agents qui le prennent en charge, mais il n'a plus à porter toute la doctrine.

### 5.3 Paquet d'amorçage d'un agent

Pour une tâche donnée, l'agent lit :

```text
1. l'issue liée ;
2. les instructions globales courtes ;
3. les instructions du chemin ;
4. le README ou manifeste local ;
5. les seules preuves nécessaires ;
6. l'historique ou les archives uniquement si la tâche l'exige.
```

Le parcours global actuel, qui demande de lire plusieurs verdicts avant toute modification,
devient exceptionnel.

### 5.4 Métadonnées minimales des documents actifs

Conserver un bloc de statut, mais le réduire à des champs homogènes :

```text
type : question | hypothèse | protocole | résultat | décision | archive ;
lignée : ... ;
statut : candidat | actif | en revue | clos | remplacé | archivé ;
preuve : rapportée | reconstruite | reproduite | vérifiée ;
remplace : chemin ou aucun ;
remplacé_par : chemin ou aucun ;
issue : numéro ou aucune ;
portée : locale et description courte.
```

Ces champs peuvent ultérieurement alimenter un manifeste machine lisible. Ne pas créer ce
manifeste avant d'avoir testé la stabilité des champs sur quelques dossiers.

---

## 6. Outils GitHub à mobiliser

### 6.1 Issues, sous-issues et dépendances

Fonction proposée :

```text
Issues : unités de recherche et décisions ;
sous-issues : portes d'un test complexe ;
dépendances : blocages réels ;
commentaires : arbitrages et revue courte ;
fermeture : résultat, blocage positif ou décision d'abandon.
```

### 6.2 GitHub Projects

Le Project doit offrir plusieurs vues sans dupliquer les données :

```text
vue Maintenant : trois unités actives au maximum ;
vue Tests physiques : cycles et dossiers scientifiques ;
vue Hors-cycle : mesure, microphysique, méthode, éditorial ;
vue Bloqués : acquisition, expertise ou données manquantes ;
vue En revue : PR et décisions humaines ;
vue Généalogie : éléments clos ou remplacés si nécessaire.
```

### 6.3 Labels sobres

Limiter les labels à des dimensions difficiles à représenter autrement :

```text
lignée:* ;
type:* ;
risque:* éventuellement ;
externe-requis ;
données-requises.
```

Le statut, la priorité et l'effort appartiennent de préférence aux champs du Project.

### 6.4 Rulesets ou protection de branche

Pour `main`, un ruleset minimal pourrait :

```text
exiger une pull request ;
exiger le contrôle global du corpus ;
interdire les force-pushs ;
interdire la suppression de la branche ;
préserver la possibilité d'un merge commit.
```

Ne pas exiger pour l'instant une approbation externe obligatoire si aucun lecteur habilité
n'est disponible. Ne pas modifier ces réglages sans décision explicite de l'auteur.

### 6.5 CODEOWNERS

CODEOWNERS n'apporte actuellement que peu de valeur dans un dépôt porté par un auteur unique.
Il deviendra utile si des relecteurs externes réguliers sont associés à des chemins précis.
Il ne doit pas simuler une indépendance qui n'existe pas.

### 6.6 Discussions

Les Discussions peuvent accueillir des échanges ouverts ou des questions communautaires,
mais elles ne sont pas nécessaires au workflow interne actuel. Les introduire maintenant
ajouterait une surface de coordination sans public correspondant.

### 6.7 Tags et releases

Les jalons validés importants peuvent être marqués par des tags plutôt que par une nouvelle
vue d'ensemble datée à chaque phase. Une release privée peut fournir une note de jalon et un
point stable de citation interne.

Cette possibilité doit être testée seulement après réduction des documents de navigation.

---

## 7. Modularisation de GitHub Actions

### 7.1 Contrôles globaux rapides

Un workflow global reste exécuté sur toutes les PR :

```text
structure ;
liens ;
UTF-8 ;
assainissement ;
absence de données externes et PDF interdits ;
contrôle des métadonnées actives ;
git diff --check si applicable.
```

### 7.2 Tests spécifiques par chemin

Créer ensuite des workflows ou jobs conditionnels :

```text
cycle 3 ou code C2 modifié -> dépendances et self-test C2 ;
cycle 1 QCD modifié -> tests ou scripts QCD disponibles ;
cycle 10 modifié -> tests des modèles et sorties synthétiques ;
audit ou scripts modifiés -> compilation et tests audit ;
documents seuls -> pas d'installation scientifique lourde sans nécessité.
```

Le but n'est pas d'accélérer pour lui-même, mais de rendre chaque contrôle sémantiquement
lié au paquet modifié.

### 7.3 Contrôle de statut

Un script léger pourrait vérifier que :

```text
un document actif possède un type et un statut ;
un document remplacé pointe vers son successeur ;
une PR de résultat référence une issue ;
les chemins d'archives ne sont pas modifiés sans label ou mention explicite.
```

Ce contrôle doit commencer comme rapport informatif. Il ne devient bloquant qu'après une
phase de calibration.

---

## 8. Nettoyage de l'état GitHub

### 8.1 PR historiques ouvertes

Les PR 2, 3, 4, 5, 9, 10, 11 et 12 paraissent avoir été intégrées, remplacées ou absorbées
par la consolidation PR 14, tout en restant ouvertes ou brouillon.

Procédure recommandée, sans fermeture automatique :

```text
1. vérifier pour chaque PR que la tête pertinente est ancêtre ou que son contenu existe dans main ;
2. ajouter un commentaire de clôture indiquant la PR intégratrice ou remplaçante ;
3. fermer avec le statut remplacé ou intégré indirectement ;
4. conserver la discussion et les commits comme généalogie ;
5. ne supprimer les branches qu'après décision séparée.
```

La PR 18 reste un chantier scientifique actuel. La branche de crise fondatrice reste un
dossier critique sans PR jusqu'à décision de statut.

### 8.2 Branche `travail`

Le modèle `main + branches courtes + PR + Project` rend probablement inutile une branche
d'intégration quotidienne permanente. `travail` duplique l'état et demande une
resynchronisation manuelle.

Décision proposée pour audit, non exécution :

```text
cesser de l'utiliser pour les nouveaux chantiers ;
la conserver temporairement comme trace ;
vérifier son contenu non intégré ;
la fermer ou l'archiver après assainissement.
```

### 8.3 Registre des branches

Le registre manuel doit être requalifié en carte historique. L'état actif des branches et
PR vient de GitHub ; le Project porte le programme ; les documents ne conservent que les
décisions de rang ou les bifurcations intellectuelles.

---

## 9. Coordination et hiérarchie provisoire

### Priorité 0 — rendre l'état lisible

```text
valider la présente refonte comme audit ou la corriger ;
créer le modèle minimal Issues / Project ;
identifier les PR historiques à clore ;
figer toute nouvelle vue globale pendant cette opération.
```

### Priorité 1 — fermer les ambiguïtés actives

```text
statuer sur T1.6 / T1.7 et la PR 18 sans ouvrir T1.8 ;
décider du rang de la branche de crise fondatrice ;
déterminer quelles règles de README / AGENTS restent invariantes.
```

### Priorité 2 — calibrer les tests minimaux

```text
exécuter cycle 8 ;
exécuter cycle 6 ;
évaluer si la procédure fait réellement monter ou réduire ces dossiers.
```

### Priorité 3 — préparer les recherches à fort coût

```text
ouvrir seulement la porte 9A ou 10A ;
ne pas ouvrir simultanément les calculs lourds des cycles 9 et 10 ;
choisir une cible précise pour cycle 7 ou cycle 5.
```

### Priorité parallèle hors-cycle

Une seule unité hors-cycle active à la fois :

```text
premier contraste borné du problème de la mesure ;
ou positionnement bibliographique du chantier Q ;
ou audit du laboratoire éditorial ;
ou audit séparé du workflow humain-LLM-GitHub.
```

Le choix dépend de sa capacité à produire une décision réelle, non de la proximité
thématique avec le test physique courant.

---

## 10. Plan de migration non destructif

### Phase E0 — calibration

```text
aucune fermeture ni réécriture ;
créer un Project expérimental et trois modèles d'issue ;
y inscrire seulement les unités actives et candidates de la refonte ;
tester le parcours d'un agent sur une tâche réelle.
```

### Phase E1 — assainissement de l'état

```text
vérifier et fermer les PR remplacées ;
requalifier le registre des branches ;
arrêter l'usage actif de travail ;
conserver les références généalogiques.
```

### Phase E2 — contexte agentique

```text
réduire AGENTS.md ;
ajouter les instructions par chemin ;
réécrire le README comme porte humaine courte ;
introduire un point d'état unique.
```

### Phase E3 — CI sémantique

```text
séparer audits globaux et tests scientifiques par chemin ;
ajouter les contrôles de statut en mode informatif ;
calibrer avant de rendre bloquant.
```

### Phase E4 — arborescence éventuelle

Ne renommer ou déplacer les grands dossiers qu'après usage de la nouvelle couche de
coordination. L'arborescence actuelle est imparfaite mais connue ; une migration prématurée
produirait beaucoup de bruit de liens et peu de gain cognitif.

---

## 11. Tests d'ergonomie

La refonte ergonomique doit être elle-même testée.

### Test humain

```text
un lecteur peut-il identifier en moins de trois points d'entrée :
- ce qu'est le dépôt ;
- ce qui est actif ;
- où se trouve la preuve d'un résultat ?
```

### Test agent

```text
un agent peut-il accomplir une tâche locale sans lire une doctrine générale inutile,
sans toucher une archive et sans reconstruire l'histoire entière des branches ?
```

### Test de promotion

```text
une question peut-elle devenir hypothèse ou résultat sans qu'un champ de statut,
une issue et une décision humaine le rendent visible ?
```

### Test de clôture

```text
un résultat négatif ou une absence de gain peut-il fermer une issue sans produire
un nouveau document de méthode ?
```

### Test de maintenance

```text
une priorité change-t-elle en un seul endroit opérationnel, ou exige-t-elle encore
la mise à jour de README, AGENTS, index, carte et registre ?
```

---

## 12. Verdict

> Le dépôt actuel est robuste comme archive et comme système de contrôle, mais son ergonomie
> oblige les agents et l'auteur à reconstruire trop souvent l'état actif depuis des couches
> qui mêlent règles durables, décisions datées et programme courant. Le cloisonnement doit
> rester strict lorsqu'il protège une preuve, une source ou une confidentialité ; ailleurs,
> il doit devenir une membrane franchie par des tests de jonction explicites. GitHub Issues,
> Projects, instructions par chemin, rulesets et Actions conditionnelles peuvent reprendre
> une grande partie de la coordination aujourd'hui portée par des PR longues, des branches
> persistantes et des registres manuels. La migration doit rester non destructive et être
> calibrée sur quelques tâches avant toute réorganisation de l'arborescence.

Aucune PR n'est fermée, aucune issue ou Project n'est créé, aucune règle GitHub n'est
modifiée et aucun point d'entrée actif n'est réécrit par le présent audit.