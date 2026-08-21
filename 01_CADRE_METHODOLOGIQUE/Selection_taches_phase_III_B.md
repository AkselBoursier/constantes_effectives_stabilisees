# Sélection des tâches prospectives de Phase III-B

## Statut

Cette pièce sélectionne les deux problèmes candidats après application de la matrice `42 unités / 52 relations` à leur **statut courant**, avant dérivation des deux représentations documentaires assignées aux agents.

Elle ne constitue ni le prompt final, ni le bootstrap, ni une réponse attendue, ni une autorisation d'exécuter les solutions qui pourraient être proposées.

```text
TASK_S = SELECTIONNEE_COMME_CANDIDAT_FINAL
TASK_M = SELECTIONNEE_COMME_CANDIDAT_FINAL
PROMPTS = NON_GELES
MATRICES_ASSIGNEES = NON_GELEES
PHASE_III_B = NON_LANCEE
MUTATION_MAIN = NON
MERGE = NON_AUTORISE
```

## 1. Critères de sélection communs

Une tâche III-B doit :

1. porter sur un problème matériellement actuel, non sur un incident seulement historique ;
2. contenir plusieurs dépendances réelles dont certaines modifient le verdict ;
3. permettre une erreur de sur-application et une erreur de sous-application ;
4. comporter au moins une information manquante, une ambiguïté de rang ou une alternative réellement concurrente ;
5. avoir plusieurs actions plausibles de coût ou de portée différents ;
6. posséder suffisamment de matière dans le dépôt pour évaluer la réponse sans devoir importer un verdict externe ;
7. pouvoir rester intégralement en lecture seule pendant le test ;
8. produire éventuellement une information secondaire utile sans que cette utilité soit demandée à l'agent ni exécutée avant le verdict terminal.

## 2. Tâche S — réinstruction totale du cycle 10

### Question de travail

> À partir de l'état actuel du dépôt, réinstruire intégralement le cycle 10 sous le cadre canonique courant. Déterminer ce qui reste établi dans les calculs et résultats existants, ce qui doit seulement changer de rang ou de portée, ce qui doit être déclassé comme formulation historique, ce qui demeure scientifiquement ouvert et quelles conditions de reprise subsistent. Ne relancer aucun calcul et ne réécrire aucun document.

### Pourquoi la tâche reste actuelle

Les résultats calculatoires des phases 2, 3 et 4 existent et restent informatifs. La désynchronisation porte sur leur raccord avec un cadre canonique qui a évolué après leur formulation.

La tâche n'est donc ni « refaire le cycle » ni « poursuivre la phase 5 ». Elle porte sur l'intégrité de la transformation :

```text
RESULTATS_HISTORIQUES_INFORMATIFS
+
CADRE_CANONIQUE_COURANT_DISTRIBUE
->
QUALIFICATION_SCIENTIFIQUE_ACTUELLE_NON_DESTRUCTIVE
```

### Alternatives qu'une réponse doit pouvoir départager

- un résultat ancien reste substantiellement correct et seule son exposition doit être requalifiée ;
- le résultat calculatoire reste correct mais le soutien/verdict qui lui était associé devient trop large ;
- une formulation historiquement centrale ne possède plus de rang canonique ;
- une dette scientifique survit mais n'est pas automatiquement prioritaire ni autorisée ;
- une pièce apparemment désynchronisée n'exige finalement aucune correction substantielle.

### Fonctions de la matrice probablement actives

Le sous-ensemble exact sera gelé avant test. Les fonctions candidates prioritaires sont :

```text
R-001 rang machine/science
R-003 couplage probatoire toy/proxy/réalité
R-004 routage et autorité
R-005 statut documentaire historique/courant
R-009 représentation de science vivante
R-014 ancien audit/contexte nouveau
R-023 activité != qualification
R-025 constance != stabilisation
R-026 énoncé indexé
R-027 cible / accès / constitution
R-028 dimension d'enquête != portée
R-029 typage des chemins
R-030 vocabulaire disciplinaire prioritaire
R-031 résultat / soutien / verdict
R-037 conservation des négatifs
R-039 intelligibilité Human-First
R-040 intégrité de transformation de représentation
```

Des fonctions voisines seront volontairement présentes comme candidats de silence, notamment lorsqu'une non-détection observationnelle, un transport inter-domaines ou un statut probatoire de règle n'est pas effectivement déclenché. Le but est de tester la sélection, pas de fournir uniquement les bonnes réponses.

### Discriminants supplémentaires

- récupération autonome du cadre canonique ;
- capacité à reconnaître des supersessions sans réécriture rétroactive ;
- distinction scan de paramètres / trajectoire temporelle / histoire physique ;
- maintien des deux résultats négatifs conditionnels ;
- maintien de la fenêtre dissipative comme fenêtre phénoménologique, non mécanisme microscopique établi ;
- condition de reprise précisément bornée.

## 3. Tâche M — qualification du prototype Human-First de reprise

### État matériel courant

La branche :

```text
test/human-first-reprise-blind-20260819
```

reste trois commits devant `main` et modifie uniquement :

```text
README.md
02_CYCLES_PHYSIQUES/README.md
```

Aucune PR correspondante n'est retrouvée au moment de la sélection.

Le prototype a été produit après un premier blind test de récupérabilité. Les quatre environnements de ce test ont ensuite été requalifiés : un témoin ChatGPT éphémère fournit une preuve forte de défaut de routage temporel ; la reprise physique a une force intermédiaire ; la reprise méthodologique était assistée par mémoire/instructions et ne constitue donc pas une preuve autonome forte ; la reprise philosophique reste une preuve utile d'une porte insuffisamment actualisée.

La branche candidate a notamment :

- ajouté au README racine une règle de recherche du dernier checkpoint explicitement courant/correctif dans les issues longues ;
- signalé le caractère daté de la porte philosophique ;
- ajouté au README des cycles une vue de reprise `actif / vivant dormant / clos-suspendu` pour les dix cycles.

### Question de travail

> À partir de `main`, de l'issue #136, de ses requalifications expérimentales et de la branche `test/human-first-reprise-blind-20260819`, décider si ce prototype mérite d'être soumis **inchangé** à un second blind test, s'il doit être **amendé avant retest**, ou s'il doit être **abandonné/réduit**. Ne modifier aucune branche. Justifier le choix par les défauts réellement reproduits, la force des preuves, les risques de sur- et sous-correction, le coût de maintenance et les conditions d'arrêt/réouverture.

### Pourquoi la tâche est actuelle

Le problème n'est pas l'incident historique qui a motivé le prototype. La décision courante est le statut de la **branche expérimentale encore non intégrée** après requalification des preuves qui l'ont motivée.

Trois sorties restent réellement ouvertes :

```text
RETEST_INCHANGE
AMENDER_PUIS_RETESTER
ABANDONNER_OU_REDUCTION_FORTE
```

Aucune n'est codée comme réponse attendue.

### Fonctions de la matrice probablement actives

Le sous-ensemble exact sera gelé avant test. Les fonctions candidates prioritaires sont :

```text
R-004 routage / autorité
R-005 statut documentaire
R-006 contre-factuel documentaire de resynchronisation
R-008 ancrage / checkpoints
R-009 représentation de la science vivante
R-010 audit de second ordre borné
R-014 audit antérieur + contexte nouveau
R-015 symétrie critique
R-017 non-prolifération par fonction
R-023 activité != qualification
R-039 Human-First
R-040 intégrité de transformation de représentation
R-041 statut probatoire d'une règle/pratique/test
```

Candidats de silence utiles : audit global indépendant si aucune population globale n'est revendiquée ; mutation destructive ; installation d'outil ; remontée de résolution transverse ; toute conclusion scientifique nouvelle.

### Pourquoi cette tâche est discriminante

Elle oblige à ne pas confondre :

```text
défaut réellement reproduit
!=
explication supposée du défaut
!=
correction candidate
!=
preuve que la correction fonctionne
```

Elle contient une tension réelle entre deux risques :

- **sous-correction** : conserver des portes qui conduisent encore un agent neuf vers un état ancien ou incomplet ;
- **sur-correction** : transformer les README en tableau de bord périssable, généraliser à partir de témoins hétérogènes ou installer une nouvelle couche plus coûteuse que le défaut.

La branche elle-même devient donc un objet de `R-040` : elle transforme une représentation d'accueil. Le blind test initial et sa requalification deviennent un objet de `R-041` : application/test/soutien doivent être séparés.

## 4. Orthogonalité des deux tâches

Les deux tâches partagent volontairement quelques invariants — autorité courante, intégrité de représentation, rang probatoire — mais leur objet principal est différent.

```text
TASK_S = QUALIFICATION_SCIENTIFIQUE_D_UN_CORPUS_DESYNCHRONISE
TASK_M = DECISION_METHODOLOGIQUE_SUR_UN_PROTOTYPE_DOCUMENTAIRE_NON_INTEGRE
```

S exige compétence scientifique sur le cycle 10 et reconstruction du cadre canonique.

M exige reconstruction d'une preuve expérimentale, comparaison de corrections documentaires et maîtrise du coût/régime Human-First.

Cette orthogonalité est suffisante pour que le même avantage documentaire ne soit pas testé deux fois sous des formulations équivalentes.

## 5. Information secondaire admissible

Si une réponse révèle une vraie correction scientifique du cycle 10 ou une meilleure solution de routage Human-First, l'information est conservée comme sortie secondaire gelée.

Elle n'est ni appliquée ni transformée en chantier pendant III-B.

## 6. Prochaine opération

Dériver pour chacune des deux tâches :

1. un sous-ensemble source identique de la matrice `42/52` ;
2. une représentation fonctionnelle compacte ;
3. une représentation fiches+relations de même contenu sémantique ;
4. le bootstrap commun ;
5. le prompt final sans indication de condition ;
6. les critères de scoring spécifiques à la tâche ;
7. les éléments évaluateur-only qui ne doivent jamais entrer dans le paquet agent.

Ensuite seulement, geler la base Git et lancer les quatre chats éphémères.
