## Cas 1 — représentation intermédiaire du Cycle 7

1. **Ce que je ferais maintenant**
   Je maintiendrais `S-C7-C1` dans son statut de représentation locale de `C7-C1 / X(z) / SCI-1` et je refuserais de l'utiliser, inchangée, comme « état courant du Cycle 7 ». Le README vivant du cycle établit deux lignes actives et scientifiquement indépendantes, `C7-C1 / X(z) / SCI-1` et `C7-GAL / C0`. Une représentation ne couvrant que la première perd donc une dimension matérielle dès qu'elle devient entrée d'une décision au niveau du cycle.
   C'est exactement le régime de R-009 et R-040 : une synthèse prétendant représenter l'état réel doit conserver les états vivants pertinents, et une transformation utilisée en aval doit être contrôlée pour les dimensions perdues.

2. **Ce que je ne ferais pas encore**
   Je ne transférerais aucun verdict, blocage ou autorisation de `C7-C1` vers `C7-GAL`; je ne prendrais aucune décision « Cycle 7 entier » à partir de `S-C7-C1`; je ne lancerais pas non plus un audit exhaustif du dépôt. Le README du cycle interdit précisément l'héritage implicite entre les deux lignes.

3. **Faits et sources qui justifient la décision**
   Le cas garantit que `S-C7-C1` restitue correctement plusieurs faits locaux, dont la cause source-level du rouge, le contrat trop fort, l'absence de qualification scientifique, `SCI1 = NON_QUALIFIABLE`, `B1 = NON_AUTORISEE` et `NEW_SAMPLING = NON_AUTORISE`.  Le README vivant confirme ces faits, mais ajoute un état indépendant `C7-GAL / C0`, avec notamment `PROGRAMME_C7_GAL = OUVERT`, `LOT_C = ROUTE_ACTIVE`, `C0_A = BLOQUEE_PAR_ACCES_MATERIEL_AUX_HDF5` et `G2 = NON_OUVERTE`.
   R-009 interdit qu'une synthèse d'état écrase une partie vivante du portefeuille, et R-040 précise que la justesse du sous-ensemble transmis ne suffit pas à démontrer sa suffisance pour l'usage aval.

4. **Ce qui ferait changer de niveau d'analyse ou ouvrir un contrôle supplémentaire**
   Une décision exigeant les permissions ou blocages mouvants précis de l'une des lignes justifierait alors l'ouverture de son issue active (`#119` ou `#120`). Une prétention plus large à une synthèse/audit du portefeuille déclencherait les contrôles globaux prévus par R-009/R-011.

5. **Condition de silence / non-déclenchement**
   Si `S-C7-C1` reste utilisé uniquement pour sa fonction locale `C7-C1`, aucun contrôle de représentation du Cycle 7 entier n'est requis : R-009 prévoit explicitement qu'un audit local n'a pas à représenter tout le portefeuille.

6. **Condition d'arrêt**
   L'analyse s'arrête dès que le delta pertinent est établi : `S-C7-C1` couvre une ligne alors que l'usage aval proposé porte sur deux lignes indépendantes. Cette perte suffit à refuser l'extrapolation, sans ouvrir les issues. C'est la condition d'arrêt de R-040 : delta source→sortie et effet aval qualifiés.

7. **Pièces effectivement consultées pour ce cas**
   `00_REPRISE/cas_1_representation.md` ; `00_REPRISE/guide_reprise.md` ; `AGENTS.md` ; `README.md` ; `02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/README.md`.
   Aucune issue consultée.

---

## Cas 2 — pratique répétée sans incident

1. **Ce que je ferais maintenant**
   Je qualifierais la pratique comme **formulée et appliquée à trois reprises sans incident visible**, mais **pas comme testée**. Je ne la rendrais pas obligatoire pour tous les cycles. R-041 dit explicitement qu'une application sans incident ne vaut pas test et demande, pour parler de test, un effet attendu, un échec/coût ou contre-cas/comparaison, et une observation discriminante.

2. **Ce que je ne ferais pas encore**
   Je n'emploierais ni « testée » ni « validée », et je ne transformerais pas les trois usages favorables en promotion transverse. Une décision de promotion durable reste en outre une frontière soumise à décision humaine selon `AGENTS.md`.

3. **Faits et sources qui justifient la décision**
   Les seuls faits probatoires fournis sont trois applications et l'absence d'incident visible.  R-041 distingue précisément application, observation en situation, mise à l'épreuve, soutien/falsification, ratification et promotion.
   La pratique elle-même est cohérente avec R-008 et avec `AGENTS.md`, qui demandent des checkpoints ou consignations lors de transitions substantielles plutôt qu'à chaque action. Mais cette cohérence normative ne transforme pas les trois usages en test empirique.

4. **Ce qui ferait changer de niveau d'analyse ou ouvrir un contrôle supplémentaire**
   Une prétention explicite à « testée », « soutenue » ou « obligatoire partout » exigerait un dispositif réellement discriminant et, pour la promotion transverse, un contrôle de transport dans des situations suffisamment différentes. Une anomalie, un coût ou un contre-cas pourrait également faire monter le niveau d'analyse.

5. **Condition de silence / non-déclenchement**
   Usage ordinaire de la pratique, sans prétention probatoire ni promotion : R-041 dit de ne pas déclencher une expérimentation lourde dans ce cas.

6. **Condition d'arrêt**
   L'arrêt est atteint dès que le statut disponible est correctement explicité : **appliquée/observée sans incident, mais non testée**. Sans preuve discriminante supplémentaire, aucune promotion probatoire ne suit.

7. **Pièces effectivement consultées pour ce cas**
   `00_REPRISE/cas_2_pratique.md` ; `00_REPRISE/guide_reprise.md` ; `AGENTS.md` ; `README.md`.
   Aucune issue consultée.

---

## Cas 3 — résolution du rouge de persistance C7-C1

1. **Ce que je ferais maintenant**
   Je conserverais trois niveaux séparés : la **correction locale** du contrat `weight_sum == budget`, la **connaissance causale** selon laquelle ce rouge provenait du contrat/source, et un éventuel **apprentissage transférable** qui reste à démontrer. La cause locale et sa correction restent qualifiées comme telles.
   Je noterais aussi que le principe général immédiatement légitime existe déjà dans `AGENTS.md` : un rouge machine peut venir du harness, de la spécification ou de l'environnement et sa cause doit être reproduite avant attribution au candidat scientifique. Il n'est donc pas nécessaire de fabriquer une nouvelle règle générale à partir de ce seul incident.

2. **Ce que je ne ferais pas encore**
   Je ne généraliserais pas le défaut particulier `weight_sum == budget` à tous les futurs rouges computationnels et je ne construirais ni ne consacrerais un outil transverse commun à tous les cycles sur la seule base de cet incident. Je ne convertirais pas non plus la résolution technique en qualification scientifique de RUN1 : le README du Cycle 7 maintient explicitement `RUN1_SCIENTIFIC_QUALIFICATION = NON`, `SCI1 = NON_QUALIFIABLE` et `NEW_SAMPLING = NON_AUTORISE`.

3. **Faits et sources qui justifient la décision**
   Le cas établit une cause reproduite source/contrat, l'absence de `RUN1_DISK_LOSS` établi et l'absence de qualification scientifique.  Le README vivant confirme ces bornes.
   R-042 demande de distinguer correction locale, connaissance causale et apprentissage transférable et refuse de transformer tout correctif en règle. R-024 exige, avant généralisation d'un outil, usage répétable, périmètre compréhensible et gain supérieur aux coûts de documentation, maintenance et apprentissage.

4. **Ce qui ferait changer de niveau d'analyse ou ouvrir un contrôle supplémentaire**
   Un nouvel incident suffisamment comparable, ou une récurrence montrant que la même classe causale traverse plusieurs contextes, pourrait déclencher un test de transport. Pour un outil transverse, il faudrait en plus démontrer un besoin réutilisable et comparer le gain aux coûts.

5. **Condition de silence / non-déclenchement**
   Si l'erreur reste locale, déterministe et sans valeur de réutilisation distincte, R-042 dit de ne pas déclencher de remontée. De même, un outil one-shot sans besoin réutilisable relève du silence de R-024.

6. **Condition d'arrêt**
   Arrêt dès qu'il est établi qu'aucune valeur de reprise distincte n'est démontrée au-delà de la connaissance déjà portée par les règles existantes. Ici, le principe transverse utile — reproduire la cause d'un rouge machine avant attribution scientifique — est déjà présent dans `AGENTS.md`; la spécificité `weight_sum == budget` peut donc rester locale tant que son transport n'est pas démontré.

7. **Pièces effectivement consultées pour ce cas**
   `00_REPRISE/cas_3_resolution.md` ; `00_REPRISE/guide_reprise.md` ; `AGENTS.md` ; `02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/README.md`.
   Aucune issue consultée.

---

## Cas 4 — ancien audit local et nouvelle portée

1. **Ce que je ferais maintenant**
   Je conserverais `A-C7-C1` et ses preuves comme audit local, sans invalider sa conclusion locale, mais je refuserais son utilisation **directe** comme soutien suffisant pour une décision au niveau du Cycle 7 entier. Je déclencherais seulement l'analyse ciblée de la dépendance de ses prémisses, exclusions, critères et portée au changement de contexte. R-014 prévoit exactement ce régime.
   Le changement de portée est matériel : le README vivant indique que le Cycle 7 comprend aussi `C7-GAL / C0`, ligne active et indépendante de `C7-C1`.

2. **Ce que je ne ferais pas encore**
   Je ne déclarerais pas l'ancien audit « faux » ou obsolète ; je ne le déclarerais pas non plus suffisant pour le cycle entier. Je ne referais pas automatiquement tout l'audit et je ne lancerais pas une récursion d'audits de second ordre.

3. **Faits et sources qui justifient la décision**
   `A-C7-C1` répondait à une question explicitement limitée à la prochaine action dans `C7-C1`, et le cas précise que ses preuves locales ne sont pas remises en cause.
   Le nouvel usage porte sur **tout le Cycle 7**, alors que celui-ci comporte deux états scientifiques indépendants.  R-014 stipule qu'un audit antérieur est conservé mais que sa suffisance contextuelle pour un nouveau programme n'est ni validée ni invalidée automatiquement ; un réaudit ciblé est justifié lorsqu'une prémisse, exclusion, critère ou portée peut être touché. R-040 et R-010 bornent ensuite le contrôle du changement de représentation et l'éventuel second ordre.

4. **Ce qui ferait changer de niveau d'analyse ou ouvrir un contrôle supplémentaire**
   Si l'analyse ciblée établit qu'une prémisse, exclusion ou critère de `A-C7-C1` a effectivement servi comme prémisse aval pour la décision Cycle 7 et que l'ajout de `C7-GAL` crée un delta matériel, un contrôle de second ordre ciblé est justifié. Si l'exercice devient un audit/synthèse de portée globale du cycle, les exigences de contre-audit indépendant de R-011 peuvent alors devenir pertinentes.
   Si une décision exige ensuite l'état mouvant détaillé de `C7-GAL` ou `C7-C1`, l'issue active correspondante deviendrait nécessaire. Ce seuil n'est pas atteint pour constater le défaut de portée actuel.

5. **Condition de silence / non-déclenchement**
   R-014 prévoit le silence lorsque le nouveau contexte n'a aucun lien matériel avec l'ancienne conclusion : celle-ci reste alors simplement locale. Cette condition n'est **pas** satisfaite pour une extrapolation au Cycle 7 entier, car le changement touche directement la portée et introduit une ligne scientifique indépendante.

6. **Condition d'arrêt**
   Le contrôle ciblé doit s'arrêter dès que l'effet du changement de portée sur les prémisses et l'usage aval est qualifié ; si aucune nouvelle information discriminante n'apparaît, R-010 impose le retour au travail principal plutôt qu'une récursion d'audits.
   Dans les informations accessibles ici, **l'effet exact sur les prémisses et critères propres à `A-C7-C1` manque**. Le cas ne fournit ni chemin de fichier vers cet audit ni issue explicitement liée permettant d'en consulter le contenu. Je ne le reconstruis donc pas.

7. **Pièces effectivement consultées pour ce cas**
   `00_REPRISE/cas_4_audit.md` ; `00_REPRISE/guide_reprise.md` ; `AGENTS.md` ; `README.md` ; `02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/README.md`.
   Aucune issue consultée.

## Journal de navigation

1. `00_REPRISE/README.md` — lecture de la mission, du périmètre autorisé et de la sortie attendue.
2. `AGENTS.md` — règles d'autorité, séparation science/machine, routage et limites des promotions.
3. `README.md` — objet du dépôt, distinction constance/stabilisation et routage de l'état courant.
4. `00_REPRISE/guide_reprise.md` — critères R-008 à R-042 nécessaires à l'instruction des quatre situations.
5. `00_REPRISE/cas_1_representation.md` — faits et proposition du cas de représentation.
6. `00_REPRISE/cas_2_pratique.md` — faits et proposition de qualification/promotion de la pratique.
7. `00_REPRISE/cas_3_resolution.md` — faits de la résolution locale et proposition de généralisation.
8. `00_REPRISE/cas_4_audit.md` — portée de l'audit antérieur et nouvel usage proposé.
9. `02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/README.md` — vérification discriminante de l'état vivant du Cycle 7 et de l'indépendance `C7-C1` / `C7-GAL`.

**Issues consultées : aucune.** Les issues `#119` et `#120` ont été aperçues comme ancrages actifs, mais non ouvertes : leurs détails n'étaient pas nécessaires pour borner les quatre décisions.

## Bilan de reprise

**Trois distinctions les plus importantes pour éviter une mauvaise action :**

1. **Exactitude locale ≠ suffisance représentationnelle aval.** Une synthèse correcte de `C7-C1` ne représente pas le Cycle 7 lorsque `C7-GAL` est une ligne active indépendante. R-040 est ici décisif.
2. **Application favorable ≠ test ≠ promotion.** Trois usages sans incident ne fournissent pas les observations discriminantes exigées par R-041 et ne justifient pas une obligation transverse.
3. **Correction locale ≠ apprentissage transférable ≠ règle/outil transverse.** R-042 et R-024 imposent un test de transport et une justification fonctionnelle avant toute généralisation.

**Détour documentaire le moins utile :** aucun détour significatif. Chaque fichier ouvert faisait partie du parcours imposé ou a apporté l'information discriminante nécessaire. En particulier, je n'ai pas ouvert `#119`, `#120`, les pièces historiques ni le dossier computationnel local, car les informations déjà disponibles suffisaient.

**Information manquante :** le contenu détaillé de `A-C7-C1`, notamment la dépendance exacte de ses prémisses, exclusions et critères à sa portée locale. Aucun chemin de fichier ni lien d'issue explicite vers cet audit n'est fourni dans le cas ; cette information n'a pas été reconstruite.

**Point précis d'arrêt de la navigation :** la lecture de `02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/README.md`. Elle établit que le Cycle 7 possède deux lignes actives, indépendantes et porteuses d'états distincts, tout en confirmant les bornes de `C7-C1`. Combinée aux règles R-009/R-040, R-041, R-042/R-024 et R-014/R-010 déjà lues, cette information suffisait à instruire les quatre cas sans ouvrir les issues ni la provenance historique.
