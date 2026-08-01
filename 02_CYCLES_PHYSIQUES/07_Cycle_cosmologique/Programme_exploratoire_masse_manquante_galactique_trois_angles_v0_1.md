# Programme exploratoire — masse manquante galactique, trois angles discriminants v0.1

## 0. Statut

```text
statut : exploration datée ;
cycle : 7 — cosmologie, sous-périmètre galactique ;
date : 1er août 2026 ;
issue directrice : #83 ;
lots : #84, #85, #86 ;
autorité normative : aucune ;
ne vaut pas : conclusion en faveur ou en défaveur de la matière sombre,
              modification de la synthèse active du cycle 7,
              pré-enregistrement d’une analyse numérique,
              autorisation de calcul ou de collecte de données ;
condition de sortie : abandon, absorption dans un démonstrateur borné,
                      conservation comme état daté ou ratification humaine séparée.
```

Ce document installe un programme de recherche inspectable sans transformer une
intuition en doctrine. Il reprend la distinction active du corpus :

```text
objet physique
≠ voie d’accès
≠ modèle de reconstruction
≠ verdict ontologique.
```

La question de la matière sombre est ici reformulée comme un problème de
**masse manquante ou de champ gravitationnel excédentaire inféré**. La matière sombre
constitue une famille d’explications importante, mais elle n’est ni présupposée ni
écartée.

## 1. Phénomène cible

Le phénomène minimal à expliquer est l’écart entre :

```text
champ ou accélération inférés à partir des mouvements et du lentillage
```

et :

```text
champ reconstruit à partir des composantes baryoniques observées
sous une loi dynamique et des hypothèses d’équilibre spécifiées.
```

Cette formulation évite trois glissements :

1. appeler directement « matière sombre » tout résidu dynamique ;
2. confondre une vitesse observée avec une accélération gravitationnelle directement
   mesurée ;
3. traiter l’ajustement réussi d’une courbe comme la reconstruction d’un champ ou
   d’un espace-temps complet.

Le périmètre galactique ne suffit pas à arbitrer les contraintes des amas, du fond
diffus cosmologique, des abondances primordiales ou de la formation des grandes
structures. Toute conclusion restera donc bornée à son domaine.

## 2. Question directrice

> Une même description physique, utilisant une reconstruction baryonique commune et
> sans réinitialisation opportuniste entre observables, peut-elle prédire le champ
> radial, le champ vertical, la cinématique hors équilibre et, lorsque les données le
> permettent, le lentillage du même système ?

Trois questions secondaires organisent le programme :

1. **Accès dynamique** — quelle part de la vitesse reconstruite trace réellement le
   champ gravitationnel, et quelle part dépend du déséquilibre, de la pression ou des
   mouvements non circulaires ?
2. **Géométrie du champ** — une même description reproduit-elle conjointement les
   composantes radiale et verticale, dans et hors du plan ?
3. **Cohérence multi-observables** — la description qui déplace la matière massive
   dévie-t-elle aussi correctement la lumière avec les mêmes baryons et les mêmes
   paramètres physiques ?

## 3. Position méthodologique

### 3.1 Familles candidates

Le programme doit comparer au minimum :

```text
M0 : baryons seuls sous dynamique newtonienne ou relativité générale ;
M1 : baryons + composante sombre, avec géométrie et profil explicités ;
M2 : dynamique ou gravitation modifiée, avec prescription relativiste
     lorsque le lentillage est mobilisé ;
M3 : secteur hybride ou collectif produisant des signatures propres ;
O  : modèles d’observation et d’accès, communs ou concurrents,
     incluant déséquilibre, projection et forces non gravitationnelles.
```

`O` n’est pas une cinquième ontologie concurrente. Il représente la couche qui relie
le phénomène physique aux observables. Une erreur dans cette couche peut biaiser la
comparaison entre `M0–M3`, mais ne constitue pas par elle-même une explication globale.

### 3.2 Règle de symétrie critique

Aucune famille ne doit bénéficier d’une souplesse cachée refusée aux autres.

Il faut donc déclarer pour chaque modèle :

- paramètres universels, galactiques et instrumentaux ;
- paramètres partagés entre observables ;
- relations imposées et relations ajustées ;
- domaine de validité ;
- condition de rupture ;
- coût en degrés de liberté effectifs ;
- observables non prédites.

Une théorie qui ne fournit pas de prescription pour un observable ne doit ni recevoir
un succès implicite ni être automatiquement déclarée réfutée. Elle reçoit le verdict
local :

```text
non testable dans ce lot
```

ou :

```text
modèle incomplet pour la comparaison demandée.
```

### 3.3 Niveaux probatoires

Le programme réutilise les niveaux déjà employés dans le corpus :

```text
R1 : reproduction d’un résultat ou d’une chaîne publiée ;
R2 : cohérence interne, tests adversariaux et sensibilités ;
R3 : validation indépendante par une autre route, un autre traceur
     ou une prédiction hors échantillon.
```

Un bon ajustement isolé reste un résultat R1 ou R2 selon les contrôles. Il ne devient
pas une explication physique par simple qualité numérique.

## 4. Dépendance logique des trois axes

L’ordre scientifique initial était naturellement : champ 3D, tomographie, puis audit
du déséquilibre. L’instruction révèle une dépendance plus rigoureuse :

```text
C7-GAL-C — bilan hors équilibre
  qualifie le passage de la cinématique au champ
        ↓
C7-GAL-A — champ radial et vertical
  reconstruit la géométrie avec les accès qualifiés
        ↓
C7-GAL-B — tomographie multi-observables
  exige une description commune de la matière et de la lumière.
```

Cet ordre ne bloque pas une reproduction archivistique de C7-GAL-B. Il interdit
seulement d’interpréter une incompatibilité entre modèles avant d’avoir contrôlé que
les observables comparées sont correctement reliées au champ.

# Axe C — bilan dynamique hors équilibre

## 5. Problème

La chaîne habituelle est :

```text
spectre ou cube de données
→ vitesse de rotation reconstruite
→ vitesse circulaire
→ accélération radiale
→ profil de masse.
```

Chaque flèche contient des hypothèses. Pour le gaz, l’équation locale schématique est :

```math
\frac{\partial \mathbf v}{\partial t}
+(\mathbf v\cdot\nabla)\mathbf v
=-\nabla\Phi
-\frac{1}{\rho}\nabla P
+\mathbf f_{B}
+\mathbf f_{\mathrm{CR}}
+\mathbf f_{\mathrm{autres}}.
```

Une courbe de rotation conventionnelle absorbe ou néglige une partie de ces termes.
Le programme ne suppose ni qu’ils sont dominants, ni qu’ils sont négligeables.

## 6. Question falsifiable

> Quelle part de l’écart entre vitesse observée et vitesse circulaire gravitationnelle
> subsiste après prise en compte contrôlée des termes temporels, convectifs, de
> pression et des mouvements non axisymétriques ?

## 7. Stratégie à trois niveaux

### C1 — simulations avec vérité connue

Dans une simulation, le potentiel, l’accélération réelle et l’histoire temporelle sont
accessibles. Il devient possible de comparer :

```text
vitesse circulaire vraie
≠ vitesse du gaz
≠ courbe reconstruite après projection et réduction.
```

Sorties minimales :

- erreur radiale et temporelle de reconstruction ;
- décomposition du budget d’accélération ;
- identification des états où le biais devient fort ;
- relation entre biais réel et indicateurs observables.

Les suites FIRE et COLIBRE sont des candidates initiales, non des références imposées.
Leur résolution, leur sous-maille et leur fidélité morphologique devront être auditées.

### C2 — données résolues

Priorité aux cubes spectraux plutôt qu’aux seules courbes dérivées.

Échantillons candidats :

- PHANGS-ALMA pour les barres, bras spiraux et mouvements moléculaires résolus ;
- LITTLE THINGS pour les disques HI de galaxies naines ;
- sous-échantillons disposant de plusieurs traceurs gazeux ;
- SPARC uniquement comme couche comparative, sauf accès aux données permettant de
  revenir en amont des courbes publiées.

### C3 — transfert simulation–observation

Le résultat décisif n’est pas « les simulations montrent un biais », mais :

> Les observables disponibles permettent-elles d’identifier, avant l’inférence de
> masse, les galaxies dont la courbe reconstruite est fidèle, biaisée ou non
> identifiable ?

Un score de qualification doit être pré-enregistré à partir de :

- symétrie des côtés approchant et fuyant ;
- amplitude des harmoniques non circulaires ;
- stabilité du centre, de l’inclinaison et de l’angle de position ;
- rapport dispersion sur rotation ;
- présence de barre, interaction, accrétion ou rétroaction récente ;
- cohérence entre phases du gaz ;
- sensibilité au choix de modèle cinématique.

Les objets non qualifiés ne sont pas supprimés. Ils forment une classe de résultat :

```text
accès non qualifié pour une inférence gravitationnelle de précision.
```

## 8. Discriminants et conditions d’échec

L’hypothèse d’un biais substantiel gagne du soutien si :

- l’erreur de reconstruction est prédite hors échantillon par des indicateurs
  observables ;
- une part de la diversité des profils disparaît parmi les systèmes qualifiés ;
- les corrections changent systématiquement l’inférence du profil central ou de la
  masse manquante ;
- plusieurs traceurs convergent après correction.

Elle est limitée si :

- les systèmes les mieux qualifiés conservent le même résidu gravitationnel ;
- les termes hors équilibre restent faibles devant l’écart ;
- les corrections nécessaires contredisent les cartes cinématiques ;
- le score ne se transfère pas des simulations aux observations.

Une correction reposant principalement sur des termes non observés et librement
ajustés ne compte pas comme explication positive.

# Axe A — champ gravitationnel tridimensionnel

## 9. Problème

Une courbe de rotation mesure surtout une composante radiale proche du plan. Des halos
sphériques, aplatis, des distributions baryoniques différentes et certaines lois
modifiées peuvent produire des courbes radiales proches tout en prédisant des champs
verticaux différents.

Le champ recherché est :

```math
\mathbf g(R,z)
=g_R(R,z)\,\mathbf e_R
+g_z(R,z)\,\mathbf e_z.
```

## 10. Question falsifiable

> Une reconstruction baryonique commune et une même loi dynamique peuvent-elles
> reproduire simultanément `g_R(R,z)`, `g_z(R,z)` et leur variation hors du plan,
> sans paramètres réinitialisés selon le traceur ?

## 11. Contrôle géométrique supplémentaire

Si le champ est dérivé d’un potentiel scalaire suffisamment régulier :

```math
g_R=-\frac{\partial\Phi}{\partial R},
\qquad
g_z=-\frac{\partial\Phi}{\partial z},
```

alors les dérivées croisées doivent vérifier localement :

```math
\frac{\partial g_R}{\partial z}
=
\frac{\partial g_z}{\partial R}.
```

Ce contrôle d’intégrabilité ne choisit pas entre halo et gravité modifiée. Il vérifie
si les deux reconstructions décrivent réellement un même champ conservatif dans le
régime étudié. Une violation peut signaler :

- un déséquilibre ;
- une erreur de sélection ou de distance ;
- des populations incompatibles ;
- une reconstruction baryonique insuffisante ;
- une géométrie ou une loi incorrecte.

Il ne doit donc pas être interprété seul.

## 12. Démonstrateur candidat

La Voie lactée est prioritaire parce que Gaia DR3 fournit une information de phase
espace inaccessible pour une galaxie externe. Les compléments spectroscopiques devront
être choisis après audit de leurs fonctions de sélection et de leurs systématiques.

Observables candidates :

- courbe radiale dans et hors du plan ;
- accélération verticale ;
- spirales de phase `z-v_z` ;
- évasement et asymétries du gaz ;
- courants stellaires comme route indépendante ultérieure.

## 13. Contrat commun

Les analyses radiale et verticale doivent partager :

- distance au centre galactique et vitesse solaire ;
- géométrie du disque ;
- cartes de densité stellaire et gazeuse ;
- rapports masse-luminosité et gradients retenus ;
- paramètres globaux du halo ou de la loi modifiée ;
- traitement des populations et de la fonction de sélection.

Les paramètres réellement spécifiques à un traceur restent distincts, mais leur rôle
doit être explicite.

## 14. Discriminants et conditions d’échec

Le lot devient discriminant si une famille :

- ajuste `g_R` mais échoue stablement sur `g_z` ;
- exige des baryons incompatibles entre les deux directions ;
- prédit une variation hors plan distincte ;
- viole la compatibilité géométrique au-delà des systématiques ;
- échoue sur une population tenue hors de l’ajustement.

Le lot doit être suspendu si les effets de non-équilibre, la fonction de sélection et
les incertitudes baryoniques absorbent les différences entre familles.

# Axe B — tomographie multi-observables du même objet

## 15. Problème

La dynamique de matière massive et la déflexion de la lumière ne sondent pas
nécessairement la même combinaison de variables dans toutes les théories.

Dans une écriture faible du champ métrique, selon les conventions :

```math
ds^2
\simeq
-\left(1+\frac{2\Phi}{c^2}\right)c^2dt^2
+\left(1-\frac{2\Psi}{c^2}\right)d\mathbf x^2.
```

La dynamique non relativiste sonde principalement `Φ`, tandis que le lentillage sonde
une combinaison de `Φ` et `Ψ`. En relativité générale avec une matière ordinaire sans
stress anisotrope significatif, ces potentiels sont fortement reliés. Dans une théorie
modifiée, cette relation doit être fournie, non supposée.

## 16. Question falsifiable

> Une même distribution baryonique et une même description gravitationnelle
> prédisent-elles simultanément la cinématique de matière massive et la déflexion de la
> lumière dans le même système, sans réajuster séparément les paramètres communs ?

## 17. Démonstrateur prioritaire

Le système spiral lentille SDSS J2141−0001 constitue un précédent rare où ont été
combinés :

- lentillage fort ;
- rotation du gaz ;
- cinématique stellaire ;
- imagerie haute résolution.

Première question pratique :

> Les données, modèles et vraisemblances nécessaires à une reproduction contemporaine
> sont-ils suffisamment publics et documentés ?

La première sortie peut légitimement être une impossibilité de reproduction établie.

## 18. Contrat de paramètres partagés

Doivent être communs entre les observables :

- distance et redshift ;
- centre, orientation, inclinaison et géométrie ;
- carte de lumière et décomposition bulbe-disque ;
- masse gazeuse ;
- paramètres de population stellaire ou rapports masse-luminosité ;
- loi ou métrique gravitationnelle ;
- distribution sombre lorsqu’elle appartient au modèle.

Les fonctions de dispersion instrumentale, points d’étalonnage et bruits restent
spécifiques. Elles ne doivent pas modifier implicitement la masse physique commune.

## 19. Règle théorique

Une prescription non relativiste qui ajuste les courbes de rotation n’est pas un modèle
complet pour ce lot. Elle doit être associée à :

- une complétion relativiste déclarée ;
- ou une prescription de lentillage dérivée et testable ;
- ou un verdict explicite de non-comparabilité.

La règle vaut symétriquement pour les modèles de matière sombre : le profil utilisé
pour la rotation doit prédire le lentillage, et non être remplacé par une autre
paramétrisation sans test.

## 20. Échelons

```text
B1 : reproduction archivistique SWELLS ;
B2 : audit du partage réel des paramètres ;
B3 : comparaison de familles sur un système ;
B4 : extension à plusieurs lentilles spirales si les données le permettent ;
B5 : prospective Euclid ou Rubin, clairement séparée des données acquises.
```

## 21. Discriminants et conditions d’échec

Le lot devient discriminant si :

- un modèle ajustant la rotation échoue sur le lentillage avec les mêmes baryons ;
- les observables exigent des rapports masse-luminosité incompatibles ;
- une famille prédit une dépendance à l’inclinaison ou une géométrie de lentille
  distincte ;
- la combinaison réduit réellement la dégénérescence disque-halo ou loi-baryons ;
- une observable tenue hors ajustement est correctement prédite.

Le lot échoue si :

- les données ou vraisemblances ne sont pas reproductibles ;
- la flexibilité des modèles rend les paramètres non identifiables ;
- les différences entre familles sont dominées par la reconstruction baryonique ;
- les complétions relativistes comparées ajoutent trop de liberté pour produire une
  prédiction propre.

# Contrat transversal

## 22. Graphe commun de l’inférence

Chaque lot doit rendre explicite :

```text
données brutes
→ réduction et sélection
→ observable reconstruite
→ modèle baryonique
→ équation de passage
→ champ, potentiel ou métrique
→ prédictions
→ vraisemblance
→ comparaison et verdict borné.
```

Un paramètre doit être étiqueté :

```text
physique partagé ;
physique spécifique au modèle ;
astrophysique ;
instrumental ;
numérique ;
paramètre de sélection ;
quantité dérivée.
```

## 23. Interdits initiaux

Avant un pré-enregistrement distinct :

- aucune sélection d’objets après inspection des résultats de masse ;
- aucun réglage des critères de qualité pour favoriser une famille ;
- aucune fusion de traceurs incompatibles sans modèle de passage ;
- aucune interprétation ontologique d’un meilleur ajustement ;
- aucune conclusion générale sur la matière sombre depuis le seul domaine galactique ;
- aucun comptage de données futures comme validation présente.

## 24. Métriques recommandées

Les métriques exactes seront fixées par lot. Le socle comprend :

- contrôles prédictifs postérieurs ;
- prédiction d’une observable tenue hors ajustement ;
- sensibilité aux priors et aux fonctions de sélection ;
- compatibilité des paramètres partagés entre traceurs ;
- résidus spatiaux structurés, non seulement `χ²` global ;
- complexité effective et identifiabilité ;
- reproduction sur données simulées avec vérité connue.

Les facteurs de Bayes peuvent être utilisés, mais jamais sans audit de sensibilité aux
priors. Les critères d’information ne remplacent pas la vérification physique des
résidus.

## 25. Matrice de décisions

| Résultat | Interprétation permise | Interprétation interdite |
|---|---|---|
| les corrections hors équilibre sont faibles sur les systèmes qualifiés | elles ne suffisent pas dans ce domaine | toute systématique cinématique est négligeable |
| les corrections réduisent fortement la diversité des courbes | une part du problème était dans l’accès | la matière sombre est inexistante |
| `g_R` et `g_z` exigent une composante supplémentaire cohérente | soutien galactique à cette famille de modèles | identification de la nature microscopique de la composante |
| une loi modifiée prédit radial, vertical et lentillage | gain discriminant local | validité cosmologique générale |
| rotation et lentillage sont incompatibles sous paramètres partagés | modèle ou reconstruction communs insuffisants | réfutation ontologique immédiate d’une famille entière |
| aucune famille n’est identifiable | données ou programme insuffisants | équivalence physique des théories |

## 26. Phases et portes

### G0 — audit des sources

- vérifier le statut publié ou prépublication ;
- récupérer données, code et licences ;
- distinguer résultat, affirmation des auteurs et interprétation secondaire ;
- établir les dépendances logicielles et les données absentes.

### G1 — spécification

- sélectionner un démonstrateur par axe ;
- figer les équations de passage ;
- définir paramètres partagés, nuisances et critères d’exclusion ;
- pré-déclarer les tests de sensibilité.

### G2 — reproduction

- reproduire au moins une chaîne publiée ou un sous-résultat ;
- documenter toute impossibilité ;
- exécuter des tests adversariaux sur données simulées.

### G3 — comparaison discriminante

- comparer au moins deux familles physiques et plusieurs modèles d’accès ;
- tenir une observable ou un sous-échantillon hors ajustement ;
- publier les échecs et non-identifiabilités.

### G4 — synthèse bornée

Pour chaque axe :

```text
gain discriminant ;
limites ;
rang probatoire ;
verdict local ;
coût de poursuite ;
recommandation : arrêter, prolonger ou ratifier.
```

## 27. Registre initial des sources

Les sources suivantes constituent un point de départ à auditer, non une bibliographie
validée.

### Déséquilibre et courbes reconstruites

1. Sands et al., *Confronting the Diversity Problem: The Limits of Galaxy Rotation
   Curves as a Tool to Understand Dark Matter Profiles*, arXiv:2404.16247.
2. Liu, Li & Shen, *The Impact of Bar-induced Non-Circular Motions on the Measurement
   of Galactic Rotation Curves*, arXiv:2501.12760.
3. Dado et al., *Dynamical disequilibrium in dwarf galaxies: rethinking gas dynamics,
   rotation curves, and dark matter inference*, arXiv:2512.11033 — prépublication.
4. Lopez-Coba et al., *On the role of non-circular motions in MaNGA galaxies I:
   global properties*, arXiv:2410.21147.
5. Iorio et al., *LITTLE THINGS in 3D: robust determination of the circular velocity
   of dwarf irregular galaxies*, arXiv:1611.03865.

### Champ radial et vertical

6. Antoja et al., *The phase spiral in Gaia DR3*, arXiv:2212.11987.
7. Hunt et al., *Multiple phase spirals suggest multiple origins in Gaia DR3*,
   arXiv:2206.06125.
8. Lopez-Corredoira, *Milky Way dark matter distribution or MOND test from vertical
   stellar kinematics with Gaia DR3*, arXiv:2412.09665.
9. Wang et al., *Milky Way Dynamics Favor Dark Matter over Modified Gravity Models*,
   arXiv:2605.10857 — prépublication récente, conclusion à auditer.
10. Sylos Labini & Capuzzo-Dolcetta, *Constraining the Geometry of Galactic Dark Matter
    with Gaia Data Release 3*, arXiv:2606.12548 — prépublication récente, conclusion à
    auditer.

### Tomographie multi-observables

11. Dutton et al., *The SWELLS survey. II. Breaking the disk-halo degeneracy in the
    spiral galaxy gravitational lens SDSS J2141-0001*, arXiv:1101.1622.
12. Barnabè et al., *The SWELLS survey. IV. Precision measurements of the stellar and
    dark matter distributions in a spiral lens galaxy*, arXiv:1201.1692.
13. Treu et al., *The SWELLS Survey. I. A large spectroscopically selected sample of
    edge-on late-type lens galaxies*, arXiv:1104.5663.
14. Harvey-Hawes & Galoppo, *A Novel Test for MOND: Gravitational Lensing by Disc
    Galaxies*, arXiv:2411.17888 — proposition prospective à auditer.

## 28. Décision provisoire

```text
les trois angles sont retenus comme programme exploratoire ;
le lot C7-GAL-C est méthodologiquement prioritaire ;
C7-GAL-A porte le discriminant géométrique central ;
C7-GAL-B porte le test de cohérence le plus fort mais aussi le risque
  de données insuffisantes et de flexibilité théorique ;
aucune famille explicative n’est présélectionnée ;
aucune modification de la couche active du cycle 7 n’est encore justifiée.
```

La prochaine décision utile n’est pas de choisir une théorie. Elle est de sélectionner
le premier démonstrateur qui maximise simultanément :

```text
accessibilité des données
+ vérité ou contrôle indépendant
+ pouvoir discriminant
- flexibilité des nuisances
- coût computationnel et documentaire.
```
