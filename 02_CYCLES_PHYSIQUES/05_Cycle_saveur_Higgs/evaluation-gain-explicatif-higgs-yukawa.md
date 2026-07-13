# Évaluation du gain explicatif — pilote Higgs–Yukawa

## Statut

Ce document évalue le premier dossier expérimental après vérification physique.

Documents associés :

- [architecture-relationnelle-higgs-yukawa.md](architecture-relationnelle-higgs-yukawa.md)
- [verification-physique-higgs-yukawa.md](verification-physique-higgs-yukawa.md)

La question n’est pas de savoir si le pilote introduit une nouvelle théorie physique. Il faut déterminer s’il produit une organisation conceptuelle qui explique ou différencie davantage que la présentation compacte selon laquelle « le Higgs donne leur masse aux particules ».

## 1. Critères d’un gain explicatif

Le pilote est tenu pour explicativement utile s’il permet au moins l’une des opérations suivantes :

1. dériver une conséquence à partir d’éléments distincts ;
2. identifier le mécanisme responsable d’une relation ;
3. produire un contrefactuel déterminé ;
4. localiser ce qui reste paramétré plutôt qu’expliqué ;
5. distinguer des chaînes que le récit ordinaire superpose ;
6. exclure une attribution illégitime de constance ou de causalité.

Une simple multiplication de flèches ou de catégories ne constitue pas un gain.

## 2. Résultat principal

Le pilote produit un gain explicatif réel mais limité.

Il ne découvre pas une nouvelle relation physique. Il rend explicite la distribution du travail explicatif entre plusieurs structures :

```text
potentiel scalaire
    -> permet un régime de vide non nul dans le modèle

valeur moyenne v
    -> fixe l’échelle commune des masses électrofaibles au niveau arbre

matrices de Yukawa
    -> encodent les intensités et textures fermioniques

insertion de v
    -> transforme les interactions de Yukawa en matrices de masse

diagonalisation
    -> révèle valeurs propres et désalignements physiques

désalignement gauche up/down
    -> produit CKM dans les courants faibles chargés

limite E << M_W
    -> permet la description effective par G_F
```

Ce découpage empêche qu’un seul terme — « mécanisme de Higgs » — absorbe des fonctions différentes.

## 3. Contrefactuels

### 3.1 Si `v = 0`

Au niveau arbre dans la formulation symétrique :

```math
m_W=m_Z=0,
\qquad
M_f=0.
```

Les matrices de Yukawa peuvent toujours figurer dans le lagrangien comme couplages, mais elles ne produisent pas de termes de masse fermionique proportionnels à une valeur moyenne non nulle.

Ce contrefactuel distingue clairement :

```text
existence d’un couplage de Yukawa
≠
existence d’une masse fermionique dans le régime brisé.
```

### 3.2 Si un Yukawa propre `y_f = 0`

Pour le fermion correspondant :

```math
m_f=\frac{y_fv}{\sqrt2}=0
```

au niveau arbre, et le couplage diagonal du Higgs à ce fermion s’annule dans le Modèle standard minimal.

Ce contrefactuel montre que `v` ne suffit pas à différencier les masses.

### 3.3 Si `Y_u` et `Y_d` sont alignées

Si les deux matrices peuvent être diagonalées par la même rotation gauche, alors :

```math
V_{\mathrm{CKM}}=\mathbb I
```

à des phases non physiques près.

Les transitions faibles chargées ne mélangent plus les générations. Le mélange CKM ne provient donc pas de la seule existence de masses, mais du désalignement relatif des textures quark.

### 3.4 Si la phase physique est nulle

Si la phase irréductible de CKM s’annule :

```math
J=0,
```

et la violation CP de type CKM disparaît.

Ce contrefactuel distingue une phase de convention d’une phase physiquement irréductible.

### 3.5 Si `E` n’est pas très inférieur à `M_W`

La description locale de Fermi cesse d’être suffisante. Le propagateur du `W` et la structure électrofaible complète doivent être résolus.

Ainsi :

```text
G_F comme coefficient fixe
```

n’est explicatif et opératoire que dans un domaine de validité déterminé.

### 3.6 Si l’histoire thermique était une transition du premier ordre

Une transition du premier ordre impliquerait coexistence de phases, nucléation et discontinuités thermodynamiques. Pour les paramètres physiques du Modèle standard, les calculs non perturbatifs indiquent au contraire un crossover lisse.

Ce contraste montre que l’histoire thermique n’est pas déductible de la seule forme qualitative du potentiel classique à température nulle.

## 4. Ce qui est expliqué

Le Modèle standard, lu à travers le pilote, explique structurellement :

- pourquoi des termes de masse fermionique directs sont incompatibles avec la représentation chirale avant le régime brisé ;
- comment les interactions de Yukawa permettent des masses après insertion de la valeur moyenne du Higgs ;
- pourquoi les masses de jauge dépendent de `v` et des couplages de jauge ;
- pourquoi CKM apparaît dans les courants chargés après passage aux états de masse ;
- pourquoi une théorie locale à quatre fermions est valable lorsque `E << M_W` ;
- pourquoi certaines écritures matricielles contiennent des paramètres de convention non physiques.

## 5. Ce qui n’est pas expliqué

Le pilote permet également de localiser précisément les arrêts de l’explication :

- les valeurs de `\mu^2` et `\lambda` ;
- la valeur de l’échelle électrofaible relativement à des échelles plus profondes ;
- les valeurs et textures des matrices `Y_f` ;
- la hiérarchie des masses fermioniques ;
- l’existence de trois générations ;
- les valeurs des angles et de la phase CKM ;
- l’origine des masses neutrino, hors du noyau minimal retenu ;
- l’origine ultime des paramètres d’entrée utilisés dans l’histoire thermique.

La formule « le Higgs explique la masse » est donc trop globale. Le cadre explique une structure de génération et de compatibilité ; il ne prédit pas la distribution numérique des masses.

## 6. Réponse à la question de résolution cinématique

Question :

> Peut-on décrire la formation des constantes avec une résolution cinématique suffisante pour produire un pouvoir explicatif ?

Réponse issue du pilote :

> Une résolution cinématique seule ne suffit pas. Le pouvoir explicatif apparaît lorsque la succession est complétée par des relations dynamiques ou structurelles, des règles de dérivation, des domaines de validité et des contrefactuels.

Dans le pilote :

- la chaîne thermique produit une résolution historique du changement de régime ;
- la chaîne du lagrangien produit une explication structurelle des termes de masse ;
- la diagonalisation produit une clarification représentationnelle ;
- la chaîne d’accès produit une justification inférentielle ;
- aucune de ces chaînes, prise seule, n’explique les valeurs libres des Yukawa.

Le terme « formation » doit donc être typé :

```text
formation d’un régime
formation d’un terme effectif
formation d’une représentation physique
formation d’une estimation
```

ne désignent pas un seul processus.

## 7. Évaluation de l’hypothèse de fonction de fixité

### 7.1 Ce qui résiste

L’hypothèse est utile localement pour distinguer :

- fixation d’échelle par `v` ;
- fixation de texture et d’intensité par `Y_f` à échelle et schéma donnés ;
- fixation spectrale par les valeurs propres ;
- fixation d’orientation relative par les invariants de CKM ;
- fixation d’un raccordement effectif par `G_F` dans son régime.

### 7.2 Ce qui doit être corrigé

La formule initiale « relation processus à processus » est trop étroite.

Le dossier contient aussi :

- des relations entre paramètres ;
- des relations entre secteurs du lagrangien ;
- des opérations de changement de base ;
- des relations entre observables et paramètres inférés ;
- des changements de régime thermodynamique.

La formulation corrigée devient :

> Une fonction de fixité est le rôle local par lequel un objet physiquement ou formellement déterminé maintient une relation stable entre des états, processus, secteurs ou descriptions, dans un régime et sous des transformations explicités.

Cette formulation reste une hypothèse méthodologique, non une essence de toute constante.

### 7.3 Limite conceptuelle

Le même objet peut exercer plusieurs fonctions selon la question posée. `M_W` est une masse dans le spectre électrofaible et une échelle de validité vue depuis la théorie de Fermi.

La fonction ne doit donc pas être confondue avec le type ontologique de l’objet.

## 8. Gain pédagogique

Le pilote apporte un gain pédagogique précis s’il est présenté comme une couche ajoutée, non comme un remplacement du formalisme.

Il permet de répondre séparément à six questions souvent condensées :

| Question | Réponse localisée |
|---|---|
| Qu’est-ce qui autorise les masses ? | Le régime électrofaible brisé et la structure des interactions |
| Qu’est-ce qui fixe l’échelle commune ? | `v` avec les couplages de jauge ou de Yukawa |
| Qu’est-ce qui différencie les fermions ? | Les matrices `Y_f` |
| Qu’est-ce qui rend les masses lisibles ? | L’insertion de `v` puis la diagonalisation |
| Qu’est-ce qui produit le mélange quark ? | Le désalignement des rotations gauches |
| Comment y accède-t-on ? | Plusieurs chaînes expérimentales et inférentielles distinctes |

Le gain ne réside pas dans une simplification maximale. Il réside dans la prévention de simplifications trompeuses.

## 9. Le pilote est-il concluant ?

### Verdict

```text
Pilote concluant sous conditions.
```

Il est concluant parce qu’il :

- corrige une erreur de séquence du corpus ;
- sépare trois temporalités et quatre niveaux de description ;
- localise les paramètres libres ;
- produit des contrefactuels ;
- refuse plusieurs faux candidats à la constance ;
- révèle un gain pédagogique identifiable.

Il reste conditionnel parce qu’il ne démontre pas encore que « fonction de fixité » est le meilleur vocabulaire pour tous les cycles. Le gain le plus robuste provient pour l’instant de la méthode de relations typées et du registre explicatif.

## 10. Critères de transfert aux autres cycles

Une extension n’est admise que si le cycle suivant permet :

1. d’identifier au moins deux chaînes auparavant confondues ;
2. de typer les relations sans les transformer en nouvelles familles automatiques ;
3. de produire au moins un contrefactuel ;
4. de distinguer ce qui est expliqué, inféré, défini ou simplement paramétré ;
5. de fournir un cas où le qualificatif de constante doit être refusé ;
6. de montrer un gain qui ne dépend pas du vocabulaire propre au projet.

## 11. Décision de transfert

Le pilote autorise le passage au cycle effectif basse énergie, avec `G_F` comme point de raccordement naturel.

L’ordre proposé est maintenu :

```text
1. cycle effectif basse énergie ;
2. cycle métrologique SI comme contraste ;
3. cosmologie seulement après ces deux tests.
```

Cette décision n’entraîne pas la restauration des anciennes architectures comme résultats acquis. Chaque cycle devra être repris par la méthode resserrée.

## 12. Formule de clôture

> L’architecture relationnelle n’explique pas les valeurs que le Modèle standard laisse libres. Elle produit néanmoins un pouvoir explicatif en séparant les mécanismes, les opérations, les régimes et les voies d’accès, puis en localisant exactement le point où l’explication s’arrête.
