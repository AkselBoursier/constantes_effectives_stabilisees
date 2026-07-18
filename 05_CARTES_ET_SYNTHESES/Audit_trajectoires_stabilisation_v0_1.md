# Audit des trajectoires et profils de stabilisation v0.1

## 0. Statut

```text
statut : audit conceptuel et physique ;
fonction : déterminer quand le terme trajectoire est légitime et quand il doit être
           remplacé par le vocabulaire indigène du cas ;
effet : interdit l’usage transversal non qualifié de trajectoire.
```

## 1. Diagnostic

Le corpus utilisait `trajectoire` pour plusieurs objets hétérogènes :

```text
évolution physique dans le temps ;
installation historique d’un régime ;
flot avec l’échelle de renormalisation ;
chaîne de définition et de réalisation ;
histoire d’une reconstruction observationnelle ;
migration conceptuelle ou documentaire.
```

Ces parcours peuvent tous être ordonnés, mais ils ne sont pas des trajectoires au
même sens. Leur rassemblement sous un terme unique produit une analogie trop forte.

## 2. Quatre registres à séparer

### 2.1 Trajectoire dynamique physique

Conditions minimales :

```text
variables d’état ;
équations ou générateur ;
paramètre d’évolution temporelle ;
conditions initiales ou distribution ;
échelles caractéristiques ;
transferts d’énergie ;
observables ;
critères de rupture ou de sortie.
```

Exemples admissibles : évolution d’un champ scalaire, relaxation dissipative,
transition thermique, oscillation amortie, convergence vers un attracteur.

### 2.2 Profil de dépendance à l’échelle

Il décrit :

```text
couplage courant ;
coefficient effectif ;
flot de renormalisation ;
matching entre théories ;
découplage de degrés de liberté.
```

Ce profil n’est pas une histoire cosmique. Le paramètre de groupe n’est pas, par
défaut, le temps physique.

### 2.3 Trajectoire épistémique ou métrologique

Elle décrit une succession d’opérations :

```text
mesures ;
ajustements ;
définitions ;
réalisations ;
comparaisons ;
révisions de valeurs recommandées.
```

Il s’agit d’une histoire des conditions d’assertion, non d’une évolution de l’objet.

### 2.4 Trajectoire conceptuelle ou documentaire

Elle suit la migration d’une proposition entre textes, branches ou disciplines.
Elle est légitime pour la généalogie du corpus, mais ne peut soutenir aucune
conclusion physique.

## 3. Définition retenue pour une trajectoire physique

Pour un porteur `X`, une trajectoire physique de travail est :

```text
T_X = (X, E, R, t, B, tau_drive, tau_relax, tau_obs,
       epsilon, Q, O, C_rupture)
```

avec :

| Élément | Fonction |
|---|---|
| `X` | variable, champ, relation ou observable suivie |
| `E` | équations, action, générateur ou règle d’évolution |
| `R` | régime et approximations |
| `t` | paramètre temporel physique |
| `B` | ensemble ou bassin de conditions initiales |
| `tau_drive` | temps du forçage ou de l’expansion |
| `tau_relax` | temps de relaxation ou d’amortissement |
| `tau_obs` | fenêtre sur laquelle la fixité est affirmée |
| `epsilon` | tolérance |
| `Q` | bilan et transfert d’énergie |
| `O` | observables distinctives |
| `C_rupture` | conditions de sortie, instabilité ou changement de régime |

Le tuple n’est pas une nouvelle théorie. Il sert de test de complétude.

## 4. Profils physiques à ne pas confondre

### 4.1 Attracteur ou point fixe

Une famille de conditions initiales converge vers une région asymptotique. Le gain
explicatif dépend de la largeur du bassin, du taux de convergence et de la liberté
résiduelle de la valeur finale.

### 4.2 Métastabilité

Le système atteint rapidement un régime long-lived mais transitoire, avant une
relaxation beaucoup plus lente. La séparation des échelles de temps est centrale ;
la durée d’observation décide si le régime paraît stationnaire.

### 4.3 Suivi adiabatique

Une variable suit approximativement un minimum ou un état instantané qui se déplace.
La quasi-fixité porte sur l’écart au profil suivi, non nécessairement sur une valeur
numérique constante.

### 4.4 Freeze-out ou découplage cinétique

Le taux d’interaction devient inférieur au taux d’expansion ou au temps de forçage.
Une quantité cesse d’atteindre l’équilibre et conserve une mémoire de l’état au
moment du découplage.

### 4.5 Amortissement dissipatif

Une énergie cohérente est transférée vers d’autres degrés de liberté. Toute
stabilisation affirmée doit conserver le bilan énergétique et les produits du canal
dissipatif.

### 4.6 Transition de phase ou de régime

La structure des états disponibles et les temps de relaxation changent. La
transition ne garantit pas à elle seule la sélection unique d’une valeur tardive.

### 4.7 Quasi-stationnarité par moyenne ou séparation d’échelles

Une variable lente, une moyenne ou un état réduit peut être stable alors que les
degrés de liberté rapides continuent d’évoluer.

### 4.8 Validité effective sans trajectoire temporelle

Une description peut être stable et prédictive dans une plage d’énergie sans qu’un
système ait évolué vers elle. Ce cas doit rester hors de la catégorie dynamique.

## 5. Test appliqué au cycle 10

### 5.1 Ce qui est acquis

Le cycle 10 a correctement exigé :

```text
un porteur dynamique ;
des équations ;
des conditions initiales ;
une évolution du secteur électrofaible ;
des contraintes anciennes et tardives ;
une condition d’échec ;
la reconnaissance d’une migration éventuelle du réglage.
```

Les phases 2 et 3 ont établi des échecs locaux de modèles conservatifs simples. La
phase 4 a montré qu’un canal dissipatif phénoménologique peut ouvrir une fenêtre en
évitant la relique cohérente, mais déplace la dette vers l’origine microscopique du
taux et les produits de dissipation.

### 5.2 Ce qui n’est pas acquis

```text
une loi générale de constitution des constantes ;
un attracteur électrofaible réaliste ;
un mécanisme microscopique de dissipation ;
une histoire cosmologique complète ;
une sélection explicative de la valeur observée ;
une notion transversale de fixité dynamique.
```

### 5.3 Statut correct

Le cycle 10 est un **cas test local de dynamique de quasi-fixité électrofaible**.
Son nom historique peut rester inchangé dans la généalogie, mais ses conclusions ne
doivent pas être exportées comme principe général.

## 6. Utilité comparative possible

Une comparaison transversale n’est intéressante que si elle conserve, pour chaque
cas :

```text
mécanisme indigène ;
échelles de temps ;
forme de la fixité ;
quantité qui demeure libre ;
coût énergétique ;
condition de rupture ;
force des observations.
```

Matrice proposée :

| Cas | Profil | Ce qui se stabilise | Ce qui reste libre | Critère de rupture |
|---|---|---|---|---|
| Dilaton de moindre couplage | attraction asymptotique | couplage résiduel faible | position, potentiel, couplages | absence de convergence ou cinquième force |
| Freeze-out | découplage | abondance ou distribution figée | état au découplage, sections efficaces | reprise d’interactions ou nouveau canal |
| Métastabilité | séparation spectrale | régime transitoirement stationnaire | temps de sortie | activation, fluctuation, mode lent |
| EFT basse énergie | validité par échelle | prédictions et coefficients locaux | données UV | franchissement du cutoff |
| Cycle 10 phase 4 | amortissement phénoménologique | faible relic cohérente | origine du taux et produits | surproduction d’énergie ou contraintes tardives |

Le tableau montre immédiatement qu’une EFT n’appartient pas au même registre
temporel que les quatre autres cas.

## 7. Décision terminologique

### À éviter sans qualification

```text
trajectoire de stabilisation ;
loi de fixité dynamique ;
les constantes se stabilisent ;
la nature converge vers ses constantes.
```

### Formulations autorisées

```text
trajectoire dynamique du champ X dans le modèle M ;
profil temporel de relaxation dans le régime R ;
quasi-fixité sur la fenêtre Delta t et à la tolérance epsilon ;
flot avec l’échelle de renormalisation ;
histoire métrologique de fixation et de réalisation ;
trajectoire documentaire d’une proposition.
```

## 8. Verdict

```text
trajectoire : terme à conserver seulement avec registre explicite ;
fixité dynamique : abandon comme principe ou classe générale ;
profils temporels de stabilisation : instrument comparatif possible, sous test ;
cycle 10 : cas local conservé, sans exportation automatique.
```

## 9. Sources de première passe

- Tănase-Nicola, S., & Kurchan, J. (2004). *Metastable States, Transitions, Basins and Borders at Finite Temperatures*. Journal of Statistical Physics, 116, 1201–1245. DOI: `10.1023/B:JOSS.0000041739.53068.6A`.
- Macieszczak, K., Guță, M., Lesanovsky, I., & Garrahan, J. P. (2016). *Towards a theory of metastability in open quantum dynamics*. Physical Review Letters, 116, 240404. DOI: `10.1103/PhysRevLett.116.240404`.
- Rose, D. C., Macieszczak, K., Lesanovsky, I., & Garrahan, J. P. (2016). *Metastability in an open quantum Ising model*. Physical Review E, 94, 052132. DOI: `10.1103/PhysRevE.94.052132`.
- Lan, Z., van Horssen, M., Powell, S., & Garrahan, J. P. (2018). *Quantum Slow Relaxation and Metastability due to Dynamical Constraints*. Physical Review Letters, 121, 040603. DOI: `10.1103/PhysRevLett.121.040603`.
- de la Torre, A., Kennes, D. M., Claassen, M., et al. (2021). *Nonthermal pathways to ultrafast control in quantum materials*. Reviews of Modern Physics, 93, 041002. DOI: `10.1103/RevModPhys.93.041002`.
- Damour, T., & Polyakov, A. M. (1994). *The String Dilaton and a Least Coupling Principle*. Nuclear Physics B, 423, 532–558. DOI: `10.1016/0550-3213(94)90143-0`.

## 10. Formule de clôture

> Le temps ne fournit pas une loi générale de la constance. Il fournit des profils
> physiques distincts, dont chacun exige son mécanisme, ses échelles et son critère
> de rupture.
