# N2 — Fiche d'accès cinématique bêta à la masse effective des neutrinos v0.1

## 0. Statut, périmètre et coupure

```text
statut : fiche scientifique active du cycle neutrino ;
étape : N2 du protocole commun des quatre accès ;
date : 17 juillet 2026 ;
date de coupure bibliographique : 17 juillet 2026 inclus ;
voie étudiée : cinématique du spectre terminal de la désintégration bêta du
                tritium moléculaire, avec KATRIN comme résultat directeur ;
fonction : reconstruire la chaîne qui relie le partage d'énergie dans la
           désintégration, les électrons transmis, le modèle spectral et la
           borne sur la masse effective m_beta ;
ne vaut pas : détection positive d'une masse, détermination séparée de m_1,
              m_2 et m_3, mesure de Sigma m_nu, verdict Dirac ou Majorana,
              résultat indépendant de tout modèle de désintégration ou de
              réponse instrumentale ;
révision : requise lorsqu'une nouvelle analyse standard de masse KATRIN,
           fondée sur les campagnes postérieures à KNM5, devient publique.
```

La fiche applique le [protocole N0](N0_Protocole_commun_fiches_acces_neutrinos_v0_1.md)
et prolonge la [fiche N1 sur les oscillations](N1_Fiche_acces_oscillations_neutrinos_v0_1.md).
À la coupure, le résultat publié le plus récent sur la masse effective standard
reste l'analyse des cinq premières campagnes KATRIN, fondée sur 259 jours de
mesure entre avril 2019 et juin 2021 :

- [KATRIN, *Direct neutrino-mass measurement based on 259 days of KATRIN data*,
  Science 388 (2025)](https://doi.org/10.1126/science.adq9592) ;
- [version longue et données de méthode, arXiv:2406.13516](https://arxiv.org/html/2406.13516) ;
- [registre officiel des publications KATRIN](https://www.katrin.kit.edu/130.php).

Les publications ultérieures identifiées à la coupure portent notamment sur les
neutrinos stériles, les interactions générales, les calibrations de potentiel et
les futurs détecteurs. Elles ne remplacent pas encore ce résultat comme analyse
standard de `m_beta`.

## 1. Objet ou fonction ciblée

### 1.1 La grandeur cinématique

Dans une désintégration bêta, l'électron et l'antineutrino électronique se
partagent l'énergie disponible. Près du point terminal, une masse non nulle du
neutrino réduit l'espace de phase accessible et modifie la forme du spectre.

L'état électronique produit est une superposition des états propres de masse :

```math
|\bar\nu_e\rangle = \sum_i U_{ei}|\bar\nu_i\rangle.
```

Si les petites séparations entre les trois contributions terminales ne sont pas
résolues, la fonction cinématique accessible est :

```math
m_\beta^2 = \sum_i |U_{ei}|^2 m_i^2.
```

Cette somme est incohérente : les poids portent sur `|U_ei|^2` et les masses au
carré. Elle se distingue de :

```text
oscillations : Delta m^2_ij = m_i^2 - m_j^2 ;
cosmologie :   Sigma m_nu = somme_i m_i ;
double bêta :  m_beta_beta = |somme_i U_ei^2 m_i| sous mécanisme standard.
```

KATRIN emploie souvent le symbole `m_nu` pour cette grandeur. La présente fiche
utilise `m_beta` afin de maintenir la fonction du spectre visible.

### 1.2 Ce que signifie « direct »

L'accès est direct dans un sens borné : la masse intervient dans la cinématique
de la désintégration mesurée en laboratoire, sans recours à un modèle
cosmologique et sans dépendre du caractère Dirac ou Majorana du neutrino.

Il n'est pas sans modèle. Le passage du comptage à `m_beta` exige :

```text
théorie du spectre bêta
+ états finaux moléculaires
+ potentiel et réponse de la source
+ transmission du spectromètre
+ pertes d'énergie
+ modèle de fond
+ construction statistique.
```

La formule « mesure modèle-indépendante » doit donc être comprise comme
indépendance à l'égard de la cosmologie et de la nature Dirac/Majorana, non comme
absence de médiation théorique et instrumentale.

## 2. Production de la trace

### 2.1 Désintégration et source

KATRIN étudie la désintégration du tritium moléculaire :

```math
\mathrm{T_2}\rightarrow{}^3\mathrm{HeT^+}+e^-+\bar\nu_e.
```

Le point terminal effectif se situe près de `18,6 keV`. Une source gazeuse sans
fenêtre fournit une activité pouvant atteindre environ `100 GBq`. Les électrons
sont guidés adiabatiquement le long d'une ligne d'environ `70 m`, tandis que le
tritium est retiré par pompage différentiel et cryogénique avant la section de
spectrométrie.

La source n'est pas un simple réservoir d'événements. Sa densité de colonne, sa
pureté isotopique, sa température, son potentiel électrique, son champ
magnétique et les diffusions inélastiques déterminent la distribution d'énergie
qui atteint le spectromètre.

### 2.2 Filtre MAC-E et comptage intégral

Le spectromètre principal fonctionne comme filtre magnétique adiabatique à
collimation et filtrage électrostatique (MAC-E). Le champ magnétique transforme
une partie de l'énergie transverse en énergie longitudinale ; un potentiel de
retardation `qU` ne laisse passer que les électrons possédant une énergie
suffisante.

La largeur du filtre est de l'ordre de l'électronvolt. Les électrons transmis
sont comptés par un détecteur de plan focal à `148` pixels. Le détecteur ne mesure
pas individuellement avec la précision requise l'énergie terminale complète : la
grandeur première est le nombre d'électrons transmis pour une suite de potentiels
de retardation.

La chaîne minimale est :

```text
T2 dans la source
-> désintégration bêta et état final moléculaire
-> diffusion éventuelle dans la source
-> guidage magnétique
-> transmission ou rejet par le potentiel qU
-> comptage sur les pixels actifs
-> spectre intégral en fonction de qU
-> ajustement de m_beta^2, E0, amplitude et fond.
```

### 2.3 Campagnes et sélection

L'analyse publiée combine les cinq premières campagnes de mesure de masse
(`KNM1` à `KNM5`), prises entre avril 2019 et juin 2021. Elle comprend :

```text
259 jours de mesure ;
36 millions d'électrons dans la région d'analyse ;
une fenêtre principale de 40 eV sous le point terminal ;
des points au-dessus du terminal pour contraindre le fond ;
plusieurs configurations de source et de plan d'analyse ;
des scans d'environ trois heures avec temps optimisés par point.
```

Les scans ou pixels associés à des instabilités identifiées sont exclus selon des
critères fixés. Dans la configuration à plan d'analyse déplacé, les pixels sont
regroupés en anneaux afin de conserver les variations spatiales de potentiel et
de champ.

## 3. Observable publiée

### 3.1 Un spectre intégral, non le spectre différentiel brut

Pour chaque potentiel de retardation, KATRIN publie un comptage, un temps vivant,
une efficacité relative et les informations nécessaires à la modélisation. Le
spectre expérimental principal est donc :

```text
R_obs(qU) = taux d'électrons transmis au-dessus du seuil qU.
```

Il ne faut pas le confondre avec :

```text
l'énergie initiale de chaque électron ;
le spectre différentiel idéal d'une désintégration isolée ;
la masse manquante événement par événement ;
une lecture directe de m_beta.
```

### 3.2 Produit de données public

La collaboration publie deux fichiers structurés :

- [données spectrales `KATRIN_data_KNM1-5.json`](https://www.katrin.kit.edu/publikationen/KATRIN_data_KNM1-5.json) ;
- [entrées du modèle et systématiques `KATRIN_inputs_KNM1-5.json`](https://www.katrin.kit.edu/publikationen/KATRIN_inputs_KNM1-5.json).

Les données spectrales sont déjà agrégées par campagne, potentiel et groupe de
pixels. Elles ne constituent pas les événements bruts ni le code complet
d'acquisition. Elles rendent néanmoins possible une reconstruction substantielle
du spectre ajusté et des corrélations déclarées.

### 3.3 Point terminal et valeur Q

Le point terminal effectif `E_0` est un paramètre libre de l'ajustement. Son lien
avec la valeur `Q` exige des corrections pour :

```text
différences de fonction travail entre source, paroi arrière et spectromètre ;
recul de l'ion moléculaire ;
potentiel électrique de départ ;
calibration de l'échelle d'énergie.
```

L'analyse obtient, pour la campagne la plus stable utilisée à cette fin, une
valeur `Q` proche de `18 575,0 ± 0,3 eV`. Cette détermination constitue un contrôle
important, mais `E_0` n'est pas tenu fixe pour extraire `m_beta^2`.

## 4. Modèle de mesure ou de passage

### 4.1 Spectre différentiel moléculaire

Pour une énergie électronique `E`, une écriture schématique du spectre est :

```math
\frac{d\Gamma}{dE}
= C\,F(Z,E)\,p(E+m_e)
\sum_f P_f
\sum_i |U_{ei}|^2
\epsilon_f\sqrt{\epsilon_f^2-m_i^2}
\,\Theta(\epsilon_f-m_i),
```

avec :

```math
\epsilon_f = E_0-E-V_f.
```

`F(Z,E)` contient notamment la correction coulombienne, `P_f` et `V_f` décrivent
la probabilité et l'énergie d'un état final moléculaire. D'autres corrections
radiatives, nucléaires et de recul complètent le modèle.

Les états rotationnels, vibrationnels et électroniques de l'ion fils élargissent
irréductiblement le spectre moléculaire. Leur distribution n'est pas un fond
instrumental : elle appartient au processus physique mesuré. KATRIN utilise des
calculs *ab initio* et une évaluation améliorée de leurs incertitudes :

- [Schneidewind et al., *Improved treatment of the T2 molecular final-states
  uncertainties*, EPJC 84, 494 (2024)](https://doi.org/10.1140/epjc/s10052-024-12802-w).

### 4.2 Réponse intégrale

Le taux prédit à un potentiel `qU` s'écrit schématiquement :

```math
R(qU)
= A_s\int dE\,\frac{d\Gamma}{dE}
  f(E,qU;\xi)
+ R_{bg}(qU),
```

où `f` regroupe :

```text
transmission du MAC-E ;
angle d'acceptance ;
pertes d'énergie par diffusion dans T2 ;
densité de colonne et sections efficaces ;
champs et potentiels ;
efficacité de détection ;
répartition spatiale entre groupes de pixels.
```

Chaque campagne et chaque groupe de pixels pertinent reçoit son propre modèle de
réponse. Le paramètre `m_beta^2` est commun aux jeux de données ; le point terminal,
l'amplitude et le fond sont ajustés selon la segmentation déclarée.

### 4.3 Potentiel de la source

Les variations du potentiel dans le plasma de tritium déplacent l'énergie de
départ des électrons. Elles sont sondées par co-circulation de krypton métastable
et spectroscopie d'électrons de conversion :

- [KATRIN, *Measurement of the inhomogeneity of the tritium source electric
  potential*, EPJC 85, 757 (2025)](https://doi.org/10.1140/epjc/s10052-025-14354-z).

Cette médiation est particulièrement instructive : une largeur ou dérive de
potentiel peut imiter une modification du voisinage terminal et doit être
contrainte indépendamment de la donnée de masse.

## 5. Incertitudes, corrélations et paramètres de nuisance

### 5.1 Hiérarchie empirique à la coupure

L'incertitude totale de l'analyse des 259 jours reste dominée par la statistique.
Les contributions systématiques principales sont ensuite :

```text
densité de colonne et section efficace inélastique ;
fonction de perte d'énergie ;
fond dépendant de la durée des points de scan ;
variations du potentiel de la source ;
fond non poissonien ;
champs et potentiel du plan d'analyse.
```

Des contributions plus petites proviennent notamment de la distribution des états
finaux moléculaires, du tritium résiduel sur la paroi arrière, de l'efficacité du
détecteur, de la stabilité de la haute tension et des corrections théoriques.

### 5.2 Densité de colonne et pertes d'énergie

Un électron peut diffuser zéro, une ou plusieurs fois dans la source. La
probabilité de diffusion dépend de la densité de colonne et des sections efficaces.
La distribution des pertes déplace des électrons entre les régions du spectre
intégral.

Une source photoélectronique monoénergétique sert à calibrer ces paramètres. Une
divergence entre deux modes de mesure de la fonction de perte, identifiée après
l'installation d'une nouvelle source en 2022, a conduit à élargir fortement la
covariance associée dans l'analyse publiée. Cette décision augmente l'incertitude
systématique plutôt que de forcer une précision non justifiée.

### 5.3 Fond

Le fond résiduel comporte plusieurs composantes :

```text
électrons issus d'atomes excités dans le spectromètre ;
radon et radioactivité de surface ;
particules stockées dans un piège de Penning ;
tritium résiduel sur la paroi arrière ;
fond propre au détecteur.
```

Le déplacement du plan d'analyse réduit le fond d'environ un facteur deux. Le
taux n'est toutefois pas décrit par une constante universelle : il dépend de la
configuration, du temps passé au point de scan et de certaines structures
spatiales.

### 5.4 Corrélations

L'analyse combine `1609` points et inclut `144` paramètres systématiques
contraints. Les covariances relient notamment :

```text
paramètres communs à plusieurs campagnes ;
champs et potentiels des groupes de pixels ;
densité de colonne et fonction de perte ;
normalisation, point terminal et masse au carré ;
fond et durée des étapes de scan.
```

La masse n'est donc pas extraite en soustrayant une incertitude après le fit. Les
nuisances entrent dans la vraisemblance et sont partiellement informées par les
calibrations et par les données bêta elles-mêmes.

## 6. Construction statistique

### 6.1 Paramètre ajusté et domaine physique

L'ajustement porte sur `m_beta^2`, pas directement sur `m_beta`. Le modèle spectral
autorise temporairement des valeurs négatives de l'estimateur `m_beta^2` afin que
les fluctuations près de zéro ne soient pas tronquées dans le fit.

Une valeur ajustée négative ne correspond pas à une masse imaginaire. Elle indique
que la fluctuation du spectre se situe du côté opposé à la déformation produite
par une masse positive.

### 6.2 Vraisemblance combinée

Les campagnes à forts comptages utilisent une approximation normale ; les groupes
à comptages plus faibles dans la configuration déplacée utilisent une
vraisemblance de Poisson. Les contraintes de calibration entrent par des termes de
rappel (*pull terms*) multivariés.

Deux équipes d'analyse indépendantes réalisent le fit. Le calcul direct du modèle
est contrôlé par une approximation accélérée utilisant des réseaux de neurones
entraînés séparément pour chaque campagne ou groupe de pixels.

### 6.3 Aveuglement et corrections après ouverture

L'analyse est préparée sur des données simulées, puis aveuglée en modifiant d'une
quantité inconnue la variance de la distribution des états finaux moléculaires.
Après fixation de la procédure, la distribution réelle est rétablie.

Une erreur de combinaison dans la quatrième campagne a été découverte après une
première ouverture. La collaboration a alors :

```text
séparé KNM4 en deux périodes aux durées de scan différentes ;
révisé le fond dépendant du temps ;
réévalué la fonction de perte ;
corrigé l'évaluation de densité de colonne ;
documenté l'effet de chaque modification.
```

Ces corrections ont peu déplacé la valeur centrale par rapport à l'incertitude,
mais ont élargi les systématiques. Elles constituent une information positive sur
la chaîne de preuve et ne doivent pas être effacées d'une narration « mesure
 directe ».

### 6.4 Construction de l'intervalle

L'ajustement combiné donne :

```math
m_\beta^2 = -0.14^{+0.13}_{-0.15}\ \mathrm{eV}^2.
```

La construction principale de Lokhov–Tkachov fixe, pour une fluctuation négative,
la limite supérieure à la sensibilité expérimentale plutôt que de produire une
borne artificiellement plus stricte. Le résultat publié est :

```math
m_\beta < 0.45\ \mathrm{eV}
\qquad (90\ \%\ \mathrm{CL}).
```

À titre de contrôle, la construction de Feldman–Cousins appliquée au même
estimateur négatif donnerait environ `0,31 eV` à `90 % CL`. Les deux nombres ne
sont pas deux résultats physiques indépendants : ils montrent que la borne dépend
de la règle de couverture adoptée près de la frontière `m_beta^2 = 0`.

## 7. État empirique daté à la coupure

| Énoncé | Données ou exposition | Modèle et hypothèses | Statut statistique | Date des données | Source |
|---|---|---|---|---|---|
| KATRIN obtient `m_beta^2 = -0.14^{+0.13}_{-0.15} eV^2` | 36 millions d'électrons, 259 jours, cinq premières campagnes | spectre de T2, états finaux moléculaires, réponse MAC-E, masse unique effective non résolue | estimateur compatible avec zéro ; aucune détection | avril 2019–juin 2021 | [Science 388 (2025)](https://doi.org/10.1126/science.adq9592) |
| KATRIN fixe `m_beta < 0.45 eV` | mêmes données | construction Lokhov–Tkachov à frontière physique | borne supérieure, `90 % CL` | avril 2019–juin 2021 | [analyse longue](https://arxiv.org/html/2406.13516) |
| La construction Feldman–Cousins fournit une borne plus serrée, environ `0.31 eV` | mêmes données | même vraisemblance, règle d'intervalle différente | contrôle méthodologique ; non résultat directeur | avril 2019–juin 2021 | [analyse longue](https://arxiv.org/html/2406.13516) |
| Project 8 démontre une mesure du spectre bêta par rayonnement cyclotron | petit volume de tritium moléculaire, analyse de phase II | spectroscopie CRES, calibration krypton, analyses bayésienne et fréquentiste | preuve de principe ; limites `155 eV` et `152 eV`, non compétitives | données antérieures à 2023 | [PRL 131, 102502 (2023)](https://doi.org/10.1103/PhysRevLett.131.102502) |

La page officielle des publications KATRIN ne recense, au 17 juillet 2026, aucune
analyse standard postérieure remplaçant la limite des 259 jours. Les annonces de
sensibilité finale meilleure que `0,3 eV` et le corpus d'environ `1000` jours sont
des objectifs ou données en cours d'analyse, non un résultat de masse publié.

## 8. Résultat effectivement établi

### 8.1 Acquis

La cinématique bêta établit à la coupure :

1. une prise expérimentale locale sur la fonction `m_beta^2` ;
2. une borne de laboratoire indépendante du modèle cosmologique ;
3. une borne indépendante du caractère Dirac ou Majorana ;
4. la compatibilité du spectre KATRIN avec une masse effective inférieure à
   `0,45 eV` selon la construction principale ;
5. la faisabilité d'une publication partielle des données, réponses et
   covariances ;
6. le rôle décisif des états moléculaires, de la réponse et de la statistique dans
   une mesure dite directe.

### 8.2 Non-acquis

La voie n'établit pas :

```text
une masse positive détectée ;
la valeur de m_beta ;
les trois masses propres séparées ;
l'ordre normal ou inversé ;
Sigma m_nu ;
m_beta_beta ;
la nature Dirac ou Majorana ;
l'origine de la petitesse des masses.
```

### 8.3 La borne ne mesure pas zéro

L'énoncé :

```text
m_beta < 0.45 eV à 90 % CL
```

ne signifie ni `m_beta = 0`, ni probabilité de `90 %` que la masse soit sous la
borne. Il décrit la couverture d'une procédure fréquentiste appliquée à un
estimateur compatible avec la frontière physique.

## 9. Limites propres de l'accès

### 9.1 Combinaison non résolue

KATRIN ne résout pas les trois points terminaux séparés par les écarts de masses au
carré connus. Il contraint l'approximation effective `m_beta`. Une future résolution
beaucoup plus fine pourrait exiger un modèle explicite des trois contributions,
mais ce n'est pas le régime de la borne actuelle.

### 9.2 États moléculaires

Le tritium moléculaire fournit une source intense et contrôlable, mais l'excitation
de l'ion fils élargit le spectre. Cette largeur est un plancher systématique pour
les futures sensibilités. Le programme Project 8 vise notamment une source de
tritium atomique pour retirer cette médiation moléculaire ; ce projet reste en
phase de développement à la coupure.

### 9.3 Dépendances théoriques résiduelles

L'accès évite la cosmologie mais dépend encore :

```text
du cadre standard de désintégration bêta ;
de l'unitarité et de la définition de m_beta ;
des corrections électrofaibles et radiatives ;
du modèle moléculaire ;
de l'absence de composantes spectrales nouvelles non incluses.
```

Les recherches KATRIN sur les neutrinos stériles ou les interactions générales
montrent que le même spectre peut tester d'autres hypothèses. Une limite standard
de `m_beta` reste donc conditionnelle au modèle spectral standard déclaré.

### 9.4 Limites documentaires et reproductibilité

Les fichiers publics permettent de reproduire une part importante de l'analyse,
mais pas nécessairement :

```text
les événements bruts ;
la totalité des contrôles de qualité ;
les codes internes complets ;
chaque calibration intermédiaire ;
la procédure institutionnelle de validation.
```

La reproductibilité est substantielle mais distribuée entre données, articles de
méthode, calibrations, simulations et savoir-faire de collaboration.

## 10. Ponts vers les trois autres voies

### 10.1 Depuis les oscillations

Les oscillations fournissent :

```text
Delta m^2_21 ;
|Delta m^2_3l| ;
theta_12 et theta_13 ;
une hypothèse possible d'ordre.
```

Avec une masse minimale choisie, ces données déterminent une prédiction de
`m_beta`. Inversement, une borne KATRIN retranche une région de la masse minimale.
Elle ne sélectionne pas l'ordre à la sensibilité actuelle.

### 10.2 Vers la cosmologie

Pour un spectre `m_i` compatible avec les oscillations :

```math
m_\beta^2=\sum_i |U_{ei}|^2m_i^2,
\qquad
\Sigma m_\nu=\sum_i m_i.
```

Le passage de `m_beta` à `Sigma m_nu` exige :

```text
paramètres de mélange ;
écarts de masses ;
ordre ou marginalisation ;
masse minimale ;
absence d'états additionnels pertinents.
```

La borne de laboratoire peut contrôler une analyse cosmologique sans en partager
le modèle de structure ou les priors. À la sensibilité actuelle, elle est beaucoup
moins serrée que les bornes cosmologiques standard, mais plus locale et moins
dépendante du modèle cosmologique.

### 10.3 Vers la double bêta sans neutrino

`m_beta` est une somme incohérente, alors que `m_beta_beta` est une somme cohérente
sous hypothèse Majorana. Une borne sur `m_beta` limite l'échelle globale possible,
mais ne fixe pas les annulations dues aux phases :

```math
m_{\beta\beta}=\left|\sum_i U_{ei}^2m_i\right|.
```

Il faut ajouter :

```text
nature Majorana ;
phases de Majorana ;
mécanisme de désintégration ;
éléments de matrice nucléaire.
```

### 10.4 Tableau des ponts

| Quantité de départ | Relation ajoutée | Hypothèses nécessaires | Gain | Information toujours absente |
|---|---|---|---|---|
| `m_beta`, PMNS, `Delta m^2` | reconstruction du spectre | ordre, masse minimale | borne sur l'ancrage absolu | masses individuelles uniques |
| `m_beta` | somme des masses | trois états légers, ordre, mélange | région possible de `Sigma m_nu` | vraisemblance cosmologique |
| `m_beta` | somme cohérente | Majorana, phases, mécanisme | enveloppe maximale de `m_beta_beta` | phases et taux nucléaire |

## 11. Audit des sources et dettes restantes

### 11.1 Sources primaires et de méthode

- [KATRIN, *Direct neutrino-mass measurement based on 259 days of KATRIN data*,
  Science 388, 180–185 (2025)](https://doi.org/10.1126/science.adq9592) ;
- [version détaillée et supplément intégrés, arXiv:2406.13516](https://arxiv.org/html/2406.13516) ;
- [données spectrales publiques](https://www.katrin.kit.edu/publikationen/KATRIN_data_KNM1-5.json) ;
- [paramètres et covariances publics](https://www.katrin.kit.edu/publikationen/KATRIN_inputs_KNM1-5.json) ;
- [Schneidewind et al., états finaux moléculaires, EPJC 84 (2024)](https://doi.org/10.1140/epjc/s10052-024-12802-w) ;
- [KATRIN, inhomogénéité du potentiel de source, EPJC 85 (2025)](https://doi.org/10.1140/epjc/s10052-025-14354-z) ;
- [Project 8, première limite par spectroscopie cyclotron, PRL 131 (2023)](https://doi.org/10.1103/PhysRevLett.131.102502).

### 11.2 Contrôles kématiques hors périmètre central

Les mesures calorimétriques de capture électronique de `163Ho` par HOLMES et ECHo
contraignent également une masse électronique effective sous une chaîne d'accès
différente. Elles ne sont pas intégrées à la table centrale parce que `N2` porte
sur la désintégration bêta. Elles seront utiles à `N5` pour vérifier que
« cinématique locale » ne désigne pas une architecture instrumentale unique :

- [HOLMES, borne calorimétrique `m_nu < 27 eV` à `90 %` de crédibilité,
  arXiv:2503.19920](https://arxiv.org/abs/2503.19920) ;
- [ECHo-1k, borne `m_nu < 15 eV` à `90 %` de crédibilité,
  arXiv:2509.03423](https://arxiv.org/abs/2509.03423).

### 11.3 Dettes reportées à N5 ou à une reprise computationnelle

- reproduire numériquement le profil de vraisemblance KATRIN depuis les deux
  fichiers publics ;
- vérifier la concordance exacte entre calcul direct et approximation par réseau
  neuronal ;
- reconstruire le budget numérique complet de `m_beta^2` à partir de la table des
  systématiques ;
- comparer proprement Lokhov–Tkachov, Feldman–Cousins et plusieurs priors bayésiens
  sans mélanger couverture et crédibilité ;
- intégrer la future analyse du corpus proche de `1000` jours lorsqu'elle sera
  publiée ;
- tester quantitativement les enveloppes `m_beta` prédites à partir de N1 sous
  ordre normal et inversé.

## 12. Effet sur la question du cycle

`N2` confirme que la masse absolue n'est pas livrée comme nombre propre à chaque
état. Elle devient accessible sous une fonction déterminée :

```text
spectre terminal moléculaire
+ mélange électronique
+ réponse intégrale
+ calibrations
+ nuisance et frontière statistique
-> borne sur m_beta.
```

Le mot « local » ne signifie donc pas absence de reconstruction. Il indique que le
signal dépend d'une cinématique de laboratoire et non de l'histoire cosmologique.

La comparaison avec `N1` produit un contraste précis :

```text
N1 : relations et phases de propagation sans ancrage commun ;
N2 : ancrage quadratique électronique sans résolution des trois masses.
```

Les deux voies portent sur le même spectre, mais elles ne complètent leurs
informations qu'au moyen du modèle à trois masses et de la matrice PMNS.

## 13. Verdict N2

```text
fonction du spectre contrainte : m_beta^2 = somme_i |U_ei|^2 m_i^2 ;
trace primaire : comptages d'électrons transmis selon le potentiel de retardation ;
modèle de passage : spectre moléculaire + réponse MAC-E + pertes + fond + statistique ;
état empirique : m_beta^2 compatible avec zéro et m_beta < 0.45 eV à 90 % CL ;
acquis : meilleure borne cinématique directe de laboratoire à la coupure ;
non-acquis : détection positive, masses individuelles, ordre, nature Majorana,
             somme cosmologique et origine des masses ;
statut : fiche N2 close pour comparaison, sous dette de reproduction numérique
         et attente de l'analyse KATRIN postérieure aux 259 jours.
```

La prochaine étape est `N3` : reconstruire l'accès cosmologique à `Sigma m_nu`,
en distinguant l'effet physique des neutrinos massifs, les sondes et produits de
données, le modèle cosmologique, les priors et la construction de la borne.