# α2 — Audit borné de la voie césium de détermination de `alpha` v0.1

## 0. Statut

```text
statut : fiche scientifique locale en cours de ratification ;
date : 26 juillet 2026 ;
opération : α2, issue #36 ;
source primaire directrice : Parker et al., Science 360, 191–195 (2018) ;
version inspectée : arXiv:1812.04130, incluant le matériel supplémentaire ;
source de repondération : CODATA recommended values 2022, Rev. Mod. Phys. 97, 025002 (2025) ;
fonction : reconstruire la chaîne césium depuis l’observable de recul jusqu’à la valeur inférée de alpha ;
autorité : descriptive et locale ;
ne vaut pas : diagnostic causal de la discordance, exclusion de la chaîne,
               verdict comparatif final α2, nouvelle valeur de alpha,
               ou propagation dans la synthèse active du cycle 1.
```

## 1. Résultat directeur

La voie césium ne mesure pas directement `alpha`.

Elle mesure d’abord une fréquence de recul atomique, dont est extrait le rapport `h/m(133Cs)`. Une relation métrologique et théorique, utilisant notamment la masse relative du césium, la masse relative de l’électron et la constante de Rydberg, permet ensuite d’inférer une valeur de `alpha`.

```text
observable première : phase d’interféromètre sensible au recul photonique ;
sortie expérimentale : h/m(133Cs) ;
relations auxiliaires : masses relatives, R_inf, h et c ;
sortie inférée : alpha^-1 ;
insertion ultérieure : donnée D4, avec D6, dans l’ajustement CODATA.
```

La chaîne doit donc être auditée à deux niveaux séparés :

1. extraction expérimentale de `h/m(133Cs)` ;
2. passage de `h/m(133Cs)` à `alpha`.

## 2. Valeurs publiées

Parker et al. rapportent :

```text
h/m(133Cs) = 3.002 369 4721(12) × 10^-9 m² s^-1 ;
alpha^-1 = 137.035 999 046(27) ;
incertitude relative totale sur alpha : 0.20 ppb ;
incertitude statistique : 0.16 ppb ;
incertitude systématique : 0.12 ppb.
```

Dans CODATA 2022, la donnée de recul est reprise comme D4 :

```text
D4 : h/m(133Cs) ;
incertitude standard relative d’entrée : 4.0 × 10^-10 ;
D6 : Ar(133Cs), entrée auxiliaire corrélée au réseau des masses atomiques.
```

La valeur publiée de `alpha^-1` n’est donc pas la donnée brute de l’ajustement. CODATA ajuste D4 et D6 par l’équation d’observation commune aux voies de recul.

## 3. Relation de passage

Pour un atome `X`, la relation utilisée est :

```text
h/m(X) ≐ [Ar(e)/Ar(X)] [c alpha²/(2 R_inf)].
```

Pour le césium :

```text
mesuré expérimentalement : h/m(133Cs) ;
entrée auxiliaire : Ar(133Cs) ;
constantes reliées : Ar(e), R_inf ;
constantes exactes dans le SI révisé : h, c ;
quantité inférée : alpha.
```

Conséquence de rang :

> La voie césium est une détermination de `alpha` par recul et propagation métrologique, non une mesure directe et isolée de `alpha`.

## 4. Architecture expérimentale

L’expérience utilise des atomes de `133Cs` refroidis et lancés dans une fontaine atomique. Les atomes restent dans le même état interne `F=3, mF=0`, ce qui supprime l’effet Zeeman linéaire.

Le dispositif associe :

```text
interféromètres simultanés conjugués de Ramsey–Bordé ;
diffraction de Bragg à dix photons comme séparateur de faisceau ;
oscillations de Bloch pour accroître la séparation en impulsion ;
quatre impulsions principales de recombinaison ;
mesure de la fréquence de modulation annulant la phase totale.
```

À l’ordre dominant, la phase combinée est proportionnelle à la fréquence de recul

```text
omega_r = hbar k²/(2m).
```

L’expérience ajuste la fréquence de modulation `omega_m` jusqu’à annulation de la phase, ce qui permet d’extraire `omega_r`, puis `h/m(133Cs)`.

Paramètres déclarés :

```text
ordre de Bragg : n = 5 ;
nombre d’oscillations de Bloch : N = 125–200 ;
séparations temporelles : T = 5–80 ms ;
phase totale : 10^6–10^7 rad ;
fréquence de modulation : environ 2–3 MHz.
```

## 5. Organisation de l’analyse

La collecte s’étend sur environ sept mois. Le résultat final combine 28 déterminations de `h/m(133Cs)` par moyenne pondérée selon leur variance.

Pour chaque jeu de données :

- plusieurs valeurs du temps de séparation `T` sont utilisées ;
- la phase de diffraction peut varier entre les intervalles d’analyse ;
- une seule valeur de `h/m(133Cs)` est supposée pour le jeu considéré ;
- l’incertitude statistique finale est obtenue par la variance de la moyenne.

L’analyse est aveugle : un décalage aléatoire de fréquence, inconnu des expérimentateurs, masque le résultat dans une fenêtre d’environ `±3 ppb`. Deux codes d’analyse indépendants utilisent des méthodes d’ajustement différentes et sont comparés sur les mêmes données.

Le matériel supplémentaire indique qu’après dévoilement du résultat, aucune modification générale n’a été apportée, à l’exception :

- de la correction d’une erreur typographique dans un calcul de phase, produisant un déplacement de `0.2 ppb` ;
- de l’ajout d’une analyse des petites variations spatiales d’intensité du faisceau.

Cette procédure réduit certains risques de biais humain ; elle ne démontre pas l’exhaustivité du modèle systématique.

## 6. Budget des corrections et incertitudes

Le budget publié pour `delta alpha/alpha`, en parties par milliard, est :

| Effet | Correction (ppb) | Incertitude (ppb) | Fonction dans l’audit |
|---|---:|---:|---|
| fréquence laser | `-0.24` | `0.03` | étalonnage optique et stabilité de la référence |
| gradient d’accélération | `-1.79` | `0.02` | gravité locale et gradients magnétiques effectifs |
| phase de Gouy | `-2.60` | `0.03` | géométrie et structure spatiale du faisceau |
| alignement du faisceau | `+0.05` | `0.03` | angle de rétroréflexion |
| déplacement lumineux des oscillations de Bloch | `0` | `0.002` | décalage ac-Stark |
| déplacement de densité | `0` | `0.003` | interactions atomiques |
| indice de réfraction | `0` | `0.03` | propagation dans le nuage atomique |
| phase de speckle | `0` | `0.04` | variations spatiales aléatoires du faisceau |
| effet Sagnac | `0` | `0.001` | rotation |
| nombre d’onde de modulation | `0` | `0.001` | correction cinématique de fréquence |
| mouvement thermique des atomes | `0` | `0.08` | déformation des ellipses et phase de diffraction dépendant de `T` |
| forme d’onde non gaussienne | `0` | `0.03` | profil temporel des impulsions de Bragg |
| interféromètres parasites | `0` | `0.03` | caractère multiport de la diffraction de Bragg |
| **total systématique** | **`-4.58`** | **`0.12`** | correction nette et incertitude systématique déclarée |

Aux incertitudes expérimentales s’ajoutent :

```text
statistique : 0.16 ppb ;
masse de l’électron : 0.02 ppb ;
masse du césium : 0.03 ppb ;
constante de Rydberg : 0.003 ppb ;
total sur alpha : environ 0.20 ppb.
```

## 7. Concentration du risque systématique

Les corrections dominantes ne sont pas distribuées uniformément.

```text
phase de Gouy : -2.60 ppb ;
gradient d’accélération : -1.79 ppb ;
fréquence laser : -0.24 ppb ;
ensemble des corrections : -4.58 ppb.
```

La correction totale est donc très supérieure à l’incertitude finale annoncée. Ce fait ne constitue pas en lui-même une faiblesse : une correction peut être grande et précisément connue. Il impose cependant que l’attribution d’une incertitude de `0.12 ppb` repose sur la qualité des modèles, mesures auxiliaires et validations des corrections.

### 7.1 Phase de Gouy et profil du faisceau

La phase de Gouy dépend du rayon de courbure, de la position du col du faisceau et de la distribution transversale des atomes. Pour le faisceau apodisé utilisé dans le résultat final, le profil n’est pas assimilé à un simple faisceau gaussien.

La correction est évaluée par une simulation Monte-Carlo tridimensionnelle incorporant :

- les images du profil du faisceau ;
- l’efficacité des oscillations de Bloch selon l’intensité locale ;
- la distribution spatiale des atomes ;
- les contributions des différentes impulsions.

La valeur publiée est :

```text
correction de Gouy effective : -2.60 ± 0.03 ppb.
```

Les auteurs testent la sensibilité aux petites variations d’intensité, à différents lissages des images et à deux tailles de faisceau. Les résultats sont déclarés compatibles avec le modèle à la précision disponible.

### 7.2 Gradients d’accélération

Le montage simultané annule l’accélération uniforme, mais non tous les gradients. Le gradient de gravité est mesuré in situ par une configuration de gradiomètre atomique.

Les contributions examinées comprennent :

- gradient gravitationnel local ;
- gradient du gradient provenant de masses proches ;
- gradients magnétiques quadratiques pour l’état `mF=0`.

La correction publiée est :

```text
gradient d’accélération : -1.79 ± 0.02 ppb.
```

Une comparaison avec deux valeurs du champ magnétique de polarisation est utilisée comme contrôle supplémentaire.

### 7.3 Mouvement thermique et simulation

Le mouvement thermique modifie l’intensité des impulsions effectivement vue par les atomes et peut rendre la phase de diffraction dépendante de `T`.

Une simulation Monte-Carlo fait varier :

- rayon du nuage ;
- largeur de vitesse verticale ;
- vitesse horizontale moyenne ;
- position horizontale initiale ;
- intensité des impulsions ;
- rapport d’intensité de la dernière impulsion.

L’incertitude combinée attribuée à ce sous-dossier est `0.08 ppb`, la plus grande contribution individuelle à l’incertitude systématique.

### 7.4 Speckle et alignement

Des phases anormales atteignant initialement plusieurs dizaines de milliradians sont rapportées avant l’emploi conjoint :

- d’un contrôle en temps réel de l’alignement de la fontaine ;
- d’un filtre apodisant ;
- d’un grand nombre d’oscillations de Bloch.

Les résidus sont ensuite déclarés non résolus dans la précision finale, avec une incertitude de `0.04 ppb` attribuée au speckle.

## 8. Ce que l’expérience soutient positivement

Dans son propre domaine, l’expérience soutient :

```text
une mesure précise de la fréquence de recul du césium ;
une extraction de h/m(133Cs) ;
une valeur de alpha inférée par une relation déclarée ;
un budget d’incertitude explicitement décomposé ;
des contrôles internes et une analyse aveugle ;
une comparaison indépendante de la voie g−2 au sens de l’observable première.
```

Elle ne soutient pas seule :

```text
l’absence de systématique non modélisée ;
la cause de la discordance avec le rubidium et g−2 ;
la supériorité de la voie césium ;
une variation physique de alpha ;
une incompatibilité générale de la physique décrite par les autres chaînes.
```

## 9. Repondération par CODATA 2022

Dans l’ajustement initial CODATA 2022, D4 porte un résidu normalisé de `4.7`, le plus élevé du sous-ensemble directement pertinent pour `alpha`.

CODATA :

- conserve D4 et D6 ;
- applique le même facteur d’expansion `2.5` aux six données D1–D6 ;
- n’identifie pas de cause démontrée propre au césium ;
- ne convertit pas la discordance en variation physique ;
- élargit l’incertitude de la valeur recommandée.

Le mode de soutien probatoire devient donc double :

```text
niveau expérimental local : mesure corrigée et contrôles internes ;
niveau inter-chaînes : donnée conservée mais repondérée dans un ajustement incohérent avant expansion.
```

La discordance n’annule pas l’expérience. Elle empêche de traiter son incertitude publiée comme suffisante, à elle seule, pour fixer la pondération inter-chaînes sans décision d’ajustement.

## 10. Statut actuel de la discordance

Le premier lot documentaire ne contient pas :

- d’erratum retirant ou remplaçant la valeur Parker et al. ;
- de diagnostic causal publié établissant quelle correction explique l’écart ;
- de nouvelle détermination césium de précision comparable déjà intégrée à CODATA 2022.

Un résumé de conférence de 2025 décrit la construction d’une nouvelle fontaine atomique de cinq mètres et des tests contrôlés des systématiques liées au faisceau afin de résoudre la discordance. Ce signal de programme n’est pas un résultat évalué par les pairs et ne modifie pas le verdict local sur la mesure de 2018.

Le statut prudent reste :

```text
valeur publiée : conservée ;
chaîne expérimentale : documentée et localement cohérente selon son budget ;
accord avec les autres chaînes actuelles : insuffisant ;
cause du désaccord : suspendue ;
réplication indépendante de même architecture : absente du premier lot ;
nouvelle mesure de résolution : en attente.
```

## 11. Verdict local préparatoire

```text
admission :
  la voie césium fournit une détermination expérimentale de h/m(133Cs)
  et une inférence déclarée de alpha avec un budget systématique détaillé ;

refus :
  traiter alpha comme observable directement mesurée ;
  interpréter l’écart inter-chaînes comme variation physique ;
  déduire du seul budget interne que la discordance est résolue ;

suspension :
  cause de l’écart avec le rubidium et la voie g−2 ;
  suffisance complète des modèles de faisceau et de phase ;
  pondération relative finale entre les trois chaînes ;
  statut comparatif final de la valeur recommandée.
```

Mode de soutien probatoire :

```text
mesure locale de recul
+ propagation métrologique
+ modélisation et correction systématiques
+ repondération inter-chaînes par CODATA.
```

## 12. Dettes avant la comparaison α2

1. auditer la voie rubidium selon la même grille ;
2. auditer séparément l’inférence `g−2` et ses dépendances QED ;
3. comparer les architectures de correction des deux expériences de recul ;
4. distinguer corrélations d’entrée et dépendances communes de modèle ;
5. vérifier les données ou produits publics réellement disponibles pour chaque chaîne ;
6. ne produire le verdict comparatif α2 qu’après les trois audits locaux.

## 13. Condition d’arrêt de la fiche

La fiche césium est suffisamment instruite lorsque l’on peut répondre séparément :

```text
ce qui est mesuré : phase de recul et h/m(133Cs) ;
ce qui est corrigé : effets de faisceau, gradients, fréquence et dynamique atomique ;
ce qui est simulé : plusieurs contributions de phase et de mouvement thermique ;
ce qui est inféré : alpha par relation métrologique ;
ce qui est repondéré : D4 et D6 dans CODATA ;
ce qui demeure inconnu : cause de la discordance inter-chaînes.
```

Cette condition est remplie pour le premier lot. La fiche reste préparatoire jusqu’à comparaison avec les voies rubidium et `g−2`.