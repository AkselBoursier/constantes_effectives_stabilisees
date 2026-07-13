# 06_PHILOSOPHIE

## Audit actif — non-trivialité de Q1

Branche : `agent/audit-non-trivialite-q1`

Le pilote Stern–Gerlach est clos comme calibration. Il n'établit aucune nouveauté en mécanique quantique ni aucune thèse philosophique originale. L'audit examine seulement s'il reste un protocole méthodologique non redondant pour contrôler le transport d'inférences entre plusieurs usages d'une catégorie.

Ordre de lecture :

1. [Entrée de l'audit](AUDIT_NON_TRIVIALITE_Q1_README.md)
2. [Recouvrements avec les cadres existants](Audit_non_trivialite_Q1_recouvrements_v0_1.md)
3. [Verdict](Audit_non_trivialite_Q1_verdict_v0_1.md)
4. [Protocole candidat](Protocole_candidat_transfert_inferentiel_v0_1.md)

Statut : Q2 retiré ; Q1 conservé comme calibration ; aucun nouveau cas quantique avant le verdict bibliographique sur le protocole candidat.

## Dossier calibratoire — Q1 Stern–Gerlach

Branche : `agent/pilote-q1-stern-gerlach`

1. [Entrée du pilote](PILOTE_Q1_STERN_GERLACH_README.md)
2. [Cadrage physique et niveaux](Pilote_Q1_Stern_Gerlach_cadrage_physique_v0_1.md)
3. [Matrice des fonctions](Pilote_Q1_Stern_Gerlach_matrice_fonctions_v0_1.md)
4. [Verdict provisoire antérieur à l'audit](Pilote_Q1_Stern_Gerlach_verdict_v0_1.md)
5. [Bibliographie raisonnée](Pilote_Q1_Stern_Gerlach_bibliographie_v0_1.md)

Les deux tests restent conservés comme exercices de calibration. Leur rang est désormais fixé par l'audit actif.

## Charte de la branche philosophique v0.1

### 1. Fonction

Cette branche accueille le pan philosophique de la recherche.

Elle fait deux choses :

```text
1. capturer des situations philosophiques explorees en conversation,
   pour que la matiere ne soit pas perdue ;
2. cartographier la philosophie implicite du corpus, qui n'etait
   documentee nulle part.
```

Elle tient son rang par trois disciplines :

```text
1. exploration plutot que redaction : les chapitres, articles et
   livres relevent des plans de livrables ; la branche fournit la
   matiere, les situations et les questions ;
2. situations plutot que catalogues : chaque nom cite est rattache a
   une situation, une position ou un conflit precis ;
3. proposition plutot que decision : la methode, la carte et les
   non-theses restent stables ; la promotion d'un element vers le
   corpus actif passe par le circuit de validation.
```

### 2. La notion de situation philosophique

Une situation philosophique est ici :

```text
une configuration datee ou des theories, des decouvertes, des modes
d'acces et des positions s'enchevetrent, et dont on cherche la logique
correlative : qui pouvait influencer qui, ce que la chronologie
interdit, ce que la convergence revele, ce que le conflit a coute.
```

Une situation peut etre paradigmatique ou locale : une querelle, une
reception manquee, une coincidence datee, un concept qui change de
main suffisent a en faire une.

Methode d'une fiche de situation :

```text
1. etablir la chronologie avant toute interpretation ;
2. distinguer influence causale, convergence sans causalite,
   et intrication differee ;
3. identifier les modes d'acces en conflit, s'il y en a ;
4. noter les raccords avec le corpus, sans les forcer ;
5. marquer ce qui est verifie et ce qui est cite de memoire ;
6. finir par les questions ouvertes que la situation laisse.
```

### 3. Types de documents

| Type | Prefixe | Fonction |
|---|---|---|
| Fiche de situation | `Situation_NN_` | Capture d'une situation philosophique exploree (oeuvres closes, chronologie) |
| Fiche de voisinage | `Voisinage_NN_` | Face-a-face avec une position contemporaine vivante (methode : Releve_paysage_contemporain_v0_1.md, section 3) |
| Carte | `Carte_` | Cartographie transversale (ex : philosophie implicite du corpus) |
| Releve | `Releve_` | Etat date d'un paysage, a refaire avant chaque soumission |
| Note de conversation | `Conversation_` | Trace d'un echange non encore structure en situation |

### 4. Rang documentaire

```text
rang : exploration philosophique active ;
la branche est en amont des degagements theoriques :
elle nourrit la matrice des degagements et les fiches d'horizon,
elle ne les remplace pas.
l'integration de cette branche a l'index raisonne du corpus est
une decision de statut soumise a validation.
le sas de raccordement actuel est :
05_CARTES_ET_SYNTHESES/Audit_integration_branche_philosophique_v0_1.md
```

### 5. Documents actuels

```text
06_PHILOSOPHIE/README.md
06_PHILOSOPHIE/Situation_01_processus_expansion_acces_v0_1.md
06_PHILOSOPHIE/Situation_02_Dirac_Eddington_grands_nombres_v0_1.md
06_PHILOSOPHIE/Situation_03_SI_2019_convention_vecue_v0_1.md
06_PHILOSOPHIE/Situation_04_Regime_gris_electrique_1990_2019_v0_1.md
06_PHILOSOPHIE/Situation_05_Duhem_Quine_architectures_v0_1.md
06_PHILOSOPHIE/Situation_06_Bachelard_rectification_CODATA_v0_1.md
06_PHILOSOPHIE/Situation_07_Mach_Planck_v0_1.md
06_PHILOSOPHIE/Carte_philosophie_implicite_corpus_v0_1.md
06_PHILOSOPHIE/Releve_paysage_contemporain_v0_1.md
06_PHILOSOPHIE/Releve_paysage_brisure_electrofaible_v0_1.md
```

Voisinages en priorite (methode et ordre : releve, sections 3 et 4) :

```text
V1 Massimi (realisme perspectiviste) - avant le papier A
V2 probleme de la coordination (Tal, Papale) - avant le papier B
V3 Chang - V4 Lange - V5 Daston/Rheinberger - V6 Wimsatt
```

### 6. Etat du premier cycle et suite

Le premier cycle des situations est clos avec la situation 07.

```text
Situations traitees : 01 (processus, expansion, acces), 02 (Dirac
contre Eddington), 03 (SI 2019, convention vecue), 04 (regime gris
electrique 1990-2019, intercalee), 05 (Duhem, Quine et les
architectures), 06 (Bachelard et la rectification), 07 (Mach contre
Planck, premiere querelle d'acces sur les constantes).
```

Ordre de la suite (decide en juillet 2026) :

```text
1. synthese du premier cycle : produite
   (Synthese_premier_cycle_situations_v0_1.md, degagements D1-D8) ;
2. voisinages V1 et V2 produits (Voisinage_01_Massimi_v0_1.md ;
   Voisinage_02_Coordination_v0_1.md) : les portes des papiers A et
   B sont ouvertes, sous reserves de lectures integrales listees
   dans chaque fiche (Massimi 2022 ; Tal 2018 ; volume Routledge
   2019 ; Papale 2024 ; Wolff 2020) ;
   la suite se decide au guichet : plan de livrable du papier A,
   ou deuxieme cycle (V1-V2 ont amorce son axe), ou voisinages
   V3-V6 restants ;
3. deuxieme cycle programme : conditions d'acces et constitution
   (Programme_deuxieme_cycle_v0_1.md : Bitbol, Husserl, reperage
   esprit, Nagarjuna differe) ;
4. troisieme cycle programme : existence disciplinaire de la
   question des constantes (Programme_troisieme_cycle_v0_1.md :
   mecanismes M1-M5, coupe disciplinaire) ;
5. cycles C4 (vie materielle et institutionnelle) et C5
   (exportabilite hors physique) instruits, et jonction
   d'historicite cosmique (C6, hors serie, avec fiche d'essai) :
   Programme_cycles_C4_C5_et_jonction_C6_v0_1.md ; la regle d'arret
   tient : cinq cycles philosophiques au plus, cette jonction vivrait
   cote physique ;
6. phase de test : close. Cinq tests, synthese produite
   (Synthese_phase_de_test_v0_1.md, insights I1-I8) :
   covariance (controle de fidelite, objection de tautologie
   retenue) ; C5-1 solaire, C5-2 stabilite chimique, C5-3 Michaelis,
   C5-4 pi (cas de durcissement) ; deux tests opposables par ancrage
   OpenTimestamps ; non-trivialite de la grammaire etablie (pi
   discrimine) ; cycle C5 clos, verdict d'exportabilite borne ;
7. points de decision en attente : typologie des erreurs de rang
   (D2), matrice temporelle v0.2 (D3), extension du chantier
   covariance en carte complete des blocs (D5), ligne "constitution"
   de la carte implicite (programme C2, section 4), genre "coupe
   disciplinaire" (programme C3, section 7), regle des deux
   registres constance / constante
   (01_CADRE_METHODOLOGIQUE/Note_terminologique_constance_v0_1.md),
   fiche d'essai de la jonction d'historicite cosmique ;
8. releve de paysage brisure electrofaible : produit comme
   preparation du seuil electrofaible et de la jonction
   d'historicite cosmique, sans ouverture du chantier et sans
   extraction de fil ; sas de cadrage correspondant :
   05_CARTES_ET_SYNTHESES/Note_cadrage_BEH_zone_jonction_v0_1.md.
```