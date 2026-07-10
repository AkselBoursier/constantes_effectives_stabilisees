# Source DOCX - PROJECT_BRIEF_v0_1

## Statut

```text
lot: 0 - socle methodologique
source physique: PROJECT_BRIEF.docx
statut: extraction textuelle de travail
document actif concerne: Methode v1.3 ; carte consolidee v1.2 ; index raisonne
controle attendu: Extraction + comparaison
```

## Limite

```text
Cette extraction ne remplace pas le DOCX source.
Elle rend la matiere lisible en Markdown pour comparaison et integration.
La mise en page Word n'est pas reconstruite.
```

## Extraction

### PROJECT_BRIEF.md

#### Projet : Constantes effectives stabilisées

#### 1. Objet du projet

Ce projet explore l’idée de constantes effectives stabilisées.

La question directrice est :

Dans quelle mesure certaines grandeurs physiques aujourd’hui traitées comme constantes peuvent-elles être comprises comme des constantes effectives stabilisées, c’est-à-dire comme des valeurs définissables, mesurables et stables à l’intérieur de régimes physiques déterminés ?

L’objectif n’est pas de proposer une nouvelle théorie physique, ni de remplacer la physique existante. L’objectif est de produire une cartographie méthodologique des statuts de constance : couplages, échelles, relations, raccordements effectifs, orientations, conventions, fonctions transversales et architectures inter-familles.

La formule actuellement stabilisée est :

Une constante effective stabilisée n’est pas seulement une valeur stable ; c’est une fonction robuste dans un régime, connue par un accès déterminé, stabilisée selon un mode précis, et parfois inscrite dans une architecture plus vaste.

#### 2. État actuel du projet

Le cadre est actuellement stabilisé autour de six familles fonctionnelles supérieures :

Couplage
Paramétrer une intensité ou une interaction.
Exemples : α, αs(Q²), yf, αG(E).

Échelle
Fixer, révéler ou hiérarchiser une échelle physique.
Exemples : v, MW, ΛQCD, MPl.

Relation
Stabiliser une liaison entre grandeurs, régimes, niveaux ou spectres.
Exemples : mp/me, R = NA kB, Δm², mf = yf v / √2.
Attention : cette famille doit toujours être sous-typée.

Raccordement
Relier une description effective à une description plus complète.
Exemple central : GF.

Orientation
Stabiliser un désalignement entre bases, champs, états ou secteurs.
Exemples : θW, CKM, PMNS, phases CP.

Convention
Fixer exactement une valeur dans un système métrologique.
Exemples : kB, NA, R.

Deux anciennes familles ont été rétrogradées :

Seuil n’est plus une famille supérieure. C’est une fonction transversale : limite, borne, passage, ancrage, validité.

Fond n’est plus une famille supérieure. C’est une fonction architecturale, surtout dans l’architecture cosmologique.

Les architectures inter-familles actuellement reconnues sont :

Architecture saveur-Higgs
Échelle + Couplage + Relation + Orientation.

Architecture métrologique SI
Convention + Relation + Échelle.

Architecture effective basse énergie
Raccordement + Échelle + Couplage + Relation, encore en cours de test.

Architecture cosmologique
Nécessaire, mais délicate : elle mélange constantes, paramètres de modèle, observables reconstruites, conditions initiales et tensions de données.

#### 3. Ce qui était en cours au moment du basculement

Le travail en cours était un cycle effectif basse énergie, destiné à tester l’architecture encore provisoire :

Architecture effective basse énergie = raccordement + échelle de validité + couplage de régime + fonction seuil éventuelle.

Trois fiches ont été produites dans ce cycle :

GF
Cas central du raccordement effectif basse énergie.
GF condense, à basse énergie, l’effet de l’échange du boson W.

MW
Cas d’échelle de validité.
MW est d’abord une échelle électrofaible, puis joue une fonction de seuil de validité pour la théorie de Fermi.

αs(Q²) / ΛQCD
Cas de couplage courant + échelle dynamique.
Ce cas corrige une vision trop simple de l’effectivité : en QCD, le régime basse énergie n’est pas une simple simplification ; il correspond à l’entrée dans le non-perturbatif.

La prochaine fiche logique serait :

αG(E) / MPl
Pour tester la gravitation comme théorie effective basse énergie et l’échelle de Planck comme limite de validité attendue.

Question de la prochaine fiche :

Comment une interaction extrêmement faible à basse énergie peut-elle signaler une limite d’effectivité à très haute énergie ?

#### 4. Architecture de répertoire recommandée

Proposition de structure Windows-compatible :

constantes_effectives_stabilisees/
│
├── 00_README/
│   ├── PROJECT_BRIEF.md
│   ├── GENEALOGIE_DOCUMENTS.md
│   ├── CONSIGNES_AGENT_LOCAL.md
│   └── LEXIQUE_COURT.md
│
├── 01_CADRE_METHODOLOGIQUE/
│   ├── Note_synthese_methodologique_v1_0.md
│   ├── Carte_consolidee_v0_8.md
│   ├── Carte_consolidee_v0_7.md
│   ├── Carte_consolidee_v0_6.md
│   ├── Carte_consolidee_v0_5.md
│   ├── Carte_consolidee_v0_4.md
│   └── Notes_methodologiques_intermediaires/
│       ├── Note_critique_compression_v0_1.md
│       ├── Addendum_methodologique_v0_2.md
│       └── Note_methodologique_v0_1.md
│
├── 02_CYCLES_PHYSIQUES/
│   ├── 01_Cycle_couplages_echelles_QCD/
│   │   ├── Fiche_01_alpha.md
│   │   ├── Fiche_02_me.md
│   │   ├── Fiche_03_mp_sur_me.md
│   │   ├── Fiche_04_alpha_s_Lambda_QCD.md
│   │   └── Synthese_cycle_1.md
│   │
│   ├── 02_Cycle_electrofaible_Higgs_faible_cosmo/
│   │   ├── Fiche_05_v_Higgs.md
│   │   ├── Fiche_06_Yukawa.md
│   │   ├── Fiche_07_alphaG_MPl.md
│   │   ├── Fiche_08_GF.md
│   │   ├── Fiche_09_thetaW.md
│   │   ├── Fiche_10_Lambda_cosmologique.md
│   │   └── Synthese_cycle_2.md
│   │
│   ├── 03_Cycle_neutrinos/
│   │   ├── Fiche_11_neutrinos_vue_ensemble.md
│   │   ├── Fiche_12_Delta_m2.md
│   │   ├── Fiche_13_angles_PMNS.md
│   │   ├── Fiche_14_delta_CP.md
│   │   ├── Fiche_15_masse_absolue_neutrinos.md
│   │   └── Synthese_cycle_3.md
│   │
│   ├── 04_Cycle_thermo_metrologie/
│   │   ├── Fiche_16_kB.md
│   │   ├── Fiche_17_NA.md
│   │   ├── Fiche_18_R.md
│   │   └── Synthese_cycle_4.md
│   │
│   ├── 05_Cycle_CKM/
│   │   ├── Fiche_19_CKM.md
│   │   ├── Fiche_20_Wolfenstein.md
│   │   └── Synthese_cycle_CKM_v0_1.md
│   │
│   └── 06_Cycle_effectif_basse_energie/
│       ├── Cycle_effectif_basse_energie_v0_1_GF.md
│       ├── Cycle_effectif_basse_energie_v0_2_MW.md
│       ├── Cycle_effectif_basse_energie_v0_3_alpha_s_Lambda_QCD.md
│       └── A_FAIRE_Fiche_4_alphaG_MPl.md
│
├── 03_TESTS_TAXONOMIQUES/
│   ├── Test_familles_fragiles_v0_1.md
│   ├── Test_Seuil_v0_1.md
│   ├── Test_Fond_v0_1.md
│   └── Test_Relation_v0_1.md
│
├── 04_ARCHITECTURES_INTER_FAMILLES/
│   ├── Note_consolidation_saveur_Higgs_v0_1.md
│   ├── Architecture_metrologique_SI_notes.md
│   ├── Architecture_effective_basse_energie_notes.md
│   └── Architecture_cosmologique_notes.md
│
├── 05_CARTES_ET_SYNTHESES/
│   ├── Carte_consolidee_v0_1.md
│   ├── Carte_consolidee_v0_2.md
│   ├── Carte_consolidee_v0_3.md
│   ├── Carte_consolidee_v0_4.md
│   ├── Carte_consolidee_v0_5.md
│   ├── Carte_consolidee_v0_6.md
│   ├── Carte_consolidee_v0_7.md
│   └── Carte_consolidee_v0_8.md
│
├── 06_DEFINITIONS_ET_TABLES/
│   ├── Definitions_stabilisees.md
│   ├── Table_familles_fonctions_architectures.md
│   ├── Matrice_canonique_v0_8.md
│   └── Glossaire_symboles.md
│
├── 07_SOURCES_ET_CITATIONS/
│   ├── SOURCES_A_VERIFIER.md
│   ├── PDG_CKM_notes.md
│   ├── PDG_QCD_notes.md
│   ├── SI_2019_notes.md
│   ├── Planck_DESI_cosmologie_notes.md
│   └── Neutrinos_KATRIN_NuFIT_notes.md
│
└── 99_ARCHIVES/
    ├── versions_anciennes/
    ├── fragments_non_classes/
    └── exports_bruts_chatgpt/

#### 5. Ordre recommandé de lecture pour un agent local

L’agent ne doit pas commencer par les fiches physiques isolées. Il doit d’abord comprendre la carte finale, puis remonter la généalogie.

Ordre recommandé :

00_README/PROJECT_BRIEF.md

01_CADRE_METHODOLOGIQUE/Carte_consolidee_v0_8.md

01_CADRE_METHODOLOGIQUE/Note_synthese_methodologique_v1_0.md

03_TESTS_TAXONOMIQUES/Test_Seuil_v0_1.md

03_TESTS_TAXONOMIQUES/Test_Fond_v0_1.md

03_TESTS_TAXONOMIQUES/Test_Relation_v0_1.md

04_ARCHITECTURES_INTER_FAMILLES/Note_consolidation_saveur_Higgs_v0_1.md

02_CYCLES_PHYSIQUES/06_Cycle_effectif_basse_energie/

Les cycles physiques antérieurs, dans l’ordre numérique.

Les anciennes cartes consolidées seulement si l’agent doit comprendre l’évolution historique.

#### 6. Généalogie courte du projet

##### Phase 1 — Constitution du corpus initial

Les premières fiches testent plusieurs types de constantes :

α : couplage électromagnétique stabilisé.

me : masse fermionique liée au régime électrofaible brisé.

mp/me : rapport stratifié entre QCD et électrofaible.

αs / ΛQCD : couplage courant et échelle dynamique.

Résultat : apparition des premières familles Couplage, Échelle, Relation.

##### Phase 2 — Extension électrofaible, faible, gravitationnelle et cosmologique

Fiches principales :

v : échelle structurante du régime électrofaible.

Yukawa : couplages de texture.

αG / MPl : couplage gravitationnel effectif et échelle de Planck.

GF : raccordement effectif basse énergie.

θW : orientation de jauge.

Λ : première hypothèse de famille Fond.

Résultat : apparition de Raccordement, Orientation, Fond.

##### Phase 3 — Neutrinos

Fiches principales :

Δm² : relation spectrale et déphasage oscillatoire.

PMNS : orientation de saveur oscillatoire.

δCP : orientation complexe CP.

masse absolue neutrinos : d’abord classée comme Seuil, puis reclassée comme relation spectrale d’ancrage à fonction seuil.

Résultat : clarification entre relation spectrale, orientation, phase, seuil et borne.

##### Phase 4 — Thermodynamique et métrologie

Fiches principales :

kB : constante définissante primaire du kelvin.

NA : constante définissante primaire de la mole.

R = NA kB : constante exacte par composition.

Résultat : apparition de la famille Convention et distinction forte entre stabilisation empirique et stabilisation conventionnelle.

##### Phase 5 — CKM et orientation

Fiches principales :

CKM : orientation de saveur transitionnelle.

Wolfenstein : coordonnées hiérarchiques de l’orientation CKM.

Résultat : consolidation de la famille Orientation.
Décision importante : l’oscillation n’est pas une famille ; c’est une manifestation locale de l’orientation dans le secteur neutrino.

##### Phase 6 — Saveur-Higgs

Document principal :

Note_consolidation_saveur_Higgs_v0_1.md

Résultat : introduction d’une distinction majeure entre :

famille fonctionnelle ;

architecture inter-familles.

La saveur-Higgs n’est pas une famille. C’est une architecture articulant :

Échelle + Couplage + Relation + Orientation.

##### Phase 7 — Cartes consolidées v0.5 à v0.8

La carte évolue vers une structure à plusieurs niveaux.

Décisions majeures :

Seuil est rétrogradé en fonction transversale.

Fond est rétrogradé en fonction architecturale.

Relation survit comme famille supérieure, mais doit toujours être sous-typée.

Le noyau final contient six familles :
Couplage, Échelle, Relation, Raccordement, Orientation, Convention.

##### Phase 8 — Cycle effectif basse énergie

Documents produits :

Cycle_effectif_basse_energie_v0_1_GF.md

Cycle_effectif_basse_energie_v0_2_MW.md

Cycle_effectif_basse_energie_v0_3_alpha_s_Lambda_QCD.md

Résultat actuel :

L’architecture effective basse énergie est renforcée. Elle ne se réduit pas à l’intégration d’un médiateur massif. Elle comprend au moins deux formes d’effectivité :

Effectivité par intégration d’un médiateur massif
Exemple : GF / MW.

Effectivité par flot de couplage et changement de régime
Exemple : αs(Q²) / ΛQCD.

Prochaine fiche recommandée :

αG(E) / MPl.

#### 7. État conceptuel final à respecter

L’agent local doit respecter les décisions suivantes.

##### 7.1 Ne pas réintroduire Seuil comme famille

Seuil est une fonction transversale.

Exemples :

MW : échelle à fonction seuil.

ΛQCD : échelle dynamique à fonction seuil.

masse absolue neutrino : relation spectrale d’ancrage à fonction seuil.

##### 7.2 Ne pas réintroduire Fond comme famille

Fond est une fonction architecturale dans l’architecture cosmologique.

Λ n’est plus simplement “famille Fond”.
Formulation correcte :

Λ est un terme de fond dans l’architecture cosmologique ; sa valeur est fortement stabilisée comme paramètre du modèle ΛCDM, mais son statut physique profond et son caractère strictement constant restent ouverts.

##### 7.3 Toujours qualifier Relation

Ne jamais écrire seulement :

famille Relation

sans préciser :

relation stratifiée ;

relation compositionnelle ;

relation spectrale ;

relation constitutive de régime ;

relation d’état ;

relation normalisée.

##### 7.4 Ne pas confondre famille et architecture

Une famille classe la fonction principale d’une grandeur.

Une architecture décrit l’articulation de plusieurs familles dans un secteur.

Exemple :

CKM appartient à la famille Orientation.

CKM appartient aussi à l’architecture saveur-Higgs.

##### 7.5 Ne pas confondre régime physique et régime d’accès

Exemple :

régime physique de GF : interaction faible basse énergie ;

régime d’accès de GF : durée de vie du muon.

Exemple :

régime physique de αs(Q²) : QCD selon l’échelle de résolution ;

régime d’accès : extractions multi-processus, évolution RG, valeur de référence à MZ.

#### 8. Matrice canonique à utiliser pour les nouvelles fiches

Chaque nouvelle fiche doit idéalement contenir :

| Critère | Question |
|---|---|
| Grandeur | De quoi parle-t-on exactement ? |
| Type logique | Valeur, rapport, couplage, échelle, angle, phase, matrice, coefficient, paramètre ? |
| Dimension | Dimensionnée ou sans dimension ? |
| Famille principale | Couplage, Échelle, Relation, Raccordement, Orientation ou Convention ? |
| Sous-type local | Quelle qualification précise est nécessaire ? |
| Fonction transversale éventuelle | Seuil, borne, validité, déphasage, hiérarchie ? |
| Fonction architecturale éventuelle | Fond, paramètre d’état, densité normalisée, relation d’état, condition initiale ? |
| Régime de définition physique | Dans quel domaine la grandeur joue-t-elle un rôle ? |
| Régime d’accès épistémique | Comment est-elle mesurée, reconstruite, fixée ou bornée ? |
| Dépendance d’échelle | Court-elle avec une échelle ou dépend-elle d’un schéma ? |
| Stabilisation empirique | Forte, partielle, en cours, bornée, modèle-dépendante, ouverte ? |
| Stabilisation conventionnelle | Définissante, exacte par composition, mesurée dans le système, non concernée ? |
| Architecture éventuelle | Saveur-Higgs, SI, effective basse énergie, cosmologique ? |
| Limites | Ce que cette grandeur ne dit pas |

#### 9. Prochaine tâche recommandée pour l’agent local

Commencer par produire :

02_CYCLES_PHYSIQUES/
└── 06_Cycle_effectif_basse_energie/
    └── Cycle_effectif_basse_energie_v0_4_alphaG_MPl.md

Sujet :

[ G(E),M{} ]

Question directrice :

Comment une interaction extrêmement faible à basse énergie peut-elle signaler une limite d’effectivité à très haute énergie ?

Objectif :

Tester une troisième forme d’effectivité :

GF / MW : effectivité par intégration d’un médiateur massif.

αs(Q²) / ΛQCD : effectivité par flot de couplage et changement de régime.

αG(E) / MPl : effectivité gravitationnelle par couplage dimensionné et limite de validité attendue.

La fiche devra éviter deux erreurs :

traiter G isolément comme une constante comparable à α ;

traiter MPl comme une frontière nette plutôt que comme une échelle de validité attendue.

#### 10. Consigne de style pour l’agent

Le style attendu est :

sobre ;

conceptuellement précis ;

non spéculatif au-delà des sources ;

prudent sur les données récentes ;

structuré en fiches autonomes ;

toujours attentif aux distinctions de rang.

Éviter :

inflation de catégories ;

formulation “théorie du Tout” ;

métaphysique non contrôlée ;

assimilation de tous les paramètres à des constantes fondamentales ;

réintroduction de catégories déjà rétrogradées.

Règle générale :

Une bonne taxonomie ne nomme pas chaque différence ; elle décide quelles différences méritent un rang.
