# Cycle effectif basse energie v0.4

## Fiche 4 : alpha_G(E) et M_Pl

### 1. Fonction de la fiche

Les trois fiches precedentes ont teste deux formes d'effectivite basse energie.

Premiere forme :

```text
G_F / M_W
```

effectivite par integration d'un mediateur massif.

Deuxieme forme :

```text
alpha_s(Q^2) / Lambda_QCD
```

effectivite par flot de couplage et changement de regime.

La presente fiche teste une troisieme forme :

```text
alpha_G(E) / M_Pl
```

effectivite gravitationnelle par couplage dimensionne, suppression d'echelle et limite de validite attendue.

La question directrice est :

> Comment une interaction extremement faible a basse energie peut-elle signaler une limite d'effectivite a tres haute energie ?

La fiche doit eviter deux erreurs.

Premiere erreur :

```text
G_N = constante comparable directement a alpha
```

Deuxieme erreur :

```text
M_Pl = frontiere nette de la physique connue
```

La formulation correcte est plus prudente :

```text
G_N est une constante dimensionnee ; son contenu de couplage devient lisible a travers des rapports sans dimension, comme alpha_G(E) ~ (E / M_Pl)^2.
M_Pl est une echelle de validite attendue, non une porte mathematique nette.
```

### 2. Identification

Grandeurs :

```text
G_N
alpha_G(E)
M_Pl
```

Noms :

```text
G_N        constante gravitationnelle de Newton
alpha_G(E) couplage gravitationnel effectif sans dimension a l'echelle E
M_Pl       masse de Planck non reduite
```

Types logiques :

```text
G_N        constante dimensionnee
alpha_G(E) couplage sans dimension construit a partir d'une echelle d'energie
M_Pl       echelle d'energie / masse de reference gravitationnelle
```

Familles principales :

```text
alpha_G(E) : Couplage
M_Pl       : Echelle
G_N        : constante dimensionnee de depart, a traiter par ses rapports et ses effets
```

Sous-types :

```text
alpha_G(E) : couplage gravitationnel effectif de regime
M_Pl       : echelle de validite attendue / echelle gravitationnelle de reference
```

Fonctions transversales :

```text
Validite
Hierarchie
Seuil, seulement au sens faible d'une zone attendue de changement de description
```

Architecture :

```text
Architecture effective basse energie
```

### 3. Regime de definition physique

La gravitation est decrite avec une tres grande robustesse, dans un vaste domaine classique, par la relativite generale. Ce domaine inclut notamment la dynamique du systeme solaire, les lentilles gravitationnelles, les ondes gravitationnelles, les trous noirs classiques et la cosmologie relativiste.

Mais le cas gravitationnel differe fortement des cas precedents.

Dans le cas faible :

```text
G_F
```

condense a basse energie l'effet de l'echange du boson W.

Dans le cas QCD :

```text
alpha_s(Q^2)
```

varie avec l'echelle et produit une separation entre regime perturbatif et regime non perturbatif.

Dans le cas gravitationnel, le point central est encore different :

```text
G_N
```

est dimensionnee. En unites naturelles, ou hbar = c = 1, elle a la dimension :

```text
[G_N] = E^-2
```

Cela signifie que la force quantique effective de la gravitation ne se lit pas dans un nombre pur fixe une fois pour toutes, mais dans un rapport d'echelle.

La forme schematique est :

```text
alpha_G(E) ~ G_N E^2
```

ou, avec la masse de Planck :

```text
alpha_G(E) ~ (E / M_Pl)^2
```

La gravitation basse energie est donc un regime ou :

```text
E << M_Pl
```

et ou les corrections quantiques gravitationnelles sont fortement supprimees.

### 4. Regime d'acces epistemique

Le regime d'acces ne doit pas etre confondu avec le regime physique.

Le regime physique de la fiche est :

```text
gravitation basse energie / basse courbure, lue comme domaine effectif
```

Le regime d'acces de G_N est tout autre :

```text
mesures gravitationnelles de precision, ajustements CODATA, experiences de laboratoire
```

Le cas de G_N est particulier dans les constantes physiques : sa valeur recommandee reste beaucoup moins precise que celle de nombreuses constantes atomiques ou electrodynamiques. La table CODATA 2022 donne :

```text
G_N = 6.67430(15) x 10^-11 m^3 kg^-1 s^-2
```

avec une incertitude relative de l'ordre de :

```text
2.2 x 10^-5
```

Le PDG 2025 donne aussi la forme naturelle :

```text
G_N / (hbar c) = 6.70883(15) x 10^-39 (GeV/c^2)^-2
```

Cette forme rend plus visible le statut de couplage gravitationnel microscopique : pour une masse exprimee en GeV/c^2, le couplage sans dimension est obtenu en multipliant par le carre de cette masse.

Pour un proton :

```text
alpha_G(p) = G_N m_p^2 / (hbar c) ~ 5.9 x 10^-39
```

Pour un electron :

```text
alpha_G(e) = G_N m_e^2 / (hbar c) ~ 1.75 x 10^-45
```

Ces nombres ne disent pas que la gravitation serait "faible en soi" dans tous les regimes. Ils disent que, pour des particules ordinaires, le rapport a l'echelle de Planck est extremement petit.

### 5. Pourquoi G_N seul n'est pas le bon objet principal

Une constante dimensionnee possede une valeur numerique dependante du systeme d'unites. Dire que :

```text
G_N est petit
```

n'a pas de contenu absolu sans reference a une comparaison.

Le contenu physique devient plus propre lorsqu'on utilise des grandeurs sans dimension :

```text
alpha_G(m) = G_N m^2 / (hbar c)
```

ou, pour une energie caracteristique E :

```text
alpha_G(E) = G_N E^2 / (hbar c^5)
```

ce qui revient a :

```text
alpha_G(E) = (E / (M_Pl c^2))^2
```

En unites naturelles :

```text
alpha_G(E) = (E / M_Pl)^2
```

La famille principale de alpha_G(E) est donc :

```text
Couplage
```

mais avec une qualification indispensable :

```text
couplage gravitationnel effectif de regime, construit par rapport a une echelle d'energie
```

Ce n'est pas un couplage courant au meme sens que alpha_s(Q^2). Dans la lecture minimale de cette fiche, la croissance de alpha_G(E) vient d'abord du caractere dimensionne de G_N et du rapport d'echelle E / M_Pl.

### 6. M_Pl comme echelle de validite attendue

La masse de Planck non reduite est definie par :

```text
M_Pl = sqrt(hbar c / G_N)
```

CODATA 2022 donne :

```text
M_Pl = 2.176434(24) x 10^-8 kg
M_Pl c^2 = 1.220890(14) x 10^19 GeV
```

Dans une convention frequente en theorie des champs gravitationnelle, on utilise aussi la masse de Planck reduite :

```text
Mbar_Pl = M_Pl / sqrt(8 pi)
```

Cette difference de convention est importante numeriquement, mais elle ne change pas le statut methodologique de la fiche : il s'agit dans les deux cas d'une echelle de comparaison gravitationnelle.

La famille principale de M_Pl est :

```text
Echelle
```

Sous-type :

```text
echelle de validite attendue
```

Fonctions transversales :

```text
Validite
Hierarchie
Seuil faible
```

La fonction de seuil doit rester prudente. M_Pl ne marque pas une frontiere nette ou une nouvelle physique serait automatiquement atteinte a une valeur exacte. Elle marque plutot la region ou la description effective basse energie de la gravitation est attendue comme insuffisante.

Formulation :

> M_Pl est d'abord une echelle gravitationnelle de reference ; elle devient seuil seulement lorsqu'on l'utilise pour indiquer la limite attendue de validite de la description effective basse energie.

### 7. Gravitation comme theorie effective basse energie

La relativite generale peut etre lue comme une theorie effective des champs a basse energie. Cette lecture ne pretend pas fournir une theorie complete de la gravitation quantique. Elle dit plutot ceci :

```text
les effets fiables du bas domaine d'energie peuvent etre organises sans connaitre la completion haute energie
```

Dans cette perspective, la relativite generale reste utilisable dans le domaine :

```text
E << M_Pl
```

ou, plus generalement :

```text
faibles courbures / grandes longueurs / energies tres inferieures a l'echelle de Planck
```

Les contributions inconnues de la theorie haute energie sont alors absorbees dans des termes locaux de plus haute dimension, fortement supprimes a basse energie.

Cette structure donne une nouvelle forme d'effectivite :

```text
effectivite par suppression d'echelle
```

et non seulement :

```text
effectivite par integration d'un mediateur massif
```

ni :

```text
effectivite par changement de regime non perturbatif
```

### 8. Difference avec G_F / M_W

Le cas faible possede une structure de raccordement claire :

```text
theorie electrofaible avec boson W explicite
        -> theorie de Fermi a quatre fermions
        -> coefficient G_F
```

Dans ce cas :

```text
G_F : Raccordement
M_W : Echelle / Validite
```

Le cas gravitationnel est plus difficile.

Il n'existe pas, dans le cadre standard stabilise, une theorie haute energie complete dont G_N serait simplement le residu basse energie de la meme maniere que G_F est le residu de l'echange du W.

La structure correcte est donc :

```text
relativite generale basse energie
        -> theorie effective
        -> completion quantique inconnue ou ouverte
```

La famille Raccordement n'est pas portee ici par une constante unique comparable a G_F. Le raccordement est architectural et incomplet : M_Pl signale la region ou un raccordement plus profond est attendu, mais ne fournit pas a lui seul ce raccordement.

Formulation :

> Dans le cas gravitationnel, l'architecture effective basse energie ne raccorde pas une theorie effective a une theorie complete deja stabilisee ; elle indique le domaine ou une telle completion devient attendue.

### 9. Difference avec alpha_s(Q^2) / Lambda_QCD

Le cas QCD montre un couplage courant et une echelle dynamique :

```text
alpha_s(Q^2) : couplage courant
Lambda_QCD   : echelle dynamique
```

Le regime basse energie en QCD n'est pas un regime de suppression ; il correspond a l'entree dans le non perturbatif.

Le cas gravitationnel est inverse sous cet aspect :

```text
E << M_Pl  -> alpha_G(E) tres petit
E ~ M_Pl  -> gravitation quantique attendue
```

La basse energie gravitationnelle est donc un regime de suppression du couplage quantique effectif, non un regime de couplage fort.

Ce contraste est central :

```text
QCD basse energie         = couplage fort / confinement / non perturbatif
gravitation basse energie = couplage quantique supprime / EFT robuste
```

Il confirme que l'expression "basse energie" ne designe pas une structure unique. Elle doit toujours etre qualifiee par le type de theorie et par les degres de liberte pertinents.

### 10. Fonction de validite

La fonction de validite est la fonction transversale principale de cette fiche.

Pour la theorie de Fermi :

```text
M_W
```

indique quand l'interaction locale a quatre fermions cesse d'etre suffisante.

Pour QCD :

```text
Lambda_QCD
```

indique la region ou les methodes perturbatives cessent d'etre adaptees.

Pour la gravitation :

```text
M_Pl
```

indique la region ou la relativite generale lue comme theorie effective basse energie est attendue comme insuffisante.

La validite ne signifie pas la meme chose dans les trois cas.

```text
M_W        : validite d'une approximation locale sans W explicite
Lambda_QCD : validite relative des descriptions perturbatives
M_Pl       : validite attendue de la gravitation classique / effective basse energie
```

La fiche confirme donc la fonction transversale :

```text
Validite
```

mais sous trois formes distinctes.

### 11. Fonction de hierarchie

Le couple :

```text
alpha_G(E) / M_Pl
```

stabilise une hierarchie majeure :

```text
energies ordinaires << echelle de Planck
```

Cette hierarchie explique pourquoi la gravitation quantique est negligeable dans les processus atomiques, nucleaires, hadroniques ou electrofaibles ordinaires.

Mais la faiblesse microscopique ne doit pas etre confondue avec une faiblesse universelle.

A l'echelle macroscopique, la gravitation peut dominer parce que :

```text
les masses s'additionnent
la matiere ordinaire est globalement neutre electriquement
les effets gravitationnels ont une portee longue
```

La bonne lecture est donc multi-echelle :

```text
microscopique ordinaire : gravitation negligeable
macroscopique / cosmologique : gravitation structurante
Planckien : gravitation quantique attendue
```

La fonction transversale est :

```text
Hierarchie
```

mais elle ne doit pas devenir une famille nouvelle.

Decision :

```text
ancienne idee : constante de hierarchie d'echelle
statut v0.8    : fonction transversale de hierarchie + echelle de validite + couplage effectif
```

### 12. Stabilisation empirique

La stabilisation empirique du cas gravitationnel est double.

D'un cote, la relativite generale est extremement robuste dans son domaine classique. Les observations et experiences disponibles stabilisent fortement la gravitation comme cadre effectif basse energie et basse courbure.

De l'autre cote, la constante G_N elle-meme est beaucoup moins precisement determinee que de nombreuses constantes microscopiques. Sa valeur CODATA possede une incertitude relative de l'ordre de 10^-5, tres loin de la precision de alpha, des masses leptoniques ou de certaines constantes definissantes du SI.

La stabilisation de M_Pl depend donc de G_N :

```text
M_Pl = sqrt(hbar c / G_N)
```

Comme hbar et c sont exacts dans le SI revise, l'incertitude de M_Pl vient essentiellement de G_N.

Formulation :

```text
G_N        : mesure difficile, stabilisation empirique moins precise
M_Pl       : echelle derivee, incertitude dominee par G_N
alpha_G(E) : couplage sans dimension construit, tres fortement supprime pour E << M_Pl
```

### 13. Stabilisation conventionnelle

Ni G_N, ni M_Pl, ni alpha_G(E) ne sont des constantes definissantes du SI.

Certes :

```text
c
h
hbar = h / (2 pi)
```

sont exacts dans le SI actuel.

Mais :

```text
G_N
```

reste mesure.

Donc :

```text
M_Pl
```

n'est pas exacte par convention.

Stabilisation conventionnelle :

```text
non concernee
```

ou, plus precisement :

```text
derivee de constantes dont certaines sont exactes, mais limitee par G_N mesure
```

### 14. Lecture par la matrice v0.8

| Critere | Lecture pour alpha_G(E) | Lecture pour M_Pl |
|---|---|---|
| Grandeur | alpha_G(E) | M_Pl |
| Type logique | Couplage sans dimension construit a partir d'une echelle d'energie | Echelle d'energie / masse de reference |
| Dimension | Sans dimension | [E] ou masse |
| Famille principale | Couplage | Echelle |
| Sous-type local | Couplage gravitationnel effectif de regime | Echelle de validite attendue |
| Fonction transversale | Validite, hierarchie | Validite, hierarchie, seuil faible |
| Fonction architecturale | Non principale | Non principale |
| Regime de definition physique | Gravitation basse energie lue par rapport a une echelle E | Domaine ou la gravitation quantique devient attendue |
| Regime d'acces epistemique | Construction a partir de G_N et de l'echelle choisie | Grandeur derivee de G_N, hbar et c |
| Dependance d'echelle | Essentielle : alpha_G(E) ~ (E/M_Pl)^2 | Non couplage courant ; echelle de reference |
| Stabilisation empirique | Forte suppression pour E << M_Pl ; depend de G_N pour sa normalisation | Derivee, incertitude dominee par G_N |
| Stabilisation conventionnelle | Non concernee | Non exacte par convention, car G_N est mesure |
| Architecture | Effective basse energie / gravitation | Effective basse energie / gravitation |
| Limite | N'est pas un couplage courant QCD ; ne se mesure pas comme alpha | N'est pas une frontiere nette ni une theorie de gravitation quantique |

### 15. Ce que le cas gravitationnel confirme

Le cas :

```text
alpha_G(E) / M_Pl
```

confirme que l'architecture effective basse energie ne se reduit pas aux deux formes deja testees.

Apres :

```text
G_F / M_W
```

elle incluait :

```text
effectivite par integration d'un mediateur massif
```

Apres :

```text
alpha_s(Q^2) / Lambda_QCD
```

elle incluait :

```text
effectivite par flot de couplage et changement de regime
```

Avec :

```text
alpha_G(E) / M_Pl
```

elle inclut maintenant :

```text
effectivite par couplage dimensionne et suppression d'echelle
```

La formulation enrichie devient :

> Une architecture effective basse energie stabilise les grandeurs qui permettent de decrire ce qu'un regime donne rend accessible, integrable, courant, non resolu, non perturbatif ou fortement supprime par hierarchie d'echelle.

### 16. Ce que le cas gravitationnel corrige

Le cas gravitationnel corrige trois confusions possibles.

Premiere confusion :

```text
G_N serait comparable directement a alpha
```

Correction :

```text
G_N est dimensionnee ; la comparaison physique passe par alpha_G(E), alpha_G(m), ou d'autres rapports sans dimension.
```

Deuxieme confusion :

```text
M_Pl serait une frontiere nette
```

Correction :

```text
M_Pl est une echelle de validite attendue, dependante d'une convention de Planck reduite ou non reduite, et non une limite experimentale directement franchie.
```

Troisieme confusion :

```text
basse energie signifierait toujours simplification du meme type
```

Correction :

```text
basse energie peut signifier interaction locale simplifiee, entree dans le non perturbatif, ou suppression d'un couplage dimensionne selon la theorie consideree.
```

### 17. Decision apres la fiche

Apres les quatre fiches du cycle, l'architecture effective basse energie est nettement renforcee.

Elle articule maintenant au moins trois formes d'effectivite :

| Forme | Cas | Grandeurs principales |
|---|---|---|
| Integration d'un mediateur massif | Interaction faible basse energie | G_F / M_W |
| Flot de couplage et changement de regime | QCD | alpha_s(Q^2) / Lambda_QCD |
| Couplage dimensionne et suppression d'echelle | Gravitation | alpha_G(E) / M_Pl |

Le noyau architectural peut etre reformule ainsi :

```text
Architecture effective basse energie =
Raccordement local
+ Echelle de validite
+ Couplage de regime
+ Fonction de validite
+ Fonction de hierarchie
```

avec une precision :

```text
le raccordement peut etre porte par une constante unique, comme G_F,
ou etre seulement architectural, comme dans le cas QCD et dans le cas gravitationnel.
```

### 18. Statut apres synthese

La suite logique a ete produite :

```text
Synthese_cycle_effectif_basse_energie_v0_1.md
```

Objectif realise :

```text
stabiliser la forme finale de l'architecture effective basse energie apres les quatre cas GF, MW, alpha_s/Lambda_QCD et alpha_G/M_Pl.
```

Cette synthese a tranche trois points :

```text
1. l'architecture effective basse energie est robuste comme architecture inter-familles ;
2. plusieurs sous-types internes d'effectivite doivent etre distingues ;
3. "effectif" ne doit pas devenir une famille superieure.
```

Lecture v1.3 :

```text
alpha_G(E) / M_Pl confirme une trajectoire de stabilisation par suppression d'echelle,
avec Validite et Hierarchie comme roles contextuels,
sans creer une famille gravitationnelle effective autonome.
```

### 19. Sources de controle

Sources utilisees pour verifier les valeurs et garder le niveau de prudence attendu :

- NIST/CODATA, `Fundamental Physical Constants - Complete Listing, 2022 CODATA adjustment`, https://physics.nist.gov/cuu/Constants/Table/allascii.txt
- Mohr, Newell, Taylor, Tiesinga, `CODATA recommended values of the fundamental physical constants: 2022`, Journal of Physical and Chemical Reference Data 54, 033105 (2025), https://physics.nist.gov/cuu/pdf/JPCRD2022CODATA.pdf
- Particle Data Group, `Physical Constants`, Review of Particle Physics 2025, https://ccwww.kek.jp/pdg/2025/reviews/rpp2025-rev-phys-constants.pdf
- Donoghue, `Quantum General Relativity and Effective Field Theory`, arXiv:2211.09902, https://arxiv.org/abs/2211.09902
- Uzan, `Fundamental constants: from measurement to the universe, a window on gravitation and cosmology`, arXiv:2410.07281, https://arxiv.org/abs/2410.07281
