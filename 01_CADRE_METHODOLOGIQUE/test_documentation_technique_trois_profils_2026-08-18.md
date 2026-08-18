# Test de documentation technique sur trois profils

## Fonction et statut

Artefact interne du cadrage de documentation technique. Il teste un contrat de
documentation sur trois profils existants sans réécrire leur code, leurs
résultats ou leurs chemins.

```text
LOT = PIPELINE_BORNE + SCRIPT_LOCAL + OUTIL_TRANSVERSAL
STATUT = TEST_A_QUALIFIER
CODE = INTACT
CALCUL_NOUVEAU = NON_LANCE
PUBLICATION = NON_DECIDEE
```

## Profils

| Profil | Objet | Fonction |
|---|---|---|
| **P1** | Pipeline T1.5 ALPHA documenté par manifeste et résultat | Reproduire le traitement de produits condensés dans un périmètre borné |
| **P2** | `02_CYCLES_PHYSIQUES/03_Cycle_neutrinos/01_REPRISE_COMPUTATIONNELLE_N1_N3/analyse_tension_n1_n3.py` | Analyse locale des planchers oscillatoires et d'une vraisemblance substitutive |
| **P3** | `tools/append_audit_changelog.py` | Outil transversal d'intégrité append-only des journaux Markdown |

## Contrat documentaire commun

Chaque profil doit être documenté par quatre fiches ou sections distinctes :

```text
CODE_ET_FONCTION
ENVIRONNEMENT_ET_ENTREES
EXECUTION_ET_SORTIES
QUALIFICATION_ET_LIMITES
```

Le contrat ne demande pas nécessairement quatre fichiers. Il demande que les
quatre fonctions restent identifiables et ne soient pas absorbées dans un
résumé unique.

## P1 — Pipeline T1.5 ALPHA

### Documentation technique à conserver

- manifeste de l'archive, de l'environnement Julia et des empreintes ;
- scripts d'entrée et ordre d'exécution ;
- données condensées effectivement utilisées ;
- sorties locales non versionnées ;
- étapes reproduites et étapes non reproduites ;
- absence d'identifiant de commit du paquet distant ;
- conditions de licence et de réutilisation non établies.

### Qualification à séparer

Le pipeline traite des produits condensés et reproduit les routes et leur
combinaison dans son périmètre. Il ne produit ni nouvelle simulation lattice,
ni mesure indépendante, ni validation générale de toutes les entrées. La
documentation technique rend cette limite visible ; elle ne la corrige pas.

## P2 — Script local N1-N3

### Documentation technique à conserver

- entrées et valeurs par défaut ;
- modèles de spectre et ordres NO / IO ;
- calculs de planchers et calibration de la vraisemblance substitutive ;
- dépendances Python (`numpy`, `scipy`) ;
- modes optionnels et conditions d'utilisation ;
- sorties attendues et erreurs possibles.

### Qualification à séparer

Le script annonce explicitement qu'il ne reproduit pas les chaînes DESI. Il
constitue une analyse locale bornée, avec un modèle substitutif et des données
publiées résumées. Le fait qu'il exécute un calcul correct dans son propre
modèle ne transforme pas ce modèle en analyse officielle ni en résultat
scientifique général.

## P3 — Outil transversal append-only

### Documentation technique à conserver

- arguments et préconditions ;
- vérification du chemin, de l'extension et de l'exclusion `data_external` ;
- contrôle SHA-256 et marqueur de fin ;
- écriture atomique, vérification du préfixe et read-back ;
- contrôle `git diff --check` ;
- comportement de refus et limites de l'outil.

### Qualification à séparer

L'outil établit qu'une opération d'ajout contrôlée a respecté ses garanties
techniques dans son périmètre. Il ne qualifie pas le contenu ajouté, la portée
scientifique du journal ou la décision qui a motivé l'ajout.

## Chaîne documentaire commune

```text
CODE_DOCUMENTE
-> EXECUTION_IDENTIFIEE
-> SORTIE_OBSERVEE
-> CONTROLE_TECHNIQUE
-> QUALIFICATION_BORNEE
-> RESULTAT_SCIENTIFIQUE_EVENTUEL
```

Chaque flèche est une transition à documenter, pas une implication automatique.
Le résultat scientifique éventuel doit renvoyer vers les sorties, contrôles et
limites sans les confondre.

## Test de niveau public

Les trois profils permettent de distinguer :

```text
DOCUMENTATION_VISIBLE = CE_QUE_LE_CODE_ET_LA_CHAINE_FONT
DOCUMENTATION_REPRODUCTIBLE = CE_QUI_PEUT_ETRE_REPRIS_DANS_UN_ENVIRONNEMENT_DECLARE
REUTILISATION = CE_QUI_EST_AUTORISE_ET_REALISTEMENT_PORTABLE
RESULTAT_PUBLIC = CE_QUI_EST_SOUTENU_DANS_UN_PERIMETRE_SCIENTIFIQUE_DECLARE
```

P1 n'est pas entièrement réutilisable sans son paquet et son environnement.
P2 est local et substitutif. P3 est transversal et techniquement contrôlable,
mais son usage est lié à la discipline des journaux et ne donne aucun statut au
contenu traité.

## Test de séparation avec le workflow global

Le CI peut automatiser certaines vérifications de P1, P2 et P3 : fichiers
présents, syntaxe, dépendances déclarées, tests, empreintes, liens ou formats.
Mais le workflow global conserve les décisions humaines :

- portée scientifique ;
- choix du modèle et des données ;
- distinction reproduction / analyse substitutive ;
- promotion d'un résultat ;
- publication ou partage d'un pipeline ;
- ouverture ou clôture d'une ligne de travail.

```text
CI = COMPOSANTE_TECHNIQUE_DU_WORKFLOW_GLOBAL
CI != WORKFLOW_GLOBAL_COMPLET
AUTOMATISATION = ALLEGEMENT_COGNITIF_SELECTIF
DECISION_HUMAINE = CONSERVEE
```

## Résultat local

Le contrat documentaire est applicable aux trois profils. Il montre que la
séparation technique / résultat n'implique pas l'isolement des deux : les
transitions doivent être reliées, mais chaque niveau conserve son rang.

```text
DOCUMENTATION_DES_TROIS_PROFILS = POSSIBLE
CODE_ET_RESULTAT = SEPARABLES_ET_RELIABLES
CI = UTILE_COMME_COMPOSANTE_DU_WORKFLOW_GLOBAL
AUTOMATISATION_TOTALE = NON_RECOMMANDEE
PUBLICATION_DE_PIPELINE = A_DECIDER_PAR_NIVEAU
MIGRATION = NON_OUVERTE
PROCHAINE_ETAPE = TESTER_UNE_FICHE_DOCUMENTAIRE_SUR_UN_SEUL_PROFIL
```

Le prochain test peut réduire le contrat sur un profil réel avant toute campagne
de documentation exhaustive.
