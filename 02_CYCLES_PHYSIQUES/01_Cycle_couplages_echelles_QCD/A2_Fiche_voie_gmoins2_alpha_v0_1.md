# α2 — Audit borné de la voie `g−2` de détermination de `alpha` v0.1

## 0. Statut

```text
statut : fiche scientifique locale en cours de ratification ;
date : 26 juillet 2026 ;
opération : α2, issue #36 ;
source expérimentale directrice : Fan, Myers, Sukra et Gabrielse,
                                  Phys. Rev. Lett. 130, 071801 (2023) ;
DOI : 10.1103/PhysRevLett.130.071801 ;
version inspectée : arXiv:2209.13084v2 ;
source théorique directrice : Aoyama, Kinoshita et Nio,
                              Phys. Rev. D 97, 036001 (2018) ;
DOI : 10.1103/PhysRevD.97.036001 ;
source de repondération : CODATA recommended values 2022,
                           Rev. Mod. Phys. 97, 025002 (2025) ;
fonction : reconstruire la voie depuis la mesure du moment magnétique électronique
           jusqu’à l’inférence conditionnelle de alpha ;
autorité : descriptive et locale ;
ne vaut pas : test indépendant et simultané de la QED,
               mesure directe de alpha, reproduction complète des calculs QED,
               verdict comparatif final α2, nouvelle valeur recommandée de alpha,
               ou propagation dans la synthèse active du cycle 1.
```

## 1. Résultat directeur

La voie `g−2` ne mesure pas directement `alpha`.

Elle mesure le rapport du moment magnétique de l’électron au magnéton de Bohr, ou de manière équivalente son anomalie magnétique :

```text
g/2 = -mu/mu_B ;
a_e = (g-2)/2 = g/2 - 1.
```

Une expression du modèle standard, dominée par la série perturbative de l’électrodynamique quantique (QED), relie ensuite `a_e` à `alpha`, aux rapports de masses leptoniques et aux contributions hadroniques et électrofaibles. Sous l’hypothèse que cette expression est correcte dans le domaine considéré, elle peut être inversée pour inférer `alpha`.

La chaîne est donc :

```text
observable première : fréquences cyclotron et d’anomalie d’un électron piégé ;
sortie expérimentale : g/2 ou a_e(exp) ;
relation de passage : a_e(SM ; alpha, rapports de masses, coefficients QED, ...) ;
sortie conditionnelle : alpha^-1(a_e) ;
insertion CODATA : D1 = a_e(exp), D2 = correction portant l’incertitude théorique.
```

Deux sens d’inférence doivent rester séparés :

```text
alpha externe fourni par une voie de recul
  -> test de la prédiction du modèle standard pour a_e ;

modèle standard supposé valide + a_e mesuré
  -> détermination conditionnelle de alpha.
```

La même relation ne peut pas être comptée simultanément comme détermination indépendante de `alpha` et comme test indépendant de la théorie qui produit cette détermination.

## 2. Valeur expérimentale publiée

Fan et al. rapportent :

```text
g/2 = 1.001 159 652 180 59(13) ;
a_e(exp) = 1.159 652 180 59(13) × 10^-3 ;
incertitude relative sur g/2 : 0.13 ppt.
```

Le résultat améliore d’un facteur `2.2` la mesure publiée en 2008 par une architecture expérimentale apparentée.

Les auteurs déconseillent de moyenner naïvement les mesures de 2008 et 2022, car les méthodes similaires peuvent porter des incertitudes corrélées difficiles à quantifier.

Dans CODATA 2022, l’entrée expérimentale correspond à :

```text
D1 : a_e(exp) = 1.159 652 180 59(13) × 10^-3 ;
incertitude standard relative : 1.1 × 10^-10.
```

La valeur de `alpha^-1` publiée par inversion n’est donc pas la donnée expérimentale brute de l’ajustement.

## 3. Architecture expérimentale

L’expérience utilise un électron unique dans un piège de Penning cylindrique, placé dans un champ magnétique d’environ `5.3 T` et refroidi près de son état quantique fondamental.

Les fréquences centrales sont :

```text
fréquence cyclotron libre : nu_c ;
fréquence de spin : nu_s = (g/2) nu_c ;
fréquence d’anomalie : nu_a = nu_s - nu_c.
```

Dans l’idéal :

```text
g/2 = 1 + nu_a/nu_c.
```

Le champ magnétique s’élimine dans le rapport, mais sa stabilité reste cruciale parce que les fréquences ne sont pas mesurées simultanément.

Le dispositif associe :

```text
piège de Penning cylindrique ;
solénoïde supraconducteur auto-écranté ;
refroidissement cryogénique ;
spectroscopie de sauts quantiques cyclotron et spin ;
détection non destructive par décalage de la fréquence axiale ;
théorème d’invariance de Brown–Gabrielse ;
mesure et correction des modes de cavité.
```

L’expérience mesure alternativement les résonances cyclotron et d’anomalie. Les fréquences sont extraites de profils de raies ajustés, puis combinées avec la fréquence axiale, les corrections relativistes et la correction de cavité.

## 4. Relation expérimentale corrigée

Dans le piège réel, les fréquences propres sont modifiées par le potentiel électrostatique et les imperfections géométriques. Le théorème d’invariance relie la fréquence cyclotron libre aux trois mouvements propres :

```text
nu_c² = nu_c_bar² + nu_z_bar² + nu_m_bar².
```

À la précision utile, le rapport `g/2` est reconstruit à partir :

```text
fréquence d’anomalie modifiée ;
fréquence cyclotron modifiée ;
fréquence axiale ;
correction relativiste ;
correction de déplacement par la cavité.
```

La correction de cavité constitue la seule correction explicitement ajoutée à la quantité directement reconstruite à partir des fréquences. Elle est néanmoins centrale, car le couplage de l’oscillateur cyclotron aux modes électromagnétiques du piège décale la fréquence cyclotron.

Les fréquences et facteurs de qualité des modes sont mesurés par plusieurs méthodes. Le résultat final combine onze valeurs obtenues à des champs magnétiques différents, donc avec des corrections de cavité différentes.

## 5. Organisation de l’analyse et contrôles

Les éléments de contrôle publiés comprennent :

- mesure conduite à l’aveugle vis-à-vis des résultats et prédictions antérieurs ;
- alternance des essais cyclotron et anomalie ;
- stabilisation renforcée du champ magnétique ;
- extraction des profils de raie avec modèles incluant le mouvement axial thermique ;
- comparaison à onze champs magnétiques ;
- plusieurs méthodes de détermination des modes de cavité ;
- traitement corrélé des déplacements de cavité à champs proches ;
- comparaison avec la mesure de 2008 sans moyenne recommandée.

Le premier lot public permet d’inspecter la méthode et les équations principales. Il ne contient pas un dépôt complet des événements de sauts quantiques, des séries temporelles et du code d’ajustement permettant une reproduction indépendante intégrale.

## 6. Budget d’incertitude expérimental

Le tableau publié exprime les incertitudes sur `g/2` en unités de `10^-13` :

| Source | Incertitude (`×10^-13`) | Fonction dans l’audit |
|---|---:|---|
| statistique | `0.29` | ajustement des profils cyclotron et anomalie |
| élargissement cyclotron | `0.94` | largeur supplémentaire du profil cyclotron |
| correction de cavité | `0.90` | modes, facteurs de qualité et imperfections du piège |
| paramagnétisme nucléaire | `0.12` | effet thermique des électrodes d’argent |
| déplacement par la puissance d’excitation de l’anomalie | `0.10` | dépendance à la force du drive |
| dérive du champ magnétique | `0.09` | correction de la variation lente du champ |
| **total** | **`1.3`** | incertitude finale publiée |

Les deux contributions dominantes sont donc :

```text
élargissement cyclotron : 0.94 × 10^-13 ;
correction de cavité :   0.90 × 10^-13.
```

La précision expérimentale dépend moins d’une grande correction nette unique que de la reconstruction des profils de raie et du modèle électromagnétique du piège.

## 7. Concentration du risque expérimental

### 7.1 Élargissement de la raie cyclotron

Le profil cyclotron observé est plus large que le profil idéal prédit. Les auteurs convoluent le modèle avec une gaussienne afin de représenter cet élargissement supplémentaire.

Des fluctuations rapides du champ magnétique constituent une explication possible, sans qu’une cause unique soit établie dans l’article. L’incertitude attribuée à cet élargissement est la plus grande contribution individuelle du budget.

Le verdict autorisé est :

```text
élargissement observé et intégré au budget : oui ;
cause expérimentale unique démontrée : non.
```

### 7.2 Correction de cavité

Les modes de la cavité :

- inhibent l’émission cyclotron et rendent les sauts quantiques observables ;
- déplacent simultanément la fréquence cyclotron ;
- dépendent des dimensions réelles, fentes, défauts d’usinage et contractions thermiques du piège.

Le calcul emploie un modèle renormalisé et remplace, pour les modes observés, les fréquences idéales par les fréquences et facteurs de qualité mesurés.

La cohérence des résultats à onze champs magnétiques constitue un contrôle important. Elle ne rend pas la correction indépendante du modèle de cavité et de ses imperfections résiduelles.

### 7.3 Corrélation avec l’expérience antérieure

L’expérience de 2022 utilise un nouvel appareil et améliore la stabilité, mais conserve une architecture conceptuelle proche de la mesure de 2008 : électron unique, piège cylindrique, fréquences cyclotron et anomalie, correction de cavité.

Les auteurs refusent eux-mêmes une moyenne naïve des deux résultats en raison de corrélations méthodologiques difficiles à déterminer.

Cette prudence doit être conservée dans α2 :

```text
réplication temporelle et nouvel appareil
≠
indépendance complète des familles de systématiques.
```

## 8. Expression théorique du modèle standard

L’anomalie théorique peut être écrite schématiquement :

```text
a_e(SM) = a_e(QED) + a_e(hadronique) + a_e(électrofaible).
```

La partie QED est une série asymptotique :

```text
a_e(QED)
  = C2 (alpha/pi)
  + C4 (alpha/pi)^2
  + C6 (alpha/pi)^3
  + C8 (alpha/pi)^4
  + C10 (alpha/pi)^5
  + contributions dépendant des masses du muon et du tau.
```

Les coefficients ne sont pas tous de même statut :

```text
ordres bas : expressions analytiques ou résultats extrêmement contrôlés ;
ordres élevés : combinaisons analytiques et intégrations numériques de nombreux diagrammes ;
terme d’ordre dix : dépendance à des milliers de diagrammes et à des intégrales numériques ;
contributions hadroniques et faibles : petites mais nécessaires à la précision visée.
```

Aoyama, Kinoshita et Nio ont réévalué la contribution universelle du dixième ordre après avoir identifié une attribution incorrecte de variables d’intégration dans une intégrale du sous-ensemble V. Leur résultat révisé est :

```text
A1^(10) = 6.678(192).
```

Cet épisode documente un point méthodologique important : la théorie de passage est extraordinairement précise, mais elle possède sa propre histoire de calcul, de vérification et de correction. Elle ne doit pas être traitée comme une boîte noire exacte.

## 9. Incertitude théorique dans CODATA

CODATA représente explicitement l’incertitude résiduelle de la théorie de `a_e` par une donnée auxiliaire :

```text
D2 : delta_e = 0.000(16) × 10^-12 ;
relation : delta_e ≐ delta_th(e).
```

L’équation d’observation devient :

```text
a_e(exp) ≐ a_e(th ; alpha, ...) + delta_th(e).
```

Cette structure empêche de confondre :

```text
mesure expérimentale D1 ;
calcul central de a_e(th) ;
incertitude résiduelle de théorie D2 ;
valeur de alpha inférée par inversion.
```

La route `g−2` est donc une chaîne mixte :

```text
métrologie de fréquence
+ électrodynamique du piège
+ QED perturbative
+ rapports de masses
+ contributions hadroniques et électrofaibles
+ inversion numérique.
```

## 10. Inversion vers `alpha`

Sous le modèle standard utilisé, la mesure de Fan et al. et la théorie donnent :

```text
alpha^-1(a_e) = 137.035 999 166(15) ;
incertitude relative : 0.11 ppb.
```

Cette valeur est plus proche de la détermination rubidium que de la détermination césium du premier lot.

Cette proximité autorise seulement :

```text
constat d’accord numérique relatif dans les incertitudes déclarées.
```

Elle n’autorise pas :

```text
diagnostic causal contre la voie césium ;
preuve que rubidium et g−2 sont indépendants à tous les niveaux ;
validation circulaire de la QED ;
classement définitif des trois chaînes.
```

## 11. Dualité logique : détermination ou test

La voie possède deux usages scientifiques légitimes.

### 11.1 Usage comme détermination de `alpha`

Entrées :

```text
a_e(exp) ;
expression du modèle standard ;
coefficients QED ;
rapports de masses ;
contributions hadroniques et faibles.
```

Sortie :

```text
alpha(a_e), conditionnelle à la validité de la relation théorique.
```

### 11.2 Usage comme test du modèle standard

Entrées :

```text
alpha obtenue indépendamment par recul ;
expression du modèle standard ;
a_e(exp).
```

Sortie :

```text
écart expérience–théorie, potentiellement sensible à une erreur de calcul,
à une entrée auxiliaire ou à une contribution au-delà du modèle standard.
```

### 11.3 Interdit de double comptage

```text
utiliser a_e + QED pour déterminer alpha
puis
réinjecter ce même alpha dans a_e + QED pour déclarer un test indépendant
```

constitue une circularité probatoire.

Une comparaison correcte doit déclarer le sens d’inférence retenu pour chaque résultat.

## 12. Repondération par CODATA 2022

CODATA conserve :

```text
D1 : mesure expérimentale de a_e ;
D2 : incertitude résiduelle du calcul théorique.
```

Le facteur d’expansion `2.5` est appliqué à D1–D6, c’est-à-dire à l’ensemble formé par la voie `g−2`, les deux voies de recul et leurs entrées auxiliaires directes.

Cette décision :

- ne signifie pas que la mesure `g−2` possède une erreur expérimentale identifiée ;
- ne signifie pas que le calcul QED est réfuté ;
- empêche que l’incertitude nominale de chaque voie domine un ensemble globalement incohérent ;
- conserve les trois chaînes dans l’ajustement ;
- élargit l’incertitude de la valeur recommandée.

Le mode de soutien probatoire est donc double :

```text
niveau expérimental local : mesure ultraprécise de a_e avec modèle du piège ;
niveau inférentiel : inversion d’une relation théorique du modèle standard ;
niveau inter-chaînes : voie conservée mais repondérée dans CODATA.
```

## 13. Ce que la voie soutient positivement

Dans son domaine, la voie soutient :

```text
une mesure extrêmement précise de g/2 et a_e ;
une architecture expérimentale explicite et contrôlée ;
une observable première indépendante des reculs atomiques ;
une inférence précise de alpha sous une théorie déclarée ;
un test très sensible du modèle standard lorsqu’un alpha externe est fourni.
```

Elle ne soutient pas seule :

```text
une mesure directe de alpha ;
l’exactitude absolue et définitive de tous les coefficients théoriques ;
l’absence de contribution au-delà du modèle standard ;
la cause de la discordance entre césium, rubidium et g−2 ;
la supériorité définitive de la valeur alpha(a_e) ;
un test indépendant de la QED lorsque alpha est inféré par cette même QED.
```

## 14. Verdict local préparatoire

```text
admission :
  la voie g−2 fournit une mesure ultraprécise de g/2 et a_e ;
  l’observable première est distincte des observables de recul atomique ;
  l’inversion du modèle standard produit une détermination conditionnelle de alpha ;
  la théorie de passage et son incertitude sont explicitement présentes dans CODATA ;

refus :
  traiter alpha comme observable directement mesurée ;
  présenter la voie comme indépendante de la QED qui relie a_e à alpha ;
  compter simultanément la même relation comme détermination et test indépendant ;
  déduire de la proximité avec le rubidium que le césium est fautif ;
  interpréter le désaccord inter-chaînes comme variation physique de alpha ;

suspension :
  suffisance complète des calculs d’ordre élevé et de leurs vérifications indépendantes ;
  importance résiduelle des termes inconnus ou des contributions au-delà du modèle standard ;
  indépendance effective complète à l’égard des paramètres auxiliaires ;
  cause de la discordance entre les trois chaînes ;
  pondération comparative finale et statut de la valeur recommandée.
```

Mode de soutien probatoire :

```text
spectroscopie quantique de fréquences
+ électrodynamique et correction de cavité
+ calcul perturbatif QED
+ contributions hadroniques et électrofaibles
+ inversion conditionnelle
+ repondération inter-chaînes par CODATA.
```

## 15. Symétrie et asymétrie avec les voies de recul

La grille commune demeure :

```text
observable première ;
relation de passage ;
corrections ;
modèles ;
incertitudes ;
insertion CODATA ;
verdict local.
```

L’asymétrie fondamentale est :

```text
césium et rubidium :
  mesure de recul
  + propagation métrologique relativement courte ;

g−2 :
  mesure de fréquence plus précise
  + relation théorique beaucoup plus profonde
  + inversion du modèle standard.
```

L’indépendance probatoire doit donc être décomposée :

```text
observables premières : fortement distinctes ;
relations de passage : distinctes ;
cible alpha : commune ;
ajustement CODATA : commun ;
indépendance complète : non établie par la seule différence instrumentale.
```

## 16. Dettes avant le verdict comparatif α2

1. mettre à jour la matrice des trois chaînes avec les résultats des audits locaux ;
2. comparer les budgets de corrections sans réduire les chaînes à leur précision nominale ;
3. distinguer accord numérique, indépendance instrumentale et indépendance théorique ;
4. expliciter le sens d’inférence de la voie `g−2` dans chaque comparaison ;
5. vérifier la disponibilité publique des données, codes et covariances des trois chaînes ;
6. formuler le verdict comparatif local α2 avec admission, refus et suspension ;
7. soumettre ce verdict à validation humaine avant toute clôture d’α2 ou propagation.

## 17. Condition d’arrêt de la fiche

La fiche `g−2` est suffisamment instruite lorsque l’on peut répondre séparément :

```text
ce qui est mesuré : fréquences cyclotron et anomalie, puis g/2 et a_e ;
ce qui est corrigé : effets de cavité, profils de raie, dérive et effets du piège ;
ce qui est calculé : série QED, masses leptoniques, contributions hadroniques et faibles ;
ce qui est inféré : alpha sous hypothèse du modèle standard ;
ce qui est repondéré : D1 et D2 dans le sous-ensemble CODATA D1–D6 ;
ce qui demeure inconnu : cause de la discordance et classement final des chaînes.
```

Cette condition est remplie pour le premier lot. La fiche reste préparatoire jusqu’à validation humaine et comparaison structurée des trois chaînes.