# Synthèse active du cycle 3 — neutrinos après N5 v0.2

## 0. Statut documentaire

```text
statut : synthèse scientifique active du cycle 3 ;
date : 17 juillet 2026 ;
coupure bibliographique : 17 juillet 2026 inclus ;
remplace pour le travail courant : la synthèse de récupération comme verdict
                                    scientifique du cycle ;
conserve comme source historique : Synthese_recuperation_cycle_3_neutrinos_v0_1.md ;
base active : N0, N1, N2, N3, N4 et matrice comparative N5 ;
fonction : stabiliser l'acquis scientifique, les compatibilités, les limites et
           les dettes résiduelles du cycle neutrino ;
ne vaut pas : ajustement statistique conjoint, détermination de l'ordre, de la
              masse minimale, des phases de Majorana ou du mécanisme de masse.
```

Documents directeurs :

- [N0 — protocole commun](N0_Protocole_commun_fiches_acces_neutrinos_v0_1.md) ;
- [N1 — oscillations](N1_Fiche_acces_oscillations_neutrinos_v0_1.md) ;
- [N2 — cinématique bêta](N2_Fiche_acces_cinematique_beta_neutrinos_v0_1.md) ;
- [N3 — cosmologie](N3_Fiche_acces_cosmologie_somme_masses_neutrinos_v0_1.md) ;
- [N4 — double bêta sans neutrino](N4_Fiche_acces_double_beta_sans_neutrino_v0_1.md) ;
- [N5 — matrice comparative](N5_Matrice_comparative_quatre_acces_neutrinos_v0_1.md).

## 1. Question du cycle après reprise

La question n'est plus :

```text
quelle est la constante de masse des neutrinos ?
```

Elle devient :

> Comment plusieurs chaînes expérimentales et reconstructives contraignent-elles
> des fonctions différentes d'un même spectre, et quelles hypothèses rendent leurs
> résultats comparables sans les rendre interchangeables ?

Cette reformulation retire deux simplifications :

1. la masse absolue n'apparaît pas comme un nombre unique directement accessible ;
2. la précision numérique d'une voie ne suffit pas à lui donner une autorité sur
   toutes les propriétés du secteur.

## 2. Acquis scientifique principal

Le secteur est organisé par quatre fonctions non équivalentes :

```text
N1 : Delta m^2_ij, theta_ij, delta_CP ;
N2 : m_beta^2 = somme_i |U_ei|^2 m_i^2 ;
N3 : Sigma m_nu = somme_i m_i ;
N4 : T_1/2^0nu, puis m_beta_beta = |somme_i U_ei^2 m_i|
     sous mécanisme de Majorana léger.
```

Leur objet commun minimal est un spectre latent :

```text
{m_1, m_2, m_3}
+ matrice PMNS
+ ordre
+ masse minimale
+ hypothèses propres aux voies.
```

Le résultat du cycle est donc :

> Les accès neutrino contraignent un même secteur sans contraindre la même
> grandeur. Leur cohérence doit être démontrée par des ponts physiques et
> inférentiels qui déclarent l'information ajoutée et l'information perdue.

## 3. Portrait stabilisé des quatre voies

| Voie | Fonction contrainte | Résultat directeur à la coupure | Forme d'incomplétude |
|---|---|---|---|
| oscillations | écarts, mélange et phase de Dirac | architecture différentielle robuste ; ordre, octant et CP non définitivement fixés | translation commune des masses au carré, masse minimale et phases Majorana absentes |
| cinématique bêta | `m_beta` | `m_beta < 0.45 eV` à `90 % CL`, aucune détection | trois masses non résolues, ordre et phases absents |
| cosmologie | `Sigma m_nu` | `Sigma m_nu < 0.0642 eV` à `95 %` sous `LambdaCDM`, posterior à la frontière | dépendance au modèle, aux données, aux priors et à l'histoire thermique |
| double bêta sans neutrino | demi-vie isotopique, puis `m_beta_beta` conditionnel | aucune détection ; limite `3.8 x 10^26 yr` pour `136Xe` | nature Majorana non tranchée, phases, mécanisme et NME non identifiés |

Cette table ne constitue pas une échelle de qualité. Elle indique ce que chaque
voie sait faire et ce qu'elle ne peut pas fournir seule.

## 4. Ce qui est établi

### 4.1 Architecture différentielle

Les oscillations établissent au moins deux écarts de masses au carré non nuls et
une matrice de mélange non triviale. Elles donnent les relations internes les plus
robustes du spectre, mais pas son origine commune.

### 4.2 Ancrage cinématique local

KATRIN fournit une prise de laboratoire sur la moyenne quadratique électronique.
Cette voie évite la cosmologie et la nature Dirac/Majorana, mais dépend du spectre
moléculaire, de la réponse instrumentale, des pertes d'énergie et de la procédure
statistique.

### 4.3 Sensibilité cosmologique collective

La cosmologie atteint la région la plus basse de masse, au prix de l'architecture
de modèle la plus étendue. La borne standard est proche du plancher normal fourni
par les oscillations et devient une tension de réseau lorsque la construction
fréquentiste passe sous ce plancher.

### 4.4 Test conditionnel de Majorana

La double bêta sans neutrino est la seule voie du cycle susceptible d'établir une
violation du nombre leptonique et de tester la nature Majorana par une détection.
La non-détection actuelle ne prouve pas une nature Dirac. La conversion de demi-vie
en masse reste dominée par le mécanisme et la physique nucléaire.

## 5. Compatibilité des voies

### 5.1 Verdict global

```text
compatibilité générale à la coupure : oui ;
contradiction modèle-indépendante : aucune ;
tension principale : N1–N3 sous LambdaCDM ;
validation croisée locale de la région basse : non encore atteinte par N2 ;
exclusion robuste de Majorana ou de tout l'ordre inversé par N4 : non.
```

### 5.2 Tension oscillations–cosmologie

Sous `LambdaCDM`, DESI DR2 BAO + CMB donne une borne bayésienne de `0.0642 eV` et
une construction fréquentiste de `0.053 eV`. La seconde est inférieure au plancher
normal approximatif issu des oscillations.

Cette tension doit être localisée d'abord dans :

```text
likelihoods et choix de données ;
traitement de la frontière ;
priors et paramétrisation ;
modèle d'énergie noire ;
histoire thermique et interactions du secteur neutrino.
```

Elle ne justifie pas une moyenne entre N1 et N3. Sous `w_0w_aCDM`, la borne s'élargit
à `0.163 eV` et le conflit disparaît.

### 5.3 Cinématique et cosmologie

La borne KATRIN est compatible avec la région cosmologique mais ne la teste pas
encore. Les deux voies diffèrent par leur portée :

```text
N2 : locale, sensibilité plus faible, dépendance instrumentale et moléculaire ;
N3 : globale, sensibilité beaucoup plus forte, dépendance cosmologique majeure.
```

### 5.4 Double bêta et autres voies

Les non-détections actuelles sont compatibles avec les régions de masse permises par
les autres accès. La circulation de l'information vers `m_beta_beta` exige toujours :

```text
ordre
+ masse minimale
+ phases Majorana
+ nature Majorana
+ mécanisme
+ éléments de matrice nucléaire.
```

## 6. Correction du vocabulaire du cycle

### 6.1 Expression à abandonner comme formule directrice

```text
les trois mesures de la masse absolue des neutrinos.
```

### 6.2 Expression active

```text
les trois ancrages non équivalents du spectre après l'architecture différentielle :
quadratique électronique, somme cosmologique et amplitude cohérente conditionnelle.
```

### 6.3 Sens du terme projection

Le mot « projection » reste recevable s'il désigne une fonction mathématique précise
du spectre. Il ne doit pas devenir une métaphore générale pour toute médiation ou
toute reconstruction.

## 7. Effet sur les deux questions directrices du projet

### 7.1 Ce qui varie et ce qui tient

Ce qui tient le plus fortement dans le cycle n'est pas une valeur absolue, mais :

```text
les écarts spectraux ;
les motifs d'oscillation ;
les relations entre fonctions de masse ;
la cohérence d'un secteur à travers plusieurs régimes.
```

Les bornes varient avec l'exposition, les modèles, les priors, les calibrations et
les calculs. Leur évolution ne signifie pas une variation physique des masses.

### 7.2 Transformation de l'enquête

Le cycle impose de remplacer la comparaison de nombres par la reconstruction de :

```text
trace
-> observable publiée
-> modèle de passage
-> fonction contrainte
-> hypothèses de conversion
-> compatibilité avec les autres voies.
```

La question scientifique devient moins « quelle valeur est la bonne ? » que :

> Quel énoncé est produit par cette chaîne, et que faut-il ajouter pour le comparer
> à un autre énoncé du même secteur ?

## 8. Gain non redondant du cycle

Le cycle ne redécrit pas seulement la notion générale de dépendance au modèle. Il
fournit un cas où :

1. un même spectre porte plusieurs fonctions mathématiquement distinctes ;
2. les observables primaires appartiennent à des disciplines et échelles différentes ;
3. les conversions peuvent être écrites explicitement ;
4. les informations structurellement absentes sont localisables ;
5. une tension peut viser le pont plutôt que l'objet ;
6. la non-détection et la borne ont une fonction scientifique positive sans devenir
   des valeurs mesurées.

## 9. Transférabilité

### 9.1 Cycle 1

Le gabarit doit être testé sur les couplages en séparant :

```text
observable
+ calcul
+ échelle
+ schéma
+ corrections
+ paramètre extrait.
```

### 9.2 Cycle 7

Le gabarit doit être étendu sonde par sonde :

```text
signal
+ calibration
+ observable reconstruite
+ modèle direct
+ likelihood
+ paramètre cosmologique.
```

La transférabilité est confirmée comme méthode locale, non comme théorie universelle
de la mesure.

## 10. Dettes résiduelles

### 10.1 Computation

- profils exacts de NuFIT 6.1 ;
- raccord des conventions de différences de masses ;
- reproduction de la likelihood KATRIN ;
- reproduction des chaînes DESI et comparaison de priors ;
- calcul de bandes communes dans l'espace `m_l`, `m_beta`, `Sigma m_nu`, `m_beta_beta` ;
- combinaison multi-isotopes avec NME corrélées.

### 10.2 Veille empirique

- nouvelle analyse standard KATRIN ;
- forme complète et futurs résultats DESI ;
- nouveaux résultats JUNO, DUNE, Hyper-Kamiokande et expériences atmosphériques ;
- nouvelles limites ou détection de double bêta sans neutrino ;
- calculs nucléaires coordonnés et validation des opérateurs à courte portée.

### 10.3 Questions physiques ouvertes

```text
ordre des masses ;
violation de CP leptonique ;
masse minimale ;
nature Dirac ou Majorana ;
mécanisme de génération des masses ;
origine de la tension cosmologique ;
complétude du modèle à trois neutrinos actifs.
```

## 11. Statut de la dette prioritaire

La dette définie avant `N0` demandait de documenter séparément les oscillations, la
cinématique bêta, la cosmologie et la double bêta sans neutrino, puis de reconstruire
leurs ponts.

```text
documentation primaire : accomplie au niveau requis pour le cycle ;
état empirique daté : accompli ;
fonctions contraintes : séparées ;
modèles de passage : reconstruits ;
compatibilités : qualifiées ;
tension principale : localisée ;
dettes computationnelles : non levées, explicitement conservées.
```

La dette scientifique prioritaire du cycle 3 est donc **levée au niveau documentaire,
empirique et comparatif**, mais non au niveau d'un ajustement conjoint reproductible.

## 12. Verdict actif du cycle 3

```text
objet : secteur de trois masses et mélange sous cadre déclaré ;
acquis le plus robuste : architecture différentielle du spectre ;
ancrages : m_beta, Sigma m_nu et m_beta_beta, non équivalents ;
compatibilité générale : maintenue ;
tension : cosmologie de base contre plancher oscillatoire ;
non-acquis : détection positive locale, ordre définitif, phases Majorana,
             nature Dirac/Majorana et mécanisme de masse ;
gain pour l'enquête : démontrer les ponts avant de traiter plusieurs accès comme
                       des mesures du même objet ;
statut du cycle : consolidé scientifiquement, ouvert computationnellement.
```

Le prochain arbitrage doit comparer deux suites légitimes :

1. ouvrir le cycle 1 comme dette scientifique suivante ;
2. approfondir la tension `N1–N3` par une reprise computationnelle ciblée.

Cette décision relève de la hiérarchie générale des dettes, non du cycle neutrino
seul.
