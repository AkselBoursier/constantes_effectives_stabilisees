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
CORPUS_DE_REFERENCE_EXACT = ETABLI_PAR_MANIFESTE_GIT_BASELINE
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

### Incident réseau local pendant la lecture exhaustive

Le 17 août 2026, les tentatives d’accès local à `github.com` depuis l’environnement d’exécution de l’agent ont échoué avec une erreur de résolution DNS (`Could not resolve host` / `Temporary failure in name resolution`). Le connecteur GitHub est resté fonctionnel et a permis de poursuivre les lectures du dépôt.

L’auteur a diagnostiqué localement, avec GitHub Copilot, un rôle possible de son VPN et a constaté un rétablissement sur sa propre machine après déconnexion. Une nouvelle vérification dans l’environnement d’exécution de l’agent a toutefois continué d’échouer. Les deux environnements ne doivent donc pas être assimilés et aucune cause racine commune n’est établie.

```text
INCIDENT_DNS_CONTENEUR_LOCAL = REPRODUIT
ACCES_GITHUB_PAR_CONNECTEUR = FONCTIONNEL
ETAT_DISTANT_AMBIGU = NON
CAUSE_RACINE = NON_ETABLIE
VPN_UTILISATEUR_COMME_CAUSE_DU_CONTENEUR = NON_ETABLI
EFFET = LIMITATION_DE_LA_VOIE_LOCALE_SANS_BLOCAGE_DE_LA_LECTURE_CONNECTEUR
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

## Portée de la lecture seule

Clarification ajoutée le 17 août 2026 après explicitation humaine : la règle de **lecture seule** concerne les objets audités et les objets servant de preuves pendant leur investigation. Elle interdit de modifier ces objets pour les rendre plus cohérents, plus lisibles ou plus conformes pendant qu’ils sont justement en train d’être lus et qualifiés.

Elle ne s’applique pas au présent changelog. Le changelog est un instrument de traçabilité de l’audit et doit pouvoir être écrit au fil de la lecture lorsque les conditions de mise à jour ci-dessus sont remplies. Son écriture ne constitue pas une mutation de l’objet audité ; elle constitue l’enregistrement séparé de ce que l’audit a effectivement établi.

```text
OBJETS_AUDITES_PENDANT_INVESTIGATION = READ_ONLY_PAR_DEFAUT
SOURCES_PREUVES_ET_ARTEFACTS_LUS = NE_PAS_MODIFIER_PENDANT_QUALIFICATION
CHANGELOG_AUDIT_INTEGRAL = ECRITURE_AUTORISEE_ET_REQUISE
LECTURE_SEULE_DES_OBJETS_AUDITES -> GEL_DU_CHANGELOG = FAUX
DECOUVERTE_SIGNIFICATIVE -> INSCRIPTION_CHANGELOG_SANS_ATTENDRE_LA_CLOTURE_GENERALE
```

Cette clarification corrige une ambiguïté opératoire rencontrée pendant les cycles 1 et 2 : l’incomplétude documentaire due aux DOCX non lus ne devait pas empêcher l’inscription immédiate des remontées significatives déjà établies dans les pièces effectivement lues.

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
MANIFESTE_EXHAUSTIF_DU_CORPUS_DE_REFERENCE = ETABLI
NOMBRE_EXACT_BLOBS_GIT_DU_CORPUS = 668
CHEMINS_DUPLIQUES = 0
FICHIERS_NON_CLASSES_MATERIELLEMENT = 0
EQUIVALENCE_DOCX_MD = NON_ETABLIE
```

Le manifeste compte les blobs versionnés, non les répertoires. Chaque chemin de blob est une pièce distincte ; aucune déduplication n’est effectuée sur la seule similarité des noms, formats ou contenus supposés. Les sources binaires, extractions textuelles, code, données structurées, images et autres pièces restent dans le périmètre documentaire.

Répartition matérielle globale établie :

```text
.md = 525
.docx = 62
.py = 29
.csv = 11
.json = 10
.yaml + .yml = 10
.png = 8
.txt = 4
.ots = 2
autres extensions unitaires = 7
TOTAL = 668
```

Aucune exclusion de catégorie ou de pertinence n’est autorisée avant lecture et remontée dans le changelog.

## État initial avant première investigation complète

### Décision de couverture

L’état ci-dessous conserve la décision initiale au moment de l’ouverture de la procédure. Le manifeste ayant depuis été établi, la ligne `CORPUS_DE_REFERENCE_EXACT = A_ETABLIR_PAR_MANIFESTE` est historique et ne décrit plus l’état courant.

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

## Journal des investigations

Aucune investigation complète de cycle n’est encore enregistrée : les cycles 1 et 2 ont une couverture textuelle exhaustive mais restent matériellement incomplets tant que leurs DOCX originaux ne sont pas lus directement. Le cycle 3 est en cours.

### 2026-08-17 — Manifeste exhaustif du baseline

```text
PERIMETRE = baseline 5ff45189af7087e1dd384bb815be55c3ff1430db
COUVERTURE_MANIFESTE = COMPLETE
NOMBRE_EXACT_BLOBS_GIT = 668
CHEMINS_DUPLIQUES = 0
CLASSIFICATION_MATERIELLE_MINIMALE = ETABLIE
PERTINENCE_INTELLECTUELLE = NON_QUALIFIEE_PAR_LE_MANIFESTE
```

Le manifeste ferme l’ancienne approximation numérique du corpus. Il établit le périmètre matériel sans transformer la classification par extension ou format en filtre intellectuel.

### 2026-08-17 — Cycle 1, couplages, échelles et QCD — remontée documentaire partielle

```text
PERIMETRE = 49 blobs
MARKDOWN = 44
DOCX = 5
MARKDOWN_LUS_INTEGRALEMENT = 44/44
DOCX_LUS_DIRECTEMENT = 0/5
EXTRACTIONS_DOCX_LUES = 5/5
COUVERTURE = INCOMPLETE
EQUIVALENCE_DOCX_EXTRACTION_MD = NON_ETABLIE
```

Acquis et trajectoires remontés :

- le dossier `alpha` sépare explicitement valeur recommandée de basse énergie, running avec l’échelle, variation temporelle et variation spatiale/cosmologique ;
- la discordance des chaînes de détermination de basse énergie n’est pas convertie en variation physique de `alpha` ; cohérence nominale, cohérence opérationnelle après expansion CODATA, équivalence des chaînes et convergence causale restent distinguées ;
- la trajectoire spatiale est conservée comme prétention statistique historique, puis repondération par systématique instrumentale, puis contrainte locale mieux calibrée, sans conversion en réfutation universelle ;
- le blocage historique de reproduction ALPHA est conservé comme obstacle d’environnement avant levée ultérieure, et la reproduction reste qualifiée comme aval à partir de produits condensés ;
- la dette `m_e` a été transférée vers Saveur–Higgs avec conditions de réouverture, et non supprimée.

Limites et dettes : les cinq DOCX originaux restent à lire directement ; les extractions déclarent elles-mêmes ne pas remplacer les originaux et peuvent dégrader équations, tableaux ou graphiques. Aucun verdict scientifique nouveau n’est émis par la présente remontée.

### 2026-08-17 — Cycle 2, structuration électrofaible — remontée documentaire partielle

```text
PERIMETRE = 11 blobs
MARKDOWN = 6
TXT = 1
DOCX = 4
PIECES_TEXTUELLES_LUES_INTEGRALEMENT = 7/7
DOCX_LUS_DIRECTEMENT = 0/4
COUVERTURE = INCOMPLETE
```

Acquis et trajectoires remontés :

- la synthèse initiale proposait une taxonomie fonctionnelle forte : régime générateur, différenciation fermionique, hiérarchie d’échelle, raccordement effectif, mélange de jauge et fond cosmologique ;
- la synthèse de récupération ultérieure ne restaure pas cette taxonomie comme classification active ; elle récupère surtout la distinction entre fonction, relation, explication de valeur et mécanisme ;
- l’unité du cycle est requalifiée comme comparative et généalogique, non comme secteur physique homogène ;
- plusieurs objets ont migré vers Saveur–Higgs, basse énergie et cosmologie ; la redistribution est traitée comme bifurcation documentaire, non comme annulation du cycle ;
- aucune « stabilité électrofaible » ni « résultat négatif » global sur la stabilité du régime n’est récupéré comme verdict du cycle.

Limites et dettes : quatre DOCX originaux restent non lus directement ; `G_F`, `theta_W` et `Lambda` restent explicitement à vérifier scientifiquement depuis leurs sources primaires lors de l’audit substantiel approprié.

### 2026-08-17 — Cycle 3, neutrinos — investigation en cours

```text
PERIMETRE = 42 blobs
00_SOURCES_DOCX = 12 blobs = 6 DOCX + 6 Markdown
RACINE_ACTIVE = 8 Markdown
REPRISE_COMPUTATIONNELLE_N1_N3 = 22 blobs
COUVERTURE = EN_COURS
```

Éléments déjà remontés avant clôture du cycle :

- la synthèse de récupération décrit le secteur comme reconstruction par accès non équivalents et conserve une structure d’incomplétude contrôlée ;
- la synthèse active ultérieure porte un verdict scientifique de cycle distinct et localise une tension N1–N3 sous `LambdaCDM` sans l’ériger en contradiction modèle-indépendante ;
- la reprise computationnelle contient une généalogie C1 substitutive puis C2 contrôlée ; C1 se déclare explicitement non-reproduction des chaînes officielles ;
- C2 distingue `base_mnu`, `base_mnu059`, `base_mnu_binary_3` et `base_mnu_w_wa`, interdit leur substitution et sépare quantiles empiriques, `margestats`, maxima ponctuels et profils ;
- l’ingestion locale ultérieure reproduit trois ensembles distribués au niveau des chaînes et conserve `base_mnu_binary_3` comme absent de la distribution vérifiée, sans généraliser cette absence à toute distribution officielle ;
- le code versionné contient les garde-fous annoncés : absence explicite, contrôle des poids et colonnes, distinction des produits `iminuit`, et code de sortie bloquant sauf autorisation explicite de l’absence.

Cette entrée est provisoire. Elle doit être complétée après lecture de N0–N5, des sources historiques, des JSON/CSV/manifeste/checksum restants et qualification des six DOCX originaux.

## Compléments de procédure et de traçabilité — 2026-08-17

### Les règles restent arbitrables ; les exceptions ne sont pas silencieuses

L’auteur précise qu’une règle de l’audit peut révéler, au contact du corpus, un cas limite, une absurdité locale ou une rigidité excessive. Une nouvelle règle peut également devenir nécessaire. Ces événements ne doivent ni être ignorés ni produire une exception improvisée silencieusement.

```text
REGLE_EXISTANTE = GARDE_FOU_REVISABLE_SOUS_ARBITRAGE
REGLE_APPAREMMENT_ABSURDE_OU_TROP_BORNEE -> FAIRE_REMONTER_LE_CONFLIT_CONCRET
EXCEPTION_NOUVELLE -> NE_PAS_L_APPLIQUER_SILENCIEUSEMENT
ARBITRAGE_HUMAIN_AGENT = REQUIS_AVANT_REQUALIFICATION_DE_LA_REGLE
NOUVELLE_REGLE_POTENTIELLE -> VERIFIER_D_ABORD_NON_REDONDANCE_AVEC_REGLES_EXISTANTES
NOUVELLE_REGLE_NON_REDONDANTE_ET_ADOPTEE -> CONSIGNER_DANS_CHANGELOG
```

Le but n’est donc pas d’accumuler des prescriptions, mais de conserver des garde-fous suffisamment précis pour être utiles sans les transformer en contraintes aveugles. Lorsqu’un conflit de règles ou un cas limite survient, l’agent doit exposer ce qui coince, l’effet concret sur l’audit et les options d’arbitrage, plutôt que de forcer l’une des règles en silence.

### Incident de sélection d’outil pendant l’inventaire des cycles 1 et 2

Pendant la préparation de l’inventaire nominatif, l’agent a sélectionné à tort à plusieurs reprises l’action GitHub `create_tree` alors qu’une lecture d’arbre était recherchée. Trois appels exécutés ont renvoyé `422 Invalid tree info`. Une quatrième sélection a été bloquée avant exécution par la couche de sécurité de l’outil. Aucun appel `create_tree` n’a renvoyé de succès ; aucune branche ni aucun fichier n’a été modifié par cette séquence. La voie a ensuite été abandonnée au profit d’une lecture générique GitHub et du manifeste local déjà établi.

```text
INCIDENT_SELECTION_OUTIL_CREATE_TREE = OUI
APPELS_EXECUTES_REPONSE_422 = 3
SELECTION_BLOQUEE_AVANT_EXECUTION = 1
SUCCES_CREATE_TREE = 0
MUTATION_FICHIER_OU_BRANCHE_IDENTIFIEE = NON
CAUSE = ERREUR_DE_SELECTION_OUTIL_AGENT
EFFET_SCIENTIFIQUE = AUCUN_ETABLI
CORRECTION = RECHARGEMENT_EXPLICITE_DES_ACTIONS_DE_LECTURE
```

Une nouvelle vérification locale de `github.com` dans l’environnement d’exécution de l’agent a par ailleurs reproduit l’échec DNS déjà consigné. Le connecteur GitHub restant fonctionnel, cela ne change pas le statut scientifique ou documentaire ; cela confirme seulement que la voie locale directe reste indisponible à ce stade.

### Inventaire exact enregistré — Cycle 1

L’inventaire nominatif ci-dessous provient du manifeste exact du baseline `5ff45189af7087e1dd384bb815be55c3ff1430db`. Il complète le décompte déjà enregistré ; il n’ajoute aucun verdict de pertinence.

```text
00_Sources_docx/Fiche alpha_s - Lambda_QCD.docx
00_Sources_docx/Fiche masse de l'électron.docx
00_Sources_docx/Fiche rapport proton-électron.docx
00_Sources_docx/Fiche α v0.1.docx
00_Sources_docx/Source_docx_Fiche_alpha_s_Lambda_QCD_v0_1.md
00_Sources_docx/Source_docx_Fiche_alpha_v0_1.md
00_Sources_docx/Source_docx_Fiche_masse_electron_v0_1.md
00_Sources_docx/Source_docx_Fiche_rapport_proton_electron_v0_1.md
00_Sources_docx/Source_docx_Synthese_premier_cycle_v0_1.md
00_Sources_docx/Synthèse du premier cycle v0.1.docx
A1_Matrice_cibles_transformations_acces_alpha_v0_1.md
A1_Registre_sources_versions_alpha_v0_1.md
A2_Extraction_CODATA_alpha_v0_1.md
A2_Fiche_voie_cesium_alpha_v0_1.md
A2_Fiche_voie_gmoins2_alpha_v0_1.md
A2_Fiche_voie_rubidium_alpha_v0_1.md
A2_Matrice_chaines_determination_alpha_v0_1.md
A2_Matrice_comparative_trois_chaines_alpha_v0_2.md
A2_Verdict_comparatif_local_alpha_v0_1.md
A3_Fiche_running_alpha_Q2_v0_1.md
A3_Verdict_local_running_alpha_v0_1.md
A4_Fiche_contraintes_temporelles_alpha_v0_1.md
A4_Verdict_local_contraintes_temporelles_alpha_v0_1.md
A5_Fiche_variations_spatiales_cosmologiques_alpha_v0_1.md
A5_Verdict_local_variations_spatiales_alpha_v0_1.md
Cadrage_reprise_scientifique_cycle_1_QCD_T1_v0_1.md
D5_Arbitrage_prochaine_dette_me_rapport_proton_electron_v0_1.md
D6_Transfert_dette_me_vers_Saveur_Higgs_v0_1.md
R1_Cible_determinations_rapport_proton_electron_v0_1.md
R2_Acces_variation_rapport_proton_electron_v0_1.md
R3_Constitution_minimale_et_verdict_rapport_proton_electron_v0_1.md
Synthese_active_cycle_1_cloture_premier_perimetre_apres_D6_v0_5.md
Synthese_active_cycle_1_couplages_echelles_QCD_apres_T1_v0_2.md
Synthese_active_cycle_1_couplages_echelles_QCD_apres_alpha_v0_3.md
Synthese_active_cycle_1_couplages_echelles_QCD_apres_rapport_proton_electron_v0_4.md
Synthese_finale_dossier_alpha_v0_1.md
Synthese_recuperation_cycle_1_couplages_echelles_QCD_v0_1.md
T1_1_Registre_sources_versions_alpha_s_v0_1.md
T1_2_Fiche_extraction_alpha_s_NNPDF_global_v0_1.md
T1_2_Fiche_extraction_alpha_s_formes_evenements_v0_1.md
T1_2_Fiche_extraction_alpha_s_tau_Belle_v0_1.md
T1_3_Fiche_extraction_alpha_s_lattice_ALPHA_2026_v0_1.md
T1_3_Selection_chaine_lattice_primaire_v0_1.md
T1_4_Matrice_comparabilite_chaines_alpha_s_v0_1.md
T1_5_Manifeste_local_paquet_ALPHA_2026_v0_1.md
T1_5_Rapport_blocage_reproduction_lattice_ALPHA_2026_v0_1.md
T1_5_Resultats_reproduction_lattice_ALPHA_2026_v0_1.md
T1_6_Classification_ecarts_chaines_alpha_s_v0_1.md
T1_7_Verdict_physique_local_alpha_s_v0_1.md
```

```text
INVENTAIRE_NOMINATIF_CYCLE_1 = 49/49_BLOBS_ENREGISTRES
COUVERTURE_TEXTUELLE = 44/44_MARKDOWN_LUS
DETTE_BINAIRE = 5_DOCX_ORIGINAUX_NON_LUS_DIRECTEMENT
```

### Inventaire exact enregistré — Cycle 2

```text
00_Sources_docx/Fiche -(-theta_W-) v0.1.docx
00_Sources_docx/Fiche G_F v0.1.docx
00_Sources_docx/Fiche Lambda v0.1.docx
00_Sources_docx/Source_docx_Fiche_G_F_v0_1.md
00_Sources_docx/Source_docx_Fiche_Lambda_v0_1.md
00_Sources_docx/Source_docx_Fiche_theta_W_v0_1.md
00_Sources_docx/Source_docx_Synthese_second_cycle_v0_1.md
00_Sources_docx/Source_txt_Ecriture_Lambda_v0_1.md
00_Sources_docx/Synthèse du second cycle v0.1.docx
00_Sources_docx/Écriture.txt
Synthese_recuperation_cycle_2_structuration_electrofaible_v0_1.md
```

```text
INVENTAIRE_NOMINATIF_CYCLE_2 = 11/11_BLOBS_ENREGISTRES
COUVERTURE_TEXTUELLE = 7/7_PIECES_TEXTUELLES_LUES
DETTE_BINAIRE = 4_DOCX_ORIGINAUX_NON_LUS_DIRECTEMENT
```

### Cycle 3 — sous-dossier computationnel intégralement lu

Depuis l’entrée provisoire précédente, tous les artefacts versionnés de `01_REPRISE_COMPUTATIONNELLE_N1_N3` ont été lus documentairement : six Markdown, deux scripts Python, huit CSV, quatre JSON, un TXT et un manifeste SHA-256, soit `22/22` blobs.

```text
REPRISE_COMPUTATIONNELLE_N1_N3 = 22/22_BLOBS_LUS_INTEGRALEMENT
MARKDOWN = 6/6
PYTHON = 2/2
CSV = 8/8
JSON = 4/4
TXT = 1/1
SHA256 = 1/1
EXECUTION_NOUVELLE_PAR_L_AUDIT = NON
RECALCUL_INDEPENDANT_DES_CHECKSUMS_EXTERNES = NON
```

La généalogie computationnelle récupérée doit rester hiérarchisée :

- C1 est un diagnostic substitutif explicitement déclaré comme non-reproduction des chaînes officielles ; ses planchers et son surrogate ne deviennent donc pas une validation DESI ;
- C2 correspond à une ingestion locale contrôlée de la distribution effectivement inspectée, avec interdiction de substituer des modèles voisins et séparation entre quantiles empiriques, `margestats`, points `bestfit` et profils ;
- trois ensembles (`base_mnu`, `base_mnu059`, `base_mnu_w_wa`) ont des sorties versionnées ; `base_mnu_binary_3` est absent de la distribution vérifiée et cette absence n’est pas généralisée au-delà de ce périmètre ;
- les produits `iminuit` disponibles ne permettent pas de reconstruire un profil exact dans les cas documentés ; aucun produit voisin n’est substitué ;
- les sommes de contrôle présentes dans le dépôt sont des sorties historiques versionnées. Les octets bruts externes des chaînes DESI ne font pas partie des 668 blobs du baseline et n’ont pas été récupérés ni rehachés par le présent audit.

Sorties machine historiques lues, sans réexécution ni requalification scientifique nouvelle :

```text
base_mnu: q95_empirique = 0.06493418275 ; margestats = 0.0642 ; R-1_dernier = 0.0091471859
base_mnu059: q95_empirique = 0.1048620874 ; margestats = 0.105 ; R-1_dernier = 0.0083615890
base_mnu_w_wa: q95_empirique = 0.16390456636 ; margestats = 0.163 ; R-1_dernier = 0.0066957914
base_mnu_binary_3: not_available_in_verified_distribution
```

Ces écarts entre quantile empirique et `margestats` sont documentés comme différences de convention/statistique dans les artefacts ; ils ne sont pas transformés ici en divergence scientifique. La lecture du code confirme seulement que les garde-fous annoncés existent dans le code versionné ; elle ne vaut pas preuve d’une exécution nouvelle.

Le statut global du cycle 3 reste **EN COURS** : N0–N5 doivent encore être lus intégralement, les six extractions Markdown historiques doivent être lues, et les six DOCX originaux restent une dette binaire tant qu’ils ne sont pas accessibles directement.

### Cycle 3 — couche active N0–N5 intégralement lue

Les six pièces `N0` à `N5` ont maintenant été lues intégralement au baseline. Avec les deux synthèses de racine déjà lues, la couche active du cycle est couverte à `8/8` Markdown.

```text
N0_N5 = 6/6_LUS_INTEGRALEMENT
SYNTHESES_RACINE = 2/2_LUES_INTEGRALEMENT
RACINE_ACTIVE_CYCLE_3 = 8/8_MARKDOWN_LUS
COUVERTURE_CYCLE_3_GLOBALE = TOUJOURS_INCOMPLETE
```

Résultats structurants remontés :

- `N0` définit comme unité de comparaison un **énoncé empirique situé avec sa chaîne d’accès**, et prévoit explicitement la révision du gabarit s’il homogénéise des opérations physiquement distinctes. Cette clause est compatible avec la règle générale d’arbitrage des règles déjà consignée ; elle ne nécessite pas à ce stade une règle supplémentaire distincte.
- `N1` établit la différence entre architecture différentielle du spectre et ancrage absolu. Les oscillations contraignent les écarts de masses, le mélange et des phases sous le cadre à trois saveurs, mais restent invariantes sous translation commune des `m_i^2`. L’ajustement global est qualifié comme **inférence de second niveau**, non comme instrument unique.
- `N2` précise le sens borné de « direct » : la cinématique bêta est locale et indépendante de la cosmologie, mais elle dépend d’un modèle de désintégration, de la réponse instrumentale et d’une construction statistique. La différence entre la limite directrice Lokhov–Tkachov et le contrôle Feldman–Cousins illustre que la règle d’intervalle à la frontière fait partie de l’énoncé.
- `N3` sépare deux sources physiques de sensibilité cosmologique : **expansion** et **libre parcours/croissance**. La borne `0.0642 eV` sous `LambdaCDM`, la construction fréquentiste `0.053 eV` et l’élargissement à `0.163 eV` sous `w_0w_aCDM` sont des énoncés différents. La tension N1–N3 est explicitement localisée dans un réseau `données + likelihoods + modèle + priors + frontière`, et non attribuée comme propriété intrinsèque du neutrino.
- `N4` sépare trois niveaux : absence de pic, borne de demi-vie isotopique, puis borne conditionnelle sur `m_beta_beta` après ajout du mécanisme et de la physique nucléaire. Une non-détection ne tranche pas Dirac contre Majorana.
- `N5` remplace la formulation trop lâche « plusieurs accès à la masse absolue » par **plusieurs fonctions non équivalentes d’un spectre de masses, coordonnées par un modèle commun et des hypothèses propres à chaque voie**. Aucune paire ne fournit de contradiction modèle-indépendante ; la seule tension quantitative saillante est N1–N3 sous le modèle cosmologique de base.

La matrice N5 affirme une transférabilité du gabarit vers les architectures d’extraction du cycle 1 et les chaînes reconstructives du cycle 7, mais elle en borne elle-même la portée : ce schéma n’est pas une théorie générale de la mesure et doit être adapté localement. Cette transférabilité est donc un **signal à tester**, non une autorisation de requalifier les cycles 1 ou 7 avant leur propre audit exhaustif.

### Requalification de dettes du cycle 3 par croisement N3/N5 ↔ reprise computationnelle ultérieure

La lecture croisée de N3/N5 et du sous-dossier computationnel, postérieur dans la généalogie documentaire, modifie le statut de certaines dettes sans ouvrir de nouveau calcul :

```text
DETTE_LIRE_CHAINES_DESI_ET_REPRODUIRE_QUANTILES = PARTIELLEMENT_TRAITEE_HISTORIQUEMENT
DETTE_QUANTILES_BASE_MNU_BASE_MNU059_W_WA = SORTIES_VERSIONNEES_PRESENTES
BASE_MNU_BINARY_3 = ABSENTE_DE_LA_DISTRIBUTION_VERIFIEE_SANS_GENERALISATION
DETTE_PROFILS_FREQUENTISTES_EXACTS = OUVERTE
DETTE_REPRODUCTION_NUFIT_6_1 = OUVERTE
DETTE_REPRODUCTION_KATRIN = OUVERTE
DETTE_COMBINAISON_MULTI_ISOTOPES_NME = OUVERTE
```

Cette requalification est documentaire : le présent audit n’a pas réexécuté les chaînes DESI externes. Il établit seulement que la dette formulée dans N3/N5 a fait l’objet d’une reprise computationnelle versionnée plus tard, avec succès partiel et limites explicites.

Prochaine étape documentaire du cycle 3 : lire intégralement les six extractions Markdown historiques de `00_Sources_docx`, puis maintenir séparément la dette des six DOCX originaux tant que leur lecture directe reste techniquement impossible.

### Cycle 3 — couche historique textuelle lue ; couverture non-DOCX complète

Les six extractions Markdown de `00_Sources_docx` sont maintenant lues intégralement. Avec la racine active et la reprise computationnelle, toutes les pièces non-DOCX du cycle 3 sont donc couvertes.

```text
CYCLE_3_TOTAL_BLOBS = 42
CYCLE_3_MARKDOWN = 20/20_LUS_INTEGRALEMENT
CYCLE_3_AUTRES_NON_DOCX = 16/16_LUS_INTEGRALEMENT
CYCLE_3_NON_DOCX = 36/36_LUS_INTEGRALEMENT
CYCLE_3_DOCX_ORIGINAUX = 0/6_LUS_DIRECTEMENT
EQUIVALENCE_DOCX_EXTRACTION_MD = NON_ETABLIE
COUVERTURE_DOCUMENTAIRE_GLOBALE_CYCLE_3 = INCOMPLETE
```

Les six extractions répètent explicitement qu’elles ne remplacent pas les DOCX originaux et que les équations, tableaux, graphiques ou la mise en page peuvent être dégradés. Elles sont donc traitées comme pièces documentaires autonomes, non comme substituts probatoires complets.

La couche historique fait apparaître une taxonomie forte :

```text
Delta m^2 -> « constantes de phase oscillatoire »
theta_12, theta_23, theta_13 -> « constantes de projection oscillatoire »
delta_CP -> « constante de phase d’asymétrie oscillatoire »
masse absolue / ancrage -> « constante de seuil spectral »
ensemble du secteur -> « constantes oscillatoires de mélange et de phase »
```

La synthèse historique voulait intégrer ces catégories à une carte consolidée et introduire explicitement des **degrés de stabilisation** : fortement stabilisé, partiellement stabilisé, en cours de stabilisation, borné sans mesure positive, structurellement ouvert.

Cette couche n’est pas annulée par N0–N5, mais elle est requalifiée. Les documents actifs ultérieurs conservent plusieurs fonctions physiques sous-jacentes — différence, projection, phase, ancrage, bornes et médiations — tout en abandonnant l’idée qu’elles doivent nécessairement devenir une taxonomie canonique de « constantes ». `N5` reformule notamment l’ancien dossier de « masse absolue » comme **plusieurs fonctions non équivalentes d’un même spectre**, reliées seulement par des ponts dont les hypothèses doivent rester visibles.

```text
ANCIENNE_TAXONOMIE_NEUTRINOS = FAIT_GENEALOGIQUE_CONSERVE
RESTAURATION_COMME_TAXONOMIE_ACTIVE = NON_ETABLIE
FONCTIONS_PHYSIQUES_SOUS_JACENTES = LARGEMENT_CONSERVEES_ET_REQUALIFIEES
FORMULE « MASSE_ABSOLUE_COMME_UNIQUE_OBJET_D_ACCES » = REQUALIFIEE_PAR_N5
DEGRES_DE_STABILISATION = IDEE_HISTORIQUE_RESURGIE_A_CONSERVER_POUR_AUDIT_TRANSVERSAL
```

La fiche historique de masse absolue conserve aussi des états empiriques plus anciens — par exemple la borne Planck+BAO `0.12 eV` et une version antérieure de KamLAND-Zen — que les fiches N3/N4 ultérieures redatent avec DESI DR2 et le jeu complet KamLAND-Zen. Ces différences sont une chronologie documentaire, pas des contradictions à moyenner.

Aucune occurrence explicite suffisamment nette de la vieille question générale de « définissabilité » n’est récupérée dans ces six extractions comme programme directeur du cycle 3. Des fonctions voisines existent — conditions de manifestation, ancrage spectral, passage entre production/propagation/détection — mais leur identité avec cette ancienne question générale n’est pas établie par le seul cycle 3.

La dette binaire demeure : six DOCX originaux doivent encore être lus directement ou faire l’objet d’une procédure d’équivalence réellement établie. Cette dette n’empêche pas la poursuite de l’audit exhaustif des autres cycles ; elle reste enregistrée pour reprise ultérieure.

```text
DETTE_DOCX_C1 = 5
DETTE_DOCX_C2 = 4
DETTE_DOCX_C3 = 6
DETTE_DOCX_CUMULEE_APRES_C3 = 15
BLOCAGE_DES_CYCLES_SUIVANTS_PAR_CETTE_DETTE = NON
```

Prochaine étape : ouvrir l’inventaire exact du cycle 4 et poursuivre la lecture exhaustive, tout en conservant le cycle 3 au statut `INCOMPLETE` tant que ses six DOCX ne sont pas directement qualifiés.

### Cycle 4 — thermo-métrologie SI — couverture textuelle complète, DOCX ouverts

Inventaire exact au baseline :

```text
00_Sources_docx/Fiche N_A v0.1.docx
00_Sources_docx/Fiche R v0.1.docx
00_Sources_docx/Fiche k_B v0.1.docx
00_Sources_docx/Source_docx_Fiche_N_A_v0_1.md
00_Sources_docx/Source_docx_Fiche_R_v0_1.md
00_Sources_docx/Source_docx_Fiche_k_B_v0_1.md
00_Sources_docx/Source_docx_Synthese_quatrieme_cycle_v0_1.md
00_Sources_docx/Synthèse du quatrième cycle.docx
Synthese_recuperation_thermo_metrologique_SI_v0_1.md
```

```text
CYCLE_4_TOTAL_BLOBS = 9
CYCLE_4_MARKDOWN = 5/5_LUS_INTEGRALEMENT
CYCLE_4_DOCX_ORIGINAUX = 0/4_LUS_DIRECTEMENT
EQUIVALENCE_DOCX_EXTRACTION_MD = NON_ETABLIE
COUVERTURE_DOCUMENTAIRE_GLOBALE_CYCLE_4 = INCOMPLETE
```

La récupération active précise que ce bloc ne constitue pas le cycle SI actif complet : il sert de récupération généalogique avant l’architecture métrologique et renvoie notamment au cycle 8 et aux documents d’architecture SI. Il faut donc distinguer le quatrième cycle historique du traitement SI actif ultérieur.

Le contenu utile n’est pas la proposition triviale « certaines constantes sont exactes par convention ». Le cycle sépare plusieurs niveaux qui peuvent être confondus :

```text
constante définissante primaire ;
grandeur exacte par composition ;
rôle physique local ;
mode de stabilisation conventionnelle ;
histoire empirique ayant rendu la convention possible ;
réalisation pratique des unités avec incertitudes résiduelles.
```

`k_B` et `N_A` sont récupérées comme constantes définissantes du SI depuis 2019, mais leurs fonctions physiques restent distinctes : passage température/énergie et entropie statistique pour `k_B`, passage nombre d’entités/quantité de matière pour `N_A`. Leur exactitude numérique actuelle ne signifie ni mesure infiniment précise ni exactitude des réalisations expérimentales.

`R = N_A k_B` introduit un cas différent : `R` n’est pas une constante définissante primaire. Son exactitude est dérivée par composition de deux constantes définissantes exactes. Le document souligne aussi que `R` n’apporte pas d’information physique indépendante supplémentaire par rapport à `N_A` et `k_B` pris ensemble, tout en conservant une fonction opératoire propre dans le langage thermodynamique molaire.

La synthèse historique bifurquait explicitement deux axes : rôle/régime physique et accès/stabilisation métrologique, ainsi que stabilisation empirique et stabilisation conventionnelle. Elle formulait une règle méthodologique ancienne selon laquelle chaque fiche devrait répondre séparément à la question de la fonction physique et à celle du mode de fixation ou d’accès à la valeur.

Cette règle historique est **remontée mais non promue automatiquement en règle de gouvernance de l’audit intégral**. Elle concerne d’abord la méthode de description scientifique des constantes et recouvre déjà partiellement des distinctions actuelles entre objet, accès, régime, métrologie et statut d’énoncé. Sa portée transversale devra être testée dans les cycles ultérieurs avant toute réactivation normative générale.

```text
REGLE_HISTORIQUE_ROLE_PHYSIQUE_VS_ACCES_METROLOGIQUE = RESURGIE
FONCTION_INTELLECTUELLE = CLAIRE
PROMOTION_COMME_REGLE_AUDIT_GLOBAL = NON_ETABLIE
REDONDANCE_PARTIELLE_AVEC_CADRE_ACTUEL = PROBABLE_MAIS_A_TESTER
```

Le cycle 4 répond donc partiellement à l’ancienne interrogation sur son caractère potentiellement tautologique : sa profondeur éventuelle ne réside pas dans le constat de l’exactitude SI, mais dans la distinction entre **origine de l’exactitude, fonction physique, histoire empirique et réalisation instrumentale**. La suffisance scientifique de cette distinction pour justifier un cycle autonome reste à évaluer dans l’audit transversal ; elle n’est pas présumée par la seule lecture documentaire.

Les quatre DOCX originaux restent une dette binaire. La dette cumulée devient :

```text
DETTE_DOCX_C1 = 5
DETTE_DOCX_C2 = 4
DETTE_DOCX_C3 = 6
DETTE_DOCX_C4 = 4
DETTE_DOCX_CUMULEE_APRES_C4 = 19
```

Aucun audit scientifique substantiel nouveau n’est ouvert par cette lecture. La prochaine lecture séquentielle peut passer au cycle 5 sans effacer cette dette.

## Complément de cadrage — statut de laboratoire du projet

L’auteur précise que le dépôt ne doit pas être lu comme un produit intellectuel achevé dont chaque état antérieur serait soit une erreur à corriger, soit une doctrine à restaurer. Il fonctionne avant tout comme un **laboratoire de recherche**, avec essais de vocabulaire, architectures provisoires, bifurcations, abandons, réabsorptions, reprises et changements de niveau.

Cette précision modifie la présomption documentaire, sans diminuer l’exigence de preuve :

```text
PROJET = LABORATOIRE_EN_EVOLUTION
GENEALOGIE_COMPLEXE = ATTENDUE_COMME_PROPRIETE_DU_TRAVAIL
ETAT_ANTERIEUR_ABANDONNE -> ERREUR = NON_PRESUME
ETAT_ANTERIEUR_ABANDONNE -> DOCTRINE_A_RESTAURER = NON_PRESUME
TRANSFORMATION_DE_VOCABULAIRE -> PERTE_OU_GAIN = A_ETABLIR
BRANCHE_EXPERIMENTALE -> AUTORITE_COURANTE = NON_PRESUME
ETAT_COURANT -> VERITE_TERMINALE = NON_PRESUME
```

Conséquence pour l’audit : la généalogie doit être lue comme un ensemble d’expériences intellectuelles dont les fonctions peuvent survivre à la disparition des termes, ou au contraire avoir été réellement abandonnées. Le rôle de l’audit est de reconstruire ces transformations et leurs effets, non de lisser le laboratoire en trajectoire linéaire ni de promouvoir automatiquement l’état le plus récent.

Cette précision renforce les règles déjà établies de non-promotion, de symétrie critique et de conservation des bifurcations ; elle ne crée pas d’exception à la lecture exhaustive.

### Cycle 5 — Saveur–Higgs — couverture textuelle complète, DOCX ouverts

Arbre exact du cycle au baseline : `d42368104ea389d0e985fa594088550013870f58`.

Inventaire exact :

```text
00_Sources_docx/Fiche (v) v0.1.docx
00_Sources_docx/Fiche CKM v0.1.docx
00_Sources_docx/Fiche Wolfenstein v0.1.docx
00_Sources_docx/Fiche Yukawa v0.1.docx
00_Sources_docx/Source_docx_Fiche_CKM_v0_1.md
00_Sources_docx/Source_docx_Fiche_Wolfenstein_v0_1.md
00_Sources_docx/Source_docx_Fiche_Yukawa_v0_1.md
00_Sources_docx/Source_docx_Fiche_v_v0_1.md
00_Sources_docx/Source_docx_Synthese_cycle_CKM_v0_1.md
00_Sources_docx/Synthèse du cycle CKM v0.1.docx
Cycle_CP1_seuil_electrofaible_v0_1.md
Dette_active_masse_electron_Yukawa_v0_1.md
Fiche_masse_absolue_neutrinos_v0_1.md
Note_physique_BEH_mecanisme_v0_1.md
S1_Relation_structurelle_masse_electron_Yukawa_v0_1.md
S2_Acces_metrologiques_indirects_directs_Yukawa_electron_v0_1.md
S3_Verdict_local_masse_electron_Yukawa_acces_Higgs_v0_1.md
Synthese_CP1_seuil_electrofaible_v0_1.md
Synthese_active_cycle_5_Saveur_Higgs_apres_S1_S3_v0_2.md
Synthese_cycle_saveur_Higgs_v0_1.md
Synthese_recuperation_sources_saveur_Higgs_cible_v0_1.md
architecture-relationnelle-higgs-yukawa.md
evaluation-gain-explicatif-higgs-yukawa.md
verification-physique-higgs-yukawa.md
```

```text
CYCLE_5_TOTAL_BLOBS = 24
CYCLE_5_MARKDOWN = 19/19_LUS_INTEGRALEMENT
CYCLE_5_DOCX_ORIGINAUX = 0/5_LUS_DIRECTEMENT
EQUIVALENCE_DOCX_EXTRACTION_MD = NON_ETABLIE
COUVERTURE_DOCUMENTAIRE_GLOBALE_CYCLE_5 = INCOMPLETE
```

La trajectoire documentaire du cycle 5 est elle-même un résultat important de l’audit. Elle comporte plusieurs couches expérimentales successives qu’il ne faut ni fusionner ni hiérarchiser rétrospectivement sans contrôle :

```text
sources historiques taxonomiques
-> compression CKM / Orientation
-> pilote « architecture relationnelle / fonction de fixité »
-> sous-cycle CP-1 « constance de seuil »
-> requalification Saveur–Higgs en pont architectural
-> lot S1–S3 centré sur les rangs probatoires
-> synthèse active v0.2 = pont architectural + réseau de passages probatoires.
```

#### Résurgences historiques et requalifications

Les sources historiques proposaient notamment :

```text
v -> « constante de régime générateur » ;
Yukawa -> « constantes de différenciation fermionique » / « constantes de texture » ;
CKM -> orientation de saveur ;
Wolfenstein -> paramètres hiérarchiques d’orientation ;
CP-1 -> « constance de seuil ».
```

La synthèse historique CKM avait déjà commencé à compresser les anciennes catégories neutrino en une famille générale `Orientation`, en rétrogradant « oscillatoire » vers un régime de manifestation. La récupération Saveur–Higgs ultérieure va plus loin : elle conserve les fonctions de `v`, Yukawa, CKM et Wolfenstein mais refuse de restaurer les anciennes étiquettes comme rangs taxonomiques autonomes.

```text
ANCIENNES_CATEGORIES_SAVEUR_HIGGS = FAITS_GENEALOGIQUES_CONSERVES
RESTAURATION_COMME_TAXONOMIE_ACTIVE = NON_ETABLIE
FONCTIONS_LOCALES_SOUS_JACENTES = PARTIELLEMENT_CONSERVEES_ET_REQUALIFIEES
CP1_CONSTANCE_DE_SEUIL = EXPERIENCE_METHODOLOGIQUE_HISTORIQUE_A_NE_PAS_PROMOUVOIR_PAR_DEFAUT
```

#### Correction physique interne importante

Le pilote `architecture-relationnelle-higgs-yukawa.md` et sa vérification corrigent une séquence ancienne susceptible de suggérer que les Yukawa sont produits par la brisure électrofaible. La formulation contrôlée devient :

```text
les termes de Yukawa appartiennent déjà au Lagrangien symétrique ;
la valeur moyenne non nulle du Higgs permet leur contribution aux matrices de masse ;
la diagonalisation révèle valeurs propres et désalignements ;
elle ne crée ni n’explique la hiérarchie encodée dans les Yukawa.
```

La même vérification sépare l’ordre logique de la théorie, les opérations de représentation, les voies d’accès et l’histoire thermique. Le changement électrofaible dans le Modèle standard physique est traité comme un **crossover** et non comme un instant singulier de « formation des constantes ».

#### Pilote « fonction de fixité »

Le pilote conclut que l’hypothèse de « fonction de fixité » possède un gain local limité : elle aide à distinguer fixation d’échelle, texture, spectre, orientation et raccordement effectif, mais elle n’est pas démontrée comme vocabulaire général de tous les cycles.

Le document d’évaluation formule explicitement :

```text
PILOTE_HIGGS_YUKAWA = CONCLUANT_SOUS_CONDITIONS
GENERALISATION_FONCTION_DE_FIXITE_A_TOUS_LES_CYCLES = NON_ETABLIE
GAIN_LE_PLUS_ROBUSTE = RELATIONS_TYPEES + LOCALISATION_DES_ARRETS_DE_L_EXPLICATION
```

Le gain n’est donc pas la création d’un métalangage supplémentaire ; il réside surtout dans la séparation des mécanismes, représentations, régimes et accès, ainsi que dans la capacité à formuler des contrefactuels et à localiser ce que le Modèle standard paramètre sans l’expliquer.

#### Requalification active v0.1 -> v0.2

La synthèse v0.1 conserve le réseau :

```text
échelle de brisure
+ Yukawa
+ matrices de masse
+ diagonalisation
+ spectres
+ orientations CKM / PMNS.
```

Elle a toutefois été explicitement requalifiée : les formulations fortes d’« architecture constitutive confirmée », de « solidarité constitutive stabilisée » ou de « temporalité de constitution » ne valent plus comme verdicts généraux. Le rang actif devient :

```text
SAVEUR_HIGGS = PONT_ARCHITECTURAL_DOCUMENTE
GAIN_EXPLICATIF = CONDITIONNEL
EXPLICATION_D_ORIGINE = REFUSEE
```

La synthèse active v0.2 ajoute au pont architectural un **réseau de passages probatoires indexés**, sans généraliser automatiquement le cas électronique aux autres fermions ou orientations.

#### Dette électronique transférée depuis le cycle 1

La dette `m_e / y_e` transférée par D6 n’a pas été oubliée. S1–S3 l’ont localement résolue dans son premier périmètre.

S1 impose les distinctions :

```text
M_e
!= m_e^S(mu)
!= y_e^S(mu)
!= v^S(mu)
!= v_F
!= g_hee.
```

et les trois rangs :

```text
identité nue
!= paramétrisation renormalisée
!= raccordement à une masse physique corrigé.
```

S2 distingue métrologie, eEDM, `a_e`, `H -> e+e-` et futur `e+e- -> H` par leur cible et leur modèle de passage. Il refuse une combinaison numérique hors modèle commun et refuse toute hiérarchie universelle `direct > indirect`.

S3 porte le verdict local :

```text
M_e = masse physique très précisément déterminée ;
y_e standard = inféré avec grande précision dans le Modèle standard minimal sous conventions déclarées ;
H -> e+e- = branche directement bornée, sans observation du couplage standard ;
origine de la petitesse de y_e = NON_EXPLIQUEE ;
hiérarchie fermionique = NON_EXPLIQUEE.
```

La dette est donc close **localement**, tandis que le cycle Saveur–Higgs reste ouvert et que l’observation directe du Yukawa électronique à la valeur standard demeure non acquise.

#### Dossier neutrino présent dans le cycle 5

La fiche interne `Fiche_masse_absolue_neutrinos_v0_1.md` constitue une couche intermédiaire entre l’ancienne taxonomie neutrino et la reconstruction N0–N5 du cycle 3. Elle refuse déjà de faire de la « masse absolue » une famille autonome et requalifie « seuil spectral » comme rôle, non comme famille. Elle distingue `m_beta`, `Sigma_m_nu` et `m_beta_beta` et avertit que la trajectoire des bornes n’est pas une variation physique de la masse.

Sa présence dans Saveur–Higgs montre une interface historique réelle entre les cycles 3 et 5 ; elle n’autorise pas à déplacer rétroactivement l’autorité actuelle du dossier neutrino hors du cycle 3.

#### Dettes et limites

Les cinq DOCX originaux restent non lus directement et leurs extractions déclarent ne pas les remplacer. La dette binaire cumulée devient :

```text
DETTE_DOCX_C1 = 5
DETTE_DOCX_C2 = 4
DETTE_DOCX_C3 = 6
DETTE_DOCX_C4 = 4
DETTE_DOCX_C5 = 5
DETTE_DOCX_CUMULEE_APRES_C5 = 24
```

Aucun nouveau verdict scientifique n’est produit par le présent audit documentaire. Les valeurs et qualifications scientifiques historiques sont conservées comme contenu versionné ; leur revalidation externe n’est pas ouverte ici.

Prochaine position documentaire : ouvrir l’inventaire exact du cycle 6, tout en conservant le cycle 5 au statut `INCOMPLETE` tant que ses cinq DOCX originaux ne sont pas directement qualifiés.

## Clarification de lecture — remarques informatives, généralisation et complexité généalogique

L’auteur corrige une inférence produite lors du cycle 5 : constater une complexité généalogique substantielle dans ce cycle ne permet pas d’inférer que les cycles 1 à 4 en possèdent moins. Le statut de laboratoire concerne le projet dans son ensemble ; la complexité de chaque cycle reste à établir par sa propre lecture, sans réaudit rétroactif automatique.

Deuxième clarification : la prudence contre les généralisations automatiques n’est pas une interdiction de généraliser. Un cas particulier peut légitimement soutenir une généralisation lorsque les recoupements, contre-tests ou autres matériaux lui donnent une portée suffisante.

```text
CAS_PARTICULIER -> REGLE_UNIVERSELLE = NON_AUTOMATIQUE
CAS_PARTICULIER + SUPPORT_TRANSVERSAL_SUFFISANT -> GENERALISATION = POSSIBLE
NON_GENERALISATION_AUTOMATIQUE != INTERDICTION_DE_GENERALISER
COMPLEXITE_GENEALOGIQUE_C5 -> COMPLEXITE_MOINDRE_C1_C4 = NON_ETABLI
```

Enfin, les remarques conversationnelles de l’auteur sont **informatives par défaut**. Elles servent de contexte et peuvent orienter l’attention, mais ne doivent pas être converties automatiquement en décision de projet ou en règle nouvelle. Une prise de position explicitement décisionnelle — validation, réfutation, amendement, autorisation, interdiction ou décision équivalente — peut modifier l’état ou le cadre correspondant.

```text
REMARQUE_INFORMATIVE -> MUTATION_DU_CADRE = NON_AUTOMATIQUE
PRISE_DE_DECISION_EXPLICITE -> EFFET_A_CONSIGNER_SELON_SON_OBJET
CORRECTION_EXPLICITE_D_UNE_INFERENCE_AGENT = A_INTEGRER_COMME_CLARIFICATION
```

Cette clarification ne change pas la méthode de lecture exhaustive en cours.

### Cycle 6 — effectif basse énergie — couverture textuelle complète, DOCX ouverts

Arbre exact au baseline : `4492d3c3763e4a69b8e40984c25c2dfc0d2b5511`.

Inventaire exact :

```text
00_Sources_docx/Cycle effectif basse énergie v0.1.docx
00_Sources_docx/Cycle effectif basse énergie v0.2.docx
00_Sources_docx/Cycle effectif basse énergie v0.3.docx
00_Sources_docx/Fiche alpha_G - M_Pl (1).docx
00_Sources_docx/Fiche alpha_G - M_Pl.docx
00_Sources_docx/Source_docx_Cycle_effectif_basse_energie_v0_1.md
00_Sources_docx/Source_docx_Cycle_effectif_basse_energie_v0_2.md
00_Sources_docx/Source_docx_Cycle_effectif_basse_energie_v0_3.md
00_Sources_docx/Source_docx_Fiche_alpha_G_M_Pl_A_v0_1.md
00_Sources_docx/Source_docx_Fiche_alpha_G_M_Pl_B_v0_1.md
Cycle_effectif_basse_energie_v0_4_alphaG_MPl.md
Synthese_comparaison_alphaG_MPl_sources_v0_1.md
Synthese_cycle_effectif_basse_energie_v0_1.md
architecture-relationnelle-basse-energie.md
evaluation-gain-explicatif-basse-energie.md
verification-physique-basse-energie.md
```

```text
CYCLE_6_TOTAL_BLOBS = 16
CYCLE_6_MARKDOWN = 11/11_LUS_INTEGRALEMENT
CYCLE_6_DOCX_ORIGINAUX = 0/5_LUS_DIRECTEMENT
EQUIVALENCE_DOCX_EXTRACTION_MD = NON_ETABLIE
COUVERTURE_DOCUMENTAIRE_GLOBALE_CYCLE_6 = INCOMPLETE
```

La synthèse historique portait un verdict fort d’« architecture inter-familles confirmée ». Elle déclare désormais elle-même ce verdict historique et non autoritatif. La reprise active repart de l’hypothèse et la requalifie plus sobrement.

#### Résultat principal de la reprise

Trois opérations physiques ne doivent pas être confondues :

```text
Fermi / W : réduction locale par médiateur lourd non résolu ;
QCD : flot de couplage et changement de régime dynamique ;
gravitation EFT : expansion hiérarchique avec corrections supprimées à basse énergie.
```

Elles ne partagent pas un mécanisme physique unique de « formation d’une constante ». Le noyau commun récupéré est principalement méthodologique et structurel :

```text
séparation d’échelles ;
choix des degrés de liberté ;
symétries ;
expansion / comptage ou organisation contrôlée ;
coefficients dans un cadre déclaré ;
estimation de l’erreur ;
domaine de rupture.
```

La reprise conserve donc un résultat de type **architecture méthodologique de validité**, et non une classe ontologique générale de constantes effectives basse énergie.

#### Corrections et distinctions acquises dans le corpus

Le dossier actif établit notamment :

- `G_F` est le coefficient dominant d’une description locale dans son domaine, non un substitut universel de toute la théorie électrofaible ;
- matching, running et mélange d’opérateurs appartiennent à la chaîne EFT ; un coefficient de Wilson isolé dépend de la base, du schéma et de l’échelle et n’est pas un invariant physique autonome ;
- `alpha_s(mu)` est un couplage courant ; `Lambda_MSbar` est un paramètre d’échelle dépendant du schéma et ne doit pas être identifié sans qualification à une observable unique de confinement ;
- la gravitation peut être prédictive comme EFT de basse énergie sans complétion UV connue ; `M_Pl` organise le comptage de puissances mais n’est pas démontrée comme frontière physique nette ;
- « basse énergie » n’est pas synonyme de simplification : elle produit localité effective dans le secteur faible, entrée dans le non-perturbatif en QCD et suppression hiérarchique dans la gravitation effective.

Le rapport d’évaluation dégage en outre trois niveaux distincts :

```text
fixité de composante ;
stabilité de prédiction ;
validité de description.
```

Une prédiction peut rester stable alors que certains coefficients courent, changent de base ou sont raccordés. Cette distinction est remontée comme résultat local du cycle 6 ; sa portée transversale au reste du projet n’est ni promue ni interdite par principe et devra être soutenue si elle est généralisée.

#### Deux états alpha_G / M_Pl

Les deux extractions `A` et `B` proviennent de deux DOCX distincts. La note de comparaison établit qu’elles ne sont pas des copies et doivent rester deux états généalogiques séparés. La fiche active v0.4 les dépasse toutes deux en ajoutant notamment la distinction Planck / Planck réduite, la comparaison explicite avec Fermi et QCD, ainsi que la requalification de la « hiérarchie d’échelle » en fonction plutôt qu’en famille.

```text
ALPHAG_MPL_A_B = DEUX_ETATS_DISTINCTS
DEDUPLICATION_SILENCIEUSE = INTERDITE
ANCIENNE_CATEGORIE_HIERARCHIE_D_ECHELLE = NON_RESTAUREE_COMME_FAMILLE
```

#### Rapport aux audits antérieurs

Le premier inventaire de surface avait conclu que le gain initial d’inventaire paraissait faible dans ce cycle. La lecture exhaustive ne révèle pas un sous-dossier caché analogue au cycle 3, mais elle apporte une requalification substantielle du résultat ancien : l’unité qui résiste n’est pas celle d’une famille d’objets, mais celle d’une discipline de validité. Ainsi :

```text
GAIN_INVENTAIRE_DE_SURFACE_FAIBLE = FAIT_INITIAL_CONSERVE
GAIN_DE_LA_LECTURE_EXHAUSTIVE = REQUALIFICATION_CONCEPTUELLE_SUBSTANTIELLE
ABSENCE_DE_SURPRISE_TOPOLOGIQUE != ABSENCE_DE_GAIN_INTELLECTUEL
```

Aucun résultat scientifique n’est revalidé extérieurement par cette lecture documentaire ; les vérifications présentes sont des rapports historiques versionnés dont la suffisance pour un futur audit scientifique substantiel reste à tester selon le programme général.

#### Dette binaire

Les cinq DOCX originaux restent non lus directement. Les extractions annoncent explicitement qu’elles ne les remplacent pas.

```text
DETTE_DOCX_C1 = 5
DETTE_DOCX_C2 = 4
DETTE_DOCX_C3 = 6
DETTE_DOCX_C4 = 4
DETTE_DOCX_C5 = 5
DETTE_DOCX_C6 = 5
DETTE_DOCX_CUMULEE_APRES_C6 = 29
```

La dette n’empêche pas l’ouverture du cycle 7. Le cycle 6 reste `INCOMPLETE` au sens documentaire global tant que les cinq DOCX originaux ne sont pas qualifiés directement ou par une procédure d’équivalence effectivement établie.

Prochaine position documentaire : ouvrir l’inventaire exhaustif du cycle 7, sans présumer que ses routes vivantes, ses rapports computationnels ou ses issues résument suffisamment ses 66 blobs.

### Cycle 7 — inventaire exact et couche de racine intégralement lue

Arbre exact au baseline : `3df6810ef1a6b1f98f74c7d37dfc9fe7f14668f2`.

Le cycle contient exactement 66 blobs et, contrairement aux cycles 1 à 6, aucun DOCX. La répartition matérielle exacte est :

```text
Markdown = 31
Python = 23
YAML = 9
TXT = 2
PowerShell = 1
TOTAL = 66
```

La racine contient 13 Markdown ; le sous-dossier `01_REPRISE_COMPUTATIONNELLE_C7_C1` contient 53 blobs : 18 Markdown, 23 Python, 9 YAML, 2 TXT et 1 PowerShell.

```text
CYCLE_7_RACINE_MARKDOWN = 13/13_LUS_INTEGRALEMENT
CYCLE_7_REPRISE_COMPUTATIONNELLE = 0/53_A_CE_PALIER
CYCLE_7_TOTAL_LU = 13/66
COUVERTURE_CYCLE_7 = EN_COURS
DETTE_DOCX_C7 = 0
```

#### Trajectoire de la couche cosmologique de racine

La racine conserve plusieurs états successifs : cadrage des objets cosmologiques, fiches `Lambda`, `H_0`, `Omega_i`, `w`, `A_s/n_s`, `sigma_8/S_8`, synthèse historique, plan de reprise, puis triptyque `architecture / vérification / évaluation`.

La synthèse historique avait formulé une `macro-architecture` de fonctions et sous-réseaux. Le triptyque de reprise la requalifie explicitement :

```text
ARCHITECTURE_COSMOLOGIQUE_INFERENTIELLE_RECONSTRUCTIVE = CONFIRMEE_DANS_CETTE_REPRISE_HISTORIQUE
MACRO_ARCHITECTURE_DE_CONSTANTES = REFUSEE_DANS_CETTE_REPRISE_HISTORIQUE
```

Cette qualification est conservée comme résultat historique versionné. Elle ne vaut pas automatiquement verdict scientifique actuel du cycle 7, dont les lignes courantes `C7-C1 / X(z) / SCI-1` et `C7-GAL / C0` sont plus tardives et indépendantes.

#### Distinctions remontées dans les 13 pièces

La couche de racine sépare notamment :

```text
Lambda : paramètre de loi candidat à la constance dans GR + Lambda ;
H_0 : valeur actuelle de H(t), donc paramètre d'état ;
Omega_i : rapports normalisés dépendant de rho_crit et de l'époque ;
w : relation / paramétrisation d'état ;
A_s, n_s : paramètres primordiaux à pivot déclaré ;
sigma_8, S_8 : reconstructions tardives et combinaisons adaptées à des dégénérescences ;
tension : propriété comparative de réseaux d'inférence, non objet physique autonome.
```

Le triptyque insiste en outre sur la séparation de trois chaînes :

```text
chaîne physique ;
chaîne paramétrique ;
chaîne inférentielle.
```

et sur la règle historique :

```text
fixé dans un fit != constant physiquement.
```

Ces distinctions seront recoupées avec les artefacts computationnels ; elles ne sont pas tenues pour confirmées par la seule synthèse.

#### Relation avec les lignes actives

Le README courant sépare explicitement :

```text
C7-C1 / X(z) / SCI-1
!=
C7-GAL / C0
```

Aucun état, blocage, autorisation ou verdict ne se transfère entre les deux. Le README signale aussi que le rouge de persistance de RUN1 a une cause source/contrat qualifiée sans qualification scientifique de RUN1, tandis que C7-GAL reste bloquée sur l'accès matériel à certains HDF5. Ces états sont seulement enregistrés ici comme contenu du README ; ils devront être reconstruits depuis les pièces concernées et ne sont pas utilisés comme substitut aux 53 blobs restant à lire.

Prochaine étape documentaire : lecture exhaustive des 53 blobs de `01_REPRISE_COMPUTATIONNELLE_C7_C1`, en commençant par README, requirements, configurations et manifeste de provenance avant les rapports et scripts.

#### Cycle 7 — jalon computationnel : provenance, configurations, G1 et G2.1–G2.3

À ce palier, 19 des 53 blobs de la reprise computationnelle ont été lus, soit 32/66 blobs pour le cycle 7 entier.

```text
REPRISE_COMPUTATIONNELLE_LUE = 19/53
CYCLE_7_TOTAL_LU = 32/66
CONFIGS = 9/9_LUES
MANIFESTE_PROVENANCE = 1/1_LU
README_ET_REQUIREMENTS = 3/3_LUS
RAPPORTS_LUS = 6/16
SCRIPTS_LUS = 0/24
```

Les deux gels d’environnement restent distincts : l’environnement directeur historique utilise notamment `Cobaya 3.5`, `CAMB 1.5.4`, `NumPy 1.26.4`, tandis que le contrôle secondaire utilise `Cobaya 3.5.7` et ajoute `typing_extensions`. Ils ne sont pas fusionnés en un environnement unique.

Le manifeste G1.0 borne la provenance : données BAO officielles hors Git, octets épinglés et hachés ; références YAML conservées ; compression CMB publique transcrite avec convention explicite `theta_star=0.01041` et conversion `/100` depuis la sérialisation CAMB ; prior CPL `w0 ~ U[-3,1]`, `wa ~ U[-3,2]`, `w0+wa<0`.

Les YAML locaux ΛCDM/CPL conservent les blocs `theory/params/sampler` des références historiques et remplacent les bindings NERSC par la transcription locale contrôlée ; la sortie a été supprimée à G1.0. Les quatre configurations `X(z)` font varier uniquement la grille M2a/M2b et la convention de spline natural/not-a-knot, à graines distinctes ; elles portent toutes `inference.autorisee: false`.

G1.0 puis G1.2 documentent une qualification de la vraisemblance commune avant MCMC. BAO est triangulée entre bindings historiques, transcription locale et vraisemblance stock à environ `1e-6` sur les points fixes. La compression CMB publique arrondie ne reproduit pas byte-à-byte la compression interne DESI ; son effet a été quantifié par repondération exacte intégrale et jugé sous les seuils historiques ratifiés. Ce statut doit rester : **qualification historique versionnée**, non revalidation externe par le présent audit.

G1.3 rapporte ensuite les reproductions ΛCDM et CPL sous la vraisemblance commune, avec séparation explicite entre posterior, MAP, maximum de vraisemblance et minimum rencontré dans les chaînes. Les départs naïfs de minimisation CPL ont tous échoué à retrouver la vallée pertinente ; ce résultat négatif a été conservé, puis des départs informés depuis les chaînes ont été utilisés. Il ne faut donc pas réécrire rétroactivement la réussite finale comme absence d’échec d’optimisation.

G2.1 est un rapport de validation instrumentale, sans MCMC ni posterior `X(z)`. Il documente notamment : identité `X=1` avec ΛCDM, comparaison natural/not-a-knot, domaine signé, continuation constante, stabilité numérique, voie indépendante pour plusieurs quantités et fautes injectées. La convention de spline est montrée comme scientifiquement active sur les profils de stress ; aucune convention n’est promue par ce seul constat.

Le pré-enregistrement G2.2 fixe avant inférence quatre variantes co-primaires, familles de priors, conditions de troncature, diagnostics de convergence, statistiques, sensibilités et règles d’amendement. Il interdit explicitement d’éliminer ou promouvoir une variante après inspection des résultats et refuse Wilks automatique pour les splines.

G2.3 qualifie les configurations sans inférence et installe une porte auto-bloquante : schéma YAML intégral, garde des sorties hors Git, refus des options MCMC/minimisation, tests de logprior, identité, ré-exécution des contrôles et fautes injectées. Une condition fausse doit produire un code non nul ; un simple `false` dans un JSON n’est pas accepté comme garde suffisante.

```text
G1_G2_3 = CHAINE_DE_QUALIFICATION_TECHNIQUE_HISTORIQUE_REMONTEE
RESULTAT_SCIENTIFIQUE_XZ = NON_PRODUIT_PAR_CES_PORTES
MCMC_XZ_AVANT_AUTORISATION_ULTERIEURE = ABSENTE_DANS_CES_PIECES
ECHECS_OPTIMISATION_CPL_NAIVE = RESULTAT_NEGATIF_CONSERVE
CONVENTION_SPLINE = DECISION_SCIENTIFIQUEMENT_ACTIVE_DANS_LES_TESTS_DE_STRESS
```

Prochaine étape : lire la série G2.4, puis les rapports de durcissement/sentinelle/capacité, avant de confronter les assertions des rapports aux 24 scripts versionnés.

#### Cycle 7 — clôture documentaire intégrale du baseline

La lecture des dix rapports restants de G2.4/CAP/REJ/SENT puis des vingt-quatre scripts versionnés ferme le périmètre matériel du cycle 7.

```text
CYCLE_7_RACINE = 13/13_MARKDOWN_LUS
REPRISE_README_REQUIREMENTS = 3/3_LUS
REPRISE_CONFIGS = 9/9_LUES
REPRISE_MANIFESTE = 1/1_LU
REPRISE_REPORTS = 16/16_LUS
REPRISE_SCRIPTS = 24/24_LUS
REPRISE_COMPUTATIONNELLE = 53/53_BLOBS_LUS
CYCLE_7_TOTAL = 66/66_BLOBS_LUS
DETTE_DOCX_C7 = 0
COUVERTURE_DOCUMENTAIRE_CYCLE_7 = COMPLETE
EXECUTION_NOUVELLE_PAR_L_AUDIT = NON
REVALIDATION_SCIENTIFIQUE_EXTERNE = NON
```

Cette complétude porte sur le corpus Git du baseline. Elle ne remplace pas les données externes, les sorties hors Git, les issues ou les artefacts matériels auxquels les documents renvoient, et elle ne transforme pas les qualifications historiques en résultats recalculés par le présent audit.

##### Chaîne G2.4 : capacité, optimisation et amendement

La qualification du lanceur a d'abord conclu que le plan initial de 32 chaînes était techniquement prohibitif dans l'environnement local. Ce résultat de capacité a déclenché une optimisation du calcul, non une modification du modèle, des priors ou des variantes scientifiques.

L'optimisation sépare les paramètres lents de fond des nœuds `X_i` rapides et introduit un cache exact, sans émulateur. Elle a d'abord reproduit l'oracle directeur, puis cette équivalence a exposé une faiblesse numérique de l'oracle acoustique lui-même. L'amendement A1 a donc corrigé la règle acoustique et conservé la règle antérieure comme `legacy` au lieu de réétiqueter rétroactivement les anciens résultats. Le contrôle direct jusqu'à `z=10^8`, devenu numériquement vacant, est retiré de la porte d'acceptation au profit d'une quadrature Gauss–Legendre segmentée et d'une borne analytique de queue.

```text
OPTIMISATION_REUSSIE_CONTRE_ORACLE -> ORACLE_SCIENTIFIQUEMENT_SUFFISANT = FAUX
DEFAUT_ORACLE_DECOUVERT_APRES_EQUIVALENCE = CONSERVE
AMENDEMENT_A1 = CORRECTION_NUMERIQUE_BORNEE
ANCIENNE_REGLE = CONSERVEE_COMME_LEGACY
S5_ENVELOPES_SCIENTIFIQUES = NON_RATIFIEES
```

##### Le vert de harnais n'est pas une preuve suffisante

Plusieurs épisodes indépendants établissent dans le corpus lui-même qu'un harnais peut être vert tout en fournissant une preuve vacante ou mal attribuée.

Dans G2.4d, un premier ensemble de fautes injectées paraissait entièrement détecté, mais cinq gardes aval étaient en réalité inatteignables : une exception antérieure suffisait à produire l'échec attendu. La correction impose ensuite l'identité de la cause, l'ordonnancement des contrôles et un scénario nominal positif qui doit atteindre la porte cible.

REJ-1 rencontre une vacuité d'une autre nature : après l'existence légitime d'un run sentinelle, des qualificateurs conçus pour un monde vide ne testent plus la garde annoncée. Le correctif substitue explicitement un monde synthétique seulement dans le harnais, vérifie l'atteinte de la porte et restaure ensuite le monde réel, sans relâcher la garde de production.

SENT-0A/B découvre après une première qualification deux défauts supplémentaires : une fenêtre TOCTOU lors de l'acquisition du répertoire et une machine d'état du manifeste trop permissive. Ils sont corrigés par acquisition exclusive atomique et finalisation monotone.

CAP-1 conserve enfin une première passe rouge avec plusieurs causes distinctes, dont une preuve de verrou redevenue vacante et une interrogation système intermittente. Les branches réellement inatteignables sont déclarées telles plutôt que simulées artificiellement comme couvertes.

```text
VERT_HARNAIS -> PREUVE_NON_VACANTE = NON_GARANTI
ECHEC_MACHINE -> CANDIDAT_SCIENTIFIQUE_EN_CAUSE = NON_AUTOMATIQUE
CAUSE_D_ECHEC = A_REPRODUIRE_ET_LOCALISER
PREUVE_DE_GARDE = EXIGE_ATTEINTE_DE_LA_PORTE + CAUSE_EXACTE + CAS_NOMINAL
```

Cette convergence avec une règle générale déjà établie ne crée pas une nouvelle règle : elle lui fournit plusieurs cas documentaires internes supplémentaires.

##### Recoupement rapports ↔ code

La lecture des 24 scripts confirme que les distinctions revendiquées ne sont pas seulement narratives :

- acquisition BAO bornée par taille et empreintes ;
- conversion explicite de `theta_star` dans la compression CMB ;
- voies de contrôle BAO et acoustiques distinctes du code directeur ;
- séparation MAP / maximum de vraisemblance / minimum rencontré ;
- domaine signé de `X(z)` et rejet par invalidité du fond, non par positivité imposée de `X` ;
- quatre variantes M2a/M2b × natural/not-a-knot maintenues distinctes ;
- adaptateur rapide exact avec séparation lent/rapide, sans émulation ;
- modes numériques `legacy` et amendés maintenus explicitement distincts ;
- qualificateurs auto-bloquants et injections de fautes ;
- acquisition atomique du run, machine d'état monotone et contrat privé de préparation ;
- politique de capacité séparée de la convergence ;
- driver PowerShell sans timeout ni relance automatique ;
- heartbeat observateur en ajout seulement, sans fonction de pilotage scientifique.

Les deux scripts de MCMC n'ont pas le même rang : `run_mcmc_g1_3.py` appartient à la reproduction des références ΛCDM/CPL ; `run_mcmc_xz_g2_4.py` est le lanceur de production `X(z)` entouré des gardes ultérieures. Leur présence dans le corpus ne vaut pas exécution nouvelle par l'audit.

Le qualificateur SENT-0D reconstruit un franchissement étroit à deux clés, sous contrat de préparation scellé et périmètre sentinelle. Le qualificateur SENT-0 vérifie notamment que cette ouverture étroite ne devient pas une autorisation générale de production.

##### Effet sur l'état scientifique

La lecture exhaustive du cycle 7 améliore fortement la reconstruction des causes, des portes et des bifurcations computationnelles, mais elle n'autorise aucune promotion scientifique de RUN1 ou de SCI-1.

Le point d'entrée courant du cycle conserve explicitement la séparation :

```text
RUN1_PERSISTENCE_RED = CAUSE_SOURCE_CONTRAT_QUALIFIEE_DANS_LE_CONTEXTE_COURANT
RUN1_SCIENTIFIC_QUALIFICATION = NON
SCI1 = NON_QUALIFIABLE_DANS_L_ETAT_COURANT
NEW_SAMPLING = NON_AUTORISE
C7_C1 != C7_GAL
```

Ces états sont enregistrés comme état documentaire courant du baseline et non reproduits expérimentalement par le présent audit. La complétude `66/66` n'ouvre donc ni B1, ni un nouveau sampling, ni une conclusion sur la géométrie intrinsèque du posterior.

Le cycle 7 est le premier cycle parcouru sous ce changelog dont le corpus versionné peut être déclaré **documentairement complet sans dette de format**. Cela ne lui confère aucun rang scientifique supérieur aux cycles 1 à 6 ; ceux-ci restent incomplets principalement à cause de leurs DOCX originaux non lus directement.

Prochaine position documentaire propre : ouvrir l'inventaire exact du cycle 8 — métrologique SI — sans utiliser la synthèse du cycle 4 comme substitut à sa lecture.