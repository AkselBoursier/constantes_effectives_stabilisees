# N0 — Protocole commun des fiches d'accès neutrino v0.1

## 0. Statut et fonction

```text
statut : protocole actif pour l'exécution des étapes N1 à N5 ;
date : 17 juillet 2026 ;
date de coupure bibliographique : 17 juillet 2026 inclus ;
fonction : fixer le gabarit commun, la hiérarchie des sources, les règles de
           datation et les conditions de comparaison des quatre accès du cycle
           neutrino ;
base interne : synthèse de récupération du cycle 3, relevé contemporain du
               problème de la mesure, matrice d'incidence sur les dix cycles et
               arbitrage de la dette prioritaire ;
porte sur : oscillations, cinématique bêta, cosmologie de la somme des masses et
            double bêta sans neutrino ;
ne vaut pas : revue générale de la physique des neutrinos, état empirique déjà
               vérifié, classement définitif des expériences ou conclusion
               ontologique sur l'objet neutrino ;
révision : si une fiche montre que le gabarit homogénéise des opérations
           physiquement distinctes ou qu'une règle de source empêche de
           reconstruire une chaîne d'accès décisive.
```

Le protocole accomplit l'étape `N0` décidée dans l'[arbitrage de la dette
prioritaire](../../05_CARTES_ET_SYNTHESES/Arbitrage_dette_prioritaire_dix_cycles_v0_1.md).
Il prépare quatre reprises empiriques séparées avant leur comparaison. Il ne
préjuge ni leur résultat ni leur degré de compatibilité.

## 1. Principe directeur : comparer des énoncés situés, non des nombres isolés

Les quatre voies portent sur un même secteur physique, mais elles ne produisent
ni la même trace, ni le même objet publié, ni la même fonction du spectre. Le
protocole conserve donc une chaîne commune minimale sans imposer une identité des
opérations :

```text
objet ou processus ciblé
-> interaction ou sensibilité physique
-> trace enregistrée
-> sélection, calibration et corrections
-> observable publiée
-> modèle de mesure ou de passage
-> estimation, borne, exclusion ou posterior
-> énoncé scientifique situé.
```

L'unité de comparaison est un **énoncé empirique reconstruit avec sa chaîne
d'accès**. Elle comprend au minimum :

```text
grandeur ou fonction contrainte
+ données ou exposition
+ modèle et hypothèses
+ paramètres de nuisance et corrélations
+ convention statistique
+ résultat daté
+ limites de l'inférence.
```

Une valeur numérique sans ces éléments ne constitue pas un résultat comparable.
Inversement, les rubriques communes ne doivent pas être remplies artificiellement
lorsqu'une opération n'existe pas dans une voie donnée.

## 2. Datation et coupure bibliographique

### 2.1 Coupure commune

Sont admissibles dans les fiches `N1` à `N4` les documents rendus publics au plus
tard le **17 juillet 2026**. Une publication, une version acceptée ou un produit
de données postérieur est placé dans une rubrique de veille post-coupure ; il ne
modifie pas silencieusement le corpus de référence.

La coupure est bibliographique, non expérimentale. Une publication de 2026 peut
analyser des données arrêtées plusieurs années auparavant. Chaque source doit
donc porter quatre dates distinctes lorsqu'elles sont disponibles :

| Date | Fonction |
|---|---|
| publication ou diffusion publique | situe le document dans la littérature |
| coupure des données ou période d'exposition | situe l'état empirique réellement analysé |
| version de l'analyse, du modèle ou du produit de données | rend une source évolutive identifiable |
| date de consultation | permet de retrouver l'état d'une page ou d'un ajustement vivant |

### 2.2 Sources évolutives

Les ajustements globaux, pages de résultats, chaînes de Monte-Carlo et dépôts de
données peuvent être mis à jour sans nouvelle publication de méthode. Une fiche
doit alors enregistrer :

```text
nom de la ressource ;
version explicite ;
date des données annoncée par la ressource ;
date de consultation ;
publication méthodologique à citer conjointement ;
fichiers ou tableaux effectivement utilisés.
```

La formule « état de 2026 » est interdite si elle désigne seulement une page
consultée en 2026 alors que son jeu de données s'arrête en 2024 ou 2025.

### 2.3 Antériorité et actualité

La source la plus récente ne remplace pas automatiquement les sources antérieures.
Une publication historique reste nécessaire lorsqu'elle définit l'observable, la
méthode ou un changement d'analyse encore actif. L'actualité sert à dater le
résultat ; elle ne suffit pas à expliquer sa production.

## 3. Hiérarchie externe des sources

La hiérarchie est relative au type d'énoncé. Il n'existe pas une source unique
dominant toute la chaîne.

| Rang | Type de source | Fonction recevable | Limite |
|---:|---|---|---|
| `S1` | article de résultat d'une collaboration, version publiée | résultat empirique, données, méthode statistique déclarée | ne remplace pas les documents techniques nécessaires pour reconstruire les corrections |
| `S1p` | prépublication officielle d'une collaboration, résultat accepté ou non encore publié | état empirique provisoire lorsque la version publiée n'existe pas à la coupure | statut provisoire à déclarer ; rechercher ensuite la version de référence |
| `S2` | produit officiel de données, vraisemblance, chaînes, note technique ou article de méthode de la collaboration | reproductibilité, modèle de réponse, covariances, sélections et paramètres de nuisance | ne porte pas seul un verdict physique global |
| `S3` | ajustement global ou analyse coordonnée de plusieurs expériences | combinaison, corrélations inter-expériences et comparaison des paramètres | ne remplace pas les sources primaires pour les détecteurs, données et systématiques propres |
| `S4` | analyse indépendante spécialisée, calcul théorique ou étude de sensibilité aux modèles | tester robustesse, dépendance de modèle, éléments de matrice ou conventions | doit être distinguée du résultat produit par la collaboration |
| `S5` | revue de référence, Particle Data Group, manuel ou article pédagogique spécialisé | définitions, repérage du champ et généalogie | source d'orientation, non preuve suffisante d'un état empirique récent |
| `S6` | communiqué, page de nouvelles, conférence, diapositive ou média | découvrir une publication ou dater une annonce | ne soutient pas seul une valeur, une préférence ou une exclusion |

### 3.1 Règles d'autorité par type d'énoncé

- Un énoncé sur l'exposition, la sélection, le bruit de fond ou la réponse du
  détecteur doit remonter aux sources `S1` ou `S2` de la collaboration.
- Un énoncé sur une combinaison mondiale des paramètres d'oscillation peut être
  appuyé par une source `S3`, mais les tensions ou dépendances importantes doivent
  être rapportées aux expériences ou jeux de données concernés.
- Une borne cosmologique doit être accompagnée du modèle cosmologique, des jeux de
  données, des priors et de la convention statistique ; l'étiquette « la plus
  forte » n'est pas un résultat transportable entre modèles.
- En double bêta sans neutrino, la limite expérimentale primaire porte sur la
  demi-vie. La conversion en masse effective exige des sources `S4` sur les
  éléments de matrice nucléaire et le mécanisme retenu.
- Une revue ou un communiqué ne peut jamais réparer l'absence d'une source
  primaire identifiable.

### 3.2 Contradictions

En cas de désaccord, la fiche ne choisit pas automatiquement la source la plus
récente ou la valeur la plus précise. Elle localise le désaccord dans :

```text
données ;
sélection ;
calibration ;
modèle de réponse ;
paramétrisation ;
prior ;
traitement des corrélations ;
construction statistique ;
modèle physique ou cosmologique ;
conversion théorique.
```

Un désaccord non résolu est conservé comme résultat du dossier s'il change la
portée de l'inférence.

## 4. Paquet minimal de preuves par fiche

Chaque fiche doit réunir un paquet minimal, adapté à sa voie :

1. une source de définition ou de formalisme pour la fonction du spectre ciblée ;
2. au moins une source primaire donnant l'état empirique retenu à la coupure ;
3. une source de méthode, de réponse, de vraisemblance ou de systématiques lorsque
   ces éléments ne sont pas suffisamment exposés dans l'article principal ;
4. le produit de données, les profils, chaînes ou tables publiques lorsqu'ils sont
   disponibles et décisifs ;
5. une source de coordination ou de synthèse pour situer le résultat parmi les
   autres expériences ;
6. une analyse alternative lorsque la dépendance à un modèle, un prior, un
   élément de matrice ou une convention modifie substantiellement la conclusion.

L'absence d'un élément doit être déclarée. Elle ne peut pas être masquée par une
bibliographie plus longue.

### 4.1 Oscillations

Le paquet doit articuler :

```text
résultats des expériences ou analyses conjointes
+ ajustement global identifié et versionné
+ traitement des effets de matière
+ conventions d'ordre et de Delta m^2
+ corrélations et dégénérescences
+ distinction entre données incluses et profils externes importés.
```

L'ajustement global coordonne les expériences ; il n'est pas considéré comme un
instrument unique ayant directement produit toutes les traces.

### 4.2 Cinématique bêta

Le paquet doit articuler :

```text
spectre terminal et observable instrumentale
+ modèle de réponse
+ corrections et arrière-plans
+ paramètres de nuisance
+ construction de l'estimateur ou de la limite
+ profils de vraisemblance ou données publiques si disponibles.
```

Le caractère local ou cinématique de l'accès ne dispense pas de reconstruire le
modèle de mesure.

### 4.3 Cosmologie

Le paquet doit articuler :

```text
produits de données des sondes
+ vraisemblances ou chaînes utilisées
+ modèle cosmologique de base
+ extensions testées
+ priors, frontière physique et paramétrisation des masses
+ dégénérescences avec les autres paramètres
+ analyse de sensibilité au choix des données et du modèle.
```

Une borne obtenue sous `LambdaCDM` et une borne obtenue avec énergie noire
dynamique ne sont pas deux estimations interchangeables du même énoncé.

### 4.4 Double bêta sans neutrino

Le paquet doit articuler :

```text
isotope et exposition
+ fenêtre de signal, efficacité et bruit de fond
+ demi-vie observée et sensibilité attendue
+ méthode statistique
+ mécanisme de désintégration supposé
+ ensemble explicite d'éléments de matrice nucléaire
+ conversion conditionnelle vers m_beta_beta.
```

Les expériences sur des isotopes différents restent comparables par une chaîne de
conversion déclarée, non par juxtaposition immédiate de leurs demi-vies.

## 5. Gabarit commun des fiches `N1` à `N4`

Chaque fiche reprend les rubriques suivantes. Leur ordre peut être adapté si la
physique l'exige, mais aucune rubrique décisive ne doit disparaître sans
justification.

### 0. Statut, périmètre et coupure

- voie étudiée ;
- question précise ;
- date de coupure bibliographique ;
- période ou coupure des données principales ;
- modèle ou cadre de référence ;
- résultat que la fiche ne prétend pas établir.

### 1. Objet ou fonction ciblée

- objet physique ou processus ;
- fonction du spectre contrainte ;
- définition mathématique ;
- conventions de signes, d'ordre, de saveur, de pivot ou de paramétrisation.

### 2. Production de la trace

- préparation ou population source ;
- interaction pertinente ;
- signal brut ;
- dispositif ou sonde ;
- sélection, efficacité et enregistrement.

### 3. Observable publiée

- donnée brute, donnée corrigée, spectre, taux, corrélation ou résumé statistique ;
- différence entre l'indication instrumentale et l'objet publié ;
- éventuel dépliement, compression ou combinaison.

### 4. Modèle de mesure ou de passage

- équation ou simulation reliant l'observable au paramètre ;
- réponse instrumentale ou modèle direct ;
- hypothèses physiques ;
- paramètres tenus fixes ou ajustés conjointement ;
- niveau auquel intervient la théorie.

### 5. Incertitudes, corrélations et dégénérescences

- incertitudes statistiques et systématiques ;
- corrélations internes et externes ;
- paramètres de nuisance ;
- dégénérescences physiques ou paramétriques ;
- dépendances de modèle qui ne se réduisent pas à une barre d'erreur.

### 6. Construction statistique

- estimateur, vraisemblance ou posterior ;
- intervalle de confiance ou intervalle crédible ;
- niveau annoncé ;
- frontière physique et traitement des valeurs non physiques ;
- résultat observé, résultat attendu et sensibilité distingués.

### 7. État empirique daté

La fiche présente une table minimale :

| Énoncé | Données ou exposition | Modèle et hypothèses | Statut statistique | Date des données | Source |
|---|---|---|---|---|---|

La table n'est remplie qu'après reconstruction des sections précédentes.

### 8. Résultat effectivement établi

Séparer explicitement :

```text
ce qui est détecté ou estimé ;
ce qui est seulement borné ou exclu ;
ce qui est préféré sous un modèle ;
ce qui demeure non identifiable par cette voie ;
ce qui dépend d'une conversion supplémentaire.
```

### 9. Limites propres de l'accès

- information structurellement absente ;
- limite de sensibilité actuelle ;
- dépendance à une hypothèse ;
- ambiguïté statistique ;
- dépendance à une autre discipline ou à un autre calcul.

### 10. Ponts vers les trois autres voies

Pour chaque pont :

```text
quantité de départ ;
relations physiques utilisées ;
hypothèses ajoutées ;
incertitudes propagées ;
information gagnée ;
information qui reste absente.
```

Un pont conditionnel n'est jamais présenté comme une mesure commune déjà donnée.

### 11. Audit des sources et dettes restantes

- sources primaires mobilisées ;
- source évolutive et version ;
- données ou likelihood publiques disponibles ;
- désaccords conservés ;
- documents décisifs non accessibles ;
- vérifications à reporter à `N5`.

## 6. Vocabulaire contrôlé des résultats

| Terme | Usage dans les fiches |
|---|---|
| détection | signal distingué de l'hypothèse nulle selon un critère déclaré |
| estimation | valeur ou distribution attribuée à un paramètre sous un modèle déclaré |
| borne supérieure ou inférieure | limite sur un domaine admissible, sans valeur positive détectée par définition |
| exclusion | région ou hypothèse rejetée selon une construction statistique déclarée |
| préférence | différence relative entre modèles, ordres ou régions ; ne vaut pas détection sans seuil et test appropriés |
| sensibilité attendue | performance médiane ou projetée en l'absence de signal ; distincte du résultat observé |
| posterior | distribution conditionnelle aux données, au modèle et aux priors ; non synonyme de fréquence physique |
| tension | incompatibilité quantitative entre inférences déclarées ; non objet physique autonome |
| projection | fonction déterminée du spectre sous une opération d'accès ; ne signifie pas irréalité de l'objet |

Règles obligatoires :

1. ne pas transformer une borne en mesure positive ;
2. ne pas confondre limite observée et sensibilité attendue ;
3. ne pas fusionner intervalle fréquentiste et intervalle bayésien ;
4. ne pas comparer directement des niveaux de confiance différents sans
   information permettant la conversion ;
5. qualifier tout emploi de « direct », « modèle-indépendant » ou « robuste » par
   rapport aux hypothèses effectivement évitées ;
6. ne pas appeler « masse du neutrino » une fonction effective sans la nommer.

## 7. Fonctions du spectre et conversions interdites

Les quatre voies partagent les masses propres `m_i`, mais elles n'en construisent
pas la même fonction :

```text
oscillations : Delta m^2_ij = m_i^2 - m_j^2, angles et phases de mélange ;
cinématique :  m_beta^2 = somme_i |U_ei|^2 m_i^2 ;
cosmologie :   Sigma m_nu = somme_i m_i ;
double bêta :  m_beta_beta = |somme_i U_ei^2 m_i| sous mécanisme standard.
```

| Voie | Résultat primaire de l'accès | Conversion interdite sans hypothèses supplémentaires |
|---|---|---|
| oscillations | écarts de masses au carré, mélange et motifs de transition | déduire les masses absolues ou la nature Majorana |
| cinématique bêta | contrainte sur `m_beta` par le spectre terminal | attribuer séparément `m_1`, `m_2`, `m_3` |
| cosmologie | contrainte sur `Sigma m_nu` ou une paramétrisation équivalente sous modèle | la présenter comme mesure locale ou indépendante du modèle cosmologique |
| double bêta sans neutrino | limite ou signal sur une demi-vie pour un isotope | convertir en `m_beta_beta`, puis en masses absolues, sans mécanisme, phases et matrices nucléaires |

Les conversions deviennent recevables lorsqu'elles déclarent au minimum l'ordre
des masses, le paramètre d'ancrage, les éléments de la matrice de
Pontecorvo–Maki–Nakagawa–Sakata (PMNS), les phases pertinentes, le modèle
cosmologique ou le mécanisme de double bêta nécessaires. Leur résultat reste
conditionnel à ces entrées.

## 8. Corpus d'amorçage à la coupure

Cette liste sert à lancer les recherches. Elle n'est ni exhaustive ni déjà
validée comme corpus final des quatre fiches.

### 8.1 Oscillations

- [NuFIT 6.1 — ajustement à trois neutrinos fondé sur les données disponibles en
  novembre 2025](https://www.nu-fit.org/?q=node%2F309), source évolutive `S3` à
  citer avec sa version et sa date de consultation ;
- [NuFIT 6.0 — article méthodologique et analyse globale publiée](https://doi.org/10.1007/JHEP12(2024)216),
  source `S3` de méthode et de comparaison ;
- [analyse conjointe T2K–NOvA](https://doi.org/10.1038/s41586-025-09599-3),
  source primaire combinée `S1` pour une partie du secteur longue base.

`N1` devra remonter des paramètres combinés aux expériences solaires, réacteur,
accélérateur et atmosphériques réellement déterminantes, sans prendre NuFIT pour
la source instrumentale de leurs résultats.

### 8.2 Cinématique bêta

- [KATRIN, mesure directe fondée sur 259 jours de données](https://doi.org/10.1126/science.adq9592),
  source primaire `S1` publiée en avril 2025 ;
- [page officielle des résultats KATRIN](https://www.katrin.kit.edu/1271.php),
  source de repérage et d'accès aux documents de collaboration.

`N2` devra identifier séparément l'article de résultat, le modèle de réponse, les
sources systématiques et les produits de vraisemblance disponibles.

### 8.3 Cosmologie

- [DESI DR2 — contraintes sur la physique des neutrinos](https://arxiv.org/abs/2503.14744),
  résultat de collaboration publié en 2025 ;
- [page officielle des publications DESI DR2](https://data.desi.lbl.gov/doc/papers/dr2/),
  qui relie articles, validations et produits de données ;
- [produits cosmologiques DESI et chaînes publiques](https://data.desi.lbl.gov/doc/papers/),
  sources `S2` pour la reproductibilité et la comparaison des modèles.

`N3` ne prendra aucune borne unique comme état du secteur. Il reconstruira les
jeux de données, le modèle, les priors, la frontière des masses et la sensibilité
aux extensions avant toute comparaison.

### 8.4 Double bêta sans neutrino

- [LEGEND-200 — premiers résultats publiés](https://doi.org/10.1103/25tk-nctn),
  source primaire `S1` publiée en janvier 2026 ;
- [page officielle LEGEND](https://legend-exp.org/), source de repérage des
  résultats et documents de collaboration.

`N4` devra compléter ce point d'entrée par les expériences pertinentes sur
d'autres isotopes, les méthodes statistiques et plusieurs calculs d'éléments de
matrice nucléaire. La meilleure limite de demi-vie sur un isotope ne vaut pas à
elle seule meilleure contrainte universelle sur `m_beta_beta`.

## 9. Procédure d'exécution d'une fiche

Chaque étape `N1` à `N4` suit le même cycle de travail :

```text
1. borner la question et geler un corpus initial ;
2. construire la table de provenance et de datation ;
3. reconstruire la chaîne de la trace au résultat ;
4. extraire les hypothèses, nuisances, corrélations et conventions ;
5. formuler séparément acquis, borne, préférence et limite ;
6. rechercher les analyses qui changent la portée du résultat ;
7. contrôler les ponts vers les trois autres voies ;
8. clore la fiche avec ses dettes résiduelles explicites.
```

Les noms de fichiers prévus sont :

```text
N1_Fiche_acces_oscillations_neutrinos_v0_1.md
N2_Fiche_acces_cinematique_beta_neutrinos_v0_1.md
N3_Fiche_acces_cosmologie_somme_masses_neutrinos_v0_1.md
N4_Fiche_acces_double_beta_sans_neutrino_v0_1.md
N5_Matrice_comparative_quatre_acces_neutrinos_v0_1.md
```

La révision de la synthèse générale du cycle intervient après la matrice `N5`, non
après chaque fiche isolée.

## 10. Contrôles de clôture

Une fiche n'est pas close si l'une des conditions suivantes subsiste :

- aucune source primaire ne soutient le résultat empirique principal ;
- la coupure des données est confondue avec la date de publication ;
- l'observable publiée et la fonction du spectre inférée restent indifférenciées ;
- le modèle de mesure, le modèle cosmologique ou le mécanisme supposé est implicite ;
- le niveau statistique, la frontière physique ou la nature de l'intervalle est
  absent ;
- une limite attendue est présentée comme limite observée ;
- une conversion entre voies est formulée sans ses hypothèses ;
- une source de communication remplace un article ou un produit officiel ;
- un désaccord qui modifie la conclusion est lissé dans une moyenne narrative ;
- le gabarit produit des rubriques formelles sans contenu physique identifiable.

La fiche peut être close avec une dette ou une contradiction ouverte si celle-ci
est précisément localisée et si sa résolution dépasse le lot borné.

## 11. Verdict `N0`

```text
date de coupure : 17 juillet 2026 inclus ;
unité de comparaison : énoncé empirique + chaîne d'accès + modèle + statut
                        statistique ;
hiérarchie des sources : relative au type d'énoncé, avec priorité aux résultats,
                         méthodes et produits primaires ;
gabarit : commun sur onze rubriques, révisable si une différence physique est
          effacée ;
ponts : conditionnels et accompagnés de leurs hypothèses ;
prochaine étape : N1 — fiche d'accès par oscillations.
```

`N0` fixe la discipline commune. Il ne fournit encore aucun verdict actualisé sur
les paramètres d'oscillation, l'échelle absolue, l'ordre des masses, la nature du
neutrino ou la compatibilité des quatre voies.