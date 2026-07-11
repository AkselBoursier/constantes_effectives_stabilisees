# Architecture metrologique SI - notes d'integration

## Statut apres l'extension k_B / N_A / R / c / h / e

### 1. Fonction de la note

Cette note integre le resultat de l'extension metrologique SI dans le niveau des architectures inter-familles.

Elle ne remplace pas la fiche c / h / e. Elle en extrait la consequence taxonomique principale :

```text
Architecture metrologique SI = architecture inter-familles confirmee et etendue
```

et non :

```text
nouvelle famille superieure
```

La note sert de reference courte pour les cartes consolidees ulterieures.

Complement de reprise positive :

```text
04_ARCHITECTURES_INTER_FAMILLES/Cercle2_lot2B_Metrologique_SI_v0_1.md
```

La presente note reste la consolidation locale.

Le lot 2B fixe la formulation positive a privilegier pour les reprises
ulterieures.

### 2. Decision centrale

L'architecture metrologique SI est confirmee comme architecture robuste.

Elle articule principalement :

```text
Convention
Composition exacte
Relation qualifiee lorsque le role physique l'exige
Echelle
Realisation pratique
Role physique conserve
```

La decision de rang est :

```text
metrologique SI = architecture de definition et de realisation
```

et non :

```text
metrologique SI = famille fonctionnelle autonome
```

Cette decision evite de creer une famille trop large qui absorberait toutes les constantes exactes, les relations de conversion, les choix d'unites et les grandeurs physiquement structurantes.

### 3. Definition locale proposee

Une architecture metrologique SI est une configuration inter-familles dans laquelle des constantes definissantes et des compositions exactes rendent operatoire un systeme coherent d'unites, sans epuiser le role physique des grandeurs qui y sont fixees.

Cette definition repose sur cinq elements.

```text
1. Constantes definissantes primaires
2. Compositions exactes
3. Definitions d'unites
4. Realisations pratiques
5. Roles physiques conserves
```

Le point important est le cinquieme. L'exactitude numerique dans le SI ne transforme pas une grandeur physique en simple convention.

### 4. Corpus stabilise

Le corpus stabilise comprend deux niveaux.

Premier niveau : constantes definissantes ou deja stabilisees comme definissantes dans l'architecture SI.

| Grandeur | Statut SI | Fonction locale | Role physique conserve |
|---|---|---|---|
| k_B | Constante definissante primaire | Convention | Relation energie / temperature |
| N_A | Constante definissante primaire | Convention | Comptage moleculaire / quantite de matiere |
| c | Constante definissante primaire | Convention | Relation espace-temps / echelle causale |
| h | Constante definissante primaire | Convention | Quantum d'action / relation quantique |
| e | Constante definissante primaire | Convention | Quantum de charge / entree du couplage electromagnetique |

Second niveau : constantes exactes par composition.

| Grandeur | Structure | Statut |
|---|---|---|
| R | N_A k_B | Composition exacte |
| K_J | 2 e / h | Composition exacte |
| R_K | h / e^2 | Composition exacte |

Ces grandeurs ne sont pas toutes du meme type. C'est precisement pourquoi le niveau architectural est necessaire.

### 5. Deux formes internes de l'architecture SI

La note distingue deux formes internes.

#### 5.1 Constantes definissantes primaires

Cas :

```text
k_B
N_A
c
h
e
```

Structure :

```text
valeur numerique fixee
+ unite correspondante
+ realisation pratique
+ role physique conserve
```

Lecture taxonomique :

```text
famille principale : Convention
sous-type : constante definissante primaire
```

Decision :

```text
Convention est la famille principale dans l'architecture SI, mais elle ne suffit pas a decrire tout le role physique.
```

#### 5.2 Compositions exactes

Cas :

```text
R = N_A k_B
K_J = 2 e / h
R_K = h / e^2
```

Structure :

```text
constantes definissantes exactes
-> composition mathematique
-> grandeur exacte par composition dans le SI
```

Lecture taxonomique :

```text
rang 0 : composition exacte
famille principale : non forcee par defaut dans Relation
architecture : Metrologique SI
```

Decision :

```text
une constante exacte par composition n'est pas une constante definissante primaire.
```

Elle herite son exactitude du systeme de definition.

### 6. Statuts locaux

#### 6.1 k_B

Statut :

```text
constante definissante primaire du kelvin
```

Lecture physique :

```text
relation energie / temperature
```

Classement :

```text
Convention + role relationnel thermodynamique
```

#### 6.2 N_A

Statut :

```text
constante definissante primaire de la mole
```

Lecture physique :

```text
relation entre comptage microscopique et quantite de matiere
```

Classement :

```text
Convention + relation de comptage
```

#### 6.3 R

Statut :

```text
constante exacte par composition
```

Structure :

```text
R = N_A k_B
```

Classement :

```text
Composition exacte dans l'architecture SI
```

R n'est pas une constante definissante primaire. Son exactitude vient de la composition de deux constantes definissantes.

#### 6.4 c

Statut :

```text
constante definissante primaire du SI
```

Lecture physique :

```text
relation espace-temps / echelle causale
```

Classement :

```text
Convention dans l'architecture SI
Relation qualifiee / Echelle dans son role physique relativiste
```

Decision :

```text
c n'est pas seulement une convention.
```

#### 6.5 h

Statut :

```text
constante definissante primaire du SI
```

Lecture physique :

```text
quantum d'action
relation energie-frequence
```

Classement :

```text
Convention dans l'architecture SI
Echelle d'action + relation quantique qualifiee dans son role physique
```

Decision :

```text
h est exacte dans le SI, mais son exactitude ne donne pas une interpretation physique unique de la quantification.
```

#### 6.6 e

Statut :

```text
constante definissante primaire du SI
```

Lecture physique :

```text
quantum de charge electrique
```

Classement :

```text
Convention dans l'architecture SI
Echelle de charge + entree du couplage electromagnetique
```

Decision :

```text
e ne doit pas etre confondu avec alpha.
```

La bonne distinction est :

```text
e : charge dimensionnee exacte dans le SI
alpha : couplage electromagnetique sans dimension determine experimentalement
```

### 7. Exactitude, realisation et contenu physique

La note confirme une regle centrale :

```text
Exactitude conventionnelle n'est pas precision empirique.
```

Dans le SI, les valeurs numeriques de certaines constantes sont exactes parce qu'elles definissent les unites.

Cela ne signifie pas :

```text
realisation pratique sans incertitude
mesure physique parfaite
explication theorique complete
reduction de la grandeur a une convention
```

Regle stabilisee :

```text
Toujours distinguer valeur definissante, realisation pratique et contenu physique.
```

Exemples :

```text
c exact dans le SI ne supprime pas le role physique de la structure relativiste.
h exact dans le SI ne resout pas l'interpretation de la quantification.
e exact dans le SI ne fixe pas alpha.
R exact par composition n'est pas une constante definissante primaire.
```

### 8. Regime physique et regime d'acces

| Grandeur | Regime physique | Regime d'acces |
|---|---|---|
| k_B | Thermodynamique, physique statistique | Definition du kelvin, realisations thermometriques |
| N_A | Comptage, quantite de matiere | Definition de la mole, realisations chimiques et atomiques |
| R | Thermodynamique macroscopique | Composition exacte N_A k_B |
| c | Relativite, propagation dans le vide, causalite | Realisations longueur-temps |
| h | Physique quantique, action, spectroscopie | Realisations du kilogramme, balances de Kibble |
| e | Charge elementaire, electromagnetisme | Definition de l'ampere, comptage de charge |
| K_J | Metrologie electrique quantique | Effet Josephson |
| R_K | Metrologie electrique quantique | Effet Hall quantique |

Decision :

```text
Le regime d'acces SI ne remplace pas le regime physique.
```

Il rend le regime physique operatoire dans un systeme de mesure.

### 9. Distinction entre famille et architecture

La note confirme la regle generale :

```text
Une famille classe la fonction principale d'une grandeur.
Une architecture decrit l'articulation de plusieurs familles dans un regime.
```

Ainsi :

```text
k_B appartient a Convention dans l'architecture SI.
N_A appartient a Convention dans l'architecture SI.
c appartient a Convention dans l'architecture SI.
h appartient a Convention dans l'architecture SI.
e appartient a Convention dans l'architecture SI.
R releve d'abord du rang 0 comme composition exacte.
K_J releve d'abord du rang 0 comme composition exacte.
R_K releve d'abord du rang 0 comme composition exacte.
```

Mais ensemble, ces grandeurs appartiennent a :

```text
Architecture metrologique SI
```

Il ne faut donc pas ecrire :

```text
famille metrologique
famille definition
famille conversion
```

sauf comme formules provisoires a corriger.

### 10. Formule compacte de l'architecture

Formule courte :

```text
Architecture metrologique SI =
Convention
+ Composition exacte
+ Echelle physique conservee
+ Realisation pratique
+ Systeme coherent d'unites
```

Forme developpee :

```text
Architecture metrologique SI =
{k_B, N_A, c, h, e}
+ {R, K_J, R_K}
+ {Convention, Composition exacte, Echelle, relation qualifiee}
+ {definitions d'unites, realisations pratiques}
+ {roles physiques conserves}
```

Precision :

```text
exactitude SI = exactitude de definition, non epuisement physique.
```

### 11. Limites de l'architecture

Cette architecture ne doit pas tout absorber.

Elle ne classe pas automatiquement :

```text
toute constante dimensionnee
toute constante exacte par choix d'unites naturelles
toute grandeur servant de conversion
toute relation mathematique entre constantes
```

Une grandeur appartient a cette architecture seulement si son role concerne explicitement :

```text
une definition d'unite SI
une relation exacte heritee de constantes definissantes
une realisation pratique du systeme d'unites
une articulation entre convention et role physique
```

La note ne resout pas :

```text
la philosophie complete de la mesure
l'origine physique de c, h ou e
l'interpretation de la quantification
la dynamique du couplage electromagnetique
```

Elle fixe seulement le statut methodologique de l'architecture.

### 12. Points reportes dans les cartes consolidees

Les cartes consolidees ulterieures doivent conserver six decisions.

```text
1. Architecture metrologique SI est confirmee et etendue.
2. Metrologique SI ne doit pas devenir une famille superieure.
3. Convention reste la famille principale des constantes definissantes.
4. Les constantes exactes par composition relevent d'abord du rang 0 ; Relation n'est pas la case par defaut.
5. Exactitude SI n'est pas precision empirique.
6. Une constante definissante peut garder un role physique fort.
```

Elles doivent aussi conserver l'extension du corpus SI :

```text
c
h
e
K_J
R_K
```

en plus de :

```text
k_B
N_A
R
```

### 13. Formule de travail

Formule longue :

> L'architecture metrologique SI stabilise des constantes en fixant leurs valeurs numeriques dans un systeme coherent d'unites, mais elle conserve la distinction entre definition, realisation pratique, relation compositionnelle et role physique.

Formule courte :

> Une constante definissante peut etre exacte dans le SI sans etre seulement conventionnelle en physique. La convention y est libre en sa forme et dictee en son contenu : on ne conventionne que ce qui n'a plus de latitude (note de correction modale v0.1).

### 14. Suite recommandee

Suite produite ensuite :

```text
05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_1.md
```

Prolongement de refonte produit ensuite :

```text
05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_2_refonte.md
```

Objectif :

```text
mettre a jour la carte de reference avec l'architecture metrologique SI etendue,
puis l'integrer dans la refonte par rangs, roles et dependances.
```

### 15. Documents sources internes

Documents internes a relier a cette note :

```text
PROJECT_BRIEF.docx
01_CADRE_METHODOLOGIQUE/Note_synthese_methodologique_v1_1.md
05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_0.md
05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_2_refonte.md
02_CYCLES_PHYSIQUES/08_Cycle_metrologique_SI/Cycle_metrologique_SI_v0_1_c_h_e.md
02_CYCLES_PHYSIQUES/06_Cycle_effectif_basse_energie/Cycle_effectif_basse_energie_v0_4_alphaG_MPl.md
02_CYCLES_PHYSIQUES/06_Cycle_effectif_basse_energie/Synthese_cycle_effectif_basse_energie_v0_1.md
```

Les source