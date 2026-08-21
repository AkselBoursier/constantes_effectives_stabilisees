## Cas 1 — représentation intermédiaire du Cycle 7

1. **Ce que je ferais maintenant**
   Je maintiendrais `S-C7-C1` dans son statut de représentation **localement correcte pour `C7-C1 / X(z) / SCI-1`**, mais je refuserais son emploi, inchangé et seul, comme « état courant du Cycle 7 ». Pour une décision au niveau du cycle, il faut au minimum rétablir la seconde ligne indépendante `C7-GAL / C0` et son état propre. Le raccord `source → représentation` est donc acceptable localement mais insuffisant pour l’usage aval proposé.

2. **Ce que je ne ferais pas encore**
   Je ne préparerais aucune décision de cycle entier à partir de `S-C7-C1` seule. Je ne transférerais notamment ni `SCI1 = NON_QUALIFIABLE`, ni `B1 = NON_AUTORISEE`, ni `NEW_SAMPLING = NON_AUTORISE` vers `C7-GAL`, puisque les deux lignes n’échangent ni état scientifique ni autorisation par défaut.

3. **Faits et sources qui justifient la décision**
   Le cas dit explicitement que `S-C7-C1` a été produite **uniquement** pour la reprise de `C7-C1`.  Le README vivant du Cycle 7 établit deux lignes actives et indépendantes, `C7-C1 / X(z) / SCI-1` et `C7-GAL / C0`, avec deux états scientifiques différents. `C7-GAL` possède notamment un programme ouvert, une route `LOT_C`, une fermeture matérielle encore ouverte et des portes propres.  Le guide de reprise autorise précisément la qualification « localement juste mais insuffisant pour l’aval » lorsqu'une représentation perd une dimension pertinente pour son nouvel usage.

4. **Ce qui ferait changer de niveau d’analyse ou ouvrir un contrôle supplémentaire**
   La tentative effective de faire de cette réduction une entrée de décision cycle-wide déclenche le contrôle `R-040`. Si le delta de représentation affectait ensuite une prémisse, la sélection ou la capacité de détection de l’analyse aval, un audit de second ordre `R-010` deviendrait justifié.

5. **Condition de silence ou de non-déclenchement**
   Aucun contrôle supplémentaire n’est requis si `S-C7-C1` reste utilisée uniquement pour sa fonction déclarée de reprise de `C7-C1` et qu’aucune prétention cycle-wide n’est formulée.

6. **Condition d’arrêt**
   Pour la proposition présente, l’information est suffisante dès qu’il est établi que le Cycle 7 comporte une deuxième ligne active indépendante, absente de `S-C7-C1`. Il n’est pas nécessaire d’ouvrir les issues actives pour rejeter l’équivalence « `S-C7-C1` = état courant du Cycle 7 ».

7. **Pièces effectivement consultées pour ce cas**
   `00_REPRISE/cas_1_representation.md` ; `02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/README.md` ; ainsi que les règles transverses déjà lues dans `AGENTS.md`, `README.md` et `00_REPRISE/guide_reprise.md`. Aucune issue consultée.

---

## Cas 2 — pratique répétée sans incident

1. **Ce que je ferais maintenant**
   Je qualifierais la pratique comme **formulée, appliquée trois fois et observée sans incident visible**, pas comme « testée ». Je laisserais son statut probatoire inchangé tant qu’aucune observation discriminante n’a été organisée.

2. **Ce que je ne ferais pas encore**
   Je ne la déclarerais pas « testée » et je ne la rendrais pas obligatoire pour tous les cycles physiques. Une application sans incident ne devient pas un test, et une éventuelle promotion reste distincte de l’établissement du statut probatoire.

3. **Faits et sources qui justifient la décision**
   Les seuls faits apportés sont trois usages et l’absence d’incident visible.  Le guide `R-041` exige, pour monter en statut, d’expliciter l’effet attendu, l’échec ou le coût possible, un contre-cas ou une comparaison et une observation discriminante ; il dit explicitement qu’« une application sans incident ne devient pas un test ».  `AGENTS.md` contient déjà une règle de travail apparentée : consigner les changements qui modifient substantiellement question, périmètre, résultat, blocage, validation ou décision suivante, sans documenter chaque action technique. Il précise aussi qu’une exploration ou pratique ne devient pas une règle durable sans qualification et validation.

4. **Ce qui ferait changer de niveau d’analyse ou ouvrir un contrôle supplémentaire**
   Une véritable prétention probatoire nécessiterait un contrôle `R-041` avec critères d’échec et comparaison discriminante. Si l’épreuve révélait un biais de sélection ou un angle mort dans les trois séquences observées, elle pourrait ouvrir `R-010/R-015`. Une généralisation à tous les cycles nécessiterait en plus d’établir la transportabilité et une validation humaine appropriée.

5. **Condition de silence ou de non-déclenchement**
   Un usage ordinaire de cette pratique, sans prétention à avoir démontré son efficacité et sans projet de promotion, reste silencieux : `R-041` n’a pas à être relancé à chaque emploi.

6. **Condition d’arrêt**
   L’analyse s’arrête lorsque le statut et les preuves disponibles sont explicites : ici, « appliquée trois fois, sans incident visible, mais non testée ». Sans nouveau discriminant, aucun approfondissement documentaire n’est justifié.

7. **Pièces effectivement consultées pour ce cas**
   `00_REPRISE/cas_2_pratique.md` ; `AGENTS.md` ; `00_REPRISE/guide_reprise.md`. Aucune issue consultée.

---

## Cas 3 — résolution du rouge de persistance C7-C1

1. **Ce que je ferais maintenant**
   Je séparerais les trois sorties prévues par `R-042` :

* **solution locale** : la correction du contrat `weight_sum == budget`, trop fort, reste attachée au problème C7-C1 instruit ;
* **connaissance causale** : conserver comme récupérable le fait que ce rouge précis a été reproduit au niveau source/contrat et n’établit pas une perte disque ni une qualification scientifique de RUN1 ;
* **apprentissage candidat** : seulement envisager un transport vers d’autres cas si des situations indépendantes montrent que le même mécanisme est pertinent.

2. **Ce que je ne ferais pas encore**
   Je n’en tirerais ni une nouvelle règle générique pour tous les futurs rouges computationnels, ni un outil transverse commun à tous les cycles. Le cas local ne suffit pas à établir la portée de ces deux promotions.

3. **Faits et sources qui justifient la décision**
   Le cas et le README du Cycle 7 établissent que la cause du rouge de persistance est reproduite au niveau source/contrat, que le contrat était trop fort, que `RUN1_DISK_LOSS` n’est pas établi et que la qualification scientifique reste absente.   `AGENTS.md` porte déjà la règle transverse utile : un rouge machine peut venir du harness, de la spécification ou de l’environnement ; sa cause doit être reproduite avant attribution au candidat scientifique. Il n’est donc pas nécessaire d’inventer une seconde règle générale à partir de ce seul incident.  Le guide `R-042` impose de tester le transport avant règle, outil ou mécanisme transverse.

4. **Ce qui ferait changer de niveau d’analyse ou ouvrir un contrôle supplémentaire**
   Des incidents indépendants, coûteux ou récurrents présentant le même mécanisme causal pourraient justifier un test de transport. Si un mécanisme ou outillage transverse devient réellement candidat, le guide route alors vers `R-024`, après comparaison du support approprié.

5. **Condition de silence ou de non-déclenchement**
   Pas de remontée supplémentaire si la résolution n’a pas de valeur de reprise distincte hors de C7-C1, ou si la connaissance utile est déjà portée par une surface existante. Pas de création d’une règle pour chaque correctif.

6. **Condition d’arrêt**
   Pour le cas présent, on s’arrête une fois les trois sorties séparées et la portée locale de la causalité établie. En l’absence d’un second terrain discriminant, il n’y a rien qui permette de tester honnêtement un transport générique.

7. **Pièces effectivement consultées pour ce cas**
   `00_REPRISE/cas_3_resolution.md` ; `02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/README.md` ; `AGENTS.md` ; `00_REPRISE/guide_reprise.md`. Aucune issue consultée.

---

## Cas 4 — ancien audit local et nouvelle portée

1. **Ce que je ferais maintenant**
   Je conserverais les preuves locales de `A-C7-C1` dans leur portée d’origine, mais je bloquerais son transport direct comme soutien suffisant pour une décision portant sur le Cycle 7 entier. J’ouvrirais uniquement un contrôle borné du **changement de portée et de sélection** : que faudrait-il ajouter ou ré-instruire pour passer de `C7-C1` au cycle comportant aussi `C7-GAL` ?

2. **Ce que je ne ferais pas encore**
   Je n’annulerais pas les preuves locales de l’ancien audit et je ne réauditerais pas mécaniquement tout son contenu. Inversement, je ne considérerais pas sa conclusion locale comme transportée au niveau cycle avant l’épreuve de portée.

3. **Faits et sources qui justifient la décision**
   `A-C7-C1` répondait à une question explicitement limitée à la prochaine action dans `C7-C1`, et le cas stipule que ses preuves locales ne sont pas remises en cause.  Le nouvel usage vise le **Cycle 7 entier**. Or son README vivant établit que le cycle comporte une seconde ligne active, `C7-GAL / C0`, scientifiquement indépendante de `C7-C1`.  Le guide prévoit qu’un ancien audit n’est réaudité que si le nouveau contexte touche prémisse, exclusion, critère ou portée ; ici, la portée et la sélection sont précisément modifiées. Les preuves locales peuvent donc être conservées tout en bornant l’usage élargi.

4. **Ce qui ferait changer de niveau d’analyse ou ouvrir un contrôle supplémentaire**
   Le passage de `C7-C1` à « Cycle 7 entier » suffit à justifier un audit de second ordre borné (`R-010`), notamment sur la sélection d’entrée (`R-011`) puisque `C7-GAL` constitue une famille indépendante qui n’était pas dans la question locale. Si l’on voulait ensuite mener un véritable audit global du cycle, il faudrait aussi chercher un contre-échantillon indépendant et vérifier qu’aucune nouvelle famille discriminante n’apparaît.

5. **Condition de silence ou de non-déclenchement**
   Si `A-C7-C1` reste utilisé exclusivement pour sa question et sa portée originales, et qu’aucune prémisse, exclusion, critère ou portée n’a changé, il n’y a aucune raison de le réauditer.

6. **Condition d’arrêt**
   Pour la proposition actuelle, je considère l’information suffisante dès que deux faits sont établis : l’audit est local à `C7-C1`, tandis que le Cycle 7 comporte aussi une ligne `C7-GAL` indépendante. Cela suffit à interdire le transport direct sans remettre en cause les preuves locales. Je n’ouvre donc ni les issues #119/#120 ni la provenance historique.

7. **Pièces effectivement consultées pour ce cas**
   `00_REPRISE/cas_4_audit.md` ; `02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/README.md` ; `00_REPRISE/guide_reprise.md` ; règles transverses de `AGENTS.md` et routage de `README.md`. Aucune issue consultée.

## Journal de navigation

1. `00_REPRISE/README.md` — lecture de la mission, du périmètre autorisé et de la sortie exigée.
2. `AGENTS.md` — règles d’autorité, séparation machine/science, routage et limites de promotion.
3. `README.md` — objet du dépôt, distinction constance/stabilisation et localisation de l’état courant.
4. `00_REPRISE/guide_reprise.md` — grille fonctionnelle `R-008/R-009`, `R-040`, `R-010`, `R-041`, `R-042` et conditions de silence/arrêt.
5. `00_REPRISE/cas_1_representation.md` — faits du cas de représentation.
6. `02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/README.md` — vérification discriminante des deux lignes actives indépendantes et de leurs états bornés.
7. `00_REPRISE/cas_2_pratique.md` — faits du cas de pratique répétée.
8. `00_REPRISE/cas_3_resolution.md` — faits du cas de résolution computationnelle.
9. `00_REPRISE/cas_4_audit.md` — faits du cas de changement de portée d’un audit local.

Aucune issue, pull request, autre branche, tag, commit ou historique Git n’a été consulté.

## Bilan de reprise

* **Trois distinctions déterminantes :**

  1. **justesse locale d’une représentation ≠ suffisance pour un usage aval plus large** ;
  2. **pratique appliquée sans incident ≠ pratique testée ≠ règle promue** ;
  3. **preuve locale valide ≠ transport automatique de sa conclusion vers une portée plus large**.
     À cela s’ajoute, pour le cas computationnel, la séparation essentielle entre cause d’un rouge machine, qualification scientifique et généralisation d’un correctif.

* **Détour documentaire le moins utile :** aucun détour inutile. Le seul fichier local supplémentaire ouvert au-delà du parcours imposé et des quatre cas, `02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/README.md`, fournit directement l’information discriminante commune aux cas 1 et 4 et borne aussi le cas 3.

* **Information manquante :** aucune information indispensable à l’instruction demandée. Les contenus détaillés des issues #119 et #120 pourraient devenir nécessaires pour prendre une décision opérationnelle actuelle dans chacune des deux lignes, mais ils ne sont pas nécessaires pour trancher les propositions soumises ici.

* **Point précis d’arrêt de navigation :** après lecture de `00_REPRISE/cas_4_audit.md`. À ce stade, les règles de niveau étaient déjà établies par `00_REPRISE/guide_reprise.md` et le fait discriminant — deux lignes actives indépendantes dans le Cycle 7 — avait été établi par `02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/README.md`. Aucune autorité plus profonde n’était nécessaire pour borner les quatre décisions.
