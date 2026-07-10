# Architecture Saveur-Higgs - notes d'integration

## Statut apres conversion de la note historique et refonte v1.3

### 1. Fonction de la note

Cette note met l'architecture Saveur-Higgs au meme format que les autres architectures inter-familles actives.

Elle prolonge la note historique :

```text
Note de consolidation saveur-Higgs v0.1.docx
```

Elle integre aussi les corrections introduites par :

```text
01_CADRE_METHODOLOGIQUE/Note_synthese_methodologique_v1_3_pre_familial_et_temporalite.md
01_CADRE_METHODOLOGIQUE/Matrice_criblage_taxonomique_v0_1.md
```

La note ne remplace pas les fiches locales sur `v`, les Yukawa, CKM, PMNS ou les neutrinos.

Elle en extrait la consequence taxonomique principale :

```text
Architecture Saveur-Higgs = architecture constitutive inter-familles
```

et non :

```text
nouvelle famille superieure
```

### 2. Decision centrale

L'architecture Saveur-Higgs est confirmee comme architecture robuste.

Elle articule principalement :

```text
Echelle
Couplage
Relation constitutive sous audit
Orientation
Spectres de masse
Manifestations transitionnelles ou oscillatoires
```

La decision de rang est :

```text
Saveur-Higgs = architecture constitutive
```

et non :

```text
Saveur-Higgs = famille fonctionnelle autonome
```

Cette decision evite deux erreurs opposees :

```text
fragmenter le secteur en familles locales trop nombreuses,
ou creer une famille Saveur-Higgs qui absorberait echelles, couplages, masses et orientations.
```

### 3. Definition locale proposee

Une architecture Saveur-Higgs est une configuration inter-familles dans laquelle une echelle de brisure, des matrices de couplage, des spectres de masses et des matrices d'orientation deviennent solidaires dans le regime electrofaible brise.

Cette definition repose sur six elements.

```text
1. Une echelle commune : v
2. Des couplages de texture : Y_f
3. Une diagonalisation des matrices de masse
4. Des masses fermioniques stabilisees : m_f
5. Des orientations entre bases : CKM et PMNS
6. Des manifestations phenomenologiques distinctes : transitions, oscillations, phases CP
```

Le point important est le troisieme.

Les masses et les orientations ne sont pas ajoutees exterieurement aux Yukawa. Elles deviennent lisibles apres brisure electrofaible et diagonalisation.

### 4. Corpus stabilise

Le corpus stabilise comprend plusieurs niveaux.

| Grandeur | Rang v1.3 | Famille ou role principal | Fonction dans l'architecture |
|---|---|---|---|
| `v` | Echelle | Echelle | Echelle electrofaible du regime brise |
| `Y_u`, `Y_d`, `Y_e` | Matrices | Couplage | Couplages de texture distribuant l'echelle entre fermions |
| `m_f` | Valeurs spectrales / relation constitutive | Role de spectre stabilise | Masses physiques apres brisure et diagonalisation |
| `CKM` | Matrice | Orientation | Desalignement transitionnel dans le secteur quark |
| `PMNS` | Matrice | Orientation | Desalignement oscillatoire dans le secteur leptonique massif |
| `Delta m^2` | Ecart spectral | Role de dephasage | Ecarts qui stabilisent les oscillations neutrino |
| Phases CP | Phase | Orientation complexe | Asymetries CP dans les secteurs quark ou neutrino |
| Masse absolue neutrino | Borne / projection | Seuil spectral ou projection | Ancrage partiel du spectre neutrino |

Ces grandeurs n'appartiennent pas toutes a la meme famille.

C'est precisement pourquoi le niveau architectural est necessaire.

### 5. Forme constitutive de l'architecture

La structure minimale est :

```text
v
+ Y_f
+ diagonalisation
-> m_f
+ desalignements entre bases
-> CKM / PMNS
```

Dans le cas diagonal simplifie :

```text
m_f = y_f v / sqrt(2)
```

Dans le cas general :

```text
M_f = Y_f v / sqrt(2)
```

puis les matrices de masse sont diagonalisees.

La formule `m_f = y_f v / sqrt(2)` ne doit donc pas etre traitee comme une simple relation isolee.

Elle est le signe local d'une architecture constitutive.

### 6. Formes internes

#### 6.1 Echelle electrofaible

Cas principal :

```text
v
```

Lecture :

```text
echelle du regime electrofaible brise
```

Decision :

```text
v appartient a la famille Echelle.
```

Precision :

```text
v ne genere pas seul les masses ;
il fournit l'echelle commune que les Yukawa distribuent.
```

#### 6.2 Couplages de texture

Cas principaux :

```text
Y_u
Y_d
Y_e
```

Lecture :

```text
couplages au champ de Higgs,
organises sous forme matricielle,
distribuant l'echelle electrofaible entre generations.
```

Decision :

```text
les Yukawa relevent d'abord de Couplage.
```

Sous-type utile :

```text
couplage de texture
```

Limite :

```text
differenciation fermionique n'est pas une famille autonome.
```

#### 6.3 Masses fermioniques

Cas principaux :

```text
m_u, m_c, m_t
m_d, m_s, m_b
m_e, m_mu, m_tau
```

Lecture :

```text
valeurs spectrales stabilisees dans le regime electrofaible brise.
```

Decision v1.3 :

```text
ne pas classer automatiquement les masses fermioniques dans Relation.
```

La relation constitutive est reelle, mais son bon rang est architectural.

La masse physique est mieux lue comme :

```text
valeur stabilisee issue de l'articulation entre echelle, couplage et diagonalisation.
```

#### 6.4 Orientation CKM

Cas principal :

```text
CKM
```

Structure :

```text
V_CKM = U_L^u dagger U_L^d
```

Lecture :

```text
desalignement entre les rotations gauches des secteurs quark up et down.
```

Decision :

```text
CKM releve de la famille Orientation.
```

Manifestation :

```text
transitionnelle : desintegrations faibles, melanges de mesons, observables CP.
```

CKM n'est pas une constante de saveur autonome.

C'est la trace observable d'un desalignement interne aux textures de Yukawa.

#### 6.5 Parametrisation de Wolfenstein

Cas :

```text
lambda, A, rho, eta
```

Lecture :

```text
coordonnees hierarchiques de CKM.
```

Decision :

```text
Wolfenstein ne constitue pas une nouvelle famille.
```

Role contextuel :

```text
hierarchie locale de l'orientation CKM.
```

#### 6.6 Orientation PMNS

Cas principal :

```text
PMNS
```

Structure typique :

```text
U_PMNS = U_L^e dagger U_nu
```

Lecture :

```text
desalignement entre la base des leptons charges et la base des neutrinos massifs.
```

Decision :

```text
PMNS releve de la famille Orientation.
```

Manifestation :

```text
oscillatoire : changement de saveur des neutrinos au cours de la propagation.
```

Prudence :

```text
PMNS suppose un secteur neutrino massif,
qui depasse le Modele standard minimal.
```

#### 6.7 Ecarts spectraux neutrino

Cas principaux :

```text
Delta m^2_21
Delta m^2_31
Delta m^2_32
```

Lecture :

```text
ecarts spectraux stabilisant les dephasages oscillatoires.
```

Decision :

```text
Delta m^2 n'est pas une famille oscillatoire.
```

Rang v1.3 :

```text
forme logique : ecart spectral
role contextuel : dephasage oscillatoire
famille candidate : Relation sous audit ou Echelle locale selon le dossier
```

### 7. Matrice de criblage appliquee

| Cas | Forme logique | Famille candidate | Role contextuel | Decision |
|---|---|---|---|---|
| `v` | Valeur / echelle | Echelle | Echelle structurante | Classement confirme |
| `Y_f` | Matrice | Couplage | Texture de distribution | Classement confirme avec sous-type |
| `m_f` | Valeur spectrale issue d'une relation | Relation sous audit / Echelle locale | Spectre stabilise | Classement deplace vers architecture |
| `CKM` | Matrice | Orientation | Orientation transitionnelle | Classement confirme |
| `PMNS` | Matrice | Orientation | Orientation oscillatoire | Classement confirme avec prudence neutrino |
| `Delta m^2` | Ecart | Relation sous audit | Dephasage oscillatoire | Role contextuel a expliciter |
| Masse absolue neutrino | Borne / projection | Echelle ou seuil sous audit | Ancrage spectral | Dossier ouvert |

Conclusion :

```text
Relation intervient dans l'ecriture,
mais elle ne suffit pas a classer l'architecture.
```

### 8. Regime physique et regime d'acces

Le regime physique principal est :

```text
regime electrofaible brise
```

Le regime d'acces varie selon les objets.

| Grandeur | Regime d'acces | Robustesse |
|---|---|---|
| `v` | Infere via `G_F`, masses faibles et ajustements electrofaibles | Forte dans le cadre standard |
| Yukawa charges | Inferees via masses et couplages au Higgs | Forte pour certains effets, origine ouverte |
| Masses de leptons charges | Mesures directes ou spectroscopiques | Forte |
| Masses de quarks | Reconstruites avec dependance de schema | Robuste mais scheme-dependante |
| CKM | Desintegrations faibles, mesons, fits globaux | Forte globale, tensions locales possibles |
| PMNS | Oscillations neutrino | Forte pour plusieurs angles, incomplete pour certaines phases |
| `Delta m^2` | Oscillations neutrino | Forte pour les ecarts, pas pour l'ancrage absolu |
| Masse absolue neutrino | Beta decay, cosmologie, double beta sans neutrino selon hypotheses | Bornee / ouverte |

Regle :

```text
une grandeur de l'architecture Saveur-Higgs doit toujours etre accompagnee de son acces.
```

### 9. Couplage modele-acces

L'architecture Saveur-Higgs a un couplage modele-acces intermediaire.

Elle est moins reconstructive que l'architecture cosmologique, mais elle n'est pas purement directe.

Exemples :

```text
les masses de quarks dependent d'un schema de definition ;
CKM depend de fits globaux et d'observables faibles ;
PMNS depend du cadre neutrino massif ;
la masse absolue des neutrinos depend de routes d'acces heterogenes.
```

Decision :

```text
les grandeurs de saveur ne doivent pas etre traitees comme des nombres nus.
```

Elles sont stabilisees par une combinaison de regime, modele, acces et diagonalisation.

### 10. Profil temporel

Le profil temporel dominant est :

```text
temporalite de constitution.
```

La structure devient lisible selon une sequence conceptuelle :

```text
regime electrofaible non brise
-> brisure electrofaible
-> matrices de masse
-> diagonalisation
-> spectres physiques
-> orientations observables
-> manifestations transitionnelles ou oscillatoires
```

Cette temporalite ne doit pas etre confondue avec une histoire complete de l'origine des Yukawa.

Elle indique seulement :

```text
le regime dans lequel les masses et orientations deviennent definissables et observables.
```

### 11. Stress test d'architecture

L'architecture Saveur-Higgs resiste au stress test.

| Test | Resultat |
|---|---|
| Plusieurs familles sont-elles solidaires ? | Oui : Echelle, Couplage, Orientation, roles relationnels et spectraux |
| Le retrait de `v` modifie-t-il l'ensemble ? | Oui : plus d'echelle commune de brisure |
| Le retrait des Yukawa modifie-t-il l'ensemble ? | Oui : plus de distribution entre fermions |
| Le retrait de la diagonalisation modifie-t-il l'ensemble ? | Oui : plus de masses physiques ni d'orientations lisibles |
| Le retrait de CKM / PMNS modifie-t-il l'ensemble ? | Oui : disparition des orientations observables |
| Le regime physique est-il explicite ? | Oui : electrofaible brise, avec prudence neutrino |
| Le regime d'acces est-il explicite ? | Oui, mais variable selon les objets |
| L'architecture se reduit-elle a Relation ? | Non |

Conclusion :

```text
Saveur-Higgs est une architecture constitutive confirmee.
```

### 12. Limites conservees

Cette note ne resout pas :

```text
l'origine des valeurs de Yukawa,
l'origine des hierarchies de masses,
la raison du contraste entre CKM et PMNS,
la nature Dirac ou Majorana des neutrinos,
l'origine dynamique des textures,
l'ancrage absolu complet du spectre neutrino.
```

Ces limites ne fragilisent pas l'architecture comme architecture.

Elles indiquent seulement ce que l'architecture stabilise :

```text
une organisation fonctionnelle du secteur,
non une theorie complete de son origine.
```

### 13. Consequences pour la carte consolidee

La carte consolidee de refonte traite Saveur-Higgs comme architecture active au meme rang documentaire que :

```text
Architecture metrologique SI
Architecture effective basse energie
Architecture cosmologique
```

Elle corrige aussi la lecture de `Relation`.

Ancienne lecture possible :

```text
m_f = relation constitutive, donc Relation.
```

Lecture v1.3 :

```text
m_f a une forme relationnelle,
mais le classement robuste passe par l'architecture Saveur-Higgs.
```

Document de refonte produit ensuite :

```text
05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_2_refonte.md
```

### 14. Documents integres

Documents historiques :

```text
Note de consolidation saveur-Higgs v0.1.docx
Fiche Yukawa v0.1.docx
Fiche CKM v0.1.docx
Fiche Wolfenstein v0.1.docx
Fiche Delta m^2.docx
Fiche Angles de Melange Leptoniques.docx
Fiche masse absolue des neutrinos.docx
```

Documents Markdown actifs :

```text
01_CADRE_METHODOLOGIQUE/Note_synthese_methodologique_v1_3_pre_familial_et_temporalite.md
01_CADRE_METHODOLOGIQUE/Matrice_criblage_taxonomique_v0_1.md
05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_1.md
05_CARTES_ET_SYNTHESES/Synthese_architectures_inter_familles_v1_0.md
01_CADRE_METHODOLOGIQUE/Revision_de_fond_v0_1_temporalite.md
01_CADRE_METHODOLOGIQUE/Fiche_criblage_critiques_v0_1.md
```

### 15. Statut apres integration

La dette documentaire Saveur-Higgs est levee au niveau Markdown.

Statut :

```text
architecture active,
constitutive,
confirmee,
avec limites explicites.
```

Carte de dependances produite ensuite :

```text
05_CARTES_ET_SYNTHESES/Carte_dependances_architectures_v0_1.md
```

Carte consolidee de refonte produite ensuite :

```text
05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_2_refonte.md
```

### 16. Formule de cloture

L'architecture Saveur-Higgs ne dit pas pourquoi les textures de saveur sont ce qu'elles sont.

Elle dit comment elles deviennent une structure stabilisee.

Formule finale :

> Dans le secteur Saveur-Higgs, la constance n'est pas portee par un type unique de grandeur ; elle resulte d'une architecture constitutive ou echelle, couplages, spectres et orientations deviennent solidaires dans le regime electrofaible brise.
