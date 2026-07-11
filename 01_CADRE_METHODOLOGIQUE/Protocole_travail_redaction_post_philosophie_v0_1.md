# Protocole de travail et de redaction post-branche philosophique v0.1

## Regles actives pour les prochains documents

### 0. Statut documentaire

```text
statut : protocole operatoire interne ;
fonction : synchroniser les regles methodologiques issues de la
branche philosophique avec la poursuite du corpus ;
effet : fixe les protocoles que tout nouveau document doit suivre,
sans rouvrir la methode v1.3 ni modifier le pan physique stabilise.
```

Documents integres :

```text
01_CADRE_METHODOLOGIQUE/Reecriture_positive_vocabulaire_v0_3.md
01_CADRE_METHODOLOGIQUE/Test_reecriture_structurelle_v0_1.md
01_CADRE_METHODOLOGIQUE/Note_terminologique_constance_v0_1.md
01_CADRE_METHODOLOGIQUE/Note_correction_modale_convention_v0_1.md
01_CADRE_METHODOLOGIQUE/Workflow_GitHub_v0_2.md
01_CADRE_METHODOLOGIQUE/Protocole_synchronisation_v0_1.md
01_CADRE_METHODOLOGIQUE/Protocole_horodatage_tests_v0_1.md
06_PHILOSOPHIE/Audit_solidite_v0_1.md
06_PHILOSOPHIE/Synthese_phase_de_test_v0_1.md
05_CARTES_ET_SYNTHESES/Audit_integration_branche_philosophique_v0_1.md
05_CARTES_ET_SYNTHESES/Programme_publication_v0_1.md
```

### 1. Regle active de redaction positive

```text
la v0.3 de la reecriture positive est la version active.
Elle s'applique a tout nouveau document des sa premiere version.
```

Regles d'usage :

```text
1. dire d'abord ce que le cas est, ce qu'il stabilise, quel rang il
   tient et par quel circuit il peut changer de rang ;
2. formuler les titres et sections comme disciplines, conditions
   d'ouverture, statuts ou fonctions, plutot que comme interdits ;
3. conserver les refus, limites, non-theses et tests rates dans leurs
   conteneurs sanctionnes ;
4. proteger la force des refus : la reecriture positive ne transforme
   pas "non confirme" en "reste a confirmer" ;
5. appliquer la charite de rang aux positions discutees : decrire
   d'abord ce qu'elles ont stabilise, puis donner le verdict.
```

Formule courte :

```text
le cadre devient positif ; les refus gardent leur force.
```

### 2. Regle des deux registres

```text
constante : la grandeur, son usage physique, sa valeur, sa mesure ;
constance : le statut de la grandeur, ses modes, sa trajectoire,
ses conditions de maintien ou de defaisance.
```

Usage dans les prochains documents :

```text
1. employer "constance" pour Q1, T0, T1, les modes, trajectoires,
   conditions et limites ;
2. employer "constante" pour les objets physiques ou metrologiques
   nommes ;
3. conserver "constantes effectives stabilisees" comme nom du cadre ;
4. utiliser la formule d'interface : la constance des constantes.
```

Statut :

```text
regle en epreuve d'usage, deja assez stable pour guider la redaction ;
elle reste ajustable si elle produit des lourdeurs ou ambiguites.
```

### 3. Clause modale de la convention

Toute mention du mode definissant, de l'absorption conventionnelle ou
du SI 2019 suit la correction modale :

```text
necessite du contenu a l'intervalle pres ;
liberte de la forme ;
insignifiance de la latitude residuelle.
```

Critere associe :

```text
on ne conventionne que ce qui n'a plus de latitude.
```

Usage :

```text
1. le SI se traite comme cas de latitude epuisee ;
2. H_0 et les tensions persistantes se traitent comme latitude
   vivante, non absorbable ;
3. toute comparaison convention / tension passe par le critere de
   latitude, pas par une opposition arbitraire / reel.
```

### 4. Statut probatoire des formules

Toute formule forte porte le statut de sa piece la plus faible.

Echelle active :

```text
P1 : verifie sur primaire, plein usage ;
P2 : verifie sur secondaire fiable, usage avec source ;
P3 : recherche documentaire, usage prudent ;
P4 : memoire informee, usage interne seulement ;
P5 : construction propre, motif ou programme ;
P6 : hypothese non testee.
```

Regle pratique :

```text
1. aucune formule de manuscrit ne s'appuie sans signalement sur P4,
   P5 ou P6 ;
2. une formule belle mais P5/P6 s'ecrit comme programme ;
3. H1 reste hypothese tant que son test explicite n'est pas execute ;
4. la covariance CODATA reste controle de fidelite, non preuve forte ;
5. C5 etablit une exportabilite comparative bornee, non la these
   physique centrale.
```

### 5. Regle de positionnement

```text
Q1 qualification reste le seuil :
dans quelle mesure une grandeur peut-elle etre qualifiee de constante ?

Q2 formation est ouverte :
dans quelles conditions le statut de constance se forme-t-il,
se maintient-il et se defait-il ?
```

Ordre d'usage :

```text
1. Q2 presuppose Q1 ;
2. les plans A1/A2 relevent de Q1 ;
3. H1 et la formation physique / epistemique relevent de Q2 ;
4. l'horizon anthropique, C6 et BEH restent des zones de jonction
   a cadrer separement ;
5. aucune reserve programmatique ne devient argument central sans
   condition d'entree explicite.
```

### 6. Protocole Git et synchronisation

Regle de branches :

```text
main : etat valide du corpus ;
branches thematiques : chantiers soumis a validation ;
travail : branche d'integration quotidienne.
```

Regle de commit :

```text
1. message : docs: <imperatif anglais, une ligne> ;
2. un changement logique par commit ;
3. push apres verification ;
4. les documents partages se modifient par couche additive quand
   c'est possible.
```

Regle d'arborescence :

```text
1. un index supplementaire complete un index stable ;
2. un document recent corrige le rang d'un ancien, il ne l'efface pas ;
3. aucun deplacement ou renommage sans inventaire des references.
```

### 7. Protocole des tests a predictions

Pour tout test avec predictions verrouillees :

```text
1. rediger les predictions seules, sans acquisition ;
2. commit des predictions ;
3. attendre l'ancrage externe confirme par l'auteur
   (OpenTimestamps ou OSF selon le statut du test) ;
4. seulement ensuite acquerir les donnees et produire le verdict ;
5. committer les resultats separement.
```

Regle :

```text
aucune acquisition avant confirmation de l'ancrage.
```

### 8. Limite des livrables

```text
les plans peuvent etre nombreux ;
les ebauches redigees restent limitees a trois en cours.
```

Usage :

```text
1. un plan n'est pas une redaction ;
2. une redaction engage la coherence et entre dans la limite ;
3. le programme de publication donne l'envergure, pas un calendrier.
```

### 9. Check-list avant tout nouveau document

```text
1. Quel rang le document tient-il ?
2. Quels documents integre-t-il ?
3. Quel document prolonge-t-il ou corrige-t-il ?
4. Q1, Q2, reserve ou jonction ?
5. Quelle regle de reecriture positive s'applique ?
6. Les refus eventuels gardent-ils leur force exacte ?
7. Les formules fortes ont-elles un statut probatoire explicite ?
8. "constante" ou "constance" est-il employe au bon registre ?
9. Le SI ou la convention portent-ils la clause modale ?
10. Le document exige-t-il un protocole d'horodatage ?
11. Le raccord README / index est-il additif ?
12. Le commit correspond-il a un seul changement logique ?
```

### 10. Formule de cloture

```text
La branche philosophique n'ajoute pas seulement du contenu ; elle
change le regime de travail. Les prochains documents doivent donc
ecrire positivement, assigner leurs rangs, dater leurs tests,
separer constante et constance, borner les formules fortes, et
laisser les zones de jonction s'ouvrir par cadrage dedie.
```
