# Addendum C7-GAL-D — concordance inter-échelles et indépendance probatoire v0.1

## 0. Statut

```text
statut : exploration datée ;
cycle : 7 — cosmologie ;
raccorde : programme C7-GAL, issue directrice #83 ;
axe : D — transversal ;
issue dédiée : #91 ;
autorité normative : aucune ;
ne remplace pas : les trois lots galactiques A–C ;
condition de sortie : cartographie des dépendances, sélection d’un premier raccord
                      quantitatif, puis décision humaine séparée.
```

Cet addendum conserve la généalogie du programme : les trois angles A–C restent des
démonstrateurs galactiques. D ajoute une question inter-échelles apparue après leur
installation.

## 1. Distinction directrice

```text
abondance cosmologique de matière sombre
≠ distribution de matière sombre dans les halos
≠ inférence locale de cette distribution.
```

Ces trois niveaux ne sont ni indépendants ni interchangeables.

- le CMB contraint une abondance cosmologique sous un modèle donné ;
- la formation des structures relie cette abondance aux halos ;
- les observations tardives reconstruisent des distributions locales ou statistiques.

Un accord entre ces niveaux peut constituer une validation convergente forte, mais le
gain probatoire dépend de l’indépendance réelle des données, priors, modèles de passage
et simulations mobilisés.

## 2. Question directrice

> Quelle part de la concordance `CMB → croissance → structures tardives` constitue une
> validation réellement indépendante de la matière sombre, et quelle part exprime la
> propagation cohérente d’hypothèses ou paramètres communs ?

La question n’est pas de dévaluer les analyses multi-sondes. Elle vise à distinguer :

```text
nouvelle information empirique
≠ propagation d’une contrainte antérieure
≠ cohérence interne d’un même cadre
≠ validation hors échantillon.
```

## 3. Sous-question D1 — dépendance probatoire

Pour chaque route tardive retenue, cartographier :

- données réellement distinctes ;
- paramètres cosmologiques libres, hérités ou recalibrés ;
- priors externes ;
- hypothèses de fond communes ;
- fonctions de transfert ;
- simulations ou émulateurs ;
- nuisance astrophysique ;
- observable qui resterait informative si la contrainte CMB sur `Ω_c h²` était retirée.

Routes candidates :

```text
CMB primaire ;
CMB lensing ;
BAO et croissance ;
RSD ;
lentillage faible ;
amas ;
statistiques de grandes structures ;
dynamique galactique, seulement comme niveau local distinct.
```

Aucun score synthétique d’« indépendance » n’est présupposé. Une matrice de dépendance
est préférable à un nombre dont le sens serait fragile.

## 4. Sous-question D2 — fraction cosmique et fractions locales

La fraction baryonique cosmologique ne doit pas être comparée directement à la fraction
d’une galaxie individuelle.

Chaîne à instruire :

```text
fraction cosmique moyenne
→ accrétion dans les halos
→ refroidissement / chauffage
→ formation stellaire
→ éjection / réaccrétion
→ redistribution radiale
→ réponse du halo
→ fraction observée à bas redshift.
```

Questions discriminantes :

1. quelles classes de halos approchent la fraction cosmique ?
2. où sont attendus les baryons non présents dans les étoiles ou le gaz froid ?
3. quelle dispersion est attendue à masse de halo fixée ?
4. quelle part de cette dispersion dépend du modèle de feedback ?
5. quels observables contraignent la matière circumgalactique et intergalactique sans
   réutiliser simplement la masse de halo déjà inférée ?

## 5. Sous-question D3 — co-évolution baryons / halo

Une distribution sombre à `z≈0` n’est pas nécessairement un fond passif qui aurait
simplement accueilli les baryons.

Distinguer :

```text
interaction directe DM–matière standard
≠ auto-interaction DM–DM
≠ couplage gravitationnel collectif
≠ réponse du halo à une variation temporelle du potentiel baryonique.
```

Mécanismes à auditer :

- contraction du halo lors de la concentration baryonique ;
- transfert d’énergie par fluctuations rapides du potentiel ;
- friction dynamique ;
- expulsions et réaccrétions de gaz ;
- réponse aux barres, satellites et fusions ;
- dépendance à l’histoire de formation.

Question centrale :

> Dans quelle mesure la distribution sombre inférée à bas redshift est-elle elle-même
> le produit historique de la dynamique baryonique utilisée comme traceur ?

Cette question se raccorde directement à C7-GAL-C (#86).

## 6. Matrice de travail proposée

Pour chaque sonde ou résultat :

| Colonne | Question |
|---|---|
| Observable primaire | Qu’est-ce qui est effectivement mesuré ? |
| Objet reconstruit | Quelle grandeur physique ou statistique est inférée ? |
| Paramètres communs | Quels paramètres sont partagés avec le CMB ou d’autres sondes ? |
| Priors externes | Quelles informations viennent d’ailleurs ? |
| Modèle de passage | Quelle chaîne transforme l’observable en contrainte cosmologique ? |
| Simulation / émulateur | Quelle dépendance numérique ou astrophysique intervient ? |
| Nuisances | Qu’est-ce qui peut absorber une discordance ? |
| Test sans prior CMB | Que reste-t-il contraint indépendamment ? |
| Validation hors échantillon | Quelle prédiction n’a pas servi à l’ajustement initial ? |
| Rupture | Quel résultat invaliderait le raccord local ? |

## 7. Première hiérarchie d’instruction

Ordre recommandé :

```text
D0 — CMB primaire : isoler ce qui contraint Ω_b h² et Ω_c h² ;
D1 — CMB lensing : distinguer données nouvelles et paramètres hérités ;
D2 — BAO + croissance/RSD : cartographier les dépendances communes ;
D3 — lentillage faible / amas : ajouter l’astrophysique baryonique ;
D4 — raccord aux halos galactiques : seulement après les niveaux précédents.
```

Cet ordre évite d’utiliser immédiatement les galaxies comme « confirmation » de la
fraction cosmique alors que la formation des halos constitue précisément le pont à
examiner.

## 8. Conditions d’échec

L’axe D échoue méthodologiquement si :

- « Planck mesure 84/16 » est traité comme une observation directe de particules ;
- la fraction cosmique est attendue dans chaque galaxie sans modèle de formation ;
- deux analyses partageant données, priors ou simulations dominantes sont comptées
  comme validations pleinement indépendantes ;
- une anomalie galactique est promue directement en réfutation de l’inférence CMB ;
- l’accord CMB est utilisé pour valider sans test un profil de halo local ;
- la complexité des dépendances est réduite à un score d’indépendance non justifié.

## 9. Conditions de réussite

Le lot gagne une valeur discriminante s’il permet de séparer explicitement :

```text
concordance multi-données réellement indépendante ;
concordance partiellement indépendante ;
propagation cohérente d’un même cadre ;
validation hors échantillon ;
tension ou rupture de raccord.
```

La sortie recherchée est une carte de la chaîne probatoire, pas un verdict général sur
la matière sombre.

## 10. Décision de raccord

```text
A–C : trois démonstrateurs galactiques conservés ;
D   : axe transversal inter-échelles ajouté ;
C ↔ D : raccord explicite par la co-évolution baryons / halo ;
aucune modification automatique de l’index ou des synthèses actives.
```
