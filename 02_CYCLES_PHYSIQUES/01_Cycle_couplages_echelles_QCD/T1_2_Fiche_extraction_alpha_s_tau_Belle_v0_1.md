# T1.2 — Fiche d’extraction de `alpha_s` par désintégrations hadroniques du tau v0.1

## 0. Statut

```text
statut : fiche primaire de chaîne d’extraction ;
date de contrôle : 21 juillet 2026 ;
source de référence : Phys. Rev. D 111, 074010 (2025) ;
texte de travail : arXiv:2502.08147v2 ;
fonction : rendre contrôlable la chaîne basse énergie de T1 ;
ne vaut pas : reproduction du fit, arbitrage général FOPT/CIPT, validation de toutes
               les données exclusives ou nouvelle détermination de alpha_s.
```

La version arXiv v2 corrige le signe de `C_10` sans changement annoncé du résultat
principal. Ce décalage de version est conservé explicitement.

## 1. Porteur et transformation

### Porteurs à distinguer

```text
observable : fonction spectrale vectorielle isovectorielle non étrange ;
paramètre extrait : alpha_s^(n_f=3) dans le schéma MS-bar à une échelle basse ;
relation de transport : évolution RG et raccordements vers alpha_s^(n_f=5)(m_Z) ;
objet du test T1 : cohérence de la chaîne spectre -> FESR -> fit -> transport.
```

### Transformations déclarées

```text
intégration en s jusqu’à une borne s_0 ;
variation de s_0 dans la fenêtre de fit ;
choix des fonctions poids des sommes de règles à énergie finie ;
traitement perturbatif ;
modélisation OPE et violations de dualité ;
transport de l’échelle du tau vers m_Z ;
franchissement des seuils de saveurs.
```

La variation avec l’échelle ou avec `s_0` n’est pas une variation temporelle de la
constante forte.

## 2. Données et observable

L’analyse reconstruit une fonction spectrale vectorielle inclusive non étrange à partir
de contributions exclusives.

### Canaux dominants

```text
pi- pi0 : ALEPH, OPAL et Belle ;
2 pi- pi+ pi0 : ALEPH et OPAL ;
pi- 3 pi0 : ALEPH et OPAL.
```

Les trois modes représentent environ 98 % du canal vectoriel non étrange par fraction
de branchement. L’introduction des données Belle à haute statistique concerne le mode
`pi- pi0`; Belle ne fournit pas dans cette analyse les deux modes `4 pi`.

### Modes résiduels

Les contributions résiduelles emploient notamment des données BaBar pour `K Kbar` et
des sections efficaces d’électroproduction converties par la relation de courant
vectoriel conservé (CVC) pour plusieurs modes sous-dominants. Les auteurs indiquent que
la fonction spectrale inclusive obtenue repose sur des données expérimentales pour au
moins 99,95 % de la fraction de branchement, sans entrée Monte-Carlo pour compléter le
spectre inclusif.

### Normalisation

Les spectres unitaires sont multipliés par des fractions de branchement issues des
moyennes du Heavy Flavor Averaging Group (HFLAV). La modification des moyennes HFLAV du
mode `pi- 3 pi0` est identifiée par les auteurs comme la cause principale du déplacement
du résultat par rapport à leur analyse antérieure.

La moyenne HFLAV 2022 employée pour ce mode est
`B_(pi- 3 pi0) = 0.01040(71)`. Par rapport à HFLAV 2019, sa valeur centrale baisse de
`9 %` et son incertitude est multipliée par `2,4`. Les contrôles publiés séparent
partiellement cet effet de l'ajout de Belle :

```text
fractions 2019, sans Belle : alpha_s(m_tau^2) = 0.3075(84) ;
fractions 2019, avec Belle : alpha_s(m_tau^2) = 0.3055(81) ;
fractions 2022, sans Belle : alpha_s(m_tau^2) = 0.3001(97) ;
fractions 2022, avec Belle : alpha_s(m_tau^2) = 0.2983(92), erreur statistique.
```

Les auteurs attribuent ainsi près de `80 %` du déplacement vers le bas, relativement à
leur analyse tau antérieure, à la mise à jour HFLAV et près de `20 %` à l'ajout de
Belle. **Cette attribution concerne le déplacement entre deux analyses tau
apparentées. Elle ne suffit pas à attribuer l'écart tau–lattice, tau–NNPDF ou
tau–formes d'événements à une cause unique.**

## 3. Chaîne expérimentale et covariance

```text
spectres exclusifs unitaires
-> combinaison par mode
-> multiplication par fractions de branchement
-> combinaison 2 pi + 4 pi
-> ajout des modes résiduels
-> fonction spectrale inclusive
-> moments FESR corrélés.
```

La fonction spectrale combinée est discrétisée en `63` groupes. Pour les dix fenêtres
finales, les auteurs calculent une moyenne diagonale des valeurs ajustées afin d'éviter
le biais associé aux très fortes corrélations, puis propagent l'erreur au moyen de la
matrice complète de covariance de ces dix valeurs.

Points contrôlés dans le texte :

- les matrices de covariance séparées des modes `4 pi` ALEPH et OPAL sont difficiles à
  employer directement ;
- pour le mode OPAL `pi- 3 pi0`, seules les entrées diagonales sont utilisées dans le fit
  de combinaison, tandis que la matrice complète intervient dans la propagation des
  erreurs ;
- les petites corrélations induites par les fractions de branchement sont conservées ;
- une annexe traite le biais de d’Agostini dans la combinaison de données corrélées ;
- les données CLEO `pi- pi0` sont étudiées comme contrôle mais ne sont pas retenues dans
  le résultat principal en raison d’informations systématiques bin-à-bin incomplètes.

Ces choix appartiennent à la chaîne d’accès. Ils ne constituent pas des propriétés de
`alpha_s` elle-même.

## 4. Théorie de l’extraction

L’extraction utilise des sommes de règles à énergie finie (FESR) appliquées aux moments
de la fonction spectrale.

```text
partie perturbative : fonction d’Adler dans le schéma MS-bar ;
traitement retenu : perturbation à ordre fixe (FOPT) ;
corrections non perturbatives : développement en produits d’opérateurs (OPE) ;
au-delà de l’OPE : modèle de violations de dualité (DV) ajusté aux données.
```

Les auteurs écartent dans cette analyse la perturbation améliorée sur le contour (CIPT),
en invoquant son incompatibilité avec l’OPE standard selon une série de travaux récents.
Pour T1, ce point est enregistré comme **choix théorique structurant de la chaîne**, non
comme arbitrage général clos par le présent corpus.

L'approche dite `truncated OPE` n'est pas retenue : les auteurs soutiennent que la mise à
zéro de contributions OPE de dimension supérieure produit des incohérences sur les
moments considérés à cette échelle.

Le résultat central repose sur le poids `w_0 = 1`. Les poids
`w_2 = 1-y^2`, `w_3 = (1-y)^2(1+2y)` et `w_4 = (1-y^2)^2`, avec
`y = s/s_0`, servent à des ajustements simultanés de stabilité. La borne supérieure est
`s_0^max = 3.0871 GeV^2`. Les dix bornes inférieures retenues vont de
`1.4747` à `1.9249 GeV^2`; les départs plus bas signalent la dégradation attendue de la
description, tandis que les départs plus hauts perdent en précision.

## 5. Paramètres et résultat

### Résultat transporté publié

```text
alpha_s^(5)(m_Z^2) = 0.1159 +/- 0.0014.
```

Ce nombre est le résultat final annoncé par l’article et la prépublication v2.

### Paramètre natif et budget publié

Le paramètre ajusté appartient au régime `n_f = 3`, dans le schéma `MS-bar`, à
l'échelle de la masse du tau :

```text
alpha_s^(3)(m_tau^2)
  = 0.2983
    +/- 0.0092_stat
    +/- 0.0026_fit
    +/- 0.0022_pert
    +/- 0.0025_c
  = 0.2983 +/- 0.0101.
```

Les composantes ont les fonctions suivantes :

- `stat` provient de l'ajustement central et de la propagation corrélée sur les dix
  fenêtres retenues ;
- `fit` est l'étendue des résultats obtenus en ajoutant chacun des poids `w_2`, `w_3`
  et `w_4` au poids central `w_0` ;
- `pert` provient d'une variation de `+/- 50 %` du coefficient inconnu `c_51`; elle est
  légèrement supérieure à la variation d'échelle publiée, `0.0021` ;
- `c` couvre une correction sous-dominante `c/s` de l'ansatz des violations de dualité ;
  l'excursion initiale asymétrique `-0.0010/+0.0039` est symétrisée à `0.0025` par les
  auteurs.

Cette décomposition est native de la publication. Elle ne fournit ni une matrice de
covariance complète entre `alpha_s`, les paramètres du développement en produits
d'opérateurs (OPE) et ceux de violation de dualité (DV), ni une preuve d'indépendance
des quatre composantes. La somme quadratique publiée ne doit donc pas être réinterprétée
comme une factorisation physique des sources.

## 6. Transport vers la référence commune

Le passage vers `alpha_s^(n_f=5)(m_Z)` requiert :

```text
équation du groupe de renormalisation ;
ordre déclaré de la fonction bêta ;
seuils de quarks lourds ;
ordre et échelles de matching ;
masses utilisées aux raccordements ;
propagation de l’incertitude du paramètre natif.
```

Le transport publié emploie l'évolution à cinq boucles et le matching à quatre boucles,
aux seuils `2 m_c(m_c)` et `2 m_b(m_b)`, avec les masses `MS-bar` prises dans le Particle
Data Group (PDG). Il mène
de `0.2983 +/- 0.0101` à `0.1159 +/- 0.0014`. Les auteurs qualifient l'incertitude
additionnelle du running de très petite ; déplacer les raccordements vers `m_c(m_c)` et
`m_b(m_b)` modifie la valeur finale de `0.00008`, variation non ajoutée au budget final.
Il est donc interdit de traiter `0.1159(14)` comme si toute son incertitude provenait
directement de la fonction spectrale, ou comme si le transport était exactement sans
incertitude.

## 7. Typage des chemins

```text
chemin physique : running de alpha_s selon l’équation RG dans une théorie déclarée ;
chaîne expérimentale : combinaison des spectres, fractions de branchement et covariances ;
chemin inférentiel : moments FESR, choix de poids, OPE, DV et ajustement multiparamétrique ;
chemin computationnel : algorithmes de combinaison et d’optimisation ;
chemin de représentation : schéma MS-bar et prescription FOPT ;
chemin de raccordement : changement de n_f aux seuils ;
histoire temporelle de alpha_s : non établie et non pertinente pour cette extraction.
```

## 8. Test de maintien

La chaîne ne teste pas l’identité numérique de `alpha_s` entre `m_tau` et `m_Z`. Elle
teste si un paramètre extrait à basse énergie, après corrections et transport déclarés,
est compatible avec la dynamique de renormalisation utilisée pour le rapporter à une
référence commune.

Le porteur du maintien testé par cette chaîne est donc :

```text
la compatibilité conditionnelle entre la fonction spectrale, la représentation FESR,
les corrections non perturbatives et la relation RG de transport.
```

La valeur native, le budget publié, les fenêtres finales et les réglages de transport
sont désormais assez déterminés pour la comparaison T1.6. Ce constat ne vaut pas
reproduction : les données, les ajustements FESR et la covariance multiparamétrique
complète n'ont pas été réexécutés dans le corpus.

## 9. Dimensions et portée

```text
dimension objet : coefficient de couplage défini dans un schéma et à une échelle ;
dimension accès : fonction spectrale reconstruite et fit FESR multiparamétrique ;
dimension constitution : dynamique QCD perturbative et non perturbative du canal ;
portée physique : extraction locale de alpha_s et test du running après transport ;
portée épistémologique : dépendance de la précision aux covariances, poids et modèles DV ;
portée ontologique : non engagée.
```

## 10. Limites et statut pour la comparaison

```text
valeur native et budget publié : extraits ;
fenêtres, poids et nombre de groupes : extraits ;
réglages de transport : extraits ;
statut pour la classification T1.6 : close ;
données et code complets du fit : non reproduits ;
covariance complète alpha_s–OPE–DV : non acquise ;
indépendance des composantes d'incertitude : non établie.
```

La chaîne est donc **fermée pour l'entrée descriptive de T1.6**, mais non reproduite.
Elle autorise une comparaison de valeurs finales et d'intervalles publiés ; elle
n'autorise ni une combinaison statistique inter-chaînes, ni une attribution causale
complète de leurs écarts, ni une nouvelle détermination de `alpha_s`.
