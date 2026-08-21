## Décision

**`AMENDER_PUIS_RETESTER`**

La branche expérimentale répond à un défaut réel, mais elle mélange deux corrections de routage relativement légères avec une représentation globale de l’état des dix cycles qui réintroduit précisément un coût de synchronisation que les requalifications ultérieures ont identifié comme problématique. Elle ne mérite donc ni d’être abandonnée, ni d’être retestée inchangée.

### 1. Delta réel par rapport à `main@c9deaf1…`

La branche est à **3 commits au-dessus** de la base, sans retard, et ne modifie que deux fichiers :

- `README.md` : **+3 / -1** ;
- `02_CYCLES_PHYSIQUES/README.md` : **+19**.

Dans le README racine, elle fait deux choses.

Premièrement, elle avertit que le README philosophie conserve encore un état programmatique de juillet 2026 et que ses mentions de chantier actif, branche de travail et prochaine opération ne suffisent pas à établir l’état courant. C’est une correction locale de lecture : empêcher qu’un marqueur historiquement vrai soit pris pour une autorité opérationnelle actuelle.

Deuxièmement, elle ajoute qu’une issue longue peut avoir un corps d’ouverture devenu historiquement conservé tandis que des commentaires ultérieurs changent l’état de reprise, et demande alors de rechercher le dernier checkpoint explicitement courant, terminal ou correctif.

Dans l’accueil des cycles, elle ajoute une section **« État de reprise des recherches »** qui introduit trois régimes — activité opérationnelle, question vivante sans opération sélectionnée, périmètre clos/suspendu — puis donne un état de reprise pour chacun des dix cycles. Elle précise elle-même que cette vue doit être **resynchronisée** à chaque changement de l’état d’un cycle.

### 2. Les frictions visées sont réelles

Le diagnostic sous-jacent ne doit pas être rejeté au motif que le paquet est expérimental.

D’abord, la requalification ultérieure sur `main` dit explicitement que la **reconstruction de l’état des recherches scientifiques vivantes** avait été identifiée comme une dimension insuffisamment transmise entre deux phases de travail. Le besoin de mieux transmettre « qu’est-ce qui est réellement reprenable maintenant ? » est donc documenté ; ce n’est pas une invention de la branche.

Ensuite, l’archéologie a retrouvé un problème plus ancien de contexte agentique : fournir assez d’état et de généalogie pour qu’un nouvel agent ne se perde pas, sans créer une seconde représentation totale du projet ni le préorienter excessivement. Elle a également requalifié les anciens prototypes Human-First comme des prototypes ou des observations situées, pas comme des cibles automatiquement ratifiées.

Enfin, les requalifications de `#135` établissent que **corps principal seul** et **suite de checkpoints seule** ont chacun une faiblesse réelle. Le corps peut être intelligible mais incomplet ; les checkpoints gardent utilement les corrections sans effacer l’histoire, mais leur accumulation transforme la reprise en lecture croissante des commentaires. La conclusion provisoire est très précise : l’ancrage principal doit pouvoir porter un état courant suffisamment complet et les checkpoints ne doivent pas devenir le seul moyen de connaître le courant.

Donc le défaut que cherche à corriger la branche existe bien.

### 3. Mais la preuve ne soutient pas la branche telle quelle

C’est ici que le statut probatoire baisse.

Je n’ai pas retrouvé, dans les surfaces autorisées, une preuve permettant de dire que **ce delta précis** — et notamment le tableau des dix cycles — a subi un test contrôlé répondant aux quatre éléments requis : effet attendu pré-engagé, critère d’échec/coût, comparaison ou contre-cas, observation discriminante. L’existence de la branche, son intitulé `reprise-blind`, les précédents Human-First et une application favorable ne suffisent pas à lui donner le statut de règle testée.

Les essais antérieurs sont néanmoins informatifs : reconstruction aveugle pour réduire l’auto-confirmation, tests de sur-ouverture **et** de sur-fermeture, transfert inter-domaine capable de conclure « pas de nouvelle couche nécessaire ». L’archéologie les conserve comme fonctions ou falsificateurs utiles, tout en refusant de les transformer en procédures universelles.

La requalification la plus importante pour cette branche est ultérieure : `#135` conclut que les checkpoints ont une utilité réelle pour la généalogie, mais que **« checkpoint successif comme état courant » a un coût cumulatif**. Cela touche directement la nouvelle phrase du README qui demande de retrouver le dernier checkpoint comme état opérationnel. La phrase vise le bon problème, mais sa solution est devenue trop forte au regard de l’expérience suivante.

### 4. Sous-correction et sur-correction ne sont pas symétriquement nulles

**Sous-corriger**, c’est conserver `main` exactement comme aujourd’hui. Ce choix laisse subsister un risque suffisamment observé : un lecteur peut atteindre une pièce vraie mais historiquement située et manquer l’état de reprise réellement courant. Le besoin de transmission de l’état vivant reste explicitement ouvert sur `main`.

Mais **sur-corriger**, c’est transformer ce besoin en second tableau de bord transverse. C’est ce que fait la table des dix cycles.

Le `main` de référence avait justement choisi une architecture plus légère : le README racine donne l’objet et le routage, les accueils locaux portent l’état scientifique local, les issues actives portent les portes, autorisations et blocages mouvants, Git porte la généalogie. Il dit explicitement vouloir éviter de dupliquer un tableau de bord détaillé dans chaque accueil. L’accueil des cycles dit de même que les synthèses, rapports et issues doivent porter l’état détaillé plutôt que transformer l’accueil en tableau de bord global.

La branche ajoute précisément une surface dérivée des dix états et reconnaît qu’elle doit être resynchronisée. Ce n’est pas un coût théorique : `#135` a retrouvé un épisode où une promotion locale a entraîné la resynchronisation de **huit fichiers**, puis CI, audit de pré-promotion et validation humaine ; la chaîne « propagation → désynchronisations/statuts faux → nouvelle resynchronisation » est donc observée.

La fonction utile de la table est réelle ; son **support** est excessif.

### 5. Amendement recommandé avant tout nouveau test

Je conserverais la première correction du README racine sur le volet philosophie : elle est locale, directement liée à une surface historiquement trompeuse et ne crée pratiquement pas de nouvel état à maintenir.

Je conserverais aussi la fonction de la correction concernant les issues longues, mais **pas sa formulation actuelle comme heuristique “dernier checkpoint = courant”**. Elle devrait plutôt exprimer :

**ancrage vivant courant d’abord ; checkpoint correctif pour retrouver une transition lorsque l’ancrage n’a pas encore été reconsolidé ; accumulation de checkpoints = signal qu’une reconsolidation est nécessaire.**

C’est exactement la direction soutenue par la requalification ultérieure : état courant dans l’ancrage principal, généalogie distincte seulement lorsqu’elle achète une information supplémentaire.

En revanche, je supprimerais ou réduirais fortement le tableau des dix cycles **avant** le nouveau test. Une correction plus petite peut protéger la même fonction : expliquer en quelques lignes que `résultat/synthèse existant ≠ opération actuellement sélectionnée`, que les états actif / vivant mais dormant / clos-suspendu doivent être distingués lorsqu’ils comptent pour la reprise, puis router vers l’accueil ou l’issue vivante de chaque cycle pour le statut courant et les conditions de réouverture.

Autrement dit : **conserver la distinction, ne pas recopier ses dix valeurs courantes**.

C’est une réduction de la solution, pas un abandon de son diagnostic.

### 6. Pourquoi ce n’est pas `RETESTER_INCHANGE`

Le fait matériel qui empêche ce verdict est la requalification ultérieure combinée :

- checkpoints : fonction réelle, mais coût cumulatif s’ils deviennent le support du courant ;
- synchronisation globale : fonction de routage plausible, mais churn et désynchronisation observables ;
- l’état scientifique vivant doit pourtant mieux être transmis.

Tester inchangée une solution dont deux mécanismes ont déjà reçu une objection discriminante postérieure serait gaspiller le prochain test.

Le fait qui m’aurait fait choisir l’alternative la plus proche, **`RETESTER_INCHANGE`**, aurait été une trace montrant que, dans un test aveugle contrôlé, **le tableau explicite des dix cycles** — et non simplement la distinction de régimes plus un bon routage — était nécessaire pour éviter une erreur de reprise, avec un critère de coût/resynchronisation également pré-engagé. Je n’ai pas trouvé cette preuve.

### 7. Ce qui devra rouvrir après le prochain test

Après amendement, le test doit porter sur une question beaucoup plus discriminante que « le texte est-il plus clair ? » :

> un lecteur nouveau peut-il déterminer correctement ce qui est actuellement actionnable, dormant, clos/suspendu et où se trouve l’autorité courante, sans tableau global périssable et sans transformer la chronologie des checkpoints en état courant ?

Trois sorties suffisent.

Si le routage allégé permet une reprise correcte sur des cas actifs **et** dormants/clos, le tableau global ne mérite pas de revenir.

Si des erreurs reproductibles subsistent parce que l’information nécessaire est dispersée au point que le routage ne suffit pas, il faut rouvrir une représentation transverse — mais seulement pour les dimensions précisément manquantes, pas automatiquement pour dix mini-synthèses de cycle.

Si le lecteur continue à choisir mécaniquement « le dernier commentaire » comme autorité, il faut encore réduire ou reformuler la règle de checkpoint et privilégier la reconsolidation de l’ancrage principal.

Le paquet possède donc une **observation fondatrice crédible**, mais pas encore une **forme documentaire qualifiée**. C’est exactement la situation où l’amendement précède utilement le retest.

---

MATRICE\_LUE = OUI

SOURCES\_REELLEMENT\_UTILISEES = `main@c9deaf1fe86b742d9227f0385e975809f64dc9bd` (`README.md`, `02_CYCLES_PHYSIQUES/README.md`) ; `test/human-first-reprise-blind-20260819` (mêmes deux fichiers et comparaison de branche) ; issues/commentaires autorisés de `main`, principalement #104, #118 et #135, avec les épisodes de reprise qu’ils reconstruisent ; les trois fichiers du paquet d’audit uniquement comme cadrage/contrôle, jamais comme preuve factuelle du dépôt.

FONCTIONS\_ACTIVEES = stale état programmatique / corps d’issue historiquement conservé -> risque de prendre une trace vraie pour l’autorité courante -> R-004/R-005 + R-006 -> conserver une correction locale de routage ; accumulation de checkpoints -> état courant difficile à reconstruire -> R-008 -> amender la règle « dernier checkpoint » vers ancrage courant reconsolidé + checkpoints généalogiques ; tableau des dix cycles prétendant représenter l’état de reprise -> R-009 + R-040 -> exiger fidélité d’état séparément de l’intelligibilité ; besoin Human-First pour nouveau lecteur -> R-039 -> conserver langage naturel et distinction actif/dormant/clos ; revendication implicite de solution éprouvée -> R-041 -> statut probatoire insuffisant pour retest inchangé/promotion ; nouvelle surface transverse à resynchroniser -> R-017 -> préférer le routage plus léger ; portée globale du tableau et risque sous/sur-correction -> R-011/R-015 -> ne pas conclure à partir des seuls cas favorables.

FONCTIONS\_VOISINES\_LAISSEES\_SILENCIEUSES = R-010/R-014 : les requalifications ultérieures ont été utilisées pour réévaluer directement le statut probatoire via R-041, mais elles ne justifient pas ici un nouvel audit de second ordre de tout le système de règles ou du corpus scientifique.

INFORMATIONS\_MANQUANTES\_BLOQUANTES = AUCUNE pour décider `AMENDER_PUIS_RETESTER`.

INFORMATIONS\_MANQUANTES\_NON\_BLOQUANTES = trace brute et pré-engagement complet du test aveugle spécifique ayant produit cette branche = NON\_ETABLI ; nécessité propre du tableau explicite des dix cycles par rapport à un routage plus léger = NON\_ETABLIE ; fidélité actuelle ligne par ligne de chacun des dix états de la table = NON\_ETABLIE dans cette mission et non nécessaire au verdict structurel ; ratification humaine d’une promotion de ce paquet précis = NON\_ETABLIE.

AUCUNE\_MUTATION\_EFFECTUEE = OUI