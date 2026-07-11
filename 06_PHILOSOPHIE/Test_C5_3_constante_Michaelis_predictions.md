# Test C5-3 : la constante de Michaelis (K_M) - PREDICTIONS VERROUILLEES

## Fichier de predictions, ancre avant acquisition

### 0. Statut documentaire

```text
statut : predictions verrouillees du test C5-3, cycle C5
(exportabilite de la grammaire hors physique) ;
CE FICHIER NE CONTIENT AUCUNE DONNEE ACQUISE : il est redige et
ancre (empreinte SHA-256, OpenTimestamps) avant toute recherche
sur sources, conformement au protocole d'horodatage v0.1.
Les resultats iront dans un fichier separe, posterieur a l'ancrage.

troisieme cas hors echantillon : la constante de Michaelis n'a
jamais ete utilisee dans la construction du corpus. Circularite
residuelle declaree : le redacteur possede la biochimie generale
du sujet (definition de K_M, equation de Michaelis-Menten), mais
l'acquisition verifiera sur sources le detail (dependances,
critiques, infrastructure de donnees, debats de statut).
```

### 1. Objet et falsificateurs

```text
objet : K_M, dite "constante de Michaelis", parametre de l'equation
de vitesse enzymatique v = V_max [S] / (K_M + [S]).

criteres C1-C4 : determination, discrimination, valeur ajoutee,
non-forcage (identiques aux tests C5-1 et C5-2).

falsificateurs declares :
E2 - la grille absorbe sans discriminer ;
E3 - la grille ne dit rien que la biochimie ne dise deja d'elle-meme
     (le risque principal, comme en C5-2) ;
E4 - il faut inventer une categorie.
```

### 2. Predictions verrouillees

```text
P-M1 : la grille qualifiera K_M en mode effectif, dependante des
conditions (temperature, pH, force ionique) et surtout relative a
un modele (le schema cinetique de Michaelis-Menten et ses
hypotheses : etat quasi stationnaire, une seule etape limitante).
La forme au rang 0 sera un quotient d'etat, non une valeur libre.

P-M2 : K_M ne sera jamais stabilisee par absorption conventionnelle
(aucune valeur votee exacte) ; comme en C5-2, la latitude de la
valeur reste ouverte par indexation aux conditions et au modele -
confirmation attendue du critere de latitude (on ne conventionne
que ce qui n'a plus de latitude).

P-M3 : la trajectoire fera apparaitre au moins une station du
vocabulaire du corpus : requalification par raffinement du modele
(par exemple, K_M reinterpretee quand le mecanisme simple est
remplace par un mecanisme plus complexe), et/ou tension entre
K_M "apparent" et K_M "vrai" - c'est-a-dire un vocabulaire indigene
du conditionnement (constantes apparentes), que la grille devra
reconnaitre comme equivalent local plutot qu'imposer le sien.

P-M4 : aucune architecture au sens du corpus ; au plus des
dependances de reseau simples (K_M lie a k_cat, a V_max, a la
concentration d'enzyme). Au plus un raffinement declare, aucune
categorie inventee.

prediction de valeur ajoutee (la plus risquee) :
P-M5 : la valeur ajoutee, si elle existe, sera comparative -
K_M relevera du meme mode effectif que G_F en physique (coefficient
effectif valide dans un domaine, sous un modele qui masque une
structure plus fine). Si aucun rapprochement de ce genre ne tient,
la valeur ajoutee sera declaree absente et le test echouera sur C3.
```

### 3. Criteres de verdict fixes

```text
le test passe si C1, C2, C4 tiennent et si C3 produit au moins un
enonce absent du traitement biochimique standard.
le test echoue si E2, E3 ou E4 se declenche.
verdict et donnees : fichier separe, posterieur a l'ancrage.
```
