# Index raisonne du corpus v1.0

## Navigation, statuts documentaires et ordre de lecture

### 1. Fonction de l'index

Cet index ne modifie pas la methode.

Il sert a rendre le corpus navigable apres :

```text
la carte consolidee v1.1
la synthese des architectures inter-familles v1.0
la note methodologique v1.2
la revision temporelle et le criblage critique
la note methodologique v1.3
la carte des dependances architecturales v0.1
la carte consolidee v1.2 de refonte
le workflow GitHub provisoire
```

Objectif :

```text
distinguer les documents actifs,
les documents de consolidation,
les cycles de preuve,
les notes d'architecture,
et les archives historiques.
```

L'index evite une confusion simple :

```text
tous les documents du dossier ne sont pas au meme rang.
```

### 2. Principe de lecture

Le corpus doit etre lu par couches.

```text
1. Brief et documents fondateurs.
2. Methode active.
3. Carte de reference.
4. Syntheses transversales.
5. Notes d'architecture.
6. Cycles physiques.
7. Archives historiques.
```

Regle :

```text
un document plus recent ne rend pas toujours inutile un document ancien,
mais il peut en corriger le rang, le vocabulaire ou la fonction.
```

### 3. Statuts documentaires

L'index utilise six statuts.

| Statut | Sens | Usage |
|---|---|---|
| Reference active | Document a utiliser en priorite | Methode, carte, synthese transverse |
| Protocole actif | Document d'application reutilisable | Matrices de criblage, tests de resistance |
| Consolidation | Document qui stabilise un cycle ou une architecture | Notes d'architecture, syntheses de cycles |
| Preuve locale | Fiche ou cycle qui justifie une decision | Fiches physiques detaillees |
| Archive historique | Document utile pour comprendre l'evolution | Anciennes cartes, anciens tests, fichiers Word racine |
| A produire | Document utile mais non encore cree | Lacunes identifiees |

### 4. Documents de reference active

Ces documents forment le noyau actif du corpus.

| Document | Statut | Role |
|---|---|---|
| `01_CADRE_METHODOLOGIQUE/Note_synthese_methodologique_v1_3_pre_familial_et_temporalite.md` | Reference active | Methode actuelle : rang pre-familial, roles contextuels, temporalite |
| `01_CADRE_METHODOLOGIQUE/Workflow_GitHub_v0_1.md` | Protocole actif | Versionnement prudent du corpus |
| `05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_2_refonte.md` | Reference active | Carte generale actuelle apres refonte v1.3 |
| `05_CARTES_ET_SYNTHESES/Synthese_architectures_inter_familles_v1_0.md` | Reference active | Comparaison des quatre architectures |
| `05_CARTES_ET_SYNTHESES/Carte_dependances_architectures_v0_1.md` | Consolidation active | Reseaux de dependance entre architectures |
| `05_CARTES_ET_SYNTHESES/Index_raisonne_du_corpus_v1_0.md` | Reference active | Navigation et statut des documents |

Ordre recommande :

```text
Note_synthese_methodologique_v1_3_pre_familial_et_temporalite.md
Matrice_criblage_taxonomique_v0_1.md
Workflow_GitHub_v0_1.md
Synthese_architectures_inter_familles_v1_0.md
Carte_dependances_architectures_v0_1.md
Carte_consolidee_v1_2_refonte.md
Index_raisonne_du_corpus_v1_0.md
```

### 5. Documents methodologiques

| Document | Statut | Role |
|---|---|---|
| `01_CADRE_METHODOLOGIQUE/Note_synthese_methodologique_v1_3_pre_familial_et_temporalite.md` | Reference active | Methode actuelle apres criblage : rang 0, roles contextuels, temporalite |
| `01_CADRE_METHODOLOGIQUE/Matrice_criblage_taxonomique_v0_1.md` | Protocole actif | Application operationnelle de la methode v1.3 aux cas litigieux |
| `01_CADRE_METHODOLOGIQUE/Workflow_GitHub_v0_1.md` | Protocole actif | Regle de commit, push et branches apres stabilisation documentaire |
| `01_CADRE_METHODOLOGIQUE/Note_synthese_methodologique_v1_2.md` | Consolidation historique | Methode avant rang pre-familial et temporalite explicite |
| `01_CADRE_METHODOLOGIQUE/Fiche_criblage_critiques_v0_1.md` | Revision active | Extraction et recoupement des huit critiques constructives |
| `01_CADRE_METHODOLOGIQUE/Revision_de_fond_v0_1_temporalite.md` | Revision active | Reorganisation de fond autour de la temporalite |
| `01_CADRE_METHODOLOGIQUE/Note_synthese_methodologique_v1_1.md` | Consolidation historique | Socle methodologique precedent |
| `01_CADRE_METHODOLOGIQUE/Mise_a_jour_methodologie_v1_1_notes.md` | Archive de consolidation | Notes preparatoires de la v1.1 |

Decision :

```text
pour toute nouvelle fiche, partir de la v1.3.
```

Pour comprendre la refonte de la methode, lire aussi :

```text
01_CADRE_METHODOLOGIQUE/Note_synthese_methodologique_v1_2.md
01_CADRE_METHODOLOGIQUE/Fiche_criblage_critiques_v0_1.md
01_CADRE_METHODOLOGIQUE/Revision_de_fond_v0_1_temporalite.md
```

La v1.1 reste utile pour comprendre la transition vers :

```text
regime d'acces
architecture inter-familles
extension SI
```

### 6. Cartes et syntheses generales

| Document | Statut | Role |
|---|---|---|
| `05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_2_refonte.md` | Reference active | Carte generale actuelle apres methode v1.3 |
| `05_CARTES_ET_SYNTHESES/Synthese_architectures_inter_familles_v1_0.md` | Reference active | Synthese transverse des architectures |
| `05_CARTES_ET_SYNTHESES/Carte_dependances_architectures_v0_1.md` | Consolidation active | Representation des architectures comme reseaux de dependance |
| `05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_1.md` | Consolidation historique | Carte avant rang pre-familial et refonte de Relation |
| `05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_0.md` | Archive de consolidation | Etape avant extension SI |
| `05_CARTES_ET_SYNTHESES/Carte_consolidee_v0_9.md` | Archive de consolidation | Etape avant cosmologie et SI consolidees |

Decision :

```text
Carte_consolidee_v1_2_refonte.md remplace la v1.1 comme carte de reference active.
```

Les cartes anterieures restent utiles pour retracer les decisions.

### 7. Architectures inter-familles

Le corpus stabilise quatre architectures.

| Architecture | Forme | Document principal | Statut |
|---|---|---|---|
| Saveur-Higgs | Constitutive | `04_ARCHITECTURES_INTER_FAMILLES/Architecture_saveur_Higgs_notes.md` | Consolidation active |
| Metrologique SI | Definitionnelle | `04_ARCHITECTURES_INTER_FAMILLES/Architecture_metrologique_SI_notes.md` | Consolidation active |
| Effective basse energie | Validite | `04_ARCHITECTURES_INTER_FAMILLES/Architecture_effective_basse_energie_notes.md` | Consolidation active |
| Cosmologique | Inferentielle / reconstructive | `04_ARCHITECTURES_INTER_FAMILLES/Architecture_cosmologique_notes.md` + stress test v0.1 | Consolidation active avec sous-reseaux |

Regle de rang :

```text
une architecture inter-familles n'est pas une famille superieure.
```

Point documentaire :

```text
l'architecture Saveur-Higgs dispose maintenant d'une note Markdown active,
au meme rang documentaire que les autres architectures inter-familles.
```

Archive historique source :

```text
Note de consolidation saveur-Higgs v0.1.docx
```

La note Markdown doit etre lue en priorite ; le Word racine sert a retracer la genealogie.

### 8. Cycle effectif basse energie

Dossier :

```text
02_CYCLES_PHYSIQUES/06_Cycle_effectif_basse_energie/
```

Documents actifs :

| Document | Statut | Role |
|---|---|---|
| `02_CYCLES_PHYSIQUES/06_Cycle_effectif_basse_energie/Cycle_effectif_basse_energie_v0_4_alphaG_MPl.md` | Preuve locale | Cas gravitationnel effectif |
| `02_CYCLES_PHYSIQUES/06_Cycle_effectif_basse_energie/Synthese_cycle_effectif_basse_energie_v0_1.md` | Consolidation | Synthese du cycle |
| `04_ARCHITECTURES_INTER_FAMILLES/Architecture_effective_basse_energie_notes.md` | Consolidation active | Architecture issue du cycle |

Documents racine historiques associes :

```text
Cycle effectif basse energie v0.1 a v0.3
Fiches G_F, alpha_s / Lambda_QCD, alpha_G / M_Pl
```

Decision :

```text
pour comprendre l'architecture effective,
lire d'abord la synthese de cycle,
puis la note d'architecture.
```

### 9. Cycle cosmologique

Dossier :

```text
02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/
```

Documents actifs :

| Ordre | Document | Statut | Role |
|---|---|---|---|
| 1 | `02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Cycle_cosmologique_v0_1_cadrage.md` | Preuve locale | Cadrage prudent |
| 2 | `02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Cycle_cosmologique_v0_2_Lambda.md` | Preuve locale | Lambda |
| 3 | `02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Cycle_cosmologique_v0_3_H0.md` | Preuve locale | H_0 |
| 4 | `02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Cycle_cosmologique_v0_4_Omega_i.md` | Preuve locale | Omega_i |
| 5 | `02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Cycle_cosmologique_v0_5_w.md` | Preuve locale | w |
| 6 | `02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Cycle_cosmologique_v0_6_As_ns.md` | Preuve locale | A_s et n_s |
| 7 | `02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Cycle_cosmologique_v0_7_sigma8_S8.md` | Preuve locale | sigma_8 et S_8 |
| 8 | `02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Synthese_cycle_cosmologique_v0_1.md` | Consolidation | Synthese du cycle |
| 9 | `04_ARCHITECTURES_INTER_FAMILLES/Architecture_cosmologique_notes.md` | Consolidation active | Architecture issue du cycle |

Decision :

```text
pour une lecture rapide, lire la synthese du cycle et la note d'architecture.
pour verifier une decision locale, revenir a la fiche correspondante.
```

### 10. Cycle metrologique SI

Dossier :

```text
02_CYCLES_PHYSIQUES/08_Cycle_metrologique_SI/
```

Documents actifs :

| Document | Statut | Role |
|---|---|---|
| `02_CYCLES_PHYSIQUES/08_Cycle_metrologique_SI/Cycle_metrologique_SI_v0_1_c_h_e.md` | Preuve locale | Extension SI a c, h, e, K_J, R_K |
| `04_ARCHITECTURES_INTER_FAMILLES/Architecture_metrologique_SI_notes.md` | Consolidation active | Architecture SI etendue |

Documents racine historiques associes :

```text
Fiches k_B, N_A, R
```

Decision :

```text
la reference actuelle pour le SI est la note d'architecture metrologique,
avec le cycle c / h / e comme preuve locale recente.
```

### 11. Archives Word racine

Le dossier racine contient de nombreux fichiers Word anterieurs.

Ils doivent etre conserves comme :

```text
provenance historique
archives de cycles
fiches initiales
tests taxonomiques
anciennes cartes
```

Ils ne doivent pas etre traites comme la couche active de la methode.

Groupes principaux :

| Groupe | Role |
|---|---|
| Brief initial | Point de depart du projet |
| Methodes et addenda initiaux | Genese de la methode |
| Tests de familles | Exploration des familles fragiles |
| Fiches physiques initiales | Preuves locales anciennes |
| Syntheses de cycles initiales | Consolidations historiques |
| Cartes consolidees v0.1 a v0.8 | Evolution de la carte avant l'arborescence Markdown |

Regle de conservation :

```text
ne pas renommer ni deplacer les fichiers Word racine tant que les dependances internes ne sont pas verifiees.
```

Regle d'usage :

```text
si un document Markdown recent contredit ou precise un document Word ancien,
le document Markdown recent prime pour le travail actuel.
```

### 12. Ordre de lecture selon l'objectif

#### 12.1 Comprendre la methode actuelle

```text
01_CADRE_METHODOLOGIQUE/Note_synthese_methodologique_v1_3_pre_familial_et_temporalite.md
01_CADRE_METHODOLOGIQUE/Matrice_criblage_taxonomique_v0_1.md
05_CARTES_ET_SYNTHESES/Carte_dependances_architectures_v0_1.md
05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_2_refonte.md
05_CARTES_ET_SYNTHESES/Synthese_architectures_inter_familles_v1_0.md
```

#### 12.2 Comprendre les architectures

```text
05_CARTES_ET_SYNTHESES/Synthese_architectures_inter_familles_v1_0.md
04_ARCHITECTURES_INTER_FAMILLES/Architecture_saveur_Higgs_notes.md
04_ARCHITECTURES_INTER_FAMILLES/Architecture_metrologique_SI_notes.md
04_ARCHITECTURES_INTER_FAMILLES/Architecture_effective_basse_energie_notes.md
04_ARCHITECTURES_INTER_FAMILLES/Architecture_cosmologique_notes.md
```

Pour retracer la genealogie Saveur-Higgs :

```text
consulter ensuite la note Word racine de consolidation Saveur-Higgs.
```

#### 12.3 Verifier une decision physique locale

```text
chercher d'abord la synthese du cycle concerne,
puis revenir a la fiche locale.
```

Exemples :

```text
H_0 -> Synthese_cycle_cosmologique_v0_1.md puis Cycle_cosmologique_v0_3_H0.md
c / h / e -> Architecture_metrologique_SI_notes.md puis Cycle_metrologique_SI_v0_1_c_h_e.md
alpha_G / M_Pl -> Synthese_cycle_effectif_basse_energie_v0_1.md puis Cycle_effectif_basse_energie_v0_4_alphaG_MPl.md
```

#### 12.4 Retracer l'histoire du projet

```text
PROJECT_BRIEF.docx
documents Word racine
Carte_consolidee_v0_9.md
Carte_consolidee_v1_0.md
Carte_consolidee_v1_1.md
Note_synthese_methodologique_v1_1.md
Note_synthese_methodologique_v1_2.md
Revision_de_fond_v0_1_temporalite.md
Fiche_criblage_critiques_v0_1.md
Note_synthese_methodologique_v1_3_pre_familial_et_temporalite.md
Matrice_criblage_taxonomique_v0_1.md
Architecture_saveur_Higgs_notes.md
Carte_dependances_architectures_v0_1.md
Carte_consolidee_v1_2_refonte.md
Architecture_cosmologique_stress_test_v0_1.md
```

### 13. Dependances principales

Les dependances peuvent etre lues ainsi.

```text
PROJECT_BRIEF.docx
  -> documents Word racine
  -> Note_synthese_methodologique_v1_1.md
  -> Carte_consolidee_v0_9.md
  -> Carte_consolidee_v1_0.md
  -> cycles effectif / cosmologique / metrologique
  -> notes d'architecture
  -> Carte_consolidee_v1_1.md
  -> Synthese_architectures_inter_familles_v1_0.md
  -> Note_synthese_methodologique_v1_2.md
  -> Revision_de_fond_v0_1_temporalite.md
  -> Fiche_criblage_critiques_v0_1.md
  -> Note_synthese_methodologique_v1_3_pre_familial_et_temporalite.md
  -> Matrice_criblage_taxonomique_v0_1.md
  -> Architecture_saveur_Higgs_notes.md
  -> Carte_dependances_architectures_v0_1.md
  -> Carte_consolidee_v1_2_refonte.md
  -> Architecture_cosmologique_stress_test_v0_1.md
  -> Index_raisonne_du_corpus_v1_0.md
```

Lecture fonctionnelle :

```text
methode -> criblage -> architecture -> dependances -> carte consolidee -> stress test
```

### 14. Lacunes documentaires identifiees

Cet index fait apparaitre plusieurs lacunes possibles.

Depuis la revision de fond sur la temporalite et le criblage des critiques, la premiere lacune methodologique devient prioritaire.

#### 14.1 Methode v1.3 produite

La version methodologique active integrant explicitement les apports de la revision temporelle et du criblage critique est produite.

```text
le rang pre-familial de forme logique,
la refonte de Relation,
les roles contextuels,
les axes physique / acces,
la trajectoire de stabilisation,
et la temporalite.
```

Document produit :

```text
01_CADRE_METHODOLOGIQUE/Note_synthese_methodologique_v1_3_pre_familial_et_temporalite.md
```

Statut :

```text
reference active pour les nouvelles fiches.
```

Raison :

```text
les critiques montrent que la methode doit changer l'ordre des questions :
forme logique avant famille,
fonction avant role,
acces et modele comme axes orthogonaux,
temporalite comme trajectoire.
```

Documents d'application produits ensuite :

```text
01_CADRE_METHODOLOGIQUE/Matrice_criblage_taxonomique_v0_1.md
05_CARTES_ET_SYNTHESES/Carte_dependances_architectures_v0_1.md
05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_2_refonte.md
04_ARCHITECTURES_INTER_FAMILLES/Architecture_cosmologique_stress_test_v0_1.md
```

Stress test cosmologique produit :

```text
04_ARCHITECTURES_INTER_FAMILLES/Architecture_cosmologique_stress_test_v0_1.md
```

#### 14.2 Note Markdown Saveur-Higgs produite

La note Markdown dediee est produite :

```text
04_ARCHITECTURES_INTER_FAMILLES/Architecture_saveur_Higgs_notes.md
```

Statut :

```text
consolidation active,
integree dans la carte consolidee v1.2.
```

Raison :

```text
Saveur-Higgs etait deja traite dans les archives Word, la carte v1.1 et la synthese transverse.
La note Markdown leve l'asymetrie documentaire entre les quatre architectures actives.
```

#### 14.3 README de dossier

Il pourrait etre utile d'ajouter un README minimal au dossier racine.

Forme possible :

```text
README.md
```

Role :

```text
renvoyer vers l'index raisonne,
la note methodologique v1.3,
et la carte consolidee v1.1.
```

Statut :

```text
utile si le corpus doit etre partage ou relu hors de cette conversation.
```

#### 14.4 Normalisation future des archives

Une normalisation des noms de fichiers Word pourrait etre envisagee plus tard.

Statut :

```text
a ne pas faire maintenant.
```

Raison :

```text
les dependances internes et citations croisees ne sont pas encore auditees.
```

### 15. Regles pour les prochaines etapes

Avant d'ouvrir un nouveau cycle physique :

```text
1. Verifier si la question releve deja d'une architecture stabilisee.
2. Lire la note methodologique v1.3.
3. Appliquer la matrice de criblage si le classement est litigieux.
4. Lire la carte v1.1.
5. Identifier le cycle ou la fiche de preuve la plus proche.
6. Ne creer une nouvelle famille que si le test de resistance et le test d'architecture echouent.
```

Avant de produire une nouvelle synthese :

```text
1. Dire quels documents elle integre.
2. Dire quel rang elle stabilise.
3. Dire quels documents elle remplace ou prolonge.
4. Dire quelles limites elle conserve.
```

Avant de deplacer ou renommer un fichier :

```text
1. Inventorier les references internes.
2. Distinguer les fichiers actifs des archives.
3. Creer une table de correspondance.
4. Ne rien deplacer sans raison documentaire explicite.
```

### 16. Carte active du corpus

La carte active du corpus peut etre resumee ainsi.

```text
Methode active :
01_CADRE_METHODOLOGIQUE/Note_synthese_methodologique_v1_3_pre_familial_et_temporalite.md

Methode historique recente :
01_CADRE_METHODOLOGIQUE/Note_synthese_methodologique_v1_2.md

Protocole actif :
01_CADRE_METHODOLOGIQUE/Matrice_criblage_taxonomique_v0_1.md
01_CADRE_METHODOLOGIQUE/Workflow_GitHub_v0_1.md

Carte active :
05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_2_refonte.md

Carte historique recente :
05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_1.md

Carte de dependances active :
05_CARTES_ET_SYNTHESES/Carte_dependances_architectures_v0_1.md

Synthese transverse active :
05_CARTES_ET_SYNTHESES/Synthese_architectures_inter_familles_v1_0.md

Index actif :
05_CARTES_ET_SYNTHESES/Index_raisonne_du_corpus_v1_0.md

Revision active :
01_CADRE_METHODOLOGIQUE/Revision_de_fond_v0_1_temporalite.md
01_CADRE_METHODOLOGIQUE/Fiche_criblage_critiques_v0_1.md

Architectures actives :
04_ARCHITECTURES_INTER_FAMILLES/Architecture_saveur_Higgs_notes.md
04_ARCHITECTURES_INTER_FAMILLES/Architecture_metrologique_SI_notes.md
04_ARCHITECTURES_INTER_FAMILLES/Architecture_effective_basse_energie_notes.md
04_ARCHITECTURES_INTER_FAMILLES/Architecture_cosmologique_notes.md
04_ARCHITECTURES_INTER_FAMILLES/Architecture_cosmologique_stress_test_v0_1.md

Cycles actifs :
02_CYCLES_PHYSIQUES/06_Cycle_effectif_basse_energie/
02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/
02_CYCLES_PHYSIQUES/08_Cycle_metrologique_SI/
```

### 17. Formule de cloture

L'index peut etre resume par trois regles.

```text
la methode donne les criteres
la carte donne l'etat consolide
les cycles et architectures donnent les preuves
```

Formule finale :

> Un corpus robuste n'est pas seulement une accumulation de notes ; c'est une hierarchie lisible de statuts, de preuves et de syntheses.
