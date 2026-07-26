# R2 — Accès à la variation du rapport proton–électron `m_p/m_e` v0.1

## 0. Statut

```text
statut : instruction scientifique préparatoire du premier lot R1–R3 ;
date : 26 juillet 2026 ;
issue : #45 ;
fonction : comparer les accès temporels locaux et astrophysiques ;
ne vaut pas : verdict final sur la constitution du rapport,
               clôture de la dette m_e,
               combinaison numérique inter-domaines,
               propagation dans la synthèse active,
               ni modification du cadre canonique.
```

## 1. Question R2

> Que contraint réellement chaque accès lorsqu’il est présenté comme un test de variation de `m_p/m_e` ?

Dans tout le document :

```text
rho_pe := m_p/m_e.
```

R2 distingue trois objets qui ne doivent pas être convertis l’un dans l’autre sans modèle supplémentaire :

```text
dérive locale :
  (1/rho_pe) d rho_pe/dt autour du présent ;

modulation locale :
  réponse périodique corrélée à une variable déclarée,
  ici le potentiel gravitationnel solaire ;

différence astrophysique finie :
  Delta rho_pe/rho_pe entre un absorbeur distant
  et la référence de laboratoire actuelle.
```

Une ligne de visée cosmologique mélange nécessairement distance, époque et environnement. Elle ne constitue donc pas un test temporel pur au même sens qu’une série d’horloges dans un laboratoire.

## 2. Corpus primaire borné

### 2.1 Horloges

Source directrice :

- R. Lange et al., *Improved limits for violations of local position invariance from atomic clock comparisons*, Physical Review Letters 126, 011102 (2021), arXiv:2010.06620.

Cette source compare :

```text
Yb+ E3 / Yb+ E2 :
  ratio de deux transitions optiques,
  principalement discriminant pour alpha ;

Yb+ E3 / Cs :
  fréquence optique référencée à deux fontaines au césium,
  sensible à alpha, rho_pe et à un paramètre nucléaire X_q.
```

### 2.2 Spectres moléculaires radio

Source directrice :

- S. Muller et al., *A study of submillimeter methanol absorption toward PKS 1830−211: excitation, invariance of the proton–electron mass ratio, and systematics*, Astronomy & Astrophysics 652, A5 (2021), arXiv:2105.08015.

Cette source analyse des transitions du méthanol dans l’absorbeur à `z = 0.89` vers PKS 1830−211, avec des coefficients de sensibilité `K_mu` différents et une régression multivariée des déplacements de vitesse.

### 2.3 Spectres moléculaires optiques

Source directrice :

- M. Daprà et al., *Constraint on a varying proton-to-electron mass ratio from H2 and HD absorption at z_abs ≃ 2.34*, Monthly Notices of the Royal Astronomical Society 465, 4057–4073 (2017), arXiv:1611.05191.

Cette source analyse 106 transitions `H2` et `HD` dans l’absorbeur vers Q1232+082, avec ajustement global des profils et traitement explicite des distorsions de calibration en longueur d’onde.

## 3. Forme générale des observables

### 3.1 Horloges

Pour une fréquence de transition `F`, la source adopte une paramétrisation de la forme :

```text
Delta F/F
=
  k_alpha Delta alpha/alpha
+ k_mu Delta rho_pe/rho_pe
+ k_q Delta X_q/X_q.
```

Les coefficients `k` sont des coefficients théoriques de sensibilité de la transition. Le résultat sur `rho_pe` ne provient donc pas de la seule stabilité instrumentale des horloges : il dépend aussi de la séparation des sensibilités à `alpha` et au secteur nucléaire.

### 3.2 Spectres astrophysiques

Pour deux transitions moléculaires `i` et `j` :

```text
Delta v/c
=
Delta K_mu × Delta rho_pe/rho_pe,
```

avec :

```text
Delta K_mu := K_mu,i - K_mu,j.
```

L’observable première est un déplacement relatif de fréquence, de longueur d’onde ou de vitesse entre raies. La sortie `Delta rho_pe/rho_pe` est obtenue après :

```text
fréquences de laboratoire ;
coefficients de sensibilité calculés ;
modèle cinématique de l’absorbeur ;
calibration de l’instrument ;
modèle des profils de raie ;
hypothèse que les transitions comparées sondent
une matière suffisamment co-spatiale ou modélisable.
```

## 4. Accès A — comparaisons d’horloges

### 4.1 Observable première

Lange et al. utilisent deux séries :

```text
11 mesures du ratio Yb+ E3/E2
sur environ 1 500 jours ;

mesures absolues de Yb+ E3
référencées à deux fontaines Cs
sur plusieurs années.
```

La première série isole principalement `alpha`, parce que les deux fréquences sont optiques et ont des sensibilités relativistes différentes.

La seconde compare une transition électronique optique à une transition hyperfine du césium. Elle possède donc une sensibilité non nulle à :

```text
alpha ;
rho_pe ;
X_q := m_q/Lambda_QCD,
paramètre représentant une dépendance nucléaire résiduelle.
```

### 4.2 Familles de variation testées

Deux familles sont ajustées :

```text
famille T1 : dérive linéaire en fonction du temps ;

famille T2 : modulation annuelle en phase
             avec la variation du potentiel solaire à la Terre.
```

Ces familles ne couvrent pas :

```text
transitoires courts ;
oscillations à fréquence libre ;
variations non linéaires ;
dépendances spatiales non corrélées au potentiel solaire ;
changements anciens ou cosmologiques.
```

### 4.3 Résultats

La combinaison des mesures et des sensibilités donne :

```text
(1/rho_pe) d rho_pe/dt
= -8(36) × 10^-18 par an ;

(c^2/rho_pe) d rho_pe/dPhi
= 7(45) × 10^-8.
```

Les deux résultats sont compatibles avec zéro.

### 4.4 Dépendances probatoires

Le résultat de dérive sur `rho_pe` n’est pas fourni par un unique ratio d’horloges. Il mobilise :

```text
la dérive mesurée de E3/Cs ;
la contrainte sur alpha issue de E3/E2 ;
une contrainte antérieure sur X_q ;
les coefficients de sensibilité atomiques et nucléaires ;
les corrections systématiques des horloges ;
la réalisation du temps par les fontaines Cs.
```

La valeur obtenue est donc un résultat de séparation paramétrique dans un réseau de comparaisons.

### 4.5 Rang local

```text
mesuré :
  ratios de fréquences au cours du temps ;

calculé :
  coefficients de sensibilité et corrections ;

ajusté :
  pente linéaire et amplitude annuelle ;

inféré :
  dérive et couplage de rho_pe
  après séparation de alpha et X_q.
```

### 4.6 Portée

Cet accès soutient :

```text
absence de dérive linéaire détectée
au niveau déclaré autour du présent ;

absence de modulation annuelle détectée
corrélée au potentiel solaire
au niveau déclaré.
```

Il ne soutient pas une invariance temporelle universelle de `rho_pe`.

## 5. Accès B — méthanol radio à `z = 0.89`

### 5.1 Pourquoi le méthanol est sensible

Les transitions torsionnelles et rotationnelles du méthanol possèdent des coefficients `K_mu` variés. Une comparaison entre transitions de la même espèce réduit le risque de ségrégation chimique qui apparaît lorsque des molécules différentes sont comparées.

Cette réduction n’élimine pas :

```text
la structure spatiale du fond radio ;
la variabilité temporelle du quasar ;
les gradients de température ou de vitesse ;
les différences d’excitation entre transitions ;
les incertitudes de fréquences de repos ;
les effets de sélection de composantes cinématiques.
```

### 5.2 Observable et modèle

L’observable est le centroïde de vitesse `v_i` de chaque transition. Le modèle le plus simple serait :

```text
v_i/c
=
K_mu,i Delta rho_pe/rho_pe + constante.
```

Mais l’ajustement simple présente une dispersion excessive. La source introduit alors une régression multivariée comprenant notamment :

```text
K_mu ;
époque d’observation ;
énergie du niveau inférieur ;
terme constant.
```

La fréquence d’observation est également testée comme variable concurrente.

### 5.3 Déplacement d’attribution

Le résultat brut suggère que les centroïdes varient avec plusieurs variables. L’analyse montre que :

```text
la corrélation avec l’époque d’observation est dominante ;
une corrélation plus faible avec l’énergie inférieure
peut signaler un gradient température–vitesse ;
la corrélation avec la fréquence d’observation
n’est pas significative dans cette analyse ;
la corrélation résiduelle avec K_mu
n’est pas significative après régression multivariée.
```

Une partie du déplacement initialement disponible pour une attribution à `rho_pe` est donc réattribuée à l’évolution du fond radio et à la structure du gaz absorbant.

### 5.4 Résultat

La régression finale donne :

```text
Delta rho_pe/rho_pe
= (-1.8 ± 1.2) × 10^-7
à un écart-type ;

|Delta rho_pe/rho_pe|
< 3.6 × 10^-7
à trois écarts-types.
```

Le résultat est compatible avec zéro pour cette ligne de visée et ce modèle de systématiques.

### 5.5 Portée

Cet accès soutient :

```text
une non-détection locale sur une ligne de visée
à environ 7.5 milliards d’années de temps de regard ;

la capacité discriminante des coefficients K_mu ;

la nécessité d’intégrer la variabilité morphologique
et temporelle du fond radio dans l’attribution.
```

Il ne soutient pas une invariance cosmologique globale de `rho_pe`.

## 6. Accès C — `H2` et `HD` optiques à `z ≃ 2.34`

### 6.1 Observable et sensibilité

L’analyse utilise 106 transitions de `H2` et `HD` réparties sur une large plage spectrale. Les transitions de Lyman et Werner possèdent des coefficients de sensibilité différents mais un levier `Delta K_mu` beaucoup plus faible que les transitions très sensibles du méthanol.

L’information sur `rho_pe` provient donc d’une corrélation collective entre :

```text
positions des raies ;
coefficients K_mu ;
structure en composantes de vitesse ;
paramètres de largeur et de colonne ;
redshift commun ;
fréquences de laboratoire.
```

### 6.2 Modèle d’absorbeur

Les raies moléculaires sont ajustées simultanément avec :

```text
les raies H2 et HD partiellement superposées ;
la forêt Lyman-alpha ;
les raies métalliques pertinentes ;
plusieurs composantes cinématiques ;
un paramètre global Delta rho_pe/rho_pe.
```

L’accès ne compare donc pas des raies isolées une à une ; il dépend d’un modèle global de l’absorbeur.

### 6.3 Calibration concurrente

La source examine notamment :

```text
distorsions à longue portée de l’échelle de longueurs d’onde ;
distorsions intra-ordre ;
absence de calibrations ThAr attachées à certaines poses ;
redispersion et combinaison des expositions ;
choix de la structure cinématique.
```

L’incertitude systématique est dominée par les distorsions à longue portée. Une transformation instrumentale de l’échelle spectrale peut donc imiter une corrélation avec `K_mu`.

### 6.4 Résultat

La valeur publiée est :

```text
Delta rho_pe/rho_pe
= (19 ± 9_stat ± 5_sys) × 10^-6.
```

L’écart à zéro reste inférieur à deux écarts-types lorsque les incertitudes statistique et systématique sont considérées ensemble. La source le classe comme compatible avec les autres non-détections de la série d’absorbeurs étudiés.

### 6.5 Portée

Cet accès soutient :

```text
une contrainte de l’ordre de 10^-5
sur une ligne de visée à grand redshift ;

la possibilité de tester rho_pe
avec de nombreuses raies d’une même espèce ;

la nécessité de traiter explicitement
les distorsions spectrographiques et le modèle cinématique.
```

Il ne soutient ni une détection établie ni une invariance universelle.

## 7. Matrice comparative R2

| Accès | Observable première | Transformation testée | Relation de passage | Systématique discriminante | Sortie |
|---|---|---|---|---|---|
| Yb+/Cs et Yb+ E3/E2 | ratios de fréquences répétés | dérive linéaire locale | coefficients `k_alpha`, `k_mu`, `k_q` + séparation paramétrique | dérives systématiques des horloges, sensibilité nucléaire | `(1/rho_pe) d rho_pe/dt` |
| horloges et potentiel solaire | ratios de fréquences saisonniers | modulation annuelle imposée | phase et amplitude du potentiel solaire | saisonnalité instrumentale, séparation alpha/X_q | `(c^2/rho_pe) d rho_pe/dPhi` |
| méthanol PKS 1830−211 | centroïdes de raies radio | différence finie distante/locale | `Delta v/c = Delta K_mu Delta rho_pe/rho_pe` | évolution du fond radio, excitation et cinématique | `Delta rho_pe/rho_pe` à `z=0.89` |
| H2/HD Q1232+082 | positions de nombreuses raies optiques | différence finie distante/locale | ajustement global avec `K_mu` | distorsion de longueur d’onde et modèle de composantes | `Delta rho_pe/rho_pe` à `z≈2.34` |

## 8. Non-combinabilité directe

Les résultats ne doivent pas être réunis dans une moyenne unique parce que :

```text
les fonctions ajustées diffèrent ;
les périodes et domaines diffèrent ;
les variables concurrentes diffèrent ;
les conventions statistiques diffèrent ;
les covariances inter-domaines ne sont pas disponibles ;
une différence finie cosmologique
n’équivaut pas à une dérive linéaire locale.
```

Même une conversion indicative :

```text
Delta rho_pe/rho_pe divisé par un temps de regard
```

imposerait une histoire linéaire, monotone et spatialement uniforme que les observations ne testent pas.

## 9. Ce que chaque résultat négatif conserve

### 9.1 Horloges

Le résultat négatif conserve une information parce que le dispositif est sensible aux familles déclarées :

```text
pente linéaire ;
modulation annuelle à phase connue.
```

### 9.2 Méthanol

Le résultat négatif conserve une information après comparaison de transitions à `K_mu` différents et après introduction de variables concurrentes capables d’expliquer les déplacements de raies.

### 9.3 H2/HD

Le résultat conserve une information parce que le modèle global exploite de nombreuses raies avec des `K_mu` différents et évalue une transformation instrumentale concurrente. Sa portée reste limitée par la calibration spectrographique.

La compatibilité avec zéro n’est donc informative que relativement à une sensibilité et à une famille de transformations déclarées.

## 10. Résultat R2 préparatoire

```text
admission :
  les horloges contraignent une dérive linéaire locale
  et une modulation annuelle déclarée autour du présent ;

  les spectres moléculaires contraignent
  des différences finies sur des lignes de visée particulières ;

  les coefficients de sensibilité rendent les accès discriminants
  mais constituent des relations théoriques de passage ;

  les résultats examinés sont compatibles avec zéro
  dans leurs domaines et modèles respectifs ;

  les analyses astrophysiques montrent explicitement
  que l’attribution peut être déplacée vers l’instrument,
  le fond radio ou la structure cinématique ;

refus :
  une invariance temporelle ou cosmologique universelle ;

  la conversion automatique d’une différence cosmologique
  en dérive annuelle ;

  la déduction séparée d’une variation de m_p ou de m_e
  depuis le seul rapport ;

  la qualification de mesure directe de rho_pe ;

  la combinaison numérique des horloges,
  du méthanol et de H2/HD ;

  la compatibilité avec zéro comme preuve suffisante
  sans contrôle de la sensibilité et des transformations concurrentes ;

suspension :
  formes temporelles non linéaires ou transitoires ;

  homogénéité spatiale de rho_pe ;

  statut global sur l’ensemble du ciel et de l’histoire cosmique ;

  indépendance complète des coefficients de sensibilité
  et des modèles moléculaires ;

  attribution d’une éventuelle variation future
  au numérateur ou au dénominateur séparément.
```

## 11. Gain pour R3

R2 impose à R3 de ne pas expliquer les contraintes de variation par une formule unique du type :

```text
Delta rho_pe/rho_pe
=
Delta m_p/m_p - Delta m_e/m_e
```

sans préciser le modèle qui relie les observables aux transformations du proton et de l’électron.

R3 devra distinguer :

```text
identité algébrique du rapport ;
constitution QCD de la masse protonique ;
statut électrofaible de la masse électronique ;
coefficients de sensibilité des observables ;
modèles supplémentaires nécessaires
pour séparer numérateur et dénominateur.
```

## 12. Condition d’arrêt de R2

```text
horloges :
  observable, familles et dépendances déclarées ;

méthanol :
  sensibilité, régression et systématiques déclarées ;

H2/HD :
  modèle global et calibration concurrente déclarés ;

comparabilité fonctionnelle : établie ;
combinaison numérique : refusée ;
verdict de constitution : réservé à R3.
```
