# Test de la combinaison architecturale hybride

## Fonction et statut

Artefact interne du palier 4, seconde partie, de la reconception de
l'environnement de travail. Il teste une combinaison conceptuelle sur le lot
pilote, sans la convertir en dossiers, fichiers cibles ou registre central.

```text
PALIER = 4B / TEST_DE_COMBINAISON_ARCHITECTURALE
SOCLE = OBJETS_AUTONOMES + RELATIONS_EXPLICITES
VUES = PLANS_FONCTIONNELS
CONTEXTES = DOMAINES_DE_RECHERCHE
STATUTS = AXE_INDEPENDANT
STATUT = PROTOTYPE_CONCEPTUEL_A_QUALIFIER
MIGRATION = NON_OUVERTE
```

## Hypothese testee

La combinaison peut conserver simultanément :

- la stabilité des objets lorsque les chemins changent ;
- la lisibilité des plans pour les lecteurs et workflows ;
- la continuité des domaines pour les travaux de recherche ;
- l'indépendance des statuts et de la provenance ;
- l'ouverture aux contenus transversaux ou émergents.

Elle échoue si les plans deviennent des conteneurs canoniques, si les domaines
absorbent les fonctions communes, ou si les relations exigent un registre
central plus lourd que le gain de contrôle obtenu.

## Architecture abstraite proposée

```text
OBJET_DE_TRAVAIL
  + IDENTITE_STABLE
  + CONTENU_CANONIQUE
  + PORTEE_ET_LIMITES
  + STATUT_LOCAL
  + PROVENANCE
  + RELATIONS

DOMAINE_DE_RECHERCHE
  = CONTEXTE_DE_QUESTION_ET_DE_TRAVAIL

PLAN_FONCTIONNEL
  = VUE_SELECTIONNEE_POUR_UN_PUBLIC_OU_UN_WORKFLOW

RELATION
  = DEPENDANCE_SEMANTIQUE, PREUVE, PROVENANCE, COMPLEMENT, ROUTE OU VOISINAGE
```

Aucun de ces éléments ne doit être déduit automatiquement d'un chemin. Les
plans et domaines peuvent évoluer sans imposer une copie de l'objet.

## Application aux six objets du lot

| Objet | Objet autonome | Domaine ou question | Plan ou vue utile | Statut indépendant |
|---|---|---|---|---|
| **L1** | Accueil du projet, questions et limites | Projet transversal | Vue publique | Courant, révisable |
| **L2** | Synthèse des accès neutrino | Cycle neutrinos / reconstruction du secteur | Vue de recherche et synthèse publique sélective | Actif dans un périmètre borné |
| **L3** | Blocage d'accès au paquet de reproduction | Reproduction lattice / reprise computationnelle | Vue de recherche, route de preuve | Blocage d'exécution caractérisé |
| **L4** | Décision objet / accès / constitution | Méthodologie transversale | Vue méthodologique et route de qualification | Active dans son périmètre |
| **L5** | Mode d'emploi de l'archive antérieure | Généalogie du projet | Vue de provenance | Archive non autoritative |
| **L6** | Plan de livrable théorique | Écriture et qualification de la constance | Vue de laboratoire éditorial | Expérimental, non promu |

Le même objet peut être présent dans plusieurs vues, mais chaque apparition
reste une projection et renvoie à l'objet autonome. La présence dans une vue ne
modifie pas le statut de l'objet.

## Contrôle de hiérarchie cachée

La combinaison est recevable seulement si les tests suivants restent vrais :

```text
PLAN_FONCTIONNEL != CONTENEUR_CANONIQUE
DOMAINE != STATUT_GLOBAL_DE_TOUTES_SES_PIECES
VUE != COPIE_INDEPENDANTE
CHEMIN != IDENTITE
REGISTRE_CENTRAL != PREALABLE_OBLIGATOIRE
```

### Résultat du contrôle

- Le plan public peut sélectionner L1, une partie de L2 et des routes vers L4
  sans devenir la source de L2 ou L4.
- Le domaine neutrino peut organiser L2 et ses pièces directrices sans absorber
  les règles méthodologiques transversales de L4.
- Le domaine computationnel peut exposer L3 comme blocage sans le transformer en
  état scientifique global.
- La vue de provenance peut relier L5 aux objets concernés sans rendre l'archive
  autoritative.
- La vue de laboratoire peut exposer L6 sans le faire entrer dans le flux
  public.

Le contrôle ne révèle pas de hiérarchie cachée nécessaire sur ce lot, mais il
identifie deux conditions : les relations doivent être qualifiées, et les vues
doivent rester légères.

## Test de non-duplication

Pour chaque objet, comparer la présence dans les vues avec le contenu de
l'objet autonome :

| Objet | Vues possibles | Risque de duplication | Garde-fou |
|---|---|---|---|
| L1 | Public, recherche | Reformulation qui devient une nouvelle autorité | Un seul objet d'accueil, vues limitées |
| L2 | Recherche, public, provenance | Synthèse publique concurrente du résultat actif | Renvoi à la synthèse porteuse et portée conservée |
| L3 | Recherche, preuve, provenance | Blocage recopié comme résultat négatif | Type de blocage et condition de reprise explicites |
| L4 | Méthode, recherche, provenance | Contrat répété dans chaque domaine | Relation vers la décision et application locale |
| L5 | Provenance, public optionnel | Histoire imposée au nouveau lecteur | Route facultative et statut d'archive visible |
| L6 | Laboratoire, provenance | Plan traité comme essai promu | Statut expérimental et validation séparée |

## Test de migration conceptuelle

Sans déplacer les sources, simuler deux changements de distribution :

1. remplacer une vue publique courte par une vue publique plus développée ;
2. remplacer un classement par domaine par un classement par question.

Le contenu des six objets ne change pas. Seules les sélections, l'ordre, le
contexte et les relations de route changent. Les relations sémantiques et
probatoires doivent rester identiques ; les routes peuvent être remplacées.

```text
MIGRATION_CONCEPTUELLE = RECOMPOSITION_DES_VUES
OBJETS_SOURCES = INCHANGES
RELATIONS_SEMANTIQUES = CONSERVEES
ROUTES_DISTRIBUTIVES = REMPLACABLES
```

Cette simulation est possible sur le lot. Elle ne démontre pas encore que toute
l'arborescence du dépôt peut être migrée ainsi.

## Limites et points à instruire

- Certains objets comme L4 ont un caractère transversal qui ne se laisse pas
  réduire à un domaine unique.
- L2 nécessiterait probablement des relations plus détaillées avec ses pièces
  de preuve avant toute automatisation.
- Les statuts actuels sont parfois portés par des documents, des issues et des
  décisions conjointement ; il faudra distinguer état de l'objet, état de la
  ligne de travail et autorisation.
- Les vues légères ne suffiront pas à elles seules pour les gros dossiers de
  provenance ou de computation.
- Un registre relationnel pourra devenir utile, mais seulement après avoir
  mesuré le coût réel de la maintenance manuelle.

## Verdict local

```text
COMBINAISON_HYBRIDE = COHERENTE_SUR_LE_LOT
OBJETS_AUTONOMES = SOCLE_RETENU_PROVISOIREMENT
PLANS = VUES_NON_CANONIQUES
DOMAINES = CONTEXTES_NON_STATUTS
STATUTS = A_DECOUPLER_PAR_OBJET_LIGNE_ET_AUTORISATION
MIGRATION_CONCEPTUELLE = POSSIBLE_SUR_LE_LOT
MIGRATION_REELLE = NON_OUVERTE
REGISTRE_CENTRAL = NON_JUSTIFIE_A_CE_PALIER
PROCHAINE_ETAPE = TESTER_LE_DECOUPLAGE_DES_STATUTS_ET_DES_AUTORISATIONS
```

La combinaison est suffisamment cohérente pour poursuivre. Elle reste une
proposition de laboratoire : sa généralisation exige un autre lot et un test
spécifique des statuts, autorisations et relations computationnelles.
