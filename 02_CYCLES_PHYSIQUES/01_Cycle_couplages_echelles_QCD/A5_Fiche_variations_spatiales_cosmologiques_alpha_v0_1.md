# α5 — Audit borné des variations spatiales et cosmologiques de `alpha` v0.1

## 0. Statut

```text
statut : fiche scientifique locale sous délégation procédurale ;
date : 26 juillet 2026 ;
opération : α5, issue #40 ;
sources directrices :
  Webb et al., Phys. Rev. Lett. 107, 191101 (2011) ;
  Whitmore & Murphy, MNRAS 447, 446–462 (2015) ;
  Murphy et al., A&A 658, A123 (2022) ;
fonction : reconstruire la trajectoire probatoire allant
           d’une prétention dipolaire historique
           à sa repondération instrumentale,
           puis à une contrainte locale mieux calibrée ;
autorité : descriptive et locale ;
ne vaut pas : méta-analyse cosmologique exhaustive,
               validation ou réfutation universelle d’un dipôle,
               équivalence des échantillons,
               ou propagation automatique dans la synthèse du cycle 1.
```

## 1. Résultat directeur

Le premier lot ne permet ni d’admettre un dipôle cosmologique établi, ni de conclure à une invariance spatiale universelle.

Il permet d’établir une trajectoire probatoire :

```text
1. prétention positive :
   un motif dipolaire est ajusté aux échantillons Keck/HIRES et VLT/UVES ;

2. repondération instrumentale :
   des distorsions de longueur d’onde à longue portée sont identifiées
   dans les spectrographes et peuvent produire des biais de Delta alpha/alpha ;

3. contrainte locale renforcée :
   ESPRESSO, calibré par peigne de fréquences laser,
   obtient une valeur compatible avec zéro sur une ligne de visée précise ;

4. statut global :
   suspendu, car les domaines, échantillons et modèles ne sont pas identiques.
```

## 2. Non-identités obligatoires

```text
variation avec le redshift
≠
variation spatiale dipolaire ;

une ligne de visée
≠
un échantillon tout-ciel ;

signification statistique
≠
indépendance vis-à-vis des systématiques ;

correction d’une calibration
≠
résolution de toutes les ambiguïtés de profil ;

compatibilité locale avec zéro
≠
invariance cosmologique universelle ;

affaiblissement d’une preuve
≠
réfutation logique de toute variation possible.
```

## 3. Chaîne spectroscopique commune

Les méthodes de quasars ne mesurent pas directement `alpha`.

```text
spectre de quasar
+ système absorbant à redshift z
+ transitions atomiques de sensibilités différentes
+ calibration en longueur d’onde
+ modèle de composantes de vitesse
+ données atomiques de laboratoire
-> Delta alpha/alpha inféré.
```

La méthode Many-Multiplet utilise des transitions dont les coefficients de sensibilité à `alpha` diffèrent en amplitude et en signe. Une variation relative modifie les espacements attendus entre les raies.

La puissance discriminante dépend donc simultanément :

- de la diversité des sensibilités atomiques ;
- de la calibration spectrale ;
- de la structure cinématique de l’absorbeur ;
- de la résolution et du rapport signal/bruit ;
- de la sélection des composantes et transitions ;
- de la convergence de l’ajustement.

## 4. Prétention dipolaire historique

Webb et al. combinent des mesures issues principalement de :

```text
Keck/HIRES : directions majoritairement septentrionales ;
VLT/UVES : directions majoritairement australes ;
méthode : Many-Multiplet sur absorbeurs métalliques ;
modèles : monopole, dipôle, dipôle + monopole,
          gradient proportionnel à la distance de regard en arrière.
```

Le modèle dipolaire prend notamment la forme :

```text
Delta alpha/alpha = A cos(Theta) + m
```

ou, sans monopole :

```text
Delta alpha/alpha = A cos(Theta).
```

Le résultat annoncé est un motif spatial d’environ `4.1–4.2 sigma`, avec une direction proche de :

```text
ascension droite : environ 17.4–17.5 h ;
déclinaison : environ -58 degrés ;
amplitude dipolaire sans monopole :
  environ (1.02 ± 0.21) × 10^-5.
```

Le papier effectue des tests de robustesse, des coupes d’échantillon et des comparaisons de quasars observés par les deux télescopes. Il reconnaît néanmoins qu’une systématique non détectée peut produire le motif.

Conséquence de rang :

> La prétention positive est un résultat statistique historiquement réel de la chaîne d’analyse ; elle n’est pas une observation indépendante de la calibration et de la composition des échantillons.

## 5. Confusion possible entre espace, époque et accès

Les absorbeurs se trouvent à des redshifts différents et dans des directions différentes. Un motif apparent peut dépendre :

```text
de la direction sur le ciel ;
du redshift ;
de la sélection des transitions accessibles à chaque redshift ;
du télescope et du spectrographe ;
de la période d’observation ;
de la calibration et de la réduction ;
de la structure propre des absorbeurs.
```

Le modèle dipolaire cherche à séparer certaines de ces dépendances, mais les couvertures de ciel et les instruments sont partiellement confondus. Le « porteur du test » n’est donc pas un espace abstrait seul : c’est une attribution à des absorbeurs observés par des chaînes instrumentales situées.

## 6. Systématique de calibration identifiée

Whitmore et Murphy développent une supercalibration en comparant :

```text
spectres d’astéroïdes ou d’étoiles jumelles solaires
avec
spectre solaire de laboratoire à haute précision.
```

Cette méthode révèle dans les archives UVES et HIRES :

```text
distorsions à l’échelle d’un ordre echelle ;
distorsions à longue portée sur 1000–3000 angströms ;
amplitudes typiques : environ ±200 m s^-1 par 1000 angströms ;
variabilité avec l’époque et la configuration instrumentale.
```

Ces distorsions déplacent différemment des transitions éloignées en longueur d’onde et peuvent donc imiter un `Delta alpha/alpha` non nul.

L’application d’un modèle simple de ces distorsions à des spectres simulés :

```text
reproduit des aspects importants des résultats VLT/UVES ;
affaiblit substantiellement la preuve de variation ;
explique partiellement les résultats HIRES ;
ne les explique pas tous de manière auto-cohérente à tous les redshifts.
```

Le résultat de Whitmore et Murphy ne vaut donc ni correction rétrospective exacte de chaque spectre, ni réfutation complète du dipôle. Il établit qu’une famille instrumentale majeure, auparavant insuffisamment contrôlée, possède la puissance nécessaire pour produire des biais du bon ordre.

## 7. Repondération probatoire

Après identification des distorsions, la hiérarchie change :

```text
avant :
  signification statistique du dipôle
  sous les systématiques alors modélisées ;

après :
  existence démontrée d’une systématique
  capable de reproduire des traits essentiels ;

conséquence :
  la prétention positive perd le rang
  d’indication robuste indépendante de l’instrument ;

mais :
  certaines structures historiques restent non expliquées
  par le modèle simple de distorsion.
```

C’est une repondération, non une suppression rétroactive des résultats publiés.

## 8. Contrainte locale ESPRESSO

Murphy et al. observent le quasar brillant HE 0515−4414 :

```text
temps d’observation : 16.1 h ;
absorbeur : z = 1.15 ;
spectrographe : ESPRESSO au VLT ;
résolution : R ≈ 145 000 ;
calibration : peigne de fréquences laser ;
rapport signal/bruit : environ 105 par pixel de 0.4 km s^-1 ;
analyse : initialement aveugle ;
produits : spectre réduit et ajustements publiquement accessibles.
```

Résultat :

```text
Delta alpha/alpha
  = 1.3 ± 1.3_stat ± 0.4_syst ppm.
```

Cette valeur est compatible avec zéro.

Le peigne de fréquences laser réduit fortement la dette de calibration à longue portée qui affectait les spectres historiques. Les principales incertitudes restantes sont déplacées vers :

- les ambiguïtés de modélisation du profil d’absorption ;
- la redispersion des expositions ;
- la convergence de l’algorithme d’estimation ;
- le choix du modèle cinématique.

## 9. Portée de la non-détection ESPRESSO

Le contrôle P27 est satisfait localement :

```text
cible : Delta alpha/alpha pour un absorbeur précis ;
domaine : une ligne de visée à z=1.15 ;
sensibilité : précision ppm et transitions multiples ;
calibration : peigne de fréquences laser ;
tolérance : erreurs statistique et systématique séparées ;
résultat : compatible avec zéro.
```

La mesure soutient :

```text
aucune variation détectée sur cet absorbeur
au niveau de précision déclaré ;

une réduction substantielle des incertitudes
liées à la calibration de longueur d’onde ;

la possibilité d’une analyse publique plus reproductible.
```

Elle ne soutient pas :

```text
l’absence de dipôle sur tout le ciel ;
une invariance à tous redshifts ;
la réfutation de chaque mesure historique ;
l’absence de toute systématique de profil ;
une conclusion cosmologique universelle.
```

## 10. Résultat combiné publié de rang secondaire

Les auteurs combinent ESPRESSO avec 28 mesures où les erreurs de calibration ont été atténuées :

```text
Delta alpha/alpha
  = -0.5 ± 0.5_stat ± 0.4_syst ppm
  pour 0.6 < z < 2.4.
```

Dans α5, ce résultat est conservé comme indication agrégée publiée. Il n’est pas reproduit ni promu en test complet du modèle dipolaire historique, car :

- la couverture angulaire n’est pas équivalente ;
- les méthodes et instruments restent hétérogènes ;
- une moyenne ne teste pas nécessairement une structure dipolaire ;
- les covariances et sélections ne sont pas reconstruites ici.

## 11. Comparaison des trois moments probatoires

| Dimension | Webb et al. | Whitmore & Murphy | ESPRESSO |
|---|---|---|---|
| fonction | prétention positive | diagnostic instrumental | contrainte locale |
| accès | grands échantillons HIRES/UVES | supercalibrations d’archives et simulations | un absorbeur à haute résolution |
| calibration | ThAr standard, contrôles disponibles à l’époque | mesure de distorsions par référence solaire | peigne de fréquences laser |
| résultat | dipôle statistiquement préféré | biais capables d’affaiblir la preuve | `Delta alpha/alpha` compatible avec zéro |
| force | couverture et pluralité d’absorbeurs | identification d’une systématique majeure | calibration et analyse aveugle renforcées |
| limite | instrument et ciel partiellement confondus | modèle simple non exhaustif | portée locale, profil complexe |

## 12. Résultat scientifique local

```text
prétention historique :
  conservée comme résultat statistique de sa chaîne ;

preuve cosmologique robuste :
  non admise après repondération instrumentale ;

systématique de calibration :
  positivement établie et discriminante ;

explication complète du dipôle :
  non établie ;

non-détection locale ESPRESSO :
  admise comme contrainte discriminante sur une ligne de visée ;

invariance spatiale universelle :
  non établie ;

statut global de la variation spatiale :
  suspendu dans le premier lot.
```

## 13. Réponse locale aux questions publiques

### Q1

La frontière entre variation et maintien se déplace avec la qualité de l’accès. Un motif initialement attribuable à `alpha` devient moins attribuable lorsque l’instrument révèle une transformation concurrente des longueurs d’onde. Une non-détection mieux calibrée soutient alors un maintien local, non universel.

### Q2

L’attribution devient opératoire par :

```text
sensibilités atomiques
+ calibration de longueur d’onde
+ sélection des absorbeurs
+ modèle de vitesse
+ couverture angulaire et redshift
+ traitement des systématiques
+ accès public aux produits.
```

L’enquête ne porte plus seulement sur la valeur de `Delta alpha/alpha`, mais sur la capacité de la chaîne à distinguer variation physique, distorsion instrumentale et ambiguïté de profil.

## 14. Condition d’arrêt

```text
prétention positive : identifiée ;
modèle dipolaire : identifié ;
accès et échantillons : distingués ;
systématique majeure : identifiée ;
portée explicative : bornée ;
non-détection locale : discriminante ;
portée globale : suspendue.
```

Cette condition est remplie pour le premier lot α5.