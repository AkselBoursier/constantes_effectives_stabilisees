# Reprise comparative des cycles 1 et 6 — échelle, régime et validité v0.1

Cette reprise constitue le premier test de la pondération des cycles physiques
validée pour mise à l'épreuve le 14 juillet 2026. Elle compare le cycle 1,
consacré aux couplages et aux échelles, et le cycle 6, consacré aux théories
effectives à basse énergie.

## 0. Statut et limites

```text
statut : première mise à l'épreuve comparative ;
fonction : distinguer plusieurs transformations auparavant rapprochées sous le
           seul vocabulaire de l'échelle ou de la dynamique ;
base : synthèses actives et vérifications déjà présentes dans le dépôt ;
ne vaut pas : nouvelle revue de littérature, contrôle indépendant des valeurs,
              unification des deux cycles ou doctrine générale de la dynamique ;
révision : requise si la distinction échoue sur les autres secteurs physiques.
```

Documents principaux :

- cycle 1 : [synthèse de récupération des couplages, échelles et de la
  chromodynamique quantique (QCD)](../02_CYCLES_PHYSIQUES/01_Cycle_couplages_echelles_QCD/Synthese_recuperation_cycle_1_couplages_echelles_QCD_v0_1.md) ;
- cycle 6 : [dossier relationnel sur la basse
  énergie](../02_CYCLES_PHYSIQUES/06_Cycle_effectif_basse_energie/architecture-relationnelle-basse-energie.md),
  [vérification
  physique](../02_CYCLES_PHYSIQUES/06_Cycle_effectif_basse_energie/verification-physique-basse-energie.md)
  et [évaluation du gain
  explicatif](../02_CYCLES_PHYSIQUES/06_Cycle_effectif_basse_energie/evaluation-gain-explicatif-basse-energie.md).

La synthèse historique initiale du cycle 6 reste une source de récupération.
Son verdict d'« architecture inter-familles confirmée » a été remplacé par un
résultat plus limité : une architecture méthodologique de validité.

## 1. Les deux questions directrices

### 1.1 Frontière entre ce qui varie et ce qui tient

Comment déclarer la transformation pertinente avant de demander si une
grandeur ou une relation tient ?

Le contraste oblige à séparer au moins :

- la comparaison de phénomènes à différentes échelles cinématiques ;
- le changement d'une échelle auxiliaire de calcul ;
- le passage entre régimes où les descriptions adaptées diffèrent ;
- l'épreuve du domaine dans lequel une approximation reste contrôlée ;
- une évolution temporelle réelle, qui demande un porteur et une histoire.

### 1.2 Transformation de l'enquête

Que doit faire l'enquête lorsque la constance recherchée ne réside pas dans un
nombre isolé, mais dans la cohérence d'une prédiction à travers des changements
d'échelle, de représentation ou de régime ?

La réponse locale n'est pas de déclarer toute constante « dynamique ». Elle est
d'identifier ce qui varie, ce qui doit se compenser et ce qui signale la rupture
d'une description.

## 2. Résultat comparatif principal

Le premier test fait apparaître quatre plans, dont les trois premiers étaient
rapprochés dans la question comparative initiale.

| Plan | Question contrôlable | Exemple principal | Ce qu'il ne faut pas en déduire |
|---|---|---|---|
| dépendance à une échelle cinématique `Q` | comment des phénomènes comparés changent-ils avec l'énergie ou l'impulsion caractéristique ? | évolution de la force de l'interaction forte lorsque `Q` change | qu'un même système évolue nécessairement dans le temps |
| dépendance à l'échelle de renormalisation `mu` | comment les composantes calculées se redistribuent-elles sous un choix auxiliaire ? | `alpha_s(mu)` et coefficients de Wilson `C_i(mu)` | que l'observable physique dépend librement de ce choix |
| changement de régime ou de description | quand les degrés de liberté, l'expansion ou les méthodes adéquates changent-ils ? | perte du contrôle perturbatif en QCD ; raccordement autour d'un seuil | qu'un objet disparaît brutalement à une frontière universelle |
| domaine de validité | où une approximation possède-t-elle une erreur contrôlée ? | théorie de Fermi pour `|q²| << M_W²` ; expansion en `E/M_Pl` | qu'un domaine de description est lui-même un processus physique |

Cette séparation n'isole pas quatre mondes sans relation. Une échelle physique
caractéristique peut guider le choix de `mu`, un changement de régime peut
imposer une nouvelle théorie effective des champs (EFT), et son raccordement
peut redéfinir les degrés de liberté actifs. Mais les liens doivent être établis
cas par cas.

> Dépendance à l'échelle, changement de régime et validité limitée peuvent
> former une même chaîne d'analyse sans constituer une même transformation.

## 3. Ce que chaque cycle apporte

### 3.1 Cycle 1 : déclarer la transformation

Le cycle 1 fournit le garde-fou initial :

```text
stabilité dans le temps
≠ indépendance à l'échelle
≠ identité de régime
≠ simplicité théorique.
```

Ses cas empêchent notamment :

- de citer `alpha_s` sans échelle, schéma, processus et domaine ;
- de traiter `Lambda_QCD` comme une frontière physique dure et universelle ;
- d'identifier la simplicité numérique d'un rapport à la simplicité de sa
  constitution ;
- de convertir la précision d'une valeur de référence en invariance sous toute
  transformation.

Sa force principale est discriminante : il apprend d'abord à refuser une
question de constance insuffisamment indexée.

### 3.2 Cycle 6 : contrôler la description

Le cycle 6 donne un contenu positif à plusieurs de ces indexations :

- dans la théorie de Fermi, le développement en `q²/M_W²` explique la localité
  apparente, le coefficient dominant et l'ordre des corrections ;
- dans une EFT, le raccordement, le comptage en puissances, le groupe de
  renormalisation (RG) et le mélange d'opérateurs organisent la prédiction ;
- en QCD basse énergie, l'augmentation du couplage et la perte du contrôle
  perturbatif conduisent à d'autres degrés de liberté et méthodes ;
- en gravitation effective, de petits rapports comme `E/M_Pl` hiérarchisent les
  corrections sans transformer `M_Pl` en seuil expérimental abrupt.

Sa force principale est constructive : il montre comment une description peut
rester prédictive avec des coefficients qui varient selon l'échelle, le schéma
ou la base.

### 3.3 Non-redondance

Les deux cycles se recouvrent sur `alpha_s` et `Lambda_QCD`, mais ils n'ont pas
la même fonction :

| Cycle 1 | Cycle 6 |
|---|---|
| demande sous quelle transformation la constance est évaluée | demande comment une description conserve son contrôle dans un domaine |
| compare valeur de référence, couplage courant, échelle et constitution | compare réduction locale, changement de régime et expansion hiérarchique |
| repère les confusions | organise raccordement, corrections et conditions de rupture |

Le recouvrement sert donc de test commun, non de motif de fusion.

## 4. Ce qui tient réellement

La comparaison déplace le lieu possible de la constance.

### 4.1 Fixité d'une composante

Une valeur peut être fixée dans une convention, à une échelle et dans un schéma
donnés. Cette fixité locale ne garantit pas son invariance sous changement de
cadre.

### 4.2 Stabilité d'une prédiction

Les dépendances de l'échelle auxiliaire, du schéma ou de la base doivent se
compenser dans l'observable physique, à l'ordre de précision considéré. Une
dépendance résiduelle après troncature sert aussi à estimer une incertitude
théorique ; elle n'est pas une liberté physique arbitraire de l'observable.

### 4.3 Validité d'une description

Une expansion tient tant que son paramètre de contrôle reste petit et que les
termes négligés demeurent bornés à la précision demandée. Ce qui tient est alors
une relation entre domaine, hiérarchie des corrections et exigence de précision,
non un coefficient absolument fixe.

### 4.4 Continuité physique sous changement de description

Lorsque les degrés de liberté ou les méthodes changent, des observables et des
relations de raccordement permettent de comparer les descriptions. La
continuité pertinente n'est pas l'identité terme à terme des paramètres.

## 5. Effet sur l'enquête scientifique

Le contraste modifie les exigences minimales d'une affirmation de constance.

1. **Nommer la variable de transformation.** Distinguer temps, énergie ou
   impulsion physique `Q`, échelle de renormalisation `mu`, schéma, base et
   ordre d'approximation.
2. **Identifier le porteur.** Préciser si l'énoncé porte sur un coefficient, une
   relation, une observable, un secteur ou une description.
3. **Déclarer le domaine.** Donner les rapports d'échelle, les degrés de liberté
   actifs et la condition de rupture.
4. **Suivre les compensations.** Ne pas attribuer à un coefficient individuel
   l'invariance qui appartient à une amplitude ou à une observable.
5. **Séparer comparaison et histoire.** Une famille de mesures effectuées à des
   `Q` différents ne constitue pas, sans chaîne physique supplémentaire,
   l'histoire temporelle d'un même système.
6. **Conserver l'erreur comme contenu.** Le comptage en puissances, la
   troncature et la dépendance résiduelle font partie de la portée du résultat.

Ce résultat répond à la seconde question directrice : travailler sur des
constances dépendantes d'un régime ne conduit pas seulement à qualifier les
valeurs. Cela transforme les conditions sous lesquelles deux calculs, mesures
ou descriptions peuvent être comparés.

## 6. Dimension pratique soumise au test de retrait

La dimension pratique est conservée seulement lorsqu'elle modifie l'inférence :

- des déterminations de `alpha_s` issues de processus et d'échelles différents
  doivent être transportées et comparées dans un cadre commun ;
- les choix de raccordement, d'ordre perturbatif, de degrés de liberté actifs
  et de méthode non perturbative modifient les incertitudes et la comparabilité ;
- l'accès à une observable ne donne pas séparément les coefficients dépendants
  d'une base : ceux-ci sont reconstruits dans une chaîne de calcul et de modèle.

Les conditions institutionnelles générales de la recherche ne sont pas
ajoutées ici : leur retrait ne change pas le présent argument physique ou
épistémique. Cette décision applique l'heuristique provisoire sans en faire une
formule universelle de tri.

## 7. Dettes maintenues séparées

La comparaison n'efface pas les dettes propres aux cycles.

| Dette | Cycle 1 | Cycle 6 |
|---|---|---|
| contrôle des valeurs et des sources primaires | encore requis | vérification spécialisée déjà plus avancée |
| distinction des schémas et conventions | à approfondir pour `Lambda_QCD` | explicitée, à conserver dans chaque application |
| calcul reproductible nouveau | absent de cette reprise | absent de cette reprise |
| extension à d'autres secteurs | non requise pour le résultat local | ne doit pas devenir une généralisation automatique de l'EFT |
| portée philosophique | à tester transversalement | limitée à une architecture méthodologique de validité |

## 8. Épreuve de la pondération

| Critère | Résultat du test |
|---|---|
| prise physique locale | oui : `alpha_s`, `Lambda_QCD`, théorie de Fermi, coefficients de Wilson et expansion gravitationnelle fournissent des mécanismes différenciés |
| force pour la frontière | oui : la frontière varie selon `Q`, `mu`, le régime et la précision demandée |
| force pour l'enquête | oui : indexation, raccordement, compensation et estimation d'erreur deviennent des exigences explicites |
| état de preuve | hétérogène et déclaré : récupération forte au cycle 1, vérification plus avancée au cycle 6, aucune nouvelle validation externe ici |
| risque d'inflation | contenu par le refus d'appeler toute dépendance une dynamique temporelle ou toute validité une ontologie |

### Verdict provisoire

La pondération passe ce premier test : elle ne produit ni deux portraits
juxtaposés ni une fusion. Elle fait apparaître une distinction supplémentaire,
entre `Q` et `mu`, et précise ce qui change dans l'enquête.

Ce verdict ne valide pas définitivement la pondération. Un échec sur les autres
couples peut encore conduire à la corriger.

## 9. Questions laissées ouvertes

1. Dans quels cas une variation d'échelle est-elle reliée à l'histoire physique
   d'un même système plutôt qu'à une comparaison de situations ?
2. Quels observables ou raccordements permettent d'établir qu'un changement de
   description conserve bien le même contenu physique pertinent ?
3. Comment la non-perturbativité transforme-t-elle les voies d'accès, et pas
   seulement les outils de calcul ?
4. Jusqu'où l'architecture méthodologique de validité des EFT se transfère-t-elle
   avant de devenir une analogie vide ?

Ces questions restent des sorties du contraste. Elles ne sont pas promues en
programme général avant l'épreuve des autres couples.

