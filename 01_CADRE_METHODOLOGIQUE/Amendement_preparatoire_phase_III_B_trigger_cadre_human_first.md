# Amendement préparatoire Phase III-B — trigger, récupération canonique et Human-First

## Statut

Ce document amende la préparation de la Phase III-B après la première évaluation secondaire de III-A et après réinstruction de la matrice `42 unités / 52 relations` de la PR #139.

Il ne lance aucun test, ne modifie aucun résultat scientifique, ne promeut aucune règle dans `AGENTS.md`, ne modifie pas `main` et n'autorise aucun merge.

```text
PHASE_III_A_EVALUATION_1 = RECUE_ET_ETUDIEE
EVALUATION_1_FICHIER_SOURCE = Evaluation_1_phase_III-A.md
EVALUATION_1_SHA256 = d60b5d8a2724c04fa75881f7f3576fae77fe8596894c4c533ffb3b36538bea6c
SCORES_PHASE_I_II = GELES
SCORES_III_A = SECONDAIRES
PHASE_III_B = NON_LANCEE
TRIGGER_EXPERIMENTAL = A_PRE_ENREGISTRER
PROMOTION_TRIGGER_MAIN = NON_OUVERTE
MUTATION_SCIENTIFIQUE = NON
MERGE_#139 = NON_AUTORISE
```

L'Évaluation 1 a notamment fait apparaître un besoin distinct d'**ancrage fonctionnel des références** : une règle ou une source n'est informative pour le scoring que si la réponse montre quel fait concret satisfait son déclencheur, quelle fonction est protégée et quelle décision en est modifiée. Le présent amendement transforme ce point en contrôle prospectif sans réécrire rétroactivement la grille III-A.

## 1. Ce que la matrice de #139 représente pour III-B

La matrice n'est pas une liste homogène de commandements. Chaque unité encode notamment :

```text
fonction protégée
+ sujet
+ sources/antécédents
+ régime déclaré
+ régime ratifié
+ régime appliqué de facto
+ déclencheur
+ exceptions / silence / arrêt
+ mécanisme d'enforcement
+ épisodes d'application et de silence
+ sous- et sur-applications
+ bénéfices et coûts
+ contre-cas/tests
+ statut probatoire
+ verdict provisoire
+ action éventuelle et condition de déclenchement
```

Les relations typent ensuite les rapports entre unités : spécialisation, composition, contrôle, soutien, indépendance fonctionnelle, tension, transport conditionnel, déclenchement conditionnel, etc.

Conséquence expérimentale : une bonne réponse ne se mesure pas au nombre de `R-xxx` reconnus. Elle doit **sélectionner les fonctions déclenchées dans leur bon régime, composer les relations qui changent l'argument et laisser silencieuses les fonctions non déclenchées**.

## 2. Trigger actif avant tout travail substantiel

### 2.1 Faisabilité expérimentale

Un trigger actif est réalisable dans le dispositif III-B si les deux conditions reçoivent exactement le même bootstrap et si seule la représentation de la matrice varie.

Structure candidate :

```text
00_REPRISE/README.md
00_REPRISE/matrice_assignee.md
```

Le prompt humain commun ne doit indiquer que le bootstrap, par exemple :

```text
Commencez par lire et appliquer intégralement 00_REPRISE/README.md,
puis accomplissez la mission qui y est définie.
```

Le bootstrap doit imposer, avant analyse substantielle :

1. lecture complète de `00_REPRISE/matrice_assignee.md` ;
2. usage de cette matrice comme **surface expérimentale de contrôle**, jamais comme autorité scientifique ;
3. activation seulement des fonctions dont le déclencheur est matériellement établi ;
4. maintien explicite du silence lorsque le régime ou le déclencheur manque ;
5. recherche autonome dans le dépôt des sources scientifiques, décisions et autorités courantes nécessaires à la mission ;
6. interdiction d'utiliser une mémoire extérieure du projet comme substitut au dépôt ;
7. séparation entre réponse principale destinée à l'humain et trace technique de contrôle.

### 2.2 Invariance entre conditions

Pour qu'une comparaison D17/D61 reste interprétable :

```text
MEME_FONCTIONNALITE_SEMANTIQUE = OUI
MEMES_REGLES_SOURCES = OUI
MEMES_RELATIONS_SOURCES = OUI
MEME_BOOTSTRAP = OUI
MEME_MISSION = OUI
MEME_BASE_GIT = OUI
SEULE_VARIABLE_DOCUMENTAIRE = ORGANISATION_DE_LA_MATRICE_ASSIGNEE
```

Les noms `D17`, `D61`, `2D`, `fiches+relations`, `compact` ou `source` ne doivent pas être visibles dans le paquet remis aux agents.

Une condition ne doit pas recevoir davantage de fonctions que l'autre. Si les contenus diffèrent, le test devient un test de corpus et non un test de représentation.

### 2.3 Ce que le trigger ne doit pas révéler

Le trigger ne doit pas donner le chemin du cadre canonique, sa formulation correcte ni la liste des documents que l'agent doit considérer comme autorités.

Il impose **comment instruire**, pas **quoi conclure**.

Cette séparation est nécessaire pour transformer la récupérabilité du cadre canonique en variable discriminante réelle.

## 3. Trigger expérimental et trigger durable : deux questions différentes

### 3.1 Expérience

Le bootstrap explicite ci-dessus peut garantir, à l'intérieur du protocole, que l'agent est instruit de charger sa matrice avant le travail.

Le respect effectif reste observable et doit être scoré ; une instruction présente n'est pas une preuve qu'elle a été correctement appliquée.

### 3.2 Dépôt durable

Aucun fichier unique ne peut actuellement être présumé déclencheur universel pour tous les types d'agents susceptibles de lire un dépôt.

`AGENTS.md` constitue un mécanisme natif pour les environnements qui l'honorent comme instruction de dépôt. D'autres agents ou connecteurs peuvent au contraire découvrir les fichiers par recherche induite par le prompt, sans garantie d'injection automatique d'`AGENTS.md`.

Le verdict recevable avant test est donc :

```text
TRIGGER_EXPERIMENTAL_DETERMINISTE = POSSIBLE
TRIGGER_REPO_UNIVERSEL_TOUT_AGENT = NON_GARANTI
TRIGGER_DURABLE = A_QUALIFIER_PAR_CLASSE_D_AGENT_APRES_PHASE_III
```

Aucune promotion sur `main` ne sera décidée avant les résultats complets. Si le mécanisme est retenu ultérieurement, le support devra être le plus léger qui donne une adoption réelle : `AGENTS.md` racine pour les agents qui l'injectent, route Human-First d'accueil pour les lecteurs/agents qui naviguent par recherche, ou combinaison minimale si les tests montrent qu'une seule surface ne suffit pas.

## 4. Récupération autonome du cadre canonique comme test

### 4.1 Pourquoi elle est discriminante

Le cadre actuel est distribué dans plusieurs strates historiques et courantes. Une partie de sa genèse a été travaillée dans le pan philosophique, mais plusieurs formulations anciennes ont ensuite été requalifiées.

Le test ne doit donc pas demander seulement :

```text
l'agent a-t-il trouvé un document parlant du cadre ?
```

mais :

```text
l'agent a-t-il reconstruit le rang courant des sources,
identifié les supersessions,
et extrait les distinctions qui gouvernent réellement la tâche ?
```

Trouver une strate ancienne et la traiter comme canonique constitue un échec de routage/autorité même si le texte ancien est historiquement pertinent.

### 4.2 Pré-vol de faisabilité

Avant lancement, l'expérimentateur vérifie seulement que, sur la base Git gelée :

- la racine du dépôt est lisible ;
- la recherche de fichiers et la lecture de documents fonctionnent ;
- au moins un fichier connu non remis dans le bootstrap est récupérable par l'agent.

Ce pré-vol ne révèle ni le chemin du cadre canonique ni le contenu attendu.

### 4.3 Axe de scoring spécifique — récupération canonique

Quatre dimensions, 0–4 chacune, sans total global fusionné avec les autres axes :

| ID | Dimension | Score 4 attendu |
|---|---|---|
| `RC1` | Routage d'autorité | Retrouve plusieurs surfaces pertinentes, distingue courant/historique/provenance et justifie lesquelles gouvernent la tâche. |
| `RC2` | Reconstruction du noyau | Reconstruit les distinctions canoniques nécessaires sans dépendre d'une formule historique unique. |
| `RC3` | Gestion des supersessions | Identifie au moins une formulation historiquement importante mais requalifiée et évite toute rétroprojection ou restauration silencieuse. |
| `RC4` | Transfert vers le cas | Montre exactement comment le cadre retrouvé change la qualification du dossier étudié, sans propagation automatique. |

Une absence d'information doit pouvoir produire `NON_ETABLI` plutôt qu'une reconstruction inventée.

## 5. Couche fonctionnelle prospective issue de la matrice

La grille qualitative de III-A reste utile, mais III-B ajoute une couche directement dérivée du modèle `42/52`.

### F1 — sélection du régime et des déclencheurs

L'agent identifie les fonctions réellement déclenchées, leurs exceptions et leurs conditions de silence. Il évite à la fois sous-application et sur-application.

### F2 — ancrage fonctionnel des références

Pour chaque fonction importante invoquée explicitement ou implicitement, la chaîne suivante doit être reconstructible :

```text
fait matériel
→ déclencheur satisfait
→ fonction protégée
→ opération / contrôle
→ conséquence sur la décision
```

Score maximal seulement si la réponse explique aussi pourquoi une fonction voisine plausible ne s'applique pas ou reste silencieuse.

### F3 — composition relationnelle

L'agent distingue complément, spécialisation, contrôle, indépendance et transport conditionnel lorsque ces relations changent l'argument. Une proximité documentaire ou graphique ne vaut ni causalité ni transitivité.

### F4 — intégrité de l'état et de la représentation

L'agent établit l'état courant nécessaire, distingue autorité/provenance/historique et contrôle le delta lorsqu'un ancien cadre, une synthèse ou une réduction devient entrée de la décision présente.

Chaque dimension est scorée 0–4. Les quatre profils restent séparés au premier passage.

## 6. Raffinements de la grille qualitative après Évaluation 1

Les axes III-A sont conservés comme famille de mesures, avec les corrections prospectives suivantes :

- `E3` : un score élevé exige une alternative ou un contre-cas réellement caractérisé et discriminant, pas la mention abstraite qu'un contre-cas serait utile ;
- `S1` : couverture = toutes les dimensions qui changent la décision, non remplissage de toutes les rubriques ;
- `S2` : hiérarchisation = priorité d'information, c'est-à-dire quel fait doit être établi d'abord et pourquoi ;
- `E7` : score 4 seulement si au moins deux transitions inter-niveaux sont justifiées et qu'une propagation plausible est explicitement refusée ;
- `S4` : score 4 seulement si surpromotion, sous-exploitation et sélection d'entrée sont examinées conjointement lorsque pertinentes ;
- `C8` est séparé en `C8a invention détectable` et `C8b affirmation factuelle importante insuffisamment vérifiable/attribuée` ;
- `M3` doit distinguer le risque de sur-/sous-application du simple coût ;
- l'efficacité descriptive reste hors des totaux principaux ;
- l'ancrage fonctionnel n'est pas ajouté comme doublon dans les anciens axes : il devient `F2` dans la couche fonctionnelle propre à III-B.

Les critères proches du plafond restent comme garde-fous, mais ne doivent pas être interprétés comme principaux discriminants entre réponses déjà compétentes.

## 7. Grille Human-First séparée

La qualité Human-First constitue un troisième objet d'évaluation, distinct de la correction scientifique et de la discipline méthodologique.

Elle est définie dans :

```text
01_CADRE_METHODOLOGIQUE/Grille_Human_First_III_B.csv
```

Principe important : la grille Human-First doit porter sur la **réponse principale destinée à l'humain**, sans donner de points parce que l'annexe technique, les codes `R-xxx`, les chemins ou le journal de navigation sont détaillés.

L'évaluation humaine est primaire pour cette grille. Un score produit par un LLM peut servir de second regard structurel, mais ne suffit pas à établir qu'un document est réellement intelligible pour un humain.

Pour limiter le biais de familiarité, les réponses seront anonymisées avant lecture comparative et la condition documentaire ne sera révélée qu'après scoring Human-First.

## 8. Séparation réponse humaine / trace de contrôle

Chaque agent produit deux blocs :

1. **Réponse principale** : langage naturel primaire, raisonnement et verdict nécessaires à la tâche ;
2. **Trace de contrôle compacte** : matrice lue, sources réellement utilisées, fonctions activées avec leur ancrage factuel, fonctions voisines laissées silencieuses lorsqu'elles étaient tentantes, informations manquantes bloquantes ou non bloquantes.

La trace ne doit pas envahir le flux principal. Elle sert au scoring fonctionnel et à l'audit expérimental ; la grille Human-First est appliquée au premier bloc.

## 9. Double information sans bifurcation

La Phase III-B reste une expérience jusqu'à son verdict terminal.

Elle peut produire secondairement des informations utiles sur le dépôt, mais ces informations sont mises en quarantaine pendant l'expérience :

```text
RESULTAT_PRIMAIRE = PERFORMANCE_DU_DISPOSITIF_DOCUMENTAIRE
SORTIE_SECONDAIRE = PISTE_REELLE_EVENTUELLE_DU_DEPOT
SORTIE_SECONDAIRE != AUTORISATION
SORTIE_SECONDAIRE != NOUVEAU_CHANTIER
SORTIE_SECONDAIRE != MUTATION
```

Une possibilité latérale utile relève d'abord de la capture légère (`R-018`). Une connaissance causale issue d'une véritable résolution ne peut remonter selon `R-042` qu'après test de transport. Les agents testés ne reçoivent pas comme objectif de « trouver des idées nouvelles », afin de ne pas récompenser la dispersion.

Aucune piste secondaire n'est exécutée avant clôture de III-B.

## 10. Tâche scientifique candidate — réinstruction totale du cycle 10

### 10.1 Mission candidate

Le cycle 10 est retenu comme candidat scientifique fort pour une **réinstruction totale et non destructive** :

> reconstruire le statut actuel des résultats du cycle 10 sous le cadre canonique courant, déterminer ce qui reste acquis, ce qui doit être requalifié, ce qui perd une portée antérieure, ce qui demeure ouvert et quelles conditions de reprise scientifiques survivent, sans relancer de calcul ni réécrire les pièces historiques.

### 10.2 Pourquoi le cas est discriminant

Le cycle contient déjà :

- deux résultats négatifs conditionnels sur des architectures conservatrices ;
- une fenêtre dissipative phénoménologique non vide ;
- plusieurs passages entre scan paramétrique, trajectoire calculée, quasi-fixité, bilan énergétique et interprétation ;
- une terminologie partiellement antérieure au cadre canonique actuel.

Une mauvaise réponse peut donc échouer symétriquement :

```text
CONSERVATION_SERVILE_DE_L_ANCIEN_CADRE
OU
NETTOYAGE_DESTRUCTIF_DES_RESULTATS_INFORMATIFS
```

La bonne sortie doit préserver le calcul et les négatifs à leur rang exact tout en réinstruisant les conclusions.

### 10.3 Variable supplémentaire testée

Le chemin du cadre canonique ne sera pas donné. La tâche scientifique teste donc simultanément :

```text
qualité de la réinstruction scientifique
+
récupération autonome du cadre canonique distribué
+
bonne application de la matrice assignée
```

Le référentiel évaluateur est conservé séparément de tout paquet remis aux agents.

## 11. Tâche méthodologique / écosystémique

Elle n'est pas encore figée.

Condition supplémentaire imposée après correction de sélection : le cas doit être **matériellement actuel au moment du test**, porter une décision encore ouverte et ne pas être simplement un incident historique déjà résolu.

Il sera recherché à partir de l'état vivant du dépôt puis soumis à la matrice avant sélection.

```text
TASK_S_CYCLE10 = CANDIDAT_FORT_A_FINALISER
TASK_M = A_IDENTIFIER_SUR_PROBLEME_ACTUEL
MATRICES_TASK_S = A_DERIVER_DU_MEME_SOUS_ENSEMBLE_42_52
MATRICES_TASK_M = A_DERIVER_APRES_SELECTION_DU_CAS
TRIGGER = A_GELER_AVANT_REPONSES
GRILLES = A_GELER_AVANT_REPONSES
PHASE_III_B = NON_LANCEE
```

## 12. Condition de passage au test

III-B ne commence qu'après :

1. gel du bootstrap commun ;
2. gel de la base Git ;
3. gel des deux représentations sémantiquement équivalentes pour chaque tâche ;
4. gel de la mission de chaque tâche ;
5. gel des grilles fonctionnelle, qualitative, scientifique/méthodologique et Human-First ;
6. gel du référentiel évaluateur du cadre canonique pour la tâche S ;
7. sélection et justification de la tâche M actuelle ;
8. vérification que les agents peuvent matériellement rechercher/lire le dépôt sans leur révéler la route canonique ;
9. préparation de l'anonymisation et de la conservation verbatim des quatre réponses.

Aucune de ces préparations ne vaut promotion du prototype, de la matrice ou du trigger dans `main`.
