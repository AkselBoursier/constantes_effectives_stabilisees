# N5 — Matrice comparative des quatre accès neutrino v0.1

## 0. Statut, fonction et coupure

```text
statut : synthèse comparative active du cycle neutrino ;
étape : N5 du protocole commun des quatre accès ;
date : 17 juillet 2026 ;
date de coupure bibliographique : 17 juillet 2026 inclus ;
fonction : comparer les fonctions du spectre contraintes, reconstruire les ponts
           légitimes, qualifier les compatibilités et localiser les désaccords ;
base : N0, N1 oscillations, N2 cinématique bêta, N3 cosmologie et N4 double bêta
       sans neutrino ;
ne vaut pas : ajustement statistique conjoint des quatre likelihoods, moyenne des
              bornes, détermination définitive de l'ordre, de la masse minimale ou
              de la nature Dirac/Majorana ;
révision : requise à chaque nouveau résultat directeur ou si une reproduction
           numérique modifie une compatibilité formulée ici.
```

La matrice applique le [protocole N0](N0_Protocole_commun_fiches_acces_neutrinos_v0_1.md)
aux quatre fiches :

- [N1 — oscillations](N1_Fiche_acces_oscillations_neutrinos_v0_1.md) ;
- [N2 — cinématique bêta](N2_Fiche_acces_cinematique_beta_neutrinos_v0_1.md) ;
- [N3 — cosmologie](N3_Fiche_acces_cosmologie_somme_masses_neutrinos_v0_1.md) ;
- [N4 — double bêta sans neutrino](N4_Fiche_acces_double_beta_sans_neutrino_v0_1.md).

Elle ne recherche pas un nombre synthétique appelé « masse du neutrino ». Elle
compare quatre énoncés situés, chacun reconstruit avec sa trace, son modèle de
passage, ses hypothèses et son statut statistique.

## 1. Résultat directeur

Le secteur ne livre pas quatre mesures répétées de la même grandeur :

```text
N1 : différences de masses au carré, mélange et phase de Dirac ;
N2 : moyenne quadratique incohérente sur la composante électronique m_beta ;
N3 : somme linéaire collective Sigma m_nu dans une histoire cosmologique ;
N4 : demi-vie isotopique, puis somme cohérente m_beta_beta sous mécanisme Majorana.
```

Leur articulation devient possible seulement si un modèle commun introduit un
spectre latent :

```text
{m_1, m_2, m_3}
+ matrice PMNS
+ ordre des masses
+ hypothèses propres à la cosmologie ou à la double bêta.
```

Le résultat central du cycle peut donc être formulé ainsi :

> L'identité empirique du secteur neutrino est éprouvée par la cohérence de
> fonctions non équivalentes d'un même spectre sous des ponts déclarés ; elle ne
> résulte ni d'un nombre commun directement lu, ni de la seule répétition du mot
> « masse ».

## 2. Matrice principale des chaînes d'accès

| Dimension | N1 — oscillations | N2 — cinématique bêta | N3 — cosmologie | N4 — double bêta sans neutrino |
|---|---|---|---|---|
| objet physique immédiat | propagation et conversion entre états de saveur et de masse | partage d'énergie dans la désintégration bêta | effets thermiques et gravitationnels du secteur relicte | processus nucléaire violant le nombre leptonique de deux unités |
| fonction contrainte | `Delta m^2_ij`, `theta_ij`, `delta_CP` | `m_beta^2 = somme_i |U_ei|^2 m_i^2` | `Sigma m_nu = somme_i m_i` | primaire : `T_1/2^0nu` ; conditionnelle : `m_beta_beta = |somme_i U_ei^2 m_i|` |
| trace primaire | distributions d'événements en énergie, direction et topologie | comptages d'électrons transmis selon le potentiel de retardation | spectres CMB, lentillage, redshifts, corrélations et multipoles de structure | dépôts d'énergie autour de `Q_beta_beta`, vertex, multiplicité et topologie selon le détecteur |
| observable publiée | spectres, taux, rapports proche–lointain, contours et profils | spectre intégral `R(qU)`, entrées de réponse et covariances | distances BAO, spectres CMB, lentillage, forme complète et likelihoods | spectres, exposition, efficacité, fond, limite de taux ou demi-vie |
| modèle de passage | flux + propagation en vide/matière + interactions + réponse + statistique | spectre moléculaire + états finaux + réponse MAC-E + pertes + fond + statistique | histoire thermique + code de Boltzmann + expansion + croissance + sondes + likelihoods + priors | réponse spectrale + fond + efficacité ; puis mécanisme + espace de phase + matrice nucléaire pour la masse |
| état empirique directeur | architecture différentielle fortement étayée ; ordre, octant et CP non définitivement fixés | `m_beta < 0.45 eV` à `90 % CL`, aucune détection positive | `Sigma m_nu < 0.0642 eV` à `95 %` sous `LambdaCDM`, posterior à la frontière | aucune détection ; `T_1/2^0nu > 3.8 x 10^26 yr` pour `136Xe`, conversions de masse conditionnelles |
| type d'information | relationnelle et différentielle | ancrage local quadratique | reconstruction globale linéaire | test de violation du nombre leptonique et amplitude cohérente conditionnelle |
| dépendance dominante | cadre à trois saveurs, effets de matière, interactions neutrino–noyau, corrélations globales | modèle moléculaire, potentiel, réponse, pertes et frontière statistique | modèle cosmologique, histoire thermique, likelihoods CMB/BAO, priors et dégénérescences | fonds rares, efficacité, mécanisme, éléments de matrice nucléaire et phases |
| information structurellement absente | translation commune des `m_i^2`, masse minimale, phases de Majorana | résolution séparée des trois masses, ordre à la sensibilité actuelle, phases | accès local, masses individuelles, phases, indépendance du modèle | masse simple sans phases, mécanisme identifié par le taux seul, nature Dirac déduite d'une non-détection |
| niveau de reproductibilité | profils globaux publics mais likelihoods expérimentales incomplètes | données et covariances substantielles, événements et codes complets non publics | chaînes et likelihoods nombreuses mais reconstruction totale distribuée | articles détaillés, absence d'une suite commune de likelihoods multi-isotopes |

Cette matrice ne définit pas un classement global de « directness ». Elle distingue :

```text
directness de la trace vers l'observable primaire ;
directness de l'observable vers une fonction de masse ;
longueur de la conversion vers le spectre latent.
```

Ainsi, `N4` peut être expérimentalement direct sur une demi-vie tout en étant très
conditionnel sur `m_beta_beta`. `N2` est local sans être dépourvu de modèle. `N3`
est globalement reconstructif sans être empiriquement arbitraire.

## 3. Carte mathématique commune

### 3.1 Paramètre d'ancrage et ordre

Pour construire un spectre compatible avec `N1`, il faut ajouter une masse légère
`m_l` et un ordre. En notant `Delta m_A^2` la magnitude de l'écart atmosphérique :

#### Ordre normal

```math
m_1=m_l,
\qquad
m_2=\sqrt{m_l^2+\Delta m_{21}^2},
\qquad
m_3=\sqrt{m_l^2+\Delta m_A^2}.
```

#### Ordre inversé

```math
m_3=m_l,
\qquad
m_1=\sqrt{m_l^2+\Delta m_A^2},
\qquad
m_2=\sqrt{m_l^2+\Delta m_A^2+\Delta m_{21}^2}.
```

Les conventions exactes sur `Delta m_3l^2`, `Delta m_ee^2` et `Delta m_mumu^2`
doivent être raccordées avant tout calcul numérique fin.

### 3.2 Fonctions dérivées

Une fois le spectre et les éléments PMNS déclarés :

```math
m_\beta^2=\sum_i |U_{ei}|^2m_i^2,
```

```math
\Sigma m_\nu=\sum_i m_i,
```

```math
m_{\beta\beta}=\left|\sum_i U_{ei}^2m_i\right|.
```

Les deux premières fonctions ne dépendent pas des phases de Majorana. La troisième
en dépend et ne devient une observable de double bêta qu'après ajout du mécanisme
et des éléments de matrice nucléaire.

### 3.3 Planchers issus des oscillations

Sous trois états actifs et les écarts de `N1`, les planchers approximatifs sont :

```text
ordre normal : Sigma m_nu voisin ou supérieur à 0.059 eV ;
ordre inversé : Sigma m_nu voisin ou supérieur à 0.10 eV.
```

Ces planchers ne sont pas des mesures cosmologiques. Ils sont les minima cinématiques
du modèle spectral informé par les oscillations.

## 4. Table des conversions légitimes

| Départ | Information à ajouter | Sortie recevable | Raccourci interdit |
|---|---|---|---|
| `Delta m^2`, PMNS | ordre + `m_l` | spectre `m_i`, puis `m_beta` et `Sigma m_nu` | déduire une masse absolue des seuls écarts |
| `Delta m^2`, PMNS | ordre + `m_l` + phases Majorana | bande de `m_beta_beta` | traiter `delta_CP` comme phase de Majorana |
| borne sur `m_beta` | N1 + ordre + modèle à trois états | région admissible de `m_l` et `Sigma m_nu` | attribuer séparément `m_1`, `m_2`, `m_3` |
| borne sur `Sigma m_nu` | cosmologie, histoire thermique, N1, ordre ou marginalisation | région de `m_l` et prédiction conditionnelle de `m_beta` | présenter la borne comme pesée locale ou indépendante du modèle |
| demi-vie `T_1/2^0nu` | mécanisme + `G^0nu` + `M^0nu` + `g_A` | borne conditionnelle sur `m_beta_beta` | comparer directement les demi-vies de plusieurs isotopes comme masses |
| borne sur `m_beta_beta` | N1 + nature Majorana + phases + mécanisme | régions du spectre compatibles | inverser vers une masse unique sans dégénérescences |
| combinaison des quatre voies | likelihoods, statistiques et dépendances communes explicitement reconstruites | ajustement joint du spectre et des hypothèses | multiplier des bornes ou convertir leurs pourcentages par simple équivalence |

## 5. Compatibilités par paire à la coupure

Les qualifications suivantes distinguent :

```text
compatibilité empirique : aucun résultat primaire ne s'exclut directement ;
compatibilité sous modèle : les résultats peuvent être décrits par un spectre commun
                            avec les hypothèses déclarées ;
tension conditionnelle : une combinaison donnée préfère une région difficilement
                          compatible avec une autre sous le même modèle ;
contradiction : aucune région commune après propagation fidèle des incertitudes et
                hypothèses — situation non établie à la coupure.
```

### 5.1 N1 — N2 : compatibilité, faible recouvrement de sensibilité

`N1` fixe les écarts et les poids électroniques. `N2` limite l'ancrage quadratique à
`m_beta < 0.45 eV`. La région de faibles masses permise par les oscillations reste
largement sous la sensibilité actuelle de KATRIN.

```text
verdict : compatible ;
gain : N1 transforme m_beta en contrainte sur m_l sous ordre déclaré ;
limite : N2 ne distingue pas l'ordre et ne teste pas encore les planchers de N1.
```

Une future détection cinématique élevée serait un test indépendant majeur, mais le
résultat actuel ne sélectionne aucune portion basse du spectre.

### 5.2 N1 — N3 : tension forte mais conditionnelle à LambdaCDM

Sous `LambdaCDM`, trois masses dégénérées et le prior `Sigma m_nu >= 0`, DESI DR2
BAO + CMB donne :

```text
borne bayésienne : Sigma m_nu < 0.0642 eV à 95 % ;
construction Feldman–Cousins : Sigma m_nu < 0.053 eV à 95 %.
```

La seconde passe sous le plancher normal approximatif de `N1`. Le posterior de la
première est comprimé contre sa frontière. Cette situation constitue une tension
du réseau, non une réfutation directe des oscillations.

Sous `w_0w_aCDM`, la borne devient `0.163 eV` et la tension disparaît. La localisation
prioritaire du désaccord est donc :

```text
likelihoods CMB et BAO
+ modèle d'expansion
+ prior et paramétrisation de masse
+ histoire thermique du secteur neutrino,
```

avant toute révision de l'architecture différentielle fortement étayée par `N1`.

Une analyse indépendante publiée en juin 2026 revendique une évidence décisive pour
l'ordre normal sous cosmologie standard. Elle réanalyse essentiellement le même
réseau DESI–CMB–oscillations ; elle constitue un stress test de sélection de modèle,
non un cinquième accès indépendant.

```text
verdict : tension conditionnelle forte sous LambdaCDM ;
          pas de contradiction modèle-indépendante ;
conséquence : l'ordre inversé est fortement défavorisé dans le modèle de base,
              mais non éliminé par N1 seul ni sous toutes les extensions.
```

### 5.3 N1 — N4 : compatibilité, nature et phases non identifiées

Les non-détections de `N4` sont compatibles avec les deux ordres. Même pour des
neutrinos de Majorana, `m_beta_beta` peut être réduit par les phases et la masse
minimale. Les conversions nucléaires actuelles ne fournissent pas une exclusion
robuste de tout le domaine inversé pour tous les calculs.

```text
verdict : compatible ;
gain : N1 fournit les modules PMNS et les écarts nécessaires aux bandes de masse ;
limite : phases Majorana, mécanisme et NME restent absents.
```

### 5.4 N2 — N3 : compatibilité et hiérarchie de portée

La région privilégiée par `N3` sous `LambdaCDM` implique un `m_beta` très inférieur
à la borne actuelle de KATRIN. `N2` ne confirme donc pas numériquement la borne
cosmologique ; il lui reste simplement compatible dans une région beaucoup plus
large.

```text
verdict : compatible, sans validation croisée actuelle ;
N2 : local, moins dépendant de la cosmologie, sensibilité plus faible ;
N3 : beaucoup plus serré, dépendance globale plus forte.
```

Une future mesure positive de `m_beta` dans une région incompatible avec toutes les
extensions cosmologiques raisonnables obligerait à examiner :

```text
modèle spectral KATRIN ;
états additionnels ou interactions nouvelles ;
histoire thermique, stabilité ou abondance cosmologique des neutrinos ;
modèle cosmologique et systématiques des sondes.
```

### 5.5 N2 — N4 : compatibilité sans conversion unique

`m_beta` est une somme incohérente ; `m_beta_beta` est une somme cohérente. Une borne
sur la première limite l'échelle globale mais ne fixe pas les annulations de la
seconde.

```text
verdict : compatible ;
gain : une future détection de m_beta resserrerait l'enveloppe maximale de m_beta_beta ;
limite : phases, nature Majorana, mécanisme et NME empêchent une prédiction unique.
```

### 5.6 N3 — N4 : compatibilité, forte dépendance du pont

Une faible `Sigma m_nu` réduit les bandes possibles de `m_beta_beta` sous trois états
standards, surtout si l'ordre normal est retenu. Les non-détections actuelles de
`N4` restent compatibles avec cette région basse.

Le pont cumule toutefois :

```text
modèle cosmologique
+ histoire thermique
+ ordre et masse minimale
+ phases Majorana
+ mécanisme 0nu beta beta
+ matrices nucléaires.
```

```text
verdict : compatible ;
conséquence : aucune non-détection actuelle ne confirme la borne cosmologique ;
              aucune tension cosmologique ne peut exclure directement un futur
              signal nucléaire de mécanisme non standard.
```

## 6. Carte synthétique de compatibilité

| Paire | Statut à la coupure | Information commune | Principal obstacle |
|---|---|---|---|
| N1–N2 | compatible | spectre à trois masses et poids électroniques | sensibilité cinématique encore trop haute |
| N1–N3 | tension conditionnelle sous `LambdaCDM` | planchers de somme et ordre | modèle cosmologique, frontière et priors |
| N1–N4 | compatible | PMNS, écarts et bandes sous phases | Majorana, phases, mécanisme et NME |
| N2–N3 | compatible sans validation croisée | ancrage absolu du même spectre | portées et modèles très différents |
| N2–N4 | compatible | échelle de masse électronique | cohérence de phase et physique nucléaire |
| N3–N4 | compatible sous pont long | spectre et somme sous modèle | cosmologie + phases + mécanisme + NME |

Aucune paire n'établit une contradiction modèle-indépendante à la coupure. La seule
tension quantitativement saillante est `N1–N3` sous la combinaison cosmologique de
base.

## 7. Hiérarchie des informations, non hiérarchie des expériences

Les quatre voies ordonnent l'information selon des dimensions différentes :

| Information | N1 | N2 | N3 | N4 |
|---|---:|---:|---:|---:|
| écarts de masses | directe dans le modèle d'oscillation | importée | importée pour les planchers | importée pour les bandes |
| orientation PMNS | contrainte | importée pour interprétation | peu déterminante pour l'effet total | importée et phases supplémentaires requises |
| masse minimale | absente | bornée faiblement sous N1 | bornée fortement sous cosmologie déclarée | dégénérée avec phases et mécanisme |
| somme des masses | non déterminée | dérivable sous spectre | cible principale | importée pour construire des enveloppes |
| phases Majorana | absentes | absentes | absentes | déterminantes mais non identifiées |
| nature Majorana | non testée | non testée | non testée | testable par détection, non tranchée par non-détection |
| histoire thermique | sans rôle | sans rôle | hypothèse centrale | sans rôle dans la demi-vie, ajoutée dans le pont N3–N4 |
| matrice nucléaire | sans rôle | sans rôle | sans rôle | hypothèse centrale de conversion |

La voie la plus précise numériquement n'est donc pas supérieure sur toutes les
questions. `N3` contraint fortement la somme mais ne teste pas Majorana. `N4` teste
potentiellement une violation du nombre leptonique mais ne donne pas une masse sans
physique nucléaire. `N1` établit les relations les plus robustes mais laisse libre
l'ancrage. `N2` fournit l'accès local le moins dépendant de la cosmologie, à une
sensibilité encore insuffisante pour la région basse.

## 8. Protocole de localisation d'un désaccord futur

### 8.1 Désaccord interne à une voie

Avant toute nouvelle physique, contrôler :

```text
données et sélection ;
calibration et réponse ;
modèle de fond ;
corrélations et paramètres de nuisance ;
construction statistique ;
version et datation de l'analyse.
```

### 8.2 Désaccord N1 — N2

Ordre de contrôle :

```text
modèle spectral et réponse KATRIN ;
conventions et paramètres PMNS importés ;
composantes spectrales additionnelles ;
non-unitarité, états stériles ou interactions générales.
```

### 8.3 Désaccord N1 — N3 ou N2 — N3

Ordre de contrôle :

```text
likelihoods CMB, lentillage et BAO ;
choix des données et covariances ;
priors et paramétrisation de masse ;
modèle d'énergie noire, courbure et gravitation ;
histoire thermique, stabilité et interactions des neutrinos ;
secteur à trois états et résultats locaux.
```

Le modèle cosmologique doit être testé avant de convertir une tension en propriété
intrinsèque du neutrino.

### 8.4 Désaccord impliquant N4

Ordre de contrôle :

```text
signification statistique et stabilité du signal ;
fonds, calibration et confirmation dans un autre isotope ;
mécanisme dominant ;
éléments de matrice nucléaire et g_A ;
phases et spectre fourni par N1–N3 ;
opérateurs ou particules au-delà du mécanisme léger.
```

Une détection `0nu beta beta` incompatible avec les bandes standard ne réfuterait pas
immédiatement la cosmologie ou KATRIN : elle pourrait identifier un mécanisme de
violation du nombre leptonique différent de l'échange léger.

## 9. Révision de la thèse du cycle 3

### 9.1 Formulation ancienne devenue trop lâche

```text
plusieurs accès à la masse absolue des neutrinos.
```

Cette formule suggère un nombre commun déjà isolé. Elle est remplacée par :

```text
plusieurs fonctions non équivalentes d'un spectre de masses,
coordonnées par un modèle commun et des hypothèses propres à chaque voie.
```

### 9.2 Résultat scientifique révisé

Le cycle établit :

1. une architecture différentielle robuste par oscillations ;
2. trois ancrages non équivalents — quadratique, linéaire et cohérent conditionnel ;
3. une différence entre observable primaire et grandeur convertie ;
4. une compatibilité générale des voies à la coupure ;
5. une tension localisée entre oscillations et cosmologie sous `LambdaCDM` ;
6. l'impossibilité de hiérarchiser les accès par la seule précision numérique ;
7. la nécessité de traiter l'incomplétude comme partie positive du résultat.

### 9.3 Résultat épistémique borné

Le terme commun « neutrino » ne garantit pas l'équivalence des opérations. La
cohérence du secteur repose sur la possibilité de faire circuler l'information par
des ponts physiques contrôlés, tout en conservant les pertes propres à chaque voie.

Cette conclusion ne démontre ni que les opérations constituent l'objet, ni qu'un
objet complet est donné indépendamment de toute médiation. Elle fixe une exigence de
méthode pour l'enquête scientifique.

## 10. Transférabilité du gabarit

### 10.1 Vers le cycle 1 — couplages, échelles et QCD

Le gabarit est transférable pour distinguer :

```text
paramètre renormalisé ;
observable expérimentale ;
échelle et schéma ;
calcul perturbatif ou non perturbatif ;
corrections et extraction ;
conversion entre déterminations.
```

Le gain attendu est comparable : empêcher que plusieurs déterminations de `alpha_s`
ou d'un couplage soient traitées comme lectures directes d'un même nombre sans
raccord d'échelle, de schéma et de régime.

### 10.2 Vers le cycle 7 — cosmologie

Le gabarit est transférable aux chaînes de bout en bout :

```text
signal brut
-> catalogue ou carte
-> observable reconstruite
-> modèle direct
-> likelihood
-> paramètre et tension.
```

`N3` montre cependant que le cycle 7 exige un découpage par sonde et par sous-réseau,
plutôt qu'une fiche globale unique.

### 10.3 Limite de la transférabilité

Le schéma n'est pas une théorie générale de la mesure. Il est utile lorsque :

```text
plusieurs opérations contraignent un même secteur ;
les fonctions ciblées sont distinctes ;
les conversions exigent des hypothèses identifiables ;
les désaccords peuvent être localisés dans une chaîne.
```

Il doit être modifié si ces conditions ne sont pas réunies.

## 11. Dettes résiduelles

### 11.1 Dette computationnelle

- extraire et comparer les profils numériques exacts de NuFIT 6.1 ;
- convertir rigoureusement `Delta m_ee^2`, `Delta m_mumu^2` et `Delta m_3l^2` ;
- reproduire le profil KATRIN depuis les données et covariances publiques ;
- reproduire les quantiles et maxima DESI pour plusieurs priors de masse ;
- construire des bandes communes `m_l`, `m_beta`, `Sigma m_nu`, `m_beta_beta` ;
- combiner plusieurs isotopes avec un ensemble cohérent de NME et leurs corrélations.

### 11.2 Dette documentaire

- conserver une table de versions et de dates des données pour chaque résultat ;
- vérifier la disponibilité réelle des likelihoods et chaînes ;
- distinguer article de collaboration, produit de données et analyse indépendante ;
- réviser la matrice à chaque nouveau résultat directeur, sans écraser l'état antérieur.

### 11.3 Dette scientifique ouverte

- ordre des masses ;
- violation de CP leptoniqe ;
- masse minimale et détection positive ;
- nature Dirac ou Majorana ;
- mécanisme de génération des masses ;
- origine de la tension cosmologique sous `LambdaCDM` ;
- validité exhaustive du cadre à trois états actifs.

## 12. Critères de clôture et de réouverture

`N5` est close comme comparaison documentaire et scientifique lorsque :

```text
les quatre fonctions sont séparées ;
les observables primaires sont distinguées des conversions ;
les hypothèses de chaque pont sont explicites ;
les compatibilités par paire sont qualifiées ;
la tension N1–N3 est localisée sans verdict excessif ;
les dettes computationnelles sont conservées.
```

La matrice doit être rouverte si :

```text
KATRIN publie une nouvelle analyse standard de masse ;
DESI, ACT, Planck ou une nouvelle sonde modifie l'état directeur de Sigma m_nu ;
une expérience 0nu beta beta rapporte un signal ou une limite changeant les bandes ;
les oscillations tranchent l'ordre, l'octant ou CP à un niveau robuste ;
un calcul nucléaire coordonné modifie fortement les conversions ;
une reproduction numérique révèle une incompatibilité absente des publications.
```

## 13. Verdict N5

```text
objet commun minimal : spectre de trois masses et mélange sous cadre déclaré ;
N1 : architecture différentielle ;
N2 : ancrage quadratique électronique local ;
N3 : somme collective reconstruite cosmologiquement ;
N4 : demi-vie isotopique et amplitude cohérente conditionnelle ;
compatibilité générale : oui, à la coupure ;
tension principale : N1–N3 sous LambdaCDM et traitement de frontière ;
contradiction modèle-indépendante : aucune établie ;
acquis du cycle : plusieurs accès non équivalents peuvent éprouver un même secteur
                  seulement par des ponts explicites qui conservent leurs pertes ;
transférabilité : confirmée vers les architectures d'extraction du cycle 1 et les
                  chaînes reconstructives du cycle 7, sous adaptation locale ;
statut : dette scientifique prioritaire du cycle 3 levée au niveau documentaire,
         empirique et comparatif ; dettes computationnelles conservées.
```

La prochaine opération n'est plus une cinquième fiche d'accès. Elle consiste à
stabiliser la synthèse active du cycle 3, puis à décider si le chantier prioritaire
suivant est le cycle 1 ou une reprise computationnelle ciblée de la tension `N1–N3`.
