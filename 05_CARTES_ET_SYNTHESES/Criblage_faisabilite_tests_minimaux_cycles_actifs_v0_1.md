# Criblage de faisabilité des tests minimaux des cycles actifs v0.1

## 0. Statut

```text
statut : criblage préparatoire de troisième passe ;
date : 21 juillet 2026 ;
branche : agent/crise-fondatrice-audit-fondations ;
fonction : déterminer quels tests minimaux peuvent réellement être exécutés, à quel coût
           cognitif et technique, avec quel pouvoir discriminant et quelle condition d'arrêt ;
ne vaut pas : classement de valeur des cycles, allocation définitive du travail,
              ouverture automatique d'un chantier, ni validation des résultats attendus.
```

Ce document complète :

- `Inventaire_valeur_autonome_dix_cycles_v0_1.md` ;
- `Audit_maturite_potentiel_non_teste_cycles_actifs_v0_1.md` ;
- `Carte_refonte_hors_dix_cycles_v0_1.md`.

Le principe est :

```text
potentiel intellectuel
≠
faisabilité immédiate ;

faisabilité immédiate
≠
priorité scientifique absolue.
```

Un test minimal doit pouvoir faire monter, stabiliser ou réduire le statut d'un dossier.
Un travail qui ne pourrait que produire une nouvelle synthèse compatible avec le cadrage
n'est pas retenu comme test discriminant.

---

## 1. Critères de faisabilité

### F1 — accessibilité des matériaux

```text
sources primaires ;
données ou produits publics ;
code, formats ou documentation ;
licence et provenance ;
volume compatible avec une reprise locale.
```

### F2 — opération non verbale

Le test doit comporter au moins une opération résistante à une simple reformulation :

```text
calcul ;
reproduction ;
profil statistique ;
propagation d'incertitude ;
running ou matching ;
comparaison quantitative ;
reconstruction de chaîne ;
exclusion documentaire établie sur sources primaires.
```

### F3 — pouvoir discriminant

Le résultat doit pouvoir modifier une décision :

```text
comparaison recevable ou non ;
objet effectivement contraint ;
source dominante d'incertitude ;
validité d'un mécanisme ;
statut d'une prétendue tension ;
portée d'une généralisation ;
maintien ou réduction du cycle.
```

### F4 — coût et dépendances

Le coût est qualifié sans durée prévisionnelle :

```text
faible : données et outils disponibles, périmètre étroit ;
moyen : acquisition ou adaptation de code, plusieurs conventions à contrôler ;
élevé : modification substantielle d'un modèle, calcul scientifique nouveau,
        nombreuses dépendances ou validation spécialisée.
```

### F5 — condition d'arrêt

Chaque test doit posséder une sortie négative recevable. Une impossibilité documentée,
un résultat standard correctement reproduit ou l'absence de gain propre peuvent clore le
test sans ouvrir une nouvelle couche de méthode.

---

## 2. Cycle 1 — couplages, échelles et QCD

### Test candidat

Reproduire une étape non triviale d'une chaîne phénoménologique publique de détermination
de `alpha_s`, puis comparer sa structure d'incertitude au pipeline lattice ALPHA 2026.

### Cible réaliste

Une chaîne fondée sur des distributions de formes d'événements publiées dans HEPData et,
si possible, sur une analyse Rivet existante. Le test ne doit pas prétendre reproduire
d'emblée l'ajustement moderne complet à 895 intervalles, avec toutes ses corrections de
puissance et son enveloppe théorique, si le code et les covariances ne sont pas publics.

Sources et outils repérés :

- HEPData, distributions et résultats JADE sur les formes d'événements ;
- analyses Rivet associées à plusieurs jeux de données ;
- publication moderne déjà fichée dans T1 pour le verdict final de `alpha_s`.

### Opération minimale

```text
1. sélectionner une distribution et une énergie documentées ;
2. récupérer les données, erreurs et covariance lorsqu'elle existe ;
3. reproduire un calcul ou un ajustement borné, avec une théorie explicitement choisie ;
4. varier au moins une hypothèse théorique ou une échelle ;
5. comparer le budget obtenu au type de budget de la chaîne lattice ;
6. dire si cette comparaison change réellement le statut de T1.6/T1.7.
```

### Faisabilité

```text
accessibilité : moyenne à forte pour les données historiques publiques ;
code exact de la chaîne moderne : non établi ;
coût : moyen ;
pouvoir discriminant : moyen à fort ;
risque : produire seulement une calibration ancienne sans incidence sur le verdict moderne.
```

### Condition d'arrêt

Si aucune étape moderne substantielle ne peut être rejouée et si le test historique ne
révèle qu'une dépendance théorique déjà connue, classer le résultat comme calibration
documentaire et ne pas prolonger T1 vers une philosophie générale.

### Décision de criblage

```text
faisable après réduction du périmètre ;
non premier test à lancer ;
T1.6/T1.7 restent suspendus comme conclusions de cycle jusqu'à décision séparée.
```

---

## 3. Cycle 5 — Saveur–Higgs

### Test candidat

Reconstituer un sous-dossier CKM borné, de l'observable publiée à la contrainte sur un
élément de matrice, puis tester ce que la carte Saveur–Higgs ajoute réellement.

### Cible réaliste

Le premier rang de CKM ou une tension locale `V_us` / `V_ud`, avec :

```text
décroissance ou observable choisie ;
corrections théoriques ;
entrée expérimentale ;
likelihood ou combinaison ;
paramètre CKM extrait ;
test d'unitarité correspondant.
```

Outils repérés :

- revue CKM du Particle Data Group ;
- paquet ouvert `flavio`, comprenant observables de saveur, paramètres, prédictions et
  construction de likelihoods ;
- formats et bases de paramètres utilisables pour une reprise locale.

### Opération minimale

```text
1. choisir une seule extraction ou une petite combinaison ;
2. reconstruire les entrées et corrections principales ;
3. exécuter la prédiction et la likelihood avec flavio ou calcul équivalent ;
4. identifier les corrélations et paramètres de nuisance ;
5. tester si la représentation architecturale modifie un diagnostic scientifique,
   plutôt que de simplement réénoncer le réseau de dépendances.
```

### Faisabilité

```text
accessibilité : forte ;
outillage : fort ;
coût : faible à moyen ;
pouvoir discriminant : fort pour le statut du cycle 5 ;
risque : choisir une tension trop vaste ou dépendante d'une combinaison globale non publique.
```

### Condition d'arrêt

Si l'architecture Saveur–Higgs n'ajoute aucune conséquence au traitement standard de
l'extraction, conserver le cycle comme synthèse sectorielle et abandonner la recherche
d'un gain méthodologique propre sur ce cas.

### Décision de criblage

```text
faisable après verrouillage exact de la cible ;
bon candidat de deuxième vague ;
privilégier un dossier CKM étroit plutôt qu'un ajustement global ou tout le secteur Higgs.
```

---

## 4. Cycle 6 — théories effectives à basse énergie

### Test candidat

Suivre un coefficient depuis une échelle haute jusqu'à une observable basse énergie par
running et matching, puis distinguer la variation des coefficients de la stabilité de la
prédiction physique.

### Outils repérés

```text
WCxf : format public d'échange des coefficients de Wilson ;
wilson : running et matching SMEFT -> WET ;
flavio : calcul de plusieurs observables de basse énergie ;
documentation et exemples publics.
```

### Opération minimale

```text
1. choisir un opérateur et une convention de base ;
2. fixer un coefficient à une échelle haute ;
3. exécuter running et matching vers WET ;
4. calculer une observable avec flavio ou outil équivalent ;
5. répéter sous changement contrôlé d'échelle ou de représentation ;
6. vérifier ce qui change dans les coefficients et ce qui demeure stable dans la prédiction ;
7. comparer les trois mécanismes du cycle seulement après ce résultat local.
```

### Faisabilité

```text
accessibilité : très forte ;
outillage : très fort ;
coût : faible à moyen ;
pouvoir discriminant : fort ;
risque : choisir un exemple trop pédagogique qui ne teste aucune difficulté du cycle.
```

### Condition de montée

Le cycle monte si le test rend visible une différence non triviale entre stabilité de la
prédiction, dépendance de base, matching et validité, ou s'il montre qu'une comparaison
intersectorielle corrige une inférence concrète.

### Condition de réduction

Si le test ne fait qu'illustrer la grammaire standard des EFT, clore T3 comme démonstration
pédagogique et ne pas revendiquer de méthode comparative propre.

### Décision de criblage

```text
prêt à être exécuté ;
excellent test de calibration méthodologique ;
priorité de faisabilité élevée, sans préjuger de sa valeur philosophique.
```

---

## 5. Cycle 7 — cosmologie

### Test candidat

Reproduire une chaîne d'inférence cosmologique complète et tester l'effet d'un changement
contrôlé de modèle, de prior ou de combinaison de données.

### Matériaux repérés

```text
produits publics DESI Data Release 2 ;
chaînes cosmologiques et maxima postérieurs distribués ;
likelihood DESI DR2 disponible dans Cobaya ;
environnement local déjà acquis lors de C2.
```

### Cible réaliste

Ne pas répéter le chantier neutrino C2. Choisir par exemple :

```text
H_0 et Omega_m sous une combinaison bornée ;
ou w_0 / w_a sous deux choix de données ;
ou un déplacement de tension sous changement explicite de modèle ou de prior.
```

### Opération minimale

```text
1. verrouiller modèle, jeux de données et paramètres ;
2. reproduire une chaîne ou un postérieur officiel ;
3. changer une seule hypothèse structurante ;
4. quantifier le déplacement du postérieur et des dégénérescences ;
5. déterminer si la prétendue propriété de l'objet ou tension visait en réalité le pont
   inférentiel, le modèle ou les données.
```

### Faisabilité

```text
accessibilité : forte ;
outillage : fort ;
coût : moyen ;
pouvoir discriminant : fort ;
risque : duplication du cycle 3 ou dérive vers une veille cosmologique générale.
```

### Condition d'arrêt

Une reproduction qui ne change aucune décision conceptuelle reste un dossier de compétence
computationnelle. Un changement de modèle qui déplace seulement les chiffres sans localiser
le mécanisme inférentiel ne suffit pas à ouvrir une généralisation.

### Décision de criblage

```text
faisable après verrouillage d'une cible non neutrino ;
bon candidat de première ou deuxième vague selon disponibilité computationnelle ;
maintenir une seule sonde ou combinaison par test.
```

---

## 6. Cycle 8 — Système international d'unités

### Test candidat

Quantifier le déplacement de l'incertitude et la fonction de la valeur de référence dans
les comparaisons successives de réalisations du kilogramme après la redéfinition du SI.

### Matériaux repérés

```text
Bureau international des poids et mesures : brochure du SI et mises en pratique ;
Key Comparison Database : comparaisons internationales de réalisations du kilogramme ;
résultats quantitatifs disponibles pour plusieurs campagnes postérieures à 2019.
```

La comparaison 2024, publiée en 2026, fournit notamment une valeur de référence de
comparaison et son incertitude. Les campagnes précédentes permettent une comparaison
datée des écarts, de la dispersion et du rôle de la valeur de consensus.

### Opération minimale

```text
1. sélectionner les comparaisons 2019, 2021 et 2024 ou le sous-ensemble officiellement
   comparable ;
2. reconstruire les valeurs de référence, incertitudes et écarts des laboratoires ;
3. comparer dispersion, incertitude de référence et compatibilités ;
4. identifier ce que la fixation de h a changé dans la fonction de l'expérience ;
5. identifier où l'incertitude demeure et comment elle circule.
```

### Faisabilité

```text
accessibilité : très forte ;
outillage : tableur ou script léger suffisant ;
coût : faible à moyen ;
pouvoir discriminant : moyen à fort ;
risque : prendre une comparaison institutionnelle pour une démonstration philosophique.
```

### Condition d'arrêt

Si le résultat confirme seulement la structure officielle du SI sans conséquence
supplémentaire, le cycle reste une étude métrologique autonome. Ce résultat est recevable
et suffit à clore le test.

### Décision de criblage

```text
prêt à être exécuté ;
meilleur rapport accessibilité / netteté du résultat ;
priorité de faisabilité la plus élevée.
```

---

## 7. Cycle 9 — fine-tuning

### Test candidat

Construire explicitement l'espace de variation et la région de viabilité d'un seul cas,
avant tout langage d'improbabilité.

### Cible recommandée

Un test sur l'échelle faible et la nucléosynthèse primordiale, plutôt que le cas Hoyle en
première reprise. Le cas doit conserver plusieurs variables ou corrélations physiques au
lieu d'une coupe unidimensionnelle isolée.

Outils et voisinages repérés :

```text
LINX : code JAX public, rapide et différentiable pour la nucléosynthèse primordiale ;
AlterBBN et autres codes de nucléosynthèse comme voisins ;
littérature sur la variation de l'échelle faible dans un espace multidimensionnel et les
frontières catastrophiques de BBN.
```

### Opération minimale en deux portes

#### Porte 9A — reconstruction du problème

```text
1. identifier les variables réellement indépendantes du cas publié ;
2. reconstruire les relations analytiques et les frontières de viabilité ;
3. vérifier ce qui est tenu fixe et pourquoi ;
4. déterminer quelles directions compensées sont physiques, libres ou simplement choisies.
```

#### Porte 9B — calcul

```text
5. reproduire une coupe bidimensionnelle avec un code BBN public ou une adaptation bornée ;
6. comparer coupe, région multidimensionnelle et critère de viabilité ;
7. refuser tout langage probabiliste en l'absence de mesure justifiée ;
8. localiser la contingence résiduelle après les corrélations.
```

### Faisabilité

```text
accessibilité : moyenne à forte pour le code BBN ;
adaptation au changement de l'échelle faible : non prête à l'emploi ;
coût : élevé ;
pouvoir discriminant : très fort ;
risque : transformer une modification complexe de code en confirmation implicite du cadrage.
```

### Condition d'arrêt

Si la porte 9A ne permet pas de définir des variables et une région scientifiquement
contrôlables, ne pas ouvrir le calcul. Si le calcul reproduit seulement une fenêtre déjà
connue sans clarifier la contingence, conserver le cas comme reconstruction de littérature.

### Décision de criblage

```text
forte valeur scientifique potentielle ;
non prêt pour exécution immédiate ;
ouvrir d'abord un dossier de sélection et de reconstruction, sans branche de calcul.
```

---

## 8. Cycle 10 — quasi-fixité électrofaible

### Test candidat

Comparer la fenêtre phénoménologique requise pour `Gamma/H` à un mécanisme microscopique
minimal de transfert ou de désintégration du condensat.

### Cibles possibles

```text
mélange scalaire-Higgs sous légère brisure de Z_2 ;
désintégration vers fermions légers ;
transfert vers un second scalaire relativiste ;
annihilation ou évaporation thermique du condensat.
```

La littérature fournit des contraintes sur les scalaires de portail Higgs, leurs durées de
vie, leurs désintégrations hadroniques, les condensats oscillants et la nucléosynthèse. Aucun
code prêt à l'emploi n'a été identifié pour le modèle exact du cycle.

### Opération minimale en trois portes

#### Porte 10A — sélection

```text
choisir un seul canal ;
écrire le lagrangien minimal ;
déterminer les paramètres indépendants ;
établir les contraintes déjà publiées.
```

#### Porte 10B — ordre de grandeur

```text
dériver le taux microscopique ;
le comparer à la fenêtre requise de Gamma/H ;
identifier le domaine thermique pertinent ;
vérifier les ordres de grandeur BBN, mélange et rayonnement caché.
```

#### Porte 10C — intégration

```text
n'intégrer les équations cosmologiques modifiées que si un domaine non vide subsiste.
```

### Faisabilité

```text
accessibilité de la littérature : moyenne à forte ;
outillage exact : faible ;
coût : élevé ;
pouvoir discriminant : très fort ;
risque : ouvrir un vaste modèle BSM avant d'avoir éliminé le canal par ordre de grandeur.
```

### Condition d'arrêt

Un canal exclu par les taux requis ou les contraintes connues constitue un résultat négatif
suffisant. Ne pas chercher immédiatement un nouveau canal dans la même branche sans revue.

### Décision de criblage

```text
recherche physique de haute valeur ;
commencer par une note de sélection et des ordres de grandeur ;
calcul complet seulement après passage des portes 10A et 10B.
```

---

## 9. Portefeuille de faisabilité

### Groupe A — prêts à être exécutés

```text
cycle 8 : comparaisons post-2019 des réalisations du kilogramme ;
cycle 6 : running, matching et observable avec WCxf / wilson / flavio.
```

Ces deux tests ont un périmètre clair, des matériaux publics, une sortie négative recevable
et un coût limité. Ils sont particulièrement adaptés pour vérifier que la nouvelle méthode
de tests minimaux ne produit pas automatiquement un résultat favorable.

### Groupe B — prêts après verrouillage de la cible

```text
cycle 7 : chaîne DESI / Cobaya sur un paramètre non neutrino ;
cycle 5 : extraction CKM étroite avec flavio et sources primaires.
```

### Groupe C — faisables après acquisition ou réduction supplémentaire

```text
cycle 1 : sous-chaîne publique de formes d'événements ;
```

Le cycle 1 est déjà actif et avancé, mais le test phénoménologique exact doit être choisi
en fonction de la disponibilité réelle des données, covariances et calculs.

### Groupe D — programmes de recherche à portes successives

```text
cycle 9 : espace multidimensionnel de fine-tuning et BBN ;
cycle 10 : mécanisme microscopique de dissipation.
```

Leur valeur potentielle est élevée. Leur coût interdit de les ouvrir comme simples tâches
documentaires. Ils exigent une décision scientifique après chaque porte.

---

## 10. Ordre de lancement proposé

L'ordre proposé n'est pas une hiérarchie intellectuelle :

```text
0. stabiliser l'ergonomie et l'état des chantiers ;
1. exécuter un test court et quantitatif : cycle 8 ;
2. exécuter un test technique de transformation : cycle 6 ;
3. choisir entre cycle 7 et cycle 5 selon la question la plus nette ;
4. ouvrir en parallèle uniquement la porte de sélection du cycle 9 ou 10 ;
5. reprendre la chaîne phénoménologique QCD après décision sur le statut de la PR 18.
```

Le cycle 9 ne doit pas être repoussé parce qu'il est coûteux. Sa porte 9A peut être ouverte
comme travail de fond sans lancer immédiatement une branche computationnelle. Le même
principe vaut pour 10A.

---

## 11. Limite de travail en cours

À tout moment :

```text
un chantier de refonte / ergonomie ;
un test physique ou métrologique exécuté ;
un chantier de sélection difficile ou un audit hors-cycle.
```

Aucun quatrième chantier actif ne doit être ouvert avant clôture, blocage documenté ou
mise en attente explicite de l'un des trois.

Cette limite porte sur les unités cognitives actives, non sur le nombre matériel de branches
encore présentes dans l'historique GitHub.

---

## 12. Verdict de criblage

> Le dépôt dispose de plusieurs tests minimaux réellement exécutables. Les cycles 8 et 6
> offrent les meilleures conditions pour calibrer la nouvelle procédure ; les cycles 7 et 5
> sont bien outillés après réduction de la cible ; le cycle 1 demande une sélection prudente
> de la chaîne phénoménologique ; les cycles 9 et 10 doivent être traités comme des programmes
> de recherche à portes successives. La faisabilité ne détermine pas la valeur, mais elle
> permet de coordonner le travail sans confondre promesse, maturité et résultat.

Aucune branche de test, pull request, issue ou modification canonique n'est ouverte par le
présent criblage.