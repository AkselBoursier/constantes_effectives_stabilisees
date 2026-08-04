# C7-GAL-C0-B — pré-spécification de la route gravitationnelle G2

Version : `v0.2`
Date : `2026-08-04`
Issue : `#97`
Nature : `PREPARATION_ONLY`
Coexistence au moment de la rédaction : `ACTIVE`
Remplace : `v0.1`, commit `38985b9c8957b84fc7c2e62344a9c1842ed1eb4d`
Motif : corrections d'audit + extension `G2-FIELD`/`G2-EOM`
Verdict de cette version : `C0-B_V02_PRETE_A_AUDIT_FINAL`

## 1. Statut, portée et vocabulaire de preuve

Ce document prépare une future évaluation de faisabilité de G2. Il ne contient
ni calcul FIRE, ni résultat scientifique sur `m11d` ou `m11e`, ni autorisation
de lancer G2. Il ne ferme pas C0-A et ne transfère aucun paramètre opérationnel
de C7-C1 vers C7-GAL.

La porte applique la distinction suivante :

> discipline générale de provenance, séparation des environnements et
> garde-fous réutilisables ; paramètres scientifiques et computationnels de
> C7-GAL à établir séparément.

Les statuts employés sont :

- `DOCUMENTE` : soutenu directement par une source primaire ou par un fichier
  public propre aux simulations visées ;
- `CONVENTION_EXPLICITE` : correspondance de notation explicitement sourcée,
  sans prétention à une identité entre conventions historiques ;
- `ETABLI_PAR_C0A` : constat d'entrée hérité du commentaire C0-A de `#88`, sans
  nouvelle lecture des snapshots ;
- `INFERENCE_CONTROLEE` : conséquence explicite de plusieurs faits documentés,
  avec hypothèses visibles ;
- `PROPOSITION` : règle candidate à auditer avant adoption ;
- `PROPOSITION_SOUS_CONDITION` : route candidate dont un prérequis explicite
  n'est pas encore établi et qui ne peut servir de référence avant fermeture ;
- `A_RATIFIER` : valeur, seuil ou choix à figer avant toute lecture du résultat
  cible ;
- `NON_ETABLI` : information que les sources consultées ne suffisent pas à
  fixer.

Le mot « référence » désigne un comparateur numérique assorti d'un budget
d'erreur et d'un niveau de fidélité déclaré. Aucun objet reconstruit n'est
qualifié de vérité gravitationnelle totale.

### 1.1 Corrections v0.2 après audit

1. nomenclature des softenings ;
2. `G2-FIELD` / `G2-EOM` et `grad-h` ;
3. séparation solver/discretization/kernel ;
4. périodicité / `BoxSize` / mode moyen ;
5. budget d'erreur ;
6. hiérarchie de fidélité ;
7. règle `FIELD -> EOM`.

## 2. État d'entrée C0-A et coexistence

### 2.1 État factuel hérité

| Objet | État | Statut |
| --- | --- | --- |
| `m11d_res7100/snapshot_600` | identifié et inventorié | `ETABLI_PAR_C0A` |
| `m11e_res7100/snapshot_600` | identifié et inventorié | `ETABLI_PAR_C0A` |
| `Potential` dans PartType0/1/2/4 | absent | `ETABLI_PAR_C0A` |
| PartTypes présents | 0, 1, 2, 4 | `ETABLI_PAR_C0A` |
| Champs communs utiles | `Coordinates`, `Velocities`, `Masses` | `ETABLI_PAR_C0A` |
| Champs gaz utiles | `Density`, `InternalEnergy`, `SmoothingLength`, `NeutralHydrogenAbundance`, `StarFormationRate` | `ETABLI_PAR_C0A` |
| Centre galactique explicite | absent du snapshot | `ETABLI_PAR_C0A` |
| Vitesse système explicite | absente du snapshot | `ETABLI_PAR_C0A` |
| Attributs explicites `UnitLength/UnitMass/UnitVelocity` | absents du snapshot | `ETABLI_PAR_C0A` |
| G1 | `INDISPONIBLE` | `ETABLI_PAR_C0A` |
| G2 | `A_INSTRUIRE` | `ETABLI_PAR_C0A` |
| C0-A | `SUSPENDUE_COEXISTENCE_CALCUL` | `ETABLI_PAR_C0A` |

Aucun HDF5 n'a été rouvert pour C0-B.

### 2.2 Contrôle léger de coexistence

Le checkout directeur était propre, sur `main`, au commit
`05e13bb7c07d2d070d16574c3c58edf488bea8d0`. Les processus locaux pertinents
de SENT-0F2 attempt2 étaient encore présents. La présente porte retient donc :

```text
COEXISTENCE = ACTIVE
```

Un worktree distinct a été créé à partir de ce commit. Le HEAD, l'index et
l'arbre du checkout directeur sont restés inchangés.

## 3. Contrat d'unités FIRE-2/GIZMO

### 3.1 Autorités spécifiques

La diffusion FIRE-2 DR1 documente les unités HDF5 et les correspondances de
PartTypes. Les petits fichiers publics `gizmo_parameters.txt-usedvalues` de
`m11d_res7100` et `m11e_res7100` donnent en outre, identiquement pour les deux
runs :

| Paramètre | Valeur | Statut |
| --- | ---: | --- |
| `ComovingIntegrationOn` | 1 | `DOCUMENTE` |
| `HubbleParam` | 0.68 | `DOCUMENTE` |
| `UnitLength_in_cm` | `3.08568e21` | `DOCUMENTE` |
| `UnitMass_in_g` | `1.989e43` | `DOCUMENTE` |
| `UnitVelocity_in_cm_per_s` | `100000` | `DOCUMENTE` |

Les trois unités internes correspondent respectivement à 1 kpc,
`10^10 M_sun` et 1 km/s. En sortie cosmologique, les facteurs `a` et `h`
ci-dessous restent nécessaires. Pour les snapshots, `a` est `Header/Time` et
`h` est `Header/HubbleParam`. DR1 place `snapshot_600` à `z = 0`, donc
`a = 1` dans la convention de diffusion ; les deux simulations relèvent de la
cosmologie Planck `h = 0.68` du tableau 1 de DR1.

### 3.2 Chaîne de conversion

Pour une valeur brute `q_HDF5`, la chaîne normative est :

```text
q_HDF5 -> unité de code publiée -> facteurs a/h -> quantité physique
```

| Champ | Quantité | Unité brute HDF5 | Dépendance `a` | Dépendance `h` | Unité physique à `z ~= 0` | Preuve | Statut |
| --- | --- | --- | ---: | ---: | --- | --- | --- |
| `Coordinates` | position cartésienne comobile | `h^-1 kpc` comobile | multiplier par `a` | diviser par `h` | `x_phys = x_HDF5 / 0.68` kpc | DR1 §4.2 ; paramètres propres | `DOCUMENTE` |
| `Velocities` | vitesse particulière 3D | `sqrt(a) km s^-1` | multiplier par `sqrt(a)` | aucune | `v_pec = v_HDF5` km/s | DR1 §4.2 | `DOCUMENTE` |
| `Masses` | masse de particule/cellule | `10^10 h^-1 M_sun` | aucune | diviser par `h` | `m = q_HDF5 10^10/0.68 M_sun` | DR1 §4.2 | `DOCUMENTE` |
| `Density` | densité massique du gaz | `10^10 h^2 a^-3 M_sun kpc^-3` | diviser par `a^3` | multiplier par `h^2` | `rho = q_HDF5 10^10 (0.68)^2 M_sun kpc^-3` | DR1 §4.2 | `DOCUMENTE` |
| `SmoothingLength` | rayon complet de support du noyau de voisinage | `h^-1 kpc` comobile | multiplier par `a` | diviser par `h` | `H = q_HDF5/0.68` kpc | DR1 §4.2 | `DOCUMENTE` |
| `InternalEnergy` | énergie interne spécifique | `km^2 s^-2` | aucune | aucune | `u = q_HDF5 (km/s)^2` | DR1 §4.2 | `DOCUMENTE` |

Points normatifs :

1. `Velocities` ne doit pas être traitée comme une vitesse comobile ordinaire
   à multiplier par `a` : le facteur publié est `sqrt(a)`.
2. `SmoothingLength` est le rayon de support compact du noyau, et non le
   softening équivalent Plummer.
3. Les différences de position doivent appliquer la convention périodique
   avant conversion physique.
4. Les soustractions de vitesse doivent être faites après conversion dans la
   même convention de vitesse particulière que la vitesse d'hôte.
5. Toute implémentation future enregistrera `a`, `h`, les unités internes et la
   constante gravitationnelle utilisée dans son manifeste. La valeur numérique
   et la source de `G` dans le système `kpc`, `km/s`, `M_sun` sont
   `A_RATIFIER` avant le premier test de solveur.

### 3.3 Constante gravitationnelle

La valeur conventionnelle candidate dans le système de sortie est :

```text
G_conv = 4.300917270e-6 kpc (km/s)^2 M_sun^-1
```

Elle découle du paramètre solaire nominal `GM_sun` de la résolution IAU 2015 B3
et de la conversion `kpc`/`km s^-1`. CODATA devient pertinent si `M_sun` est
rattachée au kilogramme plutôt qu'au paramètre nominal. La convention, la
version et la cohérence avec les constantes du changeset GIZMO seront inscrites
au manifeste futur. L'arrondi affiché est très inférieur aux écarts de quelques
dizaines de parties par million possibles entre conventions ; leur pertinence
scientifique reste `A_RATIFIER` contre le budget G2.

## 4. Contrat de softening gravitationnel

### 4.0 Nomenclature normative

Aucune valeur numérique n'est appelée simplement « softening ». Les cinq
objets suivants ne sont pas interchangeables :

| Symbole | Objet physique/numérique | Où il apparaît | Relation aux autres | Statut |
| --- | --- | --- | --- | --- |
| `H_kernel` | rayon complet de support compact du kernel de masse M4 | calcul de voisinage et loi de force spline | rayon au-delà duquel la source redevient exactement newtonienne | `DOCUMENTE` |
| `epsilon_Plummer` | longueur d'une loi de Plummer donnant une résolution de force conventionnellement équivalente ; ce n'est pas la loi exécutée | tableaux FIRE, paramètres GADGET/GIZMO historiques et comparaisons entre codes | conversion dépendante du kernel | `CONVENTION_EXPLICITE` |
| `Delta_x_FIRE` | espacement interélément `Delta_x=(m_i/rho_i)^(1/3)` en 3D, utilisé comme échelle de résolution FIRE | Hopkins et al. 2018 §4.2.2 | FIRE pose dans cette section `epsilon_FIRE = h_i = Delta_x_FIRE` | `DOCUMENTE` |
| `SmoothingLength_HDF5` | champ sauvegardé pour le gaz ; malgré son nom SPH historique, rayon maximal de recherche/support | snapshot, PartType0 | `SmoothingLength_HDF5 = H_kernel` dans la documentation de sortie GIZMO | `DOCUMENTE` |
| `softening_param_code` | `SofteningGas/Halo/Disk/Stars` et `MaxPhys` dans les fichiers propres aux runs | fichier de paramètres ; minimum si l'espèce est adaptative, valeur fixe sinon | convention GADGET/GIZMO annoncée comme approximativement Plummer-équivalente | `CONVENTION_EXPLICITE` |

| Correspondance publiée | Convention et portée | Exactitude | Source primaire | Statut |
| --- | --- | --- | --- | --- |
| `SmoothingLength_HDF5 = H_kernel` | format GIZMO, gaz | identité de définition du champ sauvegardé | guide GIZMO, `SmoothingLength` | `DOCUMENTE` |
| `H_kernel ~= 2.8 epsilon_Plummer` | cubic spline/M4 du guide GIZMO ; gaz ou collisionnel utilisant ce kernel | facteur de conversion conventionnel annoncé « 2.8 par exemple » ; valeur exacte imprimée par le code au démarrage | guide GIZMO, `KERNEL_FAC_FROM_FORCESOFT_TO_PLUMMER` | `CONVENTION_EXPLICITE` |
| `epsilon_FIRE = h_i = Delta_x_FIRE` | définition de résolution adoptée dans FIRE-2 §4.2.2 | identité de notation dans cet article, pas identité avec le champ HDF5 | Hopkins et al. 2018, éq. 9 et §4.2.2 | `DOCUMENTE` |
| `epsilon_Plummer ~= (2/3) epsilon_FIRE` | kernel FIRE-2 par défaut ; même forme déclarée pour gaz, étoiles et DM | approximation publiée | Hopkins et al. 2018 §4.2.2 | `DOCUMENTE` |
| `H_kernel ~= 2 epsilon_FIRE` | guide GIZMO, cubic spline avec nombre effectif de voisins 32 | relation générale/documentaire à confirmer pour le changeset historique | guide GIZMO, définition de `KernelLength` | `A_RATIFIER` |

Les facteurs `2.8` et `2/3` proviennent donc de deux choix de paramétrisation
historiques et sont tous deux approximatifs dans les textes cités. Ils ne sont
pas imposés comme une chaîne algébrique exacte. En particulier, la v0.2
interdit de déduire exactement `H_kernel` de `Delta_x_FIRE`, ou inversement.
Pour l'implémentation future, le gaz utilisera directement
`SmoothingLength_HDF5`; la conversion des paramètres fixes vers `H_kernel`
sera ratifiée contre le changeset GIZMO `415:2f1ff61cf4c2` ou sa sortie de
démarrage qualifiée avant tout calcul.

### 4.1 Réglages propres à `m11d_res7100` et `m11e_res7100`

Les deux fichiers de compilation publics activent
`ADAPTIVE_GRAVSOFT_FORGAS`. Ils n'activent pas le softening adaptatif pour les
espèces collisionnelles. Ils utilisent le réglage de voisinage
`DesNumNgb = 32` et `MinGasHsmlFractional = 1`.

Les noms historiques GADGET/GIZMO se mappent ainsi : `Gas` -> PartType0,
`Halo` -> PartType1, `Disk` -> PartType2, `Stars` -> PartType4. DR1 confirme
que PartType1 est le DM haute résolution du zoom et PartType2 le DM basse
résolution du volume cosmologique.

À bas redshift, `MaxPhys` plafonne le paramètre de code en unités physiques.
La conversion exacte de ce paramètre à `z = 0` est
`softening_param_code,phys = MaxPhys/h` kpc. Son interprétation comme
`epsilon_Plummer` est une convention de comparaison documentée, non une loi de
Plummer exécutée. Les nombres du tableau 1 de DR1 sont arrondis.

| Espèce | PartType | Fixe/adaptatif | Valeur ou règle à `z = 0` | Kernel | Source | Statut |
| --- | ---: | --- | --- | --- | --- | --- |
| gaz | 0 | adaptatif, avec minimum | `H_kernel,i = SmoothingLength_HDF5,i a/h`; minimum du paramètre de code `0.0007/0.68 kpc ~= 1.03 pc`, publié en convention Plummer-équivalente | spline M4 compact | config/paramètres propres ; DR1 tableau 1 et §4.2 ; Hopkins et al. 2018 §2.2/4.2 | `DOCUMENTE` |
| DM haute résolution | 1 | fixe | `softening_param_code,phys = 0.028/0.68 kpc ~= 41.2 pc`, convention Plummer-équivalente (DR1 : 40 pc) | spline M4 compact | paramètres propres ; DR1 tableau 1 | `DOCUMENTE` |
| DM basse résolution | 2 | fixe | `softening_param_code,phys = 0.2/0.68 kpc ~= 294 pc`, convention Plummer-équivalente | spline M4 compact | `SofteningDiskMaxPhys` propre aux deux runs ; mapping DR1 | `DOCUMENTE` |
| étoiles | 4 | fixe | `softening_param_code,phys = 0.0028/0.68 kpc ~= 4.12 pc`, convention Plummer-équivalente (DR1 : 4 pc) | spline M4 compact | paramètres propres ; DR1 tableau 1 | `DOCUMENTE` |

Au-dessus de la transition `a = 0.1` (`z = 9`), les valeurs de code comobiles
sont respectivement `SofteningGas = 0.007`, `SofteningStars = 0.028`,
`SofteningHalo = 0.28` et `SofteningDisk = 2`. En dessous de `z = 9`, les
`MaxPhys` ci-dessus rendent les minima/fixes physiques. Cette règle est
cohérente avec la prescription FIRE-2 publiée « comobile à haut redshift,
physique à bas redshift ».

### 4.2 Loi de force de masse pour `G2-FIELD`

La loi de source n'est pas une force de Plummer. GIZMO représente les éléments
par une distribution de masse spline M4 compacte :

- le champ d'une source est exactement newtonien pour `r >= H_kernel` ;
- `H_kernel ~= 2.8 epsilon_Plummer` est la conversion conventionnelle du guide
  pour le cubic spline, et non une identité universelle ;
- pour le gaz, `H_kernel` sera lu directement dans `SmoothingLength_HDF5` ;
- pour PartType1, PartType2 et PartType4, la conversion de
  `softening_param_code` vers `H_kernel` devra reproduire le facteur du
  changeset historique qualifié, pas seulement un `2.8` recopié ;
- le guide GIZMO actuel documente par défaut l'emploi du plus grand support
  lors d'une paire à softenings différents ; la conformité exacte du changeset
  `415:2f1ff61cf4c2` et de ses limiteurs reste `A_RATIFIER`.

La note DR1 « minimum adaptive force softening (Plummer equivalent) ... equals
the hydrodynamic smoothing kernel » est conservée comme terminologie historique :
elle documente le couplage des résolutions gravitationnelle et hydrodynamique,
mais n'autorise pas l'égalité numérique silencieuse
`epsilon_Plummer = SmoothingLength_HDF5`.

### 4.3 `G2-FIELD`, `G2-EOM` et corrections adaptatives

**`G2-FIELD`** est le champ instantané associé aux sources de masse FIRE,
reconstruit avec le kernel, les softenings et les conditions de bord déclarés,
et évalué à des points tests sans masse :

```text
g_FIELD(x) = champ des distributions de masse adoucies, à état figé
```

Le point test n'acquiert ni densité, ni voisinage, ni softening adaptatif. Cet
objet répond à une équation de Poisson adoucie spécifiée et reste décomposable
par espèces.

**`G2-EOM`** est l'accélération gravitationnelle effectivement utilisée dans
l'équation du mouvement d'un élément FIRE identifié :

```text
a_EOM,i = interaction gravitationnelle symétrisée + corrections adaptatives
```

Pour une particule à softening fixe, la dette adaptative ne s'applique pas.
Pour le gaz, `ADAPTIVE_GRAVSOFT_FORGAS` lie le softening au kernel/volume local.
Comme `h_i` dépend de la densité et donc des positions des voisins, la variation
du Lagrangien discret contient des dérivées supplémentaires. Price & Monaghan
(2007), éq. 27, montrent que le premier terme est la force adoucie et que le
terme adaptatif additionnel restaure la conservation d'énergie ; le guide
GIZMO annonce une formulation lagrangienne pleinement conservative apparentée,
avec des choix de symétrisation propres au code.

Ces termes appartiennent à l'équation du mouvement de l'élément adaptatif. Ils
ne définissent pas automatiquement un champ universel fonction de la seule
position : ils dépendent notamment du voisinage, de la relation `h(rho)`, des
dérivées du kernel/potentiel par rapport à `h`, des facteurs de type `Omega` et
`zeta`, des planchers/plafonds et de la symétrisation interespèces. Aucun terme
`grad-h` ne sera redistribué comme une densité source gazeuse supplémentaire
sans dérivation démontrée.

Une reproduction exacte de `G2-EOM` demanderait au minimum :

1. le changeset et les options de compilation exacts ;
2. la relation densité-voisinage-softening et ses dérivées ;
3. les voisins, masses, positions, densités et `H_kernel` cohérents ;
4. les règles de paire, limites et branchements du code ;
5. un oracle EOM synthétique qualifié avant FIRE.

Les champs publics nécessaires à une partie de cette reconstruction existent,
mais leur suffisance algorithmique n'est pas démontrée. L'amplitude de
`a_EOM-g_FIELD` dans `m11d/m11e` est `NON_ETABLIE`. La v0.2 ne la suppose ni
nulle ni négligeable.

### 4.4 Conditions périodiques, `BoxSize` et mode moyen

Deux questions sont séparées :

1. le run original calculait-il un champ périodique TreePM ? **Oui,
   `DOCUMENTE`** ;
2. le snapshot public permet-il d'en reproduire exactement toutes les sources
   et conventions ? **`NON_ETABLI` à ce stade**.

Les petits fichiers propres à `m11d_res7100` et `m11e_res7100` sont identiques
sur les points suivants : `ComovingIntegrationOn=1`, `BoxSize=58480` unités de
code, soit `58.480 h^-1 Mpc` comobiles, `PERIODIC`, `PMGRID=1024`,
`PM_PLACEHIGHRESREGION=1+2+16`, `PM_HIRES_REGION_CLIPPING=2000`, et changeset
GIZMO `415:2f1ff61cf4c2`. Le bitmask de placement haute résolution vise les
types 0, 1 et 4 ; cela ne prouve pas que PartType2 soit absent du PM global.

GADGET-2 §2.1 définit, pour la boîte périodique, un potentiel particulier où la
densité moyenne est soustraite. Sa partie PM emploie la fonction de Green
périodique en Fourier ; le mode uniforme ne produit donc pas l'accélération
particulière recherchée. La convention exacte du mode `k=0`, les facteurs
comobiles/physiques et la normalisation du changeset FIRE restent à qualifier
ensemble, et non par analogie avec une bibliothèque actuelle.

| Élément | Run original | Snapshot public / état C0-A | Suffisant pour reproduction ? | Statut |
| --- | --- | --- | --- | --- |
| `BoxSize` | `58480` unités de code, périodique | concordance avec l'attribut Header du fichier local non rouverte dans C0-B | non avant vérification de concordance | `A_RATIFIER` |
| PartType0 | source baryonique ; inclus dans région PM haute résolution | présent | oui pour les masses instantanées si le snapshot est complet | `INFERENCE_CONTROLEE` |
| PartType1 | DM haute résolution ; inclus dans région PM haute résolution | présent | même condition | `INFERENCE_CONTROLEE` |
| PartType2 | DM basse résolution du volume cosmologique | présent | essentiel au champ longue portée ; couverture spatiale complète non réauditée | `A_RATIFIER` |
| PartType4 | étoiles ; inclus dans région PM haute résolution | présent | oui pour les masses instantanées si le snapshot est complet | `INFERENCE_CONTROLEE` |
| espèces éventuelles PT3/PT5 | aucune présence établie dans C0-A | groupes absents de l'inventaire d'entrée | suffisant seulement si leur nombre total est nul | `ETABLI_PAR_C0A`, suffisance `A_RATIFIER` |
| fond moyen | soustrait dans le potentiel particulier | pas un tableau de particules dédié | reconstructible seulement avec convention et couverture complètes | `A_RATIFIER` |
| images périodiques | générées par la condition de bord | non stockées comme particules | dérivables de `BoxSize` si toutes les sources sont disponibles | `INFERENCE_CONTROLEE` |
| PM longue portée | `PMGRID=1024` et région haute résolution configurée | état de grille/forces non sauvegardé ; positions de sources annoncées dans un snapshot complet DR1 | recalcul possible en principe, fidélité exacte non démontrée | `NON_ETABLI` |

DR1 appelle ces produits des « full/complete snapshots » et annonce toutes les
propriétés stockées de toutes les particules. Cette déclaration soutient la
possibilité de reconstruction, mais ne remplace pas la vérification de la
couverture de la boîte, des comptes par espèce et du `BoxSize` du fichier visé.
Aucun HDF5 n'est rouvert pour fermer cette dette dans C0-B.

La grandeur candidate reste différentielle dans le référentiel hôte :

```text
g_FIELD,rel(x) = g_FIELD(x) - g_FIELD(x_center)
```

La soustraction retire une accélération uniforme, pas les marées. Jusqu'à la
fermeture de la matrice et la réussite de T7 :

```text
D-PERIODIC = PROPOSITION_SOUS_CONDITION
D-LOCAL-CONTROL = CONTROLE local isolé, jamais promu par commodité
```

La ratification de `D-PERIODIC` exigera la concordance `BoxSize`, la preuve de
couverture des sources, la convention du mode moyen et un oracle périodique.
À défaut, la limite devra être publiée comme `E_boundary`; elle ne pourra pas
être absorbée dans l'erreur du solveur.

## 5. Référentiel galactique et centrage

### 5.1 C1 — référentiel FIRE publié

Pour la suite Core, `track/host_coordinates.hdf5` contient :

| Objet | Contenu publié | Unité | Construction | Statut |
| --- | --- | --- | --- | --- |
| `host.position` | position 3D de l'hôte, tableau `Nsnapshot x Nhost x 3` | kpc comobile | étoiles appartenant à l'hôte à `z=0`, suivies dans les snapshots ; centre recalculé à chaque époque | `DOCUMENTE` |
| `host.velocity` | vitesse 3D de l'hôte, même forme | km/s | même population suivie | `DOCUMENTE` |
| `host.rotation` | tenseur de rotation, `Nsnapshot x Nhost x 3 x 3` | sans dimension | tenseur d'inertie de la galaxie principale | `DOCUMENTE` |

DR1 recommande explicitement cette route pour localiser l'hôte de la suite
Core. Le produit n'a pas été téléchargé pendant C0-B. Son acquisition et sa
provenance relèvent d'une autorisation ultérieure conforme à `#64`.

Les catalogues `halo/rockstar_dm/halo_NNN.hdf5`, construits avec
ROCKSTAR-GALAXIES sur le DM, fournissent notamment position, vitesse et
propriétés du halo. L'hôte primaire est le halo le plus massif non contaminé
par le DM basse résolution dans la région zoom. Les fichiers associés
`star_NNN.hdf5` fournissent notamment centre de masse et vitesse stellaires,
`star.radius.50`, `star.radius.90`, dispersions de vitesse et masse de DM basse
résolution. Ces catalogues sont une route de comparaison, pas une preuve que le
centre stellaire et le centre dynamique coïncident.

### 5.2 C2 — contrôle indépendant depuis les particules

La route C2 proposée est fixée sans référence à une courbe attendue :

1. convertir positions et masses selon le contrat d'unités ;
2. appliquer les distances périodiques ;
3. obtenir séparément un centre stellaire et un centre PartType1 par sphères
   rétrécissantes/centre de masse itératif ;
4. arrêter chaque itération selon un critère fondé sur la résolution, le nombre
   effectif de particules et la stabilité entre deux itérations, non selon la
   courbe de rotation ;
5. définir la vitesse système par un estimateur robuste des vitesses dans une
   ouverture fixée autour du centre de position ;
6. conserver les résultats des deux traceurs, leurs incertitudes de
   rééchantillonnage et leur sensibilité aux paramètres d'itération.

DR1 documente une méthode stellaire apparentée : centre de masse initial,
sphère initiale d'environ 1 Mpc, réduction du rayon d'environ 50 % à chaque
itération jusqu'à une échelle d'environ 10 pc, puis vitesse dans une ouverture
fixe typiquement inférieure ou égale à 8 kpc. Ces nombres sont descriptifs de
la méthode publiée ; ils ne sont pas automatiquement ratifiés pour C2. Les
valeurs exactes de l'ouverture, du facteur de réduction et de l'arrêt seront
gelées après tests synthétiques de centrage et avant toute analyse cible.

### 5.3 Concordance C1/C2

Les critères numériques sont `A_RATIFIER`, mais leur mode de construction est
préenregistré :

- tolérance spatiale : maximum d'un plancher lié aux softenings des traceurs et
  de l'incertitude de stabilité/rééchantillonnage de C2 ;
- tolérance de vitesse : maximum de l'incertitude de l'estimateur de vitesse et
  d'un plancher lié à la précision scientifique minimale ultérieure ;
- les multiplicateurs de sécurité sont fixés sur simulations synthétiques et
  tests de stabilité, jamais sur l'écart cinématique-gravité de `m11d/m11e`.

Réaction préenregistrée :

| Résultat | Réaction |
| --- | --- |
| C1 et C2 concordent dans les tolérances | C1 est le référentiel primaire publié ; C2 reste le contrôle indépendant |
| désaccord limité à une méthode C2 instable | déclarer l'instabilité, corriger le protocole sur synthétiques, puis recommencer avant toute courbe cible |
| désaccord C1/C2 robuste | suspendre le résultat de référence ; exécuter la sensibilité symétrique préenregistrée sur tous les centres, sans sélectionner celui qui réduit l'écart scientifique |
| absence de référentiel stable | verdict futur `REFERENTIEL_NON_UNIQUE`; aucune courbe G2 de référence |

Les écarts de position et de vitesse ne seront pas fusionnés : `E_center`
mesure la sensibilité du champ et de ses composantes au centre retenu ;
`E_velocity_frame` mesure la sensibilité de la cinématique O1 à la vitesse
système. Le second n'est pas une erreur du champ statique, mais entre dans la
comparaison O1/G2. Les deux enveloppes seront produites symétriquement.

## 6. Orientation du disque

### 6.1 Route principale candidate

La candidate `PROPOSITION` est : axe `z` parallèle au moment angulaire du HI,
après fixation du centre et de la vitesse système. Elle est motivée par la
comparaison intrinsèque future avec la cinématique du gaz neutre, mais elle
présente quatre risques :

- dépendance au rayon choisi ;
- contamination par gaz extraplanaire, flux entrant ou sortant ;
- axe mal conditionné ou multi-composante pendant une fusion, particulièrement
  pertinent pour `m11e` ;
- circularité méthodologique si l'on retient le gaz ou le rayon qui rapproche
  ensuite cinématique et gravité.

Le rayon `R_orient` sera défini par une taille stellaire publiée indépendante
du résidu cible, par exemple une règle gelée à partir de `star.radius.90`, avec
éventuel plafond physique. Le multiplicateur et le plafond sont `A_RATIFIER`
sur critères de résolution, de nombre de traceurs et de portée physique, avant
toute lecture de l'écart final. Il n'y aura pas de sélection primaire par
circularité orbitale, car celle-ci requiert déjà une estimation du potentiel.

La qualité de l'axe HI sera évaluée par : norme du moment angulaire, incertitude
angulaire par rééchantillonnage, et stabilité dans une suite préenregistrée
d'ouvertures emboîtées. Les ouvertures ne seront pas ajoutées après inspection
du résultat cible.

### 6.2 Contrôles alternatifs

Les contrôles suivants seront calculés symétriquement :

- moment angulaire stellaire dans la même règle d'ouverture ;
- axes principaux stellaires ;
- `host.rotation` publié ;
- axe HI avec une définition physique alternative du gaz neutre, seulement si
  cette définition est fixée avant le résultat cible.

Un désaccord supérieur à une tolérance angulaire `A_RATIFIER` ne déclenchera
pas le choix de l'axe donnant la courbe la plus régulière. Il déclenchera soit
une enveloppe de sensibilité sur toutes les orientations préenregistrées, soit
le statut futur `DISQUE_NON_ORIENTABLE`.

`E_orientation` est l'enveloppe obtenue en reprojetant le même champ vectoriel
selon toutes les orientations préenregistrées. Elle reste distincte de
`E_center` et de `E_solver`; une orientation instable ne sera pas « corrigée »
par changement de paramètres gravitationnels.

## 7. Familles de solveurs gravitationnels

### 7.1 Ordre de décision

L'ordre obligatoire est :

```text
distribution de masse et force représentées par FIRE
-> approximation numérique admissible
-> famille candidate
-> coût
```

La taille des snapshots ne justifie ni un changement de kernel, ni l'abandon
de PartType2, ni le remplacement du champ cylindrique par une masse sphérique.

### 7.2 Comparaison

Soit `N` le nombre de sources, `M` le nombre de points d'évaluation et `Ng` le
nombre de cellules d'une grille 3D.

| Méthode | Complexité indicative | RAM | Précision contrôlable par | Softening | Géométrie | Avantage | Risque principal | Verdict |
| --- | ---: | ---: | --- | --- | --- | --- | --- | --- |
| somme directe | `O(N M)` | `O(N + M)` | arithmétique et kernel exact | M4 exact possible | isolée ; périodicité coûteuse | oracle sans erreur d'ouverture sur petits tests | rédhibitoire à l'échelle FIRE | `CONTROLE` |
| arbre Barnes-Hut / multipolaire hiérarchique | typiquement `O((N+M) log N)` | `O(N)` | angle d'ouverture, critère géométrique, ordre multipolaire | M4 exact au proche champ possible | isolée par défaut ; correction périodique nécessaire | cibles arbitraires, décomposition facile, proche de la partie arbre de GIZMO | erreur anisotrope, périodicité/PM manquante, dépendance au critère d'ouverture | `CANDIDATE` |
| Fast Multipole Method | asymptotiquement `O(N+M)` | `O(N+M)` | ordre d'expansion et tolérance | proche champ M4 spécialisé nécessaire | isolée ou périodique selon implémentation | bonne scalabilité et contrôle d'erreur potentiel | adaptation du kernel, disponibilité d'une implémentation validée, complexité d'intégration | `CANDIDATE_SECONDAIRE` |
| Particle-Mesh / FFT | `O(N + Ng log Ng + M)` | `O(Ng)` | maille, schéma de dépôt/interpolation, déconv. | kernel effectif mêlé à la grille | périodique naturelle | reproduit le long champ et la densité moyenne cosmologiques | lissage de grille, anisotropie, résolution coûteuse du disque mince | `CONTROLE` |
| TreePM hybride | arbre + `O(Ng log Ng)` | `O(N + Ng)` | séparation court/long rayon, ouverture, grille | M4 au court rayon ; PM au long rayon | périodique | famille la plus proche du solveur effectivement utilisé par FIRE-2 | mise en œuvre et validation les plus exigeantes ; paramètres de séparation à geler | `CANDIDATE` |

### 7.3 Bibliothèques existantes

`pytreegrav` 1.1.4 est `A_TESTER` comme brique de champ local : sa publication
JOSS documente un octree inspiré de GADGET-2, des points cibles arbitraires, la
somme directe de contrôle, le kernel spline M4 avec rayon par particule et
l'emploi du plus grand softening pour une paire recouvrante. Il ne documente
pas une reproduction complète du PM périodique FIRE ni les termes `grad-h` des
équations du mouvement. Il ne peut donc pas devenir seul la référence
`D-PERIODIC` sans extension et validation.

Le code GIZMO et son changeset public sont la référence algorithmique pour le
kernel. Lancer GIZMO comme solveur n'est ni proposé ni autorisé dans C0-B.
Aucune bibliothèque n'a été installée et aucun logiciel n'est choisi
définitivement.

### 7.4 Pré-décision recommandée

La route à auditer est un hybride :

1. court champ par arbre avec noyau M4 et softenings par source ;
2. long champ périodique par PM ou correction périodique validée ;
3. somme directe sur problèmes synthétiques et petits ensembles comme oracle ;
4. PM seul comme contrôle de grande échelle ;
5. FMM seulement si une implémentation supportant le même proche champ et les
   mêmes conditions périodiques est identifiée.

Cette pré-décision est `PROPOSITION`, pas un choix de logiciel ratifié. Elle ne
peut atteindre F2 tant que la suffisance des sources et des conditions de bord
périodiques n'est pas établie ; avant cela, une reconstruction isolée relève de
F1 et reste un contrôle local.

## 8. Sorties primaires, fidélité et règle `FIELD -> EOM`

### 8.1 Champ primaire

Le produit primaire futur est `G2-FIELD` dans un repère cylindrique gelé :

```text
g_R_FIELD(R,z), g_z_FIELD(R,z)
```

Le produit minimal enregistrera aussi les coordonnées, `g_x/g_y/g_z`, la
composante azimutale de contrôle, unités, centre, rotation, kernel, softenings,
conditions de bord, paramètres du solveur, provenance et budget d'erreur.

Si et seulement si une porte EOM distincte devient nécessaire, elle produira
pour des éléments identifiés :

```text
a_R_EOM,i, a_z_EOM,i
```

Ces sorties ne seront ni substituées ni mélangées. Seulement après validation
du champ, la transformation secondaire pourra être calculée :

```text
v_grav,FIELD(R) = sqrt(R |g_R_FIELD(R,0)|)
```

Le signe radial devra être entrant. La formule sphérique
`v_sph(r)=sqrt(G M(<r)/r)` reste un contrôle F0 et ne remplace jamais le champ
d'un disque aplati.

### 8.2 Hiérarchie de fidélité gravitationnelle

| Niveau | Objet | Usage autorisé | Limite |
| --- | --- | --- | --- |
| F0 | Newtonien sphérique `GM(<r)/r` | contrôle secondaire | perd géométrie et champ vertical |
| F1 | champ local isolé, masses réelles + kernel | contrôle local et bords croissants | omet périodicité et marées non locales |
| F2 | `G2-FIELD` avec conditions de bord suffisamment fidèles | référence de champ candidate | ne reproduit pas automatiquement l'EOM adaptative du gaz |
| F3 | `G2-EOM` pour éléments adaptatifs | référence de l'équation du mouvement si scientifiquement requise | coût et reproductibilité supérieurs ; dépend de l'état de l'élément |
| F4 | accélérations internes originales FIRE | oracle potentiel seulement si un jour disponibles et qualifiées | absentes des snapshots actuels ; provenance et signification à établir |

Deux inférences sont interdites : `facile à calculer = plus vrai` et
`plus fidèle algorithmiquement = automatiquement nécessaire
scientifiquement`. Le niveau requis dépend de la taille de l'effet étudié et
du budget d'erreur ratifié.

### 8.3 Règle scientifique `FIELD -> EOM`

Avant `m11d/m11e`, une métrique de différence FIELD/EOM, son domaine et son
échelle de normalisation seront ratifiés sur synthétiques et sur le budget de
la plus petite différence scientifique visée. Aucun seuil numérique n'est fixé
ici ; tous sont `A_RATIFIER` avant inspection du résidu cible.

| Cas | Constat préenregistré | Décision |
| --- | --- | --- |
| A | FIELD et EOM démontrés équivalents dans le budget pertinent | `G2-FIELD` peut servir de référence pour le test considéré |
| B | différence bornée, non négligeable mais sous-dominante | conserver `G2-FIELD` avec enveloppe systématique `E_EOM` explicite |
| C | différence comparable à l'effet scientifique étudié | `G2-FIELD` seul est insuffisant ; ouvrir une porte `G2-EOM` distincte |
| D | différence impossible à borner avec données/algorithmes publics | verdict `LIMITATION_REPRODUCTIBILITE_EOM` |

La ratification comparera `E_EOM` au budget scientifique annoncé et aux autres
planchers d'erreur, jamais au résidu observé entre cinématique et gravité dans
les deux galaxies.

### 8.4 Question du premier test scientifique

Le premier test C7-GAL-C ne demandera pas « FIRE reproduit-il parfaitement sa
propre accélération interne ? », mais :

> Une reconstruction contrôlée du champ gravitationnel pertinent permet-elle
> d'évaluer indépendamment l'écart entre cinématique du gaz et support
> gravitationnel, et quelle fidélité à l'équation du mouvement FIRE est
> nécessaire pour rendre cet écart interprétable ?

Il comparera d'abord une route cinématique intrinsèque O1 à `G2-FIELD`. La
porte FIELD/EOM dira ensuite si F2 suffit ou si F3 est nécessaire. La
projection et la pseudo-observation O2 restent ultérieures.

## 9. Décomposition des composantes

Au niveau FIELD, le solveur produira séparément :

```text
g_FIELD,gas

g_FIELD,PT1

g_FIELD,PT2

g_FIELD,PT4

g_FIELD,total
```

PartType1 est le DM haute résolution et PartType2 le DM basse résolution. PT2
ne sera ni fusionné silencieusement avec PT1, ni omis selon une attente sur sa
position. Le test de fermeture FIELD est vectoriel :

```text
Delta_close,FIELD = g_FIELD,total
                    - sum(g_FIELD,gas, g_FIELD,PT1,
                          g_FIELD,PT2, g_FIELD,PT4)
```

La tolérance dépendra de `E_solver`, de l'arrondi et de la stratégie de somme ;
elle sera gelée avant FIRE. Une bonne fermeture ne valide ni le kernel ni les
conditions de bord.

Au niveau EOM, une décomposition ne sera publiée que si la dérivation du code
la justifie. Les interactions de masse par espèce et la correction adaptative
de l'élément cible devront alors rester séparées :

```text
a_EOM,i = sum_s a_pair,i<-s + a_adapt,i
```

`a_adapt,i` ne sera pas attribuée silencieusement à `g_FIELD,gas` comme si elle
provenait d'une nouvelle densité. Cette séparation décrit l'origine numérique
des termes ; elle ne constitue aucun verdict sur la matière sombre.

## 10. Validation synthétique hiérarchisée avant FIRE

Aucun test n'est exécuté dans C0-B. Chaque futur test sépare trois étages.

### 10.1 Niveau S — erreur du solveur

Pour exactement les mêmes particules, positions, masses, `H_kernel`, conditions
de bord et points d'évaluation, la somme directe avec la même loi de paire est
l'oracle discret isolé. Arbre, FMM, PM et hybride sont comparés individuellement
à cet oracle :

```text
E_solver = résultat_méthode - oracle_discret_commun
```

Pour un problème périodique, l'oracle doit lui-même être périodique et qualifié
(Ewald, solution de Fourier ou équivalent) ; une somme directe isolée n'est pas
un oracle de T7.

### 10.2 Niveau D — erreur de discrétisation

À solveur exact fixé, comparer la réalisation particulaire à l'espérance du
continuum représenté avec le même kernel lorsque celle-ci est disponible. Ce
niveau mesure nombre fini, shot noise, placement spatial et réalisation
aléatoire :

```text
E_discrete = oracle_discret - continuum_avec_kernel
```

Plusieurs réalisations à graines préenregistrées sont nécessaires. Si le
continuum adouci n'a pas de solution fermée, l'estimation par ensembles et sa
incertitude seront définies avant le test ; elle ne sera pas imputée au solveur.

### 10.3 Niveau K — effet du kernel/softening

Comparer enfin le continuum adouci par le modèle M4 au continuum analytique non
adouci :

```text
E_kernel = continuum_avec_kernel - continuum_non_adouci
```

`E_kernel` est un écart de représentation physique-numérique, pas un défaut du
solveur. Les trois erreurs peuvent être corrélées et ne sont pas additionnées
quadratiquement sans démonstration.

### T1 — loi de force du kernel M4

Tester direction, normalisation, continuité des morceaux polynomiaux,
transition à `H_kernel` et retour newtonien. Comparer la somme directe à une
expression indépendante de la loi M4, y compris pour supports inégaux. T1-S
qualifie l'implémentation de paire ; T1-K documente la différence avec le point
newtonien et avec une force de Plummer. Les conventions `H_kernel`,
`epsilon_Plummer` et `Delta_x_FIRE` restent affichées séparément.

### T2 — sphère de Plummer

- `T2-S` : mêmes particules et softenings, méthodes approximatives contre somme
  directe ;
- `T2-D` : oracle discret contre continuum Plummer soumis au même modèle M4 ou
  son espérance d'ensemble ;
- `T2-K` : continuum adouci contre
  `g(r)=-G M r/(r^2+b^2)^(3/2)` non adouci.

« Plummer » nomme ici la distribution analytique, jamais le kernel FIRE.

### T3 — profil de Hernquist

Appliquer T3-S/D/K sur une forte dynamique radiale. Le masque central sera
fondé avant exécution sur résolution, échantillonnage et kernel. Aucune zone ne
sera retirée parce que son erreur observée est grande.

### T4 — disque de Miyamoto-Nagai

Appliquer T4-S/D/K à `g_R` et `g_z`, dans le plan, hors plan et près de l'axe.
Si une réalisation particulaire est utilisée, la variance entre réalisations
est rapportée séparément de l'erreur du solveur. Ce test est obligatoire pour
la géométrie aplatie.

### T5 — superposition et composantes

Tester séparément : (i) linéarité du continuum analytique ; (ii) fermeture
numérique FIELD à oracle discret commun ; (iii) décomposition/recomposition par
espèce. Une compensation d'erreurs entre composantes ne valide pas le total.

### T6 — invariances

Tester translation, rotation/covariance vectorielle, permutation, changement
cohérent d'unités et partition/recomposition. La graine et la réalisation
restent identiques au niveau S ; les variations de graine relèvent du niveau D.

### T7 — périodicité et fond moyen

Après ratification de la convention périodique, utiliser une distribution
homogène plus perturbation et un mode de Fourier unique. Tester `BoxSize`,
images, soustraction du mode moyen, facteurs comobiles/physiques, accélération
différentielle, PM et raccord court/long. L'oracle sera analytique périodique ou
indépendant qualifié. T7 valide un algorithme ; il ne prouve pas à lui seul que
le snapshot public contient toutes les sources du run.

### T8 — comparaison interméthodes à oracle commun

Sur chaque même entrée discrète, comparer séparément arbre, FMM, PM et hybride
au même oracle direct/périodique qualifié, pour les vecteurs, `g_R_FIELD` et
`g_z_FIELD`. L'accord de plusieurs méthodes approximatives n'est jamais un
vote majoritaire produisant une référence.

## 11. Budget d'erreur G2

Le budget conceptuel est :

```text
E_total = f(E_units, E_center, E_velocity_frame, E_orientation,
            E_discrete, E_kernel, E_solver, E_boundary,
            E_component_closure, E_EOM, E_projection)
```

`f` n'est pas présumée quadratique : indépendance, signe, covariance et
cohérence spatiale devront être établis avant combinaison.

| Source | Nature | Mesurable sur synthétique ? | Mesurable sur FIRE futur ? | Corrélée à | Statut |
| --- | --- | --- | --- | --- | --- |
| `E_units` | conversion `a/h`, unités et `G` | oui, changement cohérent d'unités | oui par manifeste et identités dimensionnelles | kernel, domaine, `G` | `A_RATIFIER` |
| `E_center` | déplacement du point origine | oui, centres injectés | oui par C1/C2 et sensibilité symétrique | orientation, champ différentiel | `A_RATIFIER` |
| `E_velocity_frame` | erreur de vitesse système, propre à O1 | oui, vitesse injectée | oui par C1/C2 | centre, sélection du gaz | `A_RATIFIER` |
| `E_orientation` | rotation du repère et mélange des composantes | oui | oui par axes préenregistrés | centre, domaine radial | `A_RATIFIER` |
| `E_discrete` | échantillonnage fini et shot noise | oui, niveau D/ensembles | seulement par diagnostics de résolution autorisés ultérieurement | kernel, densité, espèce | `PROPOSITION` |
| `E_kernel` | écart continuum adouci/non adouci et convention de support | oui, niveau K | oui par sensibilité préenregistrée, sans changer la référence post hoc | discrétisation, espèce | `A_RATIFIER` |
| `E_solver` | approximation arbre/FMM/PM/hybride | oui, niveau S | oui par convergence numérique bornée | géométrie, kernel, bords | `A_RATIFIER` |
| `E_boundary` | boîte, mode moyen, images, sources manquantes | oui pour l'algorithme T7 | seulement si couverture publique qualifiée | centre différentiel, PM | `NON_ETABLI` |
| `E_component_closure` | arrondi/ordre de somme/décomposition | oui, T5 | oui sur sorties FIELD futures | solveur, dynamique des masses | `A_RATIFIER` |
| `E_EOM` / `grad-h` | passage champ à EOM d'un élément adaptatif | oui sur oracle EOM dédié | non sans porte et reconstruction EOM | densité, voisinage, kernel | `NON_ETABLI` |
| `E_projection` | inclination, faisceau, bruit et inférence O2 | hors G2 ; synthétique O2 futur | futur seulement | orientation, sélection, cinématique | `NON_ETABLI` |

`E_units`, `E_center`, `E_orientation`, `E_discrete`, `E_kernel`, `E_solver`,
`E_boundary` et `E_component_closure` appartiennent au dossier `G2-FIELD`.
`E_EOM` apparaît au passage `G2-FIELD -> G2-EOM`.
`E_velocity_frame` appartient à O1 et à la comparaison O1/G2 ;
`E_projection` n'apparaît qu'au passage intrinsèque vers O2.

## 12. Métriques et tolérances à ratifier

Pour chaque test, enregistrer séparément les niveaux S, D et K. Chaque ligne de
résultat nommera son oracle et enregistrera au minimum :

- erreur relative médiane sur la norme ;
- P95 de l'erreur relative ;
- erreur maximale hors masque analytique préenregistré ;
- angle entre vecteurs numérique et analytique ;
- erreurs séparées sur `g_R` et `g_z` ;
- fermeture des composantes ;
- stabilité au raffinement ;
- biais signé, afin de ne pas masquer une compensation dans une norme absolue.

Lorsque le champ analytique s'annule, l'erreur relative est mal définie. On
utilisera alors une erreur absolue normalisée par une échelle analytique fixée
avant le test. Les masques de singularité, seuils de norme pour l'angle et
planchers de dénominateur sont `A_RATIFIER` avant exécution.

Aucun seuil universel de 1 % n'est imposé. Les tolérances de `E_solver`,
`E_discrete`, `E_kernel`, `E_boundary`, fermeture et FIELD/EOM sont ratifiées
séparément à partir de leur oracle propre, de la résolution FIRE, de la plus
petite différence scientifique annoncée et d'une marge fixée avant cible.
L'accord analytique total ne sera jamais attribué en bloc au solveur.

Si la précision nécessaire à la question scientifique est plus fine que le
plancher démontré par la validation, G2 sera déclarée insuffisante ; les seuils
ne seront pas relâchés après observation.

## 13. Convergence numérique préenregistrée

### 13.1 Paramètres à faire varier

| Famille | Paramètres de convergence |
| --- | --- |
| arbre | angle/critère d'ouverture, ordre multipolaire, précision arithmétique, taille des feuilles |
| FMM | ordre d'expansion, tolérance, séparation proche/lointain |
| PM | nombre et forme des cellules, dépôt, interpolation, déconv., solveur FFT, traitement du mode zéro |
| hybride | échelle de séparation arbre-PM et chacun des paramètres ci-dessus |
| champ évalué | nombre et placement des points, domaine radial, épaisseur et échantillonnage en `z`, traitement de `R=0` |
| physique numérique | kernel, softenings par espèce, règle des paires, périodicité, domaine source, bords |

### 13.2 Règle d'arrêt de raffinement

Une suite géométrique de raffinements et un ordre fixe seront définis avant
FIRE. Au niveau S, chaque raffinement est jugé contre l'oracle discret commun ;
au niveau D, `N` et les réalisations varient à solveur suffisamment précis ; au
niveau K, le modèle adouci reste explicitement distinct du continuum non
adouci. Le raffinement retenu sera le premier satisfaisant toutes les métriques
ratifiées, avec le niveau suivant comme contrôle. Il ne sera choisi ni sur la
douceur visuelle de la courbe FIRE ni sur un accord fortuit entre méthodes.

Avant toute lecture scientifique, un budget mémoire/temps sera établi sur des
problèmes synthétiques croissants. Il devra inclure sources, arbre, grilles,
points cibles et sorties par composante. Ce benchmark ne sera pas extrapolé en
modifiant la loi de force pour rendre le coût acceptable.

## 14. Préenregistrement anti-post-hoc

Les choix suivants ne pourront pas être optimisés après observation de l'écart
entre cinématique et gravité dans `m11d/m11e` :

```text
centre
vitesse système
orientation
rayon d'orientation
sélection du traceur d'orientation
bins radiaux
points d'évaluation
épaisseur verticale
softening et kernel
convention et version de G
niveau de fidélité F0-F4
seuils et cas FIELD/EOM
allocation du budget d'erreur
conditions de bord
paramètres du solveur
seuils de convergence
domaine source et domaine analysé
masques de singularité
```

Chaque choix sera soit préenregistré et gelé, soit inclus dans une étude de
sensibilité symétrique dont tous les membres sont définis avant le résultat
cible. Aucun membre de la sensibilité ne sera promu comme référence parce qu'il
rapproche une courbe d'une attente.

## 15. Niveaux intrinsèques et observable

| Niveau | Objet | Inclut | Exclut |
| --- | --- | --- | --- |
| `G2-FIELD` | champ de la distribution de masse FIRE à points tests | espèces, kernel, softenings et bords qualifiés | corrections propres à l'EOM adaptative d'un élément |
| `G2-EOM` | accélération gravitationnelle d'un élément FIRE identifié | force symétrisée et termes conservatifs requis | projection instrumentale |
| `O1` | cinématique intrinsèque du gaz | vitesses particulières et référentiel intrinsèque | faisceau, inclination observée, bruit |
| `O2` futur | pseudo-observation | projection et dégradation préenregistrées | recalibration rétrospective de FIELD ou EOM |

Le premier test compare O1 à `G2-FIELD`, assorti de son budget. La règle de
§8.3 décide si `E_EOM` impose ensuite F3. O2 ne servira jamais à choisir centre,
orientation, kernel, solveur ou niveau de fidélité.

## 16. Dettes restantes et conditions d'ouverture

| Dette | Nature | Condition de fermeture | Statut |
| --- | --- | --- | --- |
| acquisition de `host_coordinates.hdf5` et catalogues ratifiés | donnée/provenance | autorisation distincte et manifeste conforme à `#64` | `A_RATIFIER` |
| tolérances centre/vitesse/orientation et `R_orient` | référentiel | synthétiques dédiés, rééchantillonnage et précision scientifique minimale | `A_RATIFIER` |
| correspondance historique `softening_param_code -> H_kernel` et règle de paire | kernel | qualifier changeset `415:2f1ff61cf4c2`, facteur de démarrage ou code source correspondant | `A_RATIFIER` |
| `BoxSize` et couverture de toutes les sources périodiques | donnée/bords | concordance Header, comptes d'espèces et preuve que le snapshot complet couvre la boîte requise | `A_RATIFIER` |
| mode moyen, PM et raccord TreePM | numérique/bords | convention comobile, oracle périodique et réussite de T7 | `A_RATIFIER` |
| seuils des cas FIELD/EOM | scientifique | rapportés à la plus petite différence visée avant résidu cible | `A_RATIFIER` |
| reproductibilité `grad-h` / EOM | équation du mouvement | code gelé, voisinage/dérivées/symétrisation et oracle EOM ; requise seulement si cas C | `NON_ETABLI` |
| logiciel, version et environnement | reproductibilité | capacité M4/périodique revue, environnement séparé autorisé et figé | `A_RATIFIER` |
| paramètres de convergence et allocation du budget | numérique | T1-T8 avec niveaux S/D/K et tolérances ratifiées | `A_RATIFIER` |
| coût RAM/temps | infrastructure future | benchmark synthétique autorisé seulement après choix physique | `A_RATIFIER` |
| valeur/version de `G` | unités | convention métrologique enregistrée et arrondi comparé au budget | `A_RATIFIER` |

Les paramètres propres aux quatre PartTypes sont documentés. La dette de
softening restante ne porte plus sur une valeur manquante, mais sur la
correspondance exacte entre conventions et code historique avant
implémentation. PartType2 reste explicitement requis.

`D-PERIODIC` demeure `PROPOSITION_SOUS_CONDITION`. L'indisponibilité actuelle
de `G2-EOM` ne bloque pas l'audit d'une route F2 ; elle devient bloquante si la
règle §8.3 mène au cas C ou D.

Aucune demande G2 ne pourra précéder : audit final de ce document, ratification
des dettes pertinentes au niveau F visé, autorisations distinctes de données
et d'environnement, puis validation synthétique sans lecture du résidu cible.

## 17. Recommandations

1. Ratifier la table de correspondance des softenings contre le changeset
   historique ; utiliser `SmoothingLength_HDF5` directement pour le gaz.
2. Maintenir `D-PERIODIC` sous condition jusqu'à preuve de `BoxSize`, couverture,
   mode moyen et T7 ; conserver F1 isolé comme contrôle.
3. Ratifier le budget et les cas A-D FIELD/EOM avant toute comparaison O1/G2.
4. Conserver C1 publié et C2 indépendant, avec sensibilités symétriques de
   `E_center`, `E_velocity_frame` et `E_orientation`.
5. Valider chaque méthode au niveau S contre un oracle commun, puis seulement
   mesurer D et K ; ne jamais adopter une méthode par vote interméthodes.
6. Évaluer arbre M4 et hybride TreePM sans choisir de logiciel avant T1-T8.
7. Produire `g_R_FIELD/g_z_FIELD` et leur décomposition avant toute vitesse ;
   n'ouvrir `a_R_EOM/a_z_EOM` que selon §8.3.
8. Maintenir l'interdiction d'ajuster le dispositif sur l'écart scientifique.

## 18. Verdict v0.2

```text
C0-B_V02_PRETE_A_AUDIT_FINAL
```

Ce verdict signifie uniquement que la pré-spécification documentaire est prête
pour audit scientifique final. Il ne signifie pas :

```text
C0-B ratifiée
C0-A fermée
G2 autorisée
environnement autorisé
host_coordinates autorisé
tests synthétiques autorisés
solveur choisi
calcul FIRE autorisé
```

La règle de sortie demeure :

```text
mieux définir ce que nous devrons calculer
avant de décider comment le calculer
et avant de commencer à le calculer
```

## 19. Sources primaires et traçabilité documentaire

1. **Wetzel et al. (2023)**, *Public Data Release of the FIRE-2 Cosmological
   Zoom-in Simulations of Galaxy Formation*, ApJS 265:44, DOI
   [10.3847/1538-4365/acb99a](https://doi.org/10.3847/1538-4365/acb99a),
   publié le 23 mars 2023. §4.2 et tableau 1, note p. 5 : unités,
   `SmoothingLength`, softenings Plummer-équivalents publiés et annonce de
   snapshots complets contenant toutes les particules stockées ; §§4.3-4.7 :
   centrage et catalogues. La note ne fixe pas à elle seule la conversion
   exacte entre rayon HDF5 et paramètre historique.
2. **Wetzel et al. (2025)**, *Second public data release of the FIRE-2
   cosmological zoom-in simulations of galaxy formation*, arXiv:2508.06608v2,
   27 août 2025,
   [arXiv](https://arxiv.org/abs/2508.06608). Autorité sur l'étendue DR2 et la
   disponibilité des 601 snapshots Core ; ne remplace pas les conventions DR1.
3. **Fichiers publics propres à m11d_res7100**,
   [`gizmo_parameters.txt-usedvalues`](https://users.flatironinstitute.org/~mgrudic/fire2_public_release/core/m11d_res7100/gizmo_parameters.txt-usedvalues)
   et [`gizmo_config.h`](https://users.flatironinstitute.org/~mgrudic/fire2_public_release/core/m11d_res7100/gizmo_config.h),
   consultés le 4 août 2026 : `BoxSize=58480`, cosmologie, unités, softenings,
   `ADAPTIVE_GRAVSOFT_FORGAS`, `PERIODIC`, `PMGRID=1024`, région PM haute
   résolution et changeset `415:2f1ff61cf4c2`.
4. **Fichiers publics propres à m11e_res7100**,
   [`gizmo_parameters.txt-usedvalues`](https://users.flatironinstitute.org/~mgrudic/fire2_public_release/core/m11e_res7100/gizmo_parameters.txt-usedvalues)
   et [`gizmo_config.h`](https://users.flatironinstitute.org/~mgrudic/fire2_public_release/core/m11e_res7100/gizmo_config.h),
   consultés le 4 août 2026 : mêmes valeurs pertinentes et même changeset.
5. **Hopkins et al. (2018)**, *FIRE-2 Simulations: Physics versus Numerics in
   Galaxy Formation*, MNRAS 480, 800-863, DOI
   [10.1093/mnras/sty1690](https://doi.org/10.1093/mnras/sty1690).
   §2.2 et surtout §4.2.2, éq. 9 : `epsilon_FIRE=h_i=Delta_x`,
   `rho_i=m_i/h_i^3`, `epsilon_Plummer ~= (2/3) epsilon_FIRE`, même forme de
   kernel pour gaz/étoiles/DM, adaptation gaz et choix fixes collisionnels.
6. **Hopkins (2015)**, *A new class of accurate, mesh-free hydrodynamic
   simulation methods*, MNRAS 450, 53-110, DOI
   [10.1093/mnras/stv195](https://doi.org/10.1093/mnras/stv195).
   Autorité sur la reconstruction de masse MFM/MFV et son couplage à la
   gravité ; source contextuelle, non substitut au changeset historique.
7. **GIZMO User Guide**, documentation officielle, sections `Snapshot Format`,
   `Adaptive Force Softenings` et `Gravity Parameters`, consultée le
   4 août 2026 : [documentation](https://www.tapir.caltech.edu/~phopkins/Site/GIZMO_files/gizmo_documentation.html).
   Documente `SmoothingLength` comme rayon de support/recherche, la formulation
   lagrangienne conservative, les deux nomenclatures historiques et le facteur
   `KERNEL_FAC_FROM_FORCESOFT_TO_PLUMMER` annoncé à titre d'exemple à 2.8 pour
   le cubic spline ; la valeur exacte est imprimée par le code au démarrage.
8. **Price & Monaghan (2007)**, *An energy-conserving formalism for adaptive
   gravitational force softening in smoothed particle hydrodynamics and
   N-body codes*, MNRAS 374, 1347-1358, DOI
   [10.1111/j.1365-2966.2006.11241.x](https://doi.org/10.1111/j.1365-2966.2006.11241.x).
   §3, éq. 27 : séparation force adoucie/terme adaptatif/pression ; §4.2,
   éq. 33-40 : relation `h(rho)`, voisinage, `Omega`, `zeta` et cohérence de la
   résolution implicite.
9. **Springel (2005)**, *The cosmological simulation code GADGET-2*, MNRAS 364,
   1105-1134, DOI
   [10.1111/j.1365-2966.2005.09655.x](https://doi.org/10.1111/j.1365-2966.2005.09655.x).
   §2.1, éq. 2-3 : potentiel particulier périodique et soustraction de la
   densité moyenne ; §§3.1-3.2, éq. 20-21 : images, TreePM et PM périodique.
10. **Behroozi, Wechsler & Wu (2013)**, *The ROCKSTAR Phase-space Temporal Halo
    Finder and the Velocity Offsets of Cluster Cores*, ApJ 762:109, DOI
    [10.1088/0004-637X/762/2/109](https://doi.org/10.1088/0004-637X/762/2/109).
11. **Barnes & Hut (1986)**, *A hierarchical O(N log N) force-calculation
    algorithm*, Nature 324, 446-449, DOI
    [10.1038/324446a0](https://doi.org/10.1038/324446a0).
12. **Greengard & Rokhlin (1987)**, *A fast algorithm for particle
    simulations*, J. Comput. Phys. 73, 325-348, DOI
    [10.1016/0021-9991(87)90140-9](https://doi.org/10.1016/0021-9991(87)90140-9).
13. **Hockney & Eastwood (1988)**, *Computer Simulation Using Particles*.
    Autorité classique pour Particle-Mesh et FFT.
14. **Grudic et al. (2021)**, *pytreegrav: A fast Python gravity solver*, JOSS
    6(68):3675, DOI
    [10.21105/joss.03675](https://doi.org/10.21105/joss.03675).
    Sections « Statement of need » et implémentation, notamment pages 1-3.
15. **Plummer (1911)**, MNRAS 71, 460-470, DOI
    [10.1093/mnras/71.5.460](https://doi.org/10.1093/mnras/71.5.460) ;
    **Hernquist (1990)**, ApJ 356, 359, DOI
    [10.1086/168845](https://doi.org/10.1086/168845) ;
    **Miyamoto & Nagai (1975)**, PASJ 27, 533. Autorités pour les tests
    analytiques T2-T4.

16. **IAU 2015 Resolution B3**, paramètres nominaux solaires et planétaires,
    décrite par Prša et al. (2016), AJ 152:41, DOI
    [10.3847/0004-6256/152/2/41](https://doi.org/10.3847/0004-6256/152/2/41).
    Source de la convention nominale `GM_sun` utilisée pour la candidate de G.
17. **CODATA 2018**, Tiesinga et al. (2021), *CODATA recommended values of the
    fundamental physical constants: 2018*, Rev. Mod. Phys. 93, 025010, DOI
    [10.1103/RevModPhys.93.025010](https://doi.org/10.1103/RevModPhys.93.025010).
    Source métrologique possible pour `G` en SI ; version à enregistrer.
