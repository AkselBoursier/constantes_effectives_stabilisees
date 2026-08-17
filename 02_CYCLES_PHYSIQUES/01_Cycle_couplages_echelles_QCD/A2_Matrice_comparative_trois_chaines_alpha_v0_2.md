# α2 — Matrice comparative des trois chaînes de détermination de la valeur de basse énergie de `alpha` v0.2

## 0. Statut

```text
statut : matrice comparative après audits locaux validés ;
date : 26 juillet 2026 ;
opération : α2, issue #36 ;
entrées :
  A2_Extraction_CODATA_alpha_v0_1.md ;
  A2_Matrice_chaines_determination_alpha_v0_1.md ;
  A2_Fiche_voie_cesium_alpha_v0_1.md ;
  A2_Fiche_voie_rubidium_alpha_v0_1.md ;
  A2_Fiche_voie_gmoins2_alpha_v0_1.md ;
fonction : comparer les trois chaînes selon une grille commune sans les rendre équivalentes ;
autorité : descriptive et comparative ;
ne vaut pas : nouvelle moyenne, reproduction indépendante des expériences ou de CODATA,
               classement définitif de vérité, diagnostic causal de la discordance,
               variation physique de alpha ou propagation dans la synthèse active du cycle 1.
```

La matrice v0.1 séparait les chaînes avant leurs audits locaux. La présente v0.2 intègre les résultats validés des trois fiches et prépare le verdict comparatif local d’α2.

## 1. Cible commune et chaînes hétérogènes

Les trois voies produisent des valeurs exprimées dans une convention commune de basse énergie, mais elles ne mesurent pas la même observable première et ne mobilisent pas la même relation de passage.

```text
cible numérique commune : valeur dérivée de alpha^-1 à basse énergie ;

voie césium :
  recul atomique -> h/m(133Cs) -> relation métrologique -> alpha ;

voie rubidium :
  recul atomique -> h/m(87Rb) -> relation métrologique -> alpha ;

voie g−2 :
  fréquences d’un électron piégé -> a_e -> modèle standard/QED -> alpha.
```

La comparabilité des sorties n’implique donc ni identité des observables, ni identité des modèles, ni équivalence probatoire.

## 2. Matrice comparative principale

| Dimension | Césium | Rubidium | `g−2` électronique |
|---|---|---|---|
| Observable première | phase interférométrique sensible au recul | déphasage et variation de vitesse par recul | fréquences cyclotron et d’anomalie d’un électron piégé |
| Sortie expérimentale | `h/m(133Cs)` | `h/m(87Rb)` | `g/2` ou `a_e(exp)` |
| Relation de passage | relation de recul avec `Ar(Cs)`, `Ar(e)` et `R_inf` | même forme de relation avec `Ar(Rb)`, `Ar(e)` et `R_inf` | inversion de `a_e(SM; alpha, rapports de masses, coefficients QED, contributions hadroniques et faibles)` |
| Nature de l’inférence | propagation métrologique | propagation métrologique | inférence théorique conditionnelle profonde |
| Correction ou modèle dominant | phase de Gouy, gradients d’accélération, mouvement thermique | front d’onde et phase de Gouy, phase Raman, déplacements lumineux | profils de raie, élargissement cyclotron, modes de cavité ; coefficients QED d’ordre élevé |
| Contrôles principaux | analyse aveugle, deux codes, configurations temporelles, simulations 3D | inversions de directions, auto-alignement, compensation de rotation, simulations du champ optique | analyse aveugle, onze champs magnétiques, plusieurs déterminations des modes de cavité |
| Valeur publiée de `alpha^-1` | `137.035 999 046(27)` | `137.035 999 206(11)` | `137.035 999 166(15)` |
| Incertitude nominale relative déclarée | `0.20 ppb` | `0.081 ppb` | `0.11 ppb` sur `alpha` inféré |
| Entrées CODATA | D4 + D6 | D3 + D5 | D1 + D2 |
| Résidu normalisé initial CODATA | `+4.7` pour D4 | `−2.3` pour D3 | pas de résidu supérieur à 2 signalé pour D1 dans le sous-dossier extrait |
| Accessibilité publique du premier lot | article et supplément ; pas de données brutes complètes | article et données étendues ; données et code sur demande | article et équations principales ; pas de dépôt complet des événements et du code |
| Limite comparative majeure | cause du déplacement non identifiée | précision élevée ne vaut pas supériorité | dépendance constitutive à la théorie utilisée pour l’inversion |

## 3. Écarts numériques indicatifs

À partir des trois valeurs dérivées publiées et de leurs incertitudes nominales, en supposant provisoirement des erreurs indépendantes et gaussiennes, les écarts indicatifs sont :

| Paire | Écart sur `alpha^-1` | Incertitude combinée nominale | Écart indicatif |
|---|---:|---:|---:|
| césium – rubidium | `160 × 10^-9` | `29.2 × 10^-9` | `5.49 sigma` |
| césium – `g−2` | `120 × 10^-9` | `30.9 × 10^-9` | `3.89 sigma` |
| rubidium – `g−2` | `40 × 10^-9` | `18.6 × 10^-9` | `2.15 sigma` |

Ces nombres ont une fonction descriptive limitée.

Ils ne remplacent pas l’ajustement CODATA, parce qu’ils :

- utilisent les valeurs dérivées plutôt que les données D1–D6 ;
- supposent une indépendance nominale qui n’est pas établie dans toutes ses dimensions ;
- ne propagent pas les constantes ajustées et les covariances communes ;
- n’intègrent pas la décision d’expansion des incertitudes ;
- ne diagnostiquent aucune cause physique ou instrumentale.

Leur portée autorisée est seulement :

> Le sous-ensemble des déterminations publiées n’est pas numériquement cohérent sous ses seules incertitudes nominales, la discordance étant principalement structurée par la position de la voie césium.

Cette formulation ne signifie pas que la voie césium est démontrée fautive.

## 4. Décomposition de l’indépendance

L’indépendance doit être qualifiée selon plusieurs dimensions.

| Dimension | Césium–rubidium | Recul–`g−2` | Verdict comparatif |
|---|---|---|---|
| appareils | distincts | fortement distincts | indépendance instrumentale substantielle admise |
| espèces ou système physique | atomes différents | atomes contre électron unique | observables physiquement distinctes admises |
| observable première | deux reculs atomiques de même famille | recul contre anomalie magnétique | forte distinction des observables admise |
| relation de passage | même forme métrologique | relations différentes | non-équivalence des inférences admise |
| données auxiliaires | `Ar(e)`, `R_inf`, architecture métrologique communes | rapports de masses et ajustement communs, mais théories principales différentes | indépendance auxiliaire complète refusée |
| systématiques | familles optiques proches, budgets et montages distincts | familles expérimentales différentes | corrélation inter-expériences non quantifiée |
| insertion finale | même ajustement CODATA | même ajustement CODATA | dépendance commune au niveau de la recommandation |

La différence d’appareil ne suffit donc pas à établir une indépendance probatoire complète.

## 5. Comparaison des architectures de correction

### 5.1 Césium

```text
correction nette publiée : -4.58 ppb ;
incertitude systématique : 0.12 ppb ;
termes dominants : phase de Gouy et gradients d’accélération ;
architecture : plusieurs grandes corrections de même signe,
               soutenues par mesures auxiliaires et simulations.
```

### 5.2 Rubidium

```text
correction systématique nette : +64.2 × 10^-11 ;
incertitude systématique : 6.8 × 10^-11 ;
terme dominant : phase de Gouy/front d’onde à +108.2 × 10^-11 ;
architecture : compensation entre plusieurs corrections importantes de signes opposés.
```

### 5.3 `g−2`

```text
pas de grande correction nette unique comparable aux voies de recul ;
incertitudes dominantes : élargissement cyclotron et correction de cavité ;
architecture : reconstruction de profils de raie et modèle électromagnétique du piège,
               puis théorie QED pour le passage vers alpha.
```

La comparaison des amplitudes de corrections ne permet pas un classement direct. Une grande correction peut être bien déterminée ; une faible correction nette peut résulter de compensations ; une théorie de passage peut porter une profondeur de dépendance sans correction expérimentale analogue.

## 6. Dualité propre à la voie `g−2`

La voie `g−2` doit déclarer son sens d’inférence.

```text
sens A — détermination de alpha :
  a_e mesuré + modèle standard supposé valide -> alpha(a_e) ;

sens B — test du modèle standard :
  alpha externe obtenu par recul + modèle standard -> prédiction de a_e.
```

Interdit comparatif :

```text
utiliser la voie g−2 pour déterminer alpha
puis compter l’accord reconstruit avec la même relation
comme confirmation indépendante de la QED.
```

Dans la comparaison α2, `g−2` est retenu dans le sens A : détermination conditionnelle de `alpha`.

## 7. Rôle de CODATA

CODATA n’ajoute pas une quatrième mesure. Il transforme le conflit entre données et équations d’observation en une sortie recommandée accompagnée d’une incertitude élargie.

```text
ajustement initial :
  chi² = 109.6 pour 54 degrés de liberté ;
  probabilité = 0.001 % ;
  rapport de Birge = 1.42 ;

traitement :
  facteur d’expansion 2.5 sur D1–D6 ;

ajustement final global :
  chi² = 44.2 pour 54 degrés de liberté ;
  probabilité = 0.83 ;
  rapport de Birge = 0.90 ;

sortie :
  alpha^-1 = 137.035 999 177(21).
```

La décision CODATA soutient une cohérence opérationnelle de l’ajustement après élargissement. Elle ne démontre pas que les causes de la discordance ont été résolues ou que les trois chaînes sont physiquement équivalentes.

## 8. Comparabilité, cohérence et équivalence

### 8.1 Comparabilité

Admise conditionnellement : les trois sorties peuvent être transportées vers une même convention de basse énergie et comparées numériquement.

### 8.2 Cohérence nominale

Refusée pour le triplet pris avec les seules incertitudes publiées : la paire césium–rubidium présente notamment un écart indicatif supérieur à cinq incertitudes combinées nominales.

### 8.3 Cohérence ajustée

Admise au sens opérationnel de CODATA après expansion commune des incertitudes : les données sont conservées dans un ajustement global statistiquement acceptable.

### 8.4 Équivalence

Refusée : les chaînes ne mesurent pas la même observable, n’emploient pas la même théorie de passage et ne portent pas le même mode de soutien probatoire.

### 8.5 Convergence causale

Suspendue : l’état actuel ne permet pas d’attribuer la discordance à une correction déterminée, à une expérience précise, au calcul QED ou à une contribution physique nouvelle.

## 9. Accessibilité et reproductibilité

| Voie | Reproduction publique du premier lot | Limite |
|---|---|---|
| césium | méthode, supplément, corrections et simulations décrites | absence de données brutes et de code complets |
| rubidium | article, données étendues et budgets publiés | données détaillées et code sur demande |
| `g−2` | méthode, équations et budget publiés | événements, séries temporelles et chaîne complète de calcul non déposés |
| CODATA | données ajustées, équations et décisions publiées | reproduction numérique complète non effectuée dans α2 |

La comparaison est donc documentaire et analytique. Elle ne constitue pas une reproduction expérimentale ou computationnelle indépendante.

## 10. Résultat comparatif préparatoire

```text
admission :
  trois observables premières distinctes ;
  trois déterminations comparables sous une convention commune ;
  indépendance instrumentale substantielle ;
  discordance nominale documentée ;
  traitement explicite de cette discordance par CODATA ;

refus :
  équivalence des chaînes ;
  indépendance probatoire complète ;
  classement par la seule précision nominale ;
  valeur CODATA comme quatrième mesure ;
  accord après expansion comme résolution causale ;

suspension :
  cause de la discordance ;
  covariance inter-chaînes complète ;
  identification d’une chaîne fautive ;
  rôle éventuel d’une physique au-delà du modèle standard ;
  préférence scientifique finale entre les trois déterminations.
```

## 11. Condition d’arrêt de la matrice

La matrice comparative est suffisamment instruite lorsque l’on peut distinguer :

```text
ce qui est comparable : les sorties numériques sous convention commune ;
ce qui est indépendant : plusieurs appareils et observables premières ;
ce qui est partagé : certaines relations, entrées auxiliaires et l’ajustement CODATA ;
ce qui est incohérent : le triplet sous incertitudes nominales ;
ce qui est rendu opératoire : une valeur recommandée après expansion ;
ce qui demeure inconnu : la cause de la discordance.
```

Cette condition est remplie pour le premier lot. Le verdict comparatif local α2 peut être formulé séparément et soumis à validation humaine.
