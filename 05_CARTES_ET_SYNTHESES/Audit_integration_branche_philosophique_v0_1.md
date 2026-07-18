# Audit d'integration de la branche philosophique v0.1

## Tri de raccordement, statuts d'usage et micro-corrections avant commit sur travail

### 0. Statut documentaire

```text
statut : audit court d'integration ;
fonction : evaluer ce que la branche philosophique ajoute au corpus,
ce qui peut etre raccorde tout de suite, ce qui doit rester en reserve,
et quelles formulations doivent etre resserrees avant stabilisation.
branche de travail : travail.
effet : aucune fusion vers main ; aucun changement de rang du pan
physique ; seules des corrections locales de rang et de formulation
sont autorisees dans ce cycle.
```

Documents principalement controles :

```text
06_PHILOSOPHIE/README.md
06_PHILOSOPHIE/Audit_solidite_v0_1.md
06_PHILOSOPHIE/Carte_philosophie_implicite_corpus_v0_1.md
06_PHILOSOPHIE/Synthese_phase_de_test_v0_1.md
06_PHILOSOPHIE/Voisinage_02_Coordination_v0_1.md
05_CARTES_ET_SYNTHESES/Note_ouverture_question_genetique_v0_1.md
05_CARTES_ET_SYNTHESES/Mise_a_jour_intellectuelle_v0_1.md
05_CARTES_ET_SYNTHESES/Plan_livrable_papier_A_v0_1.md
05_CARTES_ET_SYNTHESES/Index_supplement_pan_philosophique_v0_1.md
```

### 1. Verdict general

```text
la branche philosophique n'est pas un simple habillage rhetorique du
pan physique. Elle apporte des instruments utilisables : statuts
probatoires, voisinages, tests d'exportabilite, distinction Q1/Q2,
et plans de livrables.

son integration brute serait toutefois prematuree. Elle doit passer
par un tri de rang : certains documents deviennent des references de
navigation et d'audit ; d'autres restent des reserves programmatiques
ou des horizons differes.
```

### 2. Apports a conserver comme actifs

| Apport | Document porteur | Statut d'integration |
|---|---|---|
| Distinction Q1 / Q2 | `Note_ouverture_question_genetique_v0_1.md` | Fort : Q1 qualification reste le seuil ; Q2 formation est ouverte, non substitutive |
| Audit probatoire P1-P6 | `Audit_solidite_v0_1.md` | Fort : a reprendre comme discipline interne avant toute redaction |
| Non-trivialite de la grammaire | `Synthese_phase_de_test_v0_1.md`, test `pi` | Fort, mais borne : prouve la discrimination, non la these physique |
| Exportabilite comparative | Tests C5 | Utilisable : montre une valeur comparative hors terrain natal |
| Voisinages V1/V2 | `Voisinage_01`, `Voisinage_02` | Utilisable avec lectures requises et corrections de rang |
| Plans A1/A2 | `Plan_livrable_A1`, `Plan_livrable_A2` | Utiles comme plans focalises, pas comme redaction ouverte |
| Regle des deux registres | `Note_terminologique_constance_v0_1.md` | A conserver : elle clarifie constante / constance |

### 3. Elements a garder en reserve

```text
1. L'horizon anthropique reste differe. La fiche est utile parce
   qu'elle pose des conditions d'entree ; elle ne doit pas devenir
   un argument central avant ces conditions.

2. H1 reste une hypothese de couplage, non un resultat. Son statut
   depend d'un test explicite avec contre-exemples.

3. Le programme de publication donne l'envergure, mais ne doit pas
   donner une impression de maturite redactionnelle superieure a la
   maturite probatoire.

4. Les chantiers CP-1 a CP-4, V-dim, C6 et la question
   Brout-Englert-Higgs sont des signaux de jonction. Ils deviennent
   interessants apres raccordement, pas dans ce commit.

5. La covariance CODATA garde rang de controle de fidelite. Elle ne
   doit pas etre citee comme preuve forte de la grammaire, puisque
   l'objection de quasi-tautologie a ete retenue.
```

### 4. Micro-corrections requises

Deux types de corrections sont necessaires avant stabilisation sur
`travail`.

```text
correction de rang :
remplacer les formules ou "le corpus explique" par des formules ou
"le corpus propose d'expliquer", tant que H1 n'est pas testee.

correction de modalite :
remplacer les formulations qui presentent une orientation
methodologique comme une orientation reelle deja etablie.
```

Corrections ciblees dans ce cycle :

| Fichier | Correction |
|---|---|
| `06_PHILOSOPHIE/Voisinage_02_Coordination_v0_1.md` | Formule finale de V2 : passage de l'explication au programme |
| `05_CARTES_ET_SYNTHESES/Mise_a_jour_intellectuelle_v0_1.md` | HI-1 : passage de "these controlee" a "engagement controle", sans promotion doctrinale |
| `05_CARTES_ET_SYNTHESES/Mise_a_jour_intellectuelle_v0_1.md` | HI-4 : teleologie lue comme orientation methodologique, non comme orientation reelle |
| `06_PHILOSOPHIE/Programme_deuxieme_cycle_v0_1.md` | Correction de format : suppression d'un octet NUL final qui faisait apparaitre le `.md` comme binaire |

### 5. Regle d'integration

```text
une piece philosophique peut entrer dans la navigation active si elle
fait au moins l'une des choses suivantes :

1. clarifier un statut deja actif du pan physique ;
2. expliciter une limite ou un risque probatoire ;
3. fournir un voisin bibliographique identifiable ;
4. tester une frontiere de la grammaire ;
5. organiser un livrable sans rouvrir prematurement le fond.

elle reste en reserve si elle ouvre une these nouvelle, un horizon
anthropique, une genealogie forte, une speculation cosmologique ou
un mecanisme physique non encore instruit.
```

### 6. Point de jonction Brout-Englert-Higgs

```text
constat : le pan physique et le pan philosophique convergent tous
deux vers le mecanisme de Brout-Englert-Higgs comme zone de jonction :
brisure, constitution de secteur, acquisition de masse, regime deja
brise, historicite cosmique.

statut dans le present audit : signal reconnu, non ouvert.
raison : l'ouverture BEH toucherait a la fois CP-1, CP-2, C6 et la
question de formation Q2. Elle doit venir apres le raccordement de
la branche philosophique et apres une note dediee de cadrage.
```

### 7. Formule de cloture

```text
La branche philosophique apporte des instruments, pas une doctrine
cle en main. Son bon usage est de durcir le corpus : assigner les
statuts, dater les tests, borner les formules, ouvrir Q2 sans
affaiblir Q1. Ce qui entre maintenant doit rendre le pan physique
plus prudent, non plus emphatique.
```
