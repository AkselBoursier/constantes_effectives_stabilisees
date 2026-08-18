# Suite du changelog vivant de l’audit intégral — 2026-08-18

## Fonction et rang

Ce document est un **journal complémentaire de continuité** du fichier :

`01_CADRE_METHODOLOGIQUE/changelog_audit_integral.md`

Il est créé à la demande explicite de l’auteur le 2026-08-18, après constat que le connecteur GitHub disponible n’expose pas d’opération d’append ou de patch textuel sur un fichier existant, mais seulement un remplacement UTF-8 intégral.

La création de cette suite évite de reconstruire le changelog principal depuis une réponse tronquée et donc de risquer une perte de mémoire d’audit.

```text
CHANGELOG_PRINCIPAL = CONSERVE_INCHANGE
CHANGELOG_COMPLEMENTAIRE = MEMOIRE_DE_CONTINUITE_AUTORISEE_PAR_L_AUTEUR
NOUVELLE_AUTORITE_SCIENTIFIQUE = NON
REMPLACEMENT_DU_CHANGELOG_PRINCIPAL = NON
FUSION_ULTERIEURE_AUTOMATIQUE = NON
RECONCILIATION_ULTERIEURE = A_FAIRE_EXPLICITEMENT_SI_UN_PATCH_SUR_DEVIENT_DISPONIBLE
```

Point de raccord vérifié avant création : le changelog principal courant, blob `1746c524e37c064ca043f49d8f1601ce816030d1`, se termine après la lecture de `04_ARCHITECTURES` et désigne `05_CARTES_ET_SYNTHESES` comme prochaine position documentaire propre.

Corpus de référence inchangé :

```text
BASELINE = 5ff45189af7087e1dd384bb815be55c3ff1430db
NOMBRE_EXACT_BLOBS_GIT = 668
LECTURE_DES_OBJETS_AUDITES = READ_ONLY_PAR_DEFAUT
ECRITURE_DU_PRESENT_JOURNAL = AUTORISEE
```

---

## 2026-08-18 — `05_CARTES_ET_SYNTHESES` : clôture non-DOCX

Arbre baseline :

```text
TREE_SHA_05 = 9cb52afb3b5dc208aca108027945c3c4c5ee0c5a
TOTAL_BLOBS = 141
MARKDOWN = 133
TSV = 1
DOCX = 7
```

Couverture atteinte :

```text
MARKDOWN_LUS_INTEGRALEMENT = 133/133
TSV_LU_INTEGRALEMENT = 1/1
OBJETS_NON_DOCX_LUS = 134/134
DOCX_ORIGINAUX_LUS_DIRECTEMENT = 0/7
EQUIVALENCE_DOCX_EXTRACTION_MD = NON_ETABLIE
COUVERTURE_NON_DOCX_05 = COMPLETE
COUVERTURE_DOCUMENTAIRE_GLOBALE_05 = INCOMPLETE
```

Les sept DOCX originaux demeurent une dette de lecture directe. Cette dette n’est pas contournable par simple invocation des extractions Markdown : le corpus contient lui-même la règle selon laquelle une extraction ne remplace pas sa source et qu’une restitution incertaine doit revenir à l’original.

### Distinction retrouvée : suffisance locale != exhaustivité

Les plans et synthèses de remontée des sources DOCX montrent que la phase pré-Cercle 2 avait volontairement adopté une **suffisance architecturale ciblée** : relire ce qui pouvait modifier le rang des architectures avant leur reprise, sans remonter tout le corpus physique.

La synthèse de suffisance précise explicitement que ce seuil :

```text
!= epuisement des DOCX
!= archivage final
!= genealogie complete
```

Conséquence pour le présent audit :

```text
SEUIL_DE_SUFFISANCE_ANTERIEUR_ATTEINT -> CORPUS_EXHAUSTIVEMENT_LU = FAUX
CONVERSION_DOCX_VERS_MD_PRODUITE -> EQUIVALENCE_SOURCE_EXTRACTION = FAUX
```

Cette résurgence renforce directement la règle actuelle d’exhaustivité sans créer de nouvelle règle.

### Plans, programmes et abandons documentés

Plusieurs documents de `05` sont des programmes, plans ou sas dont le statut a ensuite changé. Leur présence ne doit pas être convertie en dette automatiquement.

Exemple net : `Plan_instruction_echelles_philosophiques_v0_1.md` porte un déclassement indiquant que P0, E-1 et E0 ont été exécutés, mais que E1, E2, E3 et la synthèse finale ne doivent pas être produits.

```text
LIVRABLE_PLANIFIE_MAIS_EXPLICITEMENT_ABANDONNE -> DETTE_OMISE = NON_PRESUME
ABSENCE_DE_LIVRABLE = A_LIRE_AVEC_STATUT_DU_PLAN
```

Cette structure est cohérente avec le statut général du dépôt comme laboratoire en évolution.

### Généalogie du premier dégagement de thèse

Les versions `Premier_degagement_these_v0_1`, `v0_2` et `v0_3` montrent une correction doctrinale substantielle :

```text
v0.1 : borne / reconstruction / constitution encore traitées comme « modes de constance » ;
v0.2 : priorité locale du test de ce qui tient ;
v0.3 : désubstantialisation du « porteur », T0 requalifié en règle normative d’attribution,
       introduction explicite de la suspension,
       abandon de « constante effective » comme classe transversale.
```

Ce trajet ne doit pas être aplati en doctrine moyenne.

```text
TRANSFORMATION_DE_VOCABULAIRE = TRANSFORMATION_DE_RANG_ET_DE_PROBLEME_DANS_CE_CAS
FUSION_DES_VERSIONS_EN_DOCTRINE_MOYENNE = REFUSEE
```

### Rectification de la séquence objet / constitution / accès

`Rectification_acces_trajectoires_stabilisation_v0_1.md` retire explicitement l’ordre linéaire :

`constitution -> objet -> accès`

comme règle générale et le remplace par une boucle contrôlée dont le point d’entrée dépend du cas. Le même document retire aussi `fixité dynamique` du vocabulaire général.

Cette correction est un exemple de laboratoire où une règle ayant d’abord corrigé un excès antérieur est ensuite elle-même jugée trop rigide.

### Dé-promotion de plusieurs intuitions fortes

Les registres de critiques et d’originalité montrent que plusieurs notions ont été volontairement ramenées à un rang plus faible :

```text
pouvoir de refus = surpromu dans une phase antérieure ;
hiérarchie objet / constitution / accès = surpromue dans une phase antérieure ;
H0 comme cas négatif central = surpromu dans une phase antérieure ;
originalité physique forte = NON_ETABLIE ;
originalité conceptuelle forte = NON_ETABLIE ;
originalité comparative / méthodologique = PLAUSIBLE_MAIS_A_DEMONTRER.
```

Le verdict d’originalité versionné autorise alors :

```text
O0 = ETABLI
O1 = FORTEMENT_PLAUSIBLE
O2 = A_TESTER
O3 = NON_ETABLI
O4 = NON_REVENDIQUE
```

Ces niveaux sont historiques et ne sont pas réévalués scientifiquement par la présente lecture.

### Réserve pédagogique

Les analogies retirées des arguments n’ont pas été simplement perdues : elles sont conservées dans une réserve pédagogique avec désanalogies, points d’arrêt et inférences interdites.

```text
RETRAIT_D_UNE_ANALOGIE_DU_NOYAU_ARGUMENTATIF -> PERTE_DOCUMENTAIRE = FAUX_DANS_CE_CAS
CONSERVATION_HEURISTIQUE != VALIDATION_DOCTRINALE
```

### Réécriture historique de PR #14

`Rapport_recriture_historique_PDF_PR14_v0_1.md` et `Mapping_SHA_recriture_PDF_PR14_2026-07-18.tsv` documentent une opération technique de réécriture de l’historique avec table `old -> new` commit par commit.

Le TSV a été lu intégralement. Il contient à la fois des SHA inchangés et des SHA réécrits lorsque l’ascendance est affectée. La tête historique annoncée `7b2d330... -> e545233...` est présente dans la table.

```text
MAPPING_SHA_PR14 = PROVENANCE_TECHNIQUE_LUE
RESULTAT_SCIENTIFIQUE_NOUVEAU = NON
```

### Synthèses architecturales : rang historique

`Synthese_architectures_inter_familles_v1_0.md` stabilise historiquement quatre formes : constitutive, définitionnelle, validité, inférentielle/reconstructive, et propose une grammaire commune de solidarité, régime, accès, stabilisation et limite.

Cette synthèse est à conserver comme étape de la généalogie. Sa propre descendance documentaire montre ensuite des refontes et corrections ; sa présence ne suffit donc pas à promouvoir les quatre formes comme ontologie courante du projet.

### Refondation des cycles

`synthese-refondation-des-cycles.md` se qualifie elle-même comme synthèse substantielle datée, non tableau de bord courant ni autorité opérationnelle présente.

Elle soutient alors notamment :

```text
fixité d’un coefficient != stabilité d’une prédiction != validité d’une description ;
exactitude définitionnelle != invariance physique != précision empirique ;
fixé dans un modèle ou un ajustement != constant physiquement.
```

Elle conserve une réponse provisoire à « qu’est-ce qu’une constante physique ? » et une hypothèse pluraliste, tout en déclarant plusieurs thèses non établies.

Cette couche reste un fait généalogique important, sans être promue par défaut comme formulation terminale.

---

## 2026-08-18 — `06_PHILOSOPHIE` : ouverture et état intermédiaire

Arbre baseline établi :

```text
TREE_SHA_06 = 6f78cff0d7a74f1490a84a7f12aed39483835339
TOTAL_BLOBS = 39
MARKDOWN = 37
OPENTIMESTAMPS_OTS = 2
DOCX = 0
```

État de lecture au moment de cette entrée :

```text
MARKDOWN_LUS = 12/37
OTS_LUS_MATERIELLEMENT = 0/2
COUVERTURE_06 = EN_COURS
```

Markdown lus à ce palier :

```text
README.md
Carte_philosophie_implicite_corpus_v0_1.md
Audit_solidite_v0_1.md
Situation_01_processus_expansion_acces_v0_1.md
Situation_02_Dirac_Eddington_grands_nombres_v0_1.md
Situation_03_SI_2019_convention_vecue_v0_1.md
Situation_04_Regime_gris_electrique_1990_2019_v0_1.md
Situation_05_Duhem_Quine_architectures_v0_1.md
Situation_06_Bachelard_rectification_CODATA_v0_1.md
Situation_07_Mach_Planck_v0_1.md
Synthese_premier_cycle_situations_v0_1.md
Releve_paysage_contemporain_v0_1.md
```

### Rang explicite de la branche philosophique

Le README fixe historiquement une discipline forte :

```text
exploration plutôt que rédaction ;
situations plutôt que catalogues ;
proposition plutôt que décision.
```

La carte de philosophie implicite déclare ses lignes comme engagements à instruire, non comme doctrine. L’audit de solidité interroge explicitement le risque que le rédacteur-modèle fabrique une cohérence séduisante.

```text
BRANCHE_06 -> DOCTRINE_ACTIVE = NON_PRESUME
IMPLICITE_CARTOGRAPHIE -> THESE_ENDOSSEE = NON
CONVERGENCE_NARRATIVE_ELEGANTE -> PREUVE = NON
```

### Risque structurel explicitement reconnu par le corpus

`Audit_solidite_v0_1.md` identifie trois explications concurrentes au fait que les premiers cas ne faisaient pas échouer la grille :

```text
(a) grille effectivement bonne ;
(b) sélection de cas favorables ;
(c) optimisation narrative du rédacteur-modèle / LLM.
```

Le document conclut qu’un audit interne supplémentaire ne peut pas départager ces possibilités et recommande un test dur dont le corpus ne contrôle pas la réponse.

Cette autocritique est un élément intellectuel important à conserver : le projet avait déjà identifié la différence entre cohérence rédactionnelle et résistance externe.

### Tension S03 / H1

`Situation_03_SI_2019_convention_vecue_v0_1.md` appelle localement le SI 2019 « preuve institutionnelle » de l’hypothèse H1.

Mais `Audit_solidite_v0_1.md` classe :

```text
H1 = P6 = hypothèse non testée ;
S03 = pièce favorable la plus présentable du triplet historique ;
S04 et S07 = dettes de vérification plus fortes.
```

Qualification retenue par le présent audit :

```text
S03 = CAS_FORT_POUR_H1
S03 -> H1_ETABLIE = NON
FORMULATION « PREUVE_INSTITUTIONNELLE_DE_H1 » = SURPROMOTION_LOCALE_HISTORIQUE
```

Aucune correction du fichier source n’est effectuée.

### Tension Situation 05 / audit de solidité

`Situation_05_Duhem_Quine_architectures_v0_1.md` emploie localement des formulations fortes telles que « position originale confirmée » et présente le test de retrait comme mesure du degré de holisme.

Or l’audit de solidité indique qu’au moment de son diagnostic aucun test dur extérieur capable de produire un « non » indépendant de la grille n’avait encore été exécuté.

Qualification retenue :

```text
TYPAGE_DES_SOLIDARITES = PROPOSITION_INTERESSANTE_A_CONSERVER
TEST_DE_RETRAIT_COMME_OUTIL = A_EPROUVER
« POSITION_ORIGINALE_CONFIRMEE » = AUTO_VALIDATION_TROP_FORTE_A_CE_PALIER
PROMOTION_EN_RESULTAT_PHILOSOPHIQUE_GENERAL = NON_ETABLIE
```

### Fonctions positives déjà remontées des situations 01–07

Sans valider leurs reconstructions historiques contre les sources externes, la lecture documentaire fait remonter plusieurs fonctions intellectuelles :

```text
- distinction influence causale / convergence sans causalité / intrication différée ;
- pluralité des lectures des grands nombres : nécessité, historicisation, sélection, conditionnement ;
- distinction grandeur / valeur numérique / unité / définition / réalisation dans le SI ;
- régime gris électrique comme cas de décalage documenté entre pratique et système légal ;
- typage local des solidarités et question du retrait ;
- rectification CODATA et covariance comme piste de contrôle externe ;
- distinction grandeur / unité / réalisation dans la querelle Mach–Planck.
```

Ces fonctions sont conservées comme matière philosophique et généalogique ; leur exactitude historique ou leur originalité philosophique ne sont pas revalidées par la seule lecture du dépôt.

### Prochaine étape

Poursuivre exhaustivement les 25 Markdown restants et les deux fichiers `.ots`, sans utiliser le README ou la synthèse du premier cycle comme substituts.
