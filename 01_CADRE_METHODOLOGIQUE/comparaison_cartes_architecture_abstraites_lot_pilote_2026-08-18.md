# Comparaison des cartes d'architecture abstraites

## Fonction et statut

Artefact interne du palier 4 de la reconception de l'environnement de travail.
Il compare des principes d'organisation sans créer de dossiers, déplacer des
pièces ou décider d'une migration.

```text
PALIER = 4 / COMPARAISON_DE_CARTES_ABSTRAITES
LOT = L1 A L6 DU MAPPAGE_PILOTE
STATUT = COMPARAISON_A_QUALIFIER
ARBORESCENCE_REELLE = NON_MODIFIEE
DESTINATIONS = NON_DEFINIES
MIGRATION = NON_OUVERTE
```

## Cartes comparées

### Carte A — plans fonctionnels

```text
PUBLIC
RECHERCHE
PREUVE
PROVENANCE
LABORATOIRE
```

Chaque plan regroupe sa fonction dominante, avec des relations explicites vers
les autres plans.

### Carte B — domaines avec fonctions internes

```text
DOMAINE_PHYSIQUE
DOMAINE_COMPUTATIONNEL
DOMAINE_METHODOLOGIQUE
DOMAINE_PHILOSOPHIQUE
DOMAINE_EDITORIAL
```

Chaque domaine contient, lorsque nécessaire, accueil, synthèse, preuve,
provenance et laboratoire local.

### Carte C — objets autonomes et vues tardives

```text
OBJETS_DE_TRAVAIL_STABLES
DOSSIERS_DE_QUESTION_OU_DOMAINE
VUES_PUBLIQUES_ET_DE_RECHERCHE
PROVENANCE_ET_RELATIONS
```

Les vues sont des projections composées à partir des objets ; elles peuvent
changer sans déplacer l'objet porteur du sens.

## Mappage du lot selon les cartes

| Objet | Carte A : plan dominant | Carte B : domaine dominant | Carte C : objet et vues |
|---|---|---|---|
| **L1 README racine** | Public | Editorial ou transversal | Objet d'accueil, projeté dans la vue publique |
| **L2 Synthèse neutrinos** | Recherche, avec preuves reliées | Physique | Objet de synthèse lié au domaine neutrino et aux pièces de preuve |
| **L3 Blocage ALPHA** | Preuve, avec reprise computationnelle | Computationnel | Objet de blocage et condition de reprise, projeté dans la vue de recherche |
| **L4 Décision statuts** | Preuve méthodologique ou contrat transversal | Méthodologique | Objet de décision avec portée et relations explicites |
| **L5 Travaux antérieurs** | Provenance | Editorial, philosophique ou transversal | Objet d'archive et route généalogique |
| **L6 Plan théorique** | Laboratoire | Editorial | Objet d'essai avec vue de laboratoire |

Le mappage montre déjà qu'aucune carte ne supprime la pluralité des fonctions.
La différence porte sur ce qui devient le principe dominant : plan, domaine ou
objet autonome.

## Comparaison des critères

| Critère | Carte A : plans | Carte B : domaines | Carte C : objets et vues |
|---|---|---|---|
| **Lisibilité publique** | Forte si le plan public reste court ; risque de routes vers plusieurs plans. | Variable ; un domaine peut mélanger accueil, preuve et provenance. | Forte si les vues sont bien composées ; risque de navigation plus abstraite. |
| **Continuité avec le dépôt actuel** | Moyenne ; les numéros et domaines devraient être remappés vers des fonctions. | Forte ; les cycles et volets restent les ancrages visibles. | Moyenne ; demande un nouveau vocabulaire d'identité et de relation. |
| **Stabilité lors d'un changement de chemin** | Moyenne à forte si les plans ne deviennent pas des copies. | Faible à moyenne si les chemins internes portent encore le statut. | Forte en principe, car l'objet est distinct de la vue. |
| **Risque de duplication** | Élevé pour les pièces transversales et les README de liaison. | Élevé si chaque domaine reproduit les mêmes fonctions. | Faible, mais les vues peuvent devenir des copies déguisées. |
| **Gestion des statuts** | Bonne si le statut est un axe séparé ; mauvaise s'il est encodé par plan. | Risque de statut global attribué à un domaine hétérogène. | Bonne si le statut est porté par l'objet ou la relation concernée. |
| **Gestion de la provenance** | Visible comme plan distinct, mais risque de l'isoler du contexte. | Dispersée dans chaque domaine ; coût de réassemblage élevé. | Reliée aux objets et disponible comme vue spécifique. |
| **Adaptation aux contenus émergents** | Bonne si un objet peut rester transversal ; faible si tout doit entrer dans un plan. | Moyenne ; les nouveaux contenus doivent être rattachés à un domaine. | Forte ; un objet peut rester non classé ou transversal. |
| **Coût de conception initial** | Moyen ; les plans sont intuitifs mais les limites doivent être fixées. | Faible au départ, élevé lors de la maintenance transversale. | Élevé ; il faut définir identités, relations et règles de vues. |
| **Coût de maintenance** | Moyen si les vues restent légères. | Élevé lorsque les fonctions sont répétées dans les domaines. | Potentiellement faible après stabilisation, mais dépend des relations. |
| **Compatibilité avec CI futur** | Bonne pour contrôler les plans une fois qualifiés. | Bonne localement, plus complexe transversalement. | Bonne pour contrôler objets, relations et vues, mais seulement après définition des contrats. |

## Analyse des pertes et duplications

### Carte A

**Pertes possibles :** le plan dominant peut masquer qu'une pièce relève de
plusieurs registres ou fonctions ; une décision méthodologique transversale
pourrait être réduite à une pièce de preuve parmi d'autres.

**Duplications possibles :** cartes publiques, index de recherche et routes de
provenance peuvent répéter les mêmes descriptions si leur statut de vue n'est
pas explicite.

**Correction nécessaire :** autoriser les objets transversaux et conserver les
relations sémantiques hors du simple classement par plan.

### Carte B

**Pertes possibles :** les fonctions partagées peuvent être subordonnées au
domaine ; la différence entre une preuve computationnelle et un résultat
scientifique peut devenir moins visible.

**Duplications possibles :** chaque domaine peut recréer son accueil, sa
provenance et ses contrats méthodologiques, avec des versions divergentes.

**Correction nécessaire :** limiter la répétition des fonctions communes et
maintenir une couche de relations transversales.

### Carte C

**Pertes possibles :** une relation importante peut être oubliée si elle n'est
pas enregistrée explicitement ; l'abstraction peut éloigner un lecteur qui ne
connaît pas le vocabulaire du modèle.

**Duplications possibles :** les vues peuvent recopier les objets au lieu de
les projeter, surtout si aucun contrôle de contenu canonique n'existe.

**Correction nécessaire :** distinguer route, complément, preuve, provenance et
dépendance sémantique, puis imposer un renvoi vers l'objet porteur.

## Test de résistance du modèle

| Cas | Carte qui résiste le mieux | Pourquoi | Réserve |
|---|---|---|---|
| Changement de chemin public | C | La vue peut être reconstruite sans déplacer l'objet. | Relations à expliciter. |
| Nouvelle pièce transversale | C, puis A | L'objet peut rester transversal ; A peut offrir un plan de rattachement. | B force plus facilement un domaine. |
| Résultat computationnel bloqué | A ou C | Le blocage peut rester une preuve locale ou un objet de reprise. | Ne pas le transformer en verdict scientifique. |
| Décision méthodologique générale | A | Le plan preuve / méthode la rend visible transversalement. | Peut isoler la décision de ses applications. |
| Nouveau lecteur | A avec une vue publique légère | Les plans peuvent être expliqués simplement. | C exige une composition de vue claire. |
| Reprise généalogique | C, puis A | La provenance peut suivre les objets. | B disperse la trajectoire. |
| Essai éditorial non promu | A ou C | Laboratoire explicite ou statut porté par l'objet. | Ne pas créer de copie publique. |

## Résultat comparatif

La Carte B est la plus continue avec l'organisation actuelle, mais elle risque de
reproduire la logique qui a créé la dispersion : les fonctions sont répétées et
les relations transversales sont difficiles à maintenir.

La Carte A clarifie fortement les fonctions et semble adaptée à des vues
publiques distinctes, mais elle ne suffit pas à elle seule pour les objets
transversaux et les identités stables.

La Carte C offre la meilleure stabilité conceptuelle pour les changements de
chemins, la conservation du contenu canonique et les pièces émergentes. Elle
coûte davantage au départ et ne doit pas être appliquée comme une abstraction
sans vues lisibles.

## Recommandation locale

Ne pas choisir une carte pure. Tester une combinaison prudente :

```text
OBJETS_AUTONOMES_ET_RELATIONS_EXPLICITES = SOCLE
PLANS_FONCTIONNELS = VUES_DE_DISTRIBUTION_ET_DE_TRAVAIL
DOMAINES = CONTEXTES_DE_RECHERCHE
STATUTS = AXE_INDEPENDANT
```

Cette combinaison conserve la stabilité de C, la lisibilité fonctionnelle de A
et la continuité des domaines de B, sans faire de ces trois dimensions une
hiérarchie unique.

## Verdict local du palier 4

```text
CARTE_A = UTILE_COMME_VUE_FONCTIONNELLE
CARTE_B = UTILE_COMME_CONTINUITE_DE_DOMAINE, RISQUE_DE_REPRODUCTION
CARTE_C = SOCLE_CONCEPTUEL_LE_PLUS_STABLE
COMBINAISON_A_B_C = A_TESTER
ARBORESCENCE_REELLE = NON_DEFINIE
MIGRATION = NON_OUVERTE
PROCHAINE_ETAPE = TESTER_UNE_COMBINAISON_SUR_UN_LOT_REDUIT
```

Ce résultat est une recommandation locale du laboratoire, non une décision
finale d'architecture.
