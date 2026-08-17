# Synthèse active du cycle 1 — couplages, échelles et QCD après T1 et le dossier `alpha` v0.3

## 0. Statut

```text
statut : synthèse active du cycle 1 au 26 juillet 2026 ;
remplace pour l’usage courant :
  Synthese_active_cycle_1_couplages_echelles_QCD_apres_T1_v0_2.md ;
conserve la v0.2 : comme état actif antérieur à l’intégration du dossier alpha ;
base scientifique :
  T1.1–T1.8 ;
  dossier alpha, opérations α1–α5 ;
fonction : réunir les résultats ratifiés du cycle 1 sans recopier les dossiers locaux ;
ne vaut pas :
  clôture générale du cycle ;
  verdict global non indexé sur alpha ou alpha_s ;
  extension automatique à m_e ou m_p/m_e ;
  conclusion inter-cycle ou ontologique.
```

Cette synthèse est la sortie de l’opération D4. Elle propage de manière bornée les résultats validés du dossier `alpha`, conserve les acquis QCD–T1 et ferme la dette locale `alpha` sans rouvrir les calculs ni modifier le cadre canonique.

## 1. Statut du cycle après D4

```text
cycle 1 : ouvert et partiellement instruit ;
sous-dossier QCD–T1 : localement clos et validé ;
dossier alpha : localement clos, validé et intégré ;
T1.8 : propagation QCD accomplie ;
D4 : propagation alpha accomplie ;
m_e et m_p/m_e : dettes scientifiques distinctes encore ouvertes ;
test global futur de alpha_s : suspendu faute de matériaux suffisants ;
portée inter-cycle : non engagée.
```

## 2. Résultat directeur du cycle

Le cycle confirme la dissociation suivante :

```text
stabilité dans le temps
≠ dépendance à l’échelle
≠ identité de régime
≠ stabilité d’une valeur recommandée
≠ simplicité théorique.
```

Le symbole ou le nom disciplinaire ne fixe pas à lui seul la cible du test. Toute attribution doit être rapportée à une cible, une transformation, un accès, une relation de passage, un domaine et une tolérance.

## 3. Acquis QCD–T1 conservé

T1 a comparé quatre déterminations publiées de `alpha_s` : chaîne tau, chaîne NNPDF globale, formes d’événements et chaîne lattice ALPHA 2026.

### 3.1 Résultat physique et computationnel local

À partir des produits condensés distribués, le pipeline aval ALPHA a reproduit à la précision d’affichage :

| Sortie | Reproduite |
|---|---:|
| route directe, `Lambda_MSbar^(3)` | `347.139 ± 11 MeV` |
| route par découplage, `Lambda_MSbar^(3)` | `342.198 ± 10 MeV` |
| combinaison corrélée, `Lambda_MSbar^(3)` | `344.352 ± 8.7 MeV` |
| `alpha_s^(5)(m_Z)` | `0.118755 ± 0.00058` |

Mode de soutien : reproduction computationnelle aval à partir des produits condensés fournis. Les simulations, données amont et trois chaînes phénoménologiques n’ont pas été reproduites.

### 3.2 Verdict comparatif local

```text
admission :
  comparabilité conditionnelle des sorties finales
  sous une convention commune ;

refus :
  équivalence des quatre chaînes ;
  résultat physique inter-chaînes déduit de la seule comparaison ;

suspension :
  compatibilité statistique globale ;
  cohérence physique commune des extractions,
  évolutions et raccordements.
```

Une valeur rapportée à une référence commune n’est pas nécessairement une mesure commune.

## 4. Résultats du dossier `alpha` intégrés

Le dossier `alpha` sépare quatre cibles qui ne peuvent pas être résumées par un verdict unique « `alpha` est constante » ou « `alpha` varie ».

### 4.1 Valeur de référence de basse énergie

Trois chaînes produisent des déterminations comparables de `alpha^-1` :

```text
césium :   137.035 999 046(27) ;
rubidium : 137.035 999 206(11) ;
g−2 :      137.035 999 166(15).
```

Le triplet est nominalement discordant. CODATA conserve les chaînes, élargit les incertitudes du sous-ensemble pertinent par un facteur `2.5` et recommande :

```text
alpha^-1 = 137.035 999 177(21).
```

Rang : mesures premières hétérogènes, relations de passage, inférences conditionnelles et ajustement métrologique. La valeur recommandée est une référence opérationnelle, non une mesure unique, une quatrième détermination indépendante ou une preuve d’invariance physique.

### 4.2 Dépendance à l’échelle

La diffusion Bhabha L3 teste le couplage espace-like par :

```text
alpha(Q²) = alpha(0) / [1 - C Delta alpha(Q²)] ;
C = 1.05 ± 0.07_stat ± 0.14_syst.
```

Dans le domaine publié, `C=0` est exclu et `C=1` est compatible. Le résultat physique positif est le running avec `Q²`, non le maintien numérique de `alpha(0)` sous changement d’échelle.

### 4.3 Contraintes temporelles

Les comparaisons d’horloges contraignent :

```text
(1/alpha) d alpha/dt = 1.0(1.1) × 10^-18 yr^-1 ;
(c²/alpha) d alpha/dPhi = 14(11) × 10^-9.
```

Ces paramètres sont compatibles avec zéro. Le soutien est une non-détection discriminante pour une dérive linéaire lente et une modulation annuelle corrélée au potentiel solaire. Les formes non linéaires, oscillatoires, transitoires et les autres domaines restent hors portée.

### 4.4 Contraintes spatiales ou cosmologiques

La prétention dipolaire historique issue de Keck/HIRES et VLT/UVES demeure un résultat historique de sa chaîne. Les supercalibrations ont établi des distorsions de longueur d’onde à longue portée capables de reproduire des aspects importants des résultats et d’affaiblir substantiellement leur attribution à `alpha`, sans tout expliquer.

ESPRESSO obtient localement :

```text
Delta alpha/alpha = 1.3 ± 1.3_stat ± 0.4_syst ppm.
```

Cette non-détection locale est discriminante sur la ligne de visée étudiée. Elle ne soutient ni une invariance cosmologique universelle ni un verdict global sur le modèle dipolaire.

## 5. Résultats transversaux désormais actifs dans le cycle

### 5.1 Le symbole ne fixe pas la cible

`alpha` peut désigner une valeur recommandée, un couplage à une échelle, un paramètre de dérive ou un paramètre spatial. Ces cibles ne sont pas substituables.

### 5.2 La transformation fixe le sens de la variation

```text
changement de chaîne : dispersion de déterminations ;
changement de Q² : running physique positif ;
changement temporel : paramètres de variation contraints ;
changement spatial : attribution disputée et localement contrainte.
```

Aucun résultat ne se transfère automatiquement d’une transformation à une autre.

### 5.3 Le maintien peut porter sur une relation

```text
QCD–T1 : maintien des relations d’évolution et de raccordement ;
alpha basse énergie : maintien d’une référence opérationnelle par ajustement ;
alpha(Q²) : maintien d’une relation de running tandis que la valeur varie ;
temps : absence de paramètres détectables pour deux familles ;
espace : compatibilité locale avec zéro sous un accès renforcé.
```

La notion de maintien n’implique donc pas toujours une identité numérique.

### 5.4 L’accès peut déplacer l’attribution

Le dossier spatial montre qu’une variation initialement attribuée à la cible peut être partiellement réattribuée à l’instrument lorsqu’une calibration plus discriminante révèle une transformation concurrente.

```text
absence initiale de diagnostic instrumental
≠ absence de systématique instrumentale.
```

### 5.5 La précision ne fixe pas seule le rang

```text
faible incertitude nominale ≠ indépendance probatoire complète ;
grande correction ≠ correction erronée ;
compatibilité avec zéro ≠ invariance universelle ;
signification statistique élevée ≠ attribution physique indépendante de l’accès.
```

## 6. Réponse consolidée aux questions publiques

### Q1 — Frontière entre variation et maintien

La frontière est reconstruite pour chaque transformation :

- dans QCD, les valeurs et accès dépendent de l’échelle et de la chaîne, tandis que les relations d’évolution rendent le transport contrôlable ;
- à basse énergie, la dispersion entre chaînes est distinguée d’une variation de la cible ;
- avec `Q²`, la variation est admise comme comportement physique attendu ;
- dans le temps, le maintien n’est soutenu que pour les familles qu’un dispositif sensible ne détecte pas ;
- dans l’espace, l’attribution change lorsqu’un accès révèle une transformation instrumentale concurrente.

### Q2 — Structures qui rendent le maintien opératoire

Le maintien ou la comparabilité deviennent opératoires par des architectures différentes :

```text
groupe de renormalisation et raccordements ;
ajustement de chaînes et expansion d’incertitudes ;
calculs radiatifs ;
sensibilités atomiques et modèles temporels ;
calibration spectrale et modélisation d’absorbeurs.
```

L’enquête se déplace ainsi de « quelle valeur reste la même ? » vers « quelle cible est attribuée, sous quelle transformation, par quelle chaîne, avec quelle sensibilité, et qu’est-ce qui est effectivement maintenu ? »

## 7. Répartition des rangs

```text
résultats physiques positifs :
  reproduction aval ALPHA ;
  running espace-like de alpha(Q²) ;

résultats métrologiques et comparatifs :
  comparabilité conditionnelle des chaînes alpha_s ;
  référence CODATA issue de chaînes alpha discordantes ;

résultats négatifs discriminants :
  contraintes temporelles sur deux familles ;
  non-détection locale ESPRESSO ;

résultat instrumental :
  distorsions spectrales à longue portée établies ;

résultats méthodologiques / épistémiques :
  indexation des attributions ;
  non-équivalence des accès ;
  déplacement possible de l’attribution par l’accès ;

nouvelle taxonomie : aucune ;
portée ontologique : non engagée.
```

## 8. Limites conservées

- La reproduction ALPHA reste aval et dépend des produits condensés.
- Les vraisemblances et covariances inter-chaînes manquent pour un test global de `alpha_s`.
- La cause de la discordance entre les chaînes de basse énergie de `alpha` demeure inconnue.
- Les modèles expérimentaux, métrologiques et théoriques ne sont pas validés de manière définitive.
- Les contraintes temporelles ne portent pas sur toutes les formes de variation.
- Le statut spatial ou cosmologique global reste suspendu.
- Les verdicts ne s’étendent pas à `m_e`, `m_p/m_e` ou aux autres cycles.

## 9. Dettes restantes du cycle 1

### 9.1 `m_e`

- préciser la cible des comparaisons et les transformations effectivement testées ;
- distinguer masse physique, masse courante, rapports sans dimension et changements d’unités ;
- relier la constitution électrofaible sans déduire automatiquement un verdict de constance.

### 9.2 `m_p/m_e`

- préciser les accès expérimentaux et la cible effectivement contrainte ;
- distinguer simplicité formelle du rapport et hétérogénéité de ses constitutions ;
- décrire les contributions à la masse du proton sans les réduire à la seule `Lambda_QCD`.

### 9.3 QCD après T1

- conserver les vraisemblances et covariances croisées comme dette nécessaire à un test global futur ;
- ne rouvrir le premier lot qu’en présence de matériaux modifiant le verdict.

La dette `alpha` est close pour le premier lot. Elle ne sera rouverte qu’en présence de nouvelles mesures, d’un nouvel ajustement CODATA ou de matériaux modifiant substantiellement le verdict.

## 10. Granularité pour la suite

Le dossier `alpha` a servi de banc d’essai méthodologique à haute résolution. Sa structure ne devient pas un formulaire obligatoire.

```text
principe :
  réutiliser les distinctions déjà acquises par référence ;

subdiviser seulement si la subdivision change :
  le verdict ;
  le rang probatoire ;
  la cible attribuée ;
  ou la décision scientifique suivante ;

profondeur future :
  proportionnée à la dette et au gain discriminant.
```

Cette règle applique P28 : la rigueur doit protéger la recherche sans devenir un second projet qui la concurrence.

## 11. Décision active après D4

```text
acquis QCD–T1 : conservés ;
dossier alpha : validé, localement clos et propagé ;
dette alpha : close pour le premier lot ;
m_e et m_p/m_e : dettes ouvertes ;
test global alpha_s : suspendu faute de matériaux ;
cycle 1 : ouvert et partiellement instruit ;
point d’entrée actif : présente synthèse v0.3 ;
états antérieurs conservés : synthèses v0.2 et v0.1 ;
prochaine décision : D5, sélection entre m_e et m_p/m_e.
```