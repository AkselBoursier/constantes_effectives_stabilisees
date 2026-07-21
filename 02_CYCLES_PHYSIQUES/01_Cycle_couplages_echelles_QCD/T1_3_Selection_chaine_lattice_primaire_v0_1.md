# T1.3 — Sélection de la chaîne lattice primaire v0.1

## 0. Statut

```text
statut : décision locale de sélection documentaire ;
date : 21 juillet 2026 ;
fonction : choisir la chaîne lattice primaire du premier lot T1 ;
ne vaut pas : validation indépendante du résultat, moyenne lattice ou préférence
               générale pour une méthode de détermination de alpha_s.
```

## 1. Choix retenu

La chaîne primaire retenue est :

Mattia Dalla Brida et al. (ALPHA Collaboration), « High-precision calculation of the
quark–gluon coupling from lattice QCD », *Nature* **652**, 328–334 (2026), publié le
8 avril 2026, DOI `10.1038/s41586-026-10339-4`.

```text
résultat : alpha_s^(n_f=5)(m_Z) = 0.11876(58) ;
quantité intermédiaire combinée : Lambda_MSbar^(3) = 344.4(8.7) MeV ;
méthodes internes : step scaling direct en QCD à trois saveurs et découplage vers
                    la théorie de jauge pure ;
statut : article primaire publié, ouvert, accompagné de données et code de réplication.
```

## 2. Motif de la sélection

Le cadrage initial envisageait une détermination primaire par step scaling ou par
découplage non perturbatif. L’article 2026 est plus instructif pour T1 parce qu’il réunit
ces deux routes sans les rendre identiques :

```text
route A : running non perturbatif direct en QCD N_f = 3 ;
route B : quarks lourds fictifs, limite de découplage et raccord à N_f = 0 ;
composante commune : fixation de l’échelle physique et échelle intermédiaire mu_dec ;
sortie commune : Lambda_MSbar^(3), puis matching vers alpha_s^(5)(m_Z).
```

Cette structure permet d’étudier à l’intérieur d’un même article :

- deux chemins computationnels et inférentiels distincts ;
- leur corrélation par des entrées communes ;
- la différence entre accord de méthodes et indépendance statistique ;
- la conversion d’une échelle QCD en coefficient de référence à `m_Z`.

## 3. Relation aux études antérieures

L’article ALPHA 2022 sur le découplage non perturbatif, qui donnait
`alpha_s(m_Z) = 0.11823(84)`, reste un antécédent direct. Il n’est pas retenu comme
chaîne principale parce que l’article 2026 :

1. emploie une détermination non perturbative du coefficient d’amélioration `b_g`,
   supprimant la systématique dominante de l’implémentation antérieure ;
2. ajoute des simulations plus fines et une analyse directe améliorée ;
3. combine explicitement les routes directe et découplage ;
4. publie un paquet de réplication réduit annoncé comme suffisant pour reproduire les
   analyses et nombres finaux.

La valeur 2022 ne doit pas être comparée à la valeur 2026 comme une mesure indépendante :
les deux travaux partagent des données, des échelles et une généalogie méthodologique.

## 4. Autorité et matériaux verrouillés

```text
version de référence : article Nature du 8 avril 2026 ;
supplément : informations supplémentaires liées à l’article ;
réplication : paquet public replication-package-2501.06633 ;
données : sous-dossier data au format BDIO ;
analyse : méthode Gamma et différentiation automatique ;
code de simulation : version modifiée d’openQCD 1.6, branche gbar-massive ;
code de reproduction : fourni dans le paquet de réplication.
```

Le numéro interne `2501.06633` du paquet de réplication est un identifiant de dépôt ; il
ne doit pas être interprété comme la référence arXiv de l’article.

## 5. Conséquence pour le protocole

```text
T1.3 sélection : close ;
T1.3 fiche primaire : à produire immédiatement ;
T1.4 matrice : autorisée après la fiche lattice ;
T1.5 reproduction : peut commencer par le paquet lattice, qui est le seul des quatre
                     dossiers à annoncer une réplication complète des nombres finaux.
```

La sélection est motivée par la contrôlabilité de la chaîne, non par la seule précision de
sa valeur finale.