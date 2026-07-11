# Test de covariance : architectures contre correlations CODATA v0.1

## Le premier test que le corpus ne peut pas gagner par elegance

### 0. Statut documentaire

```text
statut : test empirique (chantier D5, recommande par l'audit de
solidite, option 1 du point nodal) ;
principe d'integrite : les predictions de la section 2 ont ete
redigees et enregistrees AVANT toute consultation des donnees ;
les donnees sont les coefficients de correlation publies par le
NIST pour l'ajustement CODATA en vigueur - donnees publiques que
ni l'auteur ni le redacteur ne controlent ;
le test peut echouer, et un echec serait un resultat de premier
rang contre la lecture architecturale (T5, D5).
```

### 1. Ce que le test teste, et sa limite declaree d'avance

```text
la these testee : les architectures du corpus, dessinees par
analyse fonctionnelle et de statut (independamment de toute
statistique), decoupent le reseau des constantes aux memes joints
que la matrice de covariance de l'ajustement.

la limite, declaree honnetement avant le resultat : les
correlations CODATA decoulent des equations d'observation et de la
propagation des incertitudes ; un critique dira qu'y retrouver des
blocs est trivial. Reponse tenue d'avance : le test est une
condition necessaire, non suffisante - si meme cette consistance
echoue, la lecture architecturale est en difficulte serieuse ;
si elle reussit, le gain est modeste et se dit ainsi : la carte
architecturale est compatible avec les joints statistiques du
reseau. Ni plus, ni moins.
```

Contexte physique post-2019 (rappel sans consultation des donnees) :

```text
h, e, k_B, N_A sont exactes : leurs correlations sont sans objet.
Les constantes ajustees restantes incluent notamment alpha, R_inf,
les masses en kg (m_e, m_p, ...), les rapports de masses, et G.
Relation structurante connue : m_e = 2 R_inf h / (c alpha^2) ;
l'incertitude de R_inf etant tres inferieure a celle de alpha^2,
la masse en kg est attendue comme grandeur aval de alpha.
```

### 2. Predictions declarees avant consultation

Traduction de la carte architecturale en predictions chiffrees :

```text
P1 - le bloc de realisation de la masse (architecture metrologique
etendue) : alpha est le noeud porteur des masses en kg apres 2019.
Prediction : r(alpha, m_e) <= -0.99 (correlation forte, de signe
negatif car m_e varie comme alpha^-2).

P2 - la quasi-autonomie du secteur gravitationnel (architecture
effective basse energie ; Cao-Schweber ; fiche alpha_G / M_Pl) :
G ne tient a aucun noeud du reseau electromagnetique-spectroscopique.
Prediction : |r(G, alpha)| <= 0.2 et |r(G, m_e)| <= 0.2.

P3 - la solidarite de composition (rapports de masses mesures en
pieges, masse en kg tiree du bloc alpha) : les masses en kg varient
ensemble. Prediction : r(m_e, m_p) >= +0.99.

P4 - la frontiere interne du bloc (entree spectroscopique distincte
de l'entree alpha) : R_inf est mesuree par des routes largement
independantes de alpha. Prediction : |r(alpha, R_inf)| <= 0.3.
P4 est la prediction la plus risquee : une forte correlation
alpha-R_inf serait un echec de frontiere.
```

Conditions d'echec :

```text
E1 : P1 ou P3 echoue (le bloc porteur n'existe pas) -> echec majeur
     de la lecture architecturale du reseau metrologique ;
E2 : P2 echoue (G solidaire du bloc) -> echec de la quasi-autonomie,
     revision de l'architecture effective requise ;
E3 : P4 echoue -> les frontieres internes du corpus ne correspondent
     pas aux joints statistiques ; la carte doit etre redessinee ;
E4 : donnees inaccessibles en session -> le test est reporte, non
     repute reussi.
```

### 3. Source des donnees

```text
coefficients de correlation de l'ajustement CODATA en vigueur,
publies par le NIST (physics.nist.gov, outil des correlations),
releves apres la redaction des sections 1 et 2.
```

### 4. Resultats : condition E4 declenchee, avec une decouverte

Journal d'acquisition (juillet 2026) :

```text
1. outil de correlations du NIST, opere dans un navigateur reel :
   la selection de la premiere constante fonctionne (alpha, valeurs
   CODATA 2022 affichees) ; la page finale de paire renvoie soit
   "ill-formed request" (liens a deux pipes servis par le site
   lui-meme), soit un gabarit non rempli affichant litteralement
   "me|alphXXXYYY" a la place du coefficient.
   Verifie dans les deux ordres (me|alph et alph|me), memes
   symptomes : l'outil est casse cote serveur a l'etape finale.

2. papier CODATA 2022 abrege (arXiv:2409.03787, consulte) :
   correlations d'entree seulement (AMDC, energies de liaison) ;
   les correlations de sortie des valeurs recommandees sont
   renvoyees au site et au papier detaille, non publie a ce jour.

3. archive Wayback du point d'acces : aucune capture des pages de
   paires.

conclusion d'acquisition : les correlations de sortie de
l'ajustement en vigueur sont actuellement inaccessibles au public -
non par restriction, mais par panne de l'unique point de
dissemination.
```

### 5. Verdict

```text
E4 : test reporte, non repute reussi. Les predictions P1-P4 restent
verrouillees telles quelles pour l'execution future ; leur date de
redaction anterieure a toute donnee est etablie par ce document.

decouverte incidente, a verser au cycle C4 (vie materielle des
constantes) : la couche de dissemination des correlations CODATA -
l'ombre numerique des solidarites - est en panne, sans que la
litterature s'en emeuve. La matrice de covariance n'est publiee
nulle part ailleurs que dans l'outil casse : la solidarite chiffree
des constantes n'a, en juillet 2026, aucun support public
fonctionnel. C'est une donnee de premiere main pour C4, et une
ironie de rang : le test de la solidarite est bloque par une
defaillance de la solidarite documentaire.

actions de reprise :
1. signaler la panne au NIST (contact : pml-webmaster@nist.gov) -
   action a la main de l'auteur ;
2. re-executer le test des retablissement de l'outil ou publication
   du papier detaille CODATA 2022 ;
3. en attendant, la phase de test se poursuit par le deuxieme test
   dur (H1 sur les fiches existantes, plan d'arene axe 5).
```
