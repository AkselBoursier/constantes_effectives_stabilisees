# Test des identités et des relations du lot pilote

## Fonction et statut

Artefact interne du palier 5B de la reconception. Il teste si les objets du lot
pilote restent identifiables lorsque leur vue, leur domaine de lecture ou leur
chemin de distribution change.

```text
PALIER = 5B / IDENTITES_ET_RELATIONS
STATUT = TEST_A_QUALIFIER
SOURCES = INTACTES
CHEMINS = IDENTIFIANTS_D_OBSERVATION_SEULEMENT
MIGRATION = NON_OUVERTE
```

## Hypothese testee

Une architecture stable doit conserver l'identité de travail d'un objet et la
nature de ses relations indépendamment de la vue qui le distribue. Une relation
ne doit pas être reconstruite à partir d'un lien Markdown ou d'une proximité de
dossier.

```text
IDENTITE = CONTENU + PORTEE + STATUT + PROVENANCE_MINIMALE
RELATION = TYPE + SOURCE + CIBLE + PORTEE + CONDITION
CHEMIN = ADRESSE_ACTUELLE, NON_IDENTITE
```

## Identités abstraites du lot

| Objet | Identité de travail | Ce qui ne suffit pas à l'identifier |
|---|---|---|
| **L1** | Accueil du projet : objet, questions, distinction minimale, routes humaines | Le seul nom `README.md` ou sa position à la racine |
| **L2** | Synthèse scientifique active des accès neutrino après N5, dans son périmètre | Le seul nom du cycle ou la version du fichier |
| **L3** | Rapport de blocage d'accès au paquet de reproduction lattice ALPHA, diagnostic environnemental borné | Le mot « blocage » ou le dossier QCD seul |
| **L4** | Décision de rang sur objet, accès et constitution, active dans son périmètre | Le numéro de version ou le seul emplacement méthodologique |
| **L5** | Route de provenance des travaux antérieurs, archive non autoritative | Le numéro `91` ou la date des pièces |
| **L6** | Plan expérimental d'un livrable théorique, soumis à validation éditoriale | Le mot « plan » ou son emplacement dans le laboratoire |

Chaque identité comporte un contenu unique, une fonction dominante, une portée
et un statut. Elle peut survivre à une nouvelle destination ou à une nouvelle
vue.

## Relations abstraites

| Source | Type | Cible | Portée / condition |
|---|---|---|---|
| L1 | Route de lecture | L2 | Oriente vers la reprise scientifique ; n'établit pas le verdict de L2. |
| L1 | Route de qualification | L4 | Signale une méthode applicable ; ne transforme pas L1 en document normatif. |
| L2 | Dépendance probatoire | N0-N5 et pièces locales | Les voies et limites fondent la synthèse ; la dépendance doit rester bornée au cycle. |
| L2 | Relation de provenance | Synthèse de récupération précédente | L'état antérieur est conservé comme source historique, sans autorité courante automatique. |
| L3 | Dépendance de reprise | Paquet externe, accès réseau ou support local | La reprise dépend d'une condition matérielle ; le blocage ne devient pas un verdict scientifique. |
| L4 | Relation normative | Documents qui appliquent la distinction objet / accès / constitution | La portée est celle de la décision, pas une autorisation universelle. |
| L5 | Provenance | Travaux, décisions et archives antérieurs | Permet la comparaison et la reprise instruite ; n'établit pas la validité actuelle. |
| L6 | Provenance / source éditoriale | Lectures pivots et décisions de rédaction | Le plan organise un essai ; il ne valide pas les sources ni le texte final. |
| L2 ↔ L4 | Articulation méthodologique | Qualification des accès et des limites | L4 encadre la lecture ; L2 porte le résultat scientifique de son cycle. |
| L3 ↔ L4 | Articulation technique / méthodologique | Séparation calcul, diagnostic, qualification et résultat | L4 fournit une règle de lecture ; L3 reste un cas local. |
| L5 ↔ L6 | Relation généalogique / expérimentale | Reprise éventuelle de formes ou matériaux | Aucune continuité automatique ; comparaison et validation nécessaires. |

## Test de changement de vue

Simuler trois changements sans modifier les objets :

1. L2 passe de la vue de recherche à une vue publique sélective ;
2. L3 passe d'une route de preuve à une vue de reprise computationnelle ;
3. L5 passe d'une route généalogique détaillée à une route historique optionnelle.

Pour chaque changement, vérifier :

- l'identité de l'objet reste la même ;
- le statut et la portée restent inchangés ;
- les relations sémantiques et probatoires sont conservées ;
- seules la sélection, l'ordre, le contexte et les routes distributives changent ;
- aucune vue ne devient une nouvelle autorité par sa visibilité.

```text
CHANGEMENT_DE_VUE = NE_CHANGE_PAS_L_IDENTITE
CHANGEMENT_DE_DOMAINE_DE_LECTURE = NE_CHANGE_PAS_LE_VERDICT
ROUTE_DISTRIBUTIVE = REMPLACABLE
DEPENDANCE_SEMANTIQUE = A_CONSERVER_EXPLICITEMENT
```

## Test de réattribution

Le modèle doit refuser les réattributions automatiques suivantes :

```text
MEME_CHEMIN -> MEME_OBJET
MEME_DOSSIER -> MEME_STATUT
MEME_PUBLICATION_DANS_UNE_VUE -> MEME_AUTORITE
MEME_PROVENANCE -> MEME_VALIDITE
MEME_RELATION_DE_VOISINAGE -> DEPENDANCE_SEMANTIQUE
```

À l'inverse, un changement de nom ou de chemin ne doit pas faire perdre une
identité si le contenu, la portée, la provenance et les relations sont
retracés.

## Résultats du test

### Résultats positifs

- Les six identités peuvent être décrites sans dépendre de leur chemin actuel.
- Les relations de route, de preuve, de provenance, de reprise et de norme sont
  discriminables.
- Le changement de vue ne modifie pas l'identité ni le statut dans les trois
  simulations.
- Le modèle évite de faire d'une archive, d'une route ou d'un dossier une
  autorité par simple position.

### Tensions restantes

- L2 possède un réseau de pièces directrices dont la granularité devra être
  testée avant une représentation plus formelle.
- L4 est une décision à la fois normative, méthodologique et historiquement
  située ; son identité doit conserver ces dimensions sans créer de copies.
- Les relations L3 ↔ L4 ne doivent pas laisser croire qu'une règle de lecture
  remplace l'accès matériel manquant.
- Les relations généalogiques de L5 ↔ L6 peuvent être riches sans justifier une
  continuité éditoriale ou scientifique.

Ces tensions ne falsifient pas le modèle, mais elles empêchent encore toute
formalisation automatique ou migration générale.

## Verdict local

```text
IDENTITES_SANS_CHEMIN = POSSIBLES_SUR_LE_LOT
RELATIONS_TYPÉES = NECESSAIRES
CHANGEMENT_DE_VUE = COMPATIBLE_AVEC_LA_STABILITE_DES_OBJETS
REATTRIBUTION_PAR_CHEMIN = REFUSEE
AUTOMATISATION_DES_RELATIONS = PREMATUREE
MIGRATION = NON_OUVERTE
PROCHAINE_ETAPE = DEFINIR_LE_CONTRAT_MINIMAL_D_UN_OBJET_MIGRABLE
```

Le test justifie la poursuite vers un contrat minimal d'objet migrable, sans
impliquer qu'une migration réelle soit souhaitable ou autorisée.
