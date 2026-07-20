# Cadrage de la reprise scientifique du cycle 1 — QCD et test T1 v0.1

## 0. Statut et portée

```text
statut : ouverture scientifique bornée du cycle 1 ;
date : 20 juillet 2026 ;
branche : agent/cycle-1-qcd-t1 ;
base : nouveau main après fusion de la PR 16 ;
fonction : transformer T1 en enquête physique exécutable sur plusieurs chaînes
d'extraction de alpha_s ;
ne vaut pas : nouvelle moyenne mondiale, revue générale de toute la QCD, validation
d'une variation temporelle, modification du statut canonique de « constante
effective » ou reprise générale de Lambda_QCD.
```

La reprise part de l'acquis déjà conservé : stabilité temporelle, dépendance à
l'échelle, changement de régime et simplicité théorique ne sont pas équivalents.
Elle ne cherche pas à ajouter une catégorie de constantes. Elle demande ce qui est
réellement maintenu lorsque des déterminations issues de processus différents sont
transportées dans un cadre commun.

## 1. Question physique de T1

La question n'est pas :

> Quelle est la valeur unique de la constante forte ?

Elle devient :

> Lorsque plusieurs observables, mesurées ou calculées à des échelles et par des
> méthodes différentes, conduisent à des déterminations de `alpha_s`, quelle
> quantité ou relation est soumise au test de cohérence après déclaration du
> schéma, de l'ordre perturbatif, des corrections et du transport vers une
> référence commune ?

Quatre porteurs possibles doivent rester séparés :

```text
A. alpha_s^(n_f)(mu) dans un schéma déclaré ;
B. la trajectoire du groupe de renormalisation reliant plusieurs échelles ;
C. l'observable physique dont alpha_s est un paramètre extrait ;
D. la cohérence d'un ensemble de chaînes d'extraction après transport commun.
```

Le test devra déterminer lequel de ces porteurs soutient effectivement l'énoncé de
maintien. Il est interdit de transformer la trajectoire du groupe de
renormalisation en histoire temporelle d'un même système.

## 2. Transformations et chemins à typer

Chaque fiche de détermination devra distinguer au minimum :

```text
échelle cinématique Q ;
échelle de renormalisation mu_R ;
échelle de factorisation mu_F lorsqu'elle intervient ;
schéma de renormalisation ;
nombre de saveurs actives n_f ;
ordre perturbatif et éventuelle resommation ;
seuils et raccordements ;
corrections non perturbatives ou d'hadronisation ;
modèle statistique, paramètres de nuisance et corrélations.
```

Les chemins sont nommés séparément :

```text
chemin d'extraction : données ou observable -> corrections -> paramètre ;
chemin de transport : alpha_s(mu_0) -> évolution RG -> échelle commune ;
chemin de raccordement : franchissement de seuils et changement de n_f ;
chemin de combinaison : covariance, hypothèses d'indépendance et moyenne ;
histoire physique : non établie par les chemins précédents.
```

## 3. Référence commune et contrôle externe

La convention de comparaison initiale sera, sauf impossibilité explicitée :

```text
alpha_s^(5)(m_Z) dans le schéma MS-bar.
```

Le `Review of Particle Physics` 2025 fournit le contrôle de paysage, non la cible à
reproduire. Il donne une moyenne mondiale de contexte
`alpha_s(m_Z^2) = 0.1180 ± 0.0009` et montre la cohérence du running sur plusieurs
ordres de grandeur en énergie. Cette moyenne ne sera pas utilisée pour forcer les
résultats individuels ni pour décider à l'avance de leur compatibilité.

Le contrôle doit porter sur les opérations, pas seulement sur la proximité des
nombres finaux.

## 4. Premier échantillon borné

Le premier lot retient trois déterminations primaires suffisamment différentes
pour tester T1, plus un contrôle lattice composite.

### 4.1 Désintégrations hadroniques du tau — basse échelle

Source initiale : D. Boito et al., *The strong coupling from hadronic tau-decay
data including tau -> pi pi0 nu_tau from Belle* (2025).

```text
observable primaire : fonction spectrale vectorielle isovectorielle inclusive et
                       moments de sommes de règles à énergie finie ;
processus : désintégrations hadroniques du tau, complétées par des données
            d'électroproduction pour certains modes ;
échelle caractéristique : de l'ordre de m_tau ;
paramètre rapporté : alpha_s transporté vers m_Z ;
résultat publié dans le préprint : alpha_s(m_Z^2) = 0.1159(14) ;
points critiques : construction de la fonction spectrale, fonctions poids,
                   OPE, violations de dualité, choix perturbatif, données HFLAV
                   et corrélations entre canaux.
```

Fonction dans T1 : tester une extraction à basse échelle dont le transport vers
`m_Z` amplifie l'importance du traitement perturbatif et non perturbatif.

### 4.2 Ajustement global des distributions partoniques — large domaine de Q

Source initiale : NNPDF Collaboration, *A Determination of alpha_s(m_Z) at
approximate N3LO QCD x NLO QED Accuracy from a Global PDF Analysis* (2025).

```text
observables primaires : données de diffusion profondément inélastique et processus
                        hadroniques de collisionneurs dans un ajustement global ;
processus : ajustement simultané de alpha_s et des distributions partoniques ;
échelles : domaine étendu, avec évolution DGLAP et échelles propres aux processus ;
ordre : NNLO et approximation N3LO en QCD, corrections QED NLO ;
paramètre rapporté : alpha_s(m_Z) = 0.1194^{+0.0007}_{-0.0014} ;
points critiques : corrélation alpha_s-PDF, covariance expérimentale, incertitudes
                   de termes d'ordre supérieur manquants, masse du quark top,
                   méthodologie Monte Carlo et tests de fermeture.
```

Fonction dans T1 : tester un cas où le paramètre et une structure fonctionnelle
hautement corrélée sont ajustés ensemble, de sorte que la chaîne d'accès ne peut
pas être réduite à une observable unique.

### 4.3 Formes d'événements en annihilation électron-positron — plusieurs énergies

Source initiale : P. Nason et G. Zanderighi, *Fits of alpha_s from event-shapes in
the three-jet region: extension to all energies* (2025).

```text
observables primaires : distributions de formes et de jets dans e+e- ;
processus : données de plusieurs expériences entre 22 et 207 GeV ;
échelles : énergie de centre de masse et échelles internes des observables ;
paramètres ajustés : alpha_s et paramètre non perturbatif alpha_0 ;
paramètre rapporté : alpha_s(m_Z) = 0.1181 avec incertitudes expérimentales et
                     théoriques séparées ;
points critiques : choix d'échelle, effets de masse, limites de fit,
                   schéma de corrections de puissance, hadronisation et
                   corrélation perturbatif/non perturbatif.
```

Fonction dans T1 : tester simultanément le running à plusieurs énergies et la
séparation entre corrections perturbatives et non perturbatives.

### 4.4 Contrôle lattice composite — non compté comme fiche primaire unique

Le `FLAG Review 2024` et la synthèse PDG 2025 servent de carte de contrôle des
familles lattice. L'estimation FLAG 2024 rapportée par le PDG est
`alpha_s(m_Z^2) = 0.1183 ± 0.0007`.

Ce nombre agrège plusieurs stratégies et ne sera pas traité comme une chaîne
d'extraction unique. Une phase ultérieure devra sélectionner au moins une
détermination lattice primaire — par exemple par step scaling ou découplage — et
documenter séparément : observable de calibration, fixation de l'échelle,
extrapolation au continuum, schéma intermédiaire, raccord perturbatif et transport
vers `MS-bar` à `m_Z`.

## 5. Fiche commune de détermination

Chaque cas du premier lot devra remplir la même structure :

| Champ | Contenu attendu |
|---|---|
| source primaire | article, version, date et statut de publication |
| observable primaire | quantité directement mesurée ou calculée |
| données | expériences, jeux, domaine cinématique et sélections |
| processus | réaction ou calcul qui porte la sensibilité à `alpha_s` |
| échelle physique | `Q` ou domaine de `Q` pertinent |
| échelles auxiliaires | `mu_R`, `mu_F`, échelles de resommation ou de matching |
| schéma et saveurs | définition de `alpha_s`, `n_f` et conventions |
| ordre théorique | ordre fixe, resommation, évolution et approximations |
| corrections | masses, électrofaible, hadronisation, OPE, puissance, réseau |
| nuisance et corrélations | paramètres associés, covariance et dépendances communes |
| paramètre extrait | valeur à l'échelle native et définition exacte |
| transport | beta-fonction, seuils, matching et ordre du transport |
| résultat commun | valeur rapportée ou recalculée à `m_Z` |
| incertitude | séparation expérimentale, théorique, non perturbative et transport |
| test de maintien | coefficient, relation RG, observable ou cohérence inter-chaînes |
| limites | ce que la fiche ne permet pas de conclure |

## 6. Comparaison et règle de décision

Le premier lot ne calculera pas une nouvelle moyenne mondiale. Il produira une
matrice de comparabilité.

Pour chaque écart entre deux déterminations, la matrice devra indiquer si la cause
est :

```text
isolée ;
associée à plusieurs choix ;
non identifiable avec les matériaux disponibles.
```

Les familles d'écarts à suivre sont :

```text
données et covariance ;
observable et sensibilité paramétrique ;
ordre perturbatif et resommation ;
échelles auxiliaires ;
corrections non perturbatives ;
paramètres de nuisance ;
transport RG et raccordement aux seuils ;
présentation ou combinaison des incertitudes.
```

Une compatibilité numérique finale ne suffira pas à déclarer les chaînes
équivalentes. Une différence numérique ne suffira pas non plus à conclure à une
incohérence physique tant que les hypothèses, corrélations et conventions ne sont
pas alignées.

## 7. Résultat attendu de T1

T1 devra répondre à la question suivante :

```text
Le maintien constaté porte-t-il sur la valeur d'un coefficient, sur la forme du
running, sur les relations de transport et de matching, ou sur la cohérence de
plusieurs observables avec une même dynamique de renormalisation ?
```

Hypothèse de travail, non verdict : le porteur le plus robuste devrait être la
cohérence conditionnelle des observables et des chaînes d'extraction avec une même
évolution RG, plutôt que l'identité numérique de `alpha_s` à toutes les échelles.

La portée ontologique reste non engagée. La question de portée physique,
épistémologique ou ontologique (`Q3`) demeure un contrôle interne non public.

## 8. Séquence exécutable

```text
T1.1 verrouiller les trois sources primaires et leurs versions ;
T1.2 produire une fiche complète pour chaque détermination ;
T1.3 sélectionner une détermination lattice primaire distincte ;
T1.4 construire la matrice de comparabilité et de corrélations ;
T1.5 vérifier ou reproduire le transport vers m_Z lorsque les entrées suffisent ;
T1.6 classifier les écarts et les dépendances de chemin ;
T1.7 formuler le verdict physique local ;
T1.8 seulement ensuite propager les acquis dans la synthèse du cycle 1.
```

Aucune modification de la synthèse active, du cadre canonique ou des questions
publiques n'est autorisée par le seul présent cadrage.

## 9. Sources initiales

- Particle Data Group, *Quantum Chromodynamics*, Review of Particle Physics 2025,
  révision d'août 2025.
- D. Boito et al., *The strong coupling from hadronic tau-decay data including
  tau -> pi-pi0 nu_tau from Belle*, arXiv:2502.08147.
- NNPDF Collaboration, *A Determination of alpha_s(m_Z) at aN3LO QCD x NLO QED
  Accuracy from a Global PDF Analysis*, arXiv:2506.13871.
- P. Nason et G. Zanderighi, *Fits of alpha_s from event-shapes in the three-jet
  region: extension to all energies*, arXiv:2501.18173.
- Flavour Lattice Averaging Group, *FLAG Review 2024*, arXiv:2411.04268.
