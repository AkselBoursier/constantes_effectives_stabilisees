# α2 — Verdict comparatif local sur la valeur de basse énergie de `alpha` v0.1

## 0. Statut

```text
statut : verdict comparatif proposé, en attente de validation humaine ;
date : 26 juillet 2026 ;
opération : α2, issue #36 ;
entrées directes :
  A2_Extraction_CODATA_alpha_v0_1.md ;
  A2_Matrice_comparative_trois_chaines_alpha_v0_2.md ;
  A2_Fiche_voie_cesium_alpha_v0_1.md ;
  A2_Fiche_voie_rubidium_alpha_v0_1.md ;
  A2_Fiche_voie_gmoins2_alpha_v0_1.md ;
fonction : statuer localement sur la comparabilité des trois déterminations
           et sur le rang de la valeur recommandée CODATA ;
autorité : proposition soumise à validation de l’auteur ;
ne vaut pas : verdict sur alpha(Q²), variation temporelle ou spatiale,
               diagnostic causal de la discordance, nouvelle moyenne,
               clôture du dossier alpha entier ou propagation automatique.
```

## 1. Question tranchée

> Que représente une valeur recommandée de `alpha`, par quelles chaînes devient-elle déterminable, et que signifie le désaccord entre les trois déterminations du premier lot lorsque leurs observables, relations auxiliaires et dépendances théoriques diffèrent ?

## 2. Réponse courte

Les trois chaînes produisent des déterminations numériquement comparables de `alpha` dans une même convention de basse énergie, mais elles ne constituent ni trois mesures directes de la même observable ni trois confirmations probatoirement équivalentes.

Leur triplet est incohérent sous les seules incertitudes nominales publiées. CODATA ne résout pas la cause de cette discordance : il la traite méthodologiquement par une expansion commune des incertitudes, conserve les trois voies et produit une valeur recommandée opérationnelle issue d’un ajustement global.

La valeur CODATA est donc :

```text
une sortie ajustée et conditionnelle d’un réseau de données et de relations ;
non une mesure unique ;
non une quatrième détermination indépendante ;
non une preuve d’invariance physique de alpha.
```

## 3. Ce qui est admis

### 3.1 Trois mesures premières distinctes

```text
césium : h/m(133Cs) par recul atomique ;
rubidium : h/m(87Rb) par recul atomique ;
g−2 : a_e par spectroscopie d’un électron piégé.
```

Les appareils, systèmes physiques et observables premières sont distincts. Cette pluralité fournit une indépendance instrumentale et observationnelle substantielle.

### 3.2 Trois déterminations comparables sous convention commune

Chaque chaîne transforme son observable première en une valeur de `alpha^-1` à basse énergie par une relation déclarée. Les sorties peuvent donc être comparées numériquement dans la convention commune employée par CODATA.

Cette comparabilité est conditionnelle à :

```text
la validité des relations de passage ;
la propagation des entrées auxiliaires ;
les budgets d’incertitude ;
le sens d’inférence déclaré pour g−2 ;
la convention de basse énergie commune.
```

### 3.3 Une discordance nominale réelle

Les valeurs publiées sont :

```text
césium :   alpha^-1 = 137.035 999 046(27) ;
rubidium : alpha^-1 = 137.035 999 206(11) ;
g−2 :      alpha^-1 = 137.035 999 166(15).
```

Sous une comparaison indicative utilisant les incertitudes nominales comme indépendantes :

```text
césium–rubidium : 5.49 sigma ;
césium–g−2 :      3.89 sigma ;
rubidium–g−2 :    2.15 sigma.
```

Cette structure autorise à dire que le triplet n’est pas cohérent sous ses seules incertitudes nominales. Elle n’autorise pas à identifier la cause de l’écart ni à déclarer une voie fautive.

### 3.4 Le traitement CODATA comme décision méthodologique explicite

CODATA conserve D1–D6 et applique un facteur d’expansion commun de `2.5` à leurs incertitudes. La valeur recommandée devient :

```text
alpha^-1 = 137.035 999 177(21) ;
incertitude standard relative = 1.6 × 10^-10.
```

Ce traitement est admis comme production d’une référence opérationnelle prudente face à un sous-ensemble incohérent. Il préserve les données au lieu de sélectionner arbitrairement une chaîne.

### 3.5 Deux usages distincts de la voie `g−2`

La voie `g−2` peut légitimement :

```text
déterminer alpha, si le modèle standard est supposé valide ;

ou

tester le modèle standard, si alpha est fourni par une voie externe.
```

Ces deux usages sont admis à condition de ne pas être comptés simultanément comme preuves indépendantes.

## 4. Ce qui est refusé

### 4.1 La mesure directe de `alpha`

Aucune des trois expériences ne lit directement `alpha` comme observable première.

```text
mesure -> relation de passage -> détermination de alpha.
```

### 4.2 L’équivalence des chaînes

Les chaînes diffèrent par :

```text
observable ;
appareil ;
système physique ;
corrections ;
relation de passage ;
données auxiliaires ;
profondeur théorique ;
mode de soutien probatoire.
```

Elles sont comparables sans être équivalentes.

### 4.3 L’indépendance probatoire complète

La différence des appareils ne supprime pas :

- les dépendances communes des deux voies de recul à `Ar(e)` et `R_inf` ;
- l’architecture métrologique commune des reculs ;
- les entrées auxiliaires propres à la théorie de `a_e` ;
- l’insertion commune de toutes les voies dans CODATA ;
- les corrélations ou covariances inter-chaînes qui ne sont pas entièrement quantifiées dans le premier lot.

### 4.4 Le classement par la seule précision nominale

La voie rubidium est nominalement la plus précise, mais sa correction optique dominante et son insertion dans un sous-ensemble incohérent empêchent de convertir cette précision en preuve automatique de supériorité.

De même, la profondeur théorique de `g−2` et le résidu élevé du césium n’autorisent pas un classement de vérité sans diagnostic supplémentaire.

### 4.5 CODATA comme quatrième mesure

La valeur recommandée réutilise les données et relations des trois voies. Elle ne constitue pas une confirmation indépendante de celles-ci.

### 4.6 L’accord après expansion comme résolution physique

L’expansion des incertitudes rend l’ajustement statistiquement acceptable. Elle ne démontre pas :

```text
que les systématiques sont identifiées ;
que les chaînes décrivent exactement la même réalité probatoire ;
que le désaccord est purement statistique ;
que la physique sous-jacente est définitivement close.
```

### 4.7 Le désaccord comme variation physique de `alpha`

Le désaccord porte sur des déterminations contemporaines d’une valeur de référence, obtenues par des chaînes différentes. Il ne constitue pas un test de variation temporelle, spatiale ou avec l’échelle.

## 5. Ce qui demeure suspendu

```text
cause de la discordance entre les trois chaînes ;
identification éventuelle d’une systématique dominante non modélisée ;
suffisance complète des modèles optiques des deux voies de recul ;
suffisance complète des calculs QED d’ordre élevé ;
covariance inter-chaînes complète ;
indépendance effective des paramètres auxiliaires ;
rôle éventuel d’une contribution au-delà du modèle standard ;
préférence scientifique définitive entre les trois voies ;
évolution future de la recommandation après nouvelles mesures ou prochain ajustement CODATA.
```

La suspension n’équivaut ni à une égalité des hypothèses ni à une ignorance totale. Elle signifie que le premier lot ne discrimine pas suffisamment ces possibilités.

## 6. Statut comparatif des trois voies

### 6.1 Césium

```text
valeur publiée : conservée ;
chaîne : documentée ;
précision interne : admise dans son budget ;
résidu CODATA : élevé ;
cause du déplacement : suspendue ;
exclusion : refusée.
```

### 6.2 Rubidium

```text
valeur publiée : conservée ;
chaîne : documentée ;
précision interne : la plus élevée du premier lot ;
accord relatif avec g−2 : constaté ;
supériorité causale : non établie ;
classement définitif : refusé.
```

### 6.3 `g−2`

```text
mesure de a_e : admise comme ultraprécise ;
valeur de alpha : conditionnelle au modèle standard ;
accord relatif avec rubidium : constaté ;
indépendance de la QED : refusée ;
double usage comme détermination et test : interdit.
```

## 7. Statut de la valeur recommandée CODATA

La valeur recommandée possède le rang suivant :

```text
objet : sortie d’un ajustement global ;
fonction : référence numérique opérationnelle ;
conditions : jeu de données CODATA 2022,
             équations d’observation,
             covariances,
             facteur d’expansion,
             convention de basse énergie ;
portée : métrologique et comparative ;
limite : ne tranche pas la cause de la discordance.
```

Il n’est pas nécessaire de créer un nouveau statut transversal pour cette situation. Les catégories existantes suffisent : mesure première, détermination conditionnelle, ajustement et référence recommandée.

## 8. Réponse locale aux questions publiques

### Q1 — Comment les sciences établissent-elles et déplacent-elles la frontière entre variation et maintien ?

Dans α2, la dispersion des valeurs ne doit pas être attribuée à une variation physique de `alpha`. La frontière est maintenue en distinguant :

```text
variation de la grandeur physique ;
variation des sorties entre chaînes ;
révision d’une valeur recommandée ;
incertitude sur les relations et les corrections.
```

Le désaccord est ici localisé au niveau des déterminations et de leur cohérence, non au niveau d’une transformation physique de `alpha`.

### Q2 — Par quelles structures le maintien devient-il opératoire et que change-t-il pour l’enquête ?

La valeur de référence devient opératoire par une chaîne composite :

```text
observables hétérogènes ;
corrections instrumentales ;
relations théoriques ou métrologiques ;
entrées auxiliaires ;
covariances ;
ajustement par moindres carrés ;
expansion prudente des incertitudes ;
publication d’une valeur recommandée.
```

Cela change l’enquête : la question pertinente n’est plus seulement « quelle est la valeur ? », mais « quelle architecture permet de la recommander malgré des déterminations discordantes, et que laisse-t-elle irrésolu ? »

## 9. Verdict final proposé

```text
admission :
  comparabilité conditionnelle des trois déterminations
  sous une convention commune de basse énergie ;
  distinction substantielle des observables et appareils ;
  discordance nominale documentée ;
  valeur CODATA admise comme sortie ajustée et référence opérationnelle ;
  traitement de l’incohérence par expansion explicite des incertitudes ;

refus :
  mesure directe de alpha ;
  équivalence des chaînes ;
  indépendance probatoire complète ;
  cohérence du triplet sous les seules incertitudes nominales ;
  classement de vérité par la précision ;
  CODATA comme quatrième mesure ;
  double comptage de g−2 comme détermination et test indépendant ;
  désaccord comme variation physique de alpha ;
  accord après expansion comme résolution causale ;

suspension :
  cause de la discordance ;
  chaîne éventuellement biaisée ;
  covariance complète ;
  suffisance définitive des modèles expérimentaux et théoriques ;
  contribution éventuelle au-delà du modèle standard ;
  préférence scientifique finale entre les trois voies.
```

## 10. Condition de clôture d’α2

α2 peut être close après validation humaine de ce verdict, car le premier lot permet désormais de répondre séparément :

```text
ce qui est mesuré directement ;
ce qui est inféré ;
ce qui est ajusté ;
ce qui est comparable ;
ce qui est commun aux chaînes ;
ce qui est discordant ;
ce qui est rendu opérationnel ;
ce qui demeure suspendu.
```

La clôture d’α2 n’autoriserait pas automatiquement :

```text
la fusion de la PR 35 ;
la propagation dans la synthèse du cycle 1 ;
l’ouverture d’un verdict général « alpha est constante » ;
l’extension vers alpha(Q²), le temps ou les quasars.
```

Ces décisions doivent rester séparées.
