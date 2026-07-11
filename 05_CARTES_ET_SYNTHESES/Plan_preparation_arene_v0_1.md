# Plan de preparation de l'arene v0.1

## Travaux prealables aux conditions d'entree de la fiche d'horizon anthropique

### 0. Statut documentaire

```text
statut : plan de travail actif ;
il organise la preparation du chantier defini par la section 6 de la
fiche d'horizon anthropique ;
il n'autorise pas l'entree dans l'arene : il la prepare ;
les decisions conceptuelles rencontrees en cours de route restent
soumises a validation explicite (workflow GitHub v0.1).
```

Documents lies :

```text
05_CARTES_ET_SYNTHESES/Fiche_horizon_anthropique_v0_1.md
05_CARTES_ET_SYNTHESES/Note_ouverture_question_genetique_v0_1.md
05_CARTES_ET_SYNTHESES/Matrice_degagements_theoriques_v0_1.md
01_CADRE_METHODOLOGIQUE/Matrice_temporelle_v0_1.md
```

### 1. Principe du plan

On ne se lance pas dans un chantier comme celui-ci a l'aveugle.

Le plan distingue :

```text
travaux documentaires : extraction et organisation de materiau deja
present dans le corpus ; delegables apres accord de principe ;

travaux conceptuels : definitions nouvelles, tests d'hypotheses ;
chaque sortie est un point de decision soumis a validation ;

travaux bibliographiques : lectures primaires et verifications ;
delegables, mais leurs syntheses sont relues avant integration.
```

Chaque axe indique : livrable, type, dependances, et la condition
d'entree (section 6 de la fiche d'horizon) qu'il prepare.

### 2. Axe 1 : note de lecture Carter et corpus anthropique primaire

```text
livrable : Note_lecture_Carter_1974_v0_1.md
type : bibliographique puis conceptuel
condition preparee : condition 5 (passe bibliographique dediee)
dependances : aucune ; le texte primaire est lu (PDF local disponible)
```

Contenu attendu :

```text
1. les trois classes de prediction (traditionnelle, WAP, SAP) avec les
   exemples exacts de Carter (masse stellaire, argument de Dicke,
   restriction sur kappa) ;
2. la distinction stricte WAP d'histoire unique / SAP promu par
   ensemble, avec citations ;
3. la question d'Icke et la reponse de Carter (superselection),
   comme point d'ancrage du corpus ;
4. le voeu de Carter (constantes derivees d'une structure plus
   profonde) et sa relation a la carte du conditionne ;
5. l'objection de quasi-tautologie : etat de la discussion, positions
   principales, et la maniere dont la formulation candidate du
   deplacement 3 doit l'affronter.
```

Extension de l'axe (apres la note Carter) :

```text
lectures primaires restantes, par ordre de priorite :
1. Dicke (1961) : l'argument d'epoque original ;
2. Hossenfelder (2018 ; 2021) : critique de la naturalite et du
   reglage fin comme "screams for explanation" ; a traiter comme
   allie sur la critique probabiliste, en distinguant soigneusement
   sa critique (la mesure de probabilite n'est pas justifiee) de la
   critique genetique du cadre (l'espace de variation lui-meme est
   mal defini pour les grandeurs conditionnees) ;
3. McGrew et Vestrup (2001) : non-normalisabilite ;
4. Barnes (2012) contre Stenger (2011) : la co-variation ;
5. Bostrom (2002) : effets de selection d'observation.
```

### 3. Axe 2 : carte du conditionne

```text
livrable : Carte_du_conditionne_v0_1.md
type : documentaire (extraction) puis conceptuel (frontiere)
condition preparee : conditions 1 et 4 ; deplacement 1 de la fiche
dependances : fiches et cycles existants ; aucun nouveau cas requis
```

Contenu attendu :

```text
1. inventaire des grandeurs traitees par le corpus, classees en :
   conditionnees (avec la chaine de conditionnement explicite :
   m_f <- y_f, v <- brisure electrofaible ; G_F <- M_W ; etc.),
   entrees non conditionnees (textures de Yukawa, Lambda, conditions
   initiales, parametres libres residuels),
   cas frontieres (a documenter sans trancher) ;
2. pour chaque grandeur conditionnee : le test de retrait deja
   disponible dans les fiches, reformule comme condition ;
3. la frontiere conditionne / entree comme resultat provisoire :
   c'est la carte qui localise le residu anthropique.
```

Regle de prudence :

```text
la carte ne cree aucune categorie nouvelle ; elle reorganise ce que
les fiches disent deja. Si un cas exige une decision conceptuelle
(exemple : statut de M_Pl), il est marque "frontiere" et remonte en
point de decision.
```

### 4. Axe 3 : portee de retroaction

```text
livrable : Note_portee_retroaction_v0_1.md
type : conceptuel (point de decision a la sortie)
condition preparee : condition 3
dependances : axe 2 (la carte du conditionne fournit les chaines)
```

Contenu attendu :

```text
1. definition operationnelle : etendre le test de retrait dans le
   temps ; que perd-on en aval si cette stabilisation n'avait pas eu
   lieu, ou avait eu lieu autrement ?
2. test sur le couple porteur : confinement (stabilisation massive
   sans reconfiguration des parametres des autres secteurs) contre
   brisure electrofaible (reconfiguration du milieu d'effectuation
   de tout ce qui suit) ;
3. confrontation au generative entrenchment de Wimsatt : ce que la
   transposition conserve, ce qu'elle doit abandonner (le concept
   est developpemental, pas physique) ;
4. echelle provisoire de portee : locale / sectorielle /
   reconfigurante, avec test de retrait diachronique pour chaque cas.
```

Garde-fou :

```text
la portee de retroaction ne devient ni une famille fonctionnelle ni
une architecture : c'est un champ de la trajectoire (rang 5).
```

### 5. Axe 4 : formalisation de la necessite conditionnelle de regime

```text
livrable : Note_modalite_conditionnelle_v0_1.md
type : conceptuel (point de decision a la sortie)
condition preparee : condition 4
dependances : axes 2 et 3
```

Contenu attendu :

```text
1. definition : etant donne un milieu d'effectuation et des
   stabilisations anterieures, une grandeur conditionnee ne dispose
   plus de variation libre ; sa constance est necessaire
   conditionnellement, contingente absolument ;
2. distinction stricte d'avec : necessite metaphysique, necessite
   nomologique, contingence brute ;
3. traitement du risque de "genetic fallacy" : la genese d'un statut
   ne fonde ni n'invalide sa legitimite (la qualification T0 reste
   le seuil de droit) ;
4. consequence pour le contrefactuel du reglage fin : sur quel
   domaine "aurait pu etre autre" garde un sens.
```

### 6. Axe 5 : test de H1 sur les fiches existantes

```text
livrable : Test_H1_couplage_formation_v0_1.md
type : conceptuel (test d'hypothese)
condition preparee : condition 1
dependances : note d'ouverture genetique (tables 4.1 et 4.2) ; axe 2
```

Contenu attendu :

```text
1. application des deux tables (formation physique / formation
   epistemique) a chaque fiche sensible :
   m_f, k_B / R, alpha_s / Lambda_QCD, G_F / M_W, H_0,
   sigma_8 / S_8, A_s / n_s, CKM / PMNS, borne neutrino, M_Pl ;
2. recherche active de contre-exemples au couplage ;
3. sortie en trois cas : H1 resiste (resultat central), H1 echoue
   (resultat aussi : independance des deux faces), H1 se raffine
   (couplage partiel, a specifier).
```

### 7. Ordre de marche et dependances

```text
etape 1 (delegable apres accord) : axe 2, carte du conditionne ;
  extraction pure, aucun risque conceptuel.
etape 2 (delegable) : axe 1, note de lecture Carter ;
  le materiau est deja largement extrait dans la fiche d'horizon.
etape 3 : axe 5, test de H1 ; premiere sortie conceptuelle,
  point de decision a la fin.
etape 4 : axe 3, portee de retroaction ; s'appuie sur la carte.
etape 5 : axe 4, modalite conditionnelle ; s'appuie sur tout.
etape 6 : lectures primaires restantes de l'axe 1 (Dicke,
  Hossenfelder, McGrew-Vestrup, Barnes, Stenger, Bostrom),
  en parallele des etapes 3 a 5.
```

Relation aux papiers (note d'ouverture genetique, section 8) :

```text
le papier A (qualification) ne depend d'aucun de ces axes ;
il peut etre planifie des maintenant.
le papier B (formation) depend des axes 2, 3 et 5.
l'entree dans l'arene depend de tout, papiers A et B compris
(conditions 1 a 5 de la fiche d'horizon).
```

### 8. Discipline du plan

```text
1. la redaction d'un texte "reglage fin" commence apres la levee des
   cinq conditions d'entree ;
2. H1, la portee de retroaction et la modalite conditionnelle
   deviennent des acquis par validation explicite ;
3. la methode v1.3 et la carte v1.3 restent stables pendant la
   preparation ; tout besoin de modification remonte comme point de
   decision.
```

### 9. Formule de cloture

```text
Preparer l'arene, c'est refuser d'y entrer desarme :
la carte localise le residu, les lectures fixent les adversaires
reels, les definitions donnent les armes, et les conditions d'entree
decident de l'heure.
```
