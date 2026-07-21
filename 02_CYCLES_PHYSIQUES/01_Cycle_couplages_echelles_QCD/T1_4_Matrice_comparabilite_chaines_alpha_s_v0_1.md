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
| tau — FESR | `0.1159(14)` | symétrique, composition détaillée à extraire | `alpha_s^(3)` à basse échelle, puis transport |
| NNPDF global | `0.1194^{+0.0007}_{-0.0014}` | asymétrique, TCM et positivité | directement `alpha_s^(5)(m_Z)` |
| formes d’événements | `0.1181^{+0.0002+0.0018}_{-0.0005-0.0021}` | expérimental et théorique séparés | directement `alpha_s^(5)(M_Z)` |
| lattice ALPHA 2026 | `0.11876(58)` | dominée par statistique, avec échelle robuste | `Lambda_MSbar^(3)`, puis matching vers `N_f=5` |

Toutes les valeurs finales sont exprimées dans le schéma `MS-bar` à l’échelle du boson Z
et peuvent donc être placées sur un même axe numérique. Cette condition est nécessaire,
mais elle ne rend pas les chaînes équivalentes.

## 2. Observable, données et objet ajusté

| Dimension | Tau | NNPDF global | Formes d’événements | Lattice ALPHA 2026 |
|---|---|---|---|---|
| entrée primaire | fonctions spectrales vectorielles | données globales DIS et collisionneurs | distributions `T`, `C`, `y_23` | observables de couplage en volume fini |
| domaine d’échelle | ordre de `m_tau` | large domaine propre aux processus | `22–207 GeV` | `0.2–140 GeV` non perturbatif + raccords |
| objet conjoint | OPE et paramètres DV | PDF fonctionnelles | paramètre `alpha_0` | échelles GF/SF, limites du continuum |
| sortie intermédiaire | moments FESR | minimum global du fit | minimum dans `(alpha_s, alpha_0)` | `Lambda_MSbar^(3)` par deux routes |
| sortie finale | `alpha_s^(5)(m_Z)` | `alpha_s^(5)(m_Z)` | `alpha_s^(5)(M_Z)` | `alpha_s^(5)(m_Z)` |

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
| transport / matching | `N_f=3 -> 5`, basse énergie vers `m_Z` | paramètre déjà à `m_Z`, running dans les prédictions | paramètre déjà à `M_Z`, running dans les prédictions | `Lambda^(3) -> alpha_s^(5)(m_Z)` |
| histoire temporelle | non pertinente | non pertinente | non pertinente | non pertinente |

## 5. Corrélations internes et croisées

### 5.1 Corrélations internes établies

```text
tau : spectres, fractions de branchement, moments, OPE et DV ;
NNPDF : alpha_s, PDF, processus, covariance expérimentale et théorique ;
formes : alpha_s, alpha_0, bins, expériences et schémas de masse ;
lattice : routes directe et découplage, fixation de l’échelle et mu_dec.
```

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
tau - lattice : -0.00286 ;
NNPDF - lattice : +0.00064 ;
formes - lattice : -0.00066.
```

En supposant provisoirement des erreurs indépendantes et, seulement pour le cas tau, une
combinaison quadratique simple avec l’erreur lattice, l’écart tau–lattice est d’environ
`1.9 sigma`. Ce nombre n’est pas un test de tension publiable : la décomposition exacte de
l’incertitude tau et les corrélations de transport ne sont pas encore extraites.

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
| transport RG et seuils | non identifiable quantitativement | réglages tau incomplets ; lattice réplicable |
| présentation des incertitudes | associée à plusieurs choix | symétrique, asymétrique, séparée, variance détaillée |
| cause de l’écart tau | non identifiable | aucune composante unique isolée à ce stade |

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
prochaine opération : T1.5, commencer par la reproduction lattice publique.
```

La matrice est suffisante pour choisir la reproduction prioritaire. Elle ne suffit pas
pour formuler le verdict physique final de T1.