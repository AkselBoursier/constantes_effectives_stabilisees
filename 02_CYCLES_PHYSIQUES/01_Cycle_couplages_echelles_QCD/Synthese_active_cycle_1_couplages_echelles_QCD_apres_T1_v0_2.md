# Synthèse active du cycle 1 — couplages, échelles et chromodynamique quantique (QCD) après T1 v0.2

## 0. Statut

```text
statut : synthèse active du cycle 1 au 26 juillet 2026 ;
remplace pour l’usage courant : Synthese_recuperation_cycle_1_couplages_echelles_QCD_v0_1.md ;
conserve la v0.1 : comme état de récupération documentaire antérieur à T1 ;
base scientifique nouvelle : T1.1–T1.7, intégrés dans main ;
fonction : réunir les acquis récupérés et les résultats ratifiés de la reprise QCD–T1 ;
ne vaut pas : clôture générale du cycle, test global de compatibilité des déterminations
               de alpha_s, résultat physique commun aux quatre chaînes, extension
               automatique à alpha, m_e ou m_p/m_e, ou conclusion ontologique.
```

Cette synthèse est la sortie de l’opération T1.8. Elle propage de manière bornée les
résultats de T1.5–T1.7 sans rouvrir les calculs ni modifier le cadre canonique.

## 1. Statut du cycle après T1

```text
cycle 1 : scientifiquement rouvert et partiellement instruit ;
sous-dossier QCD–T1 : localement clos et validé ;
T1.8 : propagation documentaire bornée accomplie ;
alpha, m_e et m_p/m_e : dettes scientifiques distinctes encore ouvertes ;
portée inter-cycle : non engagée par cette synthèse.
```

La reprise T1 ne clôt pas le cycle dans son ensemble. Elle fournit un premier
sous-dossier scientifiquement instruit sur les chaînes de détermination de `alpha_s`.

## 2. Acquis récupéré conservé

Le résultat directeur du cycle demeure la dissociation suivante :

```text
stabilité dans le temps
≠ indépendance à l’échelle
≠ identité de régime
≠ simplicité théorique.
```

Les quatre ensembles du cycle restent hétérogènes :

| Ensemble | Fonction comparative |
|---|---|
| constante de structure fine `alpha` | distinguer valeur de référence, stabilité temporelle testée et couplage courant |
| masse de l’électron `m_e` | distinguer grandeur physique dans le régime électrofaible brisé et changements d’unités ou de régime |
| rapport proton–électron `m_p/m_e` | montrer qu’un rapport sans dimension peut relier des constitutions physiques différentes |
| `alpha_s(Q²)` et `Lambda_QCD` | rendre explicites dépendance d’échelle, schéma, processus, nombre de saveurs et changement de régime |

La typologie exploratoire initiale n’est pas restaurée. Le vocabulaire disciplinaire
local et les transformations effectivement testées restent premiers.

## 3. Périmètre exact de T1

T1 a comparé un premier lot de quatre déterminations publiées de `alpha_s` :

```text
chaîne tau ;
chaîne NNPDF globale ;
chaîne formes d’événements ;
chaîne lattice ALPHA 2026.
```

La reprise a distingué quatre cibles ou fonctions analytiques :

| Cible ou fonction | Rôle | Limite |
|---|---|---|
| valeur `alpha_s^(n_f)(mu)` | valeur comparable lorsque schéma, nombre de saveurs, échelle et convention sont fixés | elle dépend de l’échelle ; l’identité numérique entre régimes n’est pas le maintien testé |
| relation du groupe de renormalisation | transformation déclarée entre échelles et régimes | elle n’est pas une histoire temporelle du couplage |
| observable d’extraction | accès propre à chaque détermination | elle n’est pas commune aux quatre chaînes |
| comparaison après transport commun | objet construit permettant de comparer les sorties finales | elle n’est ni un porteur physique démontré ni un test global de cohérence |

La comparaison construite conserve les différences d’objet, d’accès, de transformation
et d’incertitude ; elle ne les absorbe pas.

## 4. Résultat physique et computationnel local

Le résultat physique positif établi reste interne à la chaîne ALPHA.

À partir des produits condensés distribués, le pipeline aval a reproduit à la précision
d’affichage de la publication :

| Sortie | Publiée | Reproduite |
|---|---:|---:|
| route directe, `Lambda_MSbar^(3)` | `347(11) MeV` | `347.139 ± 11 MeV` |
| route par découplage, `Lambda_MSbar^(3)` | `342(10) MeV` | `342.198 ± 10 MeV` |
| combinaison corrélée, `Lambda_MSbar^(3)` | `344.4(8.7) MeV` | `344.352 ± 8.7 MeV` |
| `alpha_s^(5)(m_Z)` | `0.11876(58)` | `0.118755 ± 0.00058` |

Mode de soutien probatoire :

```text
reproduction computationnelle aval
à partir des produits condensés fournis.
```

Cette reproduction ne constitue pas :

- une nouvelle génération de configurations lattice ;
- une production indépendante des données condensées ;
- une reconstruction complète des calculs amont ;
- une nouvelle mesure de `alpha_s` ;
- une validation générale de toutes les entrées du paquet.

## 5. Verdict comparatif local propagé

Les quatre sorties finales peuvent être rapportées à `alpha_s^(5)(m_Z)` sous une
convention commune sans que les chaînes deviennent équivalentes.

```text
admission :
  comparabilité conditionnelle des sorties finales
  sous une convention commune ;

refus :
  équivalence des quatre chaînes ;
  existence d’un porteur physique inter-chaînes
  démontré par la seule comparaison ;

suspension :
  compatibilité statistique globale ;
  cohérence physique commune des extractions,
  évolutions et raccordements.
```

Mode de soutien probatoire inter-chaînes :

```text
documentation des publications ;
transport vers une référence conventionnelle commune ;
comparaison structurelle des objets, transformations,
incertitudes et corrélations disponibles.
```

Limites probatoires :

```text
vraisemblances complètes absentes ;
covariances croisées absentes ;
trois chaînes phénoménologiques non reproduites.
```

L’énoncé « aucune incompatibilité globale n’est établie » décrit une limite du dossier.
Il ne constitue ni une preuve positive de compatibilité ni une cohérence physique commune.

## 6. Réponse locale à la première question publique

> Comment les sciences établissent-elles, utilisent-elles et déplacent-elles la frontière
> entre ce qui varie et ce qui tient ?

Dans le sous-dossier T1 :

```text
varient ou diffèrent selon la chaîne :
  valeur du couplage avec l’échelle ;
  observable ;
  méthode d’extraction ;
  corrections ;
  schémas intermédiaires ;
  paramètres associés et de nuisance ;

tiennent sous transformations déclarées :
  relations d’évolution utilisées ;
  règles de raccordement déclarées ;
  définition de la référence commune ;
  possibilité de rapporter les sorties au même axe numérique
  sans rendre les chaînes équivalentes.
```

La frontière locale se situe donc entre les valeurs et accès dépendant de l’échelle et
de la chaîne, d’une part, et les relations déclarées qui permettent le transport et la
comparaison, d’autre part.

## 7. Réponse locale à la seconde question publique

> Par quelles structures, opérations et chemins de détermination un maintien devient-il
> opératoire ou affirmable dans un régime, et que change cette reconstruction pour
> l’enquête scientifique ?

La comparaison devient opératoire par la déclaration du schéma, de l’échelle, du nombre
de saveurs et de l’ordre perturbatif, puis par la séparation de trois opérations :

1. extraire un paramètre depuis une observable et une chaîne d’accès propres ;
2. transporter ce paramètre par le groupe de renormalisation ;
3. effectuer les raccordements déclarés lors des changements de régime.

Les covariances, paramètres associés et choix de représentation appartiennent au dossier
de preuve. Une valeur rapportée à une référence commune n’est pas nécessairement une
mesure commune.

La reprise déplace ainsi l’enquête depuis la recherche d’une valeur identique hors
contexte vers le contrôle des transformations et des chaînes qui rendent les résultats
comparables.

## 8. Répartition des rangs

```text
résultat physique établi :
  reproduction aval du pipeline ALPHA
  et accord interne corrélé de ses deux routes ;

résultat comparatif :
  mise sur une référence numérique commune
  et non-équivalence des quatre chaînes ;

résultat méthodologique / épistémique :
  limites d’attribution et impossibilité d’un verdict global
  avec les matériaux présents ;

résultat physique commun aux quatre chaînes :
  non établi ;

portée ontologique :
  non engagée ;

nouvelle taxonomie :
  aucune.
```

## 9. Limites à conserver avec l’acquis

- La reproduction ALPHA commence aux produits condensés et ne refait pas les simulations.
- Les trois chaînes phénoménologiques sont documentées mais non reproduites.
- Aucune covariance inter-chaînes ne permet un test global ou une combinaison.
- Les formes d’incertitude publiées restent hétérogènes et ne sont pas converties en un
  nombre commun de sigmas.
- La variation temporelle de `alpha_s` n’est ni testée ni pertinente dans T1.
- Le verdict ne s’étend pas automatiquement à toutes les déterminations de `alpha_s`.
- Le verdict ne s’étend pas à `alpha`, `m_e` ou `m_p/m_e`.

## 10. Dettes restantes du cycle 1

### 10.1 `alpha`

- contrôler les valeurs de référence et les contraintes de variation à partir des sources
  primaires et des publications ultérieures ;
- séparer explicitement variation temporelle ou spatiale, dépendance en énergie et choix
de schéma ;
- décider si le cas nécessite une fiche active propre ou reste transversal.

### 10.2 `m_e`

- préciser la cible exacte des comparaisons et les transformations testées ;
- distinguer masse physique, masse courante, rapport dimensionless et changement d’unités ;
- relier la constitution électrofaible sans en déduire automatiquement un verdict de constance.

### 10.3 `m_p/m_e`

- préciser les accès expérimentaux et la cible effectivement contrainte ;
- distinguer la simplicité formelle du rapport et l’hétérogénéité de ses constitutions ;
- décrire les contributions à la masse du proton sans les réduire à la seule `Lambda_QCD`.

### 10.4 QCD après T1

- conserver les vraisemblances et covariances croisées comme dette nécessaire à un test
global futur ;
- ne rouvrir le premier lot qu’en présence de nouveaux matériaux modifiant le verdict ;
- ne propager vers une conclusion inter-cycle qu’après comparaison contrôlée avec d’autres
cas d’accès multiples.

## 11. Décision active après T1.8

```text
acquis du cycle :
  stabilité temporelle, dépendance d’échelle, identité de régime
  et simplicité théorique restent distinctes ;

acquis T1 :
  comparabilité conditionnelle des chaînes de alpha_s
  sous transformations déclarées ;

résultat physique positif :
  interne à la reproduction ALPHA ;

équivalence des chaînes :
  refusée ;

compatibilité globale et cohérence physique commune :
  suspendues ;

séquence locale QCD–T1 :
  close ;

cycle 1 dans son ensemble :
  ouvert et partiellement instruit ;

point d’entrée actif :
  présente synthèse v0.2 ;

état antérieur conservé :
  synthèse de récupération v0.1.
```
