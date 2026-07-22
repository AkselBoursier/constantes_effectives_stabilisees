# T1.3 — Fiche d’extraction lattice ALPHA 2026 de `alpha_s(m_Z)` v0.1

## 0. Statut

```text
statut : fiche primaire de chaîne d’extraction ;
date de contrôle : 21 juillet 2026 ;
source de référence : Nature 652, 328–334 (2026) ;
fonction : rendre contrôlables les deux routes lattice et leur combinaison ;
ne vaut pas : reproduction exécutée du paquet public, audit du code de simulation,
               validation indépendante des extrapolations ou moyenne lattice générale.
```

## 1. Porteurs et niveaux de sortie

La chaîne produit plusieurs objets qu’il faut maintenir distincts :

```text
couplages de volume fini dans des schémas GF et SF ;
échelles de référence définies par ces couplages ;
Lambda_MSbar^(3) dans la théorie à trois saveurs ;
relations de matching entre N_f = 3, 4 et 5 ;
alpha_s^(5)(m_Z) dans le schéma MS-bar ;
accord entre deux routes non perturbatives vers Lambda_MSbar^(3).
```

Le paramètre final est :

```text
alpha_s = alpha_MSbar^(N_f=5) ;
référence : m_Z ;
résultat : alpha_s(m_Z) = 0.11876(58).
```

Le porteur du test de maintien ne peut donc pas être réduit à la valeur finale : il inclut
la cohérence entre couplages de schémas intermédiaires, échelles, limites du continuum,
matching et deux routes vers le même `Lambda_MSbar^(3)`.

## 2. Entrée physique et fixation de l’échelle

Les simulations lattice sont raccordées à la physique hadronique basse énergie par des
résultats de fixation d’échelle provenant de plusieurs calculs. Une échelle technique de
flot de gradient, `sqrt(t_0)`, sert d’intermédiaire entre les entrées expérimentales et
l’échelle de découplage.

Les déterminations disponibles de `sqrt(t_0)` présentent une dispersion supérieure aux
erreurs individuelles. Les auteurs appliquent une procédure inspirée du Particle Data
Group puis élargissent encore l’incertitude afin de couvrir les valeurs centrales
précises :

```text
sqrt(t_0) = 0.1434(7)_stat(17)_robust(18)_total fm.
```

Cette composante robuste est la principale incertitude non statistique, mais son retrait
ne réduirait l’erreur finale sur `alpha_s` que d’environ 10 % selon l’article.

L’échelle intermédiaire est définie par :

```text
alpha_GF(mu_dec) = 3.949 / (4 pi) ;
mu_dec sqrt(t_0) = 0.5831(71) ;
mu_dec = 803(14) MeV.
```

La définition de `mu_dec` est une opération de schéma et de fixation d’échelle, non une
frontière physique dure de la QCD.

## 3. Route A — step scaling direct en QCD à trois saveurs

### Domaine non perturbatif

```text
théorie simulée : QCD N_f = 3 ;
échelle de volume fini : mu = 1/L ;
basse à moyenne énergie : schéma de flot de gradient (GF) ;
haute énergie : schéma de Schrödinger fonctionnel (SF).
```

Le jeu direct comprend 98 simulations sur 10 volumes entre environ 0,2 et 4,4 GeV,
avec une nouvelle résolution fine allant jusqu’à `L/a = 64`. Il est raccordé aux
simulations de haute énergie antérieures, couvrant environ 4 à 140 GeV de manière non
perturbative.

Le step scaling compare des volumes `L` et `2L`, extrapole chaque étape au continuum et
itère les changements d’échelle. Cette trajectoire est un chemin computationnel et une
représentation non perturbative du running ; elle n’est pas l’histoire temporelle d’un
système.

### Résultat de la route directe

```text
Lambda_MSbar^(3) / mu_dec = 0.433(11) ;
Lambda_MSbar^(3) = 347(11) MeV.
```

Les conversions de schéma vers `MS-bar` n’interviennent qu’à haute énergie, où le
couplage est faible.

## 4. Route B — découplage non perturbatif

Trois quarks fictifs dégénérés de masse invariante par renormalisation `M` sont introduits.
À énergie bien inférieure à `M`, la théorie massive se rapproche de la théorie de jauge
pure `N_f = 0`, avec corrections en puissances de `1/M`.

```text
z = M / mu_dec : 4, 6, 8, 10, 12 ;
M approximatif : 3 à 10 GeV ;
condition de coupe centrale : (a M)^2 < 0.16 ;
corrections de découplage dominantes : O(1/M^2).
```

Une détermination non perturbative de `b_g` permet d’annuler les termes dangereux
linéaires en `aM` qui dominaient auparavant l’incertitude systématique de cette route.
Les couplages massifs sont extrapolés conjointement en espacement de réseau et en masse,
puis raccordés au running très précis de la théorie de jauge pure.

Exemples de valeurs continues rapportées :

```text
alpha_GF(mu_dec, M) = 0.4184(22) pour z = 4 ;
alpha_GF(mu_dec, M) = 0.4600(41) pour z = 12.
```

L’extrapolation vers `M -> infini` conduit à :

```text
Lambda_MSbar^(3) / mu_dec = 0.426(10) ;
Lambda_MSbar^(3) = 342(10) MeV.
```

## 5. Combinaison des routes

Les deux méthodes ont des systématiques très différentes, mais ne sont pas totalement
indépendantes : elles partagent notamment la fixation de l’échelle basse énergie et
`mu_dec`.

Leur accord autorise dans l’article une combinaison corrélée :

```text
Lambda_MSbar^(3) = 344.4(8.7) MeV.
```

Le passage à la théorie à cinq saveurs inclut les effets des quarks charm et bottom par
matching perturbatif à ordre élevé, avec contrôle des effets non perturbatifs résiduels.
Il conduit à :

```text
alpha_s^(5)(m_Z) = 0.11876(58).
```

L’article indique que les incertitudes statistiques dominent dans les deux routes et que
la troncature perturbative ne représente qu’une faible fraction du budget de variance.

## 6. Schémas, running et raccordements

```text
schémas non perturbatifs : GF et SF en volume fini ;
schéma de sortie : MS-bar ;
fonction bêta MS-bar : connue à cinq boucles ;
matching N_f = 3 -> 4 -> 5 : relations perturbatives de haute précision ;
matching N_f = 3 -> 0 dans la route B : facteur P connu à quatre boucles, complété par
                                      simulations massives et limite de découplage.
```

La connaissance de `Lambda_MSbar` et de la fonction bêta détermine le couplage à toute
échelle dans la théorie et le schéma déclarés. Le maintien porte sur cette relation de
running, non sur l’identité numérique de `alpha_s(mu)` lorsque `mu` change.

## 7. Chaîne computationnelle et réplication

```text
production des configurations : version modifiée d’openQCD 1.6 ;
branche publique du code massif : gbar-massive ;
format de données : BDIO ;
analyse statistique : méthode Gamma ;
propagation des erreurs : différentiation automatique ;
paquet de réplication : jeu réduit annoncé comme suffisant pour reproduire les analyses
                        et nombres finaux.
```

Le paquet contient les données réduites, des fichiers d’entrée et le code d’analyse. Il
rend la route lattice plus reproductible à court terme que les trois chaînes
phénoménologiques du premier lot, dont les fits nécessitent des ensembles de données et
des infrastructures plus dispersés.

## 8. Typage des chemins

```text
chemin physique : running RG de la QCD et découplage des saveurs lourdes ;
chaîne de réalisation numérique : champs lattice, volumes, espacements et observables GF/SF ;
chemin computationnel A : step scaling et limites du continuum successives ;
chemin computationnel B : masses fictives, limite du continuum puis M -> infini ;
chemin inférentiel : extrapolations corrélées et combinaison des deux routes ;
chemin métrologique : fixation de l’unité physique par sqrt(t_0) et données hadroniques ;
chemin de représentation : schémas GF, SF et MS-bar ;
chemin de raccordement : N_f = 0, 3, 4 et 5 ;
histoire temporelle : non pertinente.
```

## 9. Test de maintien provisoire

La chaîne fournit un cas particulièrement net où la constance pertinente ne peut être
l’identité d’une valeur sous changement d’échelle. Deux constructions numériques
différentes aboutissent à des estimations compatibles d’un même paramètre `Lambda_MSbar^(3)`,
puis à une même relation de running et de matching vers `alpha_s^(5)(m_Z)`.

Le porteur provisoire du maintien est :

```text
la cohérence d’une structure RG et de ses raccordements, réalisée par deux chemins
non perturbatifs distincts mais partiellement corrélés.
```

Le résultat teste simultanément :

- l’universalité attendue de la limite du continuum ;
- la cohérence des changements de schéma ;
- la compatibilité des routes directe et découplage ;
- la stabilité du paramètre de sortie sous variations d’analyse déclarées.

## 10. Dimensions et portée

```text
dimension objet : Lambda_MSbar^(3), beta-fonction et alpha_s^(5)(m_Z) ;
dimension accès : observables lattice, extrapolations et fixation de l’échelle ;
dimension constitution : dynamique QCD non perturbative et découpages N_f ;
portée physique : détermination de premier principe de la relation de running ;
portée épistémologique : accord de routes, corrélations et budgets d’erreur ;
portée ontologique : non engagée.
```

## 11. Limites et opération suivante

La fiche établit la structure principale, mais la reproduction n’est pas encore exécutée.
Elle doit contrôler :

1. l’intégrité et la version du paquet de réplication ;
2. les dépendances Julia, C ou Python requises ;
3. la reconstruction des deux valeurs de `Lambda_MSbar^(3)` et de leur combinaison ;
4. le matching vers `alpha_s^(5)(m_Z)` ;
5. la décomposition du budget d’erreur ;
6. la sensibilité aux variantes d’extrapolation incluses dans le paquet.

Contrairement aux trois autres fiches, ces opérations sont annoncées comme réalisables à
partir d’un paquet public borné. Elles constituent donc le point d’entrée prioritaire de
T1.5 après construction de la matrice T1.4.