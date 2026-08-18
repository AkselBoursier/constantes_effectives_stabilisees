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
