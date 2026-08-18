# Changelog de la phase 2 — audit scientifique des resultats porteurs

## Fonction et rang

Ce fichier est le journal courant de la phase 2 scientifique sous le cadrage
#130. Il n'est ni une synthese scientifique, ni une nouvelle autorite, ni un
remplacement du changelog integral.

Les regles d'ecriture heritees sont celles de :

- `01_CADRE_METHODOLOGIQUE/changelog_audit_integral.md` ;
- `01_CADRE_METHODOLOGIQUE/changelog_audit_integral_suite_2026-08-18.md` ;
- `01_CADRE_METHODOLOGIQUE/programme_audits.md`, notamment les sections 1.7 et 1.8.

Le journal de phase conserve les resultats positifs et negatifs, limites,
dettes, contradictions, triangulations, incidents, effets sur les decisions et
etats `NON_ETABLI` ou `NON_DECIDABLE`. Il peut pointer vers une entree deja
complete au lieu de la recopier.

```text
PHASE = 2 / AUDIT_SCIENTIFIQUE_DES_RESULTATS_PORTEURS
ISSUE_DE_CADRAGE = #130
STATUT = EN_COURS
CORPUS_DE_DEPART = RESULTATS_ET_DETTES_REMONTEES_EN_PHASE_1
RELECTURE_GLOBALE_DES_668_BLOBS = NON_PAR_DEFAUT
NOUVEAU_CALCUL = NON_LANCE
MUTATION_SCIENTIFIQUE = AUCUNE
```

## Regle de raccord sans perte

Les premieres entrees de phase 2 ont ete appendues dans la partie 2 du
changelog integral avant l'ouverture de ce fichier. Elles restent dans leur
emplacement historique et ne sont pas recopiees ici. Le present journal prend
le relais a partir de cette entree de raccord.

Entrees historiques de phase 2 a consulter :

- validation de #130 et transition phase 1 -> phase 2 ;
- cartographie initiale de C1 ;
- triangulation C1 / QCD-T1 / PR #18 ;
- qualification locale de `alpha(Q2)` et `m_p/m_e` ;
- qualification des contraintes temporelles et spatiales de `alpha`.

```text
SOURCE_HISTORIQUE = changelog_audit_integral_suite_2026-08-18.md
RACCORD = APRES_COMMIT_02df636
DUPLICATION = REFUSEE
PROVENANCE = CONSERVEE_PAR_FICHIER_ET_HISTORIQUE_GIT
```

Cette organisation est technique. Elle ne reduit pas la matiere des entrees
historiques et ne ferme pas la phase 2.

## Etat herite de la phase 1

```text
PHASE_1_DOCUMENTAIRE = CLOTUREE_SOUS_REGIMES_DECLARES
COUVERTURE = MANIFESTE_ET_REGIMES_DOCUMENTES
QUALIFICATION_SCIENTIFIQUE = NON_DEDUITE_AUTOMATIQUEMENT
AUDITS_ANTERIEURS = CONSERVES, SUFFISANCE_CONTEXTUELLE_NON_PRESUMEE
```

## Etat de la phase 2

```text
C1 = QUALIFIE_DANS_LE_PERIMETRE_LOCAL
ALPHA_Q2 = QUALIFIE_DANS_LE_PERIMETRE_LOCAL
ALPHA_TEMPOREL = QUALIFIE_DANS_LE_PERIMETRE_LOCAL
ALPHA_SPATIAL = QUALIFIE_LOCAL_PAR_REATTRIBUTION_PARTIELLE, GLOBAL_SUSPENDU
M_P_SUR_M_E = QUALIFIE_DANS_LE_PERIMETRE_LOCAL, ATTRIBUTION_CAUSALE_NON_ETABLIE
QCD_T1 = COMPARABILITE_CONDITIONNELLE, EQUIVALENCE_REFUSEE, GLOBAL_SUSPENDU
USAGE_TRANSVERSAL_NON_CONDITIONNE = NON_ETABLI
REOUVERTURE_C1 = NON_DECLENCHEE
```

## Prochaine instruction

Passer a la sentinelle S2 de #130 : cycle 3, neutrinos. Commencer par la
synthese active, identifier l'usage materiel eventuel, puis descendre seulement
vers N0-N5 si une conclusion l'exige. Le controle C2 et le controle de rang C7
restent des controles bornes ; ils n'autorisent ni sampling ni audit scientifique
hors critere d'extension.

```text
PROCHAINE_SENTINELLE = S2 / CYCLE_3_NEUTRINOS
PORTE_D_APPROFONDISSEMENT = A_TESTER
TRIANGULATION = SUR_LACUNE_OU_CONTRADICTION_MATERIELLE
ARRET_LOCAL = DES_QUE_LA_QUESTION_EST_SUFFISAMMENT_INSTRUITE
```
