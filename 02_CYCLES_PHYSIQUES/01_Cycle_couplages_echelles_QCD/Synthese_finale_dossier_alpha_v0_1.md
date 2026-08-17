# Synthèse finale du dossier `alpha` — α1 à α5 v0.1

## 0. Statut

```text
statut : synthèse finale proposée, en attente de validation humaine ;
date : 26 juillet 2026 ;
périmètre : dossier alpha du cycle 1, opérations α1–α5 ;
branche : agent/cycle-1-alpha-a1 ;
PR : #35 ;
fonction : articuler les résultats locaux validés ou adoptés
           selon quatre transformations distinctes ;
autorité : proposition de synthèse ;
ne vaut pas : fusion dans main,
               propagation dans la synthèse active du cycle 1,
               clôture du cycle 1 entier,
               ni verdict universel « alpha est constante ».
```

### Entrées directes

```text
α1 :
  A1_Registre_sources_versions_alpha_v0_1.md ;
  A1_Matrice_cibles_transformations_acces_alpha_v0_1.md ;

α2 :
  A2_Extraction_CODATA_alpha_v0_1.md ;
  A2_Matrice_chaines_determination_alpha_v0_1.md ;
  A2_Fiche_voie_cesium_alpha_v0_1.md ;
  A2_Fiche_voie_rubidium_alpha_v0_1.md ;
  A2_Fiche_voie_gmoins2_alpha_v0_1.md ;
  A2_Matrice_comparative_trois_chaines_alpha_v0_2.md ;
  A2_Verdict_comparatif_local_alpha_v0_1.md ;

α3 :
  A3_Fiche_running_alpha_Q2_v0_1.md ;
  A3_Verdict_local_running_alpha_v0_1.md ;

α4 :
  A4_Fiche_contraintes_temporelles_alpha_v0_1.md ;
  A4_Verdict_local_contraintes_temporelles_alpha_v0_1.md ;

α5 :
  A5_Fiche_variations_spatiales_cosmologiques_alpha_v0_1.md ;
  A5_Verdict_local_variations_spatiales_alpha_v0_1.md.
```

## 1. Question de synthèse

> Que devient l’énoncé « `alpha` est constante » lorsque l’on sépare la valeur de référence de basse énergie, la dépendance au transfert d’impulsion, les contraintes temporelles et les contraintes spatiales ou cosmologiques ?

## 2. Réponse courte

Il n’existe pas, dans le premier lot, un unique résultat scientifique pouvant être correctement résumé par « `alpha` est constante » ou « `alpha` varie ».

Le symbole `alpha` intervient dans quatre attributions distinctes :

```text
A. une valeur de référence de basse énergie
   est déterminée par plusieurs chaînes discordantes
   et rendue opérationnelle par un ajustement CODATA ;

B. le couplage effectif alpha(Q²)
   varie positivement avec l’échelle
   selon le running électromagnétique attendu ;

C. certaines variations temporelles
   — dérive linéaire lente et modulation annuelle liée au potentiel —
   ne sont pas détectées dans les domaines testés ;

D. une prétention spatiale historique
   est substantiellement repondérée par une systématique instrumentale,
   tandis qu’une ligne de visée mieux calibrée est compatible avec zéro ;
   le statut spatial global demeure suspendu.
```

La proposition correcte n’est donc pas un statut global de `alpha`, mais une famille d’attributions indexées :

```text
cible
+ transformation
+ accès
+ relation de passage
+ domaine
+ tolérance
+ mode de soutien probatoire.
```

## 3. Matrice consolidée

| Dossier | Cible analytique | Transformation | Observable ou accès premier | Résultat local | Rang probatoire | Limite principale |
|---|---|---|---|---|---|---|
| α2 | valeur de basse énergie et valeur recommandée | changement de chaîne, de données ou d’ajustement | `h/m(133Cs)`, `h/m(87Rb)`, `a_e` | trois déterminations comparables mais nominalement discordantes ; référence CODATA après expansion | mesures premières + inférences + ajustement métrologique | cause de la discordance inconnue ; aucune variation physique testée |
| α3 | couplage espace-like `alpha(Q²)` | transfert d’impulsion `Q²` | section efficace différentielle de Bhabha | running positivement observé ; `C=0` exclu localement ; `C=1` compatible | signal positif différentiel et ajustement paramétrique | dépendance au domaine, à `Delta alpha(Q²)` et aux calculs radiatifs |
| α4 | paramètres de variation temporelle | temps linéaire et potentiel solaire annuel | rapports de fréquences d’horloges | paramètres compatibles avec zéro | non-détection discriminante pour deux familles | autres spectres temporels, transitoires et formes non linéaires hors domaine |
| α5 | `Delta alpha/alpha` spatial ou cosmologique | direction, redshift, ligne de visée | spectres d’absorbeurs de quasars | prétention historique repondérée ; systématique instrumentale établie ; non-détection locale ESPRESSO | conflit d’accès + diagnostic instrumental + contrainte locale | aucun verdict spatial ou cosmologique global |

## 4. α2 — Valeur de référence de basse énergie

### 4.1 Ce qui est mesuré

```text
césium :
  recul atomique -> h/m(133Cs) ;

rubidium :
  recul atomique -> h/m(87Rb) ;

g−2 :
  fréquences cyclotron et d’anomalie -> a_e.
```

Aucune expérience ne mesure directement `alpha` comme observable première.

### 4.2 Ce qui est inféré

```text
voies de recul :
  h/m(X)
  + masses atomiques relatives
  + Ar(e)
  + R_inf
  -> alpha ;

voie g−2 :
  a_e(exp)
  + expression du modèle standard/QED
  + rapports de masses
  + contributions hadroniques et faibles
  -> alpha conditionnel.
```

### 4.3 Ce qui est ajusté

Les valeurs publiées du premier lot sont :

```text
césium :
  alpha^-1 = 137.035 999 046(27) ;

rubidium :
  alpha^-1 = 137.035 999 206(11) ;

g−2 :
  alpha^-1 = 137.035 999 166(15).
```

Le triplet n’est pas cohérent sous les seules incertitudes nominales. Les écarts descriptifs indicatifs sont :

```text
césium–rubidium : 5.49 sigma ;
césium–g−2 :      3.89 sigma ;
rubidium–g−2 :    2.15 sigma.
```

CODATA conserve les trois chaînes, applique un facteur d’expansion commun de `2.5` aux données D1–D6 et recommande :

```text
alpha^-1 = 137.035 999 177(21).
```

### 4.4 Verdict de rang

```text
admis :
  valeur recommandée comme sortie d’un ajustement global
  et référence numérique opérationnelle ;

refusé :
  mesure unique de alpha ;
  quatrième mesure indépendante ;
  résolution causale de la discordance ;
  variation physique déduite des écarts entre chaînes ;

suspendu :
  cause de la discordance ;
  chaîne éventuellement biaisée ;
  préférence scientifique définitive.
```

La stabilité de la référence n’est donc pas une propriété observée directement dans un objet isolé. Elle est produite par un réseau de mesures, de relations, de covariances et de décisions d’ajustement.

## 5. α3 — Dépendance à l’échelle

### 5.1 Transformation pertinente

```text
alpha(0)
≠
alpha(Q²).
```

La transformation n’est ni le temps ni la position, mais le transfert d’impulsion espace-like.

### 5.2 Résultat positif

L3 ajuste :

```text
alpha(Q²)
  = alpha(0) / [1 - C Delta alpha(Q²)] ;

C = 1.05 ± 0.07_stat ± 0.14_syst.
```

Dans le domaine :

```text
1800 GeV² < -Q² < 21600 GeV²,
```

le résultat est compatible avec `C=1` et l’hypothèse `C=0` est exclue dans la famille publiée. OPAL fournit un appui positif de même rang général dans un domaine espace-like inférieur.

### 5.3 Verdict de rang

```text
ce qui varie :
  le couplage effectif avec Q² ;

ce qui est maintenu :
  une relation de running compatible avec la QED ;

ce qui est refusé :
  maintien numérique de alpha(0) sous changement d’échelle ;
  variation temporelle déduite du running ;
  mesure absolue modèle-indépendante à chaque point ;

ce qui demeure suspendu :
  reproduction indépendante des générateurs ;
  séparation complète des contributions ;
  extension hors domaine et traduction inter-schémas.
```

La dépendance à l’échelle est ici le résultat physique positif attendu. La variation n’est pas l’échec d’une constance ; elle appartient à la définition opératoire du couplage renormalisé.

## 6. α4 — Contraintes temporelles

### 6.1 Ce qui est mesuré

Les horloges mesurent des fréquences et des rapports de fréquences. La variation de `alpha` est inférée par des coefficients de sensibilité atomique.

Le premier lot retient :

```text
rapport E3/E2 de 171Yb+ ;
fréquence E3 rapportée à des fontaines au césium ;
séries pluriannuelles ;
modèle de dérive linéaire ;
modèle de modulation annuelle avec le potentiel solaire.
```

### 6.2 Résultats

```text
(1/alpha) d alpha/dt
  = 1.0(1.1) × 10^-18 yr^-1 ;

(c²/alpha) d alpha/dPhi
  = 14(11) × 10^-9.
```

Les deux paramètres sont compatibles avec zéro.

### 6.3 Verdict de rang

```text
admis :
  absence de signal significatif
  pour une dérive linéaire lente
  et une modulation annuelle corrélée au potentiel ;

mode de soutien :
  non-détection discriminante ;

refusé :
  invariance temporelle universelle ;
  mesure directe de alpha par une horloge ;
  extension aux oscillations, transitoires
  et formes non testées ;

suspendu :
  variations non linéaires ;
  autres bandes de fréquence ;
  événements transitoires ;
  portée hors du domaine terrestre et de la période observée.
```

Le maintien temporel n’est attribuable qu’aux familles pour lesquelles le dispositif possède une sensibilité déclarée.

## 7. α5 — Contraintes spatiales et cosmologiques

### 7.1 Prétention positive historique

Webb et al. ont publié un ajustement dipolaire d’environ `4.1–4.2 sigma` à partir d’échantillons Keck/HIRES et VLT/UVES. Ce résultat demeure un fait historique de la chaîne d’analyse employée.

Il ne possède pas, à lui seul, le rang d’une variation physique indépendante de l’instrument.

### 7.2 Repondération instrumentale

Whitmore et Murphy ont établi des distorsions de longueur d’onde à longue portée, typiquement de l’ordre de :

```text
±200 m s^-1 par 1000 angströms,
```

capables de produire des biais de `Delta alpha/alpha` du bon ordre et de reproduire des aspects importants des résultats historiques.

Ces distorsions affaiblissent substantiellement l’attribution du motif à `alpha`, sans expliquer auto-cohéremment tous les résultats historiques.

### 7.3 Contrainte locale renforcée

ESPRESSO obtient sur l’absorbeur à `z=1.15` vers HE 0515−4414 :

```text
Delta alpha/alpha
  = 1.3 ± 1.3_stat ± 0.4_syst ppm.
```

La valeur est compatible avec zéro. Le peigne de fréquences laser réduit fortement la dette de calibration à longue portée ; les ambiguïtés de profil et de convergence demeurent.

### 7.4 Verdict de rang

```text
admis :
  prétention positive historique ;
  systématique instrumentale positivement établie ;
  affaiblissement substantiel de la preuve historique ;
  non-détection locale ESPRESSO discriminante ;

refusé :
  dipôle cosmologique physiquement établi ;
  explication instrumentale complète ;
  généralisation d’une ligne de visée ;
  invariance cosmologique universelle ;

suspendu :
  statut spatial global ;
  cause complète des résultats historiques ;
  cohérence de tous les échantillons ;
  modèle dipolaire actuel et portée hors domaine.
```

## 8. Résultats transversaux du dossier

### 8.1 Le symbole ne fixe pas la cible

Le même symbole `alpha` peut désigner :

```text
une valeur recommandée de basse énergie ;
un couplage effectif à une échelle donnée ;
un paramètre de dérive temporelle ;
un paramètre spatial ou cosmologique.
```

Ces cibles ne sont pas substituables.

### 8.2 La transformation fixe le sens de « variation »

```text
changement de chaîne :
  dispersion de déterminations ;

changement de Q² :
  running physique positif ;

changement temporel :
  paramètres de variation contraints ;

changement spatial ou cosmologique :
  attribution disputée et localement contrainte.
```

Aucune de ces variations ne doit être automatiquement transférée aux autres transformations.

### 8.3 Le maintien porte souvent sur une relation

Le dossier fait apparaître quatre formes de maintien :

```text
α2 :
  maintien d’une référence opérationnelle
  par ajustement malgré la discordance ;

α3 :
  maintien d’une relation de running
  tandis que la valeur du couplage varie ;

α4 :
  absence de paramètres temporels détectables
  pour deux familles sensibles ;

α5 :
  maintien local compatible avec zéro
  sur une ligne de visée mieux calibrée.
```

La notion de maintien n’implique donc pas toujours l’identité numérique d’une valeur.

### 8.4 L’accès peut déplacer l’attribution

α5 montre un cas particulièrement discriminant : une variation initialement attribuée à la cible devient partiellement réattribuable à la chaîne instrumentale lorsque la calibration acquiert une puissance discriminante nouvelle.

```text
absence initiale de diagnostic instrumental
≠
absence de systématique instrumentale.
```

Ce résultat prolonge réflexivement P27 : l’absence d’un incident documenté ne démontre pas que le dispositif antérieur pouvait rendre cet incident observable.

### 8.5 La précision ne fixe pas seule le rang

```text
une faible incertitude nominale
≠
une indépendance probatoire complète ;

une grande correction
≠
une correction erronée ;

une compatibilité avec zéro
≠
une invariance universelle ;

une signification statistique élevée
≠
une attribution physique indépendante de l’accès.
```

## 9. Réponse consolidée aux questions publiques

### Q1 — Comment les sciences établissent-elles et déplacent-elles la frontière entre variation et maintien ?

Le dossier `alpha` montre que cette frontière n’est pas tracée une fois pour toutes autour d’une grandeur. Elle est reconstruite pour chaque transformation.

```text
à basse énergie :
  la dispersion entre chaînes est distinguée
  d’une variation de la cible ;

avec Q² :
  la variation est admise comme comportement physique attendu ;

dans le temps :
  le maintien est soutenu seulement pour les familles
  qu’un dispositif sensible ne détecte pas ;

dans l’espace cosmologique :
  l’attribution change lorsque l’instrument
  révèle une transformation concurrente.
```

La frontière dépend donc conjointement de la cible, de la transformation et de la puissance discriminante de l’accès.

### Q2 — Par quelles structures le maintien devient-il opératoire et que change-t-il pour l’enquête ?

Le maintien devient opératoire par des architectures différentes :

```text
ajustement de chaînes et expansion d’incertitudes ;
relation de renormalisation et calcul radiatif ;
sensibilités atomiques et modèles temporels ;
calibration spectrale et modélisation d’absorbeurs.
```

Cela transforme l’enquête. La question pertinente n’est plus seulement :

```text
« alpha garde-t-elle la même valeur ? »
```

mais :

```text
« quelle cible est attribuée,
  sous quelle transformation,
  par quelle chaîne,
  avec quelle sensibilité,
  et qu’est-ce qui est réellement maintenu ? »
```

## 10. Verdict final proposé du dossier `alpha`

### 10.1 Admission

```text
admission :
  une valeur de basse énergie peut être rendue opérationnelle
  comme sortie ajustée et conditionnelle ;

  les trois chaînes α2 sont comparables
  mais nominalement discordantes et non équivalentes ;

  le running espace-like de alpha(Q²)
  est positivement soutenu dans les domaines étudiés ;

  une dérive temporelle linéaire lente
  et une modulation annuelle au potentiel solaire
  sont contraintes sans signal significatif ;

  une systématique spectrale majeure
  a substantiellement repondéré la prétention dipolaire historique ;

  ESPRESSO fournit une non-détection locale discriminante ;

  les différents résultats peuvent être articulés
  sans créer un nouveau statut transversal de constante.
```

### 10.2 Refus

```text
refus :
  un verdict global non indexé « alpha est constante » ;

  un verdict global non indexé « alpha varie » ;

  la mesure directe de alpha dans les quatre dossiers ;

  l’identité de alpha(0), alpha(Q²),
  d alpha/dt et Delta alpha/alpha cosmologique ;

  la transformation des écarts α2
  en variation physique ;

  le maintien numérique sous changement de Q² ;

  l’invariance temporelle ou spatiale universelle ;

  le dipôle cosmologique comme résultat physiquement établi ;

  la précision, la signification statistique
  ou la compatibilité avec zéro comme critères suffisants de rang ;

  la création d’une classe « constante effective stabilisée »
  ou d’un nouveau statut transversal pour résumer le dossier.
```

### 10.3 Suspension

```text
suspension :
  cause de la discordance entre les déterminations α2 ;

  suffisance définitive de tous les modèles
  expérimentaux, métrologiques et théoriques ;

  formes temporelles non testées ;

  statut global d’une variation spatiale ou cosmologique ;

  compatibilité complète entre tous les accès historiques ;

  portée hors des domaines, périodes, directions
  et schémas effectivement étudiés ;

  hiérarchie scientifique future après nouvelles mesures
  et prochain ajustement CODATA.
```

## 11. Conclusion scientifique proposée

Le dossier `alpha` ne confirme pas l’existence d’une catégorie générale de « constante stabilisée ». Il confirme la nécessité d’une lecture dynamique et indexée des attributions de constance.

```text
la valeur de référence est ajustée ;
le couplage est transporté entre échelles ;
les variations temporelles sont contraintes par familles ;
les variations spatiales sont attribuées à travers
une concurrence entre cible, instrument et modèle.
```

L’apport scientifique du dossier n’est donc pas de remplacer la constance par la variation. Il est de montrer que les sciences distribuent, selon les accès, ce qui doit être tenu pour variable, maintenu, ajusté, transporté, contraint ou suspendu.

## 12. Décisions soumises à validation humaine

La présente synthèse autorise à examiner séparément les décisions suivantes :

```text
D1 — valider le verdict final du dossier alpha ;

D2 — déclarer la séquence α1–α5 localement close ;

D3 — autoriser le passage de la PR #35 en Ready for review,
     puis sa fusion dans main après contrôle final ;

D4 — ouvrir ultérieurement une opération distincte
     de propagation bornée vers la synthèse active du cycle 1 ;

D5 — après intégration du dossier alpha,
     sélectionner entre m_e et m_p/m_e
     la prochaine dette scientifique du cycle 1.
```

Ces décisions ne doivent pas être confondues. La validation de D1 et D2 ne vaut pas automatiquement autorisation de D3 ou D4.