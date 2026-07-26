# α3 — Audit borné du couplage courant `alpha(Q²)` v0.1

## 0. Statut

```text
statut : fiche scientifique locale sous délégation procédurale ;
date : 26 juillet 2026 ;
opération : α3, issue #38 ;
source primaire directrice : L3 Collaboration,
                              Phys. Lett. B 623, 26–36 (2005) ;
DOI : 10.1016/j.physletb.2005.07.052 ;
version ouverte : arXiv:hep-ex/0507078 ;
source d’appui : OPAL Collaboration,
                 Eur. Phys. J. C 45, 1–21 (2006) ;
fonction : reconstruire le test expérimental de la dépendance espace-like
           du couplage électromagnétique avec le transfert d’impulsion ;
autorité : descriptive et locale ;
ne vaut pas : mesure directe universelle de alpha(Q²),
               variation temporelle ou spatiale de alpha(0),
               reconstruction indépendante des générateurs,
               verdict général sur « alpha est constante »,
               ou propagation automatique dans la synthèse du cycle 1.
```

## 1. Résultat directeur

Dans α3, la transformation testée est le transfert d’impulsion quadratique espace-like `Q² < 0`.

```text
cible : couplage électromagnétique effectif alpha(Q²) ;
transformation : variation de -Q² dans un domaine de collision ;
observable première : section efficace différentielle de diffusion Bhabha ;
relation d’accès : prédiction radiative de la section efficace selon alpha(Q²) ;
paramètre ajusté : amplitude C du running attendu ;
résultat attendu en QED : C = 1 ;
hypothèse sans running : C = 0.
```

Le test ne demande donc pas si la valeur numérique de basse énergie est maintenue lorsque `Q²` change. Il demande si la section efficace suit la dépendance en `Q²` produite par la polarisation du vide.

## 2. Non-identités obligatoires

```text
alpha(0)
≠
alpha(Q²) ;

valeur CODATA de basse énergie
≠
valeur du couplage effectif à grand transfert ;

variation avec Q²
≠
variation avec le temps ;

running prédit par la renormalisation
≠
instabilité empirique d’une constante ;

ajustement du paramètre C
≠
mesure absolue indépendante de alpha(Q²) à chaque point.
```

## 3. Mécanisme théorique de passage

La propagation du photon reçoit des insertions de polarisation du vide. Les boucles virtuelles chargées modifient la relation entre la charge définie à basse énergie et l’interaction effective sondée à un transfert donné.

La paramétrisation employée par L3 est :

```text
alpha(Q²) = alpha(0) / [1 - C Delta alpha(Q²)].
```

```text
C = 1 : amplitude du running prévue dans l’évaluation QED utilisée ;
C = 0 : couplage indépendant de Q² dans cette paramétrisation ;
Delta alpha(Q²) : correction de polarisation du vide fournie au calcul ;
alpha(0) : ancrage de basse énergie, non paramètre libre du test principal.
```

Les contributions leptoniques à `Delta alpha(Q²)` sont calculables perturbativement avec haute précision. Les contributions hadroniques reposent sur une évaluation utilisant des données de production hadronique et des relations de dispersion. Le test de L3 est donc expérimental, mais il n’est pas sans théorie de passage.

## 4. Domaine expérimental L3

```text
processus : e+ e- -> e+ e- ;
installation : LEP, détecteur L3 ;
années : 1998–2000 ;
energies du centre de masse : 189–209 GeV ;
luminosité intégrée : 607.4 pb^-1 ;
événements sélectionnés : environ 40 000 ;
angles : |cos(theta)| < 0.9 ;
domaine effectivement sondé :
  1800 GeV² < -Q² < 21600 GeV².
```

La diffusion est dominée dans l’essentiel de ce domaine par l’échange de photon en canal `t`. Le transfert dépend de l’énergie du centre de masse et de l’angle de diffusion. Les dix intervalles angulaires et huit groupes d’énergie produisent 80 mesures différentielles.

## 5. Observable et chaîne de détermination

La quantité mesurée n’est pas `alpha(Q²)` isolément.

```text
comptage d’événements
+ acceptance du détecteur
+ luminosité intégrée
-> section efficace différentielle mesurée ;

section efficace différentielle mesurée
+ prédiction radiative paramétrée par C
-> ajustement du paramètre C ;

C
+ forme déclarée de Delta alpha(Q²)
-> représentation du running dans le domaine étudié.
```

La luminosité est elle-même déterminée par la diffusion Bhabha à petit angle dans le moniteur de luminosité. L’analyse doit donc propager la dépendance à `C` à la fois dans la prédiction de grande angle et dans l’estimation de luminosité.

## 6. Rôle des générateurs et calculs

```text
BHLUMI 4.04 :
  calcul de la diffusion Bhabha à petit angle
  utilisée pour la luminosité ;

BHWIDE 1.03 :
  diffusion Bhabha à grand angle,
  corrections radiatives et dépendance à C ;

GEANT :
  réponse du détecteur et effets de propagation ;

autres générateurs :
  fonds leptoniques, bosoniques et deux-photons.
```

La section efficace est décrite comme une partie de Born multipliée par un terme radiatif dominé par l’émission réelle de photons. L’extraction de `C` dépend donc de la précision de la prédiction de Bhabha, de la mise en œuvre du running et de l’acceptance.

## 7. Contrôles expérimentaux

Les contrôles publiés comprennent :

- sélection séparée dans les régions barrel et endcap ;
- rejet de la zone de transition calorimétrique ;
- coupure d’acolinarité contre le rayonnement initial dur ;
- identification calorimétrique et association aux traces ;
- repliement en `|cos(theta)|` pour réduire les effets de confusion de charge ;
- simulation temporelle des inefficacités du détecteur ;
- contrôle des migrations entre intervalles ;
- traitement conservateur des incertitudes systématiques comme corrélées.

## 8. Incertitudes dominantes

Les familles principales sont :

```text
prédiction théorique de la section efficace :
  environ 0.5 % à 1.5 % selon la région angulaire ;

sélection expérimentale :
  environ 1 % à 10 % selon l’intervalle ;

termes radiatifs supérieurs non inclus dans la paramétrisation BHWIDE :
  incertitude assignée d’environ 0.2 % à 1.5 % ;

luminosité et acceptance :
  propagées dans le même ajustement ;

fonds et migrations :
  contrôlés, migrations déclarées négligeables au niveau utile.
```

L’incertitude systématique finale sur `C` est supérieure à l’incertitude statistique. Le résultat positif dépend donc substantiellement de la maîtrise de la section efficace théorique et des sélections.

## 9. Résultat de l’ajustement

L3 obtient :

```text
C = 1.05 ± 0.07_stat ± 0.14_syst.
```

Le résultat est compatible avec `C = 1`.

```text
ajustement avec running :
  chi² = 91.9 pour 79 degrés de liberté ;
  niveau de confiance = 17 % ;

hypothèse sans running C = 0 :
  chi² = 316 pour 80 degrés de liberté ;
  niveau de confiance extrêmement faible.
```

La source décrit donc `C=0` comme exclu dans le cadre du test publié.

## 10. Portée de l’exclusion de `C=0`

L’exclusion est probante relativement à une famille précise :

```text
forme de Delta alpha(Q²) utilisée ;
amplitude globale libre C ;
domaine 1800–21600 GeV² en -Q² ;
observable Bhabha à grand angle ;
modèle radiatif et générateurs employés ;
traitement déclaré des systématiques.
```

Elle soutient :

```text
la section efficace varie avec Q² comme attendu
pour un couplage électromagnétique courant ;

l’hypothèse d’une absence complète de running
selon C=0 est incompatible avec ces données ;

l’amplitude observée est compatible avec la prédiction QED C=1.
```

Elle ne soutient pas seule :

```text
une reconstruction modèle-indépendante de alpha(Q²) ;
une invariance ou une variation temporelle de alpha(0) ;
une mesure universelle dans tous les schémas et domaines ;
une séparation expérimentale complète des contributions
leptoniques et hadroniques ;
la validité absolue de toutes les corrections radiatives.
```

## 11. Appui OPAL et différence de rang

OPAL utilise la diffusion Bhabha à petit angle dans le domaine :

```text
1.81 GeV² < -Q² < 6.07 GeV².
```

Le résultat différentiel publié est :

```text
Delta alpha(-6.07 GeV²) - Delta alpha(-1.81 GeV²)
  = (440 ± 58_stat ± 43_exp ± 30_th) × 10^-5.
```

OPAL exclut une valeur constante dans cet intervalle à plus de cinq écarts-types et rapporte une sensibilité à la contribution hadronique.

La fonction d’OPAL dans α3 est un contrôle de rang :

```text
même transformation générale : Q² espace-like ;
observable de même famille : diffusion Bhabha ;
domaine et géométrie : différents ;
architecture de systématiques : différente ;
résultat : confirmation positive du running,
           sans équivalence complète avec L3.
```

## 12. Résultat scientifique local

```text
résultat physique positif :
  dépendance du couplage électromagnétique effectif
  avec le transfert espace-like observée par Bhabha ;

porteur du test :
  relation entre section efficace différentielle
  et couplage courant dans le domaine déclaré ;

forme de maintien :
  maintien de la relation de running prévue,
  non maintien numérique de alpha(0) ;

mode de soutien probatoire :
  signal différentiel positif
  + ajustement paramétrique
  + comparaison à une hypothèse sans running
  + calcul radiatif et contrôle instrumental.
```

## 13. Réponse locale aux questions publiques

### Q1

La frontière entre variation et maintien se déplace ici parce que la variation avec l’échelle n’est pas une anomalie à éliminer : elle est le comportement physique attendu. Ce qui est maintenu est la relation fonctionnelle de l’évolution, dans les incertitudes du test.

### Q2

Le maintien devient opératoire par :

```text
une observable de collision ;
un domaine de Q² ;
une fonction de polarisation du vide ;
un paramètre d’amplitude C ;
des générateurs radiatifs ;
un ajustement différentiel ;
une hypothèse nulle explicite.
```

L’enquête ne demande plus « alpha garde-t-elle la même valeur ? », mais « la transformation d’échelle suit-elle la relation de running déclarée ? »

## 14. Condition d’arrêt

```text
ce qui est mesuré : section efficace différentielle de Bhabha ;
ce qui est paramétré : amplitude C de Delta alpha(Q²) ;
ce qui est calculé : corrections radiatives, luminosité et acceptance ;
transformation testée : Q² espace-like ;
hypothèse exclue : C=0 dans la famille déclarée ;
résultat positif : compatibilité avec C=1 ;
portée : locale aux domaines et modèles du test ;
non-pertinent : variation temporelle ou cosmologique de alpha(0).
```

Cette condition est remplie pour le premier lot α3.