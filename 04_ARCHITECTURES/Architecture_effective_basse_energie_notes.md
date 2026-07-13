# Architecture effective basse energie - notes d'integration

## Statut apres le cycle G_F / M_W / alpha_s / Lambda_QCD / alpha_G / M_Pl

### 1. Fonction de la note

Cette note integre le resultat du cycle effectif basse energie dans le niveau des architectures inter-familles.

Elle ne remplace pas la synthese du cycle. Elle en extrait la consequence taxonomique principale :

```text
Architecture effective basse energie = architecture inter-familles confirmee
```

et non :

```text
nouvelle famille superieure
```

La note doit donc servir de reference courte pour les prochaines cartes consolidees.

Complement de reprise positive :

```text
04_ARCHITECTURES/Cercle2_lot2C_Effective_basse_energie_v0_1.md
```

La presente note reste la consolidation locale.

Le lot 2C fixe la formulation positive a privilegier pour les reprises
ulterieures.

### 2. Decision centrale

L'architecture effective basse energie est confirmee comme architecture robuste.

Elle articule principalement :

```text
Raccordement
Echelle
Couplage
Relation sous audit, lorsque des liaisons de regime doivent etre explicitees
```

Elle mobilise aussi des fonctions transversales :

```text
Validite
Seuil
Hierarchie
```

La decision de rang est :

```text
effectif = mode architectural de description
```

et non :

```text
effectif = famille fonctionnelle autonome
```

Cette decision evite de creer une famille trop large qui absorberait les coefficients, les echelles, les couplages courants et les limites de validite.

### 3. Definition locale proposee

Une architecture effective basse energie est une configuration inter-familles dans laquelle un regime limite stabilise des coefficients, couplages, echelles et fonctions de validite permettant de decrire un domaine sans resoudre explicitement toute la structure pertinente a plus haute energie, a plus courte distance ou dans un autre regime de description.

Cette definition repose sur quatre elements.

```text
1. Regime limite
2. Grandeurs stabilisees
3. Non-resolution explicite
4. Domaine de validite
```

Le point important est le quatrieme. Une description effective n'est pas seulement une description simplifiee. C'est une description dont le domaine de validite doit etre explicite.

Lecture v1.3 :

```text
l'architecture effective basse energie doit etre lue comme une trajectoire de stabilisation de validite,
non comme une famille et non comme une simple liste de constantes dependantes d'echelle.
```

### 4. Corpus stabilise

Le cycle a stabilise six grandeurs principales :

| Grandeur | Famille principale | Fonction dans l'architecture |
|---|---|---|
| G_F | Raccordement | Coefficient effectif de l'interaction faible basse energie |
| M_W | Echelle | Echelle electrofaible et seuil de validite de la theorie de Fermi |
| alpha_s(Q^2) | Couplage | Couplage courant de QCD selon l'echelle |
| Lambda_QCD | Echelle | Echelle dynamique du changement de regime QCD |
| alpha_G(E) | Couplage | Couplage gravitationnel effectif construit par rapport a une echelle |
| M_Pl | Echelle | Echelle de validite attendue de la gravitation effective basse energie |

Ces grandeurs n'appartiennent pas toutes a la meme famille. C'est precisement pourquoi le niveau architectural est necessaire.

### 5. Trois formes internes d'effectivite

Le cycle distingue trois formes d'effectivite.

#### 5.1 Integration d'un mediateur massif

Cas :

```text
G_F / M_W
```

Structure :

```text
theorie electrofaible avec W explicite
-> theorie de Fermi a quatre fermions
-> coefficient G_F
```

Lecture taxonomique :

```text
G_F : Raccordement
M_W : Echelle + Validite
```

Dans ce cas, le raccordement est local et porte par une constante identifiable.

#### 5.2 Flot de couplage et changement de regime

Cas :

```text
alpha_s(Q^2) / Lambda_QCD
```

Structure :

```text
couplage courant
+ echelle dynamique
+ separation perturbatif / non perturbatif
+ changement de degres de liberte pertinents
```

Lecture taxonomique :

```text
alpha_s(Q^2) : Couplage
Lambda_QCD   : Echelle
```

Dans ce cas, le raccordement n'est pas porte par une constante unique. Il est distribue dans l'architecture.

#### 5.3 Couplage dimensionne et suppression d'echelle

Cas :

```text
alpha_G(E) / M_Pl
```

Structure :

```text
G_N dimensionne
-> alpha_G(E) ~ (E / M_Pl)^2
-> suppression pour E << M_Pl
-> limite de validite attendue pres de l'echelle de Planck
```

Lecture taxonomique :

```text
alpha_G(E) : Couplage
M_Pl       : Echelle
G_N        : constante dimensionnee de depart, a lire par ses rapports
```

Dans ce cas, le raccordement est attendu plutot que completement stabilise : la relativite generale peut etre lue comme theorie effective basse energie, mais la completion quantique reste ouverte.

### 6. Distinction entre famille et architecture

La note confirme la regle generale :

```text
Une famille classe la fonction principale d'une grandeur.
Une architecture decrit l'articulation de plusieurs familles dans un regime.
```

Ainsi :

```text
G_F appartient a la famille Raccordement.
M_W appartient a la famille Echelle.
alpha_s(Q^2) appartient a la famille Couplage.
Lambda_QCD appartient a la famille Echelle.
alpha_G(E) appartient a la famille Couplage.
M_Pl appartient a la famille Echelle.
```

Mais ensemble, ces grandeurs appartiennent a :

```text
Architecture effective basse energie
```

Il ne faut donc pas ecrire :

```text
famille effective basse energie
```

sauf comme formule provisoire a corriger.

### 7. Statut de Raccordement

Le cycle clarifie la famille Raccordement.

Il existe un raccordement local :

```text
G_F
```

La grandeur porte directement la fonction de passage entre la theorie de Fermi et la theorie electrofaible.

Il existe aussi un raccordement architectural :

```text
alpha_s(Q^2) / Lambda_QCD
alpha_G(E) / M_Pl
```

Dans ces cas, le passage entre descriptions est distribue entre couplage, echelle, degres de liberte et domaine de validite.

Decision :

```text
Raccordement reste une famille lorsqu'une grandeur porte principalement cette fonction.
Raccordement peut devenir architectural lorsqu'aucune grandeur unique ne porte tout le passage.
```

### 8. Statut de Validite

La fonction Validite devient centrale dans cette architecture.

Elle repond a la question :

```text
dans quel domaine une description reste-t-elle applicable ?
```

Elle est plus precise que Seuil.

```text
Seuil   : ou se situe une limite ou zone de passage ?
Validite : quelle description vaut dans quel domaine ?
```

Cas principaux :

| Grandeur | Fonction de validite |
|---|---|
| M_W | Domaine de validite de la theorie de Fermi |
| Lambda_QCD | Domaine de validite des methodes perturbatives en QCD |
| M_Pl | Domaine de validite attendue de la gravitation effective basse energie |

Decision :

```text
Validite = fonction transversale centrale de l'architecture effective basse energie.
```

### 9. Statut de Seuil

La note confirme la retrogradation de Seuil.

```text
Seuil n'est pas une famille superieure.
```

Dans cette architecture :

```text
M_W        = echelle a fonction seuil pour la theorie de Fermi
Lambda_QCD = echelle dynamique a fonction seuil perturbatif / non perturbatif
M_Pl       = echelle a fonction seuil faible ou attendue
```

Le classement principal reste :

```text
Echelle
```

Formulation a retenir :

> Un seuil est souvent la maniere dont une echelle devient visible depuis une description qui cesse d'etre suffisante.

### 10. Statut de Hierarchie

La fonction Hierarchie est egalement renforcee.

Elle apparait sous plusieurs formes :

```text
E << M_W
Q par rapport a Lambda_QCD
E << M_Pl
```

Mais elle ne doit pas devenir une famille.

Decision :

```text
Hierarchie = fonction transversale forte
```

et non :

```text
famille Hierarchie
```

La formulation corrigee est :

```text
couplage ou echelle a fonction hierarchique
```

et non :

```text
constante de hierarchie d'echelle
```

### 11. Ce que "basse energie" veut dire ici

Le cycle montre que l'expression "basse energie" change de sens selon le secteur.

| Secteur | Sens de basse energie | Effet |
|---|---|---|
| Interaction faible | E << M_W | Description locale simplifiee |
| QCD | Q proche ou inferieur a Lambda_QCD | Entree dans le non perturbatif |
| Gravitation | E << M_Pl | Suppression du couplage quantique gravitationnel |

Il faut donc eviter :

```text
basse energie = simplification uniforme
```

La bonne formulation est :

```text
basse energie = regime dans lequel certains degres de liberte, corrections ou descriptions plus completes ne sont pas traites explicitement de la meme maniere.
```

### 12. Formule compacte de l'architecture

Formule courte :

```text
Architecture effective basse energie =
Raccordement
+ Echelle de validite
+ Couplage de regime
+ Fonctions Validite / Seuil / Hierarchie
```

Forme developpee :

```text
Architecture effective basse energie =
{G_F, M_W, alpha_s(Q^2), Lambda_QCD, alpha_G(E), M_Pl}
+ {Raccordement, Echelle, Couplage}
+ {Validite, Seuil, Hierarchie}
+ {regimes de description adaptes}
```

Precision :

```text
le raccordement peut etre local, distribue ou attendu.
```

### 13. Limites de l'architecture

Cette architecture ne doit pas tout absorber.

Elle ne classe pas automatiquement :

```text
toute grandeur dependante d'une echelle
toute approximation
toute constante dimensionnee
toute transition de regime
```

Une grandeur appartient a cette architecture seulement si son role concerne explicitement :

```text
un regime limite de description
une non-resolution explicite
une echelle ou fonction de validite
un raccordement local, distribue ou attendu
```

La note ne resout pas :

```text
l'origine des constantes
la completion quantique de la gravitation
la dynamique profonde des couplages
la nature ultime des seuils
```

Elle fixe seulement le statut methodologique de l'architecture.

### 14. Points reportes dans les cartes consolidees

Les cartes consolidees ulterieures doivent conserver cinq decisions.

```text
1. Architecture effective basse energie est confirmee comme architecture inter-familles.
2. Effectif ne doit pas devenir une famille superieure.
3. Raccordement peut etre local ou architectural.
4. Validite devient une fonction transversale centrale.
5. Seuil et Hierarchie restent des fonctions transversales.
```

Elles doivent aussi distinguer les trois formes internes :

```text
effectivite par integration d'un mediateur massif
effectivite par flot de couplage et changement de regime
effectivite par couplage dimensionne et suppression d'echelle
```

### 15. Formule de travail

Formule longue :

> Une architecture effective basse energie stabilise des grandeurs qui rendent operatoire un regime de description en indiquant ce qui est condense, non resolu, courant, non perturbatif, supprime ou seulement attendu au-dela du domaine de validite.

Formule courte :

> L'effectivite stabilise moins une valeur qu'une validite de description.

### 16. Statut apres resynchronisation

Suites produites ensuite :

```text
1. integration dans les cartes consolidees ;
2. ouverture prudente du cycle cosmologique ;
3. refonte v1.2 par rangs, roles et dependances.
4. reprise des cycles physiques selon la methode v1.3.
```

La prudence cosmologique reste methodologique, mais elle n'est plus une attente documentaire : le cycle cosmologique et son stress test ont ete produits puis repris.

Le point conserve est que la cosmologie melange :

```text
constantes
parametres de modele
observables reconstruites
conditions initiales
tensions de donnees
```

Le travail ulterieur a aussi consolide les architectures deja confirmees :

```text
saveur-Higgs
metrologique SI
effective basse energie
```

Document de refonte produit ensuite :

```text
05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_2_refonte.md
```

Audit transversal produit ensuite :

```text
05_CARTES_ET_SYNTHESES/Audit_resynchronisation_theorique_v0_1.md
```

### 17. Documents sources internes

Documents internes a relier a cette note :

```text
PROJECT_BRIEF.docx
Carte consolidee v0.8.docx
Cycle effectif basse energie v0.1.docx
Cycle effectif basse energie v0.2.docx
Cycle effectif basse energie v0.3.docx
02_CYCLES_PHYSIQUES/06_Cycle_effectif_basse_energie/Cycle_effectif_basse_energie_v0_4_alphaG_MPl.md
02_CYCLES_PHYSIQUES/06_Cycle_effectif_basse_energie/Synthese_cycle_effectif_basse_energie_v0_1.md
01_CADRE_METHODOLOGIQUE/Note_synthese_methodologique_v1_3_pre_familial_et_temporalite.md
```
