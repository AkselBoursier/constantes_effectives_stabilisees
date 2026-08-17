# Feuille de route post-consolidation v0.1

## 0. Fonction et statut

```text
fonction : organiser les opérations après restauration d’un tronc lisible ;
date : 18 juillet 2026 ;
base : vue récente, vue globale v0.4, arbitrage des dettes et reprise N1–N3 ;
ne vaut pas : calendrier rigide, hiérarchie définitive des cycles ou décision de
              publication ;
principe : séparer consolidation, recherche scientifique, calcul, rédaction et
           reprise philosophique.
```

La feuille de route est organisée par **portes de passage**, non par accumulation de
fichiers. Une phase est close lorsque son résultat, son statut et sa dette suivante
sont visibles.

## 1. Phase P0 — Consolider le tronc

### But

Faire de `main` un état actuel, cohérent et navigable du corpus sans prétendre que
les dettes scientifiques sont terminées.

### Opérations

1. Conserver le laboratoire éditorial sous son nom actif :

```text
93_LABORATOIRE_EDITORIAL_EXPERIMENTAL
```

Le renommage a été effectué par `git mv` afin de conserver l’historique, y compris
les PDF et autres fichiers binaires.

2. Vérifier et mettre à jour toutes les références internes à l’ancien chemin.
3. Ajouter une vue récente et une vue globale — réalisées dans le présent lot.
4. Mettre à jour le README central et l’accueil des dix cycles.
5. Vérifier le statut des deux PDF du laboratoire éditorial avant fusion ; les
   conserver seulement si leur redistribution publique est compatible avec leurs
   conditions d’accès. Sinon, conserver les fiches de lecture et remplacer les PDF
   par une référence bibliographique et une instruction de récupération.
6. Auditer le diff complet entre la branche cumulative et `main`.
7. Retargeter la PR de tête vers `main` et remplacer son titre et son corps devenus
   obsolètes.
8. Laisser la fusion elle-même à une décision explicite de l’auteur.

### Critères de passage

```text
aucune référence cassée ;
audits structure, liens et encodage réussis ;
aucune donnée externe suivie par Git ;
portes d’entrée datées et cohérentes ;
PR de consolidation fidèle au diff réel ;
dettes visibles sans être prises pour des régressions.
```

## 2. Phase P1 — Clore ou suspendre proprement C2

### But

Transformer la disponibilité locale des produits DESI DR2 en reproduction
contrôlée des résultats utiles à la tension `N1–N3`.

### Entrée locale

```text
data_external/desi_dr2
```

Ce répertoire reste ignoré par Git.

### Opérations

1. Contrôler l’archive par MD5 et les produits utilisés par SHA-256.
2. Ingestérer séparément :

```text
base_mnu ;
base_mnu059 ;
base_mnu_binary_3 ;
base_mnu_w_wa.
```

3. Reproduire les quantiles pondérés et les comparer aux `margestats`.
4. Extraire les diagnostics de convergence.
5. Séparer maxima de posterior, maxima de vraisemblance et profils disponibles.
6. Calculer les corrélations de la masse avec les paramètres cosmologiques
   pertinents.
7. Documenter ce qui dépend du support, de l’ordre, du prior et du modèle
   d’expansion.
8. Remplacer les entrées oscillatoires indépendantes de `C1` par des profils
   numériques versionnés lorsque leur redistribution et leur provenance sont
   établies.

### Critères de clôture

```text
0,0642 eV reproduit ou écart expliqué ;
quantile base_mnu059 effectivement calculé ;
0,163 eV reproduit ou écart expliqué ;
base_mnu_binary_3 analysé comme produit distinct ;
maxima et profils correctement qualifiés ;
aucune chaîne brute dans Git ;
rapport C2 v0.2 publié.
```

Si certains produits restent absents, `C2` peut être suspendue proprement avec un
manifeste positif des absences ; elle ne doit pas bloquer indéfiniment le reste du
programme.

## 3. Phase P2 — Reprendre le cycle 1

### But

Instruire la dette prioritaire suivante : couplages, échelles et chromodynamique
quantique (`QCD`).

### Questions directrices

```text
qu’est-ce qui dépend de l’échelle cinématique ou de renormalisation ?
qu’est-ce qui définit un changement de régime ?
comment alpha_s et Lambda_QCD sont-elles reliées sans être la même grandeur ?
quel statut portent les masses et rapports de masses ?
quelles déterminations sont effectivement indépendantes ?
```

### Protocole minimal

1. Inventaire primaire des observables et déterminations.
2. Déclaration des schémas et échelles.
3. Chaînes de calcul ou d’ajustement.
4. Valeurs actuelles et corrélations.
5. Résultats positifs et non-acquisitions.
6. Comparaison contrôlée avec le cycle 6.

### Critère de sortie

Une synthèse active remplace la seule synthèse de récupération et localise les
dettes computationnelles restantes.

## 4. Phase P3 — Contrôles métrologiques 4 et 8

### But

Utiliser les cycles 4 et 8 comme contrôles quantitatifs des distinctions entre
mesure, fixation, composition exacte et réalisation.

### Opérations

```text
cartographier les chaînes de réalisation ;
identifier les covariances ;
distinguer incertitude de réalisation et exactitude définissante ;
comparer les fonctions de N_A, R, k_B, c, h et e ;
mesurer ce qui change effectivement après fixation.
```

Cette phase peut être menée avant ou après le cycle 1 selon les besoins de l’essai,
mais elle ne doit pas devenir une philosophie générale de la constance.

## 5. Phase P4 — Reprises sectorielles 2, 5 et 6

### Cycle 2

Réexaminer les fonctions électrofaibles sans verdict global de stabilité.

### Cycle 5

Remonter aux likelihoods, événements, simulations et extractions du réseau
Saveur–Higgs.

### Cycle 6

Choisir plusieurs cas de théorie effective et rendre explicites bases, matching,
troncatures et incertitudes.

### Résultat attendu

Un contraste plus précis entre :

```text
architecture de secteur ;
paramètres de saveur ;
coefficient effectif ;
seuil et domaine de validité ;
explication d’origine.
```

## 6. Phase P5 — Cosmologie générale, cycle 7

### Condition d’ouverture

Ne pas ouvrir le cycle entier comme simple mise à jour bibliographique. Définir une
question et une combinaison de sondes bornées.

### Entrées possibles

```text
H0 et échelles de distance ;
S8 et croissance ;
énergie noire DESI DR2 ;
reconstruction des masses neutrino ;
comparaison BAO, forme complète, lentillage et supernovae.
```

### Règle

Chaque reprise doit séparer observable, produit de données, likelihood, modèle de
passage, nuisance, prior et construction statistique.

## 7. Phase P6 — Ajustement fin et quasi-fixité, cycles 9 et 10

### Cycle 9

Construire les espaces et mesures sous lesquels une sensibilité peut être qualifiée
d’improbabilité.

### Cycle 10

Tester des mécanismes microscopiques capables ou incapables de produire la fenêtre
dissipative phénoménologique.

### Critère commun

```text
ne pas convertir une possibilité en probabilité ;
ne pas convertir une trajectoire en histoire ;
ne pas déplacer silencieusement la dette énergétique ou le réglage.
```

## 8. Voie parallèle E — Laboratoire éditorial expérimental

Le laboratoire éditorial peut progresser en parallèle des phases scientifiques,
avec une règle de non-ingérence :

> un besoin narratif ne peut pas transformer une dette ouverte en résultat acquis.

### Sous-étapes

1. Renommer le répertoire et conserver l’historique.
2. Séparer clairement :

```text
plans ;
sources et fiches ;
travail d’écriture ;
relecture ;
versions candidates.
```

3. Établir une véritable différence entre `travail_ecriture` et `relecture`.
4. Soumettre chaque section à quatre contrôles :

```text
exactitude physique ;
fonction argumentative ;
attribution et littérature ;
limites et modalisation.
```

5. N’intégrer au texte public que les cycles dont le résultat requis est assez
   stabilisé.

### Première cible

L’essai *Qualifier la constance* reste un coup d’essai à forte valeur diagnostique.
Il ne devient pas automatiquement le livrable directeur du projet.

## 9. Voie parallèle H — Philosophie en réserve

Le pan philosophique ne reprend pas comme programme autonome par inertie. Il peut
être rouvert lorsque :

```text
une question scientifique appelle une clarification conceptuelle ;
un argument éditorial rencontre une objection précise ;
un pilote exige un positionnement bibliographique ;
une distinction du cadre échoue sur plusieurs cas.
```

Les matériaux Stern–Gerlach, interférence, coupes et accès sont alors traités comme
ressources ciblées, non comme centre implicite.

## 10. Cadence Git après consolidation

```text
main : état validé et lisible ;
une branche thématique : une dette bornée ;
une PR : un objet, un résultat et ses limites ;
les données externes : hors Git ;
les sorties dérivées : versionnées ;
les décisions : enregistrées seulement lorsqu’elles changent rang, portée ou ordre.
```

Éviter une nouvelle pile longue de PR. Une branche suivante doit partir du `main`
mis à jour, sauf dépendance scientifique réelle et explicitement déclarée.

## 11. Ordre recommandé immédiat

```text
P0 — consolidation et visibilité ;
P1 — ingestion locale DESI DR2 et verdict C2 ;
P2 — cycle 1 ;
E  — laboratoire éditorial en parallèle, sans priorité scientifique ;
P3–P6 — selon les résultats et besoins comparatifs ;
H  — philosophie sur question précise.
```

## 12. Règle de révision de la feuille de route

Cette feuille doit être révisée lorsqu’un chantier :

```text
révèle une dépendance non anticipée ;
invalide la pondération d’un cycle ;
produit un résultat qui change l’ordre des dettes ;
ou impose une décision éditoriale nouvelle.
```

Elle ne doit pas être réécrite pour chaque commit de routine.
