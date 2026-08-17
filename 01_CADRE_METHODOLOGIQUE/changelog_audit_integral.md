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
CORPUS_DE_REFERENCE_EXACT = A_ETABLIR_PAR_MANIFESTE
```

Les titres, README, routes vivantes, noms de fichiers, répertoires, catégories et statuts documentaires peuvent orienter la navigation. Ils ne peuvent pas servir à exclure un document avant lecture de son contenu.

## Exigence d’exhaustivité

Pour l’audit engagé sous ce programme :

```text
LECTURE_DOCUMENTAIRE_DU_CORPUS_DE_REFERENCE = EXHAUSTIVE
AUDIT_DE_SURFACE_COMME_SUBSTITUT = REFUSE
```

Chaque document du corpus de référence doit être lu intégralement avant d’être tenu pour sans effet sur les audits. Tant que le manifeste exact n’est pas établi, aucune pièce ne peut être exclue par pertinence supposée, catégorie, titre, rang, emplacement ou routage.

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

## Intégrité opérationnelle et signalement des incidents

Toute erreur rencontrée pendant une opération qui peut affecter l’état du dépôt ou la confiance dans cet état doit être signalée explicitement au moment où elle survient. Cela inclut notamment les erreurs d’API, de passerelle, de service, de CI, de persistance, de lecture après écriture ou toute réponse contradictoire d’un outil.

```text
INCIDENT_RENCONTRE -> SIGNALEMENT_HUMAIN_IMMEDIAT
ERREUR_5XX -> ETAT_DE_L_ECRITURE = INCONNU_JUSQU_A_RELECTURE
CONTOURNEMENT_REUSSI != INCIDENT_ANNULE
READ_BACK_CONFORME = NECESSAIRE_APRES_ETAT_AMBIGU
ETAT_CONTRADICTOIRE_OU_NON_RELISIBLE -> MUTATIONS_SUSPENDUES
```

Un incident n’est jamais contourné silencieusement. Si une autre voie technique permet ensuite d’obtenir l’état demandé, l’incident initial reste consigné avec son type, l’opération concernée, ce qui était connu ou inconnu au moment de l’erreur, le contrôle effectué ensuite et l’état finalement relu. Une cause racine ne doit pas être inventée à partir du seul code HTTP.

### Incident observé pendant la préparation de la PR #131

Le 17 août 2026, plusieurs opérations GitHub ont produit des erreurs intermittentes `502` lors de la création ou de la modification de la PR #131. Des lectures, écritures de fichiers, commentaires et exécutions CI ont par ailleurs réussi. Une modification du corps de la PR a échoué sur `502`, un no-op avec le même endpoint a réussi, une nouvelle modification a de nouveau échoué, puis la même modification a finalement réussi et a été relue conforme.

```text
INCIDENT_502_#131 = REPRODUIT_INTERMITTENT
CAUSE_RACINE = NON_ETABLIE
CORRUPTION_PR_#131 = NON_IDENTIFIEE
CORPS_ATTENDU_APRES_REPRISE = RELU_CONFORME
CONTOURNEMENT_SILENCIEUX = INTERDIT
```

L’auteur a également signalé avoir rencontré auparavant sur GitHub une erreur qu’il décrit approximativement comme « bad gateway / 503 ». Le code HTTP exact n’est pas établi à partir de son souvenir. La durée exacte n’est pas établie non plus ; la seule borne certaine rapportée est `moins de trois heures`.

```text
INCIDENT_UTILISATEUR_ANTERIEUR = SIGNALE
CODE_HTTP_EXACT = NON_ETABLI
DUREE_EXACTE = NON_ETABLIE
BORNE_DUREE_RAPPORTEE = MOINS_DE_TROIS_HEURES
IDENTITE_DE_CAUSE_AVEC_LES_502_#131 = NON_ETABLIE
```

### Incident pendant le contrôle substantiel de #131 et reprise observée

Pendant le contrôle substantiel de #131, deux tentatives consécutives d’ajout du commentaire de verdict ont renvoyé `502`. Après chaque erreur, une relecture de la conversation de PR a montré que le commentaire n’avait pas été persisté. Le seuil de suspension convenu a donc été appliqué et aucune promotion ni fusion n’a été tentée dans cet état.

L’auteur a ensuite redémarré son ordinateur et signalé que sa connexion Internet paraissait fonctionner normalement. Ce redémarrage constitue un événement local observé, mais aucun lien causal avec les erreurs GitHub n’est établi. Une nouvelle tentative d’écriture du même commentaire a ensuite réussi et sa relecture immédiate a confirmé sa persistance exacte.

```text
INCIDENT_502_COMMENTAIRE_CONTROLE_#131 = 2_ECHECS_CONSECUTIFS_NON_PERSISTES
SUSPENSION_DES_MUTATIONS = APPLIQUEE
REDEMARRAGE_LOCAL_UTILISATEUR = EFFECTUE
ECRITURE_TEST_APRES_REDEMARRAGE = SUCCES_RELUE_CONFORME
CAUSE_DU_RETABLISSEMENT = NON_ETABLIE
VOIE_D_ECRITURE = RETABLIE_PROVISOIREMENT
```

Si aucune récidive n’est observée au cours d’opérations ultérieures réellement représentatives, cet incident pourra être requalifié comme **incident transitoire historique non reproduit dans la suite observée**. Ce déclassement ne supprime pas sa trace, ne lui attribue aucune cause rétrospective et n’est pas déclenché par un délai arbitraire.

```text
DECLASSEMENT_INCIDENT = CONDITIONNEL
CRITERE = ABSENCE_DE_RECIDIVE_SUR_OPERATIONS_REPRESENTATIVES
EFFACEMENT_DE_L_INCIDENT = NON
CAUSE_RACINE_APRES_DECLASSEMENT = NON_ETABLIE
```

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
7. lorsqu’un incident d’intégrité opérationnelle survient ou est requalifié après vérification ;
8. avant toute réduction substantielle du corpus de travail fondée sur les lectures déjà effectuées.

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
INCIDENTS_D_INTEGRITE_OPERATIONNELLE
NON_ETABLI_OU_NON_DECIDABLE
EFFET_SUR_LES_AUDITS_EN_COURS = NON_ETABLI_PAR_DEFAUT
PROCHAINE_CONSEQUENCE_EVENTUELLE
```

Aucune rubrique n’est remplie par supposition. Une rubrique vide ou encore inconnue reste explicitement non établie lorsque son statut compte pour la suite.

## Corpus de référence initial

```text
BASELINE_GIT_MAIN = 5ff45189af7087e1dd384bb815be55c3ff1430db
DATE_DE_DECISION = 2026-08-17
MANIFESTE_EXHAUSTIF_DU_CORPUS_DE_REFERENCE = A_ETABLIR
NOMBRE_EXACT_DE_DOCUMENTS_DU_CORPUS = NON_ETABLI_A_CE_STADE
```

Le nombre exact n’est pas fixé ici à partir d’un décompte approximatif. Le manifeste exhaustif devra distinguer au moins les blobs versionnés, les documents lisibles, les sources binaires ou doublonnées, le code et les autres pièces dont l’équivalence éventuelle ne peut être présumée.

Aucune exclusion de catégorie ou de pertinence n’est autorisée avant lecture et remontée dans le changelog.

## État initial avant première investigation complète

### Décision de couverture

```text
AUDIT_DOCUMENTAIRE_EXHAUSTIF = DECIDE
LECTURE_INTEGRALE_AVANT_EXCLUSION = REQUISE
CORPUS_DE_REFERENCE_EXACT = A_ETABLIR_PAR_MANIFESTE
REDUCTION_PROGRESSIVE = AUTORISEE_APRES_REMONTEE
AUDITS_ANTERIEURS = CONSERVES_COMME_PREUVES_ET_HISTORIQUE
SUFFISANCE_CONTEXTUELLE_AUDITS_ANTERIEURS = NON_ETABLIE_PAR_DEFAUT
SIGNALEMENT_INCIDENTS_INTEGRITE = OBLIGATOIRE
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
ABSENCE_D_ELEMENT_PROFOND_NON_LU = NON_ETABLI
INVESTIGATION_COMPLETE_C6 = NON_EFFECTUEE_SOUS_CE_CHANGELOG
```

Le dernier point est essentiel : l’absence de surprise dans un inventaire n’autorise plus à conclure qu’une lecture exhaustive ne produira rien.

## Journal des investigations complètes

Aucune investigation complète de cycle n’est encore enregistrée sous ce changelog.

La première entrée sera créée après lecture intégrale du premier cycle choisi, avec manifeste de couverture et remontée de tous les éléments significatifs identifiés avant réduction éventuelle.
