# Cycle cosmologique v0.4

## Fiche 3 : Omega_i

### 1. Fonction de la fiche

Cette fiche porte sur :

```text
Omega_i
```

et plus particulierement sur :

```text
Omega_m
Omega_Lambda
Omega_b
Omega_c
```

La question directrice est :

> Comment les parametres Omega_i stabilisent-ils des densites normalisees sans devenir des constantes primitives ?

Objectif :

```text
classer Omega_m, Omega_Lambda, Omega_b et Omega_c comme relations normalisees dans l'architecture cosmologique.
```

La fiche doit eviter quatre erreurs.

Premiere erreur :

```text
Omega_i = constante fondamentale
```

Deuxieme erreur :

```text
Omega_Lambda = Lambda
```

Troisieme erreur :

```text
Omega_m = mesure directe de toute la matiere
```

Quatrieme erreur :

```text
Omega_i = propriete independante du modele cosmologique
```

La bonne formulation est :

```text
Omega_i est une fraction normalisee par la densite critique, definie dans un modele cosmologique et inferee par des regimes d'acces precis.
```

### 2. Identification

Grandeur :

```text
Omega_i
```

Nom :

```text
parametre de densite normalisee
```

Definition generale :

```text
Omega_i(t) = rho_i(t) / rho_crit(t)
```

Densite critique :

```text
rho_crit(t) = 3 H(t)^2 / (8 pi G)
```

Au temps actuel :

```text
Omega_i,0 = rho_i,0 / rho_crit,0
rho_crit,0 = 3 H_0^2 / (8 pi G)
```

Type logique :

```text
relation normalisee
```

Dimension :

```text
sans dimension
```

Statut de rang :

```text
famille principale : Relation
sous-type : relation normalisee
fonction architecturale : Densite normalisee
architecture : Cosmologique
```

### 3. Pourquoi Omega_i n'est pas une constante primitive

Omega_i n'est pas une constante primitive parce qu'il s'agit d'un rapport.

Il depend de deux termes :

```text
rho_i
rho_crit
```

Or :

```text
rho_crit depend de H(t)
```

et donc, au temps actuel :

```text
rho_crit,0 depend de H_0
```

Omega_i n'est donc pas une densite absolue. C'est une densite rapportee a une densite critique.

La formulation correcte est :

```text
Omega_i = relation normalisee entre une composante cosmologique et rho_crit
```

et non :

```text
Omega_i = constante fondamentale de composition de l'univers
```

### 4. Regime de definition physique

Le regime de definition physique est celui des modeles cosmologiques de Friedmann-Lemaitre.

Dans ce cadre, l'equation de Friedmann permet d'ecrire la dynamique d'expansion comme une somme de contributions normalisees.

Une forme schematique est :

```text
H(t)^2 / H_0^2 =
Omega_m,0 a^-3
+ Omega_r,0 a^-4
+ Omega_k,0 a^-2
+ Omega_Lambda,0
```

dans un modele simple avec matiere, rayonnement, courbure et Lambda.

Cette ecriture montre que les Omega_i ne sont pas seulement des nombres de catalogue. Ils servent a decomposer la dynamique cosmologique.

Le regime physique est donc :

```text
decomposition normalisee du contenu cosmologique dans une dynamique d'expansion
```

et non :

```text
couplage local
echelle de masse
constante definissante d'unites
```

### 5. Regime d'acces epistemique

Les Omega_i ne sont pas mesures comme des objets isoles.

Ils sont inferes dans des modeles a partir de plusieurs sondes :

```text
CMB
BAO
supernovae
lentille gravitationnelle
amas
abondances primordiales
croissance des structures
ajustements combines
```

Leur regime d'acces depend de la composante consideree.

Exemples :

| Parametre | Acces typique | Dependances |
|---|---|---|
| Omega_b h^2 | CMB, BBN, abondances primordiales | physique baryonique, nucleosynthese, CMB |
| Omega_c h^2 | CMB, grandes structures, lentille | modele de matiere noire froide |
| Omega_m | CMB, BAO, SNe, lentille, croissance | composition de la matiere et modele d'expansion |
| Omega_Lambda | CMB + geometrie + expansion tardive | hypothese LambdaCDM ou extensions |

Regle :

```text
Omega_i appartient au regime d'inference cosmologique, non a une mesure directe simple.
```

### 6. Omega_i, H_0 et rho_crit

La fiche H_0 a montre que H_0 est un parametre d'etat actuel.

Omega_i depend de H_0 par :

```text
rho_crit,0 = 3 H_0^2 / (8 pi G)
```

Cela signifie que :

```text
changer H_0 change la densite critique actuelle
```

et donc change la lecture normalisee des densites.

Ce point est methodologiquement important.

Omega_i n'est pas une grandeur independante de H_0. Elle est solidaire de l'architecture :

```text
H_0 -> rho_crit,0 -> Omega_i
```

Formulation :

> Omega_i est une coordonnee relationnelle de l'etat cosmologique : elle rapporte une composante a une densite critique elle-meme definie par le taux d'expansion.

### 7. Omega_Lambda n'est pas Lambda

La fiche Lambda a deja pose cette distinction.

```text
Lambda
```

est un terme dimensionne dans les equations gravitationnelles.

```text
Omega_Lambda
```

est une densite normalisee associee a ce terme.

Dans une convention usuelle :

```text
Omega_Lambda = rho_Lambda / rho_crit,0
```

et, pour une constante cosmologique stricte :

```text
Omega_Lambda = Lambda c^2 / (3 H_0^2)
```

La distinction taxonomique est :

```text
Lambda        : terme de fond
Omega_Lambda  : relation normalisee / densite normalisee
w             : relation d'etat
```

Il ne faut donc pas ecrire :

```text
Omega_Lambda est la constante cosmologique
```

Il faut ecrire :

```text
Omega_Lambda est la fraction normalisee associee a la composante Lambda dans un modele donne.
```

### 8. Omega_m, Omega_b et Omega_c

Les parametres de matiere doivent etre distingues.

```text
Omega_m
```

designe la densite totale de matiere normalisee.

Elle inclut typiquement :

```text
matiere baryonique
matiere noire froide
eventuelle contribution de neutrinos non relativistes, selon convention et modele
```

On ecrit souvent :

```text
Omega_m = Omega_b + Omega_c + Omega_nu
```

selon les conventions retenues.

```text
Omega_b
```

designe la fraction baryonique normalisee.

```text
Omega_c
```

designe la fraction de matiere noire froide normalisee.

Ces trois grandeurs sont relationnelles.

Elles ne disent pas directement :

```text
la nature microscopique de la matiere noire
l'origine de la baryogenese
la masse absolue des neutrinos
```

Elles disent :

```text
quelle fraction normalisee du budget cosmologique est attribuee a chaque composante dans un modele donne.
```

### 9. Omega_i et fermeture cosmologique

Dans une cosmologie de Friedmann-Lemaitre, les Omega_i servent aussi a formuler une condition de fermeture.

Schema :

```text
Omega_tot = somme_i Omega_i
```

Avec une composante de courbure :

```text
Omega_k = 1 - Omega_tot
```

Dans un modele spatialement plat :

```text
Omega_k = 0
```

et donc :

```text
somme_i Omega_i = 1
```

Cette relation est importante, mais elle ne transforme pas les Omega_i en constantes primitives.

Elle montre au contraire leur nature relationnelle :

```text
chaque Omega_i prend sens dans une decomposition globale contrainte.
```

### 10. Stabilisation empirique

Les Omega_i sont fortement stabilises dans certains modeles, mais leur statut reste modele-dependant.

Planck 2018 donne, dans le modele plat base LambdaCDM :

```text
Omega_c h^2 = 0.120 +/- 0.001
Omega_b h^2 = 0.0224 +/- 0.0001
Omega_m = 0.315 +/- 0.007
```

Dans ce meme cadre plat, cela correspond a un budget tardif approximatif :

```text
Omega_m      autour de 0.315
Omega_Lambda autour de 0.685
Omega_b      autour de 0.049
Omega_c      autour de 0.265
```

Ces nombres ne doivent pas etre lus comme des constantes fondamentales.

Ils sont :

```text
des parametres inferes dans un modele cosmologique ;
des fractions normalisees par rho_crit ;
des grandeurs dependantes de H_0, de la courbure, des hypotheses sur les neutrinos et du modele d'energie noire.
```

DESI DR2 confirme que les mesures BAO contraignent fortement l'histoire d'expansion. Les resultats DR2 restent bien decrits par un modele plat LambdaCDM, mais les combinaisons avec CMB et supernovae exercent une pression sur ce cadre et peuvent favoriser des modeles d'energie noire dynamique.

La formulation prudente est :

```text
Omega_i est fortement contraint dans LambdaCDM, mais sa valeur et son interpretation dependent du modele et des jeux de donnees.
```

### 11. Stabilisation conventionnelle

Omega_i n'est pas une constante definissante du SI.

Sa valeur n'est pas fixee par convention metrologique.

Stabilisation conventionnelle :

```text
non concernee
```

Le fait que Omega_i soit sans dimension ne le rend pas conventionnellement exact.

Il faut distinguer :

```text
sans dimension
exact par convention
```

Omega_i est sans dimension, mais il reste inferentiel et modele-dependant.

### 12. Lecture par la matrice cosmologique

| Critere | Lecture pour Omega_i |
|---|---|
| Grandeur | Omega_i ; surtout Omega_m, Omega_Lambda, Omega_b, Omega_c |
| Type logique | Densite normalisee ; rapport rho_i / rho_crit |
| Dimension | Sans dimension |
| Famille principale | Relation |
| Sous-type local | Relation normalisee |
| Fonction architecturale principale | Densite normalisee |
| Fonction transversale | Normalisation, fermeture, dependance de modele |
| Regime de definition physique | Dynamique de Friedmann-Lemaitre et decomposition du contenu cosmologique |
| Regime d'acces epistemique | CMB, BAO, SNe, BBN, lentille, croissance, ajustements combines |
| Dependances de modele | Forte : LambdaCDM, courbure, neutrinos, wCDM, w0waCDM, systematiques |
| Stabilisation empirique | Forte dans LambdaCDM, mais modele-dependante |
| Stabilisation conventionnelle | Non concernee |
| Architecture | Cosmologique |
| Limite | Ne donne pas seul la nature microscopique des composantes ni l'origine de l'energie noire |

### 13. Ce que Omega_i confirme

Omega_i confirme que Relation doit rester une famille.

Mais il confirme aussi que Relation doit rester qualifiee.

La bonne classification n'est pas :

```text
Omega_i = Relation
```

Elle est :

```text
Omega_i = Relation normalisee
```

avec fonction architecturale :

```text
Densite normalisee
```

Ce cas confirme donc la structure v1.1 :

```text
famille principale + sous-type + fonction architecturale
```

### 14. Ce que Omega_i ne confirme pas

Omega_i ne confirme pas :

```text
Cosmologie comme famille
```

Il ne confirme pas :

```text
Fond comme famille
```

Il ne confirme pas :

```text
Omega_Lambda comme identique a Lambda
```

Il ne confirme pas non plus :

```text
les fractions cosmologiques comme constantes primitives de la nature
```

Les Omega_i sont des grandeurs puissantes parce qu'elles condensent le budget cosmologique dans un modele. Cette puissance ne doit pas etre confondue avec un statut fondamental simple.

### 15. Decision locale

Decision de classement :

```text
Omega_i = relation normalisee dans l'architecture cosmologique.
```

Statut :

```text
famille principale : Relation
sous-type : relation normalisee
fonction architecturale : Densite normalisee
architecture : Cosmologique
stabilisation empirique : forte dans LambdaCDM, mais modele-dependante
stabilisation conventionnelle : non concernee
```

Formulation finale :

> Omega_i ne designe pas une constante primitive ; il designe la fraction normalisee d'une composante cosmologique par rapport a la densite critique, donc une relation de composition dans une architecture d'expansion.

### 16. Effet sur le cycle cosmologique

Apres Lambda, H_0 et Omega_i, le cycle possede trois niveaux distincts.

```text
Lambda : terme de fond
H_0    : parametre d'etat actuel
Omega_i : densite normalisee / relation normalisee
```

Ces trois niveaux sont solidaires, mais non confondus.

Relations principales :

```text
H_0 definit rho_crit,0
rho_crit,0 normalise Omega_i
Lambda peut etre exprime par Omega_Lambda
Omega_i contribue a l'equation d'expansion
```

Le cycle peut maintenant passer a :

```text
w
```

car w testera un autre niveau :

```text
relation d'etat
```

### 17. Prochaine fiche

La prochaine fiche logique est :

```text
Cycle_cosmologique_v0_5_w.md
```

Question directrice :

> Comment w peut-il etre une relation d'etat et une parametrisation phenomenologique sans devenir une explication physique de l'energie noire ?

Objectif :

```text
classer w comme relation d'etat dans l'architecture cosmologique, en distinguant w = -1, w constant et w(a) dynamique.
```

### 18. Effet sur la carte et la methode

La fiche Omega_i renforce deux points de la note methodologique v1.1.

Premier point :

```text
Relation est conservee, mais elle doit etre sous-typee.
```

Deuxieme point :

```text
les fonctions architecturales cosmologiques sont necessaires pour ne pas forcer toute grandeur dans une famille simple.
```

Elle ajoute aussi une regle pratique :

```text
toute fiche cosmologique doit distinguer grandeur dimensionnee, densite associee et densite normalisee.
```

Exemple :

```text
Lambda        : terme dimensionne
rho_Lambda    : densite associee
Omega_Lambda  : densite normalisee
```

### 19. Sources de controle

Sources utilisees pour cette fiche :

- Planck Collaboration, `Planck 2018 results. VI. Cosmological parameters`, arXiv:1807.06209, https://arxiv.org/abs/1807.06209
- DESI Collaboration, `DESI DR2 Results II: Measurements of Baryon Acoustic Oscillations and Cosmological Constraints`, arXiv:2503.14738, https://arxiv.org/abs/2503.14738
- DESI, `DESI DR2 Publications`, https://data.desi.lbl.gov/doc/papers/dr2/
- DESI, `DESI DR2 Results: March 19 Guide`, 19 March 2025, https://www.desi.lbl.gov/2025/03/19/desi-dr2-results-march-19-guide/

### 20. Documents internes a relier

Documents internes :

```text
01_CADRE_METHODOLOGIQUE/Note_synthese_methodologique_v1_1.md
02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Cycle_cosmologique_v0_1_cadrage.md
02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Cycle_cosmologique_v0_2_Lambda.md
02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Cycle_cosmologique_v0_3_H0.md
05_CARTES_ET_SYNTHESES/Carte_consolidee_v0_9.md
PROJECT_BRIEF.docx
```
