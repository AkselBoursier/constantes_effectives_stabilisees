# Test C5-3 : la constante de Michaelis - VERDICT

## Fichier de resultats, posterieur a l'ancrage des predictions

### 0. Statut documentaire

```text
statut : resultats et verdict du test C5-3 ;
predictions verrouillees et ancrees (SHA-256
012da069d479151b2e74a8cb965a9690b699d477e6e678637b217246234f07b7,
OpenTimestamps, reçu .ots au depot) dans le fichier
Test_C5_3_constante_Michaelis_predictions.md, avant toute
acquisition ; le present fichier est posterieur a l'ancrage.
Premier test du corpus a anteriorite opposable (protocole
d'horodatage v0.1).
acquisition : integralement sur sources, juillet 2026.
```

### 1. Acquisition (sur sources)

```text
1. K_M n'est pas une constante de dissociation : c'est une constante
   d'etat stationnaire. Le "paradoxe de Michaelis-Menten" : K_M est
   la concentration de substrat donnant la demi-vitesse maximale,
   generalement superieure a la constante de dissociation K_d de
   l'affinite ; l'assimiler a l'affinite demande prudence
   (Canela et al. 2019 a et b ; Dalziel 1962, Nature).

2. K_M est relative a un modele : selon le schema (equilibre rapide
   de Michaelis-Menten, ou etat quasi stationnaire de Briggs-
   Haldane), la meme forme d'equation recoit une interpretation
   differente de K_M (Dalziel 1962 ; Srinivasan 2021, FEBS J,
   guide de reference).

3. domaine de validite explicite : l'equation ne vaut que sous
   l'hypothese "reactant stationary" (distincte de l'etat
   stationnaire) ; zones sQSSA / rQSSA a validite limitee, cartes
   de validite explicites (Schnell 2014, FEBS J ; Udema 2023).

4. vocabulaire indigene du conditionnement : "K_M apparent" contre
   K_M vrai, "constante de Michaelis apparente comme constante de
   dissociation apparente", dependance au pH documentee
   (Cohlberg 1979 ; Cornish-Bowden 1976).

5. requalification par raffinement du modele : critiques du
   k_cat/K_M comme mesure de specificite, correction des constantes
   de Michaelis pour reactions reversibles, recherche des
   "constantes de temps perdues" au-dela de Michaelis-Menten
   (Barnsley 2022 ; Pinto et al. 2016).

6. infrastructure : bases de donnees enzymologiques (type BRENDA,
   non verifiee ici en detail) ; standardisation des conditions
   d'essai. A confirmer si le cas va en manuscrit.
```

### 2. Application de la grille et confrontation aux predictions

| Rang | Reponse | Prediction |
|---|---|---|
| Forme (rang 0) | Quotient d'etat stationnaire, non une dissociation ; relatif au schema cinetique | P-M1 (quotient d'etat) confirmee |
| Regime | Domaine de validite declare (reactant stationary ; sQSSA/rQSSA) ; T, pH | P-M1 (mode effectif, dependance conditions) confirmee |
| Fonction situee | Parametre de vitesse, instrument de prediction cinetique | - |
| Acces | Determination par vitesses initiales ; courbes de progression ; pre-etat-stationnaire | - |
| Trajectoire | Michaelis-Menten (1913) -> correction Briggs-Haldane -> critiques du sens (K_M vs K_d) -> post-Michaelis-Menten | P-M3 (requalification par raffinement) confirmee |
| Architecture | Aucune au sens du corpus ; dependances simples (k_cat, V_max, [E], k1) | P-M4 confirmee |
| Limite conservee | K_M n'est pas l'affinite ; validite bornee des hypotheses ; apparent vs vrai | - |

```text
P-M2 (pas d'absorption conventionnelle ; latitude ouverte par
conditions et modele) : confirmee - aucune valeur de K_M n'est
votee exacte ; le critere de latitude tient (troisieme cas
concordant apres SI et stabilite chimique).

P-M3 (vocabulaire indigene du conditionnement, reconnu comme
equivalent local) : confirmee - "K_M apparent" est exactement le
"constantes apparentes" attendu ; la grille le reconnait, ne
l'impose pas.
```

### 3. La prediction risquee P-M5 : confirmee

```text
P-M5 predisait : K_M releve du meme mode effectif que G_F -
coefficient effectif valide dans un domaine, sous un modele qui
masque une structure plus fine.

les sources le confirment litteralement :
K_M est un parametre effectif d'etat stationnaire qui condense les
constantes de vitesse elementaires (k1, k-1, k2) sans les livrer ;
il n'est pas la grandeur "fondamentale" du systeme (K_d, ou k1, que
la biologie des systemes juge plus decisif : Canela 2019). C'est la
structure exacte de G_F : un coefficient effectif qui condense, a
basse energie, l'echange du boson W, sans livrer la theorie
electrofaible complete.

le rapprochement fait circuler une question dans chaque sens
(critere de la "regle des motifs" discutee, non consignee) :
- vers la biochimie : existe-t-il un analogue de l'echelle de
  validite M_W, une echelle de conditions au-dela de laquelle le
  schema effectif cesse (le franchissement sQSSA -> rQSSA en est un
  candidat) ?
- vers la physique : la distinction K_M apparent / K_d vrai est-elle
  un analogue de la distinction coefficient effectif / parametre de
  la completion ?
Le rapprochement travaille ; il n'est pas decoratif. Il se publie
avec sa desanalogie : G_F a une completion UV connue et unique
(electrofaible), K_M a une "completion" qui est un jeu de constantes
de vitesse mesurables, non une theorie plus fondamentale.
```

### 4. Verdict

```text
C1 determination : tenu.
C2 discrimination : tenu - mode effectif relatif a un modele,
   distinct des cas SI (definissant), solaire (nominal) et stabilite
   chimique (effectif de milieu). K_M ajoute un sous-cas : effectif
   relatif a un modele, ou le conditionnement est autant theorique
   (le schema cinetique) que materiel (T, pH).
C3 valeur ajoutee : tenu - deux apports :
   (i) P-M5, l'identification structurelle K_M / G_F, qui fait
   circuler une question dans chaque discipline ;
   (ii) le raffinement du "conditionnement" : la chimie de milieu
   (C5-2) conditionnait par le milieu materiel ; K_M conditionne
   aussi par le modele (le schema cinetique choisi). Le corpus
   distingue deja regime physique et regime d'acces ; K_M montre un
   troisieme conditionnement, par le modele - a rapprocher du
   couplage modele-acces (T8) deja present en cosmologie. La
   grammaire relie un cas biologique a un cas cosmologique.
C4 non-forcage : tenu - aucune categorie inventee ; le sous-cas
   "effectif relatif a un modele" est un raffinement du mode
   effectif, pas une classe nouvelle.

conditions d'echec : aucune declenchee. E3, le falsificateur
principal, ecarte par P-M5 et par le troisieme conditionnement.

les cinq predictions verrouillees et ancrees sont confirmees.

portee : troisieme cas hors echantillon favorable, et le premier a
anteriorite opposable (ancrage OpenTimestamps anterieur a
l'acquisition). Le cycle C5 dispose maintenant de trois cas
(solaire, stabilite chimique, Michaelis) sur trois terrains
distincts (astrophysique nominale, chimie de milieu, enzymologie
model-relative), tous favorables, dont un opposable.
```

### 5. Consequence pour le cycle C5

```text
seuil de cloture atteignable : trois cas concordants suffisent a
un verdict d'exportabilite prudent. Deux options au guichet :
1. clore C5 par une synthese (verdict d'exportabilite : la grammaire
   s'exporte, sa valeur hors terrain natal est comparative et
   discriminante, ses limites sont les desanalogies conservees) ;
2. un quatrieme cas de durcissement (un cas ou la grille pourrait
   echouer : une grandeur d'une science humaine, ou une "constante"
   mathematique - pi, e - ou le mode effectif n'a aucune prise).

recommandation : option 2 avant cloture - une "constante"
mathematique testerait la frontiere externe de la grammaire (une
constante sans regime, sans acces empirique, sans milieu), la ou
un echec serait instructif et attendu. Ce serait le vrai test de
non-trivialite du cycle.
```

### 6. Sources du test

```text
Canela, E. I., et al. (2019). The meaning of the Michaelis-Menten
  constant: Km describes a steady-state. bioRxiv. (verifiee)
Canela, E. I., et al. (2019). The Michaelis-Menten paradox: Km is
  not an equilibrium constant but a steady-state constant. bioRxiv.
  (verifiee)
Dalziel, K. (1962). Physical significance of Michaelis constants.
  Nature, 196. (verifiee)
Srinivasan, B. (2021). A guide to the Michaelis-Menten equation:
  steady state and beyond. The FEBS Journal, 289. (verifiee)
Schnell, S. (2014). Validity of the Michaelis-Menten equation.
  The FEBS Journal, 281. (verifiee)
Cohlberg, J. A. (1979). Km as an apparent dissociation constant.
  Journal of Chemical Education, 56. (verifiee)
Cornish-Bowden, A. (1976). Interpretation of pH-independence of Km.
  The Biochemical Journal, 153. (verifiee)
Pinto, M. F., et al. (2016). In search of lost time constants and
  of non-Michaelis-Menten parameters. Perspectives on Science, 4.
  (verifiee)
Barnsley, E. A. (2022). Henri-Michaelis-Menten kinetics of
  reversible enzymic reactions. Science Progress, 105. (verifiee)
```
