# T1.6 — Classification des écarts entre chaînes de détermination de `alpha_s` v0.1

Ce document classe les écarts du premier lot sans convertir leur description en
attribution causale générale.

## 0. Statut

```text
statut : résultat local clos de classification du premier lot T1 ;
date : 21 juillet 2026 ;
entrées : registre T1.1, fiches T1.2–T1.3, matrice T1.4 et reproduction T1.5 ;
fonction : attribuer un statut contrôlé aux écarts entre quatre chaînes ;
ne vaut pas : explication causale complète, moyenne mondiale, nouveau test de tension,
               reproduction des trois chaînes phénoménologiques ou verdict ontologique.
```

## 1. Règle de classification

Les écarts sont classés, non expliqués au-delà des preuves disponibles :

```text
isolé :
  une opération ou une entrée identifiée permet de rattacher l'écart
  à une cause déterminée dans le périmètre étudié ;

associé à plusieurs choix :
  plusieurs composantes documentées contribuent et ne peuvent être
  séparées quantitativement avec les matériaux présents ;

non identifiable :
  les données, covariances ou expériences contrefactuelles nécessaires
  ne sont pas disponibles.
```

Un écart reçoit un statut principal et, lorsque nécessaire, un sous-statut par
dimension. La comparabilité à une référence commune ne vaut ni équivalence des chaînes,
ni indépendance statistique. La différence est définie par `Delta(A,B) = A - B`.

## 2. Valeurs rapportées à la référence commune

| Chaîne | `alpha_s^(5)(m_Z)` | Incertitude conservée | Intervalle descriptif |
|---|---:|---|---:|
| tau — FESR | `0.1159` | `+/- 0.0014` | `[0.1145 ; 0.1173]` |
| NNPDF global | `0.1194` | `+0.0007 / -0.0014` | `[0.1180 ; 0.1201]` |
| formes d'événements | `0.1181` | expérimental `+0.0002 / -0.0005`; théorique `+0.0018 / -0.0021` | expérimental `[0.1176 ; 0.1183]`; théorique `[0.1160 ; 0.1199]` |
| lattice ALPHA | `0.118755` | `+/- 0.00058` | `[0.118175 ; 0.119335]` |

Ces intervalles reprennent séparément les présentations publiées. Ils ne sont pas
convertis en intervalles de confiance homogènes. En particulier, les composantes
expérimentale et théorique des formes d'événements ne sont ni symétrisées ni additionnées
ici.

## 3. Différences de valeurs centrales

| Comparaison | Différence centrale |
|---|---:|
| tau − lattice | `-0.002855` |
| tau − NNPDF | `-0.003500` |
| tau − formes d'événements | `-0.002200` |
| NNPDF − lattice | `+0.000645` |
| formes d'événements − lattice | `-0.000655` |
| NNPDF − formes d'événements | `+0.001300` |

Pour tau–lattice seulement, les deux erreurs finales sont symétriques. Sous l'hypothèse
descriptive d'indépendance :

```text
|0.1159 - 0.118755| / sqrt(0.0014^2 + 0.00058^2) = 1.884.
```

Il s'agit d'une **distance descriptive sous hypothèse d'indépendance**, et non d'un test
publiable de tension ni d'une preuve d'incompatibilité. Aucun nombre de sigmas n'est
calculé pour NNPDF ou les formes d'événements : il faudrait une prescription commune
pour l'asymétrie, la séparation expérimental/théorique et les corrélations inter-chaînes.

Lecture des seuls intervalles :

- tau ne recouvre ni l'intervalle NNPDF ni l'intervalle lattice à leur niveau publié ;
- tau ne recouvre pas la seule composante expérimentale des formes, mais recouvre leur
  excursion théorique publiée ;
- NNPDF, formes d'événements et lattice ont des intervalles descriptivement recouvrants.

Ces constats géométriques ne constituent pas des décisions de compatibilité statistique.

## 4. Écart interne à la chaîne lattice

Les deux routes reproduites vers `Lambda_MSbar^(3)` donnent :

```text
route directe : 347.139 +/- 11 MeV ;
route par découplage : 342.198 +/- 10 MeV ;
différence centrale : 4.941 MeV ;
corrélation reproduite : 0.330514 ;
chi^2 de la combinaison : 0.158409 ;
combinaison corrélée : 344.352 +/- 8.7 MeV.
```

```text
statut principal : isolé et traité à l'intérieur de la chaîne ;
opération isolée : comparaison puis combinaison de deux routes différentes ;
relation : routes partiellement corrélées ;
ne vaut pas : indépendance statistique, explication physique unique de la différence,
               validation des simulations ou des données condensées amont.
```

Cet écart interne est séparé des six écarts inter-chaînes : le pipeline le traite avec
la covariance reproduite, mais T1.5 ne refait pas les simulations lattice.

## 5. Classification des six comparaisons

| Comparaison | Statut principal | Sous-statuts et constat |
|---|---|---|
| tau–lattice | **associé à plusieurs choix** | cause unique **non identifiable** ; tension non établie ; distance descriptive `1.884` sous indépendance |
| tau–NNPDF | **associé à plusieurs choix** | objets statistiques et paramètres associés différents ; cause unique non identifiable ; anomalie physique non établie |
| tau–formes | **associé à plusieurs choix** | le recouvrement dépend de la composante théorique conservée séparément ; cause unique non identifiable ; anomalie physique non établie |
| NNPDF–lattice | **non identifiable** quant à la cause du faible écart | compatibilité descriptive oui ; explication causale non requise ; covariance inter-chaînes non établie ; tension non |
| formes–lattice | **non identifiable** quant à la cause du faible écart | compatibilité descriptive oui ; enveloppe théorique dominante du côté formes ; tension non |
| NNPDF–formes | **associé à plusieurs choix** | intervalles recouvrants ; PDF associées à NNPDF, `alpha_0` aux formes ; covariance croisée absente ; tension non établie |

### 5.1 Cas tau–lattice

Les dimensions documentées sont :

- données et normalisations tau, notamment les fractions de branchement du Heavy Flavor
  Averaging Group (HFLAV), face aux produits lattice condensés et à la fixation d'échelle ;
- covariances expérimentales des modes tau, face à la covariance des routes lattice ;
- poids des sommes de règles à énergie finie (FESR) et fenêtre en `s_0` ;
- développement en produits d'opérateurs (OPE), violations de dualité (DV) et
  prescription perturbative à ordre fixe (FOPT) ;
- troncature perturbative, puis évolutions et raccordements propres aux deux chaînes.

Dans la chaîne tau, `0.0092_stat` est la composante dominante du budget natif
`0.0101` : la limite principale appartient ici à la statistique et à la chaîne d'accès.
Le transport vers `m_Z` est annoncé comme apportant une incertitude additionnelle très
petite et n'est pas identifié comme cause dominante. La mise à jour HFLAV explique la
plus grande part du déplacement par rapport à l'analyse tau antérieure ; elle n'isole
pas la cause de l'écart tau–lattice.

### 5.2 Cas tau–NNPDF et tau–formes

Le spectre tau et ses moments FESR ne partagent ni l'observable, ni la fonction de coût,
ni les paramètres associés des fits globaux de distributions de partons (PDF) ou de
formes d'événements. Les décalages centraux sont donc associés à plusieurs choix
documentés, mais les expériences contrefactuelles nécessaires pour les séparer ne sont
pas disponibles. Aucune anomalie physique n'est établie.

### 5.3 Cas NNPDF–lattice, formes–lattice et NNPDF–formes

Les faibles écarts centraux sont descriptivement couverts par les intervalles publiés.
Pour les formes d'événements, l'enveloppe théorique domine la précision. Pour NNPDF, la
sortie reste corrélée aux PDF et son incertitude est asymétrique. L'absence de covariance
croisée interdit de transformer ces recouvrements en combinaison globale ; elle ne crée
pas pour autant une tension à expliquer.

## 6. Dimensions, chemins et portée

```text
dimension objet : même coefficient renormalisé à schéma, n_f et échelle fixés ;
dimension accès : spectres, données globales, distributions et produits lattice distincts ;
dimension constitution : évolution QCD et raccordements déclarés rendent la comparaison
                         opératoire sans rendre identiques les chaînes ;

chemin physique : relation de groupe de renormalisation entre échelles ;
chaînes expérimentales ou de réalisation : propres à chaque détermination ;
chemins inférentiels et computationnels : propres aux fits et au pipeline lattice ;
choix de représentation et de raccordement : conservés dans le dossier de preuve ;
variation temporelle : non testée et non pertinente ;
portée ontologique : non engagée.
```

## 7. Résultat de T1.6

```text
classification des écarts internes et inter-chaînes : accomplie ;
causalité complète : non revendiquée ;
reproduction des trois chaînes phénoménologiques : non requise pour reconnaître
                                                   les limites de l'attribution ;
moyenne mondiale : aucune ;
tension nouvelle : aucune déclarée ;
statut T1.6 : clos dans ce périmètre.
```

Les statuts `associé à plusieurs choix` et `non identifiable` sont des résultats
positifs de contrôle : ils fixent la limite de ce que les matériaux présents permettent
d'attribuer. Cette clôture autorise un projet de verdict local T1.7, sous relecture ;
elle n'ouvre pas T1.8.
