# Audit de maturité et de potentiel non testé des cycles actifs v0.1

## 0. Statut

```text
statut : deuxième passe de requalification des cycles ;
date : 21 juillet 2026 ;
branche : agent/crise-fondatrice-audit-fondations ;
fonction : distinguer la valeur actuellement démontrée, la maturité acquise et le
           potentiel encore non testé des cycles actifs ;
ne vaut pas : classement général, allocation définitive du travail, validation de
              publication, ni retour à une thèse commune aux cycles.
```

Le présent audit complète l'`Inventaire_valeur_autonome_dix_cycles_v0_1.md`.

L'inventaire précédent répondait principalement à la question :

```text
qu'est-ce qui demeure actuellement établi si toute thèse générale disparaît ?
```

Cette question était nécessaire, mais elle ne suffisait pas. Un cycle peu approfondi
peut paraître faible parce qu'il n'a pas encore reçu les opérations susceptibles de
faire apparaître sa valeur. Inversement, un cycle très développé peut paraître plus
fécond parce que son volume documentaire, ses calculs et sa visibilité rendent ses
résultats plus faciles à reconnaître.

La deuxième passe ajoute donc deux questions :

```text
quelle possibilité réelle le cycle a-t-il déjà reçue de produire un résultat ?

quel test borné pourrait encore révéler une valeur non visible ou établir que le
potentiel supposé n'est pas confirmé ?
```

---

## 1. Biais corrigés

### 1.1 Biais de maturité

```text
cycle approfondi
-> davantage de sources, calculs, objections et résultats visibles
-> apparence de valeur intrinsèque supérieure.
```

L'approfondissement produit des preuves réelles, mais il n'est pas distribué également.
La valeur démontrée ne doit donc pas être convertie automatiquement en potentiel
intrinsèque.

### 1.2 Biais de survie documentaire

Un cycle qui a été repris plusieurs fois dispose de synthèses actives, de décisions de
rang et de routes de lecture. Un cycle abandonné tôt conserve souvent des sources plus
fragiles, des DOCX ou une nomenclature devenue obsolète. Cette différence d'état peut
être prise à tort pour une différence de qualité intellectuelle.

### 1.3 Biais de tractabilité technique

Les dossiers disposant de données publiques, de scripts ou de produits distribués
permettent plus facilement une reproduction visible. Une question théorique,
historique ou métrologique peut exiger d'autres formes de preuve et paraître moins forte
si la computation devient implicitement le modèle de toute maturité.

### 1.4 Biais de centralité architecturale

Un cycle placé au centre d'une carte ou relié à plusieurs documents peut sembler plus
important par effet de navigation. Cette centralité est parfois le produit d'une
réorganisation antérieure et non d'un résultat propre.

### 1.5 Biais de sélection humaine

Les cycles les plus développés ont souvent été ceux qui avaient déjà produit une
intuition, une tension ou un intérêt particulier pour l'auteur. Leur maturation confirme
partiellement cette sélection antérieure ; elle ne constitue pas une expérience équitable
entre tous les cycles.

---

## 2. Dimensions de l'audit

Aucune note unique n'est calculée. Les dimensions restent séparées.

### G — profondeur généalogique

```text
question : le cycle possède-t-il une histoire antérieure, des intuitions, manuscrits,
           objections ou bifurcations déjà documentés ?

fort ne signifie pas : valide ou original ;
faible ne signifie pas : sans potentiel.
```

### Q — maturité de la question

```text
forte : question locale, discriminante, opérationnalisable et susceptible d'échouer ;
partielle : question intéressante mais trop large ou encore divisée en plusieurs dossiers ;
faible : formulation surtout classificatoire, analogique ou dépendante d'une thèse générale.
```

### L — maturité bibliographique

```text
forte : sources primaires et voisinages proches identifiés et contrôlés ;
partielle : littérature pertinente présente mais inégalement vérifiée ou périssable ;
faible / non testée : synthèse principalement interne ou références encore rapportées.
```

### E — prise empirique ou physique

```text
forte : données, contraintes, mécanismes ou exclusions précisément établis ;
partielle : reconstruction sectorielle correcte sans résultat empirique propre ;
faible : proposition principalement conceptuelle ou documentaire.
```

### C — prise computationnelle

```text
forte : calcul ou pipeline réexécuté avec entrées et limites documentées ;
partielle : calculs locaux, produits distribués ou reproductions aval ;
non requise : le contrat du cycle ne demande pas de computation ;
absente mais requise : dette réelle.
```

### A — exposition adversariale

```text
forte : hypothèse concurrente, cas négatif ou test susceptible de faire perdre le cycle ;
partielle : limites déclarées mais peu de confrontation indépendante ;
faible : le dossier produit surtout des reformulations compatibles avec son cadrage.
```

### O — autonomie à l'égard de la thèse générale

```text
forte : le cycle conserve une question, un résultat ou une dette sans vocabulaire transversal ;
partielle : certains résultats survivent, mais le fil principal dépend encore du cadre ;
faible : le cycle était principalement une application de la thèse ou de la taxonomie.
```

### P — potentiel non testé

Le potentiel n'est pas une qualité attribuée par intuition seule. Il est formulé comme
une possibilité conditionnelle :

```text
si telle opération bornée est accomplie,
alors le cycle pourrait produire tel type de résultat ;
sinon son statut doit être réduit ou archivé.
```

---

## 3. Cycle 1 — couplages, échelles et QCD

### Profil de maturité

```text
G : moyenne ; la question fondatrice des régimes et de la définissabilité est ancienne,
    mais le dossier QCD spécialisé est récent ;
Q : forte pour la comparaison des chaînes alpha_s ;
L : forte pour T1.1-T1.5, partielle pour alpha, m_e et m_p/m_e ;
E : partielle à forte ; résultats publiés reconstruits, aucune nouvelle mesure ;
C : partielle ; pipeline ALPHA aval reproduit, simulations amont non reproduites ;
A : partielle ; plusieurs chaînes comparées, une seule chaîne reproduite ;
O : forte ; la question de comparabilité est physiquement autonome.
```

### Biais de maturité observé

Le rang du cycle a effectivement changé après T1.1-T1.5. Avant la reprise, il pouvait
être lu comme une distinction conceptuelle standard entre running et variation
temporelle. La reproduction ALPHA a créé une prise locale nouvelle. Le cycle démontre
donc que l'approfondissement peut modifier légitimement une requalification.

### Potentiel non testé

Le potentiel principal ne réside plus dans une nouvelle définition de la constance. Il
réside dans la reconstruction comparée des chaînes qui déterminent `alpha_s` à partir
d'objets, d'ordres perturbatifs, de corrections et de covariances hétérogènes.

### Test minimal discriminant C1-P

```text
sélectionner une chaîne phénoménologique accessible ;
acquérir ou reconstruire ses entrées publiques ;
rejouer au moins une étape non triviale de l'extraction ou du profil ;
comparer sa structure d'incertitude à la chaîne ALPHA ;
identifier une conséquence qui ne se réduit pas à « les méthodes sont différentes ».
```

### Condition de montée

Le cycle monte si la reproduction révèle une dépendance, une covariance, un choix
d'ordre ou une non-comparabilité qui modifie le verdict physique ou la manière de
combiner les résultats.

### Condition de réduction

Si une deuxième chaîne confirme seulement les distinctions standard déjà déclarées,
le cycle reste un dossier technique de comparabilité sans prolongement transversal.

---

## 4. Cycle 3 — neutrinos

### Profil de maturité

```text
G : moyenne à forte ; lignée antérieure sur les accès et la mesure ;
Q : forte et opérationnalisée ;
L : forte et datée pour N0-N5, avec veille empirique requise ;
E : forte comme reconstruction des quatre voies ;
C : partielle à forte pour C1-C2, sans ajustement conjoint intégral ;
A : forte ; tensions, bornes, non-détections et changements de modèle sont conservés ;
O : forte.
```

### Biais de maturité observé

Le cycle bénéficie d'un approfondissement exceptionnel. Mais cet approfondissement n'a
pas seulement augmenté son volume : il a produit un résultat autonome, à savoir la
séparation de quatre fonctions du spectre latent et la localisation des informations
nécessaires à leurs conversions.

### Potentiel non testé

Le potentiel restant est moins général que la première maturation. Il concerne une
reconstruction quantitative commune dans l'espace des masses, de l'ordre et des phases,
ou la reproduction plus complète d'une likelihood particulière.

### Test minimal discriminant C3-P

Choisir une seule opération :

```text
option A : reproduire une likelihood ou un profil complet de l'une des voies ;
option B : construire une carte commune m_min, m_beta, Sigma m_nu, m_beta_beta
           avec hypothèses et bandes séparées ;
option C : tester quantitativement le déplacement de la tension N1-N3 sous un
           changement précis de modèle ou de prior.
```

### Condition de montée

Le cycle monte vers un dossier publiable spécialisé si la nouvelle opération fournit
une figure, une exclusion, une compatibilité ou une localisation de tension qui ne soit
pas une simple actualisation de valeurs.

### Condition de stabilisation

Si le nouveau travail ne produit qu'une mise à jour numérique, le cycle peut être tenu
pour mûr comme revue comparative datée sans extension immédiate.

---

## 5. Cycle 5 — Saveur–Higgs

### Profil de maturité

```text
G : moyenne ; plusieurs fiches antérieures et redistribution depuis le cycle 2 ;
Q : partielle à forte ; réseau clair, sous-questions encore nombreuses ;
L : partielle ; synthèse correcte mais peu d'extractions primaires reconstruites ;
E : partielle ; architecture standard documentée, peu de prise sur les tensions actuelles ;
C : absente mais pas toujours requise ;
A : partielle ; origine des Yukawa refusée, mais peu de tests capables de modifier le dossier ;
O : moyenne à forte ; le réseau sectoriel survit, certaines formulations anciennes non.
```

### Biais de maturité observé

Le cycle a été qualifié de pont parce qu'il est principalement synthétique. Cette
qualification est exacte pour son état actuel, mais elle ne démontre pas qu'un
sous-dossier plus précis ne puisse produire une valeur autonome.

### Potentiel non testé

Le potentiel réside dans la confrontation d'une architecture de dépendances à une
extraction ou une tension réelle : ajustement CKM, détermination d'un Yukawa, schéma de
masse ou cohérence de plusieurs observables.

### Test minimal discriminant C5-P

```text
sélectionner un seul sous-dossier vivant ;
reconstruire observable -> corrections -> likelihood -> paramètre ou combinaison ;
identifier ce que l'architecture Saveur-Higgs ajoute ou interdit ;
comparer au traitement sectoriel standard sans vocabulaire du projet.
```

### Condition de montée

Le cycle monte si la carte de dépendances modifie une attribution de tension, une
hypothèse d'indépendance ou une demande d'explication.

### Condition de réduction

S'il ne fait que réexposer le lagrangien, la diagonalisation et les paramètres déjà
connus, il reste une synthèse pédagogique et un pont documentaire.

---

## 6. Cycle 6 — théories effectives à basse énergie

### Profil de maturité

```text
G : moyenne ; issu de redistributions et d'une architecture active ;
Q : forte conceptuellement ;
L : forte pour la grammaire générale, partielle pour les tests intersectoriels ;
E : partielle ; exemples physiques corrects mais peu de résultat propre ;
C : faible ou non requise selon le cas ;
A : partielle ; la dette T3 est précisément un test adversarial manquant ;
O : forte comme dossier EFT, plus faible comme contribution comparative originale.
```

### Biais de maturité observé

Le cycle paraît mûr parce que la littérature EFT fournit déjà une grammaire très
structurée. Cette maturité du domaine peut masquer l'absence de gain propre au cycle.

### Potentiel non testé

Le potentiel n'est pas d'ajouter davantage d'exemples. Il est de vérifier si une
comparaison entre plusieurs formes d'effectivité produit un diagnostic absent des
traitements sectoriels ordinaires.

### Test minimal discriminant C6-P — T3

```text
choisir deux secteurs dont les mécanismes basse énergie diffèrent ;
formuler une inférence ou une confusion précise à tester ;
appliquer les descriptions sectorielles standards ;
appliquer ensuite la comparaison intersectorielle ;
identifier une décision différente ou constater l'absence de gain.
```

### Condition de montée

Le cycle monte si T3 interdit une assimilation, révèle une dette ou change une décision
que les analyses séparées laissaient invisible.

### Condition de réduction

Si T3 ne produit aucun effet différentiel, le cycle devient une excellente synthèse
pédagogique des EFT, sans revendication méthodologique propre.

---

## 7. Cycle 7 — cosmologie

### Profil de maturité

```text
G : forte ; cosmologie, temps, inférence et tensions sont présents dans plusieurs lignées ;
Q : forte comme architecture d'inférence ;
L : partielle et rapidement périssable ;
E : partielle ; valeurs et résultats rapportés, peu de chaîne complète reproduite dans le cycle ;
C : faible à partielle ; la reprise DESI du cycle 3 fournit un précédent, non une maturité générale ;
A : partielle ; plusieurs exclusions conceptuelles, peu de reproductions concurrentes ;
O : forte.
```

### Biais de maturité observé

Le cycle est probablement sous-évalué par rapport à son potentiel. Sa carte est riche,
mais l'absence d'une reprise sonde par sonde l'a maintenu au rang de synthèse
inférentielle.

### Potentiel non testé

Le potentiel porte sur une chaîne complète allant d'un produit observationnel à un
paramètre ou une tension, avec variantes de modèle, de prior ou de calibration.

### Test minimal discriminant C7-P

```text
choisir une sonde et un paramètre ou une combinaison ;
acquérir le produit public et la documentation de likelihood ;
reproduire un résultat borné ;
modifier une hypothèse clairement déclarée ;
mesurer ce qui change dans l'objet inféré et dans la tension éventuelle.
```

### Condition de montée

Le cycle monte s'il produit une reconstruction quantitative contrôlée ou localise une
tension dans une opération déterminée plutôt que dans un nom de paramètre.

### Condition de réduction

Si les ressources publiques ne permettent pas une reprise raisonnable ou si le résultat
reste une reformulation générale de la dépendance au modèle, le cycle demeure une revue
architecturale vivante.

---

## 8. Cycle 8 — Système international d'unités

### Profil de maturité

```text
G : moyenne ; cycle 4 et situations philosophiques fournissent des antécédents ;
Q : forte et locale ;
L : forte pour les documents officiels, partielle pour l'histoire détaillée des réalisations ;
E : partielle à forte comme effet métrologique descriptif ;
C : non requise pour le noyau, mais traitement quantitatif des covariances manquant ;
A : partielle ; objection de tautologie traitée, transfert hors métrologie non acquis ;
O : forte.
```

### Biais de maturité observé

Le cycle peut être sous-évalué parce que ses résultats sont institutionnels,
métrologiques et quantitatifs sans prendre la forme d'une nouvelle expérience physique.
Il peut aussi être surévalué si des distinctions officielles connues sont présentées
comme découverte conceptuelle.

### Potentiel non testé

Le potentiel réside dans l'analyse quantitative du déplacement des incertitudes et de la
fonction des expériences après la révision du SI.

### Test minimal discriminant C8-P

```text
sélectionner une unité ou une chaîne de réalisation ;
comparer avant et après redéfinition : grandeur ajustée, valeur fixée, réalisation,
incertitudes et constantes dérivées ;
reconstruire au moins une covariance ou un budget d'incertitude ;
identifier un effet qui ne soit pas contenu dans la seule phrase « la valeur est exacte ».
```

### Condition de montée

Le cycle monte s'il montre quantitativement comment une décision définitionnelle change
une fonction expérimentale ou redistribue une incertitude entre grandeurs.

### Condition de stabilisation

À défaut, il reste une étude de cas métrologique solide et pédagogique.

---

## 9. Cycle 9 — fine-tuning

### Profil de maturité

```text
G : très forte ; manuscrit de février 2026, critiques, déflations et cycle actif ;
Q : forte ; deux questions propres et plusieurs discriminants ;
L : inégale ; paysage large, vérification primaire variable selon les cas ;
E : inégale ; quatre dossiers instruits à des profondeurs différentes ;
C : faible ; espaces et régions souvent décrits sans reconstruction complète ;
A : partielle à forte ; verdicts différenciés, mais risque de sélectionner les cas favorables ;
O : forte ; le cycle possède son contrat indépendamment de la thèse des constantes.
```

### Biais de maturité observé

Le cycle bénéficie d'une profondeur antérieure réelle, mais une partie de cette
profondeur est philosophique et spéculative. Elle ne doit pas être comptée comme preuve
physique. Inversement, la refonte récente ne doit pas effacer les questions et les
lectures accumulées.

### Potentiel non testé

Le potentiel est élevé, mais il ne sera établi que lorsqu'un cas sera reconstruit dans
un espace physique explicite plutôt que traité principalement par synthèse de
littérature.

### Test minimal discriminant C9-P

```text
choisir un seul cas ;
établir les variables réellement indépendantes ;
définir le protocole de variation et les corrélations ;
construire ou reprendre la région admissible ;
distinguer sensibilité, possibilité et probabilité ;
identifier la contingence résiduelle ;
comparer au meilleur traitement existant du cas.
```

Le langage probabiliste est interdit si aucune mesure justifiée n'est disponible.

### Condition de montée

Le cycle monte s'il modifie quantitativement la largeur, la connexité, les directions
compensées ou le rang explicatif d'un réglage allégué.

### Condition de réduction

Si le test ne produit qu'une déflation verbale de la métaphore des cadrans ou répète les
critiques connues de naturalité et des priors, le cycle reste un programme de revue et de
clarification, non une contribution propre.

---

## 10. Cycle 10 — quasi-fixité électrofaible

### Profil de maturité

```text
G : moyenne à forte ; question reliée au fine-tuning et à la lignée temporelle ;
Q : forte et calculable ;
L : partielle ; modèle local plus avancé que son positionnement complet dans la littérature ;
E : partielle ; contraintes cosmologiques imposées à un toy model, aucune prise empirique directe ;
C : forte localement ; calculs, scans et résultats négatifs conservés ;
A : forte pour les modèles testés, faible à partielle pour les alternatives microscopiques ;
O : forte.
```

### Biais de maturité observé

La computation rend le cycle particulièrement visible et convaincant. Elle ne doit pas
masquer la simplicité du modèle ni transformer une fenêtre phénoménologique en scénario
physique probable.

### Potentiel non testé

Le potentiel réside dans la réalisation microscopique du canal dissipatif et dans son
exposition aux contraintes indépendantes.

### Test minimal discriminant C10-P

```text
sélectionner un mécanisme microscopique minimal ;
dériver ou justifier le terme dissipatif effectif ;
identifier le secteur récepteur et son devenir thermique ;
calculer au moins un ensemble de contraintes indépendantes ;
réexécuter le bilan cosmologique avec ce mécanisme.
```

### Condition de montée

Le cycle monte s'il conserve une fenêtre non vide sous un mécanisme calculable et des
contraintes empiriques explicites.

### Condition de réduction

Si aucun mécanisme plausible ne réalise les taux requis ou si les contraintes ferment
la fenêtre, le résultat négatif doit être conservé et le projet réduit sans être jugé
inutile.

---

## 11. Cycles 2 et 4

Les cycles 2 et 4 ne reçoivent pas de test autonome dans cette passe.

```text
cycle 2 : ses sous-dossiers sont distribués entre 5, 6, 7 et 9 ;
cycle 4 : son contenu est principalement absorbé par le cycle 8.
```

Cette décision ne repose pas sur leur faible maturité, mais sur le changement de l'unité
de recherche pertinente. Une question issue de ces cycles peut être réactivée dans un
dossier actif sans restaurer le cycle comme totalité.

---

## 12. Matrice synthétique

| Cycle | Maturité démontrée | Potentiel non testé | Test minimal | Risque principal |
|---|---|---|---|---|
| 1 | forte localement pour ALPHA, partielle inter-chaînes | élevé | reproduire une chaîne phénoménologique | prendre l'hétérogénéité pour un résultat nouveau |
| 3 | forte | moyen à élevé, plus spécialisé | likelihood ou carte commune des masses | prolonger sans gain au-delà d'une mise à jour |
| 5 | partielle | incertain à élevé | extraction ou tension Saveur–Higgs | rester une synthèse du modèle standard |
| 6 | forte comme grammaire standard | conditionnel | test T3 différentiel | confondre maturité du champ et gain du cycle |
| 7 | partielle | élevé | chaîne cosmologique complète | cartographie sans reprise des données |
| 8 | moyenne à forte localement | moyen | déplacement quantitatif d'incertitude | redécouvrir le SI officiel |
| 9 | forte conceptuellement, inégale physiquement | très élevé mais risqué | un cas complet dans son espace physique | déflation philosophique sans calcul |
| 10 | forte computationnellement, partielle physiquement | élevé et étroit | mécanisme microscopique | surinterpréter un toy model |

Aucune ligne ne fournit une priorité automatique.

---

## 13. Principe d'égalité d'opportunité

Il serait disproportionné d'approfondir tous les cycles au même volume. En revanche,
chaque cycle encore actif doit recevoir, avant une rétrogradation durable, une chance
bornée de produire son résultat discriminant.

```text
égalité d'opportunité
≠ égalité de nombre de fichiers ou d'heures ;

égalité d'opportunité
= un test adapté au contrat du cycle,
  avec entrée, opération, sortie et condition d'arrêt.
```

### Plafond d'effort

Chaque test minimal doit être assez borné pour pouvoir conduire à l'une des trois sorties :

```text
montée : une valeur autonome nouvelle est établie ;
stabilisation : la valeur actuelle est confirmée sans extension ;
réduction : le potentiel supposé n'est pas confirmé dans ce périmètre.
```

Un test qui génère une architecture indéfinie avant de produire une sortie est mal borné.

---

## 14. Effet sur les priorités de l'inventaire précédent

Les priorités formulées dans l'inventaire de valeur autonome doivent être lues comme une
photographie de la valeur démontrée, non comme une décision définitive sur le potentiel.

Formulation corrigée :

```text
résultats actuellement les plus établis : cycles 3 et 10 ;
cycle en maturation scientifique nette : cycle 1 ;
programme à profondeur conceptuelle forte mais preuve physique inégale : cycle 9 ;
cycles sous-testés à potentiel réel : 5, 7 et 8 ;
cycle dont le gain propre dépend d'un test restant : 6 ;
unités historiques absorbées : 2 et 4.
```

Le mot `prioritaire` ne doit plus être employé sans préciser le motif :

```text
priorité de maturation ;
priorité de potentiel ;
priorité de dette technique ;
priorité éditoriale ;
priorité de conservation.
```

---

## 15. Verdict

> La profondeur de développement a influencé l'évaluation des cycles de deux manières :
> légitimement, parce qu'elle a produit des preuves et des résultats ; inégalement,
> parce que tous les cycles n'ont pas reçu la même possibilité de produire ces preuves.
> L'inventaire de valeur autonome reste valide comme état des acquis. Il ne devient une
> politique de recherche qu'après des tests minimaux discriminants donnant aux cycles
> actifs une possibilité comparable de monter, de se stabiliser ou de se réduire.

Aucune PR, fusion, suppression ou réorganisation des cycles n'est autorisée par ce
document.