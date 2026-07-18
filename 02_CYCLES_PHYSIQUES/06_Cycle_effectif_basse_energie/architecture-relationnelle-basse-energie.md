# Dossier de transfert — architecture relationnelle basse énergie

## Statut

Ce document ouvre la reprise du cycle effectif basse énergie après la clôture conditionnellement positive du pilote Higgs–Yukawa et du test des cinq cas sentinelles.

Il procède d’abord par extraction et requalification du corpus interne. L’ancienne conclusion :

```text
architecture effective basse énergie confirmée
```

n’est pas reprise comme résultat acquis. Elle devient une hypothèse à éprouver.

Document source principal :

- [Synthese_cycle_effectif_basse_energie_v0_1.md](Synthese_cycle_effectif_basse_energie_v0_1.md)

## 1. Question du dossier

> Que devient une interaction ou une description lorsque certaines structures ne sont plus résolues explicitement dans le régime considéré ?

La question complémentaire est :

> Le terme « constante effective basse énergie » désigne-t-il une classe cohérente d’objets, ou plusieurs opérations de description irréductibles ?

## 2. Acquis internes à conserver

Le corpus distingue déjà quatre pôles :

```text
G_F / M_W
alpha_s(mu) / Lambda_QCD
G_N / alpha_G(E) / M_Pl
validité d’une description
```

Il contient surtout un acquis important :

```text
« basse énergie » n’a pas le même sens dans tous les secteurs.
```

- dans l’interaction faible, elle permet une approximation locale ;
- en QCD, elle conduit vers le couplage fort et le non-perturbatif ;
- en gravitation quantique effective, elle correspond à une suppression par des rapports d’échelle.

Cette différence doit être conservée sans transformer automatiquement ces cas en membres d’une architecture unique.

## 3. Principe de reprise

Chaque cas sera décrit par :

1. la théorie ou description de départ ;
2. le régime d’énergie ou de distance ;
3. ce qui n’est plus résolu explicitement ;
4. ce qui reste comme degrés de liberté ;
5. les coefficients ou échelles introduits ;
6. l’opération de raccordement ou de changement de description ;
7. la voie d’accès expérimentale ;
8. la condition de rupture de la description ;
9. le contrefactuel permettant d’éprouver l’explication.

Aucune famille générale n’est postulée.

## 4. Chaîne A — théorie de Fermi et secteur électrofaible

### 4.1 Description plus résolue

Dans le Modèle standard électrofaible, les processus faibles chargés sont médiés par le boson `W`.

Schématiquement, le propagateur contient :

```math
\frac{1}{q^2-M_W^2}.
```

Lorsque :

```text
|q^2| << M_W^2,
```

on peut développer :

```math
\frac{1}{q^2-M_W^2}
=-\frac{1}{M_W^2}
\left(1+\frac{q^2}{M_W^2}+\cdots\right).
```

Le terme dominant donne une interaction locale à quatre fermions.

### 4.2 Chaîne relationnelle

```text
théorie électrofaible avec W explicite
        |
        v
hiérarchie |q²| << M_W²
        |
        v
développement du propagateur
        |
        v
opérateurs locaux à quatre fermions
        |
        v
coefficient dominant G_F
        |
        v
corrections en q² / M_W² et corrections radiatives
```

Au niveau arbre :

```math
\frac{G_F}{\sqrt2}=\frac{g^2}{8M_W^2}.
```

### 4.3 Ce qui est expliqué

La description plus complète explique :

- pourquoi l’interaction semble locale à basse énergie ;
- pourquoi le coefficient est lié à `g` et `M_W` ;
- pourquoi des corrections apparaissent en puissances de `q^2/M_W^2` ;
- pourquoi la théorie de Fermi cesse d’être suffisante en approchant l’échelle du `W`.

### 4.4 Ce qui n’est pas expliqué

Cette réduction n’explique pas par elle-même :

- les valeurs ultimes de `g`, `M_W` ou `v` ;
- l’origine du secteur électrofaible ;
- l’absence ou la présence d’opérateurs de nouvelle physique.

## 5. Chaîne B — raccordement et évolution des coefficients

L’expression « intégrer le `W` » ne suffit pas à décrire toute la théorie effective.

Une chaîne plus complète est :

```text
théorie à haute énergie
        |
        v
choix d’une échelle de raccordement mu ~ M_W
        |
        v
calcul des coefficients de Wilson
        |
        v
évolution par groupe de renormalisation
        |
        v
seuils intermédiaires et changement de degrés de liberté
        |
        v
matrice d’éléments à basse énergie
        |
        v
observable
```

Un coefficient de Wilson n’est donc pas généralement un nombre fixe indépendant de l’échelle, de la base d’opérateurs ou du schéma.

### Première correction conceptuelle

```text
coefficient effectif
≠
constante absolue
```

La fixité éventuelle est relative :

```text
base + schéma + échelle + ordre + domaine cinématique.
```

## 6. Chaîne C — accès à `G_F`

```text
durée de vie du muon
+ espace de phase
+ corrections QED
+ corrections électrofaibles
        |
        v
extraction de G_F
        |
        v
comparaison avec d’autres processus faibles
```

Cette chaîne est inférentielle. Elle ne doit pas être confondue avec le processus de raccordement théorique.

La valeur très précise de `G_F` dépend d’une articulation entre observable, conventions et calculs. Sa précision ne transforme pas la théorie de Fermi en description universelle.

## 7. Chaîne D — QCD : un cas contrasté

### 7.1 Flot du couplage

```math
\mu^2\frac{d\alpha_s}{d\mu^2}=\beta(\alpha_s).
```

À haute énergie, la liberté asymptotique rend la description perturbative efficace. Lorsque l’échelle diminue, le couplage augmente et la perturbation devient insuffisante.

### 7.2 Chaîne relationnelle

```text
Q élevé
        |
        v
alpha_s(Q) faible
        |
        v
description perturbative en quarks et gluons
        |
        v
évolution vers Q ~ Lambda_QCD
        |
        v
couplage fort et effets non perturbatifs
        |
        v
degrés de liberté hadroniques / méthodes adaptées
```

### Décision provisoire

La QCD basse énergie n’est pas un autre exemple simple de « médiateur lourd intégré ».

Elle constitue un contre-exemple à l’équation :

```text
basse énergie = description plus simple obtenue par suppression d’un propagateur lourd.
```

`alpha_s(Q)` doit être refusé comme constante simpliciter. `Lambda_QCD` marque une échelle dynamique, mais son statut précis dépend du schéma et de la définition utilisée.

## 8. Chaîne E — gravitation comme théorie effective

À basse énergie par rapport à l’échelle de Planck, les corrections quantiques gravitationnelles sont organisées par des puissances de rapports d’échelle.

Schématiquement :

```math
\alpha_G(E)\sim\frac{G_NE^2}{\hbar c^5}
\sim\left(\frac{E}{M_{\mathrm{Pl}}}\right)^2
```

selon les conventions choisies.

### Chaîne relationnelle

```text
relativité générale comme terme dominant
        |
        v
E / M_Pl << 1
        |
        v
corrections d’ordre supérieur supprimées
        |
        v
prédictions effectives basse énergie
        |
        v
perte de contrôle attendue lorsque la hiérarchie disparaît
```

### Prudence

Ce cas ne fournit pas un raccordement complet à une théorie UV connue. Il montre qu’une théorie peut être effective et prédictive à basse énergie même lorsque sa complétion à haute énergie reste ouverte.

`M_Pl` ne doit pas être traité sans précaution comme une frontière expérimentale nette où une nouvelle théorie apparaît brusquement.

## 9. Trois opérations provisoirement distinguées

| Opération | Cas | Ce qui change |
|---|---|---|
| réduction locale par médiateur lourd | Fermi / `W` | le propagateur est développé et remplacé par des opérateurs locaux |
| changement de régime dynamique | QCD | le couplage court et les degrés de liberté adaptés changent |
| expansion hiérarchique | gravitation effective | les corrections sont organisées par des rapports d’échelle petits |

Ces opérations ne sont pas encore déclarées membres d’une architecture unique.

La question de phase 2 sera :

> Possèdent-elles un noyau commun plus précis que le seul fait de dépendre d’un domaine de validité ?

## 10. Hypothèse commune minimale

Le noyau commun candidat n’est pas une « constante effective » unique, mais une structure de description :

```text
séparation d’échelles
+ choix de degrés de liberté
+ approximation ou expansion contrôlée
+ coefficients dépendant d’un cadre
+ estimation de l’erreur
+ domaine de rupture
```

Une théorie effective est explicative lorsqu’elle ne se contente pas d’ajuster des coefficients, mais relie leurs formes, leurs ordres de grandeur, leur évolution et leurs corrections à une structure plus résolue ou à des symétries.

## 11. Contrefactuels initiaux

### 11.1 Si `M_W` n’était pas grand devant l’impulsion transférée

Le développement local échouerait et `G_F` seul ne décrirait plus le processus.

### 11.2 Si `alpha_s` ne courait pas

La distinction entre régime perturbatif et régime de confinement serait profondément modifiée. `Lambda_QCD` ne jouerait pas le même rôle dynamique.

### 11.3 Si `E/M_Pl` n’était pas petit

L’expansion effective gravitationnelle perdrait son paramètre de contrôle et les opérateurs d’ordre supérieur ne seraient plus supprimés.

### 11.4 Si deux bases d’opérateurs étaient reliées par une redéfinition de champs

Les coefficients individuels pourraient changer tandis que les amplitudes physiques resteraient invariantes. La fonction de fixité ne peut donc pas être attribuée naïvement à chaque coefficient pris isolément.

## 12. Objets et fonctions locales

| Objet | Type | Fonction locale | Limite de l’attribution |
|---|---|---|---|
| `G_F` | coefficient effectif | fixe le terme local dominant dans un cadre basse énergie | dépend du cadre, des corrections et du domaine |
| `M_W` | masse physique / échelle | contrôle l’expansion du propagateur | n’est pas un seuil abrupt universel |
| coefficient de Wilson `C_i(mu)` | paramètre renormalisé | pondère un opérateur dans une base donnée | dépend de l’échelle, du schéma et de la base |
| `alpha_s(mu)` | couplage courant | organise la force du régime perturbatif | varie avec `mu` |
| `Lambda_QCD` | échelle dynamique | caractérise le changement de régime QCD | définition et valeur dépendantes du schéma |
| `G_N` | paramètre dimensionné | fixe le couplage gravitationnel classique | la force quantique se lit mieux par un rapport sans dimension |
| `M_Pl` | échelle construite | organise l’expansion hiérarchique gravitationnelle | pas une frontière nette démontrée |

## 13. Conditions d’échec du dossier

Le transfert échoue si :

- « effectif » devient une famille générale sans critère supplémentaire ;
- les trois opérations sont unifiées uniquement parce qu’elles possèdent toutes une échelle ;
- un coefficient de Wilson est traité comme invariant indépendamment de sa base et de son échelle ;
- la QCD basse énergie est décrite comme une simple intégration de modes lourds ;
- l’échelle de Planck est présentée comme un seuil expérimental net ;
- la précision de `G_F` est confondue avec l’universalité sans domaine de la théorie de Fermi ;
- aucune estimation d’erreur ou condition de rupture n’est fournie.

## 14. Travail de phase 2

La vérification externe devra :

1. contrôler le développement du propagateur et la normalisation de `G_F` ;
2. préciser matching, running, mélange d’opérateurs et dépendance de base ;
3. distinguer `Lambda_QCD` comme paramètre de schéma de l’échelle physique de confinement ;
4. contrôler la formulation de la gravitation comme EFT et le rôle de `M_Pl` ;
5. produire un registre explicatif et des contre-exemples plus stricts ;
6. décider si le noyau commun est physique, méthodologique ou seulement formel.

## 15. Décision provisoire

```text
Cycle basse énergie : matière interne substantielle, architecture générale non encore confirmée.
```

> Le corpus avait raison de refuser une image uniforme de la basse énergie. La refondation doit maintenant déterminer si les différents cas partagent une structure explicative commune ou seulement un vocabulaire de validité et d’échelle.
