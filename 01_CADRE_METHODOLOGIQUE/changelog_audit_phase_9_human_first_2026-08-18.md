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
