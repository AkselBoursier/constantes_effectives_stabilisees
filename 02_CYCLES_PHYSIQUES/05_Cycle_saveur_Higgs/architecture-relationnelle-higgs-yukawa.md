# Dossier pilote — architecture relationnelle Higgs–Yukawa

## Statut

Ce document ouvre la phase 1 du premier dossier expérimental de la refondation.

Il procède d'abord par extraction et requalification du corpus interne. Il ne propose pas encore une nouvelle taxonomie générale et ne considère pas les conclusions classificatoires antérieures comme acquises.

Le secteur neutrino est laissé hors du noyau initial. Il pourra être réintroduit ultérieurement comme extension distincte, puisque les masses et mélanges neutrino dépassent le Modèle standard minimal.

## 1. Question du pilote

> Que permet de voir une description relationnelle du secteur Higgs–Yukawa que ne montre pas immédiatement la narration selon laquelle « le Higgs donne leur masse aux particules » ?

Cette question est instruite à partir de la question plus générale :

> Qu'est-ce qu'une constante physique lorsqu'on la considère non comme un nombre isolé, mais comme un élément exerçant une fonction de fixité dans une architecture de processus ?

Le pilote ne cherche pas encore à définir définitivement le mot `constante`. Il examine ce que cette question oblige à distinguer dans un domaine physique précis.

## 2. Corpus interne repris

Le noyau documentaire est constitué de :

- la fiche sur la valeur moyenne du champ de Higgs `v` ;
- la fiche sur les matrices et couplages de Yukawa ;
- la fiche CKM ;
- la synthèse du cycle Saveur–Higgs ;
- la note d'architecture Saveur–Higgs ;
- la synthèse du cycle effectif basse énergie pour le raccordement par `G_F`.

Ces documents apportent déjà :

- la distinction entre échelle électrofaible, couplages, masses et orientations ;
- les relations `M_f = Y_f v / sqrt(2)` et `V_CKM = U_L^{u†} U_L^d` ;
- la différence entre paramètres libres, grandeurs dérivées et voies d'accès ;
- l'identification explicite de limites : origine des Yukawa, hiérarchie des masses, contraste entre secteurs de mélange et nature des masses neutrino.

## 3. Principe de reprise

Chaque élément du corpus doit être requalifié selon l'un des statuts suivants :

1. relation physique ou mathématique ;
2. processus dynamique ou thermique ;
3. opération de représentation ou de calcul ;
4. voie d'accès expérimentale ou inférentielle ;
5. interprétation philosophique ;
6. hypothèse propre au projet.

Une relation entre objets ne sera plus tenue pour une architecture explicative par le seul fait que ses éléments sont solidaires. Il faudra montrer ce que cette relation permet de dériver, de distinguer ou d'exclure.

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

La reconstruction minimale doit donc distinguer trois chaînes.

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
        +--> désalignement U_L^{u†} U_L^d = V_CKM
```

Cette chaîne est principalement structurelle. Elle décrit des dépendances au sein de la théorie.

Elle n'explique pas encore :

- pourquoi le potentiel du Higgs possède ses paramètres particuliers ;
- pourquoi les matrices `Y_f` ont leur texture et leur hiérarchie ;
- pourquoi trois générations existent ;
- pourquoi les masses observées prennent leurs valeurs particulières.

## 6. Chaîne B — histoire thermique

```text
température du plasma
+ potentiel effectif à température finie
        |
        v
évolution du minimum thermodynamique
        |
        v
crossover électrofaible
        |
        v
régime de basse température avec v(T) non nul
```

Cette chaîne concerne l'histoire thermique du régime électrofaible.

Elle ne doit pas être confondue avec l'ordre logique de constitution de la théorie. La formulation du lagrangien, le choix d'une base, la diagonalisation et le refroidissement cosmologique ne sont pas des étapes d'une même temporalité.

La phase 2 devra vérifier précisément :

- la définition de `v(T)` ;
- la portée du langage de brisure spontanée à température finie ;
- le statut du crossover pour les paramètres physiques du Modèle standard ;
- la différence entre température caractéristique, échelle électrofaible et valeur du vide à température nulle.

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
inférence de l'échelle v
```

Au niveau arbre :

```text
G_F / sqrt(2) = 1 / (2 v^2)
```

Cette relation relie une mesure basse énergie à un paramètre du régime électrofaible brisé. Elle ne signifie pas que `G_F` et `v` sont le même type d'objet.

### 7.2 Accès aux Yukawa

```text
masses fermioniques + valeur de v + schéma de renormalisation
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

L'accès varie fortement selon le fermion. Il faudra distinguer les paramètres extraits des masses, les couplages testés dans les processus du Higgs et les dépendances au schéma et à l'échelle.

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
| potentiel du Higgs | structure dynamique du secteur scalaire | détermine les états du vide permis dans le modèle | n'explique pas à lui seul les valeurs des Yukawa |
| `v` | valeur moyenne du champ dans le vide brisé | fixe une échelle commune du régime électrofaible | ne distribue pas seul les masses entre fermions |
| `Y_f` | matrices de couplage sans dimension | paramètrent la texture des couplages Higgs–fermions | leur hiérarchie n'est pas expliquée par le Modèle standard |
| `M_f` | matrices de masse dérivées dans le régime brisé | combinent l'échelle `v` et les textures `Y_f` | ne sont pas des entrées indépendantes de `v` et `Y_f` dans cette écriture |
| `m_f` | valeurs propres spectrales | caractérisent les états de masse après diagonalisation | ne doivent pas être appelées constantes sans préciser échelle, schéma et domaine |
| `V_CKM` | structure unitaire de désalignement | règle les transitions faibles chargées entre saveurs de quarks | ses neuf éléments écrits ne sont pas neuf constantes physiques indépendantes |
| `G_F` | coefficient effectif basse énergie | condense l'échange faible dans le régime `E << M_W` | n'est pas l'origine dynamique de `v` |

## 9. Première hypothèse de fonction de fixité

Dans ce pilote, une fonction de fixité désigne provisoirement le rôle par lequel un objet maintient déterminée une relation entre des processus ou secteurs variables dans un régime donné.

Forme abstraite :

```text
R(P_1, P_2 ; c) = 0
```

où `c` est tenu fixe relativement aux variations admises dans le régime étudié.

Cette formulation doit rester testable. Elle échoue si elle revient seulement à dire qu'un paramètre est fixe parce qu'il est traité comme fixe.

Dans le secteur Higgs–Yukawa, plusieurs fonctions distinctes apparaissent déjà :

- fixation d'échelle par `v` ;
- paramétrage d'intensité et de texture par `Y_f` ;
- fixation spectrale par les valeurs propres de `M_f` ;
- orientation relative par le contenu physique de CKM ;
- raccordement effectif par `G_F`.

Le dossier devra déterminer si ces fonctions partagent un noyau conceptuel réel ou si le mot `constante` recouvre ici plusieurs statuts irréductibles.

## 10. Registre explicatif initial

| Proposition | Statut explicatif provisoire |
|---|---|
| Le régime brisé permet des termes de masse fermionique proportionnels à `Y_f v` | expliqué structurellement dans le modèle |
| Les masses des fermions sont différentes | représenté par les différentes valeurs propres de `Y_f`, non expliqué dans leur origine |
| CKM apparaît dans les courants faibles chargés | expliqué par le désalignement des diagonalisation gauches de `Y_u` et `Y_d` |
| Les valeurs numériques des angles CKM ont leur hiérarchie observée | paramétré et mesuré, non expliqué par le Modèle standard |
| `G_F` décrit les processus faibles à basse énergie | expliqué par une réduction effective contrôlée dans le régime approprié |
| La valeur observée de `v` est reliée à `G_F` | inférée avec un cadre théorique et des corrections ; son origine ultime reste ouverte |
| Le régime électrofaible s'installe dans l'histoire thermique | descriptible par le potentiel effectif thermique ; résolution à vérifier en phase 2 |

## 11. Gain attendu par rapport à la narration usuelle

Le dossier sera concluant s'il permet de remplacer l'énoncé compact :

> Le champ de Higgs donne leur masse aux particules.

par une description différenciée qui montre :

1. que le secteur scalaire, les couplages de Yukawa et la diagonalisation jouent des rôles distincts ;
2. que la génération formelle d'un terme de masse n'explique pas la valeur du couplage correspondant ;
3. que l'histoire thermique, la constitution théorique et l'accès expérimental sont trois chaînes reliées mais non identiques ;
4. que les grandeurs appelées constantes n'exercent pas toutes la même fonction de fixité ;
5. que les limites explicatives peuvent être localisées au lieu d'être masquées par la formule générale.

## 12. Conditions d'échec du pilote

Le pilote échoue si :

- les relations typées n'ajoutent rien aux équations déjà connues ;
- la notion de fonction de fixité ne permet aucune exclusion ;
- les trois chaînes restent confondues ;
- la description transforme des paramètres libres en mécanismes explicatifs ;
- les voies d'accès sont prises pour des processus constitutifs de l'objet ;
- l'architecture est déclarée robuste uniquement parce que chacun de ses éléments est nécessaire à la description choisie ;
- la méthode ne peut pas être appliquée à un cas négatif ou contrasté.

## 13. Travail de phase 2

La phase 2 sera une vérification physique ciblée. Elle devra :

1. restaurer et contrôler les équations dégradées lors des extractions DOCX ;
2. distinguer les relations au niveau arbre de leurs corrections radiatives ;
3. préciser la dépendance des Yukawa et des masses de quarks à l'échelle et au schéma ;
4. vérifier la formulation du potentiel du Higgs et du potentiel effectif thermique ;
5. identifier les quantités CKM invariantes sous les conventions de phase ;
6. établir un registre de sources primaires ou de synthèses de référence pour chaque proposition physique ;
7. produire au moins un contre-exemple où la notion de fonction de fixité doit être refusée.

Aucune généralisation aux autres cycles ne sera engagée avant cette vérification.

## 14. Décision provisoire

Le corpus Saveur–Higgs n'est pas abandonné. Il devient le matériau d'un test plus strict.

> La refondation conserve les relations physiques, les voies d'accès et les limites déjà identifiées, mais suspend les anciennes familles jusqu'à ce que leur nécessité et leur pouvoir explicatif soient démontrés.
