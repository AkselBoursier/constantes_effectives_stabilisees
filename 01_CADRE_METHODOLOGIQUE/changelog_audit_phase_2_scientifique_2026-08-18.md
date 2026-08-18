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

---

## 2026-08-18 — S2 : cycle 3, fonctions non équivalentes d'un spectre

### Porte d'approfondissement

La synthèse active du cycle 3 identifie un usage matériel : soutenir la
distinction entre un même secteur physique et plusieurs fonctions contraintes
par des accès différents. Cet usage ne repose pas sur le seul mot « masse » ni
sur une illustration documentaire.

```text
USAGE_MATERIEL_S2 = ETABLI
QUESTION = COMPARER_DES_FONCTIONS_D_UN_SPECTRE_SANS_LES_RENDRE_INTERCHANGEABLES
POINT_DE_DESCENTE = N5_MATRICE_COMPARATIVE_QUATRE_ACCES
N0_A_N4 = NON_DESCENDUS_A_CE_PALIER
```

### Résultat local examiné

N5 distingue :

```text
N1 = DIFFERENCES_DE_MASSES, MELANGE, PHASE_DE_DIRAC
N2 = MOYENNE_QUADRATIQUE_ELECTRONIQUE
N3 = SOMME_COSMOLOGIQUE
N4 = DEMI_VIE, PUIS AMPLITUDE_COHERENTE_CONDITIONNELLE
```

La comparaison devient recevable seulement après déclaration d'un spectre
latent, de la matrice PMNS, de l'ordre, de la masse minimale et des hypothèses
propres à la cosmologie ou à la double bêta. N5 associe à chaque accès sa trace,
son modèle de passage, sa fonction contrainte, ses absences structurelles et
son niveau de reproductibilité.

### Portée et limites

```text
RESULTAT_LOCAL = FONCTIONS_NON_EQUIVALENTES_D_UN_MEME_SECTEUR = ETABLI
PONTS_DE_COMPARAISON = DECLARES_ET_BORNES
COMPATIBILITE_GENERALE = QUALIFIEE_A_LA_COUPURE, SANS_CONTRADICTION_MODELE_INDEPENDANTE
TENSION_N1_N3 = CONDITIONNELLE_A_LAMBDA_CDM_ET_AUX_CONSTRUCTIONS_STATISTIQUES
AJUSTEMENT_CONJOINT = NON_ETABLI
DETERMINATION_DE_L_ORDRE = NON_ETABLIE_COMME_RESULTAT_UNIVERSEL
NATURE_DIRAC_MAJORANA = NON_TRANCHEE
```

La fonction comparative de S2 est donc qualifiée dans son périmètre : elle
montre comment un même secteur peut être contraint par des grandeurs non
équivalentes, et où les ponts physiques ou inférentiels ajoutent leurs
hypothèses. Elle ne fournit pas une mesure unique de la masse des neutrinos,
ni un ajustement conjoint reproductible.

```text
S2 = QUALIFIEE_DANS_LE_PERIMETRE_LOCAL
USAGE_TRANSVERSAL_NON_CONDITIONNE = NON_ETABLI
TRIANGULATION_SUPPLEMENTAIRE = NON_REQUISE_A_CE_PALIER
DETTE_COMPUTATIONNELLE = CONSERVEE
NOUVEAU_CALCUL = NON_LANCE
PROCHAINE_SENTINELLE = S3 / CYCLE_5_SAVEUR_HIGGS
```

---

## 2026-08-18 — S3 : cas électronique Saveur–Higgs

### Porte d'approfondissement

La synthèse active du cycle 5 porte un usage matériel distinct : elle utilise
le cas électronique pour tester comment une architecture de relations devient
un réseau de passages probatoires, sans confondre masse physique, paramètre
renormalisé, Yukawa inféré et accès direct au vertex Higgs–électron.

```text
USAGE_MATERIEL_S3 = ETABLI
QUESTION = DISTINGUER_ARCHITECTURE, DETERMINATION, INFERENCE, RACCORDEMENT, ACCES_DIRECT
POINT_DE_DESCENTE = SYNTHESE_ACTIVE_S1_S3
S1_A_S3 = NON_DESCENDUS_A_CE_PALIER
```

### Résultat local examiné

Le cas distingue les cibles :

```text
M_E = MASSE_PHYSIQUE
M_E_S_MU = PARAMETRE_DE_MASSE_RENORMALISE
Y_E_S_MU = YUKAWA_RENORMALISE_INFERÉ
V_S_MU = PARAMETRE_ELECTROFAIBLE_RENORMALISE
V_F = ECHELLE_DERIVEE_DE_G_F
G_HEE = VERTEX_HIGGS_ELECTRON
```

Il distingue également trois rangs de la relation masse–Yukawa : identité nue,
paramétrisation renormalisée et raccordement radiatif à une masse physique. La
chaîne probatoire va de la détermination métrologique de `M_e` à l'inférence du
Yukawa sous cadre déclaré, puis aux accès indirects et à la recherche directe.

### Portée et limites

```text
M_E = DETERMINÉE_AVEC_GRANDE_PRECISION
Y_E = INFERE_SOUS_MODELE_ET_SCHEMA_DECLARÉS
ACCES_INDIRECTS = COMPLEMENTAIRES, MODELE_DEPENDANTS
H_E_E_DIRECT = BORNE_SANS_OBSERVATION
ORIGINE_DU_YUKAWA = NON_EXPLIQUEE
GENERALISATION_AUX_AUTRES_FERMIONS = NON_ETABLIE
AJUSTEMENT_GLOBAL_SMEFT = NON_ETABLI
```

Le lot électronique établit donc localement qu'une relation structurelle peut
être accompagnée d'un réseau de passages probatoires indexés. Il ne fournit ni
mesure directe acquise du Yukawa électronique, ni explication de la hiérarchie
fermionique, ni autorisation de propager automatiquement le profil aux autres
fermions ou matrices.

```text
S3 = QUALIFIEE_DANS_LE_PERIMETRE_LOCAL
USAGE_TRANSVERSAL_NON_CONDITIONNE = NON_ETABLI
TRIANGULATION_SUPPLEMENTAIRE = NON_REQUISE_A_CE_PALIER
REOUVERTURE_S3 = SUR_MATERIAU_MODIFIANT_CIBLE, RANG OU VERDICT
NOUVEAU_CALCUL = NON_LANCE
PROCHAINE_SENTINELLE = S4 / CYCLE_6_THEORIES_EFFECTIVES_BASSE_ENERGIE
```
