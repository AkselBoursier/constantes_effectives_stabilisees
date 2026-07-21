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

L’approche dite `truncated OPE` n’est pas retenue : les auteurs soutiennent que la mise à
zéro de contributions OPE de dimension supérieure produit des incohérences sur les
moments considérés à cette échelle.

## 5. Paramètres et résultat

### Résultat transporté publié

```text
alpha_s(m_Z^2) = 0.1159(14).
```

Ce nombre est le résultat final annoncé par l’article et la prépublication v2.

### Paramètre natif

Le paramètre physiquement ajusté appartient au régime `n_f = 3`, dans le schéma
`MS-bar`, à une échelle de l’ordre de la masse du tau. La valeur numérique native exacte,
sa covariance avec les paramètres OPE/DV et sa décomposition d’incertitude ne sont pas
encore verrouillées dans la présente fiche.

Statut :

```text
existence du paramètre natif : établie ;
valeur native exacte : non extraite ;
covariance complète du fit : non extraite ;
fenêtre exacte en s_0 et jeu final de moments : non extraits.
```

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

L’article fournit le résultat transporté, mais les réglages exacts de cette opération ne
sont pas encore extraits dans cette fiche. Il est donc interdit de traiter `0.1159(14)`
comme si toute son incertitude provenait directement de la fonction spectrale.

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

## 8. Test de maintien provisoire

La chaîne ne teste pas l’identité numérique de `alpha_s` entre `m_tau` et `m_Z`. Elle
teste si un paramètre extrait à basse énergie, après corrections et transport déclarés,
est compatible avec la dynamique de renormalisation utilisée pour le rapporter à une
référence commune.

Le porteur provisoire du maintien est donc :

```text
la compatibilité conditionnelle entre la fonction spectrale, la représentation FESR,
les corrections non perturbatives et la relation RG de transport.
```

Ce verdict reste provisoire tant que la valeur native, la covariance du fit et les
réglages de transport ne sont pas extraits.

## 9. Dimensions et portée

```text
dimension objet : coefficient de couplage défini dans un schéma et à une échelle ;
dimension accès : fonction spectrale reconstruite et fit FESR multiparamétrique ;
dimension constitution : dynamique QCD perturbative et non perturbative du canal ;
portée physique : extraction locale de alpha_s et test du running après transport ;
portée épistémologique : dépendance de la précision aux covariances, poids et modèles DV ;
portée ontologique : non engagée.
```

## 10. Limites et opération suivante

La fiche établit la structure de la chaîne mais ne permet pas encore une reproduction du
transport ni un audit quantitatif complet de ses incertitudes.

Éléments à extraire avant clôture de cette chaîne :

1. valeur exacte de `alpha_s^(3)(m_tau^2)` ou de la valeur native effectivement retenue ;
2. fenêtre finale en `s_0`, fonctions poids et nombre de points ;
3. paramètres OPE/DV et covariance utile avec `alpha_s` ;
4. ordre de la fonction bêta, masses de seuil et matching employés ;
5. part d’incertitude attribuable à l’extraction et au transport.

Ces lacunes ne bloquent pas la rédaction des deux autres fiches T1.2. Elles bloqueront en
revanche la reproduction T1.5 et toute comparaison quantitative qui prétendrait séparer
l’incertitude native de celle du transport.