# Audit épistémique du workflow humain–LLM–GitHub v0.1

## 0. Statut

```text
statut : audit fondationnel du dispositif de travail ;
date : 21 juillet 2026 ;
fonction : distinguer intégrité, cohérence, contrôle et validation ;
ne vaut pas : critique générale de l’usage des LLM, rejet de GitHub ou preuve que les
               résultats antérieurs sont faux.
```

## 1. Question

Le workflow actuel combine :

```text
un auteur humain qui choisit, oriente et arbitre ;
plusieurs LLM qui recherchent, rédigent, critiquent et programment ;
Git et GitHub qui conservent les états, automatisent des contrôles et organisent les portes.
```

Cette pluralité fonctionnelle ne constitue pas automatiquement une pluralité épistémique.
L’audit demande quelles erreurs chaque composante peut réellement détecter, et quelles
erreurs peuvent être partagées par tout le système.

## 2. Ce que GitHub valide réellement

### Capacités fortes

```text
provenance et historique des modifications ;
identité des versions et des branches ;
intégrité de fichiers ;
reproductibilité de commandes codées ;
contrôle de structure, liens, encodage et données interdites ;
visibilité des divergences et possibilité de revenir à un état antérieur.
```

### Incapacités structurelles

GitHub ne décide pas :

```text
si une question est importante ;
si un concept correspond à une différence réelle ;
si une inférence est originale ;
si une littérature a été comprise loyalement ;
si les critères automatiques sont bien choisis ;
si une conclusion prudente est substantielle ou triviale.
```

Un workflow vert signifie que les conditions programmées sont satisfaites. Il ne valide
pas les conditions elles-mêmes.

## 3. Ce que les LLM apportent réellement

### Capacités fortes

```text
exploration rapide de variantes ;
recherche et extraction documentaire ;
contrôle de cohérence explicite ;
génération d’objections et de contre-formulations ;
assistance au code et aux calculs ;
comparaison de structures complexes ;
conservation d’une discipline rédactionnelle.
```

### Risques

```text
production d’une cohérence verbale supérieure à la compréhension effective ;
erreurs partagées entre modèles ;
sensibilité au cadrage et au vocabulaire du corpus ;
préférence pour une réparation architecturale plutôt que pour l’abandon d’une question ;
modalisation qui réduit le risque de fausseté en réduisant aussi le contenu ;
relecture de documents rédigés selon les mêmes attentes que le relecteur ;
confusion entre consensus d’agents et indépendance des preuves.
```

Les recherches récentes sur les LLM montrent que des modèles différents peuvent présenter
des erreurs fortement corrélées. Les modèles plus performants ou plus dociles peuvent aussi
fournir des réponses plausibles mais fausses que la supervision humaine détecte mal. La
multiplication des agents ne suffit donc pas à créer une triangulation.

## 4. Risques propres à l’auteur humain

L’auteur reste la seule instance responsable du choix des problèmes et des arbitrages.
Cette centralité est nécessaire, mais crée des risques :

```text
biais de cohérence autobiographique ;
reconstruction rétrospective des intentions ;
sélection des branches de recherche jugées prometteuses ;
attachement à un vocabulaire devenu familier ;
fatigue devant l’ampleur du corpus ;
délégation progressive des critères de rigueur aux agents ;
confusion entre maîtrise du dispositif et maîtrise du champ scientifique.
```

La réflexivité de l’auteur réduit ces risques sans les supprimer. Un aveu de biais ne vaut
pas correction du biais.

## 5. Boucle circulaire possible

```text
l’auteur propose une intuition ;
un LLM la transforme en cadre ;
un autre LLM applique le cadre ;
GitHub vérifie la conformité de l’application ;
un LLM relit la conformité et propose une modalisation ;
l’auteur valide la prudence obtenue ;
la répétition stabilise le vocabulaire et donne une impression d’objectivité.
```

Cette boucle peut produire des documents exacts, utiles et traçables. Elle peut aussi
stabiliser une question mal posée ou une contribution inexistante.

## 6. Registre d’indépendance

Toute revendication de validation devra désormais remplir un registre :

| Dimension | Question | États possibles |
|---|---|---|
| données | les preuves proviennent-elles de matériaux distincts ? | indépendante / partagée / inconnue |
| méthode | les procédures ont-elles des modes d’échec différents ? | indépendante / partiellement / non |
| modèle | les analyses reposent-elles sur des hypothèses concurrentes ? | concurrentes / proches / identiques |
| cadrage | les évaluateurs reçoivent-ils le vocabulaire et la thèse du projet ? | aveugle / partiel / commun |
| auteur | l’évaluation dépend-elle du même arbitrage humain ? | externe / mixte / interne |
| intérêt | l’agent peut-il réellement conclure à l’échec ? | oui / limité / non |
| compétence | le domaine est-il couvert par une expertise démontrable ? | établie / indirecte / inconnue |

Une convergence entièrement `partagée / proche / commune / interne` est une cohérence du
système, non une validation indépendante.

## 7. Niveaux de contrôle révisés

### V0 — intégrité

```text
fichiers, versions, liens, encodage, empreintes, absence de données interdites.
```

### V1 — reproductibilité interne

```text
le même code et les mêmes données reproduisent les mêmes sorties.
```

### V2 — reconstruction documentaire

```text
les affirmations correspondent aux sources consultées et leur portée est conservée.
```

### V3 — critique adversariale interne

```text
un agent cherche activement à réfuter l’argument, avec accès aux sources mais sans mission
implicite de réparation.
```

### V4 — résistance externe

```text
littérature concurrente, calcul indépendant, données distinctes ou lecteur humain extérieur.
```

### V5 — contribution

```text
une conséquence nouvelle résiste à V0–V4 et se distingue explicitement des antériorités.
```

Les audits GitHub actuels couvrent surtout V0 et une partie de V1. Les LLM peuvent aider à
V2 et V3. Ils ne suffisent pas seuls à V4 ou V5.

## 8. Protocole adversarial minimal

Pour chaque thèse candidate :

1. produire une version sans vocabulaire du projet ;
2. demander à un agent séparé de reconstruire la meilleure antériorité concurrente ;
3. fournir à un autre agent seulement la thèse nue et les sources, sans généalogie du corpus ;
4. exiger une décision parmi `déjà connu / différence mineure / conséquence propre / faux` ;
5. comparer les raisons, non les seules décisions ;
6. vérifier les points décisifs directement dans les sources ;
7. conserver les désaccords non résolus ;
8. ne pas transformer immédiatement une objection en nouvelle rubrique du cadre.

## 9. Tests spécifiques aux LLM

### Test de permutation

Reformuler la même question sans les termes stabilisés du corpus. Une forte variation du
verdict indique une dépendance au cadrage.

### Test anti-projet

Demander une démonstration de H-0 avec les mêmes ressources et le même niveau d’effort que
pour H-P.

### Test de provenance

Pour chaque proposition substantielle, distinguer :

```text
source primaire ;
inférence du modèle ;
formulation de l’auteur ;
convention interne du corpus.
```

### Test de non-réparation

Lorsqu’une objection atteint la thèse, interdire temporairement toute reformulation de
sauvetage. Évaluer d’abord si la version attaquée doit être abandonnée.

### Test de désaccord raisonné

Une pluralité d’agents n’est utile que si les prémisses, sources et opérations qui conduisent
au désaccord sont visibles. Un vote majoritaire sans cette décomposition est exclu.

## 10. Modification des portes GitHub

Les contrôles automatiques restent utiles, mais leur statut doit être affiché :

```text
vert technique : intégrité et tests codés réussis ;
vert documentaire : sources et citations contrôlées ;
vert scientifique : interdit comme label automatique ;
originalité validée : interdit sans revue externe et argument comparatif explicite.
```

Aucune PR ne doit être fusionnée au motif que « tous les audits sont verts » lorsque la
décision porte sur une thèse ou une question directrice.

## 11. Rôle futur d’un lecteur humain externe

Avant toute revendication O2 ou O3 :

```text
fournir un dossier court, non l’ensemble du dépôt ;
présenter H-P, H-0, trois cas et les conséquences alléguées ;
masquer autant que possible la généalogie émotionnelle du projet ;
demander où le résultat est déjà connu, où il est faux et ce qu’il change ;
conserver la réponse négative comme résultat, non comme obstacle éditorial.
```

La revue externe ne doit intervenir qu’après réduction du corpus à un argument lisible.
L’ampleur actuelle du dépôt ferait porter au lecteur le coût de découvrir lui-même la thèse.

## 12. Verdict provisoire

```text
GitHub : infrastructure de mémoire et d’intégrité, non gardien de la vérité ;
LLM : instruments puissants mais corrélés, non experts indépendants par simple pluralité ;
auteur : arbitre responsable, mais partie prenante du système évalué ;
workflow actuel : fort sur V0–V2, partiellement fort sur V3, faible sur V4–V5 ;
conséquence : aucune convergence interne ne suffira désormais à déclarer une contribution.
```

## 13. Références de départ

```text
Lisa Messeri et M. J. Crockett, Artificial intelligence and illusions of understanding
in scientific research, Nature 627, 49–58, 2024.

Elliot Myunghoon Kim et al., Correlated Errors in Large Language Models,
Proceedings of ICML 2025.

Lexin Zhou et al., Larger and more instructable language models become less reliable,
Nature 634, 61–68, 2024.

Hyungyu Shin et al., Automatically Evaluating the Paper Reviewing Capability of Large
Language Models, arXiv:2502.17086, 2025.

Michael Weisberg, Robustness Analysis, Philosophy of Science 73, 730–742, 2006.

Jonah Schupbach, Robustness Analysis as Explanatory Reasoning, British Journal for the
Philosophy of Science 69, 275–300, 2018.

Robert Hudson, Seeing Things: The Philosophy of Reliable Observation, Oxford University
Press, 2013.
```
