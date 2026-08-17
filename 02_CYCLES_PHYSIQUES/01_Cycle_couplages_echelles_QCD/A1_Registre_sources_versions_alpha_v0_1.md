# α1 — Registre borné des sources et versions pour la constante de structure fine v0.1

## 0. Statut

```text
statut : document exploratoire de verrouillage des sources ;
date : 26 juillet 2026 ;
opération : α1, issue #34 ;
fonction : fixer un premier lot primaire avant les fiches α2–α5 ;
autorité : aucune autorité de verdict ;
ne vaut pas : revue exhaustive, combinaison numérique, validation générale de la littérature
               ou conclusion sur la constance de alpha.
```

Ce registre sépare quatre cibles qui ne doivent pas être identifiées :

```text
A. valeur de référence de basse énergie et chaînes de détermination ;
B. couplage courant alpha(Q²) et dépendance à l’échelle ;
C. variation temporelle ou couplage au potentiel gravitationnel ;
D. variation spatiale ou cosmologique.
```

Les versions de revue par les pairs sont prioritaires. Un identifiant arXiv ou un dépôt de données est conservé lorsqu’il ajoute une version inspectable, un historique ou des produits publics. Le verrouillage indique la version utilisée ; il ne ratifie pas encore les modèles, les sensibilités ni les traitements de systématiques.

## 1. Cible A — valeur de référence et chaînes de détermination

### A0 — Ajustement CODATA 2022

| Champ | Verrouillage |
|---|---|
| Référence | P. J. Mohr, D. B. Newell, B. N. Taylor et E. Tiesinga, « CODATA recommended values of the fundamental physical constants: 2022 » |
| Version principale | *Reviews of Modern Physics* 97, 025002 (2025), publiée le 30 avril 2025 |
| DOI | `10.1103/RevModPhys.97.025002` |
| Base de données associée | NIST Standard Reference Database 121, version 9.0, valeurs mises à jour le 9 mai 2024 |
| Coupure des données | données théoriques et expérimentales disponibles jusqu’au 31 décembre 2022 |
| Fonction dans α1 | documenter la valeur recommandée comme sortie d’un ajustement cohérent par moindres carrés, non comme mesure unique |
| Transformation pertinente | changement du jeu de données, des relations d’entrée, des corrélations ou de l’ajustement |
| Limite | l’étiquette « 2022 » désigne la coupure des données ; la publication détaillée date de 2025 |

Décision de verrouillage : **source directrice de la cible A**.

Le prochain ajustement régulier annoncé est CODATA 2026 ; aucune valeur recommandée CODATA 2026 n’est disponible au moment du verrouillage. Toute mise à jour future devra être traitée comme une nouvelle version de l’ajustement, non comme une variation temporelle de la grandeur physique.

### A1 — Recul atomique du césium

| Champ | Verrouillage |
|---|---|
| Référence | R. H. Parker, C. Yu, W. Zhong, B. Estey et H. Müller, « Measurement of the fine-structure constant as a test of the Standard Model » |
| Version principale | *Science* 360 (2018), publiée le 12 avril 2018 |
| DOI | `10.1126/science.aap7706` |
| Version ouverte repérée | arXiv:`1812.04130` |
| Observable première | fréquence de recul de `133Cs` dans un interféromètre à ondes de matière |
| Sortie rapportée | détermination de `alpha` à partir de `h/m_Cs` et des relations auxiliaires nécessaires |
| Fonction dans α1 | chaîne indépendante de détermination de basse énergie par recul atomique |
| Limite | le résultat dépend de la chaîne métrologique et théorique reliant le recul à `alpha` ; il ne teste ni `alpha(Q²)` ni une dérive temporelle |

Décision de verrouillage : **source primaire active pour la chaîne césium**.

### A2 — Recul atomique du rubidium

| Champ | Verrouillage |
|---|---|
| Référence | L. Morel, Z. Yao, P. Cladé et S. Guellati-Khélifa, « Determination of the fine-structure constant with an accuracy of 81 parts per trillion » |
| Version principale | *Nature* 588, 61–65 (2020), publiée le 2 décembre 2020 |
| DOI | `10.1038/s41586-020-2964-7` |
| Observable première | vitesse de recul d’un atome de `87Rb` absorbant un photon, mesurée par interférométrie atomique |
| Sortie rapportée | `alpha^{-1} = 137.035999206(11)` |
| Fonction dans α1 | chaîne indépendante de détermination de basse énergie par recul atomique |
| Point comparatif | le résultat publié diffère de plus de cinq écarts-types de la détermination césium alors disponible |
| Limite | le désaccord entre chaînes n’est pas une variation physique de `alpha` ; il demande un audit des chaînes, corrections et corrélations |

Décision de verrouillage : **source primaire active pour la chaîne rubidium**.

### A3 — Moment magnétique de l’électron et inversion QED

| Champ | Verrouillage |
|---|---|
| Référence | X. Fan, T. G. Myers, B. A. D. Sukra et G. Gabrielse, « Measurement of the Electron Magnetic Moment » |
| Version principale | *Physical Review Letters* 130, 071801 (2023), publiée le 17 février 2023 |
| DOI | `10.1103/PhysRevLett.130.071801` |
| Version ouverte repérée | arXiv:`2209.13084` |
| Observable première | moment magnétique d’un électron unique dans un piège de Penning |
| Relation à `alpha` | la mesure, combinée au calcul QED du moment anormal, peut être inversée pour produire une détermination conditionnelle de `alpha` |
| Sortie conditionnelle rapportée | `alpha^{-1} = 137.035999166(15)` sous la théorie QED employée |
| Fonction dans α1 | distinguer une mesure directe d’observable d’une inférence de `alpha` dépendante d’une théorie de liaison |
| Limite | cette route ne doit pas être comptée comme indépendante du calcul QED lorsqu’elle sert ensuite à tester ce même calcul |

Décision de verrouillage : **source primaire active comme chaîne inférentielle distincte, non comme mesure directe de `alpha`**.

### Dette de la cible A

Avant α2, il faudra extraire du CODATA 2022 :

```text
les données d’entrée effectivement retenues pour alpha ;
les facteurs d’ajustement ;
les corrélations utiles ;
le traitement du désaccord césium–rubidium ;
la place exacte du moment magnétique de l’électron dans l’ajustement.
```

## 2. Cible B — couplage courant `alpha(Q²)`

### B1 — L3, diffusion Bhabha à grand transfert d’impulsion

| Champ | Verrouillage |
|---|---|
| Référence | L3 Collaboration, « Measurement of the running of the electromagnetic coupling at large momentum-transfer at LEP » |
| Version principale | *Physics Letters B* 623, 26–36 (2005), publiée le 8 septembre 2005 |
| DOI | `10.1016/j.physletb.2005.07.052` |
| Version ouverte repérée | arXiv:`hep-ex/0507078` |
| Données | environ 40 000 événements de diffusion Bhabha à `sqrt(s)=189–209 GeV` |
| Domaine déclaré | `1800 GeV² < -Q² < 21600 GeV²` |
| Paramétrisation testée | `alpha(Q²)=alpha(0)/(1-C Delta alpha(Q²))`, avec `C=1` pour l’évolution QED attendue et `C=0` pour l’absence de running |
| Résultat publié | `C = 1.05 ± 0.07_stat ± 0.14_syst` ; hypothèse `C=0` exclue dans le test publié |
| Fonction dans α1 | cas positif où la transformation d’échelle doit produire une variation du couplage renormalisé |
| Limite | le résultat porte sur un domaine de transfert d’impulsion et une observable de collision ; il ne teste pas une variation temporelle de `alpha(0)` |

Décision de verrouillage : **source primaire active pour la cible B**.

### Dette de la cible B

Avant α3, il faudra distinguer :

```text
alpha(0) ;
alpha(Q²) dans le domaine espace-like du test ;
la fonction Delta alpha(Q²) utilisée ;
les contributions leptoniques et hadroniques ;
les dépendances au générateur, au modèle radiatif et à l’acceptance ;
la portée exacte de l’exclusion de C=0.
```

## 3. Cible C — variation temporelle et couplage au potentiel

### C1 — Comparaisons d’horloges `171Yb+`

| Champ | Verrouillage |
|---|---|
| Référence | R. Lange et al., « Improved Limits for Violations of Local Position Invariance from Atomic Clock Comparisons » |
| Version principale | *Physical Review Letters* 126, 011102 (2021), publiée le 6 janvier 2021 |
| DOI | `10.1103/PhysRevLett.126.011102` |
| Version ouverte repérée | arXiv:`2010.06620` |
| Observables premières | rapport des transitions E3/E2 de `171Yb+` et fréquence E3 rapportée à deux fontaines au césium, suivis sur plusieurs années |
| Modèles de variation testés | dérive linéaire temporelle et couplage à la variation annuelle du potentiel gravitationnel solaire |
| Contraintes publiées | `(1/alpha)(d alpha/dt)=1.0(1.1)×10^-18 yr^-1` ; `(c²/alpha)(d alpha/dPhi)=14(11)×10^-9` |
| Fonction dans α1 | cas de non-détection potentiellement discriminante pour deux familles déclarées de variations |
| Limite | la contrainte dépend des coefficients de sensibilité atomique et de l’analyse conjointe des paramètres ; elle n’établit pas une invariance temporelle universelle |

Décision de verrouillage : **source primaire directrice pour le premier lot temporel**.

### C2 — Antécédent de comparaison directe de deux transitions `171Yb+`

| Champ | Verrouillage |
|---|---|
| Référence | R. M. Godun et al., « Frequency Ratio of Two Optical Clock Transitions in `171Yb+` and Constraints on the Time Variation of Fundamental Constants » |
| Version principale | *Physical Review Letters* 113, 210801 (2014), publiée le 17 novembre 2014 |
| DOI | `10.1103/PhysRevLett.113.210801` |
| Fonction dans α1 | documenter l’architecture de sensibilité différentielle entre deux transitions du même ion |
| Limite | la contrainte finale combine aussi d’autres expériences ; la mesure de rapport ne se convertit pas seule en dérive de `alpha` |

Décision de verrouillage : **source d’appui méthodologique, non source directrice du résultat temporel courant**.

### Dette de la cible C

Avant α4, il faudra reconstruire :

```text
les coefficients de sensibilité de chaque transition ;
les paramètres simultanément ajustés ;
les séries temporelles et leurs covariances ;
la famille exacte de dérive ou modulation testée ;
les fréquences auxquelles une recherche oscillatoire serait sensible ;
la distinction entre dérive temporelle et couplage au potentiel.
```

Les recherches oscillatoires liées à la matière noire ultralégère sont différées : elles constituent une famille de variations différente de la dérive linéaire retenue dans le premier lot.

## 4. Cible D — variation spatiale ou cosmologique

### D1 — Prétention dipolaire historique

| Champ | Verrouillage |
|---|---|
| Référence | J. K. Webb et al., « Indications of a Spatial Variation of the Fine Structure Constant » |
| Version principale | *Physical Review Letters* 107, 191101 (2011), publiée le 31 octobre 2011 |
| DOI | `10.1103/PhysRevLett.107.191101` |
| Données | échantillons d’absorbeurs de quasars obtenus avec Keck/HIRES et VLT/UVES |
| Modèle testé | motif dipolaire spatial dans `Delta alpha/alpha` |
| Résultat publié | ajustement dipolaire annoncé à `4.2 sigma`, sous les systématiques alors identifiées |
| Fonction dans α1 | prétention positive historique à réévaluer avec les connaissances ultérieures sur les calibrations |
| Limite | le papier reconnaît la possibilité de systématiques non détectées ; le niveau de signification n’est pas un verdict indépendant de la chaîne instrumentale |

Décision de verrouillage : **source primaire de la prétention positive historique**.

### D2 — Supercalibration et distorsions à longue portée

| Champ | Verrouillage |
|---|---|
| Référence | J. B. Whitmore et M. T. Murphy, « Impact of instrumental systematic errors on fine-structure constant measurements with quasar spectra » |
| Version principale | *Monthly Notices of the Royal Astronomical Society* 447, 446–462 (2015), publiée en ligne le 17 décembre 2014 |
| DOI | `10.1093/mnras/stu2420` |
| Version ouverte repérée | arXiv:`1409.4467` |
| Méthode | supercalibration de spectrographes par comparaison d’astéroïdes ou d’étoiles jumelles solaires avec un spectre solaire de référence |
| Résultat instrumental | distorsions de longueur d’onde à longue portée, typiquement de l’ordre de `±200 m s^-1` par `1000 Å`, observées dans les archives UVES et HIRES |
| Effet sur le dossier | les distorsions modélisées reproduisent des aspects importants des résultats UVES et affaiblissent substantiellement la preuve de variation ; elles n’expliquent pas de façon auto-cohérente tous les résultats HIRES |
| Fonction dans α1 | repondération probatoire après identification d’une systématique instrumentale majeure |
| Limite | l’étude ne fournit pas à elle seule un verdict global sur toutes les mesures de quasars |

Décision de verrouillage : **source primaire active sur les systématiques de calibration**.

### D3 — ESPRESSO, absorbeur vers HE 0515−4414

| Champ | Verrouillage |
|---|---|
| Référence | M. T. Murphy et al., « Fundamental physics with ESPRESSO: Precise limit on variations in the fine-structure constant towards the bright quasar HE 0515−4414 » |
| Version principale | *Astronomy & Astrophysics* 658, A123 (2022) |
| DOI | `10.1051/0004-6361/202142257` |
| Version ouverte repérée | arXiv:`2112.05819` |
| Données | 16,1 heures d’observation ESPRESSO d’un absorbeur à `z=1.15`, spectre calibré par peigne de fréquences laser |
| Résultat publié | `Delta alpha/alpha = 1.3 ± 1.3_stat ± 0.4_syst ppm` sur cette ligne de visée |
| Produits | spectre réduit et produits d’analyse annoncés comme publics, dépôt Zenodo associé |
| Fonction dans α1 | contrainte locale récente avec calibration instrumentale renforcée et systématiques explicitement séparées |
| Limite | une ligne de visée ne teste ni le dipôle global complet ni une invariance cosmologique universelle ; les ambiguïtés de modélisation du profil restent importantes |

Décision de verrouillage : **source primaire active pour une non-détection locale calibrée**.

### Dette de la cible D

Avant α5, il faudra distinguer :

```text
variation spatiale, évolution avec le redshift et modèle dipolaire ;
absorbeurs et méthodes spectrales effectivement employés ;
calibration ThAr, supercalibration et peigne de fréquences ;
modélisation des composantes de vitesse ;
convergence de l’optimisation ;
indépendance ou recouvrement des échantillons ;
portée locale de chaque ligne de visée.
```

La mesure LAMOST par doublet d’émission et les contraintes cosmologiques de recombinaison sont conservées comme **extensions possibles**, non intégrées au premier lot α1 : elles portent sur d’autres observables, précisions et dépendances de modèle.

## 5. Tableau de verrouillage consolidé

| ID | Cible | Source directrice | Version verrouillée | Mode de soutien pressenti | Verdict autorisé à α1 |
|---|---|---|---|---|---|
| A0 | valeur recommandée | CODATA 2022 | RMP 97, 025002 (2025) | ajustement cohérent de données | aucun |
| A1 | détermination Cs | Parker et al. | *Science* 360 (2018) | mesure de recul + chaîne théorique | aucun |
| A2 | détermination Rb | Morel et al. | *Nature* 588 (2020) | mesure de recul + chaîne théorique | aucun |
| A3 | détermination conditionnelle | Fan et al. | PRL 130, 071801 (2023) | moment magnétique + QED inversée | aucun |
| B1 | running | L3 Collaboration | PLB 623 (2005) | mesure positive d’une dépendance à `Q²` | aucun |
| C1 | dérive / potentiel | Lange et al. | PRL 126, 011102 (2021) | contrainte sensible sur familles déclarées | aucun |
| C2 | architecture de sensibilité | Godun et al. | PRL 113, 210801 (2014) | rapport de fréquences et analyse combinée | aucun |
| D1 | dipôle historique | Webb et al. | PRL 107, 191101 (2011) | prétention positive sur échantillons d’archives | aucun |
| D2 | systématiques | Whitmore & Murphy | MNRAS 447 (2015) | identification et modélisation de distorsions | aucun |
| D3 | ligne de visée calibrée | Murphy et al. | A&A 658, A123 (2022) | non-détection locale discriminante | aucun |

## 6. État d’α1 après verrouillage

```text
sources primaires principales : identifiées ;
versions de référence : fixées ;
quatre cibles : séparées ;
comparabilité numérique entre les quatre cibles : non pertinente ;
verdict de constance : non ouvert ;
calcul ou reproduction : non engagé ;
prochaine opération possible : matrice initiale cible / transformation / accès /
                              soutien probatoire / limite.
```

Ce registre reste révisable si une erreur bibliographique ou une version primaire plus appropriée est identifiée. Toute substitution doit être explicite et ne vaut pas révision silencieuse du verdict futur.