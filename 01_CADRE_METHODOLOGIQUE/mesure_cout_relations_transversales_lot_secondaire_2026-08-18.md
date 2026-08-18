# Mesure du coût des relations transversales

## Fonction et statut

Artefact interne du palier 9 de la reconception. Il mesure le coût conceptuel et
opérationnel des relations du lot secondaire avant toute décision de registre,
d'index ou de migration.

```text
PALIER = 9 / COUT_DES_RELATIONS_TRANSVERSALES
LOT = T1 A T5 DU LOT_SECONDAIRE
STATUT = MESURE_A_QUALIFIER
REGISTRE_CENTRAL = NON_CREE
MIGRATION = NON_OUVERTE
```

## Hypothèse testée

Les relations transversales peuvent rester gérables sans registre central si
elles sont peu nombreuses, typées, localement vérifiables et attachées aux
objets qui portent le sens. Un registre devient justifié seulement si son gain
de contrôle dépasse le coût d'une nouvelle couche de maintenance et ne crée
pas une autorité concurrente.

## Dimensions du coût

```text
COUT_RELATION = CREATION + QUALIFICATION + MAINTENANCE + VERIFICATION + RECUPERABILITE
```

- **Création** : identifier la relation et son type.
- **Qualification** : établir sa portée, sa condition et son rang.
- **Maintenance** : la garder juste lorsque l'objet ou l'état change.
- **Vérification** : contrôler qu'elle ne devient pas une dérivation ou une
  autorisation implicite.
- **Récupérabilité** : permettre un audit ultérieur sans dépendre d'une vue
  particulière.

Ces coûts sont évalués qualitativement pour ce palier ; aucun chiffre ne doit
être traité comme une mesure générale de maintenance.

## Relations du lot secondaire

| Relation | Type | Coût de qualification | Coût de maintenance | Risque principal |
|---|---|---:|---:|---|
| T1 -> situations philosophiques | Route de branche / exploration | Faible à moyen | Moyen | Promouvoir une exploration en théorie |
| T2 -> documents scientifiques | Relation normative / qualification | Élevé | Moyen | Transformer le cadre en autorisation universelle |
| T3 -> architectures de domaines | Synthèse / articulation | Moyen à élevé | Moyen | Fabriquer une unité absente |
| T4 -> sources et cas physiques | Relation argumentative / éditoriale | Élevé | Élevé | Confondre essai et résultat établi |
| T5 -> chantiers et états datés | Jonction historique | Moyen | Élevé si l'état évolue | Prendre une carte datée pour une route vivante |
| T1 <-> T2 | Articulation philosophie / méthode | Élevé | Moyen | Confondre compatibilité et dérivation |
| T2 <-> T3 | Articulation méthode / architecture | Moyen à élevé | Moyen | Faire d'une carte une preuve |
| T3 <-> T5 | Jonction architecture / historique | Moyen | Moyen à élevé | Reconstituer une continuité artificielle |
| T4 <-> T1/T2 | Articulation éditoriale / registres | Élevé | Élevé | Promouvoir selon la richesse du texte |

## Contrôle de suffisance sans registre central

Pour chaque relation, vérifier si les éléments suivants peuvent rester lisibles
sans base relationnelle distincte :

```text
TYPE
SOURCE
CIBLE_OU_ENSEMBLE
PORTEE
CONDITION
RANG
PROVENANCE_DE_LA_RELATION
DATE_OU_ETAT
CRITERE_DE_REOUVERTURE
```

### Résultat

Les relations du lot peuvent être décrites dans les objets sources, les
documents de provenance et les vues adaptées. Les relations à coût élevé ne
sont pas nombreuses, mais elles exigent une qualification humaine et ne sont
pas de bonnes candidates pour une génération automatique immédiate.

Le lot ne montre pas encore une explosion relationnelle. Il montre plutôt un
coût concentré sur quelques articulations sensibles : T2 <-> T3, T4 <-> T1/T2
et T5 vers les états datés.

## Comparaison de trois supports

| Support | Gain | Coût / risque | Résultat local |
|---|---|---|---|
| **Relation dans l'objet** | Proximité du sens et provenance locale | Risque de dispersion si les conventions ne sont pas stables | Suffisant pour les relations simples et bornées |
| **Vue de relation** | Lecture transversale sans modifier les objets | Risque de copie ou de tableau de bord concurrent | Utile pour une question ciblée ou un audit |
| **Registre central** | Recherche et contrôle global potentiellement plus rapides | Nouvelle autorité, maintenance, désynchronisation et rigidification | Non justifié par ce lot |

## Conditions d'ouverture d'un registre

Un registre relationnel ne devrait être envisagé que si un test ultérieur établit
au moins plusieurs des conditions suivantes :

- les mêmes relations doivent être recherchées dans de nombreux domaines ;
- leur absence ou leur divergence produit des erreurs récurrentes ;
- les objets et vues locales ne permettent plus une vérification suffisante ;
- le registre peut rester dérivé ou contrôlé sans devenir l'autorité du sens ;
- son schéma accepte les relations émergentes et non classables ;
- sa maintenance est moins coûteuse que la vérification distribuée.

Aucune de ces conditions n'est suffisamment établie sur le lot secondaire.

## Résultat local

```text
RELATIONS_TRANSVERSALES = GERABLES_SANS_REGISTRE_SUR_LE_LOT
COUT_ELEVE = CONCENTRE_SUR_QUELQUES_ARTICULATIONS
RELATIONS_DANS_LES_OBJETS = SUFFISANTES_POUR_LE_LOT
VUES_DE_RELATION = UTILES_SOUS_QUESTION_CIBLEE
REGISTRE_CENTRAL = NON_JUSTIFIE
AUTOMATISATION = PREMATUREE
MIGRATION = NON_OUVERTE
PROCHAINE_ETAPE = TESTER_UNE_VUE_DE_RELATIONS_CIBLEE
```

La mesure ne ferme pas la possibilité d'un registre futur. Elle exige seulement
que son ouverture soit motivée par un déficit de contrôle observé, et non par le
seul désir de rendre l'architecture plus complète.
