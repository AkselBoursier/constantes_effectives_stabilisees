# Test du découplage entre statut, état et autorisation

## Fonction et statut

Artefact interne du palier suivant de la reconception. Il teste une distinction
architecturale émergée du lot pilote, sans modifier les statuts existants ni
reconstruire les autorisations opérationnelles.

```text
PALIER = 5A / DECOUPLAGE_STATUT_ET_AUTORISATION
STATUT = TEST_A_QUALIFIER
SOURCES = INTACTES
ISSUES_ET_AUTORISATIONS = NON_MODIFIEES
MIGRATION = NON_OUVERTE
```

## Hypothèse

Trois questions différentes doivent être séparées :

```text
STATUT_DE_L_OBJET = QUE_PORTE_CETTE_PIECE_ET_DANS_QUEL_PERIMETRE ?
ETAT_DE_LA_LIGNE = OU_EN_EST_LE_TRAVAIL_CONCERNE ?
AUTORISATION_D_AGIR = QUELLE_ACTION_EST_PERMISE_MAINTENANT ?
```

Une synthèse peut être active sans autoriser un nouveau calcul. Une ligne peut
être suspendue alors qu'un résultat antérieur reste qualifié dans son périmètre.
Une archive peut être utile sans redevenir une autorité. Une décision
méthodologique peut être active sans décider de l'état de chaque chantier.

## Cas de contrôle

| Cas | Statut de l'objet | Etat de la ligne | Autorisation | Découplage requis |
|---|---|---|---|---|
| **L2 — synthèse neutrinos** | Synthèse scientifique active dans un périmètre borné | Reprise ou approfondissement local selon la ligne concernée | Aucune autorisation automatique de nouvel ajustement conjoint | Distinguer acquis porté et travail ouvert |
| **L3 — blocage ALPHA** | Blocage d'exécution caractérisé | Reprise suspendue jusqu'à condition d'accès | Reprise possible si la condition matérielle est satisfaite ; pas de nouveau calcul par défaut | Distinguer diagnostic, état et permission |
| **L4 — décision statuts** | Décision canonique active dans son périmètre | Cadre méthodologique vivant | Oriente la qualification ; n'autorise pas une opération scientifique déterminée | Distinguer rang normatif et permission locale |
| **L5 — archive antérieure** | Archive de provenance non autoritative | Aucun chantier actif par sa seule présence | Aucune réintégration automatique | Distinguer utilité historique et autorité |
| **L6 — plan éditorial** | Plan expérimental non promu | Rédaction soumise à validation | Aucune publication automatique | Distinguer essai, décision et promotion |

## Test de confusion

Le modèle échoue si l'une des inférences suivantes devient automatique :

```text
STATUT_ACTIF -> AUTORISATION_DE_CALCUL
ARCHIVE -> AUTORITE_CURRENT
BLOCAGE -> ECHEC_SCIENTIFIQUE
DECISION_METHODOLOGIQUE -> AUTORISATION_UNIVERSELLE
PLAN_EXPERIMENTAL -> PUBLICATION
ETAT_DE_LIGNE -> INVALIDATION_DE_TOUTES_LES_PIECES
```

Ces inférences sont refusées par les cas du lot. Le statut décrit ce que porte
l'objet ; l'état décrit une ligne, une reprise ou une condition temporelle ;
l'autorisation relève d'une décision locale explicite.

## Représentation abstraite

```text
OBJET
  -> STATUT_DANS_UN_PERIMETRE
  -> PORTEE_ET_LIMITES
  -> PROVENANCE

LIGNE_DE_TRAVAIL
  -> ETAT
  -> QUESTION_ACTIVE
  -> DETTES_ET_CONDITIONS

DECISION_LOCALE
  -> AUTORISATION_D_ACTION
  -> PERIMETRE
  -> CONDITION_D_EXPIRATION_OU_DE_REOUVERTURE
```

Les trois plans peuvent être reliés, mais aucun n'est déduit automatiquement
d'un autre. Une autorisation doit pointer vers la ligne, l'action, le périmètre
et la condition qui la rendent recevable.

## Résultat local

Le découplage décrit correctement les cinq cas sans ajouter une catégorie
scientifique aux objets et sans rendre les archives ou les synthèses inertes.
Il réduit aussi le risque de transformer une vue de distribution en tableau de
permissions.

Une limite demeure : certaines décisions sont portées conjointement par une
pièce, une issue et une relation de travail. Le modèle devra donc permettre de
qualifier l'autorité comme une relation ou une décision locale, plutôt que de
l'inscrire comme propriété permanente du document.

```text
DECOUPLAGE = COHERENT_SUR_LE_LOT
STATUT = PROPRIETE_BORNEE_DE_L_OBJET
ETAT = PROPRIETE_DE_LA_LIGNE_OU_DE_LA_REPRISE
AUTORISATION = DECISION_LOCALE_EXPLICITE
AUTORISATION_DERIVEE_AUTOMATIQUE = REFUSEE
ARCHIVE_REACTIVEE_AUTOMATIQUEMENT = REFUSEE
MIGRATION = NON_OUVERTE
PROCHAINE_ETAPE = TESTER_LE_MAPPAGE_DES_RELATIONS_ET_DES_IDENTITES
```
