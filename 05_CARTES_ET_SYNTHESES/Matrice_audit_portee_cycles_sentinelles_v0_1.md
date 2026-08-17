# Matrice d’audit de portée — cycles sentinelles et régimes de constance v0.1

## 0. Statut

```text
statut : deuxième passe active de l’audit de portée ;
base : documents actifs des cycles 1, 3, 4, 6, 8 et 10 ;
protocole : Cadrage_audit_portee_regimes_constance_v0_1.md ;
fonction : tester la distinction maintien / stabilisation sur des cas physiques
           hétérogènes avant toute modification des documents directeurs ;
ne vaut pas : nouvelle vérification bibliographique, réécriture des résultats,
              taxonomie universelle ou ouverture automatique de recherches.
```

## 1. Question du test

La passe ne demande pas si chaque cycle peut être décrit avec le vocabulaire des
régimes de constance. Elle demande si ce vocabulaire produit une discrimination
contrôlable que le dossier physique exige déjà.

Pour chaque cas :

```text
porteur : qu’est-ce qui peut tenir ou varier ?
transformation : relativement à quoi ?
stabilisation : quel régime physique ou probatoire devient robuste ?
chemin : la dépendance est-elle physique, historique, expérimentale,
         computationnelle ou inférentielle ?
portée : physique, épistémologique, ontologique ou non engagée ?
incidence : clarification, requalification, test ou dette ?
```

## 2. Matrice synthétique

| Cas sentinelle | Porteur principal | Transformations pertinentes | Forme de stabilisation | Dépendance de chemin | Portée dominante | Incidence | Verdict |
|---|---|---|---|---|---|---|---|
| Cycle 1 — couplages, échelles et QCD | valeur de référence, couplage courant, échelle de schéma, masse ou rapport selon le sous-cas | énergie ou impulsion `Q`, échelle `mu`, schéma, processus, temps lorsque testé séparément | transport et comparabilité des extractions ; contrôle du régime perturbatif ou non perturbatif | principalement procédurale et représentationnelle pour les extractions, schémas et raccordements ; aucune histoire temporelle déduite | physique et épistémologique ; ontologie non engagée | 2, 3, 4 | nouveau test local dans la reprise QCD |
| Cycle 3 et C2 — neutrinos | spectre latent et fonctions distinctes `Delta m²`, `m_beta`, `Sigma m_nu`, `m_beta_beta` | changement de voie, support, prior, modèle cosmologique, données et likelihood | robustesse d’une borne, d’une compatibilité ou d’un domaine admissible | inférentielle et computationnelle ; aucune dépendance physique des masses au chemin établie | physique pour l’architecture spectrale ; épistémologique pour les bornes et comparaisons ; ontologie non engagée | 3, 4 | requalification de portée et test local borné |
| Cycles 4 et 8 — thermodynamique et SI | grandeur physique, valeur numérique définissante, relation exacte par composition, réalisation | changement d’unité, passage avant / après fixation, changement de chaîne de réalisation | stabilité normative, intersubjective et internationale des valeurs numériques et comparaisons | historique, institutionnelle et expérimentale pour la réalisation ; non physique pour le rôle de la grandeur | physique et métrologique / épistémologique ; ontologie non engagée | 1, 2, 3 | clarification et requalification suffisantes ; aucune nouvelle recherche créée par l’audit |
| Cycle 6 — théories effectives | observable ou amplitude contrôlée ; terme dominant ; coefficient seulement sous qualification | `q`, `Q`, `mu`, base, schéma, seuil, ordre et domaine de validité | stabilité d’une prédiction, d’un terme dominant ou d’une expansion à précision déclarée | computationnelle et représentationnelle pour les coefficients ; continuité physique portée par observables et matching | physique et épistémologique ; ontologie non engagée | 3, 4 | test local obligatoire sur le statut de « constante effective » |
| Cycle 10 — quasi-fixité électrofaible | grandeur électrofaible explicitement couplée à un porteur dynamique ; dans le toy model, déplacement de `v` et énergie scalaire | temps cosmique, température, conditions initiales, dissipation et tolérance | relaxation physique modélisée vers une quasi-fixité avant BBN | physique dans le modèle par trajectoires et conditions initiales ; dépendante aussi de la paramétrisation choisie | physique conditionnelle au modèle ; épistémologique pour la portée ; ontologie non engagée | 3, 4, 5 existante | requalification de portée ; dette microscopique confirmée, non créée |

## 3. Cycle 1 — couplages, échelles et QCD

### 3.1 Ce que le cycle établit déjà

Le résultat récupéré est :

```text
stabilité temporelle
≠ dépendance à l’échelle
≠ identité de régime
≠ simplicité théorique.
```

Le cycle déclare déjà le porteur et la transformation : `alpha_s(Q²)` n’est pas
une valeur isolée, `Lambda_QCD` est indexée à un schéma, et une valeur de
référence de `alpha` ne doit pas être confondue avec le couplage courant.

### 3.2 Apport de la reformulation

La formule « maintien sous transformation » clarifie que le lieu de la constance
peut être :

```text
une relation entre valeurs transportées à une échelle commune ;
une cohérence entre extractions issues de processus différents ;
une observable préservée sous redistribution des composantes de calcul ;
une stabilité temporelle testée séparément.
```

Elle interdit de traiter la trajectoire du groupe de renormalisation comme
l’histoire temporelle d’un système.

### 3.3 Dépendance de chemin

Le terme n’est recevable qu’après typage :

```text
chemin d’extraction : processus -> observable -> corrections -> paramètre ;
chemin de transport : valeur extraite -> évolution RG -> échelle commune ;
chemin de raccordement : choix de seuils, saveurs actives et conventions ;
histoire physique : non établie par les trois chemins précédents.
```

La variation d’un paramètre intermédiaire selon le schéma ou le raccordement ne
suffit pas à établir une dépendance physique de l’observable au chemin.

### 3.4 Test local proposé

Dans la reprise scientifique du cycle 1, choisir plusieurs déterminations de
`alpha_s` issues de processus et d’échelles distincts, puis documenter :

```text
observable primaire ;
processus ;
échelle cinématique ;
schéma et ordre ;
corrections ;
paramètre extrait ;
transport vers une référence commune ;
corrélations ;
quantité dont la cohérence est finalement testée.
```

Ce test appartient déjà à la dette QCD prévue. L’audit en précise la fonction :
déterminer si le maintien porte sur un coefficient, une trajectoire RG, une
relation de transport ou la cohérence des observables.

### 3.5 Verdict

```text
clarification seulement : insuffisante ;
requalification de portée : oui ;
nouveau test local : oui, intégré à la reprise QCD ;
recherche externe générale : non ;
concept non pertinent : non.
```

## 4. Cycle 3 et C2 — neutrinos

### 4.1 Ce que le cycle établit déjà

Le cycle a abandonné la recherche d’une « constante de masse » unique. Les
quatre voies contraignent des fonctions distinctes d’un spectre latent et ne
sont comparables qu’au moyen de ponts physiques et inférentiels déclarés.

Ce qui tient le plus fortement est :

```text
les écarts spectraux ;
les motifs d’oscillation ;
les relations entre fonctions du spectre ;
la cohérence conditionnelle du secteur à travers plusieurs voies.
```

Les bornes changent avec les données, modèles, priors, calibrations et méthodes.
Cette évolution ne signifie pas une variation physique des masses.

### 4.2 Apport de C2

C2 reproduit trois postérieurs distribués et conserve séparément :

```text
base_mnu ;
base_mnu059 ;
base_mnu_w_wa ;
absence bornée de base_mnu_binary_3 dans la distribution inspectée ;
quantiles empiriques ;
limites margestats ;
diagnostics de convergence ;
absence de profils exacts reconstruits.
```

Il fournit donc un cas positif où la stabilisation porte sur la reproduction
d’une chaîne d’inférence et sur la qualification de ses limites, non sur la
stabilisation physique de la masse des neutrinos.

### 4.3 Dépendance de chemin

```text
physique : non établie pour la masse par le cycle ;
inférentielle : forte, par observable, modèle de passage et hypothèses ;
statistique : support, frontière, prior, paramétrisation et convention de quantile ;
computationnelle : produit distribué, poids, lissage, interpolation et profils disponibles.
```

La dépendance au modèle d’expansion est démontrée par l’élargissement sous
`w_0w_aCDM`. Les effets propres du support, du prior et des likelihoods ne sont
pas encore complètement factorisés.

### 4.4 Test local proposé

Produire, à partir des matériaux déjà présents et sans nouvel ajustement global,
une table de sensibilité distinguant autant que possible :

```text
support autorisé ;
plancher imposé ;
prior ;
modèle d’expansion ;
jeu de données / likelihood ;
convention de résumé du posterior.
```

Le test doit indiquer pour chaque différence si elle est effectivement isolée,
seulement associée ou non identifiable avec les produits disponibles.
L’absence de `base_mnu_binary_3` et de profils exacts reste une limite positive,
non un motif de substitution.

### 4.5 Verdict

```text
clarification seulement : insuffisante ;
requalification de portée : oui ;
nouveau test local : oui, borné aux produits disponibles ;
dette de recherche : seulement si une discrimination non identifiable modifie
                      ensuite un verdict scientifique ;
concept non pertinent : non.
```

## 5. Cycles 4 et 8 — thermodynamique, métrologie et SI

### 5.1 Ce que les cycles établissent déjà

Les dossiers distinguent :

```text
grandeur physique ;
valeur numérique définissante ;
exactitude par composition ;
réalisation ;
résultat de mesure avec incertitude.
```

La fixation transforme la direction de l’inférence : une expérience qui
contribuait à ajuster une constante peut ensuite réaliser une unité, comparer
des méthodes ou déterminer une autre grandeur. L’incertitude est redistribuée,
non abolie.

### 5.2 Apport de la reformulation

Ici, le terme `régime de constance` est recevable seulement s’il ne fusionne pas :

```text
maintien d’une relation physique ;
exactitude numérique dans le SI ;
stabilité internationale des comparaisons ;
robustesse d’une réalisation concrète.
```

La stabilisation la plus nette est métrologique et normative : elle organise
l’accès et la comparabilité. Elle ne rend pas les grandeurs physiquement
invariantes par convention.

### 5.3 Dépendance de chemin

La généalogie empirique, l’acte institutionnel de fixation et les chaînes de
réalisation comptent pour le statut métrologique et la localisation des
incertitudes. Ils ne changent pas par eux-mêmes le rôle physique de `k_B`, `h`,
`e`, `c` ou `N_A`.

### 5.4 Test et dette

Le contraste avant / après fixation constitue déjà le test discriminant requis.
L’audit n’en ouvre pas un nouveau.

La cartographie quantitative des chaînes de réalisation et covariances reste une
dette scientifique antérieure et indépendante. Elle pourra préciser les formes
de stabilisation métrologique, mais elle n’est pas nécessaire pour valider la
distinction conceptuelle actuelle.

### 5.5 Verdict

```text
clarification seulement : oui, avec requalification de portée ;
nouveau test local créé par l’audit : non ;
dette existante confirmée : chaînes de réalisation et covariances ;
recherche externe immédiate : non ;
concept non pertinent : non, mais strictement localisé.
```

## 6. Cycle 6 — théories effectives à basse énergie

### 6.1 Résultat critique

Le cycle établit déjà :

```text
coefficient de Wilson individuel
≠ invariant physique autonome.
```

Les coefficients et éléments de matrice évoluent de manière complémentaire ;
les changements de base peuvent modifier les coefficients individuels sans
modifier l’amplitude physique ; la prédiction reste contrôlée dans une précision
et un domaine déclarés.

### 6.2 Ambiguïté du statut « constante effective »

Le terme peut recouvrir au moins deux situations :

```text
A. un paramètre physique de basse énergie, défini et extrait dans un domaine
   déterminé, comme G_F sous qualification précise ;
B. un coefficient de calcul dépendant de l’échelle, du schéma, de la base et de
   l’ordre, qui ne porte pas isolément l’invariance physique.
```

Les traiter comme un statut homogène de constance de l’objet serait incorrect.
Les exclure tous du vocabulaire de constance serait également trop rapide.

### 6.3 Ce qui se maintient

Selon le cas, le porteur du maintien est :

```text
la dominance d’un terme dans une expansion ;
la cohérence d’une amplitude ;
la compensation des dépendances auxiliaires ;
la hiérarchie des corrections ;
la prédictivité dans un domaine avec erreur contrôlée.
```

L’effectivité stabilise principalement une organisation du calcul et de la
prédiction. Elle ne stabilise pas nécessairement une valeur.

### 6.4 Test local obligatoire

Comparer explicitement trois objets :

```text
G_F dans la théorie de Fermi ;
un coefficient de Wilson générique C_i(mu) ;
Lambda_MSbar ou alpha_s(mu) dans le cas QCD.
```

Pour chacun, déterminer :

```text
porteur physique ;
dépendances à Q, mu, schéma, base et ordre ;
procédure d’extraction ;
quantité observable préservée ;
condition de rupture ;
raison exacte de conserver ou refuser le terme « constante effective ».
```

Ce test doit précéder toute modification de la décision canonique qui donne
`G_F` comme exemple-type de constance effective.

### 6.5 Verdict

```text
clarification seulement : refusée ;
requalification de portée : nécessaire ;
nouveau test local : obligatoire ;
recherche externe générale : non ;
modification canonique immédiate : interdite avant le test.
```

## 7. Cycle 10 — quasi-fixité électrofaible dynamique

### 7.1 Cas processuel fort

Ce cycle est le seul sentinelle où la stabilisation désigne explicitement un
processus physique temporel : une grandeur portée par un degré de liberté peut
évoluer, puis devenir quasi stationnaire relativement à un régime, une
tolérance et une durée.

Il distingue déjà :

```text
dépendance à l’échelle de renormalisation ;
dépendance thermique ;
variation dynamique dans l’espace-temps ;
variation apparente ou inférentielle.
```

### 7.2 Résultat acquis

Le toy model dissipatif établit une fenêtre phénoménologique non vide pour trois
prescriptions de dissipation. Il montre qu’un bilan énergétique ouvert peut
permettre :

```text
variation ancienne significative ;
transfert avant domination ;
quasi-fixité avant BBN ;
relique supprimée ;
entropie contrôlée.
```

Il n’établit ni mécanisme microscopique, ni thermalisation complète, ni histoire
réelle de notre univers.

### 7.3 Dépendance de chemin

La dépendance de chemin est ici physique dans le modèle : conditions initiales,
profil de dissipation et trajectoire déterminent l’état tardif. Mais la portée
de ce résultat demeure conditionnelle à la paramétrisation phénoménologique.

Il faut donc distinguer :

```text
existence d’une trajectoire viable dans le modèle ;
robustesse sur un bassin de conditions initiales ;
réalisation microscopique du taux ;
compatibilité empirique ;
histoire réelle.
```

### 7.4 Test et dette

L’audit ne crée pas une nouvelle dette. Il confirme celle déjà inscrite :
sélectionner un mécanisme microscopique minimal, dériver ou calculer le profil de
dissipation, tester sa robustesse et ses contraintes.

Cette recherche reste différée selon la feuille de route. Le concept de régime
de constance ne justifie pas de la faire remonter avant la reprise QCD.

### 7.5 Verdict

```text
clarification seulement : insuffisante ;
requalification de portée : oui ;
nouveau test local conceptuel : non, le toy model joue déjà ce rôle ;
dette physique existante : mécanisme microscopique et prise empirique ;
portée ontologique : non engagée.
```

## 8. Résultats transversaux de la passe sentinelle

### 8.1 La constance ne possède pas un porteur unique

La comparaison localise au moins cinq porteurs possibles :

```text
grandeur ou relation physique ;
observable ou amplitude ;
cohérence d’un secteur latent ;
valeur numérique définissante ;
quasi-fixité d’une trajectoire dynamique.
```

La formulation par maintien sous transformation est donc utile comme question,
mais ne définit pas une espèce unique.

### 8.2 La stabilisation est plurielle sans devenir équivoque illimitée

Les cas imposent de typer :

```text
stabilisation physique temporelle : cycle 10 ;
stabilité d’une prédiction et d’un domaine : cycles 1 et 6 ;
stabilisation inférentielle d’une borne ou compatibilité : cycle 3 et C2 ;
stabilisation métrologique de la comparabilité : cycles 4 et 8.
```

Ces formes peuvent être comparées par fonction et portée. Elles ne doivent pas
être fondues dans une catégorie ontologique commune.

### 8.3 La dépendance de chemin n’est pas une rubrique universelle positive

Elle doit pouvoir recevoir le verdict `non pertinente` ou `non établie`.

```text
cycle 10 : dépendance physique de trajectoire dans le modèle ;
cycle 3 : dépendance inférentielle et computationnelle ;
cycles 1 et 6 : dépendance des représentations et raccordements intermédiaires,
                avec invariance recherchée des observables ;
cycles 4 et 8 : dépendance historique et de réalisation pour la métrologie,
                sans production conventionnelle du rôle physique.
```

### 8.4 Les trois portées jouent correctement leur rôle de balise

```text
physique : établit le porteur, les transformations et le mécanisme local ;
épistémologique : qualifie les opérations, comparaisons, limites et droits
                  d’attribution ;
ontologique : reste non engagée dans les cinq tests sentinelles, sauf comme
              question différée possible.
```

Le niveau `non engagé` empêche que chaque dossier soit forcé à produire une
conclusion philosophique supplémentaire.

## 9. Tests retenus et recherches non ouvertes

### 9.1 Tests locaux retenus

```text
T1 — cycle 1 / QCD : transport et comparaison de plusieurs extractions de alpha_s ;
T2 — cycle 3 / C2 : table de sensibilité support / prior / modèle / données /
                    convention de posterior ;
T3 — cycle 6 : comparaison G_F / coefficient de Wilson / paramètre QCD pour
               arbitrer les usages de « constante effective ».
```

`T1` appartient à la reprise scientifique prioritaire du cycle 1. `T2` est borné
aux produits déjà disponibles. `T3` est un test conceptuel et physique interne
avant toute correction canonique.

### 9.2 Recherches non ouvertes par l’audit

```text
pas de revue générale sur les constantes ;
pas de nouvelle ontologie des régimes ;
pas de reprise générale du SI ;
pas de nouvel ajustement cosmologique global ;
pas de mécanisme microscopique du cycle 10 avant son rang prévu.
```

## 10. Verdict de deuxième passe

```text
V — changement de vitrine : confirmé mais insuffisant ;
D — ajustements distribués du cadrage : confirmé ;
T — nouveaux tests locaux : confirmé, au nombre de trois ;
R — recherche externe générale : refusée ;
N — aucune modification justifiée : refusée.
```

Le pronostic initial est confirmé : les résultats physiques restent intacts ; la
portée de plusieurs synthèses doit être rendue plus explicite ; trois tests
locaux suffisent à départager les ambiguïtés importantes ; aucune nouvelle
philosophie ne commande la réécriture des cas.

## 11. Passe suivante

Produire un registre des changements :

```text
à proposer après les tests ;
à refuser ;
à différer ;
à traiter comme simple mise à jour de statut ;
à ne jamais appliquer rétroactivement aux archives.
```

Le registre devra également décider si `Q3` reste un contrôle interne de portée
ou devient une question publique du projet.