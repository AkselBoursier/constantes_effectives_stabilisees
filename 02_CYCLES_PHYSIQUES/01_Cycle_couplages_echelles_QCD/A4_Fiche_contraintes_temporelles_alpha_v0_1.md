# α4 — Audit borné des contraintes temporelles sur `alpha` v0.1

## 0. Statut

```text
statut : fiche scientifique locale sous délégation procédurale ;
date : 26 juillet 2026 ;
opération : α4, issue #39 ;
source primaire directrice : Lange et al.,
                              Phys. Rev. Lett. 126, 011102 (2021) ;
DOI : 10.1103/PhysRevLett.126.011102 ;
version inspectée : arXiv:2010.06620v2 ;
source d’appui : Godun et al., Phys. Rev. Lett. 113, 210801 (2014) ;
produits publics : séries de rapport E3/E2 et de fréquence E3 déposées par PTB ;
fonction : reconstruire les contraintes sur une dérive linéaire de alpha
           et sur un couplage à la variation annuelle du potentiel solaire ;
autorité : descriptive et locale ;
ne vaut pas : invariance temporelle universelle,
               recherche exhaustive d’oscillations ou de transitoires,
               contrainte indépendante de tout coefficient de sensibilité,
               ou verdict sur alpha(Q²) et les quasars.
```

## 1. Résultat directeur

Une horloge ne mesure pas directement `alpha`. Elle mesure une fréquence de transition. Une comparaison d’horloges mesure un rapport de fréquences. La variation de `alpha` est inférée parce que les transitions ont des sensibilités relativistes différentes.

```text
observable première : rapport ou fréquence de transitions atomiques ;
transformation : temps ou potentiel gravitationnel solaire ;
relation de passage : sensibilité différentielle des transitions à alpha
                      et, selon la comparaison, à d’autres rapports sans dimension ;
paramètres inférés : dérive de ln(alpha) et coefficient de couplage à Phi ;
résultat : paramètres compatibles avec zéro dans les familles testées.
```

## 2. Deux chaînes expérimentales distinctes

### 2.1 Rapport optique E3/E2 de `171Yb+`

```text
transitions :
  E2 — quadrupole électrique ;
  E3 — octupole électrique ;

système : deux horloges à ion unique 171Yb+ ;
mesure : nu_E3 / nu_E2 par peigne de fréquences optiques ;
période : 11 mesures sur environ 1 500 jours,
          du 19 mai 2016 au 20 août 2020 ;
résultat moyen :
  nu_E3/nu_E2 = 0.932 829 404 530 965 376(32) ;
incertitude fractionnaire totale : 34 × 10^-18.
```

Le rapport E3/E2 est particulièrement utile parce qu’il est sensible essentiellement à `alpha` dans la paramétrisation retenue : les deux transitions appartiennent au même ion, tandis que leurs contributions relativistes diffèrent fortement.

### 2.2 Fréquence absolue E3 rapportée au césium

```text
observable : fréquence E3 comparée aux fontaines CSF1 et CSF2 ;
période étendue : mesures entre 2010 et 2019 ;
valeur récente moyenne :
  nu_E3 = 642 121 496 772 645.10(8) Hz ;
références : deux fontaines au césium ;
liaison : peigne optique et maser à hydrogène comme oscillateur volant
          pour certaines interruptions.
```

Cette seconde chaîne est sensible à `alpha`, mais aussi au rapport proton-électron `mu` et à des paramètres nucléaires associés à la transition hyperfine du césium. Elle nécessite donc une analyse conjointe, non une inversion simple vers `alpha` seule.

## 3. Relation de sensibilité

Une fréquence atomique peut être paramétrée schématiquement par :

```text
d ln(nu)
  = K_alpha d ln(alpha)
  + K_mu d ln(mu)
  + K_q d ln(m_q/Lambda_QCD).
```

Pour un rapport `R = nu_A/nu_B` :

```text
d ln(R)
  = Delta K_alpha d ln(alpha)
  + Delta K_mu d ln(mu)
  + Delta K_q d ln(m_q/Lambda_QCD).
```

Pour E3/E2, la sensibilité différentielle à `alpha` est grande, environ `-6.95` dans le calcul atomique employé. La dérive mesurée du rapport peut donc être transformée en une contrainte sur `d ln(alpha)/dt`.

Conséquence de rang :

> La sensibilité à `alpha` est calculée par structure atomique ; elle n’est pas mesurée séparément par la série temporelle elle-même.

## 4. Dérive linéaire testée

La première famille est :

```text
ln R(t) = ln R_0 + a (t - t_0).
```

Le paramètre `a` est une pente constante sur la période observée. Pour le rapport E3/E2 :

```text
(1/R) dR/dt = -6.8(7.5) × 10^-18 yr^-1 ;
```

ce qui produit :

```text
(1/alpha) d alpha/dt
  = 1.0(1.1) × 10^-18 yr^-1.
```

Le résultat est compatible avec zéro.

Cette contrainte porte sur une dérive lente approximée comme linéaire pendant la durée du jeu de données. Elle ne teste pas avec la même sensibilité :

- une oscillation rapide ;
- une variation stochastique ;
- un événement transitoire ;
- une dérive non linéaire arbitraire ;
- une variation en dehors de la période couverte.

## 5. Couplage à la variation annuelle du potentiel

La seconde famille exploite l’ellipticité de l’orbite terrestre. Le potentiel gravitationnel solaire à la Terre comporte une modulation annuelle connue.

Le modèle ajusté est de la forme :

```text
ln R(t)
  = ln R_0
  + k_R [Delta Phi(t)/c²].
```

Avec la sensibilité différentielle à `alpha`, l’analyse déduit :

```text
(c²/alpha) d alpha/dPhi
  = 14(11) × 10^-9.
```

Le résultat est compatible avec zéro à environ 1.3 écart-type.

Il s’agit d’une contrainte sur un couplage corrélé à une modulation annuelle précise, non d’une mesure générale de dépendance de `alpha` à tout champ gravitationnel.

## 6. Paramètres simultanés et dépendances

```text
E3/E2 :
  sensibilité dominante à alpha ;
  offset du rapport ;
  pente ou amplitude annuelle ;
  incertitudes statistiques et reproductibilité systématique ;

E3/Cs :
  alpha ;
  mu ;
  paramètres nucléaires ou quarks légers ;
  données externes Rb/Cs et autres comparaisons ;
  incertitudes des fontaines et du maser volant.
```

Le résultat publié sur `alpha` est donc particulièrement direct pour E3/E2, mais les résultats conjoints avec le césium reposent sur un réseau de sensibilités et de contraintes externes.

## 7. Dispositif et contrôle des systématiques

Les contrôles comprennent :

- deux horloges à ion unique et deux transitions du même isotope ;
- peigne de fréquences optiques ;
- laser stabilisé par cavité cryogénique pour améliorer la stabilité ;
- orientations magnétiques orthogonales pour réduire les décalages tensoriels ;
- budgets séparés E2 et E3 ;
- ajout d’une incertitude de reproductibilité sur les mesures de long terme ;
- deux fontaines au césium pour la fréquence absolue E3 ;
- simulations du bruit du maser pour les intervalles d’extrapolation ;
- ajustements séparés de la pente et de la modulation au potentiel.

Le budget E2 est dominé en incertitude par le rayonnement du corps noir et le décalage quadrupolaire. La reproductibilité pertinente pour une série temporelle est distinguée de l’incertitude absolue complète.

## 8. Accessibilité

PTB a publié les séries numériques utilisées pour :

```text
rapport E3/E2 de la figure 2 ;
fréquence absolue E3 de la figure 3.
```

Les données sont disponibles en format texte. Cette accessibilité permet une inspection et une réanalyse des ajustements simples, mais α4 ne réalise pas ici une reproduction numérique indépendante complète.

## 9. Contrôle P27

Le résultat négatif satisfait les conditions minimales de sensibilité :

```text
famille déclarée :
  dérive linéaire lente ;

seconde famille déclarée :
  modulation annuelle corrélée à Delta Phi ;

porteur du test :
  rapports de fréquences différentiellement sensibles ;

domaine :
  plusieurs années de mesures ;

sensibilité :
  coefficient atomique explicite et incertitudes publiées ;

sortie :
  pente et amplitude avec écart-type.
```

Il est donc légitime de dire que ces familles sont contraintes et qu’aucun signal significatif n’est détecté dans ce domaine.

Il n’est pas légitime de dire que toute variation temporelle de `alpha` est exclue.

## 10. Résultat scientifique local

```text
résultat physique :
  absence de signal significatif pour une dérive linéaire lente
  et pour un couplage annuel au potentiel solaire ;

mode de soutien probatoire :
  non-détection discriminante ;

cible analytique :
  paramètres de variation de ln(alpha)
  dans deux familles déclarées ;

portée :
  laboratoire terrestre, période et spectre temporel bornés ;

limite :
  dépendance aux sensibilités atomiques
  et aux modèles temporels ajustés.
```

## 11. Réponse locale aux questions publiques

### Q1

La frontière entre variation et maintien est établie par sensibilité différentielle : un rapport de fréquences stable ne soutient une constance de `alpha` que relativement à une famille de variations qui aurait produit un signal détectable.

### Q2

Le maintien devient opératoire par :

```text
transitions différentes
+ coefficients de sensibilité
+ série temporelle
+ modèle de pente ou de modulation
+ budget de reproductibilité
+ ajustement et covariance.
```

La non-détection n’est pas une absence brute ; elle est le résultat d’une architecture de comparaison capable de distinguer certaines variations.

## 12. Condition d’arrêt

```text
ce qui est mesuré : rapports et fréquences atomiques ;
ce qui est calculé : coefficients de sensibilité ;
familles testées : dérive linéaire et modulation annuelle ;
paramètres inférés : dérivée temporelle et couplage à Phi ;
résultat : compatibilité avec zéro ;
soutien : non-détection discriminante ;
hors domaine : oscillations larges, transitoires et formes arbitraires.
```

Cette condition est remplie pour le premier lot α4.