# Contrat minimal d'un objet migrable

## Fonction et statut

Artefact interne du palier 6 de la reconception. Il définit le minimum à
préserver pour qu'un objet puisse changer de destination sans perte de sens,
de statut ou de provenance.

```text
PALIER = 6 / CONTRAT_MINIMAL_OBJET_MIGRABLE
STATUT = SPECIFICATION_A_TESTER
FORMAT_TECHNIQUE = NON_IMPOSE
MIGRATION = NON_OUVERTE
DECISION_HUMAINE = REQUISE_AVANT_TOUT_DEPLACEMENT
```

Migrable ne signifie pas qu'un objet doit être déplacé. Cela signifie seulement
que sa conservation peut être contrôlée si une migration est un jour décidée.

## Contrat minimal

```text
IDENTITE_DE_TRAVAIL
FONCTION_DOMINANTE
REGISTRES_CONCERNES
QUESTION_OU_USAGE
CONTENU_UNIQUE
PORTEE_ET_LIMITES
STATUT_DE_L_OBJET
ETAT_DE_LA_LIGNE_SI_APPLICABLE
AUTORISATION_ASSOCIEE_SI_APPLICABLE
DEPENDANCES_SEMANTIQUES
DEPENDANCES_PROBATOIRES
RELATIONS_DE_PROVENANCE
RELATIONS_DE_COMPLEMENT_OU_DE_ROUTE
CONDITIONS_DE_REOUVERTURE
SOURCE_ET_VERSION_OBSERVEES
DESTINATION_ACTUELLE
CORRESPONDANCES_CANDIDATES
CRITERES_DE_PERTE
```

La `DESTINATION_ACTUELLE` est conservée pour la traçabilité, mais elle ne
définit pas l'identité de l'objet. Les `CORRESPONDANCES_CANDIDATES` peuvent
rester vides tant qu'aucune architecture cible n'est décidée.

## Ce qui doit rester invariant

Une migration conceptuelle est recevable seulement si les invariants suivants
sont contrôlés :

- l'identité de travail reste retrouvable ;
- le contenu unique est présent ou sa transformation est explicitement
  qualifiée ;
- la fonction et le public ne sont pas attribués à tort ;
- le statut et sa portée restent bornés ;
- l'état d'une ligne de travail n'est pas transformé en propriété permanente de
  l'objet ;
- aucune autorisation n'est déduite du déplacement ;
- les dépendances qui changent le sens ou le verdict sont conservées ;
- la provenance et les versions observées restent récupérables ;
- les contradictions, refus, limites et conditions de reprise restent visibles ;
- une décision humaine identifie la destination et le périmètre de migration.

```text
MIGRATION_SANS_PERTE = INVARIANTS_CONTROLES
MIGRATION_SANS_PERTE != COPIE_TEXTUELLE_IDENTIQUE
MIGRATION_SANS_PERTE != LIENS_REPARES_SEULS
```

Une adaptation de forme ou de longueur est donc possible, mais elle doit être
séparée de la conservation du contenu et de la qualification du statut.

## Critères de refus

Le contrat refuse une migration ou la suspend si :

```text
IDENTITE_NON_RETRACABLE
CONTENU_UNIQUE_NON_INVENTORIE
PORTEE_OU_STATUT_AMBIGUS
DEPENDANCE_SEMANTIQUE_NON_QUALIFIEE
PROVENANCE_NON_RECUPERABLE
CONTRADICTION_EFFACEE_PAR_LA_RECOMPOSITION
AUTORISATION_INFERREE_DU_CHEMIN
DECISION_HUMAINE_ABSENTE
```

Un échec du contrat n'autorise pas une simplification. Il peut conduire à une
triangulation locale, à un statut non migrable provisoire ou à la conservation
de l'objet dans sa forme actuelle.

## Application aux objets L1 à L6

| Objet | Contrat minimal suffisant sur le lot | Point encore incomplet |
|---|---|---|
| **L1** | Identité, fonction d'accueil, questions, limites et routes principales | Séparer à terme la vue publique de l'état mouvant sans dupliquer les routes |
| **L2** | Synthèse, périmètre scientifique, acquis, limites, pièces directrices et statut actif borné | Granularité des dépendances probatoires N0-N5 |
| **L3** | Blocage caractérisé, diagnostic environnemental, tentatives et condition de reprise | Relation formelle entre accès matériel, ligne de reprise et autorisation future |
| **L4** | Décision, rang, portée, règle objet / accès / constitution et provenance | Décrire ses applications locales sans la recopier |
| **L5** | Archive, fonction de provenance, statut non autoritatif et mode de reprise | Cartographie détaillée des relations vers les objets historiques |
| **L6** | Plan, fonction expérimentale, conditions de validation et statut non promu | Distinguer les sources intégrées au plan des sources seulement citées |

Le contrat est donc applicable au lot, mais certains champs restent à
instruire plus finement avant toute automatisation ou migration.

## Test de changement de destination

Pour chaque objet, simuler une destination différente sans la créer :

```text
SOURCE_ACTUELLE -> DESTINATION_ABSTRAITE_A
SOURCE_ACTUELLE -> DESTINATION_ABSTRAITE_B
```

Comparer uniquement le contrat, pas les liens actuels. Le changement est
recevable si les invariants restent vérifiables et si les pertes éventuelles
sont nommées. Une destination abstraite n'est pas une proposition de chemin.

## Verdict local

```text
CONTRAT_MINIMAL = APPLICABLE_AU_LOT
IDENTITE_ET_CONTENU = CONTROLEABLES
STATUT_ET_AUTORISATION = SEPARES
RELATIONS = A_QUALIFIER_PAR_TYPE
MIGRATION_CONCEPTUELLE = TESTABLE
MIGRATION_REELLE = NON_OUVERTE
PROCHAINE_ETAPE = SIMULER_DEUX_DESTINATIONS_ABSTRAITES
```

Le contrat fournit un garde-fou suffisant pour passer à une simulation de
migration conceptuelle. Il ne crée aucune obligation de migration et ne fixe
aucune architecture définitive.
