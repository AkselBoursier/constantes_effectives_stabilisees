# Cadrage d'une réarchitecture générale sans perte

## Fonction et statut

Artefact interne du laboratoire d'audit. Il ouvre une conception d'architecture
sans déplacer, renommer, supprimer ou réécrire les pièces existantes.

```text
CHANTIER = REARCHITECTURE_GENERALE_DU_DEPOT
STATUT = CONCEPTION_A_INSTRUIRE
BRANCHE = AUDIT_LOCALE
INVESTIGATIONS_EXISTANTES = CONSERVEES
MUTATION_DE_L_ARBORESCENCE = NON_OUVERTE
MIGRATION = NON_OUVERTE
```

Repenser l'architecture ne signifie pas recommencer les investigations. Il
s'agit de proposer un cadre plus lisible et plus fonctionnel pour accueillir
les travaux physiques, computationnels, méthodologiques, philosophiques et
éditoriaux déjà produits, ainsi que leurs prolongements.

## Hypothese de depart

La structure actuelle a servi de support historique et opérationnel, mais elle
juxtapose plusieurs principes d'organisation :

- des domaines de recherche (`02_CYCLES_PHYSIQUES`, `06_PHILOSOPHIE`) ;
- des fonctions documentaires (`01_CADRE_METHODOLOGIQUE`, `05_CARTES_ET_SYNTHESES`) ;
- des couches de provenance et d'archives (`91`, `92`) ;
- un laboratoire éditorial (`93`) ;
- des critiques, environnements et outils (`90`, `99`, `tools`, `audit`) ;
- des états et routes opérationnels portés par les README, issues et pièces
  locales.

Le problème n'est donc pas d'abord le nombre de dossiers. C'est l'absence d'un
principe dominant qui permette de savoir où un document vit, ce qu'il établit,
qui peut le lire et comment il se rattache aux autres fonctions.

Cette hypothese est falsifiable. Elle sera requalifiee si l'architecture
actuelle permet deja ces distinctions avec un cout de lecture acceptable, ou si
une nouvelle organisation cree davantage de doublons et de routes que de
clarte.

## Portee du terme « semantique »

Dans ce cadrage, « semantique » ne doit pas etre compris comme une simple
question de vocabulaire, de style ou de reformulation des documents existants.
Il peut servir de terme englobant pour l'architecture de ce que chaque piece
veut dire, etablit, suppose, borne et rend transmissible.

Le terme de travail recommande est donc :

```text
ARCHITECTURE_SEMANTIQUE_INTEGRALE
 = PHYSIQUE
 + EPISTEMIQUE
 + COMPUTATIONNELLE
 + METHODOLOGIQUE
 + PHILOSOPHIQUE
 + EDITORIALE
```

Cette somme ne fusionne pas les registres. Elle exige au contraire de conserver
leur distinction et de rendre explicites leurs passages :

| Registre | Question de sens a preserver |
|---|---|
| **Physique** | Quelle cible, quelle transformation, quel regime, quelle grandeur ou relation sont effectivement examines ? |
| **Epistemique** | Par quel acces, quelle justification, quel degre de soutien et quelle limite l'enonce devient-il recevable ? |
| **Computationnel** | Quel calcul, quelle representation, quel resultat machine et quelle qualification technique sont en jeu ? |
| **Methodologique** | Quelle regle, quel contre-test, quel critere d'arret ou d'amendement organise l'enquete ? |
| **Philosophique** | Quelle interpretation, quelle portee conceptuelle ou quel transfert est propose, et avec quel statut ? |
| **Editorial** | Pour quel public, quelle fonction, quel niveau de lecture et quelle route le contenu est-il compose ? |

Ainsi, la semantique constitue le niveau de liaison et de conservation du sens,
non un sixieme domaine qui absorberait les cinq autres. Une architecture peut
etre semantiquement coherente tout en laissant une question physique ouverte,
un calcul non qualifie ou une interpretation suspendue.

La distinction est importante :

```text
SEMANTIQUE = CE_QUI_REND_LES_REGISTRES_LISIBLES_ET_RELIABLES
             ENTRE_EUX
SEMANTIQUE != VERITE_PHYSIQUE
SEMANTIQUE != QUALIFICATION_AUTOMATIQUE
SEMANTIQUE != UNIFORMISATION_DES_REGISTRES
```

Le mot « semantique » peut donc suffire dans le nom général du chantier, a
condition que son perimetre soit declare ainsi. Dans les contrats locaux, il
faudra conserver les noms des registres concernes plutot que d'ecrire seulement
« contenu semantique ».

### Méta-règle d'ouverture et d'émergence

La liste des registres ci-dessus est initiale et illustrative. Elle n'est pas
une taxonomie fermée, ni une obligation de classement exhaustif. Un contenu
peut rester transversal, mixte, non classé ou provisoirement indécidable si
aucune catégorie ne le décrit sans perte.

```text
REGISTRES_PROPOSES = REPÈRES_INITIAUX, NON_LISTE_FERMEE
ELEMENT_EMERGENT = A_DECRIRE_AVANT_DE_LE_CLASSER
FORCAGE_DANS_UNE_CASE = REFUSE
DIMENSION_NOUVELLE = A_TESTER, NON_AJOUTER_AUTOMATIQUEMENT
STATUT_NON_CLASSABLE = RECEVABLE_ET_A_CONSERVER
```

Lorsqu'un élément nouveau apparaît, la première question n'est donc pas « dans
quelle case le faire entrer ? », mais « que change-t-il dans la compréhension,
la preuve, la méthode, la pratique ou la transmission du projet ? ». Il peut
révéler une relation entre plusieurs registres, une fonction qui les traverse,
ou une dimension que le modèle ne prévoyait pas.

Une dimension nouvelle ne devient pas une nouvelle catégorie durable par sa
seule apparition. Elle doit montrer un gain discriminant, une fonction propre
ou une nécessité de contrôle supérieure au coût de l'ajouter. Inversement,
l'absence de catégorie adaptée ne doit jamais justifier la disparition,
l'affaiblissement ou la réécriture silencieuse de l'élément.

Cette méta-règle reprend la règle générale d'émergence des règles : le modèle
reste ouvert à ce qui le met en défaut, et toute extension est locale tant
qu'elle n'a pas été testée au-delà de son cas d'apparition.

## Principes de conception

1. **Fonction avant emplacement.** Un chemin ne doit pas décider seul du rang,
   de l'etat ou de l'usage d'une pièce.
2. **Etat courant et provenance séparés.** Une vue actuelle ne doit pas porter
   toute sa généalogie ; la provenance doit rester retrouvable.
3. **Domaine et fonction distingués.** Un cycle physique, une règle
   méthodologique et une synthèse ne sont pas trois versions du même objet.
4. **Documents autonomes avant liens.** Le contenu, ses limites et ses
   dépendances sémantiques sont établis avant la distribution.
5. **Relations explicites et remplaçables.** Les liens de navigation peuvent
   changer ; les dépendances qui changent un verdict doivent être tracées comme
   telles.
6. **Historique non réécrit.** La migration produit des correspondances ; elle
   ne réorganise pas les archives pour fabriquer une cohérence rétroactive.
7. **Une architecture évolutive.** Les classes et espaces proposés restent
   amendables après un test local.
8. **Pas de centralisation automatique.** Un registre ou un index n'est créé
   que s'il apporte un contrôle que les documents locaux, Git ou les issues ne
   fournissent pas déjà.

## Séparation proposée des plans

L'architecture cible ne doit pas nécessairement reprendre les numéros actuels.
Elle pourrait distinguer cinq plans, à tester avant tout choix de chemins :

| Plan | Fonction | Exemples de contenu |
|---|---|---|
| **Public** | Permettre une lecture courante et un premier parcours. | Objet du projet, cartes, synthèses lisibles, limites. |
| **Recherche** | Organiser les travaux par domaine et question instruite. | Physique, computation, philosophie, méthodologie, interfaces. |
| **Preuve** | Conserver les pièces qui établissent, contrôlent ou bornent un résultat. | Protocoles, extractions, rapports, résultats, qualifications, contre-tests. |
| **Provenance** | Rendre les transformations et états réauditables. | Sources, versions, décisions, archives, journaux, généalogie. |
| **Laboratoire** | Tester des formes, architectures et hypothèses sans promotion automatique. | Prototypes éditoriaux, matrices, essais d'architecture, tests de migration. |

Ces plans sont des fonctions, pas encore des dossiers. Une réarchitecture
réussie pourra les matérialiser différemment selon les besoins du dépôt.

## Questions qui doivent précéder l'arborescence

```text
QUELLE_EST_L_UNITE_PRIMAIRE = DOCUMENT, DOSSIER, QUESTION, RESULTAT OU DOSSIER_DE_RECHERCHE ?
QUELLE_RELATION_EST_SEMANTIQUE = CE_QUI_CHANGE_LE_VERDICT_OU_LA_PORTÉE
QUELLE_RELATION_EST_DISTRIBUTIVE = CE_QUI_AIDE_A_NAVIGUER_SANS_ETABLIR_LE_SENS
QUEL_ETAT_DOIT_ETRE_LISIBLE = ETAT_COURANT, OUVERTURE, SUSPENSION, QUALIFICATION
QUELLE_PROVENANCE_DOIT_ETRE_RECUPERABLE = SOURCE, DECISION, VERSION, TRANSFORMATION
QUELLE_MIGRATION_EST_REVERSIBLE = CORRESPONDANCE_SANS_DEPLACEMENT_INITIAL
```

Tant que ces questions ne sont pas instruites, créer une nouvelle profondeur
d'arborescence serait prématuré.

## Options à comparer

### Option A : réorganisation par plans

Créer des espaces publics, de recherche, de preuve, de provenance et de
laboratoire, avec des routes entre eux.

- **Gain possible :** séparation claire des fonctions.
- **Risque :** déplacer des pièces qui appartiennent à plusieurs plans et
  reconstruire trop de liens.
- **Test requis :** vérifier si les documents peuvent être mappés sans
  duplication ni perte de rang.

### Option B : domaines de recherche avec fonctions internes

Conserver les grands domaines, mais imposer à l'intérieur de chacun une
séparation stable entre accueil, synthèse, preuve et provenance.

- **Gain possible :** continuité avec les travaux scientifiques existants.
- **Risque :** reproduire la plomberie actuelle dans chaque domaine.
- **Test requis :** comparer le cout de lecture transversal et la maintenance
  des fonctions répétées.

### Option C : documents autonomes et index générés tardivement

Stabiliser des documents par fonction et conserver les relations dans une
couche de navigation produite après coup.

- **Gain possible :** faible dépendance aux chemins et meilleure migrabilité.
- **Risque :** perdre des relations si elles ne sont pas distinguées des liens
  simples.
- **Test requis :** tracer les dépendances sémantiques avant de tester l'index.

Les options peuvent être combinées. Le test ne cherchera pas à élire une
architecture générale par préférence abstraite.

## Recommandation de travail

La piste la plus prometteuse est une architecture **à axes séparés**, plutôt
qu'une nouvelle hiérarchie unique :

```text
DOCUMENT_AUTONOME = UNITE_DE_SENS_ET_DE_PROVENANCE
DOMAINE = TERRAIN_DE_RECHERCHE_OU_QUESTION
FONCTION = ACCUEIL, CARTE, SYNTHESE, PREUVE, METHODE, PROVENANCE, ESSAI
STATUT = EXPLORATION, EN_COURS, SUSPENDU, QUALIFIE_DANS_LE_PERIMETRE, ARCHIVE
VUE = DISTRIBUTION_PUBLIQUE_OU_ROUTE_DE_TRAVAIL
```

Dans cette hypothèse, un dossier physique peut contenir plusieurs fonctions,
mais une synthèse ne devient pas une simple sous-section de la carte qui la
distribue. Le statut ne devrait pas être encodé uniquement dans le nom du
fichier ou dans la profondeur du chemin. La provenance ne devrait pas être
reconstruite à partir de la seule position actuelle.

### Conséquences pratiques

- Les documents porteurs de sens reçoivent un nom stable et une identité de
   travail indépendante de leur destination future.
- Les cartes, README et index servent à orienter ; ils ne deviennent pas les
   sources canoniques de tous les contenus qu'ils distribuent.
- Une même pièce peut être reliée à un domaine et à plusieurs fonctions sans
   être copiée dans plusieurs dossiers.
- Les états mouvants restent dans les portes opérationnelles appropriées ; ils
   ne sont pas figés dans une carte publique.
- Les relations sont décrites par leur nature : dépendance sémantique,
   provenance, complément, route ou simple voisinage.
- Une vue publique peut être reconstruite lorsque les chemins changent, sans
   réécrire les documents de fond.

Cette piste ne demande pas nécessairement un outil ou un registre central. Un
registre n'est justifié que si l'inventaire montre que Git, les documents
locaux et les issues ne suffisent plus à retrouver les identités, statuts et
relations.

## Deux workflows à ne pas confondre

La reconception doit distinguer au moins deux workflows, dont les objets et les
critères de réussite ne sont pas les mêmes.

### Workflow sémantique intégral

Il organise le travail sur le sens du projet : comprendre une pièce, identifier
son registre ou son caractère transversal, préserver ses limites, qualifier ses
relations, choisir sa fonction documentaire et construire une vue adaptée à un
public ou à une tâche.

```text
QUESTION_OU_BESOIN
-> CONTENU_ET_REGISTRES_CONCERNES
-> STATUT_ET_PORTEE
-> DEPENDANCES_SEMANTIQUES
-> DOCUMENT_AUTONOME_OU_RELATION
-> VUE_ET_ROUTAGE
-> TEST_DE_PERTE_ET_DE_LISIBILITE
```

Ce workflow précède la stabilisation des chemins. Il peut produire une
proposition, un refus de classer, une demande de triangulation ou une
architecture locale. Il ne transforme pas automatiquement son résultat en
publication ni en migration.

### Workflow CI et maintenance technique

Le workflow CI vérifie l'état technique du dépôt : syntaxe, liens, formats,
outils, tests automatisables, contrôles de provenance et éventuellement
génération de vues. Il ne décide pas du sens scientifique, du rang d'une pièce,
de la portée d'un résultat ou de la promotion d'un document.

```text
ARTEFACTS_ET_REGLES_DEJA_QUALIFIES
-> CONTROLES_AUTOMATISABLES
-> RAPPORT_TECHNIQUE
-> CORRECTION_OU_ESCALADE_HUMAINE
```

Le CI peut donc soutenir le workflow sémantique intégral, mais ne doit pas le
remplacer. Une vérification technique réussie établit seulement que le
contrôle technique exécuté a réussi dans son périmètre.

### Ordre de conception

Le workflow sémantique intégral est prioritaire pour la réarchitecture actuelle.
L'amélioration du CI constitue une phase ultérieure, après clarification des
objets, statuts, relations et vues qu'il devra contrôler. Concevoir le CI trop
tôt risquerait de figer l'architecture actuelle et de transformer ses chemins
transitoires en contrats durables.

## Découpage recommandé du travail

### Palier 1 : modèle conceptuel

Définir les axes, les statuts et les relations minimales avec quelques exemples
existants. Ne créer aucun dossier cible.

### Palier 2 : mappage sans déplacement

Associer un lot réduit de pièces aux axes proposés. Une pièce peut recevoir
plusieurs étiquettes de fonction, mais son contenu canonique reste unique.

### Palier 3 : test de vues

Construire sur copie une vue publique, une vue de recherche et une vue de
provenance à partir du même lot. Vérifier que chacune est lisible sans
transformer les autres en doublons.

### Palier 4 : migration pilote

Choisir un lot homogène dont les dépendances sont comprises. Créer des
correspondances réversibles entre anciennes et nouvelles destinations, sans
supprimer ni déplacer les sources.

### Palier 5 : décision d'architecture

Comparer le gain réel, les pertes, la maintenance et la possibilité de retour.
La décision humaine porte alors sur l'architecture, le périmètre de migration
et le traitement des pièces non classables.

Cette progression permet de repartir de zéro **architecturalement** sans
repartir de zéro **scientifiquement**.

## Anti-patterns à éviter

- Remplacer les dossiers numérotés par de nouveaux dossiers numérotés sans
   changer le principe d'organisation.
- Déduire le statut d'une pièce de son emplacement ou de la date de son nom.
- Faire d'un README un index, un journal, une synthèse scientifique et un
   contrat opérationnel à la fois.
- Créer une copie « publique » avant d'avoir identifié la pièce canonique et
   sa provenance.
- Générer des liens avant de distinguer les dépendances sémantiques des routes
   de navigation.
- Transformer une architecture expérimentale en règle générale parce qu'elle
   fonctionne sur un seul lot.

## Protocole de conception sans perte

1. Inventorier les fonctions et les contenus, sans modifier les sources.
2. Sélectionner un petit lot couvrant plusieurs plans mais une question locale.
3. Décrire chaque pièce par un contrat sans destination.
4. Construire deux ou trois cartes d'architecture abstraites.
5. Mapper les pièces vers chaque carte sans les déplacer.
6. Comparer pertes, duplications, ambiguïtés, coûts de liaison et lisibilité.
7. Tester la reprise d'un document ancien, d'un résultat qualifié et d'un
   prototype éditorial.
8. Consigner les éléments qui ne peuvent pas être classés proprement.
9. Soumettre une architecture candidate à décision humaine.
10. Seulement ensuite établir un plan de migration réversible, par lots.

```text
AUCUN_DEPLACEMENT_AVANT_MAPPAGE
AUCUNE_SUPPRESSION_AVANT_RECUPERABILITE
AUCUNE_REECRITURE_HISTORIQUE
AUCUNE_PROMOTION_D_UN_PROTOTYPE_PAR_SEULE_EXISTENCE
```

## Critères de réussite

Une architecture candidate doit rendre plus facile, pour un lecteur ou un
agent autorisé, de répondre à ces questions :

- Que cherche ce document ?
- Quel rang possède-t-il ?
- Est-ce un état courant, une preuve, une exploration ou une archive ?
- Quel contenu unique porte-t-il ?
- Quelles dépendances changeraient sa lecture ou son verdict ?
- Où poursuivre sans confondre approfondissement et autorisation ?
- Comment retrouver la provenance sans l'imposer à la première lecture ?

Elle doit aussi réduire le besoin de recréer les mêmes textes lorsqu'un nom,
un chemin ou une distribution change.

## Etat du chantier

```text
ARCHITECTURE_ACTUELLE = SUPPORT_HISTORIQUE_ET_OPERATIONNEL
ARCHITECTURE_CIBLE = A_CONCEVOIR
CLASSES_DOCUMENTAIRES = HYPOTHESES_EN_COURS
PROTOTYPE_LIE_AUX_CHEMINS = CONSERVE_COMME_TEMOIN
NOUVELLE_ARBORESCENCE = NON_CREEE
MIGRATION_EFFECTIVE = NON_AUTORISEE
DECISION_HUMAINE = REQUISE_AVANT_TOUTE_MUTATION
```
