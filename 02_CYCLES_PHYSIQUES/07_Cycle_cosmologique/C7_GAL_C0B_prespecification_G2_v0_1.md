# C7-GAL-C0-B — pré-spécification de la route gravitationnelle G2

Version : `v0.1`
Date : `2026-08-04`
Issue : `#97`
Nature : `PREPARATION_ONLY`
Coexistence au moment de la rédaction : `ACTIVE`
Verdict de cette version : `C0-B_PRETE_A_AUDIT`

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
- `ETABLI_PAR_C0A` : constat d'entrée hérité du commentaire C0-A de `#88`, sans
  nouvelle lecture des snapshots ;
- `INFERENCE_CONTROLEE` : conséquence explicite de plusieurs faits documentés,
  avec hypothèses visibles ;
- `PROPOSITION` : règle candidate à auditer avant adoption ;
- `A_RATIFIER` : valeur, seuil ou choix à figer avant toute lecture du résultat
  cible ;
- `NON_ETABLI` : information que les sources consultées ne suffisent pas à
  fixer.

Les expressions « vérité » ou « référence » désignent ici une référence
numérique intrinsèque à la simulation, assortie d'un budget d'erreur. Elles ne
signifient pas une vérité physique sans approximation.

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

## 4. Contrat de softening gravitationnel

### 4.1 Réglages propres à `m11d_res7100` et `m11e_res7100`

Les deux fichiers de compilation publics activent
`ADAPTIVE_GRAVSOFT_FORGAS`. Ils n'activent pas le softening adaptatif pour les
espèces collisionnelles. Ils utilisent le réglage de voisinage
`DesNumNgb = 32` et `MinGasHsmlFractional = 1`.

Les noms historiques GADGET/GIZMO se mappent ainsi : `Gas` -> PartType0,
`Halo` -> PartType1, `Disk` -> PartType2, `Stars` -> PartType4. DR1 confirme
que PartType1 est le DM haute résolution du zoom et PartType2 le DM basse
résolution du volume cosmologique.

À bas redshift, le plafond `MaxPhys` fixe la valeur physique. La conversion
exacte des paramètres à `z = 0` est `epsilon_phys = MaxPhys/h` kpc. Les nombres
publiés dans le tableau 1 de DR1 sont arrondis.

| Espèce | PartType | Fixe/adaptatif | Valeur ou règle à `z = 0` | Kernel | Source | Statut |
| --- | ---: | --- | --- | --- | --- | --- |
| gaz | 0 | adaptatif, avec minimum | support par particule `H = SmoothingLength a/h`; minimum équivalent Plummer `0.0007/0.68 kpc ~= 1.03 pc` | spline M4 compact | config/paramètres propres ; DR1 tableau 1 et §4.2 ; Hopkins et al. 2018 §2.2/4.2 | `DOCUMENTE` |
| DM haute résolution | 1 | fixe | `0.028/0.68 kpc ~= 41.2 pc` équivalent Plummer (DR1 arrondit à 40 pc) | spline M4 compact | paramètres propres ; DR1 tableau 1 | `DOCUMENTE` |
| DM basse résolution | 2 | fixe | `0.2/0.68 kpc ~= 294 pc` équivalent Plummer | spline M4 compact | `SofteningDiskMaxPhys` propre aux deux runs ; mapping DR1 | `DOCUMENTE` |
| étoiles | 4 | fixe | `0.0028/0.68 kpc ~= 4.12 pc` équivalent Plummer (DR1 arrondit à 4 pc) | spline M4 compact | paramètres propres ; DR1 tableau 1 | `DOCUMENTE` |

Au-dessus de la transition `a = 0.1` (`z = 9`), les valeurs de code comobiles
sont respectivement `SofteningGas = 0.007`, `SofteningStars = 0.028`,
`SofteningHalo = 0.28` et `SofteningDisk = 2`. En dessous de `z = 9`, les
`MaxPhys` ci-dessus rendent les minima/fixes physiques. Cette règle est
cohérente avec la prescription FIRE-2 publiée « comobile à haut redshift,
physique à bas redshift ».

### 4.2 Loi de force à reproduire

La loi prescrite n'est pas une force de Plummer. GIZMO représente chaque
élément comme une distribution de masse spline M4 à support compact :

- le champ est exactement newtonien hors du support ;
- pour le noyau cubic spline standard, le rayon de support complet vaut
  environ `H = 2.8 epsilon_Plummer` ;
- pour le gaz, `H` est fourni particule par particule par `SmoothingLength` ;
- pour PartType1, PartType2 et PartType4, le rayon de support sera construit à
  partir de la valeur fixe équivalente Plummer de l'espèce ;
- les interactions de particules aux softenings différents utilisent la règle
  de symétrisation du noyau GIZMO ; le guide et la bibliothèque scientifique
  `pytreegrav` documentent l'emploi du plus grand rayon de support pour une
  paire recouvrante.

Deux objets doivent rester séparés :

1. **champ de la distribution de masse** à des points d'évaluation sans masse :
   le point cible a un softening nul et chaque source exerce son champ M4 ;
2. **accélération d'une particule adaptativement adoucie telle qu'intégrée par
   GIZMO** : elle peut inclure les termes conservatifs liés à la variation du
   softening (`grad-h`) et les règles exactes de symétrisation.

La sortie primaire G2 est le premier objet. Une comparaison particule par
particule aux équations du mouvement FIRE relèverait d'une extension distincte
et exigerait de reproduire les termes conservatifs du code gelé. Cette
extension est `NON_ETABLI` et n'est pas requise pour définir le champ à des
points tests.

### 4.3 Conditions de bord cosmologiques

Les configurations propres aux deux runs activent une boîte périodique et un
solveur TreePM. Un simple calcul isolé autour de la galaxie ne reproduit donc
pas silencieusement la force intégrée par FIRE. La future grandeur primaire
sera une accélération différentielle dans le référentiel de l'hôte :

```text
g_rel(x) = g(x) - g(x_centre)
```

Cette soustraction retire l'accélération uniforme du référentiel, mais non les
marées à grande échelle. La procédure à ratifier devra choisir avant FIRE entre
les deux routes suivantes :

- `D-PERIODIC` : champ de toutes les espèces avec conditions périodiques et
  soustraction de la densité moyenne, au plus près de TreePM ;
- `D-LOCAL-CONTROL` : somme M4 isolée dans des domaines croissants, utilisée
  seulement si sa convergence vers `D-PERIODIC` est démontrée sur le champ
  différentiel dans le domaine galactique.

`D-PERIODIC` est la route de référence proposée. `D-LOCAL-CONTROL` ne peut pas
devenir la référence par commodité de calcul.

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

Cette pré-décision est `PROPOSITION`, pas un choix de logiciel ratifié.

## 8. Sortie primaire future : le champ

Le produit scientifique primaire de G2 sera le champ intrinsèque, dans un
repère cylindrique gelé :

```text
g_R(R,z), g_z(R,z)
```

Le produit minimal enregistrera : coordonnées des points, `g_x/g_y/g_z`,
`g_R`, composante azimutale de contrôle, unités physiques, centre, vitesse,
rotation, convention périodique, kernel, softenings, paramètres du solveur,
version du logiciel et budget d'erreur.

Seulement après validation du champ :

```text
v_grav(R) = sqrt(R |g_R(R,0)|)
```

Le signe radial devra être entrant dans le domaine où cette transformation est
utilisée. La formule sphérique

```text
v_sph(r) = sqrt(G M(<r) / r)
```

reste `CONTROLE_SECONDAIRE`. Elle ne remplace ni le champ d'un disque aplati ni
la référence G2.

## 9. Décomposition des composantes

Le solveur produira séparément :

```text
g_gas, g_DM, g_PT2, g_star, g_total
```

où `g_DM` désigne PartType1 et `g_PT2` PartType2. PartType2 ne sera ni fusionné
silencieusement avec PartType1 dans les sorties, ni omis parce qu'il est
attendu loin de la galaxie.

Le test de fermeture est :

```text
Delta_close = g_total - (g_gas + g_DM + g_PT2 + g_star)
```

La tolérance de fermeture sera dérivée des budgets numériques mesurés lors des
sommes par composante et de la somme totale, avec prise en compte de
l'arrondi. Elle sera gelée avant FIRE. Une bonne fermeture ne valide pas à elle
seule l'exactitude du champ.

Cette décomposition indique l'origine numérique des contributions :

```text
champ total != décomposition des sources != verdict sur la matière sombre
```

## 10. Batterie de validation synthétique avant FIRE

Tous les tests suivants précèdent toute exécution sur `m11d/m11e`.

### T1 — masse ponctuelle adoucie M4

Construire une source de masse connue avec rayon de support connu et évaluer
le champ sur une grille de `r/H` couvrant le centre, les morceaux polynomiaux,
la transition et le régime newtonien. Tester direction, normalisation,
continuité et exactitude newtonienne hors support. Ajouter des paires à
softenings inégaux pour tester la règle de symétrisation. Le point `r=0`, où la
direction est indéfinie, est traité par un test de norme nulle distinct.

### T2 — sphère de Plummer

Échantillonner une sphère de Plummer de masse et rayon connus et comparer au
champ analytique

```text
g(r) = -G M r / (r^2 + b^2)^(3/2).
```

Faire varier le nombre de particules, la réalisation aléatoire et le softening
numérique. Ici « Plummer » décrit la distribution analytique, pas le kernel de
softening FIRE.

### T3 — profil de Hernquist

Échantillonner un profil de Hernquist et comparer le champ radial analytique
sur une forte dynamique en rayon. Préenregistrer une exclusion du voisinage
non résolu du centre fondée sur le softening et l'échantillonnage, non sur
l'erreur observée.

### T4 — disque de Miyamoto-Nagai

Utiliser le potentiel analytique aplati pour tester conjointement `g_R(R,z)` et
`g_z(R,z)`, dans le plan, hors plan et près de l'axe. Ce test est obligatoire
avant toute interprétation d'un disque FIRE.

### T5 — superposition

Superposer au moins deux composantes analytiques de géométries différentes et
vérifier à la fois l'accord analytique du champ total et la fermeture exacte
des sorties par composante.

### T6 — invariances

Tester :

- translation commune des sources et des cibles ;
- rotation rigide et covariance vectorielle du champ ;
- permutation de l'ordre des particules ;
- partition puis recomposition des espèces ;
- changement cohérent d'unités ;
- reproductibilité à graine fixée pour les réalisations échantillonnées.

### T7 — périodicité et fond homogène

Ajouter un test périodique indépendant : distribution homogène plus
perturbation analytique ou mode de Fourier unique. Vérifier la soustraction du
mode moyen, la périodicité, l'accélération différentielle et la convergence de
la partie PM. Ce test ferme la dette de conditions de bord avant FIRE.

### T8 — accord inter-méthodes

Sur des problèmes tenant en somme directe, comparer somme directe, arbre,
FMM éventuel, PM et hybride. L'accord doit porter sur les vecteurs et les
composantes cylindriques, pas seulement sur un profil de norme.

## 11. Métriques et tolérances à ratifier

Pour chaque test, enregistrer au minimum :

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

Aucun seuil universel de 1 % n'est imposé. Le budget sera ratifié à partir de :

1. l'erreur analytique et inter-méthodes du solveur ;
2. la résolution et les softenings FIRE ;
3. l'erreur d'échantillonnage des représentations particulaires synthétiques ;
4. la plus petite différence scientifique que le futur protocole prétendra
   distinguer ;
5. une marge de sécurité fixée avant le résultat cible.

Si la précision nécessaire à la question scientifique est plus fine que le
plancher démontré par la validation, G2 sera déclarée insuffisante ; les seuils
ne seront pas relâchés après observation.

## 12. Convergence numérique préenregistrée

### 12.1 Paramètres à faire varier

| Famille | Paramètres de convergence |
| --- | --- |
| arbre | angle/critère d'ouverture, ordre multipolaire, précision arithmétique, taille des feuilles |
| FMM | ordre d'expansion, tolérance, séparation proche/lointain |
| PM | nombre et forme des cellules, dépôt, interpolation, déconv., solveur FFT, traitement du mode zéro |
| hybride | échelle de séparation arbre-PM et chacun des paramètres ci-dessus |
| champ évalué | nombre et placement des points, domaine radial, épaisseur et échantillonnage en `z`, traitement de `R=0` |
| physique numérique | kernel, softenings par espèce, règle des paires, périodicité, domaine source, bords |

### 12.2 Règle d'arrêt de raffinement

Une suite géométrique de raffinements et un ordre fixe de comparaison seront
définis avant FIRE. La convergence sera jugée contre l'analytique ou la somme
directe sur synthétiques, puis par différences entre raffinements successifs.
Le raffinement retenu sera le premier satisfaisant simultanément toutes les
métriques ratifiées, avec le niveau suivant comme contrôle. Il ne sera pas
choisi sur la douceur visuelle de la courbe FIRE.

Avant toute lecture scientifique, un budget mémoire/temps sera établi sur des
problèmes synthétiques croissants. Il devra inclure sources, arbre, grilles,
points cibles et sorties par composante. Ce benchmark ne sera pas extrapolé en
modifiant la loi de force pour rendre le coût acceptable.

## 13. Préenregistrement anti-post-hoc

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

## 14. Vérité de simulation et observable

Trois niveaux sont conservés :

| Niveau | Objet | Inclut | Exclut |
| --- | --- | --- | --- |
| `G2-TRUE` | champ gravitationnel intrinsèque de la distribution de masse FIRE | toutes les espèces, softenings, géométrie et conditions de bord validés | projection instrumentale et inférence observationnelle |
| `O1` | cinématique intrinsèque du gaz | vitesses particulières et référentiel intrinsèque | faisceau, inclination observée, bruit |
| `O2` futur | pseudo-observation | projection et dégradation instrumentale préenregistrées | modification rétrospective de G2-TRUE |

Le premier test scientifique comparera O1 à G2-TRUE. Une reconstruction
observationnelle ou une pseudo-observation ne sera pas utilisée pour calibrer
le centre, l'orientation ou le solveur de G2.

## 15. Dettes restantes et conditions d'ouverture de G2

| Dette | Nature | Condition de fermeture | Statut |
| --- | --- | --- | --- |
| acquisition de `host_coordinates.hdf5` et, si ratifié, des catalogues | donnée/provenance | autorisation distincte, manifeste `#64`, taille et empreinte du petit produit | `A_RATIFIER` |
| tolérances centre/vitesse/orientation | statistique | tests synthétiques de centrage, rééchantillonnage et précision scientifique minimale | `A_RATIFIER` |
| règle exacte de `R_orient` | méthodologique | règle fondée sur une taille indépendante et gelée avant cible | `A_RATIFIER` |
| implémentation périodique et mode moyen | numérique bloquant pour le calcul | réussite de T7 et accord avec une référence périodique | `A_RATIFIER` |
| logiciel et version | reproductibilité | revue de capacité M4/périodique, environnement séparé autorisé, version figée | `A_RATIFIER` |
| paramètres de convergence | numérique | T1-T8 et budget d'erreur ratifié | `A_RATIFIER` |
| coût RAM/temps | infrastructure | benchmark synthétique et budget avant FIRE | `A_RATIFIER` |
| termes conservatifs `grad-h` | extension équations du mouvement | requis seulement pour une future comparaison particule par particule ; code gelé et tests dédiés | `NON_ETABLI` hors périmètre G2-TRUE champ |

Les unités utiles, les softenings des quatre PartTypes et le kernel ne sont plus
des dettes ouvertes dans le périmètre du champ G2. En particulier, PartType2 a
une prescription spécifique documentée et ne justifie plus un blocage de C0-B.

G2 ne pourra être demandée qu'après : audit de ce document, ratification des
éléments ci-dessus, autorisation explicite de données/environnement, puis
réussite de la validation synthétique sans lecture du résultat cible.

## 16. Recommandations

1. Auditer en priorité la distinction `SmoothingLength`/support M4/équivalent
   Plummer et la prescription PartType2.
2. Ratifier `D-PERIODIC` comme référence du champ différentiel ; conserver la
   somme locale isolée comme contrôle de convergence seulement.
3. Acquérir ultérieurement `host_coordinates.hdf5` comme C1 et conserver un C2
   stellaire + DM réellement indépendant.
4. Conserver l'axe HI comme candidate, avec axes stellaires et rotation publiée
   comme contrôles obligatoires et un statut explicite si `m11e` n'admet pas de
   plan unique.
5. Évaluer un arbre M4 et un hybride TreePM, sans choisir une bibliothèque
   avant T1-T8.
6. Produire le champ et sa décomposition avant toute courbe de rotation.
7. Maintenir l'interdiction de tout ajustement du dispositif sur l'écart
   scientifique final.

## 17. Verdict C0-B

```text
C0-B_PRETE_A_AUDIT
```

Ce verdict signifie uniquement que les choix nécessaires à une future
G2-faisabilité sont suffisamment spécifiés pour être audités. Il ne signifie
pas :

```text
G2 autorisée
solveur choisi définitivement
calcul FIRE autorisé
C0-A fermée
PR mergeable automatiquement
```

La règle de sortie demeure :

```text
préparer la possibilité de calculer correctement
!= commencer à calculer
```

## 18. Sources primaires et traçabilité documentaire

1. **Wetzel et al. (2023)**, *Public Data Release of the FIRE-2 Cosmological
   Zoom-in Simulations of Galaxy Formation*, ApJS 265:44, publié le
   23 mars 2023, DOI
   [10.3847/1538-4365/acb99a](https://doi.org/10.3847/1538-4365/acb99a).
   Sections 2.1, 4.2, 4.3, 4.5, 4.7 et annexe ; tableau 1. Autorité principale
   pour unités, PartTypes, softenings publiés, centrage et produits de halo.
2. **Wetzel et al. (2025)**, *Second public data release of the FIRE-2
   cosmological zoom-in simulations of galaxy formation*, arXiv:2508.06608v2,
   27 août 2025,
   [arXiv](https://arxiv.org/abs/2508.06608). Autorité sur l'étendue DR2 et la
   disponibilité des 601 snapshots de la suite Core ; ne remplace pas les
   conventions détaillées de DR1.
3. **Paramètres publics m11d_res7100**, fichiers
   [`gizmo_parameters.txt-usedvalues`](https://users.flatironinstitute.org/~mgrudic/fire2_public_release/core/m11d_res7100/gizmo_parameters.txt-usedvalues)
   et
   [`gizmo_config.h`](https://users.flatironinstitute.org/~mgrudic/fire2_public_release/core/m11d_res7100/gizmo_config.h),
   consultés le 4 août 2026. Autorité spécifique pour unités, cosmologie,
   softenings, adaptation gaz et configuration périodique.
4. **Paramètres publics m11e_res7100**, fichiers
   [`gizmo_parameters.txt-usedvalues`](https://users.flatironinstitute.org/~mgrudic/fire2_public_release/core/m11e_res7100/gizmo_parameters.txt-usedvalues)
   et
   [`gizmo_config.h`](https://users.flatironinstitute.org/~mgrudic/fire2_public_release/core/m11e_res7100/gizmo_config.h),
   consultés le 4 août 2026. Même portée spécifique.
5. **Hopkins et al. (2018)**, *FIRE-2 Simulations: Physics versus Numerics in
   Galaxy Formation*, MNRAS 480, 800-863, DOI
   [10.1093/mnras/sty1690](https://doi.org/10.1093/mnras/sty1690).
   Sections 2.2 et 4.2, particulièrement 4.2.2 : TreePM, masse étendue du gaz,
   softening adaptatif, kernel commun et évolution physique/comobile.
6. **Hopkins (2015)**, *A new class of accurate, mesh-free hydrodynamic
   simulation methods*, MNRAS 450, 53-110, DOI
   [10.1093/mnras/stv195](https://doi.org/10.1093/mnras/stv195).
   Section et annexe sur la gravité/adaptive softening : formulation M4 et
   conservation.
7. **GIZMO User Guide**, documentation officielle, sections
   `Adaptive Force Softenings`, `Gravity Parameters` et format des snapshots,
   consultée le 4 août 2026 :
   [documentation](https://www.tapir.caltech.edu/~phopkins/Site/GIZMO_files/gizmo_documentation.html).
8. **Price & Monaghan (2007)**, *An energy-conserving formalism for adaptive
   gravitational force softening in smoothed particle hydrodynamics and
   N-body codes*, MNRAS 374, 1347-1358, DOI
   [10.1111/j.1365-2966.2006.11241.x](https://doi.org/10.1111/j.1365-2966.2006.11241.x).
9. **Springel (2005)**, *The cosmological simulation code GADGET-2*, MNRAS 364,
   1105-1134, DOI
   [10.1111/j.1365-2966.2005.09655.x](https://doi.org/10.1111/j.1365-2966.2005.09655.x).
   Autorité TreePM et expansion multipolaire hiérarchique.
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
