# Reprise comparative des cycles 9 et 10 — contrefactuel, dynamique et contingence

## Statut

```text
type : cinquième test comparatif après récupération des dix cycles
cycles : 9 — ajustement fin ; 10 — quasi-fixité électrofaible dynamique
question : qu'ajoute une trajectoire dynamique explicite à un audit
           contrefactuel, et à quelles conditions réduit-elle plutôt que
           déplacer la contingence ?
état : distinction établie ; résultats calculatoires locaux conservés
date : 16 juillet 2026
```

Ce document achève la série des cinq contrastes. Il compare deux opérations
qui peuvent employer les mêmes mots — variation, espace, région, trajectoire,
réglage — sans étudier le même objet.

Il ne vérifie pas à nouveau la littérature ni les calculs des deux cycles. Il
éprouve leur articulation sous les deux questions directrices du projet et
conserve leurs dettes séparées.

Documents principaux :

- cycle 9 : [cadrage de l'ajustement
  fin](../02_CYCLES_PHYSIQUES/09_Cycle_fine_tuning/cadrage-cycle-fine-tuning.md)
  et [synthèse du premier
  lot](../02_CYCLES_PHYSIQUES/09_Cycle_fine_tuning/synthese-premier-lot-fine-tuning.md) ;
- cycle 10 : [cadrage de la quasi-fixité
  électrofaible](../02_CYCLES_PHYSIQUES/10_Cycle_fixite_electrofaible_dynamique/cadrage-cycle-fixite-electrofaible-dynamique.md),
  [résultats du modèle minimal](../02_CYCLES_PHYSIQUES/10_Cycle_fixite_electrofaible_dynamique/resultats-phase2-modele-minimal.md),
  [résultats du régime quartique](../02_CYCLES_PHYSIQUES/10_Cycle_fixite_electrofaible_dynamique/resultats-phase3-regime-quartique.md)
  et [résultats du modèle
  dissipatif](../02_CYCLES_PHYSIQUES/10_Cycle_fixite_electrofaible_dynamique/resultats-phase4-toy-model-dissipatif.md).

## 1. Correction de la question comparative

La question initiale était :

> Quelle différence entre varier des paramètres entre mondes et faire évoluer
> un porteur dans un même monde ?

Elle marque une différence juste, mais sa seconde moitié est trop affirmative.
Le cycle 10 calcule des trajectoires possibles dans un modèle cosmologique ; il
n'établit pas que notre univers a suivi l'une d'elles.

La question devient :

> Qu'ajoute une trajectoire dynamique explicite à un audit contrefactuel, et à
> quelles conditions réduit-elle plutôt que déplacer la contingence ?

Cette formulation sépare :

- la comparaison de possibilités ;
- l'intégration d'une évolution dans un modèle ;
- l'établissement empirique d'une histoire physique réelle.

## 2. Deux opérations principales

### 2.1 Cycle 9 : construire et auditer un espace contrefactuel

Le cycle 9 ne demande pas d'abord comment un système change avec le temps. Il
demande ce qui arrive à une observable ou à un critère lorsque certains
paramètres, relations ou conditions sont modifiés.

Une affirmation d'ajustement fin porte au minimum sur :

```text
espace de paramètres
+ coordonnées et corrélations
+ carte vers des observables
+ critère de viabilité
+ mesure éventuelle
```

Le résultat peut être une sensibilité, une région admissible, une compensation
ou une indétermination probabiliste. Aucune trajectoire temporelle n'est requise
par définition.

### 2.2 Cycle 10 : intégrer une trajectoire portée par un système physique

Le cycle 10 introduit un champ scalaire `phi` comme porteur possible d'une
variation de l'échelle électrofaible `v`. Une trajectoire exige :

```text
variables d'état + équations + conditions initiales
-> évolution temporelle
-> valeur tardive + énergie résiduelle + observables
```

L'évolution ne peut pas être remplacée par une fonction arbitraire `v(t)` ou
par le déplacement manuel d'un curseur. Le champ, ses couplages, son potentiel,
le taux d'expansion et le transfert d'énergie doivent être spécifiés.

## 3. Cinq niveaux à ne pas confondre

| Niveau | Opération | Ce qu'elle établit au mieux |
|---|---|---|
| reparamétrisation | changer les coordonnées d'une même description | invariance ou dépendance d'un diagnostic |
| contrefactuel intramodèle | modifier des paramètres dans un modèle fixé | sensibilité et région admissible conditionnelles |
| comparaison intermodèles | changer théorie, contenu ou mécanismes | possibilité comparative, non probabilité |
| trajectoire calculée | intégrer des équations pour un jeu de paramètres et de conditions initiales | histoire possible dans le modèle |
| histoire physique établie | relier une trajectoire à des preuves empiriques discriminantes | scénario soutenu pour le monde étudié |

Le cycle 9 travaille surtout dans les trois premiers niveaux. Le cycle 10
ajoute le quatrième. Aucun des deux n'établit encore le cinquième pour une
ancienne variation électrofaible.

## 4. Un balayage dynamique conserve deux axes contrefactuels

Le scan du cycle 10 ne supprime pas le contrefactuel. Il combine :

```text
comparaison de paramètres et de conditions initiales
+
intégration temporelle pour chaque point
```

Il faut donc distinguer :

- l'axe du scan, qui compare des modèles ou des états initiaux possibles ;
- l'axe du temps, qui ordonne les états d'une solution particulière.

Un nuage de points viable n'est pas une trajectoire. Une trajectoire viable
n'est pas une fréquence de réalisation. Une fréquence de points sur une grille
n'est pas une probabilité physique sans mesure justifiée.

## 5. Comparaison des exigences

| Question | Cycle 9 — audit contrefactuel | Cycle 10 — trajectoire dynamique |
|---|---|---|
| qu'est-ce qui varie ? | paramètres, relations, conditions ou modèles déclarés | état d'un porteur et grandeurs qui en dépendent |
| qu'est-ce qui relie entrée et sortie ? | carte de dépendances ou calcul contrefactuel | équations d'évolution et couplages |
| que signifie une région ? | ensemble admissible sous un critère | bassin de conditions ou paramètres donnant des trajectoires acceptables |
| que signifie une sensibilité ? | dérivée ou variation de résultat selon une direction choisie | dépendance de la solution tardive aux paramètres ou états initiaux |
| quel résultat négatif ? | réglage non défini, dissous, déplacé ou indéterminé | absence de trajectoire satisfaisant simultanément les contraintes du modèle |
| quelle dette probabiliste ? | mesure, prior et classe de possibilités | demeure entière malgré le scan |
| quelle dette physique ? | réalisation des possibilités et origine des corrélations | mécanisme microscopique, corrections et confrontation empirique |

## 6. Cycle 9 : ce que l'audit obtient sans dynamique temporelle

### 6.1 Séparer sensibilité et improbabilité

Une observable peut être très sensible à un paramètre dans une direction sans
que la région observée soit dotée d'une faible probabilité physique. Le passage
de l'une à l'autre exige une mesure sur l'espace des possibilités.

### 6.2 Séparer coupe étroite et région multidimensionnelle

Une variation isolée peut fermer une voie tandis qu'une variation corrélée en
ouvre d'autres. Le cas d'un univers sans interaction faible, dit `weakless`,
fragilise ainsi une nécessité absolue obtenue à paramètres fixes. Il n'explique
ni l'origine des compensations ni leur poids statistique.

### 6.3 Localiser la contingence résiduelle

Le premier lot produit des verdicts différents : dissolution de faux cadrans,
réduction par corrélations, déplacement vers des paramètres plus profonds,
confirmation d'une sensibilité ou indétermination faute de mesure.

Le cycle établit donc une grammaire du diagnostic. Il ne produit pas à lui seul
le mécanisme qui réaliserait les possibilités comparées.

## 7. Cycle 10 : ce que la dynamique ajoute

Le cycle 10 impose trois exigences absentes d'un simple contrefactuel statique.

### 7.1 Un porteur et une loi d'évolution

La valeur électrofaible tardive doit devenir une sortie d'un système : champ,
potentiel, couplage au Higgs, friction cosmologique et conditions initiales.

### 7.2 Un bassin de trajectoires

La convergence d'une seule solution ne constitue pas un attracteur. Il faut
qu'un ensemble étendu de conditions initiales conduise à une relation tardive
robuste sous une tolérance déclarée.

### 7.3 Un bilan énergétique et observationnel

La convergence de `phi` vers son minimum ne suffit pas. L'énergie mobilisée
doit avoir une histoire compatible avec la nucléosynthèse primordiale (BBN),
l'expansion, les reliques, l'entropie et les contraintes tardives.

Le cycle transforme donc la question :

```text
la variable converge-t-elle ?
```

en :

```text
la variable converge-t-elle
+ son énergie devient-elle admissible
+ les observables restent-elles compatibles
+ la contingence totale diminue-t-elle ?
```

## 8. Les trois phases calculatoires du cycle 10

### 8.1 Phase 2 : fixité locale, échec cosmologique global

Dans le modèle minimal avec symétrie discrète `Z_2`, le portail scalaire–Higgs
ramène rapidement `v` vers sa valeur tardive. Mais le condensat stable devient
une relique de matière surabondante.

```text
quasi-fixité de v obtenue
!=
histoire cosmologique viable
```

Le coût de la variation n'est pas supprimé ; il est déplacé vers l'abondance du
porteur.

### 8.2 Phase 3 : amélioration de la dilution, second échec conservatif

Un régime quartique fait d'abord diluer l'énergie comme le rayonnement. Mais le
retard de la transition vers le régime massif demande une énergie initiale
plus élevée. Aucun point du scan documenté ne satisfait tous les critères pour
une variation initiale supérieure à un pour cent.

Le résultat montre qu'améliorer une étape du mécanisme peut aggraver une autre
partie du bilan.

### 8.3 Phase 4 : fenêtre dissipative effective, mécanisme encore absent

L'ouverture du bilan énergétique produit une fenêtre phénoménologique non
vide pour plusieurs profils de dissipation. Le condensat peut transférer son
énergie assez tôt, laisser une entropie contrôlée et disparaître avant la BBN.

Mais le taux de dissipation `Gamma_phi` est prescrit, non dérivé d'une
réalisation microscopique. La fenêtre établit une compatibilité effective :

```text
si un canal produit ce profil
alors le bilan simplifié peut être viable
```

Elle n'établit ni qu'un tel canal existe dans la théorie retenue, ni que notre
univers a suivi cette histoire.

## 9. La migration du réglage requalifiée

L'expression « migration du réglage » est utile, mais métaphorique. Elle ne
désigne pas le déplacement temporel d'une substance nommée réglage.

Elle désigne un changement de localisation de la dette explicative :

| Déplacement | Exemple |
|---|---|
| valeur vers paramètres | `v` devient sortie d'un potentiel et de couplages encore libres |
| valeur vers conditions initiales | la valeur tardive dépend de `phi_i` ou de sa vitesse initiale |
| fixité vers énergie | la convergence produit une relique ou une injection d'entropie |
| mécanisme effectif vers microphysique | la fenêtre dépend du profil de `Gamma_phi` à dériver |
| possibilité vers mesure | une région viable reste sans probabilité physique définie |

La formulation la plus précise est donc :

> déplacement de la contingence ou de la dette explicative.

Le terme « migration du réglage » peut rester comme raccourci, à condition de
ne pas lui attribuer un sens dynamique qu'il n'a pas.

## 10. Quand une dynamique réduit-elle réellement la contingence ?

Une valeur devenue dynamique n'est pas expliquée par ce seul changement de
statut. Le contraste dégage six conditions locales.

1. **Sortie plutôt qu'entrée.** La valeur tardive doit être produite par la
   dynamique et non réinscrite directement dans le potentiel.
2. **Bassin étendu.** Plusieurs conditions initiales doivent converger sans
   sélection étroite cachée.
3. **Paramètres non plus ajustés.** Les couplages et échelles nouveaux ne
   doivent pas exiger un choix plus fin que la valeur initiale.
4. **Bilan complet.** L'énergie du porteur, son transfert et ses reliques
   doivent rester admissibles.
5. **Robustesse.** La convergence doit résister aux corrections pertinentes et
   aux changements raisonnables du modèle.
6. **Prise empirique.** Le scénario doit produire des conséquences permettant
   de le distinguer d'une valeur simplement fixe.

Le cycle 10 satisfait partiellement les conditions 2 et 4 dans un modèle
effectif dissipatif. La condition 3 reste ouverte, et les conditions 5 et 6 ne
sont pas encore satisfaites au niveau requis pour une explication physique
complète.

## 11. Un bassin n'est pas une probabilité

La taille d'un bassin peut mesurer une robustesse aux conditions initiales dans
un domaine et des coordonnées définis. Elle ne fournit pas automatiquement :

- une distribution des conditions initiales ;
- une mesure sur les théories ;
- une fréquence de réalisation cosmologique ;
- une probabilité de la valeur tardive.

Le cycle 9 conserve donc son autorité méthodologique sur toute inférence
probabiliste. Le cycle 10 peut démontrer une insensibilité dynamique locale,
mais non une naturalité probabiliste sans hypothèses supplémentaires.

## 12. Effet sur l'enquête scientifique

Le contraste modifie l'enquête de sept manières.

1. Déclarer si la variation est un contrefactuel, un axe de scan ou le temps
   d'une solution.
2. Ne pas appeler dynamique une simple corrélation entre paramètres.
3. Exiger un porteur, des équations et un bilan pour toute histoire réelle
   proposée.
4. Évaluer la convergence et le coût énergétique séparément.
5. Traiter un résultat négatif comme localisation d'une incompatibilité, non
   comme exclusion de toute la classe de mécanismes.
6. Traiter une fenêtre phénoménologique comme condition imposée au futur
   mécanisme, non comme mécanisme déjà trouvé.
7. Réauditer la contingence après chaque extension afin de repérer son éventuel
   déplacement.

## 13. Dimension pratique soumise au test de retrait

La dimension pratique n'est pas ici institutionnelle. Elle réside dans la
construction et le contrôle du calcul : choix du domaine scanné, résolution des
équations, filtres de viabilité, reproduction des résultats et comparaison des
budgets énergétiques.

Si ces éléments sont retirés, les deux échecs conservatifs et la fenêtre
dissipative deviennent des affirmations invérifiables. Ils doivent donc rester
dans le portrait.

En revanche, l'organisation générale des équipes de cosmologie ou de physique
des particules ne modifie pas l'argument local et n'est pas ajoutée.

## 14. Portée philosophique locale

Le contraste établit qu'une explication dynamique est plus exigeante qu'une
simple ouverture des possibles : elle doit transformer une valeur en sortie
robuste d'une histoire contrainte, sans déplacer un coût équivalent vers une
autre partie du modèle.

Il ne démontre pas que les constantes physiques sont en général les produits
d'une histoire, que toute contingence possède un mécanisme de canalisation, ni
que la possibilité calculée d'une trajectoire prouve sa réalisation.

La force philosophique réside ici dans la règle de refus :

> rendre un paramètre dynamique ne l'explique pas encore.

## 15. Épreuve de la pondération

| Critère | Cycle 9 | Cycle 10 |
|---|---|---|
| fonction principale | audit méthodologique transversal | laboratoire calculatoire local |
| prise physique | dépend des cas et des espaces choisis | forte dans les modèles testés, très locale |
| résultat le plus robuste | séparation sensibilité, improbabilité, compensation et contingence | deux échecs conservatifs et contraintes sur une fenêtre dissipative |
| ouverture dominante | espace et mesure probabilistes | réalisation microscopique et histoire empirique |
| risque d'inflation | transformer une grammaire en verdict universel | transformer un modèle possible en histoire réelle |

### Verdict

La pondération passe ce cinquième test.

- Le cycle 9 reste un noyau méthodologique : il contrôle la construction du
  problème et les inférences de probabilité.
- Le cycle 10 reste un noyau calculatoire local : il montre ce qu'une dynamique
  doit payer et fournit des résultats de refus précis.
- Leur articulation est asymétrique : le cycle 9 audite aussi les paramètres
  ajoutés par le cycle 10 ; le cycle 10 donne un test physique à une partie des
  exigences formulées par le cycle 9.

La fenêtre dissipative ne change pas cette pondération. Elle définit la cible
d'une prochaine recherche microscopique.

## 16. Dettes conservées

### Cycle 9

1. Poursuivre avec des cas apportant des contrastes nouveaux.
2. Justifier toute mesure ou distribution avant un verdict probabiliste.
3. Ne pas convertir les compensations possibles en corrélations réalisées.
4. Conserver la différenciation des quatre premiers verdicts.

### Cycle 10

1. Dériver un canal de dissipation depuis un modèle microscopique minimal.
2. Réintroduire masses thermiques, degrés de liberté variables, rétroactions et
   contraintes observationnelles complètes.
3. Tester la robustesse aux corrections et aux choix de domaine du scan.
4. Chercher des signatures capables de distinguer cette histoire d'une valeur
   électrofaible simplement fixe.

### Dette commune

Ne jamais employer la densité des points d'une grille comme une mesure de
probabilité sans construction indépendante de cette mesure.

## 17. Résultat de la série des cinq contrastes

Les cinq tests produisent maintenant cinq règles locales :

1. dépendance à l'échelle, changement de régime et validité ne sont pas une
   même transformation ;
2. réseau fonctionnel, mécanisme et explication d'origine ne coïncident pas ;
3. plusieurs accès exigent des ponts avant de contraindre un même objet ;
4. une fixation métrologique transforme les expériences et déplace
   l'incertitude sans abolir l'empirie ;
5. une dynamique réduit la contingence seulement si sa trajectoire, son bassin,
   son bilan et son mécanisme résistent ensemble.

Cette série valide la pondération comme instrument provisoire. Elle ne clôt ni
les cycles physiques ni les deux questions directrices du projet.

## 18. Questions laissées ouvertes

- Quelle mesure, si elle existe, serait physiquement justifiée sur les
  conditions initiales du modèle dynamique ?
- Une réalisation microscopique de la dissipation réduira-t-elle la contingence
  ou la déplacera-t-elle encore vers ses couplages et seuils ?
- Quelles signatures permettraient de distinguer une ancienne relaxation de
  l'échelle électrofaible d'une histoire où cette échelle était déjà fixe ?
- Jusqu'où la règle « rendre dynamique n'explique pas » est-elle transférable
  à d'autres cycles sans devenir une formule générale vide ?
