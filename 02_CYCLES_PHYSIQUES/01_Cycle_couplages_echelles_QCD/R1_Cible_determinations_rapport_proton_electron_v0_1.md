# R1 — Cible et déterminations du rapport proton–électron `m_p/m_e` v0.1

## 0. Statut

```text
statut : instruction scientifique préparatoire du premier lot R1–R3 ;
date : 26 juillet 2026 ;
issue : #45 ;
fonction : verrouiller la cible, les sources et les chaînes de détermination ;
ne vaut pas : verdict final sur le rapport,
               ouverture des accès temporels ou astrophysiques,
               clôture de la dette m_e,
               propagation dans la synthèse active,
               ni modification du cadre canonique.
```

## 1. Question R1

> Que désigne exactement la valeur actuelle de `m_p/m_e`, et par quelles chaînes d’observables, de relations théoriques et d’ajustement devient-elle déterminable ?

R1 ne demande pas encore si le rapport varie. Il distingue :

```text
observable première ;
relation de passage ;
constantes auxiliaires ;
sortie inférée ;
sortie ajustée ;
dépendances et corrélations entre chaînes.
```

## 2. Verrou de notation

Dans ce dossier :

```text
rho_pe := m_p/m_e.
```

Le symbole `mu` n’est pas employé sans définition, car la littérature utilise selon les domaines :

```text
mu = m_p/m_e ;
mu = m_e/m_p ;
mu = masse réduite nucléaire ;
mu_pd = m_p m_d/(m_p + m_d).
```

Toute comparaison doit donc déclarer la convention avant de comparer des valeurs, des sensibilités ou des dérives.

## 3. Verrou de versions et de sources

### 3.1 Corpus ajusté CODATA 2022

Source directrice : Mohr, Newell, Taylor et Tiesinga, *CODATA recommended values of the fundamental physical constants: 2022*, rapport détaillé publié en 2025 et fondé sur les données disponibles au 31 décembre 2022.

Valeur recommandée :

```text
m_p/m_e = 1836.152 673 426(32) ;
incertitude relative : 1.7 × 10^-11.
```

Cette valeur est une sortie du moindre carré global CODATA. Elle n’est ni une mesure unique ni une moyenne autonome de quelques valeurs publiées de `m_p/m_e`.

### 3.2 Résultat postérieur au corpus CODATA 2022

Alighanbari, Schenkel, Korobov et Schiller, *High-accuracy laser spectroscopy of H2+ and the proton–electron mass ratio*, Nature 2025.

Sortie spectroscopique principale :

```text
[m_p/m_e]_H2+ = 1836.152 673 414(47).
```

Cette valeur est postérieure à la date de clôture CODATA 2022. Elle doit être conservée comme comparaison externe actuelle, sans être réinjectée rétroactivement dans la valeur CODATA 2022.

### 3.3 Sources primaires structurantes du corpus 2022

```text
proton / masses baryoniques :
  Heiße et al. 2017, valeur réanalysée et corrigée en 2019 ;
  Rau et al. 2020, rapports de fréquences impliquant d et HD+ ;

electron :
  Sturm et al. 2014 et Köhler et al. 2015,
  rapports spin/cyclotron d’électrons liés dans des ions hydrogénoïdes,
  associés aux calculs du facteur g lié ;

spectroscopie moléculaire HD+ :
  Alighanbari et al. 2020 ;
  Patra et al. 2020 ;
  Kortunov et al. 2021, avec correction d’auteur 2024 ;
  théorie consolidée pour CODATA par Karr et Koelemeij 2023.
```

## 4. Cible exacte

`m_p/m_e` est un rapport sans dimension de masses de repos actuelles, mais sa détermination ne consiste pas à placer directement un proton et un électron libres sur une balance commune.

Dans CODATA :

```text
m_p/m_e = A_r(p)/A_r(e),
```

où `A_r(p)` et `A_r(e)` sont des constantes ajustées dans un réseau plus large.

La cible est donc simple algébriquement mais composite du point de vue probatoire :

```text
rapport final simple
≠ chaîne de détermination simple
≠ observable première unique.
```

## 5. Chaîne A — spectrométrie de masse du proton et réseau des masses légères

### 5.1 Observable première

Pour des ions de charges connues dans un même champ magnétique :

```text
omega_c(X^{n+}) / omega_c(Y^{p+})
= n A_r(Y^{p+}) / [p A_r(X^{n+})].
```

L’observable est un rapport de fréquences cyclotron, non `m_p/m_e` lui-même.

### 5.2 Entrée proton principale dans CODATA 2022

L’entrée D15 est le rapport :

```text
omega_c(12C6+) / omega_c(p),
```

qui contraint `A_r(p)` relativement à l’ion carbone, après prise en compte :

```text
A_r(e) ;
énergie de liaison électronique de 12C6+ ;
alpha ;
R_inf ;
charge ionique déclarée.
```

La valeur de 2017 a été réanalysée et corrigée en 2019 ; cette dernière supersède la première.

### 5.3 Réseau baryonique associé

CODATA utilise aussi des rapports de fréquences impliquant :

```text
12C6+ / d ;
H2+ / d ;
12C4+ / HD+ ;
HD+ / 3He+ ;
t / 3He+ ;
4He2+ / 12C6+.
```

Ces entrées relient `A_r(p)`, `A_r(d)`, `A_r(h)`, `A_r(t)` et `A_r(alpha)` avec les masses électroniques et les énergies d’ionisation ou de liaison nécessaires.

### 5.4 Traitement des tensions

CODATA signale des incohérences entre plusieurs rapports cyclotron provenant notamment de Washington, Heidelberg et Florida State University. Un facteur d’expansion `2.5` est appliqué au sous-ensemble pertinent de données de masses afin de ne pas laisser les incertitudes nominales sous-représenter cette dispersion.

Cette opération :

```text
admet les données dans l’ajustement ;
élargit leur poids effectif ;
ne désigne pas une expérience fautive ;
ne démontre aucune variation physique du rapport.
```

## 6. Chaîne B — masse électronique par résonance de spin d’un électron lié

### 6.1 Observable première

Les expériences sur des ions hydrogénoïdes mesurent un rapport entre :

```text
fréquence de précession du spin de l’électron lié ;
fréquence cyclotron de l’ion.
```

CODATA utilise notamment les entrées D7 et D10 pour `12C5+` et `28Si13+`.

### 6.2 Relation de passage

L’inférence de `A_r(e)` mobilise :

```text
facteur g théorique de l’électron lié ;
corrections QED, nucléaires et de recul ;
masse relative de l’ion ;
énergies de liaison ;
alpha et R_inf ;
termes théoriques résiduels explicites.
```

L’électron libre n’est donc pas directement comparé au proton dans la chaîne moderne dominante. Le rapport final combine une masse protonique issue de rapports cyclotron et une masse électronique issue d’une résonance de spin liée à une théorie du facteur `g`.

### 6.3 Rang

```text
mesuré : rapports de fréquences ;
calculé : facteur g lié et corrections ;
inféré : A_r(e) ;
ajusté : cohérence avec le réseau CODATA ;
dérivé : m_p/m_e.
```

## 7. Chaîne C — spectroscopie rovibrationnelle de `HD+`

### 7.1 Observable première

Trois ensembles expérimentaux de fréquences hyperfines résolues sont intégrés dans CODATA 2022 :

```text
D27 : transition HD+ mesurée par Alighanbari et al. ;
D28 : transition HD+ mesurée par Kortunov et al. ;
D29 : transition HD+ mesurée par Patra et al.
```

Les observables sont des fréquences rovibrationnelles, non un rapport de masses directement lu.

### 7.2 Relation de passage

CODATA compare chaque fréquence expérimentale à une fréquence théorique :

```text
f_exp ≐ f_th(A_r(e), A_r(p), A_r(d), R_inf, r_p, r_d, ...) + delta_th.
```

Les calculs sont paramétrés notamment par :

```text
lambda_pd = [A_r(p) A_r(d)/(A_r(p)+A_r(d))] / A_r(e) ;
lambda_d  = A_r(d)/A_r(e) ;
R_inf ;
r_p ;
r_d ;
corrections relativistes, QED et hyperfines.
```

CODATA introduit D30–D32 comme corrections théoriques additives portant les termes non calculés.

### 7.3 Conséquence

La spectroscopie `HD+` ne détermine pas isolément `m_p/m_e`. Elle contraint d’abord des combinaisons de masses et d’autres constantes. Le rapport `m_p/m_e` apparaît après résolution conjointe du réseau ou après ajout d’informations sur `m_d/m_p`, `R_inf` et les rayons nucléaires.

### 7.4 Correction 2024

La correction d’auteur du résultat Kortunov et al. modifie la présentation et la valeur comparative publiée, mais indique que les conclusions de l’article restent inchangées. Pour CODATA 2022, les objets actifs sont les fréquences expérimentales et les équations théoriques réévaluées, non la valeur dérivée isolée publiée dans l’article original.

## 8. Chaîne D — spectroscopie `H2+` post-CODATA 2022

### 8.1 Observable et inférence

L’expérience de 2025 mesure une transition rovibrationnelle `H2+` sans Doppler avec une incertitude fractionnaire de `8 × 10^-12`, puis ajuste `m_p/m_e` par comparaison à un calcul ab initio.

Sortie :

```text
[m_p/m_e]_H2+ = 1836.152 673 414(47).
```

Elle est compatible avec CODATA 2022 :

```text
[m_p/m_e]_CODATA22 = 1836.152 673 426(32).
```

### 8.2 Position probatoire

Le résultat `H2+` :

```text
est externe au corpus CODATA 2022 ;
possède une observable et un appareil distincts de la spectrométrie de masse ;
reste conditionnel à la théorie moléculaire et à des constantes auxiliaires ;
utilise un formalisme QED apparenté à celui des analyses HD+ ;
ne constitue pas une mesure directe du rapport.
```

L’article précise que certaines sorties `H2+` et `HD+` ne sont pas indépendantes au sens fondamental lorsqu’elles partagent appareil, équipe, formalisme théorique, routines numériques et données atomiques auxiliaires.

## 9. Matrice comparative des chaînes

| Chaîne | Observable première | Relation de passage dominante | Sortie immédiate | Dépendances majeures | Statut par rapport à CODATA 2022 |
|---|---|---|---|---|---|
| Proton en piège de Penning | rapports `omega_c` entre ions | charges, masses ioniques, énergies de liaison | `A_r(p)` et réseau des masses légères | `A_r(e)`, liaisons, champ et effets du piège | entrée du LSA |
| Électron lié | rapport spin/cyclotron | facteur `g` lié et QED | `A_r(e)` | `alpha`, masses ioniques, liaisons, théorie | entrée du LSA |
| `HD+` | fréquences rovibrationnelles | théorie à trois corps + corrections | combinaisons de rapports de masses | `R_inf`, rayons, `A_r(d)`, QED, hyperfine | entrées D27–D32 du LSA |
| CODATA 2022 | ensemble des données | moindre carré corrélé | valeur recommandée `m_p/m_e` | toutes les entrées et covariances retenues | sortie ajustée |
| `H2+` 2025 | fréquence rovibrationnelle | calcul ab initio + LSA local | valeur spectroscopique `m_p/m_e` | `R_inf`, rayon protonique, QED moléculaire | comparaison postérieure |

## 10. Dépendances et indépendances

### 10.1 Distinction des appareils

```text
Penning / ESR :
  mouvement cyclotron et précession de spin ;

spectroscopie moléculaire :
  fréquences rovibrationnelles d’ions moléculaires ;

CODATA :
  ajustement statistique de toutes les relations déclarées.
```

Cette distinction suffit à parler de chaînes expérimentales différentes, mais non d’indépendance probatoire complète.

### 10.2 Dépendances communes

Les chaînes peuvent partager :

```text
alpha ;
R_inf ;
énergies de liaison ;
calculs QED ;
masses de référence ;
rayons nucléaires ;
données H, D et muoniques ;
routines théoriques ou équipes communes ;
traitement CODATA des covariances.
```

### 10.3 Non-indépendance de CODATA et HD+

La valeur CODATA 2022 inclut déjà les fréquences `HD+`. Elle ne peut donc être utilisée comme comparaison indépendante d’une valeur `HD+` reconstruite à partir des mêmes données.

### 10.4 Indépendance partielle de `H2+` 2025

`H2+` 2025 est extérieur à l’ajustement 2022 et fournit une nouvelle observable. Son indépendance reste partielle, car la conversion en rapport mobilise un cadre théorique et des constantes auxiliaires apparentés à ceux de la spectroscopie `HD+`.

## 11. Résultat R1 préparatoire

```text
admission :
  m_p/m_e est une cible sans dimension définie sans ambiguïté
  lorsque la convention est déclarée ;
  la valeur CODATA 2022 est une sortie ajustée composite ;
  les chaînes Penning/ESR et moléculaires reposent
  sur des observables et appareils distincts ;
  les données HD+ contribuent directement à CODATA 2022 ;
  H2+ 2025 fournit une comparaison postérieure compatible ;

refus :
  traiter CODATA comme une mesure indépendante ;
  traiter les valeurs HD+ incluses dans CODATA
  comme comparaisons externes indépendantes ;
  appeler directement mesuré un rapport obtenu
  par spectroscopie et calcul ab initio ;
  réduire la chaîne moderne à une comparaison libre
  proton/électron dans un même piège ;
  déduire la simplicité probatoire du caractère sans dimension ;

suspension :
  covariance complète entre les chaînes moléculaires ;
  poids futur de H2+ 2025 dans CODATA 2026 ;
  cause exacte des tensions historiques entre masses légères ;
  classement définitif des chaînes par robustesse ;
  verdict sur une variation temporelle ou spatiale.
```

## 12. Gain pour la suite

R1 établit que la valeur actuelle du rapport n’est pas portée par une chaîne unique :

```text
m_p/m_e actuel
=
réseau de masses ioniques
+ résonance de spin liée
+ théorie QED
+ spectroscopie moléculaire
+ constantes auxiliaires
+ ajustement corrélé.
```

R2 devra donc examiner les contraintes de variation en demandant, pour chaque horloge ou spectre moléculaire, quelle combinaison de `m_p`, `m_e`, paramètres nucléaires et coefficients de sensibilité est réellement testée.

## 13. Condition d’arrêt de R1

```text
cible : verrouillée ;
notation : verrouillée ;
valeur CODATA 2022 : classée comme sortie ajustée ;
chaîne Penning/ESR : reconstruite ;
chaîne HD+ : reconstruite ;
H2+ 2025 : séparée comme résultat post-CODATA ;
dépendances et non-indépendances principales : déclarées ;
verdict sur la variation : non ouvert.
```
