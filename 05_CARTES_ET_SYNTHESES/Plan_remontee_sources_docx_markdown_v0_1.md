# Plan de remontee des sources DOCX en Markdown v0.1

## Sources primaires historiques, extraction et integration

### 1. Fonction du document

Ce document corrige une ambiguite de vocabulaire documentaire.

Les fichiers `.docx` initialement a la racine ne doivent pas etre traites
comme des archives au sens faible.

Ils sont :

```text
des sources primaires historiques du corpus,
porteuses de la matiere conceptuelle et theorique initiale.
```

Ils ne deviendront des archives qu'apres :

```text
1. extraction lisible ;
2. remontee en Markdown ;
3. table de correspondance ;
4. integration explicite dans les cycles, notes ou cartes actifs ;
5. verification que rien d'important n'est perdu.
```

### 2. Constat actuel

Inventaire apres consolidation :

```text
60 fichiers DOCX ranges dans les dossiers thematiques `00_Sources_docx` ;
1 fichier Ecriture.txt lie a la fiche Lambda et range avec le lot 1B ;
61 extractions Markdown tracees dans le registre des sources primaires.
```

Un audit existe deja :

```text
05_CARTES_ET_SYNTHESES/Audit_dependances_et_reorganisation_v0_1.md
```

Cet audit a correctement pose que les Word initialement a la racine ne sont
pas des archives.

Mais il preparait surtout une reorganisation physique.

La tache presente ajoute un autre objectif :

```text
remonter la matiere source en Markdown exploitable,
deplacer les originaux sans les modifier vers leur dossier thematique,
et conserver une table de correspondance verifiable.
```

### 3. Decision de priorite

Decision :

```text
avant d'ouvrir le cercle 2 des architectures actives,
ouvrir un traitement de fond des sources DOCX primaires.
```

Raison :

```text
les architectures actives ne doivent pas etre seulement nettoyees
depuis les consolidations Markdown recentes ;
elles doivent pouvoir etre relues a partir de leur matiere source.
```

Le cercle 2 n'est pas annule.

Il est reconditionne :

```text
cercle 2 = reecriture positive des architectures
apres identification des sources DOCX utiles a chaque architecture.
```

### 4. Statuts documentaires corriges

| Statut | Sens | Action |
|---|---|---|
| Source primaire historique | DOCX porteur de matiere initiale | Extraire et remonter |
| Source de preuve locale | Fiche physique DOCX | Convertir vers le cycle concerne |
| Source de synthese initiale | Synthese DOCX de cycle ou carte ancienne | Comparer avec la synthese Markdown active |
| Source methodologique fondatrice | Brief, methode, regime, addendum, note critique | Remonter dans le cadre methodologique |
| Source d'architecture | Note ou cycle DOCX utile a une architecture | Lire avant reecriture du cercle 2 |
| Archive future | Original conserve apres extraction et integration | Classer seulement apres verification |

Regle :

```text
un fichier source ne devient archive qu'apres remontee controlee.
```

### 5. Methode de remontee

Chaque fichier ou lot de fichiers doit suivre le meme protocole.

```text
1. Identifier le fichier source et son statut.
2. Extraire le texte en Markdown de travail.
3. Conserver le nom du fichier source dans l'en-tete.
4. Distinguer extraction, synthese et integration.
5. Signaler les formulations depassees sans les effacer.
6. Rattacher le Markdown produit au cycle, a l'architecture ou a la note active.
7. Produire une ligne de correspondance source -> Markdown -> document actif.
```

Format recommande pour les fichiers Markdown de remontee :

```text
Source_docx_<nom_ascii>_v0_1.md
```

Le fichier source d'origine reste inchange, conserve dans le dossier
`00_Sources_docx` correspondant.

### 6. Lots de traitement

#### Lot 0 : socle methodologique

Documents :

```text
PROJECT_BRIEF.docx
Methode v0.1.docx
Regimes de constance.docx
Note de synthese methodologique.docx
Addendum methodologique v0.2.docx
Note critique de compression v0.1.docx
```

Objectif :

```text
remonter la genealogie methodologique,
les definitions initiales,
les tensions deja apercues,
et les formulations qui restent fecondes.
```

#### Lot 1 : fiches physiques sources

Documents :

```text
fiches alpha, masses, rapports, QCD, electroweak, neutrinos,
metrologie, CKM, syntheses de cycles initiales.
```

Objectif :

```text
reconstituer la matiere locale des cycles
avant de juger qu'une fiche Markdown recente suffit.
```

#### Lot 2 : tests taxonomiques

Documents :

```text
Test des familles fragiles.docx
Test de la famille Seuil.docx
Test de la famille Fond.docx
Test de la famille Relation v0.1.docx
```

Objectif :

```text
retrouver les problemes conceptuels initiaux,
en les relisant avec le double niveau fonction directrice /
famille fonctionnelle controlee.
```

#### Lot 3 : sources d'architecture

Documents :

```text
Note de consolidation saveur-Higgs v0.1.docx
Cycle effectif basse energie v0.1.docx
Cycle effectif basse energie v0.2.docx
Cycle effectif basse energie v0.3.docx
```

Objectif :

```text
preparer le cercle 2 des architectures actives
sur une base source, pas seulement sur les consolidations recentes.
```

#### Lot 4 : genealogie des cartes

Documents :

```text
Carte consolidee v0.1 a v0.5, v0.7, v0.8.
```

Objectif :

```text
documenter l'evolution des positions,
sans confondre ancienne carte et carte active.
```

#### Lot 5 : critiques constructives

Documents :

```text
90_Critiques_ constantes_effectives_stabilisees/*.docx
```

Objectif :

```text
maintenir le lien entre les critiques source et les choix deja integres.
```

### 7. Garde-fous

Ne pas faire :

```text
supprimer les DOCX ;
deplacer les DOCX hors du chemin declare dans la table et le registre ;
renommer les DOCX ;
traiter les DOCX comme secondaires ;
convertir en Markdown puis effacer les formulations initiales ;
ouvrir le cercle 2 sans relire les sources d'architecture utiles.
```

Faire :

```text
extraire,
relire,
annoter,
integrer,
et seulement ensuite archiver au sens strict.
```

### 8. Etat de la remontee

La table et la conversion complete sont maintenant produites :

```text
05_CARTES_ET_SYNTHESES/Table_remontee_sources_docx_v0_1.md
05_CARTES_ET_SYNTHESES/Registre_sources_primaires_v0_1.md
```

Le registre fixe les emplacements physiques, les sorties Markdown et les
empreintes SHA-256. Les futures reprises se concentrent donc sur la lecture,
la comparaison et l'integration, non sur la recuperation de fichiers racine.

Premier lot ouvert :

```text
01_CADRE_METHODOLOGIQUE/00_Sources_docx/
01_CADRE_METHODOLOGIQUE/Synthese_recuperation_lot0_socle_methodologique_v0_1.md
```

Deuxieme lot ouvert :

```text
03_TESTS_TAXONOMIQUES/
03_TESTS_TAXONOMIQUES/Synthese_recuperation_tests_taxonomiques_v0_1.md
```

Troisieme lot ouvert :

```text
04_ARCHITECTURES/00_Sources_docx/Source_docx_Note_consolidation_saveur_Higgs_v0_1.md
02_CYCLES_PHYSIQUES/06_Cycle_effectif_basse_energie/00_Sources_docx/Source_docx_Cycle_effectif_basse_energie_v0_1.md
02_CYCLES_PHYSIQUES/06_Cycle_effectif_basse_energie/00_Sources_docx/Source_docx_Cycle_effectif_basse_energie_v0_2.md
02_CYCLES_PHYSIQUES/06_Cycle_effectif_basse_energie/00_Sources_docx/Source_docx_Cycle_effectif_basse_energie_v0_3.md
04_ARCHITECTURES/Synthese_recuperation_sources_architecture_lot3_v0_1.md
```

Traitement cible pre-Cercle 2 ouvert :

```text
05_CARTES_ET_SYNTHESES/Seuil_suffisance_avant_cercle2_v0_1.md
02_CYCLES_PHYSIQUES/04_Cycle_thermo_metrologique/Synthese_recuperation_thermo_metrologique_SI_v0_1.md
02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/Synthese_recuperation_sources_saveur_Higgs_cible_v0_1.md
02_CYCLES_PHYSIQUES/06_Cycle_effectif_basse_energie/Synthese_comparaison_alphaG_MPl_sources_v0_1.md
05_CARTES_ET_SYNTHESES/Synthese_suffisance_pre_cercle2_v0_1.md
```

Statut :

```text
seuil de suffisance atteint pour ouvrir ensuite le cercle 2 ;
remontee physique complete reportee, non annulee.
```

### 9. Formule de cloture

> Les DOCX ne sont pas des dechets de l'ancienne structure ; ils sont la matiere premiere que la structure actuelle doit apprendre a rendre lisible.
