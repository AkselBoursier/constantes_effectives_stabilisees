# C7-GAL-C0 — Audit de faisabilité du premier démonstrateur FIRE-2 v0.1

## 0. Statut

```text
statut : cadrage exploratoire ;
lot parent : C7-GAL-C, issue #86 ;
porte locale : C7-GAL-C0, issue #88 ;
date : 1er août 2026 ;
autorité normative : aucune ;
calcul scientifique exécuté : aucun ;
donnée FIRE téléchargée : aucune par cette porte ;
verdict : faisabilité documentaire positive, faisabilité instrumentale encore ouverte.
```

Ce document répond à une question plus étroite que le programme général :

> Peut-on construire, à partir de données publiques, un premier test où une reconstruction
> cinématique du gaz est comparée à une référence gravitationnelle indépendante, sans
> fabriquer les termes non observables du bilan dynamique ?

La réponse actuelle est : **oui en principe, mais pas encore démontré au niveau des
fichiers**. La porte suivante doit inspecter deux snapshots réels avant toute courbe de
rotation.

## 1. Pourquoi cette porte est nécessaire

Le lot C7-GAL-C vise à contrôler le passage :

```text
cinématique observée
→ vitesse circulaire reconstruite
→ accélération gravitationnelle
→ profil de masse inféré.
```

Sands et al. montrent que ce passage peut échouer lorsque le système est hors équilibre,
mais leur analyse complète utilise des sorties de simulation supplémentaires : accélération
gravitationnelle et hydrodynamique, gradients du gaz HI, pression radiative et composantes
du tenseur de contraintes. Ces quantités ne figurent pas toutes parmi les champs standards
documentés de la diffusion publique FIRE-2.

Une reproduction terme par terme de leur analyse n'est donc pas notre point de départ.
Le test doit être reconstruit à partir de ce qui est effectivement public.

## 2. Corpus documentaire audité

### 2.1 FIRE-2 Data Release 1 et 2

Références :

- Wetzel et al. 2023, *Public Data Release of the FIRE-2 Cosmological Zoom-in Simulations of Galaxy Formation*, ApJS 265, 44, DOI 10.3847/1538-4365/acb99a ;
- Wetzel et al. 2025, *Second public data release of the FIRE-2 cosmological zoom-in simulations of galaxy formation*, arXiv:2508.06608 ;
- portail FlatHUB FIRE : https://flathub.flatironinstitute.org/fire .

DR2 rend disponibles pour les simulations `Base Physics` du Core suite les 601 snapshots
jusqu'à `z=0`, avec un espacement temporel inférieur ou voisin de 25 Myr. Les catalogues
de halos/galaxies, les arbres de fusion et des pointeurs de suivi gaz/étoiles sont également
publiés.

Les champs standards documentés incluent notamment :

```text
Coordinates
Velocities
Masses
Potential                 [présence à vérifier simulation par simulation]
Density                    [gaz]
InternalEnergy             [gaz]
SmoothingLength            [gaz]
ElectronAbundance          [gaz]
NeutralHydrogenAbundance   [gaz]
StarFormationRate          [gaz]
Metallicity
```

La présence d'un nom dans la documentation générale ne suffit pas à garantir son existence
dans `m11d` ou `m11e`. Cette vérification est la première tâche instrumentale.

### 2.2 Sands et al.

Référence :

- Sands et al. 2026, *Confronting the Diversity Problem: The Limits of Galaxy Rotation Curves as a Tool to Understand Dark Matter Profiles*, ApJ 1000, 127, arXiv:2404.16247.

Points utilisés ici :

1. les disques ordonnés peuvent reconstruire la vitesse circulaire avec des erreurs de
   l'ordre de 10 % dans le disque ;
2. les écarts peuvent atteindre plusieurs dizaines de pour cent lorsque les termes hors
   équilibre, les mouvements non circulaires ou des contraintes non thermiques deviennent
   importants ;
3. le terme temporel n'est pas accessible à partir d'une observation instantanée ;
4. certaines corrections d'équilibre peuvent empirer la reconstruction lorsque des termes
   non circulaires sont eux-mêmes produits par le déséquilibre ;
5. l'étude utilise des sorties additionnelles non garanties dans la diffusion standard.

Le tableau de Sands distingue explicitement `m11e-2` comme simulation FIRE-2 dans un
échantillon majoritairement FIRE-3. `m11e-2` est décrit comme un disque à caractéristiques
de marée dont les reconstructions sont affectées par une fusion. Cette particularité en
fait le stress-test le plus propre pour notre première porte publique.

### 2.3 Dado et al.

Référence :

- Dado et al. 2025, *Dynamical disequilibrium in dwarf galaxies: rethinking gas dynamics,
  rotation curves, and dark matter inference*, arXiv:2512.11033.

Cette prépublication COLIBRE est utilisée comme contrôle conceptuel, non comme résultat
acquis. Elle renforce deux contraintes méthodologiques :

- la correction de pression et des termes convectifs ne garantit pas une meilleure
  récupération lorsque le terme temporel est dominant ;
- il faut qualifier l'état dynamique avant d'ajouter des corrections analytiques.

Nous ne sélectionnons pas COLIBRE comme premier démonstrateur parce que l'accessibilité
publique des champs nécessaires à une reproduction indépendante n'est pas établie ici.

## 3. Choix du premier couple de simulations

### 3.1 Stress-test : `m11e` FIRE-2

Dans la diffusion FIRE-2 documentée à `z=0` :

```text
M200m ≈ 1.68 × 10^11 M_sun
Mstar,90 ≈ 1.4 × 10^9 M_sun
masse baryonique initiale par élément ≈ 7100 M_sun
taille indicative d'un snapshot ≈ 2.0 Go
cosmologie : Planck
référence d'origine : El-Badry et al. 2018
```

Motif de sélection : le cas publié FIRE-2 apparenté est perturbé par une fusion. L'état
dynamique est donc défini par une cause physique indépendante de l'erreur de reconstruction.

### 3.2 Contrôle : `m11d` FIRE-2

Dans la même diffusion :

```text
M200m ≈ 3.23 × 10^11 M_sun
Mstar,90 ≈ 3.9 × 10^9 M_sun
masse baryonique initiale par élément ≈ 7100 M_sun
taille indicative d'un snapshot ≈ 2.8 Go
cosmologie : Planck
référence d'origine : El-Badry et al. 2018
```

Motif de sélection : même lignée documentaire et résolution baryonique que `m11e`, avec
un cas de disque ordonné utilisé dans Sands comme référence de reconstruction fidèle dans
la génération FIRE-3 correspondante.

Cette dernière information ne vaut pas transfert automatique du verdict FIRE-3 vers
FIRE-2. Elle sert uniquement à motiver le choix d'un contrôle ; son état réel sera mesuré.

### 3.3 Pourquoi `m11i` n'est pas le premier stress-test

Sands décrit pour `m11i` un épisode de formation stellaire tardive associé à des erreurs
transitoires importantes. Mais ce cas est FIRE-3. La diffusion publique DR2 contient un
`m11i` FIRE-2 : l'homonymie ne suffit pas à en faire une reproduction de la simulation
FIRE-3.

`m11i` est donc conservé pour une étape ultérieure de **transfert entre générations
physiques** après gel de la méthode sur `m11e/m11d`.

## 4. Ce qui est directement observable dans les snapshots publics

Pour un snapshot donné, les champs publics permettent en principe de construire une
route cinématique sans modèle de halo :

```text
position 3D du gaz
+ vitesse 3D
+ masse
+ densité
+ fraction de H neutre
+ énergie interne
→ sélection HI
→ orientation du disque
→ profils v_phi, v_R, dispersion
→ cartes projetées et moments cinématiques.
```

La route doit conserver deux niveaux distincts :

```text
O0 : information intrinsèque du snapshot 3D ;
O1 : pseudo-observation projetée après choix d'une ligne de visée et d'une résolution.
```

Le premier test utilisera O0 pour qualifier la méthode. O1 ne sera ajouté qu'après gel des
choix de centrage, orientation, anneaux et sélection HI.

## 5. Référence gravitationnelle : dette principale de C0

La référence ne doit pas être dérivée de la même hypothèse cinématique que l'objet testé.
Trois routes sont classées ex ante.

### G1 — gradient du potentiel public

Si `Potential` est présent et suffisamment échantillonné dans `m11d/m11e`, reconstruire un
champ potentiel lissé dans le plan du disque puis calculer :

```math
v_{\rm grav}^2(R) = R\,\partial_R\Phi(R,z\simeq0).
```

Cette voie est prioritaire seulement si sa stabilité numérique peut être démontrée par :

- variation du lissage ;
- variation de l'épaisseur en `z` ;
- comparaison entre espèces servant d'échantillonnage du même potentiel ;
- fermeture avec une seconde route gravitationnelle.

Le zéro arbitraire du potentiel n'affecte pas son gradient.

### G2 — accélération recalculée depuis la distribution de masse

Si G1 est indisponible ou instable, calculer l'accélération à partir des particules/cellules
avec une méthode gravitationnelle explicitement contrôlée. Cette route est plus coûteuse et
n'est autorisée qu'après estimation du coût et test sur un sous-échantillon.

### G3 — masse sphérique comme contrôle seulement

```math
v_{\rm sph}(r)=\sqrt{\frac{G M(<r)}{r}}.
```

Cette quantité est utile comme contrôle de cohérence et pour comparer à certaines définitions
publiées de `v_c`. Elle ne peut pas devenir silencieusement la vérité primaire dans un disque
aplati ou perturbé.

### Verdict C0 sur la référence

```text
G1 : possible en principe, présence réelle à vérifier ;
G2 : possible en principe, coût à établir ;
G3 : disponible à partir des masses, mais secondaire par construction.
```

La faisabilité scientifique n'est donc pas encore fermée.

## 6. Reconstruction cinématique primaire

La première reconstruction ne cherchera pas à « corriger tout ce qui peut l'être ».
Elle doit établir une échelle de complexité.

### O1a — centrifuge minimale

Dans des anneaux cylindriques définis avant inspection des résidus :

```math
v_{\rm rec,0}(R)=\langle v_\phi\rangle_{HI}.
```

### O1b — pression comme variante

Une correction de pression, construite à partir des champs publics, est évaluée séparément.
Elle ne remplace pas O1a et son succès n'est pas présupposé.

### O1c — mouvements non circulaires

Conserver au minimum :

```text
<v_R>
σ_R, σ_phi, σ_z
asymétrie azimutale
modes m=1 et m=2 de la distribution HI.
```

Ces grandeurs servent d'abord d'indicateurs de qualification, pas de termes libres destinés
à absorber le résidu.

## 7. Variables de qualification définies sans accès à la vérité gravitationnelle

Le score futur doit être construit uniquement avec des grandeurs accessibles à O0/O1.
Candidats initiaux :

```text
Q1 : asymétrie des côtés approchant / fuyant ;
Q2 : |<v_R>| / |<v_phi>| ;
Q3 : σ_LOS / |<v_phi>| ;
Q4 : décalage centre HI / centre stellaire / centre halo ;
Q5 : amplitude m=1 de la surface HI ;
Q6 : amplitude m=2 de la surface HI ;
Q7 : variation radiale de l'axe cinématique ;
Q8 : extension et fraction HI ;
Q9 : taux de formation stellaire comme traceur de perturbation.
```

Aucun seuil numérique n'est fixé à cette porte. Les seuils ne seront définis qu'après
vérification de la résolution, des unités et du bruit numérique, puis gelés avant comparaison
à `v_grav`.

## 8. Temporalité et prévention du biais de sélection

DR2 rend disponibles 601 snapshots, ce qui permet d'étudier le temps mais crée un risque
de sélection post hoc.

Règle :

```text
l'événement ou la fenêtre temporelle est sélectionné(e)
à partir d'une variable indépendante de l'erreur cible ;
les indices de snapshots sont gelés ;
seulement ensuite v_rec - v_grav est calculé.
```

Pour `m11e`, la voie prioritaire est l'arbre de fusion public. Pour `m11d`, une fenêtre de
contrôle appariée en époque doit être définie par la même règle temporelle, non par recherche
d'une bonne courbe.

Le snapshot `600` peut être utilisé pour l'inventaire instrumental car il n'est pas choisi
pour une propriété dynamique favorable : c'est simplement l'état final conventionnel.

## 9. Budget de données

Les tailles documentées de snapshots sont de l'ordre de :

```text
m11e : 2.0 Go / snapshot
m11d : 2.8 Go / snapshot
```

Télécharger 601 snapshots de chaque simulation représenterait plusieurs téraoctets et n'est
ni nécessaire ni autorisé par le présent cadrage.

Séquence :

```text
1 snapshot m11e + 1 snapshot m11d
→ inventaire des champs
→ décision G1/G2
→ estimation coût disque/mémoire
→ sélection pré-enregistrée d'une petite fenêtre
→ téléchargement borné.
```

## 10. Porte instrumentale suivante — C0-A

C0-A doit produire, sans analyse physique :

1. inventaire HDF5 des groupes et datasets de `snapshot_600` pour `m11e` et `m11d` ;
2. présence/absence et forme de `Potential` ;
3. présence des champs HI et thermodynamiques ;
4. unités lues depuis le header et conversions contrôlées ;
5. centre et vitesse du halo principal depuis le catalogue ;
6. taille réelle des fichiers ;
7. empreinte cryptographique des fichiers effectivement utilisés ;
8. test de lecture par un outil public documenté ou un lecteur HDF5 minimal indépendant.

Cette porte ne trace aucune courbe de rotation.

## 11. Conditions d'échec

Le démonstrateur `m11e/m11d` est abandonné ou requalifié si :

- aucun accès gravitationnel indépendant de la cinématique n'est réalisable avec un coût
  raisonnable ;
- les champs HI nécessaires sont absents ou non interprétables ;
- la résolution interdit une comparaison radiale utile dans le disque ;
- le centre ou l'orientation ne peuvent pas être définis de façon stable ;
- la reproduction nécessite des sorties privées ou non documentées ;
- la méthode ne peut pas séparer clairement observable, reconstruction et vérité simulée.

Un tel échec serait un résultat méthodologique, pas une invitation à compléter les champs
manquants par hypothèse.

## 12. Verdict v0.1

```text
question C7-GAL-C : ouverte ;
FIRE-2 DR2 : corpus public pertinent ;
reproduction exacte de Sands : non établie et probablement impossible avec seuls champs standards ;
premier stress-test : m11e FIRE-2 ;
contrôle : m11d FIRE-2 ;
m11i : différé comme test de transfert FIRE-2/FIRE-3 ;
route observable : suffisamment documentée pour passer à l'inventaire ;
route gravitationnelle indépendante : dette bloquante ;
prochaine action autorisée : C0-A, inventaire de deux snapshots seulement.
```

La porte C0 n'autorise encore ni comparaison matière sombre / gravité modifiée, ni ajustement
de profils de halo, ni interprétation cosmologique.