# Résultat du test minimal — réalisations du kilogramme 2019–2024 v0.1

## 0. Statut

```text
issue : #21 ;
statut : résultat métrologique local soumis à revue ;
date : 21 juillet 2026 ;
branche : agent/test-cycle-8-kilogramme-comparaisons ;
périmètre : comparaisons clés CCM.M-K8.2019, CCM.M-K8.2021 et CCM.M-K8.2024 ;
preuve : données KCDB reconstruites quantitativement par script ;
ne vaut pas : comparaison complète des budgets de chaque laboratoire, classement de
              performance, démonstration philosophique générale ou audit des expériences.
```

## 1. Question discriminante

Le cycle avait déjà établi :

```text
valeur numérique exacte de h
≠
réalisation sans incertitude.
```

Cette distinction est correcte mais insuffisamment discriminante. Le présent test demande :

> Après la fixation exacte de `h`, où réside effectivement la stabilité opérationnelle du
> kilogramme : dans chaque expérience de réalisation, dans leur simple accord numérique,
> ou dans une couche collective de comparaison et de consensus ?

Le cycle ne monte que si les comparaisons successives montrent un effet plus précis que la
persistance générale de l'incertitude.

---

## 2. Sources et données

Données normatives :

- KCDB, `CCM.M-K8.2019` : <https://www.bipm.org/kcdb/comparison?id=1341> ;
- KCDB, `CCM.M-K8.2021` : <https://www.bipm.org/kcdb/comparison?id=1773> ;
- KCDB, `CCM.M-K8.2024` : <https://www.bipm.org/kcdb/comparison?id=1940> ;
- BIPM, troisième valeur de consensus, mise en œuvre le 1er mars 2026 :
  <https://www.bipm.org/en/-/2025-02-24-third-consensus-value-of-the-kilogram-to-be-implemented-1> ;
- BIPM, rapport final `CCM.M-K8.2024` :
  <https://www.bipm.org/en/d/-ccm-m-k8-2024>.

Pour chaque participant, la KCDB fournit :

```text
D_i = x_i - x_R ;
U_i = incertitude élargie du degré d'équivalence, niveau de confiance 95 % ;
x_R = valeur de référence de la comparaison clé (KCRV).
```

Les valeurs sont exprimées en milligrammes pour une masse nominale de `1 kg`.

En 2024, CMS est conservé dans le fichier brut mais exclu des statistiques sur la KCRV,
comme dans la procédure officielle : CMS n'a pas contribué au calcul de cette valeur de
référence.

---

## 3. Reproductibilité du calcul

Le dossier contient :

```text
donnees_ccm_m_k8_2019_2024.csv ;
analyse_comparaisons_kilogramme.py ;
resultats_synthese_comparaisons.csv ;
resultats_reproductibilite_laboratoires.csv.
```

Commande :

```powershell
python analyse_comparaisons_kilogramme.py
```

Le script :

1. calcule la dispersion descriptive des `D_i` pour chaque comparaison ;
2. conserve séparément l'écart de la KCRV à l'ancienne définition du kilogramme ;
3. reconstruit l'incertitude-type `u_i` depuis l'incertitude élargie publiée ;
4. rapporte les laboratoires présents dans les trois comparaisons à la même référence
   historique, au moyen de `D_i + (x_R - x_IPK)` ;
5. ne produit aucun test de tendance ou classement faute de covariances inter-campagnes.

Pour un participant inclus dans la KCRV :

```text
U_i = 2 sqrt(u_i^2 - u_R^2).
```

La formule publiée pour un participant exclu du calcul de la KCRV utilise au contraire la
somme des variances. Cette différence est appliquée à CMS en 2024.

---

## 4. Résultats par comparaison

| Comparaison | Participants | Écart KCRV / ancienne définition | `u_R` | Étendue des `D_i` | Écart-type descriptif | Médiane de `|D_i|` |
|---|---:|---:|---:|---:|---:|---:|
| 2019 | 7 | `-18.8 µg` | `7.5 µg` | `93.0 µg` | `30.8 µg` | `15.0 µg` |
| 2021 | 9 | `-15.2 µg` | `7.4 µg` | `94.0 µg` | `29.2 µg` | `19.0 µg` |
| 2024 | 10, dont 9 dans la KCRV | `-10.7 µg` | `6.4 µg` | `60.6 µg` | `18.2 µg` | `10.7 µg` |

### 4.1 Resserrement descriptif

Entre 2019 et 2024 :

```text
étendue centrale : 93.0 -> 60.6 µg ;
écart-type descriptif : 30.8 -> 18.2 µg ;
incertitude-type de la KCRV : 7.5 -> 6.4 µg.
```

Le troisième lot est donc plus resserré autour de sa propre valeur de référence. Cette
conclusion reste descriptive : les participants ne sont pas strictement identiques, les
méthodes et modèles d'évaluation ont évolué, et les campagnes ne disposent pas ici d'une
matrice de covariance commune.

### 4.2 Accord non uniformément résolu

Le comptage `|D_i| <= U_i`, à partir des nombres arrondis de la KCDB, donne :

```text
2019 : 7 / 7 ;
2021 : 7 / 9 ;
2024 : 8 / 9 participants inclus dans la KCRV.
```

Ce comptage n'est pas substitué au test de cohérence officiel. Le rapport BIPM sur 2021
indique que le test du chi carré global passe, tout en signalant que les deux résultats de
plus petite incertitude ne sont pas en accord entre eux. Une compatibilité d'ensemble peut
donc coexister avec une difficulté localisée entre les réalisations les plus précises.

---

## 5. Reproductibilité descriptive des laboratoires communs

Pour les six laboratoires présents dans les trois comparaisons, les valeurs sont rapportées
à l'unité de masse maintenue selon l'ancienne définition :

| Laboratoire | 2019 | 2021 | 2024 | Étendue sur trois campagnes |
|---|---:|---:|---:|---:|
| BIPM | `+6.2 µg` | `-39.1 µg` | `-17.7 µg` | `45.3 µg` |
| NIM | `-30.8 µg` | `+2.0 µg` | `-32.2 µg` | `34.2 µg` |
| NIST | `-18.8 µg` | `-15.8 µg` | `-15.0 µg` | `3.8 µg` |
| NMIJ | `-16.8 µg` | `-8.6 µg` | `-21.4 µg` | `12.8 µg` |
| NRC | `-3.8 µg` | `+3.8 µg` | `+9.5 µg` | `13.3 µg` |
| PTB | `-39.8 µg` | `-46.3 µg` | `-18.5 µg` | `27.8 µg` |

Ces étendues ne sont pas des notes de performance. Elles combinent reproductibilité,
corrections, modifications instrumentales, réévaluations des modèles et corrélations non
disponibles dans le présent dossier.

Elles montrent néanmoins que :

```text
la reproductibilité inter-campagnes est hétérogène ;
une valeur centrale collective ne remplace pas le suivi de chaque chaîne ;
la stabilité d'un laboratoire et la précision déclarée sont deux coordonnées distinctes.
```

### 5.1 Évolution des incertitudes reconstruites

Quelques profils :

```text
BIPM : 49.1 -> 41.2 -> 36.1 µg ;
NIM  : 45.6 -> 40.6 -> 29.3 µg ;
NIST : 27.1 -> 26.6 -> 13.4 µg ;
NMIJ : 21.4 -> 23.4 -> 21.0 µg ;
NRC  : 11.7 -> 11.2 -> 11.8 µg ;
PTB  : 12.9 -> 14.2 -> 13.6 µg.
```

La précision progresse fortement pour certaines réalisations et reste stable pour d'autres.
Or les difficultés d'accord observées en 2021 concernaient précisément des résultats très
précis. Réduire l'incertitude individuelle ne suffit donc pas, à elle seule, à produire une
échelle internationale immédiatement substituable entre réalisations.

---

## 6. Déplacement de la référence collective

Les KCRV successives se situent à :

```text
2019 : 1 kg - 18.8 µg ;
2021 : 1 kg - 15.2 µg ;
2024 : 1 kg - 10.7 µg,
```

par rapport à l'unité maintenue selon l'ancienne définition.

La troisième valeur de consensus, mise en œuvre le 1er mars 2026, est fixée à :

```text
1 kg - 12 µg,
avec une incertitude-type maintenue à 20 µg.
```

Elle est calculée à partir des trois comparaisons et ne se réduit pas à la KCRV 2024. Elle
impose une correction de `-5 µg` aux valeurs précédemment traçables à la deuxième valeur de
consensus.

Ce déplacement est essentiel :

```text
h reste exactement fixé ;
les expériences évoluent ;
la référence collective est révisée ;
la continuité internationale est maintenue par une règle coordonnée de dissémination.
```

---

## 7. Réponse au discriminant

### Hypothèse insuffisante

```text
la stabilité opérationnelle du kilogramme réside directement dans la valeur exacte de h.
```

Cette hypothèse est refusée. `h` rend la définition possible mais ne sélectionne pas, à lui
seul, une réalisation individuelle immédiatement utilisable comme référence mondiale.

### Hypothèse également insuffisante

```text
la stabilité réside dans l'accord spontané de toutes les réalisations primaires.
```

Cette hypothèse est également refusée. L'accord s'améliore, mais le BIPM maintient la phase
de consensus jusqu'à ce que l'accord entre expériences soit jugé satisfaisant.

### Résultat local

> Dans la phase actuelle de mise en œuvre du kilogramme redéfini, la stabilité opérationnelle
> internationale réside dans une couche de consensus coordonnée : elle agrège des réalisations
> indépendantes, conserve leur désaccord et leurs incertitudes, produit une valeur de
> dissémination révisable et organise les corrections de l'échelle de masse.

Cette couche n'est :

```text
ni la constante h ;
ni une expérience particulière ;
ni une moyenne intemporelle ;
ni une suppression institutionnelle de l'incertitude.
```

Elle est une opération métrologique collective appuyée sur les expériences.

---

## 8. Statut du gain du cycle 8

```text
R1 — résultat métrologique local : établi descriptivement ;
M1 — résultat méthodologique local : proposé pour validation ;
P1 — proposition philosophique : non ouverte ;
T1 — thèse transversale : non engagée.
```

Le gain par rapport au corpus antérieur est précis :

```text
ancien acquis : définition exacte ≠ réalisation incertaine ;

nouvel acquis : la stabilité de dissémination est produite par une couche collective,
                périodiquement révisée, qui médie entre définition et réalisations.
```

Le cycle monte donc modestement : il ne devient pas une théorie générale de la mesure, mais
il acquiert un résultat local sur l'organisation effective de la comparabilité.

---

## 9. Limites

1. Les statistiques de dispersion sont descriptives et dépendent de la composition des lots.
2. Les covariances entre campagnes et entre réalisations ne sont pas disponibles dans le
   fichier de travail.
3. Les budgets détaillés et les corrections propres à chaque laboratoire ne sont pas audités.
4. La reconstruction de `u_i` utilise les formules KCDB et les nombres publiés arrondis.
5. L'écart à l'ancienne définition sert de référence historique commune ; il n'est pas une
   affirmation selon laquelle l'ancien prototype demeure la définition actuelle.
6. Le mécanisme de consensus du kilogramme n'est pas généralisé aux autres unités du SI.

---

## 10. Condition d'arrêt et suite

Le test #21 peut être clos après revue du calcul et du verdict local.

Une suite ne serait justifiée que par une question nouvelle, par exemple :

```text
le même type de couche collective apparaît-il dans la dissémination d'une autre unité ?
```

Cette question n'est pas ouverte automatiquement. Le présent résultat ne requiert ni nouvel
audit transversal, ni réécriture immédiate du cadre, ni extension philosophique.
