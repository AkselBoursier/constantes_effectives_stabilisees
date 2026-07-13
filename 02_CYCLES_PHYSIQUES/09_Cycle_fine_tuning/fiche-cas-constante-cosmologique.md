# Fiche de cas — constante cosmologique

## Statut

Cette fiche examine le cas de la constante cosmologique comme problème de fine-tuning, cas anthropique et candidat à une réalisation statistique dans un ensemble de domaines.

Elle s'appuie sur la refondation du cycle cosmologique : `H_0`, `Omega_i`, `w`, `A_s`, `n_s`, `sigma_8` et `S_8` ne doivent pas être versés indistinctement dans la catégorie des constantes.

Le cas `Lambda` est donc isolé de son réseau d'accès.

## 1. Thèses auditées

### 1.1 Ancien problème

> Pourquoi la densité d'énergie effective du vide gravitant est-elle extrêmement petite par rapport aux échelles attendues de la physique des champs ?

### 1.2 Problème de coïncidence

> Pourquoi la densité associée à l'accélération cosmique devient-elle comparable à la densité de matière à l'époque cosmologique où nous l'observons ?

### 1.3 Thèse anthropique

> Si `Lambda` varie entre domaines, seules les régions où la formation de structures est possible contiennent des observateurs ; la valeur observée peut alors être conditionnée par cette sélection.

Ces trois problèmes ne sont pas équivalents.

## 2. Objets et statuts

| Objet | Statut |
|---|---|
| `Lambda` dans les équations d'Einstein | paramètre de loi ou terme géométrique constant dans le modèle |
| densité du vide `rho_Lambda` | représentation énergétique reliée à `Lambda` et `G` |
| contributions quantiques au vide | termes effectifs dépendant de la théorie, de la renormalisation et des seuils |
| contre-terme ou paramètre nu | élément de la paramétrisation renormalisée, non observable séparément |
| densité effective gravitant | combinaison physique après renormalisation |
| `Omega_Lambda` | rapport d'état dépendant de `H(t)` et de l'époque |
| `H_0` | valeur actuelle d'une variable dynamique |
| amplitude primordiale `Q` ou `A_s` | condition initiale perturbative |
| fraction de matière effondrée | résultat dynamique et critère de sélection possible |

Première correction :

```text
Lambda
≠ Omega_Lambda
≠ H_0
≠ accélération observée prise comme donnée brute
```

## 3. Architecture de dépendances

Dans un modèle `Lambda`CDM simple :

```text
Lambda + densités de matière/rayonnement + conditions initiales
-> histoire de H(t)
-> croissance des perturbations
-> formation de halos et galaxies
-> environnements astrophysiques
```

L'effet environnemental de `Lambda` n'est donc pas direct sur la vie. Il passe principalement par l'histoire de l'expansion et la formation des structures.

## 4. Le problème de petitesse

La constante cosmologique observée ne se réduit pas à une contribution unique calculée naïvement.

Le problème physique est la petitesse de la combinaison effective gravitant après prise en compte :

- du paramètre cosmologique dans l'action ;
- des contributions du vide des champs ;
- des seuils et transitions ;
- de la renormalisation.

Schéma :

```text
paramètre de départ
+ contributions quantiques et de seuil
-> valeur effective renormalisée
```

Une petite valeur finale peut sembler exiger des compensations extrêmement précises.

Mais la décomposition entre « valeur nue » et « corrections » dépend de la formulation. La question plus robuste est la stabilité de la petite valeur effective lorsque la théorie contient des seuils et contributions physiques connus.

## 5. Radiative stabilité

Contrairement à une simple valeur initialement petite, le problème se répète lorsque de nouvelles contributions effectives apparaissent à différentes échelles.

La difficulté est donc double :

```text
petitesse
+
stabilité de la petitesse sous les corrections et transitions
```

Cette structure rend le cas plus résistant qu'un réglage apparent provenant seulement de la redondance entre plusieurs grandeurs dérivées.

## 6. Protocole anthropique minimal

On suppose :

1. que `Lambda` prend différentes valeurs dans différents domaines ;
2. que les autres paramètres pertinents sont fixés ou suivent une distribution spécifiée ;
3. qu'une valeur positive trop grande interrompt la croissance avant la formation suffisante de structures ;
4. qu'une valeur négative de grande amplitude provoque une recollapse trop rapide ;
5. que la quantité de matière effondrée constitue un proxy pour les observateurs.

On écrit schématiquement :

```text
P(Lambda | observation)
proportionnel à
P_prior(Lambda) × F_structures(Lambda)
```

`F_structures` représente une fonction de sélection liée à la formation de structures.

## 7. Résultat et portée de l'argument de Weinberg

Les analyses de Weinberg, puis de Martel, Shapiro et Weinberg, montrent qu'une sélection par formation des galaxies peut rendre une petite valeur positive de `Lambda` observationnellement plausible dans un ensemble où `Lambda` varie.

La portée exacte est :

> Une fois admis un ensemble de domaines, un prior suffisamment régulier dans la petite région pertinente et un proxy de sélection par effondrement gravitationnel, la valeur observée peut être conditionnée par la nécessité de structures.

Ce n'est pas encore :

- un mécanisme microphysique produisant l'ensemble ;
- une dérivation unique du prior ;
- une mesure complète du multivers ;
- une explication de tous les paramètres cosmologiques.

## 8. Paramètres corrélés

Le seuil de formation des structures dépend aussi :

- de l'amplitude primordiale des fluctuations ;
- de la densité de matière ;
- du contenu en matière noire ;
- de l'époque de recombinaison ;
- de la durée disponible ;
- des critères retenus pour une structure habitable.

Une variation simultanée de `Lambda` et de l'amplitude `Q` peut déplacer la région admissible.

La question anthropique ne porte donc pas seulement sur :

```text
quelle valeur maximale de Lambda ?
```

mais sur :

```text
quelle région corrélée de {Lambda, Q, rho_m, ...} permet quelles structures ?
```

## 9. Paysage et discrétuum

Bousso et Polchinski proposent qu'un ensemble de flux quantifiés puisse produire un grand nombre de contributions discrètes à la constante cosmologique.

Avec plusieurs flux, les valeurs admissibles peuvent former un ensemble suffisamment dense pour contenir des valeurs petites.

Cette proposition fournit un mécanisme possible pour :

```text
engendrer une multiplicité de valeurs de Lambda
```

Elle ne fournit pas automatiquement :

```text
la mesure probabiliste complète
+ la dynamique de peuplement
+ la fonction de sélection
```

Le paysage rend l'hypothèse de variation plus concrète, mais ne clôt pas l'inférence statistique.

## 10. Problème de la mesure

Un ensemble comportant de très nombreux domaines ou une inflation éternelle nécessite une règle de comparaison des occurrences.

Les prescriptions de mesure peuvent modifier les probabilités attribuées aux observations.

Le problème n'est pas seulement mathématique :

- quelles régions sont comptées ?
- à quel temps ou sur quelle hypersurface ?
- comment traiter des volumes infinis ?
- quelle classe d'observateurs ou de structures pondère-t-on ?

Conséquence :

> La multiplicité physique ne suffit pas à transformer le fine-tuning en probabilité calculée.

## 11. Contrefactuels

### 11.1 `Lambda` positive plus grande, paramètres fixés

L'accélération devient dominante plus tôt et peut empêcher une fraction importante de la matière de s'effondrer en structures liées.

### 11.2 `Lambda` négative de grande amplitude

La recollapse peut intervenir avant le développement de structures durables.

### 11.3 `Lambda` et amplitude primordiale variables

Une amplitude de perturbations plus grande peut permettre une formation plus précoce des structures et modifier la limite environnementale sur `Lambda`.

### 11.4 `Lambda` remplacée par un champ dynamique

Le problème change d'objet : il faut analyser le potentiel, les conditions initiales et la dynamique du champ. Le réglage peut être réduit, transformé ou déplacé, mais n'est pas automatiquement résolu.

## 12. Ce que l'architecture relationnelle dissout

Elle dissout ou corrige :

- le traitement de `H_0` comme constante fondamentale supplémentaire ;
- le traitement de `Omega_Lambda` comme valeur primitive indépendante ;
- le comptage séparé de grandeurs reliées par la même histoire cosmologique ;
- l'idée qu'une tension de données constitue une nouvelle constante à expliquer.

## 13. Ce qu'elle ne dissout pas

Elle ne dissout pas :

- la petitesse de la valeur effective de `Lambda` ;
- sa stabilité radiative ;
- l'absence de mécanisme accepté fixant sa valeur ;
- la nécessité d'une mesure dans les explications statistiques ;
- la dépendance des conclusions anthropiques aux paramètres corrélés.

Le cas conserve donc une contingence résiduelle forte.

## 14. Principe anthropique faible

Le principe anthropique faible possède ici une fonction claire :

```text
conditionner l'observation de Lambda à l'existence de structures
```

Il ne produit pas les valeurs de `Lambda`. Il sélectionne dans un ensemble dont l'existence et la distribution doivent être établies séparément.

Le cas de la constante cosmologique est donc plus favorable à une analyse anthropique que le cas de l'échelle faible, mais cette différence est conditionnelle aux hypothèses de réalisation et de mesure.

## 15. Interprétation de dessein

Le cas peut alimenter un argument de dessein en raison de l'extrême petitesse alléguée de la région compatible avec les structures.

La présente méthode impose toutefois de séparer :

1. la sensibilité structurelle ;
2. la probabilité sous une mesure déterminée ;
3. l'absence actuelle de mécanisme ;
4. l'inférence d'une intention.

Le passage du troisième au quatrième point n'est pas une déduction de la physique seule.

## 16. Contingence résiduelle

Après audit, restent :

- la valeur effective de `Lambda` ;
- la structure des contributions du vide ;
- le choix éventuel du vide ou du secteur de flux ;
- le prior et la mesure ;
- les corrélations avec les autres paramètres cosmologiques ;
- le critère de sélection observationnelle.

## 17. Verdict provisoire

| Dimension | Verdict |
|---|---|
| multiplication de constantes cosmologiques indépendantes | largement dissoute par la refondation |
| petitesse effective de `Lambda` | problème résiduel fort |
| stabilité radiative | problème résiduel fort |
| sensibilité de la formation des structures | réelle, mais multiparamétrique |
| explication anthropique | possible sous hypothèses explicites |
| prédiction probabiliste complète | non acquise faute de mesure et de prior établis |
| dissolution par mécanisme constitutif connu | non |

Formule provisoire :

> La refondation retire du dossier plusieurs faux cadrans cosmologiques, mais elle ne dissout pas le problème de la constante cosmologique. Elle le reformule comme l'articulation de trois énigmes : petitesse et stabilité de la valeur effective, réalisation physique d'un ensemble de valeurs, et sélection observationnelle dans cet ensemble.

## 18. Sources

- Steven Weinberg, *The Cosmological Constant Problems*, arXiv:astro-ph/0005265.
- Hugo Martel, Paul R. Shapiro et Steven Weinberg, *Likely Values of the Cosmological Constant*, arXiv:astro-ph/9701099.
- Raphael Bousso et Joseph Polchinski, *Quantization of Four-form Fluxes and Dynamical Neutralization of the Cosmological Constant*, arXiv:hep-th/0004134.
- G. W. Gibbons et Neil Turok, *The Measure Problem in Cosmology*, arXiv:hep-th/0609095.
- Roni Harnik, Graham D. Kribs et Gilad Perez, *A Universe Without Weak Interactions*, arXiv:hep-ph/0604027.
- Fred C. Adams, *The Degree of Fine-Tuning in our Universe — and Others*, arXiv:1902.03928.
