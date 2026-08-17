# N1 — Fiche d'accès aux neutrinos par oscillations v0.1

## 0. Statut, périmètre et coupure

```text
statut : fiche scientifique active du cycle neutrino ;
étape : N1 du protocole commun des quatre accès ;
date : 17 juillet 2026 ;
date de coupure bibliographique : 17 juillet 2026 inclus ;
voie étudiée : oscillations de neutrinos et d'antineutrinos ;
cadre principal : mélange unitaire à trois saveurs, propagation cohérente et
                  interactions faibles standard, avec effets de matière lorsque
                  le milieu traversé les rend pertinents ;
fonction : reconstruire la chaîne qui relie production, propagation, détection,
           distributions d'événements et contraintes sur les paramètres
           d'oscillation ;
ne vaut pas : détermination des masses absolues, verdict définitif sur l'ordre
               des masses, preuve acquise de violation de charge-parité (CP),
               test exhaustif de toute physique au-delà de trois saveurs ou
               synthèse générale de la physique des neutrinos ;
révision : requise si une source primaire ou une mise à jour d'ajustement global
            modifie substantiellement l'état empirique décrit ici.
```

La fiche applique le [protocole N0](N0_Protocole_commun_fiches_acces_neutrinos_v0_1.md).
Elle sépare trois niveaux qui ne doivent pas être confondus :

```text
1. expériences et traces propres à chaque dispositif ;
2. analyses conjointes partageant réellement paramètres, modèles et corrélations ;
3. ajustements globaux coordonnant des résultats hétérogènes.
```

Un ajustement global n'est pas un instrument unique. Il combine des contraintes
issues de chaînes d'accès différentes et dépend de la manière dont les profils,
likelihoods, priors, corrélations et conventions sont importés.

## 1. Objet ou fonction ciblée

### 1.1 États de saveur, états de masse et matrice de mélange

Dans le cadre à trois neutrinos légers, les états de saveur associés aux
interactions faibles chargées sont reliés aux états propres de masse par la
matrice de Pontecorvo–Maki–Nakagawa–Sakata (PMNS) :

```math
|\nu_\alpha\rangle = \sum_{i=1}^{3} U^*_{\alpha i}|\nu_i\rangle,
\qquad
\alpha \in \{e,\mu,\tau\}.
```

La matrice unitaire est paramétrée, dans une convention usuelle, par trois angles
`theta_12`, `theta_13`, `theta_23` et une phase de Dirac `delta_CP`. Des phases de
Majorana peuvent exister si les neutrinos sont de Majorana, mais elles
n'interviennent pas dans les probabilités ordinaires d'oscillation.

La propagation relative des composantes de masse produit des phases dépendant de
`m_i^2 L / (2E)`. En vide :

```math
P_{\alpha\to\beta}(L,E)
=
\left|
\sum_i U_{\beta i}
\exp\left(-i\frac{m_i^2 L}{2E}\right)
U^*_{\alpha i}
\right|^2.
```

Une translation commune :

```text
m_i^2 -> m_i^2 + C
```

multiplie l'amplitude par une phase globale et laisse la probabilité inchangée.
Les oscillations contraignent donc des différences de masses au carré :

```math
\Delta m^2_{ij}=m_i^2-m_j^2,
```

et non l'ancrage absolu du spectre.

### 1.2 Conventions obligatoires

La fiche emploie les conventions suivantes, à déclarer lors de toute citation
numérique :

```text
Delta m^2_21 > 0 : signe fixé par le secteur solaire et les effets de matière ;
ordre normal (NO) : m_3 est l'état le plus lourd, Delta m^2_31 > 0 ;
ordre inversé (IO) : m_3 est l'état le plus léger, Delta m^2_32 < 0 ;
convention NuFIT : Delta m^2_3l = Delta m^2_31 en NO,
                    Delta m^2_3l = Delta m^2_32 en IO.
```

Les fréquences effectives mesurées dans certains canaux :

```text
Delta m^2_ee ;
Delta m^2_mumu ;
```

sont des combinaisons adaptées à une probabilité de disparition. Elles ne sont
pas des paramètres fondamentaux supplémentaires et ne doivent pas être remplacées
sans formule par `Delta m^2_31` ou `Delta m^2_32`.

### 1.3 Fonctions du secteur contraintes selon les régimes

| Régime d'accès | Signal dominant | Fonction principalement contrainte | Dépendances décisives |
|---|---|---|---|
| neutrinos solaires | survie de `nu_e`, spectre, taux, asymétrie jour–nuit | `theta_12`, `Delta m^2_21`, avec dépendance à `theta_13` | modèle solaire, sections efficaces, propagation Mikheyev–Smirnov–Wolfenstein (MSW), profil de matière terrestre |
| réacteurs à moyenne ou longue base | disparition spectrale de `anti-nu_e` | `theta_12`, `Delta m^2_21`, interférences avec le secteur atmosphérique | flux relatif, réponse énergétique, arrière-plans, distances aux cœurs |
| réacteurs à base kilométrique | disparition de `anti-nu_e` | `theta_13`, `Delta m^2_ee` | comparaison proche–lointaine, calibration énergétique, spectre de réacteur |
| accélérateurs longue base | disparition de `nu_mu` et apparition de `nu_e`, avec modes neutrino et antineutrino | `theta_23`, `|Delta m^2_3l|`, `delta_CP`, ordre sous corrélations | flux, interactions neutrino–noyau, détecteurs proches et lointains, effets de matière, contrainte réacteur sur `theta_13` |
| atmosphériques | distributions en énergie et angle zénithal de plusieurs topologies | `theta_23`, `|Delta m^2_3l|`, ordre via propagation dans la Terre | flux atmosphérique, interactions, reconstruction, composition de saveur, profil de densité terrestre |

Cette pluralité explique pourquoi aucun appareil ne « mesure la matrice PMNS »
comme un objet isolé. Les paramètres émergent d'une coordination de sensibilités
partiellement complémentaires et partiellement corrélées.

## 2. Production de la trace

### 2.1 Chaîne physique minimale

```text
processus source
-> production d'un neutrino associé à une saveur opérationnelle
-> propagation cohérente des composantes de masse
-> modification éventuelle par la matière
-> interaction faible dans le détecteur
-> particules secondaires, lumière ou charge
-> reconstruction d'énergie, direction, topologie et catégorie
-> histogrammes ou échantillons publiés
-> inférence des paramètres d'oscillation.
```

La « saveur » n'est pas observée directement pendant le vol. Elle est attribuée
opérationnellement aux états préparés et détectés par les leptons chargés et les
canaux d'interaction. Entre ces deux interfaces, la description pertinente est
celle de l'évolution cohérente dans la base de masse, sous le Hamiltonien déclaré.

### 2.2 Sources et préparations

#### Réacteurs

Les réacteurs produisent des antineutrinos électroniques par les désintégrations
bêta des produits de fission. La détection principale utilise la désintégration
bêta inverse :

```math
\bar\nu_e + p \to e^+ + n.
```

Le positron donne l'estimation principale de l'énergie, tandis que la capture
retardée du neutron fournit une coïncidence caractéristique. Les expériences à
plusieurs détecteurs réduisent la dépendance au flux absolu en comparant des
spectres à différentes bases.

#### Accélérateurs

Un faisceau de protons produit des hadrons dont les désintégrations engendrent un
faisceau dominé par `nu_mu` ou `anti-nu_mu`. Les cornes magnétiques sélectionnent
la charge des hadrons. Un détecteur proche contraint le flux, les interactions et
certaines réponses avant oscillation significative ; le détecteur lointain mesure
la disparition de `nu_mu` et l'apparition de `nu_e`.

Le détecteur proche ne supprime pas les incertitudes d'interaction. Il les
transforme en contraintes corrélées dont l'extrapolation vers le détecteur
lointain dépend des cibles, acceptances, topologies et modèles nucléaires.

#### Soleil

Les réactions de fusion produisent des neutrinos électroniques avec plusieurs
spectres. Leur propagation dans le plasma solaire modifie les états propres
instantanés par l'effet MSW. Les détecteurs mesurent des taux ou spectres par
interaction chargée, interaction neutre ou diffusion élastique. La séparation
entre flux total et composante électronique a historiquement établi la conversion
de saveur ; la détermination des paramètres exige ensuite un modèle de
propagation, des flux solaires et des réponses expérimentales.

#### Atmosphère

Les gerbes de rayons cosmiques produisent pions, kaons et muons, puis des
neutrinos couvrant de larges gammes d'énergie et de longueur de trajet. La Terre
fournit à la fois des bases allant de dizaines à environ `10^4` km et un milieu
matériel. La direction reconstruite joue donc le rôle d'une information sur la
longueur de propagation.

## 3. Observable publiée

### 3.1 L'objet publié n'est pas la probabilité idéale

Les collaborations publient typiquement :

```text
comptages par catégorie ;
spectres en énergie reconstruite ;
distributions angulaires ;
rapports proche–lointain ;
matrices de migration ou réponses ;
profils de vraisemblance ou Delta chi^2 ;
posteriors marginalisés ;
contours multidimensionnels ;
tables de systématiques et covariances.
```

Une probabilité d'oscillation idéale est insérée dans un modèle direct qui produit
des événements reconstruits. Schématiquement :

```math
N_b^{\rm pred}
=
\sum_{\alpha,\beta}
\int dE\,d\Phi\;
\Phi_\alpha(E)
P_{\alpha\to\beta}(E,L)
\sigma_\beta(E,\Phi)
\epsilon_b(E,\Phi)
R_b(E_{\rm rec}|E,\Phi)
+
B_b.
```

Ici `Phi` regroupe les variables cinématiques et topologiques ; `R_b` représente
la migration vers le bin reconstruit ; `B_b` représente les arrière-plans.
L'inférence porte sur l'accord entre ces prédictions et les données, non sur une
lecture directe de `P_{alpha beta}`.

### 3.2 Disparition et apparition

Une mesure de disparition compare une population attendue et une population
reconstruite dans le même canal de saveur. Elle contraint fortement une amplitude
de mélange et une fréquence, mais peut perdre l'information sur le signe d'une
différence de masses ou sur une phase.

Une mesure d'apparition recherche une saveur différente de celle dominant le
faisceau. Elle accroît la sensibilité à `delta_CP`, à l'ordre et aux corrélations
entre paramètres, mais dépend davantage des arrière-plans, des interactions et de
la séparation entre effets de matière et effets de phase.

### 3.3 Ajustement global comme objet documentaire propre

NuFIT 6.1 coordonne des données solaires, réacteur, accélérateur et atmosphériques
disponibles en novembre 2025. Il fournit des projections `Delta chi^2`, des régions
multidimensionnelles et des fichiers numériques. Il doit être cité avec sa version
et avec l'article méthodologique NuFIT 6.0.

Sa sortie est une reconstruction globale sous le cadre à trois saveurs. Elle ne
remplace pas :

```text
les données et modèles de détecteur des collaborations ;
les likelihoods complètes lorsqu'elles ne sont pas publiques ;
les corrélations internes non exportées ;
les différences entre constructions bayésiennes et fréquentistes.
```

## 4. Modèle de mesure ou de passage

### 4.1 Propagation en matière

Dans la base de saveur, l'évolution peut être écrite :

```math
i\frac{d}{dx}|\nu\rangle
=
\left[
\frac{1}{2E}U\,\mathrm{diag}(m_1^2,m_2^2,m_3^2)U^\dagger
+
\mathrm{diag}(V_e,0,0)
\right]|\nu\rangle,
```

avec :

```math
V_e=\sqrt{2}G_F N_e
```

pour les neutrinos et signe opposé pour les antineutrinos. La matière ne constitue
pas un bruit ajouté à une probabilité de vide ; elle modifie le Hamiltonien et peut
renforcer ou supprimer certaines conversions.

Les effets de matière jouent des rôles différents :

```text
Soleil : transformation adiabatique ou partiellement adiabatique du secteur 1–2 ;
Terre, longue base : différence neutrino–antineutrino corrélée à l'ordre ;
atmosphériques : résonances et motifs dépendant de l'énergie et du trajet.
```

Une asymétrie neutrino–antineutrino ne doit donc pas être attribuée immédiatement
à `delta_CP` : les effets de matière produisent eux aussi une asymétrie.

### 4.2 Paramètres tenus fixes ou contraints extérieurement

Les analyses de longue base ont souvent une sensibilité limitée à `theta_12` et
`Delta m^2_21`. Elles utilisent des contraintes externes sur ces paramètres et,
fréquemment, une contrainte réacteur sur `theta_13`.

L'analyse conjointe T2K–NOvA publiée en 2025 utilise notamment des contraintes
externes sur `theta_12`, `Delta m^2_21` et, dans son résultat par défaut, sur
`theta_13`. Retirer la contrainte réacteur modifie certaines préférences,
notamment l'octant de `theta_23`, sans rendre l'ensemble incohérent.

Une valeur publiée pour `delta_CP`, l'octant ou l'ordre est donc conditionnelle à
la combinaison de données et aux contraintes incorporées.

### 4.3 Cadre standard et alternatives

Le noyau de cette fiche suppose :

```text
trois neutrinos légers actifs ;
matrice PMNS unitaire ;
production et détection par interactions faibles standard ;
propagation cohérente avec masses constantes ;
profil de matière déclaré ;
absence d'interactions non standard, décroissance ou décohérence exotique.
```

Ces hypothèses peuvent être testées, mais elles ne sont pas simultanément levées
dans une extraction standard des six paramètres. Une anomalie locale ne suffit
pas à conclure à une quatrième saveur ou à une dynamique nouvelle sans analyse
propre.

## 5. Incertitudes, corrélations et dégénérescences

### 5.1 Incertitudes de flux et de source

- production hadronique et focalisation pour les faisceaux accélérateurs ;
- puissances, compositions isotopiques et spectres de réacteurs ;
- flux solaires et dépendances au modèle solaire ;
- flux atmosphériques, rayons cosmiques primaires et production de hadrons.

Les comparaisons relatives et détecteurs proches réduisent certaines incertitudes,
mais ne les abolissent pas.

### 5.2 Interactions neutrino–noyau

Dans les expériences accélérateur et atmosphériques, l'énergie du neutrino n'est
pas directement mesurée. Elle est reconstruite à partir des particules finales,
sous des modèles de cible nucléaire, d'états initiaux, de corrélations, de
réinteractions finales et de production hadronique.

Des biais de modèle peuvent déplacer simultanément :

```text
échelle d'énergie reconstruite ;
composition des échantillons ;
efficacité de sélection ;
extrapolation proche–lointain ;
forme du spectre d'apparition ou de disparition.
```

Cette couche est l'une des médiations décisives du secteur longue base.

### 5.3 Réponse et calibration

Pour les réacteurs, une non-linéarité de réponse énergétique peut imiter un
déplacement de fréquence. Pour les détecteurs Cherenkov ou calorimétriques, la
reconstruction des leptons, hadrons et topologies conditionne les catégories
publiées. Les calibrations et échantillons latéraux doivent donc être considérés
comme partie du résultat, non comme détails auxiliaires.

### 5.4 Dégénérescences physiques

#### Octant de `theta_23`

Une probabilité de disparition dominée par `sin^2(2 theta_23)` est presque
symétrique sous :

```text
theta_23 -> pi/2 - theta_23.
```

L'apparition et les effets sous-dominants brisent partiellement cette symétrie.
Une préférence d'octant reste sensible à `theta_13`, `delta_CP`, à l'ordre et aux
systématiques.

#### Ordre–phase

Dans les canaux d'apparition, ordre des masses, phase `delta_CP` et effets de
matière peuvent produire des déplacements spectraux partiellement similaires.
T2K et NOvA ont des bases et énergies différentes ; leur combinaison est donc
informative, mais sa conclusion dépend du jeu de données exact et des priors.

#### Paramètres solaires

Les données solaires et de réacteurs à longue base contraignent des combinaisons
complémentaires de `theta_12` et `Delta m^2_21`. La cohérence ou tension entre les
secteurs dépend notamment des informations jour–nuit et de la réponse spectrale.
Les premiers résultats de JUNO renforcent fortement la composante réacteur de ce
contraste.

### 5.5 Corrélations entre expériences

Les corrélations ne sont pas toutes de même rang :

```text
corrélations physiques : mêmes paramètres d'oscillation ;
corrélations externes : contraintes réacteur ou solaire partagées ;
corrélations de modèle : générateurs, sections efficaces, données hadroniques ;
corrélations instrumentales : parfois communes, souvent spécifiques ;
corrélations statistiques : inexistantes si les événements sont indépendants,
                             mais possibles si un jeu de données ou profil est réutilisé.
```

L'analyse conjointe T2K–NOvA a étudié explicitement les corrélations de flux,
d'interactions et de détecteur avant de définir son likelihood commun. Une somme
de contours publiés n'aurait pas le même statut.

## 6. Construction statistique

### 6.1 Fréquentiste et bayésien

Les collaborations et ajustements globaux n'emploient pas toujours la même
construction :

```text
profils de likelihood ou Delta chi^2 ;
intervalles corrigés de type Feldman–Cousins ;
posteriors bayésiens et régions de plus haute densité ;
Bayes factors pour hypothèses discrètes ;
p-values ou tests de goodness of fit.
```

Les intervalles ne deviennent pas interchangeables parce qu'ils portent le même
nom de paramètre. La fiche conserve la convention de chaque source.

### 6.2 Paramètres périodiques et frontières

`delta_CP` est périodique. Les valeurs `0` et `pi` correspondent à la conservation
de CP dans le cadre standard. Une exclusion locale ou un intervalle qui évite ces
valeurs dépend :

```text
de l'ordre conditionné ou marginalisé ;
du choix de prior ou de statistique ;
des contraintes sur theta_13 ;
des corrélations avec theta_23 ;
du traitement des effets de matière.
```

L'ordre et l'octant sont des hypothèses discrètes ou des régions séparées. Leur
« préférence » ne vaut pas détection sans seuil et construction explicités.

### 6.3 Résultat observé, sensibilité et projection

La sensibilité prévue à l'ordre ou à `delta_CP` sous un scénario vrai n'est pas un
résultat observé. La première analyse de JUNO démontre déjà une précision élevée
sur le secteur solaire, mais ne constitue pas encore une détermination de l'ordre
des masses.

## 7. État empirique daté à la coupure

### 7.1 Résultats primaires et analyses conjointes représentatives

| Énoncé | Données ou exposition | Modèle et hypothèses | Statut statistique | Date des données | Source |
|---|---|---|---|---|---|
| JUNO contraint simultanément `sin^2 theta_12 = 0.3092 +/- 0.0087` et `Delta m^2_21 = (7.50 +/- 0.12) x 10^-5 eV^2` en NO | 59,1 jours, réacteurs à 52,5 km | trois saveurs, réponse énergétique et fonds modélisés, résultat cité sous NO | estimation publiée ; ne détermine pas encore l'ordre | 26 août–2 novembre 2025 | [JUNO, Nature 654, 343–348 (2026)](https://doi.org/10.1038/s41586-026-10538-z) |
| Daya Bay contraint précisément `theta_13` et la fréquence atmosphérique effective | 5,55 millions de candidats, 3158 jours, capture sur gadolinium | trois saveurs, comparaison proche–lointaine ; conversion de `Delta m^2_ee` vers `Delta m^2_32` sous ordre | `sin^2 2theta_13 = 0.0851 +/- 0.0024` ; valeurs de `Delta m^2_32` conditionnées à NO ou IO | collecte achevée le 12 décembre 2020 | [Daya Bay, PRL 130, 161802 (2023)](https://doi.org/10.1103/PhysRevLett.130.161802) |
| RENO fournit une mesure finale indépendante de `theta_13` et `|Delta m^2_ee|` | 3800 jours, 1 211 995 candidats proches et 144 667 lointains | trois saveurs, capture sur gadolinium, comparaison spectrale | `sin^2 2theta_13 = 0.0920` avec erreurs stat. et syst. séparées ; `|Delta m^2_ee| = 2.57 x 10^-3 eV^2` | août 2011–mars 2023 | [RENO, PRD 111, 112006 (2025)](https://doi.org/10.1103/dc6j-5ky6) |
| IceCube DeepCore mesure le secteur atmosphérique par disparition de `nu_mu` | 3387 jours, 150 257 candidats, 5–100 GeV | trois saveurs, NO pour les valeurs citées, reconstruction par réseau convolutif | `Delta m^2_32 = 2.40^{+0.05}_{-0.04} x 10^-3 eV^2`, `sin^2 theta_23 = 0.54^{+0.04}_{-0.03}` | 2012–2021 | [IceCube DeepCore, arXiv:2405.02163](https://arxiv.org/abs/2405.02163) |
| T2K met à jour disparition, apparition et modèles de flux et d'interaction | `19.7 (16.3) x 10^20` protons sur cible en mode neutrino (antineutrino) | trois saveurs, contrainte réacteur dans le résultat principal, analyses fréquentiste et bayésienne | en NO : `delta_CP = -2.18^{+1.22}_{-0.47}`, `sin^2 theta_23 = 0.559^{+0.018}_{-0.078}`, `Delta m^2_32 = 2.506^{+0.039}_{-0.052} x 10^-3 eV^2` ; préférences non définitives | exposition accumulée avant la prépublication de juin 2025 | [T2K, PRL 135, 261801 (2025)](https://doi.org/10.1103/gh5j-5cwv) |
| NOvA fournit son analyse de dix années avec exposition neutrino doublée | données de disparition et apparition dans les deux modes | trois saveurs, analyse bayésienne, contrainte Daya Bay étudiée séparément | `Delta m^2_32 = 2.431^{+0.036}_{-0.034} x 10^-3 eV^2` en NO ; `sin^2 theta_23 = 0.55^{+0.06}_{-0.02}` ; préférence modérée pour NO, renforcée avec contrainte réacteur | environ dix années, version publique septembre 2025 | [NOvA, arXiv:2509.04361](https://arxiv.org/abs/2509.04361) et PRL 136, 011802 (2026) |
| La première analyse conjointe T2K–NOvA partage likelihoods et modèles complets des deux expériences | jeux de données des analyses individuelles référencées par la publication | posterior bayésien commun, contrainte réacteur par défaut, contraintes solaires externes | `Delta m^2_32 = 2.43^{+0.04}_{-0.03} x 10^-3 eV^2` en NO et `-2.48^{+0.03}_{-0.04} x 10^-3 eV^2` en IO ; pas de forte préférence d'ordre ; intervalles `delta_CP` dépendants de l'ordre | jeux de données antérieurs à la publication d'octobre 2025 | [T2K–NOvA, Nature 646, 818–824 (2025)](https://doi.org/10.1038/s41586-025-09599-3) |
| L'analyse conjointe Super-Kamiokande–T2K coordonne atmosphériques et faisceau avec modèle d'interaction commun | 3244,4 jours atmosphériques et exposition T2K `19.7 (16.3) x 10^20` POT | trois saveurs, corrélations de détecteur et interaction évaluées | exclusion de CP conservée au niveau `1.9 sigma` dans la construction citée ; préférence limitée pour NO | données antérieures à mai 2024 | [Super-Kamiokande–T2K, PRL 134, 011801 (2025)](https://doi.org/10.1103/PhysRevLett.134.011801) |

Les valeurs ci-dessus ne constituent pas une table de moyennes mondiales. Elles
illustrent les fonctions distinctes des chaînes d'accès et leurs constructions
statistiques.

### 7.2 État global versionné

[NuFIT 6.1](https://www.nu-fit.org/?q=node%2F309) est l'ajustement global actif à
la coupure. Il est fondé sur les données disponibles en novembre 2025 et doit être
cité avec l'article :

- [NuFIT 6.0, JHEP 12 (2024) 216](https://doi.org/10.1007/JHEP12(2024)216) ;
- [prépublication arXiv:2410.05380](https://arxiv.org/abs/2410.05380).

La version 6.1 intègre notamment les premiers résultats de JUNO et de SNO+, les
mises à jour de longue base et des informations atmosphériques Super-Kamiokande et
IceCube sous forme de tables ou profils disponibles.

Son état directeur peut être formulé sans réduire les profils à un nombre :

```text
theta_12, theta_13, Delta m^2_21 et |Delta m^2_3l| : fortement contraints ;
theta_23 : ambiguïté d'octant encore active ;
delta_CP : contrainte dépendante de l'ordre et de la combinaison de données ;
ordre des masses : préférences variables selon l'inclusion des profils
                    atmosphériques, sans verdict universel acquis à la coupure.
```

Le premier résultat de JUNO est postérieur à l'article méthodologique NuFIT 6.0,
mais inclus dans l'actualisation 6.1. Les publications finales T2K et NOvA peuvent
être postérieures à la date nominale de certaines données tout en reposant sur des
prépublications déjà publiques ; la version et la date de chaque entrée doivent
donc rester visibles.

## 8. Résultat effectivement établi

### 8.1 Acquis physiques

Les oscillations établissent de manière robuste :

1. **des états de saveur non identiques aux états propres de masse** dans le cadre
   à trois saveurs ;
2. **au moins deux différences de masses au carré non nulles**, donc un spectre
   non dégénéré ;
3. **trois angles de mélange non nuls**, avec des précisions différentes ;
4. **une cohérence quantitative entre plusieurs régimes de `L/E`**, malgré des
   sources, détecteurs et interactions hétérogènes ;
5. **la nécessité de traiter les effets de matière** pour les secteurs solaire,
   longue base et atmosphérique ;
6. **une architecture différentielle du spectre** qui fixe relations, amplitudes
   et motifs sans fixer l'origine commune des masses.

### 8.2 Paramètres bien contraints et paramètres encore structurés par des ambiguïtés

Le secteur solaire `theta_12`–`Delta m^2_21` est désormais fortement resserré par
JUNO, en coordination avec les résultats solaires et les autres réacteurs à longue
base. `theta_13` est précisément contraint par les expériences réacteur à bases
kilométriques. La fréquence atmosphérique est mesurée de façon convergente par
réacteurs, accélérateurs et atmosphériques, sous conventions de projection à
raccorder.

En revanche :

```text
octant de theta_23 : non fixé de manière robuste par toutes les combinaisons ;
delta_CP : les régions préférées et l'exclusion de CP conservation dépendent de
           l'ordre, des priors et du jeu de données ;
ordre des masses : préférences présentes mais non verdict commun indépendant des
                   profils et hypothèses à la coupure.
```

### 8.3 Ce que le terme « mesure des paramètres PMNS » signifie ici

Il signifie une inférence coordonnée :

```text
plusieurs distributions d'événements
+ plusieurs modèles de flux, interaction et réponse
+ un Hamiltonien commun à trois saveurs
+ conventions et contraintes externes
-> régions admissibles dans un espace corrélé de paramètres.
```

Il ne signifie pas l'accès direct à six propriétés indépendantes portées
séparément par chaque neutrino.

## 9. Limites propres de l'accès

### 9.1 Masse absolue absente

Les oscillations sont invariantes sous une translation commune des `m_i^2`. Elles
ne déterminent donc pas :

```text
m_1, m_2, m_3 séparément ;
la masse de l'état le plus léger ;
Sigma m_nu ;
m_beta ;
m_beta_beta.
```

Une hypothèse d'ordre et une valeur de masse minimale permettent de reconstruire
un spectre compatible, mais cette reconstruction ajoute une information que
l'oscillation ne fournit pas.

### 9.2 Nature Dirac ou Majorana

Les probabilités standards d'oscillation sont insensibles aux phases de Majorana.
Une détermination précise de `delta_CP` ne répond donc pas à la question Dirac ou
Majorana.

### 9.3 Origine des masses et du mélange

Le cadre ajuste les paramètres de la matrice PMNS et les écarts spectraux. Il
n'explique pas :

```text
le mécanisme de génération des masses ;
la petite échelle des masses ;
la texture des angles ;
la valeur de delta_CP ;
la présence ou l'absence de phases de Majorana.
```

### 9.4 Dépendance au cadre à trois saveurs

La cohérence globale soutient fortement le cadre standard dans son domaine, mais
la fiche n'effectue pas une combinaison exhaustive des recherches de neutrinos
stériles, interactions non standard, non-unitarité, décroissance ou décohérence.
Une déviation éventuelle doit être comparée au gain d'ajustement, aux pénalités de
modèle et aux systématiques propres.

### 9.5 Limites documentaires et computationnelles

Les données brutes et codes complets ne sont généralement pas publics. JUNO met à
disposition les données sources de certaines figures, mais pas les données brutes
ni l'ensemble du code d'analyse. Les collaborations longue base publient des
informations détaillées, sans toujours fournir une likelihood complète permettant
de reproduire toutes les corrélations.

NuFIT fournit des profils et fichiers numériques, mais leur fidélité dépend des
informations exportées par les expériences. Une reproduction indépendante exacte
de l'ajustement mondial n'est donc pas acquise par la seule lecture des articles.

## 10. Ponts vers les trois autres voies

### 10.1 Vers la cinématique bêta `m_beta`

```math
m_\beta^2=\sum_i |U_{ei}|^2m_i^2.
```

Apport des oscillations :

```text
|U_ei|^2 via theta_12 et theta_13 ;
Delta m^2_21 et fréquence atmosphérique ;
ordre possible comme hypothèse discrète.
```

Information ajoutée nécessaire :

```text
masse de l'état le plus léger ou mesure indépendante de m_beta.
```

Les oscillations permettent de traduire une borne sur `m_beta` en région du
spectre, mais ne produisent pas elles-mêmes cette borne.

### 10.2 Vers la cosmologie `Sigma m_nu`

```math
\Sigma m_\nu=m_1+m_2+m_3.
```

Les écarts mesurés donnent un plancher différent selon l'ordre, une fois la masse
minimale choisie. La conversion d'une borne cosmologique en contrainte sur chaque
`m_i` exige :

```text
cadre cosmologique ;
paramétrisation du spectre ;
ordre ou marginalisation ;
priors ;
jeux de données et modèle astrophysique.
```

Une préférence d'ordre issue de l'oscillation ne doit pas être imposée
silencieusement comme prior cosmologique.

### 10.3 Vers la double bêta sans neutrino `m_beta_beta`

Sous le mécanisme standard d'échange de neutrinos légers de Majorana :

```math
m_{\beta\beta}=\left|\sum_i U_{ei}^2m_i\right|.
```

Les oscillations fournissent les modules des éléments électroniques et la phase
de Dirac selon la convention, mais pas :

```text
les phases de Majorana ;
la masse minimale ;
le mécanisme de désintégration ;
les éléments de matrice nucléaire.
```

Elles délimitent donc une géométrie conditionnelle d'interférences, non une valeur
de `m_beta_beta`.

### 10.4 Tableau des ponts

| Quantité de départ | Relation ajoutée | Hypothèses nécessaires | Gain | Information toujours absente |
|---|---|---|---|---|
| `Delta m^2_ij`, PMNS | définition de `m_beta` | masse minimale, ordre | projeter un spectre sur la saveur électronique | échelle absolue sans donnée bêta |
| `Delta m^2_ij` | somme des masses | masse minimale, ordre, modèle cosmologique pour l'inférence | plancher et mapping spectral | borne cosmologique indépendante du modèle |
| PMNS, `Delta m^2_ij` | somme cohérente `m_beta_beta` | Majorana, phases, masse minimale, mécanisme, matrices nucléaires | enveloppes conditionnelles | valeur ou détection de `m_beta_beta` |

## 11. Audit des sources et dettes restantes

### 11.1 Sources primaires mobilisées

#### Réacteurs

- [JUNO Collaboration, *Measurement of reactor neutrino oscillation with the first JUNO data*, Nature 654 (2026)](https://doi.org/10.1038/s41586-026-10538-z) ;
- [Daya Bay Collaboration, *Precision Measurement of Reactor Antineutrino Oscillation at Kilometer-Scale Baselines*, PRL 130 (2023)](https://doi.org/10.1103/PhysRevLett.130.161802) ;
- [RENO Collaboration, *Measurement of reactor antineutrino oscillation parameters using the full 3800-day dataset*, PRD 111 (2025)](https://doi.org/10.1103/dc6j-5ky6) ;
- [SNO+, *Reactor Antineutrino Oscillations and Geoneutrinos in SNO+*, arXiv:2604.05746](https://arxiv.org/abs/2604.05746).

#### Accélérateurs et analyses conjointes

- [T2K Collaboration, *Results on neutrino mixing including a new far-detector muon-like sample*, PRL 135 (2025)](https://doi.org/10.1103/gh5j-5cwv) ;
- [NOvA Collaboration, *Precision measurement with 10 years of data*, arXiv:2509.04361](https://arxiv.org/abs/2509.04361) ;
- [NOvA–T2K, *Joint neutrino oscillation analysis*, Nature 646 (2025)](https://doi.org/10.1038/s41586-025-09599-3) ;
- [Super-Kamiokande–T2K, *First joint oscillation analysis*, PRL 134 (2025)](https://doi.org/10.1103/PhysRevLett.134.011801).

#### Atmosphériques

- [IceCube Collaboration, *Measurement of atmospheric neutrino oscillation parameters with 9.3 years of DeepCore data*, arXiv:2405.02163](https://arxiv.org/abs/2405.02163) ;
- [KM3NeT/ORCA, *Measurement of neutrino oscillation parameters with the first six detection units*, JHEP 10 (2024) 206](https://arxiv.org/abs/2408.07015).

#### Coordination globale

- [NuFIT 6.1 — données disponibles en novembre 2025](https://www.nu-fit.org/?q=node%2F309) ;
- [NuFIT 6.0, JHEP 12 (2024) 216](https://doi.org/10.1007/JHEP12(2024)216) ;
- [NuFIT 6.0, arXiv:2410.05380](https://arxiv.org/abs/2410.05380).

### 11.2 Sources évolutives et versions

```text
NuFIT : version 6.1, données annoncées disponibles en novembre 2025,
         consultation le 17 juillet 2026 ;
JUNO : version de référence Nature publiée le 10 juin 2026,
       données du 26 août au 2 novembre 2025 ;
NOvA : prépublication publique septembre 2025, publication PRL en 2026 ;
T2K : prépublication juin 2025, version de référence PRL 135, 261801 ;
IceCube : prépublication mai 2024, données 2012–2021.
```

### 11.3 Données ou likelihoods publiques

- NuFIT fournit des fichiers de profils et régions projetées ;
- JUNO fournit les données sources de plusieurs figures, mais pas les données
  brutes ni le code complet ;
- Daya Bay fournit des matériaux supplémentaires et des spectres de fond pour
  certains résultats ;
- les analyses conjointes longue base ne rendent pas nécessairement publique une
  likelihood complète réutilisable hors collaboration ;
- l'état précis des produits publics doit être vérifié avant tout calcul dans
  `N5`.

### 11.4 Désaccords conservés

La fiche conserve comme résultats, non comme défauts à lisser :

1. la dépendance des préférences de `delta_CP` à l'ordre ;
2. l'ambiguïté persistante de l'octant de `theta_23` ;
3. la variation de la préférence d'ordre selon l'inclusion des informations
   atmosphériques ;
4. les différences entre analyses individuelles, conjointes et globales ;
5. la non-équivalence des constructions statistiques ;
6. les tensions éventuelles entre secteurs solaire et réacteur, à redater après
   l'entrée de JUNO.

### 11.5 Dettes à reporter à N5 ou à une reprise spécialisée

- extraire les tables numériques exactes de NuFIT 6.1 et leurs variantes avec ou
  sans profils atmosphériques ;
- établir une table de conversion contrôlée entre `Delta m^2_ee`,
  `Delta m^2_mumu` et `Delta m^2_3l` ;
- vérifier la disponibilité et le format des likelihoods, chaînes et covariances
  publiques pour chaque expérience ;
- comparer les conclusions fréquentistes et bayésiennes sur `delta_CP`, l'ordre
  et l'octant sans convertir leurs niveaux par simple équivalence verbale ;
- déterminer si le premier résultat JUNO suffit à modifier quantitativement les
  enveloppes utilisées dans `N2`, `N3` et `N4` ;
- réserver les tests de stériles, non-unitarité et interactions non standard à une
  fiche dédiée si leur retrait modifie un pont entre les quatre accès.

## 12. Effet sur la question du cycle

Le résultat du cycle 3 est confirmé et précisé :

```text
les oscillations donnent une architecture différentielle du spectre,
mais cette architecture n'est pas une lecture directe d'un objet déjà complet.
```

Elle est produite par une coordination de chaînes hétérogènes :

```text
solaire et matière
+ réacteurs à plusieurs bases
+ accélérateurs proche–lointain
+ atmosphériques multi-énergies
+ analyses conjointes
+ ajustement global.
```

Cette pluralité ne dissout pas l'objet physique. Les mêmes paramètres permettent
de décrire des motifs observés dans des régimes très différents. Mais l'identité
de l'objet empirique est éprouvée par la compatibilité de ces accès, non présupposée
par l'emploi commun du mot « neutrino ».

Le gain méthodologique est double :

1. **la relation accessible peut être plus déterminée que les valeurs absolues** ;
2. **une coordination globale est un résultat d'inférence de second niveau**, qui
   doit conserver les chaînes locales au lieu de les rendre invisibles.

## 13. Verdict N1

```text
fonction du spectre contrainte : écarts de masses au carré, angles et phase de
                                  Dirac sous cadre à trois saveurs ;
trace primaire : distributions d'événements en énergie, direction et topologie ;
modèle de passage : flux + propagation + interactions + réponse + statistique ;
acquis : architecture différentielle et mélange à trois saveurs fortement étayés ;
non-acquis : échelle absolue, nature Dirac/Majorana, origine des masses,
             verdict définitif sur ordre, octant ou violation de CP ;
statut : fiche N1 close pour comparaison, sous dettes numériques et
         computationnelles explicitement reportées à N5.
```

La prochaine étape est `N2` : reconstruire l'accès cinématique bêta à `m_beta`,
en distinguant le spectre terminal enregistré, le modèle de réponse, la
construction de la limite et le passage conditionnel vers les masses propres.
