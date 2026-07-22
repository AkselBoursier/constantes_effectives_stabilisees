# T1.7 — Projet de verdict comparatif local sur `alpha_s` v0.1

Ce projet formule le résultat comparatif local autorisé par T1.6 et conserve ses limites
comme partie du verdict.

## 0. Statut

```text
statut : projet de verdict comparatif local soumis à relecture ;
date : 21 juillet 2026 ;
périmètre : premier lot tau, NNPDF, formes d'événements et lattice ALPHA 2026 ;
appui : classification descriptive T1.6 et reproduction aval lattice T1.5 bornée ;
ne vaut pas : test global de compatibilité, résultat physique commun aux quatre chaînes,
               preuve de cohérence de leurs extractions ou validation humaine finale ;
T1.8 : non ouvert ;
portée ontologique : non engagée.
```

Ce document propose un verdict comparatif local. Il ne modifie pas le cadre canonique,
ne crée aucune taxonomie, ne produit aucune moyenne mondiale et ne vaut pas validation
humaine finale.

## 1. Contrôle des quatre porteurs

| Porteur envisagé | Verdict local | Limite constitutive |
|---|---|---|
| **A. valeur `alpha_s^(n_f)(mu)`** | comparable seulement lorsque schéma, nombre de saveurs, échelle et convention sont fixés | la valeur varie avec l'échelle ; l'identité numérique entre régimes n'est pas le maintien testé |
| **B. trajectoire du groupe de renormalisation** | porte la relation de transformation entre échelles et changements de régime | c'est une relation physique d'évolution renormalisée, pas une histoire temporelle de l'objet |
| **C. observable physique d'extraction** | rend chaque détermination accessible dans son régime | spectre tau, données globales, formes d'événements et observables lattice diffèrent ; ce porteur n'est pas commun aux chaînes |
| **D. comparaison de plusieurs chaînes après transport commun** | objet construit permettant de comparer les sorties finales sous convention commune | ne constitue ni un porteur physique démontré du maintien ni un test global de cohérence des chaînes |

L'objet `D` n'absorbe pas `A`, `B` et `C`. Il organise la comparaison après conservation
de leurs différences d'objet, d'accès, de transformation et d'incertitude. Sa construction
ne démontre pas l'existence d'un maintien physique commun aux quatre chaînes.

## 2. Verdict central proposé

> Dans le premier lot, quatre déterminations publiées peuvent être rapportées à
> `alpha_s^(5)(m_Z)` dans un cadre conventionnel commun. Le corpus a reproduit le pipeline
> aval de la chaîne ALPHA et documenté les trois chaînes phénoménologiques, mais il ne
> dispose ni de leurs vraisemblances complètes ni des covariances croisées permettant un
> test global de compatibilité. Le résultat établi est donc la comparabilité conditionnelle
> et la non-équivalence des chaînes. Aucune incompatibilité globale n'est établie dans ce
> dossier, mais la cohérence physique commune de leurs extractions, évolutions et
> raccordements n'y est pas démontrée.

L'expression « aucune incompatibilité globale n'est établie » décrit une limite du dossier ;
elle ne constitue pas une preuve positive de compatibilité ou de cohérence.

## 3. Réponse locale à la première question publique

> Comment les sciences établissent-elles, utilisent-elles et déplacent-elles la frontière
> entre ce qui varie et ce qui tient ?

```text
varie :
  valeur du couplage avec l'échelle ;
  observable ;
  méthode d'extraction ;
  corrections ;
  schémas intermédiaires ;
  paramètres de nuisance ;

tient sous transformations déclarées :
  relations d'évolution utilisées dans chaque chaîne ;
  règles déclarées de matching ;
  définition commune à une référence donnée ;
  possibilité de rapporter les sorties à un même axe numérique sans rendre les chaînes
  équivalentes.
```

La frontière locale est reconstruite entre, d'une part, les valeurs et accès dépendant de
l'échelle et de la chaîne et, d'autre part, les relations déclarées qui permettent leur
transport et leur comparaison. Le présent lot établit cette opérabilité comparative, non
une cohérence physique générale des chaînes.

## 4. Réponse locale à la seconde question publique

> Par quelles structures, opérations et chemins de détermination un maintien devient-il
> opératoire ou affirmable dans un régime, et que change cette reconstruction pour
> l'enquête scientifique ?

La comparaison devient opératoire par la déclaration du schéma, de l'échelle, du nombre
de saveurs et de l'ordre perturbatif, puis par la séparation de trois opérations :

1. extraire un paramètre depuis une observable et une chaîne d'accès propres ;
2. transporter ce paramètre par le groupe de renormalisation ;
3. effectuer les raccordements déclarés lors des changements de régime.

Les covariances, paramètres associés et choix de représentation appartiennent au dossier
de preuve. Une valeur rapportée à une référence commune ne doit pas être confondue avec
une mesure commune. Cette reconstruction déplace l'enquête depuis la recherche d'une
valeur identique hors contexte vers le contrôle des transformations et des chaînes qui
rendent les résultats comparables. Elle n'autorise pas, avec les matériaux présents, à
conclure que ces chaînes valident ensemble un même résultat physique au-delà de leur
référence finale commune.

## 5. Rang et portée du résultat

```text
résultat physique établi :
  reproduction aval du pipeline ALPHA et accord interne corrélé de ses deux routes ;

résultat comparatif :
  mise sur une référence numérique commune et non-équivalence des quatre chaînes ;

résultat méthodologique / épistémique :
  limites d'attribution et impossibilité d'un verdict global avec les matériaux présents ;

résultat ontologique :
  non engagé ;

taxonomie nouvelle :
  aucune ;

variation temporelle :
  non testée et non pertinente ici.
```

Aucun résultat physique commun aux quatre chaînes n'est revendiqué. Le résultat physique
positif demeure interne à la reproduction ALPHA ; le résultat inter-chaînes est comparatif
et limité par l'absence de vraisemblances complètes et de covariances croisées.

## 6. Limites appariées à l'acquis

- La chaîne lattice a été reproduite à partir de produits condensés ; cet acquis établit
  la traçabilité du pipeline aval, sans refaire les simulations ni valider leur production
  amont.
- Les trois chaînes phénoménologiques ont été contrôlées dans leurs publications, mais
  non reproduites ; cela suffit à classifier les limites d'attribution, pas à reconstruire
  leurs vraisemblances.
- Aucune covariance inter-chaînes n'est disponible ; l'absence d'incompatibilité globale
  établie ne vaut pas cohérence démontrée ni combinaison statistique.
- La covariance intégrale `alpha_s`–OPE–DV de la chaîne tau n'est pas acquise ; le budget
  publié et la dominance statistique sont conservés sans factorisation supplémentaire.
- Les incertitudes asymétriques de NNPDF et les composantes séparées des formes
  d'événements restent sous leur forme publiée ; leur recouvrement n'est pas converti en
  nombre de sigmas.

## 7. Décision proposée pour relecture

```text
objet comparatif retenu : D, comparaison construite de chaînes hétérogènes après transport commun ;
appui transformationnel : B, relations du groupe de renormalisation ;
condition de comparaison : A fixé par schéma, n_f et échelle ;
diversité des accès : C conservée ;
statut du verdict : comparatif, local et révisable ;
résultat physique inter-chaînes : non établi ;
opération suivante autorisée : synchronisation de la PR 18 et revue du diff borné ;
T1.8 : reste fermé.
```
