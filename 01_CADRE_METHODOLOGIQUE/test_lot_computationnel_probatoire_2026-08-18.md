# Test du lot computationnel et probatoire

## Fonction et statut

Artefact interne du palier 11 de la reconception. Il teste le contrat minimal sur
un lot où les relations de preuve, d'environnement, de provenance et de résultat
sont directement liées.

```text
PALIER = 11 / LOT_COMPUTATIONNEL_PROBATOIRE
STATUT = TEST_A_QUALIFIER
CALCUL_NOUVEAU = NON_LANCE
SOURCES = INTACTES
MIGRATION = NON_OUVERTE
```

## Lot retenu

| Identifiant | Pièce | Fonction observée |
|---|---|---|
| **C1** | `02_CYCLES_PHYSIQUES/03_Cycle_neutrinos/N0_Protocole_commun_fiches_acces_neutrinos_v0_1.md` | Protocole computationnel et probatoire commun |
| **C2** | `02_CYCLES_PHYSIQUES/03_Cycle_neutrinos/N5_Matrice_comparative_quatre_acces_neutrinos_v0_1.md` | Synthèse comparative de chaînes d'accès et d'énoncés situés |
| **C3** | `02_CYCLES_PHYSIQUES/01_Cycle_couplages_echelles_QCD/T1_5_Manifeste_local_paquet_ALPHA_2026_v0_1.md` | Manifeste de provenance et d'environnement d'exécution |
| **C4** | `02_CYCLES_PHYSIQUES/01_Cycle_couplages_echelles_QCD/T1_5_Resultats_reproduction_lattice_ALPHA_2026_v0_1.md` | Résultat de reproduction du pipeline dans un périmètre borné |
| **C5** | `02_CYCLES_PHYSIQUES/01_Cycle_couplages_echelles_QCD/T1_5_Rapport_blocage_reproduction_lattice_ALPHA_2026_v0_1.md` | État antérieur de blocage d'acquisition, conservé comme provenance |

## Mappage par chaîne de preuve

```text
C1 PROTOCOLE
-> C2 COMPARAISON_DES_ENONCES
-> C3 PROVENANCE_ET_ENVIRONNEMENT
-> C4 RESULTATS_EXECUTES
-> C5 ETAT_ANTERIEUR_ET_CONDITION_DE_REPRISE
```

Cette chaîne n'est pas une simple hiérarchie. C1 ne prouve pas C2 ; il fixe les
conditions de comparaison. C3 ne valide pas C4 ; il identifie le matériau et
l'environnement. C4 ne transforme pas automatiquement le traitement des
produits condensés en reproduction de toute l'analyse. C5 conserve une
condition historique de reprise sans devenir l'état courant de C4.

## Contrat appliqué aux objets

| Objet | Identité | Statut | Portée | Limite à conserver |
|---|---|---|---|---|
| C1 | Gabarit commun des quatre accès neutrino | Protocole actif | Étapes N1-N5 et coupure déclarée | Ne préjuge ni résultat ni compatibilité |
| C2 | Matrice comparative des fonctions du spectre neutrino | Synthèse active | Comparaison N1-N4 après N5 | Ne vaut pas ajustement conjoint ni détermination ontologique |
| C3 | Manifeste local du paquet ALPHA | Provenance et exécution | Archive, environnement, scripts et empreintes effectivement contrôlés | Ne prouve ni identité de commit ni validation indépendante des données |
| C4 | Traitement exécuté des produits condensés ALPHA | Résultat technique/scientifique borné | Routes et combinaisons effectivement exécutées | Ne reproduit ni simulations brutes ni calculs amont non fournis |
| C5 | Rapport historique de blocage d'accès ALPHA | Blocage caractérisé, daté | Acquisition dans l'environnement antérieur | Ne vaut ni échec de réplication ni invalidation du résultat publié |

## Relations de preuve et de provenance

| Relation | Type | Portée | Risque de confusion |
|---|---|---|---|
| C1 -> C2 | Dépendance méthodologique | Le gabarit structure la comparaison | Prendre le gabarit pour un résultat |
| C3 -> C4 | Dépendance de provenance / environnement | Le manifeste identifie le matériau et les conditions | Prendre l'empreinte pour une validation scientifique |
| C4 -> objet scientifique ALPHA | Soutien technique borné | Le pipeline traité soutient ce qu'il a effectivement exécuté | Promouvoir la reproduction bornée en nouvelle mesure |
| C5 -> C3/C4 | Provenance temporelle et condition de reprise | Le blocage explique une étape antérieure, puis sa levée | Laisser l'état ancien masquer l'état courant |
| C2 -> pièces N1-N5 | Dépendance probatoire et comparative | Les quatre voies et leurs limites fondent la matrice | Réduire quatre accès à un nombre commun |
| C1 <-> C2 | Articulation protocole / résultat | C1 encadre ; C2 porte l'énoncé comparatif | Confondre norme de comparaison et verdict |
| C3 <-> C4 | Articulation provenance / calcul | C3 documente ; C4 rapporte l'exécution | Confondre calcul, sortie machine et qualification |

## Test des distinctions computationnelles

Le lot doit préserver explicitement :

```text
CALCUL_EXECUTE
RESULTAT_MACHINE
QUALIFICATION_TECHNIQUE
RESULTAT_SCIENTIFIQUE
VERDICT
PORTEE
CONDITION_DE_REPRISE
```

### Résultat

Le lot permet de conserver ces distinctions. C4 est un résultat d'exécution et
de qualification dans le périmètre du paquet ; il ne devient pas une nouvelle
mesure indépendante. C3 peut établir la traçabilité de l'archive et de
l'environnement, mais pas la validité physique des données. C5 reste utile pour
comprendre la temporalité de la reprise, sans être recopié comme état courant.

## Test de changement de vue

Simuler deux vues à partir du même lot :

### Vue scientifique

Sélectionner C2 et les pièces nécessaires à ses fonctions comparatives. C1 est
visible comme protocole ; C3-C5 restent des routes de preuve ou de provenance,
non des résultats scientifiques incorporés dans C2.

### Vue computationnelle

Sélectionner C3 et C4, avec C5 comme état antérieur et condition de reprise. C2
peut être relié comme objet scientifique distinct, mais ne doit pas être
présenté comme sortie du pipeline ALPHA.

```text
VUE_SCIENTIFIQUE != VUE_COMPUTATIONNELLE
C4 != NOUVELLE_MESURE
C3 != VALIDATION_PHYSIQUE
C5 != ETAT_COURANT_AUTOMATIQUE
```

## Résultats du test

- Le contrat minimal tient sur un lot directement probatoire et computationnel.
- Les relations de preuve et de provenance nécessitent des types plus précis que
  les relations de simple route.
- La distinction des niveaux machine / technique / scientifique est conservable
  dans une architecture par objets autonomes.
- Les états antérieurs de blocage peuvent être reliés sans contaminer l'état
  courant.
- Les vues scientifique et computationnelle peuvent diverger sans dupliquer les
  objets canoniques.

## Tensions restantes

- C4 possède à la fois un contenu computationnel et un résultat de portée
  scientifique ; la transition entre ces niveaux doit rester explicitement
  qualifiée.
- C3 contient des chemins d'environnement local expurgés ou historiques ; la
  provenance doit être récupérable sans exposer des données privées.
- C2 dépend d'un ensemble de pièces N1-N5 dont la granularité peut être plus fine
  que celle des vues actuelles.
- C1 impose un gabarit commun tout en refusant l'homogénéisation artificielle ;
  cette règle elle-même est une relation méthodologique à conserver.

Ces tensions sont des points de conception, non des raisons de modifier les
résultats ou de relancer un calcul.

## Verdict local

```text
CONTRAT_COMPUTATIONNEL = TIENT_SUR_LE_LOT
RELATIONS_PROBATOIRES = DOIVENT_ETRE_TYPEES
DISTINCTION_MACHINE_TECHNIQUE_SCIENCE = CONSERVABLE
VUES_SCIENTIFIQUE_ET_COMPUTATIONNELLE = SEPARABLES
CALCUL_NOUVEAU = NON_LANCE
MIGRATION = NON_OUVERTE
PROCHAINE_ETAPE = COMPARER_CE_LOT_AU_CONTRAT_GENERAL
```

Le test renforce la recommandation d'un socle par objets autonomes et relations
explicites, tout en montrant que les relations computationnelles et probatoires
exigent un vocabulaire plus strict que les simples routes de lecture.
