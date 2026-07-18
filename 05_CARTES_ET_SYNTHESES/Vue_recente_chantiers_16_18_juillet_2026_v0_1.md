# Vue récente des chantiers — 16 au 18 juillet 2026 v0.1

## 0. Fonction et statut

```text
fonction : restituer la séquence récente sans demander une lecture du corpus entier ;
période : du 16 au 18 juillet 2026 ;
base : vue d’ensemble v0.3, travaux neutrino N0–N5, reprise C1–C2,
       ouverture du laboratoire éditorial et diagnostic de consolidation ;
ne vaut pas : vue générale du projet, validation définitive des résultats,
              décision de fusion dans main ou plan éditorial contraignant.
```

Cette vue complète la vue globale v0.4. Elle répond à la question : **qu’avons-nous
fait récemment, dans quel ordre, et qu’est-ce que cela a changé ?**

## 1. Point de départ : consolidation comparative

Au 16 juillet, les dix cycles physiques avaient été récupérés et comparés par cinq
contrastes :

```text
cycles 1–6 : échelle, régime et validité ;
cycles 2–5 : fonction, architecture et explication ;
cycles 3–7 : accès, reconstruction et mesure ;
cycles 4–8 : mesure, définition et réalisation ;
cycles 9–10 : contrefactuel, dynamique et contingence.
```

La vue d’ensemble v0.3 avait alors stabilisé trois dimensions sans ordre universel :
objet, constitution et accès. Elle laissait encore ouverte la sélection d’une dette
scientifique prioritaire.

## 2. Instruction du paysage contemporain de la mesure

Le chantier suivant a refusé de traiter comme un seul problème :

```text
le problème quantique du résultat défini ;
la production et la calibration classiques ;
la mesure relativiste ;
la reconstruction cosmologique.
```

Le résultat est double :

1. une continuité des chaînes de médiation existe entre interaction, trace,
   sélection, calibration, modèle et inférence ;
2. les difficultés physiques et statistiques ne sont pas identiques d’un domaine
   à l’autre.

Cette distinction a permis de transformer les « dettes » générales des cycles en
opérations plus précises : reconstruire un accès, vérifier une source, reproduire
un calcul, expliciter une covariance ou redater un état empirique.

## 3. Arbitrage des dettes des dix cycles

L’arbitrage a retenu le cycle 3 — neutrinos — comme première dette scientifique à
lever. Les raisons étaient :

```text
pluralité nette des accès ;
actualité empirique forte ;
fonction discriminante pour le projet ;
possibilité d’un protocole commun sans homogénéiser les expériences.
```

Le cycle 1 — couplages, échelles et chromodynamique quantique — est resté le
candidat prioritaire suivant. Le cycle 7 a été différé en raison de son étendue et
de son obsolescence rapide. Les cycles 4 et 8 ont conservé leur fonction de
contrôle métrologique.

## 4. Reconstruction du cycle neutrino N0–N5

### N0 — protocole commun

`N0` a fixé la discipline des quatre fiches d’accès : trace primaire, observable,
modèle de passage, hypothèses, construction statistique, résultat positif, limites
et ponts vers les autres voies.

### N1 — oscillations

`N1` établit une architecture différentielle : écarts de masses au carré, angles
de mélange et phase. Elle ne fournit pas l’ancrage absolu du spectre.

### N2 — cinématique bêta

`N2` reconstruit la chaîne locale de KATRIN vers :

```math
m_\beta^2=\sum_i |U_{ei}|^2 m_i^2.
```

La borne publiée reste une borne cinématique locale et non une mesure positive des
masses individuelles.

### N3 — cosmologie

`N3` reconstruit l’inférence globale vers `Sigma m_nu`. La borne serrée sous
`LambdaCDM` est principalement issue de la cohérence CMB–BAO et dépend du modèle,
des likelihoods, des priors et de la paramétrisation du secteur neutrino.

### N4 — double bêta sans neutrino

`N4` conserve la demi-vie isotopique comme résultat expérimental primaire. La
conversion vers `m_beta beta` reste conditionnelle au mécanisme et aux éléments de
matrice nucléaire.

### N5 — comparaison

`N5` montre que les quatre voies contraignent quatre fonctions différentes d’un
spectre latent. Elles ne fournissent pas quatre mesures répétées d’une grandeur déjà
identifiée. La seule zone de frottement saillante se situe entre les planchers de
`N1` et la reconstruction `N3` sous le modèle cosmologique de base.

## 5. Reprise computationnelle N1–N3

### C1 — planchers, frontière et priors

`C1` a reconstruit les planchers oscillatoires :

```text
ordre normal : environ 0,05871 eV ;
ordre inversé : environ 0,09884 eV.
```

Leur incertitude propagée est trop faible pour absorber le frottement cosmologique.
Un substitut gaussien minimal a ensuite isolé l’effet de la frontière et montré que
la borne postérieure change fortement lorsque le domaine passe de `Sigma >= 0` au
plancher normal ou inversé.

### C2 — produits officiels DESI DR2

`C2` a identifié :

```text
base_mnu : frontière à zéro ;
base_mnu059 : plancher scalaire à 0,059 eV ;
base_mnu_binary_3 : traitement physique des ordres avec information oscillatoire ;
base_mnu_w_wa : ouverture de l’histoire d’expansion.
```

La phase a produit un manifeste et un lecteur pondéré, mais n’a pas déclaré les
quantiles reproduits sans lecture des chaînes. Les données sont désormais présentes
localement sous `data_external/desi_dr2`, répertoire ignoré par Git. Une instruction
spécifique encadre leur ingestion par un agent local.

## 6. Ouverture du laboratoire éditorial expérimental

Un premier environnement de rédaction a été ouvert pour tester le passage du corpus
à un essai continu. Il contient :

```text
trois états du plan soustractif ;
fiches de lecture et recherche croisée ;
premier jet de « Qualifier la constance » ;
copie destinée à une future couche de relecture.
```

Son rôle n’est pas de publier prématurément un texte, mais de tester :

```text
la sélection du matériau ;
la continuité argumentative ;
la tenue rédactionnelle ;
la capacité des cas physiques à produire un résultat lisible hors du dépôt.
```

Le répertoire `93_LABORATOIRE_EDITORIAL_EXPERIMENTAL` porte désormais son rang par
son nom, sans imposer une réserve répétée dans chaque document.

## 7. Diagnostic Git récent

La branche active est cumulative :

```text
branche : agent/contribution-q1-information-chemin ;
avance sur main avant le présent lot : 315 commits ;
retard sur main : 0 commit ;
statut technique : fusionnable ;
statut documentaire : PR et portes d’entrée désynchronisées.
```

La PR nº 14 était encore titrée comme un chantier limité à Q1 alors qu’elle contient
désormais la consolidation, les cycles récupérés, les travaux neutrino, la reprise
computationnelle et le laboratoire éditorial. La priorité validée est donc de
restaurer une représentation fidèle avant toute nouvelle dette scientifique.

## 8. Acquis de la période

```text
le problème de la mesure n’est plus unificateur par défaut ;
la dette neutrino est levée au niveau documentaire, empirique et comparatif ;
la tension N1–N3 est décomposée en plancher, likelihood, frontière, prior et modèle ;
C2 est rendue reproductible sans fausse ingestion ;
un laboratoire éditorial est ouvert sans devenir le centre de la recherche ;
la consolidation vers main devient le chantier prioritaire de visibilité.
```

## 9. Limites maintenues

```text
C2 n’est pas close tant que les chaînes locales ne sont pas ingérées ;
les autres cycles physiques ne sont pas tous actualisés ;
le premier jet éditorial n’est pas un manuscrit validé ;
la branche n’est pas encore le tronc canonique ;
la fusion reste une décision explicite de l’auteur.
```

## 10. Passage à la vue globale

La présente vue décrit une séquence. La vue globale v0.4 replace cette séquence dans
la structure générale du projet, distingue les laboratoires et fixe les dettes sans
les confondre avec les résultats déjà acquis.
