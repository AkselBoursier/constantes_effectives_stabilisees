# α2 — Audit borné de la voie rubidium de détermination de `alpha` v0.1

## 0. Statut

```text
statut : fiche scientifique locale en cours de ratification ;
date : 26 juillet 2026 ;
opération : α2, issue #36 ;
source primaire directrice : Morel, Yao, Cladé et Guellati-Khélifa,
                             Nature 588, 61–65 (2020) ;
DOI : 10.1038/s41586-020-2964-7 ;
source de repondération : CODATA recommended values 2022,
                          Rev. Mod. Phys. 97, 025002 (2025) ;
fonction : reconstruire la chaîne rubidium depuis l’observable de recul
           jusqu’à la valeur inférée de alpha ;
autorité : descriptive et locale ;
ne vaut pas : démonstration de supériorité de la voie rubidium,
               diagnostic causal de la discordance avec le césium,
               verdict comparatif final α2, nouvelle valeur de alpha,
               ou propagation dans la synthèse active du cycle 1.
```

## 1. Résultat directeur

La voie rubidium ne mesure pas directement `alpha`.

Elle mesure une vitesse ou fréquence de recul atomique, dont est extrait le rapport `h/m(87Rb)`. Une relation métrologique et théorique, mobilisant notamment la masse relative du rubidium, la masse relative de l’électron et la constante de Rydberg, permet ensuite d’inférer une valeur de `alpha`.

```text
observable première : déphasage d’interféromètre sensible au recul photonique ;
sortie expérimentale : h/m(87Rb) ;
relations auxiliaires : masses relatives, R_inf, h et c ;
sortie inférée : alpha^-1 ;
insertion ultérieure : donnée D3, avec D5, dans l’ajustement CODATA.
```

La chaîne doit donc être auditée à deux niveaux séparés :

1. extraction expérimentale de `h/m(87Rb)` ;
2. passage de `h/m(87Rb)` à `alpha`.

## 2. Valeurs publiées

Morel et al. rapportent :

```text
h/m(87Rb) = 4.591 359 258 90(65) × 10^-9 m² s^-1 ;
alpha^-1 = 137.035 999 206(11) ;
incertitude relative sur alpha : 81 parties par billion (ppt) ;
contribution statistique issue de h/m : 2.4 × 10^-11 ;
contribution systématique issue de h/m : 6.8 × 10^-11.
```

Dans CODATA 2022, la donnée de recul est reprise comme D3 :

```text
D3 : h/m(87Rb) ;
incertitude standard relative d’entrée : 1.4 × 10^-10 ;
D5 : Ar(87Rb), entrée auxiliaire reliée au réseau des masses atomiques.
```

La valeur publiée de `alpha^-1` n’est donc pas la donnée brute de l’ajustement. CODATA ajuste D3 et D5 par l’équation d’observation commune aux voies de recul.

## 3. Relation de passage

Pour un atome `X`, la relation utilisée est :

```text
h/m(X) ≐ [Ar(e)/Ar(X)] [c alpha²/(2 R_inf)].
```

Pour le rubidium :

```text
mesuré expérimentalement : h/m(87Rb) ;
entrée auxiliaire : Ar(87Rb) ;
constantes reliées : Ar(e), R_inf ;
constantes exactes dans le SI révisé : h, c ;
quantité inférée : alpha.
```

Conséquence de rang :

> La voie rubidium est une détermination de `alpha` par recul et propagation métrologique, non une mesure directe et isolée de `alpha`.

## 4. Architecture expérimentale

L’expérience utilise des atomes de `87Rb` refroidis par laser puis préparés dans un état interne et une classe de vitesse contrôlés. Elle associe :

```text
sélection et mesure de vitesse par transitions Raman ;
accélération cohérente par oscillations de Bloch ;
interférométrie de Ramsey–Bordé ;
renversement de la direction des transitions Raman ;
renversement de la direction de l’accélération atomique ;
combinaison de plusieurs configurations pour annuler ou contrôler
les effets qui changent de signe.
```

La séquence mesure la variation de vitesse produite par le transfert cohérent d’un grand nombre de moments photoniques. La comparaison des fréquences Raman avant et après l’accélération fournit le recul intégré, puis `h/m(87Rb)`.

Une configuration typique déclarée dans les données étendues utilise notamment :

```text
temps Ramsey T_R : 20 ms ;
temps d’interféromètre T : 32.9 ms ;
nombre d’oscillations de Bloch N_B : 500 ;
durée élémentaire d’oscillation : 12 microsecondes.
```

Ces valeurs caractérisent une des configurations de mesure ; elles ne résument pas à elles seules tout le protocole ni toutes les combinaisons de données.

## 5. Contrôles et organisation de l’analyse

Les matériaux publiés documentent plusieurs contrôles instrumentaux :

- auto-alignement des faisceaux afin de réduire les variations d’orientation ;
- compensation de la rotation terrestre et comparaison de résultats avec et sans compensation ;
- cartographie et interpolation du champ magnétique ;
- contrôle de fréquence et de phase des lasers Raman ;
- inversion des directions Raman et de l’accélération afin d’exploiter les symétries de signe ;
- comparaison de plusieurs configurations de puissance, de temps et de nombre d’oscillations ;
- simulations Monte-Carlo des effets liés au profil spatial des faisceaux et aux distributions atomiques.

Les données détaillées et le code d’analyse ne sont pas déposés publiquement avec l’article : ils sont annoncés comme disponibles auprès de l’auteur correspondant sur demande raisonnable. Cette limite empêche une reproduction indépendante complète à partir du seul corpus public.

## 6. Budget des corrections et incertitudes

Le budget publié est exprimé dans la Table 1 de Morel et al. en unités relatives de `10^-11` sur `h/m` ou sur la quantité propagée selon la convention du tableau.

Les contributions dominantes identifiées sont :

| Effet | Correction publiée (`×10^-11`) | Incertitude publiée (`×10^-11`) | Fonction dans l’audit |
|---|---:|---:|---|
| phase de Gouy et structure du front d’onde | `+108.2` | `5.4` | correction optique dominante et principale contribution à l’incertitude systématique |
| boucle de verrouillage de phase Raman | `−39.8` | valeur incluse dans le budget publié | correction de phase et de fréquence de la chaîne Raman |
| déplacement lumineux | `−11.0` | valeur incluse dans le budget publié | décalages ac-Stark et asymétries de puissance |
| courbure résiduelle du front d’onde | `+1.3` | `0.6` | contribution distincte liée à la courbure mesurée |
| ensemble des effets systématiques | `+64.2` | `6.8` | correction nette après compensations entre termes |

La correction de Gouy est plus grande en valeur absolue que la correction systématique totale, parce que plusieurs autres contributions ont un signe opposé. Le total résulte donc d’une compensation entre corrections importantes, non d’une absence d’effets instrumentaux.

Cette structure impose de distinguer :

```text
grandeur d’une correction ;
incertitude attribuée à cette correction ;
validation du modèle qui produit la correction ;
compensation numérique entre corrections de signes opposés.
```

Une correction importante peut être correctement déterminée. Sa grande amplitude ne constitue pas à elle seule une réfutation. Mais lorsqu’elle domine le budget, la robustesse du résultat dépend fortement de la caractérisation du faisceau, de la distribution atomique et des simulations utilisées pour calculer son effet moyen.

## 7. Concentration du risque systématique

### 7.1 Phase de Gouy et front d’onde

Le vecteur d’onde effectif vu par les atomes n’est pas celui d’une onde plane idéale. Le profil d’intensité, la phase de Gouy, la courbure du front d’onde et les aberrations produisent une correction sur le recul inféré.

L’article documente notamment :

```text
rayon du faisceau au collimateur : environ 4.9 mm ;
courbure mesurée : R^-1 = (0.9 ± 0.3) × 10^-3 m^-1 ;
caractérisation optique par imagerie et interférométrie ;
propagation des distributions atomiques dans le champ optique ;
simulations Monte-Carlo selon les configurations expérimentales.
```

Les données étendues montrent que les fluctuations locales d’intensité sont intégrées aux simulations. Pour reproduire certains comportements observés, les auteurs ajoutent dans le modèle un bruit spatial de l’ordre de 2 % à une échelle de 50 micromètres sur les images du faisceau.

Le verdict autorisé n’est pas que la correction est erronée, mais que la chaîne de mesure est fortement dépendante d’une reconstruction optique et statistique du champ effectivement échantillonné par les atomes.

### 7.2 Phase Raman et verrouillage de fréquence

La phase relative des lasers Raman entre directement dans la mesure de vitesse. Les auteurs documentent une boucle de verrouillage de phase et une correction issue de la chaîne radiofréquence et optique.

Le renversement de la direction Raman annule plusieurs effets, mais une compensation imparfaite ou une asymétrie entre les deux directions peut laisser un résidu. La correction publiée de la boucle de verrouillage est l’une des contributions de plus grande amplitude et compense partiellement la correction optique dominante.

### 7.3 Déplacements lumineux et distributions atomiques

Les déplacements lumineux dépendent des puissances, décalages et profils spatiaux des faisceaux. Les atomes dont la vitesse et la position diffèrent n’échantillonnent pas exactement la même intensité pendant la séquence.

Les données étendues montrent que les auteurs testent plusieurs puissances Raman et plusieurs paramètres temporels, et utilisent des simulations pour estimer les effets d’un défaut de compensation entre directions Raman.

### 7.4 Rotation, alignement et champ magnétique

La rotation terrestre, l’alignement des faisceaux et le champ magnétique sont contrôlés par :

- compensation active de la rotation ;
- auto-alignement des miroirs ;
- mesure du contraste en fonction des réglages ;
- cartographie du champ par transitions atomiques sensibles ;
- interpolation du champ dans la région parcourue par les atomes.

Ces contrôles réduisent des familles identifiées d’erreurs. Ils ne démontrent pas que toute covariance entre alignement, profil spatial et sélection atomique est publiquement reconstructible.

## 8. Ce que l’expérience soutient positivement

Dans son propre domaine, l’expérience soutient :

```text
une mesure précise du recul du rubidium ;
une extraction de h/m(87Rb) ;
une valeur de alpha inférée par une relation déclarée ;
un budget d’incertitude décomposé ;
des inversions de configuration et des contrôles instrumentaux ;
une détermination de alpha fondée sur une observable première
indépendante de la mesure de ae.
```

Elle ne soutient pas seule :

```text
l’absence de systématique non modélisée ;
la cause de la discordance avec le césium ;
la supériorité définitive de la voie rubidium ;
une variation physique de alpha ;
l’indépendance complète par rapport aux constantes auxiliaires
et aux modèles métrologiques communs.
```

## 9. Repondération par CODATA 2022

Dans l’ajustement initial CODATA 2022, D3 porte un résidu normalisé de `−2.3`. Il est inférieur en valeur absolue au résidu césium `4.7`, mais dépasse néanmoins le seuil de 2 utilisé pour repérer les données problématiques de l’ajustement initial.

CODATA :

- conserve D3 et D5 ;
- applique le facteur d’expansion `2.5` aux six données D1–D6 ;
- ne conserve pas l’incertitude publiée de la voie rubidium comme seule base de pondération ;
- ne diagnostique pas de cause propre au rubidium ;
- ne transforme pas la discordance en variation physique ;
- élargit l’incertitude de la valeur recommandée.

Le mode de soutien probatoire devient donc double :

```text
niveau expérimental local : mesure corrigée et contrôles internes ;
niveau inter-chaînes : donnée très précise conservée,
                        mais repondérée dans un ensemble incohérent
                        avant expansion des incertitudes.
```

La précision nominale de la voie rubidium lui donnerait un poids dominant dans une moyenne naïve. La décision CODATA empêche précisément que cette précision interne fixe seule la valeur recommandée lorsque le sous-ensemble des chaînes est incohérent.

## 10. Statut actuel de la discordance

Le premier lot documentaire établit :

```text
valeur rubidium publiée : conservée ;
chaîne expérimentale : documentée selon son budget ;
accord avec la voie g−2 actuelle : meilleur que l’accord avec le césium ;
accord global des trois chaînes : insuffisant avant expansion ;
cause du désaccord : suspendue ;
réplication indépendante de même précision : absente du premier lot ;
données et code publics : non disponibles directement.
```

L’accord relatif entre rubidium et `g−2` ne permet pas encore de conclure que le césium est fautif. Deux voies peuvent être proches pour des raisons distinctes, et la voie `g−2` possède des dépendances théoriques qui doivent être auditées séparément.

## 11. Verdict local préparatoire

```text
admission :
  la voie rubidium fournit une détermination expérimentale de h/m(87Rb)
  et une inférence déclarée de alpha avec une précision interne élevée,
  un budget systématique publié et plusieurs inversions de contrôle ;

refus :
  traiter alpha comme observable directement mesurée ;
  transformer la précision nominale en preuve de supériorité inter-chaînes ;
  interpréter l’écart avec le césium comme variation physique ;
  déduire de la proximité avec g−2 que la cause de la discordance est connue ;

suspension :
  suffisance complète des modèles de front d’onde et de distribution atomique ;
  cause de l’écart avec la voie césium ;
  indépendance effective complète à l’égard des paramètres auxiliaires ;
  pondération comparative finale entre les trois chaînes ;
  statut comparatif final de la valeur recommandée.
```

Mode de soutien probatoire :

```text
mesure locale de recul
+ propagation métrologique
+ inversions de configuration
+ modélisation optique et atomique
+ repondération inter-chaînes par CODATA.
```

## 12. Symétrie et asymétrie avec la voie césium

L’audit est symétrique par sa grille :

```text
observable première ;
relation de passage ;
corrections ;
simulations ;
incertitudes ;
insertion CODATA ;
verdict local.
```

Les résultats locaux sont asymétriques :

```text
rubidium : incertitude nominale plus faible,
            résidu CODATA initial de -2.3,
            correction dominante liée au front d’onde ;

césium : incertitude nominale plus élevée,
          résidu CODATA initial de 4.7,
          corrections dominantes liées au faisceau et aux gradients.
```

Cette asymétrie ne constitue pas encore un classement de vérité. Elle prépare la comparaison finale après l’audit de la voie `g−2`.

## 13. Dettes avant la comparaison α2

1. auditer séparément l’inférence `g−2` et ses dépendances QED ;
2. comparer les architectures de correction des deux expériences de recul ;
3. distinguer indépendance des observables premières et dépendances communes de l’inférence ;
4. établir quelles données, covariances et codes sont réellement accessibles ;
5. distinguer accord numérique et indépendance probatoire ;
6. ne produire le verdict comparatif α2 qu’après l’audit local `g−2`.

## 14. Condition d’arrêt de la fiche

La fiche rubidium est suffisamment instruite lorsque l’on peut répondre séparément :

```text
ce qui est mesuré : recul atomique et h/m(87Rb) ;
ce qui est corrigé : phase optique, phase Raman, déplacements lumineux,
                      rotation, alignement et champ magnétique ;
ce qui est simulé : effet du profil spatial, distributions atomiques
                    et défauts de compensation ;
ce qui est inféré : alpha par relation métrologique ;
ce qui est repondéré : D3 et D5 dans CODATA ;
ce qui demeure inconnu : cause de la discordance inter-chaînes.
```

Cette condition est remplie pour le premier lot. La fiche reste préparatoire jusqu’à l’audit de la voie `g−2` et à la comparaison des trois chaînes.
