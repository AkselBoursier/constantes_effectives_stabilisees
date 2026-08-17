# Changelog vivant de l’audit intégral

## Fonction et rang

Ce document est la mémoire de progression de l’audit intégral du projet.

Il ne remplace ni les documents scientifiques, ni les rapports locaux, ni les issues, ni `programme_audits.md`. Il enregistre ce qui a effectivement été lu, remonté, requalifié, laissé ouvert ou retrouvé au cours des audits afin qu’une réduction ultérieure du corpus ne dépende jamais d’un oubli ou d’un filtrage implicite.

Le présent changelog gouverne la **traçabilité de l’audit**. Il ne prétend décrire aucune règle de pensée de l’auteur.

## Principe de couverture

La trajectoire intellectuelle et documentaire du projet peut être non linéaire : bifurcations, migrations, renommages, absorptions partielles, dettes déplacées, résultats négatifs conservés loin de leur point d’origine, reprises computationnelles ou méthodologiques tardives.

En conséquence :

```text
TOPOLOGIE_DOCUMENTAIRE ~= TOPOLOGIE_INTELLECTUELLE = NON_PRESUME
RANG_APPARENT_D_UN_DOCUMENT -> IMPORTANCE_INTELLECTUELLE = NON_ETABLI
ROUTAGE_VIVANT -> EXHAUSTIVITE_DES_ACQUIS = NON_ETABLI
```

Les titres, README, routes vivantes, noms de fichiers, répertoires, catégories et statuts documentaires peuvent orienter la navigation. Ils ne peuvent pas servir à exclure un document avant lecture de son contenu.

## Exigence d’exhaustivité

Pour l’audit engagé sous ce programme :

```text
LECTURE_DOCUMENTAIRE_DU_CORPUS = EXHAUSTIVE
AUDIT_DE_SURFACE_COMME_SUBSTITUT = REFUSE
```

Chaque document du corpus auditable doit être lu intégralement avant d’être tenu pour sans effet sur les audits.

Cette exigence de lecture exhaustive ne signifie pas :

- refaire chaque calcul ;
- revérifier automatiquement chaque valeur contre la littérature ;
- réexécuter chaque script ;
- réauditer scientifiquement en profondeur chaque résultat ;
- donner le même poids à chaque document.

Elle signifie qu’aucune décision de non-pertinence, de redondance, de portée ou d’exclusion substantielle ne peut reposer uniquement sur la surface documentaire.

## Audits antérieurs : faits conservés, suffisance contextuelle non présumée

Les audits déjà effectués restent des faits historiques et leurs preuves locales ne sont ni annulées ni déclassées par principe.

Cependant, une partie de ces audits a été menée par des agents qui ne disposaient pas nécessairement de l’ensemble du contexte aujourd’hui jugé pertinent. Leur existence ne permet donc pas de présumer que leur périmètre, leurs exclusions ou leurs conclusions sont suffisants pour le présent programme.

```text
AUDIT_ANTERIEUR_EFFECTUE = FAIT_HISTORIQUE_CONSERVE
PREUVES_LOCALES_ANTERIEURES = A_CONSERVER
SUFFISANCE_CONTEXTUELLE_POUR_LE_PRESENT_PROGRAMME = NON_ETABLIE_PAR_DEFAUT
RE_AUDIT_AUTOMATIQUE_DE_TOUT = NON
```

La lecture exhaustive doit permettre, pour chaque audit antérieur rencontré, de déterminer si le contexte nouvellement remonté :

- ne change rien à sa conclusion ni à sa portée ;
- exige seulement une recontextualisation ou une réduction de portée ;
- fait apparaître une prémisse, une exclusion ou une dépendance non testée ;
- justifie alors un réaudit substantiel ciblé.

L’absence de contexte complet chez un agent antérieur n’est donc ni une invalidation automatique, ni une autorisation de conserver son verdict intact. Son effet doit être établi cas par cas à partir des contenus effectivement remontés.

## Réduction progressive autorisée

La réduction du corpus de travail devient légitime **après** remontée du contenu, jamais avant.

Un document déjà lu peut sortir du corpus de lecture active ultérieure si le changelog conserve suffisamment pour savoir :

```text
DOCUMENT_LU = OUI
FONCTION_IDENTIFIEE = ...
CONTENU_UNIQUE_REMONTE = ...
RESULTAT_OU_DETTE_REMONTE = ...
DEPENDANCES_IDENTIFIEES = ...
RAISON_DE_NON_RELECTURE_ULTERIEURE = ...
CONDITION_DE_REOUVERTURE = ...
```

Cette réduction ne supprime ni le document ni sa récupérabilité. Elle ne signifie pas que son contenu est définitivement sans importance.

## Obligation de mise à jour

Le changelog doit être mis à jour au minimum :

1. après l’investigation complète de chaque cycle physique ;
2. lorsqu’un élément nouveau ou ancien resurgit et modifie, précise ou contredit une entrée précédente ;
3. lorsqu’une dette change de statut ou d’effet ;
4. lorsqu’un résultat négatif, une bifurcation, un arbitrage ou une fonction intellectuelle jusque-là non remontée devient visible ;
5. lorsqu’une relation entre deux parties du corpus est établie, réfutée ou requalifiée ;
6. lorsqu’un contenu nouvellement remonté modifie la suffisance contextuelle attribuable à un audit antérieur ;
7. avant toute réduction substantielle du corpus de travail fondée sur les lectures déjà effectuées.

Une mise à jour peut agréger plusieurs découvertes d’une même investigation, mais elle ne doit pas laisser une nouveauté significative hors registre jusqu’à la fin générale de l’audit.

## Unité minimale d’une entrée

Chaque entrée d’investigation doit permettre de retrouver au minimum :

```text
DATE_OU_ORDRE
PERIMETRE_LU
COUVERTURE = COMPLETE / INCOMPLETE
DOCUMENTS_LUS_OU_MANIFESTE_DE_COUVERTURE
ACQUIS_POSITIFS_REMONTEES
RESULTATS_NEGATIFS_OU_LIMITES_REMONTEES
DETTES_REMONTEES
CONTRADICTIONS_OU_TENSIONS
BIFURCATIONS_MIGRATIONS_RENOMMAGES
ELEMENTS_RESURGIS
RELATIONS_A_D_AUTRES_CYCLES_OU_COUCHES
AUDITS_ANTERIEURS_RENCONTRES_ET_EFFET_DU_CONTEXTE_NOUVEAU
NON_ETABLI_OU_NON_DECIDABLE
EFFET_SUR_LES_AUDITS_EN_COURS = NON_ETABLI_PAR_DEFAUT
PROCHAINE_CONSEQUENCE_EVENTUELLE
```

Aucune rubrique n’est remplie par supposition. Une rubrique vide ou encore inconnue reste explicitement non établie lorsque son statut compte pour la suite.

## Corpus de référence initial

```text
BASELINE_GIT_MAIN = 5ff45189af7087e1dd384bb815be55c3ff1430db
DATE_DE_DECISION = 2026-08-17
MANIFESTE_EXHAUSTIF_DU_CORPUS_AUDITABLE = A_ETABLIR
NOMBRE_EXACT_DE_DOCUMENTS_AUDITABLES = NON_ETABLI_A_CE_STADE
```

Le nombre exact n’est pas fixé ici à partir d’un décompte approximatif. Le manifeste exhaustif devra distinguer au moins les blobs versionnés, les documents lisibles, les sources binaires ou doublonnées, le code et les autres pièces dont l’équivalence éventuelle ne peut être présumée.

Aucune exclusion de catégorie n’est autorisée avant cette qualification du corpus.

## État initial avant première investigation complète

### Décision de couverture

```text
AUDIT_DOCUMENTAIRE_EXHAUSTIF = DECIDE
LECTURE_INTEGRALE_AVANT_EXCLUSION = REQUISE
REDUCTION_PROGRESSIVE = AUTORISEE_APRES_REMONTEE
AUDITS_ANTERIEURS = CONSERVES_COMME_PREUVES_ET_HISTORIQUE
SUFFISANCE_CONTEXTUELLE_AUDITS_ANTERIEURS = NON_ETABLIE_PAR_DEFAUT
AUDIT_SCIENTIFIQUE_SUBSTANTIEL = NON_OUVERT_A_CE_STADE
```

### Éléments déjà apparus pendant le contrôle du cadrage

Ces éléments ne valent pas investigation complète de leurs cycles. Ils sont conservés comme signaux déjà reproduits qui ont contribué à justifier l’exigence de couverture intégrale.

#### Cycle 7 — reprise computationnelle C7-C1

Le routage vivant actuel existe bien du README du cycle vers `01_REPRISE_COMPUTATIONNELLE_C7_C1/README.md`, puis vers l’issue #119. Cependant, l’inventaire du sous-dossier a fait apparaître des rapports tels que `REJ-1`, `SENT-0A/B`, `SENT-0D`, `CAP-1` et plusieurs rapports G2.4 dont certaines fonctions méthodologiques et incidents ne sont pas exposés par le seul résumé du README.

Signal conservé :

```text
ROUTAGE_COURANT = PRESENT
ROUTAGE_COURANT_COMME_SUBSTITUT_A_LA_LECTURE = INSUFFISANT
INVESTIGATION_COMPLETE_C7 = NON_EFFECTUEE_SOUS_CE_CHANGELOG
```

#### Cycle 3 — neutrinos

L’inventaire du dossier a fait apparaître `01_REPRISE_COMPUTATIONNELLE_N1_N3`, contenant notamment des résultats de reconstruction de planchers et d’ingestion de produits DESI DR2 qui ne sont pas réductibles au simple ensemble N0–N5 annoncé par la synthèse scientifique comme base principale.

Signal conservé :

```text
SOUS_DOSSIER_COMPUTATIONNEL_POTENTIELLEMENT_DECISIF = IDENTIFIE
PORTEE_DANS_L_AUDIT_GLOBAL = NON_ETABLIE
INVESTIGATION_COMPLETE_C3 = NON_EFFECTUEE_SOUS_CE_CHANGELOG
```

#### Cycle 6 — basse énergie

L’inventaire de surface reproduit un cas où les principales pièces visibles correspondent davantage au routage déjà attendu : sources historiques, synthèses, architecture, vérification et évaluation.

Signal conservé :

```text
GAIN_DE_L_INVENTAIRE_INITIAL = FAIBLE_DANS_CE_CAS
ABSENCE_D_ELEMENT_PROFOND_NON_LU = NON_ETABLIE
INVESTIGATION_COMPLETE_C6 = NON_EFFECTUEE_SOUS_CE_CHANGELOG
```

Le dernier point est essentiel : l’absence de surprise dans un inventaire n’autorise plus à conclure qu’une lecture exhaustive ne produira rien.

## Journal des investigations complètes

Aucune investigation complète de cycle n’est encore enregistrée sous ce changelog.

La première entrée sera créée après lecture intégrale du premier cycle choisi, avec manifeste de couverture et remontée de tous les éléments significatifs identifiés avant réduction éventuelle.
