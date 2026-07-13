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

### 4. Journal d'acquisition, avec correction

```text
etape 1 - acquisition par canal automatise (redacteur-modele via
navigateur pilote) : echec. Les pages de paires renvoyaient
"ill-formed request" ou un gabarit non rempli ("me|alphXXXYYY").
Conclusion provisoire consignee alors : outil casse cote serveur.

etape 2 - controle humain independant (l'auteur, navigateur propre,
flux canonique du site) : le coefficient s'affiche normalement.
r(alpha, m_e) = -0,99999 (CODATA 2022).

correction et retractation : la conclusion de l'etape 1 etait
fausse. La panne residait dans le canal d'acces automatise
(vraisemblablement l'encodage des pipes dans les navigations
programmatiques), non dans le serveur. L'inference "bug interne"
etait trop confiante ; le controle humain l'a falsifiee.
Cette sequence est versee a l'audit de solidite comme cas concret
du risque (c) : le redacteur-modele avait produit une conclusion
coherente et elegante - et fausse.

reste de la decouverte incidente (part confirmee par l'humain) :
le bouton "Search" de l'outil est inoperant dans les deux sessions
independantes (seule la touche Entree fonctionne) ; la couche de
dissemination est degradee mais fonctionnelle. Note pour C4,
au rang reduit d'indice de fragilite.

protocole d'acquisition corrige : les coefficients sont releves par
l'auteur, canal humain, et transmis au corpus.
```

### 5. Resultats contre predictions

| Paire | Prediction verrouillee | Valeur relevee (CODATA 2022) | Statut |
|---|---|---|---|
| r(alpha, m_e) | <= -0,99 | -0,99999 | P1 confirmee |
| r(alpha, R_inf) | \|r\| <= 0,3 | +0,00125 | P4 confirmee, marge de deux ordres de grandeur |
| r(m_e, m_p) | >= +0,99 | +0,99845 | P3 confirmee |
| r(G, alpha) | \|r\| <= 0,2 | 0,00000 | P2 (premiere moitie) confirmee, nullite a la precision affichee |
| r(G, m_e) | \|r\| <= 0,2 | 0,00000 | P2 (seconde moitie) confirmee, nullite a la precision affichee |

Acquisition : valeurs relevees par l'auteur (canal humain) sur
l'outil NIST, CODATA 2022, juillet 2026. Anteriorite des predictions
etablie par l'historique Git du present document.

### 6. Verdict

```text
resultat : cinq releves, cinq predictions confirmees ; aucune des
conditions d'echec E1-E3 declenchee.

lecture, dans les limites declarees en section 1 : le test etait
une condition necessaire, non suffisante ; il est passe. Le gain se
dit exactement ainsi : la carte architecturale du corpus, dessinee
par analyse fonctionnelle et de statut, recouvre les joints
statistiques du reseau CODATA sur les cinq sondages -
le bloc porteur alpha existe (P1 : -0,99999 ; P3 : +0,99845),
la frontiere interne est nette (P4 : 0,00125, deux ordres de
grandeur sous le seuil), et l'ilot gravitationnel est exact
(P2 : 0,00000 deux fois). La quasi-autonomie des secteurs, these
philosophique chez Cao et Schweber, recoit ici des chiffres.

nuance instructive de P3 : r(m_e, m_p) = 0,99845 la ou
r(alpha, m_e) = -0,99999. L'ecart entre les deux est la trace de
la mesure independante du rapport de masses (pieges de Penning) :
la composition a son joint propre, faiblement visible. La grammaire
du corpus predit qualitativement cette hierarchie (le rapport est
une entree independante, la masse en kg est un aval pur d'alpha) ;
la difference des deux coefficients en est la signature chiffree.

statut probatoire initial (requalifie en section 7) : donnees
publiques, predictions anterieures tracables, echec possible et non
advenu.
```

### 7. Objection de tautologie : instruite et retenue

Objection posee par l'auteur apres le verdict :

```text
le corpus est bati sur les chiffres reels (CODATA, PDG, Planck) ;
les architectures ont ete dessinees en connaissant les chaines de
determination ; predire les correlations depuis les architectures,
c'est retrouver la source commune. Le test serait tautologique.
```

Instruction :

```text
l'objection est fondee en substance, et la piece a conviction est
dans le present protocole : la section 1 enonce comme "relation
structurante connue" l'equation d'observation meme dont l'ajustement
tire la correlation mesuree. Le cercle n'est pas dans la
statistique ; il est dans la construction : predictions et donnees
partagent leur source (la structure publique de l'ajustement).

nuances conservees : le test n'etait pas rigoureusement
tautologique - l'echec restait possible par erreur de comprehension
(P4 exigeait la connaissance des budgets d'incertitude ; l'attente
naive, alpha et R_inf cohabitant dans la theorie de l'hydrogene,
etait une correlation notable) - mais son poids evidentiel pour la
grammaire est faible.
```

Requalification du verdict :

```text
ce qui est etabli : un controle de fidelite (la compression du
corpus ne contient pas de contresens sur la structure post-2019 -
non acquis d'avance pour un corpus hors institution) ; une
repetition generale du pipeline de test (predictions verrouillees,
acquisition humaine independante, corrections croisees dans les
deux sens) ; des chiffres a provenance etablie, utilisables en
illustration dans les papiers.

ce qui est retire : la phrase "l'exigence de l'audit est satisfaite".
Elle ne l'est pas : ce test se gagnait par competence sur des faits
publics, non par la valeur ajoutee de la grammaire. Le test que le
corpus ne peut gagner ni par elegance ni par competence de
construction reste a executer.

candidats non tautologiques, par ordre de purete :
1. C5, l'exportabilite : appliquer la grammaire a des cas jamais
   utilises dans sa construction (equilibres chimiques, cinetique
   biologique, constante solaire) - test hors echantillon au sens
   strict ;
2. H1 durci : classifier les modes epistemiques de cas nouveaux en
   aveugle avant de verifier leur mode physique, plutot que de
   relire les fiches qui contiennent deja les deux ;
3. l'extension covariance ne comptera que si elle predit un trait
   non lisible dans les equations d'observation (par exemple un
   chevauchement d'architectures que la carte interdit).

sequence corrigee de la phase de test : C5 ou H1 durci d'abord ;
la presente fiche garde rang de controle de fidelite et de
repetition generale.
```
