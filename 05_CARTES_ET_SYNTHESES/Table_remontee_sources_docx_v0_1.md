# Table de remontee des sources DOCX v0.1

## Sources primaires, sorties Markdown et rattachements actifs

### 1. Fonction

Cette table execute le plan de remontee des sources DOCX.

Elle ne deplace aucun fichier.

Elle pilote les extractions, ouvertes ensuite lot par lot.

Elle fixe :

```text
les sources primaires a relire,
le lot de traitement,
la sortie Markdown cible,
le document actif concerne,
et le controle theorique attendu.
```

### 2. Regle de nommage

Les noms de sources sont transcrits ici en ASCII pour la lisibilite du corpus.

Cela ne renomme pas les fichiers physiques.

Regle :

```text
le nom physique DOCX reste inchange ;
le nom Markdown cible utilise un slug ASCII stable.
```

Format cible :

```text
Source_docx_<slug_ascii>_v0_1.md
```

### 3. Statuts de traitement

| Statut | Sens |
|---|---|
| P0 | Source structurante a remonter avant toute reprise theorique large |
| P1 | Source physique ou architecturale a remonter avant le cercle 2 |
| P2 | Source genealogique a remonter apres les sources structurantes |
| P3 | Source deja criblee ou critique, a reconnecter apres les lots centraux |

Types de controle :

| Controle | Sens |
|---|---|
| Extraction | Produire un Markdown de travail depuis la source |
| Comparaison | Comparer la source a un Markdown actif deja produit |
| Dedoublonnage | Comparer deux versions proches avant integration |
| Rattachement | Verifier si le rattachement genetique reste le bon rattachement theorique |
| Genealogie | Conserver l'histoire des deplacements conceptuels sans la rendre active par defaut |

### 4. Lot 0 : socle methodologique

Destination de principe :

```text
01_CADRE_METHODOLOGIQUE/00_Sources_docx/
```

Etat :

```text
ouvert ;
extractions Markdown produites ;
synthese de recuperation produite :
01_CADRE_METHODOLOGIQUE/Synthese_recuperation_lot0_socle_methodologique_v0_1.md
```

| Source primaire | Sortie Markdown cible | Document actif concerne | Priorite | Controle |
|---|---|---|---|---|
| PROJECT_BRIEF.docx | `01_CADRE_METHODOLOGIQUE/00_Sources_docx/Source_docx_PROJECT_BRIEF_v0_1.md` | Methode v1.3, carte v1.2, index | P0 | Extraction + comparaison |
| Methode v0.1.docx | `01_CADRE_METHODOLOGIQUE/00_Sources_docx/Source_docx_Methode_v0_1.md` | Methode v1.3, matrice de criblage | P0 | Extraction + genealogie |
| Regimes de constance.docx | `01_CADRE_METHODOLOGIQUE/00_Sources_docx/Source_docx_Regimes_de_constance_v0_1.md` | Methode v1.3, matrice temporelle | P0 | Extraction + comparaison |
| Note de synthese methodologique.docx | `01_CADRE_METHODOLOGIQUE/00_Sources_docx/Source_docx_Note_synthese_methodologique_v0_1.md` | Notes methodologiques v1.1, v1.2, v1.3 | P0 | Extraction + genealogie |
| Addendum methodologique v0.2.docx | `01_CADRE_METHODOLOGIQUE/00_Sources_docx/Source_docx_Addendum_methodologique_v0_2.md` | Methode v1.3, revision de fond | P0 | Extraction + comparaison |
| Note critique de compression v0.1.docx | `01_CADRE_METHODOLOGIQUE/00_Sources_docx/Source_docx_Note_critique_compression_v0_1.md` | Refonte v1.2, audit de resynchronisation | P0 | Extraction + controle des pertes |

### 5. Lot 1A : couplages, echelles et QCD

Destination de principe :

```text
02_CYCLES_PHYSIQUES/01_Cycle_couplages_echelles_QCD/
```

Ce dossier est a produire si la remontee confirme que le cycle initial doit
exister comme couche Markdown autonome.

| Source primaire | Sortie Markdown cible | Document actif concerne | Priorite | Controle |
|---|---|---|---|---|
| Fiche alpha v0.1.docx | `02_CYCLES_PHYSIQUES/01_Cycle_couplages_echelles_QCD/Source_docx_Fiche_alpha_v0_1.md` | Architecture effective basse energie, carte v1.2 | P1 | Extraction + rattachement |
| Fiche masse de l'electron.docx | `02_CYCLES_PHYSIQUES/01_Cycle_couplages_echelles_QCD/Source_docx_Fiche_masse_electron_v0_1.md` | Architecture Saveur-Higgs, cycle source 01 | P1 | Rattachement a verifier |
| Fiche rapport proton-electron.docx | `02_CYCLES_PHYSIQUES/01_Cycle_couplages_echelles_QCD/Source_docx_Fiche_rapport_proton_electron_v0_1.md` | Architecture effective, possible interface metrologique | P1 | Extraction + rattachement |
| Fiche alpha_s - Lambda_QCD.docx | `02_CYCLES_PHYSIQUES/01_Cycle_couplages_echelles_QCD/Source_docx_Fiche_alpha_s_Lambda_QCD_v0_1.md` | Architecture effective basse energie | P1 | Extraction + comparaison |
| Synthese du premier cycle v0.1.docx | `02_CYCLES_PHYSIQUES/01_Cycle_couplages_echelles_QCD/Source_docx_Synthese_premier_cycle_v0_1.md` | Future synthese du cycle source 01 | P1 | Genealogie + comparaison |

Point de vigilance :

```text
le rattachement historique de la masse de l'electron au cycle 01 ne doit pas
masquer son role constitutif dans Saveur-Higgs.
```

### 6. Lot 1B : structuration electrofaible et cas limites

Destination de principe :

```text
02_CYCLES_PHYSIQUES/02_Cycle_structurant_electrofaible/
```

Ce dossier est a produire comme couche source, sans concurrencer le cycle
Saveur-Higgs actif.

| Source primaire | Sortie Markdown cible | Document actif concerne | Priorite | Controle |
|---|---|---|---|---|
| Fiche v v0.1.docx | `02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/Source_docx_Fiche_v_v0_1.md` | Cycle Saveur-Higgs, architecture Saveur-Higgs | P1 | Extraction + comparaison cible pre-Cercle 2 |
| Fiche Yukawa v0.1.docx | `02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/Source_docx_Fiche_Yukawa_v0_1.md` | Cycle Saveur-Higgs, architecture Saveur-Higgs | P1 | Extraction + comparaison cible pre-Cercle 2 |
| Fiche G_F v0.1.docx | `02_CYCLES_PHYSIQUES/02_Cycle_structurant_electrofaible/Source_docx_Fiche_G_F_v0_1.md` | Saveur-Higgs, effective basse energie | P1 | Rattachement double |
| Fiche theta_W v0.1.docx | `02_CYCLES_PHYSIQUES/02_Cycle_structurant_electrofaible/Source_docx_Fiche_theta_W_v0_1.md` | Saveur-Higgs, electroweak | P1 | Extraction |
| Fiche alpha_G - M_Pl.docx | `02_CYCLES_PHYSIQUES/06_Cycle_effectif_basse_energie/Source_docx_Fiche_alpha_G_M_Pl_A_v0_1.md` | Cycle effectif basse energie, interface cosmologie primordiale | P1 | Dedoublonnage cible pre-Cercle 2 |
| Fiche alpha_G - M_Pl (1).docx | `02_CYCLES_PHYSIQUES/06_Cycle_effectif_basse_energie/Source_docx_Fiche_alpha_G_M_Pl_B_v0_1.md` | Cycle effectif basse energie, interface cosmologie primordiale | P1 | Dedoublonnage cible pre-Cercle 2 |
| Fiche Lambda v0.1.docx | `02_CYCLES_PHYSIQUES/02_Cycle_structurant_electrofaible/Source_docx_Fiche_Lambda_v0_1.md` | Cycle cosmologique, fiche Lambda active | P1 | Rattachement genetique / cosmologique |
| Ecriture.txt | `02_CYCLES_PHYSIQUES/02_Cycle_structurant_electrofaible/Source_txt_Ecriture_Lambda_v0_1.md` | Cycle cosmologique, fiche Lambda active | P1 | Source auxiliaire a clarifier |
| Synthese du second cycle v0.1.docx | `02_CYCLES_PHYSIQUES/02_Cycle_structurant_electrofaible/Source_docx_Synthese_second_cycle_v0_1.md` | Saveur-Higgs, effective, cosmologie | P1 | Genealogie + comparaison |

Point de vigilance :

```text
Lambda est genetiquement present dans le second cycle,
mais son usage actif releve maintenant du cycle cosmologique.
```

Etat cible pre-Cercle 2 :

```text
Fiche v, Fiche Yukawa et le doublon alpha_G / M_Pl ont ete remontees
dans les cycles actifs qu'elles conditionnent directement.
Le reste du lot 1B demeure a traiter dans la remontee physique complete.
```

### 7. Lot 1C : neutrinos

Destination de principe :

```text
02_CYCLES_PHYSIQUES/03_Cycle_neutrinos/
```

Ce dossier est a produire comme couche source et comme interface vers
Saveur-Higgs et cosmologie.

| Source primaire | Sortie Markdown cible | Document actif concerne | Priorite | Controle |
|---|---|---|---|---|
| Fiche neutrinos v0.1.docx | `02_CYCLES_PHYSIQUES/03_Cycle_neutrinos/Source_docx_Fiche_neutrinos_v0_1.md` | Cycle Saveur-Higgs, fiche masse absolue neutrinos | P1 | Extraction + comparaison |
| Fiche Delta m2.docx | `02_CYCLES_PHYSIQUES/03_Cycle_neutrinos/Source_docx_Fiche_Delta_m2_v0_1.md` | Cycle Saveur-Higgs, PMNS / oscillations | P1 | Extraction |
| Fiche Angles de Melange Leptoniques.docx | `02_CYCLES_PHYSIQUES/03_Cycle_neutrinos/Source_docx_Fiche_angles_melange_leptoniques_v0_1.md` | Cycle Saveur-Higgs, PMNS | P1 | Extraction |
| Fiche delta_CP v0.1.docx | `02_CYCLES_PHYSIQUES/03_Cycle_neutrinos/Source_docx_Fiche_delta_CP_v0_1.md` | Cycle Saveur-Higgs, CP neutrino | P1 | Extraction |
| Fiche masse absolue des neutrinos.docx | `02_CYCLES_PHYSIQUES/03_Cycle_neutrinos/Source_docx_Fiche_masse_absolue_neutrinos_v0_1.md` | Fiche Markdown deja produite, interface cosmologie | P1 | Comparaison prioritaire |
| Synthese du troisieme cycle v0.1.docx | `02_CYCLES_PHYSIQUES/03_Cycle_neutrinos/Source_docx_Synthese_troisieme_cycle_v0_1.md` | Synthese Saveur-Higgs, fiche neutrinos | P1 | Genealogie + comparaison |

### 8. Lot 1D : thermo-metrologie

Destination de principe :

```text
02_CYCLES_PHYSIQUES/04_Cycle_thermo_metrologique/
```

Ce dossier est a produire comme couche source, puis a articuler avec le cycle
metrologique SI actif.

| Source primaire | Sortie Markdown cible | Document actif concerne | Priorite | Controle |
|---|---|---|---|---|
| Fiche k_B v0.1.docx | `02_CYCLES_PHYSIQUES/04_Cycle_thermo_metrologique/Source_docx_Fiche_k_B_v0_1.md` | Cycle metrologique SI, matrice temporelle | P1 | Extraction + comparaison |
| Fiche N_A v0.1.docx | `02_CYCLES_PHYSIQUES/04_Cycle_thermo_metrologique/Source_docx_Fiche_N_A_v0_1.md` | Cycle metrologique SI | P1 | Extraction + comparaison |
| Fiche R v0.1.docx | `02_CYCLES_PHYSIQUES/04_Cycle_thermo_metrologique/Source_docx_Fiche_R_v0_1.md` | Cycle metrologique SI, relation R = N_A k_B | P1 | Extraction + controle positif |
| Synthese du quatrieme cycle.docx | `02_CYCLES_PHYSIQUES/04_Cycle_thermo_metrologique/Source_docx_Synthese_quatrieme_cycle_v0_1.md` | Architecture metrologique SI | P1 | Genealogie + comparaison |

Etat cible pre-Cercle 2 :

```text
extractions produites ;
synthese de recuperation produite :
02_CYCLES_PHYSIQUES/04_Cycle_thermo_metrologique/Synthese_recuperation_thermo_metrologique_SI_v0_1.md
```

### 9. Lot 1E : CKM et saveur

Destination de principe :

```text
02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/
```

| Source primaire | Sortie Markdown cible | Document actif concerne | Priorite | Controle |
|---|---|---|---|---|
| Fiche CKM v0.1.docx | `02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/Source_docx_Fiche_CKM_v0_1.md` | Synthese Saveur-Higgs, architecture Saveur-Higgs | P1 | Extraction + comparaison |
| Fiche Wolfenstein v0.1.docx | `02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/Source_docx_Fiche_Wolfenstein_v0_1.md` | Synthese Saveur-Higgs, architecture Saveur-Higgs | P1 | Extraction + comparaison |
| Synthese du cycle CKM v0.1.docx | `02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/Source_docx_Synthese_cycle_CKM_v0_1.md` | Synthese Saveur-Higgs | P1 | Genealogie + comparaison |

Etat cible pre-Cercle 2 :

```text
extractions produites ;
synthese de recuperation produite :
02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/Synthese_recuperation_sources_saveur_Higgs_cible_v0_1.md
```

### 10. Lot 2 : tests taxonomiques

Destination de principe :

```text
03_TESTS_TAXONOMIQUES/
```

Ce dossier est a produire si les tests doivent etre separes des notes
methodologiques actives.

Etat :

```text
ouvert ;
extractions Markdown produites ;
synthese de recuperation produite :
03_TESTS_TAXONOMIQUES/Synthese_recuperation_tests_taxonomiques_v0_1.md
```

| Source primaire | Sortie Markdown cible | Document actif concerne | Priorite | Controle |
|---|---|---|---|---|
| Test des familles fragiles.docx | `03_TESTS_TAXONOMIQUES/Source_docx_Test_familles_fragiles_v0_1.md` | Methode v1.3, reecriture positive | P0 | Extraction + controle des termes evacues |
| Test de la famille Seuil.docx | `03_TESTS_TAXONOMIQUES/Source_docx_Test_famille_Seuil_v0_1.md` | Methode v1.3, matrice de criblage | P0 | Extraction + genealogie |
| Test de la famille Fond.docx | `03_TESTS_TAXONOMIQUES/Source_docx_Test_famille_Fond_v0_1.md` | Cycle cosmologique, methode v1.3 | P0 | Extraction + comparaison |
| Test de la famille Relation v0.1.docx | `03_TESTS_TAXONOMIQUES/Source_docx_Test_famille_Relation_v0_1.md` | Reecriture positive, fiche neutrinos | P0 | Extraction + dissolution positive |

Point de vigilance :

```text
ces tests doivent remonter les problemes et distinctions,
pas restaurer les anciennes familles comme premier niveau de classement.
```

### 11. Lot 3 : sources d'architecture

Etat :

```text
ouvert ;
extractions Markdown produites ;
synthese de recuperation produite :
04_ARCHITECTURES/Synthese_recuperation_sources_architecture_lot3_v0_1.md
```

| Source primaire | Sortie Markdown cible | Document actif concerne | Priorite | Controle |
|---|---|---|---|---|
| Note de consolidation saveur-Higgs v0.1.docx | `04_ARCHITECTURES/Source_docx_Note_consolidation_saveur_Higgs_v0_1.md` | Architecture Saveur-Higgs, synthese Saveur-Higgs | P0 | Extraction avant cercle 2 |
| Cycle effectif basse energie v0.1.docx | `02_CYCLES_PHYSIQUES/06_Cycle_effectif_basse_energie/Source_docx_Cycle_effectif_basse_energie_v0_1.md` | Architecture effective basse energie | P0 | Extraction + comparaison |
| Cycle effectif basse energie v0.2.docx | `02_CYCLES_PHYSIQUES/06_Cycle_effectif_basse_energie/Source_docx_Cycle_effectif_basse_energie_v0_2.md` | Architecture effective basse energie | P0 | Extraction + comparaison |
| Cycle effectif basse energie v0.3.docx | `02_CYCLES_PHYSIQUES/06_Cycle_effectif_basse_energie/Source_docx_Cycle_effectif_basse_energie_v0_3.md` | Architecture effective basse energie | P0 | Extraction + comparaison |

Decision :

```text
le cercle 2 des architectures actives ne doit pas commencer
avant lecture de ce lot.
```

### 12. Lot 4 : genealogie des cartes

Destination de principe :

```text
05_CARTES_ET_SYNTHESES/00_Sources_docx_Genealogie_cartes/
```

| Source primaire | Sortie Markdown cible | Document actif concerne | Priorite | Controle |
|---|---|---|---|---|
| Carte consolidee v0.1.docx | `05_CARTES_ET_SYNTHESES/00_Sources_docx_Genealogie_cartes/Source_docx_Carte_consolidee_v0_1.md` | Carte v1.2, index | P2 | Genealogie |
| Carte consolidee v0.2.docx | `05_CARTES_ET_SYNTHESES/00_Sources_docx_Genealogie_cartes/Source_docx_Carte_consolidee_v0_2.md` | Carte v1.2, index | P2 | Genealogie |
| Carte consolidee v0.3.docx | `05_CARTES_ET_SYNTHESES/00_Sources_docx_Genealogie_cartes/Source_docx_Carte_consolidee_v0_3.md` | Carte v1.2, index | P2 | Genealogie |
| Carte consolidee v0.4.docx | `05_CARTES_ET_SYNTHESES/00_Sources_docx_Genealogie_cartes/Source_docx_Carte_consolidee_v0_4.md` | Carte v1.2, index | P2 | Genealogie |
| Carte consolidee v0.5.docx | `05_CARTES_ET_SYNTHESES/00_Sources_docx_Genealogie_cartes/Source_docx_Carte_consolidee_v0_5.md` | Carte v1.2, index | P2 | Genealogie |
| Carte consolidee v0.6.docx | aucun fichier trouve | Carte v1.2, index | P2 | Lacune a documenter |
| Carte consolidee v0.7.docx | `05_CARTES_ET_SYNTHESES/00_Sources_docx_Genealogie_cartes/Source_docx_Carte_consolidee_v0_7.md` | Carte v1.2, index | P2 | Genealogie |
| Carte consolidee v0.8.docx | `05_CARTES_ET_SYNTHESES/00_Sources_docx_Genealogie_cartes/Source_docx_Carte_consolidee_v0_8.md` | Carte v1.2, index, cosmologie v0.1 | P2 | Genealogie + comparaison |

### 13. Lot 5 : critiques constructives

Destination de principe :

```text
90_Critiques_ constantes_effectives_stabilisees/00_Sources_markdown/
```

Ces sources ont deja ete criblees.

La remontee Markdown sert surtout a reconnecter les critiques source aux
choix deja integres.

| Source primaire | Sortie Markdown cible | Document actif concerne | Priorite | Controle |
|---|---|---|---|---|
| Tensions cosmologiques et taxonomie des constantes physiques - Summary.docx | `90_Critiques_ constantes_effectives_stabilisees/00_Sources_markdown/Source_docx_Critique_tensions_cosmologiques_v0_1.md` | Cycle cosmologique, fiche de criblage | P3 | Comparaison |
| Taxonomie des constantes comme fonctions - Summary.docx | `90_Critiques_ constantes_effectives_stabilisees/00_Sources_markdown/Source_docx_Critique_taxonomie_fonctions_v0_1.md` | Methode v1.3, architectures | P3 | Comparaison |
| Refondre la taxonomie des constantes physiques - Summary.docx | `90_Critiques_ constantes_effectives_stabilisees/00_Sources_markdown/Source_docx_Critique_refondre_taxonomie_v0_1.md` | Revision de fond, carte v1.2 | P3 | Comparaison |
| L architecture documentaire des constantes physiques - Summary.docx | `90_Critiques_ constantes_effectives_stabilisees/00_Sources_markdown/Source_docx_Critique_architecture_documentaire_v0_1.md` | Index, audit documentaire | P3 | Comparaison |
| L architecture dynamique des constantes physiques - Summary.docx | `90_Critiques_ constantes_effectives_stabilisees/00_Sources_markdown/Source_docx_Critique_architecture_dynamique_v0_1.md` | Matrice temporelle, revision de fond | P3 | Comparaison |
| L architecture des constantes physiques effectives v2 - Summary.docx | `90_Critiques_ constantes_effectives_stabilisees/00_Sources_markdown/Source_docx_Critique_architecture_effective_v2_v0_1.md` | Architectures inter-fonctions | P3 | Comparaison |
| Les constantes fantomes des neutrinos - Summary.docx | `90_Critiques_ constantes_effectives_stabilisees/00_Sources_markdown/Source_docx_Critique_neutrinos_fantomes_v0_1.md` | Fiche masse absolue neutrinos | P3 | Comparaison |
| Fiabiliser la hierarchie des constantes physiques - Summary.docx | `90_Critiques_ constantes_effectives_stabilisees/00_Sources_markdown/Source_docx_Critique_fiabiliser_hierarchie_v0_1.md` | Methode v1.3, carte v1.2 | P3 | Comparaison |

Sous-lot 5b : critiques constructives supplementaires, criblees dans :

```text
01_CADRE_METHODOLOGIQUE/Fiche_criblage_critiques_lot2_v0_1.md
```

| Source primaire | Document actif concerne | Priorite | Controle |
|---|---|---|---|
| Architecture fonctionnelle des constantes physiques - Summary.docx | Fonctions transversales, tensions, observables reconstruites, temporalite | P2 | Criblage lot 2 |
| Le statut ontologique des constantes physiques - Summary.docx | Couplage regime-acces, tensions, test de retrait | P2 | Criblage lot 2 |
| Mathematiser la classification des constantes physiques - Summary.docx | Formalisation prudente, graphes, seuils, decision | P2 | Criblage lot 2 |
| Restructurer la matrice des constantes physiques - Summary.docx | Ordre des rangs, escalade, matrices temporelles | P2 | Criblage lot 2 |
| Transformer les tensions en anomalies cosmologiques - Summary.docx | Passerelle tensions, substitution, degenerescences cosmologiques | P2 | Criblage lot 2 |

### 14. Ordre d'execution recommande

Ordre concret :

```text
1. Lot 0 : socle methodologique.
2. Lot 2 : tests taxonomiques, car ils controlent les mots evacues.
3. Lot 3 : sources d'architecture, avant le cercle 2.
4. Lot 1 : fiches physiques sources, par sous-cycle.
5. Lot 4 : genealogie des cartes.
6. Lot 5 : critiques constructives, pour reconnecter les sources.
```

Raison :

```text
la methode et les tests doivent etre relus avant les architectures ;
les architectures doivent etre relues avant les fiches dispersees ;
les cartes et critiques servent ensuite a verifier la coherence globale.
```

### 15. Anomalies a traiter

| Anomalie | Source | Traitement |
|---|---|---|
| Duplicat alpha_G / M_Pl | Deux fichiers DOCX distincts | Compare dans `02_CYCLES_PHYSIQUES/06_Cycle_effectif_basse_energie/Synthese_comparaison_alphaG_MPl_sources_v0_1.md` ; conserver A et B comme genealogie |
| Ecriture.txt | Source auxiliaire liee a Lambda | Rattacher a Lambda sans l'effacer |
| Carte v0.6 absente | Serie v0.1 a v0.8 incomplete | Documenter la lacune dans la genealogie |
| Rattachement de Lambda | Source genetique electrofaible, usage cosmologique actif | Maintenir le double statut |
| Masse de l'electron | Source historique cycle 01, usage constitutif Saveur-Higgs | Ne pas laisser la genealogie ecraser l'architecture active |
| Anciennes familles | Tests Seuil, Fond, Relation | Extraire les problemes sans restaurer le vocabulaire comme rang premier |

### 16. Sortie attendue apres cette table

La prochaine action n'est pas une migration physique.

La prochaine action est :

```text
ouvrir le lot 0,
extraire les sources methodologiques en Markdown de travail,
produire une synthese de recuperation,
puis verifier ce que la methode active doit garder, corriger ou expliciter.
```

Ensuite seulement :

```text
ouvrir les tests taxonomiques,
puis les sources d'architecture,
puis le cercle 2.
```

### 17. Formule de cloture

```text
La remontee n'est pas un archivage ;
c'est une remise en circulation controlee de la matiere source.
```
