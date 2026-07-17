# N3 — Fiche d'accès cosmologique à la somme des masses des neutrinos v0.1

## 0. Statut, périmètre et coupure

```text
statut : fiche scientifique active du cycle neutrino ;
étape : N3 du protocole commun des quatre accès ;
date : 17 juillet 2026 ;
date de coupure bibliographique : 17 juillet 2026 inclus ;
voie étudiée : effets cosmologiques des neutrinos massifs, avec les résultats
                DESI DR2 + fond diffus cosmologique comme état directeur ;
fonction : reconstruire la chaîne qui relie l'histoire thermique et gravitationnelle
           des neutrinos, les observables de fond et de structure, les vraisemblances
           cosmologiques et la contrainte sur Sigma m_nu ;
ne vaut pas : mesure locale de masse, estimation séparée de m_1, m_2 et m_3,
              borne indépendante du modèle cosmologique, détection universelle d'une
              masse positive, verdict autonome sur l'ordre des masses ou reprise
              générale de toutes les tensions cosmologiques ;
révision : requise lorsqu'un nouveau résultat officiel DESI, CMB ou grande structure
           remplace la combinaison DR2 retenue, ou lorsqu'une extension du modèle
           modifie le verdict directeur du cycle.
```

La fiche applique le [protocole N0](N0_Protocole_commun_fiches_acces_neutrinos_v0_1.md),
prolonge la [fiche N1 sur les oscillations](N1_Fiche_acces_oscillations_neutrinos_v0_1.md)
et la [fiche N2 sur la cinématique bêta](N2_Fiche_acces_cinematique_beta_neutrinos_v0_1.md).
Elle reprend également la distinction du cycle cosmologique entre modèle dynamique,
paramètres, observables reconstruites et inférence.

Le résultat directeur à la coupure est fourni par :

- [DESI Collaboration, *Constraints on Neutrino Physics from DESI DR2 BAO and DR1 Full Shape*, Physical Review D 112, 083513 (2025)](https://doi.org/10.1103/w9pk-xsk7) ;
- [version arXiv 2503.14744 v3](https://arxiv.org/abs/2503.14744) ;
- [DESI DR2 Results II — BAO and cosmological constraints](https://doi.org/10.1103/tr6y-kpc6) ;
- [produits publics des chaînes cosmologiques DESI DR2](https://data.desi.lbl.gov/public/papers/y3/bao-cosmo-params/README.html).

À la coupure, aucune publication officielle ultérieure de DESI ne remplace cette
analyse neutrino. Les travaux de 2026 identifiés portent principalement sur des tests
d'extensions, de priors ou de systèmes de données ; ils sont utilisés comme stress
tests et non comme nouvel état directeur.

## 1. Objet ou fonction ciblée

### 1.1 La somme des masses

La fonction du spectre contrainte est :

```math
\Sigma m_\nu = m_1+m_2+m_3.
```

Elle se distingue de :

```text
oscillations : Delta m^2_ij = m_i^2-m_j^2 ;
cinématique :  m_beta^2 = somme_i |U_ei|^2 m_i^2 ;
double bêta :  m_beta_beta = |somme_i U_ei^2 m_i| sous mécanisme standard.
```

Sous une histoire thermique standard, trois espèces actives stables et la densité
relique habituelle, la densité physique actuelle des neutrinos non relativistes est
approximativement reliée à la somme par :

```math
\Omega_\nu h^2 \simeq \frac{\Sigma m_\nu}{93.14\ \mathrm{eV}}.
```

Cette relation n'est pas une définition purement cinématique. Elle incorpore :

```text
la température relicte des neutrinos ;
leur distribution de phase ;
leur nombre effectif et leur découplage ;
leur stabilité cosmologique ;
l'absence de production ou dilution non standard significative.
```

La cosmologie ne contraint donc pas seulement une somme algébrique. Elle contraint
les effets d'un secteur neutrino thermalement et gravitationnellement modélisé, puis
traduit ces effets en `Sigma m_nu`.

### 1.2 Paramétrisations du spectre

Trois paramétrisations doivent rester distinctes :

```text
A. trois masses dégénérées : m_1=m_2=m_3=Sigma m_nu/3 ;
B. une masse totale avec approximation d'un état massif ou de trois états égaux ;
C. spectre hiérarchisé par les Delta m^2 de N1 et une masse minimale m_l.
```

Le résultat DESI directeur utilise trois états dégénérés pour la borne standard,
avec un prior de non-négativité sur `Sigma m_nu`. Une analyse séparée introduit les
contraintes d'oscillation et les deux ordres pour inférer la masse de l'état le plus
léger.

L'approximation dégénérée décrit correctement une grande partie des effets actuels
pour une masse totale fixée, mais elle ne doit pas être présentée comme résultat sur
l'égalité physique des trois masses.

### 1.3 Ce que signifie « masse cosmologique »

L'expression désigne ici un paramètre d'un modèle direct de l'histoire cosmique :

```text
conditions initiales et contenu thermique
-> expansion du fond
-> recombinaison et anisotropies du CMB
-> transition relativiste / non relativiste des neutrinos
-> croissance des perturbations et libre parcours
-> lentillage et distribution de matière
-> distances BAO et spectres de puissance
-> vraisemblance jointe
-> posterior ou profil de Sigma m_nu.
```

Elle ne désigne ni une particule pesée individuellement ni un déficit d'énergie
mesuré événement par événement.

## 2. Effets physiques producteurs de sensibilité

### 2.1 Transition thermique et expansion

Les neutrinos relictes se comportent comme radiation lorsqu'ils sont relativistes,
puis contribuent progressivement à la densité de matière lorsqu'ils deviennent non
relativistes. Pour une somme fixée, cette transition modifie :

```text
H(z) et les distances intégrées ;
l'époque d'égalité matière-radiation ;
la distance angulaire à la dernière diffusion ;
le rapport entre l'échelle acoustique primordiale et les distances tardives ;
la quantité de matière qui participe efficacement à la croissance.
```

La contrainte BAO + CMB la plus serrée de DESI DR2 repose principalement sur cette
cohérence de l'histoire d'expansion. Elle n'est pas une observation isolée d'une
empreinte de libre parcours dans une carte de galaxies.

### 2.2 Libre parcours et croissance

La vitesse thermique des neutrinos empêche leur regroupement gravitationnel sous
une échelle dépendante du temps et de la masse. La fraction :

```math
f_\nu = \frac{\Omega_\nu}{\Omega_m}
```

produit une suppression dépendante de l'échelle et du redshift dans le spectre de
puissance de la matière, ainsi qu'une modification du potentiel de lentillage.

Cette signature intervient dans :

```text
le lentillage du CMB ;
la forme complète du spectre de puissance des galaxies ;
les distorsions en espace des redshifts ;
le lentillage faible et les corrélations multi-sondes ;
la forêt Lyman-alpha sous modèles astrophysiques supplémentaires.
```

Elle est plus spécifique à la croissance que la seule géométrie BAO, mais son
extraction exige des modèles de biais, non-linéarité, baryons, redshifts et réponses
de sonde. À la coupure, la contrainte DESI de forme complète fondée directement sur
cette information reste moins serrée que la borne géométrique CMB + BAO.

### 2.3 CMB primaire et lentillage du CMB

Le fond diffus cosmologique apporte plusieurs informations :

```text
spectres de température et polarisation : paramètres primordiaux, densités,
                                       échelle acoustique et profondeur optique ;
lentillage du CMB : intégrale de la structure gravitationnelle entre la dernière
                    diffusion et l'observateur ;
calibration du son primordial : ancrage du rapport entre r_d et les distances BAO.
```

Le jeu CMB directeur DESI combine :

```text
Planck PR3 à bas multipoles pour TT et EE ;
Planck PR4 NPIPE / CamSpec à hauts multipoles pour TT, TE et EE ;
lentillage Planck PR4 + ACT DR6, vraisemblance ACT v1.2.
```

La combinaison ne peut pas être remplacée dans une citation par le mot générique
« Planck » ou « CMB », car le choix de likelihood déplace les paramètres et leurs
corrélations.

## 3. Production des traces et observables publiées

### 3.1 DESI DR2 : redshifts vers distances BAO

DESI DR2 utilise les trois premières années du relevé, observées de mai 2021 à avril
2024. Les mesures BAO reposent sur plus de quatorze millions de galaxies et quasars,
ainsi que sur la forêt Lyman-alpha de plus de huit cent mille quasars.

La chaîne est :

```text
photométrie de sélection
-> attribution de fibres
-> spectres
-> classification et redshift
-> catalogues et aléatoires
-> fonction de corrélation ou spectre de puissance
-> reconstruction BAO
-> ajustement du pic acoustique
-> D_M(z)/r_d, D_H(z)/r_d ou D_V(z)/r_d
-> likelihood BAO multi-redshift.
```

Les points effectifs couvrent approximativement `0.1 < z < 4.2` par les échantillons
BGS, LRG, ELG, QSO et forêt Lyman-alpha.

Les observables BAO publiées sont des rapports de distances :

```math
D_H(z)=\frac{c}{H(z)},
\qquad
D_M(z)=\int_0^z \frac{c\,dz'}{H(z')},
```

rapportés à l'horizon acoustique `r_d`. Elles ne portent pas une étiquette
expérimentale `Sigma m_nu` avant le calcul cosmologique conjoint.

### 3.2 Planck et ACT : cartes vers spectres et reconstruction de lentillage

La chaîne CMB est :

```text
température et polarisation multi-fréquences
-> calibration, masques et séparation des avant-plans
-> spectres TT, TE et EE
-> likelihoods par domaine de multipoles
-> reconstruction quadratique du potentiel de lentillage
-> spectre C_L^{phiphi} et covariance
-> modèle de Boltzmann et paramètres cosmologiques.
```

ACT DR6 fournit une carte de lentillage couvrant environ `9400 deg^2`, reconstruite
à partir des observations 2017–2021. Les produits, likelihoods et chaînes ACT DR6
sont publics. Leur rôle dans la combinaison DESI est de contraindre la structure
intégrée et de réduire certaines dégénérescences de la masse.

### 3.3 Forme complète DESI DR1

L'analyse de forme complète utilise les multipoles monopole et quadrupole du spectre
de puissance de galaxies et quasars DESI DR1 dans six intervalles de redshift, sur
la plage principale :

```math
0.02 < k/(h\,\mathrm{Mpc}^{-1}) < 0.20.
```

Elle modélise conjointement :

```text
forme primordiale et transfert ;
libre parcours des neutrinos ;
biais de galaxies ;
distorsions en espace des redshifts ;
corrections non linéaires par théorie effective des grandes structures ;
termes stochastiques ;
fenêtre, sélection et assignation des fibres.
```

Sept paramètres de nuisance par traceur sont inclus dans la modélisation citée. La
forme complète DR1 et les BAO DR2 ne sont pas combinées directement dans le résultat
directeur, faute d'une covariance croisée DR1–DR2 suffisamment établie au moment de
l'analyse.

## 4. Modèle direct et calcul cosmologique

### 4.1 Paramètres du modèle de base

Le modèle directeur est `LambdaCDM` spatialement plat, étendu par `Sigma m_nu`.
Le noyau échantillonné comprend typiquement :

```text
omega_b = Omega_b h^2 ;
omega_c = Omega_c h^2 ;
theta_* ou un paramètre d'échelle équivalent ;
tau ;
A_s ;
n_s ;
Sigma m_nu ;
paramètres de nuisance propres aux likelihoods.
```

Sont tenus fixes ou étroitement spécifiés dans le résultat standard :

```text
forme de l'énergie noire : w=-1 ;
courbure : Omega_K=0 ;
histoire thermique standard des neutrinos ;
N_eff standard lorsque non explicitement libéré ;
trois états massifs dégénérés ;
loi de gravitation de LambdaCDM ;
conditions initiales adiabatiques et spectre primordial de loi de puissance.
```

Chaque relaxation ouvre une direction de dégénérescence susceptible de modifier la
borne.

### 4.2 Calcul direct

Un code de Boltzmann calcule, pour chaque point de paramètres :

```text
H(z), distances et horizon acoustique ;
histoire des densités neutrino ;
fonctions de transfert ;
spectres CMB TT, TE, EE et lentillage ;
spectre de puissance linéaire de la matière ;
corrections non linéaires ou modèle EFT selon la sonde ;
prédictions BAO et forme complète.
```

Les prédictions sont comparées aux likelihoods. Le résultat est une distribution
conditionnelle :

```math
p(\Sigma m_\nu,\vartheta\mid D,M,P)
\propto
\mathcal{L}(D\mid\Sigma m_\nu,\vartheta,M)\,\pi(\Sigma m_\nu,\vartheta\mid P),
```

avec `D` les données, `M` le modèle et `P` les priors. Une borne sur `Sigma m_nu`
ne peut être détachée de ce triplet.

### 4.3 Deux sources physiques de la contrainte à ne pas fusionner

Le résultat DESI sépare :

```text
A. contrainte d'expansion : CMB + BAO, très serrée sous LambdaCDM ;
B. contrainte de libre parcours : forme complète + CMB ou priors externes,
                                 plus directement liée à la croissance mais plus faible.
```

Cette distinction interdit la formule simplifiée :

```text
les galaxies mesurent directement la suppression de puissance et donnent 0.064 eV.
```

La borne de `0.0642 eV` est principalement une reconstruction de l'histoire
d'expansion dans une combinaison CMB + BAO. La meilleure contrainte DESI de forme
complète citée dans le même article est `Sigma m_nu < 0.193 eV` à `95 %`, avec des
priors CMB sélectionnés.

## 5. Données, nuisances, corrélations et dégénérescences

### 5.1 Nuisances DESI BAO

Les distances BAO incorporent notamment :

```text
sélection angulaire et radiale ;
complétude et assignation des fibres ;
erreurs de redshift et contaminants ;
choix du catalogue aléatoire ;
modèle de large bande autour du pic BAO ;
reconstruction du champ de déplacement ;
covariances entre traceurs et intervalles de redshift ;
modélisation propre à la forêt Lyman-alpha.
```

La validation sur catalogues simulés incluant des neutrinos massifs teste que la
procédure BAO ne produit pas un déplacement significatif non modélisé de l'échelle.
Elle ne valide pas à elle seule le modèle cosmologique complet utilisé ensuite.

### 5.2 Nuisances CMB

Les likelihoods CMB comportent :

```text
calibration relative des fréquences ;
poussière galactique et synchrotron ;
sources radio et infrarouges ;
effets Sunyaev–Zeldovich ;
réponse des faisceaux et bruit ;
biais de reconstruction du lentillage ;
masques et couplage de modes.
```

ACT DR6 emploie des stratégies de soustraction, durcissement des estimateurs et
tests nuls pour réduire les biais d'avant-plan dans la reconstruction du lentillage.
Ces contrôles appartiennent à la chaîne de masse : le lentillage contraint la
croissance qui est elle-même corrélée à `Sigma m_nu`.

### 5.3 Dégénérescence masse–expansion

Dans `LambdaCDM`, augmenter `Sigma m_nu` modifie la densité tardive, les distances et
la croissance. Les données compensent partiellement ces effets par des déplacements
de :

```text
H_0 ;
Omega_m ;
omega_c ;
A_s et tau ;
amplitude de lentillage ;
échelle acoustique et distances intégrées.
```

Lorsque `w_0` et `w_a` deviennent libres, l'histoire d'expansion tardive peut absorber
une partie des effets auparavant attribués à la masse. La borne s'élargit alors
fortement.

### 5.4 Dégénérescences de croissance

La suppression de puissance est corrélée à :

```text
A_s et tau ;
n_s et sa forme supposée ;
biais des traceurs ;
non-linéarité et contre-termes EFT ;
feedback baryonique ;
amplitude et calibration du lentillage ;
modèles de redshift et de sélection.
```

Une contrainte obtenue par géométrie et une contrainte obtenue par forme complète ne
sont donc pas deux répétitions statistiques du même signal.

### 5.5 Paramétrisation et ordre des masses

Les oscillations imposent approximativement des planchers :

```text
ordre normal : Sigma m_nu voisin ou supérieur à 0.059 eV ;
ordre inversé : Sigma m_nu voisin ou supérieur à 0.10 eV,
```

sous trois états actifs et les écarts de N1. Un prior cosmologique uniforme à partir
de zéro attribue du volume à une région physiquement inaccessible dans ce cadre.

À l'inverse, imposer directement un plancher d'ordre ou échantillonner la masse la
plus légère change le volume de prior et la forme du posterior. La préférence pour
un ordre n'est pas un observable brut ; elle est un rapport d'évidences ou de
vraisemblances conditionné par cette paramétrisation.

## 6. Construction statistique et frontière physique

### 6.1 Borne marginalisée standard

Avec DESI DR2 BAO + CMB, sous `LambdaCDM`, trois masses dégénérées et le prior :

```math
\Sigma m_\nu \geq 0,
```

le posterior est maximal à la frontière basse et donne :

```math
\Sigma m_\nu < 0.0642\ \mathrm{eV}
\qquad (95\ %).
```

L'article indique une largeur marginalisée d'environ `0.020 eV`. Cette borne est le
résultat bayésien directeur, mais elle est dominée par la frontière du prior : le
maximum de vraisemblance se prolonge formellement vers une masse effective négative.

### 6.2 Construction fréquentiste

Une construction de Feldman–Cousins corrige le comportement de l'intervalle près de
la frontière et donne :

```math
\Sigma m_\nu < 0.053\ \mathrm{eV}
\qquad (95\ %\ fréquentiste).
```

Cette valeur est inférieure au plancher normal fourni par les oscillations. Elle ne
signifie pas que les masses physiques sont négatives ou que N1 est réfuté. Elle
localise une incompatibilité entre :

```text
le maximum de vraisemblance de la combinaison cosmologique ;
la frontière physique du modèle standard ;
les planchers imposés par les écarts de masses ;
les hypothèses de LambdaCDM et des likelihoods.
```

### 6.3 Paramètre de masse effective négatif

Le stress test `Sigma m_nu,eff` étend formellement le paramètre vers des densités
négatives afin de mesurer où les données placeraient le maximum sans frontière. Ce
paramètre n'est pas une hypothèse de particule à masse négative. Il est un diagnostic
de la direction résiduelle dans l'espace des observables.

L'analyse DESI trouve alors une tension d'environ `3 sigma` avec le plancher des
oscillations sous `LambdaCDM`. Une interprétation physique exige de tester :

```text
systématiques de données ;
likelihoods CMB et lentillage ;
modèle d'énergie noire ;
histoire thermique ou interactions du secteur neutrino ;
gravitation et autres extensions.
```

### 6.4 Priors informés par les oscillations

Lorsque les écarts de N1 et les deux ordres sont incorporés, DESI obtient :

```math
m_l < 0.023\ \mathrm{eV}
\qquad (95\ %),
```

et une préférence pour l'ordre normal. Ce résultat ne doit pas être reformulé comme
une détermination cosmologique directe de `m_1`, `m_2` ou `m_3`. Il est la projection
du posterior cosmologique à travers le modèle spectral imposé par les oscillations.

## 7. État empirique daté à la coupure

| Énoncé | Données ou exposition | Modèle et hypothèses | Statut statistique | Date des données | Source |
|---|---|---|---|---|---|
| DESI DR2 BAO + CMB donne `Sigma m_nu < 0.0642 eV` | DESI trois ans, Planck PR3/PR4, lentillage Planck+ACT DR6 | `LambdaCDM` plat, trois masses dégénérées, prior `Sigma m_nu >= 0` | borne marginalisée à `95 %`, posterior à la frontière | DESI mai 2021–avril 2024 ; ACT 2017–2021 ; Planck antérieur | [DESI neutrino DR2](https://doi.org/10.1103/w9pk-xsk7) |
| La construction Feldman–Cousins donne `Sigma m_nu < 0.053 eV` | même combinaison | même modèle, traitement fréquentiste de la frontière | borne à `95 %`, en tension avec le plancher normal | mêmes données | [DESI neutrino DR2](https://arxiv.org/abs/2503.14744) |
| L'ajout des contraintes d'oscillation donne `m_l < 0.023 eV` et préfère l'ordre normal | même combinaison + profils d'oscillation | spectres normal et inversé, masse légère échantillonnée | inférence conditionnelle, non mesure individuelle | profils d'oscillation antérieurs à la mise à jour NuFIT 6.1 | [DESI neutrino DR2](https://doi.org/10.1103/w9pk-xsk7) |
| En `w_0w_aCDM`, la borne devient `Sigma m_nu < 0.163 eV` | DESI DR2 BAO + CMB | énergie noire dynamique à deux paramètres | borne à `95 %`, tension de masse relaxée | mêmes données | [DESI neutrino DR2](https://arxiv.org/abs/2503.14744) |
| DESI DR1 forme complète fournit `Sigma m_nu < 0.193 eV` dans la combinaison la plus forte citée | multipoles de galaxies et quasars DR1 + priors CMB sélectionnés | `LambdaCDM`, EFT des grandes structures, nuisances de biais et non-linéarité | borne complémentaire à `95 %`, sensibilité de libre parcours | DESI DR1 mai 2021–juin 2022 | [DESI neutrino DR2](https://doi.org/10.1103/w9pk-xsk7) |
| Une analyse ACT DR6 + Planck + DESI DR2 avec isocourbure neutrino trouve `Sigma m_nu < 0.057 eV`, mais `0.092 eV` avec un prior informé par la hiérarchie | CMB Planck/ACT/SPT, DESI DR2, DES Y5 SN | `LambdaCDM` avec mode d'isocourbure, variantes de prior | stress test indépendant ; pas résultat directeur | publications disponibles juin 2026 | [Hou et al., arXiv:2606.17994](https://arxiv.org/abs/2606.17994) |
| Une équation d'état d'énergie noire à quatre paramètres donne `Sigma m_nu < 0.101 eV` | Planck + DESI DR2 BAO + Pantheon+ | extension flexible de l'énergie noire | stress test indépendant de dépendance au modèle | publication décembre 2025 | [Nair et al., arXiv:2512.08752](https://arxiv.org/abs/2512.08752) |
| Une combinaison `w_0w_aCDM`, `N_eff` libre et lentillage DES Y1 trouve `Sigma m_nu = 0.098^{+0.016}_{-0.037} eV` | DESI DR2, CMB, DES Y5 SN et DES Y1 lentillage | énergie noire dynamique et contenu relativiste libre | préférence positive annoncée à `2.7 sigma`, non transportable au modèle directeur | publication juillet 2025 | [Du et al., arXiv:2507.16589](https://arxiv.org/abs/2507.16589) |

La table montre qu'il n'existe pas une « borne cosmologique 2026 » unique. Chaque
nombre est un énoncé différent, défini par son modèle, ses données et ses priors.

## 8. Résultat effectivement établi

### 8.1 Acquis physiques

La voie cosmologique établit à la coupure :

1. **une forte sensibilité collective au secteur neutrino massif** dans la cohérence
   du fond, des distances et de la croissance ;
2. **une borne extrêmement serrée sous `LambdaCDM`**, proche du plancher permis par
   l'ordre normal ;
3. **une complémentarité physique entre expansion et libre parcours**, même si la
   première produit actuellement la contrainte la plus forte ;
4. **une préférence conditionnelle pour l'ordre normal** lorsque les écarts
   d'oscillation sont incorporés ;
5. **une dépendance majeure au modèle d'énergie noire et au prior de masse** ;
6. **une tension diagnostique** entre le maximum cosmologique sous `LambdaCDM` et le
   domaine physique imposé par N1.

### 8.2 Non-acquis

La voie n'établit pas de manière indépendante :

```text
une détection positive universelle de Sigma m_nu ;
une valeur modèle-indépendante de la somme ;
les trois masses individuelles ;
la nature Dirac ou Majorana ;
les phases de Majorana ;
l'origine des masses ;
un ordre des masses indépendant des priors d'oscillation ;
une masse négative physique ;
la cause de la tension entre LambdaCDM, BAO et CMB.
```

### 8.3 La borne n'est pas une mesure locale

L'énoncé :

```text
Sigma m_nu < 0.0642 eV à 95 % sous LambdaCDM, DESI DR2 BAO + CMB,
prior non négatif et trois masses dégénérées
```

est complet. L'énoncé abrégé :

```text
la cosmologie mesure la masse des neutrinos à 0.064 eV
```

est incorrect, car il supprime :

```text
le statut de borne ;
le modèle LambdaCDM ;
la combinaison de données ;
le prior ;
la paramétrisation du spectre ;
la frontière du posterior ;
la tension avec N1.
```

### 8.4 La tension est un résultat de réseau

Le fait qu'une construction donne une limite sous le plancher normal n'est pas un
résultat négatif à effacer. Il indique que le réseau :

```text
CMB + BAO + lentillage + LambdaCDM + priors
```

préfère une direction qui ne correspond pas exactement au secteur standard fourni
par les oscillations. La localisation de cette direction est une information sur le
modèle de passage, non une nouvelle propriété intrinsèque du neutrino.

## 9. Limites propres de l'accès

### 9.1 Dépendance au modèle cosmologique

La borne varie fortement lorsque changent :

```text
l'équation d'état de l'énergie noire ;
la courbure ;
la gravitation ;
l'histoire de recombinaison ;
les conditions initiales ;
N_eff et le secteur relativiste ;
les interactions ou la stabilité des neutrinos ;
la forme du spectre primordial.
```

La relaxation `LambdaCDM -> w_0w_aCDM` suffit dans l'analyse DESI à faire passer la
borne de `0.0642` à `0.163 eV`. Cette variation n'est pas une erreur statistique sur
un même résultat : elle définit un autre énoncé conditionnel.

### 9.2 Dépendance aux jeux de données

Le résultat dépend du choix exact de :

```text
likelihood Planck à hauts et bas multipoles ;
lentillage Planck et ACT ;
points BAO et covariance ;
forme complète ou BAO seulement ;
supernovae Pantheon+, Union3 ou DES Y5 ;
lentillage faible ou forêt Lyman-alpha ajoutés ;
priors BBN, n_s, tau ou H_0.
```

Une combinaison plus riche peut resserrer la borne, la détendre ou produire une
préférence positive selon les directions de dégénérescence qu'elle coupe.

### 9.3 Astrophysique et non-linéarité

Les bornes d'expansion CMB + BAO utilisent des observables relativement robustes,
mais les sondes de croissance ajoutent :

```text
biais des galaxies et des quasars ;
modèle d'occupation des halos ;
feedback baryonique ;
modèle de la forêt Lyman-alpha ;
redshifts photométriques et alignements intrinsèques pour le lentillage faible ;
non-linéarités et limites du modèle perturbatif.
```

La sensibilité accrue au libre parcours s'accompagne donc d'une architecture de
nuisance plus profonde.

### 9.4 Reproductibilité distribuée

À la coupure :

```text
les likelihoods BAO DR2 sont publiques ;
les chaînes MCMC et maxima a posteriori DESI DR2 sont publics ;
les likelihoods et produits ACT DR6 sont publics ;
les likelihoods Planck sont publiques ;
les spectres et redshifts complets sous-jacents à DR2 ne sont pas encore publiés ;
les choix internes, validations et simulations restent répartis entre plusieurs
articles et dépôts.
```

La borne peut être réanalysée substantiellement, mais sa reproduction depuis les
photons ou spectres bruts jusqu'au posterior final n'est pas entièrement disponible
dans un paquet unique.

### 9.5 La somme efface une partie du spectre

À sensibilité actuelle, l'effet cosmologique dépend principalement de la somme. Les
différences fines entre ordre normal et inversé sont petites et corrélées aux autres
paramètres. Une préférence d'ordre apparaît surtout lorsque les contraintes de N1
structurent le domaine des spectres admissibles.

## 10. Ponts vers les trois autres voies

### 10.1 Depuis les oscillations

N1 fournit :

```text
Delta m^2_21 ;
|Delta m^2_3l| ;
theta_12, theta_13 et autres paramètres de mélange ;
deux ordres admissibles.
```

Pour une masse minimale `m_l`, les écarts donnent :

```math
\Sigma m_\nu^{NO}(m_l)
\quad\text{ou}\quad
\Sigma m_\nu^{IO}(m_l).
```

Le pont permet :

```text
d'établir les planchers de somme ;
de traduire une borne cosmologique en borne sur m_l ;
de comparer les évidences des deux ordres.
```

Il ne permet pas de considérer la préférence cosmologique d'ordre comme indépendante
de N1.

### 10.2 Vers la cinématique bêta

Avec les paramètres de mélange de N1 :

```math
m_\beta^2=\sum_i |U_{ei}|^2m_i^2,
\qquad
\Sigma m_\nu=\sum_i m_i.
```

Une borne cosmologique proche du plancher normal implique une région très basse de
`m_beta`, hors de portée actuelle de KATRIN. Mais la conversion exige :

```text
trois états légers standard ;
ordre et masse minimale ;
histoire thermique standard pour la validité de la borne cosmologique ;
absence de composantes invisibles à l'une des deux voies.
```

KATRIN contrôle le spectre local sans dépendre de `LambdaCDM`. Un désaccord futur
pourrait donc viser le modèle cosmologique, le secteur neutrino ou une systématique,
plutôt que forcer une moyenne entre les deux nombres.

### 10.3 Vers la double bêta sans neutrino

Sous le mécanisme de Majorana léger :

```math
m_{\beta\beta}=\left|\sum_i U_{ei}^2m_i\right|.
```

Une borne très basse sur `Sigma m_nu` réduit l'enveloppe possible de `m_beta_beta`,
mais elle ne fixe pas :

```text
les phases de Majorana ;
la nature Majorana ;
les annulations cohérentes ;
le mécanisme de double bêta ;
les éléments de matrice nucléaire.
```

La tension cosmologique avec le plancher normal ne peut donc pas être transportée
comme exclusion directe d'une expérience de double bêta.

### 10.4 Tableau des ponts

| Quantité de départ | Relation ajoutée | Hypothèses nécessaires | Gain | Information toujours absente |
|---|---|---|---|---|
| `Delta m^2`, ordre | reconstruction `m_i(m_l)` puis somme | trois états actifs, masse minimale | planchers et borne sur `m_l` | masse locale sans modèle spectral |
| `Sigma m_nu` | définition de `m_beta` | PMNS, ordre, spectre standard | région cinématique prédite | likelihood KATRIN et effets non standard |
| `Sigma m_nu` | somme cohérente `m_beta_beta` | Majorana, phases, mécanisme, matrices nucléaires | enveloppes conditionnelles | taux de désintégration et phases |

## 11. Audit des sources et dettes restantes

### 11.1 Sources primaires et produits officiels

- [DESI Collaboration, contraintes neutrino DR2, PRD 112 (2025)](https://doi.org/10.1103/w9pk-xsk7) ;
- [DESI DR2 Results II, mesures BAO et cosmologie](https://doi.org/10.1103/tr6y-kpc6) ;
- [DESI DR2 Results I, BAO de la forêt Lyman-alpha](https://doi.org/10.1103/2wwn-xjm5) ;
- [documentation et chaînes DESI DR2](https://data.desi.lbl.gov/public/papers/y3/bao-cosmo-params/README.html) ;
- [likelihood BAO DR2 publique](https://github.com/CobayaSampler/bao_data/tree/master/desi_bao_dr2) ;
- [ACT DR6, carte de lentillage et paramètres cosmologiques](https://arxiv.org/abs/2304.05203) ;
- [ACT DR6, mitigation des avant-plans du lentillage](https://arxiv.org/abs/2304.05196) ;
- [produits officiels ACT DR6](https://act.princeton.edu/act-dr6-data-products) ;
- [Planck PR4 CamSpec](https://arxiv.org/abs/2205.10869) ;
- [Planck PR4 HiLLiPoP / LoLLiPoP et paramètres](https://arxiv.org/abs/2309.10034).

### 11.2 Analyses alternatives utilisées comme stress tests

- [DESI, analyse étendue de l'énergie noire DR2](https://arxiv.org/abs/2503.14743) ;
- [Nair et al., énergie noire à quatre paramètres](https://arxiv.org/abs/2512.08752) ;
- [Hou et al., conditions initiales d'isocourbure et priors d'ordre](https://arxiv.org/abs/2606.17994) ;
- [Du et al., préférence positive sous combinaison étendue](https://arxiv.org/abs/2507.16589) ;
- [Kıbrıs et al., masse effective négative et modèles d'énergie noire](https://arxiv.org/abs/2605.21456).

Ces analyses ne sont pas moyennées. Elles servent à identifier les dépendances qui
changent le statut du résultat.

### 11.3 Données et produits publics

```text
DESI DR2 : distances BAO, covariance, likelihoods, chaînes et résultats MAP publics ;
DESI DR1 : catalogues publics, spectres de puissance et chaînes de forme complète ;
Planck : cartes et likelihoods publiques selon releases ;
ACT DR6 : cartes, spectres de lentillage, likelihoods et chaînes publiques ;
produits manquants : catalogue spectroscopique complet DR2 à la coupure, covariance
                    permettant de combiner proprement forme complète DR1 et BAO DR2,
                    reproduction unifiée de toutes les validations internes.
```

### 11.4 Désaccords conservés

La fiche conserve comme résultats :

1. la différence entre la borne bayésienne à frontière et la construction
   Feldman–Cousins ;
2. la tension entre la région préférée sous `LambdaCDM` et les planchers de N1 ;
3. l'élargissement majeur de la borne sous énergie noire dynamique ;
4. la différence entre information d'expansion et information de libre parcours ;
5. les préférences d'ordre dépendantes de la paramétrisation et des priors ;
6. l'existence d'analyses étendues produisant soit des bornes détendues, soit une
   préférence de masse positive.

### 11.5 Dettes reportées à N5 ou à une reprise computationnelle

- lire directement les chaînes DESI DR2 et reproduire les quantiles `0.0642` et
  `0.163 eV` avec les conventions exactes de poids ;
- reconstruire les profils fréquentistes et le calcul Feldman–Cousins ;
- comparer les priors `Sigma m_nu >= 0`, plancher normal, plancher inversé et masse
  minimale uniforme dans une paramétrisation commune ;
- quantifier la part de la contrainte provenant de chaque likelihood CMB, du
  lentillage et des différents points BAO ;
- reproduire la contrainte de forme complète et isoler géométrie, amplitude et
  suppression dépendante de l'échelle ;
- mettre à jour les planchers et enveloppes avec NuFIT 6.1 et les résultats JUNO de
  N1 ;
- tester les mappings vers `m_beta` et `m_beta_beta` sans imposer silencieusement un
  ordre ou des phases ;
- surveiller la publication de la forme complète DESI DR2 et des données
  spectroscopiques DR2.

## 12. Effet sur la question du cycle

`N3` confirme que la cosmologie ne fournit pas une quatrième pesée du même objet. La
somme devient accessible par une reconstruction d'histoire :

```text
secteur relicte standard
+ expansion et transition thermique
+ libre parcours et croissance
+ CMB, lentillage et distances BAO
+ modèle LambdaCDM ou extension
+ likelihoods et priors
-> posterior ou profil de Sigma m_nu.
```

Le contraste avec les deux premières fiches est maintenant précis :

```text
N1 : relations différentielles et mélange sans ancrage absolu ;
N2 : ancrage quadratique électronique par cinématique locale ;
N3 : somme collective reconstruite dans une histoire cosmologique.
```

La borne la plus forte est aussi la plus dépendante d'une architecture globale. Ce
n'est pas une faiblesse qui annulerait le résultat : c'est sa condition de validité.

Le cycle cosmologique est ainsi confirmé dans sa lecture active :

```text
une grandeur cosmologique se qualifie par son rôle dans le modèle,
son effet physique, ses sondes, ses dépendances et son degré de reconstruction.
```

## 13. Verdict N3

```text
fonction du spectre contrainte : Sigma m_nu = somme_i m_i ;
traces primaires : spectres et redshifts de galaxies et quasars, anisotropies CMB,
                   reconstruction de lentillage et distributions de structure ;
observables publiées : distances BAO, spectres CMB et lentillage, multipoles de
                        puissance et likelihoods ;
modèle de passage : histoire thermique + Boltzmann + expansion + croissance +
                    réponses de sondes + nuisances + inférence ;
état directeur : Sigma m_nu < 0.0642 eV à 95 % sous LambdaCDM, DESI DR2 BAO + CMB,
                 avec posterior à la frontière ;
stress fréquentiste : Sigma m_nu < 0.053 eV, sous le plancher normal de N1 ;
modèle étendu : Sigma m_nu < 0.163 eV sous w_0w_aCDM ;
acquis : sensibilité collective très forte et tension localisée du réseau
         cosmologique standard ;
non-acquis : détection positive modèle-indépendante, masses individuelles, nature
             Majorana, origine des masses et ordre autonome ;
statut : fiche N3 close pour comparaison, sous dettes de reproduction des chaînes,
         d'analyse des priors et d'actualisation à la prochaine publication DESI.
```

La prochaine étape est `N4` : reconstruire l'accès par double bêta sans neutrino, en
partant de la demi-vie et du bruit de fond expérimentaux avant toute conversion vers
`m_beta_beta`, puis en séparant mécanisme de désintégration, nature Majorana, phases
et éléments de matrice nucléaire.
