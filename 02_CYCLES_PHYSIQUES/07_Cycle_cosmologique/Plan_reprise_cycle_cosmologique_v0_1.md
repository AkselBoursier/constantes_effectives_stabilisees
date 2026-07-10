# Plan de reprise du cycle cosmologique v0.1

## Reprise controlee apres stress test cosmologique

### 1. Fonction du document

Ce document prepare une reprise du cycle cosmologique.

Il ne constitue pas un addendum durable.

Il sert a decider :

```text
ce qui doit etre reecrit,
ce qui doit rester historique,
ce qui doit etre seulement reference,
et ce qui ne doit pas encore etre ouvert.
```

Il prolonge directement :

```text
02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Synthese_cycle_cosmologique_v0_1.md
04_ARCHITECTURES_INTER_FAMILLES/Architecture_cosmologique_notes.md
04_ARCHITECTURES_INTER_FAMILLES/Architecture_cosmologique_stress_test_v0_1.md
05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_2_refonte.md
```

Question directrice :

```text
comment reprendre les fiches cosmologiques avec les sous-reseaux,
sans ajouter une couche de complexite inutile ?
```

### 2. Decision de principe

Decision :

```text
ne pas produire un addendum cosmologique permanent
si une reprise locale des fiches suffit.
```

Le stress test a rendu visible une structure plus fine.

Cette structure doit maintenant guider la reprise des fiches existantes.

Formule :

```text
le plan prepare une reecriture controlee ;
il ne remplace pas la reecriture.
```

### 3. Statut documentaire

Statut :

```text
plan de reprise transitoire.
```

Ce document doit etre utilise pour :

```text
ouvrir une reprise du cycle,
choisir l'ordre des corrections,
eviter les doublons,
et proteger les limites methodologiques.
```

Il ne doit pas devenir :

```text
une nouvelle synthese cosmologique,
une nouvelle carte consolidee,
une couche interpretative autonome,
ou une branche philosophique.
```

### 4. Role du workflow GitHub

Le workflow GitHub change la maniere de reprendre les documents.

Avant le depot Git, une reprise pouvait pousser a creer des couches successives :

```text
fiche,
note,
addendum,
addendum de l'addendum,
nouvelle synthese locale.
```

Avec Git, la reprise peut devenir plus sobre.

Regle :

```text
si la correction est une clarification interne,
modifier le document actif plutot que creer un doublon.
```

Git conserve l'historique.

Le dossier n'a donc pas besoin de conserver chaque etat intermediaire comme fichier separe.

### 5. Branche recommandee

Pour une reprise complete du cycle, la branche recommandee serait :

```text
agent/reprise-cycle-cosmologique
```

Cette branche permettrait de modifier plusieurs fiches sans rendre `main` instable.

Elle serait utile si la reprise porte sur :

```text
le cadrage,
les six fiches locales,
la synthese,
et les references croisees.
```

Pour une seule correction ponctuelle, `main` peut rester suffisant apres validation.

### 6. Frontieres du chantier

La reprise du cycle cosmologique reste dans le champ suivant :

```text
taxonomie,
methode,
statut des grandeurs,
regimes physiques,
regimes d'acces,
dependances de modele,
sous-reseaux,
et limites de classement.
```

Elle n'ouvre pas encore :

```text
prediction,
philosophie,
metaphysique des constantes,
programme cosmologique alternatif,
ou theorie physique nouvelle.
```

La branche philosophique n'est pas rejetee.

Elle est seulement notee comme horizon non actif.

Formule :

```text
ne pas enterrer la philosophie ;
ne pas l'activer avant stabilisation du socle methodologique.
```

### 7. Corpus concerne

Le corpus concerne est le cycle cosmologique Markdown.

```text
02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Cycle_cosmologique_v0_1_cadrage.md
02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Cycle_cosmologique_v0_2_Lambda.md
02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Cycle_cosmologique_v0_3_H0.md
02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Cycle_cosmologique_v0_4_Omega_i.md
02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Cycle_cosmologique_v0_5_w.md
02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Cycle_cosmologique_v0_6_As_ns.md
02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Cycle_cosmologique_v0_7_sigma8_S8.md
02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Synthese_cycle_cosmologique_v0_1.md
```

Documents de controle :

```text
04_ARCHITECTURES_INTER_FAMILLES/Architecture_cosmologique_stress_test_v0_1.md
01_CADRE_METHODOLOGIQUE/Note_synthese_methodologique_v1_3_pre_familial_et_temporalite.md
05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_2_refonte.md
```

### 8. Decisions acquises a ne pas rouvrir

La reprise ne doit pas remettre en cause les decisions suivantes.

```text
Cosmologie n'est pas une famille.
Fond n'est pas une famille.
Tension n'est pas une famille.
Lambda n'est pas Omega_Lambda.
Omega_Lambda n'est pas w.
H_0 n'est pas une constante fondamentale.
A_s n'est pas sigma_8.
S_8 n'est pas une tension.
Une valeur cosmologique doit toujours etre lue avec son regime d'acces.
```

Ces decisions peuvent etre mieux formulees.

Elles ne sont pas a replaider a chaque fiche.

### 9. Nouvelle lecture directrice

La lecture directrice issue du stress test est :

```text
Architecture cosmologique =
macro-architecture inferentielle / reconstructive
composee de sous-reseaux internes.
```

Sous-reseaux :

| Sous-reseau | Grandeurs | Fonction de reprise |
|---|---|---|
| Fond / expansion | `Lambda`, `H_0` | Distinguer fond, taux actuel et routes d'acces |
| Budget normalise | `Omega_i` | Clarifier normalisation, rho_crit, dependance a H |
| Etat de composante | `w` | Distinguer relation d'etat, parametrisation et microphysique |
| Primordial | `A_s`, `n_s` | Distinguer conditions initiales et origine physique |
| Croissance / reconstruction | `sigma_8`, `S_8` | Clarifier reconstruction, acces et tension |
| Tensions transversales | `H_0`, `S_8`, `w(a)` | Ne pas transformer une tension en categorie |

### 10. Grille de reprise de chaque fiche

Chaque fiche reprise devrait comporter explicitement :

```text
1. sous-reseau concerne ;
2. role contextuel principal ;
3. regime physique ;
4. regime d'acces ;
5. modele d'inference ;
6. test de retrait ;
7. tension eventuelle ;
8. limite conservee.
```

Cette grille reprend le protocole du stress test.

Elle doit etre integree dans les fiches elles-memes, pas seulement citee dans une note externe.

### 11. Niveaux d'intervention

La reprise doit distinguer trois niveaux.

| Niveau | Intervention | Usage |
|---|---|---|
| 1 | Correction locale | Formulation obsolete, lien manquant, statut a ajuster |
| 2 | Reprise structurelle courte | Ajout du sous-reseau, du test de retrait, de la limite |
| 3 | Reecriture de fiche | Si l'ordre interne de la fiche masque la decision actuelle |

Regle :

```text
ne pas reecrire une fiche entiere si une reprise structurelle courte suffit.
```

### 12. Plan par document

| Document | Reprise recommandee | Niveau |
|---|---|---|
| `Cycle_cosmologique_v0_1_cadrage.md` | Replacer le cadrage par macro-architecture et sous-reseaux, garder la prudence initiale | 2 |
| `Cycle_cosmologique_v0_2_Lambda.md` | Ajouter sous-reseau fond / expansion et test de retrait avec H_0, Omega_Lambda, w | 2 |
| `Cycle_cosmologique_v0_3_H0.md` | Ajouter sous-reseau fond / expansion, routes d'acces et tension transversale | 2 |
| `Cycle_cosmologique_v0_4_Omega_i.md` | Reprendre comme budget normalise, expliciter dependance a H et rho_crit | 2 |
| `Cycle_cosmologique_v0_5_w.md` | Reprendre comme etat de composante, separer parametrisation et explication physique | 2 |
| `Cycle_cosmologique_v0_6_As_ns.md` | Reprendre comme sous-reseau primordial, clarifier lien non identitaire a sigma_8 | 2 |
| `Cycle_cosmologique_v0_7_sigma8_S8.md` | Reprendre comme croissance / reconstruction, sous-reseau sous tension | 2 |
| `Synthese_cycle_cosmologique_v0_1.md` | Reecrire la synthese finale autour des sous-reseaux et non seulement des six fonctions | 3 |

Priorite :

```text
1. reprendre le cadrage ;
2. reprendre la synthese ;
3. reprendre les fiches locales ;
4. controler les references croisees.
```

Justification :

```text
le cadrage et la synthese donnent l'ossature ;
les fiches locales deviennent ensuite des preuves alignees.
```

### 13. Reprise du cadrage

Le cadrage doit garder sa prudence initiale.

Il doit toutefois remplacer la question :

```text
quelles grandeurs cosmologiques classer ?
```

par :

```text
comment classer des grandeurs cosmologiques
dans une macro-architecture a sous-reseaux ?
```

Ajouts attendus :

```text
liste des sous-reseaux,
statut de la tension comme transversal,
regle de non-ouverture philosophique,
role du modele d'inference,
et articulation avec la methode v1.3.
```

### 14. Reprise des fiches locales

Chaque fiche locale doit recevoir une section courte :

```text
Lecture apres stress test
```

Cette section doit dire :

```text
sous-reseau,
role,
dependances,
test de retrait,
limite.
```

Elle doit eviter de refaire toute la fiche si le corps principal reste valide.

### 15. Reprise de la synthese

La synthese doit etre la plus modifiee.

Elle a stabilise six fonctions :

```text
Fond
Parametre d'etat
Densite normalisee
Relation d'etat
Condition initiale
Observable reconstruite
```

La reprise doit conserver ces fonctions, mais les organiser par sous-reseaux.

Nouvelle formule cible :

```text
le cycle cosmologique stabilise une macro-architecture
dont les fonctions locales se repartissent en sous-reseaux
et dont les tensions appartiennent aux regimes d'acces et de modele.
```

### 16. Donnees et sources

La reprise v0.1 ne doit pas chercher a actualiser toutes les donnees cosmologiques.

Regle :

```text
ne verifier les sources externes que si une valeur, une date,
ou une affirmation empirique instable est modifiee.
```

Si une fiche est reprise seulement pour son statut taxonomique, les sources existantes peuvent rester.

Si une fiche modifie un etat de donnees, il faudra verifier les sources primaires.

### 17. Ce qui doit rester historique

Certaines formulations anciennes doivent rester visibles comme histoire du projet.

Mais elles ne doivent pas rester actives si elles contredisent la carte actuelle.

Regle :

```text
Git conserve l'ancien etat ;
le fichier actif peut donc etre corrige sans creer une archive manuelle.
```

Exception :

```text
si une ancienne formulation est utile pour comprendre une bifurcation methodologique,
la conserver dans une courte note historique interne.
```

### 18. Criteres de reussite

La reprise est reussie si le cycle permet de lire clairement :

```text
1. ce qui est une grandeur locale ;
2. ce qui est une fonction architecturale ;
3. ce qui est un sous-reseau ;
4. ce qui est une tension transversale ;
5. ce qui depend du modele ;
6. ce qui depend de l'acces ;
7. ce qui reste physiquement ouvert.
```

Elle echoue si elle produit :

```text
une famille Cosmologie,
une famille Tension,
une accumulation d'addenda,
ou une speculation prematuree.
```

### 19. Sequence de travail recommandee

Sequence prudente :

```text
1. creer une branche de reprise si le cycle complet est ouvert ;
2. reprendre le cadrage ;
3. reprendre la synthese ;
4. reprendre une fiche pilote ;
5. verifier l'effet sur les autres fiches ;
6. poursuivre fiche par fiche ;
7. synchroniser index et carte seulement apres stabilisation.
```

Fiche pilote recommandee :

```text
Cycle_cosmologique_v0_7_sigma8_S8.md
```

Raison :

```text
c'est la fiche ou la notion de reconstruction,
de tension et de sous-reseau candidat est la plus sensible.
```

Alternative :

```text
Cycle_cosmologique_v0_3_H0.md
```

Raison :

```text
elle teste directement le rapport entre valeur actuelle,
routes d'acces et tension transversale.
```

### 20. Decision finale

Decision :

```text
ouvrir une reprise controlee du cycle cosmologique,
mais ne pas produire d'addendum cosmologique permanent.
```

Le bon mouvement n'est pas :

```text
ajouter une couche au-dessus du cycle.
```

Il est :

```text
preparer la reecriture des fiches actives
a partir de la macro-architecture et de ses sous-reseaux.
```

Formule finale :

> La reprise cosmologique doit transformer le stress test en clarification interne du cycle, non en surcouche documentaire.
