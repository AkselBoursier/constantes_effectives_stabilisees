# Chantier Q (catégories, accès et inférences) — Stern–Gerlach : cadrage physique et niveaux v0.1

## 0. Statut

```text
statut : reconstruction physique de première passe ;
fonction : fixer l'objet avant l'analyse philosophique ;
source de contrôle : articles originaux et travaux de recherche cités dans la bibliographie ;
limite : ni revue exhaustive, ni théorie de la mesure, ni choix d'interprétation.
```

## 1. Trois Stern–Gerlach à distinguer

### Expérience historique de 1922 (`H`)

Le dispositif de Gerlach et Stern produisait un faisceau d'atomes d'argent à partir d'un four, le collimatait par deux ouvertures, le faisait passer le long d'un aimant fortement inhomogène, puis déposait les atomes sur une plaque de verre. L'exposition durait plusieurs heures et le dépôt devait être développé pour devenir visible.

Le résultat expérimental accessible n'était donc pas une suite enregistrée d'impacts individuels `+` ou `-`, mais une distribution cumulative de matière sur une plaque. Les auteurs observaient deux bandes discrètes, sans bande centrale clairement détectable, et concluaient à la quantification spatiale dans un champ magnétique.

```text
objet préparé : faisceau thermique d'atomes d'argent ;
interaction : moment magnétique atomique + champ inhomogène ;
trace : dépôt cumulatif sur plaque ;
classement : deux bandes spatiales ;
interprétation de 1922 : quantification spatiale ;
interprétation rétrospective : signature compatible avec un degré de liberté de spin 1/2.
```

Le spin électronique n'était pas encore formulé en 1922. L'expérience historique ne doit donc pas être décrite comme si ses auteurs avaient directement préparé puis mesuré un qubit de spin au sens moderne.

### Modèle quantique idéalisé (`I`)

Le modèle moderne minimal traite un atome neutre possédant un moment magnétique et un degré de liberté spatial. Une écriture courante est :

\[
\hat H = \frac{\hat{\mathbf p}^{\,2}}{2M} - \gamma\,\hat{\mathbf S}\cdot \mathbf B(\hat{\mathbf r}).
\]

Un champ compatible avec un gradient principal selon `z` peut être écrit localement sous la forme :

\[
\mathbf B(\mathbf r)= -\beta x\,\mathbf e_x +(B_0+\beta z)\,\mathbf e_z.
\]

Sous les approximations qui rendent négligeables les transitions de spin et les effets transverses, l'Hamiltonien effectif devient :

\[
\hat H_{\mathrm eff}=\frac{\hat{\mathbf p}^{\,2}}{2M}
-\gamma(B_0+\beta\hat z)\hat S_z.
\]

Pour un état initial

\[
\psi(\mathbf r)\left(\alpha\lvert +z\rangle+\beta_s\lvert -z\rangle\right),
\]

l'évolution unitaire corrèle la composante de spin et le degré de liberté spatial :

\[
\alpha\,\psi_+(\mathbf r,t)\lvert +z\rangle
+\beta_s\,\psi_-(\mathbf r,t)\lvert -z\rangle.
\]

Les deux paquets spatiaux peuvent ensuite devenir suffisamment séparés pour être distingués par une détection de position.

Cette chaîne contient plusieurs opérations distinctes :

```text
orientation matérielle du champ ;
choix formel de l'opérateur S_z ;
couplage spin–position ;
séparation partielle de paquets d'onde ;
détection spatiale ;
partition des positions en deux régions ;
attribution des étiquettes + et -.
```

Le déplacement spatial n'est pas le spin lui-même. Il constitue une corrélation exploitée pour inférer une composante de spin à partir d'une position détectée.

### Dispositifs modernes ou séquentiels (`M`)

Les dispositifs appelés Stern–Gerlach aujourd'hui peuvent servir à :

```text
préparer un sous-ensemble d'états ;
analyser une composante de moment angulaire ;
séparer des états Zeeman ou hyperfins ;
réaliser des séquences de mesure selon plusieurs axes ;
produire des faisceaux polarisés ;
étudier l'interférence ou l'information de chemin.
```

Ils emploient des espèces, des champs, des détecteurs et des régimes différents de ceux de 1922. Le terme `Stern–Gerlach` désigne donc une famille de techniques et de modèles, pas un unique objet expérimental invariant.

## 2. Ce que mesure le modèle idéal

Dans le modèle idéal, l'orientation de l'appareil fixe l'axe du couplage dominant et donc la composante de spin représentée par l'opérateur mesuré. Dire que l'appareil « choisit l'axe » ne signifie pas qu'il crée le spin ou qu'il impose à un vecteur classique préexistant de s'orienter.

La conclusion minimale est :

> Le réglage macroscopique du champ détermine quelle composante de l'opérateur de spin est corrélée à la variable spatiale de lecture.

L'inférence `position haute -> +z` ou `position basse -> -z` dépend :

```text
du modèle du couplage ;
de la calibration du champ ;
de la séparation effective des distributions ;
de la résolution du détecteur ;
du seuil ou coarse-graining qui définit les deux classes ;
des hypothèses excluant les transitions et aberrations importantes.
```

## 3. La trajectoire : trois usages à ne pas confondre

### 3.1 Trajectoire géométrique de montage

Le dispositif est conçu avec un axe de propagation et une géométrie déterminée. Cette description classique est indispensable à la fabrication, à l'alignement et à la reproductibilité.

### 3.2 Trajectoire semi-classique

On peut suivre le centre d'un paquet ou approximer le mouvement par une trajectoire newtonienne soumise à une force dépendant de la composante de spin. Cette approximation est utile pour estimer la déflexion et relier le modèle aux dimensions du montage.

### 3.3 Trajectoire microscopique individuelle

Le formalisme quantique standard n'exige pas l'attribution d'une trajectoire classique définie à chaque atome entre la source et l'écran. Les modèles qui attribuent de telles trajectoires ajoutent une structure interprétative particulière.

Le pilote doit donc éviter la phrase non qualifiée : `l'atome suit l'une des deux trajectoires`.

## 4. La mesure n'est pas un instant unique

Plusieurs événements peuvent être appelés `mesure` :

```text
entrée dans le champ ;
interaction spin–position ;
séparation suffisante des paquets ;
interaction avec le détecteur ;
formation d'une trace stable ;
classement en deux issues ;
communication d'un résultat.
```

Ces étapes ne sont pas équivalentes. L'évolution unitaire peut expliquer la corrélation et la séparation spatiale, mais elle ne suffit pas, à elle seule et sans cadre interprétatif supplémentaire, à résoudre le problème général de l'unicité du résultat individuel.

Une analyse avec détection de résolution finie montre en outre que la distinction entre états de spin est liée au caractère grossier de la lecture de position. Le coarse-graining n'est donc pas un simple embellissement narratif : il participe à la définition opérationnelle des issues distinguées.

## 5. Les approximations ont un contenu épistémique

Le schéma pédagogique idéal masque plusieurs conditions :

```text
champ dominant selon un axe ;
gradient suffisamment régulier ;
faibles transitions de spin ;
séparation spatiale supérieure à la largeur des paquets et à la résolution ;
collimation et distribution de vitesses contrôlées ;
relation calibrée entre région du détecteur et composante de spin.
```

Des traitements quantiques complets prédisent des phénomènes de focalisation et de retournement de spin et évaluent la fiabilité de l'appareil comme mesure d'une projection de spin. Le statut de `mesure de S_z` est donc une réussite de régime et d'approximation, non une identité analytique indépendante du dispositif.

## 6. Première chaîne d'accès

```text
source thermique ou préparée
-> collimation et sélection du faisceau
-> champ orienté et calibré
-> évolution conjointe espace–spin
-> séparation spatiale
-> interaction de détection
-> trace ou donnée de position
-> coarse-graining en régions
-> inférence sur une composante de spin
-> attribution et communication.
```

Chaque flèche ajoute une opération. Aucune donnée brute ne porte seule l'énoncé complet `le spin vaut + selon z`.

## 7. Garde-fous du pilote

```text
1. ne pas confondre l'expérience historique et le qubit pédagogique ;
2. ne pas confondre la position détectée et la propriété de spin ;
3. ne pas confondre l'axe matériel, l'axe formel et une direction classique préexistante ;
4. ne pas confondre séparation des paquets et résultat individuel défini ;
5. ne pas confondre trajectoire semi-classique et ontologie de trajectoires ;
6. ne pas conclure de la nécessité d'une catégorie à sa fondamentalité ;
7. ne pas attribuer à l'appareil seul la constitution de la réalité physique.
```

## 8. Hypothèse testée

Le pilote teste l'hypothèse faible suivante :

> Les catégories dites classiques ne forment pas un bloc. Elles peuvent être nécessaires à des fonctions matérielles, opératoires ou communicationnelles, dispensables dans certaines étapes formelles, et trompeuses lorsqu'elles sont transportées sans modification vers l'ontologie du système microscopique.

La matrice suivante doit confirmer, préciser ou invalider cette hypothèse.
