# Carte consolidee v1.1

## Carte de reference apres integration de l'architecture metrologique SI etendue

### 1. Fonction de la v1.1

La carte v1.1 consolide l'etat du projet apres l'integration de l'architecture metrologique SI etendue.

Elle remplace la carte v1.0 comme carte de reference.

La modification principale est :

```text
Architecture metrologique SI : confirmee et etendue.
```

Le corpus SI integre maintenant :

```text
k_B
N_A
R
c
h
e
K_J
R_K
```

La v1.1 ne modifie pas le nombre de familles superieures. Elle renforce plutot une distinction deja centrale :

```text
exactitude conventionnelle
realisation pratique
role physique
relation compositionnelle
```

### 2. Definition consolidee

Definition de reference :

> Une constante effective stabilisee n'est pas seulement une valeur stable ; c'est une fonction robuste dans un regime, connue par un acces determine, stabilisee selon un mode precis, et parfois inscrite dans une architecture plus vaste.

La v1.1 ajoute une precision pour les constantes definissantes :

```text
une valeur exacte dans le SI n'epuise pas le role physique de la grandeur.
```

Une grandeur doit donc etre analysee selon :

```text
1. sa fonction principale ;
2. son regime physique ;
3. son regime d'acces ;
4. son mode de stabilisation ;
5. son appartenance eventuelle a une architecture ;
6. ses limites d'interpretation.
```

Formule courte :

> Une constante physique est moins un nombre isole qu'un point de stabilite dans une architecture de regimes, d'acces et de fonctions.

### 3. Table de rang v1.1

La carte v1.1 retient quatre niveaux principaux.

| Rang | Categories |
|---|---|
| Familles superieures | Couplage, Echelle, Relation, Raccordement, Orientation, Convention |
| Fonctions transversales | Seuil, Borne, Validite, Dephasage, Hierarchie |
| Fonctions architecturales | Fond, Parametre d'etat, Densite normalisee, Relation d'etat, Condition initiale, Observable reconstruite |
| Architectures inter-familles | Saveur-Higgs, Metrologique SI, Effective basse energie, Cosmologique |

Regle centrale :

```text
Une categorie peut etre indispensable sans etre une famille superieure.
```

Corrections de rang stabilisees :

```text
Seuil n'est pas une famille.
Fond n'est pas une famille.
Effectif n'est pas une famille.
Cosmologie n'est pas une famille.
Metrologique SI n'est pas une famille.
Tension de donnees n'est pas une famille.
```

### 4. Noyau des six familles superieures

Les familles superieures repondent a la question :

```text
que fait principalement cette grandeur ?
```

| Famille | Fonction principale | Exemples stabilises |
|---|---|---|
| Couplage | Parametrer une intensite d'interaction ou de liaison | alpha, alpha_s(Q^2), alpha_G(E), y_f |
| Echelle | Fixer ou reveler un ordre de grandeur structurant | v, M_W, Lambda_QCD, M_Pl, h comme echelle d'action hors SI |
| Relation | Stabiliser une liaison entre grandeurs, regimes ou composantes | m_p / m_e, Delta m^2, Omega_i, w, R, K_J, R_K |
| Raccordement | Relier deux descriptions ou niveaux theoriques | G_F |
| Orientation | Stabiliser un desalignement entre bases, champs ou secteurs | theta_W, CKM, PMNS, delta_CP |
| Convention | Recevoir une valeur exacte par definition dans un systeme d'unites | k_B, N_A, c, h, e |

Ces familles restent le noyau taxonomique.

Elles ne suffisent pas toujours a decrire le role complet d'une grandeur. Les fonctions transversales, architecturales et les architectures inter-familles sont alors ajoutees sans creer de nouvelle famille.

### 5. Famille Couplage

Une constante de couplage parametre une intensite d'interaction ou de liaison entre champs, particules ou secteurs.

Sous-types stabilises :

```text
couplage de regime
couplage courant
couplage de texture
couplage effectif construit par rapport a une echelle
```

Exemples :

```text
alpha        : couplage electromagnetique sans dimension
alpha_s(Q^2): couplage courant de QCD
y_f          : couplage de Yukawa / couplage de texture
alpha_G(E)  : couplage gravitationnel effectif construit a partir de E / M_Pl
```

Regle :

```text
Un couplage dimensionne doit etre lu par ses effets, ses rapports ou sa reformulation sans dimension.
```

Point SI :

```text
e n'est pas directement alpha.
```

e est une charge dimensionnee exacte dans le SI ; alpha reste le couplage electromagnetique sans dimension.

### 6. Famille Echelle

Une constante d'echelle fixe, revele ou hierarchise un ordre de grandeur structurant pour un regime physique.

Sous-types stabilises :

```text
echelle structurante
echelle electrofaible de jauge
echelle dynamique
echelle de validite attendue
echelle derivee
echelle d'action
echelle de charge
```

Exemples :

```text
v          : echelle structurante du regime electrofaible brise
M_W        : echelle electrofaible de jauge, a fonction de validite pour la theorie de Fermi
Lambda_QCD : echelle dynamique du changement de regime QCD
M_Pl       : echelle de validite attendue de la gravitation effective basse energie
h          : echelle d'action dans le regime quantique, mais Convention dans l'architecture SI
e          : echelle de charge, mais Convention dans l'architecture SI
```

Regle :

```text
Une echelle peut jouer une fonction seuil, validite ou hierarchie sans que ces fonctions deviennent des familles.
```

### 7. Famille Relation

Une constante relationnelle stabilise une liaison entre grandeurs, regimes, niveaux, spectres ou composantes.

La famille Relation est conservee, mais sous contrainte stricte.

Regle :

```text
Ne jamais ecrire seulement "famille Relation".
Toujours preciser relation de quoi, entre quoi, dans quel regime, selon quel acces.
```

Sous-types stabilises :

```text
relation stratifiee
relation compositionnelle
relation compositionnelle exacte
relation spectrale
relation constitutive de regime
relation normalisee
relation d'etat
relation espace-temps
relation quantique
```

Exemples :

```text
m_p / m_e             : relation stratifiee
R = N_A k_B           : relation compositionnelle exacte
K_J = 2 e / h         : relation compositionnelle exacte
R_K = h / e^2         : relation compositionnelle exacte
Delta m^2             : relation spectrale
m_f = y_f v / sqrt(2) : relation constitutive de regime
Omega_i               : relation normalisee
w = p / rho           : relation d'etat
```

### 8. Famille Raccordement

Une constante de raccordement relie une description effective a une description plus complete, ou deux niveaux theoriques distincts.

Exemple central :

```text
G_F
```

Sous-types stabilises :

```text
raccordement effectif basse energie
raccordement local
raccordement architectural
raccordement attendu
```

Precision :

```text
Raccordement reste une famille lorsqu'une grandeur porte principalement cette fonction.
Raccordement peut devenir architectural lorsqu'aucune grandeur unique ne porte tout le passage.
```

### 9. Famille Orientation

Une constante d'orientation stabilise un desalignement entre bases, champs, etats ou secteurs d'interaction.

Sous-types stabilises :

```text
orientation de jauge
orientation de saveur transitionnelle
orientation de saveur oscillatoire
orientation complexe CP
coordonnees hierarchiques d'orientation
```

Regle :

```text
Delta m^2 ne doit pas etre classe comme orientation : il dephase.
Wolfenstein ne cree pas une famille : il coordonne localement une orientation.
```

### 10. Famille Convention

Une constante conventionnelle recoit une valeur exacte par definition dans un systeme d'unites, ou devient exacte par composition de constantes definissantes.

Sous-types :

```text
constante definissante primaire
constante exacte par composition
```

Exemples :

```text
k_B : constante definissante primaire du kelvin
N_A : constante definissante primaire de la mole
c   : constante definissante primaire du SI
h   : constante definissante primaire du SI
e   : constante definissante primaire du SI
R   : constante exacte par composition
K_J : constante exacte par composition
R_K : constante exacte par composition
```

Regle :

```text
Exactitude conventionnelle n'est pas precision empirique.
```

Une valeur peut etre exacte dans le SI sans que son role physique soit epuise par la convention.

### 11. Fonctions transversales

Une fonction transversale n'est pas une famille superieure.

Elle designe un role secondaire, lateral ou recurrent qu'une grandeur peut jouer en plus de sa fonction principale.

Fonctions stabilisees :

```text
Seuil
Borne
Validite
Dephasage
Hierarchie
```

| Fonction | Question | Exemples |
|---|---|---|
| Seuil | Ou se situe une limite, un passage ou un ancrage ? | M_W, Lambda_QCD, M_Pl |
| Borne | La grandeur est-elle connue par limite plutot que par mesure positive ? | masse absolue neutrino, contraintes cosmologiques |
| Validite | Quelle description vaut dans quel domaine ? | theorie de Fermi, QCD perturbative, gravitation effective |
| Dephasage | Quelle relation se manifeste comme phase dynamique ? | Delta m^2 |
| Hierarchie | Quel ecart d'echelle, masse ou melange est organise ? | Wolfenstein, E << M_W, E << M_Pl |

Regle :

```text
La fonction transversale ne remplace jamais la famille principale.
```

### 12. Fonctions architecturales

Une fonction architecturale prend sens dans une configuration globale.

Elle ne forme pas une famille superieure.

Fonctions stabilisees :

```text
Fond
Parametre d'etat
Densite normalisee
Relation d'etat
Condition initiale
Observable reconstruite
```

| Fonction architecturale | Cas principal | Decision |
|---|---|---|
| Fond | Lambda | Terme de fond, non famille |
| Parametre d'etat | H_0 | Valeur actuelle du taux d'expansion, non constante fondamentale |
| Densite normalisee | Omega_i | Relation normalisee a une densite critique |
| Relation d'etat | w | Lien pression / densite, non identification directe a Lambda |
| Condition initiale | A_s, n_s | Parametres primordiaux du spectre perturbatif |
| Observable reconstruite | sigma_8, S_8 | Grandeurs reconstruites par donnees, modele et corrections |

Regle :

```text
Une fonction architecturale devient lisible dans une architecture ; elle ne cree pas par elle-meme une famille superieure.
```

### 13. Architectures inter-familles

Une architecture inter-familles articule plusieurs familles et fonctions dans un secteur, un regime ou un systeme de description.

Une famille repond a :

```text
que fait principalement cette grandeur ?
```

Une architecture repond a :

```text
comment plusieurs fonctions deviennent-elles solidaires dans un regime ?
```

Architectures reconnues en v1.1 :

| Architecture | Statut v1.1 | Corpus de reference |
|---|---|---|
| Saveur-Higgs | Confirmee | v, Y_f, m_f, CKM, PMNS, Delta m^2 |
| Metrologique SI | Confirmee et etendue | k_B, N_A, R, c, h, e, K_J, R_K |
| Effective basse energie | Confirmee | G_F, M_W, alpha_s(Q^2), Lambda_QCD, alpha_G(E), M_Pl |
| Cosmologique | Confirmee, mais delicate | Lambda, H_0, Omega_i, w, A_s, n_s, sigma_8, S_8 |

Regle :

```text
Une architecture n'ajoute pas une famille.
Elle montre comment plusieurs familles deviennent solidaires dans un regime de description.
```

### 14. Architecture saveur-Higgs

L'architecture saveur-Higgs articule :

```text
Echelle
+ Couplage
+ Relation
+ Orientation
```

Lecture :

```text
v          : echelle electrofaible
Y_f        : couplages de texture
m_f        : masses stabilisees par relation constitutive de regime
CKM        : orientation de saveur transitionnelle
PMNS       : orientation de saveur oscillatoire
Delta m^2  : relations spectrales dans le secteur neutrino
```

Regle :

```text
Saveur-Higgs n'est pas une famille.
```

### 15. Architecture metrologique SI

Statut v1.1 :

```text
Architecture metrologique SI = architecture inter-familles confirmee et etendue
```

Elle articule :

```text
Convention
+ Relation compositionnelle exacte
+ Echelle physique conservee
+ Realisation pratique
+ Systeme coherent d'unites
```

Corpus stabilise :

```text
k_B
N_A
c
h
e
R
K_J
R_K
```

Matrice locale :

| Grandeur | Statut SI | Fonction locale | Role physique conserve |
|---|---|---|---|
| k_B | Constante definissante primaire | Convention | Relation energie / temperature |
| N_A | Constante definissante primaire | Convention | Comptage moleculaire / quantite de matiere |
| c | Constante definissante primaire | Convention | Relation espace-temps / echelle causale |
| h | Constante definissante primaire | Convention | Quantum d'action / relation quantique |
| e | Constante definissante primaire | Convention | Quantum de charge / entree du couplage electromagnetique |
| R | Relation exacte par composition | Relation | Thermodynamique macroscopique |
| K_J | Relation exacte par composition | Relation | Metrologie electrique quantique |
| R_K | Relation exacte par composition | Relation | Metrologie electrique quantique |

Regles stabilisees :

```text
Metrologique SI ne devient pas une famille.
Convention reste la famille principale des constantes definissantes.
Les constantes exactes par composition appartiennent a Relation.
Exactitude SI n'est pas precision empirique.
Une constante definissante peut garder un role physique fort.
```

Formule :

> Une constante definissante peut etre exacte dans le SI sans etre seulement conventionnelle en physique.

### 16. Architecture effective basse energie

Statut v1.1 :

```text
Architecture effective basse energie = architecture inter-familles confirmee
```

Elle articule :

```text
Raccordement
+ Echelle de validite
+ Couplage de regime
+ Relation, lorsque des liaisons de regime doivent etre explicitees
+ Fonctions Validite / Seuil / Hierarchie
```

Corpus stabilise :

```text
G_F
M_W
alpha_s(Q^2)
Lambda_QCD
alpha_G(E)
M_Pl
```

Trois formes internes d'effectivite :

| Forme | Cas | Structure |
|---|---|---|
| Integration d'un mediateur massif | G_F / M_W | Un degre de liberte lourd n'est pas resolu ; son effet devient coefficient local |
| Flot de couplage et changement de regime | alpha_s(Q^2) / Lambda_QCD | Le couplage varie avec l'echelle ; une echelle dynamique marque le changement de description |
| Couplage dimensionne et suppression d'echelle | alpha_G(E) / M_Pl | Le couplage effectif depend d'un rapport d'echelle ; la basse energie est un domaine de suppression |

Regles stabilisees :

```text
Effectif ne devient pas une famille.
Raccordement peut etre local, distribue ou attendu.
Validite devient une fonction transversale centrale.
Seuil et Hierarchie restent des fonctions transversales.
```

Formule :

> L'effectivite stabilise moins une valeur qu'une validite de description.

### 17. Architecture cosmologique

Statut v1.1 :

```text
Architecture cosmologique = architecture inter-familles confirmee
```

Elle articule :

```text
Fond
+ Parametre d'etat
+ Densite normalisee
+ Relation d'etat
+ Condition initiale
+ Observable reconstruite
+ Regimes d'acces
+ Dependances de modele
+ Tensions de donnees
```

Corpus stabilise :

```text
Lambda
H_0
Omega_i
w
A_s
n_s
sigma_8
S_8
```

Matrice locale :

| Grandeur | Statut stabilise | Fonction architecturale | Risque controle |
|---|---|---|---|
| Lambda | Terme de fond | Fond | Reintroduire Fond comme famille |
| H_0 | Parametre d'etat actuel | Parametre d'etat | Traiter H_0 comme constante fondamentale |
| Omega_i | Relation normalisee | Densite normalisee | Confondre fraction normalisee et densite absolue |
| w | Relation d'etat | Relation d'etat | Confondre parametrisation et explication physique |
| A_s / n_s | Conditions initiales perturbatives | Condition initiale | Ranger les parametres primordiaux dans Fond |
| sigma_8 / S_8 | Observables reconstruites de structure | Observable reconstruite | Transformer une tension d'acces en verdict physique |

Regles stabilisees :

```text
Cosmologie ne devient pas une famille.
Fond reste une fonction architecturale.
Observable reconstruite est une fonction architecturale.
Tension de donnees appartient au regime d'acces.
Toute stabilisation cosmologique doit etre accompagnee de son modele d'inference.
```

Formule :

> En cosmologie, stabiliser une grandeur, c'est stabiliser son role dans un modele et son acces, non isoler une constante absolue.

### 18. Regime physique et regime d'acces

La distinction entre regime physique et regime d'acces est obligatoire.

Un regime de definition physique repond a :

```text
dans quel domaine la grandeur joue-t-elle un role ?
```

Un regime d'acces epistemique repond a :

```text
comment cette grandeur est-elle mesuree, inferee, reconstruite, fixee ou bornee ?
```

Exemples :

| Grandeur | Regime physique | Regime d'acces |
|---|---|---|
| G_F | Interaction faible basse energie | Duree de vie du muon, ajustements electrofaibles |
| alpha_s(Q^2) | QCD selon l'echelle de resolution | Extractions multi-processus, evolution RG |
| M_Pl | Gravitation effective basse energie | Grandeur derivee de G_N, hbar et c |
| c | Relativite, propagation dans le vide, causalite | Realisations longueur-temps du SI |
| h | Physique quantique, action, spectroscopie | Realisations du kilogramme, balances de Kibble |
| e | Charge elementaire, electromagnetisme | Definition de l'ampere, comptage de charge |
| Lambda | Dynamique globale de l'espace-temps | Inference cosmologique combinee |
| H_0 | Taux actuel d'expansion | Distance ladder, CMB + modele, BAO + calibration |
| sigma_8 / S_8 | Croissance tardive des structures | Lensing faible, CMB + modele, amas, 3x2pt |

Regle :

```text
Un accord, un conflit ou une exactitude conventionnelle ne suffit pas a changer la famille d'une grandeur.
```

### 19. Modes de stabilisation

La stabilisation doit etre decrite explicitement.

Types principaux :

```text
empirique forte
empirique partielle
bornee
reconstruite
modele-dependante
conventionnelle definissante
exacte par composition
non concernee conventionnellement
en tension entre regimes d'acces
```

Exemples :

```text
alpha : stabilisation empirique forte
k_B : stabilisation conventionnelle definissante
c : stabilisation conventionnelle definissante, role physique conserve
h : stabilisation conventionnelle definissante, role quantique conserve
e : stabilisation conventionnelle definissante, alpha non fixe par e seul
R = N_A k_B : exacte par composition
K_J = 2 e / h : exacte par composition
R_K = h / e^2 : exacte par composition
Lambda : forte dans LambdaCDM, interpretation physique ouverte
H_0 : fortement contraint mais discordant entre routes d'acces
sigma_8 / S_8 : reconstruits, modele-dependants et sensibles aux systematiques
```

Regle :

```text
La stabilisation d'une valeur ne resout pas toujours le statut physique profond de la grandeur.
```

### 20. Tensions de donnees

Une tension de donnees n'est pas une famille.

Elle n'est pas non plus une constante nouvelle.

Elle est une propriete du reseau d'acces et d'inference.

Exemples :

```text
tension H_0
tension S_8
preference DESI pour des modeles d'energie noire dynamique
```

Regle :

```text
Tension = propriete d'acces, non categorie taxonomique.
```

### 21. Matrice canonique v1.1

Toute nouvelle fiche doit pouvoir etre ramenee a la matrice suivante.

| Critere | Question |
|---|---|
| Grandeur | De quoi parle-t-on exactement ? |
| Type logique | Valeur, rapport, couplage, echelle, angle, phase, matrice, coefficient, parametre ? |
| Dimension | Dimensionnee ou sans dimension ? |
| Famille principale | Couplage, Echelle, Relation, Raccordement, Orientation ou Convention ? |
| Sous-type local | Quelle qualification precise est necessaire ? |
| Fonction transversale eventuelle | Seuil, borne, validite, dephasage, hierarchie ? |
| Fonction architecturale eventuelle | Fond, parametre d'etat, densite normalisee, relation d'etat, condition initiale, observable reconstruite ? |
| Regime de definition physique | Dans quel domaine la grandeur joue-t-elle un role ? |
| Regime d'acces epistemique | Comment est-elle mesuree, reconstruite, fixee ou bornee ? |
| Dependance d'echelle | Court-elle avec une echelle ou depend-elle d'un schema ? |
| Stabilisation empirique | Forte, partielle, en cours, bornee, modele-dependante, ouverte ? |
| Stabilisation conventionnelle | Definissante, exacte par composition, mesuree dans le systeme, non concernee ? |
| Architecture eventuelle | Saveur-Higgs, SI, effective basse energie, cosmologique ? |
| Tension eventuelle | Tension d'acces, conflit d'inference ou non pertinente ? |
| Limites | Ce que cette grandeur ne dit pas |

### 22. Matrice metrologique SI minimale

Les fiches metrologiques SI doivent ajouter une matrice specialisee.

| Critere | Question metrologique SI |
|---|---|
| Grandeur | k_B, N_A, R, c, h, e, K_J, R_K ? |
| Type logique | Constante definissante primaire, relation exacte par composition, echelle physique, charge, action, vitesse ? |
| Famille principale SI | Convention ou Relation ? |
| Role physique conserve | Quelle fonction physique reste lisible hors de l'exactitude SI ? |
| Unite definie ou relation exacte | Quelle unite ou relation devient operatoire ? |
| Realisation pratique | Par quelle mise en pratique ou quel regime experimental la definition est-elle realisee ? |
| Stabilisation conventionnelle | Definissante, exacte par composition, ou non concernee ? |
| Limite | Ce que l'exactitude SI ne dit pas |

### 23. Matrice cosmologique minimale

Les fiches cosmologiques doivent ajouter une matrice specialisee.

| Critere | Question cosmologique |
|---|---|
| Grandeur | Lambda, H_0, Omega_i, w, A_s, n_s, sigma_8, S_8 ? |
| Type logique | Terme, parametre d'etat, densite normalisee, relation d'etat, condition initiale, observable reconstruite ? |
| Dimension | Dimensionnee ou sans dimension ? |
| Fonction architecturale | Fond, parametre d'etat, densite normalisee, relation d'etat, condition initiale, observable reconstruite ? |
| Famille principale | Relation, Echelle, Couplage, ou aucune famille simple forcee ? |
| Regime physique | Dans quel modele ou domaine cosmologique la grandeur joue-t-elle un role ? |
| Regime d'acces | CMB, BAO, supernovae, lentille faible, distance ladder, ajustement combine ? |
| Dependances de modele | LambdaCDM, wCDM, w0waCDM, courbure, neutrinos, systematiques ? |
| Stabilisation empirique | Forte, modele-dependante, en tension, ouverte ? |
| Tension eventuelle | Tension d'acces ou indice physique possible ? |
| Limite | Ce que la grandeur ne dit pas |

### 24. Protocole de classement

Pour classer une nouvelle grandeur, proceder dans cet ordre.

```text
1. Identifier la grandeur exacte.
2. Dire si elle est dimensionnee ou sans dimension.
3. Determiner sa fonction principale dans le contexte choisi.
4. Chercher si une famille superieure suffit.
5. Sous-typer la famille si elle existe.
6. Ajouter les fonctions transversales sans les confondre avec la famille.
7. Ajouter les fonctions architecturales si la grandeur joue dans une configuration globale.
8. Distinguer regime physique et regime d'acces.
9. Preciser le mode de stabilisation.
10. Identifier les tensions eventuelles comme proprietes d'acces.
11. Dire ce que la grandeur ne dit pas.
```

Regle de priorite :

```text
La fonction principale prime sur les roles secondaires, mais le contexte peut determiner la fonction principale.
```

Exemples :

```text
M_W        : Echelle, meme s'il joue une fonction seuil / validite
Lambda_QCD : Echelle, meme si elle marque un passage de regime
Delta m^2  : Relation spectrale, meme si elle dephase
theta_W    : Orientation, meme si elle depend d'un schema
G_F        : Raccordement, meme s'il implique des relations avec g, M_W et v
c          : Convention dans le SI, Relation / Echelle dans son role relativiste
h          : Convention dans le SI, Echelle d'action dans son role quantique
e          : Convention dans le SI, quantum de charge ; alpha reste le couplage sans dimension
Omega_i    : Relation normalisee + fonction architecturale Densite normalisee
S_8        : Observable reconstruite, non verdict physique unique
```

### 25. Erreurs typiques a eviter

Erreur 1 :

```text
creer une famille des qu'une fonction revient souvent
```

Correction :

```text
tester d'abord si cette fonction est transversale ou architecturale.
```

Erreur 2 :

```text
confondre mesure precise et statut fondamental
```

Correction :

```text
une grandeur peut etre tres precise et rester modele-dependante ou interpretee.
```

Erreur 3 :

```text
confondre architecture et famille
```

Correction :

```text
une architecture articule plusieurs familles ; elle ne remplace pas le noyau taxonomique.
```

Erreur 4 :

```text
classer une tension comme grandeur physique nouvelle
```

Correction :

```text
decrire la tension comme propriete du regime d'acces.
```

Erreur 5 :

```text
forcer toute grandeur cosmologique dans Couplage, Echelle ou Relation
```

Correction :

```text
accepter les fonctions architecturales lorsque la famille principale simple n'est pas pertinente.
```

Erreur 6 :

```text
confondre reconstruction et mesure directe
```

Correction :

```text
specifier les modeles, corrections et routes d'acces qui reconstruisent la grandeur.
```

Erreur 7 :

```text
confondre exactitude SI et precision empirique
```

Correction :

```text
distinguer valeur definissante, realisation pratique et role physique.
```

### 26. Decisions stabilisees par la v1.1

La carte v1.1 stabilise treize decisions.

```text
1. Le noyau reste a six familles superieures.
2. Seuil n'est pas une famille.
3. Fond n'est pas une famille.
4. Relation reste une famille, mais seulement qualifiee.
5. Validite est une fonction transversale centrale.
6. Les architectures inter-familles sont necessaires.
7. L'architecture effective basse energie est confirmee.
8. L'architecture cosmologique est confirmee.
9. L'architecture metrologique SI est confirmee et etendue.
10. Observable reconstruite est une fonction architecturale stabilisee.
11. Les tensions de donnees appartiennent au regime d'acces.
12. Exactitude SI n'est pas precision empirique.
13. Une constante definissante peut garder un role physique fort.
```

Formule de controle :

```text
famille = fonction principale
fonction transversale = role secondaire ou transversal
fonction architecturale = role dans une configuration globale
architecture = articulation de familles et fonctions dans un regime
acces = maniere dont la grandeur est connue
exactitude SI = mode de definition, non epuisement physique
```

### 27. Points encore ouverts

La carte v1.1 est une carte de reference, mais elle n'est pas une cloture du projet.

Trois chantiers restent ouverts.

#### 27.1 Synthese transversale des architectures

Les quatre architectures reconnues ont maintenant ete comparees entre elles.

Document produit :

```text
05_CARTES_ET_SYNTHESES/Synthese_architectures_inter_familles_v1_0.md
```

Question :

```text
quels invariants methodologiques traversent Saveur-Higgs, SI, effective basse energie et cosmologique ?
```

#### 27.2 Sous-cycles specialises eventuels

Des sous-cycles peuvent etre ouverts plus tard, mais seulement apres identification d'un besoin precis.

Exemples possibles :

```text
alpha et constantes electriques derivees
G_N et constantes gravitationnelles
energie noire ou inflation
autres theories effectives
```

#### 27.3 Mise en ordre documentaire

Les nouvelles notes sont dans l'arborescence recommandee.

Une consolidation documentaire ulterieure pourrait renforcer :

```text
00_README/
01_CADRE_METHODOLOGIQUE/
02_CYCLES_PHYSIQUES/
03_TESTS_TAXONOMIQUES/
04_ARCHITECTURES_INTER_FAMILLES/
05_CARTES_ET_SYNTHESES/
```

sans deplacer les archives tant que les dependances internes ne sont pas verifiees.

### 28. Mise a jour methodologique v1.2

La mise a jour methodologique issue de la synthese transversale est maintenant produite.

Document produit :

```text
01_CADRE_METHODOLOGIQUE/Note_synthese_methodologique_v1_2.md
```

Question traitee :

> Comment integrer dans la methode les invariants communs des architectures inter-familles ?

Decision methodologique :

```text
architecture inter-familles = niveau methodologique reconnu,
avec test de reconnaissance,
formes internes,
et matrice d'usage.
```

Cette etape confirme qu'il est plus prudent de stabiliser le rang des architectures avant d'ouvrir un nouveau cycle physique.

Etape documentaire produite :

```text
05_CARTES_ET_SYNTHESES/Index_raisonne_du_corpus_v1_0.md
```

Question directrice :

> Comment naviguer dans le corpus sans perdre la hierarchie entre brief, methode, cycles, architectures, syntheses et cartes ?

Decision documentaire :

```text
l'index raisonne devient le point d'entree pour naviguer dans le corpus,
sans remplacer la note methodologique v1.2 ni la carte consolidee v1.1.
```

Prolongement de revision produit ensuite :

```text
01_CADRE_METHODOLOGIQUE/Revision_de_fond_v0_1_temporalite.md
```

Statut :

```text
revision active preparant une integration methodologique de la temporalite,
sans remplacer encore la carte v1.1.
```

Methode active produite ensuite :

```text
01_CADRE_METHODOLOGIQUE/Note_synthese_methodologique_v1_3_pre_familial_et_temporalite.md
```

Protocole d'application produit ensuite :

```text
01_CADRE_METHODOLOGIQUE/Matrice_criblage_taxonomique_v0_1.md
```

Note d'architecture produite ensuite :

```text
04_ARCHITECTURES_INTER_FAMILLES/Architecture_saveur_Higgs_notes.md
```

Carte de dependances produite ensuite :

```text
05_CARTES_ET_SYNTHESES/Carte_dependances_architectures_v0_1.md
```

Carte consolidee de refonte produite ensuite :

```text
05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_2_refonte.md
```

Stress test cosmologique produit ensuite :

```text
04_ARCHITECTURES_INTER_FAMILLES/Architecture_cosmologique_stress_test_v0_1.md
```

Statut documentaire :

```text
la v1.3 prolonge la methode,
tandis que la carte v1.1 devient une carte historique recente apres la carte v1.2 de refonte.
```

### 29. Documents internes integres

Documents de reference et de prolongement associes a la v1.1 :

```text
PROJECT_BRIEF.docx
01_CADRE_METHODOLOGIQUE/Note_synthese_methodologique_v1_1.md
01_CADRE_METHODOLOGIQUE/Note_synthese_methodologique_v1_2.md
01_CADRE_METHODOLOGIQUE/Revision_de_fond_v0_1_temporalite.md
01_CADRE_METHODOLOGIQUE/Fiche_criblage_critiques_v0_1.md
01_CADRE_METHODOLOGIQUE/Note_synthese_methodologique_v1_3_pre_familial_et_temporalite.md
01_CADRE_METHODOLOGIQUE/Matrice_criblage_taxonomique_v0_1.md
04_ARCHITECTURES_INTER_FAMILLES/Architecture_saveur_Higgs_notes.md
05_CARTES_ET_SYNTHESES/Carte_dependances_architectures_v0_1.md
05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_2_refonte.md
04_ARCHITECTURES_INTER_FAMILLES/Architecture_cosmologique_stress_test_v0_1.md
05_CARTES_ET_SYNTHESES/Carte_consolidee_v0_9.md
05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_0.md
05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_1.md
05_CARTES_ET_SYNTHESES/Synthese_architectures_inter_familles_v1_0.md
05_CARTES_ET_SYNTHESES/Index_raisonne_du_corpus_v1_0.md
04_ARCHITECTURES_INTER_FAMILLES/Architecture_effective_basse_energie_notes.md
04_ARCHITECTURES_INTER_FAMILLES/Architecture_cosmologique_notes.md
04_ARCHITECTURES_INTER_FAMILLES/Architecture_metrologique_SI_notes.md
02_CYCLES_PHYSIQUES/06_Cycle_effectif_basse_energie/Synthese_cycle_effectif_basse_energie_v0_1.md
02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Synthese_cycle_cosmologique_v0_1.md
02_CYCLES_PHYSIQUES/08_Cycle_metrologique_SI/Cycle_metrologique_SI_v0_1_c_h_e.md
```

Documents cosmologiques sources de la synthese :

```text
02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Cycle_cosmologique_v0_1_cadrage.md
02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Cycle_cosmologique_v0_2_Lambda.md
02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Cycle_cosmologique_v0_3_H0.md
02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Cycle_cosmologique_v0_4_Omega_i.md
02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Cycle_cosmologique_v0_5_w.md
02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Cycle_cosmologique_v0_6_As_ns.md
02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Cycle_cosmologique_v0_7_sigma8_S8.md
```

### 30. Formule de cloture

La v1.1 peut etre resumee par six formules.

```text
constance = robustesse fonctionnelle situee
famille = fonction principale
fonction transversale = role secondaire ou transversal
fonction architecturale = role dans une configuration globale
architecture = articulation de familles dans un regime
exactitude SI = definition d'unites, non epuisement physique
```

Formule finale :

> Une architecture n'ajoute pas une famille ; elle montre comment plusieurs familles deviennent solidaires dans un regime de description.

Formule specifique v1.1 :

> La robustesse d'une constante effective est toujours situee : elle depend d'une fonction, d'un regime, d'un acces, d'un mode de stabilisation, et parfois d'une architecture qui rend plusieurs fonctions solidaires.
