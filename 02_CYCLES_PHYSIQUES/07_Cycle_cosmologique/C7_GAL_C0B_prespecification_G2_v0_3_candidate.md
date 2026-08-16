# C7-GAL-C0-B — pré-spécification G2 v0.3 candidate

Version : `v0.3-candidate`
Date : `2026-08-16`
Issue d'origine : `#97`
Dossier historique : PR `#98`, commit `10e9466be1ebc983da39a66ac31788a55e09836b`
Statut : `EXPERIMENTAL_SUCCESSOR_CANDIDATE`
Autorité canonique : `AUCUNE`

## 0. Fonction de cette version

Cette v0.3 candidate teste si la pré-spécification G2 peut devenir plus courte et plus discriminante sans perdre les protections réellement utiles de la v0.2 historique.

La v0.2 de #98 reste un dossier technique et probatoire adressable par son commit : unités détaillées, nomenclature des softenings, paramètres publics FIRE/GIZMO, périodicité, familles de solveurs, batterie S/D/K, dettes et sources. Elle n'a pas besoin d'être copiée dans l'arbre actif pour conserver cette fonction de provenance.

La répartition testée est :

```text
#98 @ 10e9466 = preuve détaillée et généalogie historique
v0.3 candidate = contrat actif minimal pour la prochaine décision scientifique
```

Toute exigence nécessaire à une décision active doit être lisible dans cette v0.3 ou être matérialisée ultérieurement dans un protocole/manifeste exécutable qualifié. Une règle qui ne serait découvrable qu'en retournant dans la v0.2 historique n'a pas d'autorité active.

Les labels historiques restent secondaires. Lorsqu'un ancien sigle est utile à la traçabilité, le nom humain de la fonction porte le sens et le sigle ne sert que de repère généalogique.

## 1. Question scientifique protégée

Le lot C7-GAL-C cherche à déterminer quelle part de l'écart entre cinématique du gaz et support gravitationnel subsiste lorsque l'accès par courbe de rotation cesse d'être supposé exact.

La route G2 ne doit donc pas produire d'abord une courbe de rotation. Elle doit d'abord reconstruire un champ gravitationnel suffisamment qualifié pour tester si une réduction en profil radial est scientifiquement admissible dans le régime étudié.

Dans ce document, la **cinématique intrinsèque du gaz** désigne les vitesses du gaz dans le référentiel galactique reconstruit, avant projection instrumentale ou pseudo-observation. Le label historique `O1` peut être utilisé comme raccourci de traçabilité, mais ne remplace pas cette définition.

La séquence active devient :

```text
sources FIRE publiques
-> champ vectoriel reconstruit
-> qualification de la géométrie et du régime
-> réduction éventuelle en profil radial
-> comparaison avec la cinématique intrinsèque du gaz
-> décision éventuelle FIELD -> EOM
```

Aucune étape ultérieure ne doit être utilisée pour régler rétroactivement une étape antérieure.

## 2. Nommer la cible avant de mesurer une erreur

### 2.1 Cible numérique primaire

La cible primaire est le champ instantané associé à la réalisation FIRE publique effectivement disponible, avec les masses discrètes, le kernel, les softenings et les conditions de bord qualifiées :

```text
G2-FIELD = champ de la réalisation numérique FIRE déclarée
```

Cette cible n'est pas appelée « vérité gravitationnelle totale ». Elle est un objet numérique situé dont la provenance et la fidélité doivent être explicites.

Le dossier historique #98 documente que, pour le gaz, le softening adaptatif est lié au kernel et que `SmoothingLength_HDF5` porte l'information de support pertinente. Pour les espèces collisionnelles à softening fixe, la correspondance exacte entre paramètre historique et support de kernel reste à qualifier contre le changeset ou une sortie de démarrage adéquate avant calcul de référence.

Ces éléments n'acquièrent une fonction opérationnelle qu'une fois recopiés avec leur source et leur valeur exacte dans le futur protocole/manifeste exécutable ; le code ne doit pas dépendre de l'interprétation implicite d'un ancien document.

### 2.2 Cible EOM conditionnelle

`G2-EOM` désigne l'accélération gravitationnelle effectivement utilisée dans l'équation du mouvement d'un élément adaptatif identifié, avec les termes conservatifs requis par la formulation du code.

Elle n'est pas présupposée nécessaire. Elle devient une dette active uniquement si la différence FIELD/EOM peut être comparable à l'effet scientifique que l'on cherche à interpréter, ou si cette différence reste impossible à borner.

### 2.3 Continuum physique : autre question

La comparaison de la réalisation discrète et adoucie à un continuum non adouci ou à une limite de résolution ne mesure pas l'erreur de reconstruction de `G2-FIELD`. Elle mesure un écart de représentation ou de résolution entre deux objets différents.

Cette comparaison peut être scientifiquement utile, mais elle doit être annoncée comme telle.

## 3. Conditions de validité avant toute courbe

Les points suivants ne constituent pas une barre d'erreur. S'ils ne sont pas suffisamment établis pour le niveau de fidélité revendiqué, la reconstruction est suspendue, limitée ou requalifiée.

### 3.1 Identité des sources et unités

Avant de revendiquer un **champ avec conditions de bord suffisamment fidèles** à la simulation (ancien niveau `F2`) :

- confirmer la concordance des attributs utiles du snapshot visé avec les conventions publiques retenues ;
- vérifier les comptes d'espèces et la couverture nécessaire des sources ;
- appliquer les conversions `a/h` provenant des sources primaires et les figer avec leurs valeurs dans le manifeste exécutable ;
- enregistrer la convention de `G` utilisée ;
- n'ouvrir une décision métrologique supplémentaire sur `G` que si l'écart entre conventions devient non négligeable devant la précision scientifique pertinente.

Une mauvaise unité ou une provenance non établie invalide le produit ; elle n'est pas absorbée dans une incertitude.

### 3.2 Softening et loi de source

- gaz : utiliser directement l'information de kernel sauvegardée lorsque sa signification pour le changeset est qualifiée ;
- PartType1 (matière sombre haute résolution), PartType2 (matière sombre basse résolution du volume) et PartType4 (étoiles) : qualifier la correspondance exacte paramètre de softening -> support de kernel avant d'en faire une référence de champ ;
- ne jamais remplacer silencieusement la loi spline par une force de Plummer ;
- conserver PartType2 tant que sa non-pertinence physique n'est pas démontrée pour le domaine étudié.

### 3.3 Conditions de bord

La route périodique reste candidate seulement après confirmation de `BoxSize`, de la couverture des sources nécessaires, de la convention du mode moyen et d'un oracle périodique qualifié.

Une reconstruction isolée peut être utilisée comme **contrôle local** (ancien niveau `F1`). Elle ne devient pas une référence avec bords qualifiés (ancien `F2`) par commodité.

## 4. Référentiel et géométrie : préserver ce que l'on cherche à tester

### 4.1 Centre et vitesse système

Le produit publié FIRE (`host_coordinates`) reste la route primaire candidate lorsqu'il sera autorisé et qualifié. Une reconstruction indépendante depuis les particules reste le contrôle.

Un désaccord robuste entre centres ou vitesses n'est pas résolu en choisissant la variante qui améliore le résidu scientifique. Il produit une sensibilité symétrique ou un verdict de référentiel insuffisamment unique.

### 4.2 Orientation

L'orientation du disque est un choix scientifique parce qu'elle détermine les composantes radiale, azimutale et verticale. La règle d'orientation doit être fixée avant inspection du résidu cinématique/champ ou incluse dans une sensibilité symétrique préenregistrée.

Aucune circularité orbitale dérivée d'un potentiel déjà reconstruit ne doit servir silencieusement à définir l'axe qui sera ensuite utilisé pour tester ce même potentiel.

### 4.3 Dépendance azimutale

Le champ primaire doit conserver la dépendance azimutale :

```text
g_FIELD(x,y,z)
```

ou, dans le repère cylindrique qualifié :

```text
g_R_FIELD(R,phi,z)
g_phi_FIELD(R,phi,z)
g_z_FIELD(R,phi,z)
```

Un produit ne doit pas devenir `g_R_FIELD(R,z)` par simple omission de `phi`.

## 5. Sorties : distinguer champ local, réduction et diagnostic circulaire

### 5.1 Sortie primaire

Le produit scientifique primaire est le champ vectoriel local, accompagné de :

- coordonnées d'évaluation ;
- composantes cartésiennes et/ou cylindriques ;
- provenance des sources ;
- centre et rotation ;
- kernel et softenings ;
- conditions de bord ;
- paramètres du solveur nécessaires à la reproductibilité ;
- statut de validité et erreurs numériques bornées.

### 5.2 Réduction azimutale ou sectorielle

Toute réduction de `phi` est un opérateur d'analyse distinct et doit être nommé. On note génériquement :

```text
g_R,red(R,z ; O_phi) = O_phi[g_R(R,phi,z)]
```

où `O_phi` peut être une moyenne azimutale, une médiane, un secteur, une composante harmonique ou un autre opérateur justifié.

Avant promotion d'un profil réduit, conserver au minimum :

- `g_phi` ;
- la variation azimutale de `g_R` et `g_z` ;
- un diagnostic de non-axisymétrie choisi avant le résidu cible ;
- la définition exacte de `O_phi`.

Le diagnostic ne doit pas être plus détaillé que nécessaire pour changer la décision scientifique suivante.

Une réduction générique n'est pas appelée « axisymétrique » ou « circulaire » par simple perte de la coordonnée `phi`.

### 5.3 Vitesse équivalente de force et vitesse circulaire axisymétrisée

À partir d'une réduction quelconque du champ radial, on peut construire la quantité dimensionnelle :

```text
v_F,red(R) = sqrt(R |g_R,red(R,0 ; O_phi)|)
```

`v_F,red` est un diagnostic de force radiale réduite. Il ne reçoit pas automatiquement le nom de vitesse circulaire.

Si `O_phi` est explicitement l'opérateur définissant la composante axisymétrique du champ — par exemple la moyenne azimutale ou le mode `m=0` selon une convention qualifiée — on peut en dériver :

```text
v_circ,axi(R) = sqrt(R |g_R,m=0(R,0)|)
```

Cette quantité est la vitesse circulaire du **champ axisymétrisé** ainsi défini. Elle n'affirme ni l'existence d'une orbite circulaire dans le champ non axisymétrique complet, ni que le gaz réel doive suivre cette vitesse.

La question dynamique vient ensuite : dans quelle mesure la cinématique intrinsèque du gaz suit-elle `v_circ,axi`, ou s'en écarte-t-elle sous l'effet de mouvements non circulaires, de termes temporels, de pression ou d'autres soutiens ? Cet écart peut être le résultat scientifique à expliquer ; il ne rend pas à lui seul la reconstruction gravitationnelle invalide.

Le nom historique `v_grav` peut être conservé comme alias de provenance, mais il ne doit pas masquer la transformation effectuée. Un autre opérateur `O_phi` conserve le nom `v_F,red` tant qu'une interprétation circulaire supplémentaire n'a pas été justifiée.

## 6. Famille de solveur : choisir après la cible, pas après le résidu

Le document ne ratifie aucun logiciel.

La route candidate reste :

```text
court champ : arbre ou méthode équivalente avec loi M4 qualifiée
long champ : méthode Particle-Mesh (PM) ou correction périodique qualifiée si requise
petits tests : somme directe ou oracle indépendant
```

Une architecture TreePM — arbre au court rayon, Particle-Mesh au long rayon — est pertinente parce que le run original utilise une séparation court/long périodique, mais la ressemblance d'algorithme ne vaut pas reproduction automatique du changeset FIRE.

Une méthode multipolaire rapide (Fast Multipole Method, FMM) ou d'autres familles peuvent rester des candidats techniques si elles reproduisent la même cible et les mêmes conditions de bord avec une qualification indépendante.

## 7. Validation : séparer trois questions

### 7.1 Le solveur reproduit-il le même objet discret ?

Niveau `S` : pour les mêmes masses, positions, softenings, conditions de bord et points d'évaluation, comparer la méthode candidate à un oracle discret approprié.

Cette étape qualifie l'accès numérique à la cible.

### 7.2 Que change la réalisation discrète ?

Niveau `D` : lorsqu'une comparaison au continuum est scientifiquement pertinente, mesurer la différence entre réalisation particulaire et représentation continue avec le même modèle de kernel.

Cette étape ne doit pas être imputée au solveur.

### 7.3 Que change le kernel/softening ?

Niveau `K` : comparer, lorsque pertinent, la représentation adoucie à une limite ou un continuum non adouci.

Cette étape qualifie un effet de représentation/résolution, pas une mauvaise reconstruction de la réalisation FIRE.

### 7.4 Tests minimaux conservés

Le dossier historique #98 contient une batterie détaillée T1-T8. La v0.3 n'en conserve comme exigences actives que les fonctions discriminantes :

- loi de paire/kernel et supports inégaux ;
- sphère de Plummer comme distribution analytique, non comme loi de softening FIRE ;
- Hernquist pour la dynamique radiale ;
- Miyamoto-Nagai pour la géométrie aplatie ;
- superposition et fermeture par composantes ;
- invariances de translation, rotation, permutation et unités ;
- périodicité, mode moyen et raccord court/long ;
- comparaison interméthodes contre un oracle commun, jamais par vote majoritaire.

Avant exécution, ces fonctions devront être transformées en protocole testable avec entrées, oracle, métriques, tolérances et sens autorisé du verdict. Les détails historiques de #98 peuvent informer cette rédaction mais ne valent pas automatiquement règle active.

## 8. Ne plus appeler tout cela un unique « budget d'erreur »

### 8.1 Conditions de validité

Exemples : provenance, conventions d'unités, couverture de sources, conditions de bord constitutives, réussite d'un oracle bloquant, fermeture compatible avec l'implémentation.

Échec -> suspension, limitation ou invalidation du niveau revendiqué.

### 8.2 Erreurs numériques bornables

Exemples : résidu du solveur, interpolation, discrétisation d'une grille d'évaluation, convergence de raffinement.

Elles peuvent recevoir une borne lorsqu'un oracle ou une convergence indépendante le permet.

### 8.3 Sensibilités de repère et de réduction

Centre, vitesse système, orientation, bins et réduction azimutale ne sont pas des erreurs du champ au même sens que le résidu d'un solveur. Ils définissent ou transforment l'accès au résultat scientifique.

Ils doivent être gelés ou explorés symétriquement avant le résidu cible.

### 8.4 Écarts de représentation/résolution

Discrétisation particulaire et kernel/softening sont rapportés à une autre cible physique ou continue lorsqu'une telle comparaison est pertinente.

### 8.5 Passage FIELD -> EOM

L'écart `E_EOM` reste séparé. Il ne devient bloquant que si sa taille ou son impossibilité de bornage peut changer l'interprétation scientifique.

## 9. Frontière entre pré-enregistrement scientifique et qualification technique

### 9.1 À geler avant exposition au résidu scientifique

Tout choix capable de changer la signification ou le verdict :

- objet comparé ;
- domaine scientifique ;
- centre, vitesse et orientation ;
- traceur ;
- opérateur de réduction ;
- conditions de bord physiquement revendiquées ;
- niveau de fidélité FIELD/EOM ;
- masque scientifique ;
- métrique et seuil de décision ;
- règle de comparaison entre cinématique intrinsèque et champ gravitationnel.

### 9.2 À qualifier techniquement hors cible

Un paramètre d'implémentation peut être choisi ou raffiné sans ratification humaine valeur par valeur lorsque :

1. la propriété protégée est déclarée ;
2. l'oracle ou le synthétique est indépendant du résidu cible ;
3. la tolérance est fixée avant cible ;
4. les échecs pertinents sont conservés ;
5. le réglage ne change ni la cible ni l'opérateur scientifique.

Cela couvre typiquement angle d'ouverture, résolution PM, ordre d'expansion, précision arithmétique et stratégie de raffinement.

Le principe de contrôle reste :

> Si cette contrainte disparaît, quelle décision scientifique devient réellement moins sûre ?

Une contrainte sans effet démontrable sur validité, cible, rang probatoire, reproductibilité ou décision suivante ne doit pas devenir une règle durable.

## 10. Décomposition des composantes

Le niveau FIELD doit conserver séparément les contributions des espèces présentes :

```text
g_gas
g_PT1
g_PT2
g_PT4
g_total
```

La fermeture vectorielle est un contrôle d'implémentation. Une bonne fermeture ne valide ni la loi de source, ni les bords, ni l'interprétation physique.

Au niveau EOM, aucune correction adaptative ne sera redistribuée arbitrairement comme nouvelle densité d'une espèce sans dérivation du code.

## 11. Dettes actives avant la prochaine décision

Seules les dettes capables de bloquer ou de changer la prochaine étape restent actives dans le document directeur :

1. confirmer `BoxSize`, comptes d'espèces et couverture nécessaire pour la route périodique revendiquée ;
2. qualifier la correspondance du softening fixe vers le support de kernel pour le changeset historique ;
3. autoriser et qualifier le référentiel publié ou son contrôle indépendant ;
4. définir le domaine spatial et les opérateurs de réduction sans inspection du résidu scientifique ;
5. transformer les fonctions de validation en protocole exécutable et fixer leurs tolérances avant cible ;
6. démontrer qu'une implémentation candidate reproduit l'oracle requis ;
7. n'ouvrir `G2-EOM` que si le test FIELD/EOM le rend nécessaire.

Les questions de coût, version de bibliothèque, paramètres fins de convergence et détails comparables restent des dettes techniques locales jusqu'à ce qu'elles puissent changer l'une de ces décisions.

## 12. Séquence de décision

```text
1. fermer l'identité matérielle minimale des snapshots et des bords
2. qualifier unités + kernel/softening + référentiel
3. définir champ vectoriel, domaine et opérateurs de réduction sans résidu cible
4. choisir une implémentation candidate
5. matérialiser et valider les tests sur oracles indépendants
6. exécuter D/K seulement pour les questions de représentation réellement pertinentes
7. reconstruire G2-FIELD en conservant phi
8. produire les diagnostics de non-axisymétrie et les réductions préenregistrées
9. construire v_F,red pour les réductions utiles
10. construire v_circ,axi seulement pour la composante axisymétrisée explicitement définie
11. comparer la cinématique intrinsèque du gaz sans présupposer qu'elle doit tracer exactement v_circ,axi
12. décider si FIELD -> EOM est nécessaire
```

Aucun résultat scientifique sur matière sombre ou gravité modifiée n'est produit par cette pré-spécification.

## 13. Falsificateurs de la v0.3 candidate

La v0.3 candidate échoue si :

- une protection importante du dossier historique disparaît sans remplacement fonctionnel ;
- elle oblige à retourner dans #98 pour comprendre une décision active ;
- une règle de #98 acquiert de fait une autorité active sans être repromue explicitement ;
- la conservation de `phi` ne peut changer aucune décision du lot C7-GAL-C ;
- la distinction validité / erreur / représentation ne change aucun verdict pratique ;
- la liberté technique hors cible permet en pratique de régler le résidu scientifique ;
- elle devient plus longue ou plus complexe par accumulation ultérieure.

## 14. Statut de sortie expérimental

```text
C0-B_V03_CANDIDATE = A_TESTER
DOSSIER_V02 = PROVENANCE_HISTORIQUE_#98@10e9466
G2 = NON_AUTORISEE
CALCUL_FIRE = NON_AUTORISE
MERGE = NON_AUTORISE
```

La question de qualification est désormais :

> Cette v0.3 permet-elle de prendre la prochaine décision G2 avec moins de règles actives, sans perdre la capacité de détecter une mauvaise cible, un mauvais accès, une réduction injustifiée ou un réglage post-hoc ?

## 15. Sources et provenance

Le dossier historique #98 @ `10e9466` conserve la traçabilité détaillée. Les sources primaires qui soutiennent les choix locaux comprennent notamment :

- Wetzel et al. (2023), diffusion publique FIRE-2 ;
- Hopkins et al. (2018), méthodes FIRE-2 ;
- documentation officielle GIZMO, notamment kernel et softenings adaptatifs ;
- Price & Monaghan (2007), softening gravitationnel adaptatif conservatif ;
- Springel (2005), GADGET-2 et TreePM périodique ;
- Sands et al. (2024), limites des reconstructions de courbes de rotation en régime non circulaire/hors équilibre.

La v0.3 candidate n'élève ni le dossier historique ni ces références au rang d'autorité normative générale du dépôt. Elles soutiennent seulement les choix physiques et numériques locaux de C7-GAL-C0-B.
