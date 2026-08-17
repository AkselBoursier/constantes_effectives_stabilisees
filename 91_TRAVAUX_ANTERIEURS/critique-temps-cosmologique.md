# Au-delà du temps cosmologique lisse : Pour une temporalité cosmologique située

**Aksel [Nom]**

*Version de travail - Novembre 2025*

---

## Résumé

La cosmologie standard repose sur un présupposé rarement questionné : le temps cosmologique *t* des équations de Friedmann-Lemaître-Robertson-Walker constituerait une structure lisse, universellement accessible, permettant une description déterministe de l'évolution de l'univers. Cet article examine de manière critique ce présupposé à travers l'analyse d'un cas récent : les modèles de collapse spontané proposés pour résoudre l'incompatibilité apparente entre mécanique quantique et relativité générale. Nous montrons que ces modèles, en supposant un "temps cosmologique universel" dans lequel les collapses se produisent "spontanément à intervalles réguliers", commettent une erreur fondamentale : ils confondent la commodité mathématique du temps cosmologique avec son accessibilité ontologique. Notre critique va au-delà des objections habituelles (non-localité, violation de la covariance) pour pointer vers une confusion plus profonde : la caractérisation même de la relativité générale comme "déterministe et lisse" repose sur la fiction d'un temps cosmologique directement accessible, alors qu'en réalité seuls des temps propres situés sont observables. Nous proposons un cadre alternatif reconnaissant l'hétérogénéité irréductible des temporalités cosmologiques et esquissons une approche où le temps cosmique émerge dynamiquement des configurations observationnelles plutôt que d'être supposé préexistant.

**Mots-clés :** temps cosmologique, cosmologie située, modèles de collapse spontané, temporalité relationnelle, observation cosmologique

---

## 1. Introduction : Le mythe du temps cosmologique lisse

Les équations de Friedmann-Lemaître-Robertson-Walker (FLRW) qui gouvernent la cosmologie standard utilisent un temps cosmologique *t* comme coordonnée fondamentale :

$$\frac{\dot{a}^2}{a^2} + \frac{kc^2}{a^2} = \frac{8\pi G}{3}\rho + \frac{\Lambda c^2}{3}$$

$$\frac{\ddot{a}}{a} = -\frac{4\pi G}{3}\left(\rho + \frac{3p}{c^2}\right) + \frac{\Lambda c^2}{3}$$

où *a(t)* est le facteur d'échelle et les dérivées temporelles sont prises par rapport à ce temps cosmologique *t*.

Cette coordonnée temporelle est généralement traitée comme une structure lisse, universellement accessible, permettant de décrire l'évolution de l'univers de manière déterministe et prédictible. La cosmologie standard suppose ainsi qu'il existe un "maintenant cosmologique" bien défini, une hypersurface de simultanéité s'étendant à travers tout l'univers observable.

### 1.1 Ce que cachent les équations

Cependant, ce temps cosmologique *t* n'est jamais mesuré directement. Les observations cosmologiques reposent toujours sur :

- **Des temps propres τ** mesurés par des observateurs situés le long de trajectoires spécifiques
- **Des redshifts z** reconstruits à partir de décalages spectraux observés
- **Des distances** inférées via des chandelles standards (supernovae Ia) ou des règles standards (oscillations acoustiques baryoniques)

La relation entre le redshift observé *z* et le temps cosmologique *t* n'est pas une mesure directe mais une reconstruction via l'intégration :

$$1 + z = \frac{a(t_0)}{a(t_e)} = \frac{1}{a(t_e)}$$

où *t₀* est le temps cosmologique "aujourd'hui" et *tₑ* le temps cosmologique d'émission. Pour obtenir *t* à partir de *z*, il faut intégrer :

$$t(z) = t_0 - \int_0^z \frac{dz'}{(1+z')H(z')}$$

Cette intégration **suppose déjà** la validité du cadre FLRW et l'existence d'un temps cosmologique lisse sous-jacent. Le temps cosmologique est donc une **reconstruction épistémique**, non une donnée ontologique brute accessible à l'observation.

### 1.2 Le présupposé déterministe

La physique standard oppose couramment deux théories fondamentales :

- **La mécanique quantique** : probabiliste, indéterministe, où les systèmes existent dans des superpositions d'états jusqu'à ce qu'une mesure les "effondre" dans un état défini
- **La relativité générale** : déterministe, où la géométrie de l'espace-temps évolue de manière lisse et prévisible selon les équations d'Einstein

Cette dichotomie structure de nombreuses tentatives de réconciliation entre MQ et RG, notamment les modèles récents de "collapse spontané" de la fonction d'onde qui prétendent résoudre l'incompatibilité en faisant "choisir" spontanément un état au système quantique.

**Mais cette caractérisation de la RG comme "déterministe et lisse" repose entièrement sur le présupposé d'un temps cosmologique accessible.** Si ce temps n'est qu'une reconstruction située, alors la RG cosmologique n'est pas "lisse" au sens épistémologique - elle a sa propre forme d'opacité temporelle.

C'est précisément ce présupposé que nous allons interroger.

---

## 2. Cas d'étude : L'épicycle de Carlesso et al.

### 2.1 Le modèle de collapse spontané appliqué à l'univers

Dans un article récent publié dans le *Journal of High Energy Physics* (février 2024), Carlesso, Gaona-Reyes, Menéndez-Pidal et Faizal proposent d'appliquer les modèles de collapse spontané de la fonction d'onde à l'échelle cosmologique pour expliquer "l'émergence de la classicalité de l'univers."

Leur argument procède ainsi :

1. Si la mécanique quantique est universelle, l'univers entier peut être dans une superposition quantique d'états, chacun correspondant à une géométrie d'espace-temps différente :

$$|\Psi_{\text{univers}}\rangle = \sum_{\lambda} c_\lambda |\Psi_\lambda\rangle$$

où chaque $|\Psi_\lambda\rangle$ représente une géométrie distincte.

2. La décohérence, qui repose sur l'interaction avec un environnement externe, ne peut expliquer l'émergence de la classicalité pour l'univers dans son ensemble (puisqu'il n'y a pas d'environnement "externe" à l'univers).

3. Les modèles de collapse spontané modifient l'équation de Schrödinger en ajoutant des termes stochastiques et non-linéaires qui induisent un collapse spontané :

$$d|\psi\rangle = -\frac{i}{\hbar}\hat{H}dt|\psi\rangle - \frac{1}{2}\sum_n \gamma_n (\hat{A}_n - \langle\hat{A}_n\rangle)^2 dt|\psi\rangle + \sum_n \sqrt{\gamma_n}(\hat{A}_n - \langle\hat{A}_n\rangle)dW_n|\psi\rangle$$

où $\gamma_n$ sont des taux de collapse et $dW_n$ sont des processus de Wiener (bruit blanc).

4. Appliqué à l'univers, ce mécanisme ferait "choisir" spontanément une géométrie classique unique parmi la superposition quantique initiale.

### 2.2 Le présupposé du "temps cosmologique universel"

L'article de Carlesso et al. affirme que leur modèle permet au collapse de se produire "spontanément à intervalles réguliers" selon une "variable d'horloge bien définie" (*well-defined clock variable*). Ils écrivent :

> "Any system localizes spontaneously in a particular state [...] Instead of having a cat being dead and alive, one finds it dead or alive. This same logic applies to the universe."

Cette transposition du paradoxe du chat de Schrödinger à l'univers entier révèle le présupposé fondamental : il existerait un temps cosmologique universel dans lequel ces collapses spontanés "se produisent" de manière déterministe (même si les résultats sont stochastiques).

**Les présupposés non questionnés :**

1. **Un référentiel temporel privilégié** : Pour que les collapses se produisent "à intervalles réguliers", il faut définir par rapport à quelle horloge ces intervalles sont mesurés. Dans la littérature sur les modèles de collapse relativistes, ce référentiel est souvent explicitement identifié au référentiel comobile du fond diffus cosmologique (CMB).

2. **La coïncidence entre temps propre et temps cosmologique** : Le modèle suppose implicitement que le temps propre des observateurs (terrestres, dans ce cas) coïncide avec le temps cosmologique dans lequel les collapses se produisent.

3. **Une simultanéité cosmique absolue** : Pour que "l'univers" collapse vers une géométrie unique, il faut une notion de simultanéité cosmique - un "maintenant universel" où le collapse se produit partout à la fois.

### 2.3 La confusion entre commodité mathématique et accessibilité ontologique

Le cœur du problème est que Carlesso et al. traitent le temps cosmologique *t* des équations FLRW comme s'il était une structure ontologique accessible, alors qu'il n'est qu'une coordonnée conventionnelle rendue possible par les symétries cosmologiques.

**Ce que font implicitement ces modèles :**

- Ils utilisent le temps cosmologique *t* comme paramètre dans lequel les collapses stochastiques se produisent
- Ils supposent que ce temps *t* est "lisse" et universellement défini
- Ils considèrent que les "intervalles réguliers" ont un sens absolu dans ce temps cosmologique

**Ce qui est problématique :**

Aucun observateur ne mesure jamais directement *t*. Les observateurs mesurent :
- Leur **temps propre** τ le long de leur trajectoire
- Des **redshifts** z d'objets cosmologiques
- Des **durées propres** (taux de désintégration, oscillations atomiques, etc.)

Le temps cosmologique *t* est reconstruit à partir de ces mesures situées en supposant la validité du cadre FLRW. Il n'est pas "donné" mais **assemblé** à partir d'observations multiples et d'hypothèses théoriques (homogénéité, isotropie).

### 2.4 Pourquoi c'est un "épicycle"

Qualifier ce modèle d'"épicycle" (au sens historique des épicycles ptoléméens) signifie qu'il ajoute une complexité technique (termes stochastiques dans l'équation de Schrödinger) pour "sauver les apparences" - ici, pour maintenir la cohérence entre mécanique quantique et relativité générale - sans questionner les présupposés conceptuels qui génèrent le problème.

**L'épicycle consiste à :**
1. Accepter sans critique la dichotomie MQ "probabiliste" vs RG "déterministe"
2. Ajouter un mécanisme ad hoc (collapse spontané) pour réconcilier ces deux descriptions
3. Supposer un temps cosmologique universel non-problématique dans lequel ce mécanisme opère

**Ce qui n'est pas questionné :**
- L'idée que la RG cosmologique serait "déterministe et lisse" (nous allons contester cela)
- La nature du temps cosmologique lui-même comme structure accessible
- La possibilité même de parler de "collapse maintenant à travers tout l'univers"

Nous allons maintenant développer une critique plus radicale : non seulement ces modèles supposent à tort un temps cosmologique accessible, mais la caractérisation même de la RG comme ayant un temps "lisse" repose sur une confusion entre formalisme mathématique et réalité épistémologique.

---

## 3. L'hétérogénéité irréductible des temporalités cosmologiques

### 3.1 Trois niveaux de temporalité

La confusion conceptuelle autour du temps cosmologique provient d'un amalgame entre trois niveaux distincts de temporalité :

#### 3.1.1 Le temps propre τ : ce qui est réellement mesuré

Le temps propre est ce que mesure effectivement toute horloge physique suivant une trajectoire donnée. En relativité générale, le temps propre le long d'une trajectoire γ entre deux événements est défini par :

$$\tau = \int_\gamma \sqrt{-g_{\mu\nu} dx^\mu dx^\nu}$$

**Caractéristiques du temps propre :**
- C'est une observable **directement accessible** à l'observateur situé
- Il dépend de la **trajectoire spécifique** de l'observateur dans l'espace-temps  
- Il n'y a **pas de relation simple** entre les temps propres de deux observateurs avec des trajectoires différentes
- C'est ce que mesurent réellement nos instruments : horloges atomiques, désintégrations radioactives, oscillations de quasars, etc.

**Point crucial :** En cosmologie, nous ne mesurons JAMAIS directement le temps cosmologique *t* des équations FLRW. Nous mesurons toujours des temps propres situés - le temps propre écoulé depuis le Big Bang le long de NOTRE trajectoire comobile, par exemple.

Pour un observateur comobile (au repos dans le référentiel où l'univers apparaît homogène et isotrope), la relation entre temps propre et temps cosmologique est simple : τ = t. Mais cette simplicité :
- Est une conséquence de la **symétrie** du problème cosmologique
- Ne s'applique qu'aux observateurs comobiles
- Ne signifie pas que *t* est "mesuré" - le temps propre τ est mesuré, et *t* est identifié à τ *en supposant* la comouvance

#### 3.1.2 Le temps cosmologique *t* : une coordonnée conventionnelle

Le temps cosmologique *t* dans la métrique FLRW :

$$ds^2 = -c^2 dt^2 + a(t)^2 \left[\frac{dr^2}{1-kr^2} + r^2(d\theta^2 + \sin^2\theta d\phi^2)\right]$$

est une **coordonnée**, pas une observable physique directe.

**Caractéristiques du temps cosmologique :**
- Il suppose un **feuilletage** de l'espace-temps en hypersurfaces de simultanéité cosmique Σ_t
- Ce feuilletage repose sur l'hypothèse de **symétrie** (homogénéité et isotropie) qui permet de définir des surfaces "au même instant cosmologique"
- C'est une **commodité mathématique** extraordinairement utile, rendue possible par les symétries cosmologiques
- Mais il n'existe **aucun chronomètre cosmique** physique qui mesurerait ce *t*

**L'illusion de la lissité :** Le temps cosmologique *t* apparaît "lisse" dans les équations parce que :

1. Les symétries FLRW permettent de choisir une coordonnée temporelle particulièrement simple où la métrique prend une forme standard

2. Cette simplicité mathématique est confondue avec une accessibilité ontologique

3. On oublie que *t* est une **reconstruction** à partir de temps propres multiples via l'hypothèse de comouvance et l'intégration depuis les redshifts observés

**Le feuilletage comme convention :** Dans un espace-temps courbe général, il existe une infinité de façons de "découper" l'espace-temps en hypersurfaces spatiales. La cosmologie FLRW choisit un feuilletage particulier parce que :
- Il respecte les symétries observées (homogénéité, isotropie)
- Il rend les équations particulièrement simples
- Il correspond à la notion intuitive de "maintenant cosmologique"

Mais ce choix reste une **convention** motivée par la commodité et la physique observée, pas une structure absolue de l'espace-temps.

#### 3.1.3 Le temps cosmique dynamique T(z) : une approche située

Dans une approche qui prend au sérieux la situativité des observations cosmologiques, on peut proposer un cadre alternatif où le "temps cosmologique" n'est pas supposé préexistant mais **émerge** des configurations observationnelles.

Au lieu de partir de *t* comme donnée fondamentale, on peut construire un **temps cosmique dynamique** T(z) qui :

- Reconnaît explicitement sa nature de **reconstruction située** depuis des observations de redshift
- Émerge des relations observationnelles entre redshift *z* et paramètres cosmologiques mesurés (notamment H(z))
- Est contraint par les données sans supposer un substrat temporel absolu préexistant
- Fait du temps cosmique une **fonction du redshift** plutôt qu'un paramètre indépendant

**Esquisse du cadre :**

Dans le modèle standard, on a :
$$dt = -\frac{dz}{(1+z)H(z)}$$

Cette relation suppose que *t* existe indépendamment et que H(z) en dérive. Dans une approche située, on peut inverser la logique : plutôt que de reconstruire t(z) en intégrant depuis H(z), on peut définir directement un **temps cosmique** T qui émerge de la structure observationnelle :

$$T(z) = \int_0^z \frac{f(z')}{(1+z')H(z')} dz'$$

où f(z) est une fonction qui peut différer de l'unité si les données suggèrent un écoulement du temps cosmique différent du standard. Cette fonction est contrainte par :
- Les observations de H(z) via les horloges cosmiques
- Les distances de luminosité d_L(z) via les supernovae  
- Les distances angulaires d_A(z) via les BAO
- La cohérence interne entre ces différentes sondes

L'idée n'est pas de "révolutionner" la cosmologie mais de proposer un **cadre épistémologique** où le temps cosmique est explicitement reconnu comme émergeant des observations, plutôt que supposé comme structure préexistante.

**Avantages conceptuels :**
1. **Humilité épistémologique** : on ne prétend pas accéder à un "temps cosmologique absolu"
2. **Situativité explicite** : T(z) est construit depuis nos observations, pas supposé indépendant d'elles
3. **Flexibilité empirique** : si les données suggèrent des déviations, elles peuvent être incorporées dans f(z)
4. **Cohérence philosophique** : le temps cosmique est traité comme ce qu'il est - une reconstruction située, pas une donnée ontologique brute

Cette approche ne prétend pas résoudre tous les problèmes de la cosmologie, mais offre un cadre où la temporalité cosmologique est pensée de manière plus cohérente avec sa nature épistémique réelle.

### 3.2 L'incommensurabilité pratique des temps propres

Au-delà de la distinction conceptuelle entre temps propre et temps cosmologique, il existe une **incommensurabilité pratique** entre les temps propres de différents observateurs qui empêche leur réduction simple à un temps cosmologique unique.

#### 3.2.1 Les temps propres ne "convergent" pas naturellement

Considérons deux observateurs avec des trajectoires cosmologiques différentes :

**Observateur A** (comobile) : suit une trajectoire où l'univers apparaît homogène et isotrope. Son temps propre τ_A coïncide avec le temps cosmologique t par construction du référentiel comobile.

**Observateur B** (non-comobile) : possède une vitesse particulière v par rapport au référentiel comobile. Son temps propre τ_B est relié au temps cosmologique par :

$$d\tau_B = \sqrt{1 - \frac{v^2}{c^2}} dt = \gamma^{-1} dt$$

où γ est le facteur de Lorentz.

Pour l'observateur B, le "maintenant cosmologique" n'est pas défini de manière unique. Selon la relativité restreinte, ce qui est simultané pour B à un instant donné dépend de son référentiel et diffère de l'hypersurface de simultanéité cosmique Σ_t.

**Exemple concret :** Un observateur dans une galaxie avec une vitesse particulière de 600 km/s par rapport au CMB (proche de la vitesse particulière de notre Groupe Local) ne mesure pas simplement "le même t" que nous avec un petit décalage. Son feuilletage naturel de l'espace-temps en hypersurfaces "spatiales" diffère du feuilletage cosmologique standard.

#### 3.2.2 La multiplicité des référentiels d'observation

En cosmologie observationnelle, nous reconstruisons l'histoire de l'univers à partir de multiples sources :
- Des **supernovae** qui explosent avec des temps propres spécifiques le long de leurs trajectoires
- Des **quasars** dont les oscillations ont des périodicités mesurées dans leur temps propre
- Le **CMB** dont les photons suivent des géodésiques nulles (temps propre = 0)
- Des **horloges cosmiques** (galaxies vieillissantes, etc.) avec leurs propres temps propres

Aucun de ces objets ne "mesure" le temps cosmologique *t*. Chacun suit sa propre trajectoire dans l'espace-temps et mesure son propre temps propre. La reconstruction de *t* nécessite :

1. **D'identifier** chaque source comme approximativement comobile (ce qui est une hypothèse)
2. **D'intégrer** les redshifts observés en supposant le cadre FLRW
3. **D'assembler** ces mesures multiples en une histoire cohérente

Cet assemblage n'est pas une simple "lecture" d'un temps préexistant, mais une **construction épistémique active** qui suppose la validité du modèle cosmologique standard.

#### 3.2.3 Les effets gravitationnels sur le temps propre

La gravitation elle-même induit des différences de temps propre entre observateurs à différentes positions dans un champ gravitationnel. Dans un espace-temps cosmologique avec inhomogénéités (structures à grande échelle), les temps propres d'observateurs à différents endroits divergent :

$$d\tau = \sqrt{-g_{00}(x^\mu)} dt$$

où g₀₀ dépend du potentiel gravitationnel local. Un observateur dans un super-amas dense ne vieillit pas au même rythme qu'un observateur dans un vide cosmique, même s'ils sont tous deux "comobiles" au sens cosmologique.

**Quantitativement :** Les différences de potentiel gravitationnel Φ entre structures cosmologiques induisent des variations relatives de temps propre de l'ordre de Φ/c² ∼ 10⁻⁵ à 10⁻⁶. Sur l'âge de l'univers (∼13.8 milliards d'années), cela représente des différences de dizaines à centaines de milliers d'années de temps propre entre observateurs dans des environnements gravitationnels différents.

Ces différences ne sont pas négligeables pour une cosmologie de précision, et elles soulignent que parler d'"âge de l'univers" comme d'un nombre unique suppose déjà qu'on a choisi un référentiel temporel privilégié (celui d'un observateur comobile dans un potentiel gravitationnel moyen).

### 3.3 Le temps cosmologique comme patchwork de reconstructions situées

Le temps cosmologique, loin d'être une structure lisse directement accessible, est mieux compris comme un **patchwork** de reconstructions situées depuis de multiples observations locales.

#### 3.3.1 La reconstruction multi-sondes

La cosmologie moderne utilise de multiples "sondes" pour contraindre l'histoire temporelle de l'univers :

**Sondes de distance :**
- **Supernovae Ia** : chandelles standards donnant d_L(z)
- **BAO** (oscillations acoustiques baryoniques) : règles standards donnant d_A(z) et H(z)
- **Lentilles gravitationnelles** : géométrie de l'espace-temps

**Sondes directes de H(z) :**
- **Horloges cosmiques** : galaxies vieillissantes dont le spectre évolue
- **BAO en mode radial** : mesure directe de H(z) via ∆z/∆χ

**Sondes de structure :**
- **CMB** : dernière surface de diffusion à z∼1100
- **Forêt Lyman-α** : structure à z∼2-4
- **Amas de galaxies** : croissance des structures

Chacune de ces sondes fournit des **contraintes partielles** sur l'histoire cosmologique. La reconstruction du temps cosmologique t(z) nécessite :

1. **Un modèle** (typiquement ΛCDM) qui relie ces observables à des paramètres cosmologiques
2. **Une hypothèse de cohérence** : toutes ces sondes racontent la "même histoire"
3. **Une inférence statistique** (méthodes bayésiennes, MCMC) pour extraire les paramètres

Ce processus n'est pas une "mesure directe" de t(z) mais une **reconstruction inférentielle** qui dépend crucialement des hypothèses du modèle.

#### 3.3.2 Les tensions observationnelles comme symptômes

Les "tensions" actuelles en cosmologie (tension H₀, tension S₈, etc.) peuvent être comprises comme des **symptômes** de la difficulté à assembler de manière cohérente ce patchwork de reconstructions temporelles.

**Exemple : La tension H₀**

La mesure locale de la constante de Hubble H₀ (via supernovae et échelle de distances) donne :
$$H_0^{\text{local}} = 73.04 \pm 1.04 \text{ km/s/Mpc}$$

La mesure via le CMB (avec le modèle ΛCDM) donne :
$$H_0^{\text{CMB}} = 67.4 \pm 0.5 \text{ km/s/Mpc}$$

Cette discordance de ∼5σ pourrait être interprétée de plusieurs façons :
1. Erreur systématique dans l'une des mesures
2. Nouvelle physique (énergie noire évoluant, courbure spatiale, etc.)
3. **Symptôme d'une difficulté plus profonde** : les reconstructions temporelles depuis différentes époques cosmologiques ne s'assemblent pas parfaitement

Nous ne suggérons pas que la tension H₀ invalide le cadre FLRW, mais seulement que ces tensions illustrent que le temps cosmologique n'est pas une structure "donnée" mais **assemblée** - et cet assemblage rencontre des difficultés.

#### 3.3.3 La circularité épistémique

Il existe une circularité dans la reconstruction du temps cosmologique :

1. Pour **mesurer H(z)** précisément, nous avons besoin de connaître les distances d(z)
2. Pour **calculer d(z)**, nous devons intégrer : $$d_C(z) = c\int_0^z \frac{dz'}{H(z')}$$
3. Cette intégration suppose que nous connaissons déjà H(z')

En pratique, on brise cette circularité en :
- Supposant un modèle paramétrique (ΛCDM avec paramètres libres)
- Ajustant les paramètres pour maximiser la cohérence entre différentes observations
- Validant la cohérence interne du modèle résultant

Mais cette procédure met en lumière que le temps cosmologique t(z) n'est pas **extrait** des données de manière model-independent, mais plutôt **co-construit** avec le modèle cosmologique lui-même.

**Conséquence philosophique :** Le temps cosmologique n'est pas une structure ontologique que nous "découvrons" dans la nature, mais une construction épistémique que nous **élaborons** en interprétant nos observations à travers un cadre théorique. Cette construction est hautement contrainte par les données et extrêmement robuste dans le régime où les données sont abondantes (z < 2), mais elle reste une construction.

### 3.4 Implications : pourquoi la RG cosmologique n'est pas "lisse" épistémologiquement

Revenons maintenant à la dichotomie initiale entre mécanique quantique "probabiliste" et relativité générale "déterministe et lisse".

#### 3.4.1 Le déterminisme apparent des équations FLRW

Les équations de Friedmann sont déterministes : si on connaît ρ(t), p(t), et les conditions initiales, alors a(t) est complètement déterminé. Mathématiquement :

$$\frac{d^2a}{dt^2} = F[a, \rho, p, \Lambda]$$

où F est une fonction déterministe. Donné a(t₀) et ȧ(t₀), toute l'évolution future et passée est en principe calculable.

**Mais ce déterminisme repose sur l'accès à *t* comme paramètre temporel bien défini.**

#### 3.4.2 L'opacité épistémique du temps cosmologique

En réalité, nous n'avons pas accès à *t* directement. Nous avons accès à :
- Des redshifts z
- Des temps propres τ le long de trajectoires spécifiques
- Des durées ∆τ entre événements

La reconstruction de t(z) nécessite :
1. D'adopter un modèle (ΛCDM)
2. D'intégrer depuis les observations de H(z)
3. D'assembler des reconstructions multi-sondes

Ce processus introduit une **opacité épistémique** : même si les équations sous-jacentes sont déterministes, notre accès à la variable temporelle elle-même est médiatisé, reconstruit, situé.

**Analogie :** C'est comme si en mécanique classique, vous ne pouviez jamais lire le temps t sur une horloge, mais seulement observer des positions x(z) où z est une variable proxy, et devoir reconstruire t(z) par intégration. Même si les équations dx/dt = v sont déterministes, votre connaissance pratique de la dynamique serait "opaque" car vous ne mesurez jamais t directement.

#### 3.4.3 La "rugosité" temporelle de la cosmologie observationnelle

Le temps cosmologique, compris comme patchwork de reconstructions, présente sa propre forme de **"rugosité"** :

1. **Discontinuité entre sondes** : différentes méthodes de reconstruction peuvent donner des résultats légèrement discordants (cf. tension H₀)

2. **Dépendance au modèle** : t(z) reconstruit dépend du modèle cosmologique supposé (ΛCDM vs alternatives)

3. **Incertitude cumulative** : plus on remonte dans le temps (z élevé), plus les incertitudes s'accumulent

4. **Zones d'ombre observationnelles** : certaines époques (dark ages, z∼10-30) sont mal contraintes

Cette "rugosité" n'est pas l'indétermination quantique, mais une **opacité épistémique spécifique** à la temporalité cosmologique : le temps cosmologique n'est pas une donnée lisse que nous lirions sur un chronomètre universel, mais un assemblage de reconstructions partielles avec leurs incohérences et incertitudes.

#### 3.4.4 Conséquence pour la dichotomie MQ/RG

La dichotomie standard :
- **MQ** : probabiliste, indéterministe, "flou"
- **RG** : déterministe, prédictible, "lisse"

est trompeuse quand on la prend au sérieux épistémologiquement.

**Reformulation plus exacte :**
- **MQ** : indétermination fondamentale sur les observables jusqu'à la mesure
- **RG cosmologique** : déterminisme formel des équations, mais opacité épistémique de la variable temporelle elle-même

Les deux théories ont des formes d'**inaccessibilité épistémique**, mais de natures différentes :
- MQ : certaines propriétés n'existent pas avant la mesure (interprétation standard)
- RG cosmologique : le temps cosmologique n'existe pas comme donnée accessible, seulement comme reconstruction

Les modèles de collapse comme celui de Carlesso et al. tentent de "résoudre" l'incompatibilité en rendant la MQ plus "classique" (via le collapse spontané), mais ils ne questionnent pas le présupposé que la RG serait épistémologiquement transparente.

**Notre thèse :** L'incompatibilité perçue entre MQ et RG repose en partie sur une compréhension naïve de la RG cosmologique comme ayant un temps "lisse" directement accessible. Une fois qu'on reconnaît l'opacité épistémique du temps cosmologique, la dichotomie s'atténue - non pas que les problèmes disparaissent, mais leur formulation change.

---

## 4. Dialogue avec la littérature philosophique

### 4.1 Le temps en cosmologie relativiste

#### 4.1.1 Carlo Rovelli : L'inexistence du temps global

Dans *The Order of Time* (2018), Carlo Rovelli argumente que le temps global n'existe pas en relativité générale - il n'y a que des temps locaux. Notre reconstruction du "temps cosmologique" serait donc une illusion d'optique théorique, une commodité qui masque la réalité plus fondamentale de temporalités locales irréductiblement multiples.

**Points de convergence avec notre critique :**
- Le temps cosmologique *t* n'est pas une structure fondamentale mais une coordonnée commode
- Seuls les temps propres locaux sont réels (mesurables)
- La notion de "maintenant cosmologique" est une construction, pas une donnée ontologique

**Où nous allons plus loin :**
Rovelli se concentre sur l'argument théorique (absence de temps global en RG). Nous ajoutons la dimension **épistémologique** : même en supposant la validité du cadre FLRW, le temps cosmologique n'est jamais observé directement mais toujours reconstruit. C'est une opacité épistémique qui s'ajoute à l'argument ontologique de Rovelli.

#### 4.1.2 Lee Smolin : La réification du temps cosmologique

Dans *Time Reborn* (2013), Lee Smolin défend au contraire que le temps cosmologique est **réel** et fondamental. Il critique les approches (comme celle de Barbour) qui traitent le temps comme émergent ou illusoire, arguant que cela mène à des paradoxes en cosmologie quantique.

**Notre critique de Smolin :**
Smolin réifie le temps cosmologique précisément de la manière que nous contestons. Il suppose que parce que le temps joue un rôle essentiel dans la description cosmologique, il doit être une structure ontologique fondamentale. Mais il confond :
- L'importance du temps dans nos descriptions (indéniable)
- L'accessibilité ontologique du temps cosmologique (problématique)

Le temps peut être "réel" au sens où les processus temporels sont réels, sans que le temps cosmologique *t* soit une structure absolue accessible. Notre approche d'un temps cosmique **émergent** T(z) reconnaît la réalité des processus temporels tout en évitant la réification du temps cosmologique comme substrat absolu.

#### 4.1.3 Julian Barbour : Le temps comme illusion - une critique

Julian Barbour, dans *The End of Time* (1999), adopte une position radicale : le temps serait une illusion complète. Seules existent des configurations spatiales ("Nows"), et ce que nous appelons "temps" serait simplement un ordre émergent entre ces configurations.

**Pourquoi nous ne suivons pas Barbour :**
Barbour élimine le temps trop radicalement. Les processus temporels sont réels :
- Les horloges mesurent quelque chose de réel (le temps propre)
- L'irréversibilité thermodynamique est réelle
- L'expansion cosmologique est un processus réel

Notre position est intermédiaire entre Smolin (le temps cosmologique comme structure absolue) et Barbour (le temps comme pure illusion) : **le temps est réel mais relationnel et situé**. Il n'est ni une structure absolue préexistante (contra Smolin) ni une pure illusion (contra Barbour), mais émerge des relations entre observateurs situés et configurations gravitationnelles.

### 4.2 Enaction et situativité

#### 4.2.1 Karen Barad : Les coupes agentielles poreuses

Karen Barad, dans *Meeting the Universe Halfway* (2007), développe le concept d'"agential cuts" (coupes agentielles) : la séparation entre sujet observateur et objet observé n'est pas donnée a priori mais se **co-constitue** à travers les pratiques d'observation.

**Application à la cosmologie :**
Le feuilletage de l'espace-temps en hypersurfaces "spatiales" (définissant un "maintenant cosmologique") est précisément une **coupe agentielle** :
- Elle n'est pas une structure absolue de l'espace-temps
- Elle émerge de nos pratiques observationnelles (choix du référentiel comobile, reconstruction depuis les redshifts)
- Elle est **poreuse** : la distinction entre "espace" et "temps" cosmologiques n'est pas absolue mais dépend du référentiel

**Concept clé : Le gradient des coupes agentielles**
Les coupes agentielles ne sont pas binaires (observateur/observé) mais admettent un **gradient de porosité** :
- Au niveau local (laboratoire) : distinction relativement stable entre observateur et système observé
- Au niveau cosmologique : l'observateur fait partie du système observé (l'univers), la coupe devient maximalement poreuse

Le temps cosmologique, comme coupe agentielle qui sépare "maintenant" de "alors", est particulièrement poreux en cosmologie car :
1. L'observateur est situé **dans** l'univers dont il reconstruit l'histoire temporelle
2. Cette reconstruction dépend de ses mesures locales (redshifts, distances)
3. Il n'y a pas de position "externe" depuis laquelle observer l'univers

#### 4.2.2 Varela/Thompson : Ni réalisme naïf ni constructivisme

Dans *The Embodied Mind* (1991), Francisco Varela, Evan Thompson et Eleanor Rosch développent l'approche **enactive** de la cognition : la connaissance n'est ni représentation d'un monde prédonné (réalisme naïf) ni pure construction mentale (constructivisme), mais **co-émergence** de l'organisme et de son environnement à travers l'action.

**Transposition à la cosmologie :**
Notre connaissance du temps cosmologique n'est ni :
- **Réaliste naïve** : lecture d'un temps préexistant sur un "chronomètre cosmique"
- **Constructiviste** : invention arbitraire d'une coordonnée temporelle sans contraintes

Mais **enactive** : le temps cosmologique **émerge** de l'interface entre :
- Des observateurs situés avec leurs instruments de mesure (redshifts, distances)
- Une configuration gravitationnelle réelle qui contraint ces mesures
- Un cadre théorique (FLRW) qui permet d'interpréter les données

Cette émergence est :
- **Contrainte** par la réalité physique (toutes les reconstructions ne sont pas équivalentes)
- **Située** (dépend de la position et des pratiques de l'observateur)
- **Relationnelle** (n'existe que dans la relation observateur-univers)

#### 4.2.3 Donna Haraway : Savoirs situés en cosmologie

Donna Haraway, dans "Situated Knowledges" (1988), critique le "regard de nulle part" (*view from nowhere*) qui prétend à une objectivité absolue décontextualisée. Elle défend que tout savoir est **situé** - produit depuis une position particulière - sans pour autant tomber dans le relativisme.

**Application à la cosmologie :**
La cosmologie standard présente souvent ses résultats (âge de l'univers : 13.8 Gyr, H₀ = 67.4 km/s/Mpc) comme des **faits décontextualisés**, des vérités objectives indépendantes de toute situativité.

Mais ces nombres sont en réalité **situés** :
- Ils sont reconstruits depuis **notre position** dans l'espace-temps (observateurs terrestres dans l'univers local à z≈0)
- Ils supposent un **référentiel temporel** particulier (celui d'un observateur comobile)
- Ils dépendent de **choix théoriques** (modèle ΛCDM, hypothèses sur l'énergie noire)

Reconnaître cette situativité n'est pas du relativisme - les données contraignent fortement nos reconstructions. Mais c'est une **humilité épistémologique** qui reconnaît que notre connaissance cosmologique est toujours produite depuis une position située, pas depuis un "regard de nulle part".

**Le temps cosmologique comme "regard de nulle part" temporel :**
Traiter le temps cosmologique *t* comme une donnée absolue revient à adopter un "regard de nulle part" **temporel** - comme si nous pouvions nous placer "hors du temps" pour observer l'univers évoluer dans ce temps absolu. En réalité, nous sommes toujours **dans** le temps (mesurant notre temps propre local) et reconstruisons *t* depuis cette position située.

### 4.3 Processualisme

#### 4.3.1 Whitehead : Processus vs substance

Alfred North Whitehead, dans *Process and Reality* (1929), développe une métaphysique où la réalité fondamentale n'est pas constituée de substances (entités permanentes) mais de **processus** (événements, occasions actuelles).

**Résonance avec notre approche :**
Le temps cosmologique n'est pas une "substance" temporelle préexistante (comme un conteneur dans lequel les événements se produiraient), mais un **processus** :
- Il émerge continuellement de l'interaction entre observateurs et configurations gravitationnelles
- Il n'est pas "là" de manière statique, mais se constitue à travers les pratiques d'observation et de reconstruction
- Les "instants cosmologiques" ne sont pas des entités fixes mais des **événements relationnels**

Dans le vocabulaire whiteheadien, chaque observation cosmologique (mesure de redshift, détection de supernova) est une "occasion actuelle" qui contribue à la construction du temps cosmique.

#### 4.3.2 Prigogine : Irréversibilité et temporalité

Ilya Prigogine, dans *La Nouvelle Alliance* (1979), insiste sur l'importance de l'**irréversibilité** et de la **flèche du temps** dans les systèmes loin de l'équilibre thermodynamique. Contre la vision réversible de la mécanique classique, il défend que le temps a une direction intrinsèque dans les processus dissipatifs.

**Lien avec notre approche :**
L'expansion cosmologique est un processus **irréversible** :
- L'entropie de l'univers croît
- Le facteur d'échelle a(t) croît monotoniquement (dans le modèle standard)
- Les structures se forment de manière irréversible

Cette irréversibilité est **réelle** et mesurable. Notre critique du temps cosmologique comme structure lisse ne nie pas cette réalité, mais souligne que :
- L'irréversibilité est une propriété des **processus** (expansion, formation de structure)
- Pas nécessairement l'existence d'un **substrat temporel absolu** dans lequel ces processus se produiraient

Le temps cosmique peut être **émergent** des processus irréversibles plutôt que leur préexistant. Dans cette perspective, c'est l'expansion elle-même qui "génère" le temps cosmique, pas le temps cosmique qui "contient" l'expansion.

---

## 5. Vers un cadre observationnel situé

### 5.1 Principes d'un cadre situé

Au lieu de partir du temps cosmologique *t* comme donnée fondamentale, nous proposons des principes pour un cadre épistémologiquement plus humble :

#### Principe 1 : Primauté du redshift
Le redshift *z* est l'observable cosmologique **primaire** - ce que nous mesurons directement via les décalages spectraux. Plutôt que de reconstruire t(z) et travailler dans l'espace des temps, nous pouvons travailler directement dans **l'espace des redshifts**.

#### Principe 2 : Temps cosmique comme fonction émergente
Le temps cosmique n'est pas supposé préexistant mais construit comme **fonction du redshift** T(z), émergeant des relations observationnelles contraintes par les données.

#### Principe 3 : Reconnaissance de la situativité
Toute reconstruction temporelle est explicitement reconnue comme **située** - produite depuis la position de l'observateur (z≈0, référentiel terrestre) et dépendante du cadre théorique adopté.

#### Principe 4 : Humilité face aux incertitudes
Les tensions et incohérences entre différentes sondes ne sont pas traitées comme des "anomalies" à éliminer à tout prix, mais comme des **indicateurs** de la difficulté intrinsèque à assembler un temps cosmologique universel depuis des observations situées multiples.

#### Principe 5 : Contrainte empirique forte
Bien que situé et reconstruit, le temps cosmique reste **fortement contraint** par les données observationnelles - toutes les reconstructions ne sont pas équivalentes. La situativité n'implique pas l'arbitraire.

### 5.2 Esquisse du temps cosmique dynamique T(z)

Développons maintenant l'approche esquissée en section 3.1.3.

#### 5.2.1 Construction standard

Dans le modèle ΛCDM standard, le temps cosmologique est obtenu par :

$$t(z) = t_0 - \int_0^z \frac{dz'}{(1+z')H(z')}$$

où H(z) est le paramètre de Hubble :

$$H(z) = H_0 \sqrt{\Omega_m(1+z)^3 + \Omega_r(1+z)^4 + \Omega_k(1+z)^2 + \Omega_\Lambda}$$

Cette reconstruction **suppose** :
- La validité du modèle ΛCDM
- L'identification du temps cosmologique *t* avec le temps propre d'un observateur comobile
- L'homogénéité et l'isotropie parfaites

#### 5.2.2 Approche alternative : temps cosmique dynamique

Plutôt que de supposer *t* et d'en dériver H(z), nous pouvons inverser la logique :

**Étape 1 : Mesurer H(z) directement**
Utiliser les horloges cosmiques, BAO, et autres sondes pour contraindre H(z) de manière aussi model-independent que possible.

**Étape 2 : Définir le temps cosmique comme fonction du redshift**
$$T(z) = T_0 - \int_0^z \frac{f(z')}{(1+z')H(z')} dz'$$

où la fonction f(z) représente un éventuel écoulement du temps cosmique différent du standard.

**Étape 3 : Contraindre f(z) par cohérence multi-sondes**
La fonction f(z) doit assurer la cohérence entre :
- Les distances de luminosité $d_L(z)$
- Les distances angulaires $d_A(z)$
- La relation distance-redshift
- L'âge des objets les plus anciens (contrainte de cohérence)

Dans le modèle standard, f(z) = 1. Mais les données pourraient suggérer des déviations.

#### 5.2.3 Lien avec la Cosmologie Chronodynamique (CCD)

Cette approche est compatible avec le cadre CCD où le temps cosmique est traité comme **dynamique** plutôt que comme paramètre fixe. Dans le CCD :

$$T(z) = \int_0^z \frac{dz'}{(1+z')H_{\text{eff}}(z')}$$

où $H_{\text{eff}}(z)$ peut différer de $H_{\text{standard}}(z)$ si l'écoulement du temps cosmique est lui-même dynamique, influencé par les configurations gravitationnelles à différentes époques.

**Intuition physique :** Si la "densité temporelle" (l'écoulement local du temps propre) varie avec les conditions gravitationnelles cosmiques, alors le temps cosmique global intégré pourrait différer du standard. Cette variation serait :
- Faible (contrainte par les observations actuelles)
- Potentiellement détectable avec la cosmologie de précision
- Une manifestation de la nature **émergente** du temps cosmique

### 5.3 Implications pour l'observation cosmologique

#### 5.3.1 Nouvelles questions observationnelles

Un cadre situé suggère de nouvelles questions :

**Q1 :** Les reconstructions de T(z) depuis différentes sondes (supernovae vs BAO vs horloges cosmiques) sont-elles parfaitement cohérentes, ou y a-t-il des écarts systématiques ?

**Q2 :** Les tensions cosmologiques (H₀, S₈) pourraient-elles refléter non pas une "nouvelle physique" au sens habituel, mais une difficulté à assembler un temps cosmologique universel depuis des observations situées à différentes époques ?

**Q3 :** Peut-on contraindre f(z) indépendamment en utilisant la cohérence interne entre multiples sondes ?

#### 5.3.2 Tests possibles

**Test 1 : Cohérence multi-époques**
Reconstruire T(z) séparément depuis :
- Observations locales (z < 0.1) : supernovae, BAO
- Observations intermédiaires (0.1 < z < 2) : quasars, horloges cosmiques  
- Observations primordiales (z > 1000) : CMB

Vérifier si ces reconstructions se raccordent de manière parfaitement lisse ou s'il existe des "coutures" indiquant une difficulté d'assemblage.

**Test 2 : Contraintes sur f(z)**
Ajuster f(z) paramétriquement (par exemple avec quelques paramètres libres) et voir si les données préfèrent f(z) ≠ 1, tout en vérifiant que cela n'introduit pas de nouveaux problèmes.

**Test 3 : Cohérence avec âges globulaires**
Les amas globulaires les plus anciens ont des âges mesurés indépendamment (via évolution stellaire). Ces âges doivent être cohérents avec T(z) reconstruit - c'est une contrainte forte.

#### 5.3.3 Limites de l'approche

Cette approche **ne prétend pas** :
- Révolutionner la cosmologie ou remplacer ΛCDM
- Résoudre toutes les tensions observationnelles
- Fournir une théorie complète du temps cosmique

Elle propose plutôt :
- Un **cadre épistémologique** plus humble et conscient de ses présupposés
- Des **questions nouvelles** sur la cohérence interne des reconstructions temporelles
- Une **conceptualisation alternative** du temps cosmique comme émergent plutôt que fondamental

Les données actuelles sont cohérentes avec f(z) = 1 dans les barres d'erreur. L'intérêt n'est pas de forcer une déviation, mais de **reconnaître conceptuellement** que le temps cosmologique est une reconstruction, pas une donnée brute.

---

## 6. Implications pour le problème quantique-gravitationnel

### 6.1 Les modèles de collapse ratent la temporalité située

Revenons maintenant au modèle de Carlesso et al. avec notre analyse en main.

#### 6.1.1 Le présupposé non questionné

Leur modèle suppose qu'il existe un "temps cosmologique universel" dans lequel :
- Les collapses spontanés se produisent "à intervalles réguliers"
- L'univers "choisit" une géométrie "maintenant"
- Cette dynamique est bien définie globalement

Notre analyse montre que ce présupposé est problématique :

1. **Il n'y a pas d'horloge cosmique universelle** qui mesurerait ces "intervalles réguliers" - seulement des temps propres locaux situés

2. **Le "maintenant cosmologique" n'est pas une donnée ontologique** mais une construction dépendant du feuilletage choisi (référentiel comobile)

3. **Parler de collapse "spontané" suppose une simultanéité cosmique** qui est précisément ce que notre critique remet en question

#### 6.1.2 La vraie incompatibilité MQ/RG

L'incompatibilité entre MQ et RG n'est pas simplement :
- MQ est probabiliste ↔ RG est déterministe

Mais plus subtilement :
- **MQ** : certaines propriétés n'existent pas avant la mesure (interprétation standard)
- **RG cosmologique** : suppose un temps cosmologique accessible dans lequel décrire l'évolution

Les deux théories ont des **structures temporelles incompatibles** :
- MQ (dans sa formulation standard) : temps absolu t apparaissant dans l'équation de Schrödinger
- RG : pas de temps absolu, seulement des temps propres relatifs

Les modèles de collapse tentent de résoudre cette incompatibilité en rendant la MQ plus "classique", mais ils **ne questionnent pas** la structure temporelle supposée de la RG. Ils ajoutent une modification ad hoc (collapse spontané) sans reconnaître que la RG elle-même n'a pas de temps cosmologique absolu accessible.

#### 6.1.3 Alternative conceptuelle

Une approche plus cohérente serait de reconnaître que **ni la MQ ni la RG ne disposent d'un temps absolu global** :
- MQ : doit être reformulée de manière covariante (ce qui est fait en théorie quantique des champs sur espace-temps courbe)
- RG cosmologique : le temps cosmologique est une reconstruction située, pas une donnée absolue

Dans cette perspective, le "problème de la mesure" en cosmologie quantique pourrait être reformulé :
- Non pas : "Comment l'univers choisit-il une géométrie dans le temps cosmologique ?"
- Mais : "Comment des observateurs situés reconstruisent-ils une histoire cosmologique cohérente depuis leurs observations locales ?"

Ce changement de perspective évite d'ajouter des mécanismes ad hoc (collapse spontané) et reconnaît que la difficulté est en partie **épistémologique** - comment coordonner des descriptions situées multiples - plutôt que purement ontologique.

### 6.2 Vers une autre approche de la gravité quantique ?

#### 6.2.1 Leçons de notre critique

Notre analyse suggère plusieurs leçons pour la recherche en gravité quantique :

**Leçon 1 : La temporalité doit être repensée fondamentalement**
Ni le temps absolu de la MQ standard, ni le temps cosmologique de la RG classique ne peuvent servir de fondation pour une théorie quantique de la gravité. Le temps doit être traité comme :
- Relationnel (dépendant des configurations physiques)
- Émergent (pas fondamental)
- Situé (différent pour différents observateurs)

**Leçon 2 : L'importance de la situativité de l'observateur**
En gravité quantique, la position de l'observateur n'est pas accessoire mais constitutive de ce qui peut être mesuré. Cela rejoint :
- Le principe holographique (information accessible dépend de la surface)
- La complémentarité des trous noirs (descriptions observer-dependent)
- L'approche relationnelle de Rovelli

**Leçon 3 : Éviter les "solutions" qui ne questionnent pas leurs présupposés**
Les tentatives de réconciliation MQ/RG qui ajoutent des mécanismes (collapse spontané, hidden variables, etc.) sans questionner les structures temporelles supposées risquent de créer des "épicycles" plutôt que des avancées conceptuelles.

#### 6.2.2 Pistes alternatives

Sans prétendre avoir de solution, nous pouvons esquisser des pistes cohérentes avec notre critique :

**Piste 1 : Gravité quantique relationnelle**
Développer une formulation où :
- Les observables sont toujours relationnelles (observateur-système)
- Le temps émerge de corrélations entre degrés de liberté
- Pas de structure temporelle absolue préexistante

Cette approche est explorée dans certaines versions de la Loop Quantum Gravity.

**Piste 2 : Cosmologie quantique située**
Plutôt que demander "Quel est l'état quantique de l'univers ?", demander :
- "Que peut observer un observateur situé dans l'univers ?"
- "Comment des observateurs situés différemment coordonnent-ils leurs descriptions ?"
- "Quelle histoire cosmologique peut être reconstruite depuis des observations situées ?"

**Piste 3 : Temps cosmique comme émergence collective**
Traiter le temps cosmique comme propriété **collective** émergeant de l'ensemble des horloges et processus physiques dans l'univers, plutôt que comme structure fondamentale. Cette approche rejoint certaines idées de :
- Julian Barbour (malgré notre critique de son éliminativisme)
- Thermal time hypothesis de Connes et Rovelli
- Approches causales de la gravité quantique

#### 6.2.3 Humilité épistémologique

Nous concluons cette section avec humilité : nous n'avons pas de solution complète au problème de la gravité quantique. Notre contribution est plus modeste :

**Clarifier ce qui est problématique** dans certaines approches actuelles (comme les modèles de collapse cosmologiques) en montrant qu'elles reposent sur des présupposés non questionnés concernant la structure temporelle cosmologique.

**Suggérer une direction conceptuelle** : reconnaître la situativité irréductible des observations cosmologiques et la nature émergente du temps cosmique plutôt que supposer un temps cosmologique absolu accessible.

**Ouvrir des questions** : Comment une théorie quantique de la gravité pourrait-elle accommoder une temporalité explicitement située et émergente ? Quelles nouvelles prédictions observationnelles découleraient d'une telle approche ?

---

## 7. Conclusion

Nous avons développé une critique du temps cosmologique comme structure "lisse" et universellement accessible, en montrant que ce présupposé - rarement questionné en cosmologie standard - repose sur une confusion entre la commodité mathématique du temps cosmologique *t* dans les équations FLRW et son accessibilité ontologique réelle.

### 7.1 Synthèse de l'argument

**Thèse principale :** Le temps cosmologique n'est pas une donnée ontologique directement accessible, mais une **reconstruction épistémique** depuis des temps propres situés multiples et des redshifts observés. Cette reconstruction :
- Suppose la validité du cadre FLRW (modèle cosmologique standard)
- Dépend du choix d'un référentiel privilégié (comobile)
- Nécessite l'intégration depuis les observations de H(z)
- Assemble un patchwork de mesures multi-sondes avec leurs cohérences et tensions

**Conséquence :** La dichotomie habituelle entre mécanique quantique "probabiliste/floue" et relativité générale "déterministe/lisse" est trompeuse. La RG cosmologique a sa propre forme d'**opacité épistémique** concernant le temps cosmologique - pas l'indétermination quantique, mais une inaccessibilité de la structure temporelle elle-même qui n'existe que comme reconstruction.

**Application critique :** Les modèles de collapse spontané (comme celui de Carlesso et al.) qui tentent de résoudre l'incompatibilité MQ/RG en faisant "choisir" spontanément une géométrie à l'univers "à intervalles réguliers" dans un "temps cosmologique universel" commettent une erreur fondamentale : ils supposent l'existence d'une structure temporelle cosmologique accessible qui n'est en réalité qu'une construction théorique.

### 7.2 Contributions

Notre analyse apporte trois contributions principales :

**1. Critique conceptuelle originale**
Nous allons au-delà des objections habituelles aux modèles de collapse (non-localité, violation de Lorentz) pour pointer vers une confusion plus profonde : la caractérisation même de la RG comme "déterministe et lisse" repose sur un présupposé non critique concernant l'accessibilité du temps cosmologique.

**2. Cadre épistémologique alternatif**
Nous esquissons une approche où le temps cosmique est explicitement reconnu comme **émergent** des configurations observationnelles plutôt que supposé préexistant. Cette approche, illustrée par le temps cosmique dynamique T(z), ne prétend pas révolutionner la cosmologie mais propose un cadre plus humble épistémologiquement.

**3. Dialogue philosophique**
Nous situons notre approche dans un dialogue avec la littérature philosophique contemporaine (Barad, Haraway, Rovelli, Varela/Thompson) montrant comment une cosmologie **située** peut être rigoureusement développée sans tomber ni dans le réalisme naïf ni dans le constructivisme arbitraire.

### 7.3 Limitations et extensions futures

**Limitations de notre approche :**
- Nous n'avons pas développé de prédictions observationnelles spécifiques testables
- Notre critique du temps cosmologique "lisse" est principalement conceptuelle
- L'approche du temps cosmique dynamique T(z) reste esquissée, pas pleinement formalisée

**Extensions futures possibles :**
1. Développer formellement le cadre T(z) avec contraintes observationnelles précises
2. Analyser quantitativement si les tensions cosmologiques actuelles (H₀, S₈) pourraient être interprétées comme difficultés d'assemblage temporel
3. Explorer les conséquences pour la cosmologie quantique d'une temporalité explicitement située
4. Dialoguer avec les approches de gravité quantique qui questionnent déjà la structure temporelle (LQG, causal sets)

### 7.4 Portée philosophique

Au-delà de la cosmologie technique, notre analyse a une portée philosophique plus large concernant **la nature du temps en physique fondamentale**.

Le temps cosmologique, traité usuellement comme structure absolue et accessible, révèle sous examen sa nature de **construction située** - ni pure convention arbitraire, ni donnée ontologique brute, mais réalité **émergente** et **relationnelle** se constituant à l'interface entre observateurs situés et configurations gravitationnelles réelles.

Cette reconnaissance de la **situativité irréductible** des observations cosmologiques - y compris de la reconstruction du temps cosmologique lui-même - n'est pas du relativisme épistémologique. Les données contraignent fortement nos reconstructions. Mais c'est une **humilité épistémologique** qui reconnaît que notre connaissance cosmologique, si impressionnante soit-elle, reste toujours produite depuis une position située, jamais depuis un "regard de nulle part" temporel.

**Le temps cosmologique est réel, mais il n'est pas lisse.**

Il est tissé d'observations multiples, de reconstructions situées, d'intégrations théoriques, d'hypothèses de cohérence - un patchwork temporel qui fonctionne remarquablement bien dans le régime observationnel actuel, mais dont nous devons reconnaître la nature construite plutôt que de le réifier en structure absolue.

Cette reconnaissance ouvre la voie à une cosmologie plus **relationnelle**, plus **processuelle**, plus **humble** - sans rien perdre de sa rigueur mathématique ou de sa puissance explicative, mais en gagnant en lucidité conceptuelle sur ce que nous faisons réellement quand nous "mesurons" le temps cosmologique.

---

## Remerciements

[À ajouter selon contexte de publication]

---

## Références

**Cosmologie et modèles de collapse :**

Carlesso, M., Gaona-Reyes, J.L., Menéndez-Pidal, L., & Faizal, M. (2024). "Spontaneous collapse models lead to the emergence of classicality of the Universe." *Journal of High Energy Physics*, 2024(2), 193.

Ghirardi, G.C., Rimini, A., & Weber, T. (1986). "Unified dynamics for microscopic and macroscopic systems." *Physical Review D*, 34(2), 470.

Pearle, P. (1989). "Combining stochastic dynamical state-vector reduction with spontaneous localization." *Physical Review A*, 39(5), 2277.

Bassi, A., & Ghirardi, G.C. (2003). "Dynamical reduction models." *Physics Reports*, 379(5-6), 257-426.

**Philosophie du temps en physique :**

Rovelli, C. (2018). *The Order of Time*. Riverhead Books.

Smolin, L. (2013). *Time Reborn: From the Crisis in Physics to the Future of the Universe*. Houghton Mifflin Harcourt.

Barbour, J. (1999). *The End of Time: The Next Revolution in Physics*. Oxford University Press.

Rovelli, C. (1991). "Time in quantum gravity: An hypothesis." *Physical Review D*, 43(2), 442.

**Enaction et situativité :**

Barad, K. (2007). *Meeting the Universe Halfway: Quantum Physics and the Entanglement of Matter and Meaning*. Duke University Press.

Varela, F.J., Thompson, E., & Rosch, E. (1991). *The Embodied Mind: Cognitive Science and Human Experience*. MIT Press.

Haraway, D. (1988). "Situated Knowledges: The Science Question in Feminism and the Privilege of Partial Perspective." *Feminist Studies*, 14(3), 575-599.

Thompson, E. (2007). *Mind in Life: Biology, Phenomenology, and the Sciences of Mind*. Harvard University Press.

**Processualisme :**

Whitehead, A.N. (1929). *Process and Reality: An Essay in Cosmology*. Macmillan.

Prigogine, I., & Stengers, I. (1979). *La Nouvelle Alliance: Métamorphose de la science*. Gallimard.

**Cosmologie observationnelle :**

Riess, A.G., et al. (2022). "A Comprehensive Measurement of the Local Value of the Hubble Constant with 1 km/s/Mpc Uncertainty from the Hubble Space Telescope and the SH0ES Team." *The Astrophysical Journal Letters*, 934(1), L7.

Planck Collaboration (2020). "Planck 2018 results. VI. Cosmological parameters." *Astronomy & Astrophysics*, 641, A6.

DESI Collaboration (2024). "DESI 2024 VI: Cosmological Constraints from the Measurements of Baryon Acoustic Oscillations." *arXiv:2404.03002*.

**Gravité quantique :**

Rovelli, C., & Smolin, L. (1995). "Discreteness of area and volume in quantum gravity." *Nuclear Physics B*, 442(3), 593-619.

Connes, A., & Rovelli, C. (1994). "Von Neumann algebra automorphisms and time-thermodynamics relation in generally covariant quantum theories." *Classical and Quantum Gravity*, 11(12), 2899.

Sorkin, R.D. (2005). "Causal sets: Discrete gravity." In *Lectures on Quantum Gravity* (pp. 305-327). Springer.

---

*Document version 1.0 - Novembre 2025*