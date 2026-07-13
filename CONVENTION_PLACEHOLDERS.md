# Convention des placeholders d'extraction et des statuts documentaires

Ce document definit les conventions utilisees dans ce corpus pour :

1. signaler les passages incomplets dans les extractions Markdown de fichiers DOCX ;
2. harmoniser les statuts documentaires entre les dossiers.

---

## 1. Placeholders d'extraction

### Origine

Les fichiers prefixes `Source_docx_*` sont des extractions textuelles de travail
a partir des sources DOCX historiques.

L'extraction automatique ou semi-manuelle produit parfois des passages incomplets,
notamment :

- des formules mathematiques tronquees ou non rendues ;
- des tableaux mal convertis ;
- des paragraphes vides correspondant a des elements graphiques ou a des equations
  complexes du fichier Word.

Ces passages apparaissent sous la forme de placeholders dans le Markdown :

```text
[  ]
[ M_W= ]
[ M_Z= ]
[ m_f= ]
[ Lambda ]
[ s_{12}= ]
```

### Regle de traitement

**Ne pas supprimer les placeholders** sans avoir verifie le DOCX source.

**Ne pas inventer le contenu absent.**

Si un passage est manifeste comme incomplet, le signaler avec la convention
suivante, ajoutee en commentaire apres le placeholder :

```markdown
[  ]

> TODO — formule ou passage a verifier dans le DOCX original.
```

Ou, si le contexte permet d'identifier la nature du passage :

```markdown
[ M_W= ]

> TODO — valeur numerique de M_W a verifier dans le DOCX original.
```

### Fichiers concernes

Les fichiers suivants contiennent des placeholders identifies (au 2026-07-13) :

| Fichier | Placeholders `[  ]` | Autres placeholders |
|---|---|---|
| `01_CADRE_METHODOLOGIQUE/00_Sources_docx/Source_docx_Note_synthese_methodologique_v0_1.md` | 115 | — |
| `03_TESTS_TAXONOMIQUES/00_Sources_docx/Source_docx_Test_famille_Fond_v0_1.md` | 101 | — |
| `01_CADRE_METHODOLOGIQUE/00_Sources_docx/Source_docx_Note_critique_compression_v0_1.md` | 64 | — |
| `03_TESTS_TAXONOMIQUES/00_Sources_docx/Source_docx_Test_famille_Relation_v0_1.md` | 62 | — |
| `01_CADRE_METHODOLOGIQUE/00_Sources_docx/Source_docx_Methode_v0_1.md` | 61 | — |
| `03_TESTS_TAXONOMIQUES/00_Sources_docx/Source_docx_Test_familles_fragiles_v0_1.md` | 54 | — |
| `02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/00_Sources_docx/Source_docx_Synthese_cycle_CKM_v0_1.md` | 49 | — |
| `02_CYCLES_PHYSIQUES/06_Cycle_effectif_basse_energie/00_Sources_docx/Source_docx_Cycle_effectif_basse_energie_v0_3.md` | 48 | — |
| `03_TESTS_TAXONOMIQUES/00_Sources_docx/Source_docx_Test_famille_Seuil_v0_1.md` | 47 | — |
| `04_ARCHITECTURES/00_Sources_docx/Source_docx_Note_consolidation_saveur_Higgs_v0_1.md` | 39 | `[ M_W= ]`, `[ M_Z= ]`, `[ m_f= ]`, `[ s_{12}= ]` |
| `02_CYCLES_PHYSIQUES/04_Cycle_thermo_metrologique/00_Sources_docx/Source_docx_Synthese_quatrieme_cycle_v0_1.md` | 34 | — |
| `02_CYCLES_PHYSIQUES/06_Cycle_effectif_basse_energie/00_Sources_docx/Source_docx_Cycle_effectif_basse_energie_v0_2.md` | 28 | — |
| `02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/00_Sources_docx/Source_docx_Fiche_CKM_v0_1.md` | 24 | — |
| `01_CADRE_METHODOLOGIQUE/00_Sources_docx/Source_docx_Addendum_methodologique_v0_2.md` | 22 | — |
| `02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/00_Sources_docx/Source_docx_Fiche_Wolfenstein_v0_1.md` | 21 | — |
| `02_CYCLES_PHYSIQUES/04_Cycle_thermo_metrologique/00_Sources_docx/Source_docx_Fiche_R_v0_1.md` | 14 | — |
| `02_CYCLES_PHYSIQUES/04_Cycle_thermo_metrologique/00_Sources_docx/Source_docx_Fiche_k_B_v0_1.md` | 13 | — |
| `02_CYCLES_PHYSIQUES/04_Cycle_thermo_metrologique/00_Sources_docx/Source_docx_Fiche_N_A_v0_1.md` | 13 | — |
| `02_CYCLES_PHYSIQUES/06_Cycle_effectif_basse_energie/00_Sources_docx/Source_docx_Fiche_alpha_G_M_Pl_B_v0_1.md` | 3 | — |

Ce tableau est produit par le script `audit/audit_placeholders.sh`.
Il reflete l'audit du 2026-07-13 (les fichiers de documentation README et CONVENTION_PLACEHOLDERS
peuvent afficher quelques faux positifs en raison des exemples dans les blocs de code).
Relancer le script pour obtenir les comptes a jour.

---

## 2. Statuts documentaires

L'ensemble du corpus utilise les statuts suivants.

| Statut | Sens | Usage |
|---|---|---|
| **Reference active** | Document a utiliser en priorite | Methode, carte, synthese transverse |
| **Protocole actif** | Document d'application reutilisable | Matrices de criblage, tests de resistance |
| **Consolidation** | Document qui stabilise un cycle ou une architecture | Notes d'architecture, syntheses de cycles |
| **Preuve locale** | Fiche ou cycle qui justifie une decision | Fiches physiques detaillees |
| **Consolidation historique recente** | Document recent mais supersede par une version ulterieure | Cartes et notes intermediaires |
| **Source primaire historique** | Document source anterieur encore porteur de matiere | DOCX ranges dans les dossiers thematiques `00_Sources_docx`, fiches initiales, tests, cartes anciennes |
| **Archive future** | Original conserve apres extraction et integration | DOCX apres remontee Markdown controlee |
| **A produire** | Document utile identifie mais non encore cree | Lacunes identifiees dans l'index |

---

## 3. Convention de statut dans les fichiers Source_docx

Chaque fichier `Source_docx_*` doit comporter un bloc de statut en tete.

Format recommande :

```markdown
## Statut

```text
lot: <numero> - <libelle du lot>
source physique: <nom du fichier DOCX source>
source physique path: <chemin thematique du fichier source>
sha256_source: <empreinte SHA-256 de la source>
statut: extraction textuelle de travail
document actif concerne: <reference au document actif>
controle attendu: <etape de verification>
```

> **Avertissement d'extraction** : ce fichier contient des placeholders
> `[  ]` correspondant a des passages incomplets (formules, tableaux, elements
> graphiques). Ne pas interpreter ces placeholders comme du contenu valide.
> Verifier contre le DOCX original avant toute reprise.
```

---

## 4. Priorites de correction

Les corrections de placeholders doivent etre realisees dans l'ordre suivant :

1. Fichiers de consolidation active ou reference active en premier.
2. Fichiers de preuve locale ensuite.
3. Sources primaires historiques en dernier.

Les extractions purement archivistiques (`Source_docx_*`) ne sont pas une
priorite de correction si leur synthese active est deja disponible.

---

## 5. Detection automatique

Commande de detection des placeholders :

```bash
bash audit/audit_placeholders.sh
```

Cette commande liste tous les fichiers Markdown contenant des placeholders
et leur nombre respectif.
