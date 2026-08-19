# Mappage abstrait du lot secondaire transversal

## Fonction et statut

Artefact interne du palier 8 de la reconception. Ce lot change de nature par
rapport au lot pilote : il porte surtout des objets philosophiques,
méthodologiques, architecturaux et éditoriaux, dont plusieurs sont
transversaux.

```text
PALIER = 8 / LOT_SECONDAIRE_TRANSVERSAL
STATUT = MAPPAGE_A_QUALIFIER
SOURCES = INTACTES
README_ARCHITECTURES_MANQUANT = FAIT_D_INVENTAIRE
MIGRATION = NON_OUVERTE
```

## Lot retenu

| Identifiant | Piece observée | Fonction dominante apparente |
|---|---|---|
| **T1** | `06_PHILOSOPHIE/README.md` | Porte de branche, charte, exploration et routage philosophique |
| **T2** | `01_CADRE_METHODOLOGIQUE/refondation-du-domaine.md` | Noyau canonique méthodologique et cadre transversal |
| **T3** | `04_ARCHITECTURES/Cercle2_lot2E_Synthese_transverse_architectures_v0_1.md` | Synthèse ou carte de relations architecturales |
| **T4** | `93_LABORATOIRE_EDITORIAL_EXPERIMENTAL/ESSAI_tentative/relecture/Qualifier la constance - Essai sur le statut des constantes physiques.md` | Essai éditorial expérimental, porteur de contenu scientifique et philosophique non promu |
| **T5** | `05_CARTES_ET_SYNTHESES/Carte_frottements_chantiers_v0_1.md` | Carte de jonction transversale datée entre chantiers |

Le README absent de `04_ARCHITECTURES` n'est pas remplacé dans ce lot. Son
absence est conservée comme information sur la distribution actuelle.

## Mappage par axes

| Objet | Registres concernés | Fonction | Statut / rang | Transversalité |
|---|---|---|---|---|
| **T1** | Philosophique, éditorial, méthodologique | Porte de branche et charte d'exploration | Exploration philosophique active ; C1-C2 établis localement, C3 non établi | Forte : relie situations, catégories, accès et inférences |
| **T2** | Méthodologique, épistémique, physique, philosophique | Noyau canonique de qualification | Canonique actif dans son périmètre | Très forte : objet / accès / constitution s'applique à plusieurs domaines |
| **T3** | Architecturale, méthodologique, éditoriale, transversal | Synthèse ou carte de relations entre architectures | À qualifier selon son propre statut documentaire | Forte : relie plusieurs terrains sans être une synthèse scientifique de chacun |
| **T4** | Éditorial, philosophique, physique, épistémique, méthodologique | Essai et proposition structurée | Expérimental, non promu ; soumis à validation | Forte : traverse plusieurs cas physiques et une interprétation philosophique |
| **T5** | Transversal, méthodologique, historique, éditorial | Carte de jonction datée | État de jonction conservé ; non route active | Très forte : relie les chantiers mais ne doit pas les absorber |

## Résultat du test de classification

Le contrat minimal reste utilisable, mais la fonction dominante ne suffit pas à
décrire ces objets. T1, T2, T4 et T5 portent plusieurs fonctions ou registres
qui changent leur lecture.

```text
FONCTION_DOMINANTE = POINT_D_ENTREE, NON_REDUCTION
TRANSVERSALITE = PROPRIETE_A_CONSERVER
REGISTRE_ARCHITECTURAL = A_DECRIRE_SANS_LE_FERMER
NON_CLASSEMENT_SIMPLE = RECEVABLE
```

T2 ne doit pas être rangé seulement comme « méthodologique » : sa distinction
objet / accès / constitution organise aussi les conditions de lecture physique,
épistémique et computationnelle. T4 ne doit pas être promu comme synthèse
scientifique simplement parce qu'il contient des résultats et des argumentations.
T5 ne doit pas devenir un tableau de bord actuel simplement parce qu'il relie
les chantiers.

## Relations essentielles

| Source | Type de relation | Cible / portée | Risque en cas de réduction |
|---|---|---|---|
| T1 | Route de branche et proposition | Situations, cartes et travaux philosophiques | Transformer une branche exploratoire en doctrine |
| T2 | Relation normative et qualification | Documents scientifiques et méthodologiques applicables | Transformer le cadre en autorisation universelle |
| T3 | Relation de synthèse architecturale | Architectures de plusieurs domaines | Fabriquer une unité scientifique absente |
| T4 | Relation éditoriale et argumentative | Sources physiques, philosophiques et méthodologiques | Promouvoir un essai de laboratoire comme résultat établi |
| T5 | Relation de jonction datée | Chantiers et états de raccordement | Remplacer les portes vivantes par un état historique |
| T1 ↔ T2 | Articulation philosophie / méthode | Passage à qualifier, non dérivation automatique | Confondre compatibilité, influence et fondement |
| T2 ↔ T3 | Articulation méthode / architecture | La méthode borne la lecture des architectures | Faire de la carte une preuve |
| T3 ↔ T5 | Articulation architecture / jonction | T5 conserve un état de liaison daté | Lire une carte historique comme route courante |
| T4 ↔ T1/T2 | Articulation éditoriale / philosophie / méthode | Proposition expérimentale à contrôler | Confondre essai, branche et noyau canonique |

## Contrôle du contrat minimal

Le contrat est satisfaisant si :

- les registres multiples sont conservés sans copies artificielles ;
- la transversalité est une propriété ou une relation, pas un dossier fourre-tout ;
- les statuts distincts restent lisibles ;
- l'absence de README d'architecture reste un fait d'inventaire ;
- les relations d'articulation ne sont pas transformées en dérivations ;
- les cartes datées ne sont pas promues en routes vivantes ;
- les essais ne sont pas promus par leur richesse de contenu ;
- le cadre canonique conserve sa portée bornée.

```text
REGISTRES_MULTIPLES = CONSERVABLES
TRANSVERSALITE = NON_REDUITE
STATUTS = DISTINGUABLES
DERIVATION_AUTOMATIQUE = REFUSEE
PROMOTION_PAR_CONTENU = REFUSEE
```

## Résultats et tensions

### Ce que le contrat conserve correctement

- la pluralité des registres dans T1 et T4 ;
- le caractère normatif mais borné de T2 ;
- la fonction de liaison de T3 et T5 sans les transformer en synthèses
  universelles ;
- le statut expérimental de l'essai ;
- la différence entre état daté, route active et provenance.

### Ce qui résiste à une classification simple

- T2 est à la fois noyau méthodologique et interface entre plusieurs régimes de
  recherche ;
- T4 est un objet éditorial mais porte une architecture argumentative qui ne se
  réduit pas au style ;
- T5 relie des chantiers sans être lui-même un chantier ;
- T1 définit une branche et ses règles de promotion sans être une simple vue.

Ces résistances ne falsifient pas le contrat. Elles montrent qu'un objet peut
être transversal sans qu'il faille créer une nouvelle catégorie durable pour
chaque cas.

## Verdict local du palier 8

```text
CONTRAT_MINIMAL_SUR_LOT_SECONDAIRE = APPLICABLE_AVEC_PRECISIONS
TRANSVERSALITE = DIMENSION_REELLE_A_CONSERVER
FONCTION_DOMINANTE = INSUFFISANTE_SEULE
REGISTRES_MULTIPLES = NECESSAIRES
NON_CLASSEMENT = RECEVABLE
NOUVELLE_CATEGORIE_GENERALE = NON_JUSTIFIEE
MIGRATION = NON_OUVERTE
PROCHAINE_ETAPE = COMPARER_LE_COUT_DES_RELATIONS_TRANSVERSALES
```

Le lot secondaire confirme la richesse du protocole : le modèle accepte les
objets transversaux sans les forcer dans une liste plus longue. Il faudra
maintenant mesurer le coût de leurs relations avant d'envisager une structure
matérielle.
