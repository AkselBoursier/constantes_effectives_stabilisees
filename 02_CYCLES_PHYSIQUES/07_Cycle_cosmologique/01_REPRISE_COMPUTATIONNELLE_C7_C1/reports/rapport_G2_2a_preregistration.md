# G2.2a — pré-enregistrement ratifié des inférences X(z)

Issue directrice : #63.

Décision humaine : D3-A à D3-H ratifiées le 29 juillet 2026, commentaire G2.2b.

Base scientifique : G2.1 fusionnée dans `main` au commit
`b7d9416326193d88c2ef45dfabcd58c72bf79ac1` ; instrument, tests I1–I9,
tolérances T8–T12 et distinction R1/R2/R3 validés selon les limites déclarées.

## 1. Statut

Ce document fixe ex ante les modèles, coordonnées, priors, contrôles,
statistiques, règles d’arrêt et conditions d’amendement du lot `X(z)`.

```text
pré-enregistrement scientifique : GELÉ ;
configuration exécutable : absente ;
MCMC / minimisation / posterior réel : absents et interdits à ce stade ;
inspection d’un résultat X(z) du lot commun : interdite ;
G2.3 : fermée jusqu’à audit et merge de ce document.
```

Les bornes numériques des amplitudes `X_i` sont des choix du projet. Elles ne
doivent jamais être présentées comme des priors Wang–Freese : la publication
de Yun Wang et Katherine Freese documente des priors plats larges, mais ne
publie pas les bornes numériques exactes des `X_i`.

## 2. Données, vraisemblance et cadre communs

Le lot conserve exactement le cadre commun de G1 :

```text
BAO : DESI DR2, 13 composantes, covariance officielle épinglée ;
CMB : compression publique arrondie sur
      (theta_star, ombh2, ombh2 + omch2) ;
géométrie : plate ;
CAMB : 1.5.4 ;
Somme m_nu : 0.06 eV ;
N_eff : 3.044 ;
BBN : prédicteur G1 ;
traitement acoustique directeur : corrected ;
contrôle numérique : fixed, non considéré comme modèle concurrent.
```

Les paramètres fixes de G1 restent fixes. Les distributions `ref` et
`proposal` servent seulement à l’initialisation et ne constituent pas des
priors scientifiques.

## 3. Registre des modèles

### 3.1 Références

```text
M0 — LambdaCDM : 3 paramètres libres de fond ;
M1 — CPL w0waCDM : 5 paramètres libres.
```

### 3.2 Reconstructions X(z)

Les quatre variantes suivantes sont co-primaires. Aucune ne peut être éliminée
ou promue après inspection d’un résultat :

```text
M2a-N — nœuds z = {0, 1/3, 2/3, 1, 4/3, 2.33}, spline natural ;
M2a-K — même grille, spline not-a-knot ;
M2b-N — nœuds z = {0, 1/3, 2/3, 1, 2.33}, spline natural ;
M2b-K — même grille, spline not-a-knot.
```

Dans chaque cas :

```text
X(0) = 1 fixé ;
les autres valeurs nodales sont libres ;
X(z >= 2.33) = X(2.33) ;
aucune conversion vers w(z) ;
aucun modèle supplémentaire de perturbations sombres ;
fond direct : H_X^2 = H_ref^2 + H0^2 Omega_X,0 [X(z)-1].
```

Le suffixe `N` désigne `natural`; le suffixe `K` désigne `not-a-knot`.

## 4. Coordonnées et priors de fond communs

```text
H0    ~ U[20, 100] km s^-1 Mpc^-1 ;
ombh2 ~ U[0.005, 0.1] ;
omm   ~ U[0.01, 0.99] ;

omch2 = omm*(H0/100)^2 - mnu/93.14 - ombh2 ;
contrainte dure : omch2 > 0.
```

Aucun changement de coordonnées d’échantillonnage ne sera introduit entre M0,
M1 et M2 sans amendement formel.

## 5. Priors des amplitudes X_i

Chaque `X_i` libre reçoit le même prior marginal au sein d’une famille. Les
contraintes de validité du fond rendent cependant le prior effectif non
rectangulaire et corrélé.

```text
P_WS — enveloppe large signée : X_i ~ U[-2, 4] ;
P_CS — prior central signé   : X_i ~ U[-1, 3] ;
P_W+ — enveloppe large positive : X_i ~ U[0, 4] ;
P_C+ — prior central positif    : X_i ~ U[0, 3] ;
P_XL — contingence très large signée : X_i ~ U[-4, 6].
```

`P_XL` n’est pas une cinquième analyse ordinaire. Elle ne peut être ouverte que
selon le déclencheur pré-enregistré suivant : accumulation résolue au voisinage
d’une frontière de `P_WS` qui empêche de distinguer contrainte par les données
et troncature par le prior. Son ouverture doit être déclarée avant toute
interprétation correspondante et appliquée à toutes les variantes structurelles
affectées.

Toutes les familles sont conditionnées par :

```text
H_X^2(z) > 0 sur tout le domaine requis ;
observables et intégrales finies ;
omch2 > 0 ;
T8–T12 satisfaites par l’instrument.
```

Cette géométrie doit être déclarée dans toute interprétation. Le volume de
l’hyperrectangle initial ne peut pas être traité comme le volume physique valide.

## 6. Réutilisation par troncature

`P_CS`, `P_W+` et `P_C+` peuvent être obtenus par troncature exacte des chaînes
`P_WS` uniquement si, pour chaque variante structurelle :

```text
ESS après troncature >= 1000 pour chaque paramètre central ;
ESS / ESS_enveloppe >= 0.10 ;
chaque chaîne initiale contribue à l’échantillon tronqué ;
aucune frontière du sous-prior ne porte une accumulation non résolue.
```

À défaut, des chaînes dédiées sous le prior déjà pré-enregistré sont
obligatoires. Les bornes ne peuvent pas être redéfinies à partir des résultats.

## 7. Porte MCMC

Pour chaque variante structurelle co-primaire sous le prior directeur `P_WS` :

```text
nombre minimal de chaînes indépendantes : 8 ;
critères Cobaya hérités de G1 :
  Rminus1_stop = 0.01 ;
  Rminus1_cl_stop = 0.02 ;
diagnostic externe : R-hat scindé et normalisé par rang <= 1.01 ;
ESS bulk >= 1000 pour chaque paramètre libre ;
ESS tail >= 1000 pour chaque paramètre libre ;
graines explicites et distinctes ;
chaînes et produits volumineux hors Git.
```

Aucune interprétation comparative ou physique n’est autorisée avant la
convergence des quatre variantes structurelles. Un échec de convergence est un
résultat de méthode à diagnostiquer, non une preuve contre le modèle.

## 8. Minimisation et statistiques globales

Les minima de vraisemblance et MAP sont recherchés par un protocole
multi-départs gelé. Les meilleurs échantillons convergés peuvent servir de
départs informés ; les échecs et minima locaux restent documentés.

Les conventions sont :

```text
nombre de points de données : n = 16
  (13 BAO + 3 composantes du prior CMB comprimé) ;

nombre de paramètres libres :
  M0 : k = 3 ;
  M1 : k = 5 ;
  M2a-N / M2a-K : k = 8 ;
  M2b-N / M2b-K : k = 7.
```

Les quantités à publier sont au minimum :

```text
chi2_min total ;
chi2_BAO et chi2_CMB séparés ;
AIC ;
AICc ;
BIC ;
minimum rencontré dans les chaînes ;
MAP et maximum de vraisemblance distingués ;
dispersion des optimisations multi-départs.
```

L’évidence bayésienne est suspendue. Elle ne peut être ajoutée sans protocole
séparé, validation numérique et analyse de sensibilité explicite aux quatre
familles de priors `X_i`.

## 9. Calibration de la préférence globale

Aucune application automatique du théorème de Wilks n’est autorisée pour les
modèles spline.

Après obtention de minima stables, la préférence globale éventuelle sera
calibrée par simulations paramétriques sous M0 :

```text
lot initial : 2 000 pseudo-données avec covariance BAO+CMB fixée ;
refit de M0 et de chaque variante M2 avec le protocole de minimisation gelé ;
si moins de 50 dépassements ou p_estime < 0.025 : extension automatique
  au total de 10 000 simulations ;
si aucun dépassement : borne empirique seulement, sans extrapolation
  gaussienne non validée.
```

Cette calibration appartient à G3, mais son déclencheur et son effectif sont
fixés ici avant l’observation du contraste réel.

## 10. Sensibilités obligatoires

```text
S1 — M2a vs M2b : effet du nombre de nœuds ;
S2 — natural vs not-a-knot : effet de la condition de bord ;
S3 — P_WS vs P_CS : effet de largeur ;
S4 — signé vs positif : effet de la contrainte X >= 0 ;
S5 — corrected vs fixed : contrôle numérique T12(b), non modèle concurrent ;
S6 — bornes partielles publiées : troncature H0 >= 30 et
     0.02 <= ombh2 <= 0.024, seulement si ESS suffisant.
```

`S6` ne doit pas être appelée « reproduction Wang–Freese » : leur prior complet,
notamment les bornes exactes des `X_i`, demeure indisponible.

Hors lot : supernovæ, spectres CMB complets, lentillage, autres grilles nodales,
pénalisation de lissage, reconstruction `w(z)` et extensions simultanées des
neutrinos.

## 11. Présentation épistémique

Les résultats devront séparer :

```text
R1 — reproductibilité du calcul ;
R2 — cohérence interne et stabilité ;
R3 — validation indépendante, avec dépendances partagées déclarées ;
effet du nombre de nœuds ;
effet de la convention de spline ;
effet du support et de la largeur du prior ;
effet de la contrainte de positivité ;
préférence globale calibrée et écarts marginaux locaux.
```

Une déviation locale de `X_i` par rapport à 1 ne constitue pas, à elle seule,
une préférence globale pour une énergie noire évolutive. Un croisement de zéro
ou une structure interpolée ne doit pas être présenté comme établi si son statut
dépend de la convention de spline ou du support du prior.

## 12. Gel et amendements

Le présent protocole est gelé avant toute inférence réelle `X(z)` du lot commun.

Tout amendement ultérieur doit :

```text
être daté et versionné ;
identifier précisément la clause modifiée ;
être motivé indépendamment d’une significativité jugée insuffisante ou excessive ;
indiquer tous les résultats déjà visibles au moment de l’amendement ;
ré-exécuter tous les modèles et sensibilités affectés ;
conserver la version antérieure dans l’historique Git et dans #63.
```

Une correction de bogue démontrée peut justifier un amendement ; elle ne permet
pas de modifier silencieusement un prior, une variante, une statistique ou une
règle d’arrêt.

## 13. Décisions humaines ratifiées

```text
D3-A — quatre variantes structurelles co-primaires : RATIFIÉE ;
D3-B — coordonnées et priors de fond G1, omch2>0 : RATIFIÉE ;
D3-C — familles de priors X_i et règles de troncature : RATIFIÉE ;
D3-D — porte MCMC et diagnostics de convergence : RATIFIÉE ;
D3-E — minimisation, n, k, AIC/AICc/BIC, évidence suspendue : RATIFIÉE ;
D3-F — absence de Wilks automatique et simulations 2 000 -> 10 000 : RATIFIÉE ;
D3-G — sensibilités S1–S6 et périmètre hors lot : RATIFIÉE ;
D3-H — gel et amendement ex ante : RATIFIÉE.
```

## 14. Condition de sortie de G2.2

G2.2 peut être close lorsque :

```text
ce document a été audité et fusionné ;
sa conformité à D3-A–H est confirmée ;
aucune configuration exécutable ou sortie d’inférence n’a précédé son gel ;
la porte suivante est ouverte par une décision humaine distincte.
```

Le merge de ce document n’autorise pas automatiquement une MCMC. La conception
et l’audit des configurations exécutables constituent l’étape suivante ; la
première inférence réelle reste conditionnée à une autorisation explicite.