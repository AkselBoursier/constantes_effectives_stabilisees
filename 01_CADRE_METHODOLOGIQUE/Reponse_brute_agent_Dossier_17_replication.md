## Cas 1 — représentation intermédiaire

1. **Ce que je ferais maintenant :** j’ouvre le raccord de représentation `R-040` et je compare la source avec la synthèse pour qualifier précisément la recherche vivante perdue et déterminer si cette perte modifie l’usage de la phase aval. Le fait que la synthèse ait correctement répondu à sa question initiale ne suffit pas : elle peut être « localement juste » tout en étant insuffisante comme entrée aval. 
2. **Ce que je ne ferais pas encore :** je ne déclencherais pas automatiquement un audit de second ordre, et je ne reconstruirais pas exhaustivement la synthèse.
3. **Justification :** une synthèse devenue entrée d’une étape suivante déclenche `R-040`; l’état scientifique vivant fait partie de ce qui doit rester récupérable pour une reprise. Une différence de représentation doit être jugée selon son effet sur l’usage aval. 
4. **Condition de changement de niveau :** si la perte touche une prémisse, la sélection ou la capacité de détection, j’ouvre `R-010`; sinon je reviens au niveau de reprise pour rendre l’état nécessaire récupérable. 
5. **Condition de silence/non-déclenchement :** aucune escalade si la recherche omise ne constitue pas une perte pertinente pour l’usage aval. 
6. **Condition d’arrêt :** lorsque le delta source→représentation et ses effets aval sont qualifiés; côté reprise, lorsque l’état courant est récupérable et non contradictoire. 
7. **Informations utilisées :** `R-008/R-009`, `R-040`, le critère « localement juste / insuffisant pour l’aval », et la boucle représentation→audit→reprise. 

## Cas 2 — pratique répétée sans incident

1. **Ce que je ferais maintenant :** j’ouvre `R-041` parce qu’une prétention probatoire (« testée ») et un projet d’extension sont formulés. Je classe les trois occurrences comme applications avec observation d’absence d’incident, mais pas comme preuve suffisante d’une mise à l’épreuve.
2. **Ce que je ne ferais pas encore :** je ne qualifierais pas la pratique de « testée » et je ne la promouvrais ni ne l’étendrais à d’autres chantiers.
3. **Justification :** le dossier dit explicitement qu’« une application sans incident ne devient pas un test » et distingue la promotion du statut probatoire. Pour monter en statut, il faut expliciter effet attendu, échec/coût, contre-cas ou comparaison, et observation discriminante. 
4. **Condition de changement de niveau :** une véritable épreuve discriminante peut faire évoluer le statut; si les preuves révèlent un biais de sélection ou un angle mort, retour vers `R-010/R-015`. 
5. **Condition de silence/non-déclenchement :** `R-041` reste silencieux pour un usage ordinaire sans prétention probatoire. Ici cette condition n’est plus remplie puisque quelqu’un propose « testée » et une extension.
6. **Condition d’arrêt :** lorsque le statut exact et les preuves disponibles sont explicites; la boucle s’arrête également si aucun nouveau discriminant n’apparaît. 
7. **Informations utilisées :** `R-041`, son échelle de statut, ses exigences probatoires, la séparation entre épreuve et promotion, et le lien éventuel vers l’audit. 

## Cas 3 — résolution difficile

1. **Ce que je ferais maintenant :** j’applique `R-042` : je sépare explicitement la **solution locale**, la **connaissance causale** désormais comprise et l’**apprentissage candidat** éventuellement transportable. Je rends la connaissance causale récupérable sur la surface existante la moins coûteuse appropriée; le dossier ne permet pas d’identifier ici quelle surface concrète il s’agit.
2. **Ce que je ne ferais pas encore :** je ne transformerais pas ce cas en règle transverse, outil ou mécanisme général, et je ne considérerais pas la pertinence possible ailleurs comme une preuve de transport.
3. **Justification :** une résolution coûteuse et causalement informative déclenche `R-042`, mais le transport est conditionnel et l’apprentissage ne devient pas automatiquement une règle.  
4. **Condition de changement de niveau :** si cette connaissance est nécessaire à la reprise, passage vers `R-008`; si un mécanisme ou un outillage transverse est envisagé, le dossier pointe vers `R-024`, mais n’en donne pas ici la procédure. Tout transport doit d’abord être éprouvé.  
5. **Condition de silence/non-déclenchement :** pas de mécanisme transverse tant que la portée hors du cas présent n’a pas été testée; ne pas promouvoir chaque correctif en règle.
6. **Condition d’arrêt :** `R-042` prévoit l’arrêt s’il n’existe aucune valeur de reprise distincte ou si la connaissance est déjà portée. 
7. **Informations utilisées :** `R-042`, la distinction solution/connaissance/apprentissage candidat, le transport conditionnel, la boucle résolution→connaissance→reprise et le pointeur vers `R-024`. 

## Cas 4 — ancien audit et nouveau contexte

1. **Ce que je ferais maintenant :** je déterminerais d’abord si le nouvel élément **touche réellement** la prémisse concernée. Le dossier ne décrit pas plus finement la procédure de cette qualification préalable. Je conserverais parallèlement les preuves locales de l’ancien audit.
2. **Ce que je ne ferais pas encore :** je n’annulerais pas l’ancien audit et je ne lancerais pas automatiquement un réaudit complet sur la seule possibilité d’un effet.
3. **Justification :** les preuves locales ne sont pas annulées automatiquement; surtout, `R-014 → R-010` précise qu’un ancien audit n’est réaudité que si le nouveau contexte touche réellement une prémisse, une exclusion, un critère ou la portée.  
4. **Condition de changement de niveau :** si l’effet est confirmé sur la prémisse — ou sur une exclusion, un critère ou la portée — j’ouvre `R-010` et réaudite ce que le dispositif pouvait manquer, y compris la sélection d’entrée si nécessaire.
5. **Condition de silence/non-déclenchement :** si le nouvel élément ne modifie finalement aucune prémisse, exclusion, critère ou portée pertinente, pas de réaudit. Le dossier exclut la réflexivité continue. 
6. **Condition d’arrêt :** si l’examen montre qu’aucune condition de déclenchement n’est réellement touchée, l’escalade s’arrête. Si un audit global est effectivement ouvert, son arrêt exige un contre-échantillon indépendant et l’absence de nouvelle famille discriminante. 
7. **Informations utilisées :** `R-010/R-011/R-014/R-015`, la conservation des preuves locales, le déclenchement conditionné par une atteinte réelle aux prémisses/exclusions/critères/portée et les règles d’arrêt du second ordre. 

### Trois distinctions les plus importantes

* **Justesse locale d’une représentation ≠ suffisance pour son usage aval.**
* **Application sans incident ≠ mise à l’épreuve probante ≠ promotion.**
* **Connaissance causale issue d’une résolution ≠ apprentissage transportable ≠ règle transverse.** 

### Point ayant le plus obligé à revenir à la source

Le cas 4 : il fallait distinguer « pourrait affecter une prémisse » de « touche réellement une prémisse ». Le repère `R-014 → R-010` impose explicitement cette seconde condition avant le réaudit. 

### Ambiguïté éventuelle

Dans le cas 4, le dossier fixe clairement **la condition** d’ouverture du réaudit, mais ne décrit pas précisément **l’opération préalable** permettant d’établir qu’un nouvel élément « touche réellement » une prémisse. Deux agents pourraient donc conduire cette qualification initiale avec des profondeurs différentes sans contredire explicitement le dossier.