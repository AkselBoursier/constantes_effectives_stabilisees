# Audit des dependances et reorganisation documentaire v0.1

## Inventaire, references croisees, anomalies et table de correspondance

> **Statut post-migration** : cet audit decrit l'inventaire avant classement.
> Les 47 DOCX et le fichier texte initialement a la racine, ainsi que les
> critiques, sont maintenant ranges sans renommage dans leurs dossiers
> thematiques. Voir
> [Registre_sources_primaires_v0_1.md](Registre_sources_primaires_v0_1.md)
> pour l'etat physique et les empreintes actuels.

### 1. Fonction de l'audit

L'index v1.0 fixait la regle :

```text
ne pas deplacer ni renommer les fichiers Word racine
tant que les dependances internes ne sont pas verifiees.
```

Cet audit execute cette verification.

Il prepare la reorganisation physique validee dans le cadrage v0.2, sous la
correction de statut actee :

```text
les documents Word de la racine ne sont pas des archives ;
ils sont le socle fondateur du projet.
```

### 2. Perimetre

```text
47 fichiers .docx a la racine
1 fichier .txt a la racine (Ecriture.txt)
25 fichiers .md dans l'arborescence 01 / 02 / 04 / 05
```

### 3. Resultat de l'audit des dependances

#### 3.1 Nature des references

Toutes les references des fichiers Markdown vers les fichiers Word sont
nominales : elles citent un nom de document dans des listes de sources.

```text
aucun lien hypertexte, aucun chemin relatif, aucune inclusion.
```

Consequence :

```text
un deplacement ne casse aucun lien technique ;
il exige seulement une table de correspondance pour la tracabilite.
```

#### 3.2 Fichiers Word cites par des documents Markdown

| Fichier Word cite | Cite par |
|---|---|
| PROJECT_BRIEF.docx | methodes v1.1 / v1.2, revision v0.1, index, cartes v0.9 / v1.0 / v1.1, les 7 fiches + synthese du cycle cosmologique, les 3 notes d'architecture, synthese du cycle effectif |
| Test de la famille Seuil.docx | methode v1.1, notes v1.1, revision v0.1 |
| Test de la famille Fond.docx | methode v1.1, notes v1.1, revision v0.1, cycle cosmologique v0.1 et v0.2 |
| Test de la famille Relation v0.1.docx | methode v1.1, notes v1.1, revision v0.1 |
| Note de consolidation saveur-Higgs v0.1.docx | methode v1.1, notes v1.1, revision v0.1, index (sans extension) |
| Note de synthese methodologique.docx | methode v1.1, notes v1.1, revision v0.1 |
| Methode v0.1.docx | revision v0.1 |
| Regimes de constance.docx | revision v0.1 |
| Note critique de compression v0.1.docx | revision v0.1 |
| Addendum methodologique v0.2.docx | revision v0.1 |
| Carte consolidee v0.8.docx | cycle cosmologique v0.1, architecture effective, carte v0.9 |
| Cycle effectif basse energie v0.1 / v0.2 / v0.3.docx | architecture effective basse energie |

Les autres fichiers Word (fiches physiques, syntheses de cycles, cartes
anterieures) ne sont pas cites nominalement par les Markdown : ils sont
couverts par des mentions generiques ("documents Word racine", "fiches
initiales").

#### 3.3 Anomalies relevees

| Anomalie | Constat | Decision requise |
|---|---|---|
| Duplicat alpha_G | `Fiche alpha_G - M_Pl.docx` et `Fiche alpha_G - M_Pl (1).docx` ont des contenus differents (sommes de controle distinctes) | comparer les deux versions, designer la version de reference, conserver l'autre avec mention |
| Ecriture.txt | contient le texte source de `Fiche Lambda v0.1.docx` sous un nom sans rapport | renommer en clair ou classer avec la fiche Lambda |
| Carte v0.6 absente | la serie des cartes Word va de v0.1 a v0.8 sans v0.6 | confirmer si la v0.6 a existe ; documenter la lacune dans la genealogie |
| Index v1.0 | classe les Word racine comme "archives historiques" | correction de statut a reporter dans le futur index v2.0 |

### 4. Statut corrige du socle fondateur

L'audit applique la decision d'Aksel :

```text
socle fondateur = documents de plein rang, integres a l'arborescence
selon leur fonction, non relegues dans un dossier d'archives.
```

Consequences :

```text
1. Les fiches Word rejoignent les cycles physiques dont elles sont les preuves.
2. Les tests taxonomiques recoivent le dossier que l'index anticipait deja
   (03_TESTS_TAXONOMIQUES).
3. Les documents fondateurs de methode rejoignent 01_CADRE_METHODOLOGIQUE
   dans un sous-dossier de socle.
4. Les cartes anterieures rejoignent 05_CARTES_ET_SYNTHESES dans un
   sous-dossier de genealogie : elles documentent l'evolution de la carte,
   fonction distincte de la carte active.
5. Aucun fichier n'est renomme. Aucun contenu n'est modifie.
```

### 5. Arborescence cible

```text
constantes_effectives_stabilisees/
|
|-- 00_README/
|   |-- README.md                       (a produire : renvois index / methode / carte / chronologie)
|   |-- Table_de_correspondance_v1_0.md (issue de cet audit)
|
|-- 01_CADRE_METHODOLOGIQUE/
|   |-- 00_Socle_fondateur/
|   |   |-- PROJECT_BRIEF.docx
|   |   |-- Regimes de constance.docx
|   |   |-- Methode v0.1.docx
|   |   |-- Note de synthese methodologique.docx
|   |   |-- Addendum methodologique v0.2.docx
|   |   |-- Note critique de compression v0.1.docx
|   |   |-- Note de synthese methodologique.docx (version Word)
|   |-- notes methodologiques Markdown actives et anterieures
|
|-- 02_CYCLES_PHYSIQUES/
|   |-- 01_Cycle_couplages_echelles_QCD/
|   |   |-- Fiche a v0.1.docx, Fiche masse de l'electron.docx,
|   |   |-- Fiche rapport proton-electron.docx, Fiche alpha_s - Lambda_QCD.docx
|   |   |-- Synthese du premier cycle v0.1.docx
|   |-- 02_Cycle_structurant_electrofaible/
|   |   |-- Fiche (v) v0.1.docx, Fiche Yukawa v0.1.docx, Fiche G_F v0.1.docx,
|   |   |-- Fiche -(-theta_W-) v0.1.docx, Fiche alpha_G - M_Pl.docx (+ duplicat),
|   |   |-- Fiche Lambda v0.1.docx (cas-limite cosmologique du cycle), Ecriture.txt
|   |   |-- Synthese du second cycle v0.1.docx
|   |-- 03_Cycle_neutrinos/
|   |   |-- Fiche neutrinos v0.1.docx, Fiche Delta m^2.docx,
|   |   |-- Fiche Angles de Melange Leptoniques.docx, Fiche delta_CP v0.1.docx,
|   |   |-- Fiche masse absolue des neutrinos.docx
|   |   |-- Synthese du troisieme cycle v0.1.docx
|   |-- 04_Cycle_thermo_metrologique/
|   |   |-- Fiche k_B v0.1.docx, Fiche N_A v0.1.docx, Fiche R v0.1.docx
|   |   |-- Synthese du quatrieme cycle.docx
|   |-- 05_Cycle_CKM_saveur/
|   |   |-- Fiche CKM v0.1.docx, Fiche Wolfenstein v0.1.docx
|   |   |-- Synthese du cycle CKM v0.1.docx
|   |-- 06_Cycle_effectif_basse_energie/
|   |   |-- (md existants) + Cycle effectif basse energie v0.1 / v0.2 / v0.3.docx
|   |-- 07_Cycle_cosmologique/          (inchange)
|   |-- 08_Cycle_metrologique_SI/       (inchange)
|
|-- 03_TESTS_TAXONOMIQUES/
|   |-- Test des familles fragiles.docx
|   |-- Test de la famille Seuil.docx
|   |-- Test de la famille Fond.docx
|   |-- Test de la famille Relation v0.1.docx
|
|-- 04_ARCHITECTURES/
|   |-- (md existants)
|   |-- Note de consolidation saveur-Higgs v0.1.docx
|   |-- Architecture_saveur_Higgs_notes.md (version Markdown produite ensuite)
|
|-- 05_CARTES_ET_SYNTHESES/
|   |-- (md actifs : carte v1.1, synthese transverse, index, audit)
|   |-- Genealogie_cartes/
|   |   |-- Carte consolidee v0.1 a v0.5, v0.7, v0.8 (Word)
|   |   |-- Carte_consolidee_v0_9.md, Carte_consolidee_v1_0.md
|   |-- Syntheses_transverses_anterieures/
|   |   |-- Note de synthese methodologique.docx (si distincte du socle : a confirmer)
|   |   |-- Note de consolidation saveur-Higgs v0.1.docx (si non rangee en 04)
```

Points laisses ouverts :

```text
1. Fiche Lambda : rattachee au second cycle (cas-limite) ou au cycle
   cosmologique (objet) ; le second cycle est propose par fidelite genetique.
2. Note de consolidation saveur-Higgs : 04 (fonction architecturale) propose
   plutot que 05 (synthese), car l'index la designe deja comme document
   principal de l'architecture.
3. Test des familles fragiles / Test de la famille Seuil : verifier si le
   premier englobe le second avant de figer la table.
```

### 6. Table de correspondance (resume par groupes)

| Groupe (racine actuelle) | Nombre | Destination |
|---|---|---|
| Documents fondateurs de methode | 6 | 01_CADRE_METHODOLOGIQUE/00_Socle_fondateur/ |
| Fiches cycle 1 (alpha, m_e, m_p/m_e, alpha_s) + synthese | 5 | 02/01_Cycle_couplages_echelles_QCD/ |
| Fiches cycle 2 (v, Yukawa, G_F, theta_W, alpha_G x2, Lambda) + synthese + Ecriture.txt | 9 | 02/02_Cycle_structurant_electrofaible/ |
| Fiches cycle 3 (neutrinos) + synthese | 6 | 02/03_Cycle_neutrinos/ |
| Fiches cycle 4 (k_B, N_A, R) + synthese | 4 | 02/04_Cycle_thermo_metrologique/ |
| Fiches cycle 5 (CKM, Wolfenstein) + synthese | 3 | 02/05_Cycle_CKM_saveur/ |
| Cycle effectif basse energie v0.1-0.3 | 3 | 02/06_Cycle_effectif_basse_energie/ |
| Tests taxonomiques | 4 | 03_TESTS_TAXONOMIQUES/ |
| Note de consolidation saveur-Higgs | 1 | 04_ARCHITECTURES/ |
| Cartes consolidees v0.1-0.8 | 7 | 05/Genealogie_cartes/ |
| Note de synthese methodologique (Word), Note de synthese methodologique.docx | 1 | 01/00_Socle_fondateur/ |
| PROJECT_BRIEF.docx | 1 | 01/00_Socle_fondateur/ (copie de reference en 00_README envisageable) |

La table nominative complete, fichier par fichier, sera produite comme :

```text
00_README/Table_de_correspondance_v1_0.md
```

au moment de la migration, avec l'etat avant / apres.

### 7. Regles de migration

```text
1. Migration seulement apres validation de cet audit par Aksel.
2. Deplacement sans renommage : les noms Word restent intacts, accents compris.
3. Table de correspondance produite le meme jour que la migration.
4. Mise a jour de l'index (v2.0) dans la meme sequence : statut socle
   fondateur, nouveaux chemins, correction "archives historiques".
5. Verification apres migration : recompte des 47 + 1 fichiers,
   aucun orphelin a la racine hors README.
6. Les anomalies (duplicat alpha_G, Ecriture.txt, carte v0.6) sont
   tranchees avant ou pendant la migration, pas apres.
```

### 8. Ce que l'audit ne fait pas

```text
1. Il ne modifie aucun contenu.
2. Il ne deplace encore aucun fichier.
3. Il ne convertit pas les Word en Markdown : le socle fondateur reste
   dans son format d'origine ; toute conversion serait un projet distinct.
4. Il ne remplace pas l'index : il prepare sa v2.0.
```

### 9. Formule de cloture

```text
l'audit confirme que la reorganisation est sure :
les dependances sont nominales, les anomalies sont locales,
et le socle fondateur peut rejoindre l'arborescence sans perte.
```

Formule finale :

> Reorganiser le corpus, ce n'est pas archiver son origine ; c'est donner au socle fondateur sa place de plein rang dans la structure qu'il a rendue possible.
