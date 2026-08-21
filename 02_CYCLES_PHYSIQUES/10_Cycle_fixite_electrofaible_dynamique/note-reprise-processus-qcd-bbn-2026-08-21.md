# Note de reprise C10 — processus, QCD, BBN et robustesse de la fenêtre dissipative

Date : 2026-08-21

## Statut

Cette note consigne une requalification scientifique intervenue lors de la reprise du cycle 10.

Elle ne constitue :

- ni un nouveau résultat de calcul ;
- ni l'ouverture d'une nouvelle phase ;
- ni la sélection d'un mécanisme microscopique ;
- ni une proposition générale sur « l'Univers comme processus ».

Les résultats des phases 2, 3 et 4 conservent leur rang antérieur. En particulier, la phase 4 conserve une **fenêtre phénoménologique dissipative non vide** dans le toy model étudié ; elle n'établit toujours aucune réalisation microscopique.

## 1. Intuition examinée

La question de reprise était de savoir si un gain scientifique pouvait provenir du fait de traiter la chaîne

```text
Gamma_phi -> plasma / QCD -> BBN
```

comme une histoire physique couplée plutôt que comme une succession d'états évalués à quelques époques.

Une formulation initiale opposait provisoirement « processus » et « foliation ». Cette opposition est abandonnée comme formulation scientifique : en relativité et en cosmologie, une foliation n'implique pas une physique statique et peut parfaitement servir à décrire une évolution dynamique.

La distinction pertinente est plus étroite :

```text
évolution couplée, éventuellement hors équilibre, avec passages de régime
versus
réduction à quelques conditions frontières ou valeurs instantanées.
```

## 2. Ce qui est déjà acquis dans la physique standard

La nucléosynthèse primordiale est déjà un problème dynamique. Les abondances légères sont obtenues en faisant évoluer des taux de réaction, des populations, l'expansion et la thermodynamique du plasma. Le gel des conversions neutron-proton résulte notamment de la compétition temporelle entre les taux faibles et le taux d'expansion de Hubble.

Il n'y a donc **aucune nouveauté propre à C10** dans l'idée générale selon laquelle « l'histoire compte ».

De même, le lien

```text
variation de v
-> masses de quarks et autres masses
-> seuils et échelle de confinement QCD
-> physique nucléaire
-> abondances BBN
```

est déjà étudié dans la littérature récente sur la variation de l'échelle faible.

Enfin, l'histoire antérieure n'est pas automatiquement observable. Si un transfert énergétique s'achève assez tôt et que les degrés de liberté pertinents retrouvent un état d'équilibre sans relique, distorsion non thermique, secteur découplé, asymétrie modifiée ou autre variable conservant une mémoire, les détails fins de l'histoire peuvent devenir sans effet sur les observables ultérieures.

## 3. Correction de portée pour C10

La proposition générale suivante n'est donc pas retenue comme question de recherche propre au cycle :

> « Voir l'Univers comme un processus plutôt qu'une succession d'états apporte-t-il un gain pour la BBN ? »

Sous cette forme, la réponse est déjà absorbée par la cosmologie thermique, la cinétique hors équilibre et la BBN contemporaines.

Cette clôture de portée ne retire rien au problème local de la phase 4. Elle évite seulement d'attribuer au cycle une nouveauté conceptuelle qui appartient déjà aux méthodes ordinaires du domaine.

## 4. Question locale qui reste ouverte

La vraie dette scientifique devient :

> **La fenêtre dissipative de phase 4 reste-t-elle non vide lorsque ses approximations les plus fragiles sont remplacées par une description suffisamment réaliste de la thermodynamique et de la relaxation du condensat ?**

Deux points sont prioritaires.

### 4.1 Thermodynamique autour de QCD

Pour les plus faibles déplacements testés en phase 4, les températures indicatives de transfert se situent autour de `0.24–0.31 GeV`, donc près de la région où les degrés de liberté relativistes et l'équation d'état changent rapidement.

L'approximation actuelle de `g_*` constant ne doit donc pas être considérée comme neutre pour cette partie de la fenêtre. Une vérification de robustesse doit au minimum distinguer `g_*(T)` et `g_*s(T)` et rétablir une relation temps-température-entropie compatible avec le crossover QCD.

### 4.2 Validité d'un terme local de friction

La phase 4 prescrit un transfert effectif

```text
Q = Gamma_phi rho_phi.
```

Ce paramétrage reste un outil phénoménologique. Cao et Boyanovsky ont montré, dans un modèle apparenté de condensat scalaire homogène se relaxant dans un univers dominé par le rayonnement, que la dynamique de relaxation à température finie peut dépendre du temps et de l'expansion et qu'un simple terme local de friction peut mal reproduire la décroissance.

Ce résultat de littérature **ne valide ni n'invalide directement C10** : leur modèle est un proxy distinct. Il suffit cependant à empêcher de traiter la forme locale de `Gamma_phi` comme une approximation automatiquement robuste.

## 5. Rôle requalifié de la BBN

La BBN ne doit pas être utilisée automatiquement comme « lecteur de toute l'histoire » entre l'échelle électrofaible et l'échelle MeV.

Pour C10, elle devient un calcul complet nécessaire seulement si une information physiquement pertinente survit jusqu'à l'époque BBN, par exemple :

- une variation résiduelle de `v` ou d'autres paramètres ;
- une population non thermique ;
- une relique scalaire ;
- un secteur de rayonnement découplé ou caché ;
- une modification persistante de l'entropie relative des secteurs ;
- une modification du rapport baryons/photons ;
- une autre quantité capable de conserver une mémoire du transfert antérieur.

Si, au contraire, les transferts de phase 4 se terminent bien avant l'échelle MeV et que le secteur visible retrouve l'état thermique standard pertinent sans mémoire résiduelle, un calcul détaillé de BBN n'a pas à reconstruire artificiellement toute l'histoire antérieure.

## 6. Ordre de travail désormais justifié

L'ordre scientifique de reprise devient :

1. **robustesse thermodynamique de la fenêtre** : vérifier l'effet d'une histoire `g_*(T)`, `g_*s(T)` et d'un crossover QCD réalistes sur la fenêtre effective déjà obtenue ;
2. **robustesse du modèle de dissipation** : déterminer quelles propriétés de la fenêtre dépendent réellement d'un `Gamma_phi` local prescrit ;
3. **sélection microscopique seulement ensuite** : si une fenêtre suffisamment stable subsiste, comparer des mécanismes concrets par la forme et l'échelle de leur taux de transfert ;
4. **BBN détaillée conditionnelle** : l'ouvrir si le mécanisme survivant transmet effectivement une mémoire ou une modification jusqu'à l'échelle MeV.

Les familles déjà listées en phase 4 — brisure légère de `Z_2` et mélange Higgs-scalaire, Yukawa à des fermions légers, second scalaire relativiste, annihilation ou évaporation thermique — restent des **familles candidates non sélectionnées**.

Aucune de ces familles n'est ouverte par la présente note.

## 7. Condition d'arrêt

Si la réintroduction d'une thermodynamique réaliste et des dépendances matériellement pertinentes montre que la fenêtre de phase 4 disparaît ou se déplace de façon telle que les taux initialement identifiés deviennent des artefacts du toy model, la recherche microscopique devra être reformulée à partir de ce nouveau résultat.

Si la fenêtre reste robuste et que les transferts se terminent assez tôt pour que toute mémoire pertinente soit effacée avant la BBN, il n'y aura pas de gain à construire une chaîne `Gamma_phi -> QCD -> BBN` plus complexe que nécessaire.

## 8. Hors périmètre de cette note

La remontée vers des époques plus anciennes et la comparaison avec des mécanismes d'inflation restent un chantier possible, mais ne sont ni ouverts ni nécessaires pour trancher la dette actuelle de C10.

## 9. Sources de contrôle

- Particle Data Group, *Big-Bang Nucleosynthesis*, Review of Particle Physics, édition 2025 / corpus PDG 2026.
- A.-K. Burns, V. Keus, M. Sher, T. M. P. Tait, *Constraints on Variation of the Weak Scale from Big Bang Nucleosynthesis*, Phys. Rev. D 109, 123506 (2024), arXiv:2402.08626.
- H. Meyer, U.-G. Meißner, *Improved Constraints on the Variation of the Weak Scale from Big Bang Nucleosynthesis*, JHEP 06 (2024) 074, arXiv:2403.09325 ; erratum JHEP 01 (2025) 033.
- S. Cao, D. Boyanovsky, *Condensate decay in a radiation dominated cosmology*, Phys. Rev. D 111, 063530 (2025), arXiv:2409.16076.

## 10. Statut terminal de la note

```text
PROCESSUS_COMME_NOUVEAUTE_GENERALE_C10 = NON_RETENU
DEPENDANCE_A_L_HISTOIRE = PHYSIQUE_STANDARD_SELON_REGIME
FENETRE_DISSIPATIVE_PHASE4 = CONSERVEE_AU_RANG_PHENOMENOLOGIQUE
ROBUSTESSE_THERMIQUE_QCD = OUVERTE
ROBUSTESSE_GAMMA_LOCAL = OUVERTE
MECANISME_MICROSCOPIQUE_SELECTIONNE = NON
BBN_DETAILLEE = CONDITIONNELLE
INFLATION = HORS_PERIMETRE_ACTUEL
```
