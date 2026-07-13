# Test des cinq cas sentinelles

## Statut

Ce document applique le critère provisoire de constance à cinq objets choisis pour leur pouvoir de discrimination.

Il ne cherche pas à produire une taxonomie complète. Il vérifie si le cadre sait :

- admettre une constance relative lorsqu’elle est justifiée ;
- refuser le qualificatif de constante lorsque l’objet est un paramètre d’état, une fonction courante ou une borne ;
- distinguer propriété physique, statut métrologique et robustesse de l’accès.

Notation de travail :

```text
C(g | R, T, epsilon)
```

`g` est tenue pour constante relativement à un régime `R`, à des transformations ou variables pertinentes `T`, et à une tolérance ou un niveau de contrôle `epsilon`.

## 1. Sources de contrôle

1. BIPM, *SI defining constants* :
   <https://www.bipm.org/en/measurement-units/si-defining-constants>
2. Particle Data Group, *Quantum Chromodynamics*, mise à jour 2025 :
   <https://pdg.lbl.gov/2025/reviews/rpp2025-rev-qcd.pdf>
3. Particle Data Group, *Cosmological Parameters*, mise à jour 2025 :
   <https://pdg.lbl.gov/2025/reviews/rpp2025-rev-cosmological-parameters.pdf>
4. Particle Data Group, *Electroweak Model and Constraints on New Physics*, mise à jour 2025–2026 :
   <https://pdg.lbl.gov/2025/reviews/rpp2025-rev-standard-model.pdf>
5. Particle Data Group, *Status of Higgs Boson Physics*, mise à jour 2025 :
   <https://pdg.lbl.gov/2025/reviews/rpp2025-rev-higgs-boson.pdf>
6. Particle Data Group, *Neutrino Masses, Mixing, and Oscillations*, édition 2024 :
   <https://pdg.lbl.gov/2024/reviews/rpp2024-rev-neutrino-mixing.pdf>

## 2. Cas 1 — `G_F`

### Objet exact

`G_F` est le coefficient de Fermi déterminé notamment à partir de la durée de vie du muon et utilisé dans la description effective des interactions faibles à basse énergie.

Au niveau arbre :

```math
\frac{G_F}{\sqrt 2}=\frac{g^2}{8m_W^2}=\frac{1}{2v^2}.
```

### Régime

```text
E << M_W
```

Dans ce domaine, le propagateur du boson `W` n’est pas résolu explicitement et son effet dominant est condensé dans une interaction locale à quatre fermions.

### Transformations ou variations pertinentes

- variation de la cinématique à l’intérieur du domaine basse énergie ;
- comparaison de plusieurs processus faibles décrits par la même théorie effective ;
- changement d’échelle de renormalisation dans un schéma et un ordre perturbatif précisés ;
- ajout des corrections radiatives et des opérateurs d’ordre supérieur.

### Tolérance ou contrôle

La tolérance est déterminée par :

- les incertitudes expérimentales de l’extraction ;
- les corrections radiatives ;
- l’erreur de troncature de la théorie effective ;
- les contributions éventuelles d’opérateurs supplémentaires.

### Décision

```text
Admis comme constante effective dans un régime spécifié.
```

### Justification

`G_F` exerce une fonction de raccordement : il permet de traiter comme fixe le coefficient dominant de l’interaction faible locale lorsque les énergies restent très inférieures à `M_W`.

Sa constance n’est ni universelle sans condition ni fondamentale au sens d’un paramètre ultime. Elle dépend du domaine d’effectivité, de la base d’opérateurs, du schéma et de l’ordre de calcul.

### Statut de l’accès

`G_F` est extrait d’un observable, principalement la durée de vie du muon, à travers une théorie incluant les corrections pertinentes. La précision de cette extraction renforce le statut inférentiel du coefficient ; elle ne crée pas son domaine de validité.

### Condition d’échec

Le qualificatif devient insuffisant lorsque :

- l’énergie approche l’échelle du `W` ;
- la structure du propagateur doit être résolue ;
- des opérateurs nouveaux contribuent de manière non négligeable ;
- le coefficient est cité sans préciser le cadre effectif.

### Forme du critère

```text
C(G_F | E << M_W, cinématique basse énergie, erreurs EFT + radiatives)
```

## 3. Cas 2 — `h` dans le SI

### Objet exact

La constante de Planck `h` joue un rôle physique dans les relations quantiques et possède, dans le SI, la valeur numérique exacte :

```math
h=6.626\,070\,15\times10^{-34}\ \mathrm{J\,s}.
```

### Régime

Deux régimes doivent être distingués :

1. le rôle physique de `h` dans les théories quantiques ;
2. son statut de constante définissante dans le Système international d’unités.

### Transformations ou variations pertinentes

Pour le statut métrologique :

- changement de réalisation pratique des unités ;
- reproduction des unités dans différents laboratoires ;
- changement de mesure d’une grandeur dérivée.

Pour le rôle physique :

- changement de système d’unités ;
- changement de représentation ;
- tests éventuels d’une variation de rapports sans dimension auxquels `h` participe.

### Tolérance ou contrôle

Dans le SI, la valeur numérique définissante est exacte et ne porte pas d’incertitude.

Les réalisations concrètes des unités, elles, possèdent des incertitudes. L’exactitude de la valeur numérique ne supprime donc ni l’incertitude expérimentale ni la dépendance de la valeur numérique à un système d’unités.

### Décision

```text
Admis comme constante métrologique définissante.
```

Son rôle physique doit être distingué de son exactitude numérique dans le SI.

### Justification

Depuis la redéfinition du SI, la valeur numérique de `h` est fixée par définition et sert à définir le kilogramme avec les autres constantes du système.

Cette exactitude ne démontre pas empiriquement que `h` serait une valeur mesurée avec une précision infinie. Elle résulte du choix métrologique de fixer sa valeur numérique.

### Statut de l’accès

Avant sa fixation, `h` faisait l’objet de déterminations expérimentales avec incertitude. Dans le SI actuel, les expériences réalisent les unités à partir de la valeur définissante ; elles ne ré-estiment pas cette valeur numérique comme une grandeur incertaine du système.

### Condition d’échec

La confusion apparaît si l’on conclut :

```text
valeur numérique exacte dans le SI
=
invariance physique démontrée sans hypothèse
=
réalisation expérimentale sans incertitude.
```

Ces trois propositions sont distinctes.

### Forme du critère

```text
C_met(h | définition du SI, réalisations équivalentes, exactitude définitionnelle)
```

## 4. Cas 3 — `alpha_s(Q)`

### Objet exact

`alpha_s(\mu)` est le couplage fort renormalisé à une échelle `\mu` dans un schéma donné, généralement `\overline{MS}`.

Son évolution est régie par :

```math
\mu^2\frac{d\alpha_s}{d\mu^2}=\beta(\alpha_s).
```

### Régime

Le domaine perturbatif de la QCD, avec :

```text
mu suffisamment supérieur à Lambda_QCD.
```

### Transformations ou variations pertinentes

- changement de l’échelle de renormalisation `\mu` ;
- changement du schéma de renormalisation ;
- franchissement des seuils de masse des quarks ;
- changement d’ordre perturbatif.

### Tolérance ou contrôle

La précision dépend :

- de l’ordre perturbatif ;
- de l’incertitude sur l’échelle ;
- du schéma ;
- des corrections non perturbatives ;
- des raccordements aux seuils.

### Décision

```text
Refusé comme constante simpliciter.
```

Une valeur telle que :

```text
alpha_s(M_Z) dans le schéma MS-bar
```

peut être utilisée comme paramètre de référence, mais la fonction `alpha_s(\mu)` varie précisément avec l’échelle.

### Justification

La dépendance d’échelle n’est pas une imperfection de mesure ; elle appartient à la structure de la théorie quantique renormalisée. La traiter comme une constante indépendante de `\mu` supprimerait une propriété physique centrale : la liberté asymptotique et le changement de régime de la QCD.

### Statut de l’accès

Les différentes déterminations expérimentales sont transportées à une échelle de référence commune à l’aide du groupe de renormalisation avant comparaison ou combinaison.

La stabilité des valeurs ramenées à `M_Z` teste la cohérence de la QCD ; elle ne rend pas `alpha_s(Q)` constante en `Q`.

### Condition d’échec

Le qualificatif de constante est rejeté si :

- l’échelle n’est pas indiquée ;
- le schéma est omis lorsque sa précision est pertinente ;
- la trajectoire de renormalisation est remplacée par un nombre unique universel.

### Forme du critère

```text
non-C(alpha_s(mu) | variation de mu)
```

On peut seulement écrire :

```text
C(alpha_s(mu_0) | mu = mu_0, schéma et ordre fixés, incertitudes déclarées)
```

mais cette constance locale est celle d’une valeur spécifiée, non de la fonction entière.

## 5. Cas 4 — `H_0`

### Objet exact

`H_0` est la valeur actuelle du paramètre de Hubble :

```math
H_0=H(t_0).
```

Le paramètre de Hubble est défini par :

```math
H(t)=\frac{\dot a(t)}{a(t)}.
```

### Régime

Le régime cosmologique homogène et isotrope décrit par un modèle de type FLRW, à l’époque présente `t_0`.

### Transformations ou variations pertinentes

- évolution temporelle ou en décalage spectral ;
- changement du modèle cosmologique utilisé pour relier les observables à `H_0` ;
- changement des jeux de données et des calibrations ;
- choix de paramétrisation et d’hypothèses sur la géométrie ou le contenu cosmique.

### Tolérance ou contrôle

La précision dépend :

- des incertitudes instrumentales et astrophysiques ;
- des calibrations ;
- des hypothèses de modèle ;
- des corrélations avec les autres paramètres cosmologiques.

### Décision

```text
Refusé comme constante physique du noyau.
```

`H_0` est un paramètre d’état actuel : la valeur à l’époque présente d’une grandeur dynamique.

### Justification

Le fait que le symbole porte historiquement le nom de « constante de Hubble » ne change pas son statut. `H(t)` évolue au cours de l’histoire cosmique ; `H_0` sélectionne un instant particulier.

Il peut être fixé dans un ajustement ou estimé de manière robuste sans devenir un invariant nomologique universel.

### Statut de l’accès

`H_0` est reconstruit par plusieurs voies : échelle des distances, lentilles temporelles, ondes gravitationnelles, anisotropies cosmologiques combinées à un modèle, etc.

La concordance ou la tension entre ces voies concerne la robustesse de l’inférence et la suffisance des modèles. Elle ne constitue pas une formation ou une variation de la constante elle-même.

### Condition d’échec

Le classement comme constante échoue dès que l’on considère la transformation :

```text
t_0 -> t
```

puisque :

```math
H(t)\neq H_0
```

en général.

### Forme du critère

```text
non-C(H(t) | variation temporelle)
```

et :

```text
H_0 = valeur d’état à t_0, avec robustesse inférentielle à évaluer séparément.
```

## 6. Cas 5 — borne sur la masse des neutrinos

### Objet exact

Une borne telle que :

```math
\sum_i m_{\nu_i}<B
```

ou :

```math
m_\beta<B
```

est un énoncé de contrainte sur une ou plusieurs grandeurs physiques. Elle n’est pas elle-même une masse de neutrino.

### Régime

Le régime dépend de la voie d’accès :

- oscillations pour les différences de masses au carré ;
- cinématique de désintégration bêta pour `m_\beta` ;
- cosmologie pour `\sum m_\nu` ;
- double bêta sans neutrino pour une masse effective `m_{\beta\beta}`, sous hypothèses supplémentaires.

### Transformations ou variations pertinentes

- changement de jeu de données ;
- changement du modèle cosmologique ;
- changement de hiérarchie ou d’hypothèse sur la nature des neutrinos ;
- changement du niveau de confiance statistique ;
- changement de paramètre effectif considéré.

### Tolérance ou contrôle

Une borne doit toujours être accompagnée :

- d’un niveau de confiance ;
- d’un modèle ;
- d’un jeu de données ;
- d’une définition exacte de la grandeur contrainte ;
- des hypothèses théoriques nécessaires.

### Décision

```text
Refusée comme constante.
```

### Justification

La borne appartient à notre état de connaissance. Elle peut se déplacer lorsque les données, les méthodes ou le modèle changent, sans que la grandeur physique sous-jacente ait nécessairement changé.

Il faut distinguer :

```text
masse ou combinaison de masses
≠
estimation
≠
intervalle
≠
borne.
```

### Statut de l’accès

Les oscillations établissent des différences de masses au carré non nulles mais ne fixent pas l’échelle absolue. Les autres routes contraignent des combinaisons différentes et reposent sur des hypothèses distinctes.

La convergence éventuelle de plusieurs bornes peut renforcer une conclusion sur les masses ; elle ne transforme pas les bornes elles-mêmes en objets physiques constants.

### Condition d’échec

Le cadre échoue s’il classe comme constante :

- une valeur limite ;
- un intervalle de confiance ;
- un résultat dépendant d’un modèle ;
- une projection de sensibilité expérimentale.

### Forme du critère

```text
non-C(borne | changement des données, du modèle ou du niveau de confiance)
```

## 7. Tableau de décision

| Cas | Objet physique ou épistémique | Décision | Fonction locale éventuelle |
|---|---|---|---|
| `G_F` | coefficient effectif | admis relativement au régime basse énergie | raccordement effectif |
| `h` dans le SI | constante physique avec valeur numérique définissante | admis comme constante métrologique | définition et conversion des unités quantiques |
| `alpha_s(\mu)` | couplage courant | refusé comme constante simpliciter | paramètre de la trajectoire RG à une échelle donnée |
| `H_0` | paramètre d’état actuel | refusé du noyau des constantes | caractérisation de l’expansion à l’époque présente |
| borne neutrino | énoncé de contrainte | refusée comme constante | qualification de l’accès |

## 8. Résultat discriminant

Le cadre n’admet pas tous les cas.

```text
2 admissions relatives
3 refus comme constantes simpliciter
```

Cette distribution confirme un pouvoir d’exclusion minimal.

Elle conduit cependant à une correction du cadre :

> La robustesse inférentielle n’est pas un quatrième statut de constance. Elle est un axe auxiliaire portant sur la solidité de l’attribution, de l’estimation ou de la contrainte.

`H_0` et les bornes neutrino peuvent présenter une forte robustesse inférentielle sans devenir des constantes physiques.

## 9. Ce que le test montre sur la fonction de fixité

La fonction de fixité ne suffit pas, à elle seule, à définir une constante.

- `G_F` maintient une relation effective stable dans un domaine contrôlé.
- `h` possède une valeur numérique fixée dans une architecture métrologique.
- `alpha_s(\mu)` organise une trajectoire plutôt qu’une fixité sous variation de l’échelle.
- `H_0` fixe une condition temporelle de référence, non une invariance.
- une borne fixe provisoirement une limite de connaissance, non une propriété de l’objet.

Le terme `fixité` doit donc être qualifié par son porteur et son niveau :

```text
fixité physique
fixité effective
fixité métrologique
fixité procédurale ou inférentielle
```

La dernière ne doit pas être promue automatiquement au rang de constance physique.

## 10. Critère d’entrée révisé

Une grandeur peut entrer dans le noyau si elle satisfait l’un des trois statuts suivants :

1. invariance physique dans un régime et sous des transformations spécifiés ;
2. coefficient effectivement fixe dans une approximation contrôlée ;
3. valeur numérique fixée par définition dans une architecture métrologique, avec distinction du rôle physique.

La robustesse inférentielle devient un axe transversal :

```text
comment savons-nous que l’attribution ou la valeur est robuste ?
```

Elle ne répond pas à la question :

```text
qu’est-ce qui est constant physiquement ?
```

## 11. Conditions générales de refus

Le qualificatif de constante doit être refusé lorsque l’objet est :

- une fonction explicitement variable sous la transformation examinée ;
- une valeur d’état sélectionnée à une époque particulière ;
- une coordonnée dépendante d’une convention sans invariant identifié ;
- une borne, un intervalle ou une tension ;
- un paramètre rendu fixe uniquement par une procédure d’ajustement ;
- une valeur dépourvue du régime, du schéma ou de l’échelle nécessaires à son identification.

## 12. Décision de clôture

```text
Test des cinq cas sentinelles : concluant.
```

Il montre que le cadre peut :

- admettre une constance relative ;
- distinguer exactitude métrologique et invariance physique ;
- refuser un couplage courant comme constante simpliciter ;
- exclure un paramètre d’état et une borne ;
- séparer le statut de l’objet de la robustesse de son accès.

> Le test ne fournit pas encore une définition universelle de la constante physique. Il établit une discipline minimale : aucune fixité numérique, procédurale ou locale ne doit être transformée en constance physique sans préciser l’objet, le régime, les transformations et le niveau auquel la fixité est attribuée.
