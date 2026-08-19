# Test des vues abstraites du lot pilote

## Fonction et statut

Artefact interne du palier 3 de la reconception de l'environnement de travail.
Il teste des projections de lecture a partir du mappage abstrait, sans creer de
nouvelle arborescence et sans dupliquer le contenu canonique des pieces.

```text
PALIER = 3 / TEST_DE_VUES
SOURCE = mappage_abstrait_lot_pilote_architecture_2026-08-18.md
STATUT = TEST_A_QUALIFIER
CONTENU_CANONIQUE = CONSERVE_DANS_LES_PIECES_SOURCES
ARBORESCENCE_CIBLE = NON_PROPOSEE
PROMOTION_PUBLIQUE = NON
```

## Hypothese testee

Un même ensemble d'objets peut produire plusieurs vues adaptées à des usages
différents, à condition que chaque vue indique son rôle et renvoie vers les
objets porteurs du contenu. Une vue ne doit pas devenir une nouvelle source
canonique par accumulation de résumés ou de statuts.

```text
OBJETS_IDENTIQUES
-> VUE_PUBLIQUE
-> VUE_DE_RECHERCHE
-> VUE_DE_PROVENANCE
CONTENU_CANONIQUE = NON_DUPLIQUE_PAR_DEFAUT
```

## Lot et objets mobilisés

Le test reprend L1 à L6 du mappage pilote : accueil général, synthèse neutrinos,
rapport de blocage computationnel, décision méthodologique, archive antérieure
et plan éditorial expérimental. Les chemins actuels ne servent qu'à retrouver
les objets observés ; ils ne sont pas testés comme architecture cible.

## Vue publique

### Fonction

Permettre à un nouveau lecteur de comprendre le projet, ses questions, ses
limites et les portes principales, sans devoir absorber la provenance, les
blocages d'exécution ou le workflow de laboratoire.

### Objets visibles en priorité

- **L1** comme objet d'accueil principal ;
- **L2** comme exemple de synthèse scientifique bornée ;
- **L4** comme repère méthodologique, seulement dans sa fonction de distinction
  et de portée ;
- **L5** comme route de provenance optionnelle ;
- **L3** et **L6** comme objets de profondeur, non comme état courant général.

### Ce que la vue doit préserver

- les deux questions du projet ;
- la différence entre objet scientifique, accès, constitution et stabilisation ;
- les limites de L2 et le caractère non scientifique du blocage L3 ;
- le statut non autoritatif de L5 et expérimental de L6.

### Ce qu'elle ne doit pas faire

- transformer L1 en tableau de bord ;
- publier le diagnostic détaillé de L3 comme résultat ;
- présenter L6 comme une publication ou une décision ;
- imposer la lecture de la généalogie ;
- créer une synthèse nouvelle qui deviendrait la source de L2 ou L4.

## Vue de recherche

### Fonction

Permettre à un chercheur de partir d'une question, d'un domaine ou d'une
condition de reprise et d'atteindre les pièces utiles avec leur portée exacte.

### Objets visibles en priorité

- **L2** et ses pièces directrices N0-N5 ;
- **L3** et ses conditions de reprise computationnelle ;
- **L4** pour la règle de qualification applicable ;
- **L1** comme route générale, sans lui attribuer un rang scientifique.

### Ce que la vue doit préserver

- la distinction entre résultat scientifique, résultat machine, qualification
  technique et blocage d'environnement ;
- les dépendances qui changent le verdict ou la possibilité de reprise ;
- les états locaux et leur portée ;
- le fait qu'une synthèse active remplace une synthèse de récupération pour le
  travail courant sans effacer cette dernière comme source historique.

### Ce qu'elle ne doit pas faire

- fusionner les quatre voies neutrino en un résultat unique ;
- transformer L4 en autorisation générale pour tous les cycles ;
- confondre une route de lecture avec une permission d'exécuter un calcul ;
- recopier dans une carte transversale tous les états mouvants des cycles.

## Vue de provenance

### Fonction

Rendre possible la reconstitution des origines, transformations, décisions,
versions et conditions de reprise sans imposer cette lecture au public courant.

### Objets visibles en priorité

- **L5** comme porte de provenance ;
- les sources et décisions reliées à **L2**, **L3**, **L4** et **L6** ;
- les états datés et archives nécessaires à la comparaison.

### Ce que la vue doit préserver

- la différence entre antériorité, autorité, validité et possibilité de reprise ;
- les transformations qui ont changé le sens ou le statut ;
- les blocages et refus historiques pertinents ;
- la récupérabilité des pièces sans déplacer l'autorité vers l'archive.

### Ce qu'elle ne doit pas faire

- reconstruire une continuité obligatoire ;
- réactiver une idée ancienne par sa seule présence ;
- remplacer les décisions actives par une chronologie ;
- devenir le contenu public par défaut.

## Comparaison des vues

| Critère | Vue publique | Vue de recherche | Vue de provenance |
|---|---|---|---|
| Question principale | Que fait le projet et où commencer ? | Que dois-je examiner pour cette question ? | Comment ce contenu et ce statut se sont-ils constitués ? |
| Fonction dominante | Orientation humaine | Reprise instruite | Réaudit et généalogie |
| Niveau de détail | Sélectif | Suffisant pour agir dans le périmètre | Détaillé selon la question |
| Statuts visibles | Courants et bornés | Locaux, conditions et permissions explicites | Datés, successifs et transformés |
| Relations prioritaires | Route, complément, limite | Dépendance sémantique et probatoire | Provenance, transformation, décision |
| Risque principal | Simplification excessive | Confusion entre preuve et autorisation | Historicisation imposée ou surpromotion du passé |
| Source canonique | Objets de travail liés | Objets et pièces de preuve | Archives, décisions et historiques reliés |

## Contrôle de non-duplication

Le test applique la distinction suivante :

```text
VUE = SELECTION + ORDONNANCEMENT + CONTEXTE + ROUTE
VUE != NOUVEAU_RESULTAT
VUE != COPIE_CANONIQUE
VUE != DECISION_DE_CLASSEMENT
```

Une formulation peut apparaître dans plusieurs vues si elle conserve le même
rang et la même portée. Une reformulation adaptée au public doit renvoyer à
l'objet porteur et ne doit pas créer une version concurrente non identifiée.

Les informations qui changent le verdict, la limite, le statut ou la condition
de reprise ne peuvent pas être réduites à un simple lien silencieux ; elles
doivent rester présentes dans l'objet canonique ou être explicitement signalées
comme relation.

## Résultats du test

### Gains observés

- Les trois vues peuvent être décrites à partir du même lot sans nouvelle
  arborescence.
- L1, L2, L3, L4, L5 et L6 changent de visibilité selon l'usage sans changer de
  statut par simple exposition.
- Les relations de navigation, de preuve et de provenance restent distinctes.
- L5 peut fournir une route généalogique sans devenir une autorité publique.

### Limites observées

- Une vue publique ne peut pas résumer seule les statuts mouvants de toutes les
  recherches.
- Une vue de recherche devra probablement être locale au domaine ou à la
  question, plutôt qu'un tableau de bord transversal unique.
- Une vue de provenance peut contenir plusieurs fonctions et ne se réduit pas à
  une chronologie.
- Le test ne permet pas encore de décider si les vues doivent être des fichiers,
  des README, des index générés ou une combinaison de ces formes.

## Verdict local du palier 3

```text
VUES_MULTIPLES_SUR_MEMES_OBJETS = POSSIBLE
CONTENU_CANONIQUE = NON_DUPLIQUE_PAR_DEFAUT
VUE_PUBLIQUE = SEPARABLE_DE_LA_PROVENANCE
VUE_DE_RECHERCHE = A_LOCALISER_PAR_QUESTION_OU_DOMAINE
VUE_DE_PROVENANCE = NECESSAIRE_MAIS_NON_IMPOSEE
ARBORESCENCE = TOUJOURS_NON_DEDUITE
MIGRATION = NON_OUVERTE
PROCHAINE_ETAPE = COMPARER_DES_CARTES_D_ARCHITECTURE_ABSTRAITES
```

Le test justifie une séparation fonctionnelle des vues, mais ne justifie pas
encore leur matérialisation en dossiers ou fichiers distincts.
