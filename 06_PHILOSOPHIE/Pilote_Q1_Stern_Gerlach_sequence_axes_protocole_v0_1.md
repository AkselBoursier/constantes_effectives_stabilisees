# Chantier Q (catégories, accès et inférences) — Séquences d'axes : protocole v0.1

## Statut

```text
statut : second test du chantier Q, corrigé méthodologiquement ;
objet : séquences idéalisées d'analyseurs Stern–Gerlach de spin 1/2 ;
fonction : distinguer préparation, sélection, analyse, séparation cohérente,
           décohérence et résultat terminal ;
limite : ces séquences ne sont pas identifiées sans réserve à l'expérience de 1922.
```

## 1. Opérations distinctes

```text
séparer : corréler spin et position ;
analyser : rendre accessibles les probabilités de deux sorties ;
détecter : produire un enregistrement ;
sélectionner : transmettre une sortie et bloquer l'autre ;
préparer : utiliser cette sortie comme entrée ultérieure ;
recombiner : réunir cohérentement les branches ;
décohérer : rendre la phase relative inexploitable ;
ignorer : ne pas conditionner l'analyse sur le chemin.
```

Un même appareil peut donc remplir plusieurs fonctions selon sa place dans la chaîne et l'usage de ses sorties.

## 2. Deux protocoles à ne pas confondre

### 2.1 Séquence sur le même système

Dans une chaîne telle que :

```text
SG_z -> sélection +z -> SG_x -> sélection +x -> SG_z,
```

le même atome transmis poursuit la séquence. Il n'est jamais ramené à l'état initial `+z` entre deux appareils. Chaque sélection ou interaction fournit l'état d'entrée de l'étage suivant. La mesure intermédiaire selon `x` ne laisse donc pas disponible un exemplaire non perturbé du même système pour une mesure ultérieure selon `z`.

### 2.2 Comparaison de plusieurs angles pour une même préparation

Lorsque l'objectif est de comparer les probabilités selon `x`, `y` et `z` pour une préparation donnée, on n'utilise pas successivement le même système comme s'il pouvait être réinitialisé sans opération. On répète la préparation sur un ensemble de systèmes supposés équivalents, puis on distribue les essais entre plusieurs réglages :

```text
préparation P -> sous-ensemble E_x -> analyse selon x ;
préparation P -> sous-ensemble E_y -> analyse selon y ;
préparation P -> sous-ensemble E_z -> analyse selon z.
```

La comparaison repose donc sur la reproductibilité de la procédure de préparation et sur des statistiques d'ensemble. Elle ne donne pas simultanément plusieurs composantes incompatibles d'un même individu non perturbé.

### 2.3 Réversibilité cohérente : cas distinct

Si les branches ont seulement été séparées de manière cohérente, sans détection ni fuite incontrôlée d'information de chemin, une opération inverse ou une recombinaison peut en principe restaurer l'état spatial et la cohérence avec une précision limitée. Ce protocole spécial ne constitue pas un retour après mesure irréversible et ne doit pas être confondu avec la repréparation d'un nouvel ensemble.

## 3. Formalisme minimal

Pour un état `|+a>` analysé selon un axe `b` formant un angle `theta` avec `a` :

```text
P(+b | +a) = cos²(theta / 2)
P(-b | +a) = sin²(theta / 2).
```

D'où :

```text
P(+z | +z) = 1 ;
P(+x | +z) = P(-x | +z) = 1/2.
```

Ces relations décrivent le modèle idéal. Elles ne remplacent pas la dynamique spatiale, les champs réels, la résolution des détecteurs ou l'analyse de cohérence.

## 4. Première séquence (`S1`) — `+z`, puis `z`

```text
source -> SG_z -> sélection +z -> SG_z -> détection.
```

La seconde analyse donne `+z` avec certitude dans le modèle idéal. Le premier dispositif ne fonctionne pas seulement comme mesure : sa sortie sélectionnée prépare le sous-ensemble soumis au second appareil.

## 5. Deuxième séquence (`S2`) — `+z`, puis `x`

```text
source -> SG_z, sélection +z -> SG_x -> détection.
```

Les sorties `+x` et `-x` sont équiprobables. L'orientation du second appareil ne présente pas simplement une propriété vectorielle classique déjà complètement déterminée : elle définit l'observable et les alternatives expérimentales pertinentes.

Ce résultat ne décide pas à lui seul si la propriété est créée, révélée, relationnelle ou seulement représentée par l'état.

## 6. Troisième séquence (`S3`) — `+z`, sélection `+x`, puis `z`

```text
source -> SG_z, sélection +z -> SG_x, sélection +x -> SG_z -> détection.
```

La dernière analyse donne `+z` et `-z` avec probabilités égales. L'étape intermédiaire prépare un état `+x` pour la suite ; elle ne constitue pas une simple lecture passive d'une valeur `x` ajoutée à une valeur `z` intacte. Aucun retour à l'état `+z` n'est effectué avant le dernier analyseur.

Le mot `perturbation` doit rester différencié : couplage dynamique, conditionnement sur une sortie, changement de l'état prédictif et perte de cohérence ne sont pas la même opération.

## 7. Séparation cohérente selon `x`

On peut écrire :

```text
|+z> = (|+x> + |-x>) / sqrt(2).
```

Une séparation cohérente produit idéalement :

```text
(|+x>|phi_+> + |-x>|phi_->) / sqrt(2).
```

La séparation spatiale n'est donc pas encore, à elle seule, un mélange classique. Tant qu'aucun enregistrement irréversible ou couplage incontrôlé ne distingue les chemins, une recombinaison suffisamment contrôlée peut en principe tester ou restaurer la cohérence.

Les réalisations modernes d'interféromètres Stern–Gerlach montrent que cette cohérence est expérimentalement testable, mais au prix d'un contrôle strict des gradients, positions, impulsions et phases.

## 8. Chemins ignorés ou décohérés

Si les deux branches deviennent orthogonales et que le chemin est ignoré ou corrélé à un environnement, l'état réduit du spin devient :

```text
rho = 1/2 |+x><+x| + 1/2 |-x><-x|.
```

Une analyse finale selon `z` donne alors `1/2, 1/2`.

## 9. Même statistique finale, états intermédiaires différents

Les deux procédures suivantes ont la même distribution finale selon `z` :

```text
A. sélectionner +x, puis analyser z ;
B. séparer en ±x, perdre la cohérence ou ignorer le chemin, puis analyser z.
```

Mais :

```text
A : état pur |+x> ;
B : mélange 1/2 |+x><+x| + 1/2 |-x><-x|.
```

Une seule lecture finale selon `z` ne reconstruit donc pas l'histoire de préparation. Pour les distinguer, il faut répéter une procédure de préparation contrôlée et effectuer d'autres analyses sur d'autres membres de l'ensemble, ou employer une recombinaison cohérente adaptée.

## 10. Distinctions obtenues

```text
séquence sur le même système != comparaison entre ensembles repréparés ;
superposition cohérente != mélange ;
séparation != détection ;
détection != sélection ;
sélection != simple lecture ;
mesure sélective != mesure non sélective ;
statistique terminale != histoire complète de préparation.
```

## 11. Sources directrices

- Tekin, B. (2015), *Stern-Gerlach Experiment with Higher Spins*, arXiv:1506.04632.
- Margalit, Y. et al. (2018/2020), *Realization of a complete Stern-Gerlach interferometer*, arXiv:1801.02708 et arXiv:2011.10928.
- Amiet, J.-P. & Weigert, S. (1998), *Reconstructing a pure state of a spin s through three Stern-Gerlach measurements*, arXiv:quant-ph/9809018.

## Verdict technique provisoire

> Une séquence de Stern–Gerlach ne peut pas être décrite rigoureusement par la seule succession de « mesures ». Il faut préciser pour chaque étage s'il sépare, détecte, sélectionne, prépare, conserve une cohérence ou l'efface, et préciser si plusieurs axes sont appliqués successivement au même système ou comparés sur des ensembles repréparés.
