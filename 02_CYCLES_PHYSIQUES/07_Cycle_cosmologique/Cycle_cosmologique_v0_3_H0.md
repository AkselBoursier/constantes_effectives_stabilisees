# Cycle cosmologique v0.3

## Fiche 2 : H_0

### 1. Fonction de la fiche

Cette fiche porte sur :

```text
H_0
```

le parametre de Hubble actuel.

La question directrice est :

> Comment H_0 peut-il etre a la fois un parametre d'etat actuel, une grandeur fortement contrainte, et le lieu d'une tension entre regimes d'acces ?

Objectif :

```text
classer H_0 comme parametre d'etat actuel dans l'architecture cosmologique, sans le traiter comme constante fondamentale.
```

La fiche doit eviter trois erreurs.

Premiere erreur :

```text
H_0 = constante fondamentale
```

Deuxieme erreur :

```text
tension H_0 = famille taxonomique
```

Troisieme erreur :

```text
mesure locale de H_0 = meme objet epistemique que l'inference CMB + LambdaCDM
```

La bonne formulation est :

```text
H_0 est une valeur actuelle du taux d'expansion, connue par plusieurs regimes d'acces, et devenue le lieu d'une tension entre routes d'inference.
```

### 2. Identification

Grandeur :

```text
H_0
```

Nom :

```text
parametre de Hubble actuel
```

Definition cosmologique :

```text
H(t) = a_dot(t) / a(t)
H_0 = H(t_0)
```

Type logique :

```text
parametre d'etat actuel
```

Dimension :

```text
[H_0] = temps^-1
```

Unite usuelle :

```text
km s^-1 Mpc^-1
```

Parametre reduit :

```text
h = H_0 / (100 km s^-1 Mpc^-1)
```

Statut de rang :

```text
fonction architecturale principale : Parametre d'etat
architecture : Cosmologique
famille superieure : aucune famille simple ne doit etre forcee
```

### 3. Pourquoi H_0 n'est pas une constante fondamentale

H_0 est souvent appele "constante de Hubble", mais cette expression est historiquement trompeuse si elle est lue trop fortement.

Le taux d'expansion cosmique :

```text
H(t)
```

depend du temps cosmique dans les modeles de Friedmann-Lemaitre.

H_0 est seulement :

```text
la valeur actuelle de H(t)
```

Il ne s'agit donc pas d'une constante fondamentale au sens de :

```text
alpha
G_F
k_B
N_A
```

La formulation taxonomique correcte est :

```text
H_0 = parametre d'etat actuel
```

et non :

```text
H_0 = famille Echelle
```

ni :

```text
H_0 = constante fondamentale cosmologique
```

### 4. Regime de definition physique

Le regime de definition physique de H_0 est celui de la cosmologie homogene et isotrope, ou l'expansion est decrite par un facteur d'echelle :

```text
a(t)
```

Dans ce cadre :

```text
H(t) = a_dot / a
```

mesure le taux instantane d'expansion.

H_0 correspond a l'evaluation de ce taux aujourd'hui :

```text
t = t_0
```

Le regime physique est donc :

```text
dynamique globale actuelle de l'expansion cosmique
```

et non :

```text
interaction locale
couplage de particules
constante definissante metrologique
```

### 5. Regimes d'acces epistemique

H_0 est particulierement important pour la methode parce qu'il possede plusieurs regimes d'acces distincts.

#### 5.1 Route locale

La route locale cherche a mesurer H_0 a partir de distances et de redshifts dans l'univers proche.

Exemple :

```text
echelle de distance Cepheides -> supernovae Ia -> diagramme distance-redshift
```

La collaboration SH0ES donne, dans son analyse HST 2022 :

```text
H_0 = 73.04 +/- 1.04 km s^-1 Mpc^-1
```

Des analyses plus recentes avec JWST continuent de tester les calibrations de Cepheides, TRGB et autres indicateurs.

Une synthese locale plus recente, le H_0 Distance Network, combine plusieurs indicateurs dans un reseau de distances et rapporte :

```text
H_0 = 73.50 +/- 0.81 km s^-1 Mpc^-1
```

Ce resultat renforce la route locale haute, mais il ne supprime pas le besoin de distinguer mesure locale, calibration et inference cosmologique.

#### 5.2 Route CMB + LambdaCDM

La route CMB n'est pas une mesure directe locale de H_0.

Elle infere H_0 dans un modele cosmologique, typiquement :

```text
base LambdaCDM
```

Planck 2018 donne :

```text
H_0 = 67.4 +/- 0.5 km s^-1 Mpc^-1
```

dans le modele LambdaCDM plat a six parametres.

#### 5.3 Route BAO et sondes combinees

Les BAO mesurent des distances relatives et l'histoire d'expansion. Pour contraindre H_0, elles doivent etre calibrees par une information externe, par exemple :

```text
CMB
BBN
sondes combinees
```

DESI DR2 fournit des mesures BAO tres precises sur les trois premieres annees de donnees. Ces resultats jouent un role majeur dans les contraintes recentes, mais leur relation a H_0 depend du modele cosmologique et des calibrations utilisees.

#### 5.4 Routes alternatives locales

Les calibrations locales ne sont pas reduites a SH0ES.

Le Chicago-Carnegie Hubble Program, utilisant JWST et plusieurs indicateurs de distance, rapporte notamment une estimation combinee autour de :

```text
H_0 = 70.39 +/- 1.22(stat) +/- 1.33(sys) +/- 0.70(sigma_SN) km s^-1 Mpc^-1
```

dans son rapport CCHP 2024 revise en 2025.

Ce resultat illustre que la route locale n'est pas un bloc unique. Elle depend des indicateurs de distance, des calibrateurs, des supernovae retenues et des modeles systematiques.

Dans les donnees JWST seules du meme programme, les routes TRGB et JAGB donnent des valeurs plus basses que SH0ES. Cette pluralite confirme que la tension H_0 doit etre lue comme une propriete du reseau d'acces, pas comme une propriete d'une seule experience.

### 6. La tension H_0

La tension H_0 designe l'ecart entre deux grandes routes d'acces :

```text
mesures locales tardives, souvent autour de 68-74 km s^-1 Mpc^-1 selon les methodes
inferences CMB + LambdaCDM, autour de 67 km s^-1 Mpc^-1
```

La tension n'est pas une grandeur physique nouvelle.

Elle est une propriete du reseau d'acces :

```text
Tension H_0 = discordance entre regimes d'inference
```

Elle peut indiquer :

```text
systematiques non comprises
differences de calibration
limite du modele LambdaCDM
besoin d'une extension phenomenologique
nouvelle physique
```

Mais elle ne doit pas etre classee comme :

```text
famille
fonction transversale autonome
constante nouvelle
```

Regle :

```text
La tension H_0 appartient au regime d'acces, non a la famille principale de H_0.
```

### 7. H_0, Lambda et Omega_i

H_0 est fortement lie a Lambda et aux densites normalisees, mais il ne se confond pas avec eux.

Dans une cosmologie de Friedmann-Lemaitre, H_0 intervient dans la densite critique :

```text
rho_crit,0 = 3 H_0^2 / (8 pi G)
```

Les densites normalisees s'ecrivent :

```text
Omega_i = rho_i / rho_crit
```

Donc :

```text
H_0       : parametre d'etat actuel
Omega_i   : densite normalisee
Lambda    : terme de fond
w         : relation d'etat
```

Ces grandeurs appartiennent a la meme architecture cosmologique, mais elles n'ont pas la meme fonction.

### 8. H_0 comme parametre d'etat actuel

La classification principale proposee est :

```text
fonction architecturale : Parametre d'etat
```

H_0 decrit l'etat actuel de l'expansion.

Il est "actuel" en deux sens.

Premier sens :

```text
il est evalue a t_0
```

Deuxieme sens :

```text
il sert a normaliser plusieurs parametres cosmologiques actuels
```

Mais cette centralite ne le rend pas fondamental au sens fort.

Formulation :

> H_0 n'est pas une constante primitive de la nature ; c'est une coordonnee actuelle de l'etat cosmologique, dont la valeur depend de routes d'acces distinctes et de cadres d'inference.

### 9. Stabilisation empirique

La stabilisation empirique de H_0 est forte, mais non convergente.

Elle est forte parce que chaque route majeure donne une valeur precise dans son propre cadre.

Elle n'est pas convergente parce que les routes ne donnent pas toutes la meme valeur.

Exemples de regimes d'acces :

| Route | Exemple de valeur | Statut |
|---|---|---|
| Planck 2018 + base LambdaCDM | 67.4 +/- 0.5 | Inference modele-dependante, tres precise |
| SH0ES 2022 | 73.04 +/- 1.04 | Mesure locale par echelle de distance Cepheides / SNe Ia |
| H0DN 2026 | 73.50 +/- 0.81 | Reseau local multi-indicateurs, covariance explicite |
| CCHP / HST+JWST 2024-2025 | 70.39 +/- 1.22(stat) +/- 1.33(sys) +/- 0.70(sigma_SN) | Route locale alternative TRGB/JAGB/Cepheides |
| DESI DR2 BAO 2025 | Contraintes geometriques fortes, dependantes de calibration | Route BAO et combinaisons de sondes |

La formulation correcte est :

```text
H_0 est fortement contraint, mais son acces est plural et actuellement conflictuel.
```

### 10. Stabilisation conventionnelle

H_0 n'est pas une constante definissante du SI.

Sa valeur n'est pas fixee par convention metrologique.

Stabilisation conventionnelle :

```text
non concernee
```

Le parametre reduit :

```text
h
```

est une normalisation commode, non une definition conventionnelle d'unite.

### 11. Lecture par la matrice cosmologique

| Critere | Lecture pour H_0 |
|---|---|
| Grandeur | H_0 |
| Type logique | Parametre d'etat actuel ; valeur actuelle du taux d'expansion |
| Dimension | Temps^-1, souvent km s^-1 Mpc^-1 |
| Famille principale | Aucune famille superieure simple ne doit etre forcee |
| Fonction architecturale principale | Parametre d'etat |
| Sous-type local | Taux d'expansion actuel |
| Fonction transversale | Tension d'acces, normalisation, relation a rho_crit |
| Regime de definition physique | Dynamique actuelle de l'expansion cosmologique |
| Regime d'acces epistemique | Distance ladder, CMB + modele, BAO + calibration, sondes combinees |
| Dependances de modele | Forte pour CMB + LambdaCDM ; variable selon route locale et calibration |
| Stabilisation empirique | Forte localement par route, mais discordante entre routes |
| Stabilisation conventionnelle | Non concernee |
| Architecture | Cosmologique |
| Limite | Ne dit pas seul la nature de l'energie noire ni la cause de la tension |

### 12. Ce que H_0 confirme

H_0 confirme que l'architecture cosmologique a besoin d'une categorie :

```text
Parametre d'etat
```

Cette categorie est distincte de :

```text
Fond
Densite normalisee
Relation d'etat
Condition initiale
Observable reconstruite
```

H_0 confirme aussi que le regime d'acces doit devenir central dans les fiches cosmologiques.

Dans les cycles precedents, le regime d'acces etait deja important. Ici, il devient decisif : le statut de H_0 ne peut pas etre compris sans distinguer mesure locale, inference CMB et calibrations BAO.

### 13. Ce que H_0 ne confirme pas

H_0 ne confirme pas :

```text
Cosmologie comme famille
```

Il ne confirme pas :

```text
Tension comme famille
```

Il ne confirme pas non plus :

```text
H_0 comme constante fondamentale
```

La tension H_0 ne prouve pas par elle-meme une nouvelle physique. Elle indique une discordance importante entre routes d'acces, qui peut avoir plusieurs interpretations.

### 14. Decision locale

Decision de classement :

```text
H_0 = parametre d'etat actuel dans l'architecture cosmologique.
```

Statut :

```text
fonction architecturale : Parametre d'etat
architecture : Cosmologique
stabilisation empirique : forte mais discordante entre regimes d'acces
stabilisation conventionnelle : non concernee
tension H_0 : propriete du regime d'acces, non famille
```

Formulation finale :

> H_0 est le taux actuel d'expansion cosmique ; il est fortement contraint par plusieurs routes d'acces, mais sa valeur est aujourd'hui le lieu d'une tension entre mesures locales et inferences dependantes du modele cosmologique.

### 15. Effet sur le cycle cosmologique

Apres Lambda et H_0, l'architecture cosmologique possede deux piliers distincts.

```text
Lambda : terme de fond
H_0    : parametre d'etat actuel
```

Ces deux grandeurs ne doivent pas etre fusionnees.

Lambda pose la question :

```text
quel terme de fond structure l'acceleration cosmique ?
```

H_0 pose la question :

```text
quel est l'etat actuel de l'expansion et comment y accede-t-on ?
```

Le cycle peut maintenant passer aux densites normalisees.

### 16. Prochaine fiche

La prochaine fiche logique est :

```text
Cycle_cosmologique_v0_4_Omega_i.md
```

Question directrice :

> Comment les parametres Omega_i stabilisent-ils des densites normalisees sans devenir des constantes primitives ?

Objectif :

```text
classer Omega_m, Omega_Lambda, Omega_b et Omega_c comme relations normalisees dans l'architecture cosmologique.
```

### 17. Effet sur la mise a jour methodologique

La fiche H_0 confirme que la methode generale doit etre mise a jour.

Deux corrections deviennent prioritaires :

```text
1. introduire explicitement les fonctions architecturales cosmologiques ;
2. donner un statut methodologique aux tensions de donnees comme proprietes du regime d'acces.
```

La note preparatoire :

```text
01_CADRE_METHODOLOGIQUE/Mise_a_jour_methodologie_v1_1_notes.md
```

peut maintenant servir de base a une vraie :

```text
Note_synthese_methodologique_v1_1.md
```

### 18. Sources de controle

Sources utilisees pour cette fiche :

- Planck Collaboration, `Planck 2018 results. VI. Cosmological parameters`, arXiv:1807.06209, https://arxiv.org/abs/1807.06209
- Riess et al., `A Comprehensive Measurement of the Local Value of the Hubble Constant with 1 km/s/Mpc Uncertainty from the Hubble Space Telescope and the SH0ES Team`, arXiv:2112.04510, https://arxiv.org/abs/2112.04510
- Freedman et al., `Status Report on the Chicago-Carnegie Hubble Program (CCHP): Measurement of the Hubble Constant Using the Hubble and James Webb Space Telescopes`, arXiv:2408.06153, https://arxiv.org/abs/2408.06153
- H0DN Collaboration, `The Local Distance Network: a community consensus report on the measurement of the Hubble constant at 1% precision`, A&A 708, A166 (2026), arXiv:2510.23823, https://arxiv.org/abs/2510.23823
- DESI Collaboration, `DESI DR2 Results II: Measurements of Baryon Acoustic Oscillations and Cosmological Constraints`, arXiv:2503.14738, https://arxiv.org/abs/2503.14738
- DESI, `DESI DR2 Results: March 19 Guide`, 19 March 2025, https://www.desi.lbl.gov/2025/03/19/desi-dr2-results-march-19-guide/

### 19. Documents internes a relier

Documents internes :

```text
02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Cycle_cosmologique_v0_1_cadrage.md
02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Cycle_cosmologique_v0_2_Lambda.md
05_CARTES_ET_SYNTHESES/Carte_consolidee_v0_9.md
01_CADRE_METHODOLOGIQUE/Mise_a_jour_methodologie_v1_1_notes.md
PROJECT_BRIEF.docx
```
