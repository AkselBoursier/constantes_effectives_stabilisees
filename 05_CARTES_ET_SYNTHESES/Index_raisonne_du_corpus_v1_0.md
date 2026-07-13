# Index raisonne du corpus v1.0

## Navigation, statuts documentaires et ordre de lecture

> **Mise a jour de rangement** : les references historiques aux "Word racine"
> decrivent l'etat precedent du depot. Les 60 DOCX et le fichier texte sont
> maintenant ranges dans les dossiers thematiques `00_Sources_docx`. Voir le
> [registre des sources primaires](Registre_sources_primaires_v0_1.md) pour
> les chemins et empreintes actuels.

### 1. Fonction de l'index

Cet index ne modifie pas la methode.

Il sert a rendre le corpus navigable apres :

```text
la carte consolidee v1.1
la synthese des architectures inter-fonctions v1.0
la note methodologique v1.2
la revision temporelle et le criblage critique
la note methodologique v1.3
la carte des dependances architecturales v0.1
la carte consolidee v1.2 de refonte
la carte consolidee v1.3 post-cercle 2
le workflow GitHub provisoire
```

Objectif :

```text
distinguer les documents actifs,
les documents de consolidation,
les cycles de preuve,
les notes d'architecture,
les sources primaires historiques,
et les archives futures.
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
7. Sources primaires historiques DOCX.
8. Archives strictes, seulement apres remontee.
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
| Source primaire historique | Document source anterieur encore porteur de matiere | DOCX ranges dans les dossiers thematiques `00_Sources_docx`, fiches initiales, tests, cartes anciennes |
| Archive future | Original conserve apres extraction et integration | DOCX apres remontee Markdown controlee |
| A produire | Document utile mais non encore cree | Lacunes identifiees |

### 4. Documents de reference active

Ces documents forment le noyau actif du corpus.

| Document | Statut | Role |
|---|---|---|
| `01_CADRE_METHODOLOGIQUE/Note_synthese_methodologique_v1_3_pre_familial_et_temporalite.md` | Reference active | Methode actuelle : forme logique, fonction directrice, famille fonctionnelle controlee, roles contextuels, temporalite |
| `01_CADRE_METHODOLOGIQUE/Note_methodologique_courte_post_v1_3.md` | Reference active | Procedure courte : forme, regime, fonction, acces, trajectoire, architecture, limite, controle |
| `01_CADRE_METHODOLOGIQUE/Note_ancrage_realiste_medie_v0_1.md` | Correction active | Ancrage physique ou operationnel des grandeurs contre une lecture derealisante |
| `01_CADRE_METHODOLOGIQUE/Note_situation_effective_et_equilibrage_SI_v0_1.md` | Correction active | Definition controlee de `situe` et reequilibrage du poids SI |
| `01_CADRE_METHODOLOGIQUE/Audit_terminologique_actif_v0_1.md` | Correction active | Formulations actives apres v0.2 : situe, acces, regime, famille, relation, architecture, borne, tension, seuil, validite |
| `01_CADRE_METHODOLOGIQUE/Workflow_GitHub_v0_1.md` | Protocole actif | Versionnement prudent du corpus |
| `05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_3_post_cercle2.md` | Reference active | Carte generale actuelle apres cercle 2 et raccord critique cible |
| `05_CARTES_ET_SYNTHESES/Matrice_acquis_theoriques_v0_1.md` | Reference active | Acquis theoriques argumentables avant controle des limites |
| `05_CARTES_ET_SYNTHESES/Note_recentrage_question_directrice_v0_1.md` | Controle actif | Recentrage sur la question : dans quelle mesure une grandeur peut-elle etre dite constante |
| `05_CARTES_ET_SYNTHESES/Fiche_limites_non_theses_v0_1.md` | Reference active | Garde-fou des limites et non-theses avant premier degagement |
| `05_CARTES_ET_SYNTHESES/Premier_degagement_these_v0_1.md` | Reference active | Premier enonce sur le statut de constance comme stabilisation effective qualifiee |
| `05_CARTES_ET_SYNTHESES/Matrice_degagements_theoriques_v0_1.md` | Reference active | Ouverture des autres theses et articulations theoriques possibles |
| `05_CARTES_ET_SYNTHESES/Mise_epreuve_degagements_theoriques_exemples_porteurs_v0_1.md` | Reference active | Test des degagements theoriques sur exemples porteurs |
| `05_CARTES_ET_SYNTHESES/Audit_mise_a_plat_conceptuelle_post_critiques_v0_1.md` | Audit actif | Mise a plat apres critiques, reequilibrage SI et definition de `situe` |
| `05_CARTES_ET_SYNTHESES/Mise_a_jour_intellectuelle_v0_2.md` | Reference active | Bilan intellectuel courant apres mise a plat conceptuelle |
| `05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_2_refonte.md` | Consolidation historique recente | Carte de rangs et dependances avant cloture du cercle 2 |
| `05_CARTES_ET_SYNTHESES/Plan_remontee_sources_docx_markdown_v0_1.md` | Protocole actif | Remontee des sources DOCX primaires en Markdown |
| `05_CARTES_ET_SYNTHESES/Table_remontee_sources_docx_v0_1.md` | Table de pilotage | Correspondance source DOCX -> Markdown cible -> document actif |
| `05_CARTES_ET_SYNTHESES/Registre_sources_primaires_v0_1.md` | Registre de provenance | Chemins thematiques et empreintes des originaux et extractions |
| `05_CARTES_ET_SYNTHESES/Seuil_suffisance_avant_cercle2_v0_1.md` | Protocole actif | Seuil de remontee ciblee avant cercle 2 |
| `05_CARTES_ET_SYNTHESES/Synthese_suffisance_pre_cercle2_v0_1.md` | Consolidation active | Cloture du traitement cible avant cercle 2 |
| `05_CARTES_ET_SYNTHESES/Synthese_architectures_inter_familles_v1_0.md` | Reference active | Comparaison des quatre architectures |
| `05_CARTES_ET_SYNTHESES/Carte_dependances_architectures_v0_1.md` | Consolidation active | Reseaux de dependance entre architectures |
| `05_CARTES_ET_SYNTHESES/Index_raisonne_du_corpus_v1_0.md` | Reference active | Navigation et statut des documents |

Ordre recommande :

```text
Note_synthese_methodologique_v1_3_pre_familial_et_temporalite.md
Note_methodologique_courte_post_v1_3.md
Note_ancrage_realiste_medie_v0_1.md
Note_situation_effective_et_equilibrage_SI_v0_1.md
Audit_terminologique_actif_v0_1.md
Matrice_criblage_taxonomique_v0_1.md
Addendum_matrice_criblage_lot2_v0_1.md
Matrice_temporelle_v0_2.md
Passerelle_escalade_tensions_cosmologiques_v0_1.md
Workflow_GitHub_v0_1.md
Synthese_architectures_inter_familles_v1_0.md
Carte_dependances_architectures_v0_1.md
Carte_consolidee_v1_3_post_cercle2.md
Matrice_acquis_theoriques_v0_1.md
Note_recentrage_question_directrice_v0_1.md
Fiche_limites_non_theses_v0_1.md
Premier_degagement_these_v0_1.md
Matrice_degagements_theoriques_v0_1.md
Mise_epreuve_degagements_theoriques_exemples_porteurs_v0_1.md
Audit_mise_a_plat_conceptuelle_post_critiques_v0_1.md
Mise_a_jour_intellectuelle_v0_2.md
Index_raisonne_du_corpus_v1_0.md
```

### 5. Documents methodologiques

| Document | Statut | Role |
|---|---|---|
| `01_CADRE_METHODOLOGIQUE/Note_synthese_methodologique_v1_3_pre_familial_et_temporalite.md` | Reference active | Methode actuelle apres criblage : rang 0, roles contextuels, temporalite |
| `01_CADRE_METHODOLOGIQUE/Note_methodologique_courte_post_v1_3.md` | Reference active | Procedure courte de premiere passe apres carte v1.3 |
| `01_CADRE_METHODOLOGIQUE/Note_ancrage_realiste_medie_v0_1.md` | Correction active | Correction realiste medie de la definition v1.3 |
| `01_CADRE_METHODOLOGIQUE/Note_situation_effective_et_equilibrage_SI_v0_1.md` | Correction active | Usage de `situe` comme precision de regime, acces et qualification ; SI borne comme cas local |
| `01_CADRE_METHODOLOGIQUE/Audit_terminologique_actif_v0_1.md` | Correction active | Vocabulaire positif et rang des termes sensibles apres la mise a jour v0.2 |
| `01_CADRE_METHODOLOGIQUE/Matrice_criblage_taxonomique_v0_1.md` | Protocole actif | Application operationnelle de la methode v1.3 aux cas litigieux |
| `01_CADRE_METHODOLOGIQUE/Addendum_matrice_criblage_lot2_v0_1.md` | Addendum actif | Couche decisionnelle issue des cinq critiques supplementaires |
| `01_CADRE_METHODOLOGIQUE/Matrice_temporelle_v0_2.md` | Protocole actif | Scission constitution physique / acces epistemique pour cas litigieux |
| `01_CADRE_METHODOLOGIQUE/Passerelle_escalade_tensions_cosmologiques_v0_1.md` | Protocole actif | Escalade prudente des tensions cosmologiques vers stress test ou substitution |
| `01_CADRE_METHODOLOGIQUE/Reecriture_positive_vocabulaire_v0_1.md` | Protocole actif | Reecriture positive des anciens termes de classement |
| `01_CADRE_METHODOLOGIQUE/Note_terminologie_chantiers_v0_1.md` | Protocole leger | Codes de chantier reserves au reperage documentaire |
| `01_CADRE_METHODOLOGIQUE/Synthese_recuperation_lot0_socle_methodologique_v0_1.md` | Consolidation active | Recuperation du socle DOCX methodologique avant tests taxonomiques |
| `01_CADRE_METHODOLOGIQUE/Workflow_GitHub_v0_1.md` | Protocole actif | Regle de commit, push et branches apres stabilisation documentaire |
| `01_CADRE_METHODOLOGIQUE/Note_synthese_methodologique_v1_2.md` | Consolidation historique | Methode avant rang de forme logique et temporalite explicite |
| `01_CADRE_METHODOLOGIQUE/Fiche_criblage_critiques_v0_1.md` | Revision active | Extraction et recoupement des huit critiques constructives |
| `01_CADRE_METHODOLOGIQUE/Fiche_criblage_critiques_lot2_v0_1.md` | Revision active | Extraction et recoupement des cinq critiques constructives supplementaires |
| `01_CADRE_METHODOLOGIQUE/Revision_de_fond_v0_1_temporalite.md` | Revision active | Reorganisation de fond autour de la temporalite |
| `01_CADRE_METHODOLOGIQUE/Note_synthese_methodologique_v1_1.md` | Consolidation historique | Socle methodologique precedent |
| `01_CADRE_METHODOLOGIQUE/Mise_a_jour_methodologie_v1_1_notes.md` | Archive de consolidation | Notes preparatoires de la v1.1 |

Tests taxonomiques remontes :

| Document | Statut | Role |
|---|---|---|
| `03_TESTS_TAXONOMIQUES/Synthese_recuperation_tests_taxonomiques_v0_1.md` | Consolidation active | Recuperation positive de Seuil, Fond, liaison stabilisee et familles fragiles |
| `03_TESTS_TAXONOMIQUES/Test_traversant_H0_passerelle_tensions_v0_1.md` | Test actif | Application addendum, matrice temporelle v0.2 et passerelle a H_0 |
| `03_TESTS_TAXONOMIQUES/README.md` | Index local | Sources DOCX extraites du lot 2 |

Decision :

```text
pour toute nouvelle fiche, partir de la v1.3.
```

Pour comprendre la refonte de la methode, lire aussi :

```text
01_CADRE_METHODOLOGIQUE/Note_synthese_methodologique_v1_2.md
01_CADRE_METHODOLOGIQUE/Note_ancrage_realiste_medie_v0_1.md
01_CADRE_METHODOLOGIQUE/Note_situation_effective_et_equilibrage_SI_v0_1.md
01_CADRE_METHODOLOGIQUE/Audit_terminologique_actif_v0_1.md
01_CADRE_METHODOLOGIQUE/Fiche_criblage_critiques_v0_1.md
01_CADRE_METHODOLOGIQUE/Fiche_criblage_critiques_lot2_v0_1.md
01_CADRE_METHODOLOGIQUE/Addendum_matrice_criblage_lot2_v0_1.md
01_CADRE_METHODOLOGIQUE/Matrice_temporelle_v0_2.md
01_CADRE_METHODOLOGIQUE/Passerelle_escalade_tensions_cosmologiques_v0_1.md
01_CADRE_METHODOLOGIQUE/Revision_de_fond_v0_1_temporalite.md
01_CADRE_METHODOLOGIQUE/Reecriture_positive_vocabulaire_v0_1.md
```

La v1.1 reste utile pour comprendre la transition vers :

```text
regime d'acces
architecture inter-fonctions
extension SI
```

### 6. Cartes et syntheses generales

| Document | Statut | Role |
|---|---|---|
| `05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_3_post_cercle2.md` | Reference active | Carte des stabilisations effectives qualifiees apres cercle 2 |
| `05_CARTES_ET_SYNTHESES/Matrice_acquis_theoriques_v0_1.md` | Reference active | Passage des stabilisations effectives aux acquis argumentables |
| `05_CARTES_ET_SYNTHESES/Note_recentrage_question_directrice_v0_1.md` | Controle actif | Subordination de la methode a la question directrice des constantes |
| `05_CARTES_ET_SYNTHESES/Fiche_limites_non_theses_v0_1.md` | Reference active | Limites, non-theses et seuil vers le premier degagement |
| `05_CARTES_ET_SYNTHESES/Premier_degagement_these_v0_1.md` | Reference active | Degagement de these v0.1 sur la qualification des constantes |
| `05_CARTES_ET_SYNTHESES/Matrice_degagements_theoriques_v0_1.md` | Reference active | Cartographie des degagements theoriques au-dela de la these-noyau |
| `05_CARTES_ET_SYNTHESES/Mise_epreuve_degagements_theoriques_exemples_porteurs_v0_1.md` | Reference active | Resistance des degagements sur `R`, `G_F`, cosmologie, Saveur-Higgs et neutrinos |
| `05_CARTES_ET_SYNTHESES/Audit_mise_a_plat_conceptuelle_post_critiques_v0_1.md` | Audit actif | Effets conceptuels des critiques, du SI rehierarchise et du terme `situe` |
| `05_CARTES_ET_SYNTHESES/Mise_a_jour_intellectuelle_v0_2.md` | Reference active | Synthese courante des acquis, deplacements et frictions |
| `05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_2_refonte.md` | Consolidation historique recente | Carte de rangs et dependances avant cercle 2 cloture |
| `05_CARTES_ET_SYNTHESES/Synthese_architectures_inter_familles_v1_0.md` | Reference active | Synthese transverse des architectures |
| `05_CARTES_ET_SYNTHESES/Carte_dependances_architectures_v0_1.md` | Consolidation active | Representation des architectures comme reseaux de dependance |
| `05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_1.md` | Consolidation historique | Carte avant rang de forme logique et requalification des liaisons |
| `05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_0.md` | Archive de consolidation | Etape avant extension SI |
| `05_CARTES_ET_SYNTHESES/Carte_consolidee_v0_9.md` | Archive de consolidation | Etape avant cosmologie et SI consolidees |

Decision :

```text
Carte_consolidee_v1_3_post_cercle2.md remplace la v1.2 comme carte de reference active.
```

Les cartes anterieures restent utiles pour retracer les decisions.

### 7. Architectures inter-fonctions

Le corpus stabilise quatre architectures.

| Architecture | Forme | Document principal | Statut |
|---|---|---|---|
| Cercle 2 | Reprise positive | `04_ARCHITECTURES/Cercle2_architectures_actives_v0_1.md` | Sequence cloturee |
| Cercle 2A Saveur-Higgs | Reprise positive constitutive | `04_ARCHITECTURES/Cercle2_lot2A_Saveur_Higgs_v0_1.md` | Produit |
| Cercle 2B Metrologique SI | Reprise positive definitionnelle | `04_ARCHITECTURES/Cercle2_lot2B_Metrologique_SI_v0_1.md` | Produit |
| Cercle 2C Effective basse energie | Reprise positive de validite | `04_ARCHITECTURES/Cercle2_lot2C_Effective_basse_energie_v0_1.md` | Produit |
| Cercle 2D Cosmologique | Reprise positive inferentielle et reconstructive | `04_ARCHITECTURES/Cercle2_lot2D_Cosmologique_v0_1.md` | Produit |
| Cercle 2E Synthese transverse | Reprise positive des modes de solidarisation | `04_ARCHITECTURES/Cercle2_lot2E_Synthese_transverse_architectures_v0_1.md` | Produit |
| Cercle 2F Controle | Controle d'occurrences et raccords de cartes | `04_ARCHITECTURES/Cercle2_lot2F_Controle_occurrences_cartes_v0_1.md` | Produit |
| Saveur-Higgs | Constitutive | `04_ARCHITECTURES/Architecture_saveur_Higgs_notes.md` | Consolidation active |
| Metrologique SI | Definitionnelle | `04_ARCHITECTURES/Architecture_metrologique_SI_notes.md` | Consolidation active |
| Effective basse energie | Validite | `04_ARCHITECTURES/Architecture_effective_basse_energie_notes.md` | Consolidation active |
| Cosmologique | Inferentielle / reconstructive | `04_ARCHITECTURES/Architecture_cosmologique_notes.md` + stress test v0.1 | Consolidation active avec sous-reseaux |
| Sources d'architecture lot 3 | Recuperation source | `04_ARCHITECTURES/Synthese_recuperation_sources_architecture_lot3_v0_1.md` | Consolidation active avant cercle 2 |

Regle de rang :

```text
une architecture inter-fonctions est une solidarite de fonctions,
pas un niveau de classement superieur.
```

Statut du cercle 2 :

```text
ouvert comme reprise positive des architectures actives,
avec controle d'occurrences et progression par lots ;
lots 2A Saveur-Higgs, 2B Metrologique SI, 2C Effective basse energie,
2D Cosmologique, 2E Synthese transverse et 2F Controle produits.
```

Point documentaire :

```text
l'architecture Saveur-Higgs dispose maintenant d'une note Markdown active,
et d'une synthese de cycle active dans 02_CYCLES_PHYSIQUES.
```

Archive historique source :

```text
Note de consolidation saveur-Higgs v0.1.docx
```

La note Markdown et la synthese de cycle doivent etre lues en priorite ; le Word racine sert a retracer la genealogie.

### 8. Cycle Saveur-Higgs

Dossier :

```text
02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/
```

Documents actifs :

| Document | Statut | Role |
|---|---|---|
| `02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/Cycle_CP1_seuil_electrofaible_v0_1.md` | Cycle consolide | Seuil electrofaible et constance de seuil |
| `02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/Synthese_CP1_seuil_electrofaible_v0_1.md` | Consolidation | Synthese du seuil electrofaible et raccord aux cartes |
| `02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/Note_physique_BEH_mecanisme_v0_1.md` | Note physique preparatoire | Mecanisme BEH, grandeurs et regimes d'acces |
| `02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/Synthese_cycle_saveur_Higgs_v0_1.md` | Consolidation | Synthese du cycle et trajectoire constitutive |
| `02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/Synthese_recuperation_sources_saveur_Higgs_cible_v0_1.md` | Consolidation source | Recuperation cible v, Yukawa, CKM, Wolfenstein avant cercle 2 |
| `02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/Fiche_masse_absolue_neutrinos_v0_1.md` | Fiche prudente | Ancrage spectral neutrino et interface cosmologique |
| `04_ARCHITECTURES/Architecture_saveur_Higgs_notes.md` | Consolidation active | Architecture issue du cycle |

Documents racine historiques associes :

```text
Note de consolidation saveur-Higgs v0.1.docx
Fiche (v) v0.1.docx
Fiche Yukawa v0.1.docx
Fiche CKM v0.1.docx
Fiche Wolfenstein v0.1.docx
Fiche Delta m^2.docx
Fiche Angles de Melange Leptoniques.docx
Fiche masse absolue des neutrinos.docx
```

Decision :

```text
pour comprendre l'architecture Saveur-Higgs,
lire d'abord le cycle du seuil electrofaible,
puis la synthese Saveur-Higgs pour la constitution interne,
puis la note d'architecture.
```

### 9. Cycle effectif basse energie

Dossier :

```text
02_CYCLES_PHYSIQUES/06_Cycle_effectif_basse_energie/
```

Documents actifs :

| Document | Statut | Role |
|---|---|---|
| `02_CYCLES_PHYSIQUES/06_Cycle_effectif_basse_energie/Cycle_effectif_basse_energie_v0_4_alphaG_MPl.md` | Preuve locale | Cas gravitationnel effectif |
| `02_CYCLES_PHYSIQUES/06_Cycle_effectif_basse_energie/Synthese_cycle_effectif_basse_energie_v0_1.md` | Consolidation | Synthese du cycle |
| `02_CYCLES_PHYSIQUES/06_Cycle_effectif_basse_energie/Synthese_comparaison_alphaG_MPl_sources_v0_1.md` | Consolidation source | Comparaison du doublon alpha_G / M_Pl |
| `04_ARCHITECTURES/Architecture_effective_basse_energie_notes.md` | Consolidation active | Architecture issue du cycle |

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

### 10. Cycle cosmologique

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
| 9 | `04_ARCHITECTURES/Architecture_cosmologique_notes.md` | Consolidation active | Architecture issue du cycle |
| 10 | `04_ARCHITECTURES/Architecture_cosmologique_stress_test_v0_1.md` | Protocole actif | Stress test des sous-reseaux |
| 11 | `02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Plan_reprise_cycle_cosmologique_v0_1.md` | Plan de reprise | Reprise controlee du cycle |
| 12 | `04_ARCHITECTURES/Cercle2_lot2D_Cosmologique_v0_1.md` | Reprise positive | Architecture inferentielle et reconstructive prudente |

Decision :

```text
pour une lecture rapide, lire la synthese du cycle, la note d'architecture et le stress test.
pour verifier une decision locale, revenir a la fiche correspondante.
pour comprendre la reprise, partir du plan de reprise v0.1 puis lire les fiches reprises.
```

### 11. Cycle metrologique SI

Dossier :

```text
02_CYCLES_PHYSIQUES/08_Cycle_metrologique_SI/
```

Documents actifs :

| Document | Statut | Role |
|---|---|---|
| `02_CYCLES_PHYSIQUES/08_Cycle_metrologique_SI/Cycle_metrologique_SI_v0_1_c_h_e.md` | Preuve locale | Extension SI a c, h, e, K_J, R_K |
| `02_CYCLES_PHYSIQUES/04_Cycle_thermo_metrologique/Synthese_recuperation_thermo_metrologique_SI_v0_1.md` | Consolidation source | Recuperation k_B, N_A, R et quatrieme cycle avant cercle 2 |
| `04_ARCHITECTURES/Architecture_metrologique_SI_notes.md` | Consolidation active | Architecture SI etendue |

Documents racine historiques associes :

```text
Fiches k_B, N_A, R
```

Decision :

```text
la reference actuelle pour le SI est la note d'architecture metrologique,
avec le cycle c / h / e comme preuve locale recente.
```

### 12. Sources DOCX primaires

Le dossier racine contient de nombreux fichiers Word anterieurs.

Ils doivent etre traites comme :

```text
sources primaires historiques
fiches initiales de preuve
tests taxonomiques sources
syntheses initiales
cartes genealogiques
```

Ils ne sont pas la couche active de la methode,
mais ils ne sont pas secondaires.

Groupes principaux :

| Groupe | Role |
|---|---|
| Brief initial | Point de depart du projet |
| Methodes et addenda initiaux | Genese de la methode |
| Tests de familles fonctionnelles | Exploration des sorties taxonomiques fragiles |
| Fiches physiques initiales | Preuves locales anciennes |
| Syntheses de cycles initiales | Consolidations historiques |
| Cartes consolidees v0.1 a v0.8 | Evolution de la carte avant l'arborescence Markdown |

Document de pilotage :

```text
05_CARTES_ET_SYNTHESES/Plan_remontee_sources_docx_markdown_v0_1.md
05_CARTES_ET_SYNTHESES/Table_remontee_sources_docx_v0_1.md
05_CARTES_ET_SYNTHESES/Seuil_suffisance_avant_cercle2_v0_1.md
05_CARTES_ET_SYNTHESES/Synthese_suffisance_pre_cercle2_v0_1.md
05_CARTES_ET_SYNTHESES/Audit_dependances_et_reorganisation_v0_1.md
```

Regle de conservation :

```text
ne pas renommer ni deplacer les fichiers Word racine tant que les dependances internes ne sont pas verifiees.
```

Regle d'usage :

```text
les Markdown recents guident le travail courant ;
les DOCX restent les sources primaires a remonter avant archivage strict.
```

### 13. Ordre de lecture selon l'objectif

#### 13.1 Comprendre la methode actuelle

```text
01_CADRE_METHODOLOGIQUE/Note_synthese_methodologique_v1_3_pre_familial_et_temporalite.md
01_CADRE_METHODOLOGIQUE/Note_methodologique_courte_post_v1_3.md
01_CADRE_METHODOLOGIQUE/Matrice_criblage_taxonomique_v0_1.md
05_CARTES_ET_SYNTHESES/Carte_dependances_architectures_v0_1.md
05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_3_post_cercle2.md
05_CARTES_ET_SYNTHESES/Matrice_acquis_theoriques_v0_1.md
05_CARTES_ET_SYNTHESES/Note_recentrage_question_directrice_v0_1.md
05_CARTES_ET_SYNTHESES/Fiche_limites_non_theses_v0_1.md
05_CARTES_ET_SYNTHESES/Premier_degagement_these_v0_1.md
05_CARTES_ET_SYNTHESES/Matrice_degagements_theoriques_v0_1.md
05_CARTES_ET_SYNTHESES/Mise_epreuve_degagements_theoriques_exemples_porteurs_v0_1.md
05_CARTES_ET_SYNTHESES/Synthese_architectures_inter_familles_v1_0.md
```

#### 13.2 Comprendre les architectures

```text
05_CARTES_ET_SYNTHESES/Synthese_architectures_inter_familles_v1_0.md
04_ARCHITECTURES/Architecture_saveur_Higgs_notes.md
04_ARCHITECTURES/Architecture_metrologique_SI_notes.md
04_ARCHITECTURES/Architecture_effective_basse_energie_notes.md
04_ARCHITECTURES/Architecture_cosmologique_notes.md
```

Pour retracer la genealogie Saveur-Higgs :

```text
consulter ensuite la note Word racine de consolidation Saveur-Higgs.
```

#### 13.3 Verifier une decision physique locale

```text
chercher d'abord la synthese du cycle concerne,
puis revenir a la fiche locale.
```

Exemples :

```text
H_0 -> Synthese_cycle_cosmologique_v0_1.md puis Cycle_cosmologique_v0_3_H0.md
c / h / e -> Architecture_metrologique_SI_notes.md puis Cycle_metrologique_SI_v0_1_c_h_e.md
alpha_G / M_Pl -> Synthese_cycle_effectif_basse_energie_v0_1.md puis Cycle_effectif_basse_energie_v0_4_alphaG_MPl.md
alpha_G / M_Pl source -> Synthese_comparaison_alphaG_MPl_sources_v0_1.md
SI source -> Synthese_recuperation_thermo_metrologique_SI_v0_1.md
Saveur-Higgs source -> Synthese_recuperation_sources_saveur_Higgs_cible_v0_1.md
```

#### 13.4 Retracer l'histoire du projet

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
Note_methodologique_courte_post_v1_3.md
Matrice_criblage_taxonomique_v0_1.md
Architecture_saveur_Higgs_notes.md
Carte_dependances_architectures_v0_1.md
Carte_consolidee_v1_2_refonte.md
Cercle2_architectures_actives_v0_1.md
Carte_consolidee_v1_3_post_cercle2.md
Matrice_acquis_theoriques_v0_1.md
Note_recentrage_question_directrice_v0_1.md
Fiche_limites_non_theses_v0_1.md
Premier_degagement_these_v0_1.md
Matrice_degagements_theoriques_v0_1.md
Mise_epreuve_degagements_theoriques_exemples_porteurs_v0_1.md
Architecture_cosmologique_stress_test_v0_1.md
Plan_reprise_cycle_cosmologique_v0_1.md
```

### 14. Dependances principales

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
  -> Note_methodologique_courte_post_v1_3.md
  -> Matrice_criblage_taxonomique_v0_1.md
  -> Architecture_saveur_Higgs_notes.md
  -> Carte_dependances_architectures_v0_1.md
  -> Carte_consolidee_v1_2_refonte.md
  -> Cercle2_architectures_actives_v0_1.md
  -> Carte_consolidee_v1_3_post_cercle2.md
  -> Matrice_acquis_theoriques_v0_1.md
  -> Note_recentrage_question_directrice_v0_1.md
  -> Fiche_limites_non_theses_v0_1.md
  -> Premier_degagement_these_v0_1.md
  -> Matrice_degagements_theoriques_v0_1.md
  -> Mise_epreuve_degagements_theoriques_exemples_porteurs_v0_1.md
  -> Architecture_cosmologique_stress_test_v0_1.md
  -> Plan_reprise_cycle_cosmologique_v0_1.md
  -> Index_raisonne_du_corpus_v1_0.md
```

Lecture fonctionnelle :

```text
methode -> criblage -> architecture -> dependances -> carte consolidee -> acquis -> limites
```

### 15. Lacunes documentaires identifiees

Cet index fait apparaitre plusieurs lacunes possibles.

Depuis la revision de fond sur la temporalite et le criblage des critiques, la premiere lacune methodologique devient prioritaire.

#### 15.1 Methode v1.3 produite

La version methodologique active integrant explicitement les apports de la revision temporelle et du criblage critique est produite.

```text
le rang de forme logique,
la requalification des liaisons stabilisees,
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
forme logique avant fonction directrice,
famille fonctionnelle seulement apres test,
fonction avant role,
acces et modele comme axes orthogonaux,
temporalite comme trajectoire.
```

Documents d'application produits ensuite :

```text
01_CADRE_METHODOLOGIQUE/Note_methodologique_courte_post_v1_3.md
01_CADRE_METHODOLOGIQUE/Matrice_criblage_taxonomique_v0_1.md
05_CARTES_ET_SYNTHESES/Carte_dependances_architectures_v0_1.md
05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_2_refonte.md
05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_3_post_cercle2.md
04_ARCHITECTURES/Architecture_cosmologique_stress_test_v0_1.md
02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/Synthese_cycle_saveur_Higgs_v0_1.md
02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/Fiche_masse_absolue_neutrinos_v0_1.md
```

Stress test cosmologique produit :

```text
04_ARCHITECTURES/Architecture_cosmologique_stress_test_v0_1.md
```

#### 15.2 Note Markdown et cycle Saveur-Higgs produits

La note Markdown dediee est produite :

```text
04_ARCHITECTURES/Architecture_saveur_Higgs_notes.md
02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/Synthese_cycle_saveur_Higgs_v0_1.md
02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/Fiche_masse_absolue_neutrinos_v0_1.md
```

Statut :

```text
consolidation active,
integree dans la carte consolidee v1.2.
```

Raison :

```text
Saveur-Higgs etait deja traite dans les sources Word racine, la carte v1.1 et la synthese transverse.
La note Markdown et la synthese de cycle levent l'asymetrie documentaire entre les quatre architectures actives.
```

#### 15.3 README de dossier produit

Un README minimal existe maintenant au dossier racine.

Forme possible :

```text
README.md
```

Role :

```text
renvoyer vers l'index raisonne,
la note methodologique v1.3,
et la carte consolidee v1.2 de refonte.
```

Statut :

```text
produit ;
utile pour entrer rapidement dans le corpus hors de cette conversation.
```

#### 15.4 Normalisation future des archives

Une normalisation des noms de fichiers Word pourrait etre envisagee plus tard.

Statut :

```text
a ne pas faire maintenant.
```

Raison :

```text
les dependances internes et citations croisees ne sont pas encore auditees.
```

### 16. Regles pour les prochaines etapes

Avant d'ouvrir un nouveau cycle physique :

```text
1. Verifier si la question releve deja d'une architecture stabilisee.
2. Lire la note methodologique v1.3.
3. Appliquer la matrice de criblage si le classement est litigieux.
4. Lire la carte v1.1.
5. Identifier le cycle ou la fiche de preuve la plus proche.
6. Ne creer une nouvelle famille fonctionnelle que si le test de resistance et le test d'architecture echouent.
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

### 17. Carte active du corpus

La carte active du corpus peut etre resumee ainsi.

```text
Methode active :
01_CADRE_METHODOLOGIQUE/Note_synthese_methodologique_v1_3_pre_familial_et_temporalite.md
01_CADRE_METHODOLOGIQUE/Note_methodologique_courte_post_v1_3.md

Methode historique recente :
01_CADRE_METHODOLOGIQUE/Note_synthese_methodologique_v1_2.md

Correction active :
01_CADRE_METHODOLOGIQUE/Note_ancrage_realiste_medie_v0_1.md
01_CADRE_METHODOLOGIQUE/Note_situation_effective_et_equilibrage_SI_v0_1.md
01_CADRE_METHODOLOGIQUE/Audit_terminologique_actif_v0_1.md

Protocole actif :
01_CADRE_METHODOLOGIQUE/Matrice_criblage_taxonomique_v0_1.md
01_CADRE_METHODOLOGIQUE/Addendum_matrice_criblage_lot2_v0_1.md
01_CADRE_METHODOLOGIQUE/Matrice_temporelle_v0_1.md
01_CADRE_METHODOLOGIQUE/Matrice_temporelle_v0_2.md
01_CADRE_METHODOLOGIQUE/Passerelle_escalade_tensions_cosmologiques_v0_1.md
01_CADRE_METHODOLOGIQUE/Application_matrice_fiches_sensibles_v0_1.md
01_CADRE_METHODOLOGIQUE/Application_matrice_temporelle_fiches_sensibles_v0_1.md
01_CADRE_METHODOLOGIQUE/Reecriture_positive_vocabulaire_v0_1.md
01_CADRE_METHODOLOGIQUE/Note_terminologie_chantiers_v0_1.md
01_CADRE_METHODOLOGIQUE/Workflow_GitHub_v0_1.md

Carte active :
05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_3_post_cercle2.md

Matrice des acquis active :
05_CARTES_ET_SYNTHESES/Matrice_acquis_theoriques_v0_1.md

Note de recentrage active :
05_CARTES_ET_SYNTHESES/Note_recentrage_question_directrice_v0_1.md

Fiche des limites active :
05_CARTES_ET_SYNTHESES/Fiche_limites_non_theses_v0_1.md

Premier degagement de these actif :
05_CARTES_ET_SYNTHESES/Premier_degagement_these_v0_1.md

Matrice des degagements active :
05_CARTES_ET_SYNTHESES/Matrice_degagements_theoriques_v0_1.md

Mise a l'epreuve active :
05_CARTES_ET_SYNTHESES/Mise_epreuve_degagements_theoriques_exemples_porteurs_v0_1.md

Audit de mise a plat actif :
05_CARTES_ET_SYNTHESES/Audit_mise_a_plat_conceptuelle_post_critiques_v0_1.md

Mise a jour intellectuelle active :
05_CARTES_ET_SYNTHESES/Mise_a_jour_intellectuelle_v0_2.md

Carte historique recente :
05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_2_refonte.md
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
01_CADRE_METHODOLOGIQUE/Fiche_criblage_critiques_lot2_v0_1.md

Architectures actives :
04_ARCHITECTURES/Architecture_saveur_Higgs_notes.md
04_ARCHITECTURES/Architecture_metrologique_SI_notes.md
04_ARCHITECTURES/Architecture_effective_basse_energie_notes.md
04_ARCHITECTURES/Architecture_cosmologique_notes.md
04_ARCHITECTURES/Architecture_cosmologique_stress_test_v0_1.md

Cycles actifs :
02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/Cycle_CP1_seuil_electrofaible_v0_1.md
02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/Synthese_CP1_seuil_electrofaible_v0_1.md
02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/Note_physique_BEH_mecanisme_v0_1.md
02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/Synthese_cycle_saveur_Higgs_v0_1.md
02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/Fiche_masse_absolue_neutrinos_v0_1.md
02_CYCLES_PHYSIQUES/06_Cycle_effectif_basse_energie/
02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/
02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Plan_reprise_cycle_cosmologique_v0_1.md
02_CYCLES_PHYSIQUES/08_Cycle_metrologique_SI/

Audit transversal :
05_CARTES_ET_SYNTHESES/Audit_resynchronisation_theorique_v0_1.md
```

### 18. Formule de cloture

L'index peut etre resume par trois regles.

```text
la methode donne les criteres
la carte donne l'etat consolide
les cycles et architectures donnent les preuves
```

Formule finale :

> Un corpus robuste n'est pas seulement une accumulation de notes ; c'est une hierarchie lisible de statuts, de preuves et de syntheses.
