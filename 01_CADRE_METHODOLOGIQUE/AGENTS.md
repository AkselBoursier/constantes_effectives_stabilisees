# Règles locales — méthodologie, méta-règles et shadow learning

Ce fichier complète le `AGENTS.md` racine pour tout travail sur la méthodologie, les règles, la gouvernance documentaire, la reprise entre agents et le shadow learning.

Pour le travail ordinaire, le `AGENTS.md` racine et le présent fichier doivent suffire. Ne pas imposer la relecture de l’archéologie ayant produit une règle déjà qualifiée. Consulter les anciennes issues, archives ou protocoles seulement pour auditer, contester, étendre ou requalifier une règle.

## 1. Statut d’une règle

Ne pas confondre :

```text
règle formulée
!= régime déclaré
!= régime humainement ratifié
!= régime appliqué de facto
!= régime justifié après audit
```

Une règle rencontrée pour la première fois par l’agent n’est pas présumée nouvelle. Avant de proposer une nouvelle règle, rechercher si un antécédent pertinent existe déjà.

## 2. Application, test, promotion et extension

Une application n’est pas automatiquement un test. Lorsqu’un test probant est revendiqué, rechercher autant que possible : effet attendu avant observation, critère d’échec ou coût excessif, contre-exemple ou comparaison, observation réellement discriminante.

Une qualification locale ne doit pas être promue lorsqu’un contexte matériellement accessible et manifestement pertinent reste non instruit.

Promotion de statut et extension de périmètre sont distinctes. La prudence doit être proportionnée à l’autorité ajoutée, au saut de domaine, au coût d’erreur, à la réversibilité et à la capacité de la règle à modifier une décision substantielle.

Lorsqu’une règle paraît utile, distinguer sa fonction de son mécanisme : intention utile, effet réellement produit, utilité nette, nécessité d’une règle explicite et nécessité de conserver cette fonction sous forme de règle sont des questions différentes. Si une fonction utile peut être portée plus simplement par Git, CI, un workflow, un état natif ou un autre mécanisme sans déplacer un jugement scientifique, considérer cette migration séparément.

## 3. Sur-extension et sous-application

Chercher symétriquement les règles appliquées trop largement et celles comprises trop localement, sous-appliquées ou retirées trop tôt. Rechercher aussi les occasions manquées et les garde-fous perdus lors d’une reformulation.

Le bon régime n’est ni global ni local par défaut.

## 4. Localiser avant d’intervenir

Lorsqu’une correction est envisagée mais que le niveau causal ou fonctionnel n’est pas établi, identifier d’abord le niveau qui produit réellement le défaut par le contrôle discriminant le moins coûteux, puis redescendre vers l’intervention minimale.

Ne pas dézoomer par principe. Si un discriminant local suffit déjà, intervenir localement. Si les corrections locales échouent ou si la friction se répète, remonter jusqu’au premier niveau causal testable.

Ne pas ouvrir un audit de l’audit supplémentaire sans anomalie précise ou gain attendu identifiable.

## 5. Couplage probatoire

Lorsqu’une propriété d’un objet réel est inférée depuis un toy, mock, proxy, fallback, harnais, conversion, extraction ou autre représentation indirecte, vérifier que le dispositif exerce effectivement la propriété revendiquée et que l’équivalence nécessaire est établie au niveau exact de l’usage.

Ne pas ajouter un contre-test coûteux lorsque la propriété ou l’équivalence pertinente est déjà directement établie.

## 6. Autoréflexion bornée

Une réflexivité bornée peut être utilisée lorsqu’un déclencheur réel apparaît, avec objet précis et condition d’arrêt.

Ne pas en déduire que l’autoréflexion continue, l’auto-déclenchement à chaque tâche, un déclencheur universel ou la supériorité générale du mode borné sont établis.

L’autoréflexion doit corriger le travail principal, pas devenir un chantier parallèle permanent.

## 7. Intelligibilité humaine

Nommer d’abord l’objet en langage naturel ; utiliser codes et sigles comme repères secondaires ; ré-expliciter le référent aux frontières de contexte lorsque nécessaire.

Une notation compacte reste légitime lorsqu’elle apporte un gain réel de précision ou de charge cognitive et que son référent demeure récupérable.

Présenter l’état courant par défaut. Réintroduire l’état antérieur lorsque comparaison temporelle, provenance, décision, réinstruction ou compréhension du changement constitue l’objet du travail.

## 8. État courant et checkpoints

Un chantier doit posséder un ancrage principal permettant de connaître suffisamment vite son état courant.

Les checkpoints successifs servent aux transitions ayant une valeur réelle de reprise ou de généalogie. Ne pas écraser un checkpoint ancien et ne pas faire des checkpoints le seul moyen de reconstruire le présent.

Créer ou mettre à jour un checkpoint lorsqu’un changement modifie substantiellement statut, régime, portée, soutien probatoire, contre-cas, décision ou prochaine opération. Une répétition sans changement d’état n’exige pas automatiquement un nouveau checkpoint.

Lorsqu’une longue issue ou PR sert de point de reprise, rechercher les checkpoints correctifs, terminaux ou explicitement courants avant d’inférer le dernier état applicable.

## 9. Non-prolifération proportionnée

La non-prolifération n’est pas un veto à la création.

Créer un document, une issue, une PR, un checkpoint ou une autre couche lorsqu’une fonction identifiable le justifie : récupération de contexte, identité propre, comparaison, preuve, décision, traçabilité, contrôle ou réduction réelle de charge.

Ne pas créer un artefact seulement parce qu’une idée existe. Ne pas refuser un artefact utile seulement parce qu’un support existant pourrait théoriquement contenir davantage d’information.

## 10. Capture légère hors périmètre

Lorsqu’une idée hors périmètre possède une valeur de reprise identifiable et un risque réel d’être perdue, la rendre récupérable dans le support existant le plus léger.

Créer un objet distinct seulement si sa fonction exige une identité propre. Une capture ne crée ni priorité ni obligation de résolution immédiate.

## 11. Interventions humaines

Une intervention humaine n’est pas automatiquement un ordre. Lorsque cela change l’action, distinguer observation, hypothèse, proposition, préférence, décision et autorisation.

Une décision ou autorisation explicite s’applique dans son périmètre sans être neutralisée au prétexte qu’une nouvelle évaluation serait possible, et sans être généralisée silencieusement au-delà de ce périmètre.

## 12. Mutations techniques

Avant une mutation : identifier la cible réelle et la fonction recherchée ; lire l’état courant et le SHA si un objet existant est modifié ; choisir l’action correspondant à la cible ; éviter les mutations sans effet matériel ; contrôler le résultat final.

Une mutation réversible peut servir de test ou de preuve lorsqu’elle est confinée et explicitement qualifiée comme telle.

## 13. Shadow learning — état courant

Les règles inscrites ci-dessus sont applicables dans leur régime sans exiger la lecture de leur histoire.

Restent à observer ou instruire avant promotion générale : autoréflexion continue ou auto-déclenchée ; seuil numérique universel de shadow learning ; automatisation générale du shadow ; cycle de vie universel ou clôture automatique des PR ; obligation générale d’horodatage prospectif ; toute extension transversale dont le régime n’est pas encore établi.
