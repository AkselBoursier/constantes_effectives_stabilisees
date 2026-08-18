# Modele conceptuel de l'architecture semantique integrale

## Fonction et statut

Artefact interne du palier 1 de la reconception de l'environnement de travail.
Il décrit des objets, axes et relations avant de proposer une arborescence.

```text
CHANTIER = RECONCEPTION_DE_L_ENVIRONNEMENT_DU_TRAVAIL
PALIER = 1 / MODELE_CONCEPTUEL
STATUT = A_TESTER
SOURCES_EXISTANTES = INTACTES
NOUVELLE_ARBORESCENCE = NON_PROPOSEE
MIGRATION = NON_OUVERTE
```

Ce modèle ne recommence aucune investigation. Il cherche seulement à fournir
un vocabulaire assez précis pour comprendre ce qui doit être conservé lorsque
la forme du dépôt changera.

## Hypothese directrice

L'unité primaire ne doit pas être un dossier numéroté ni un chemin. Elle doit
être un **objet de travail identifiable**, dont le contenu, le statut, la
portée et la provenance peuvent être décrits indépendamment de sa destination.

Les dossiers de recherche, les cartes, les README et les index sont ensuite des
agrégations ou des vues de ces objets. Ils ne doivent pas absorber leur contenu
canonique par défaut.

```text
OBJET_DE_TRAVAIL = IDENTITE + CONTENU + PORTEE + STATUT + PROVENANCE
DOSSIER_DE_RECHERCHE = GROUPEMENT_PAR_QUESTION_OU_DOMAINE
VUE = PROJECTION_POUR_UN_PUBLIC_OU_UNE_TACHE
CHEMIN = SUPPORT_DE_DISTRIBUTION, NON_IDENTITE_DU_SENS
```

Cette hypothèse reste ouverte : certains contenus peuvent nécessiter plusieurs
objets liés, une pièce transversale ou un statut non classable.

## Objets conceptuels

| Objet | Fonction | Ne doit pas être confondu avec |
|---|---|---|
| **Objet de travail** | Porter une unité de sens, de preuve, de méthode, d'essai ou de provenance. | Un fichier particulier ou un emplacement. |
| **Dossier de recherche** | Réunir des objets autour d'une question, d'un domaine ou d'une ligne de travail. | Une autorité automatique sur les objets qu'il regroupe. |
| **Vue** | Organiser une lecture pour un public ou une tâche. | La source canonique du contenu distribué. |
| **Pièce de preuve** | Établir, contrôler ou borner un énoncé dans un périmètre. | Un résultat scientifique complet ou une autorisation. |
| **État** | Décrire une situation temporelle ou opérationnelle. | Une propriété permanente du contenu. |
| **Relation** | Décrire un lien de sens, de provenance, de complément ou de navigation. | Un simple lien Markdown. |
| **Workflow** | Décrire une transformation contrôlée du travail. | Une arborescence ou un statut. |

## Axes à séparer

Un objet de travail peut être décrit par plusieurs axes indépendants :

```text
IDENTITE
DOMAINE_OU_QUESTION
REGISTRES_SEMANTIQUES
FONCTION
STATUT
PORTEE
PUBLIC_OU_USAGE
PROVENANCE
RELATIONS
CONDITIONS_DE_REOUVERTURE
```

Aucun axe ne doit être reconstruit à partir d'un autre. En particulier :

- le domaine ne détermine pas la fonction ;
- la fonction ne détermine pas le statut ;
- le statut ne détermine pas la validité scientifique ;
- la vue ne détermine pas le rang ;
- la provenance ne détermine pas la vérité du contenu ;
- le chemin ne détermine aucune de ces propriétés à lui seul.

## Registres sémantiques

Les registres proposés sont des repères initiaux et non une liste fermée :

```text
PHYSIQUE
EPISTEMIQUE
COMPUTATIONNEL
METHODOLOGIQUE
PHILOSOPHIQUE
EDITORIAL
TRANSVERSAL_OU_NON_CLASSE = RECEVABLE
```

L'étiquette `TRANSVERSAL_OU_NON_CLASSE` n'est pas une catégorie de rangement
finale. Elle signale qu'une analyse supplémentaire est nécessaire ou qu'une
pièce résiste légitimement à la partition courante.

## Fonctions documentaires provisoires

```text
ACCUEIL
CARTE
SYNTHESE
PREUVE
PROTOCOLE
QUALIFICATION
CONTRAT_METHODOLOGIQUE
PROVENANCE
ARCHIVE
ESSAI
```

Cette liste ne prescrit pas un nombre de documents. Elle sert à demander :
quelle fonction dominante est nécessaire, quelles fonctions peuvent cohabiter
sans perte, et lesquelles doivent rester séparées pour conserver leur rang ou
leur public.

## Statuts et temporalités

Le statut doit être porté explicitement, avec sa portée :

```text
EXPLORATION
EN_COURS
SUSPENDU
QUALIFIE_DANS_LE_PERIMETRE
A_REOUVRIR_SUR_CONDITION
ARCHIVE
NON_CLASSABLE = STATUT_DE_DESCRIPTION, NON_VERDICT
```

Un statut peut concerner l'objet, son usage, son accès ou une relation ; il ne
faut pas le généraliser à toute la famille documentaire. Un objet qualifié dans
son périmètre ne devient pas automatiquement une autorisation de calcul, une
vérité universelle ou une preuve non bornée.

## Relations à distinguer

| Relation | Question de contrôle |
|---|---|
| **Dépendance sémantique** | La modification ou le retrait de la source change-t-il le sens, le verdict ou la portée ? |
| **Dépendance probatoire** | La pièce fournit-elle un soutien ou un contrôle nécessaire à l'énoncé ? |
| **Provenance** | La pièce permet-elle de retrouver l'origine, la transformation ou la décision ? |
| **Complément** | La pièce ajoute-t-elle un contenu distinct sans être nécessaire au sens principal ? |
| **Contradiction ou tension** | Les pièces doivent-elles rester en relation pour rendre visible un désaccord ou une limite ? |
| **Route de lecture** | Le lien aide-t-il à poursuivre sans établir le contenu de la cible ? |
| **Voisinage** | Les pièces sont-elles rapprochées pour faciliter une exploration, sans relation forte établie ? |

Un lien de navigation cassé est un défaut technique. Une dépendance sémantique
mal identifiée est un risque de perte de sens ; les deux problèmes ne doivent
pas être traités par le même contrôle.

## Nombre de documents : règle de décision

Le modèle ne vise ni le document unique ni la multiplication des pièces. Le
nombre doit découler des fonctions et des relations :

```text
UN_DOCUMENT = SI_UNE_FONCTION_DOMINANTE_ET_UN_PUBLIC_SONT_COMPATIBLES
PLUSIEURS_DOCUMENTS = SI_RANGS, PUBLICS, STATUTS, TEMPORALITES_OU_CONTROLES_DIVERGENT
DOCUMENT_TRANSVERSAL = SI_LA_SEPARATION_PROVOQUE_UNE_PERTE_DE_SENS
VUE_DERIVEE = SI_LA_RECOMPOSITION_N_AJOUTE_PAS_DE_CONTENU_CANONIQUE
```

La consolidation est donc une décision de fonction et de contrôle, non une
opération de réduction quantitative. Une pièce supplémentaire n'est justifiée
que par un gain de discrimination, de lisibilité, de preuve, de maintenance ou
de récupération supérieur à son coût.

## Relations entre objets et vues

```text
OBJETS_DE_TRAVAIL
   -> DOSSIERS_DE_RECHERCHE
   -> VUES_PUBLIQUES_OU_DE_TRAVAIL
   -> ROUTES_DE_PROVENANCE
```

Une vue peut être recomposée lorsque les chemins changent. Elle doit conserver
les identités de travail et les relations nécessaires, mais elle ne doit pas
faire croire que sa composition actuelle est la structure ontologique du
projet.

## Test minimal du modèle

Le modèle sera confronté à un lot réduit comprenant au moins :

1. une porte d'accueil générale ;
2. une synthèse scientifique qualifiée ou bornée ;
3. une pièce de preuve ou de protocole ;
4. une règle méthodologique ;
5. une archive ou une pièce de provenance ;
6. un essai éditorial ou architectural.

Pour chaque pièce, il faudra vérifier :

- si l'identité de travail peut être décrite sans son chemin actuel ;
- si sa fonction dominante et ses fonctions secondaires sont distinguables ;
- si ses relations sont sémantiques, probatoires, historiques ou distributives ;
- si le modèle conserve ses limites, contradictions et conditions de reprise ;
- si la pièce résiste légitimement à une classification proposée.

## Résultat attendu du palier 1

```text
MODELE_CONCEPTUEL = A_CONFRONTER_AU_CORPUS
ARBORESCENCE_CIBLE = NON_DECIDEE
NOMBRE_DE_DOCUMENTS = A_DEDUIRE_DES_FONCTIONS_ET_RELATIONS
VUES = A_TESTER_APRES_IDENTIFICATION_DES_OBJETS
CI = HORS_PERIMETRE_IMMEDIAT
DECISION_HUMAINE = REQUISE_AVANT_MIGRATION
```
