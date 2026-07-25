# Matrice figement, datation et migration du réglage v0.3

## 0. Statut

```text
statut : instrument transversal soumis à relecture ;
rang : exploré — produit, non validé, révisable sans coût ;
date : 25 juillet 2026 ;
remplace : v0.1 et v0.2 du même jour, non versionnées dans le dépôt et
           remplacées avant intégration ;
fonction : donner à chaque maintien son mode de figement, sa date reconstruite et
           le lieu vers lequel son réglage a migré ;
appuis internes : cycle 1 (couplages, échelles et QCD), cycle 3 (accès),
                  cycle 7 (cosmologie), cycle 8 (Système international),
                  cycle 9 (ajustement fin), cycle 10 (quasi-fixité dynamique) ;
ne vaut pas : résultat physique nouveau, taxonomie des constantes, thèse sur
              l'origine des valeurs, ouverture ontologique, ni verdict sur
              T1, T2 ou T3 ;
portée de l'énoncé : physique pour les colonnes 1 et 2, épistémologique pour la
                     colonne 3 ; ontologique : non engagée.
```

Modifications cumulées par rapport à la v0.1 :

```text
ajout du mode M4 — changement d'accès sans changement d'objet ;
ajout de la ligne gravitationnelle, porteuse de M4 ;
ajout d'une section de test de l'instrument par le figement distribué du pion ;
correction de la formulation énergétique de la ligne gravitationnelle ;
substitution d'un exemple relativiste à l'exemple métrologique en section 8 ;
inscription explicite de ce qui n'entre pas dans cette version, et pourquoi ;
ajout de la ligne supraconductrice comme épreuve de la généralité de M3 ;
scission de la colonne des dates en date inférée unique et date réalisée
  répétable, conséquence directe de la ligne supraconductrice.
```

Cette matrice ne classe pas des constantes. Elle classe des **opérations de
figement** et n'admet une ligne que si les trois colonnes reçoivent une réponse
déterminée, la troisième pouvant être `non établie`.

## 1. Distinction directrice de l'instrument

```text
mode de figement : ce qui fait qu'un maintien cesse de dépendre de la variable
                   qui le faisait varier ;
date : instant, dans une histoire thermique reconstruite, où cette cessation
       devient effective ;
migration du réglage : lieu du dispositif théorique où la contingence
                       antérieurement portée par la valeur se reporte.
```

## 2. Les quatre modes admis

```text
M1 — épuisement des seuils : la variable cesse d'agir faute de contributeurs ;
M2 — changement de régime : la variable continue d'agir mais la description
     valide change ;
M3 — constitution des objets : ce n'est pas une valeur qui change, c'est un
     porteur qui apparaît ;
M4 — changement d'accès sans changement d'objet : ni la valeur ni l'objet ne
     changent, mais la voie par laquelle l'objet devient disponible cesse ou
     devient disponible à une date déterminée.
```

`M4` est la seule catégorie dont la date ne porte pas sur un figement. Elle
mobilise la distinction établie par les cycles 3 et 7 entre l'objet et l'accès.
Elle ne doit pas servir de case d'accueil pour les cas mal renseignés : son
emploi exige que l'objet soit nommé, que les deux accès soient nommés, et que
l'un des deux soit daté.

## 3. Typage du chemin des dates

```text
type de chemin : inférentiel et computationnel ;
statut : les dates ne sont pas observées, elles sont reconstruites dans le modèle
         cosmologique standard couplé à l'histoire thermique du Modèle standard ;
conséquence : une révision du modèle déplace la date sans invalider le mode ;
verdict disponible : non établie.
```

Aucune de ces dates n'est une mesure. Les traiter comme telles reproduirait
exactement la confusion que la présente matrice sert à empêcher.

## 4. Matrice

| Maintien | Mode | Date reconstruite | Migration du réglage |
|---|---|---|---|
| Couplage électromagnétique effectif aux basses énergies, stabilisé à sa valeur terminale | `M1` — épuisement des seuils chargés | Autour de l'annihilation des paires électron-positron, échelle thermique voisine de 0,5 MeV, quelques secondes après le début reconstruit, avant la nucléosynthèse | Vers le spectre des masses chargées, dont le seuil le plus bas fixe l'arrêt, et vers la valeur du couplage à une échelle de référence, qui reste libre — **hypothèse à éprouver** |
| Échelle hadronique et masses des états liés de la chromodynamique | `M2` — changement de régime, du perturbatif au non perturbatif | Transition de confinement, échelle thermique voisine de 150 à 160 MeV, ordre de la dizaine de microsecondes | Vers le couplage sans dimension pris à une échelle de référence et le contenu en saveurs, la masse du proton n'étant pas un paramètre libre mais une transmutation dimensionnelle — **hypothèse à éprouver** |
| Valeur du vide électrofaible, constante de Fermi, masses au repos des particules élémentaires | `M3` — constitution des objets | Transition électrofaible, échelle thermique voisine de 160 GeV, ordre de la dizaine de picosecondes | Vers les paramètres du potentiel scalaire, les couplages de Yukawa et, selon le cycle 10, les conditions initiales et la fonction de couplage — **partiellement acquis en local, non généralisé** |
| Couplage gravitationnel : accès par la masse au repos contre accès par l'énergie-impulsion | `M4` — changement d'accès sans changement d'objet | L'objet n'est pas daté ; ce qui est daté est la disponibilité de l'accès par la masse au repos, subordonnée à la transition électrofaible, puis au confinement pour les masses hadroniques | Vers l'écart entre objet et accès, le plus large du corpus : le rôle cosmologique du couplage n'est jamais qu'inféré par les équations d'évolution — **hypothèse à éprouver** |
| Ouverture du gap supraconducteur et masse effective du photon dans le milieu | `M3` — constitution des objets | **Date réalisée répétable** : franchissement de la température critique de l'échantillon, observable directement et reproductible à volonté | Vers les paramètres du matériau — fréquence de coupure phononique, densité d'états au niveau de Fermi, couplage électron-phonon — donc vers un maintien local et non universel — **hypothèse à éprouver** |
| Contre-exemple recherché : stabilisation dynamique réduisant le nombre de paramètres libres sans en introduire d'autres | non renseigné | non renseignée | `non établie` — **à chercher activement** |

### 4.1 Note sur la ligne gravitationnelle

La gravitation ne couple pas à la masse mais au tenseur énergie-impulsion,
c'est-à-dire à l'énergie, à l'impulsion et aux pressions. Le rayonnement gravite,
et il commande l'expansion pendant toute l'ère radiative : la densité invoquée
avant la transition électrofaible est une densité d'énergie et non une densité de
masse déguisée. Ce qui devient indisponible au-dessus du seuil n'est donc pas la
gravitation, mais un accès à elle — la formulation par une force entre masses, la
particule d'épreuve de masse donnée, la comparaison d'une masse inertielle et
d'une masse grave. Deux réserves accompagnent cette ligne. D'une part, dans le
plasma symétrique les particules acquièrent des masses thermiques de l'ordre du
couplage multiplié par la température : elles ne sont pas dépourvues d'inertie,
elles sont massives autrement. D'autre part, la question d'un couplage
gravitationnel courant relève du programme de la sûreté asymptotique et demeure
`non établie` ; la relativité générale n'est pas perturbativement renormalisable
et aucun point fixe n'est acquis.

Cette ligne est aussi la seule dont l'objet n'a pas rejoint le régime
définitionnel de 2019, ses déterminations restant discordantes à quelques dizaines
de millionièmes en valeur relative. Elle est donc le point où la question de
l'arbitrage de la discordance et le cycle 8 portent sur le même objet.

### 4.2 Note sur la ligne supraconductrice

Cette ligne n'entre pas comme analogie pédagogique, ce qu'interdit la dixième
règle de contribution, mais comme mécanisme de même classe, avec sa filiation
documentée. La direction du transport historique est d'ailleurs l'inverse de
celle que l'on suppose habituellement : le potentiel de Ginzburg et Landau
(1950) a la forme du potentiel scalaire, Nambu traite l'invariance de jauge et
les quasi-particules dans la théorie de la supraconductivité en 1960, et
Anderson publie en 1963 le texte où le photon acquiert une masse effective dans
le milieu, avant les articles de 1964 sur le mécanisme de brisure électrofaible.
La supraconductivité est le site où le mécanisme a été pensé, non un cas
d'application dérivé.

Son intérêt pour l'instrument est ailleurs, et il est plus fort que prévu. Dans
le secteur électrofaible, `M3` produit des valeurs tenues pour universelles ;
dans un supraconducteur, le même mode produit un maintien dépendant du
matériau. Si ce contraste tient, alors `M3` ne détermine pas à lui seul
l'universalité du maintien qu'il institue, et la troisième colonne doit
distinguer une migration vers des paramètres universels d'une migration vers des
paramètres contingents. C'est par là que cette ligne peut faire échouer `M3`.

Parenté formelle à signaler comme telle, et non comme identité : dans la théorie
de Bardeen, Cooper et Schrieffer, la température critique dépend
exponentiellement de l'inverse du couplage, structure identique à celle par
laquelle l'échelle hadronique sort d'un couplage sans dimension. Les mécanismes
restent distincts — équation du gap avec coupure phononique d'un côté, groupe de
renormalisation de l'autre — et cette ligne fait donc écho à la migration
inscrite en `M2` sans s'y réduire.

### 4.3 Conséquence sur la colonne des dates

L'entrée de cette ligne scinde la deuxième colonne :

```text
date inférée unique : reconstruite dans un modèle, non répétable, non observée ;
date réalisée répétable : franchie sur un échantillon, observée, reproductible.
```

Cette scission est le gain principal de la version : elle fournit le critère de
databilité à deux régimes qui manquait à la matrice temporelle. Elle en est aussi
le risque principal, inscrit en section 10 : si les deux régimes n'ont rien de
commun, la colonne cesse d'être une colonne et l'instrument se dédouble.

## 5. Test de l'instrument : le figement distribué

Le pion n'est pas versé comme cas mais comme épreuve de la matrice elle-même. Sa
masse au carré est proportionnelle au produit des masses des quarks légers par le
condensat chiral, selon la relation de Gell-Mann, Oakes et Renner : un seul
maintien reçoit donc sa valeur de deux mécanismes distincts, datés séparément.

| Contribution | Mode | Date reconstruite |
|---|---|---|
| Masses des quarks légers, par les couplages de Yukawa | `M3` | Transition électrofaible |
| Condensat chiral, par la brisure de symétrie chirale | `M2` | Transition de la chromodynamique |

```text
question posée à l'instrument :
la matrice sait-elle traiter un figement distribué sur deux événements,
ou exige-t-elle une ligne par mécanisme et perd-elle alors l'objet ?

verdict : non rendu ;
enjeu : si l'objet est perdu, l'instrument est insuffisamment discriminant,
        et le résultat porte sur l'instrument, non sur le monde.
```

## 6. Ce que la matrice met à l'épreuve

Thèse soumise à réfutation :

> Le réglage fin ne diminue pas lorsqu'on lui donne une histoire ; il change de
> porteur. Il passe de la valeur au mécanisme, puis du mécanisme à
> l'ordonnancement des mécanismes.

```text
condition d'échec : l'existence d'un cas remplissant la dernière ligne ;
statut actuel : non réfutée et non établie ;
règle de conduite : chercher le contre-exemple, ne pas attendre qu'il se présente.
```

Le résultat conditionnel de Barrow et Graham sur l'absence d'attracteur constant
tardif appuie indirectement la thèse sans la démontrer : si le plateau n'est pas
générique, un modèle qui le produit est un modèle contraint. Cet appui reste
indirect et ne vaut pas preuve.

## 7. Réglage de l'ordonnancement

La séquence des trois premières lignes est elle-même un objet, distinct des
valeurs qu'elle ordonne :

```text
transition électrofaible avant confinement ;
confinement avant gel du couplage électromagnétique ;
gel du couplage électromagnétique avant nucléosynthèse.
```

Cette propriété est structurelle et non numérique. Elle n'est pas traitée par les
audits d'ajustement fin fondés sur des intervalles de valeurs, et constitue la
seule ouverture de la présente matrice vers une question non encore instruite.

## 8. Contrôle des deux dispositifs

Un même symbole ne possède pas le même statut selon le dispositif :

```text
dispositif métrologique : constante fixée par convention, non mesurée,
                          incertitude déplacée vers les réalisations ;
dispositif cosmologique : unités naturelles, symbole absorbé, seules les
                          combinaisons sans dimension sont contraintes.
```

Règle de transport :

```text
un énoncé formé dans un dispositif ne se transporte pas dans l'autre par simple
conservation du symbole ; il exige une règle de traduction déclarée.
```

Deux cas documentés, de force inégale. Le premier est physique et non
philosophique : Ellis et Uzan (2005) montrent que les théories à vitesse de la
lumière variable doivent d'abord dire *quel* `c` varie, le symbole recouvrant des
rôles distincts selon qu'il apparaît dans les transformations de Lorentz et la
métrique, dans la propagation électromagnétique, ou dans le couplage des équations
du champ. Le second est plus fort encore, car ce n'est pas une convention qui y
fait disparaître l'objet mais un cadre théorique : selon le théorème de Buchert et
Ehlers, il n'existe pas de réaction cinématique globale en cosmologie
newtonienne. L'objet n'est disponible que dans le dispositif relativiste.

## 9. Ce qui n'entre pas dans cette version, et pourquoi

```text
graviton : une ligne laisserait les colonnes 2 et 3 vides ; l'exclusion est
           procédurale et non ontologique, et la ligne reste rouvrable ;

réaction cosmologique et moyennage : question différente — les grandeurs
           moyennées obéissent-elles aux mêmes équations que les grandeurs
           locales ? — versée dans la note sur les deux régimes de grossissement,
           où elle alimente T3 plutôt que la présente matrice ;

dynamique entre deux figements : exclue par construction ; une trajectoire se
           raconte toujours, une case vide non, et la matrice perdrait sa seule
           propriété intéressante, celle de pouvoir échouer ;

gap supraconducteur : versé dans la matrice en section 4, avec sa note propre ;
           il n'est donc plus en attente. Sa fonction reste celle d'une épreuve
           de la généralité de M3, non celle d'un cas de confirmation.
```

## 10. Limites appariées

```text
les trois premières lignes reprennent des acquis de cycle, sans nouveau calcul ;
les lignes gravitationnelle et supraconductrice sont neuves et n'ont pas encore
  été confrontées aux fiches locales ;
la scission de la colonne des dates peut dissoudre la colonne : si aucun énoncé
  transversal ne vaut pour les deux régimes, l'instrument doit être dédoublé ;
la troisième colonne est une hypothèse de travail, non un résultat ;
les dates dépendent du modèle et doivent être redatées avec lui ;
aucune généralisation à d'autres secteurs n'est autorisée par cette version ;
la dernière ligne est le seul contenu réfutant possible de l'instrument.
```

## 11. Références de première passe

- Barrow, J. D., & Graham, A. A. H. *General dynamics of varying-alpha universes*.
  arXiv : `1307.6816`.
- Buchert, T., Mourier, P., & Roy, X. (2018). Cosmological backreaction and its
  dependence on spacetime foliation. *Classical and Quantum Gravity*, 35, 24LT02.
  DOI : `10.1088/1361-6382/aaebce`.
- Anderson, P. W. (1963). Plasmons, gauge invariance, and mass. *Physical
  Review*, 130(1), 439–442.
- Bardeen, J., Cooper, L. N., & Schrieffer, J. R. (1957). Theory of
  superconductivity. *Physical Review*, 108, 1175–1204.
- Damour, T., & Polyakov, A. M. (1994). The string dilaton and a least coupling
  principle. *Nuclear Physics B*, 423, 532–558.
- Damour, T., Piazza, F., & Veneziano, G. (2002). Violations of the equivalence
  principle in a dilaton-runaway scenario. *Physical Review D*, 66, 046007.
- Ellis, G. F. R., & Uzan, J.-P. (2005). `c` is the speed of light, isn't it ?
  *American Journal of Physics*, 73(3), 240–247. DOI : `10.1119/1.1819929`.
- Gell-Mann, M., Oakes, R. J., & Renner, B. (1968). Behavior of current
  divergences under SU(3) × SU(3). *Physical Review*, 175, 2195–2199.
- Nambu, Y. (1960). Quasi-particles and gauge invariance in the theory of
  superconductivity. *Physical Review*, 117, 648–663.
- Martins, C. J. A. P. (2017). *The status of varying constants : a review of the
  physics, searches and implications*. arXiv : `1709.02923`.
