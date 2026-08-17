# Chantier Q (catégories, accès et inférences) — Stern–Gerlach : matrice des fonctions v0.1

## 0. Légende

- La préparation ou l'individuation de l'objet d'étude est notée `PREP`.
- Le réglage, l'intervention ou le contrôle matériel sont notés `OPER`.
- Le rôle dans le modèle, le calcul ou la représentation est noté `FORM`.
- L'enregistrement ou la stabilisation d'une trace sont notés `ENR`.
- L'inférence à partir des traces est notée `INF`.
- La description publique et reproductible est notée `COM`.
- La fonction pédagogique est notée `PED`.
- Le risque d'engagement ontologique excédant la fonction établie est noté
  `ONT?`.

Les colonnes distinguent l'expérience historique (`H`), le modèle quantique
idéalisé (`I`) et les dispositifs modernes ou séquentiels (`M`).

## 1. Vue synthétique

| Catégorie | H — 1922 | I — modèle idéal | M — usages modernes | Profil principal | Risque de migration |
|---|---|---|---|---|---|
| atome / particule | unité supposée du faisceau, non détectée individuellement | système composite espace × spin | unité préparée et parfois détectée événement par événement | PREP, FORM, INF | point matériel classique doté d'une trajectoire complète |
| faisceau | objet matériel préparé et collimaté | ensemble ou distribution d'états | ressource préparée, filtrée ou polarisée | PREP, OPER, COM | confondre ensemble, mélange et superposition |
| trajectoire | géométrie de propagation et approximation cinématique | option semi-classique, non exigée par l'évolution ondulatoire | reconstruction ou approximation selon le dispositif | OPER, FORM, PED | chemin microscopique classique préexistant |
| orientation | orientation du champ et du montage | paramètre déterminant la composante couplée | variable de contrôle des séquences | OPER, FORM | direction intrinsèque classique déjà possédée |
| axe | géométrie macroscopique de l'aimant | base et opérateur `S_n` | repère de préparation et d'analyse | OPER, FORM, COM | axe matériel = axe propre de l'objet |
| position | coordonnée du dépôt cumulatif | variable pointeur corrélée au spin | donnée de détecteur | FORM, ENR, INF | position = spin ou propriété directement lue |
| impact / dépôt | dépôt collectif après plusieurs heures | événement idéalisé ou région de lecture | événement détecté ou image résolue | ENR, INF | trace unique supposée déjà donnée dans H |
| deux bandes / deux classes | structure empirique du dépôt | spectre à deux valeurs + séparation spatiale + seuil | classes de détection calibrées | ENR, INF, COM | deux orientations classiques préexistantes |
| état | non formulé dans le langage moderne du spin | vecteur ou opérateur de densité | objet de préparation et de tomographie | FORM, PREP, INF | chose matérielle simple indépendamment de l'interprétation |
| propriété | quantification spatiale attribuée à l'atome | valeur d'une composante dans un contexte de mesure | attribution conditionnelle à préparation et protocole | INF, COM, ONT? | propriété non contextuelle révélée sans transformation |
| mesure | dispositif et exposition complets | chaîne interaction–corrélation–détection–classification | opération instrumentale parfois séquentielle | OPER, ENR, INF | instant unique ou simple lecture passive |
| résultat | motif cumulatif de deux bandes | issue `+/-` ou distribution prédite | événement, fréquence, corrélation ou état préparé | ENR, INF, COM | effacer la différence entre trace, donnée et énoncé |

## 2. Analyse par catégorie

### 2.1 Atome / particule

**H.** Le terme individue ce qui compose le faisceau, mais l'expérience enregistre une couche de matière accumulée. Elle ne fournit pas un journal d'atomes singuliers.

**I.** L'atome est représenté par un état dans un produit d'espaces : degré spatial et degré de spin. Le mot `particule` ne justifie pas une ontologie de point classique.

**M.** Selon le détecteur, l'atome peut être compté individuellement, filtré ou réutilisé comme état préparé.

```text
fonction stable : individuer le porteur du moment magnétique et de la détection ;
fonction variable : point classique, paquet d'onde, excitation, événement détecté ;
interdit : importer la première image dans toutes les étapes.
```

### 2.2 Faisceau

Le faisceau est une catégorie fortement classique et néanmoins indispensable à la pratique : flux, largeur, divergence, vitesse, collimation et intensité.

Il ne faut toutefois pas lui attribuer automatiquement un état quantique pur commun. Un faisceau thermique peut être un mélange statistique. Une suite de dispositifs peut transformer un faisceau en sous-ensemble préparé.

Le faisceau montre qu'une catégorie macroscopique peut être indispensable à la préparation sans constituer une propriété fondamentale de chaque atome.

### 2.3 Trajectoire

Trois fonctions doivent rester séparées :

```text
géométrie du montage et axe moyen de propagation — OPER ;
mouvement du centre d'un paquet ou approximation newtonienne — FORM ;
chemin individuel défini — engagement interprétatif supplémentaire.
```

La trajectoire est le meilleur cas négatif de la matrice : utile dans certaines opérations et explications, mais dispensable dans un traitement quantique complet du couplage espace–spin.

### 2.4 Orientation

L'orientation du champ est une variable macroscopique réelle, réglable et communicable. Dans le modèle idéal, elle détermine l'opérateur de composante qui entre dans l'interaction effective.

La phrase correcte est :

> le dispositif oriente le couplage et sélectionne la composante représentée dans cette opération.

La phrase excessive est :

> le dispositif révèle l'orientation complète que le spin possédait déjà comme un vecteur classique.

### 2.5 Axe

Le mot `axe` accomplit au moins trois fonctions :

```text
axe géométrique du montage ;
axe du champ dominant ;
axe formel définissant une base et un opérateur de composante.
```

Ces fonctions sont coordonnées, mais non identiques. La réussite expérimentale exige précisément leur mise en correspondance par calibration et modélisation.

### 2.6 Position

La position est la variable d'accès qui transporte l'information sur le spin vers le registre de détection.

```text
spin -> couplage dépendant du champ -> impulsion/position -> trace -> classe.
```

La position n'est donc ni un simple décor ni la propriété de spin. Elle joue le rôle de médiation matérielle et formelle.

### 2.7 Impact et dépôt

Dans H, le terme pertinent est d'abord `dépôt cumulatif`. Parler d'impacts individuels observés rétro-projette un dispositif moderne dans l'expérience historique.

Dans I, l'impact est souvent introduit comme résultat final sans modélisation du détecteur. Il sert alors de frontière pédagogique ou interprétative.

Dans M, un événement de détecteur peut être localisé, horodaté et classé, mais sa signification dépend encore du modèle de l'instrument.

### 2.8 Deux bandes et deux classes

Les deux bandes historiques sont une structure empirique du dépôt. Les deux valeurs propres de `S_z` sont une structure du formalisme. Les deux régions du détecteur sont une partition opératoire. Leur concordance est le résultat du dispositif et du modèle, non une identité lexicale.

```text
spectre discret != deux traces != deux seuils != deux objets classiques.
```

### 2.9 État

L'état quantique est indispensable à la prédiction et à la comparaison de séquences d'appareils. Son statut ontologique reste interprétation-dépendant.

La matrice ne décidera donc pas si l'état est réel, informationnel, relationnel ou dispositionnel. Elle enregistre seulement ses fonctions :

```text
préparer ;
représenter ;
calculer ;
conditionner des probabilités ;
mettre en relation plusieurs appareils.
```

### 2.10 Propriété

Le terme `propriété` peut désigner :

```text
une valeur propre préparée ;
une valeur obtenue dans une opération ;
une disposition à produire certaines statistiques ;
une attribution interprétative au système ;
une caractéristique stable de l'espèce atomique.
```

Le pilote interdit de passer de l'une à l'autre sans argument. La question `le spin avait-il déjà cette valeur ?` ne reçoit pas de réponse unique du seul schéma expérimental.

### 2.11 Mesure

Le terme est distribué sur une chaîne :

```text
réglage de l'axe ;
interaction ;
corrélation espace–spin ;
séparation ;
détection ;
stabilisation d'une trace ;
classification ;
énoncé de résultat.
```

Une théorie peut expliquer certaines transitions de cette chaîne sans expliquer toutes les autres. Employer `mesure` pour l'ensemble reste pratique, mais ne doit pas masquer les opérations.

### 2.12 Résultat

Dans H, le résultat est principalement un motif collectif reproductible. Dans I, il peut être l'une des deux issues idéales ou la distribution de Born. Dans M, il peut être un événement individuel, une fréquence, une corrélation ou un état préparé en sortie.

Le mot `résultat` change donc d'unité et d'échelle. Cette migration est philosophiquement plus importante que son apparente continuité lexicale.

## 3. Matrice des accès

| Étape | Matériel | Opératoire | Représentationnel | Inférentiel | Intersubjectif | Pédagogique |
|---|---:|---:|---:|---:|---:|---:|
| production du faisceau | fort | fort | moyen | faible | moyen | moyen |
| collimation | fort | fort | moyen | faible | fort | moyen |
| orientation du champ | fort | fort | fort | moyen | fort | fort |
| interaction spin–position | fort | moyen | très fort | moyen | moyen | fort |
| séparation spatiale | fort | moyen | très fort | moyen | moyen | fort |
| détection | très fort | fort | moyen | fort | fort | moyen |
| coarse-graining en deux régions | moyen | fort | fort | très fort | fort | fort |
| attribution `+/-` | faible | moyen | très fort | très fort | très fort | très fort |
| portée ontologique | faible | faible | fort | très fort | fort | très fort |

Le profil confirme que l'accès ne peut être placé uniquement après la physique : il intervient dans la préparation, le choix de l'observable, la corrélation, la détection et l'inférence.

## 4. Coupes non équivalentes

| Coupe | Ce qu'elle sépare | Ce qu'elle modifie | Ce qu'elle ne décide pas seule |
|---|---|---|---|
| matérielle | source, aimant, vol libre, détecteur | contrôle et provenance des interactions | ontologie du système |
| système / appareil | degrés traités comme objet et pointeur | structure du modèle de mesure | emplacement d'un effondrement réel |
| formelle | espace spatial × espace de spin | calcul des corrélations | nature métaphysique des facteurs |
| choix d'axe | composante `S_n` parmi d'autres | probabilités et états propres pertinents | orientation classique complète du spin |
| coarse-graining | régions de positions et seuils | classes de résultats, erreurs et information | spectre fondamental à lui seul |
| historique | dispositif de 1922 / reconstruction moderne | sens des termes et conclusions disponibles | vérité d'une interprétation actuelle |
| pédagogique | ce qui est montré / reporté | charge cognitive et contresens possibles | structure physique réelle |

Le mot `coupe` n'est donc pas un concept unique déjà constitué. Il désigne une famille de partitions dont les effets doivent être spécifiés.

## 5. Premier résultat de discrimination

La matrice produit au moins quatre profils différents :

```text
axe/orientation : nécessaire matériellement et formellement ;
trajectoire : utile comme approximation, dispensable comme structure générale ;
impact/dépôt : essentiel à l'enregistrement mais distinct de la propriété ;
propriété/état : essentiels à l'inférence et au formalisme, ontologiquement ouverts.
```

Le résultat provisoire n'est donc pas `les catégories classiques sont nécessaires`, mais :

> Leur nécessité est locale, fonctionnelle et asymétrique ; une catégorie peut être indispensable dans une couche et illégitime dans une autre.
