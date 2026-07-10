# Note de synthese methodologique v1.3

## Rang pre-familial, roles contextuels et temporalite

### 1. Fonction de la v1.3

La v1.3 integre deux chantiers devenus inseparables :

```text
1. le rang pre-familial de forme logique de stabilisation ;
2. l'axe temporel comme trajectoire de stabilisation.
```

Elle s'appuie sur :

```text
01_CADRE_METHODOLOGIQUE/Note_synthese_methodologique_v1_2.md
01_CADRE_METHODOLOGIQUE/Revision_de_fond_v0_1_temporalite.md
01_CADRE_METHODOLOGIQUE/Fiche_criblage_critiques_v0_1.md
05_CARTES_ET_SYNTHESES/Index_raisonne_du_corpus_v1_0.md
```

La v1.3 ne propose pas une nouvelle physique.

Elle corrige l'ordre des questions.

Formule de la correction :

```text
avant de demander a quelle famille appartient une grandeur,
il faut demander quelle forme de stabilisation elle prend,
dans quel regime elle opere,
par quel acces elle est connue,
et quelle trajectoire de stabilisation elle suit.
```

### 2. Definition directrice enrichie

Definition v1.3 :

> Une constante effective stabilisee est une grandeur dont une valeur, une forme, une relation, un role ou une dependance devient robuste dans un regime donne, selon un acces determine, avec un mode et une trajectoire de stabilisation explicites, sans que cette robustesse implique necessairement une constance absolue, une universalite hors contexte ou un statut fondamental.

Formule courte conservee :

```text
constance = robustesse fonctionnelle situee
```

Formule enrichie :

```text
constance effective stabilisee =
forme stabilisee
+ fonction principale
+ role contextuel
+ regime physique
+ regime d'acces
+ architecture eventuelle
+ trajectoire temporelle.
```

### 3. Difference entre v1.2 et v1.3

| Point | v1.2 | v1.3 |
|---|---|---|
| Premiere question | Quelle famille ? | Quelle forme logique de stabilisation ? |
| Relation | Famille superieure conservee mais surveillee | Famille faible sous audit, jamais reponse par defaut |
| Fonctions transversales / architecturales | Deux niveaux distincts | Roles contextuels avec portee locale, transversale ou architecturale |
| Regime physique / acces | Deux champs obligatoires | Deux axes orthogonaux, avec couplage modele-acces |
| Architecture | Niveau reconnu par matrice | Reseau de solidarite soumis a stress test |
| Stabilisation | Mode de robustesse | Mode + trajectoire |
| Temporalite | Implicite ou annexe | Axe methodologique transversal |
| Tensions | Proprietes du regime d'acces | Proprietes d'acces pouvant devenir signaux de test de validite |

Decision :

```text
la v1.3 ne remplace pas les garde-fous de la v1.2 ;
elle les deplace dans un ordre plus robuste.
```

### 4. Table des rangs v1.3

La methode distingue maintenant six rangs.

| Rang | Nom | Question |
|---|---|---|
| 0 | Forme logique de stabilisation | Qu'est-ce qui est stabilise formellement ? |
| 1 | Famille fonctionnelle | Que fait principalement la grandeur dans ce regime ? |
| 2 | Role contextuel | Quel role local, transversal ou architectural joue-t-elle ? |
| 3 | Axes physique / acces | Dans quel regime opere-t-elle et par quel acces est-elle connue ? |
| 4 | Architecture / reseau | Quelles dependances solidaires produit-elle ? |
| 5 | Temporalite / trajectoire | Comment son statut s'installe, varie, persiste ou se transforme ? |

Regle :

```text
un rang ne supprime pas les autres ;
il interdit seulement de poser trop tot la mauvaise question.
```

### 5. Rang 0 : forme logique de stabilisation

Le rang 0 est ajoute avant les familles.

Question :

```text
quelle forme prend ce qui est stabilise ?
```

Il ne classe pas encore la fonction physique.

Il identifie la forme logique du stable.

| Forme logique | Question locale | Exemples |
|---|---|---|
| Valeur | Une valeur numerique est-elle stabilisee ? | c, h, e, masses |
| Rapport | Un rapport est-il stabilise ? | m_p / m_e, Omega_i |
| Ecart | Un ecart spectral est-il stabilise ? | Delta m^2 |
| Composition | Une composition exacte ou derivee est-elle stabilisee ? | R = N_A k_B, K_J = 2e/h |
| Equation ou relation d'etat | Une relation fonctionnelle de comportement est-elle stabilisee ? | w |
| Fonction d'echelle | Une dependance a Q, E ou a un schema est-elle stabilisee ? | alpha_s(Q^2), alpha_G(E) |
| Matrice | Une structure matricielle est-elle stabilisee ? | CKM, PMNS, Yukawa |
| Phase | Une phase ou orientation complexe est-elle stabilisee ou contrainte ? | delta_CP, phases de Majorana |
| Projection | Une grandeur accessible par projection est-elle stabilisee ? | masses neutrino selon acces |
| Observable reconstruite | Une grandeur reconstruite est-elle stabilisee ? | sigma_8, S_8 |
| Condition initiale | Une condition d'entree d'un modele est-elle stabilisee ? | A_s, n_s |
| Convention definissante | Une valeur est-elle fixee par definition ? | k_B, N_A, h, e |
| Borne | Une limite sans detection positive est-elle stabilisee ? | masses absolues neutrino, certains parametres ouverts |

Regle :

```text
deux grandeurs ayant la meme forme logique peuvent avoir des fonctions differentes.
```

Exemples :

```text
Omega_i et m_p / m_e sont tous deux des rapports,
mais ils ne jouent pas le meme role.

CKM et PMNS sont toutes deux des matrices,
mais leurs manifestations phenomenologiques different.

k_B et h sont des valeurs exactes dans le SI,
mais leur role physique n'est pas epuise par cette exactitude.
```

### 6. Rang 1 : familles fonctionnelles

Les familles repondent a une autre question.

```text
que fait principalement la grandeur dans le regime considere ?
```

Le noyau v1.3 distingue cinq familles fortes et une famille sous audit.

Familles fortes :

```text
Couplage
Echelle
Raccordement
Orientation
Convention
```

Famille sous audit :

```text
Relation
```

Cette decision ne supprime pas encore Relation.

Elle empeche son usage comme reponse par defaut.

### 7. Statut de Relation en v1.3

La critique principale est acceptee :

```text
toute constante est relationnelle d'une certaine maniere.
```

Donc :

```text
Relation ne peut pas etre une famille ordinaire si elle signifie seulement "mettre en rapport".
```

Decision v1.3 :

```text
Relation devient une famille faible sous audit.
```

Elle ne peut etre utilisee que si trois conditions sont remplies.

```text
1. La liaison stabilisee est l'objet principal de la grandeur.
2. Cette liaison ne se reduit pas a une simple forme logique du rang 0.
3. Elle ne se decrit pas mieux comme role contextuel, fonction architecturale ou architecture.
```

Interdit :

```text
classer une grandeur dans Relation seulement parce qu'elle est un rapport,
un ecart,
une composition,
une equation,
ou une normalisation.
```

Exemples a re-tester :

| Cas | Rang 0 | Decision v1.3 |
|---|---|---|
| R = N_A k_B | Composition exacte | Convention SI + composition, pas Relation par defaut |
| Delta m^2 | Ecart spectral | Dynamique de phase / dephasage oscillatoire a tester |
| Omega_i | Rapport normalise | Densite normalisee dans architecture cosmologique |
| w | Equation ou relation d'etat | Role contextuel d'etat cosmologique |
| m_f = y_f v / sqrt(2) | Relation constitutive | Architecture Saveur-Higgs, masse stabilisee de regime |
| m_p / m_e | Rapport stratifie | Hierarchie d'echelles ou relation stratifiee a tester |

Formule :

```text
Relation cesse d'etre une case ;
elle devient une question de decomposition.
```

### 8. Rang 2 : role contextuel

La v1.3 ne supprime pas les anciennes fonctions transversales et architecturales.

Elle les regroupe sous une categorie plus generale :

```text
role contextuel
```

Chaque role contextuel doit avoir une portee.

Portee possible :

```text
locale
transversale
architecturale
documentaire
```

Exemples :

| Ancien statut | Role contextuel v1.3 | Portee |
|---|---|---|
| Seuil | Passage, limite ou ancrage | Transversale |
| Borne | Acces par limite sans detection positive | Transversale / acces |
| Validite | Domaine ou une description reste applicable | Transversale ou architecturale |
| Dephasage | Manifestation dynamique d'un ecart spectral | Locale ou transversale |
| Hierarchie | Ordre d'echelles ou d'intensites | Transversale |
| Fond | Terme ou condition globale de dynamique | Architecturale |
| Parametre d'etat | Etat d'un systeme dans un modele | Architecturale |
| Densite normalisee | Repartition relative dans un modele | Architecturale |
| Relation d'etat | Comportement d'une composante | Architecturale |
| Condition initiale | Donnee d'entree d'une evolution | Architecturale |
| Observable reconstruite | Grandeur inferee par modele et acces | Architecturale |
| Realisation pratique | Mise en oeuvre d'une definition | Architecturale locale SI |

Regle :

```text
le role contextuel ne remplace pas la famille ;
il dit comment la fonction principale opere dans un contexte.
```

### 9. Rang 3 : axes physique et acces

La v1.3 conserve la distinction :

```text
regime physique
regime d'acces
```

Mais elle ajoute une precision.

Ces deux axes sont orthogonaux.

Ils ne doivent etre :

```text
ni confondus,
ni separes comme s'ils etaient independants.
```

Nouveau champ :

```text
couplage modele-acces
```

Question :

```text
quel modele, schema, convention ou protocole transforme ce qui devient accessible ?
```

Exemples :

```text
sigma_8 et S_8 : donnees de structure + modele cosmologique + corrections.
H_0 : routes locales, CMB + modele, BAO + calibration.
A_s : acces CMB couple a tau et au modele primordial.
k_B : role thermodynamique + definition SI + realisations pratiques.
alpha_s(M_Z) : extractions multi-processus + evolution RG.
```

Nouveau champ associe :

```text
robustesse de l'acces
```

Types :

```text
directe
indirecte
reconstruite
combinee
bornee
fragile
conventionnelle
en tension
```

### 10. Rang 4 : architecture comme reseau

La v1.2 reconnaissait les architectures.

La v1.3 les soumet a un stress test.

Definition conservee :

```text
une architecture inter-familles est une solidarite de fonctions dans un regime,
non une nouvelle famille.
```

Precision v1.3 :

```text
une architecture doit dire quel type de solidarite elle revendique.
```

Types de solidarite :

| Type | Question | Exemple |
|---|---|---|
| Constitutive | Les grandeurs constituent-elles ensemble un secteur ? | Saveur-Higgs |
| Definitionnelle | Les grandeurs fixent-elles un systeme de definitions ? | Metrologique SI |
| De validite | Les grandeurs definissent-elles un domaine de description ? | Effective basse energie |
| Inferentielle | Les grandeurs sont-elles stabilisees par un reseau de modeles et d'acces ? | Cosmologie |
| Reconstructive | Les grandeurs sont-elles inferees par des routes multiples ? | sigma_8 / S_8, H_0 |
| Operationnelle | Les grandeurs rendent-elles une pratique de mesure possible ? | Realisations SI |

Stress test d'architecture :

```text
1. Quel type de solidarite est revendique ?
2. Quelles grandeurs sont necessaires ?
3. Que devient chaque grandeur si l'une des autres est retiree ?
4. La solidarite est-elle physique, definitionnelle, inferentielle, operationnelle ou documentaire ?
5. L'acces commun suffit-il vraiment a etablir une architecture ?
6. Faut-il eclater l'architecture en sous-architectures ?
7. La tension interne signale-t-elle une fragilite d'acces ou une rupture de validite possible ?
```

Sorties possibles :

```text
architecture confirmee
architecture locale
architecture eclatee
architecture de reconstruction
simple regroupement documentaire
```

### 11. Rang 5 : temporalite et trajectoire

La temporalite reste un axe transversal.

Elle ne devient pas une famille.

Elle ne devient pas une architecture.

Elle repond a :

```text
comment la grandeur entre-t-elle dans son statut,
comment ce statut persiste-t-il,
comment varie-t-il,
comment devient-il accessible,
et comment se transforme-t-il ?
```

Les cinq temporalites conservees sont :

```text
constitution
variation ou flot
transition ou validite
acces et inference
maturation methodologique
```

La v1.3 ajoute le terme :

```text
trajectoire de stabilisation
```

Exemples :

| Trajectoire | Sens |
|---|---|
| Convergence empirique | Plusieurs acces se rapprochent |
| Divergence inter-acces | Les acces restent discordants |
| Stabilisation bornee | La grandeur reste connue par limites |
| Reconstruction modele-dependante | La grandeur est stabilisee par inference |
| Absorption conventionnelle | La valeur devient definissante dans un systeme |
| Blocage par degenerescence | La stabilisation depend d'autres parametres non resolus |
| Tension candidate a rupture | La tension teste la validite du modele ou de l'architecture |

Exemples :

```text
k_B : stabilisation empirique historique -> absorption conventionnelle SI.
H_0 : forte stabilisation locale + divergence inter-acces.
delta_CP : stabilisation partielle, bloquee par hierarchie et donnees.
sigma_8 / S_8 : reconstruction modele-dependante, tension inter-acces.
alpha_s(Q^2) : dependance d'echelle controlee, non instabilite.
```

### 12. Tensions de donnees en v1.3

La v1.2 disait :

```text
Tension = propriete d'acces, non categorie taxonomique.
```

La v1.3 conserve cette prudence.

Mais elle ajoute :

```text
une tension persistante peut devenir un signal actif pour tester la validite d'une architecture.
```

Niveaux de tension :

| Niveau | Sens |
|---|---|
| Locale | Tension dans un sous-ensemble d'acces |
| Inter-acces | Tension entre routes independantes |
| Persistante | Tension robuste a plusieurs analyses |
| Modele-dependante | Tension sensible au modele d'inference |
| Candidate a rupture | Tension qui impose un stress test de validite |

Regle :

```text
aucune tension ne reclassifie automatiquement une grandeur.
```

Mais :

```text
une tension persistante oblige a documenter le stress test correspondant.
```

### 13. Manifestation phenomenologique

La v1.3 ajoute un champ :

```text
manifestation phenomenologique
```

Question :

```text
comment la grandeur se manifeste-t-elle dans les phenomenes accessibles ?
```

Exemples :

```text
CKM : orientation de saveur a manifestation transitionnelle.
PMNS : orientation de saveur a manifestation oscillatoire.
Delta m^2 : ecart spectral a manifestation dephasante.
G_F : raccordement effectif manifeste dans la desintegration du muon.
Lambda_QCD : echelle dynamique manifeste dans le changement perturbatif / non perturbatif.
S_8 : observable reconstruite manifeste dans les donnees de structure.
```

Ce champ evite une confusion :

```text
deux grandeurs peuvent avoir une famille proche,
mais des manifestations phenomenologiques differentes.
```

### 14. Protocole de classement v1.3

Pour toute nouvelle fiche, appliquer l'ordre suivant.

```text
1. Identifier la grandeur exacte.
2. Identifier la forme logique de stabilisation.
3. Identifier le regime physique pertinent.
4. Identifier le regime d'acces.
5. Identifier le couplage modele-acces.
6. Determiner la famille fonctionnelle principale.
7. Verifier si Relation est vraiment necessaire ou seulement apparente.
8. Ajouter les roles contextuels avec leur portee.
9. Decrire la manifestation phenomenologique.
10. Decrire le mode et la trajectoire de stabilisation.
11. Tester l'existence d'une architecture ou d'un reseau de dependance.
12. Appliquer le stress test d'architecture si necessaire.
13. Identifier les tensions et leur niveau d'activation.
14. Nommer les limites et les erreurs evitees.
```

Regle de priorite :

```text
la forme logique vient avant la famille,
mais la forme logique ne remplace pas la famille.
```

### 15. Matrice canonique v1.3

| Champ | Question |
|---|---|
| Grandeur | De quoi parle-t-on exactement ? |
| Forme logique | Valeur, rapport, ecart, composition, matrice, phase, observable, condition initiale ? |
| Variable eventuelle | t, z, Q, E, schema, convention, jeu de donnees ? |
| Regime physique | Dans quel domaine opere-t-elle ? |
| Regime d'acces | Comment est-elle connue ? |
| Couplage modele-acces | Quel modele, schema ou convention conditionne l'acces ? |
| Robustesse de l'acces | Directe, reconstruite, combinee, fragile, conventionnelle, en tension ? |
| Famille fonctionnelle | Que fait principalement la grandeur ? |
| Statut de Relation | Relation est-elle evitee, qualifiee ou vraiment necessaire ? |
| Role contextuel | Role local, transversal, architectural ou documentaire ? |
| Portee du role | Locale, transversale, architecturale, documentaire ? |
| Manifestation phenomenologique | Comment la grandeur se manifeste-t-elle ? |
| Mode de stabilisation | Empirique, bornee, reconstruite, conventionnelle, exacte par composition ? |
| Trajectoire de stabilisation | Convergence, divergence, absorption, blocage, reconstruction ? |
| Tension eventuelle | Passive, inter-acces, persistante, candidate a rupture ? |
| Architecture eventuelle | Quelle solidarite specifiee ? |
| Test de retrait | Que perd-on si cette grandeur est retiree ? |
| Limites | Ce que la grandeur ne dit pas |
| Erreur evitee | Quelle confusion de rang, d'acces ou de temps est evitee ? |

### 16. Test de resistance des familles

Avant de creer ou maintenir une famille, poser huit questions.

```text
1. La categorie nomme-t-elle une fonction principale ?
2. Cette fonction est-elle irreductible a une forme logique ?
3. Est-elle irreductible a un role contextuel ?
4. Est-elle irreductible a une architecture ?
5. Peut-elle classer plusieurs cas heterogenes sans les ecraser ?
6. Peut-on donner un contre-exemple qui la ferait devenir fourre-tout ?
7. Que perd-on si on la supprime ?
8. Que gagne-t-on si on la retrograde ?
```

Sorties possibles :

```text
famille conservee
famille renommee
famille sous audit
role contextuel
forme logique
architecture
archive taxonomique
```

### 17. Consequences pour les familles existantes

#### 17.1 Couplage

Statut :

```text
famille forte conservee.
```

Question :

```text
la grandeur parametre-t-elle une intensite, une interaction ou une texture de couplage ?
```

Ajouts v1.3 :

```text
preciser la variable d'echelle si le couplage court ;
preciser le regime ou la texture est definissable ;
preciser la trajectoire de stabilisation.
```

#### 17.2 Echelle

Statut :

```text
famille forte conservee.
```

Question :

```text
la grandeur fixe-t-elle, revele-t-elle ou hierarchise-t-elle un ordre de grandeur structurant ?
```

Ajouts v1.3 :

```text
distinguer echelle physique, seuil, validite et hierarchie.
```

#### 17.3 Raccordement

Statut :

```text
famille forte conservee.
```

Question :

```text
la grandeur relie-t-elle deux descriptions, deux niveaux ou une theorie effective a une structure plus complete ?
```

Ajouts v1.3 :

```text
specifier la limite de validite et le test de retrait.
```

#### 17.4 Orientation

Statut :

```text
famille forte conservee.
```

Question :

```text
la grandeur stabilise-t-elle un desalignement entre bases, champs, etats ou secteurs ?
```

Ajouts v1.3 :

```text
specifier la manifestation phenomenologique :
transitionnelle, oscillatoire, CP, geometrique, spectrale.
```

#### 17.5 Convention

Statut :

```text
famille forte conservee.
```

Question :

```text
la grandeur fixe-t-elle une valeur dans un systeme de definition ou d'unites ?
```

Ajouts v1.3 :

```text
distinguer valeur definissante,
realisation pratique,
role physique conserve,
et stabilisation absorbee par convention.
```

#### 17.6 Relation

Statut :

```text
famille faible sous audit.
```

Question :

```text
la liaison stabilisee est-elle vraiment la fonction principale,
ou seulement la forme logique du cas ?
```

Ajout v1.3 :

```text
toute occurrence de Relation doit etre accompagnee d'un test de non-reduction.
```

### 18. Consequences pour les architectures

Les quatre architectures restent reconnues, mais leur statut est precise.

| Architecture | Statut v1.3 | Point a renforcer |
|---|---|---|
| Saveur-Higgs | Confirmee, note Markdown active produite | Reseau de dependance a representer |
| Metrologique SI | Confirmee | Trajectoire de stabilisation absorbee par convention |
| Effective basse energie | Confirmee | Reseaux de validite, transitions et tests de retrait |
| Cosmologique | Macro-architecture confirmee par stress test | Sous-reseaux internes et couplage modele-acces |

Decision :

```text
aucune architecture n'est supprimee en v1.3,
mais toute architecture peut etre re-testee.
```

### 19. Chantiers ouverts apres v1.3

La v1.3 ouvre plusieurs chantiers prioritaires.

Les premiers chantiers sont maintenant produits :

```text
matrice de criblage taxonomique,
note d'architecture Saveur-Higgs,
carte des dependances architecturales,
stress test cosmologique,
reprise des cycles physiques,
audit de resynchronisation theorique.
```

#### 19.1 Matrice de criblage taxonomique

Document produit :

```text
01_CADRE_METHODOLOGIQUE/Matrice_criblage_taxonomique_v0_1.md
```

Role :

```text
formaliser le test de resistance des familles,
le statut de Relation,
et le stress test d'architecture.
```

Statut :

```text
protocole actif pour les nouvelles fiches et les cas litigieux.
```

#### 19.2 Note d'architecture Saveur-Higgs

Document produit :

```text
04_ARCHITECTURES_INTER_FAMILLES/Architecture_saveur_Higgs_notes.md
```

Role :

```text
mettre l'architecture constitutive au meme format que les autres architectures.
```

Statut :

```text
consolidation active integree dans la carte v1.2.
```

#### 19.3 Carte de dependances architecturales

Document produit :

```text
05_CARTES_ET_SYNTHESES/Carte_dependances_architectures_v0_1.md
```

Role :

```text
representer les architectures comme reseaux de dependance,
non seulement comme tableaux.
```

Statut :

```text
consolidation active integree dans la carte v1.2.
```

#### 19.4 Carte consolidee de refonte

Document produit :

```text
05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_2_refonte.md
```

Role :

```text
integrer la methode v1.3,
la matrice de criblage,
les architectures actives,
et la carte des dependances.
```

#### 19.5 Stress test cosmologique

Document produit :

```text
04_ARCHITECTURES_INTER_FAMILLES/Architecture_cosmologique_stress_test_v0_1.md
```

Role :

```text
tester si l'architecture cosmologique doit rester unique
ou etre decomposee en sous-architectures :
primordiale, tardive, reconstruction, tensions.
```

Decision :

```text
macro-architecture conservee,
mais lue par sous-reseaux internes :
fond-expansion, budget, etat, primordial, croissance-reconstruction,
et tensions transversales.
```

#### 19.6 Workflow GitHub provisoire

Document produit :

```text
01_CADRE_METHODOLOGIQUE/Workflow_GitHub_v0_1.md
```

Role :

```text
encadrer le versionnement du corpus sans remplacer la methode theorique.
```

Regle :

```text
quand une etape conceptuelle est stabilisee,
signaler un point de decision et attendre validation ;
quand une etape documentaire ou technique est stabilisee,
committer et pousser peuvent etre delegues avec resume exact.
```

#### 19.7 Reprise des cycles physiques et audit transversal

Documents produits :

```text
02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/Synthese_cycle_saveur_Higgs_v0_1.md
05_CARTES_ET_SYNTHESES/Audit_resynchronisation_theorique_v0_1.md
```

Role :

```text
appliquer la methode v1.3 aux quatre cycles physiques actifs,
puis verifier la coherence theorique entre les architectures.
```

Statut :

```text
synchronisation documentaire active ;
les choix conceptuels nouveaux restent soumis a validation.
```

### 20. Documents integres

Documents methodologiques :

```text
01_CADRE_METHODOLOGIQUE/Note_synthese_methodologique_v1_1.md
01_CADRE_METHODOLOGIQUE/Note_synthese_methodologique_v1_2.md
01_CADRE_METHODOLOGIQUE/Revision_de_fond_v0_1_temporalite.md
01_CADRE_METHODOLOGIQUE/Fiche_criblage_critiques_v0_1.md
01_CADRE_METHODOLOGIQUE/Workflow_GitHub_v0_1.md
```

Documents de reference :

```text
05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_1.md
05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_2_refonte.md
05_CARTES_ET_SYNTHESES/Synthese_architectures_inter_familles_v1_0.md
05_CARTES_ET_SYNTHESES/Index_raisonne_du_corpus_v1_0.md
```

Documents produits en application de la v1.3 :

```text
01_CADRE_METHODOLOGIQUE/Matrice_criblage_taxonomique_v0_1.md
04_ARCHITECTURES_INTER_FAMILLES/Architecture_saveur_Higgs_notes.md
05_CARTES_ET_SYNTHESES/Carte_dependances_architectures_v0_1.md
05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_2_refonte.md
04_ARCHITECTURES_INTER_FAMILLES/Architecture_cosmologique_stress_test_v0_1.md
01_CADRE_METHODOLOGIQUE/Workflow_GitHub_v0_1.md
```

Architectures :

```text
04_ARCHITECTURES_INTER_FAMILLES/Architecture_saveur_Higgs_notes.md
04_ARCHITECTURES_INTER_FAMILLES/Architecture_effective_basse_energie_notes.md
04_ARCHITECTURES_INTER_FAMILLES/Architecture_cosmologique_notes.md
04_ARCHITECTURES_INTER_FAMILLES/Architecture_metrologique_SI_notes.md
```

Critiques source :

```text
90_Critiques_ constantes_effectives_stabilisees/
```

### 21. Formule de cloture

La v1.3 peut etre resumee par quatre deplacements.

```text
de la famille vers la forme logique ;
de la fonction isolee vers le role contextuel ;
du tableau vers le reseau de dependance ;
du statut fixe vers la trajectoire de stabilisation.
```

Formule finale :

> Une constante effective stabilisee n'est pas d'abord une case taxonomique ; c'est une forme stabilisee qui prend fonction dans un regime, devient accessible par un dispositif, s'inscrit parfois dans une architecture, et suit une trajectoire de stabilisation.
