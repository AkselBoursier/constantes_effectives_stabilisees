# Simulation de migration conceptuelle vers deux destinations

## Fonction et statut

Artefact interne du palier 7 de la reconception. Il simule deux destinations
abstraites à partir du contrat minimal, sans créer de chemins, dossiers ou
fichiers cibles.

```text
PALIER = 7 / SIMULATION_MIGRATION_CONCEPTUELLE
SOURCE = contrat_minimal_objet_migrable_lot_pilote_2026-08-18.md
DESTINATION_A = ORGANISATION_PAR_PLANS_FONCTIONNELS
DESTINATION_B = ORGANISATION_PAR_DOMAINES_ET_QUESTIONS
STATUT = SIMULATION_A_QUALIFIER
MIGRATION_REELLE = NON_OUVERTE
```

## Règle de la simulation

Les destinations sont des modèles de distribution, pas des propositions
matérielles. Pour chaque objet L1-L6, seuls le contexte de lecture, la
sélection, l'ordre et les relations de route changent. L'identité, le contenu
unique, le statut, la portée, les dépendances et la provenance doivent rester
retrouvables.

```text
DESTINATION_ABSTRAITE = MODELE_DE_VUE
OBJETS_CANONIQUES = INCHANGES
RELATIONS_SEMANTIQUES = INCHANGEES
ROUTES_DISTRIBUTIVES = RECOMPOSABLES
```

## Destination A — organisation par plans fonctionnels

```text
PUBLIC
RECHERCHE
PREUVE
PROVENANCE
LABORATOIRE
```

### Projection du lot

| Objet | Plan dominant | Relations à préserver |
|---|---|---|
| L1 accueil | Public | Routes vers recherche et méthode |
| L2 synthèse neutrinos | Recherche | Dépendances probatoires et provenance |
| L3 blocage ALPHA | Preuve | Condition de reprise computationnelle |
| L4 décision statuts | Preuve / méthode transversale | Portée normative et applications locales |
| L5 archive antérieure | Provenance | Antériorité sans autorité automatique |
| L6 plan théorique | Laboratoire | Conditions de validation et sources éditoriales |

### Risques propres à A

- L4 peut être réduit à un plan de preuve alors que sa fonction normative est
  transversale.
- L1 peut devenir un index des plans au lieu de rester une porte publique.
- Les relations de recherche et de preuve peuvent être confondues avec une
  hiérarchie de validation.

### Garde-fous

```text
PLAN != RANG
PREUVE != AUTORISATION
PUBLIC != SOURCE_CANONIQUE_DE_LA_RECHERCHE
```

## Destination B — organisation par domaines et questions

```text
PHYSIQUE
COMPUTATIONNEL
METHODOLOGIQUE
PHILOSOPHIQUE
EDITORIAL
QUESTIONS_TRANSVERSALES
```

### Projection du lot

| Objet | Domaine ou question dominante | Relations à préserver |
|---|---|---|
| L1 accueil | Projet transversal | Routes vers les domaines et les vues |
| L2 synthèse neutrinos | Physique / accès au secteur neutrino | Pièces probatoires, portée et provenance |
| L3 blocage ALPHA | Computationnel / reproduction | Condition matérielle de reprise et diagnostic borné |
| L4 décision statuts | Méthodologique / objet-accès-constitution | Portée normative et relations d'application |
| L5 archive antérieure | Question transversale / généalogie | Antériorité, transformations et vérification indépendante |
| L6 plan théorique | Editorial / qualification de la constance | Statut expérimental, sources et validation |

### Risques propres à B

- Les fonctions communes peuvent être reproduites dans chaque domaine.
- L4 peut être enfermé dans la méthodologie alors qu'il articule plusieurs
  registres.
- L5 et L6 peuvent être reliés par une continuité éditoriale supposée.

### Garde-fous

```text
DOMAINE != FONCTION_UNIQUE
DOMAINE != STATUT_GLOBAL
CONTINUITE_GENEALOGIQUE != VALIDITE
```

## Contrôle des invariants

| Invariant | Destination A | Destination B | Résultat |
|---|---|---|---|
| Identité de travail | Conservée si le plan reste une vue | Conservée si le domaine reste un contexte | Passe |
| Contenu unique | Conservé dans l'objet canonique | Conservé dans l'objet canonique | Passe |
| Fonction dominante | Visible, mais L4 demande une fonction transversale | Visible, mais L4 dépasse un seul domaine | Passe sous réserve |
| Statut de l'objet | Ne doit pas être déduit du plan | Ne doit pas être déduit du domaine | Passe sous garde-fou |
| Etat de la ligne | À maintenir hors du plan | À maintenir hors du domaine | Passe |
| Autorisation | Ne peut pas être déduite de preuve ou public | Ne peut pas être déduite de domaine ou question | Passe |
| Dépendances sémantiques | Relations explicites entre plans | Relations explicites entre domaines | Passe |
| Provenance | Plan distinct mais relié aux objets | Dispersée par domaine, relation à préserver | Passe sous coût plus élevé |
| Contradictions et limites | Visibles si les vues restent sélectives | Visibles si la transversalité n'est pas écrasée | Passe sous réserve |
| Migrabilité inverse | Retour possible au contrat abstrait | Retour possible au contrat abstrait | Passe |

## Comparaison des coûts

| Dimension | Destination A | Destination B |
|---|---|---|
| Lisibilité initiale | Bonne pour distinguer les fonctions | Bonne pour retrouver un domaine de travail |
| Risque de duplication | Routes et plans transversaux | Fonctions répétées dans les domaines |
| Traitement des pièces transversales | Demande des relations hors plans | Demande des domaines ou questions transversaux |
| Provenance | Visible mais potentiellement séparée du contexte | Contextuelle mais plus dispersée |
| Réversibilité conceptuelle | Bonne | Bonne |
| Coût de maintenance anticipé | Modéré | Plus élevé si chaque domaine recrée les mêmes fonctions |
| Dépendance à une arborescence | Faible si plans = vues | Moyenne si domaines deviennent des conteneurs |

## Résultat de la simulation

La simulation réussit sur les deux destinations abstraites : le contrat minimal
permet de conserver les invariants et de recomposer les routes. Elle ne permet
pas de désigner une destination matérielle meilleure dans l'ensemble.

La Destination A favorise la lisibilité fonctionnelle et la séparation public /
preuve / provenance. La Destination B favorise la continuité des travaux par
domaine et question. Les deux exigent un socle d'objets autonomes et de
relations explicites pour éviter que leur principe dominant ne devienne une
nouvelle hiérarchie fermée.

```text
SIMULATION_A = PASSE
SIMULATION_B = PASSE
INVARIANTS = CONSERVABLES_DANS_LES_DEUX_MODELES
DESTINATION_MATERIELLE = NON_CHOISIE
ARCHITECTURE_FINALE = NON_DECIDEE
MIGRATION_REELLE = NON_OUVERTE
```

## Conditions avant toute migration pilote

Avant de choisir un lot de migration réel, il faudra :

1. tester le contrat sur un lot qui n'est pas principalement documentaire ;
2. détailler les relations probatoires de L2 et computationnelles de L3 ;
3. vérifier les objets transversaux et non classables ;
4. comparer la maintenance manuelle des relations ;
5. obtenir une décision humaine sur la destination, le lot et le mode de retour.

La simulation justifie la poursuite de la conception, pas le déplacement des
sources.
