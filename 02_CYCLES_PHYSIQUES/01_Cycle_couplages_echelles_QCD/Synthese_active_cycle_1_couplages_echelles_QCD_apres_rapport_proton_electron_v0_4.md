# Synthèse active du cycle 1 — couplages, échelles et QCD après T1, `alpha` et `m_p/m_e` v0.4

## 0. Statut

```text
statut : synthèse active du cycle 1 au 26 juillet 2026 ;
remplace pour l’usage courant :
  Synthese_active_cycle_1_couplages_echelles_QCD_apres_alpha_v0_3.md ;
conserve la v0.3 : comme état actif antérieur à l’intégration de m_p/m_e ;
base scientifique :
  T1.1–T1.8 ;
  dossier alpha, opérations α1–α5 ;
  premier lot m_p/m_e, R1–R3 ;
fonction : réunir les résultats ratifiés du cycle 1 sans recopier les dossiers locaux ;
ne vaut pas :
  clôture générale du cycle ;
  verdict global non indexé sur alpha, alpha_s ou m_p/m_e ;
  clôture automatique de la dette autonome m_e ;
  conclusion inter-cycle ou ontologique.
```

Cette synthèse propage de manière bornée le premier lot validé `m_p/m_e`, conserve les acquis QCD–T1 et `alpha`, ferme la dette locale du rapport pour ce premier lot et requalifie la décision suivante sans modifier le cadre canonique.

## 1. Statut du cycle après la propagation de `m_p/m_e`

```text
cycle 1 : ouvert et largement instruit dans son premier périmètre ;
sous-dossier QCD–T1 : localement clos et validé ;
dossier alpha : localement clos, validé et propagé ;
premier lot m_p/m_e : localement clos, validé et propagé ;
dette autonome m_e : ouverte, mais sa nécessité doit être arbitrée ;
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
≠ simplicité théorique
≠ simplicité physique d’un rapport sans dimension.
```

Toute attribution doit être rapportée à une cible, une transformation, un accès, une relation de passage, un domaine et une tolérance. La constitution de la cible peut en outre limiter ce que l’accès permet d’expliquer.

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

## 4. Résultats du dossier `alpha` conservés

Le dossier `alpha` sépare une valeur de référence, un couplage dépendant de l’échelle, des paramètres temporels et des paramètres spatiaux.

### 4.1 Valeur de référence de basse énergie

```text
césium :   alpha^-1 = 137.035 999 046(27) ;
rubidium : alpha^-1 = 137.035 999 206(11) ;
g−2 :      alpha^-1 = 137.035 999 166(15).
```

Le triplet est nominalement discordant. CODATA conserve les chaînes, élargit les incertitudes du sous-ensemble pertinent par un facteur `2.5` et recommande :

```text
alpha^-1 = 137.035 999 177(21).
```

Cette valeur est une référence opérationnelle issue d’un ajustement, non une mesure unique ou une preuve d’invariance.

### 4.2 Dépendance à l’échelle

La diffusion Bhabha L3 soutient le running espace-like de `alpha(Q²)` dans son domaine publié. Le résultat positif est la dépendance à `Q²`, non le maintien numérique de `alpha(0)` sous changement d’échelle.

### 4.3 Contraintes temporelles

```text
(1/alpha) d alpha/dt = 1.0(1.1) × 10^-18 yr^-1 ;
(c²/alpha) d alpha/dPhi = 14(11) × 10^-9.
```

Ces paramètres sont compatibles avec zéro pour une dérive linéaire lente et une modulation annuelle corrélée au potentiel solaire. Les autres formes restent hors portée.

### 4.4 Contraintes spatiales ou cosmologiques

Les distorsions de longueur d’onde à longue portée repondèrent la prétention dipolaire historique. ESPRESSO obtient localement :

```text
Delta alpha/alpha = 1.3 ± 1.3_stat ± 0.4_syst ppm.
```

Cette non-détection locale ne soutient ni une invariance cosmologique universelle ni un verdict global sur le modèle dipolaire.

## 5. Résultats du premier lot `m_p/m_e` intégrés

Le premier lot distingue la détermination actuelle du rapport, les transformations testées et l’explication éventuelle de leur origine.

### 5.1 Valeur actuelle et chaînes de détermination

CODATA 2022 recommande :

```text
m_p/m_e = 1836.152 673 426(32).
```

Cette valeur est une sortie ajustée composite. Elle combine un réseau de rapports de fréquences cyclotron, la détermination de la masse électronique par résonance de spin d’un électron lié et facteur `g` théorique, des données spectroscopiques `HD+`, des constantes auxiliaires et leurs covariances.

Le résultat `H2+` publié en 2025 fournit une comparaison postérieure :

```text
[m_p/m_e]_H2+ = 1836.152 673 414(47).
```

Il est compatible avec CODATA 2022, mais reste une inférence spectroscopique conditionnelle à un calcul ab initio et à des constantes auxiliaires. CODATA, `HD+` et `H2+` ne constituent donc pas trois mesures directes et complètement indépendantes du rapport.

### 5.2 Accès à la variation

Trois transformations restent distinctes :

```text
dérive locale autour du présent ;
modulation annuelle corrélée au potentiel solaire ;
différence astrophysique finie entre une ligne de visée et le laboratoire actuel.
```

Les horloges donnent :

```text
(1/rho_pe) d rho_pe/dt = -8(36) × 10^-18 par an ;
(c²/rho_pe) d rho_pe/dPhi = 7(45) × 10^-8,
avec rho_pe := m_p/m_e.
```

Les deux paramètres sont compatibles avec zéro pour les familles déclarées.

Le méthanol à `z = 0.89` donne :

```text
Delta rho_pe/rho_pe = (-1.8 ± 1.2) × 10^-7 ;
|Delta rho_pe/rho_pe| < 3.6 × 10^-7 à 3 sigma.
```

L’analyse réattribue une part importante des déplacements à l’évolution du fond radio et à la structure du gaz absorbant.

`H2/HD` à `z ≃ 2.34` donne :

```text
Delta rho_pe/rho_pe = (19 ± 9_stat ± 5_sys) × 10^-6.
```

Le résultat reste inférieur à deux écarts-types lorsque les incertitudes sont combinées. Les distorsions spectrographiques et le modèle cinématique limitent son attribution.

Ces résultats ne doivent pas être moyennés : une dérive locale, une modulation imposée et une différence cosmologique finie ne testent pas la même fonction.

### 5.3 Constitution minimale

```text
m_p/m_e
=
[masse d’un état protonique principalement issue de la dynamique QCD]
/
[masse électronique du régime électrofaible brisé].
```

La masse protonique n’est ni la somme des masses des quarks de valence ni une réalisation exacte de `Lambda_QCD`. La masse totale est physique ; ses décompositions détaillées dépendent du schéma, de l’échelle et de la base d’opérateurs.

Dans le Modèle standard, `m_e = y_e v/sqrt(2)` exprime une relation structurelle après brisure électrofaible. La précision métrologique de `m_e` ne constitue pas une mesure directe du Yukawa électronique `y_e`.

Pour de petites variations :

```text
Delta rho_pe/rho_pe
=
Delta m_p/m_p - Delta m_e/m_e.
```

Cette identité ne fournit aucune attribution causale. Séparer une variation de `m_p`, une variation de `m_e` ou une cause commune exige un modèle supplémentaire et plusieurs observables indépendantes.

## 6. Résultats transversaux désormais actifs

### 6.1 Le symbole ou le rapport ne fixe pas la cible probatoire

Une notation compacte peut désigner une valeur ajustée, un couplage à une échelle, un paramètre de dérive, une différence spatiale ou un rapport de masses. La forme mathématique ne fixe ni l’observable première ni le rang de l’inférence.

### 6.2 La transformation fixe le sens de la variation

```text
changement de chaîne : dispersion de déterminations ;
changement de Q² : running physique positif ;
changement temporel : paramètres de variation contraints ;
changement spatial : attribution disputée et localement contrainte ;
changement du rapport m_p/m_e : différence relationnelle
                                sans attribution séparée des deux masses.
```

### 6.3 Le maintien peut porter sur une relation

```text
QCD–T1 : maintien des relations d’évolution et de raccordement ;
alpha basse énergie : maintien d’une référence opérationnelle par ajustement ;
alpha(Q²) : maintien d’une relation de running tandis que la valeur varie ;
m_p/m_e actuel : maintien d’une valeur ajustée dans un réseau composite ;
temps : absence de paramètres détectables pour des familles déclarées ;
espace : compatibilités locales avec zéro sous des accès bornés.
```

### 6.4 L’accès peut déplacer l’attribution

Les dossiers spatiaux de `alpha` et `m_p/m_e` montrent qu’un déplacement initialement disponible pour la cible peut être réattribué à l’instrument, au fond observé, à l’excitation ou à la structure cinématique lorsqu’un modèle plus discriminant rend ces transformations concurrentes visibles.

```text
absence initiale de diagnostic
≠ absence de transformation concurrente.
```

### 6.5 Sans dimension ne signifie pas physiquement simple

Le caractère sans dimension de `m_p/m_e` élimine la dépendance à un changement commun d’unité. Il n’élimine ni l’hétérogénéité de ses deux termes, ni la pluralité de leurs chaînes de détermination, ni la dépendance à des modèles pour expliquer une variation.

### 6.6 Déterminer, contraindre et expliquer restent distincts

```text
déterminer une valeur
≠ contraindre une transformation
≠ expliquer l’origine d’une transformation.
```

La précision ne suffit pas à franchir ces niveaux.

## 7. Réponse consolidée aux questions publiques

### Q1 — Frontière entre variation et maintien

La frontière est reconstruite pour chaque transformation :

- dans QCD, les valeurs dépendent de l’échelle et de la chaîne, tandis que les relations d’évolution rendent leur transport contrôlable ;
- à basse énergie, la dispersion entre chaînes est distinguée d’une variation de la cible ;
- avec `Q²`, la variation de `alpha` est admise comme comportement physique attendu ;
- dans le temps, le maintien n’est soutenu que pour les familles qu’un dispositif sensible ne détecte pas ;
- dans l’espace, l’attribution change lorsque l’accès révèle une transformation instrumentale ou astrophysique concurrente ;
- pour `m_p/m_e`, une contrainte sur le rapport ne sépare pas les transformations du proton et de l’électron.

### Q2 — Structures qui rendent le maintien opératoire

```text
groupe de renormalisation et raccordements ;
ajustements corrélés et expansion d’incertitudes ;
calculs radiatifs et facteurs g liés ;
spectroscopie moléculaire et calculs ab initio ;
coefficients de sensibilité atomiques ou moléculaires ;
modèles temporels, cinématiques et astrophysiques ;
calibrations instrumentales ;
modèles de constitution reliant QCD et secteur électrofaible.
```

L’enquête se déplace de « quelle valeur reste la même ? » vers « quelle cible est attribuée, sous quelle transformation, par quelle chaîne, avec quelle sensibilité, et quel modèle serait nécessaire pour expliquer ce qui est observé ? »

## 8. Répartition des rangs

```text
résultats physiques positifs :
  reproduction aval ALPHA ;
  running espace-like de alpha(Q²) ;

résultats métrologiques et comparatifs :
  comparabilité conditionnelle des chaînes alpha_s ;
  référence CODATA issue de chaînes alpha discordantes ;
  valeur CODATA de m_p/m_e comme sortie ajustée composite ;
  compatibilité du résultat H2+ 2025 avec cette référence ;

résultats négatifs discriminants :
  contraintes temporelles sur alpha et m_p/m_e ;
  non-détections locales par ESPRESSO et méthanol ;
  contrainte H2/HD compatible avec zéro au rang publié ;

résultats instrumentaux ou d’environnement :
  distorsions spectrales à longue portée ;
  évolution du fond radio et structure des absorbeurs ;

résultats méthodologiques / épistémiques :
  indexation des attributions ;
  non-équivalence des accès ;
  déplacement possible de l’attribution ;
  distinction détermination / contrainte / explication ;
  simplicité dimensionnelle ≠ simplicité physique ;

nouvelle taxonomie : aucune ;
portée ontologique : non engagée.
```

## 9. Limites conservées

- La reproduction ALPHA reste aval et dépend des produits condensés.
- Les vraisemblances et covariances inter-chaînes manquent pour un test global de `alpha_s`.
- La cause de la discordance entre les chaînes de basse énergie de `alpha` demeure inconnue.
- Les contraintes temporelles ne portent pas sur toutes les formes de variation.
- Les résultats astrophysiques restent locaux à leurs lignes de visée et à leurs modèles.
- La valeur CODATA de `m_p/m_e` n’est pas une observable première unique.
- Une variation éventuelle du rapport ne peut être attribuée séparément à `m_p` ou `m_e` sans modèle.
- Les décompositions de la masse protonique ne sont pas des ontologies uniques.
- La précision de `m_e` ne mesure pas directement `y_e`.
- La portée inter-cycle et ontologique reste non engagée.

## 10. Dettes restantes du cycle 1

### 10.1 Dette autonome `m_e`

R3 a instruit `m_e` au rang nécessaire pour interpréter le dénominateur du rapport. Il reste à décider si une instruction autonome apporterait un gain scientifique nouveau, notamment sur :

```text
masse physique et paramètres renormalisés ;
chaînes de détermination propres ;
relation au Yukawa électronique et au secteur de Higgs ;
transformations qui ne sont pas déjà contraintes par m_p/m_e ;
rattachement au cycle 1 ou au cycle Saveur–Higgs.
```

Cette dette reste ouverte, mais elle n’est plus présupposée comme prochaine instruction obligatoire.

### 10.2 QCD après T1

Les vraisemblances et covariances croisées restent nécessaires à un éventuel test global inter-chaînes de `alpha_s`. Ne pas rouvrir T1 sans matériaux modifiant le verdict.

Les dettes `alpha` et `m_p/m_e` sont closes pour leur premier lot. Elles ne seront rouvertes qu’en présence de nouvelles mesures, d’un nouvel ajustement ou de matériaux modifiant substantiellement leur verdict.

## 11. Granularité pour la suite

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

Le premier lot `m_p/m_e` confirme qu’une structure compacte R1–R3 suffit lorsque les distinctions héritées sont réutilisées plutôt que redémontrées.

## 12. Décision active après la propagation de `m_p/m_e`

```text
acquis QCD–T1 : conservés ;
dossier alpha : validé, localement clos et propagé ;
premier lot m_p/m_e : validé, localement clos et propagé ;
dettes alpha et m_p/m_e : closes pour leur premier lot ;
dette autonome m_e : ouverte, nécessité à arbitrer ;
test global alpha_s : suspendu faute de matériaux ;
cycle 1 : ouvert et largement instruit dans son premier périmètre ;
point d’entrée actif : présente synthèse v0.4 ;
états antérieurs conservés : synthèses v0.3, v0.2 et v0.1 ;
prochaine décision : arbitrer entre
  une instruction autonome de m_e,
  son déplacement vers Saveur–Higgs,
  ou la clôture/suspension du premier périmètre du cycle 1.
```
