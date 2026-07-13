# Dossier pilote — architecture relationnelle Higgs–Yukawa

## Statut

Ce document constitue le dossier central du premier cas expérimental de la refondation.

La phase 1 a extrait et requalifié le corpus interne. La phase 2 a contrôlé les équations, les corrections radiatives, les dépendances d’échelle et de schéma, l’histoire thermique et les invariants de CKM.

Documents de contrôle :

- [verification-physique-higgs-yukawa.md](verification-physique-higgs-yukawa.md)
- [evaluation-gain-explicatif-higgs-yukawa.md](evaluation-gain-explicatif-higgs-yukawa.md)

Le pilote est conclu **sous conditions** : la méthode produit un gain explicatif identifiable, mais elle ne démontre pas encore que la notion de fonction de fixité puisse être généralisée à tous les cycles.

Le secteur neutrino reste hors du noyau initial. Il pourra être réintroduit ultérieurement comme extension distincte, puisque les masses et mélanges neutrino dépassent le Modèle standard minimal.

## 1. Question du pilote

> Que permet de voir une description relationnelle du secteur Higgs–Yukawa que ne montre pas immédiatement la narration selon laquelle « le Higgs donne leur masse aux particules » ?

Cette question est instruite à partir de la question plus générale :

> Qu'est-ce qu'une constante physique lorsqu'on la considère non comme un nombre isolé, mais comme un élément exerçant une fonction de fixité dans une architecture de relations typées ?

Le pilote ne cherche pas à définir définitivement le mot `constante`. Il examine ce que cette question oblige à distinguer dans un domaine physique précis.

## 2. Corpus interne repris

Le noyau documentaire est constitué de :

- la fiche sur la valeur moyenne du champ de Higgs `v` ;
- la fiche sur les matrices et couplages de Yukawa ;
- la fiche CKM ;
- la synthèse du cycle Saveur–Higgs ;
- la note d'architecture Saveur–Higgs ;
- la synthèse du cycle effectif basse énergie pour le raccordement par `G_F`.

Ces documents apportaient déjà :

- la distinction entre échelle électrofaible, couplages, masses et orientations ;
- les relations `M_f = Y_f v / sqrt(2)` et, selon la convention de rotation, `V_CKM = U_{uL}† U_{dL}` ;
- la différence entre paramètres libres, grandeurs dérivées et voies d'accès ;
- l'identification explicite de limites : origine des Yukawa, hiérarchie des masses, contraste entre secteurs de mélange et nature des masses neutrino.

## 3. Principe de reprise

Chaque élément du corpus est requalifié selon l'un des statuts suivants :

1. relation physique ou mathématique ;
2. processus dynamique ou thermique ;
3. opération de représentation ou de calcul ;
4. voie d'accès expérimentale ou inférentielle ;
5. interprétation philosophique ;
6. hypothèse propre au projet.

Une relation entre objets n’est pas tenue pour une architecture explicative par le seul fait que ses éléments sont solidaires. Il faut montrer ce qu’elle permet de dériver, de distinguer, d’exclure ou de formuler contrefactuellement.

## 4. Correction de la chaîne antérieure

La chaîne suivante est insuffisante :

```text
régime électrofaible non brisé
-> brisure électrofaible
-> matrices de Yukawa
-> matrices de masse
-> diagonalisation
-> masses et orientations
```

Elle peut laisser croire que les matrices de Yukawa sont produites par la brisure électrofaible. Or les termes de Yukawa appartiennent déjà au lagrangien du Modèle standard dans sa formulation symétrique. La valeur moyenne non nulle du champ de Higgs permet ensuite à ces couplages de produire des matrices de masse.

La reconstruction minimale distingue donc trois chaînes.

## 5. Chaîne A — constitution théorique

```text
structure de jauge
+ contenu en champs
+ potentiel du Higgs
+ matrices de Yukawa Y_u, Y_d, Y_e
        |
        v
choix du vide / régime électrofaible brisé
        |
        v
valeur moyenne non nulle v
        |
        v
matrices de masse M_f = Y_f v / sqrt(2)
        |
        v
diagonalisation biunitaire
        |
        +--> valeurs propres de masse
        |
        +--> désalignement gauche relatif = V_CKM
```

Cette chaîne est principalement structurelle. Elle décrit des dépendances au sein de la théorie.

Elle n'explique pas :

- pourquoi le potentiel du Higgs possède ses paramètres particuliers ;
- pourquoi les matrices `Y_f` ont leur texture et leur hiérarchie ;
- pourquoi trois générations existent ;
- pourquoi les masses observées prennent leurs valeurs particulières.

## 6. Chaîne B — histoire thermique

La formulation contrôlée ne repose pas sur l’apparition ponctuelle d’un `v(T)` unique :

```text
température du plasma
+ paramètres thermiques de la théorie effective
        |
        v
évolution continue du condensat invariant de jauge
et des observables thermodynamiques
        |
        v
maximum de susceptibilité
        |
        v
région pseudocritique du crossover électrofaible
        |
        v
régime de basse température
```

Cette chaîne concerne l'histoire thermique du secteur électrofaible.

Pour les paramètres physiques du Modèle standard, le changement est un crossover lisse, avec une température pseudocritique proche de `159,5 GeV`, et non une transition de phase singulière.

Elle ne doit pas être confondue avec l'ordre logique de constitution de la théorie. La formulation du lagrangien, le choix d'une base, la diagonalisation et le refroidissement cosmologique ne sont pas des étapes d'une même temporalité.

Le symbole `v(T)` peut être utilisé dans une paramétrisation contrôlée, mais il ne doit pas être présenté sans précaution comme un paramètre d’ordre unique, directement observable et indépendant de la jauge.

## 7. Chaîne C — accès expérimental et inférentiel

### 7.1 Accès à l'échelle électrofaible

```text
désintégration du muon
+ théorie effective de Fermi
+ corrections électrofaibles
        |
        v
détermination de G_F
        |
        v
inférence de l'échelle de Fermi v_F
```

Au niveau arbre :

```math
\frac{G_F}{\sqrt 2}=\frac{1}{2v^2}.
```

Cette relation relie une mesure basse énergie à un paramètre du régime électrofaible brisé. Elle ne signifie pas que `G_F` et `v` sont le même type d'objet, ni que la relation d’arbre constitue une identité universelle entre tous les paramètres renormalisés.

### 7.2 Accès aux Yukawa

```text
masses fermioniques
+ échelle électrofaible
+ schéma et échelle de renormalisation
        |
        v
inférence des paramètres de Yukawa
```

et, de manière complémentaire :

```text
production et désintégrations du boson de Higgs
        |
        v
tests directs ou semi-directs des couplages Higgs–fermions
```

L'accès varie fortement selon le fermion. Il faut distinguer les paramètres extraits des masses, les couplages testés dans les processus du Higgs et les dépendances au schéma et à l'échelle.

### 7.3 Accès à CKM

```text
désintégrations faibles
+ physique des mésons
+ éléments de matrice hadroniques
+ ajustements globaux
        |
        v
contenu physique de CKM
```

La matrice écrite dépend de conventions de phase. Le contenu physique doit être recherché dans les modules pertinents, les angles, la phase physique et les invariants de rephasage, notamment l'invariant de Jarlskog.

## 8. Objets et fonctions provisoires

Le tableau suivant ne constitue pas une taxonomie générale. Il sert uniquement à empêcher la confusion des fonctions locales.

| Objet | Type d'objet | Fonction locale | Ce qu'il ne faut pas lui attribuer |
|---|---|---|---|
| potentiel du Higgs | structure dynamique du secteur scalaire | détermine les états du vide permis dans le modèle | n'explique pas à lui seul ses propres paramètres ni les valeurs des Yukawa |
| `v` | paramètre de valeur moyenne dans une description du vide brisé | fixe une échelle commune du régime électrofaible au niveau arbre | ne distribue pas seul les masses entre fermions |
| `Y_f` | matrices de couplage renormalisées | paramètrent la texture des couplages Higgs–fermions à schéma et échelle donnés | leur hiérarchie n'est pas expliquée par le Modèle standard |
| `M_f` | matrices de masse dérivées dans le régime brisé | combinent l'échelle `v` et les textures `Y_f` | ne sont pas des entrées indépendantes de `v` et `Y_f` dans cette écriture |
| `m_f` | valeurs propres spectrales | caractérisent les états de masse après diagonalisation | ne doivent pas être appelées constantes sans préciser définition, échelle, schéma et domaine |
| `V_CKM` | classe physique de désalignement unitaire | règle les transitions faibles chargées entre saveurs de quarks | ses neuf éléments complexes écrits ne sont pas neuf constantes physiques indépendantes |
| `G_F` | coefficient effectif basse énergie | condense l'échange faible dans le régime `E << M_W` | n'est pas l'origine dynamique de `v` |

## 9. Hypothèse corrigée de fonction de fixité

Dans ce pilote, une fonction de fixité désigne provisoirement :

> le rôle local par lequel un objet physiquement ou formellement déterminé maintient une relation stable entre des états, processus, secteurs ou descriptions, dans un régime et sous des transformations explicités.

Forme abstraite :

```text
R(X_1, X_2 ; c | régime, transformations) = 0
```

où `c` est tenu fixe relativement aux variations admises et où les `X_i` peuvent être des processus, des états, des secteurs ou des descriptions.

Cette formulation échoue si elle revient seulement à dire qu'un paramètre est fixe parce qu'il est traité comme fixe.

Dans le secteur Higgs–Yukawa, plusieurs fonctions distinctes apparaissent :

- fixation d'échelle par `v` dans une description donnée ;
- paramétrage d'intensité et de texture par `Y_f` à échelle et schéma donnés ;
- fixation spectrale par les valeurs propres de `M_f` ;
- orientation relative par le contenu invariant de CKM ;
- raccordement effectif par `G_F`.

Le pilote ne démontre pas que ces fonctions partagent une essence unique. Il montre qu’elles peuvent être comparées sans être confondues.

## 10. Registre explicatif contrôlé

| Proposition | Statut explicatif |
|---|---|
| Le régime brisé permet des termes de masse fermionique proportionnels à `Y_f v` | expliqué structurellement dans le modèle |
| Les masses des fermions sont différentes | représenté par les différentes valeurs propres de `Y_f`, non expliqué dans leur origine |
| CKM apparaît dans les courants faibles chargés | expliqué par le désalignement des rotations gauches de `Y_u` et `Y_d` |
| Les valeurs numériques des angles CKM ont leur hiérarchie observée | paramétré et mesuré, non expliqué par le Modèle standard |
| `G_F` décrit les processus faibles à basse énergie | expliqué par une réduction effective contrôlée dans le régime approprié |
| L’échelle `v_F` est reliée à `G_F` | inférée avec un cadre théorique ; les corrections et le schéma doivent être distingués |
| Le secteur électrofaible change de régime dans l’histoire thermique | décrit par un crossover et des observables thermodynamiques ; pas par un instant unique de formation |
| Une phase particulière d’une entrée CKM est constante | refusé sans invariant de rephasage |
| Un Yukawa de quark est une valeur constante sans qualification | refusé sans schéma ni échelle |

## 11. Gain obtenu par rapport à la narration usuelle

L'énoncé compact :

> Le champ de Higgs donne leur masse aux particules.

est remplacé par une description différenciée qui montre :

1. que le secteur scalaire, les couplages de jauge, les couplages de Yukawa et la diagonalisation jouent des rôles distincts ;
2. que la génération formelle d'un terme de masse n'explique pas la valeur du couplage correspondant ;
3. que l'histoire thermique, la constitution théorique et l'accès expérimental sont trois chaînes reliées mais non identiques ;
4. que les grandeurs appelées constantes n'exercent pas toutes la même fonction de fixité ;
5. que les limites explicatives peuvent être localisées au lieu d'être masquées par la formule générale ;
6. qu’une écriture conventionnelle doit être distinguée de son contenu invariant.

Le gain le plus robuste ne réside pas dans l’ajout d’un vocabulaire, mais dans la séparation des relations et dans la localisation des arrêts de l’explication.

## 12. Conditions d'échec du pilote

Le pilote aurait échoué si :

- les relations typées n'avaient rien ajouté aux équations déjà connues ;
- la notion de fonction de fixité n'avait permis aucune exclusion ;
- les trois chaînes étaient restées confondues ;
- la description avait transformé des paramètres libres en mécanismes explicatifs ;
- les voies d'accès avaient été prises pour des processus constitutifs de l'objet ;
- l'architecture avait été déclarée robuste uniquement parce que chacun de ses éléments était nécessaire à la description choisie ;
- la méthode n'avait pu être appliquée à un cas négatif ou contrasté.

Ces échecs ont été évités dans le pilote, mais ils restent des critères obligatoires pour les cycles suivants.

## 13. Résultats de la phase 2

La vérification physique a :

1. restauré les équations principales du potentiel, des masses de jauge, des Yukawa, de CKM et de `G_F` ;
2. distingué les relations au niveau arbre de leurs corrections radiatives ;
3. précisé la dépendance des Yukawa et des masses de quarks à l'échelle et au schéma ;
4. remplacé le récit d’une transition ponctuelle par celui d’un crossover thermodynamique contrôlé ;
5. identifié les quantités CKM invariantes sous les conventions de phase ;
6. établi un registre de sources de référence ;
7. produit plusieurs contre-exemples où la fonction de fixité doit être refusée.

## 14. Décision

```text
Pilote Higgs–Yukawa : concluant sous conditions.
```

Le corpus Saveur–Higgs n'est pas abandonné. Sa matière physique et plusieurs de ses distinctions sont conservées. Ses anciennes familles ne sont pas restaurées comme résultats acquis.

Le pilote autorise le passage au cycle effectif basse énergie, qui devra être repris avec les mêmes exigences : relations typées, contrefactuels, distinctions entre objet et accès, et pouvoir explicatif indépendant du vocabulaire interne.

> La refondation conserve les relations physiques, les voies d'accès et les limites déjà identifiées ; elle ne réintroduit une architecture qu’après avoir montré ce qu’elle dérive, distingue, exclut et laisse inexpliqué.
