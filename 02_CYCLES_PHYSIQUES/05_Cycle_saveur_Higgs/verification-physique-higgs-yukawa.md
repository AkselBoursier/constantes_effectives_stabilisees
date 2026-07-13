# Vérification physique du pilote Higgs–Yukawa

## Statut

Ce document consigne la phase 2 du dossier pilote. Il contrôle les relations physiques reprises du corpus, distingue niveau arbre et niveau quantique, précise les dépendances de schéma et d’échelle, et identifie les quantités dont le contenu est invariant.

Il ne remplace pas le dossier principal :

- [architecture-relationnelle-higgs-yukawa.md](architecture-relationnelle-higgs-yukawa.md)

Il en constitue le registre de vérification.

## 1. Sources de contrôle

Les propositions ont été contrôlées en priorité contre les synthèses de référence et travaux suivants :

1. Particle Data Group, *Status of Higgs Boson Physics*, mise à jour 2025 :
   <https://pdg.lbl.gov/2025/reviews/rpp2025-rev-higgs-boson.pdf>
2. Particle Data Group, *CKM Quark-Mixing Matrix*, mise à jour 2025 :
   <https://pdg.lbl.gov/2025/reviews/rpp2025-rev-ckm-matrix.pdf>
3. Particle Data Group, *Electroweak Model and Constraints on New Physics*, mise à jour 2025–2026 :
   <https://pdg.lbl.gov/2025/reviews/rpp2025-rev-standard-model.pdf>
4. Particle Data Group, *Quark Masses*, mise à jour 2025 :
   <https://pdg.lbl.gov/2025/reviews/rpp2025-rev-quark-masses.pdf>
5. M. D’Onofrio et K. Rummukainen, *The Standard Model cross-over on the lattice* :
   <https://arxiv.org/abs/1508.07161>

Les valeurs numériques expérimentales ne sont pas le centre de ce document. Elles seront actualisées seulement lorsqu’elles sont nécessaires à une distinction conceptuelle.

## 2. Secteur scalaire au niveau arbre

Le potentiel scalaire renormalisable minimal du Modèle standard s’écrit :

```math
V(\Phi)=\mu^2\,\Phi^\dagger\Phi+\lambda(\Phi^\dagger\Phi)^2.
```

Pour :

```math
\mu^2<0, \qquad \lambda>0,
```

le minimum classique satisfait :

```math
\langle\Phi^\dagger\Phi\rangle=\frac{v^2}{2},
\qquad
v^2=-\frac{\mu^2}{\lambda}.
```

Dans la jauge unitaire, on peut paramétrer le doublet par :

```math
\Phi(x)=\frac{1}{\sqrt 2}
\begin{pmatrix}
0\\
v+H(x)
\end{pmatrix}.
```

Les relations au niveau arbre sont alors :

```math
m_W=\frac{gv}{2},
\qquad
m_Z=\frac{v}{2}\sqrt{g^2+g'^2},
\qquad
m_\gamma=0,
```

et :

```math
m_H^2=2\lambda v^2.
```

### Décision de contrôle

Les relations du corpus entre potentiel, vide, échelle électrofaible et masses de jauge sont confirmées au niveau arbre.

### Limite

Ces relations ne signifient pas que le potentiel explique les valeurs de `\mu^2` et `\lambda`. Le modèle relie les paramètres ; il ne dérive pas leur valeur depuis une structure plus profonde.

## 3. Secteur de Yukawa avant et après le régime brisé

Le lagrangien de Yukawa appartient déjà à la formulation symétrique du Modèle standard :

```math
\mathcal L_Y=
-\overline Q_L Y_d\Phi d_R
-\overline Q_L Y_u\widetilde\Phi u_R
-\overline L_L Y_e\Phi e_R
+\mathrm{h.c.}
```

avec :

```math
\widetilde\Phi=i\sigma_2\Phi^*.
```

Après insertion de la valeur moyenne du champ :

```math
M_f=\frac{v}{\sqrt 2}Y_f,
\qquad f=u,d,e.
```

Dans une base où la matrice de masse est diagonale :

```math
m_{f_i}=\frac{v}{\sqrt 2}y_{f_i}
```

au niveau arbre.

### Décision de contrôle

La chaîne corrigée du dossier principal est confirmée :

```text
les Yukawa ne sont pas produits par la brisure ;
la valeur moyenne non nulle transforme leur contribution en matrices de masse.
```

Le terme « génération des masses » doit donc être compris en un sens précis : le régime brisé rend possibles les termes de masse compatibles avec la structure de jauge, mais les valeurs des matrices `Y_f` restent des paramètres libres du Modèle standard.

## 4. Diagonalisation et apparition de CKM

Pour chaque secteur quark, une décomposition biunitaire permet d’écrire :

```math
U_{fL}^\dagger M_f U_{fR}=D_f,
```

où `D_f` est diagonale à entrées positives.

Selon la convention choisie pour le sens des rotations de champs, la matrice CKM s’écrit :

```math
V_{\mathrm{CKM}}=U_{uL}^\dagger U_{dL}
```

ou sous la forme équivalente employée par le PDG avec les matrices inverses. Le contenu physique est le désalignement relatif des rotations gauches, non l’orientation absolue d’une base.

La matrice CKM unitaire `3 × 3` contient, après élimination des phases non physiques, quatre paramètres physiques :

```text
trois angles de mélange ;
une phase violant CP.
```

### Quantités robustes sous rephasage

Les objets suivants ont un contenu physique indépendant des conventions de phase :

- les modules `|V_ij|` ;
- trois angles et une phase dans une paramétrisation fixée ;
- les rapports complexes définissant les triangles d’unitarité ;
- l’invariant de Jarlskog `J`, mesure de la violation CP indépendante des conventions de phase.

### Décision de contrôle

Il est impropre de traiter les neuf entrées complexes écrites de CKM comme neuf « constantes physiques » indépendantes. La fonction éventuelle de fixité est portée par la classe d’équivalence physique de la matrice et par ses invariants, non par une écriture arbitraire.

## 5. Relation entre `G_F` et l’échelle électrofaible

Au niveau arbre, l’échange du boson `W` à basse énergie donne :

```math
\frac{G_F}{\sqrt 2}=\frac{g^2}{8m_W^2}=\frac{1}{2v^2}.
```

D’où :

```math
v=(\sqrt 2 G_F)^{-1/2}\simeq 246\ \mathrm{GeV}.
```

Cette relation justifie l’expression « échelle de Fermi » ou « échelle électrofaible ».

### Corrections radiatives

Au-delà du niveau arbre, le lien entre les observables d’entrée et les paramètres renormalisés inclut des corrections électrofaibles. Le PDG les organise notamment à travers `\Delta r` dans la relation entre `G_F`, `m_W`, `m_Z` et le couplage électromagnétique.

Il faut donc distinguer :

1. `G_F`, extrait de la durée de vie du muon dans un cadre théorique précis ;
2. la valeur conventionnelle `v_F=(\sqrt 2G_F)^{-1/2}` utilisée comme échelle d’entrée ;
3. un paramètre de valeur moyenne renormalisé dans un schéma de calcul ;
4. les relations au niveau arbre, qui ne sont pas des identités exactes à tous les ordres entre tous ces objets.

### Décision de contrôle

`G_F` donne un accès de précision à l’échelle électrofaible. Il ne constitue pas le processus physique qui produit le vide du secteur scalaire.

## 6. Dépendance d’échelle et de schéma

### 6.1 Masses de quarks

Les masses de quarks ne sont pas des observables directement mesurées comme la masse d’une particule asymptotique libre. Elles sont des paramètres renormalisés.

Dans le schéma `\overline{\mathrm{MS}}`, on écrit une masse courante :

```math
\overline m_q(\mu),
```

dont l’évolution satisfait une équation de groupe de renormalisation :

```math
\mu^2\frac{d\overline m_q(\mu)}{d\mu^2}
=-\gamma_m(\alpha_s(\mu))\,\overline m_q(\mu).
```

Une valeur de masse de quark sans schéma et sans échelle est donc incomplète.

### 6.2 Yukawa renormalisés

Les matrices de Yukawa du lagrangien quantique sont elles aussi des paramètres renormalisés. Leur valeur dépend du schéma et de l’échelle. La relation :

```math
y_f=\frac{\sqrt 2\,m_f}{v}
```

est exacte au niveau arbre dans une convention commune, mais reçoit des corrections de raccordement et doit être appliquée à des quantités définies de manière compatible au-delà du niveau arbre.

Pour les quarks, la forte dépendance QCD des masses courantes rend cette précaution indispensable. Pour les leptons chargés, la distinction entre masse de pôle et paramètre de Yukawa renormalisé subsiste, même si les effets sont moins spectaculaires.

### 6.3 CKM sous l’échelle faible

Le PDG indique que, sous l’échelle faible, les éléments CKM peuvent être traités comme constants dans la théorie effective usuelle, la dépendance d’échelle pertinente étant portée par les masses courantes et les opérateurs de dimension supérieure. Cette stabilité de basse énergie ne transforme pas une convention de phase en observable.

### Décision de contrôle

Les expressions « constante de Yukawa » et « masse de quark constante » ne sont acceptables qu’avec une qualification de régime, de schéma et d’échelle.

## 7. Histoire thermique : du langage de transition au crossover

Pour la masse physique du Higgs, le Modèle standard ne prédit pas une transition de phase électrofaible du premier ou du second ordre. Les simulations non perturbatives indiquent un crossover lisse.

La température pseudocritique est déterminée à partir du maximum de la susceptibilité du condensat invariant de jauge :

```math
\langle\Phi^\dagger\Phi\rangle,
```

avec :

```math
T_c\simeq 159.5\pm1.5\ \mathrm{GeV}
```

et une région de crossover étroite, d’environ quelques GeV.

### Correction de vocabulaire

Le récit suivant est trop brutal :

```text
à une température précise, la symétrie se brise et v apparaît.
```

La formulation contrôlée est :

```text
les observables thermodynamiques du secteur électrofaible évoluent continûment ;
le condensat invariant de jauge et sa susceptibilité permettent de repérer une région pseudocritique ;
le régime de basse température est relié sans singularité au régime de haute température.
```

Le symbole `v(T)` peut être utile dans une paramétrisation ou un calcul donné, mais il ne doit pas être présenté sans précaution comme un paramètre d’ordre unique, directement observable et indépendant de la jauge.

### Décision de contrôle

Il n’existe pas, dans le Modèle standard physique, un instant singulier où les masses et constantes « se forment » toutes ensemble. La résolution thermique décrit une transformation continue du régime et non une création ponctuelle des paramètres du lagrangien.

## 8. Accès expérimental aux Yukawa

Les masses permettent d’inférer des Yukawa dans le cadre du Modèle standard et avec des conventions de renormalisation précisées. Les processus de production et de désintégration du boson de Higgs testent en outre la structure des couplages Higgs–fermions.

Les résultats du LHC ont établi les couplages aux fermions de troisième génération — `t`, `b`, `\tau` — à un niveau compatible avec le Modèle standard. Une évidence existe également pour le canal muonique, tandis que les couplages au charme, à l’électron et aux quarks légers restent beaucoup moins directement contraints.

### Décision de contrôle

L’expression « Yukawa mesuré » recouvre plusieurs opérations :

- inférence depuis une masse ;
- test d’un taux de production ou de désintégration ;
- ajustement global de modificateurs de couplage ;
- hypothèses sur les autres couplages et sur la largeur totale du Higgs.

Une voie d’accès ne doit pas être confondue avec l’origine physique de la valeur obtenue.

## 9. Registre des propositions contrôlées

| Proposition | Verdict | Qualification requise |
|---|---|---|
| Le potentiel minimal permet un minimum non nul | Confirmé | niveau classique / arbre |
| `v` fixe l’échelle des masses `W` et `Z` | Confirmé | niveau arbre, corrections au-delà |
| Les Yukawa apparaissent après la brisure | Refusé | ils sont déjà dans le lagrangien symétrique |
| Les Yukawa produisent des matrices de masse après insertion de `v` | Confirmé | niveau arbre ; paramètres renormalisés au niveau quantique |
| La diagonalisation crée la hiérarchie des masses | Refusé | elle révèle les valeurs propres déjà encodées dans `Y_f` |
| CKM est le désalignement des rotations gauches | Confirmé | convention de rotation à préciser |
| Les neuf entrées complexes de CKM sont neuf constantes physiques | Refusé | quatre paramètres physiques pour trois générations |
| `G_F` détermine directement le mécanisme du vide | Refusé | accès basse énergie, non origine dynamique |
| `v=(\sqrt2G_F)^{-1/2}` est une identité universelle à tous les ordres | Refusé | relation d’arbre / définition d’échelle d’entrée ; corrections et schémas |
| Une masse de quark est un nombre indépendant du schéma | Refusé | schéma et échelle requis |
| Le régime électrofaible s’installe par transition abrupte | Refusé dans le Modèle standard physique | crossover lisse |
| La température pseudocritique et `v(0)` sont une même grandeur | Refusé | température thermodynamique et échelle de vide distinctes |

## 10. Contre-exemples à la fonction de fixité

### 10.1 Une entrée de matrice dépendant de la convention

La phase d’une entrée particulière de CKM peut être modifiée par rephasage des champs sans changer les prédictions physiques. Elle ne peut donc pas recevoir isolément une fonction de fixité physique.

Le candidat pertinent est un invariant ou une classe d’équivalence, par exemple `J`, les modules ou les triangles d’unitarité.

### 10.2 Un Yukawa sans échelle ni schéma

Le symbole `y_q` donné sans échelle ni schéma ne désigne pas une valeur physique suffisamment déterminée au niveau quantique. Le qualifier de constante simpliciter doit être refusé.

### 10.3 Une valeur ajustée dans un modèle arbitraire

Un coefficient numérique rendu fixe uniquement parce qu’un ajustement l’a gelé ne devient pas une constante physique. Il faut identifier une portée inter-situations, une relation nomologique ou une approximation effective contrôlée.

### Résultat

La notion de fonction de fixité possède un pouvoir d’exclusion seulement si elle porte sur un contenu invariant et si son domaine est spécifié. Elle échoue lorsqu’elle s’applique à une coordonnée conventionnelle, à un paramètre incomplet ou à une valeur simplement bloquée par procédure.

## 11. Ce que la vérification change dans le pilote

La description contrôlée distingue désormais quatre niveaux :

```text
Niveau 1 — paramètres et structures du lagrangien
potentiel, couplages de jauge, matrices de Yukawa

Niveau 2 — régime du vide et quantités dérivées
v, matrices de masse, masses de jauge

Niveau 3 — opérations de représentation
choix de jauge, rotations de base, diagonalisation, paramétrisations CKM

Niveau 4 — accès et reconstruction
muon, masses, désintégrations du Higgs, transitions faibles, fits globaux
```

L’histoire thermique traverse cette architecture sans être identique à son ordre logique : elle décrit l’évolution d’observables thermodynamiques et d’un condensat invariant de jauge à travers un crossover.

## 12. Conclusion de phase 2

La matière principale du corpus est physiquement récupérable, mais cinq corrections sont désormais obligatoires :

1. les Yukawa précèdent logiquement la brisure électrofaible ;
2. diagonaliser n’explique pas la texture des Yukawa ;
3. `v`, masses et Yukawa doivent être distingués selon le niveau arbre, le schéma et l’échelle ;
4. le contenu physique de CKM réside dans ses paramètres indépendants et invariants, non dans toute écriture matricielle ;
5. l’histoire thermique est un crossover décrit par des observables thermodynamiques, non un instant unique de formation des constantes.

> La vérification ne détruit pas l’architecture relationnelle. Elle la rend plus précise en séparant ce qui appartient au lagrangien, au régime du vide, aux opérations de représentation, à l’histoire thermique et aux voies d’accès.
