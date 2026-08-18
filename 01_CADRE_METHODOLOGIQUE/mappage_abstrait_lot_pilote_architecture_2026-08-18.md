# Mappage abstrait du lot pilote

## Fonction et statut

Artefact interne du palier 2 de la reconception de l'environnement de travail.
Les chemins cites ci-dessous sont des identifiants d'observation du clone ; ils
ne constituent ni des destinations cibles, ni des recommandations de migration.

```text
PALIER = 2 / MAPPAGE_ABSTRAIT_SANS_DEPLACEMENT
LOT = 6 PIECES, 6 FONCTIONS DOMINANTES
STATUT = MAPPAGE_A_TESTER
SOURCES = INTACTES
DESTINATIONS_FUTURES = NON_DEFINIES
MIGRATION = NON_OUVERTE
```

## Hypothese testee

Les six pieces peuvent etre decrites par des axes separes : objet de travail,
domaine ou question, registres semantiques, fonction, statut, portee, public,
provenance et relations. Si une piece ne peut pas etre decrite sans son chemin,
ou si le mappage lui impose une fonction qu'elle n'exerce pas, le modele doit
etre requalifie plutot que la piece forcee.

## Lot retenu

| Identifiant d'observation | Fonction dominante observee | Pourquoi cette piece |
|---|---|---|
| `L1` | Accueil | `README.md` : porte publique generale et routage humain. |
| `L2` | Synthese scientifique | `02_CYCLES_PHYSIQUES/03_Cycle_neutrinos/Synthese_active_cycle_3_neutrinos_apres_N5_v0_2.md` : resultat actif borne, acquis et limites explicites. |
| `L3` | Blocage ou rapport de preuve computationnelle | `02_CYCLES_PHYSIQUES/01_Cycle_couplages_echelles_QCD/T1_5_Rapport_blocage_reproduction_lattice_ALPHA_2026_v0_1.md` : obstacle d'acquisition caractérisé, sans conclusion scientifique excessive. |
| `L4` | Decision ou contrat methodologique | `01_CADRE_METHODOLOGIQUE/Decision_statuts_constance_acces_constitution_v0_1.md` : decision de rang et distinction normative active dans son perimetre. |
| `L5` | Provenance et genealogie | `91_TRAVAUX_ANTERIEURS/README.md` : mode d'emploi d'une archive, sans autorite active automatique. |
| `L6` | Plan ou essai editorial | `93_LABORATOIRE_EDITORIAL_EXPERIMENTAL/ESSAI_tentative/plans/Plan_livrable_theorique_v0_3.md` : structure de rédaction expérimentale, non texte public autorisé. |

## Mappage par axes

| Objet | Domaine ou question | Registres | Fonction | Statut observé | Portée / limite | Public ou usage |
|---|---|---|---|---|---|---|
| **L1 README racine** | Projet général et routes d'entrée | Editorial ; methodologique ; transversal | Accueil | Vue publique courante | Ne porte ni verdict scientifique détaillé ni état opérationnel complet | Nouveau lecteur ; orientation humaine |
| **L2 Synthèse neutrinos** | Accès et reconstruction du secteur neutrino | Physique ; epistemique ; methodologique | Synthèse scientifique | Actif dans un périmètre borné | Ne vaut pas détermination conjointe, ordre, masse minimale, phases de Majorana ou mécanisme de masse | Reprise scientifique et comparaison des voies |
| **L3 Rapport de blocage ALPHA** | Reproduction computationnelle d'un résultat lattice | Computationnel ; epistemique ; methodologique | Rapport de preuve / blocage | Blocage d'exécution caractérisé | Ne vaut ni échec de réplication, ni critique du paquet, ni invalidation du résultat publié | Reprise computationnelle et décision de condition de reprise |
| **L4 Décision statuts** | Distinction objet, accès et constitution | Methodologique ; epistemique ; philosophique ; transversal | Décision / contrat méthodologique | Canonique active dans son périmètre | Ne supprime pas les acquis ; ne commande pas automatiquement les états programmatiques locaux | Qualification et arbitrage méthodologique |
| **L5 Travaux antérieurs** | Trajectoire et reprises historiques | Provenance ; editorial ; philosophique ; transversal | Archive / route généalogique | Archive non autoritative | Une présence ancienne n'établit ni validité ni droit de reprise automatique | Audit historique et comparaison |
| **L6 Plan théorique v0.3** | Composition d'un essai sur la qualification de la constance | Editorial ; methodologique ; epistemique ; philosophique | Plan / essai de laboratoire | Expérimental, soumis à validation section par section | Ne vaut ni texte public ni validation scientifique | Conception éditoriale et test de structure |

## Contenu unique à protéger

### L1 — README racine

- les deux questions publiques du projet ;
- la distinction constance / stabilisation ;
- les routes humaines et la séparation entre état courant et provenance ;
- l'avertissement qu'un document ancien n'est pas automatiquement l'autorité
  actuelle.

### L2 — Synthèse neutrinos

- la distinction des quatre voies d'accès et de leurs fonctions non équivalentes ;
- le spectre latent comme objet commun minimal ;
- les résultats et limites propres à chaque voie ;
- le refus d'une échelle de qualité unique entre les accès.

### L3 — Rapport de blocage

- la distinction entre blocage d'environnement et défaut scientifique ;
- les tentatives d'accès effectivement exécutées ;
- la condition exacte de reprise ;
- le refus de surqualifier le blocage en échec de réplication.

### L4 — Décision méthodologique

- les trois niveaux objet / accès / constitution ;
- la règle de non-confusion entre stabilisation de l'accès et constance de l'objet ;
- le rang canonique et la portée bornée de la décision.

### L5 — Provenance antérieure

- la fonction d'archive non autoritative ;
- la chaîne de reprise historique avec vérification indépendante ;
- les limites de la chronologie reconstruite ;
- les précautions sur les métadonnées et les matériaux anciens.

### L6 — Plan éditorial

- les budgets et la structure du livrable ;
- les conditions de rédaction et les lectures pivots ;
- les limites documentaires restantes ;
- la distinction entre plan, texte et validation scientifique.

## Relations observées

| Source | Relation | Cible ou ensemble | Contrôle requis |
|---|---|---|---|
| L1 | Route de lecture | L2, L4, autres portes | Le routage ne doit pas acquérir le rang du contenu cible. |
| L2 | Dépendance probatoire / complément | Fiches N0-N5 et pièces locales du cycle | Les voies et limites doivent rester comparables sans être fusionnées. |
| L3 | Dépendance de reprise | Paquet externe et conditions d'accès | Un blocage réseau ne doit pas devenir un verdict scientifique. |
| L4 | Contrat méthodologique | Documents applicables dans son périmètre | La précédence doit rester distinguée de la simple date ou du chemin. |
| L5 | Provenance | Travaux et décisions antérieurs | Une route généalogique ne vaut pas autorisation de réintégration. |
| L6 | Plan expérimental | Sources et décisions éditoriales | Le plan ne doit pas être promu comme document public ou scientifique. |
| L2 <-> L4 | Articulation méthodologique | Qualification des accès et des portées | L4 encadre une lecture ; il ne remplace pas le résultat de L2. |
| L3 <-> L4 | Articulation méthodologique | Distinction machine / qualification / résultat | Le diagnostic computationnel reste local à L3. |
| L5 <-> L6 | Provenance / matériau expérimental | Reprise éventuelle de formes anciennes | La reprise exige comparaison et validation, pas continuité automatique. |

## Résultats du mappage

### Ce que le modèle décrit correctement

- Les six fonctions dominantes sont distinctes sans exiger six nouvelles
  arborescences.
- Les statuts ne sont pas interchangeables : actif borné, blocage caractérisé,
  décision canonique, archive et expérimentation ont des effets différents.
- Les liens de L1 ne sont pas du même type que les relations probatoires de L2
  ou la provenance de L5.
- Les limites et les conditions de reprise peuvent être conservées comme des
  propriétés de l'objet, indépendamment de sa destination.
- L3 montre qu'un résultat négatif d'environnement peut être un objet de travail
  autonome sans devenir un résultat scientifique négatif.

### Ce que le modèle ne doit pas encore décider

- le nombre final de documents actifs ;
- l'arborescence cible ;
- la fusion ou la séparation matérielle des pièces ;
- la création d'un registre central ;
- la génération automatique des liens ;
- la promotion publique de L6 ou d'une vue dérivée.

### Tensions ou limites du modèle

- L4 relève à la fois de la méthode, de l'épistémique et d'une histoire de
  décision ; la pluralité des registres ne doit pas produire des copies.
- L2 dépend d'un ensemble de pièces locales dont la granularité actuelle peut
  être conservée provisoirement sans être reconduite comme architecture cible.
- L5 est un dossier de provenance qui contient des fonctions de routage ; cela
  montre qu'une fonction dominante n'épuise pas la description.
- L1 et L6 ont une fonction éditoriale, mais des publics, statuts et usages
  incompatibles avec une consolidation directe.

Ces tensions sont des résultats du mappage, pas des défauts à corriger
immédiatement. Elles indiquent les points à examiner au test de vues.

## Verdict local du palier 2

```text
MAPPAGE_SANS_CHEMIN = POSSIBLE_SUR_LE_LOT
FONCTION_DOMINANTE = UTILE_MAIS_NON_EXCLUSIVE
REGISTRES_MULTIPLES = NECESSAIRES
OBJETS_NON_CLASSABLES = PREVUS_PAR_LE_MODELE
NOMBRE_DE_DOCUMENTS = NON_DEDUIT_A_CE_PALIER
ARBORESCENCE = NON_DEDUITE_A_CE_PALIER
PROCHAINE_ETAPE = TESTER_DES_VUES_SANS_RECOMPOSER_LE_CONTENU_CANONIQUE
```

Le modèle est suffisamment discriminant pour passer au test de vues, mais le
lot ne justifie encore aucune migration ni décision sur le nombre de documents.
