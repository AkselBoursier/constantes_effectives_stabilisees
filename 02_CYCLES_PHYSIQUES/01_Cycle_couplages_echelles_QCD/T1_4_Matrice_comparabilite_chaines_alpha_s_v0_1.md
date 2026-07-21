# T1.4 — Matrice de comparabilité des chaînes de détermination de `alpha_s` v0.1

## 0. Statut

```text
statut : comparaison structurelle du premier lot ;
date : 21 juillet 2026 ;
entrées : trois fiches phénoménologiques et une fiche lattice primaire ;
fonction : identifier ce qui est comparable avant calcul de compatibilité ;
ne vaut pas : moyenne, combinaison statistique, test de tension définitif ou verdict T1.
```

## 1. Résultats rapportés à la référence commune

| Chaîne | Résultat publié | Forme de l’incertitude | Paramètre natif |
|---|---:|---|---|
| tau — FESR | `0.1159 +/- 0.0014` | natif : `+/-0.0092_stat +/-0.0026_fit +/-0.0022_pert +/-0.0025_c = +/-0.0101`, puis transport | `alpha_s^(3)(m_tau^2) = 0.2983 +/- 0.0101` |
| NNPDF global | `0.1194^{+0.0007}_{-0.0014}` | asymétrique, TCM et positivité | directement `alpha_s^(5)(m_Z)` |
| formes d’événements | `0.1181^{+0.0002+0.0018}_{-0.0005-0.0021}` | expérimental et théorique séparés | directement `alpha_s^(5)(M_Z)` |
| lattice ALPHA 2026 | `0.118755 +/- 0.00058` | dominée par statistique, avec échelle robuste | `Lambda_MSbar^(3)`, puis matching vers `N_f=5` |

Toutes les valeurs finales sont exprimées dans le schéma `MS-bar` à l’échelle du boson Z
et peuvent donc être placées sur un même axe numérique. Cette condition est nécessaire,
mais elle ne rend pas les chaînes équivalentes.

## 2. Observable, données et objet ajusté

| Dimension | Tau | NNPDF global | Formes d’événements | Lattice ALPHA 2026 |
|---|---|---|---|---|
| entrée primaire | fonction spectrale vectorielle combinée en `63` groupes | données globales DIS et collisionneurs | distributions `T`, `C`, `y_23` | observables de couplage en volume fini |
| domaine d’échelle | `s_0^max = 3.0871 GeV^2`; dix `s_0^min` de `1.4747` à `1.9249 GeV^2` | large domaine propre aux processus | `22–207 GeV` | `0.2–140 GeV` non perturbatif + raccords |
| objet conjoint | OPE et paramètres DV | PDF fonctionnelles | paramètre `alpha_0` | échelles GF/SF, limites du continuum |
| sortie intermédiaire | moments FESR, poids central `w_0` et contrôles `w_2,w_3,w_4` | minimum global du fit | minimum dans `(alpha_s, alpha_0)` | `Lambda_MSbar^(3)` par deux routes |
| sortie finale | `alpha_s^(5)(m_Z)` | `alpha_s^(5)(m_Z)` | `alpha_s^(5)(M_Z)` | `alpha_s^(5)(m_Z)` |

Dans la chaîne tau, la moyenne HFLAV 2022 `B_(pi- 3 pi0) = 0.01040(71)` baisse
d'environ `9 %` et porte une erreur environ `2,4` fois plus grande que l'entrée 2019.
Les auteurs en font la source principale du déplacement et de l'élargissement par
rapport à leur analyse tau antérieure, non une cause isolée des écarts inter-chaînes.

## 3. Théorie, approximation et non-perturbatif

| Contrôle | Tau | NNPDF global | Formes d’événements | Lattice ALPHA 2026 |
|---|---|---|---|---|
| perturbatif | fonction d’Adler, FOPT | NNLO / aN3LO QCD, NLO QED | NNLO fixe avec EERAD3 | seulement à haute énergie et pour matching |
| resommation | CIPT exclue dans la chaîne | évolution et calculs propres aux processus | pas de résommation centrale en région 3 jets | running non perturbatif par step scaling |
| non-perturbatif | OPE + violations de dualité | PDF ajustées ; corrections de processus | corrections de puissance `alpha_0` | dynamique lattice de premier principe |
| schémas auxiliaires | poids FESR et prescription perturbative | paramétrisation PDF, positivité | schémas de masses `E`, `p`, `D`, standard | GF, SF, `MS-bar` |
| changement de régime | seuils lourds après extraction | matching des saveurs dans l’évolution | masses lourdes et hadronisation | `N_f=0,3,4,5`, continuum et découplage |

## 4. Chaînes de chemin

| Type de chemin | Tau | NNPDF global | Formes d’événements | Lattice ALPHA 2026 |
|---|---|---|---|---|
| expérimental / réalisation | reconstruction spectrale | agrégation multi-processus | histogrammes multi-expériences | simulations et fixation d’échelle |
| inférentiel | fit FESR multiparamétrique | CRM / TCM global | `chi^2` global `alpha_s-alpha_0` | extrapolations et combinaison corrélée |
| computationnel | moments, combinaison, optimisation | EKO, PineAPPL, répliques | EERAD3 et grilles adaptatives | openQCD, step scaling, paquet de réplication |
| représentation | `MS-bar`, FOPT, poids | PDF, ordre, positivité | observables et schémas de masse | GF, SF, `MS-bar` |
| transport / matching | évolution à cinq boucles, matching à quatre boucles aux seuils `2m_c` et `2m_b`; incertitude additionnelle annoncée très petite | paramètre déjà à `m_Z`, running dans les prédictions | paramètre déjà à `M_Z`, running dans les prédictions | `Lambda^(3) -> alpha_s^(5)(m_Z)` |
| histoire temporelle | non pertinente | non pertinente | non pertinente | non pertinente |

## 5. Corrélations internes et croisées

### 5.1 Corrélations internes établies

```text
tau : spectres, fractions de branchement, moments, OPE et DV ; moyenne des dix
      fenêtres avec propagation de leur covariance complète ;
NNPDF : alpha_s, PDF, processus, covariance expérimentale et théorique ;
formes : alpha_s, alpha_0, bins, expériences et schémas de masse ;
lattice : routes directe et découplage, fixation de l’échelle et mu_dec.
```

Pour tau, la covariance complète entre `alpha_s`, les paramètres OPE et les paramètres
DV n'est pas acquise dans le corpus. Le budget publié ne démontre pas non plus
l'indépendance des composantes `stat`, `fit`, `pert` et `c`.

### 5.2 Corrélations croisées entre chaînes

Aucune matrice de covariance inter-chaînes n’est disponible. Les dépendances communes
possibles comprennent :

- la masse du boson Z et les masses de quarks utilisées pour les raccordements ;
- les mêmes coefficients de fonction bêta et relations de matching ;
- des conventions communes du schéma `MS-bar` ;
- des synthèses ou entrées externes communes ponctuelles ;
- des données de collisionneurs potentiellement partagées entre certains fits globaux,
  mais pas avec les chaînes tau ou lattice dans leur entrée principale.

Ces éléments sont probablement sous-dominants pour une lecture descriptive, mais leur
absence interdit une combinaison statistique rigoureuse du présent lot.

## 6. Comparaison numérique descriptive

La valeur lattice 2026 sert ici de repère indépendant et non de vérité imposée.

```text
tau - lattice : -0.002855 ;
tau - NNPDF : -0.003500 ;
tau - formes : -0.002200 ;
NNPDF - lattice : +0.000645 ;
formes - lattice : -0.000655 ;
NNPDF - formes : +0.001300.
```

En supposant provisoirement des erreurs indépendantes et, seulement pour le cas tau, une
combinaison quadratique simple avec l’erreur lattice, l’écart tau–lattice vaut
`1.884` distances descriptives. Ce nombre n’est pas un test de tension publiable :
l'indépendance inter-chaînes est une hypothèse et les corrélations de transport ne sont
pas disponibles.

Pour NNPDF et formes d’événements, l’asymétrie et la séparation des composantes empêchent
de condenser correctement l’écart en un unique nombre de sigmas sans prescription
supplémentaire. Visuellement, leurs intervalles publiés recouvrent le voisinage de la
valeur lattice.

## 7. Classification des écarts

| Famille | État actuel | Commentaire |
|---|---|---|
| données et covariance | associée à plusieurs choix | objets expérimentaux entièrement différents |
| observable et sensibilité | associée à plusieurs choix | spectre, PDF globales, formes, couplages lattice |
| ordre perturbatif | associée à plusieurs choix | traitements et domaines non homogènes |
| échelles auxiliaires | associée à plusieurs choix | `mu_R`, `mu_F`, volumes, `mu_dec`, bornes `s_0` |
| non-perturbatif | associée à plusieurs choix | DV/OPE, PDF, puissance, lattice |
| paramètres de nuisance | associée à plusieurs choix | structures très différentes |
| transport RG et seuils | associée à plusieurs choix, mais effet inter-chaînes non isolé | réglages tau extraits ; pipeline lattice répliqué |
| présentation des incertitudes | associée à plusieurs choix | symétrique, asymétrique, séparée, variance détaillée |
| cause de l’écart tau | non identifiable | HFLAV/Belle expliquent le déplacement interne entre analyses tau, non l'écart aux autres chaînes |

## 8. Porteur provisoire de la cohérence par chaîne

```text
tau : compatibilité spectre–FESR–corrections–transport ;
NNPDF : cohérence du système corrélé alpha_s + PDF avec le jeu global ;
formes : cohérence multi-échelles du running et de la séparation perturbatif / NP ;
lattice : cohérence de deux routes non perturbatives vers Lambda_MSbar^(3), puis matching.
```

Le dénominateur commun n’est donc pas une opération identique. Il est :

> la possibilité de rapporter des chaînes hétérogènes à une même définition de
> `alpha_s^(5)(m_Z)` tout en conservant les transformations, schémas et incertitudes qui
> conditionnent chaque détermination.

## 9. Résultat de T1.4

```text
comparabilité numérique finale : établie sous convention commune ;
équivalence des chaînes : refusée ;
indépendance statistique complète : non établie ;
matrice de covariance inter-chaînes : absente ;
écart tau : signal descriptif à instruire, pas tension établie ;
opération rendue possible : T1.6, classer les six écarts centraux sans combinaison globale.
```

La matrice est désormais complétée par l'extraction quantitative tau et par la
reproduction T1.5 du pipeline lattice à partir des produits condensés. Elle suffit pour
fournir l'entrée de la classification T1.6 ; elle ne suffit pas, seule, à formuler une
moyenne ou un test de tension global.
