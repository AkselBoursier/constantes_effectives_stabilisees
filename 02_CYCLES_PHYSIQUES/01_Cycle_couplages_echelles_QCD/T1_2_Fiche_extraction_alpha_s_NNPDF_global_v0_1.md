# T1.2 — Fiche d’extraction globale NNPDF de `alpha_s(m_Z)` v0.1

## 0. Statut

```text
statut : fiche primaire de chaîne d’extraction ;
date de contrôle : 21 juillet 2026 ;
source de référence : Eur. Phys. J. C 85, 1001 (2025) ;
texte de travail : arXiv:2506.13871v2 ;
fonction : rendre contrôlable une extraction globale corrélée de alpha_s et des PDF ;
ne vaut pas : reproduction du fit NNPDF, validation indépendante du jeu de données,
               moyenne mondiale ou mesure de alpha_s(Q) par bins d’échelle.
```

## 1. Porteur et transformation

### Porteurs à distinguer

```text
paramètre rapporté : alpha_s^(n_f=5)(m_Z) dans le schéma MS-bar ;
structure ajustée conjointement : distributions partoniques (PDF) ;
objet statistique : qualité globale des prédictions sur un ensemble multi-processus ;
objet T1 : cohérence du paramètre avec les PDF, les covariances et les prédictions
           d’ordre perturbatif déclaré.
```

Cette chaîne ne part pas d’une observable unique et ne transporte pas une valeur native
depuis une échelle basse. Elle ajuste directement une valeur de référence à `m_Z`, dont
les effets se propagent aux prédictions à différentes échelles par les équations
d’évolution et les calculs propres aux processus.

### Transformations déclarées

```text
variation du paramètre alpha_s(m_Z) sur une grille de valeurs ;
évolution des PDF ;
passage NNLO -> aN3LO ;
ajout ou retrait des corrections QED ;
variation du jeu de données ;
variation de la solution des équations d’évolution ;
variation de la covariance utilisée pour les répliques ;
variation de la masse du quark top ;
activation ou retrait de contraintes de positivité.
```

## 2. Données et observables

Le jeu global NNPDF4.0 réunit des données de cible fixe et de collisionneurs :

```text
diffusion profondément inélastique ;
processus Drell–Yan et production de bosons électrofaibles ;
jets inclusifs et dijets ;
production de photons directs ;
production de quarks top ;
autres processus hadroniques du jeu global NNPDF4.0.
```

Le paramètre n’est donc pas associé à une seule sensibilité expérimentale. Chaque groupe
de processus contraint des combinaisons différentes de PDF et de `alpha_s`, avec des
corrélations croisées.

Les valeurs préférées par les `chi^2` partiels ne doivent pas être lues comme des
extractions indépendantes par processus ni combinées par moyenne pondérée. Les auteurs
soulignent qu’elles négligeraient les corrélations entre processus et la compensation
possible par les autres paramètres du fit global.

## 3. Méthodes d’extraction

Deux méthodes sont appliquées en parallèle.

### 3.1 Correlated Replica Method (CRM)

```text
cadre : maximum de vraisemblance fréquentiste ;
outil : rééchantillonnage Monte-Carlo corrélé ;
fonction : déterminer simultanément alpha_s et les PDF en conservant leur corrélation.
```

### 3.2 Theory Covariance Method (TCM)

```text
cadre : estimation bayésienne du posterior ;
outil : matrice de covariance théorique pour les ordres supérieurs manquants ;
fonction : traiter les corrélations entre incertitudes théoriques des prédictions et
           celles incorporées dans la détermination des PDF.
```

Les deux méthodes sont soumises à des tests de fermeture sur données synthétiques. Ces
tests servent à détecter des biais liés notamment au traitement des incertitudes
multiplicatives et aux contraintes de positivité.

Le résultat final est retenu à partir de la TCM, qui emploie le plus grand nombre de
répliques. L’incertitude inférieure finale inclut linéairement l’écart observé entre les
résultats TCM avec et sans positivité.

## 4. Théorie et pipeline

```text
QCD : NNLO et approximation aN3LO ;
QED : corrections NLO et PDF du photon ;
incertitudes d’ordres supérieurs manquants : incluses par covariance théorique ;
évolution : code EKO ;
grilles rapides : PineAPPL ;
matching des quarks lourds : implémentation actualisée citée par les auteurs.
```

Les calculs reposent sur la méthodologie et le jeu de données NNPDF4.0. Les auteurs
étudient l’effet :

- d’une solution exacte ou développée des équations d’évolution ;
- de la matrice de covariance expérimentale ou de la matrice `t_0` pour générer les
  répliques ;
- de la valeur de la masse du quark top ;
- des corrections QED ;
- de l’ordre perturbatif ;
- du jeu de données retenu.

## 5. Échantillonnage, nuisance et corrélations

Pour les résultats de base décrits dans l’article :

```text
CRM : 250 répliques pour chacune de 12 valeurs de alpha_s ;
TCM : 550 répliques ;
filtrage post-fit : sélection des valeurs aberrantes selon la méthodologie NNPDF ;
incertitudes : intervalles à un écart-type et à 68 % de niveau de confiance ;
contrôle de taille finie : bootstrap, effet inférieur au pour mille sur la valeur centrale.
```

Les PDF sont des paramètres fonctionnels de nuisance fortement corrélés avec `alpha_s`.
Les incertitudes expérimentales corrélées, les incertitudes théoriques corrélées, la
positivité et la génération des répliques appartiennent donc à l’identité de la chaîne
d’extraction.

## 6. Résultat

```text
alpha_s(m_Z) = 0.1194^{+0.0007}_{-0.0014}
ordre : aN3LO_QCD x NLO_QED ;
incertitudes d’ordres supérieurs manquants : incluses ;
méthode finale : TCM avec prescription de positivité décrite par les auteurs.
```

Le résultat est directement paramétré à la référence commune `m_Z`. Il n’existe pas ici
de valeur native basse énergie à transporter vers `m_Z` comme dans le cas tau.

Les auteurs rendent publics des ensembles de PDF au format LHAPDF pour plusieurs valeurs
de `alpha_s(m_Z)`, aux ordres NNLO et aN3LO, avec ou sans QED, incluant les incertitudes
d’ordres supérieurs manquants. Les répliques portant le même indice pour différentes
valeurs de `alpha_s` sont corrélées parce qu’elles proviennent de la même réplique de
données sous-jacente.

## 7. Typage des chemins

```text
chemin physique : évolution DGLAP et running de alpha_s dans les prédictions ;
chaîne expérimentale : agrégation des jeux de données multi-processus ;
chemin inférentiel : vraisemblance globale, CRM ou TCM, covariance et sélection post-fit ;
chemin computationnel : EKO, PineAPPL, génération et ajustement des répliques ;
chemin de représentation : paramétrisation des PDF, schéma MS-bar et ordre perturbatif ;
chemin de raccordement : matching des saveurs lourdes dans l’évolution ;
histoire temporelle : non pertinente.
```

## 8. Test de maintien provisoire

Cette chaîne ne montre pas qu’une valeur identique de `alpha_s` est mesurée séparément
par chaque processus. Elle teste si un même paramètre de référence et un même ensemble de
PDF permettent une description globale cohérente, après prise en compte des corrélations
et incertitudes théoriques déclarées.

Le porteur provisoire du maintien est :

```text
la cohérence globale d’un système corrélé alpha_s + PDF avec les données et les
prédictions multi-processus au niveau d’approximation déclaré.
```

Ce porteur est plus large que le coefficient isolé. La valeur finale ne peut pas être
dissociée de la structure fonctionnelle des PDF et du modèle global de covariance.

## 9. Dimensions et portée

```text
dimension objet : coefficient alpha_s(m_Z) dans le schéma MS-bar ;
dimension accès : fit global, données multi-processus et covariance ;
dimension constitution : évolution perturbative, factorisation et structure partonique ;
portée physique : valeur globale de référence cohérente avec le jeu de données déclaré ;
portée épistémologique : rôle des corrélations, des biais de méthode et des MHOUs ;
portée ontologique : non engagée.
```

## 10. Limites et opération suivante

La fiche permet une comparaison structurelle avec le cas tau, mais pas une reproduction
intégrale du fit.

Éléments à verrouiller pour une reproduction quantitative :

1. liste versionnée complète des données et coupes du jeu NNPDF4.0 utilisé ;
2. configurations exactes EKO/PineAPPL et tables théoriques ;
3. définition numérique de la grille des 12 valeurs de `alpha_s` ;
4. répliques, sélections post-fit et matrices de covariance ;
5. décomposition numérique complète de l’incertitude finale.

Les ensembles LHAPDF publics rendent possible un contrôle ultérieur des prédictions,
mais ils ne suffisent pas seuls à reproduire le minimum global ni la covariance de
`alpha_s`. Cette limite ne bloque pas la troisième fiche T1.2.