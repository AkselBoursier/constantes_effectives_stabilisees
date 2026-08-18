# Changelog de la phase 4 — audit methodologique

## Fonction et rang

Ce fichier est le journal courant de la phase 4 methodologique, ouverte apres
la qualification de la phase 3. Il ne modifie pas le cadre canonique et ne
autorise aucune reecriture durable par lui-meme.

Regles heritees :

- `01_CADRE_METHODOLOGIQUE/programme_audits.md`, sections 1.7 et 1.8 ;
- `01_CADRE_METHODOLOGIQUE/changelog_audit_integral.md` ;
- `01_CADRE_METHODOLOGIQUE/changelog_audit_phase_2_scientifique_2026-08-18.md` ;
- `01_CADRE_METHODOLOGIQUE/changelog_audit_phase_3_conceptuelle_2026-08-18.md`.

```text
PHASE = 4 / AUDIT_METHODOLOGIQUE
STATUT = QUALIFIEE_DANS_LE_PERIMETRE
PHASE_2 = QUALIFIEE_DANS_LE_PERIMETRE
PHASE_3 = QUALIFIEE_DANS_LE_PERIMETRE
PHASE_5_ET_SUIVANTES = NON_OUVERTES
MUTATION_CANONIQUE = AUCUNE
REECRITURE_DOCUMENTAIRE = AUCUNE
NOUVEAU_CALCUL = NON_LANCE
```

## Point de depart

La phase 4 repart des resultats scientifiques et des fonctions conceptuelles
qualifies. Elle ne relit pas par defaut le corpus general. Elle teste si les
regles et distinctions methodologiques sont justifiees par les problemes et
supports etablis, ou si elles sont locales, redondantes, trop fortes, mal
placees, non justifiees ou non decidables.

Sources initiales :

- `01_CADRE_METHODOLOGIQUE/Ajustements_directeurs_D1_D5_regimes_constance_v0_1.md` ;
- `01_CADRE_METHODOLOGIQUE/Decision_statuts_constance_acces_constitution_v0_1.md` ;
- `01_CADRE_METHODOLOGIQUE/refondation-du-domaine.md` ;
- sorties F1–F8 de la phase 3 ;
- sorties locales des phases 2 et 3, uniquement lorsqu'une regle depend d'elles.

```text
POINT_DE_DEPART = REGLES_ET_DISTINCTIONS_DEJA_EN_PLACE
TEST = JUSTIFICATION_PAR_PROBLEME, DISCRIMINATION, RISQUE ET SUPPORT
RELECTURE_GLOBALE = NON_PAR_DEFAUT
```

## Questions de phase

1. D1–D5 controlent-ils effectivement les erreurs et confusions rencontrees ?
2. Les regles sont-elles proportionnees aux gains discriminants observes ?
3. Une regle locale est-elle promue au-dela de son domaine ?
4. Une distinction est-elle redondante avec les pratiques disciplinaires ou
   suffisamment utile pour un controle transversal ?
5. Une regle est-elle trop forte, mal placee, non justifiee ou non decidable ?
6. Quelles consequences documentaires sont justifiees, et lesquelles doivent
   rester suspendues ?

## Carte initiale des objets methodologiques

```text
D1 = CONSTANCE / STABILISATION
D2 = PORTEUR / TRANSFORMATION / REGIME / ECHELLE / TOLERANCE
D3 = DIMENSIONS_DE_L_ENQUETE / PORTEE_DE_L_ENONCE
D4 = TYPAGE_DES_DEPENDANCES_DE_CHEMIN
D5 = DEUX_QUESTIONS_PUBLIQUES
OBJET_ACCES_CONSTITUTION = DECISION_DE_RANG_ACTIVE
```

Cette carte est un perimetre de test, non une autorisation d'appliquer D1–D5 a
chaque document ni de modifier les documents sources.

## Contrat de qualification methodologique

Pour chaque regle examinee, conserver :

```text
PROBLEME_CONTROLE
SUPPORT_SCIENTIFIQUE_OU_CONCEPTUEL
DISCRIMINATION_OBSERVEE
ALTERNATIVE_OU_REDONDANCE
RISQUE_DE_SURPORTÉE
DECISION = CONSERVEE / LOCALE / REDONDANTE / TROP_FORTE / NON_JUSTIFIEE / NON_DECIDABLE
EFFET_SUR_UNE_MUTATION = NON_ETABLI_PAR_DEFAUT
```

Les sorties positives et negatives ont le meme rang probatoire. Une regle
coherente mais sans gain discriminant peut etre conservee comme materiau local
sans devenir une regle directrice.

## Premiere instruction

Commencer par D1–D3, qui sont deja mis a l'epreuve dans les phases 2 et 3 :

- tester la separation constance/stabilisation ;
- tester la declaration du porteur et de la transformation ;
- tester la separation des dimensions de l'enquete et de la portee.

```text
PREMIERE_INSTRUCTION = D1_A_D3
PHASE_4 = EN_COURS
MUTATION_CANONIQUE = NON_AUTORISEE_PAR_CE_JOURNAL
PROCHAINE_DECISION = QUALIFIER_LA_JUSTIFICATION_D_UNE_REGLE
```

---

## 2026-08-18 — D1–D3 : justification methodologique locale

### D1 — constance et stabilisation

Les phases 2 et 3 montrent un probleme controle : une non-detection, une
calibration, une reconstruction ou une dissipation peuvent stabiliser un acces
ou un regime sans etablir une constance de l'objet. `alpha(Q2)` fournit le
contrepoint d'une relation d'evolution qualifiee sans histoire temporelle de
stabilisation.

```text
PROBLEME_CONTROLE = CONFUSION_DU_STATUT_DE_L_OBJET_AVEC_LES_CONDITIONS_D_ASSERTION
DISCRIMINATION = CHANGE_LE_RANG_D_UNE_CONCLUSION
REDONDANCE = PARTIELLE_DANS_LES_DOMAINES, NON_TRANSVERSALEMENT_SUFFISANTE
DECISION = CONSERVEE_COMME_REGLE_DE_RANG
PORTEE = LOCALE_AUX_ENONCES_INDEXES
EFFET_SUR_UNE_MUTATION = NON_ETABLI
```

D1 est justifiee, mais n'autorise aucune lecture dynamique de toute constance.

### D2 — porteur et transformation

Les cycles 1, 3, 5, 6, 8 et 10 montrent que le porteur du test peut etre une
observable, une relation, un coefficient, une prediction ou une description,
et que la transformation peut relever du temps, de l'echelle, d'un schema,
d'un raccordement ou d'une voie d'acces. Sans cette declaration, les verdicts
locaux se fusionnent indeument.

```text
PROBLEME_CONTROLE = ATTRIBUTION_SANS_CIBLE_NI_TRANSFORMATION_EXPLICITE
DISCRIMINATION = PERMET_DE_BORNER_VARIATION, MAINTIEN ET COMPARABILITE
REDONDANCE = VOCABULAIRES_LOCAUX_PRESENTS, CONTRAT_TRANSVERSAL_NON_REDONDANT
DECISION = CONSERVEE_COMME_CONTROLE, NON_COMME_FORMULAIRE_UNIVERSEL
PORTEE = METHODOLOGIQUE_TRANSVERSALE
EFFET_SUR_UNE_MUTATION = NON_ETABLI
```

### D3 — dimensions de l'enquete et portee de l'enonce

La phase 2 a separe les fonctions physiques des niveaux de conclusion ; la
phase 3 a confirme qu'une distinction d'acces ne porte pas automatiquement une
portee ontologique. D3 evite donc qu'une conclusion locale sur l'objet, la
constitution ou l'acces soit promue au-dela de son rang.

```text
PROBLEME_CONTROLE = CONFUSION_DU_LIEU_DE_L_OPERATION_AVEC_LA_PORTEE_DU_VERDICT
DISCRIMINATION = SEPARATION_OBJET_CONSTITUTION_ACCES / PHYSIQUE EPISTEMIQUE ONTOLOGIQUE
REDONDANCE = NON_ETABLIE, DOUBLE_COORDONNEE NECESSAIRE
DECISION = CONSERVEE_COMME_CONTROLE_INTERNE
PORTEE = BORNEE, Q3_NON_PUBLIQUE
EFFET_SUR_UNE_MUTATION = NON_ETABLI
```

### Sortie D1–D3

```text
D1 = JUSTIFIEE_ET_CONSERVEE
D2 = JUSTIFIEE_ET_CONSERVEE_COMME_CONTROLE
D3 = JUSTIFIEE_ET_CONSERVEE_COMME_COORDONNEE_NON_HIERARCHIQUE
SURPORTÉE = NON_REPRODUITE
MUTATION_CANONIQUE = NON_AUTORISEE
PROCHAINE_INSTRUCTION = D4_D5
```

---

## 2026-08-18 — D4–D5 : chemins et questions publiques

### D4 — typage des dependances de chemin

La phase 2 a montre que running, calibration, ajustement, histoire documentaire
et dynamique physique ne sont pas interchangeables. Le cycle 10 et l'audit des
trajectoires fournissent le contre-test direct : une suite ordonnee n'est pas
automatiquement une trajectoire physique.

```text
PROBLEME_CONTROLE = CONVERSION_D_UNE_SEQUENCE_EN_HISTOIRE_PHYSIQUE
DISCRIMINATION = SEPARE_PHYSIQUE, ECHELLE, EXPERIMENTAL, METROLOGIQUE,
                 COMPUTATIONNEL, INFERENTIEL, HISTORIQUE, REPRESENTATION
REDONDANCE = VOCABULAIRES_LOCAUX_PRESENTS, TYPAGE_TRANSVERSAL_JUSTIFIE
DECISION = CONSERVEE_COMME_CONTROLE_DE_TYPAGE
PORTEE = LOCALE_AU_CHEMIN_QUI_MODIFIE_L_ARGUMENT
EFFET_SUR_UNE_MUTATION = NON_ETABLI
```

D4 n'impose pas de nommer un chemin lorsque cette distinction ne change aucun
verdict ; les sorties `NON_ETABLI` et `NON_PERTINENTE` restent recevables.

### D5 — deux questions publiques

Les phases 2 et 3 utilisent effectivement les deux questions : la premiere
porte sur la frontiere entre variation et maintien, la seconde sur les
structures et operations de determination. Elles sont complementaires, mais
la seconde n'absorbe pas la premiere et la question de portee reste interne.

```text
PROBLEME_CONTROLE = FUSION_DES_QUESTIONS_EN_UNE_THESE_UNIQUE
DISCRIMINATION = SEPARATION_FRONTIERE / DETERMINATION_ET_ENQUETE
REDONDANCE = AUCUNE, FONCTIONS_COMPLEMENTAIRES
DECISION = CONSERVEE_COMME_DOUBLE_ENTREE_PUBLIQUE
PORTEE = QUESTIONS_DE_RECHERCHE, NON_VERDICTS
EFFET_SUR_UNE_MUTATION = NON_ETABLI
```

### Contre-audit methodologique

```text
SURPORTÉE_DES_REGLES = NON_REPRODUITE
REDONDANCE_TOTALE = NON_ETABLIE
FORMULAIRE_UNIVERSEL = REFUSE
HIERARCHIE_DES_DIMENSIONS = REFUSEE
AUTORISATION_DE_REECRITURE_CANONIQUE = NON
NOUVELLE_REGLE_DURABLE = AUCUNE
NOUVELLE_META_REGLE = AUCUNE
```

Les regles D1–D5 sont donc conservees comme controles proportionnes et
contextuels. Leur application ne produit pas une nouvelle couche normative.

---

## 2026-08-18 — Clôture de la phase 4 dans son périmètre

```text
D1_A_D5 = JUSTIFIES_ET_CONSERVES
OBJET_ACCES_CONSTITUTION = DECISION_DE_RANG_CONSERVEE
REGLES_TROP_FORTES = NON_IDENTIFIEES
REGLES_REDONDANTES = NON_IDENTIFIEES_COMME_TOTALES
REGLES_NON_JUSTIFIEES = AUCUNE_A_CE_PALIER
REGLES_NON_DECIDABLES = AUCUNE_A_CE_PALIER
NOUVELLE_REGLE_DURABLE = AUCUNE
NOUVELLE_META_REGLE = AUCUNE
PHASE_4 = QUALIFIEE_DANS_LE_PERIMETRE
PHASE_5 = NON_OUVERTE
MUTATION_CANONIQUE = AUCUNE
NOUVEAU_CALCUL = NON_LANCE
```

La phase 4 établit la justification locale des contrôles méthodologiques, sans
autoriser leur application uniforme à tous les documents ni leur propagation
comme grille autonome hors contexte. Les phases suivantes restent fermées.
