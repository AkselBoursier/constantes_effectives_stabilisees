# Pilote Q1 — Interférence et marquage des voies : cadrage v0.1

## Statut

```text
rang : troisième test de Q1 ;
objet : interféromètre à deux voies avec marqueur quantique ;
cible : contribution à des conversations existantes, non nouveauté physique.
```

## Question

> Que signifie qu’une indication de voie soit encodée, accessible, lue, enregistrée ou neutralisée par un autre choix de lecture, et quelles attributions chacune de ces situations autorise-t-elle ?

## Modèle minimal

Après corrélation avec un marqueur :

```text
|Psi> = (|0>|m0> + exp(i phi)|1>|m1>) / sqrt(2).
```

Dans le cas pur et équilibré :

```text
V = |<m0|m1>| ;
D² + V² <= 1.
```

`V` désigne la visibilité et `D` la distinguabilité. Ces relations sont établies ; elles ne constituent pas un résultat nouveau du projet.

## Configurations comparées

```text
A. m0 = m1 : cohérence complète et franges dans la distribution marginale ;
B. <m0|m1> = 0 : voies corrélées à des marqueurs orthogonaux,
   sans franges dans la distribution marginale du système ;
C. lecture dans la base {m0,m1} : attribution conditionnelle d’une voie ;
D. lecture dans une base complémentaire : deux sous-ensembles conditionnels,
   en frange et antifrange, dont la somme reste sans franges.
```

L’« effacement » ne modifie pas rétroactivement une détection. Il change la base de lecture du marqueur et le tri des corrélations rendues visibles.

## Opérations à distinguer

```text
séparer ; corréler ; rendre distinguable ; lire ; enregistrer ;
conditionner ; ignorer ; décohérer ; recombiner.
```

## Critère de contribution

Le test doit distinguer au minimum :

```text
indication encodée dans une corrélation ;
indication accessible par une mesure possible ;
indication effectivement lue ;
indication enregistrée et publiquement disponible ;
indication utilisée pour conditionner une attribution de voie.
```

Il échoue s’il répète seulement l’opposition générale entre connaissance de la voie et interférence.

## Sources directrices

- Wootters & Zurek (1979), complémentarité quantitative.
- Scully, Englert & Walther (1991), marquage quantique.
- Englert (1996), visibilité et distinguabilité.
- Dürr, Nonn & Rempe (1998), test expérimental de la complémentarité.
- Kim et al. (2000), effaceur quantique à choix retardé.

## Limites

Le test ne décide ni une trajectoire individuelle, ni une rétrocausalité, ni l’interprétation correcte de la mécanique quantique.