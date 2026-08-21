## Cas 1 — représentation intermédiaire

1. **Maintenant :** j’ouvre un **raccord de représentation `R-040`** et je compare la source à la synthèse pour qualifier la recherche vivante omise et vérifier si cette perte modifie l’usage aval. Une synthèse peut être correcte pour sa fonction initiale tout en étant insuffisante comme entrée de l’étape suivante. 
2. **Pas encore :** je ne lance pas automatiquement un audit de second ordre et je ne conclus pas que la synthèse est globalement fausse.
3. **Justification :** le dossier distingue explicitement « localement juste » et « insuffisant pour l’aval » ; la proximité entre éléments ne vaut ni autorisation ni promotion. 
4. **Changement de niveau :** j’ouvre `R-010` si la perte touche une **prémisse, la sélection ou la capacité de détection** ; une perte d’état vivant peut aussi déclencher ce second ordre.  
5. **Silence / non-déclenchement :** pas d’audit supplémentaire si aucune perte n’est pertinente pour l’usage aval.
6. **Arrêt :** lorsque le delta source → représentation et ses effets aval sont qualifiés ; si nécessaire, retour ensuite vers la reprise courante. 
7. **Informations utilisées :** `R-008/R-009`, `R-040`, la boucle représentation → audit → reprise, et le repère `R-009 → R-010`. 

## Cas 2 — pratique répétée sans incident

1. **Maintenant :** puisque quelqu’un veut qualifier la pratique de « testée » et l’étendre, j’ouvre `R-041` et j’explicite l’effet attendu, l’échec ou le coût, un contre-cas ou une comparaison, et l’observation qui serait discriminante. 
2. **Pas encore :** je ne la déclare ni « testée », ni validée, ni promue sur la seule base de trois applications sans incident.
3. **Justification :** le dossier dit explicitement qu’**une application sans incident ne devient pas un test** et que la promotion reste une décision extérieure. 
4. **Changement de niveau :** si l’examen probatoire révèle un biais de sélection ou un angle mort, je retourne vers l’audit de second ordre `R-010/R-015`. 
5. **Silence / non-déclenchement :** `R-041` reste silencieux lors d’un usage ordinaire sans prétention probatoire ; ce silence ne s’applique plus ici puisque la qualification « testée » et l’extension sont proposées.
6. **Arrêt :** lorsque le statut de la pratique et les preuves disponibles sont explicites ; la boucle s’arrête si aucun nouveau discriminant n’apparaît.  
7. **Informations utilisées :** `R-041`, la boucle pratique → épreuve → statut, et le principe selon lequel succès, mauvais cas et coûts contribuent au statut sans auto-promotion. 

## Cas 3 — résolution difficile

1. **Maintenant :** j’ouvre `R-042` et je sépare explicitement **solution locale**, **connaissance causale** et **apprentissage candidat**. Je rends la connaissance causale récupérable sur la surface existante la moins coûteuse si elle présente une valeur de reprise. 
2. **Pas encore :** je ne transforme pas cette résolution en règle, mécanisme transverse ou pratique générale, puisque son transport hors du cas n’est pas établi.
3. **Justification :** le transport est conditionnel et doit être éprouvé ; le dossier précise qu’un apprentissage ne devient pas automatiquement une règle.  
4. **Changement de niveau :** vers `R-008` si cette connaissance devient nécessaire à la reprise ; vers `R-024` seulement si un mécanisme ou un outillage transverse est envisagé **après test de transport et comparaison du support**.  
5. **Silence / non-déclenchement :** pas de mécanisme transverse tant que la portée hors du cas n’a pas été éprouvée ; une simple possibilité reste distincte d’une connaissance causale remontée. 
6. **Arrêt :** si la résolution n’a aucune valeur de reprise distincte ou si la connaissance est déjà portée ailleurs ; ne pas transformer chaque correctif en règle. 
7. **Informations utilisées :** `R-042`, la boucle résolution → connaissance → reprise, et les repères `R-042 → R-018` / `R-042 → R-024`. 

## Cas 4 — ancien audit et nouveau contexte

1. **Maintenant :** je détermine d’abord si le nouvel élément **touche réellement** une prémisse, une exclusion, un critère ou la portée de l’ancien audit. Je conserve entre-temps les preuves locales qui restent valides.  
2. **Pas encore :** je n’annule pas l’ancien audit et je ne lance pas un réaudit complet sur la seule possibilité d’un effet.
3. **Justification :** le second ordre peut conserver, requalifier ou borner un audit, sans annuler automatiquement ses preuves locales ; un ancien audit n’est réaudité que si le nouveau contexte touche réellement ses prémisses, exclusions, critères ou portée.  
4. **Changement de niveau :** si cette atteinte est établie, j’ouvre `R-010` et réaudite ce que le dispositif pouvait manquer, y compris la sélection d’entrée si l’audit est global.  
5. **Silence / non-déclenchement :** pas de réflexivité continue ni de réaudit si aucune prémisse, exclusion, critère ou portée n’a réellement changé.
6. **Arrêt :** si l’effet du nouvel élément s’avère ne pas toucher ces dimensions, arrêt sans réaudit. Si un **audit global** est effectivement ouvert, arrêt après contre-échantillon indépendant et absence de nouvelle famille discriminante. 
7. **Informations utilisées :** `R-010/R-011/R-014/R-015`, le maintien des preuves locales, le seuil de réaudit et la condition particulière d’arrêt d’un audit global.

### Trois distinctions les plus importantes

* **Correct localement ≠ suffisant pour l’usage aval.** 
* **Application sans incident ≠ mise à l’épreuve probante.** 
* **Validité des preuves locales ≠ maintien automatique de la portée ou des prémisses d’un audit.** 

### Point ayant le plus obligé à revenir à la source

Le **cas 4**, pour distinguer « un élément qui *pourrait* affecter une prémisse » du seuil formulé par le dossier : un ancien audit n’est réaudité que si le nouveau contexte la **touche réellement**. 

### Ambiguïté éventuelle

Dans le cas 1, deux agents pourraient diverger sur le moment précis où l’omission d’un état vivant devient une **« perte matérielle »** : `R-040` demande d’abord de tester si la différence change l’usage aval, tandis que le repère `R-009 → R-010` indique qu’une perte d’état vivant **peut** déclencher le second ordre. Le dossier ne fixe pas plus finement ce seuil.