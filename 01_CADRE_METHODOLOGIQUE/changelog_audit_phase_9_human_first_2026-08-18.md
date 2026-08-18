# Changelog de la phase 9 — normalisation documentaire Human-First

## Fonction et rang

Journal de cadrage et d'execution de la phase 9 Human-First. Cette phase ne
supprime pas l'histoire du laboratoire et ne transforme pas les documents
publics en compte rendu de fabrication.

Regles heritees :

- `01_CADRE_METHODOLOGIQUE/programme_audits.md`, sections 1.7, 1.8 et regle
  Human-First representation publique / laboratoire ;
- journaux des phases 1 a 8 ;
- `01_CADRE_METHODOLOGIQUE/Reecriture_positive_vocabulaire_v0_1.md` ;
- `01_CADRE_METHODOLOGIQUE/Protocole_travail_redaction_post_philosophie_v0_1.md` ;
- `93_LABORATOIRE_EDITORIAL_EXPERIMENTAL/README.md` lorsqu'il est disponible
  dans le corpus auditable.

```text
PHASE = 9 / NORMALISATION_DOCUMENTAIRE_HUMAN_FIRST
STATUT = EN_COURS
PHASE_2_A_8 = QUALIFIEES_DANS_LE_PERIMETRE
AUDIT_GLOBAL = NON_CLOTURE
RECONSTRUCTION_EFFECTIVE = OUVERTE_SUR_BRANCHE_DE_TRAVAIL
MUTATION_IRREVERSIBLE = NON_AUTORISEE_PAR_CE_CADRAGE
SUPPRESSION = NON_AUTORISEE_PAR_DEFAUT
NOUVEAU_CALCUL = NON_LANCE
```

## Separation des vues

```text
VUE_PUBLIQUE = ETAT_COURANT_LISIBLE, LANGAGE_NATUREL, FONCTION_ET_PORTEE
VUE_LABORATOIRE = PROVENANCE, GENEALOGIE, JOURNAUX, DETTES, ETATS_DATÉS
```

Les documents d'accueil et de distribution ne racontent pas par defaut la
construction du projet, la sequence de l'audit, les interventions d'agents ou
la maintenance du depot. Ils decrivent ce que le projet est, ce qu'il examine,
ce qu'il etablit et ses limites.

Une genealogie peut etre conservee en annexe ou dans une route separee,
explicitement optionnelle. Elle ne doit pas etre necessaire pour comprendre
l'etat courant.

Cette separation ne produit ni etat fige ni effacement de l'histoire : l'etat
public reste revisable et la provenance reste recuperable dans les journaux,
archives, issues et Git.

## Regles d'ecriture

La reecriture positive v0.3 est active :

```text
DIRE_D_ABORD_CE_QUE_LE_CAS_EST
NOMMER_SON_RANG_ET_SA_FONCTION
APPAIRER_TOUTE_LIMITE_A_UN_CONTENU_POSITIVEMENT_NOMME
CONSERVER_LES_REFUS_SANS_LES_AFFAIBLIR
EMPLOYER_UN_LANGAGE_NATUREL_DANS_LES_VUES_PUBLIQUES
```

La negation reste utile pour fixer une limite ou un refus, mais elle ne doit pas
porter seule la description. La tuyauterie de l'audit reste dans ses journaux,
issues, archives ou outils de provenance, hors du flux principal d'accueil.

## Gate avant toute relecture publique

Aucune relecture ou reecriture publique n'est engagee avant un inventaire des
cibles et de leurs fonctions :

```text
DOCUMENT_CIBLE
FONCTION_ACTUELLE
PUBLIC_HUMAN_FIRST_OU_LABORATOIRE
CONTENU_UNIQUE
DEPENDANCES
RANG_ETAT
PROVENANCE
DESTINATION_PROPOSEE
RISQUE_DE_PERTE
DECISION_HUMAINE_REQUISE
```

Une proposition de deplacement, declassement, fusion ou suppression exige une
verification du contenu unique, de la fonction probatoire, des dependances
vivantes et de la recuperabilite Git. Le present cadrage n'autorise aucune de
ces operations.

## Etat initial de la phase

```text
REGLE_DE_SEPARATION_PUBLIC_LABORATOIRE = JUSTIFIEE_PAR_TEST_D_ABLATION
HISTORICITE_DANS_ACCUEIL = OPTIONNELLE, NON_IMPOSEE
TUYAUTERIE_DANS_FLUX_PUBLIC = A_RELEGUER_HORS_FLUX_PRINCIPAL
DOCUMENTS_PUBLICS = A_INVENTORIER_AVANT_REECRITURE
ANNEXE_GENEALOGIQUE = A_DISCUTER_AVEC_L_AUTEUR
```

La phase est donc ouverte comme cadrage et inventaire, pas comme campagne de
polissage automatique.

## Prochaine instruction

Construire l'inventaire cible des documents d'accueil et de distribution, puis
proposer une architecture de vues publiques et de routes optionnelles vers la
provenance. Aucune reecriture en masse, suppression, fusion ou modification de
l'etat scientifique n'est autorisee avant validation humaine du perimetre.

## Inventaire initial des règles d'ecriture et essais éditoriaux

### Réécriture positive

```text
Reecriture_positive_vocabulaire_v0_1 = ETAPE_GENEALOGIQUE
Reecriture_positive_vocabulaire_v0_2 = EXTENSION_STRUCTURELLE, SOURCE_HISTORIQUE
Reecriture_positive_vocabulaire_v0_3 = CANDIDAT_ACTIF, TESTE_SUR_TROIS_GENRES
Test_reecriture_structurelle_v0_1 = VALIDATION_BORNEE, DEPLOIEMENT_PAR_CERCLES
```

La v0.3 conserve les refus factuels, les non-thèses et les sorties négatives
dans leurs conteneurs propres. Elle ajoute la complétude informative, la
charité de rang et les registres de modalité. Son principe n'est donc pas une
interdiction de dire non : il exige que le texte nomme d'abord le résultat, la
fonction, l'appui ou le rang, puis conserve la limite avec toute sa force.

```text
V0_3 = REGLE_DE_REDACTION_ACTIVE_A_EVALUER_DOCUMENT_PAR_DOCUMENT
V0_1_V0_2 = PROVENANCE_GENEALOGIQUE, NON_CANDIDATS_CONCURRENTS
TEST_STRUCTUREL = SUPPORT_SATISFAISANT, GENERALISATION_A_CONTROLER
```

### Protocole de rédaction post-philosophie

Le protocole post-philosophie fournit le noyau opératoire : écriture positive,
deux registres `constance` / `constante`, statuts probatoires P1-P6,
correction modale, positionnement Q1/Q2 et discipline Git. Il guide les
nouveaux documents, mais ne décide pas à lui seul quels documents doivent
devenir publics, historiques ou annexes.

```text
PROTOCOLE_POST_PHILOSOPHIE = GUIDE_OPERATOIRE
STATUT_PUBLIC_DES_DOCUMENTS = A_DETERMINER_PAR_INVENTAIRE_HUMAN_FIRST
SEPARATION_VUE_PUBLIQUE_LABORATOIRE = ADDENDUM_PHASE_9_REQUIS
```

### Non-prolifération et consolidation

La synthèse de récupération du socle méthodologique et la note critique de
compression portent le principe suivant : une distinction locale peut rester
utile dans une fiche sans devenir une famille générale ; la compression doit
changer le niveau sans appauvrir la carte.

```text
COMPRESSION = GAIN_DE_CLARTE_SANS_PERTE_DE_DISCRIMINATION
FUSION = AUTORISEE_SEULEMENT_APRES_REMONTEE_ET_CONTROLE_DU_CONTENU_UNIQUE
DOCUMENT_UNIQUE_PAR_FONCTION = HYPOTHESE_DE_CONSOLIDATION_A_TESTER
```

Cette règle ne justifie pas encore une fusion concrète : les fonctions, publics,
statuts et dépendances des documents cibles doivent d'abord être inventoriés.

### Laboratoire éditorial

Le laboratoire contient actuellement des plans, une tentative de rédaction et
une relecture de l'essai `Qualifier la constance`. Ces pièces montrent une
capacité rédactionnelle et des choix de structure, mais l'essai conserve des
formulations historiques, des affirmations longues et un appareil de sources
qui exigeraient une qualification distincte avant diffusion.

```text
ESSAI_QUALIFIER_LA_CONSTANCE = MATERIAU_EXPERIMENTAL
PLAN_LIVRABLE_THEORIQUE = PLAN_DE_REDACTION, NON_TEXTE_PUBLIC_AUTORISE
RELECTURE = CONTROLE_EDITORIAL, NON_VALIDATION_SCIENTIFIQUE
LABORATOIRE_EDITORIAL = PROVENANCE_ET_ESSAIS, NON_FLUX_PUBLIC
README_DU_LABORATOIRE = NON_TROUVE_DANS_LE_CLONE_A_CE_PALIER
```

L'absence du README attendu est une lacune d'inventaire à vérifier, non une
autorisation de créer ou de déplacer un document.

## Décision de phase à ce palier

```text
REGLES_D_ECRITURE_REMONTEES = OUI
REGLE_ACTIVE_CANDIDATE = REECRITURE_POSITIVE_V0_3
REGLE_DE_COMPRESSION = JUSTIFIEE_COMME_CRITERE, NON_COMME_FUSION_AUTOMATIQUE
VUE_PUBLIQUE_LABORATOIRE = DISTINCTION_JUSTIFIEE
REECRITURE_PUBLIQUE = NON_OUVERTE
DEPLACEMENT_OU_SUPPRESSION = NON_AUTORISE
PROCHAINE_INSTRUCTION = INVENTORIER_LES_README_ET_DOCUMENTS_D_ACCUEIL
```

## Audit structurel des deux portes publiques principales

### README racine

```text
LIGNES = 55
FONCTION = OBJET_DU_PROJET, QUESTIONS, DISTINCTION_MINIMALE, ROUTAGE_HUMAIN
TUYAUTERIE_EXPLICITE = FAIBLE
HISTORICITE_EXPLICITE = LIMITEE_AU_NOM_HISTORIQUE
ETAT = PORTE_PUBLIQUE_COURANTE_COMPATIBLE_HUMAN_FIRST
```

Le README racine présente le projet, ses deux questions, la distinction
constance/stabilisation et les portes de lecture. Sa section sur l'état courant
reste utile pour le routage, mais devra être distinguée, au polissage, d'un
tableau de bord de laboratoire.

### Accueil des cycles physiques

```text
LIGNES = 35
FONCTION = PRESENTATION_DES_DIX_CYCLES_ET_ROUTAGE_SCIENTIFIQUE
TABLEAU_DES_CYCLES = OUI
VERSIONNAGE_DES_CIBLES = PRESENT
ETATS_ET_ISSUES = PRESENTS_PAR_REFERENCE
ETAT = PORTE_HYBRIDE_PUBLIC / LABORATOIRE
```

L'accueil des cycles est lisible et utile, mais il combine la présentation des
terrains avec des chemins de reprise, des versions de synthèses, des résultats
locaux et une issue active (#115). Cette hybridation ne constitue pas encore
une faute : le fichier sert effectivement de routage vivant. Elle devient
toutefois la première cible de séparation des vues Human-First.

### Décision de cadrage

```text
README_RACINE = CONSERVE_COMME_BASE_PUBLIQUE, A_POLIR_APRES_ARCHITECTURE_VALIDEE
README_CYCLES = CONSERVE_COMME_ROUTAGE_HYBRIDE, SEPARATION_PUBLIC/LABORATOIRE_A_TESTER
REDACTION_IMMEDIATE = NON
FUSION_OU_DEPLACEMENT = NON
PROCHAINE_INSTRUCTION = DEFINIR_LA_STRUCTURE_CIBLE_DU_README_RACINE_ET_DES_CYCLES
```

Le test d'ablation ne justifie pas encore de réécrire : les deux documents
remplissent actuellement une fonction de navigation réelle. La phase 9 doit
d'abord proposer une architecture cible séparant présentation, état courant et
profondeur de laboratoire, puis soumettre cette architecture à validation.

## Précision terminologique : consolidation éditoriale sémantique

La proposition initiale de « concaténation sémantique » est retenue comme
intuition, mais amendée comme terme opératoire :

```text
CONSOLIDATION_EDITORIALE_SEMANTIQUE = TERME_DE_TRAVAIL
COMPRESSION = DESCRIPTION_INSUFFISANTE_SI_QUANTITATIVE
CONCATENATION = AUCUNE_OPERATION_MECANIQUE
```

La consolidation vise un document par fonction dominante, rédigé naturellement
pour son public, à partir de plusieurs pièces dont le sens a été cartographié.
Elle ne crée pas une synthèse moyenne : les contradictions, limites, résultats
négatifs, rangs et conditions de réouverture restent visibles à leur place.

```text
GAINS_ATTENDUS = LISIBILITE, PROFONDEUR, NON_PROLIFERATION, RECUPERABILITE
RISQUE_PRINCIPAL = FABRIQUER_UNE_CONTINUITE_OU_PERDRE_UN_ELEMENT_UNIQUE
TEST_OBLIGATOIRE = MATRICE_SOURCES_CONTENU_REPRIS_DEVENIR
DECISION_SUR_LES_ARCHIVES = SEPAREE, NON_PRESUPPOSEE
```

La consolidation ne sera testée qu'après inventaire d'un lot homogène. Le
premier essai devra être réversible, comparer le texte source et le texte
consolidé, et être soumis à une lecture humaine avant toute promotion dans une
vue publique.

### Méta-règle appliquée au test lui-même

Le test de consolidation s'approche des règles générales de l'audit sans leur
être exclusivement assujetti comme à une norme immuable. Il tient compte de
leur évolution, de leur portée locale ou transversale et de la classe du
document testé.

```text
TEST = INSTRUCTION_ADAPTATIVE, NON_EXAMEN_DE_CONFORMITE_MECANIQUE
REGLES_DE_REFERENCE = EVOLUTIVES, LOCALES_OU_TRANSVERSALES_SELON_LE_CAS
BUT_DU_TEST = LISIBILITE, PROFONDEUR, PORTÉE_ET_CONSERVATION_DU_SENS
CHEMIN_DU_TEST = ADAPTABLE_AU_GENRE_ET_AU_PUBLIC
META_REGLE = S_APPLIQUE_AU_TEST_LUI_MEME
```

Un test peut donc conclure qu'une règle est suffisante, locale, trop forte,
incomplète ou à amender. Il doit conserver la raison, le matériau observé, le
gain attendu et la condition de reprise. Il ne transforme pas une adaptation
locale en nouvelle règle générale sans satisfaire le test d'amendement du
programme.

## Validation provisoire et étapes préparatoires au premier test

Validation humaine reçue pour le cadrage de la consolidation éditoriale
sémantique. Cette validation ne vaut pas autorisation de modifier les README,
de fusionner des documents ou de déplacer des archives.

Avant le premier test, la phase 9 suivra cette séquence :

```text
1. MATRICE_DES_DOCUMENTS_CIBLES
2. CONTRAT_DE_CAPACITE_EDITORIALE_PAR_DOCUMENT
3. SELECTION_D_UN_LOT_HOMOGENE
4. PROTOTYPE_REVERSIBLE_SUR_COPIE
5. COMPARAISON_SOURCES / CONSOLIDATION / PERTES
6. LECTURE_HUMAINE_ET_DECISION_DE_PROMOTION
```

Le premier lot candidat reste limité aux deux portes publiques déjà auditées :
`README.md` et `02_CYCLES_PHYSIQUES/README.md`. Ce choix est un point de départ
réversible, non une exclusivité de la phase 9 ; il permet de tester la méthode
sur des fonctions proches mais non identiques : accueil général et accueil
scientifique.

```text
VALIDATION_HUMAINE = CADRAGE_PROVISOIRE_ACCEPTE
REDACTION_PUBLIQUE = TOUJOURS_NON_OUVERTE
PREMIER_LOT = A_CARTOGRAPHIER_AVANT_PROTOTYPE
ARCHIVES = AUCUNE_DECISION_PRise
```

## Sas de resynchronisation : capacité du projet et capacité des documents

L'audit des phases 1 à 8 a qualifié des résultats, des fonctions, des règles,
des interfaces et des limites. Il n'a pas encore transformé cette qualification
en contrat explicite pour chaque document public. La phase 9 ajoute donc un sas
de resynchronisation avant tout polissage :

```text
RESULTATS_QUALIFIES
-> CE_QUE_LE_PROJET_PEUT_PORTER
-> CE_QUE_CHAQUE_DOCUMENT_PEUT_DIRE
-> PUBLIC_ET_FONCTION_DU_DOCUMENT
-> FORME, LONGUEUR ET ROUTE_DE_PROVENANCE
```

Ce sas ne crée pas une nouvelle phase d'audit. Il précise la fonction de la
phase 9 et empêche une réécriture fidèle de la forme ancienne de conserver des
énoncés que l'audit a requalifiés, ou de supprimer des limites qui restent
constitutives de la portée.

### Matrice minimale à produire pour chaque document cible

```text
DOCUMENT
PUBLIC_VISE
FONCTION_UNIQUE_OU_DOMINANTE
RESULTATS_ET_FONCTIONS_QUE_LE_PROJET_PEUT_PORTER
ENONCES_AUTORISES
ENONCES_A_BORNER_OU_A_RENVOYER
CONTENU_DE_LABORATOIRE_A_RELEGUER
CONTENU_UNIQUE_A_CONSERVER
FORMAT_ET_LONGUEUR_PROPORTIONNES
ROUTE_OPTIONNELLE_VERS_PROVENANCE
DECISION_HUMAINE_REQUISE
```

La matrice doit permettre de répondre à la question « que peut dire ce
document ? », et non seulement « que contient-il aujourd'hui ? ». Un document
ne doit pas porter simultanément l'accueil, la preuve détaillée, la généalogie,
le journal d'audit et le workflow agentique lorsque ces fonctions peuvent être
séparées sans perte.

### Architecture éditoriale cible à discuter

```text
VUE_PUBLIQUE = projet, questions, acquis qualifiés, limites, points d'entrée
VUE_SCIENTIFIQUE = synthèses et pièces locales nécessaires à un résultat
VUE_METHODOLOGIQUE = règles actives et contrats de qualification
VUE_PROVENANCE = archives, généalogie, états datés, décisions et changelogs
VUE_AGENTIQUE = AGENTS.md, workflow, contraintes d'intervention
VUE_EXPERIMENTALE = laboratoire éditorial, plans et essais non promus
```

La cible n'est pas un fichier unique pour tout le dépôt. Elle vise plutôt un
document principal par fonction dominante, avec des annexes ou routes de
provenance optionnelles. La compression est réussie lorsque le lecteur peut
comprendre l'état courant sans lire la fabrication du projet, tandis que la
provenance reste récupérable pour un audit ultérieur.

```text
RESYNCHRONISATION_SEMANTIQUE = REQUISE_AVANT_REECRITURE
CAPACITE_DU_PROJET = A_DECRIRE_PAR_PORTÉE_ET_RANG
CAPACITE_DU_DOCUMENT = A_DECRIRE_PAR_PUBLIC_ET_FONCTION
CONSOLIDATION = A_PROPOSER_APRES_MATRICE_DOCUMENTAIRE
SUPPRESSION_OU_DEPLACEMENT = TOUJOURS_SOUS_GATE_HUMAIN
```

Cette proposition est une extension opératoire de la phase 9, non une
autorisation de polissage. Elle sera testée par ablation : sans ce sas, une
réécriture peut rester lisible tout en publiant une capacité dépassée ou en
mélangeant état courant et généalogie ; avec lui, chaque document reçoit une
portée vérifiable avant sa rédaction.

## Inventaire des portes d'accueil et de distribution

### Vues publiques ou de routage humain

```text
README.md = VUE_PUBLIQUE_PRINCIPALE, OBJET, QUESTIONS, ROUTAGE
02_CYCLES_PHYSIQUES/README.md = VUE_PUBLIQUE_SCIENTIFIQUE, ROUTAGE_DES_CYCLES
06_PHILOSOPHIE/README.md = VUE_DE_BRANCHE, CHARTE, RANG, ROUTAGE_LOCAL
99_DOCUMENTATION_ENVIRONNEMENTS_LOCAUX/README.md = VUE_PUBLIQUE_EXPURGEE,
                                                      CONTRAT_ET_FRONTIERES
```

Ces portes sont lisibles par un nouveau lecteur, mais elles n'ont pas toutes
la même fonction. Le README racine porte l'entrée générale ; l'accueil des
cycles porte le routage scientifique ; le README philosophique porte une
branche exploratoire ; le dossier 99 porte une notice publique d'environnement.
Elles ne doivent pas être fusionnées dans un tableau de bord unique.

### Vues opératoires, agentiques ou de provenance

```text
AGENTS.md = REGLES_D_INTERVENTION_AGENTIQUE, NON_PAGE_DE_DISTRIBUTION
91_TRAVAUX_ANTERIEURS/README.md = GENEALOGIE_OPTIONNELLE, ARCHIVE_EXPLICATIVE
92_ARCHIVES_CONVERSATIONNELLES/README.md = PROVENANCE_ARCHIVISTIQUE,
                                           NON_AUTORITE_ACTIVE
```

`AGENTS.md` doit rester précis pour l'intervention agentique et ne pas être
transformé en accueil général. Les dossiers 91 et 92 disposent déjà d'un
langage de provenance qui permet une consultation optionnelle sans imposer
l'historicité au lecteur courant.

### Absences de porte locale

```text
01_CADRE_METHODOLOGIQUE/README.md = NON_TROUVE_DANS_LE_CLONE
05_CARTES_ET_SYNTHESES/README.md = NON_TROUVE_DANS_LE_CLONE
93_LABORATOIRE_EDITORIAL_EXPERIMENTAL/README.md = NON_TROUVE_DANS_LE_CLONE
```

Ces absences sont des faits d'inventaire, non encore des défauts à corriger.
Avant de créer une porte, il faut établir si le README racine, un index actif,
un document de cadre ou le laboratoire porte déjà la fonction de routage. La
création d'un README n'est justifiée que par un gain de navigation supérieur à
son coût de maintenance.

### Première décision Human-First

```text
PORTE_PUBLIQUE_PRINCIPALE = README_RACINE
PORTE_SCIENTIFIQUE = README_CYCLES
PORTE_PHILOSOPHIQUE = README_06
PORTES_DE_PROVENANCE = 91, 92
PORTE_ENVIRONNEMENT_PUBLIC = 99
AGENTS = COUCHE_OPERATIONNELLE_SEPAREE
README_MANQUANTS = A_EVALUER, NON_A_CREER_PAR_DEFAUT
RELECTURE_ET_REECRITURE = OUVERTE_SUR_LOTS_BORNES
RECONSTRUCTION = A_COMMENCER_APRES_QUALIFICATION_DES_CIBLES
PROMOTION_DES_RESULTATS = SOUS_DECISION_HUMAINE
PROCHAINE_INSTRUCTION = RECONSTRUIRE_PROGRESSIVEMENT_LES_PORTES_HUMAN_FIRST
```

Cette première réduction du champ diminue le risque de prolifération : deux
portes publiques principales sont à examiner avant toute addition, tandis que
les autres conservent leur spécialisation.

## Premier prototype reversible : carte publique des cycles

Un prototype interne a ete produit dans le laboratoire editorial :
`93_LABORATOIRE_EDITORIAL_EXPERIMENTAL/ESSAI_tentative/travail_ecriture/Prototype_carte_publique_cycles_Human_First_2026-08-18.md`.
Il teste l'option d'une carte publique complete sur les dix cycles, avec des
liens d'approfondissement, sans reprendre dans le flux principal les journaux,
dettes et etats de maintenance.

Le test des routes a d'abord falsifie le prototype : les liens relatifs etaient
calcules depuis un niveau incorrect du laboratoire. Une seconde verification a
confirme la profondeur reelle de trois niveaux sous la racine, puis tous les
liens locaux ont ete corriges et controles.

La comparaison de contenu a egalement fait remonter trois elements uniques qui
avaient ete omis dans la premiere version : les deux lignes independantes de
C7 (`C7-C1 / X(z)` et `C7-GAL`), le complement 2026 du cycle 8 et les resultats
des phases 2, 3 et 4 du cycle 10. Ils ont ete reintegres avant qualification du
prototype.

```text
PROTOTYPE = PRODUIT_SUR_COPIE
ROUTES_LOCALES = 15 / 15 RESOLUES
CONTENU_UNIQUE_RETRACE = OUI
DEFAUTS_DETECTES_ET_CORRIGES = 2
PROMOTION_PUBLIQUE = NON
RESULTAT = CARTE_PUBLIQUE_POSSIBLE_SOUS_CONTROLE_DES_ROUTES_ET_DU_CONTENU
SEPARATION_EN_DOCUMENT_SUPPLEMENTAIRE = NON_DECIDEE
PROCHAINE_INSTRUCTION = COMPARER_LISIBILITE_ET_COUT_DE_MAINTENANCE
```

Ce résultat reste local au genre « carte d'accueil scientifique ». Il ne
justifie ni une réécriture du README source, ni une règle générale de
séparation documentaire.

## Requalification : éviter la boucle des destinations

Le retour sur le prototype montre une limite de la stratégie initiale. La
verification des liens a ete utile pour controler l'etat present du clone,
mais elle attachait deja le texte a une arborescence que la restructuration
pourrait remplacer. Corriger les chemins aujourd'hui ne garantit donc pas la
migrabilite du contenu demain ; cela peut au contraire multiplier les reprises
des documents parents et enfants.

```text
HYPOTHESE_DE_CARTE_LIEE_AUX_CHEMINS = REQUALIFIEE
VALEUR_DU_PROTOTYPE = TEMOIN_DE_CONTROLE, NON_ARCHITECTURE_CIBLE
BOUCLE_DE_REDISTRIBUTION = RISQUE_RECONNU
RESTRUCTURATION_PAR_CHEMINS = SUSPENDUE
```

Le prototype est conserve comme essai date et non promu. Aucun lien n'est
retravaille dans les documents publics tant que les fonctions et classes
documentaires ne sont pas suffisamment stabilisees.

## Nouveau sas propose : classes avant destinations

Un cadrage interne ouvre un test par classes documentaires :
`01_CADRE_METHODOLOGIQUE/cadrage_test_classes_documentaires_human_first_2026-08-18.md`.
Il ne cree pas une nouvelle architecture durable. Il teste d'abord des contrats
de contenu sans chemin ni nom de destination, puis leur capacite a migrer vers
plusieurs organisations possibles.

```text
CLASSES_AVANT_CHEMINS = A_TESTER
CONTRAT_SANS_DESTINATION = A_TESTER
DOCUMENT_AUTONOME = A_TESTER_SUR_LOT_HOMOGENE
LIENS = A_CONSTRUIRE_APRES_STABILISATION_DES_CLASSES
ARCHITECTURE_FINALE = NON_DECIDEE
NOUVEL_AUDIT_GLOBAL = NON_JUSTIFIE_A_CE_PALIER
```

Ce sas peut conduire a conserver la distribution actuelle, a redefinir des
classes, a isoler des documents uniques ou a rouvrir une question locale. Il
ne presuppose ni une fusion par classe, ni une multiplication des README, ni
une migration de masse. Le depot reste un laboratoire dans la branche d'audit
et aucune restructuration effective n'est ouverte.

## Ouverture du cadrage de réarchitecture générale

Le retour suivant élargit le chantier : la question ne porte plus seulement
sur la forme des portes Human-First, mais sur l'architecture générale qui doit
accueillir les continuations physiques, computationnelles, méthodologiques,
philosophiques et éditoriales. La structure actuelle est conservée comme
support historique et opératoire ; elle n'est pas traitée comme une cible
intouchable ni comme un modèle à reproduire automatiquement.

Le cadrage interne est consigné dans :
`01_CADRE_METHODOLOGIQUE/cadrage_rearchitecture_generale_sans_perte_2026-08-18.md`.

```text
REARCHITECTURE_GENERALE = CONCEPTION_A_INSTRUIRE
INVESTIGATIONS_EXISTANTES = CONSERVEES
ARBORESCENCE_ACTUELLE = TEMOIN_HISTORIQUE_ET_OPERATIONNEL
NOUVELLE_ARBORESCENCE = NON_CREEE
MIGRATION = NON_OUVERTE
```

Le cadrage distingue les plans public, recherche, preuve, provenance et
laboratoire, mais ne les convertit pas encore en dossiers. Trois options sont
à comparer : réorganisation par plans, domaines avec fonctions internes, ou
documents autonomes avec indexation tardive. Le choix devra venir d'un
mappage sans déplacement et d'un contrôle des pertes, duplications,
dépendances et coûts de liaison.

Cette ouverture ne constitue pas un nouvel audit scientifique global. Elle
réoriente la phase 9 vers une conception d'architecture et peut révéler des
retours locaux nécessaires ; elle ne relance aucune investigation par défaut.

## Recommandation architecturale provisoire

Le cadrage est complété par une piste à axes séparés : document autonome,
domaine, fonction, statut et vue de distribution. Cette piste évite de faire
porter par un seul chemin l'identité, le rang, l'état et l'usage d'une pièce.

```text
PIECE_CANONIQUE = DOCUMENT_AUTONOME
AXES = DOMAINE + FONCTION + STATUT + VUE
CARTE_ET_INDEX = VUES_DERIVEES
LIEN = SEMANTIQUE, PROVENANCE, COMPLEMENT, ROUTE_OU_VOISINAGE
```

La recommandation reste une hypothèse, non une décision d'architecture. Elle
sera testée par modèle conceptuel, mappage sans déplacement, vues sur copie,
puis migration pilote. Elle permettrait de repartir de zéro architecturalement
sans recommencer les investigations scientifiques.

Les anti-patterns explicitement retenus sont la simple renumérotation des
dossiers, le statut déduit du chemin, le README cumulant toutes les fonctions,
la duplication publique avant identification de la pièce canonique et la
généralisation depuis un seul lot.

## Ouverture effective du premier test

La matrice interne de capacité est produite pour le premier lot :
`01_CADRE_METHODOLOGIQUE/matrice_capacite_documents_human_first_2026-08-18.md`.
Elle confirme que le lot est homogène par fonction d'accueil, mais distingue
deux capacités : le README racine porte déjà une vue publique conceptuelle,
tandis que l'accueil des cycles combine une carte scientifique et un routage
vivant.

```text
MATRICE_DES_CIBLES = PRODUITE
CONTRAT_DE_CAPACITE = PRECISE_DANS_LA_MATRICE
README_RACINE = TEMOIN_DE_CONTROLE, PAS_DE_PROTOTYPE_A_CE_PALIER
README_CYCLES = PREMIERE_CIBLE_DE_PROTOTYPE_SUR_COPIE
MUTATION_DES_SOURCES = NON
PROMOTION_PUBLIQUE = NON_OUVERTE
```

## Clarification : sémantique comme architecture intégrale du sens

Le terme « sémantique » est élargi pour ce chantier. Il ne désigne pas une
simple réécriture lexicale ou éditoriale, mais la conservation et la liaison
contrôlable de ce que les pièces veulent dire, établissent, supposent, bornent
et rendent transmissible.

```text
ARCHITECTURE_SEMANTIQUE_INTEGRALE
 = PHYSIQUE + EPISTEMIQUE + COMPUTATIONNELLE
 + METHODOLOGIQUE + PHILOSOPHIQUE + EDITORIALE
```

Cette extension n'absorbe pas les registres les uns dans les autres. Elle
demande de conserver leurs questions propres et leurs statuts, puis de rendre
explicites leurs passages. La sémantique n'est donc ni une vérité physique,
ni une qualification automatique, ni une uniformisation des écritures.

```text
SEMANTIQUE = NIVEAU_DE_LIAISON_ET_DE_CONSERVATION_DU_SENS
REGISTRES = DISTINCTS, MAIS ARTICULABLES
CONTRATS_LOCAUX = NOMMER_LES_REGISTRES_EFFECTIVEMENT_CONCERNES
ARCHITECTURE_RECOMMANDEE = SEMANTIQUE_INTEGRALE, NON_REDUCTION_AU_STYLE
```

Le terme peut ainsi suffire pour nommer le chantier général, à condition que
ce périmètre soit déclaré dans le cadrage et que les contrats locaux précisent
toujours s'ils portent sur la physique, l'épistémique, le computationnel, la
méthodologie, la philosophie ou l'éditorial.

### Méta-règle : la liste reste ouverte

Les registres nommés ne constituent pas une liste exhaustive. Ils servent de
repères initiaux pour instruire l'architecture sémantique intégrale. Un élément
qui ne rentre pas proprement dans ces repères peut rester transversal, mixte,
non classé ou indécidable ; il ne doit pas être forcé dans une case pour
produire une apparence de complétude.

```text
LISTE_DES_REGISTRES = OUVERTE
ELEMENT_EMERGENT = A_DECRIRE_ET_A_TESTER
FORCAGE_TAXONOMIQUE = REFUSE
NOUVELLE_DIMENSION = A_JUSTIFIER_PAR_UN_GAIN_DISCRIMINANT
GENERALISATION = NON_AUTOMATIQUE
```

L'absence d'une catégorie adaptée est elle-même une information du test. Elle
peut signaler une relation transversale ou une dimension émergente, sans
imposer immédiatement d'allonger la liste. Toute extension reste locale tant
qu'elle n'a pas montré sa nécessité et sa portée.

## Distinction des workflows

La suggestion relative aux workflows est intégrée au cadrage de réarchitecture.
Le workflow prioritaire de la phase actuelle est le **workflow sémantique
intégral** : il traite le contenu, les registres, les statuts, les relations,
les fonctions documentaires, les vues et les contrôles de perte.

Le **workflow CI** est distinct. Il traite les contrôles techniques
automatisables, la syntaxe, les liens, les formats, les tests et la maintenance
des artefacts déjà qualifiés. Il peut soutenir le workflow sémantique, mais ne
peut ni décider du sens, ni établir un rang scientifique, ni autoriser une
promotion documentaire.

```text
WORKFLOW_SEMANTIQUE_INTEGRALE = PRIORITAIRE_MAINTENANT
WORKFLOW_CI = PHASE_ULTERIEURE
CI = SUPPORT_TECHNIQUE, NON_ARBITRE_DU_SENS
```

L'amélioration du CI sera donc instruite après la clarification des objets et
relations de la nouvelle architecture, afin de ne pas transformer les chemins
actuels en contrats durables par simple automatisation.

## Palier 1 : modèle conceptuel de l'architecture

Le passage à l'étape suivante est ouvert avec le modèle interne :
`01_CADRE_METHODOLOGIQUE/modele_conceptuel_architecture_semantique_integrale_2026-08-18.md`.
Il ne propose encore aucune arborescence. Il distingue l'objet de travail,
le dossier de recherche, la vue, la pièce de preuve, l'état, la relation et le
workflow.

```text
PALIER_1 = MODELE_CONCEPTUEL
OBJET_PRIMAIRE = OBJET_DE_TRAVAIL, NON_CHEMIN
NOMBRE_DE_DOCUMENTS = A_DEDUIRE_DES_FONCTIONS_ET_RELATIONS
OBJET_TRANSVERSAL_OU_NON_CLASSE = RECEVABLE
VUES_ET_LIENS = A_TESTER_APRES_IDENTIFICATION_DES_OBJETS
ARBORESCENCE_CIBLE = NON_DECIDEE
MIGRATION = NON_OUVERTE
```

## Palier 2 : mappage abstrait du lot pilote

Le mappage est consigné dans :
`01_CADRE_METHODOLOGIQUE/mappage_abstrait_lot_pilote_architecture_2026-08-18.md`.
Le lot comprend six pièces observées dans leurs fonctions actuelles : accueil,
synthèse scientifique, blocage computationnel, décision méthodologique,
provenance et plan éditorial expérimental.

```text
PALIER_2 = MAPPAGE_ABSTRAIT_SANS_DEPLACEMENT
LOT = 6 PIECES
MAPPAGE_SANS_CHEMIN = POSSIBLE_SUR_LE_LOT
FONCTION_DOMINANTE = UTILE_MAIS_NON_EXCLUSIVE
REGISTRES_MULTIPLES = NECESSAIRES
NOMBRE_DE_DOCUMENTS = NON_DEDUIT_A_CE_PALIER
ARBORESCENCE = NON_DEDUITE_A_CE_PALIER
```

Le mappage montre que les statuts et relations ne sont pas interchangeables :
un blocage d'exécution, une décision canonique, une archive et un essai ne
produisent pas les mêmes effets. Il confirme aussi qu'une pièce peut relever de
plusieurs registres sans devoir être copiée. Les tensions relevées concernent
la pluralité de L4, le routage présent dans L5 et l'incompatibilité de public et
de statut entre L1 et L6 ; elles seront testées au palier des vues, sans
correction immédiate.

## Palier 3 : test des vues abstraites

Le test des vues est consigné dans :
`01_CADRE_METHODOLOGIQUE/test_vues_abstraites_lot_pilote_architecture_2026-08-18.md`.
Il projette le même lot sur trois usages : vue publique, vue de recherche et
vue de provenance. Les objets et leur contenu canonique restent inchangés.

```text
PALIER_3 = TEST_DE_VUES
VUES_MULTIPLES_SUR_MEMES_OBJETS = POSSIBLE
CONTENU_CANONIQUE = NON_DUPLIQUE_PAR_DEFAUT
VUE_PUBLIQUE = SEPARABLE_DE_LA_PROVENANCE
VUE_DE_RECHERCHE = A_LOCALISER_PAR_QUESTION_OU_DOMAINE
ARBORESCENCE = TOUJOURS_NON_DEDUITE
MIGRATION = NON_OUVERTE
```

Le test montre qu'une vue publique peut rester sélective, qu'une vue de
provenance peut être proposée sans imposer la généalogie et qu'une vue de
recherche ne doit probablement pas devenir un tableau de bord transversal.
Il ne décide pas encore si ces vues seront des fichiers, des README, des index
générés ou une combinaison de ces formes.

## Palier 4 : comparaison des cartes d'architecture abstraites

La comparaison est consignée dans :
`01_CADRE_METHODOLOGIQUE/comparaison_cartes_architecture_abstraites_lot_pilote_2026-08-18.md`.
Trois cartes ont été confrontées sur le même lot : plans fonctionnels,
domaines avec fonctions internes, et objets autonomes avec vues tardives.

```text
PALIER_4 = COMPARAISON_DE_CARTES_ABSTRAITES
CARTE_A = UTILE_COMME_VUE_FONCTIONNELLE
CARTE_B = CONTINUITE_DE_DOMAINE, RISQUE_DE_REPRODUCTION
CARTE_C = SOCLE_CONCEPTUEL_LE_PLUS_STABLE
COMBINAISON_A_B_C = A_TESTER
ARBORESCENCE_REELLE = NON_DEFINIE
MIGRATION = NON_OUVERTE
```

La recommandation locale est de tester une combinaison : objets autonomes et
relations explicites comme socle, plans fonctionnels comme vues de distribution
et de travail, domaines comme contextes de recherche, et statuts comme axe
indépendant. Cette combinaison conserve les gains des trois cartes sans faire
du plan, du domaine et de l'objet une hiérarchie unique.

## Palier 4B : test de la combinaison architecturale hybride

Le test de combinaison est consigné dans :
`01_CADRE_METHODOLOGIQUE/test_combinaison_architecture_hybride_lot_pilote_2026-08-18.md`.
Il vérifie sur le lot pilote si les objets autonomes peuvent accueillir les
plans comme vues et les domaines comme contextes, sans créer de hiérarchie
cachée ni de registre central préalable.

```text
PALIER_4B = TEST_DE_COMBINAISON_ARCHITECTURALE
COMBINAISON_HYBRIDE = COHERENTE_SUR_LE_LOT
OBJETS_AUTONOMES = SOCLE_RETENU_PROVISOIREMENT
PLANS = VUES_NON_CANONIQUES
DOMAINES = CONTEXTES_NON_STATUTS
MIGRATION_CONCEPTUELLE = POSSIBLE_SUR_LE_LOT
REGISTRE_CENTRAL = NON_JUSTIFIE_A_CE_PALIER
MIGRATION_REELLE = NON_OUVERTE
```

Le test ne révèle pas de hiérarchie cachée nécessaire sur ce lot. Il fait
toutefois émerger un point à instruire avant toute généralisation : le statut
d'un objet, l'état d'une ligne de travail et l'autorisation d'agir ne doivent
pas être confondus. Les relations computationnelles et les dépendances de L2
devront également être testées avec une granularité plus fine.

## Palier 5A : découplage du statut, de l'état et de l'autorisation

Le test est consigné dans :
`01_CADRE_METHODOLOGIQUE/test_decouplage_statut_et_autorisation_lot_pilote_2026-08-18.md`.
Il confronte la distinction à cinq cas du lot : synthèse scientifique active,
blocage computationnel, décision méthodologique, archive de provenance et plan
éditorial expérimental.

```text
PALIER_5A = DECOUPLAGE_STATUT_ET_AUTORISATION
DECOUPLAGE = COHERENT_SUR_LE_LOT
STATUT = PROPRIETE_BORNEE_DE_L_OBJET
ETAT = PROPRIETE_DE_LA_LIGNE_OU_DE_LA_REPRISE
AUTORISATION = DECISION_LOCALE_EXPLICITE
AUTORISATION_DERIVEE_AUTOMATIQUE = REFUSEE
ARCHIVE_REACTIVEE_AUTOMATIQUEMENT = REFUSEE
MIGRATION = NON_OUVERTE
```

Le test confirme qu'une synthèse active n'autorise pas automatiquement un
calcul, qu'un blocage d'accès ne constitue pas un échec scientifique et qu'une
archive utile ne redevient pas une autorité. La distinction reste locale au
lot et devra être confrontée à d'autres lignes, issues et relations avant
toute généralisation architecturale.

## Palier 5B : test des identités et des relations

Le test est consigné dans :
`01_CADRE_METHODOLOGIQUE/test_identites_relations_lot_pilote_2026-08-18.md`.
Il vérifie que les objets restent identifiables lorsque les vues ou domaines
de lecture changent, et que les relations ne sont pas réduites à des chemins
ou à des liens Markdown.

```text
PALIER_5B = IDENTITES_ET_RELATIONS
IDENTITES_SANS_CHEMIN = POSSIBLES_SUR_LE_LOT
RELATIONS_TYPEES = NECESSAIRES
CHANGEMENT_DE_VUE = COMPATIBLE_AVEC_LA_STABILITE_DES_OBJETS
REATTRIBUTION_PAR_CHEMIN = REFUSEE
AUTOMATISATION_DES_RELATIONS = PREMATUREE
MIGRATION = NON_OUVERTE
```

Le test confirme que les relations de route, de preuve, de provenance, de
reprise et de norme sont discriminables. Il laisse toutefois ouvertes la
granularité du réseau de pièces de L2, la pluralité de L4 et la formalisation
des relations computationnelles. La prochaine instruction est de définir un
contrat minimal d'objet migrable, sans ouvrir de migration réelle.

## Palier 6 : contrat minimal d'un objet migrable

Le contrat est consigné dans :
`01_CADRE_METHODOLOGIQUE/contrat_minimal_objet_migrable_lot_pilote_2026-08-18.md`.
Il ne prescrit ni déplacement ni format technique. Il définit les invariants à
contrôler si une destination change un jour : identité, contenu unique, portée,
statut, relations, provenance, conditions de reprise et critères de perte.

```text
PALIER_6 = CONTRAT_MINIMAL_OBJET_MIGRABLE
CONTRAT_MINIMAL = APPLICABLE_AU_LOT
IDENTITE_ET_CONTENU = CONTROLEABLES
STATUT_ET_AUTORISATION = SEPARES
RELATIONS = A_QUALIFIER_PAR_TYPE
MIGRATION_CONCEPTUELLE = TESTABLE
MIGRATION_REELLE = NON_OUVERTE
```

Le contrat refuse une migration lorsque l'identité n'est pas retraçable, que le
contenu unique ou la provenance ne sont pas inventoriés, qu'une dépendance
sémantique reste ambiguë ou qu'une autorisation est inférée du chemin. Les
champs incomplets du lot concernent surtout la granularité probatoire de L2,
les relations d'accès de L3 et les applications locales de L4.

## Palier 7 : simulation de deux destinations abstraites

La simulation est consignée dans :
`01_CADRE_METHODOLOGIQUE/simulation_migration_conceptuelle_deux_destinations_2026-08-18.md`.
Elle confronte le contrat minimal à deux modèles de distribution : plans
fonctionnels d'une part, domaines et questions d'autre part. Aucun chemin ou
dossier cible n'est créé.

```text
PALIER_7 = SIMULATION_MIGRATION_CONCEPTUELLE
SIMULATION_A = PASSE
SIMULATION_B = PASSE
INVARIANTS = CONSERVABLES_DANS_LES_DEUX_MODELES
DESTINATION_MATERIELLE = NON_CHOISIE
ARCHITECTURE_FINALE = NON_DECIDEE
MIGRATION_REELLE = NON_OUVERTE
```

La destination par plans favorise la lisibilité fonctionnelle et la séparation
public / preuve / provenance. La destination par domaines conserve mieux la
continuité des travaux par question, mais expose davantage au risque de
répéter les fonctions communes. Les deux simulations exigent le socle d'objets
autonomes et de relations explicites.

Avant toute migration pilote, il faudra tester le contrat sur un lot d'une
autre nature, détailler les relations probatoires et computationnelles,
examiner les objets transversaux et obtenir une décision humaine sur le lot,
la destination et le mode de retour.

## Palier 8 : mappage abstrait d'un lot secondaire transversal

Le lot secondaire est consigné dans :
`01_CADRE_METHODOLOGIQUE/mappage_abstrait_lot_secondaire_transversal_2026-08-18.md`.
Il comprend une porte philosophique, le noyau méthodologique canonique, une
carte architecturale transversale, un essai éditorial expérimental et une carte
de jonction datée. Il ne reprend donc pas la dominante scientifique du premier
lot.

```text
PALIER_8 = LOT_SECONDAIRE_TRANSVERSAL
CONTRAT_MINIMAL_SUR_LOT_SECONDAIRE = APPLICABLE_AVEC_PRECISIONS
TRANSVERSALITE = DIMENSION_REELLE_A_CONSERVER
FONCTION_DOMINANTE = INSUFFISANTE_SEULE
REGISTRES_MULTIPLES = NECESSAIRES
NON_CLASSEMENT = RECEVABLE
NOUVELLE_CATEGORIE_GENERALE = NON_JUSTIFIEE
MIGRATION = NON_OUVERTE
```

Le test confirme que T2 ne se réduit pas à la méthode, que T4 ne devient pas
une synthèse scientifique par sa richesse et que T5 ne devient pas une route
vivante par sa fonction de jonction. La transversalité peut rester une
propriété ou une relation sans produire un dossier fourre-tout. L'absence de
`04_ARCHITECTURES/README.md` reste un fait d'inventaire : elle ne justifie pas
la création immédiate d'une nouvelle porte.

## Palier 9 : mesure du coût des relations transversales

La mesure est consignée dans :
`01_CADRE_METHODOLOGIQUE/mesure_cout_relations_transversales_lot_secondaire_2026-08-18.md`.
Elle évalue qualitativement la création, la qualification, la maintenance, la
vérification et la récupérabilité des relations du lot secondaire.

```text
PALIER_9 = COUT_DES_RELATIONS_TRANSVERSALES
RELATIONS_TRANSVERSALES = GERABLES_SANS_REGISTRE_SUR_LE_LOT
COUT_ELEVE = CONCENTRE_SUR_QUELQUES_ARTICULATIONS
VUES_DE_RELATION = UTILES_SOUS_QUESTION_CIBLEE
REGISTRE_CENTRAL = NON_JUSTIFIE
AUTOMATISATION = PREMATUREE
MIGRATION = NON_OUVERTE
```

Le lot ne montre pas d'explosion relationnelle. Le coût est concentré sur les
articulations méthode / architecture, éditorial / philosophie / méthode et les
jonctions historiques. Une vue de relations ciblée pourra être testée ; un
registre général ne sera pas ouvert sans déficit de contrôle observé.

## Palier 10 : test d'une vue de relations ciblée

Le prototype est consigné dans :
`01_CADRE_METHODOLOGIQUE/test_vue_relations_ciblee_lot_secondaire_2026-08-18.md`.
Il sélectionne les articulations sensibles T1 à T5 sans résumer les objets et
sans créer de registre central.

```text
PALIER_10 = VUE_DE_RELATIONS_CIBLEE
VUE_DE_RELATIONS_CIBLEE = UTILE_SUR_LE_LOT
REGISTRE_CENTRAL = NON_REQUIS
CONTENU_CANONIQUE = NON_DUPLIQUE
RELATIONS_TRANSVERSALES = RENDUES_LISIBLES_SOUS_QUESTION
VUE_EXHAUSTIVE = NON_RECOMMANDEE
RECONSTRUIBILITE = OUI
MIGRATION = NON_OUVERTE
```

Le test confirme qu'une vue relationnelle locale peut rendre visibles les
passages entre philosophie, méthode, architecture, éditorial et provenance.
Elle doit rester une projection motivée par une question, et non devenir une
nouvelle autorité. Le prochain lot à tester sera computationnel ou probatoire,
afin d'exposer le modèle à des relations dont la portée pour un résultat est
plus directement contrôlée.

## Palier 11 : test du lot computationnel et probatoire

Le test est consigné dans :
`01_CADRE_METHODOLOGIQUE/test_lot_computationnel_probatoire_2026-08-18.md`.
Le lot comprend un protocole commun neutrino, une matrice comparative, un
manifeste de provenance ALPHA, un résultat de reproduction borné et un rapport
historique de blocage.

```text
PALIER_11 = LOT_COMPUTATIONNEL_PROBATOIRE
CONTRAT_COMPUTATIONNEL = TIENT_SUR_LE_LOT
RELATIONS_PROBATOIRES = DOIVENT_ETRE_TYPEES
DISTINCTION_MACHINE_TECHNIQUE_SCIENCE = CONSERVABLE
VUES_SCIENTIFIQUE_ET_COMPUTATIONNELLE = SEPARABLES
CALCUL_NOUVEAU = NON_LANCE
MIGRATION = NON_OUVERTE
```

Le test confirme qu'un résultat de reproduction borné ne devient pas une
nouvelle mesure, qu'une empreinte de provenance ne devient pas une validation
physique et qu'un blocage historique ne devient pas l'état courant. Les
relations computationnelles et probatoires exigent un vocabulaire plus strict
que les routes de lecture, mais elles restent compatibles avec le socle par
objets autonomes et relations explicites.

## Amendement : documentation technique, résultats et workflow du laboratoire

Le lot computationnel fait émerger une couche de reconception supplémentaire.
Le cadrage est consigné dans :
`01_CADRE_METHODOLOGIQUE/cadrage_documentation_code_pipelines_workflow_laboratoire_2026-08-18.md`.
La documentation du code et des pipelines ne sera pas traitée comme une
réécriture des résultats, ni comme une preuve scientifique par elle-même.

```text
CODE
-> ENVIRONNEMENT
-> EXECUTION
-> SORTIES_MACHINE
-> QUALIFICATION_TECHNIQUE
-> RESULTAT_SCIENTIFIQUE
-> VERDICT_ET_PORTEE
```

Quatre couches sont distinguées : documentation du code, documentation
d'exécution, qualification technique et résultat scientifique. Une cinquième
fonction, la documentation locale du workflow général du laboratoire, décrit
les passages, contrôles humains, statuts, promotions et retours ; elle reste
distincte du CI et des résultats.

```text
DOCUMENTATION_TECHNIQUE = A_INSTRUIRE
DOCUMENTATION_WORKFLOW_GLOBAL = A_CONSERVER_LOCALEMENT
RESULTATS_SCIENTIFIQUES = SEPARES_DES_SCRIPTS_ET_SORTIES
PIPELINES_PUBLICS = NIVEAUX_DE_PUBLICATION_A_DISTINGUER
CI = A_AMELIORER_PLUS_TARD
MIGRATION = NON_OUVERTE
```

Avant toute documentation exhaustive du code, un petit lot représentant un
pipeline borné, un script local et un outil transversal sera testé. Aucun
pipeline ne sera rendu public par la seule présence d'un script ou d'un
manifeste ; le niveau effectivement documenté, reproductible ou réutilisable
devra être déclaré.

## Test documentaire sur trois profils computationnels

Le test est consigné dans :
`01_CADRE_METHODOLOGIQUE/test_documentation_technique_trois_profils_2026-08-18.md`.
Il couvre un pipeline ALPHA borné, un script local d'analyse neutrino et l'outil
transversal append-only des journaux.

```text
DOCUMENTATION_DES_TROIS_PROFILS = POSSIBLE
CODE_ET_RESULTAT = SEPARABLES_ET_RELIABLES
CI = COMPOSANTE_TECHNIQUE_DU_WORKFLOW_GLOBAL
AUTOMATISATION = ALLEGEMENT_COGNITIF_SELECTIF
DECISION_HUMAINE = CONSERVEE
PUBLICATION_DE_PIPELINE = A_DECIDER_PAR_NIVEAU
MIGRATION = NON_OUVERTE
```

Le test confirme la chaîne `code -> environnement -> exécution -> sortie
machine -> qualification technique -> résultat scientifique`. Documenter le
code ne valide pas le modèle ; documenter l'exécution ne crée pas une nouvelle
mesure ; l'outil CI ne qualifie pas le contenu qu'il contrôle.

La distinction ne sépare pas artificiellement le workflow global du CI : le CI
en est une composante technique. L'amélioration future cherchera des opérations
répétitives, contrôlables et réversibles qui allègent la charge cognitive,
mais les choix de modèle, de données, de portée, de promotion et d'autorisation
restent humains.

## L'audit comme objet documentaire local

La reconception conserve également la possibilité de documenter l'audit
lui-même : phases, contre-tests, retours, décisions, effets sur la
transformation du projet et éléments non transférables. Cette documentation
ne doit pas être confondue avec les résultats scientifiques produits ou
qualifiés par l'audit.

```text
AUDIT = OBJET_DE_WORKFLOW_ET_DE_PROVENANCE
EFFETS_DE_L_AUDIT = A_EVALUER
SEPARATION_DES_PHASES = A_DECIDER_APRES_RESULTATS
TEMPLATE_AUDIT = POSSIBILITE_NON_AUTORISEE_PAR_DEFAUT
CI = COMPOSANTE_DU_WORKFLOW_GLOBAL
DECISIONS_HUMAINES = CONSERVEES
```

La valeur d'une éventuelle templateisation sera jugée après coup : gain réel
de continuité, réduction des pertes, allègement cognitif, réutilisabilité et
absence de rigidification. L'audit reste pour l'instant un workflow local du
laboratoire, documenté comme tel.

## Test d'une fiche documentaire sur un outil de conservation

La première fiche unitaire est consignée dans :
`01_CADRE_METHODOLOGIQUE/fiche_documentation_outil_append_audit_2026-08-18.md`.
Elle documente `tools/append_audit_changelog.py` comme outil de conservation
transversal.

```text
FICHE_OUTIL_APPEND = PRODUITE
CONTRAT_DOCUMENTAIRE = SUFFISANT_POUR_CE_PROFIL
GARANTIES_TECHNIQUES = DISTINCTES_DU_CONTENU
CHARGE_COGNITIVE = REDUITE_SUR_L_OPERATION_APPEND
DECISION_HUMAINE = CONSERVEE
TEMPLATE_GENERAL = NON_DEDUIT
PROMOTION_PUBLIQUE = NON_OUVERTE
```

La fiche distingue les préconditions, les garanties, les refus et les limites
de l'outil. Elle n'interprète pas le contenu ajouté, ne qualifie aucun résultat
scientifique et ne transforme pas l'outil local en workflow public. Le prochain
test comparera ce profil à un outil d'audit structurel.

## Outils internes : inventaire sélectif sans prolifération

La proposition relative aux outils mobilisés ou créés dans le laboratoire est
retenue comme un cadrage de tri, non comme un nouveau projet. Elle est décrite
dans :
`01_CADRE_METHODOLOGIQUE/cadrage_outils_internes_et_workflow_partageable_2026-08-18.md`.

```text
OUTILS_INTERNES = OBJETS_A_EVALUER
INVENTAIRE_GLOBAL = NON_LANCE
PREMIER_LOT = SELECTIF
NOUVEAU_PROJET = NON_CREE
RESULTAT_LOCAL = POSSIBLE
PROPOSITION_DE_WORKFLOW_PARTAGEABLE = A_TESTER
PROMOTION_PUBLIQUE = NON_OUVERTE
```

Le premier inventaire pourra couvrir un outil de conservation, un outil
d'audit, un script computationnel local et un outil éditorial ou de
coordination. Le critère ne sera pas la nouveauté de l'outil, mais le gain
réel de charge cognitive, la clarté de ses garanties, ses limites, sa
réutilisabilité et la conservation des décisions humaines.

## Décision de mise en veille active du fil outils

Le fil outils et workflow n'est pas clôturé catégoriquement. Il a produit les
résultats locaux nécessaires pour guider la suite, mais sa valeur fonctionnelle
et sa transportabilité seront mieux testées directement sur pièce lors des
opérations futures.

```text
FIL_OUTILS = MIS_EN_VEILLE_ACTIVE
RESULTATS_LOCAUX = CONSERVES
PROMOTION = NON_OUVERTE
TEST_DIRECT_SUR_PIECE = A_REPRENDRE_AU_BESOIN
TEMPLATE = NON_DECIDE
RETOUR_AU_FIL_PRINCIPAL = OUI
```

La suite revient donc au fil principal : documentation computationnelle,
reconception générale et tests de l'audit. Une opération concrète pourra
rouvrir le fil outils si elle apporte un discriminant nouveau ; aucune étape
artificielle d'inventaire ou de templatisation n'est ajoutée pour le fermer.

## Retour au fil principal : fiche du pipeline computationnel borné

Après la mise en veille active du fil outils, le travail reprend avec la
documentation computationnelle. La première fiche unitaire de pipeline est :
`01_CADRE_METHODOLOGIQUE/fiche_documentation_pipeline_alpha_borne_2026-08-18.md`.

```text
RETOUR_AU_FIL_PRINCIPAL = EFFECTIF
PROFIL = PIPELINE_DE_REPRISE_COMPUTATIONNELLE_BORNE
DOCUMENTATION_COMPUTATIONNELLE = SUFFISANTE_POUR_LE_PERIMETRE
CHAINES_CODE_ENVIRONNEMENT_RESULTAT = DISTINCTES_ET_RELIEES
RESULTAT_LOCAL = RECEVABLE_DANS_SON_PERIMETRE
REPRODUCTION_DE_L_ANALYSE_COMPLETE = NON_ETABLIE
PROMOTION = NON_OUVERTE
```

La fiche conserve la chaîne des opérations, la provenance du paquet, les
sorties et les limites. Elle distingue explicitement résultat machine,
qualification technique et résultat scientifique. Elle montre aussi que la
documentation computationnelle peut être suffisante pour un périmètre sans
prétendre documenter ou reproduire l'analyse entière.

Le modèle sera confronté à un lot réduit comprenant accueil, synthèse,
preuve ou protocole, règle méthodologique, provenance et essai. Le contrôle
portera sur la conservation des identités, statuts, limites, contradictions,
conditions de reprise et relations ; il pourra conclure qu'une pièce résiste
légitimement à la partition proposée.

Le test suivant comparera la forme actuelle de l'accueil des cycles à une
proposition éventuellement séparée entre carte publique et détails de
routage. La décision dépendra du gain de lisibilité et de contrôle observé,
non d'une obligation préalable de créer un document supplémentaire. Le
contenu unique, les limites, les indépendances entre cycles et les routes
scientifiques seront contrôlés avant toute proposition de promotion.

## Synthèse architecturale de contrôle

Une synthèse unique rassemble désormais les résultats de la reconception :
`01_CADRE_METHODOLOGIQUE/synthese_architecturale_controle_2026-08-18.md`.
Elle ne crée ni nouvelle phase de test ni nouvelle arborescence. Elle distingue
les invariants déjà observés, les hypothèses encore ouvertes, le fil outils en
veille active et les décisions réservées à l'humain.

```text
SYNTHESE_ARCHITECTURALE = PRODUITE
DIRECTION = COHERENTE
IMAGE_GLOBALE = PARTIELLEMENT_VISIBLE_MAIS_PLUS_CONTRAINTE
CHAOS_RECONSTRUIT = NON_DEMONTRE
RISQUE_DE_METAPROLIFERATION = REEL_ET_SURVEILLE
NOUVEAU_TEST = EXIGE_UN_DISCRIMINANT
MIGRATION = NON_OUVERTE
LECTURE_HUMAINE = REQUISE_AVANT_PASSAGE
```

Le socle provisoire reste : objets autonomes, relations explicites, plans comme
vues, domaines comme contextes, statuts et autorisations découplés. Le nombre
final de documents, l'arborescence, le registre relationnel, le template de
l'audit et le CI futur restent indécidés.

## Passage à la reconstruction effective Human-First

La synthèse de contrôle ne clôt pas l'audit et ne vaut pas architecture finale.
Elle fournit désormais une direction suffisante pour commencer la reconstruction
effective du dépôt, sans relancer une campagne générale de tests. Les tests et
cadrages précédents deviennent des contraintes de travail et des contrôles de
conservation ; ils ne sont pas remplacés par une nouvelle série d'épreuves.

```text
AUDIT_GLOBAL = NON_CLOTURE
PHASE_9 = EN_COURS
RECONSTRUCTION_EFFECTIVE = OUVERTE
RECONSTRUCTION = PROGRESSIVE, BORNEE, REVERSIBLE
RETOUR_A_LA_PHYSIQUE = EXCLU_TANT_QUE_FORME_ET_INFRASTRUCTURE_NON_RECONSTRUITES
RETOUR_A_LA_PHILOSOPHIE = EXCLU_TANT_QUE_LA_PORTEE_DE_LA_RECONSTRUCTION_N_EST_PAS_QUALIFIEE
NOUVELLE_CAMPAGNE_DE_TESTS = NON_REQUISE_A_CE_STADE
```

La reconstruction commence par des lots de portes ou de documents à fonction
dominante. Pour chaque lot :

1. identifier la fonction actuelle, le public, le contenu unique, les limites,
  les dépendances et la provenance ;
2. rédiger une forme Human-First sur la branche de travail, sans supprimer ni
  déplacer la source avant contrôle ;
3. comparer l'ancienne et la nouvelle forme sur le sens, les statuts, les
  relations, les limites et les routes ;
4. conserver les écarts, pertes éventuelles, refus et décisions dans le journal
  de phase ;
5. soumettre toute promotion, suppression ou déplacement à une décision humaine.

Le premier lot effectif doit être choisi parmi les portes d'accueil déjà
identifiées, en priorité le README racine et l'accueil des cycles. Le choix du
lot ne préjuge ni de l'arborescence finale ni de la création d'un document
supplémentaire. Le dépôt général peut donc commencer à prendre une forme
Human-First tout en restant un chantier d'audit ouvert.

## Premier lot de reconstruction effective : accueil des cycles

Le premier lot est ouvert sur `02_CYCLES_PHYSIQUES/README.md`. Le README racine
est conservé comme témoin de contrôle, car sa fonction d'accueil conceptuel et
de routage humain est déjà compatible avec le contrat Human-First établi.

La réécriture locale de l'accueil des cycles conserve :

- la distinction propre au cycle 8 entre dissémination, valeur de consensus et
  réalisation ;
- le lien vers l'évaluation scientifique du cycle ;
- la route de provenance vers l'issue #115 ;
- l'absence de réécriture rétroactive de l'évaluation.

La modification déplace seulement le détail opérationnel de l'issue hors du
flux principal, sans créer de nouveau document ni déplacer la source.

```text
LOT_1 = README_CYCLES_PHYSIQUES
README_RACINE = CONSERVE_COMME_TEMOIN
CONTENU_UNIQUE = CONSERVE
ROUTE_SCIENTIFIQUE = CONSERVE
ROUTE_DE_PROVENANCE = CONSERVE_ET_RENDU_OPTIONNEL
NOUVEAU_DOCUMENT = NON
DEPLACEMENT = NON
SUPPRESSION = NON
PROMOTION = A_DECIDER_HUMAINE
RESULTAT = POLISSAGE_HUMAN_FIRST_LOCAL_RECEVABLE
```

## Mobilisation des outils sur pièces

La clôture des tests abstraits d'outillage ne vaut pas clôture de l'usage des
outils. À partir de ce lot, les outils déjà fabriqués sont mobilisés sur les
pièces de reconstruction lorsque leur fonction et leur classe le justifient.
Le premier lot a déjà utilisé la matrice de capacité pour qualifier la cible et
l'audit structurel pour contrôler les liens, les clôtures Markdown et les
marqueurs de conflit. Les avertissements de références anciennes ont été
conservés comme dette distincte, sans élargir artificiellement le lot.

```text
TESTS_ABSTRAITS_OUTILLAGE = CLOS_DANS_LEUR_PERIMETRE
OUTILS_EXISTANTS = MOBILISABLES_SUR_PIECE
EVALUATION_SUR_PIECE = MODE_DE_TRAVAIL_ACTIF
OUTIL_APPEND_ONLY = RESERVE_A_LA_JOURNALISATION_STRUCTURELLE
NOUVEL_OUTIL = NON_REQUIS_SANS_DEFICIT
CHAQUE_OPERATION = OUTIL + CLASSE + ENTREE + SORTIE + LIMITE + DECISION
CHANGELOG = MEMOIRE_OPERATOIRE_ET_PROVENANCE
CHANGELOG != AUTORITE_SCIENTIFIQUE
```

Le polissage intervient donc dans le workflow Human-First dès qu'une pièce est
reconstruite, sous la forme d'une opération contrôlée et réversible. Les
protocoles de réécriture restent les règles de rédaction et de contrôle de
perte ; ils ne constituent pas un préalable pour différer toute application,
ni une permission de réécrire sans qualification de la pièce.

L'outil d'écriture est explicitement ajouté à cette mobilisation. Il s'appuie
sur `01_CADRE_METHODOLOGIQUE/Reecriture_positive_vocabulaire_v0_3.md` et
`01_CADRE_METHODOLOGIQUE/Protocole_travail_redaction_post_philosophie_v0_1.md`.
Pour chaque pièce, il impose une relecture complète avant rédaction, puis
nomme la classe, le public, la fonction, la portée, les acquis et les limites.
La formulation positive vient ensuite ; elle conserve les refus, les dettes,
les conditions de rupture et les bornes de validité.

```text
OUTIL_D_ECRITURE = MOBILISE_SUR_PIECE
RELECTURE_COMPLETE = PREALABLE_A_LA_REECRITURE
REECRITURE_POSITIVE = ACTIVE
LIMITES_ET_REFUS = CONSERVES
COMPARAISON_AVANT_APRES = REQUISE
SKILL_DE_REDACTION = A_EVALUER_APRES_USAGES_REELS
```

La skill n'est donc pas créée à ce stade. Plusieurs opérations sur des classes
de documents différentes devront d'abord montrer un gain réel de continuité et
de charge cognitive, sans transformer le protocole local en nouvelle couche
obligatoire.

## Préparation opérationnelle du workflow

Le terme « compilation » est retenu ici comme métaphore informatique bornée :
il désigne la vérification que les fonctions nécessaires à une opération de
reconstruction sont disponibles, compatibles et appelables dans le dépôt. Il
ne désigne ni une compilation du sens, ni une validation scientifique, ni une
automatisation complète de la rédaction.

```text
COMPILATION_METAPHORIQUE = PARTIELLE_ET_LOCALE
PERIMETRE_CONTROLE = OUTILS_ET_CONTRATS_RECENTS
WORKFLOW_GLOBAL = NON_COMPILE
CORPUS_DE_REECRITURE = NON_TRAITE
OUTILS = EXECUTABLES_DANS_LEUR_PERIMETRE
CONTRATS = PRESENTS_DANS_LEUR_PERIMETRE
ENTREES_ET_SORTIES = IDENTIFIABLES_LOCALLEMENT
LIMITES = DECLAREES_MAIS_COUVERTURE_INCOMPLETE
LECTURE_HUMAINE = NON_DELEGABLEE
DECISION_DE_PROMOTION = NON_AUTOMATIQUE
```

Le contrôle de préparation a confirmé seulement :

- l'exécutabilité de l'outil append-only et de l'audit structurel ;
- la présence du contrat de mobilisation sélective sur pièce ;
- la présence du circuit de relecture complète et de réécriture positive ;
- l'absence d'erreur structurelle dans le corpus contrôlé.

Il n'a pas confirmé la qualité de la prose du corpus, la réécriture complète
des documents, la couverture des cercles prévus, ni la compilation de toutes
les fonctions nécessaires à la reconstruction générale. Les deux portes déjà
polies sont des pièces pilotes : leur texte reste susceptible d'une reprise
Human-First complète.

Les neuf avertissements de références potentiellement anciennes restent une
dette documentaire identifiée. Ils ne bloquent pas les contrôles locaux, mais
ils contribuent à montrer que l'état global n'est pas prêt à être déclaré
terminé. La prochaine étape est donc la compilation progressive du workflow
complet par classes de documents, suivie d'une réécriture réelle et contrôlée
du corpus, sans prétendre que les premiers polissages constituent ce résultat.

## Deuxième pièce : porte locale du cycle 7

Le circuit de reconstruction est appliqué au README local du cycle 7,
`02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/README.md`, dont la fonction est
plus sensible qu'une carte générale : il route deux lignes scientifiques
indépendantes et expose des états bornés, des blocages et des permissions.

La relecture complète a conduit à un polissage limité des passages de fonction,
de provenance et de reprise. Les blocs d'état de `C7-C1 / X(z) / SCI-1` et de
`C7-GAL / C0` sont conservés, ainsi que les routes vers `#119` et `#120`.
L'écriture positive rend la fonction de la porte plus directe sans transformer
un blocage en autorisation, un état technique en résultat scientifique ou une
issue en autorité générale.

```text
PIECE_2 = README_LOCAL_CYCLE_7
CLASSE = PORTE_DE_ROUTAGE_SCIENTIFIQUE_VIVANTE
RELECTURE_COMPLETE = EFFECTUEE
REECRITURE = BORNEE_AU_CADRE_ET_AU_ROUTAGE
ETATS_SCIENTIFIQUES = CONSERVES
INDEPENDANCE_C7_C1_C7_GAL = CONSERVEE
PORTES_SCI1_B1_G2 = CONSERVEES
RESULTAT = POLISSAGE_HUMAN_FIRST_RECEVABLE_SUR_PIECE_SENSIBLE
PROMOTION = A_DECIDER_HUMAINE
```
