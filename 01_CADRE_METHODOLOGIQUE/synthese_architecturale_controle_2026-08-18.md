# Synthèse architecturale de contrôle

## Fonction et statut

Document de contrôle du laboratoire. Il rassemble les résultats des cadrages et
tests de reconception menés jusqu'ici, sans créer une nouvelle série d'épreuves,
une arborescence cible ou une migration.

```text
CHANTIER = RECONCEPTION_DE_L_ENVIRONNEMENT_DU_TRAVAIL
STATUT = SYNTHESE_DE_CONTROLE_A_VALIDER
SOURCES_SCIENTIFIQUES = INTACTES
ARCHITECTURE_CIBLE = NON_DECIDEE
MIGRATION = NON_OUVERTE
PROLIFERATION_DE_TESTS = SUSPENDUE_A_CE_PALIER
```

## Question de contrôle

Les tests ont-ils réellement rendu le projet plus compréhensible et migrable,
ou ont-ils simplement remplacé la fragmentation généalogique par une nouvelle
prolifération de catégories et de documents ?

## Ce qui est établi localement

### 1. Un socle d'objets plutôt qu'une hiérarchie unique

Le chemin ne suffit pas à définir l'identité, la fonction, le statut ou la
provenance d'une pièce. Un objet de travail doit pouvoir être décrit hors de sa
destination :

```text
OBJET_DE_TRAVAIL = IDENTITE + CONTENU + PORTEE + STATUT + PROVENANCE
```

Les dossiers, cartes, README et index peuvent organiser des vues, mais ne
deviennent pas automatiquement les sources canoniques des contenus.

### 2. Des axes séparés

Les tests ont distingué :

```text
OBJET
DOMAINE_OU_QUESTION
FONCTION
STATUT
ETAT_DE_LA_LIGNE
AUTORISATION
VUE
PROVENANCE
RELATIONS
```

Aucun axe ne doit être déduit automatiquement d'un autre. En particulier :

- un domaine ne détermine pas une fonction unique ;
- une fonction ne détermine pas le statut ;
- un statut actif n'est pas une autorisation ;
- une vue ne devient pas une autorité par sa visibilité ;
- une archive ne redevient pas active par sa présence ;
- un chemin ne constitue pas une identité.

### 3. Une architecture sémantique intégrale mais ouverte

La sémantique intégrale relie les registres physique, épistémique,
computationnel, méthodologique, philosophique et éditorial, sans les fusionner.
La liste reste ouverte : transversalité, non-classement ou dimension émergente
sont des résultats recevables.

```text
ARCHITECTURE_SEMANTIQUE_INTEGRALE = LIAISON_ET_CONSERVATION_DU_SENS
REGISTRES = DISTINCTS_ET_ARTICULABLES
FORCAGE_TAXONOMIQUE = REFUSE
```

### 4. Des vues multiples sur les mêmes objets

Une vue publique, une vue de recherche, une vue de provenance ou une vue de
relations peuvent sélectionner et ordonner les mêmes objets sans en créer des
copies canoniques.

```text
VUE = SELECTION + ORDRE + CONTEXTE + ROUTE
VUE != NOUVEAU_RESULTAT
VUE != REGISTRE_EXHAUSTIF
```

La vue de recherche doit probablement rester locale à une question ou à un
domaine. Une vue relationnelle peut être utile sous question ciblée ; une vue
exhaustive est déconseillée.

### 5. Des relations typées

Les relations de route, de complément, de provenance, de preuve, de reprise,
de norme, de contradiction et de dépendance sémantique ne sont pas
interchangeables. Les liens Markdown sont des supports techniques ; ils ne
suffisent pas à décrire la relation.

```text
RELATION = TYPE + SOURCE + CIBLE + PORTEE + CONDITION
```

Les relations transversales du lot secondaire restent gérables sans registre
central. Un registre général n'est pas justifié par les résultats obtenus.

### 6. Une chaîne computationnelle séparée et reliée

Le code, l'environnement, l'exécution, la sortie machine, la qualification
technique, le résultat scientifique, le verdict et la portée doivent rester
séparés tout en étant reliés :

```text
CODE
-> ENVIRONNEMENT
-> EXECUTION
-> SORTIE_MACHINE
-> QUALIFICATION_TECHNIQUE
-> RESULTAT_SCIENTIFIQUE
-> VERDICT_ET_PORTEE
```

La documentation du code ne valide pas le modèle. Une reproduction bornée ne
constitue pas une nouvelle mesure. Une empreinte de provenance ne constitue pas
une validation physique.

### 7. Un workflow global composé, non remplacé par le CI

Le workflow global comprend la sémantique, la recherche, la provenance, les
décisions humaines et le CI. Le CI en est une composante technique ; il peut
réduire la charge cognitive sur des opérations répétitives, contrôlables et
réversibles, sans décider du modèle, de la portée, de la promotion ou de
l'autorisation.

### 8. Un audit lui-même documentable

L'audit est un objet possible de workflow et de provenance. Ses phases, retours,
contre-tests, résultats négatifs et effets sur la transformation du projet
peuvent être documentés séparément des résultats scientifiques qu'il a
qualifiés. Sa séparation en phases réutilisables ou sa templatisation reste
conditionnelle à l'évaluation de sa valeur réelle.

## Ce qui reste hypothétique

```text
ARBORESCENCE_MATERIELLE = NON_DEFINIE
NOMBRE_FINAL_DE_DOCUMENTS = NON_DEFINI
REGISTRE_RELATIONNEL = NON_JUSTIFIE_A_CE_PALIER
DOCUMENTS_AUTONOMES = SOCLE_PROVISOIRE
PLANS_FONCTIONNELS = VUES_A_TESTER
DOMAINES = CONTEXTES_DE_RECHERCHE
TEMPLATE_AUDIT = NON_DECIDE
PIPELINES_PUBLICS = NIVEAUX_A_QUALIFIER
CI_FUTUR = A_CONCEVOIR_APRES_QUALIFICATION_DES_OBJETS
```

Les deux destinations abstraites testées passent le contrôle des invariants,
mais aucune destination matérielle n'est préférée de manière définitive. La
combinaison la plus contrainte à ce stade est :

```text
OBJETS_AUTONOMES_ET_RELATIONS_EXPLICITES = SOCLE
PLANS_FONCTIONNELS = VUES_DE_DISTRIBUTION
DOMAINES = CONTEXTES_DE_RECHERCHE
STATUTS_ET_AUTORISATIONS = DECOUPLES
```

## Ce qui est en veille active

Le fil outils et workflow n'est pas fermé. Il est mis en veille active afin que
les outils puissent être testés directement sur pièce lors d'opérations réelles.
Aucun inventaire exhaustif, paquet public ou template général n'est en cours.

```text
FIL_OUTILS = MIS_EN_VEILLE_ACTIVE
RESULTATS_LOCAUX = CONSERVES
PROMOTION_PUBLIQUE = NON_OUVERTE
TEST_DIRECT_SUR_PIECE = DECLENCHEUR_POSSIBLE_DE_REOUVERTURE
```

## Diagnostic de convergence

Les tests ont produit une direction plus contrainte, et non une architecture
achevée. La convergence est réelle sur les invariants et les distinctions :

- les pièces ne sont plus forcées dans une seule hiérarchie ;
- les objets transversaux peuvent rester transversaux ;
- les statuts, états et autorisations sont séparés ;
- la provenance reste récupérable sans gouverner l'état courant ;
- les vues peuvent changer sans déplacer le contenu canonique ;
- les résultats computationnels ne sont pas confondus avec leur documentation.

Le risque de métaprolifération existe néanmoins. Il est contrôlé par la règle
suivante : ce document devient la synthèse de contrôle du palier, et aucune
nouvelle catégorie ou série de tests n'est ajoutée sans discriminant matériel.

```text
DIRECTION = COHERENTE
IMAGE_GLOBALE = PARTIELLEMENT_VISIBLE_MAIS_PLUS_CONTRAINTE
CHAOS_RECONSTRUIT = NON_DEMONTRE
RISQUE_DE_METAPROLIFERATION = REEL_ET_SURVEILLE
NOUVEAU_TEST = EXIGE_UN_DISCRIMINANT
```

## Décision de passage réservée

La prochaine décision ne porte pas encore sur une migration. Elle devra choisir
entre :

1. poursuivre avec un mappage élargi mais toujours abstrait ;
2. préparer une architecture candidate sur copie ;
3. documenter d'abord le workflow global du laboratoire ;
4. suspendre la reconception et reprendre une ligne scientifique prioritaire.

Cette décision exige une lecture humaine de la présente synthèse. Aucun de ces
choix n'est activé automatiquement par la production du document.
