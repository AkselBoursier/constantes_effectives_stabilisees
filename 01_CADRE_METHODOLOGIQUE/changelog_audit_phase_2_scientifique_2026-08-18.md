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

---

## 2026-08-18 — Contrôles pré-engagés C7 et C2

### NC-RANG — Cycle 7

Le README vivant de C7 confirme deux lignes indépendantes et sépare leurs
états. Pour C7-C1, la cause du problème de persistance est qualifiée au niveau
source/contrat, mais `SCI1 = NON_QUALIFIABLE`, `B1 = NON_AUTORISEE` et
`NEW_SAMPLING = NON_AUTORISE`. Pour C7-GAL, l'accès matériel aux HDF5 bloque
la fermeture de C0-A et `G2 = NON_OUVERTE`.

```text
ACTIVITE_OPERATIONNELLE = ETABLIE
SUPPORT_SCIENTIFIQUE = NON_DEDUIT
AUTORISATION_COMPUTATIONNELLE = NON_DEDUITE
CONTROLE_C7 = EXECUTE_DANS_LE_PERIMETRE_DE_RANG
REAUDIT_SCIENTIFIQUE_C7 = NON_DECLENCHE
NOUVEAU_SAMPLING = NON_LANCE
```

C7 confirme donc le falsificateur de rang prévu par #130, sans produire de
résultat scientifique nouveau pour la phase 2.

### CHALLENGE — Cycle 2

La synthèse de récupération décrit un cycle hétérogène, redistribué vers les
cycles Saveur–Higgs, effectif et cosmologique. Elle conserve comme acquis une
distinction entre fonction, relation, explication de valeur et mécanisme, mais
refuse l'unité physique et la taxonomie initiale du cycle ; les vérifications
empiriques indépendantes restent des dettes séparées.

```text
CHALLENGE_C2 = MATERIEL_POUR_L_HOMOGENEITE_ET_LA_PORTEE_DE_L_ARCHITECTURE
CONTRE_EXEMPLE_SCIENTIFIQUE_INDEPENDANT = NON_ETABLI
EXTENSION_SCIENTIFIQUE_C2 = NON_DECLENCHEE
AUDIT_C2_COMPLET = NON_OUVERT
```

C2 exerce donc une pression adversariale réelle : une cohérence architecturale
ne peut pas être promue en unité physique parce que des fonctions ont été
regroupées dans un même cycle. Mais son contenu actuel ne permet pas de
qualifier scientifiquement de nouveaux résultats sans ouvrir une instruction
distincte des dettes qu'il énumère. Il n'y a pas de résurgence non prévue par
les critères d'extension de #130.

Cette limite de portée n'est pas inscrite comme une dette autonome de phase 2.
Elle reste un résultat du challenge, utile pour borner les conclusions et pour
orienter éventuellement la phase 3 ; une dette scientifique ne sera déclarée
que si une instruction ultérieure identifie une question précise, un gain
discriminant attendu et une condition de reprise.

```text
C2_LIMITE_DE_PORTEE = RESULTAT_DE_CHALLENGE
DETTE_SCIENTIFIQUE_C2 = NON_DECLAREE_A_CE_PALIER
DECLARATION_DETTE_FUTURE = CONDITIONNELLE_A_UNE_QUESTION_PRECISE
```

---

## 2026-08-18 — Clôture de la phase 2 sous périmètre qualifié

Les six sentinelles candidates ont franchi leur porte d'approfondissement, et
les deux contrôles pré-engagés ont été exécutés dans leur périmètre borné.

```text
S1_C1 = QUALIFIE_DANS_LE_PERIMETRE_LOCAL
S2_C3 = QUALIFIE_DANS_LE_PERIMETRE_LOCAL
S3_C5 = QUALIFIE_DANS_LE_PERIMETRE_LOCAL
S4_C6 = QUALIFIE_DANS_LE_PERIMETRE_LOCAL
S5_C8 = QUALIFIE_DANS_LE_PERIMETRE_LOCAL
S6_C10 = QUALIFIE_DANS_LE_PERIMETRE_LOCAL
C7 = CONTROLE_DE_RANG_EXECUTE, SANS_REAUDIT_SCIENTIFIQUE
C2 = CHALLENGE_ADVERSARIAL_EXECUTE, EXTENSION_NON_DECLENCHEE
C4_C9 = HORS_PERIMETRE, A_REOUVRIR_SUR_CRITERE
```

### Résultat de phase

La phase 2 établit dans son périmètre que plusieurs résultats locaux soutiennent
des distinctions opératoires concernant cible, transformation, accès,
constitution, modèle et domaine. Elle n'établit pas une architecture
scientifique universelle, une taxonomie nouvelle, une originalité générale ou
un transfert automatique vers les phases conceptuelle, méthodologique ou
philosophique.

```text
PHASE_2 = QUALIFIEE_DANS_LE_PERIMETRE
USAGE_TRANSVERSAL_NON_CONDITIONNE = NON_ETABLI
EFFET_SUR_PHASE_3 = CONDITIONNEL, NON_AUTORISATION_AUTOMATIQUE
DETTES_COMPUTATIONNELLES = CONSERVEES
DETTES_DE_FRAICHEUR = CONSERVEES_LORSQU_ESPACEES
NOUVEAU_CALCUL = NON_LANCE
MUTATION_SCIENTIFIQUE = AUCUNE
```

### Conditions de réouverture

La phase 2 reste réouvrable si un résultat sentinelle est révisé, si une dette
scientifique devient matériellement nécessaire à une conclusion, si un
contre-audit produit un faux raccord ou si une question validée introduit un
résultat hors périmètre. Une réouverture devra identifier le déclencheur, la
conclusion à retester et le périmètre minimal.

La phase 3 conceptuelle n'est pas ouverte par cette clôture.

```text
PROCHAINE_ETAPE = ATTENDRE_OUVERTURE_EXPLICITE_DE_L_ETAPE_3
ETAT_DES_PHASES_3_A_9 = NON_OUVERTES_PAR_CETTE_PHASE
```

---

## 2026-08-18 — S4 : théories effectives à basse énergie

La porte d'approfondissement est franchie par l'évaluation active du cycle 6,
qui identifie un usage matériel : distinguer fixité d'une composante, stabilité
d'une prédiction et validité d'une description.

```text
USAGE_MATERIEL_S4 = ETABLI
FIXITE_DE_COMPOSANTE = COEFFICIENT_OU_PARAMETRE_DANS_UNE_CONVENTION
STABILITE_DE_PREDICTION = OBSERVABLE_SOUS_COMPENSATION_DES_DEPENDANCES_AUXILIAIRES
VALIDITE_DE_DESCRIPTION = TRONCATURE_AVEC_ERREUR_CONTROLEE_DANS_UN_DOMAINE
```

Les cas Fermi, QCD et gravitationnel montrent trois opérations différentes
(réduction locale, changement de régime dynamique et expansion hiérarchique).
Le gain est local et indépendant du vocabulaire interne : matching, running,
power counting et contrôle des corrections organisent une description sans
produire une espèce uniforme de « constante effective ».

```text
S4 = QUALIFIEE_DANS_LE_PERIMETRE_LOCAL
ANCIENNE_TAXONOMIE_INTER_FAMILLES = NON_RESTAUREE
TRANSFERT_PHILOSOPHIQUE_GENERAL = NON_ETABLI
NOUVEAU_CALCUL = NON_LANCE
```

---

## 2026-08-18 — S5 : métrologie du Système international

Le cycle 8 franchit la porte d'approfondissement par son effet différentiel
local sur les expériences, réalisations, incertitudes et inférences.

```text
USAGE_MATERIEL_S5 = ETABLI
INVARIANCE = PROPRIETE_PHYSIQUE_SOUS_TRANSFORMATIONS
VALIDITE_CONTROLEE = PREDICTION_DANS_UN_DOMAINE_AVEC_ERREUR_ESTIMABLE
EXACTITUDE_DEFINITIONNELLE = VALEUR_NUMERIQUE_FIXEE_SANS_INCERTITUDE_DANS_UN_SYSTEME
ROBUSTESSE_DE_REALISATION = REPRODUCTION_DANS_LES_INCERTITUDES_DECLAREES
```

Le résultat établi est une architecture métrologique définitionnelle et
institutionnelle, avec déplacement de l'incertitude vers les réalisations et
les grandeurs dérivées. L'hétérogénéité physique de `c`, `h`, `e`, `k_B`, `N_A`,
`Delta nu_Cs` et `K_cd` est conservée ; le rôle définissant commun ne crée pas
une nature physique commune.

```text
S5 = QUALIFIEE_DANS_LE_PERIMETRE_LOCAL
GAIN_DIFFERENTIEL_LOCAL = ETABLI
TRANSFERT_PHILOSOPHIQUE_GENERAL = NON_ETABLI
PASSAGE_A_LA_COSMOLOGIE = AUTORISE_DANS_LE_DOCUMENT_SOURCE, NON_OUVERT_PAR_CET_AUDIT
NOUVEAU_CALCUL = NON_LANCE
```

---

## 2026-08-18 — S6 : quasi-fixité électrofaible dynamique

Le cadrage et les résultats locaux des phases 2–4 ont été examinés comme tests
de modèles bornés. Leur fonction matérielle est de tester si une fixité tardive
peut être constituée dans un même univers, avec un bilan énergétique acceptable.

```text
USAGE_MATERIEL_S6 = ETABLI
PHASE_2_MODELE_CONSERVATIF = AUCUN_POINT_DU_SCAN_SATISFAISANT_TOUTES_LES_CONDITIONS
PHASE_3_REGIME_QUARTIQUE = INSUFFISANT_SANS_EVACUATION_OU_REDISTRIBUTION
PHASE_4_TOY_DISSIPATIF = FENETRE_PHENOMENOLOGIQUE_NON_VIDE
```

La phase 4 établit seulement qu'un bilan énergétique ouvert peut occuper une
fenêtre paramétrée avant la BBN avec une entropie contrôlée dans le toy model.
Elle ne dérive pas `Gamma_phi` d'un lagrangien, ne réalise pas une
thermalisation complète et ne décrit pas l'histoire réelle de l'univers.
Les résultats négatifs des phases 2–3 restent conservés comme falsificateurs
locaux : amortir la variable ne suffit pas à rendre acceptable l'énergie du
porteur.

```text
S6 = QUALIFIEE_DANS_LE_PERIMETRE_LOCAL
RESULTAT_SCIENTIFIQUE_UNIVERSEL = NON_ETABLI
MECANISME_MICROSCOPIQUE = NON_ETABLI
REINTERPRETATION_DU_TOY_MODEL_EN_HISTOIRE_PHYSIQUE = REFUSEE
NOUVEAU_CALCUL = NON_LANCE
```
