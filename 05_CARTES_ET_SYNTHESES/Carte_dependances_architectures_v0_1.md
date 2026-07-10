# Carte des dependances architecturales v0.1

## Reseaux inter-familles apres la methode v1.3

### 1. Fonction de la carte

Cette carte represente les architectures inter-familles comme des reseaux de dependance.

Elle prolonge :

```text
01_CADRE_METHODOLOGIQUE/Note_synthese_methodologique_v1_3_pre_familial_et_temporalite.md
01_CADRE_METHODOLOGIQUE/Matrice_criblage_taxonomique_v0_1.md
02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/Synthese_cycle_saveur_Higgs_v0_1.md
04_ARCHITECTURES_INTER_FAMILLES/Architecture_saveur_Higgs_notes.md
04_ARCHITECTURES_INTER_FAMILLES/Architecture_metrologique_SI_notes.md
04_ARCHITECTURES_INTER_FAMILLES/Architecture_effective_basse_energie_notes.md
04_ARCHITECTURES_INTER_FAMILLES/Architecture_cosmologique_notes.md
```

Elle ne remplace pas encore une carte consolidee generale.

Elle sert a preparer une carte de refonte en montrant :

```text
quels noeuds sont solidaires,
quels retraits cassent une architecture,
quels acces conditionnent la stabilisation,
et quels points restent ouverts.
```

Regle directrice :

```text
une architecture est un reseau de dependances fonctionnelles,
non une ligne supplementaire dans une taxonomie.
```

### 2. Les quatre reseaux actifs

| Architecture | Forme dominante | Type de dependance | Noeud critique | Risque evite |
|---|---|---|---|---|
| Saveur-Higgs | Constitutive | Constitution d'un secteur apres brisure et diagonalisation | `v + Y_f + diagonalisation` | Famille Saveur-Higgs ou fragmentation locale |
| Metrologique SI | Definitionnelle / operationnelle | Definitions d'unites, compositions exactes et realisations | Constantes definissantes | Famille metrologique ou reduction conventionnelle |
| Effective basse energie | Validite | Domaine de description, echelles, seuils et raccordements | Echelle de validite | Famille Effectif ou approximation vague |
| Cosmologique | Inferentielle / reconstructive | Modele global, acces multiples, tensions et reconstruction | Couplage modele-acces | Famille Cosmologie ou tableau de parametres |

Decision :

```text
les quatre architectures restent actives,
mais elles ne dependent pas du meme type de solidarite.
```

### 3. Grammaire commune des dependances

Une architecture active doit pouvoir etre lue selon sept dependances.

| Dependence | Question | Effet methodologique |
|---|---|---|
| Dependence de regime | Dans quel regime les grandeurs prennent-elles sens ? | Evite le classement hors contexte |
| Dependence fonctionnelle | Quelles fonctions deviennent solidaires ? | Evite la simple juxtaposition |
| Dependence d'acces | Comment les grandeurs sont-elles connues ? | Evite les nombres nus |
| Dependence de modele | Quel cadre conditionne l'inference ou l'usage ? | Evite la naturalisation prematuree |
| Dependence temporelle | Comment le statut s'installe ou se transforme ? | Evite le tableau statique |
| Dependence de retrait | Que perd-on si un noeud est retire ? | Teste la robustesse architecturale |
| Dependence de limite | Ce que l'architecture ne resout pas | Evite l'inflation theorique |

Formule :

```text
architecture =
regime
+ fonctions solidaires
+ acces
+ modele ou definition
+ trajectoire
+ test de retrait
+ limites explicites.
```

### 4. Carte locale : Saveur-Higgs

Type :

```text
architecture constitutive.
```

Reseau minimal :

```text
regime electrofaible brise
-> v
-> Y_f
-> matrices de masse
-> diagonalisation
-> m_f
-> CKM / PMNS
-> manifestations transitionnelles ou oscillatoires
```

Table de dependances :

| Noeud | Depend de | Rend possible | Retrait |
|---|---|---|---|
| `v` | Brisure electrofaible | Echelle commune des masses faibles et fermioniques | Plus d'echelle commune |
| `Y_f` | Couplages au Higgs | Distribution de l'echelle entre fermions | Plus de texture de masse |
| Diagonalisation | Matrices de masse | Spectres physiques et orientations | Plus de masses physiques ni de desalignements lisibles |
| `m_f` | `v`, `Y_f`, diagonalisation | Spectres fermioniques stabilises | Perte des valeurs de masse du regime brise |
| CKM | Desalignement des secteurs quark | Transitions faibles, melanges de mesons, CP | Perte de l'orientation transitionnelle |
| PMNS | Secteur neutrino massif | Oscillations de saveur | Perte de l'orientation oscillatoire |
| `Delta m^2` | Spectre neutrino massif | Dephasages oscillatoires | Oscillations sans echelle spectrale stabilisee |

Lecture v1.3 :

```text
la relation m_f = y_f v / sqrt(2) est un signe local,
mais la dependance robuste est architecturale.
```

Limites conservees :

```text
origine des Yukawa,
hierarchies de masses,
contraste CKM / PMNS,
nature Dirac ou Majorana des neutrinos,
ancrage absolu du spectre neutrino.
```

### 5. Carte locale : Metrologique SI

Type :

```text
architecture definitionnelle et operationnelle.
```

Reseau minimal :

```text
constantes definissantes
-> definitions d'unites
-> compositions exactes
-> realisations pratiques
-> systeme coherent de mesure
-> roles physiques conserves
```

Table de dependances :

| Noeud | Depend de | Rend possible | Retrait |
|---|---|---|---|
| `k_B`, `N_A`, `c`, `h`, `e` | Decision definitionnelle SI | Unites exactes associees | Perte du socle definitionnel |
| `R` | `N_A k_B` | Composition thermodynamique exacte | Perte d'une composition exacte, pas du role physique de k_B |
| `K_J` | `2 e / h` | Metrologie electrique quantique | Perte d'une composition pratique exacte |
| `R_K` | `h / e^2` | Resistance Hall quantique exacte | Perte d'une composition pratique exacte |
| Realisations pratiques | Procedures experimentales | Mise en oeuvre des definitions | Exactitude formelle sans acces operationnel |
| Roles physiques conserves | Regimes physiques propres | Non-reduction des constantes a la convention | Appauvrissement conceptuel |

Lecture v1.3 :

```text
exactitude numerique ne signifie pas epuisement physique.
```

Limites conservees :

```text
origine physique de c, h ou e,
interpretation de la quantification,
dynamique du couplage electromagnetique,
philosophie complete de la mesure.
```

### 6. Carte locale : Effective basse energie

Type :

```text
architecture de validite.
```

Reseau minimal :

```text
regime limite
-> echelle de validite
-> non-resolution explicite
-> couplages ou coefficients effectifs
-> raccordement local, distribue ou attendu
-> domaine de description
```

Table de dependances :

| Noeud | Depend de | Rend possible | Retrait |
|---|---|---|---|
| `G_F` | Integration du mediateur `W` | Theorie de Fermi basse energie | Perte du raccordement local faible |
| `M_W` | Theorie electrofaible | Seuil de validite de Fermi | Validite du coefficient mal bornee |
| `alpha_s(Q^2)` | Echelle `Q` | Couplage courant QCD | Perte du flot de couplage |
| `Lambda_QCD` | Dynamique QCD | Separation perturbatif / non perturbatif | Changement de regime non localise |
| `alpha_G(E)` | Rapport a l'echelle d'energie | Couplage gravitationnel effectif | Perte de la lecture dimensionnelle |
| `M_Pl` | `G_N`, `hbar`, `c` | Echelle de suppression ou validite attendue | Limite gravitationnelle non balisee |

Lecture v1.3 :

```text
l'effectivite ne stabilise pas seulement une valeur ;
elle stabilise un domaine de description.
```

Limites conservees :

```text
completion quantique de la gravitation,
dynamique profonde des couplages,
nature ultime des seuils,
origine des constantes.
```

### 7. Carte locale : Cosmologique

Type :

```text
architecture inferentielle et reconstructive.
```

Reseau minimal :

```text
modele cosmologique
-> fonctions architecturales
-> grandeurs globales ou reconstruites
-> regimes d'acces multiples
-> dependances d'inference
-> tensions ou convergences
```

Table de dependances :

| Noeud | Depend de | Rend possible | Retrait |
|---|---|---|---|
| `Lambda` | Modele de fond | Terme de fond dans LambdaCDM | Perte du role de fond accelere |
| `H_0` | Expansion actuelle + acces | Parametre d'etat present | Expansion actuelle mal normalisee |
| `Omega_i` | `rho_i / rho_crit` | Budget normalise | Composition globale non comparable |
| `w` | Relation pression / densite | Parametrisation d'etat | Composante noire moins testable |
| `A_s`, `n_s` | Spectre primordial | Conditions initiales perturbatives | Lien primordial mal specifie |
| `sigma_8`, `S_8` | Croissance tardive + modele | Observables reconstruites | Tensions de structure non formulables |
| Regimes d'acces | CMB, BAO, SNe, ladder, lensing, amas | Contraintes croisees | Robustesse confondue avec un seul acces |
| Modele d'inference | LambdaCDM, wCDM, w0waCDM, calibrations | Extraction des valeurs | Naturalisation prematuree des parametres |

Lecture v1.3 :

```text
en cosmologie, le role et l'acces font partie du classement.
```

Limites conservees :

```text
nature de l'energie noire,
origine de Lambda,
tensions H_0 et S_8,
physique microfondatrice de l'inflation,
validite ultime de LambdaCDM.
```

### 8. Matrice comparative des dependances

| Architecture | Noeud generateur | Noeud d'acces | Noeud temporel | Noeud fragile |
|---|---|---|---|---|
| Saveur-Higgs | Brisure + `v` + `Y_f` | Masses, transitions, oscillations, fits | Constitution apres brisure | Origine des Yukawa et secteur neutrino |
| Metrologique SI | Definitions d'unites | Realisations pratiques | Absorption conventionnelle | Confusion exactitude / realisation |
| Effective basse energie | Regime limite + echelle | Experiences dans un domaine de validite | Transition, flot, validite | Completion ou seuil profond ouvert |
| Cosmologique | Modele global | Reseaux d'inference | Acces, reconstruction, evolution cosmique | Sous-reseaux, tensions et dependances de modele |

Conclusion :

```text
la meme notion d'architecture couvre quatre formes de dependance,
mais pas une seule forme de causalite.
```

### 9. Typologie des aretes

Les dependances ne sont pas toutes du meme type.

| Type d'arete | Sens | Exemple |
|---|---|---|
| Constitutive | Un noeud rend un autre definissable dans un regime | `v + Y_f -> m_f` |
| Compositionnelle | Une relation exacte derive d'elements definissants | `R = N_A k_B` |
| Operationnelle | Une procedure rend une definition praticable | Realisations SI |
| Effective | Une grandeur condense une structure non resolue | `G_F` |
| De validite | Une echelle borne un domaine | `M_W`, `Lambda_QCD`, `M_Pl` |
| Inferentielle | Une valeur est extraite par modele et donnees | `H_0`, `sigma_8`, `S_8` |
| De tension | Une discordance appartient au reseau d'acces | Tension `H_0`, tension `S_8` |
| Temporelle | Un statut apparait par constitution, flot, convention ou inference | Brisure, flot QCD, SI, cosmologie |

Regle :

```text
une carte de dependances doit nommer le type d'arete,
pas seulement relier deux grandeurs.
```

### 10. Tests de retrait transversaux

| Retrait | Effet | Interpretation |
|---|---|---|
| Retirer le regime | Les grandeurs deviennent des labels flottants | Pas d'architecture sans regime |
| Retirer l'acces | Les valeurs deviennent des nombres sans statut epistemique | Pas de robustesse sans acces |
| Retirer le modele | Les grandeurs reconstruites perdent leur cadre | Critique surtout en cosmologie |
| Retirer la temporalite | La carte redevient un tableau statique | La stabilisation n'est plus decrite |
| Retirer le test de limite | L'architecture devient inflationniste | Risque de famille deguisee |
| Retirer un noeud central | Le reseau se deforme ou s'effondre | Test local de robustesse |

Decision :

```text
une architecture est robuste si son reseau change reellement
quand un noeud central est retire.
```

### 11. Points de contact entre architectures

Les architectures ne sont pas isolees.

| Contact | Architectures concernees | Sens |
|---|---|---|
| `v` / `M_W` / `G_F` | Saveur-Higgs et effective basse energie | Le regime electrofaible brise nourrit aussi le raccordement faible basse energie |
| `h`, `c`, `e` / `alpha` | SI et couplages physiques | La convention SI fixe des valeurs dimensionnees sans epuiser les couplages sans dimension |
| `M_Pl` / cosmologie | Effective et cosmologique | Echelle gravitationnelle, regimes primordiaux et limites d'inference |
| Neutrinos / cosmologie | Saveur-Higgs et cosmologique | Masse absolue, oscillations, contraintes cosmologiques |
| Tensions d'acces | Cosmologie et autres architectures | La cosmologie rend explicite un probleme general de regime d'acces |

Regle :

```text
un contact entre architectures n'est pas automatiquement une nouvelle architecture.
```

Il peut etre :

```text
un raccordement,
une dependance de fond,
une contrainte externe,
un acces supplementaire,
ou un chantier futur.
```

### 12. Consequences pour Relation

La carte confirme la refonte de Relation.

Relation apparait dans plusieurs architectures :

```text
m_f = y_f v / sqrt(2)
R = N_A k_B
K_J = 2 e / h
R_K = h / e^2
Omega_i = rho_i / rho_crit
w = p / rho
```

Mais ces occurrences ne sont pas equivalentes.

| Cas | Type de relation | Bon rang |
|---|---|---|
| `m_f = y_f v / sqrt(2)` | Constitutive locale | Architecture Saveur-Higgs |
| `R = N_A k_B` | Composition exacte | Architecture SI + composition exacte |
| `K_J`, `R_K` | Composition metrologique exacte | Architecture SI + realisation pratique |
| `Omega_i` | Normalisation cosmologique | Role de densite normalisee |
| `w` | Relation d'etat | Role contextuel d'etat |

Decision :

```text
Relation n'est pas supprimee,
mais elle doit etre sous-typee par son reseau de dependance.
```

### 13. Consequences pour la temporalite

La carte confirme que la temporalite est un axe transversal.

| Architecture | Profil temporel | Forme de stabilisation |
|---|---|---|
| Saveur-Higgs | Constitution | Les masses et orientations deviennent lisibles apres brisure et diagonalisation |
| SI | Absorption conventionnelle | Certaines valeurs deviennent definissantes sans perdre leur role physique |
| Effective basse energie | Validite, transition, flot | Les grandeurs valent dans un domaine ou selon une echelle |
| Cosmologique | Acces, inference, evolution | Les valeurs sont stabilisees par histoire cosmique et routes d'inference |

Regle :

```text
le temps ne cree pas une famille ;
il expose la trajectoire d'une stabilisation.
```

### 14. Consequences pour la carte consolidee v1.2

La carte consolidee v1.2 ne devait pas seulement ajouter des lignes.

Elle devait changer la forme de presentation.

Elle distingue :

```text
1. familles fonctionnelles fortes ;
2. Relation comme famille faible sous audit ;
3. roles contextuels ;
4. architectures actives ;
5. dependances inter-architectures ;
6. trajectoires de stabilisation ;
7. limites et tests de retrait.
```

Document produit :

```text
05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_2_refonte.md
```

Role :

```text
integrer la methode v1.3,
la matrice de criblage,
les quatre architectures actives,
et la carte des dependances.
```

### 15. Documents integres

Documents methodologiques :

```text
01_CADRE_METHODOLOGIQUE/Note_synthese_methodologique_v1_3_pre_familial_et_temporalite.md
01_CADRE_METHODOLOGIQUE/Matrice_criblage_taxonomique_v0_1.md
01_CADRE_METHODOLOGIQUE/Revision_de_fond_v0_1_temporalite.md
01_CADRE_METHODOLOGIQUE/Fiche_criblage_critiques_v0_1.md
```

Architectures actives :

```text
04_ARCHITECTURES_INTER_FAMILLES/Architecture_saveur_Higgs_notes.md
04_ARCHITECTURES_INTER_FAMILLES/Architecture_metrologique_SI_notes.md
04_ARCHITECTURES_INTER_FAMILLES/Architecture_effective_basse_energie_notes.md
04_ARCHITECTURES_INTER_FAMILLES/Architecture_cosmologique_notes.md
```

Syntheses et cartes :

```text
05_CARTES_ET_SYNTHESES/Synthese_architectures_inter_familles_v1_0.md
05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_1.md
05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_2_refonte.md
05_CARTES_ET_SYNTHESES/Index_raisonne_du_corpus_v1_0.md
```

Stress test associe :

```text
04_ARCHITECTURES_INTER_FAMILLES/Architecture_cosmologique_stress_test_v0_1.md
```

### 16. Statut documentaire

Cette carte est une consolidation transversale.

Statut :

```text
consolidation transversale integree dans la carte consolidee v1.2.
```

Elle autorise :

```text
l'application du test de retrait aux architectures,
et la lecture de Relation par reseau de dependance.
```

Elle n'autorise pas encore :

```text
une nouvelle famille,
une fusion des architectures,
ou une resolution des tensions physiques ouvertes.
```

### 17. Formule de cloture

Une architecture n'est pas seulement un groupe de constantes.

C'est une forme de dependance stabilisee.

Formule finale :

> La carte des dependances montre ce que la taxonomie seule ne montre pas : une constante effective stabilisee tient son statut d'un reseau de regime, de fonction, d'acces, de temporalite et de limites.
