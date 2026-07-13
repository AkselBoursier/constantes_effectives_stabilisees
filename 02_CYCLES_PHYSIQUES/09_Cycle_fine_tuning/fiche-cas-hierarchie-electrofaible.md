# Fiche de cas — hiérarchie électrofaible

## Statut

Cette fiche instruit le premier cas du cycle fine-tuning.

Elle distingue trois questions souvent réunies :

1. la sensibilité technique du paramètre de masse du Higgs à une physique ultraviolette ;
2. la petitesse relative de l'échelle électrofaible ;
3. la nécessité environnementale d'une interaction faible proche de celle de notre univers.

Aucune de ces questions ne doit être tenue pour équivalente aux deux autres.

## 1. Thèse auditée

Formulation courante :

> L'échelle électrofaible est extraordinairement petite par rapport aux échelles de grande unification ou de Planck ; le paramètre du Higgs doit donc être réglé avec une précision extrême.

Formulation environnementale :

> Une variation importante de l'échelle électrofaible empêcherait l'existence de noyaux, d'atomes ou de structures complexes.

La fiche vérifie séparément ces deux affirmations.

## 2. Objets et statuts

| Objet | Statut dans le cadre |
|---|---|
| paramètre quadratique du potentiel du Higgs | paramètre de théorie, dépendant de la convention et du schéma de renormalisation |
| couplage quartique `lambda` | couplage courant dépendant de l'échelle |
| valeur moyenne `v` | grandeur dérivée dans le régime électrofaible brisé |
| masse physique du Higgs `m_h` | observable de pôle, reliée aux paramètres renormalisés et aux corrections |
| matrices de Yukawa `Y_f` | couplages courants sans dimension |
| masses fermioniques | grandeurs dérivées de `Y_f`, `v`, de l'échelle et du schéma |
| `Lambda_QCD` | échelle dynamique produite par le flot de renormalisation |
| échelle ultraviolette `M` | seuil ou échelle d'une théorie plus complète, non observable unique universelle |

Première correction :

```text
v n'est pas un cadran indépendant des paramètres du potentiel.
les masses fermioniques ne sont pas indépendantes de v et des Yukawa.
```

## 3. Relations au niveau arbre

Avec une convention simple :

```text
V(H) = -m^2 H†H + lambda (H†H)^2
```

le minimum brisé donne :

```text
v^2 = m^2 / lambda
```

et :

```text
m_h^2 = 2 lambda v^2
M_f = Y_f v / sqrt(2)
M_W = g v / 2
M_Z = v sqrt(g^2 + g'^2) / 2
```

Ces relations montrent que plusieurs valeurs invoquées dans les narrations du fine-tuning appartiennent à une même architecture de dépendances.

Elles ne disent pas pourquoi `m^2`, `lambda`, les Yukawa ou les seuils ultraviolets possèdent leurs valeurs.

## 4. Trois protocoles de variation

### 4.1 Variation technique ultraviolette

On suppose une théorie contenant le Higgs et des états lourds couplés à lui. On étudie la sensibilité du paramètre de masse basse énergie aux paramètres et seuils de la théorie ultraviolette.

Question :

> Des contributions physiquement distinctes doivent-elles se compenser pour produire la valeur électrofaible observée ?

Ce protocole dépend du contenu de la théorie au-dessus du Modèle standard. Sans spécification de seuils lourds et de leurs couplages, la taille physique du réglage n'est pas entièrement déterminée.

### 4.2 Variation environnementale à un paramètre

On varie le paramètre de masse du Higgs, en maintenant notamment certains couplages sans dimension et l'échelle QCD selon le protocole choisi.

La variation de `v` modifie alors corrélativement :

```text
m_f ∝ y_f v
M_W ∝ g v
M_Z ∝ sqrt(g^2 + g'^2) v
```

Les différences de masses nucléoniques, les désintégrations bêta et la stabilité nucléaire peuvent être affectées.

Ce protocole teste une direction particulière de l'espace des paramètres. Il ne prouve pas que cette direction est la seule physiquement réalisable.

### 4.3 Variation corrélée

On autorise plusieurs paramètres cosmologiques et microscopiques à varier ensemble afin de maintenir certaines structures : chimie, nucléosynthèse, étoiles ou abondances.

Le cas d'un univers sans interaction faible montre qu'une variation multiparamétrique peut ouvrir des trajectoires très différentes de celles obtenues en tournant un seul cadran.

Ce protocole soulève une question supplémentaire :

> La corrélation est-elle produite par une théorie ou seulement choisie pour construire un contre-exemple viable ?

## 5. Sensibilité et paramétrisation

Une mesure locale classique peut prendre la forme :

```text
Delta_i = |∂ ln O / ∂ ln p_i|
```

Elle dépend de :

- l'observable `O` ;
- la liste des paramètres `p_i` ;
- la distinction entre paramètres indépendants et liés ;
- l'échelle de référence ;
- la théorie ultraviolette ;
- la paramétrisation.

Une grande valeur de `Delta_i` peut signaler une carte fortement étirée entre paramètres et observable. Elle ne fournit pas, seule, la probabilité que le monde réalise cette région.

## 6. Quadraticité et seuils physiques

Le langage des divergences quadratiques est dépendant du régulateur et de la formulation. La question physique la plus robuste est la sensibilité du paramètre du Higgs à des seuils lourds réellement couplés au secteur scalaire.

Schéma de lecture :

```text
état lourd de masse M
+ couplage au Higgs
-> correction de seuil au paramètre quadratique
-> sensibilité éventuelle de v à M
```

Si aucun état lourd pertinent n'est spécifié, l'inférence directe depuis l'échelle de Planck vers une compensation numérique précise doit rester prudente.

Inversement, la dépendance de la formulation ne suffit pas à prouver que tout problème de hiérarchie est un artefact : une théorie ultraviolette concrète peut produire des corrections de seuil physiquement significatives.

## 7. Ce que le mécanisme de Higgs explique

Le secteur Higgs–Yukawa explique structurellement :

- comment les masses des bosons faibles sont compatibles avec la structure de jauge ;
- comment les termes de masse fermionique apparaissent après le choix du vide ;
- comment masses et mélanges sont reliés aux matrices de Yukawa.

Il n'explique pas :

- pourquoi le paramètre quadratique prend sa valeur ;
- pourquoi `lambda` possède sa valeur ;
- pourquoi les Yukawa ont leurs textures ;
- pourquoi l'échelle électrofaible se situe là relativement à une éventuelle échelle ultraviolette.

Le mécanisme réduit donc la contingence apparente des masses comme liste indépendante, mais laisse une contingence du secteur générateur.

## 8. Contrefactuels

### 8.1 Si `v = 0`

Dans la phase symétrique :

- les bosons faibles n'obtiennent pas leurs masses par ce mécanisme ;
- les fermions chargés n'obtiennent pas les termes de masse standards ;
- la structure basse énergie de notre monde n'est pas reproduite.

### 8.2 Si `v` augmente avec Yukawa fixes

Les masses fermioniques et faibles augmentent ensemble, tandis que `Lambda_QCD` peut être tenue fixe dans le protocole. Les rapports entre échelle électrofaible, masses des quarks légers et physique nucléaire changent.

### 8.3 Si `v` augmente avec Yukawa ajustés

Certaines masses fermioniques peuvent être maintenues, mais la force et la portée des processus faibles changent. Le résultat environnemental n'est pas le même que dans le protocole précédent.

### 8.4 Si les seuils lourds sont absents ou découplés

La sensibilité technique à ces seuils disparaît ou diminue. Le problème de hiérarchie dépend donc de la théorie plus complète et de ses couplages, pas seulement du lagrangien basse énergie isolé.

## 9. Lecture des résultats existants

Les analyses environnementales à variation restreinte trouvent une fenêtre où la physique nucléaire analogue à la nôtre reste possible lorsque l'échelle faible varie relativement à QCD.

Le contre-exemple de l'univers sans interaction faible montre toutefois que la nécessité anthropique d'une échelle faible proche de la nôtre n'est pas établie sans préciser l'ensemble des paramètres autorisés à varier.

Il faut donc distinguer :

```text
fenêtre étroite dans une coupe de l'espace des paramètres
≠
région étroite dans l'espace physique complet des possibilités
```

## 10. Réponse anthropique

Le principe anthropique faible peut conditionner l'observation à l'existence de structures nucléaires ou chimiques dans un ensemble où le paramètre du Higgs varie.

Mais l'argument exige :

- que cette variation soit physiquement réalisée ;
- une distribution sur les valeurs ;
- les corrélations avec les Yukawa, QCD et les paramètres cosmologiques ;
- un critère de sélection.

La seule existence d'une fenêtre environnementale ne fournit pas ces éléments.

## 11. Contingence résiduelle

Après reconstruction, plusieurs questions restent ouvertes :

1. structure ultraviolette du secteur scalaire ;
2. valeur du paramètre quadratique ;
3. présence et couplage de seuils lourds ;
4. distribution éventuelle des paramètres entre domaines ;
5. corrélations entre le secteur Higgs, les Yukawa et QCD.

La contingence n'est pas supprimée. Elle est localisée.

## 12. Verdict provisoire

| Dimension | Verdict |
|---|---|
| masses comme cadrans indépendants | largement dissous par l'architecture Higgs–Yukawa |
| sensibilité du Higgs à des seuils lourds | problème réel dans une théorie ultraviolette spécifiée |
| nombre universel de fine-tuning | non établi sans choix de paramètres, échelle et mesure |
| nécessité anthropique de notre échelle faible | affaiblie par les variations corrélées et le contre-exemple weakless |
| origine de l'échelle électrofaible | contingence résiduelle ouverte |

Formule provisoire :

> La hiérarchie électrofaible n'est ni un simple artefact verbal ni un réglage probabiliste déjà quantifié. Elle désigne un ensemble de sensibilités dont le contenu physique dépend de la théorie ultraviolette, tandis que son interprétation anthropique dépend du protocole de variation et des corrélations admises.

## 13. Sources

- G. F. Giudice, *Naturally Speaking: The Naturalness Criterion and Physics at the LHC*, arXiv:0801.2562.
- Joshua Rosaler et Robert Harlander, *Naturalness, Wilsonian Renormalization, and "Fundamental Parameters" in Quantum Field Theory*, arXiv:1809.09489.
- V. Agrawal, S. M. Barr, John F. Donoghue et D. Seckel, *Anthropic considerations in multiple domain theories and the scale of electroweak symmetry breaking*, arXiv:hep-ph/9801253.
- Roni Harnik, Graham D. Kribs et Gilad Perez, *A Universe Without Weak Interactions*, arXiv:hep-ph/0604027.
- Fred C. Adams, *The Degree of Fine-Tuning in our Universe — and Others*, arXiv:1902.03928.
