# R3 — Constitution minimale et verdict local du rapport proton–électron `m_p/m_e` v0.1

## 0. Statut

```text
statut : proposition de synthèse locale du premier lot R1–R3 ;
date : 26 juillet 2026 ;
issue : #45 ;
fonction : articuler constitution, détermination et variation du rapport ;
autorité : aucune avant validation humaine ;
ne vaut pas : clôture de la dette m_e,
               propagation dans la synthèse active,
               modification du cadre canonique,
               ni verdict universel sur la constance du rapport.
```

## 1. Question R3

> Que faut-il savoir de la constitution de `m_p` et de `m_e` pour interpréter correctement une valeur ou une contrainte de variation de `m_p/m_e`, sans transformer le rapport en explication de ses propres termes ?

Dans tout le document :

```text
rho_pe := m_p/m_e.
```

R3 ne cherche pas une décomposition exhaustive du proton ni une monographie du secteur de Higgs. Il retient seulement les distinctions capables de modifier le verdict sur `rho_pe`.

## 2. Identité algébrique et insuffisance explicative

Pour de petites variations, l’identité différentielle est :

```text
Delta rho_pe/rho_pe
=
Delta m_p/m_p - Delta m_e/m_e.
```

Cette relation est exacte au premier ordre pour les deux masses physiques comparées. Elle ne fournit cependant aucune attribution causale.

Elle ne dit pas :

```text
quelle transformation de QCD modifie m_p ;
quelle transformation électrofaible modifie m_e ;
si les deux masses varient de manière corrélée ;
si une observable est également sensible à alpha,
aux paramètres nucléaires ou à l’environnement ;
quelle fonction temporelle ou spatiale est engagée.
```

Une contrainte sur `rho_pe` ne devient une contrainte séparée sur `m_p` ou `m_e` qu’après ajout d’un modèle de dépendance.

## 3. Numérateur — ce que désigne la masse du proton

### 3.1 Cible physique

La masse du proton est la masse de repos d’un état hadronique stable. Elle est une observable physique globale, distincte des masses de quarks définies dans le lagrangien renormalisé.

Le proton n’est donc pas :

```text
la somme des masses de deux quarks u et d’un quark d ;
une particule élémentaire dotée d’un unique paramètre de masse ;
une réalisation numérique directe de Lambda_QCD.
```

### 3.2 Origine dynamique dominante

Les calculs de QCD sur réseau confirment que la plus grande part de la masse protonique provient de la dynamique des champs de quarks et de gluons, et non de la seule somme des termes de masse explicites des quarks légers.

Une décomposition publiée à partir du tenseur énergie–impulsion de QCD, dans un schéma et à une échelle déclarés, distribue par exemple la masse entre :

```text
terme de masse scalaire des quarks ;
énergie des quarks ;
énergie des champs gluoniques ;
anomalie de trace.
```

Cette distribution confirme une origine principalement dynamique. Elle ne définit pas quatre substances indépendantes contenues dans le proton.

### 3.3 Dépendance au schéma de la décomposition

Les décompositions de la masse hadronique utilisent des opérateurs renormalisés du tenseur énergie–impulsion. La valeur totale de `m_p` est physique, mais la séparation numérique de certaines contributions dépend :

```text
du schéma de renormalisation ;
de l’échelle ;
de la base d’opérateurs ;
de la somme exacte utilisée ;
du traitement de l’anomalie de trace.
```

Il est donc légitime de dire que la masse protonique est largement issue de la dynamique QCD. Il serait excessif de transformer une décomposition particulière en ontologie unique de la masse.

### 3.4 Rôle de `Lambda_QCD`

`Lambda_QCD` fournit une échelle caractéristique essentielle de la dynamique forte. Dans des modèles de variation, on écrit souvent schématiquement :

```text
m_p ~ Lambda_QCD
```

Cette relation indique une sensibilité dominante, non une identité exacte.

La masse protonique dépend aussi :

```text
des masses de quarks légers et étranges ;
des corrections électromagnétiques ;
du point de définition de la théorie ;
des réponses non perturbatives de l’état lié.
```

R3 refuse donc de remplacer `m_p` par `Lambda_QCD` dans l’interprétation d’une contrainte sans coefficients de sensibilité et modèle déclarés.

## 4. Dénominateur — ce que désigne la masse de l’électron

### 4.1 Masse physique et paramètre renormalisé

La masse électronique qui entre dans `rho_pe` est la masse physique de l’électron utilisée dans le réseau métrologique de R1.

Dans une théorie quantique des champs, il faut cependant distinguer :

```text
masse physique ou masse au pôle ;
paramètre de masse renormalisé ;
schéma et échelle de renormalisation ;
corrections radiatives reliant ces objets.
```

Pour le dossier actuel, la distinction n’est approfondie que lorsqu’elle modifie une relation de passage ou un modèle de variation.

### 4.2 Relation au secteur de Higgs

Dans le Modèle standard, après brisure électrofaible, la relation d’arbre est :

```text
m_e = y_e v/sqrt(2),
```

avec `y_e` le couplage de Yukawa électronique et `v` la valeur moyenne du champ de Higgs.

Cette formule fixe la structure du modèle, mais elle ne permet pas de dire que la précision métrologique sur `m_e` constitue une mesure directe de `y_e`.

L’inférence de `y_e` depuis `m_e` suppose :

```text
le Modèle standard ;
une valeur de v obtenue par le secteur électrofaible ;
une convention de renormalisation ;
les corrections radiatives appropriées ;
l’absence d’opérateurs nouveaux modifiant la relation masse–Higgs.
```

Les recherches directes du couplage Higgs–électron n’ont pas atteint une précision comparable à celle de la masse électronique. R3 conserve donc la relation structurelle, mais refuse l’équivalence probatoire entre mesure de `m_e` et mesure directe de `y_e`.

### 4.3 Modèles de variation

Une variation de la masse électronique peut être paramétrée, selon le modèle, par :

```text
variation de y_e ;
variation de v ;
corrections radiatives dépendantes d’autres paramètres ;
couplage d’un champ scalaire à l’électron ;
combinaison corrélée de plusieurs de ces termes.
```

Aucune de ces possibilités n’est sélectionnée par une contrainte sur `rho_pe` seule.

## 5. Constitution relationnelle du rapport

Le caractère sans dimension de `rho_pe` résout un problème : sa valeur ne change pas par simple changement d’unité commune.

Il ne résout pas :

```text
l’hétérogénéité physique du numérateur et du dénominateur ;
la pluralité de leurs chaînes de détermination ;
la dépendance des observables à des coefficients théoriques ;
la séparation des transformations sous-jacentes.
```

La constitution minimale peut être représentée ainsi :

```text
rho_pe
=
[état protonique de QCD]
/
[masse électronique du régime électrofaible brisé].
```

Cette écriture n’est pas une nouvelle classe de constantes. Elle indique uniquement pourquoi un rapport métrologiquement robuste peut rester physiquement stratifié.

## 6. Trois niveaux qu’il faut maintenir séparés

### 6.1 Valeur actuelle

```text
rho_pe = 1836.152 673 426(32)
```

est une sortie ajustée du réseau CODATA 2022, reconstruite dans R1.

### 6.2 Contraintes de variation

R2 contraint :

```text
une dérive linéaire locale ;
une modulation annuelle corrélée au potentiel solaire ;
des différences finies sur des lignes de visée astrophysiques.
```

Ces contraintes portent sur `rho_pe` à travers des coefficients de sensibilité et des modèles d’accès.

### 6.3 Explication d’origine

L’explication d’une éventuelle variation exigerait un modèle reliant `rho_pe` à des paramètres plus fondamentaux, par exemple :

```text
Lambda_QCD ;
masses de quarks ;
alpha ;
y_e ;
v ;
couplages à un champ scalaire.
```

Le passage du niveau 2 au niveau 3 n’est ni automatique ni fourni par les données seules.

## 7. Formes de modèles admissibles

R3 distingue trois rangs de modélisation.

### 7.1 Paramétrisation phénoménologique

```text
rho_pe(t, x) = rho_pe,0 [1 + epsilon(t, x)].
```

Elle permet d’ajuster une dérive, une modulation ou une différence finie, sans expliquer la transformation.

### 7.2 Décomposition en paramètres du Modèle standard

Une relation indicative peut prendre la forme :

```text
Delta rho_pe/rho_pe
=
K_Lambda Delta Lambda_QCD/Lambda_QCD
+ somme_q K_q Delta m_q/m_q
+ K_alpha Delta alpha/alpha
- Delta y_e/y_e
- Delta v/v
+ ...
```

Les coefficients `K` ne sont pas universels. Ils dépendent du modèle de séparation, de la définition des paramètres et des calculs hadroniques utilisés.

### 7.3 Modèle de champ sous-jacent

Un champ scalaire ou autre degré de liberté peut produire des variations corrélées de plusieurs paramètres. Dans ce cas, une seule grandeur dynamique sous-jacente peut affecter simultanément :

```text
QCD ;
les masses de quarks ;
le secteur électrofaible ;
le Yukawa électronique ;
alpha.
```

Une attribution séparée à `m_p` ou `m_e` exige alors les couplages du modèle et plusieurs observables indépendantes.

## 8. Ce que R1–R3 apportent conjointement

```text
R1 :
  la valeur actuelle est une sortie ajustée composite ;

R2 :
  les accès à la variation testent des familles différentes
  et mobilisent des coefficients de sensibilité ;

R3 :
  le rapport met en relation deux masses de constitution hétérogène
  et ne sépare leurs transformations qu’avec un modèle supplémentaire.
```

Le gain n’est pas d’avoir créé une nouvelle catégorie relationnelle. Il est d’avoir localisé trois opérations scientifiques distinctes :

```text
déterminer le rapport ;
contraindre sa variation ;
expliquer une éventuelle variation.
```

## 9. Verdict local unique proposé

### 9.1 Admission

```text
m_p/m_e est une cible physique sans dimension
lorsque la convention du rapport est déclarée ;

sa valeur actuelle est une sortie ajustée composite,
non une observable première unique ;

la masse protonique est celle d’un état hadronique
principalement constitué par la dynamique QCD ;

les décompositions détaillées de m_p
sont dépendantes du schéma, de l’échelle
et de la somme utilisée ;

la masse électronique est reliée dans le Modèle standard
au Yukawa électronique et à la valeur du champ de Higgs ;

la précision de m_e ne constitue pas
une mesure directe de y_e ;

les horloges et les spectres moléculaires
contraignent le rapport par des relations de sensibilité déclarées ;

les résultats R2 sont compatibles avec zéro
dans leurs familles, périodes et lignes de visée ;

une séparation de Delta m_p et Delta m_e
requiert un modèle supplémentaire.
```

### 9.2 Refus

```text
m_p/m_e comme nombre physiquement simple
au seul motif qu’il est sans dimension ;

m_p comme somme des masses de quarks de valence ;

m_p = Lambda_QCD comme identité exacte ;

une décomposition particulière de la masse protonique
comme ontologie unique et indépendante du schéma ;

m_e = y_e v/sqrt(2) comme relation suffisante
sans convention, corrections et hypothèses de modèle ;

la mesure précise de m_e comme mesure directe
et équivalente du Yukawa électronique ;

une variation séparée de m_p ou de m_e
déduite du seul rapport ;

une invariance temporelle ou cosmologique universelle ;

la combinaison numérique des accès R2 ;

la création d’une nouvelle classe transversale
pour désigner la constitution relationnelle du rapport.
```

### 9.3 Suspension

```text
valeurs universelles des coefficients reliant m_p
à Lambda_QCD, aux masses de quarks et à alpha ;

séparation model-independent des contributions
à une éventuelle variation de m_p ;

mesure directe du Yukawa électronique
au rang de précision de m_e ;

formes temporelles ou spatiales non testées ;

homogénéité cosmologique globale de rho_pe ;

attribution future d’un signal éventuel
au numérateur, au dénominateur ou à une cause commune ;

nécessité ultérieure d’un dossier autonome m_e ;

poids du résultat H2+ 2025
dans un futur ajustement CODATA.
```

## 10. Verdict méthodologique du premier lot

Le premier lot confirme une structure plus sobre que le dossier `alpha` :

```text
une cible ;
trois chaînes de détermination ;
trois formes de transformation testée ;
une constitution minimale ;
un verdict unique.
```

La profondeur supplémentaire n’est justifiée que si elle modifie l’un des éléments suivants :

```text
cible attribuée ;
relation de passage ;
rang probatoire ;
portée du résultat ;
décision scientifique suivante.
```

## 11. Condition d’arrêt du premier lot R1–R3

```text
notation : verrouillée ;
valeur actuelle : classée ;
chaînes de détermination : reconstruites ;
accès de variation : comparés sans combinaison abusive ;
constitution protonique : instruite au rang nécessaire ;
constitution électronique : instruite au rang nécessaire ;
séparation numérateur/dénominateur : refusée sans modèle ;
verdict local unique : formulé ;
propagation : non ouverte ;
dette m_e autonome : maintenue ouverte.
```

La prochaine décision humaine porte uniquement sur :

```text
V1 : validation du verdict local unique R1–R3 ;
V2 : clôture du premier lot #45 ;
V3 : autorisation du contrôle final et de la fusion de la PR #46.
```

La propagation vers la synthèse active et le statut ultérieur de la dette `m_e` restent des décisions distinctes.

## 12. Sources primaires directrices de R3

- Y.-B. Yang et al., *Proton Mass Decomposition from the QCD Energy Momentum Tensor*, Physical Review Letters 121, 212001 (2018).
- A. Metz, B. Pasquini et S. Rodini, *Revisiting the proton mass decomposition*, Physical Review D 102, 114042 (2020).
- ATLAS Collaboration, recherche de l’interaction du boson de Higgs avec les électrons par `H -> e+e-`, 2019.
- Les sources primaires de R1 et R2 pour les chaînes de détermination, les horloges et les spectres moléculaires.
