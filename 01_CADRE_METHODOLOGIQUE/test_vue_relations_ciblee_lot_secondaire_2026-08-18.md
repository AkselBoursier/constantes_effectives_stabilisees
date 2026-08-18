# Test d'une vue de relations ciblée

## Fonction et statut

Artefact interne du palier 10 de la reconception. Cette vue est un prototype de
lecture pour une question précise ; elle ne constitue ni un registre central ni
une nouvelle source canonique.

```text
PALIER = 10 / VUE_DE_RELATIONS_CIBLEE
LOT = RELATIONS_SENSIBLES_DU_LOT_SECONDAIRE
STATUT = PROTOTYPE_DE_VUE_A_QUALIFIER
REGISTRE_CENTRAL = NON
CONTENU_CANONIQUE = PORTE_PAR_LES_OBJETS_SOURCES
MIGRATION = NON_OUVERTE
```

## Question servie

Comment les objets transversaux T1 à T5 se relient-ils lorsque la relation
elle-même doit être examinée, sans transformer cette vue en carte générale du
dépôt ?

La vue ne cherche pas à résumer les objets. Elle sélectionne uniquement les
relations qui justifient une lecture conjointe ou un contrôle de non-confusion.

## Relations sélectionnées

| Relation | Type | Pourquoi la montrer | Ce que la vue ne conclut pas |
|---|---|---|---|
| T1 ↔ T2 | Articulation philosophie / méthode | Vérifier le passage entre exploration philosophique et cadre normatif | Compatibilité ne signifie pas dérivation ni fondement |
| T2 ↔ T3 | Articulation méthode / architecture | Examiner comment une règle borne une carte architecturale | La carte ne devient pas une preuve scientifique |
| T3 ↔ T5 | Jonction architecture / état daté | Distinguer relation architecturale et généalogie de raccordement | L'état daté ne devient pas une route vivante |
| T4 ↔ T1/T2 | Articulation essai / registres | Contrôler le statut d'un essai traversant plusieurs registres | La richesse de l'essai ne vaut ni promotion ni validation |
| T5 -> chantiers | Provenance / jonction | Retrouver les relations historiques utiles à une réauditabilité | La carte ne remplace pas les portes actives |

## Forme de la vue

Chaque relation est présentée avec un contrat court :

```text
SOURCE
CIBLE_OU_ENSEMBLE
TYPE_DE_RELATION
QUESTION_SERVIE
PORTEE
CONDITION_DE_VALIDITE
STATUT_DE_LA_RELATION
PROVENANCE
CE_QUE_LA_RELATION_N_ETABLIT_PAS
ROUTE_VERS_LES_OBJETS
```

La vue ne contient pas le texte complet de T1 à T5. Elle renvoie vers les objets
sources et conserve seulement les éléments nécessaires pour comprendre
pourquoi la relation est montrée et ce qu'elle ne permet pas d'inférer.

## Contrôle de non-surpromotion

La vue doit refuser les raccourcis suivants :

```text
RELATION_VISIBLE -> RELATION_IMPORTANTE_UNIVERSELLEMENT
ARTICULATION -> DERIVATION
JONCTION_HISTORIQUE -> CONTINUITE_ACTUELLE
COMPATIBILITE -> FONDEMENT
PROXIMITE -> DEPENDANCE
VUE_CIBLEE -> REGISTRE_GENERAL
```

La présence d'une relation dans cette vue signifie seulement qu'elle est
pertinente pour la question locale du test.

## Contrôle de non-duplication

La vue est recevable si :

- elle ne recopie pas les contenus uniques des objets ;
- elle conserve le type et la portée de chaque relation ;
- elle renvoie vers la provenance de la relation ;
- elle indique les limites d'inférence ;
- elle peut être supprimée ou reconstruite sans perte des objets sources ;
- son maintien reste proportionné à la question servie.

```text
VUE = PROJECTION_RELATIONNELLE
VUE != DOCUMENT_CANONIQUE
VUE != REGISTRE_EXHAUSTIF
VUE != NOUVELLE_AUTORITE
```

## Résultat du test

La vue ciblée rend lisibles les articulations sensibles sans exiger de registre
central. Elle apporte un gain pour les questions de passage entre philosophie,
méthode, architecture, éditorial et provenance.

Le gain disparaît si la vue tente de couvrir toutes les relations du dépôt ou si
elle recopie les objets qu'elle relie. La forme utile est donc locale, motivée
par une question et reconstruisible.

Les relations T1 ↔ T2 et T4 ↔ T1/T2 demandent une vigilance particulière :
elles traversent plusieurs registres et risquent d'être lues comme des
fondements. Les relations T3 ↔ T5 demandent de maintenir la distinction entre
architecture abstraite et état historique.

## Verdict local

```text
VUE_DE_RELATIONS_CIBLEE = UTILE_SUR_LE_LOT
REGISTRE_CENTRAL = NON_REQUIS
CONTENU_CANONIQUE = NON_DUPLIQUE
RELATIONS_TRANSVERSALES = RENDUES_LISIBLES_SOUS_QUESTION
VUE_EXHAUSTIVE = NON_RECOMMANDEE
RECONSTRUIBILITE = OUI
MIGRATION = NON_OUVERTE
PROCHAINE_ETAPE = EVALUER_LE_MODELE_SUR_UN_LOT_COMPUTATIONNEL_OU_PROBATOIRE
```

Le test justifie des vues relationnelles locales et temporaires, non une couche
relationnelle générale imposée à tout le dépôt.
