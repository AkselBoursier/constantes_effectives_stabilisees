# N4 — Fiche d'accès par double bêta sans neutrino v0.1

## 0. Statut, périmètre et coupure

```text
statut : fiche scientifique active du cycle neutrino ;
étape : N4 du protocole commun des quatre accès ;
date : 17 juillet 2026 ;
date de coupure bibliographique : 17 juillet 2026 inclus ;
voie étudiée : recherches de double bêta sans neutrino dans plusieurs isotopes,
                avec KamLAND-Zen, LEGEND-200 et CUORE comme résultats directeurs ;
fonction : reconstruire la chaîne qui relie exposition isotopique, dépôt d'énergie,
           sélection, bruit de fond, limite de demi-vie et conversion conditionnelle
           vers la masse effective de Majorana m_beta_beta ;
ne vaut pas : détection du processus, mesure directe d'une masse, preuve qu'un
              échange de neutrinos légers domine, exclusion générale de la nature
              Majorana ou comparaison immédiate des demi-vies entre isotopes ;
révision : requise lorsqu'une nouvelle analyse officielle remplace l'un des résultats
           directeurs ou lorsqu'un calcul nucléaire modifie substantiellement les
           conversions retenues.
```

La fiche applique le [protocole N0](N0_Protocole_commun_fiches_acces_neutrinos_v0_1.md),
prolonge la [fiche N1 sur les oscillations](N1_Fiche_acces_oscillations_neutrinos_v0_1.md),
la [fiche N2 sur la cinématique bêta](N2_Fiche_acces_cinematique_beta_neutrinos_v0_1.md)
et la [fiche N3 sur la somme cosmologique](N3_Fiche_acces_cosmologie_somme_masses_neutrinos_v0_1.md).

Les résultats directeurs à la coupure sont :

- [KamLAND-Zen, *Search for Majorana Neutrinos with the Complete KamLAND-Zen Dataset*,
  Physical Review Letters 135, 262501 (2025)](https://doi.org/10.1103/jkf6-48j8) ;
- [LEGEND-200, *First Results on the Search for Lepton Number Violating
  Neutrinoless Double Beta Decay*, Physical Review Letters (2025)](https://doi.org/10.1103/25tk-nctn) ;
- [CUORE, *Constraints on Lepton Number Violation with the 2 tonne-year CUORE
  Dataset*, Science (2025)](https://doi.org/10.1126/science.adp6474).

Aucune de ces expériences ne rapporte une évidence de double bêta sans neutrino à
la coupure.

## 1. Objet ou fonction ciblée

### 1.1 Processus avec et sans neutrinos

La double désintégration bêta autorisée par le modèle standard transforme deux
neutrons en deux protons, deux électrons et deux antineutrinos :

```math
(A,Z)\rightarrow(A,Z+2)+2e^-+2\bar\nu_e.
```

La variante sans neutrino recherchée est :

```math
(A,Z)\rightarrow(A,Z+2)+2e^-.
```

Elle viole le nombre leptonique total de deux unités. Dans un détecteur qui contient
l'isotope source, sa signature calorimétrique idéale est un dépôt d'énergie au voisinage
de la valeur `Q_beta_beta`, car les deux électrons emportent presque toute l'énergie
disponible.

Le résultat expérimental primaire n'est toutefois ni `m_beta_beta` ni une masse propre.
C'est un taux ou une demi-vie propre à un isotope :

```math
T_{1/2}^{0\nu}(^{A}X).
```

### 1.2 Masse effective sous échange de neutrinos légers

Si le mécanisme dominant est l'échange de trois neutrinos légers de Majorana, la
combinaison leptoniqe pertinente est :

```math
m_{\beta\beta}
=
\left|\sum_i U_{ei}^{2}m_i\right|.
```

Contrairement à `m_beta`, cette somme est cohérente. Les phases contenues dans
`U_{ei}^2`, notamment les phases de Majorana, peuvent produire des renforcements ou
des annulations.

La relation entre demi-vie et masse prend alors la forme conventionnelle :

```math
\left[T_{1/2}^{0\nu}\right]^{-1}
=
G^{0\nu}(Q,Z)\,g_A^4\,|M^{0\nu}|^2
\left|\frac{m_{\beta\beta}}{m_e}\right|^2.
```

Elle ajoute au résultat expérimental :

```text
un facteur d'espace de phase G^0nu ;
un élément de matrice nucléaire M^0nu ;
une convention sur g_A ;
le mécanisme d'échange de neutrinos légers ;
la cohérence des phases de Majorana.
```

Une limite de demi-vie est donc un résultat expérimental plus primaire que la plage
convertie de `m_beta_beta`.

### 1.3 Ce qu'établirait une observation

Une observation confirmée du processus établirait une violation du nombre leptonique.
Dans le cadre général du théorème dit de la boîte noire, elle implique l'existence
d'un terme de masse de Majorana, même si le mécanisme microscopique dominant n'est
pas l'échange standard de neutrinos légers.

Elle n'établirait pas automatiquement :

```text
que le mécanisme léger domine le taux ;
que la valeur extraite par la formule standard est unique ;
que les contributions de courants droits, particules lourdes ou opérateurs courts
sont absentes ;
que les phases de Majorana peuvent être reconstruites depuis un isotope unique.
```

Le passage :

```text
détection -> m_beta_beta
```

reste donc conditionnel, même si la détection elle-même aurait une portée physique
majeure.

## 2. Production des traces : trois architectures expérimentales

### 2.1 Germanium enrichi : LEGEND-200

LEGEND-200 utilise des détecteurs semi-conducteurs en germanium enrichi en `^{76}Ge`.
Le matériau source est aussi le détecteur. Le signal attendu est un dépôt proche de :

```text
Q_beta_beta(76Ge) voisin de 2039 keV.
```

La chaîne minimale est :

```text
noyau de 76Ge dans le cristal
-> dépôt des deux électrons dans un ou plusieurs volumes
-> création de charges
-> forme et amplitude de l'impulsion
-> coupures de multiplicité et de forme d'impulsion
-> veto par scintillation de l'argon liquide
-> spectre à haute résolution autour de Q_beta_beta
-> vraisemblance de signal et de fond
-> limite sur T_1/2^0nu.
```

Les atouts principaux sont :

```text
excellente résolution énergétique ;
forte efficacité lorsque l'énergie reste dans un cristal ;
discrimination des événements multi-sites ;
indice de fond très bas ;
continuité avec GERDA et MAJORANA DEMONSTRATOR.
```

La première analyse LEGEND-200 porte sur `61 kg yr`. Plus de la moitié de l'exposition
provient des détecteurs les plus performants. Le résultat propre à LEGEND-200 donne :

```math
T_{1/2}^{0\nu}(^{76}\mathrm{Ge})>0.5\times10^{26}\ \mathrm{yr}
\qquad(90\ %\ CL).
```

La combinaison LEGEND-200 + GERDA + MAJORANA DEMONSTRATOR donne :

```math
T_{1/2}^{0\nu}(^{76}\mathrm{Ge})>1.9\times10^{26}\ \mathrm{yr}
\qquad(90\ %\ CL),
```

pour une sensibilité d'exclusion médiane de `2.8 x 10^26 yr`. Sous échange léger et
selon les éléments de matrice utilisés, la collaboration cite :

```math
m_{\beta\beta}<70-200\ \mathrm{meV}.
```

### 2.2 Xénon dissous dans un scintillateur : KamLAND-Zen

KamLAND-Zen dissout du xénon enrichi en `^{136}Xe` dans un scintillateur liquide contenu
dans un ballon interne. La signature idéale est un pic dans la somme d'énergie à :

```text
Q_beta_beta(136Xe) voisin de 2.458 MeV.
```

La chaîne est :

```text
désintégration dans le Xe-LS
-> scintillation des dépôts d'énergie
-> temps et charges des photomultiplicateurs
-> reconstruction de l'énergie et du vertex
-> volume fiduciel et coupures de coïncidence
-> veto des muons et produits de spallation
-> ajustement spectral et spatial des fonds
-> limite sur le nombre d'événements 0nu
-> limite sur T_1/2^0nu.
```

Le jeu KamLAND-Zen 800 complet contient `745 kg` de xénon enrichi et une exposition
de `2.097 tonne yr` de `^{136}Xe`, acquise du 5 février 2019 au 12 janvier 2024. Les
principaux contrôles portent notamment sur :

```text
radioactivité du ballon interne ;
produits de spallation du xénon ;
queue du spectre 2nu beta beta ;
réponse et stabilité des photomultiplicateurs ;
reconstruction du vertex ;
points chauds et volumes fiduciels ;
modèle spectral multi-composantes.
```

Combiné avec la phase KamLAND-Zen antérieure, le résultat donne :

```math
T_{1/2}^{0\nu}(^{136}\mathrm{Xe})>3.8\times10^{26}\ \mathrm{yr}
\qquad(90\ %\ CL).
```

Sous échange léger et avec un ensemble phénoménologique d'éléments de matrice, la
conversion citée est :

```math
m_{\beta\beta}<28-122\ \mathrm{meV}.
```

### 2.3 Bolomètres en tellurite : CUORE

CUORE utilise `988` cristaux de `TeO_2` refroidis à quelques millikelvins et recherche
le processus dans `^{130}Te`. L'isotope est contenu dans l'absorbeur calorimétrique.
Le signal idéal est un dépôt thermique au voisinage de `Q_beta_beta`.

La chaîne est :

```text
dépôt d'énergie dans un cristal de TeO2
-> élévation de température
-> impulsion du thermistor
-> stabilisation du gain et calibration
-> sélection de qualité et anti-coïncidence entre cristaux
-> spectre autour de Q_beta_beta
-> modèle de pic, lignes gamma et fond continu
-> posterior du taux 0nu
-> limite sur T_1/2^0nu.
```

Le résultat publié en 2025 utilise plus de `2 tonne yr` d'exposition en `TeO_2` et
cinq années d'exploitation stable d'un réseau proche de mille bolomètres. Il ne trouve
aucune évidence et donne :

```math
T_{1/2}^{0\nu}(^{130}\mathrm{Te})>3.5\times10^{25}\ \mathrm{yr}
\qquad(90\ %\ intervalle\ crédible).
```

L'exposition en masse de détecteur ne doit pas être confondue avec une exposition
isotopique directement comparable à celle de KamLAND-Zen ou LEGEND. Il faut tenir
compte de la fraction isotopique, de l'efficacité, de la résolution et du fond.

## 3. Observable publiée

### 3.1 Le signal publié est une composante spectrale

Les expériences publient typiquement :

```text
spectre en énergie ;
région de recherche autour de Q_beta_beta ;
exposition isotopique ou de détecteur ;
efficacité de sélection ;
résolution énergétique ;
indice ou modèle de fond ;
comptages observés ;
sensibilité attendue ;
limite observée sur le taux ou la demi-vie.
```

L'objet publié n'est pas une image directe des deux électrons dans toutes les
architectures. LEGEND et CUORE mesurent surtout un dépôt calorimétrique localisé ;
KamLAND-Zen reconstruit une énergie et un vertex dans un grand volume scintillant.
Les expériences de suivi pourraient ajouter des angles ou trajectoires, mais ce n'est
pas le régime directeur de cette fiche.

### 3.2 De l'événement au taux

Pour une exposition isotopique donnée, le nombre attendu d'événements est
schématiquement :

```math
\mu_{0\nu}
=
\ln 2\,
\frac{N_A}{W}
\frac{a\,M\,t\,\varepsilon}{T_{1/2}^{0\nu}},
```

avec :

```text
W : masse molaire de l'isotope ;
a : fraction isotopique ;
M t : exposition du matériau pertinent ;
epsilon : efficacité totale ;
T_1/2^0nu : demi-vie recherchée.
```

Cette relation est simple seulement en apparence. L'efficacité dépend de la
containment de l'énergie, des seuils, des coupures, de la multiplicité, du volume
fiduciel et des périodes de données.

### 3.3 Limite observée et sensibilité attendue

La limite observée fluctue avec les événements présents dans la région de recherche.
La sensibilité attendue décrit la distribution des limites qu'une procédure produirait
en l'absence de signal selon le modèle de fond.

LEGEND illustre directement la distinction :

```text
sensibilité médiane combinée : 2.8 x 10^26 yr ;
limite observée combinée :    1.9 x 10^26 yr.
```

Le résultat observé moins fort que la sensibilité ne constitue pas une indication de
signal tant que la vraisemblance et le test de découverte ne le soutiennent pas.

## 4. Modèle de mesure ou de passage

### 4.1 Modèle spectral

Pour chaque expérience, la vraisemblance compare les données à un modèle comprenant :

```text
pic 0nu beta beta à Q_beta_beta ;
forme et résolution du pic ;
efficacité dépendante de la période et du sous-détecteur ;
fonds continus ;
lignes gamma ou alpha ;
composantes cosmogéniques et de spallation ;
contraintes de calibration ;
incertitudes de forme et de normalisation.
```

Le modèle peut être un fit non borné dans une fenêtre étroite, un ajustement spectral
large ou une analyse combinant énergie, position et topologie.

### 4.2 Passage de la demi-vie à m_beta_beta

La conversion standard s'écrit :

```math
m_{\beta\beta}
=
\frac{m_e}
{g_A^2\,|M^{0\nu}|\,\sqrt{G^{0\nu}T_{1/2}^{0\nu}}}.
```

Elle montre pourquoi une demi-vie plus longue dans un isotope ne donne pas
nécessairement une meilleure borne universelle sur `m_beta_beta`. Les isotopes ont :

```text
facteurs d'espace de phase différents ;
éléments de matrice différents ;
valeurs Q différentes ;
architectures de bruit et de résolution différentes ;
incertitudes théoriques non identiques.
```

Une table classant uniquement les demi-vies ne classe donc pas directement les prises
sur la masse.

### 4.3 Éléments de matrice nucléaire

Les calculs mobilisent plusieurs méthodes :

```text
modèle en couches ;
quasi-particle random phase approximation ;
modèle des bosons en interaction ;
théorie de la fonctionnelle de densité ;
méthodes ab initio ;
opérateurs à courte portée issus de la théorie effective chirale.
```

Les écarts portent sur :

```text
corrélations nucléaires ;
espaces de modèle et troncatures ;
interactions effectives ;
traitement de g_A ;
opérateurs à un et deux corps ;
termes de courte portée ;
incertitudes et corrélations entre isotopes.
```

À la coupure, deux travaux ab initio de 2026 renforcent le besoin de traiter la
conversion comme une inférence théorique propre :

- [Todd et al., *Ab initio short-range nuclear matrix elements for neutrinoless
  double-beta decay*, arXiv:2604.22727](https://arxiv.org/abs/2604.22727) ;
- [Shickele et al., *Global Ab initio Neutrino Mass Limits from Neutrinoless
  Double-Beta Decay*, arXiv:2606.09288](https://arxiv.org/abs/2606.09288).

Le second combine plusieurs expériences et isotopes dans un cadre bayésien avec des
éléments de matrice ab initio. Il conclut que les expériences actuelles n'ont
probablement pas encore une couverture robuste du domaine autorisé par les
oscillations et que la combinaison multi-isotopes est physiquement informative.

### 4.4 Mécanismes concurrents

La formule en `m_beta_beta` suppose l'échange de neutrinos légers. D'autres mécanismes
peuvent générer le même changement de nombre leptonique :

```text
échange de particules lourdes ;
courants droits ;
opérateurs de contact ;
neutrinos stériles à différentes échelles ;
médiateurs scalaires ou supersymétriques selon les modèles.
```

Le taux peut alors contenir plusieurs amplitudes et interférences. Un isotope unique
et un spectre calorimétrique unique ne suffisent généralement pas à identifier le
mécanisme.

## 5. Incertitudes, corrélations et fonds

### 5.1 Fonds communs et spécifiques

Les fonds possibles comprennent :

```text
chaînes uranium et thorium ;
lignes gamma voisines ;
contamination de surface ;
radon ;
activation cosmogénique ;
muons et neutrons ;
produits de spallation ;
queue du spectre 2nu beta beta ;
événements multi-sites mal classés ;
instabilités de gain ou de reconstruction.
```

Leur poids varie fortement selon l'architecture.

### 5.2 Résolution énergétique

Une meilleure résolution réduit la quantité de fond intégrée dans la région de
recherche et sépare mieux un pic étroit de lignes voisines. Elle est particulièrement
forte pour le germanium et les bolomètres. KamLAND-Zen compense une résolution plus
large par une grande masse isotopique, une reconstruction spatiale et des modèles de
fond détaillés.

La résolution ne résume toutefois pas la sensibilité. Il faut aussi considérer :

```text
exposition ;
efficacité ;
indice de fond ;
volume fiduciel ;
capacité de veto ;
forme des fonds ;
stabilité temporelle ;
statistique de la région de recherche.
```

### 5.3 Corrélations internes

Les nuisances peuvent être corrélées entre périodes, détecteurs ou catégories :

```text
calibration énergétique ;
résolution ;
efficacité de sélection ;
activité isotopique ;
formes de fond ;
contamination commune ;
modèle de réponse ;
normalisation des composantes.
```

La combinaison de campagnes ne se réduit pas à additionner les expositions.

### 5.4 Corrélations entre expériences

Les événements de KamLAND-Zen, LEGEND et CUORE sont indépendants, mais leurs
conversions en masse partagent :

```text
le mécanisme léger supposé ;
les paramètres d'oscillation ;
les conventions de g_A ;
les méthodes nucléaires et leurs corrélations ;
les priors sur m_beta_beta ou les phases.
```

Une combinaison multi-isotopes doit donc séparer :

```text
likelihoods expérimentales indépendantes ;
incertitudes nucléaires partiellement corrélées ;
hypothèse de mécanisme commune.
```

## 6. Construction statistique

### 6.1 Fréquentiste et bayésien

Les résultats ne partagent pas tous la même construction. LEGEND et KamLAND-Zen
rapportent des limites à `90 % CL` selon leurs procédures de collaboration. CUORE
rapporte un intervalle crédible bayésien à `90 %`.

Ces nombres ne deviennent pas directement combinables parce qu'ils portent le même
pourcentage. Une combinaison exige les likelihoods ou une reconstruction fidèle de
leurs statistiques.

### 6.2 Paramètre physique borné

Le taux de signal est non négatif :

```math
\Gamma_{0\nu}\geq0.
```

Une fluctuation déficitaire peut produire une limite observée plus forte que la
sensibilité ; une fluctuation excédentaire peut l'affaiblir sans satisfaire un seuil
de découverte. La procédure près de la frontière doit être déclarée.

### 6.3 Régime de fond nul ou non nul

Dans un régime presque sans fond, la sensibilité en demi-vie croît approximativement
comme l'exposition :

```text
T_1/2 sensitivity proportionnelle à M t.
```

Lorsque le fond domine, elle croît plus lentement, approximativement comme :

```text
T_1/2 sensitivity proportionnelle à sqrt(M t / (B Delta E)).
```

Cette différence explique pourquoi un faible indice de fond et une excellente
résolution peuvent compenser une masse moindre.

### 6.4 Découverte et exclusion

Une limite de demi-vie est une exclusion. Une découverte demanderait :

```text
un excès local et global significatif ;
une stabilité entre sous-périodes et catégories ;
une incompatibilité avec les fonds connus ;
une énergie compatible avec Q_beta_beta ;
des contrôles instrumentaux et de calibration ;
idéalement une confirmation dans une autre architecture ou un autre isotope.
```

La confirmation multi-isotopes serait particulièrement forte, mais les taux ne
seraient comparables qu'après choix du mécanisme et calculs nucléaires.

## 7. État empirique daté à la coupure

| Énoncé | Isotope, exposition et architecture | Statut statistique | Résultat primaire | Conversion conditionnelle | Source |
|---|---|---|---|---|---|
| KamLAND-Zen ne trouve pas de signal dans le jeu complet Zen 800 combiné à la phase précédente | `^{136}Xe`, `745 kg`, `2.097 tonne yr` isotopiques, scintillateur chargé en xénon ; données février 2019–janvier 2024 | limite `90 % CL` | `T_1/2^0nu > 3.8 x 10^26 yr` | `m_beta_beta < 28–122 meV` sous échange léger et NME phénoménologiques | [PRL 135, 262501 (2025)](https://doi.org/10.1103/jkf6-48j8) |
| LEGEND-200 ne trouve pas de signal dans sa première exposition | `^{76}Ge`, `61 kg yr`, germanium source-détecteur dans argon liquide | limite `90 % CL` | LEGEND seul : `T_1/2^0nu > 0.5 x 10^26 yr` | non utilisée seule comme état directeur | [LEGEND-200](https://doi.org/10.1103/25tk-nctn) |
| La combinaison des expériences germanium améliore la limite mais fluctue sous sa sensibilité médiane | `^{76}Ge`, LEGEND-200 + GERDA + MAJORANA | limite observée `90 % CL`, sensibilité médiane `2.8 x 10^26 yr` | `T_1/2^0nu > 1.9 x 10^26 yr` | `m_beta_beta < 70–200 meV` sous échange léger | [arXiv:2505.10440](https://arxiv.org/abs/2505.10440) |
| CUORE ne trouve pas de signal avec le jeu de deux tonnes-années | `^{130}Te`, plus de `2 tonne yr` de `TeO_2`, bolomètres calorimétriques | limite bayésienne, intervalle crédible `90 %` | `T_1/2^0nu > 3.5 x 10^25 yr` | conversion dépendante du jeu de NME, non prise comme comparaison primaire | [Science 2025](https://doi.org/10.1126/science.adp6474) |
| EXO-200 fournit un contrôle historique de la même isotope que KamLAND-Zen avec une TPC au xénon liquide | `^{136}Xe`, `234.1 kg yr`, charge + scintillation et topologie mono/multi-site | limite `90 % CL` | `T_1/2^0nu > 3.5 x 10^25 yr` | ancienne conversion, non état directeur | [EXO-200](https://arxiv.org/abs/1906.02723) |

La plus grande limite de demi-vie à la coupure est celle de KamLAND-Zen sur `^{136}Xe`.
Cette phrase ne signifie pas qu'un isotope ou une expérience possède automatiquement
la meilleure sensibilité universelle à tout mécanisme ou à toute valeur de
`m_beta_beta`.

## 8. Résultat effectivement établi

### 8.1 Acquis expérimentaux

La voie établit à la coupure :

1. **aucune évidence confirmée de double bêta sans neutrino** dans les résultats
   directeurs ;
2. **des limites de demi-vie au-delà de `10^26 yr`** pour `^{136}Xe` et `^{76}Ge`
   combiné ;
3. **plusieurs architectures complémentaires** capables de contrôler des fonds et
   réponses très différents ;
4. **une forte sensibilité conditionnelle à `m_beta_beta`** sous échange léger ;
5. **une dépendance nucléaire dominante dans la conversion de la demi-vie vers la
   masse** ;
6. **l'intérêt scientifique d'une comparaison multi-isotopes**, qui teste à la fois
   expériences, éléments de matrice et mécanismes.

### 8.2 Non-acquis

La voie n'établit pas :

```text
que les neutrinos sont Dirac ;
que m_beta_beta est nul ;
une valeur positive de m_beta_beta ;
les phases de Majorana ;
la masse minimale ;
l'ordre des masses de manière autonome ;
le mécanisme dominant du processus ;
une exclusion robuste de tout le domaine inversé pour tous les calculs nucléaires ;
l'origine des masses ou de la violation du nombre leptonique.
```

### 8.3 Une non-détection ne tranche pas Dirac contre Majorana

Même si les neutrinos sont de Majorana, le taux peut être trop faible en raison de :

```text
masses faibles ;
annulations de phases ;
petit élément de matrice ;
sensibilité expérimentale insuffisante ;
mécanisme léger sous-dominant ;
interférences entre amplitudes.
```

L'absence de pic ne constitue donc pas une preuve de nature Dirac.

### 8.4 L'accès le plus conditionnel du cycle

Parmi les quatre fiches, `N4` possède la chaîne de conversion la plus longue :

```text
comptages et spectre
-> taux ou demi-vie isotopique
-> mécanisme de désintégration
-> calcul nucléaire
-> m_beta_beta
-> masses, mélange et phases.
```

Cette conditionnalité ne rend pas l'expérience faible. Elle localise les opérations
supplémentaires nécessaires pour attribuer une masse à partir d'un processus rare.

## 9. Limites propres de l'accès

### 9.1 Annulations de phases

Sous échange léger :

```math
m_{\beta\beta}=|c_{12}^2c_{13}^2m_1
+s_{12}^2c_{13}^2m_2e^{i\alpha_{21}}
+s_{13}^2m_3e^{i(\alpha_{31}-2\delta_{CP})}|.
```

Les modules de mélange et écarts de masses sont contraints par `N1`, mais les phases
de Majorana restent inconnues. Une somme faible peut donc coexister avec des masses
propres non nulles.

### 9.2 Mécanisme non identifiable par le taux seul

Un même taux peut être produit par des mécanismes différents. La seule énergie totale
des deux électrons ne fournit pas toujours assez d'information pour les distinguer.
Des observables supplémentaires peuvent aider :

```text
distribution angulaire ;
partage d'énergie entre électrons ;
transitions vers états excités ;
comparaison de plusieurs isotopes ;
recherche de processus corrélés ;
contraintes collider ou saveur.
```

Les expériences directrices de cette fiche sont principalement calorimétriques et
ne disposent pas toutes de ces informations événement par événement.

### 9.3 Incertitude nucléaire

La largeur des plages `m_beta_beta` citées par KamLAND-Zen et LEGEND est plus grande
que l'incertitude expérimentale sur la demi-vie convertie. Cette largeur ne doit pas
être ajoutée comme une simple erreur gaussienne : elle reflète des modèles, espaces et
opérateurs différents.

### 9.4 Comparabilité des isotopes

Comparer `^{76}Ge`, `^{130}Te` et `^{136}Xe` exige :

```text
le même mécanisme ;
les facteurs d'espace de phase correspondants ;
un ensemble cohérent de NME ;
une convention commune sur g_A ;
les likelihoods de demi-vie ;
les corrélations théoriques entre isotopes.
```

La phrase « KamLAND-Zen est deux fois plus sensible que LEGEND parce que sa demi-vie
est deux fois plus longue » est donc fausse.

### 9.5 Accès documentaire

Les articles fournissent spectres, efficacités, expositions et modèles détaillés,
mais aucune suite commune de likelihoods machine-lisibles ne permet encore de
reproduire uniformément toutes les limites et leur combinaison. Les données brutes,
les contrôles internes et les modèles complets restent distribués entre collaborations.

## 10. Ponts vers les trois autres voies

### 10.1 Depuis les oscillations

`N1` fournit :

```text
Delta m^2_21 ;
|Delta m^2_3l| ;
theta_12 et theta_13 ;
delta_CP selon convention ;
les ordres normal et inversé.
```

Il ne fournit pas :

```text
la masse minimale ;
les phases de Majorana ;
la nature Majorana ;
le mécanisme 0nu beta beta.
```

Avec une masse minimale et des phases choisies, `N1` permet de calculer des bandes de
`m_beta_beta`. Il ne transforme pas une limite de demi-vie en mesure sans calcul
nucléaire.

### 10.2 Vers la cinématique bêta

```math
m_\beta^2=\sum_i|U_{ei}|^2m_i^2,
\qquad
m_{\beta\beta}=\left|\sum_iU_{ei}^2m_i\right|.
```

`m_beta` ne dépend pas des phases de Majorana, alors que `m_beta_beta` y est sensible.
Une borne KATRIN élevée limite l'échelle globale mais ne prédit pas un taux unique.
Une future détection cinématique combinée à une non-détection très forte de `0nu` pourrait
contraindre les phases, la nature ou le mécanisme, mais pas par simple soustraction de
deux nombres.

### 10.3 Vers la cosmologie

```math
\Sigma m_\nu=\sum_i m_i.
```

Une borne cosmologique basse réduit l'enveloppe maximale de `m_beta_beta` sous trois
états standards, mais ajoute :

```text
le modèle cosmologique ;
l'histoire thermique ;
les priors de masse ;
l'ordre ou la marginalisation ;
la compatibilité avec N1.
```

La tension de `N3` avec le plancher normal ne peut pas être transportée directement
comme exclusion d'un signal `0nu`. Inversement, une détection `0nu` incompatible avec
les enveloppes cosmologiques pourrait signaler un mécanisme non standard, une histoire
cosmologique non standard ou un problème de conversion nucléaire.

### 10.4 Tableau des ponts

| Quantité de départ | Relation ajoutée | Hypothèses nécessaires | Gain | Information toujours absente |
|---|---|---|---|---|
| `Delta m^2`, PMNS | somme cohérente | masse minimale, phases Majorana, nature Majorana | bandes de `m_beta_beta` | taux nucléaire et mécanisme |
| `m_beta` | reconstruction du spectre puis somme cohérente | ordre, phases, trois états | enveloppe de masse absolue | phases et NME |
| `Sigma m_nu` | spectre puis somme cohérente | modèle cosmologique, ordre, phases | plafond conditionnel sur `m_beta_beta` | mécanisme et taux isotopique |
| `T_1/2^0nu` | formule de désintégration | mécanisme léger, `G^0nu`, `M^0nu`, `g_A` | borne sur `m_beta_beta` | masses individuelles et phases uniques |

## 11. Audit des sources et dettes restantes

### 11.1 Sources expérimentales primaires

- [KamLAND-Zen, jeu complet Zen 800, PRL 135, 262501 (2025)](https://doi.org/10.1103/jkf6-48j8) ;
- [version révisée de KamLAND-Zen, arXiv:2406.11438 v2](https://arxiv.org/abs/2406.11438) ;
- [LEGEND-200, première recherche, PRL (2025)](https://doi.org/10.1103/25tk-nctn) ;
- [version détaillée LEGEND-200, arXiv:2505.10440](https://arxiv.org/abs/2505.10440) ;
- [CUORE, jeu de deux tonnes-années, Science (2025)](https://doi.org/10.1126/science.adp6474) ;
- [version auteur CUORE, arXiv:2404.04453 v2](https://arxiv.org/abs/2404.04453) ;
- [EXO-200, jeu complet, arXiv:1906.02723](https://arxiv.org/abs/1906.02723).

### 11.2 Sources théoriques structurantes

- [Schechter et Valle, conséquence de type boîte noire, Physical Review D 25,
  2951 (1982)](https://doi.org/10.1103/PhysRevD.25.2951) ;
- [Todd et al., NME ab initio à courte portée, arXiv:2604.22727](https://arxiv.org/abs/2604.22727) ;
- [Shickele et al., limites globales ab initio, arXiv:2606.09288](https://arxiv.org/abs/2606.09288).

### 11.3 Désaccords conservés

La fiche conserve comme résultats :

1. la différence entre demi-vie isotopique et masse effective ;
2. l'étendue des conversions due aux NME ;
3. la différence entre limite observée et sensibilité attendue ;
4. la non-équivalence statistique des limites fréquentistes et bayésiennes ;
5. la possibilité de mécanismes concurrents ;
6. la nécessité d'une combinaison multi-isotopes pour tester les conversions ;
7. le fait que les calculs ab initio récents peuvent modifier le jugement sur la
   couverture du domaine inversé.

### 11.4 Dettes reportées à N5 ou à une reprise computationnelle

- extraire les likelihoods ou profils de taux disponibles pour KamLAND-Zen, LEGEND,
  CUORE et EXO-200 ;
- reconstruire les limites observées et sensibilités à partir des modèles publiés ;
- convertir les demi-vies avec un ensemble commun de facteurs de phase et de NME ;
- comparer séparément modèles phénoménologiques, méthodes ab initio et terme court ;
- construire une covariance théorique inter-isotopes au lieu de juxtaposer des plages ;
- mettre à jour les bandes `m_beta_beta` avec NuFIT 6.1 et les premiers résultats JUNO ;
- propager les bornes de `N2` et `N3` vers les mêmes variables spectrales ;
- tester l'effet des différentes priors sur la masse minimale et les phases ;
- distinguer combinaison sous mécanisme léger et tests de mécanismes concurrents ;
- vérifier la disponibilité de données machine-lisibles et documenter les absences.

## 12. Effet sur la question du cycle

`N4` confirme que la quatrième voie ne produit pas une quatrième masse directement
comparable. Elle procède en deux inférences de rang différent :

```text
architecture expérimentale
-> limite de demi-vie propre à un isotope ;

limite de demi-vie
+ mécanisme
+ physique nucléaire
-> borne conditionnelle sur m_beta_beta.
```

Le contraste entre les quatre accès est désormais complet :

```text
N1 : différences de masses au carré et mélange par propagation ;
N2 : moyenne quadratique électronique par cinématique locale ;
N3 : somme collective par reconstruction cosmologique ;
N4 : somme cohérente conditionnelle par un processus nucléaire non observé.
```

La pluralité des accès n'est pas une pluralité de lectures du même nombre. Elle révèle
quatre fonctions du spectre, quatre chaînes de médiation et quatre formes distinctes
d'incomplétude.

Le gain principal de `N4` est de séparer trois énoncés souvent compressés :

```text
aucun pic observé ;
une demi-vie isotopique est bornée ;
une masse effective est bornée sous mécanisme et NME déclarés.
```

## 13. Verdict N4

```text
fonction du spectre ciblée : m_beta_beta = |somme_i U_ei^2 m_i| sous échange léger ;
trace primaire : dépôts d'énergie près de Q_beta_beta, avec énergie, position,
                 multiplicité ou forme d'impulsion selon l'expérience ;
observable primaire : spectre, nombre de signaux admissibles et demi-vie isotopique ;
modèle de passage expérimental : exposition + efficacité + réponse + fonds + statistique ;
conversion supplémentaire : facteur de phase + NME + g_A + mécanisme ;
état directeur : aucune détection ; KamLAND-Zen T_1/2 > 3.8 x 10^26 yr pour 136Xe,
                 LEGEND combiné > 1.9 x 10^26 yr pour 76Ge,
                 CUORE > 3.5 x 10^25 yr pour 130Te ;
acquis : fortes limites multi-isotopes et prise conditionnelle sur la nature Majorana ;
non-acquis : valeur positive de m_beta_beta, phases, mécanisme, nature Dirac/Majorana
             tranchée par non-détection et couverture universelle de l'ordre inversé ;
statut : fiche N4 close pour comparaison, sous dettes de combinaison statistique,
         d'harmonisation nucléaire et de test des mécanismes.
```

La prochaine étape est `N5` : construire la matrice comparative des quatre accès,
leurs fonctions du spectre, leurs chaînes de preuve, leurs hypothèses de pont et les
incompatibilités qui ne peuvent être interprétées sans réviser un modèle ou une
conversion.
