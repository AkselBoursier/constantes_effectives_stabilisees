# Cycle cosmologique v0.6

## Fiche 5 : A_s et n_s

### 1. Fonction de la fiche

Cette fiche porte sur :

```text
A_s
n_s
```

les deux parametres usuels du spectre primordial des perturbations scalaires.

La question directrice est :

> Comment A_s et n_s stabilisent-ils des conditions initiales perturbatives sans devenir des constantes de fond ?

Objectif :

```text
classer A_s et n_s comme conditions initiales perturbatives dans l'architecture cosmologique.
```

La fiche doit eviter quatre erreurs.

Premiere erreur :

```text
A_s et n_s = constantes fondamentales
```

Deuxieme erreur :

```text
A_s et n_s = Fond cosmologique
```

Troisieme erreur :

```text
A_s = sigma_8
```

Quatrieme erreur :

```text
n_s = explication physique de l'inflation
```

La bonne formulation est :

```text
A_s et n_s parametrent la forme initiale du spectre primordial scalaire ; ils sont fortement contraints par le CMB, mais restent des parametres de conditions initiales dans un modele cosmologique.
```

### 2. Identification

Grandeurs :

```text
A_s
n_s
```

Noms :

```text
A_s : amplitude scalaire primordiale
n_s : indice spectral scalaire
```

Definition usuelle du spectre de courbure primordial :

```text
P_R(k) = A_s (k / k_*)^(n_s - 1)
```

Pivot usuel :

```text
k_* = 0.05 Mpc^-1
```

Type logique :

```text
parametres du spectre primordial
conditions initiales perturbatives
```

Dimension :

```text
sans dimension
```

Statut de rang :

```text
fonction architecturale principale : Condition initiale
architecture : Cosmologique
famille superieure : aucune famille simple ne doit etre forcee pour le couple A_s / n_s
```

Lectures locales :

```text
A_s : amplitude normalisee du spectre primordial
n_s : pente ou forme spectrale du spectre primordial
```

### 3. Pourquoi A_s et n_s ne sont pas des constantes de fond

Les fiches precedentes ont distingue :

```text
Lambda  : terme de fond
H_0     : parametre d'etat actuel
Omega_i : densite normalisee
w       : relation d'etat
```

A_s et n_s ne jouent aucun de ces roles.

Ils ne decrivent pas directement :

```text
l'acceleration tardive
la densite critique actuelle
la fraction de matiere ou d'energie noire
la relation pression / densite d'une composante tardive
```

Ils parametrent plutot :

```text
les perturbations scalaires initiales
```

qui servent ensuite de graines a la formation des anisotropies du CMB et des grandes structures.

La formulation correcte est :

```text
A_s / n_s = conditions initiales perturbatives
```

et non :

```text
A_s / n_s = Fond
```

### 4. Regime de definition physique

Le regime de definition physique est celui des perturbations cosmologiques primordiales.

Dans le modele de base, les fluctuations scalaires initiales sont decrites par un spectre de puissance presque invariant d'echelle :

```text
P_R(k) = A_s (k / k_*)^(n_s - 1)
```

Role de A_s :

```text
fixer l'amplitude globale des perturbations scalaires au pivot k_*
```

Role de n_s :

```text
fixer l'inclinaison spectrale du spectre scalaire
```

Cas particulier :

```text
n_s = 1
```

correspond a une invariance d'echelle exacte.

Les donnees Planck favorisent :

```text
n_s < 1
```

ce qui signifie un spectre legerement rouge.

Mais cette inclinaison n'est pas, a elle seule, une theorie physique de l'origine des perturbations.

### 5. Regime d'acces epistemique

A_s et n_s ne sont pas mesures directement comme des constantes locales.

Ils sont inferes principalement a partir de :

```text
anisotropies de temperature du CMB
polarisation du CMB
lensing CMB
grandes structures
ajustements cosmologiques combines
```

Le regime d'acces est donc :

```text
inference cosmologique a partir de la forme du spectre des anisotropies et de la croissance ulterieure.
```

Point important :

```text
le CMB primaire contraint fortement A_s e^(-2 tau)
```

ou :

```text
tau
```

est la profondeur optique de reionisation.

Donc A_s est lie a un regime d'acces particulier :

```text
amplitude primordiale + reionisation + lensing + croissance
```

n_s est surtout contraint par :

```text
la dependance en echelle de la puissance primordiale
```

et par sa propagation dans les anisotropies du CMB.

### 6. Stabilisation empirique

Planck 2018 donne, dans le modele de base LambdaCDM :

```text
ln(10^10 A_s) = 3.044 +/- 0.014
n_s = 0.9649 +/- 0.0042
```

Ces valeurs correspondent a :

```text
A_s autour de 2.1 x 10^-9
```

Le point methodologique important est double.

Premier point :

```text
A_s et n_s sont fortement contraints dans LambdaCDM.
```

Deuxieme point :

```text
leur interpretation depend du modele primordial retenu.
```

Si l'on autorise :

```text
running de n_s
tenseurs primordiaux
isocourbure
non-gaussianites
reconstructions non parametriques du spectre
```

alors leur statut change de precision et d'interpretation.

Formulation prudente :

```text
A_s et n_s sont fortement stabilises comme parametres du spectre scalaire primordial dans LambdaCDM, mais ils ne suffisent pas a identifier une theorie unique de l'origine des perturbations.
```

### 7. n_s et l'inflation

n_s est souvent discute dans le cadre de l'inflation.

La raison est simple :

```text
un spectre presque invariant d'echelle, mais legerement incline, est une prediction generique de nombreuses classes inflationnaires.
```

Cependant, la classification methodologique doit rester prudente.

n_s ne doit pas etre transforme en :

```text
preuve unique d'un modele inflationnaire particulier
```

Il faut distinguer :

```text
parametre spectral mesure
classe de modeles compatibles
modele microphysique de l'inflation
```

Planck 2018 contraint fortement de nombreux modeles inflationnaires, mais n'identifie pas une origine physique unique.

Regle :

```text
n_s teste la forme du spectre primordial ; il ne donne pas seul la physique complete de l'inflation.
```

### 8. A_s et sigma_8 ne sont pas identiques

La prochaine fiche portera sur :

```text
sigma_8
S_8
```

Il faut preparer la distinction.

A_s est :

```text
une amplitude primordiale
```

sigma_8 est :

```text
une amplitude tardive de la fluctuation de matiere sur une echelle de 8 h^-1 Mpc
```

Ces deux grandeurs sont reliees par l'evolution cosmologique, mais elles ne sont pas identiques.

Schema :

```text
A_s
-> croissance lineaire
-> transfert de puissance
-> sigma_8
-> S_8
```

Donc :

```text
A_s : condition initiale perturbative
sigma_8 / S_8 : observables ou amplitudes reconstruites de structure
```

Cette distinction sera centrale pour traiter les tensions de croissance des structures.

### 9. A_s, n_s et les autres parametres cosmologiques

A_s et n_s ne sont pas isoles.

Ils interagissent avec :

```text
Omega_m
Omega_b
Omega_c
H_0
tau
masse des neutrinos
w
sigma_8
```

Mais ils ne doivent pas etre confondus avec ces grandeurs.

Exemples :

```text
A_s influence l'amplitude initiale de la puissance.
tau modifie l'acces CMB a cette amplitude.
Omega_m et H_0 influencent la croissance et les distances.
w influence l'expansion tardive.
sigma_8 condense l'amplitude tardive de structure.
```

La classification principale reste donc :

```text
Condition initiale perturbative
```

### 10. Stabilisation conventionnelle

A_s et n_s ne sont pas des constantes definissantes du SI.

Leurs valeurs ne sont pas fixees par convention metrologique.

Stabilisation conventionnelle :

```text
non concernee
```

Le fait qu'ils soient sans dimension ne les rend pas conventionnellement exacts.

### 11. Lecture par la matrice cosmologique

| Critere | Lecture pour A_s / n_s |
|---|---|
| Grandeur | A_s et n_s |
| Type logique | Parametres du spectre primordial scalaire |
| Dimension | Sans dimension |
| Famille principale | Aucune famille superieure simple ne doit etre forcee pour le couple |
| Sous-type local | Amplitude primordiale ; inclinaison spectrale |
| Fonction architecturale principale | Condition initiale |
| Fonction transversale | Validite de modele, dependance au pivot, dependance a tau, lien avec croissance |
| Regime de definition physique | Perturbations scalaires primordiales |
| Regime d'acces epistemique | CMB temperature, polarisation, lensing, grandes structures, ajustements combines |
| Dependances de modele | LambdaCDM, inflation, running, tenseurs, isocourbure, neutrinos, reionisation |
| Stabilisation empirique | Forte dans LambdaCDM, mais interpretation primitive ouverte |
| Stabilisation conventionnelle | Non concernee |
| Architecture | Cosmologique |
| Limite | Ne donne pas seul l'origine physique des perturbations ni l'amplitude tardive des structures |

### 12. Ce que A_s et n_s confirment

A_s et n_s confirment que l'architecture cosmologique a besoin de la fonction :

```text
Condition initiale
```

Cette fonction est distincte de :

```text
Fond
Parametre d'etat
Densite normalisee
Relation d'etat
Observable reconstruite
```

Ils confirment aussi qu'une grandeur peut etre tres fortement stabilisee empiriquement sans etre une constante fondamentale.

Leur stabilite dans les ajustements cosmologiques ne doit pas etre confondue avec :

```text
invariance absolue
definition metrologique
explication microphysique complete
```

### 13. Ce que A_s et n_s ne confirment pas

A_s et n_s ne confirment pas :

```text
Cosmologie comme famille
```

Ils ne confirment pas :

```text
Fond comme famille
```

Ils ne confirment pas non plus :

```text
un modele inflationnaire unique
```

Ils ne doivent pas etre confondus avec :

```text
sigma_8
S_8
tensions de croissance des structures
```

Ils preparent plutot le passage vers ces observables reconstruites.

### 14. Decision locale

Decision de classement :

```text
A_s et n_s = conditions initiales perturbatives dans l'architecture cosmologique.
```

Statut :

```text
fonction architecturale : Condition initiale
architecture : Cosmologique
famille superieure : aucune famille simple ne doit etre forcee pour le couple
stabilisation empirique : forte dans LambdaCDM, interpretation primitive ouverte
stabilisation conventionnelle : non concernee
```

Formulation finale :

> A_s et n_s ne sont pas des constantes de fond ; ils parametrent l'amplitude et la forme du spectre primordial scalaire, c'est-a-dire des conditions initiales perturbatives dont l'acces passe principalement par le CMB et les grandes structures.

### 15. Effet sur le cycle cosmologique

Apres Lambda, H_0, Omega_i, w et A_s / n_s, le cycle distingue cinq niveaux.

```text
Lambda    : terme de fond
H_0       : parametre d'etat actuel
Omega_i   : densite normalisee / relation normalisee
w         : relation d'etat
A_s, n_s  : conditions initiales perturbatives
```

Ces niveaux sont solidaires, mais non confondus.

Relations principales :

```text
A_s fixe l'amplitude initiale des perturbations scalaires.
n_s fixe leur inclinaison spectrale.
Omega_i et H_0 structurent l'evolution et les distances.
w modifie l'expansion tardive.
sigma_8 / S_8 condenseront l'amplitude tardive reconstruite.
```

Le cycle peut maintenant passer aux amplitudes de structure.

### 16. Prochaine fiche

La prochaine fiche logique est :

```text
Cycle_cosmologique_v0_7_sigma8_S8.md
```

Question directrice :

> Comment sigma_8 et S_8 condensent-ils des amplitudes reconstruites de structure sans devenir des constantes primitives ?

Objectif :

```text
classer sigma_8 et S_8 comme observables ou amplitudes reconstruites dans l'architecture cosmologique.
```

### 17. Effet sur la carte et la methode

La fiche A_s / n_s renforce trois regles methodologiques.

Premiere regle :

```text
condition initiale n'est pas Fond.
```

Deuxieme regle :

```text
parametre primordial n'est pas observable tardive.
```

Troisieme regle :

```text
contrainte inflationnaire n'est pas explication microphysique unique.
```

Elle ajoute aussi une transition importante :

```text
la fiche suivante devra distinguer amplitude initiale et amplitude tardive reconstruite.
```

### 18. Sources de controle

Sources utilisees pour cette fiche :

- Planck Collaboration, `Planck 2018 results. VI. Cosmological parameters`, arXiv:1807.06209, https://arxiv.org/abs/1807.06209
- Planck Collaboration, `Planck 2018 results. X. Constraints on inflation`, arXiv:1807.06211, https://arxiv.org/abs/1807.06211
- DESI Collaboration, `DESI DR2 Results II: Measurements of Baryon Acoustic Oscillations and Cosmological Constraints`, arXiv:2503.14738, https://arxiv.org/abs/2503.14738

### 19. Documents internes a relier

Documents internes :

```text
01_CADRE_METHODOLOGIQUE/Note_synthese_methodologique_v1_1.md
02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Cycle_cosmologique_v0_1_cadrage.md
02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Cycle_cosmologique_v0_2_Lambda.md
02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Cycle_cosmologique_v0_3_H0.md
02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Cycle_cosmologique_v0_4_Omega_i.md
02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Cycle_cosmologique_v0_5_w.md
05_CARTES_ET_SYNTHESES/Carte_consolidee_v0_9.md
PROJECT_BRIEF.docx
```
