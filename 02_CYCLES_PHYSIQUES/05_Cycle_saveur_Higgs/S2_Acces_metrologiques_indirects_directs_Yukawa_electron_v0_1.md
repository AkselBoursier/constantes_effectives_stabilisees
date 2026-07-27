# S2 — Accès métrologiques, indirects et directs au Yukawa électronique v0.1

## 0. Statut

```text
statut : résultat scientifique local du lot Saveur–Higgs S1–S3 ;
date : 27 juillet 2026 ;
issue : #55 ;
bloc : S2 — accès ;
fonction : comparer les opérations qui déterminent M_e,
           infèrent y_e ou contraignent l’interaction H–e–e ;
base interne : S1, R1–R3, D6–D8 ;
ne vaut pas : verdict final S3,
               combinaison globale des contraintes,
               mesure directe acquise de y_e,
               ajustement SMEFT,
               ni modification de la synthèse active Saveur–Higgs.
```

## 1. Question exacte

> Comment la métrologie de la masse électronique, les observables indirectes de précision, la recherche directe `H → e+e−` et la production résonante future contraignent-elles des cibles reliées sans contraindre le même objet ni posséder le même rang probatoire ?

S2 compare quatre fonctions :

```text
déterminer une masse physique ;
inférer un paramètre de Yukawa dans un cadre ;
contraindre indirectement une composante de couplage ;
chercher directement une amplitude impliquant le Higgs.
```

## 2. Notations héritées de S1

```text
M_e : masse physique de l’électron ;
y_e^S(mu) : paramètre de Yukawa renormalisé ;
v^S(mu) : paramètre électrofaible renormalisé ;
v_F : échelle dérivée de G_F ;
g_hee : interaction Higgs–électron dans une amplitude déclarée.
```

Dans un modèle à modificateurs, S2 peut écrire localement :

```text
g_hee = kappa_e × g_hee^SM
```

pour une composante CP-paire, et `tilde_kappa_e` pour une composante CP-impaire. Cette convention n’est pas universelle.

## 3. Métrologie — détermination de `M_e`

R1 a déjà reconstruit :

```text
rapports de fréquences et de masses
+ relations théoriques
+ corrections et covariances
+ ajustement CODATA
→ valeur recommandée de M_e ou de rapports contenant M_e.
```

S2 réutilise cette chaîne sans la reproduire.

```text
cible immédiate : M_e ;
non-cibles immédiates : y_e^S(mu), g_hee, kappa_e, tilde_kappa_e.
```

Le passage de `M_e` à `y_e^S(mu)` exige le cadre minimal, une définition de `v`, un schéma, une échelle et les corrections radiatives fixées par S1.

Verdict de rang :

```text
M_e : détermination métrologique très précise ;
y_e : inférence conditionnelle ;
g_hee : non observé par la métrologie de masse.
```

## 4. Contraintes indirectes de précision

Une observable indirecte devient sensible à une modification du couplage électronique par des boucles, du mélange d’opérateurs ou des états supplémentaires. Sa portée dépend donc du modèle de passage.

### 4.1 Moment dipolaire électrique de l’électron

Roussy et al. obtiennent un résultat compatible avec zéro et la borne :

```text
|d_e| < 4.1 × 10^(-30) e·cm
à 90 % de confiance.
```

Cette expérience contraint `d_e`, non directement `tilde_kappa_e`. Une conversion vers une composante CP-impaire du couplage Higgs–électron doit déclarer :

```text
opérateurs présents ;
coefficients CP-impairs autorisés ;
calculs de boucles et évolution de renormalisation ;
autres Yukawa et phases ;
compensations possibles entre opérateurs.
```

Altmannshofer, Brod et Schmaltz fournissent un exemple de calcul à deux boucles dans une paramétrisation restreinte. Leur nombre publié en 2015 dépend de la borne EDM et des hypothèses alors retenues ; S2 ne le transpose pas mécaniquement à la mesure de 2023.

```text
eEDM : contrainte indirecte extrêmement sensible
       sur certaines composantes CP-impaires ;

non : borne universelle sur le module,
      la composante CP-paire ou y_e^S(mu).
```

### 4.2 Moment magnétique anomal de l’électron

`a_e = (g−2)_e/2` est mesuré avec une très grande précision. Son écart au Modèle standard exige toutefois une valeur indépendante de `alpha` et les contributions QED, hadroniques et électrofaibles.

Pour employer `a_e` comme sonde de `y_e`, un modèle doit relier la modification du Yukawa à des contributions radiatives. Des modèles simplifiés étudiés en 2025 rendent `a_e` aussi sensible ou plus sensible qu’un futur passage au pôle du Higgs ; d’autres permettent des modifications qui échappent à cette voie.

```text
a_e : observable de précision directe ;
contrainte sur y_e : indirecte,
                       dépendante de alpha,
                       du spectre, des opérateurs
                       et des corrélations du modèle.
```

Aucune borne numérique unique sur `kappa_e` n’est retenue depuis `a_e`.

### 4.3 Complémentarité CP

```text
eEDM : sensibilité privilégiée aux phases CP-impaires ;
a_e : sensibilité à des contributions CP-paires,
      mais dépendante du modèle et de alpha.
```

Cette complémentarité ne justifie aucune moyenne.

## 5. Recherche directe `H → e+e−`

### 5.1 Résultat CMS

CMS utilise `138 fb^−1` de collisions proton–proton à `13 TeV`, avec des catégories visant notamment la fusion de gluons et la fusion de bosons vecteurs. La recherche vise une résonance étroite dans la masse invariante du couple électron–positon sur un fond dominé par Drell–Yan.

```text
aucun signal significatif ;
B(H → e+e−) < 3.0 × 10^(-4)
à 95 % de confiance ;
limite directe publiée la plus stricte identifiée
à la coupure bibliographique de S2.
```

La prédiction standard est d’environ :

```text
B_SM(H → e+e−) ≈ 5 × 10^(-9).
```

### 5.2 Sens de l’accès direct

```text
produire un Higgs réel
→ rechercher son état final e+e−
→ contraindre le taux de désintégration.
```

La recherche ne reconstruit pas `y_e` depuis `M_e` ; elle vise une amplitude impliquant le Higgs et les électrons.

### 5.3 Conversion conditionnelle vers `kappa_e`

La publication borne une branche de désintégration. Une traduction en `kappa_e` doit déclarer :

```text
production du Higgs ;
largeur totale ;
autres contributions à l’amplitude ;
relation entre g_hee et kappa_e ;
structure CP du vertex.
```

Dans un modèle illustratif où seul le couplage CP-pair électronique est remis à l’échelle, où production et largeur restent standard et où le taux varie comme `|kappa_e|^2` :

```text
|kappa_e| ≲ sqrt[(3.0 × 10^(-4))/(5 × 10^(-9))]
          ≈ 2.45 × 10^2.
```

Cette conversion est produite par S2 ; elle n’est ni la limite brute publiée ni une borne modèle-indépendante sur `y_e^S(mu)`.

```text
branche de désintégration : directement bornée ;
amplitude H–e–e : directement visée, non observée ;
kappa_e : contraint après hypothèses ;
y_e renormalisé : non mesuré sans raccordement ;
origine de la masse : non testée par la non-détection seule.
```

## 6. Production résonante future `e+e− → H`

À une énergie proche de la masse du Higgs, la production en canal `s` fournit un accès direct complémentaire à l’interaction électronique à l’entrée du processus.

La sensibilité dépend notamment de :

```text
dispersion en énergie et monochromatisation ;
rayonnement initial ;
calibration de l’énergie ;
luminosité ;
bruits de fond ;
canaux de désintégration du Higgs.
```

Les études FCC-ee concluent qu’un passage dédié pourrait mesurer ou borner directement le Yukawa électronique, mais soulignent les difficultés de fond, de monochromatisation et de calendrier. Les travaux 2025–2026 restent des études de faisabilité, d’optique ou de modèles ; ils ne constituent pas une mesure.

Des modèles rendent `a_e` plus sensible que ce canal ; d’autres laissent la production résonante comme seule voie décisive. Le gain du canal direct est de réduire la distance entre cible et observable, non de supprimer toute dépendance au modèle et à l’appareil.

## 7. Matrice comparative

| Famille | Observable immédiate | Cible immédiate | Pont vers le Yukawa | Sortie actuelle | Rang |
|---|---|---|---|---|---|
| métrologie | rapports de masses et fréquences | `M_e` | Modèle standard + `v` + schéma + corrections | valeur précise | détermination de masse |
| eEDM | précession / `d_e` | interaction CP-impaire effective | boucles + opérateurs + hypothèses CP | borne compatible avec zéro | contrainte indirecte |
| `a_e` | moment magnétique anomal | contribution radiative totale | `alpha` indépendante + modèle UV/EFT | test de précision | contrainte indirecte |
| `H → e+e−` | branche de désintégration | amplitude Higgs vers `e+e−` | production + largeur + vertex | borne, aucune observation | recherche directe |
| `e+e− → H` | section résonante | amplitude d’entrée `e+e−H` | faisceaux + largeur + canaux | perspective | accès direct futur |

```text
précision sur M_e
≠ sensibilité à d_e
≠ test radiatif par a_e
≠ limite sur une branche du Higgs
≠ précision future sur une section résonante.
```

## 8. Non-combinabilité numérique

S2 refuse une combinaison numérique parce que :

```text
cibles immédiates différentes ;
composantes CP différentes ;
modèles de passage différents ;
sorties statistiques différentes ;
absence de covariances croisées ;
canal résonant non encore mesuré.
```

Une synthèse globale exigerait une vraisemblance commune dans un modèle choisi : ce serait un nouveau chantier.

## 9. Résultat local S2

### 9.1 Admission

```text
- la métrologie détermine M_e sans observer H–e–e ;
- M_e permet une inférence conditionnelle de y_e ;
- l’eEDM contraint fortement certaines composantes CP-impaires ;
- a_e peut contraindre y_e dans des modèles déclarés ;
- CMS borne B(H → e+e−) à 3.0 × 10^(-4)
  sans observer le canal ;
- e+e− → H constituerait un accès direct futur.
```

### 9.2 Refus

```text
- précision de M_e = mesure directe de y_e ;
- borne sur d_e = borne universelle sur y_e ;
- a_e = mesure modèle-indépendante du Yukawa ;
- limite de branche = borne sur kappa_e sans hypothèses ;
- perspective FCC-ee = résultat acquis ;
- hiérarchie universelle direct > indirect ;
- moyenne de contraintes non commensurables ;
- non-détection H → e+e− = confirmation générale
  de l’origine higgsienne de la masse.
```

### 9.3 Suspension

```text
- valeur finale de y_e^S(mu) dans un schéma choisi ;
- borne globale sur kappa_e et tilde_kappa_e ;
- compensations dans un ajustement SMEFT ;
- contrainte universelle issue de a_e ;
- résultat Run 3 dédié à H → e+e− ;
- précision réalisable au pôle du Higgs ;
- observation directe à la valeur standard ;
- origine et naturalité de la hiérarchie électronique.
```

## 10. Conséquence pour S3

S3 devra distinguer :

```text
1. ce que démontre la précision de M_e ;
2. ce qu’elle permet d’inférer sur y_e dans le Modèle standard ;
3. ce que contraignent eEDM, a_e et H → e+e− ;
4. ce qui demeure non établi sur le mécanisme de masse.
```

Le verdict final ne recherchera pas une contrainte numérique unique ; il attribuera à chaque chaîne son objet, son modèle de passage et son rang probatoire.

## 11. Sources de verrouillage

### 11.1 Sources internes

- `S1_Relation_structurelle_masse_electron_Yukawa_v0_1.md` ;
- `R1_Cible_determinations_rapport_proton_electron_v0_1.md` ;
- `R3_Constitution_minimale_et_verdict_rapport_proton_electron_v0_1.md` ;
- `Dette_active_masse_electron_Yukawa_v0_1.md` ;
- `D8_Arbitrage_prochaine_dette_apres_cloture_cycle_1_v0_1.md`.

### 11.2 Sources primaires externes

- Tiesinga et al., *CODATA recommended values of the fundamental physical constants: 2022*, Reviews of Modern Physics 97, 025002 (2025) ;
- Roussy et al., *An improved bound on the electron’s electric dipole moment*, Science 381, 46–50 (2023), arXiv:2212.11841 ;
- Fan et al., *Measurement of the Electron Magnetic Moment*, Physical Review Letters 130, 071801 (2023), arXiv:2209.13084 ;
- Morel et al., *Determination of the fine-structure constant with an accuracy of 81 parts per trillion*, Nature 588, 61–65 (2020) ;
- Altmannshofer, Brod et Schmaltz, *Experimental constraints on the coupling of the Higgs boson to electrons*, JHEP 05 (2015) 125, arXiv:1503.04830 ;
- CMS Collaboration, *Search for the Higgs boson decay to a pair of electrons in proton-proton collisions at sqrt(s)=13 TeV*, Physics Letters B 846 (2023) 137783, arXiv:2208.00265 ;
- d’Enterria, Poldaru et Wojcik, *Measuring the electron Yukawa coupling via resonant s-channel Higgs production at FCC-ee*, European Physical Journal Plus 137 (2022) 201, arXiv:2107.02686 ;
- Erdelyi, Gröber et Selimović, *Probing new physics with the electron Yukawa coupling*, JHEP 05 (2025) 135 ;
- Allwicher et al., *The price of a large electron Yukawa modification*, JHEP 03 (2026) 201.

## 12. Condition locale de sortie

```text
- M_e, y_e, d_e, a_e, B(H → e+e−) et la section résonante
  sont reconnus comme des cibles ou observables distinctes ;
- chaque contrainte indirecte porte son modèle de passage ;
- la borne CMS reste une borne directe sur une branche ;
- la production résonante reste une perspective ;
- aucune combinaison numérique n’est effectuée ;
- S3 peut produire un verdict unique sans effacer
  l’hétérogénéité des accès.
```