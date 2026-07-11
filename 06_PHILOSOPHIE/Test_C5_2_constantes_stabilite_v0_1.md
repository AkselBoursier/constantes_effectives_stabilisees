# Test C5-2 : les constantes de stabilite des complexes v0.1

## Le cas instruit de zero

### 0. Statut documentaire

```text
statut : test empirique du cycle C5, deuxieme cas ;
caractere hors echantillon renforce : jamais utilise dans la
construction du corpus (une seule occurrence nominale dans les
resultats d'une recherche du releve, sans analyse), et le redacteur
declare ne posseder que la chimie generale du sujet - aucune
connaissance de la metrologie propre des constantes de stabilite
(bases de donnees, protocoles d'evaluation, conventions de milieu).
L'acquisition se fera integralement sur sources, avant toute
application de la grille. C'est la mitigation demandee par le
verdict de C5-1.
```

### 1. Criteres et falsificateurs

```text
criteres C1-C4 : identiques au test C5-1 (determination,
discrimination, valeur ajoutee, non-forcage).

deplacement du risque principal, declare d'avance : la chimie des
equilibres indexe ouvertement ses "constantes" sur le milieu
(temperature, force ionique, solvant). Le danger n'est donc plus
E2 (absorption sans discrimination) mais E3 : que la grille n'ait
rien a ajouter a ce que la discipline dit deja d'elle-meme.
Si la chimie possede un vocabulaire indigene complet du
conditionnement, la valeur ajoutee devra venir d'ailleurs -
ou etre declaree absente, et le test echouera sur C3.
```

### 2. Predictions verrouillees avant acquisition

```text
P-K1 : la grille qualifiera ces grandeurs en mode effectif
(validite par domaine de milieu), sans mode definissant ni
reconstruit dominants ; le regime fera partie du statut par
declaration explicite de la discipline - a la difference de la
physique fondamentale, ou le corpus a du l'etablir.

P-K2 : il existera une infrastructure de compilation critique
(bases de donnees evaluees, recommandations d'instances
internationales) jouant structurellement le role de CODATA -
avec au moins une station du vocabulaire du corpus applicable
(rectification par reevaluation critique, tension entre
determinations, convention d'etat de reference).

P-K3 : la chimie possede probablement deja un vocabulaire indigene
du conditionnement (constantes dites conditionnelles ou
apparentes) ; si c'est le cas, la grille devra le reconnaitre
comme equivalent local plutot que d'imposer le sien - et la valeur
ajoutee (C3) devra se chercher au niveau comparatif : la grammaire
comme langue commune entre les vocabulaires indigenes des
disciplines. Au plus un raffinement, aucune categorie inventee.
```

### 3. Acquisition (integralement sur sources, juillet 2026)

```text
1. l'indexation au milieu est declaree par la discipline : les
   constantes de stabilite dependent de la temperature et de la
   force ionique ; la theorie d'interaction specifique des ions
   (SIT) fournit la methode generale de correction entre forces
   ioniques jusqu'a environ 5 molal, avec logiciels produits sous
   projets IUPAC (Pettit et al. 2009).

2. l'infrastructure de compilation existe depuis 1957 : la base
   IUPAC des constantes de stabilite (SC-Database), issue d'une
   lignee editoriale qui inclut Schwarzenbach, Sillen, Bjerrum,
   Martell et Irving (Pettit 2001) ; cote americain, la base NIST
   SRD 46 "critically selected" (Smith & Martell 2004).

3. l'evaluation critique est institutionnalisee avec un vocabulaire
   de rangs explicite : donnees classees "Recommended",
   "Provisional", "Recommended-1", "accepted / rejected", avec
   seuils chiffres (ecart-type inferieur a 0,05 unite log pour R) ;
   erreurs typiques de mesure recensees par ligande (Anderegg et
   al. 2005 ; Arnaud-Neu et al. 2003 ; Beck 1977).

4. dynamique de saturation documentee : la collecte de nouvelles
   constantes perd de l'importance, les mesures recentes sont
   souvent moins rigoureuses (mesurees pour confirmer un mecanisme,
   non pour l'usage general) ; le besoin bascule vers l'evaluation
   critique de l'existant et la propagation des erreurs dans les
   courbes de speciation (Pettit et al. 2009).

5. acces multiples : titrations pH-metriques (Bjerrum-Calvin,
   Irving-Rossotti), electrophorese sur papier, et desormais
   estimation ab initio (Purgel et al. 2023, precision 0,5-1 unite
   log dans les cas favorables).
```

### 4. Application de la grille

| Rang | Reponse pour le cas |
|---|---|
| Forme (rang 0) | Quotient d'equilibre : rapport d'etat indexe (milieu, etat standard, echelle concentration/activite) |
| Regime | Declare par la discipline : temperature, force ionique, solvant ; domaine de validite des corrections SIT explicite (jusqu'a 5 molal) |
| Fonction situee | Prediction de speciation ; applications biomedicales et environnementales ; la constante est un instrument de calcul d'etats |
| Acces | Pluriel (titrations, electrophorese, ab initio) ; rigueur declinante documentee ; evaluation critique par rangs (R, P, R1, rejete) |
| Trajectoire | Compilation (1957-) ; saturation de collecte et bascule vers l'evaluation (station nouvelle, documentee par la discipline elle-meme) ; rectification par reevaluation critique ; transposition de milieu par SIT |
| Architecture | Aucune au sens du corpus ; dependances de reseau simples : etats standards, echelles d'activite. La grille n'invente rien |
| Limite conservee | Constantes de concentration contre constantes d'activite ; erreurs non propagees historiquement aux courbes de speciation ; qualite heterogene du fonds |

Qualification produite :

```text
constances effectives de milieu, a indexation declaree : le mode
effectif s'applique sans forcage, et la discipline enonce d'elle-
meme ce que le corpus a du etablir pour la physique fondamentale -
le regime fait partie du statut.

fait remarquable, intelligible par le critere de latitude (note de
correction modale) : ces constantes ne sont jamais absorbees par
convention - leur valeur garde sa latitude par indexation au
milieu. La discipline conventionne alors l'inverse : le cadre
(etats standards, conditions de reference, 25 C, force ionique de
reference), non la valeur. La chimie fixe le milieu la ou la
metrologie fixe le contenu - les deux gestes sont les deux issues
du meme critere.
```

### 5. Verdict

```text
C1 determination : tenu.
C2 discrimination : tenu - mode effectif de milieu, non absorbable,
   distinct du cas SI et du cas solaire ; P-K1 confirmee.
C3 valeur ajoutee : tenu, au niveau comparatif que P-K3 anticipait,
   avec trois apports :
   (i) la correction SIT entre forces ioniques et le flot de
   renormalisation entre echelles sont structurellement le meme
   geste - le transport regle d'une constante entre regimes par la
   theorie - qu'aucune des deux litteratures ne nomme ; station
   candidate pour la matrice temporelle v0.2 : "transport entre
   regimes" (generalisant flot RG et SIT) ;
   (ii) la conventionnalisation du cadre au lieu de la valeur :
   l'inverse exact du SI, predit intelligible par le critere de
   latitude - le critere gagne un second cas d'application ;
   (iii) la station "saturation de collecte, bascule vers
   l'evaluation" : documentee par la discipline, absente du
   vocabulaire du corpus, candidate pour la matrice temporelle.
   P-K2 confirmee (infrastructure critique avec rangs explicites,
   plus riche que CODATA sur un point : elle grade au lieu de
   moyenner).
C4 non-forcage : tenu - un raffinement declare (le transport entre
   regimes generalise deux mecanismes indigenes, il n'invente pas
   de classe) ; P-K3 confirmee (vocabulaire indigene reconnu, la
   grammaire opere comme langue commune).

conditions d'echec : aucune declenchee ; E3, le falsificateur
redoute, est ecarte par les trois apports comparatifs.

portee : deuxieme cas hors echantillon favorable, cette fois avec
acquisition integralement sur sources. Le motif qui se dessine sur
deux cas : la valeur de la grammaire hors terrain natal est
comparative - elle nomme des structures que les vocabulaires
indigenes portent sans les relier (rectification, absorption,
grading, transport entre regimes). Enonce a tenir prudemment
jusqu'au troisieme cas ou a la cloture du cycle.

note d'horodatage : predictions et resultats commites ensemble ;
anteriorite etablie par l'ordre de conversation seulement, valeur
probante reduite d'autant (protocole d'horodatage v0.1).
```

### 6. Sources du test

```text
Pettit, L. D. (2001). The IUPAC stability constants database.
  Chemistry International. (verifiee)
Pettit, L. D., et al. (2009). A more realistic approach to
  speciation using the IUPAC Stability Constants Database. Pure and
  Applied Chemistry. (verifiee ; SIT, saturation, erreurs)
Anderegg, G., et al. (2005). Critical evaluation of stability
  constants of metal complexes of complexones (IUPAC Technical
  Report). Pure and Applied Chemistry. (verifiee ; R/P)
Arnaud-Neu, F., et al. (2003). Critical evaluation... crown ethers
  (IUPAC Technical Report). Pure and Applied Chemistry. (verifiee ;
  seuils chiffres R/P/R1, accepted/rejected)
Smith, R. M., & Martell, A. E. (2004). NIST Critically Selected
  Stability Constants of Metal Complexes Database (SRD 46).
  (verifiee)
Beck, M. (1977). Critical evaluation of equilibrium constants in
  solution. Pure and Applied Chemistry. (verifiee)
Purgel, M., et al. (2023). First principle determination of
  stability constants... Int. J. Quantum Chemistry. (verifiee)
```
