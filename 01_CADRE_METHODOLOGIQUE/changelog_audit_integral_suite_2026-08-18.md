# Changelog vivant de l’audit intégral — partie 2

## Fonction et rang

Ce document est la **partie 2 du même changelog vivant de l’audit intégral** commencé dans :

`01_CADRE_METHODOLOGIQUE/changelog_audit_integral.md`

Il ne constitue ni un journal secondaire, ni une synthèse, ni une mémoire allégée. La séparation en deux fichiers est uniquement technique : le connecteur GitHub disponible ne permettait pas un append/patch sûr du premier fichier sans reconstruction intégrale depuis des réponses potentiellement tronquées.

**Toutes les règles du changelog principal s’appliquent ici intégralement, sans exception, affaiblissement ni changement de rang.** Cela inclut notamment : couverture exhaustive du corpus de référence avant exclusion, conservation des faits et preuves des audits antérieurs, signalement des incidents, réduction seulement après remontée suffisante, obligation de mise à jour continue, lecture seule des objets audités mais écriture requise du changelog, et unité minimale d’entrée.

Cette continuité signifie en particulier qu’une lecture exhaustive ne peut pas être remplacée par une petite synthèse qui ferait disparaître des éléments uniques. Une entrée peut agréger plusieurs découvertes d’une même investigation, mais elle doit conserver assez de matière pour retrouver les acquis positifs, résultats négatifs, limites, dettes, contradictions, bifurcations, migrations, renommages, éléments resurgis, relations transversales, effets sur audits antérieurs, incidents, `NON_ETABLI` / `NON_DECIDABLE` et conséquences éventuelles.

```text
CHANGELOG_AUDIT_INTEGRAL_PARTIE_1 = changelog_audit_integral.md
CHANGELOG_AUDIT_INTEGRAL_PARTIE_2 = PRESENT_FICHIER
REGLES_PARTIE_1 -> PARTIE_2 = HERITAGE_INTEGRAL
PARTIE_2 = CONTINUATION_DIRECTE_DU_MEME_INSTRUMENT_DE_TRACABILITE
PARTIE_2 = SYNTHESE_SECONDAIRE = FAUX
LECTURE_EXHAUSTIVE -> COMPRESSION_AVEC_PERTE_D_ELEMENTS_UNIQUES = INTERDITE
UNITE_MINIMALE_D_ENTREE = IDENTIQUE_A_LA_PARTIE_1
NOUVELLE_AUTORITE_SCIENTIFIQUE = NON
REMPLACEMENT_DE_LA_PARTIE_1 = NON
FUSION_ULTERIEURE_AUTOMATIQUE = NON
```

Point de raccord vérifié avant création : le changelog principal courant, blob `1746c524e37c064ca043f49d8f1601ce816030d1`, se termine après la lecture de `04_ARCHITECTURES` et désigne `05_CARTES_ET_SYNTHESES` comme prochaine position documentaire propre.

Corpus de référence inchangé :

```text
BASELINE = 5ff45189af7087e1dd384bb815be55c3ff1430db
NOMBRE_EXACT_BLOBS_GIT = 668
LECTURE_DES_OBJETS_AUDITES = READ_ONLY_PAR_DEFAUT
ECRITURE_DU_PRESENT_CHANGELOG = AUTORISEE_ET_REQUISE
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

---

## 2026-08-18 — `06_PHILOSOPHIE` : clôture documentaire intégrale du baseline

La lecture des vingt-cinq Markdown restants et des deux reçus OpenTimestamps ferme le périmètre matériel du dossier.

```text
TREE_SHA_06 = 6f78cff0d7a74f1490a84a7f12aed39483835339
MARKDOWN_LUS_INTEGRALEMENT = 37/37
OTS_LUS_MATERIELLEMENT = 2/2
TOTAL_BLOBS_LUS = 39/39
DOCX = 0
COUVERTURE_DOCUMENTAIRE_06 = COMPLETE
REVALIDATION_HISTORIQUE_EXTERNE = NON
REVALIDATION_PHILOSOPHIQUE_EXTERNE = NON
```

### Programmes philosophiques : exécution et abandon ne doivent pas être confondus

Les programmes C2 et C3 restent des programmes soumis à validation dans leurs propres documents. Le programme C4/C5/C6 porte en revanche une couche de déclassement ultérieure : C5 a été exécuté et clos ; C4 reste à re-décider ; C6 a changé de nature et devient une jonction vers le versant physique plutôt qu’un sixième cycle philosophique.

```text
PROGRAMME_PRESENT_DANS_CORPUS -> EXECUTION = NON_PRESUME
C5_EXPORTABILITE = EXECUTE_ET_CLOS_DANS_LA_COUCHE_ULTERIEURE
C4 = A_REDECIDER
C6 = JONCTION_PHYSIQUE_PHILOSOPHIQUE, NON_SIXIEME_CYCLE
```

### Test de covariance : résultat favorable puis rétrogradation probatoire

`Test_covariance_architectures_v0_1.md` verrouille cinq prédictions sur les corrélations CODATA et rapporte cinq confirmations. Mais le même document instruit ensuite l’objection de tautologie : les architectures et les prédictions partageaient directement une partie de la structure publique de l’ajustement.

Le verdict est donc explicitement requalifié :

```text
COVARIANCE_CODATA = CONTROLE_DE_FIDELITE
PREUVE_FORTE_DE_LA_GRAMMAIRE = NON
« EXIGENCE_DE_L_AUDIT_SATISFAITE » = RETIREE_PAR_LE_DOCUMENT_LUI_MEME
```

Cette auto-rétractation est un résultat méthodologique important : un test peut passer numériquement tout en perdre une partie substantielle de son poids probatoire après examen de sa dépendance aux données de construction.

### Cycle C5 : quatre cas hors échantillon et portée bornée

Les quatre cas sont :

```text
C5-1 constante solaire : valeur nominale stabilisée d’un référent variable ;
C5-2 constantes de stabilité : effectivité indexée au milieu ;
C5-3 constante de Michaelis K_M : effectivité relative au modèle et aux conditions ;
C5-4 pi : cas de durcissement hors domaine empirique.
```

Les trois premiers produisent des qualifications différenciées ; le quatrième laisse volontairement vides les rangs physiques et refuse d’inventer un mode de « nécessité mathématique » pour absorber le cas.

Le verdict d’exportabilité doit rester borné aux cas testés :

```text
EXPORTABILITE_SUR_QUATRE_CAS = FAVORABLE_ET_DISCRIMINANTE
EXPORTABILITE_UNIVERSELLE = NON_ETABLIE
PI -> GRAMMAIRE_NON_TOTALISANTE_UNIVERSELLEMENT = NON_ETABLI
PI = CONTRE_TYPE_LOCAL_OU_LA_PROCEDURE_SAIT_EXCLURE_SANS_FORCAGE
```

### OpenTimestamps : antériorité technique, non validation substantielle

Les deux fichiers `.ots` sont présents comme blobs distincts et ont été lus matériellement en base64. Ils portent le format OpenTimestamps et accompagnent séparément :

```text
Test_C5_3_constante_Michaelis_predictions.md
Test_C5_4_constante_mathematique_predictions.md
```

```text
OTS_PRESENT_ET_DISTINCT = ETABLI
ANTERIORITE_TECHNIQUE_DES_FICHIERS_DE_PREDICTIONS = DOCUMENTEE
CONTENU_DES_PREDICTIONS_VALIDÉ_PAR_HORODATAGE = FAUX
HORODATAGE -> VERITE_SCIENTIFIQUE = FAUX
```

### Stern–Gerlach : calibration plutôt que nouvelle théorie de la mesure

Le dossier distingue explicitement : expérience historique de 1922, modèle quantique idéalisé et dispositifs modernes. Il sépare aussi les fonctions matérielles, opératoires, formelles, d’enregistrement, inférentielles, communicationnelles et pédagogiques.

Résultats documentaires robustes :

```text
EXPERIENCE_HISTORIQUE != MODELE_IDEAL != DISPOSITIF_MODERNE
SEPARATION != DETECTION != SELECTION != PREPARATION
STATISTIQUE_TERMINALE -> HISTOIRE_UNIQUE_DE_PREPARATION = FAUX
ABSENCE_D_ACCES_LOCAL_A_LA_PHASE -> DISPARITION_ONTOLOGIQUE_DE_COHERENCE = NON
```

Le dossier déclare lui-même que les distinctions formelles centrales sont largement occupées dans la littérature et ne revendique aucune nouvelle théorie de la mesure.

### Résurgence de la notion de coupe

`Pilote_Q1_Stern_Gerlach_matrice_fonctions_v0_1.md` et le verdict de première passe disent explicitement que `coupe` n’est pas encore un concept unique constitué. Le terme recouvre alors plusieurs partitions non équivalentes :

```text
matérielle ;
système / appareil ;
formelle ;
choix d’axe ;
coarse-graining ;
historique ;
pédagogique.
```

Qualification généalogique :

```text
COUPE_DANS_STERN_GERLACH = FAMILLE_DE_PARTITIONS_A_EFFETS_SPECIFIES
THEORIE_GENERALE_DE_LA_COUPE = NON_OBTENUE_A_CE_PALIER
EVOLUTION_ULTERIEURE_DU_CONCEPT = A_RECONSTRUIRE_TRANSVERSALEMENT, NON_A_RETROPROJETER
```

Cette résurgence est particulièrement importante pour un audit ultérieur du manuscrit/cadre, mais elle ne doit pas être relue à travers la définition plus tardive sans preuve de continuité.

### Interférence et information de chemin : contribution clarificatrice candidate

Le troisième test distingue cinq statuts d’information :

```text
encodée ;
accessible ;
lue ;
enregistrée ;
utilisée pour conditionner une inférence.
```

Il distingue aussi distributions marginales, conjointes et conditionnelles, et refuse les lectures rétrocausales naïves de l’« effacement ».

Mais l’évaluation finale est explicitement prudente :

```text
NOUVEAUTE_PHYSIQUE = AUCUNE_REVENDIQUEE
C0_CORRECTION_DOCUMENTATION = ETABLI
C1_COORDINATION_DE_COUCHES = ETABLI
C2_CONTRIBUTION_DIFFERENCIEE = PLAUSIBLE_A_CONTROLER_BIBLIOGRAPHIQUEMENT
C3_PROTOCOLE_TRANSFERABLE = NON_ETABLI
C4_NOUVEAUTE_SUBSTANTIELLE = NON_RECHERCHEE
```

Le dossier `06_PHILOSOPHIE` est donc fermé documentairement sans transformer sa richesse exploratoire en doctrine ou en résultat philosophique général.

Prochaine position documentaire propre : `90_Critiques_ constantes_effectives_stabilisees`.


---

## 2026-08-18 — `90_Critiques_ constantes_effectives_stabilisees` : reprise locale et controle des sources

### Perimetre et methode

La reprise commence a la position indiquee par la partie 2 du changelog :
`90_Critiques_ constantes_effectives_stabilisees`.

Le controle est effectue dans le clone local dedie a l'audit, sur la branche
`audit/changelog-reprise-2026-08-18`, au HEAD `e76c92da08aa9e84f62b28f5e88296b3f4ecab50`.
Le corpus scientifique et les donnees externes ne sont pas modifies.

Inventaire local du bloc au baseline :

```text
TOTAL_BLOBS_90 = 34
DOCX = 13
MARKDOWN = 13
PNG = 8
DOCX_SHA256_DECLARED_AND_MATCHED = 13/13
DOCX_WORD_DOCUMENT_XML_READ = 13/13
PNG_VISUALLY_INSPECTED = 8/8
EXTERNAL_SCIENTIFIC_REVALIDATION = NON
```

Les 13 extractions Markdown ont ete relues dans le cadre de cette reprise. Les
13 originaux DOCX ont ensuite ete ouverts localement et leur `word/document.xml`
a ete lu pour controler le texte structurel, les noeuds textuels et les tables
contenues dans le document. Les 13 SHA-256 declares dans les extractions
correspondent aux SHA-256 calcules sur les DOCX locaux. Une erreur apparente de
chemin pour quatre noms accentues provenait seulement du decodage de la sortie
PowerShell ; la verification par correspondance locale a confirme les quatre
hashes manquants.

Cette verification etablit la provenance et la couverture materielle locale.
Elle ne transforme pas l'extraction en equivalence generale de mise en page :
la presentation Word, les proprietes de style, les elements non contenus dans
`word/document.xml` et l'interpretation scientifique externe ne sont pas
revalides par cette operation.

### Les PNG sont des pieces documentaires, non de simples illustrations

Les huit PNG extraits des DOCX ont ete inspectes visuellement. Ils contiennent
des planches de synthese avec des titres, diagnostics, seuils, statuts et plans
d'action. Ils ne peuvent donc pas etre omis comme simples elements decoratifs.

Les formulations visuelles rendent notamment explicites :

```text
CONSOLIDATION -> SAS_DYNAMIQUE_VERS_REFERENCE = PROPOSITION_HISTORIQUE
AUCUNE_OUVERTURE_SANS_VERROUILLAGE_PREALABLE = PROPOSITION_HISTORIQUE
SEUIL_ARCHITECTURE >= 3_NOEUDS = CRITERE_PROPOSE
PROTOCOLE_H0_S8 > 5_SIGMA = CRITERE_PROPOSE
HIGGS_VS_DELTA_M2 = CADRAGE_NARRATIF_PROPOSE
REGIME_ET_ACCES_FUSIONNES = PROPOSITION_BORNEE_AUX_CONSTANTES_EFFECTIVES
TENSIONS -> STATUT_ONTOLOGIQUE_PROVISOIRE = PROPOSITION_HISTORIQUE
```

Ces formulations ont une fonction genealogique importante : elles montrent des
moments ou le projet, ou un agent de critique, a tente de durcir la taxonomie,
de transformer une tension en declencheur, ou de faire passer une architecture
d'un statut descriptif a un statut decisionnel. Elles ne constituent pas pour
cela des decisions humaines, des regles actuelles ou des autorisations de calcul.

### Acquis et propositions retrouvees dans les 13 DOCX

Les sources critiques convergent vers plusieurs lignes de travail :

- la distinction entre famille, fonction transversale et architecture est
  jugee insuffisamment decisionnelle dans plusieurs critiques ;
- la cosmologie est repetitivement decrite comme un reseau d'inferences et de
  tensions, avec des propositions de double etiquetage, de trajectoire
  diachronique et de tests de substitution ;
- les cas neutrino sont presentes comme un deplacement d'une constante-valeur
  vers des relations oscillatoires, avec une mise en avant des limites de
  l'acces PMNS aux phases de Majorana ;
- le SI 2019 est mobilise comme cas de distinction entre stabilisation empirique,
  fixation conventionnelle et realisation pratique ;
- plusieurs critiques demandent de remplacer un test de retrait binaire par un
  test de destabilisation, de substitution ou de resistance ;
- plusieurs engagements restent au statut `[TBD]`, sans preuve dans ce lot de
  leur execution ni de leur promotion durable.

Ces lignes se recoupent avec des resurgences deja notees dans les cycles et les
architectures, mais le recoupement ne vaut pas validation de la theorie proposee.
Les formulations fortes comme « automatiser la discipline », « indicateur de
rupture de validite », « statut ontologique provisoire » ou « effondrement
immediat du sens physique » restent des assertions a qualifier, non des verdicts.

### Controle de compatibilite avec le cadre courant

Le lot contient des prescriptions qui entrent potentiellement en tension avec
les regles actuellement applicables : promotion automatique d'une tension,
seuil universel de `5 sigma`, fusion generale du regime et de l'acces, blocage
automatique de nouveaux cycles, ou transformation d'un test editorial en
algorithme de decision.

Statut retenu :

```text
PRESCRIPTIONS_HISTORIQUES_DU_LOT = CONSERVEES
PROMOTION_AUTOMATIQUE_EN_REGLE_COURANTE = NON
SEUIL_UNIVERSEL_5_SIGMA = NON_VALIDE_COMME_REGLE_GENERALE
STATUT_ONTOLOGIQUE_D_UNE_TENSION = NON_PROMU
NOUVELLE_AUTORISATION_COMPUTATIONNELLE = AUCUNE
REVALIDATION_SCIENTIFIQUE_EXTERNE = NON_EFFECTUEE
```

Toute reutilisation de ces propositions doit etre instruite dans le domaine
competent, avec cible, transformation, regime, modele, tolerance et condition
de rupture explicites. En particulier, aucune proposition issue de ce lot
n'autorise un nouveau sampling, une modification de la partie computationnelle
ou une requalification de C7-C1 / C7-GAL.

### Etat de couverture et suite

Le bloc `90_Critiques_ constantes_effectives_stabilisees` est desormais couvert
materiellement dans cette reprise locale : les 13 Markdown, les 13 DOCX et les
8 PNG ont ete lus ou inspectes selon leur nature. Cette fermeture de couverture
ne ferme aucune qualification scientifique et ne supprime aucune dette de
revalidation externe.

```text
COUVERTURE_MATERIELLE_90 = COMPLETE
QUALIFICATION_SCIENTIFIQUE_90 = NON_OUVERTE_PAR_CETTE_LECTURE
PRESCRIPTIONS_A_RETESTER = OUI
DETTES_EXPLICITES_DU_LOT = CONSERVEES
PROCHAINE_ACTION = RECOUPER_90_AVEC_LES_ENTREES_ET_CARTES_DEJA_LUES
```

---

## 2026-08-18 — `90_Critiques_ constantes_effectives_stabilisees` : recoupement avec le cadre deja remonte

Le recoupement du lot 90 avec `Fiche_criblage_critiques_lot2_v0_1.md`,
`Addendum_matrice_criblage_lot2_v0_1.md`, `Passerelle_escalade_tensions_cosmologiques_v0_1.md`,
`Audit_resynchronisation_theorique_v0_1.md`, `Audit_dependances_et_reorganisation_v0_1.md`
et `Index_raisonne_du_corpus_v1_0.md` montre que les propositions fortes des DOCX
n'apparaissent pas comme des decisions isolees du lot 90.

### Continuites confirmees

```text
CLASSIFICATION_EN_SORTIE = DEJA_INTEGREE_COMME_COUCHE_DECISIONNELLE
COUPLAGE_FORT_REGIME_ACCES = DEJA_REMANIE_LOCALEMENT
TENSIONS = OBJETS_DE_PROTOCOLE, NON_ANOMALIES_AUTOMATIQUES
TEST_DE_RETRAIT = CONSERVE_ET_COMPLETE_PAR_DEGRADATION_SUBSTITUTION
TEMPORALITE_SCINDEE = DEJA_PORTEE_PAR_MATRICE_V0_2
ESCALADE = GRADUEE, SANS SAUT DIRECT TENSION -> ANOMALIE
RELATION = SOUS_AUDIT, NON_FAMILLE_REFUGE
```

La fiche de criblage transforme explicitement les propositions brutes du lot 2
en statuts differencies : `A integrer`, `A remanier`, `A tester`, `A tenir en
reserve` ou `A refuser comme telle`. L'addendum rend la classification finale
et les verrous d'options proceduraux, tout en maintenant la possibilite de
`classement differe`, `classement refuse` et `point de bascule candidat`.

La passerelle cosmologique interdit le saut direct d'une tension vers une
anomalie. Elle exige l'examen des routes d'acces, de leur independance, des
degenerescences, des systematiques, du modele de fond, de la temporalite et
d'une substitution controlee.

### Requalification des propositions du lot 90

```text
SEUIL_UNIVERSEL_5_SIGMA = REFUSE_COMME_REGLE_GENERALE
SEUIL_FIXE_TROIS_NOEUDS = REFUSE_COMME_QUANTIFICATION_UNIVERSELLE
FUSION_GENERALE_REGIME_ACCES = REFUSEE
STATUT_ONTOLOGIQUE_PROVISOIRE_D_UNE_TENSION = REMPLACE_PAR STATUT HEURISTIQUE PROBATOIRE
BLOCAGE_AUTOMATIQUE_DE_TOUT_NOUVEAU_CYCLE = NON_ADOPTE
MATHEMATISATION_TOTALE_DU_CORPUS = NON_ADOPTEE
```

Ces refus ne suppriment pas les objections dont les propositions procedaient.
Ils conservent leur fonction de falsification ou d'orientation : reduire
l'arbitraire des cas litigieux, rendre visibles les couplages, tester la
resilience et empecher une classification prematuree.

### Relation avec les documents de reorganisation

L'audit des dependances a deja etabli que les DOCX sont des pieces du socle et
que leur deplacement physique ne doit pas etre confondu avec une suppression,
une conversion ou une perte de provenance. L'index raisonne avait encore une
fonction de navigation et de classement qui devait etre corrigee par les
qualifications ulterieures ; il ne peut pas servir seul de preuve de pertinence
ou d'exhaustivite.

Le lot 90 renforce donc une conclusion documentaire, sans ouvrir de migration :
les sources DOCX, leurs extractions et leurs PNG doivent rester distinguables,
et les propositions historiques doivent rester recuperables sans etre
promues par simple presence dans une synthese.

### Statut de reprise

```text
RECOUPLEMENT_90_AVEC_CADRE_ANTERIEUR = EFFECTUE
CONTINUITE_METHODOLOGIQUE = CONFIRMEE_DANS_LE_PERIMETRE_LU
NOUVELLE_REGLE_SCIENTIFIQUE = AUCUNE
NOUVELLE_AUTORISATION_COMPUTATIONNELLE = AUCUNE
REINSTRUCTION_SUBSTANTIELLE = NON_OUVERTE
PROCHAINE_ETAPE = RECONSTRUIRE_LA_PORTE_DOCUMENTAIRE_SUIVANTE_SANS_EXCLUSION
```

---

## 2026-08-18 — `91_TRAVAUX_ANTERIEURS` : ouverture de la porte documentaire

Inventaire local au baseline courant :

```text
TOTAL_BLOBS_91 = 85
MARKDOWN = 82
DOCX = 2
JSON = 1
COUVERTURE_DOCUMENTAIRE_91 = OUVERTE
```

Le dossier contient des manuscrits, essais, recherches, registres de decisions,
archives conversationnelles et reconstructions genealogiques. Son README declare
qu'il s'agit d'une archive de trajectoire, non d'une autorite active, et demande
une comparaison avec l'etat courant avant toute reprise. Cette indication route
la lecture mais n'autorise aucune exclusion : les 85 blobs restent dans le
corpus jusqu'a leur lecture et leur remontee.

### Premiers points d'entree lus

Les points d'entree `README.md` et `SOURCE_HIERARCHY.md`, ainsi que les documents
recommandes `POSTURE_EPISTEMIQUE.md`, `ARCHEOLOGIE_BIFURCATIONS_fevrier-juin2026.md`,
`CHANGELOG_CONCEPTUEL.md`, `DECISION_LEDGER.md`, `Annexe_genealogique.md` et
`le_reglage_fin_v9.md` ont ete lus comme contexte historique.

Ils font remonter plusieurs elements qui devront etre distingues dans la suite :

```text
POSTURE_RELATIONNELLE_ET_REFLEXIVE = ORIENTATION_HISTORIQUE
COUPE_CONSTITUTIVE_UNIVERSELLE = THESIS_HISTORIQUE_RETIREE_OU_SUSPENDUE
COUPLAGE_STRUCTUREL_HORS_BIOLOGIE = EXTENSION_A_REINSTRUIRE
DEFINISSABILITE = QUESTION_HISTORIQUE, FONCTION_PORTEUSE_NON_TRANCHEE
PERCOLATION = PISTE_HISTORIQUE_A_REINSTRUIRE, NON_RESTAUREE
ORIGINALITE_THEORIQUE_FORTE = NON_DEMONTEE_DANS_LE_REGISTRE_LU
GAIN_METHODOLOGIQUE = A_TESTER_PAR_COMPARAISON_SOUSTRACTIVE
```

Le `DECISION_LEDGER` conserve des decisions historiques compatibles avec le
programme actuel sur plusieurs points : reconstruction disciplinaire avant
traduction, modalisation des propositions, possibilite d'echec, regionalisation
des concepts et interdiction des remplacements lexicaux globaux. En revanche,
`SOURCE_HIERARCHY.md` et la posture ancienne appartiennent a leur chantier de
phase 1 et ne remplacent pas le programme vivant actuel.

### Tension de methode conservee

La posture epistemique ancienne privilegie la justesse sur l'exhaustivite et
le dossier 91 se presente comme une archive a parcourir genealogiquement. Le
programme actuel exige au contraire la lecture exhaustive du corpus de reference
avant toute exclusion documentaire. La regle de reprise est donc :

```text
JUSTESSE_COMME_POSTURE_HISTORIQUE = CONSERVEE_COMME_CONTEXTE
EXHAUSTIVITE_DOCUMENTAIRE_ACTUELLE = REGLE_APPLICABLE
ARCHIVE_91_COMME_FILTRAGE_DE_PERTINENCE = REFUSE
ARCHIVE_91_COMME_SOURCE_D_AUTORITE_ACTIVE = REFUSE
```

Cette tension ne constitue pas une incoherence a corriger dans les anciens
documents. Elle doit etre conservee comme changement de programme et controlee
dans les lectures ulterieures, notamment lorsque des questions anciennes
resurgissent sous un vocabulaire plus recent.

### Etat et prochaine action

```text
COUVERTURE_MATERIELLE_91 = 0/85 A CE PALIER
POINTS_D_ENTREE_LUS = 8
DOCX_91_LUS_DIRECTEMENT = 0/2
JSON_91_LU_INTEGRALEMENT = 0/1
AUDIT_SCIENTIFIQUE_SUBSTANTIEL = NON_OUVERT
PROCHAINE_ACTION = LIRE_LES_REGISTRES_ET_CONTROLES_91_AVANT_LES_ARCHIVES_CONVERSATIONNELLES
```

---

## 2026-08-18 — `91_TRAVAUX_ANTERIEURS` : registres et controles de phase remontes

Les documents `CONCEPT_STATUS.md`, `OPEN_QUESTIONS.md`, `PHASE5_CONTROLE.md`,
`PHASE6_CONTROLE.md`, `PHASE7_CONTROLE.md`, `PHASE8_AUDIT_TRANSVERSAL.md` et
`PHASE8_CONTROLE.md` ont ete lus comme registres historiques et controles de
production. Ils ne remplacent pas le programme vivant actuel, mais ils rendent
la genealogie des retraits, suspensions, regionalisations et validations locales
plus explicite.

### Continuite avec les regles actuellement applicables

```text
COUPE = FAMILLE_CANDIDATE, INVARIANT_TRANSVERSAL_NON_ETABLI
TOUTE_COUPE_EST_CONSTITUTIVE = RETIREE
COUPLAGE_STRUCTUREL = REGIONALISE, TRADUCTION_INDEPENDANTE_REQUISE
ONTO_EPISTEMOLOGIE_FORTE = SUSPENDUE
POROSITE_GENERALE = RETIREE_OU_SUSPENDUE
SEDIMENTATION = REGIONALISEE
ORIGINALITE_THEORIQUE_FORTE = NON_DEMONTEE
EXEMPLES_SCIENTIFIQUES = TERRAINS_D_EPREUVE, NON_PREUVES_DU_CADRE
MIGRATION = LOCALE, NON_SUBSTITUTIVE
```

Les controles de phase 5 a 8 confirment que la v13 est une architecture de
travail coherente et conditionnelle, non une theorie transversale demontree.
Ils conservent les echecs possibles : redescription, retrait, suspension,
fragmentation, regionalisation, inapplicabilite, deformation, refutation locale
et redondance conceptuelle. Cette memoire negative est compatible avec la
fonction du changelog et ne doit pas etre lissée en bilan positif.

### Questions et limites resurgies

Les questions suivantes restent ouvertes dans les registres lus :

```text
INVARIANT_MINIMAL_DE_COUPE = OUVERT_STRUCTURANT
GAIN_NON_REDONDANT = METHODOLOGIQUEMENT_DISPONIBLE, PEU_TESTE_SUR_DOSSIERS_COMPLETS
VOISINS_PAR_SOURCES_PRIMAIRES = OUVERT_BIBLIOGRAPHIQUE
EXEMPLES_SCIENTIFIQUES_COMPLETS = OUVERT_DISCIPLINAIRE
CONSTITUTION_ET_CO_CONSTITUTION = CHARGE_DE_PREUVE_FORTE
ONTO_EPISTEMOLOGIE_FORTE = SUSPENDUE
```

Le dossier README signale par ailleurs deux renvois absents dans
`MANUSCRIT_LIVRE_soustraction_de_soi.md`. Ils sont conserves comme anomalies
documentaires ; ils ne seront ni reconstruits ni remplaces par conjecture.

### Statut intermediaire

```text
REGISTRES_91_LUS = 7
COUVERTURE_MATERIELLE_91 = INCOMPLETE
DOCX_91_LUS_DIRECTEMENT = 0/2
JSON_91_LU_INTEGRALEMENT = 0/1
ARCHIVES_CONVERSATIONNELLES = NON_OUVERTES_A_CE_PALIER
AUDIT_SCIENTIFIQUE_SUBSTANTIEL = NON_OUVERT
PROCHAINE_ACTION = LIRE_LES_CONTROLES_RESTANTS_ET_LES_DOCUMENTS_DE_TRAVAIL_CIBLES
```

---

## 2026-08-18 — `91_TRAVAUX_ANTERIEURS` : migrations et prose historique recoupees

Les documents `M_migrations.md`, `T0_MANUSCRIT_NOUVEAU.md`,
`RECHERCHE_CONTRE_SOI_T1.md`, `essai_suspension_categories.md` et
`phenomenologie_des_coupes.md` ont ete lus dans cette passe.

### Resultat principal

Les textes historiques portent encore, avec des degres de modalisation variables,
des formulations que les registres K/M et l'audit transversal ont depuis
retirees, suspendues ou regionalisees :

```text
TOUTE_COUPE_EST_CONSTITUTIVE = THESIS_HISTORIQUE_NON_ACTIVE
POROSITE_COMME_CATEGORIE_GENERALE = THESIS_HISTORIQUE_NON_ACTIVE
COUPLAGE_STRUCTUREL_ETENDU = EXTENSION_HISTORIQUE_A_REINSTRUIRE
CO_CONSTITUTION_UNIVERSELLE = HYPOTHESE_HISTORIQUE_FORTE, NON_PREMISSE
LEGIFERATION_UNIVERSELLE = PROPOSITION_METAPHYSIQUE_HISTORIQUE, SUSPENDUE
REEL_AUTO_INTERROGATIF = FORMULATION_PHENOMENOLOGIQUE/METAPHORIQUE, NON_RESULTAT
```

Le texte `M_migrations.md` ne demande pas de corriger ces documents historiques.
Il impose de qualifier chaque occurrence selon sa fonction : citation, trace
genealogique, critique, hypothese locale, argument actuel ou formulation a
retirer. Cette regle est compatible avec l'exigence actuelle de conservation
sans promotion.

### Recoupements et limites

`RECHERCHE_CONTRE_SOI_T1.md` apporte une critique importante des pretentions
d'originalite : Barad et Spencer-Brown sont des antecedents directs a confronter,
le couplage structurel reste d'abord biologique, et l'originalite theorique
forte ne peut pas etre deduite de l'absence d'une expression exacte dans la
litterature. Ces observations recoupent P8-003 et la typologie des voisins,
mais le rapport de recherche lui-meme reste une piece historique, non une
validation bibliographique actuelle.

`T0_MANUSCRIT_NOUVEAU.md` contient un partage utile entre physique standard,
proposition philosophique et statut modal, mais il conserve aussi des claims
de second ordre qui exigeraient un audit disciplinaire avant toute reprise.

`essai_suspension_categories.md` et `phenomenologie_des_coupes.md` conservent
des noyaux phenomenologiques et pedagogiques, mais leurs termes generaux
(`porosite`, `coupes vivantes`, `ethique de la reliance`, `reel auto-interrogatif`)
ne sont pas automatiquement des concepts du cadre actuel. Ils doivent rester
des matériaux de genese et des candidats a instruire.

### Statut intermediaire

```text
TEXTES_CIBLES_LUS_DANS_CETTE_PASSE = 5
COUVERTURE_MATERIELLE_91 = INCOMPLETE
CONCEPTS_HISTORIQUES_RESURGIS = CONSERVES_SANS_PROMOTION
REINSTRUCTION_SCIENTIFIQUE = NON_OUVERTE
PROCHAINE_ACTION = CONTINUER_LES_CONTROLES_91_ET_LES_DOCUMENTS_DE_TRAVAIL_NON_LUS
```

---

## 2026-08-18 — `91_TRAVAUX_ANTERIEURS` : premieres pieces brutes etat intermediaire

Les deux DOCX et l'export JSON du dossier ont ete ouverts localement pour
controle materiel. L'export JSON a une taille de `693199` octets et contient
une version assainie des conversations : les identifiants, URL signees et
metadonnees techniques sans fonction documentaire sont retires, tandis que
les contenus de messages, titres, horodatages et roles sont conserves.

### Refondation du cadre

Le DOCX `Projet de refondation du cadre des coupes constitutives.docx` confirme
explicitement la requalification v12 -> v13 :

```text
TOUTE_COUPE_EST_CONSTITUTIVE = INTENABLE_ET_RETIREE
CO_CONSTITUTION_GENERALE = INTENABLE_ET_RETIREE
GRADIENT_PHYSIQUE_BIOLOGIQUE_REFLEXIF = RETIRE
DESTINS_TRANSVERSAUX = RETIRES
POROSITE_GENERALE = RETIREE
SEDIMENTATION_UNIVERSELLE = RETIREE
VARIATION_LOCALE = INSUFFISANTE_COMME_PREUVE_DE_TRANSVERSALITE
MIGRATION_PAR_REMPLACEMENT_LEXICAL = INTERDITE
PROGRAMME_COMPARATIF_V13 = ORIENTATION_RETENUE
```

Cette pièce renforce la continuité avec le programme et les registres déjà
lus ; elle ne constitue pas une autorisation de réactiver les formulations
qu'elle décrit comme historiques.

Le DOCX `motif_coupe_constitutive.docx` est un essai philosophique transversal
ancien, structuré autour de la complémentarité, de la perception, de la Gestalt,
de la métastabilité et des coupes agentielles. Il doit être lu comme une pièce
généalogique et un candidat de comparaison, non comme une preuve d'invariant
transversal ou d'originalité théorique.

### Export conversationnel

La structure JSON montre des conversations assainies contenant des propositions,
des corrections, des hésitations et des formulations explicitement non canoniques.
Les messages ne seront pas traités comme décisions humaines par défaut. Leur
lecture doit préserver les bifurcations et les corrections, sans exposer les
métadonnées retirées ni convertir les suggestions de modèles en autorité.

```text
DOCX_CONTROLE_MATERIEL = 2/2
JSON_STRUCTURE_CONTROLEE = OUI
JSON_LECTURE_CONVERSATIONNELLE_COMPLETE = NON_ETABLIE_A_CE_PALIER
COUVERTURE_MATERIELLE_91 = INCOMPLETE
AUDIT_SCIENTIFIQUE_SUBSTANTIEL = NON_OUVERT
PROCHAINE_ACTION = POURSUIVRE_LA_LECTURE_JSON_ET_DES_PIECES_91_RESTANTES
```

---

## 2026-08-18 — `91_TRAVAUX_ANTERIEURS` : cartographie minimale de l'export conversationnel

L'export JSON assaini contient `30` conversations. Un index local a ete produit
sans identifiants, URL, chemins de telechargement ni contenu de messages :

```text
CONVERSATIONS = 30
MESSAGES_ET_ROLES = CONSERVES_DANS_L_EXPORT
METADONNEES_TECHNIQUES_SENSIBLES = RETIREES_PAR_L_ASSAINISSEMENT
LECTURE_INTEGRALE_DES_MESSAGES = NON_ETABLIE_A_CE_PALIER
```

Les titres font apparaitre plusieurs foyers distincts : hard problem et
cognition, temps cosmologique, trous noirs, conscience, manuscrits, critiques
et cartes conceptuelles. Cette pluralite interdit de reconstruire une trajectoire
unique a partir des titres. Elle servira seulement a ordonner la lecture des
messages, en conservant les bifurcations et les corrections comme materiaux
historiques.

Les pieces jointes mentionnees dans l'export ne sont pas presumees accessibles
ni equivalentes aux blobs presents dans le corpus. Leur nom ou leur taille ne
constitue pas une preuve de lecture, et aucune extraction absente ne sera
reconstruite par conjecture.

```text
INDEX_CONVERSATIONNEL = ETABLI
COUVERTURE_MATERIELLE_91 = INCOMPLETE
ARCHIVE_JSON = TOUJOURS_OUVERTE
AUDIT_SCIENTIFIQUE_SUBSTANTIEL = NON_OUVERT
PROCHAINE_ACTION = LIRE_LES_CONVERSATIONS_PAR_FOYERS_SANS_PROMOTION_AUTOMATIQUE
```
