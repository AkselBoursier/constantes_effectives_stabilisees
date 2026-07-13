# constantes_effectives_stabilisees

Corpus de travail sur les constantes effectives stabilisees.

**Question directrice** : dans quelle mesure une grandeur peut-elle etre dite constante ?

Definition de reference (v1.3) :

> Une constante effective stabilisee est une grandeur dont une valeur, une forme, une liaison qualifiee, un role ou une dependance devient robuste dans un regime donne, selon un acces determine, avec un mode et une trajectoire de stabilisation explicites, sans que cette robustesse implique necessairement une constance absolue, une universalite hors contexte ou un statut fondamental.

---

## Entree rapide

Point d'entree recommande :

- [Grille de lecture des 8 modes](05_CARTES_ET_SYNTHESES/Grille_lecture_8_modes_v0_1.md) — formulaire court et table des modes pour toute grandeur
- [Index raisonne du corpus v1.0](05_CARTES_ET_SYNTHESES/Index_raisonne_du_corpus_v1_0.md) — navigation globale, statuts et ordre de lecture

Puis, dans l'ordre :

| Priorite | Document | Role |
|---|---|---|
| 1 | [Grille de lecture des 8 modes](05_CARTES_ET_SYNTHESES/Grille_lecture_8_modes_v0_1.md) | Point d'entree pratique : modes, architectures, formulaire court |
| 2 | [Note methodologique courte post-v1.3](01_CADRE_METHODOLOGIQUE/Note_methodologique_courte_post_v1_3.md) | Procedure courte de criblage pour cas litigieux |
| 3 | [Carte consolidee v1.3](05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_3_post_cercle2.md) | Carte generale actuelle apres cercle 2 |
| 4 | [Matrice acquis theoriques](05_CARTES_ET_SYNTHESES/Matrice_acquis_theoriques_v0_1.md) | Acquis argumentables avant controle des limites |
| 5 | [Fiche limites et non-theses](05_CARTES_ET_SYNTHESES/Fiche_limites_non_theses_v0_1.md) | Garde-fous et limites explicites |
| 6 | [Premier degagement de these](05_CARTES_ET_SYNTHESES/Premier_degagement_these_v0_1.md) | Premier enonce sur la stabilisation effective situee |
| 7 | [Matrice degagements theoriques](05_CARTES_ET_SYNTHESES/Matrice_degagements_theoriques_v0_1.md) | Autres theses et articulations possibles |
| 8 | [Mise a l'epreuve sur exemples](05_CARTES_ET_SYNTHESES/Mise_epreuve_degagements_theoriques_exemples_porteurs_v0_1.md) | Test sur exemples porteurs |
| 9 | [Audit de resynchronisation](05_CARTES_ET_SYNTHESES/Audit_resynchronisation_theorique_v0_1.md) | Controle de coherence theorique |

---

## Arborescence du depot

```text
constantes_effectives_stabilisees/
│
├── README.md                          ← ce fichier
├── GLOSSAIRE.md                       ← termes cles du projet
├── CONVENTION_PLACEHOLDERS.md         ← convention des extractions et statuts
│
├── audit/                             ← scripts d'audit sans dependance lourde
│   ├── audit_placeholders.sh
│   ├── audit_liens.sh
│   └── audit_encodage.sh
│
├── 01_CADRE_METHODOLOGIQUE/           ← methode, matrices, protocoles
│   ├── 00_Sources_docx/               ← extractions DOCX methodologiques (lot 0)
│   └── *.md
│
├── 02_CYCLES_PHYSIQUES/               ← fiches et syntheses par cycle
│   ├── 04_Cycle_thermo_metrologique/
│   ├── 05_Cycle_saveur_Higgs/
│   ├── 06_Cycle_effectif_basse_energie/
│   ├── 07_Cycle_cosmologique/
│   └── 08_Cycle_metrologique_SI/
│
├── 03_TESTS_TAXONOMIQUES/             ← tests de passage des anciennes familles
│
├── 04_ARCHITECTURES/                  ← architectures actives et cercle 2
│
├── 05_CARTES_ET_SYNTHESES/            ← cartes, index, syntheses transversales
│
├── 90_Critiques_.../                  ← documents critiques exterieurs (DOCX)
│
└── *.docx                             ← sources DOCX racine historiques
```

---

## Statuts documentaires

| Statut | Description |
|---|---|
| **Reference active** | Document a utiliser en priorite (methode, carte, synthese transverse) |
| **Protocole actif** | Document d'application reutilisable (matrices, tests) |
| **Consolidation** | Document qui stabilise un cycle ou une architecture |
| **Preuve locale** | Fiche ou cycle qui justifie une decision locale |
| **Source primaire historique** | Document source anterieur encore porteur de matiere |
| **Archive future** | DOCX conserve apres extraction et integration Markdown |
| **A produire** | Document utile identifie mais non encore cree |

Voir : [Convention des placeholders et statuts](CONVENTION_PLACEHOLDERS.md)

---

## Documents actifs

### Methode et protocole

| Document | Statut |
|---|---|
| [Note methodologique v1.3](01_CADRE_METHODOLOGIQUE/Note_synthese_methodologique_v1_3_pre_familial_et_temporalite.md) | Reference active |
| [Note methodologique courte post-v1.3](01_CADRE_METHODOLOGIQUE/Note_methodologique_courte_post_v1_3.md) | Reference active |
| [Matrice de criblage taxonomique](01_CADRE_METHODOLOGIQUE/Matrice_criblage_taxonomique_v0_1.md) | Protocole actif |
| [Matrice temporelle](01_CADRE_METHODOLOGIQUE/Matrice_temporelle_v0_1.md) | Protocole actif |
| [Application matrice fiches sensibles](01_CADRE_METHODOLOGIQUE/Application_matrice_fiches_sensibles_v0_1.md) | Protocole actif |
| [Application matrice temporelle fiches sensibles](01_CADRE_METHODOLOGIQUE/Application_matrice_temporelle_fiches_sensibles_v0_1.md) | Protocole actif |
| [Reecriture positive du vocabulaire](01_CADRE_METHODOLOGIQUE/Reecriture_positive_vocabulaire_v0_1.md) | Reference active |
| [Synthese recuperation lot 0](01_CADRE_METHODOLOGIQUE/Synthese_recuperation_lot0_socle_methodologique_v0_1.md) | Consolidation |
| [Workflow GitHub](01_CADRE_METHODOLOGIQUE/Workflow_GitHub_v0_1.md) | Protocole actif |

### Cycles physiques

| Cycle | Synthese active | Dossier |
|---|---|---|
| Thermo-metrologique | [Synthese recuperation thermo-metrologique](02_CYCLES_PHYSIQUES/04_Cycle_thermo_metrologique/Synthese_recuperation_thermo_metrologique_SI_v0_1.md) | [04_Cycle_thermo_metrologique](02_CYCLES_PHYSIQUES/04_Cycle_thermo_metrologique/) |
| Saveur-Higgs | [Synthese cycle saveur-Higgs](02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/Synthese_cycle_saveur_Higgs_v0_1.md) | [05_Cycle_saveur_Higgs](02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/) |
| Effectif basse energie | [Synthese cycle effectif basse energie](02_CYCLES_PHYSIQUES/06_Cycle_effectif_basse_energie/Synthese_cycle_effectif_basse_energie_v0_1.md) | [06_Cycle_effectif_basse_energie](02_CYCLES_PHYSIQUES/06_Cycle_effectif_basse_energie/) |
| Cosmologique | [Synthese cycle cosmologique](02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Synthese_cycle_cosmologique_v0_1.md) | [07_Cycle_cosmologique](02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/) |
| Metrologique SI | [Cycle metrologique SI v0.1](02_CYCLES_PHYSIQUES/08_Cycle_metrologique_SI/Cycle_metrologique_SI_v0_1_c_h_e.md) | [08_Cycle_metrologique_SI](02_CYCLES_PHYSIQUES/08_Cycle_metrologique_SI/) |

### Archives taxonomiques

| Document | Statut |
|---|---|
| [Audit de taxonomie v0.1](05_CARTES_ET_SYNTHESES/Audit_taxonomie_v0_1.md) | Reference active — diagnostic et decisions |
| [Synthese recuperation tests taxonomiques](03_TESTS_TAXONOMIQUES/Synthese_recuperation_tests_taxonomiques_v0_1.md) | Archive historique — genealogie des categories |

Voir le [README du dossier 03_TESTS_TAXONOMIQUES](03_TESTS_TAXONOMIQUES/README.md).

### Architectures inter-familles

| Document | Statut |
|---|---|
| [Cercle 2 — architectures actives](04_ARCHITECTURES/Cercle2_architectures_actives_v0_1.md) | Reference active |
| [Cercle 2 — lot 2A Saveur-Higgs](04_ARCHITECTURES/Cercle2_lot2A_Saveur_Higgs_v0_1.md) | Consolidation |
| [Cercle 2 — lot 2B Metrologique SI](04_ARCHITECTURES/Cercle2_lot2B_Metrologique_SI_v0_1.md) | Consolidation |
| [Cercle 2 — lot 2C Effectif basse energie](04_ARCHITECTURES/Cercle2_lot2C_Effective_basse_energie_v0_1.md) | Consolidation |
| [Cercle 2 — lot 2D Cosmologique](04_ARCHITECTURES/Cercle2_lot2D_Cosmologique_v0_1.md) | Consolidation |
| [Cercle 2 — lot 2E Synthese transverse architectures](04_ARCHITECTURES/Cercle2_lot2E_Synthese_transverse_architectures_v0_1.md) | Reference active |
| [Cercle 2 — lot 2F Controle occurrences cartes](04_ARCHITECTURES/Cercle2_lot2F_Controle_occurrences_cartes_v0_1.md) | Protocole actif |
| [Synthese recuperation sources architecture lot 3](04_ARCHITECTURES/Synthese_recuperation_sources_architecture_lot3_v0_1.md) | Consolidation |
| [Architecture Saveur-Higgs — notes](04_ARCHITECTURES/Architecture_saveur_Higgs_notes.md) | Consolidation |
| [Architecture Effectif basse energie — notes](04_ARCHITECTURES/Architecture_effective_basse_energie_notes.md) | Consolidation |
| [Architecture Metrologique SI — notes](04_ARCHITECTURES/Architecture_metrologique_SI_notes.md) | Consolidation |
| [Architecture Cosmologique — notes](04_ARCHITECTURES/Architecture_cosmologique_notes.md) | Consolidation |

### Cartes et syntheses

| Document | Statut |
|---|---|
| [Grille de lecture des 8 modes](05_CARTES_ET_SYNTHESES/Grille_lecture_8_modes_v0_1.md) | Reference active |
| [Audit de taxonomie v0.1](05_CARTES_ET_SYNTHESES/Audit_taxonomie_v0_1.md) | Reference active |
| [Index raisonne du corpus v1.0](05_CARTES_ET_SYNTHESES/Index_raisonne_du_corpus_v1_0.md) | Reference active |
| [Carte consolidee v1.3 post-cercle 2](05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_3_post_cercle2.md) | Reference active |
| [Carte consolidee v1.2 refonte](05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_2_refonte.md) | Consolidation historique recente |
| [Synthese architectures inter-familles v1.0](05_CARTES_ET_SYNTHESES/Synthese_architectures_inter_familles_v1_0.md) | Reference active |
| [Carte dependances architectures](05_CARTES_ET_SYNTHESES/Carte_dependances_architectures_v0_1.md) | Consolidation active |
| [Matrice acquis theoriques](05_CARTES_ET_SYNTHESES/Matrice_acquis_theoriques_v0_1.md) | Reference active |
| [Note recentrage question directrice](05_CARTES_ET_SYNTHESES/Note_recentrage_question_directrice_v0_1.md) | Controle actif |
| [Fiche limites et non-theses](05_CARTES_ET_SYNTHESES/Fiche_limites_non_theses_v0_1.md) | Reference active |
| [Premier degagement de these](05_CARTES_ET_SYNTHESES/Premier_degagement_these_v0_1.md) | Reference active |
| [Matrice degagements theoriques](05_CARTES_ET_SYNTHESES/Matrice_degagements_theoriques_v0_1.md) | Reference active |
| [Mise a l'epreuve sur exemples porteurs](05_CARTES_ET_SYNTHESES/Mise_epreuve_degagements_theoriques_exemples_porteurs_v0_1.md) | Reference active |
| [Audit resynchronisation theorique](05_CARTES_ET_SYNTHESES/Audit_resynchronisation_theorique_v0_1.md) | Reference active |
| [Plan remontee sources DOCX Markdown](05_CARTES_ET_SYNTHESES/Plan_remontee_sources_docx_markdown_v0_1.md) | Protocole actif |
| [Table remontee sources DOCX](05_CARTES_ET_SYNTHESES/Table_remontee_sources_docx_v0_1.md) | Table de pilotage |
| [Seuil de suffisance avant cercle 2](05_CARTES_ET_SYNTHESES/Seuil_suffisance_avant_cercle2_v0_1.md) | Protocole actif |
| [Synthese suffisance pre-cercle 2](05_CARTES_ET_SYNTHESES/Synthese_suffisance_pre_cercle2_v0_1.md) | Consolidation active |

---

## Sources DOCX historiques

Les fichiers `.docx` a la racine du depot sont les sources primaires historiques.

Ils ne sont pas modifies.

Les extractions Markdown correspondantes sont dans les sous-dossiers `Source_docx_*`.

> **Attention** : les fichiers `Source_docx_*` contiennent des placeholders d'extraction
> comme `[  ]`, `[ M_W= ]`, `[ m_f= ]` correspondant a des passages incomplets.
> Voir [CONVENTION_PLACEHOLDERS.md](CONVENTION_PLACEHOLDERS.md) pour la convention.

---

## Glossaire

Voir [GLOSSAIRE.md](GLOSSAIRE.md) pour les definitions des termes cles :
Seuil, Fond, Relation, architecture, role contextuel, mode de solidarisation.

---

## Workflow GitHub

Le depot GitHub sert de journal de versions du corpus.

Regle actuelle :

```text
les decisions conceptuelles restent soumises a validation explicite ;
les synchronisations documentaires, controles, commits et pushs peuvent etre delegues apres stabilisation.
```

Document de reference : [Workflow GitHub](01_CADRE_METHODOLOGIQUE/Workflow_GitHub_v0_1.md)

Depot distant : https://github.com/AkselBoursier/constantes_effectives_stabilisees

---

## Audit et controles

Des scripts d'audit legers sont disponibles dans le dossier [`audit/`](audit/).

Commandes :

```bash
# Detecter les placeholders d'extraction dans tous les fichiers Markdown
bash audit/audit_placeholders.sh

# Verifier les liens Markdown relatifs
bash audit/audit_liens.sh

# Controler l'encodage UTF-8 et les titres dupliques
bash audit/audit_encodage.sh
```

Ces scripts ne necessitent pas de dependances externes : ils utilisent uniquement
les outils Unix standards (`grep`, `awk`, `file`, `sort`, `uniq`).

---

## Regles de contribution et de reprise

```text
1. Ne pas modifier le contenu scientifique des sources historiques DOCX.
2. Ne pas supprimer les DOCX ni les extractions Source_docx_*.
3. Ne pas transformer les architectures physiques actives en familles.
   L'evolution de la taxonomie methodologique est autorisee
   apres audit explicite.
4. Ne pas fabriquer de references scientifiques absentes des fichiers sources.
5. Conserver le francais et les conventions lexicales du projet.
6. Signaler les passages d'extraction incomplets avec la convention :
   > TODO — formule ou passage a verifier dans le DOCX original.
7. Toute decision conceptuelle reste soumise a validation explicite.
8. Privilegier des commits petits, lisibles et reversibles.
```
