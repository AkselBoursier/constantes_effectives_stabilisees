# Fiche masse absolue des neutrinos v0.1

## Ancrage spectral, projections d'acces et interface cosmologique

### 1. Fonction du document

Cette fiche reprend le dossier historique :

```text
Fiche masse absolue des neutrinos.docx
```

Elle l'integre dans le cadre actif :

```text
01_CADRE_METHODOLOGIQUE/Note_synthese_methodologique_v1_3_pre_familial_et_temporalite.md
01_CADRE_METHODOLOGIQUE/Matrice_criblage_taxonomique_v0_1.md
01_CADRE_METHODOLOGIQUE/Application_matrice_fiches_sensibles_v0_1.md
02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/Synthese_cycle_saveur_Higgs_v0_1.md
04_ARCHITECTURES_INTER_FAMILLES/Architecture_saveur_Higgs_notes.md
```

Objectif :

```text
stabiliser le statut methodologique de la masse absolue des neutrinos
sans creer de nouvelle famille prematuree.
```

La fiche ne vise pas a donner une table numerique actualisee des bornes experimentales.

Elle vise a dire :

```text
ce qui est classe,
ce qui est seulement borne,
ce qui releve d'un acces,
ce qui releve d'une hypothese,
et ce qui doit rester ouvert.
```

### 2. Objet physique

La masse absolue des neutrinos designe l'ancrage du spectre :

```text
m_1
m_2
m_3
```

Les oscillations stabilisent des ecarts et des orientations :

```text
Delta m^2_21
Delta m^2_31 ou Delta m^2_32
PMNS
```

Mais elles ne fixent pas directement :

```text
la masse du neutrino le plus leger,
la somme totale des masses,
la nature Dirac ou Majorana,
les phases de Majorana,
la valeur absolue de chacun des m_i.
```

Formule de prudence :

```text
les oscillations donnent l'architecture differentielle du spectre,
non son niveau absolu.
```

### 3. Pourquoi ce dossier est sensible

Le dossier est sensible parce qu'il croise trois niveaux qui peuvent etre confondus.

```text
1. Le spectre neutrino massif dans Saveur-Higgs.
2. Les projections experimentales de ce spectre.
3. Les contraintes cosmologiques globales sur la somme ou les effets collectifs.
```

Erreur a eviter :

```text
transformer une borne cosmologique ou une projection cinematique
en masse absolue directement mesuree.
```

Autre erreur a eviter :

```text
deduire l'ancrage absolu du spectre a partir des seuls Delta m^2.
```

### 4. Les trois voies d'acces

La masse absolue n'apparait pas sous une forme empirique unique.

Elle est contrainte par trois voies principales.

| Voie | Grandeur effective | Type d'acces | Prudence |
|---|---|---|---|
| Desintegration beta | `m_beta` | Cinematique locale | Borne directe, non detection positive complete |
| Cosmologie | `Sigma_m_nu = m_1 + m_2 + m_3` | Effet global sur expansion et structures | Forte dependance de modele et de jeux de donnees |
| Double beta sans neutrino | `m_beta_beta` | Processus conditionnel Majorana | Hypothese Majorana, phases, matrices nucleaires |

Ces trois grandeurs ne sont pas interchangeables.

Elles regardent le meme spectre, mais par trois interfaces differentes :

```text
m_beta       : cinematique locale ;
Sigma_m_nu   : effet gravitationnel et cosmologique collectif ;
m_beta_beta  : coherence de Majorana sous hypotheses.
```

### 5. Masse cinematique effective

La desintegration beta contraint une masse effective de type :

```text
m_beta^2 = sum_i |U_ei|^2 m_i^2
```

Lecture :

```text
projection cinematique locale du spectre neutrino sur la saveur electronique.
```

Cette voie est la plus directe au sens experimental local.

Mais son statut reste celui d'une borne tant qu'aucune masse positive n'est mesuree de facon convergente.

Classification :

| Rang | Lecture |
|---|---|
| Rang 0 | Projection cinematique |
| Rang 1 | Pas une famille autonome |
| Rang 2 | Role de borne locale |
| Rang 3 | Acces direct mais limite par sensibilite |
| Rang 4 | Saveur-Higgs, via PMNS et spectre massif |
| Rang 5 | Trajectoire de bornes experimentales |

### 6. Somme cosmologique

La cosmologie contraint une somme :

```text
Sigma_m_nu = m_1 + m_2 + m_3
```

Lecture :

```text
effet collectif des masses neutrino dans un modele cosmologique donne.
```

Cette voie peut etre tres contraignante.

Mais elle n'est pas une mesure locale directe de chaque masse.

Elle depend de :

```text
LambdaCDM ou extensions,
BAO,
CMB,
croissance des structures,
priors,
energie noire,
courbure,
systematiques de jeux de donnees.
```

Classification :

| Rang | Lecture |
|---|---|
| Rang 0 | Somme spectrale globale |
| Rang 1 | Pas une famille cosmologique autonome |
| Rang 2 | Role de contrainte globale |
| Rang 3 | Acces reconstructif et modele-dependant |
| Rang 4 | Interface Saveur-Higgs / cosmologie |
| Rang 5 | Trajectoire de resserrement ou relaxation des bornes selon modeles |

Regle :

```text
une contrainte sur Sigma_m_nu ne doit pas etre confondue
avec une determination directe de m_1, m_2 et m_3.
```

### 7. Masse effective de Majorana

La double desintegration beta sans neutrino, si elle etait observee dans le mecanisme standard, pointerait vers une structure de Majorana.

La grandeur associee est de type :

```text
m_beta_beta = |sum_i U_ei^2 m_i|
```

Lecture :

```text
projection coherente du spectre, sensible aux phases.
```

Cette grandeur n'est pas seulement une masse.

Elle depend de :

```text
masses absolues,
elements PMNS,
phases de Majorana,
elements de matrice nucleaire,
hypothese de mecanisme.
```

Point repris des critiques :

```text
certaines grandeurs structurantes peuvent etre absentes d'un regime d'acces donne.
```

Dans le vocabulaire actif, on ne cree pas une categorie de "constantes fantomes".

On retient plutot :

```text
parametres structurants hors acces direct du regime considere.
```

Classification :

| Rang | Lecture |
|---|---|
| Rang 0 | Projection coherente conditionnelle |
| Rang 1 | Pas une famille autonome |
| Rang 2 | Role de test de nature et de phase |
| Rang 3 | Acces indirect, conditionnel et dependant des matrices nucleaires |
| Rang 4 | Interface Saveur-Higgs / hypothese Majorana |
| Rang 5 | Stabilisation suspendue a une detection et a un mecanisme |

### 8. Ordre des masses et masse minimale

Les oscillations imposent des ecarts.

Elles laissent ouvert l'ancrage absolu.

Deux lectures restent utiles :

```text
ordre normal : le plus leger est associe au bas du spectre normal ;
ordre inverse : le plus leger est associe au niveau separe du doublet plus lourd.
```

La masse du plus leger agit comme variable d'ancrage.

Si elle est tres faible :

```text
le spectre reste hierarchique.
```

Si elle est grande devant les ecarts :

```text
le spectre devient quasi degenere.
```

Le role "seuil spectral" est donc pertinent.

Mais il doit rester un role, non une famille :

```text
seuil spectral = maniere dont l'ancrage absolu modifie la lecture du spectre.
```

### 9. Application de la matrice v1.3

| Rang | Decision |
|---|---|
| Rang 0 | Ancrage spectral incomplet et projections d'acces |
| Rang 1 | Aucune famille principale stabilisee |
| Rang 2 | Borne, projection, seuil spectral selon la voie |
| Rang 3 | Acces heterogenes : beta, cosmologie, double beta sans neutrino |
| Rang 4 | Interface Saveur-Higgs / cosmologie |
| Rang 5 | Stabilisation bornee, non convergence positive complete |

Decision :

```text
la masse absolue des neutrinos n'est pas une nouvelle famille.
```

Elle est :

```text
un dossier d'ancrage spectral,
traverse par plusieurs projections d'acces,
et maintenu sous prudence d'architecture.
```

### 10. Rapport a Relation

La masse absolue des neutrinos comporte des relations :

```text
Delta m^2_ij = m_i^2 - m_j^2
Sigma_m_nu = m_1 + m_2 + m_3
m_beta^2 = sum_i |U_ei|^2 m_i^2
m_beta_beta = |sum_i U_ei^2 m_i|
```

Mais ces relations ne suffisent pas a classer le dossier.

Elles expriment des formes d'acces ou des projections.

Le classement robuste passe par :

```text
spectre,
projection,
borne,
architecture,
regime d'acces.
```

Regle :

```text
Relation ne doit pas absorber le dossier neutrino
simplement parce que les observables sont relationnelles.
```

### 11. Rapport a la cosmologie

La cosmologie n'est pas un simple appendice.

Elle donne une voie de contrainte majeure sur :

```text
Sigma_m_nu
```

Mais la masse absolue ne doit pas etre reclassee comme grandeur cosmologique principale.

Raison :

```text
le spectre appartient d'abord au secteur neutrino massif ;
la cosmologie contraint certains effets globaux de ce spectre.
```

Formule :

```text
la cosmologie est une voie d'acces et une interface,
non le lieu principal de constitution du spectre neutrino.
```

### 12. Rapport a la temporalite

Trois temporalites doivent etre distinguees.

| Temporalite | Exemple | Statut |
|---|---|---|
| Propagation oscillatoire | Phase selon `L/E` | Temporalite physique de manifestation |
| Evolution cosmologique | Effet sur expansion et croissance | Temporalite reconstructive et modele-dependante |
| Histoire experimentale | Resserrement des bornes | Temporalite epistemique, non variation de la constante |

Erreur a eviter :

```text
confondre la trajectoire des bornes avec une variation physique de la masse.
```

### 13. Ce que la fiche stabilise

Cette fiche stabilise six points.

```text
1. Les Delta m^2 ne fixent pas la masse absolue.
2. m_beta, Sigma_m_nu et m_beta_beta ne sont pas equivalents.
3. La voie cosmologique est puissante mais modele-dependante.
4. La voie Majorana est conditionnelle et sensible aux phases.
5. Le role de seuil spectral est utile mais non familial.
6. Le dossier reste une interface Saveur-Higgs / cosmologie.
```

### 14. Ce que la fiche ne stabilise pas

La fiche ne stabilise pas :

```text
une valeur absolue positive des masses neutrino ;
le choix definitif de l'ordre normal ou inverse ;
la nature Dirac ou Majorana ;
les phases de Majorana ;
une origine mecanistique des petites masses neutrino ;
une nouvelle famille taxonomique.
```

### 15. Regle operative pour les reprises locales

Toute reprise du dossier neutrino doit separer quatre questions.

```text
1. Parle-t-on des ecarts oscillatoires ou de l'ancrage absolu ?
2. Parle-t-on de m_beta, de Sigma_m_nu ou de m_beta_beta ?
3. L'acces suppose-t-il un modele cosmologique ou une hypothese Majorana ?
4. La conclusion porte-t-elle sur une masse, une borne, une projection ou un role architectural ?
```

Si ces quatre questions ne sont pas separees, la fiche doit rester sous audit.

### 16. Formule de cloture

> La masse absolue des neutrinos n'est pas la simple valeur manquante d'un spectre deja connu ; c'est l'ancrage encore borne d'un spectre dont les ecarts sont stabilises, mais dont les projections d'acces ne convergent pas encore en une determination unique.
