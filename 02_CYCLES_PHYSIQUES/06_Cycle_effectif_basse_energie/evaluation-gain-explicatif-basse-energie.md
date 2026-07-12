# Évaluation du gain explicatif — cycle basse énergie

## Statut

Ce document clôt l’évaluation du cycle repris.

Documents associés :

- [architecture-relationnelle-basse-energie.md](architecture-relationnelle-basse-energie.md)
- [verification-physique-basse-energie.md](verification-physique-basse-energie.md)

## 1. Question d’évaluation

> La reprise permet-elle de montrer quelque chose de plus précis que l’énoncé général selon lequel une théorie effective vaut seulement à basse énergie ?

## 2. Résultat principal

```text
Cycle concluant, avec changement de statut conceptuel.
```

L’ancienne formule :

```text
architecture inter-familles de constantes effectives
```

est trop forte et trop ontologique.

La formule qui résiste est :

> Une architecture de validité organise une description par la séparation d’échelles, le choix de degrés de liberté, les symétries, le comptage en puissances, le raccordement, l’évolution des coefficients et l’estimation de l’erreur.

L’unité du cycle ne provient pas d’un même type d’objet constant. Elle provient d’une même discipline de description.

## 3. Trois opérations qui ne doivent pas être confondues

### 3.1 Réduction locale

Dans le cas de Fermi :

```text
médiateur lourd non résolu
-> développement du propagateur
-> opérateurs locaux
-> G_F et corrections contrôlées.
```

### 3.2 Changement de régime dynamique

Dans le cas QCD :

```text
flot du couplage
-> perte du contrôle perturbatif
-> degrés de liberté et méthodes adaptés.
```

### 3.3 Expansion hiérarchique

Dans le cas gravitationnel :

```text
petits rapports E/M_Pl ou faible courbure
-> suppression des opérateurs d’ordre supérieur
-> prédictions de basse énergie malgré une UV ouverte.
```

Ces opérations partagent une structure EFT, mais pas un mécanisme physique unique.

## 4. Pouvoir explicatif local

### 4.1 Cas de Fermi

Le cycle explique :

- pourquoi l’interaction paraît locale ;
- pourquoi `G_F` possède une dimension inverse d’énergie au carré ;
- pourquoi la première correction est contrôlée par `q²/M_W²` ;
- pourquoi l’approximation cesse d’être suffisante à l’échelle électrofaible.

Il ne fait pas que constater que `G_F` est stable.

### 4.2 Cas QCD

Le cycle explique :

- pourquoi une valeur unique de `alpha_s` est insuffisante ;
- pourquoi les déterminations doivent être transportées à une échelle commune ;
- pourquoi la basse énergie n’est pas nécessairement plus simple ;
- pourquoi `Lambda_MSbar` n’est pas une observable brute de confinement.

### 4.3 Cas gravitationnel

Le cycle explique :

- pourquoi la relativité générale peut être utilisée comme théorie quantique effective à basse énergie ;
- pourquoi certaines corrections sont universelles tandis que d’autres dépendent de coefficients locaux ;
- pourquoi l’absence de complétion UV connue n’annule pas toute prédictivité ;
- pourquoi `M_Pl` ne doit pas être transformée en seuil abrupt.

## 5. Ce que le cycle rend visible sur les constantes

Le cycle fournit une réponse différenciée :

| Objet | Statut après reprise |
|---|---|
| `G_F` | constante effective relative à un régime et à une normalisation |
| `M_W` | masse physique jouant aussi le rôle d’échelle de contrôle |
| `C_i(mu)` | coefficient dépendant de la base, du schéma et de l’échelle |
| `alpha_s(mu)` | couplage courant, refusé comme constante sous variation de `mu` |
| `Lambda_MSbar` | paramètre d’échelle d’une trajectoire RG dans un schéma |
| `G_N` | paramètre dimensionné du terme dominant gravitationnel |
| `M_Pl` | échelle construite organisant le comptage en puissances |

L’expression « constante effective » ne peut donc pas être appliquée uniformément à tous ces objets.

## 6. Contrefactuels et conditions de rupture

Le dossier produit des contrefactuels précis :

- sans la hiérarchie `q²/M_W²`, l’interaction locale de Fermi échoue ;
- sans running de QCD, la structure du changement de régime serait différente ;
- sous changement de base, les coefficients individuels changent mais l’amplitude reste ;
- sans petit rapport gravitationnel, le comptage en puissances perd son contrôle.

Ces contrefactuels donnent un pouvoir explicatif supérieur à une carte statique de grandeurs.

## 7. Réponse à la question de la fonction de fixité

La fonction de fixité est localement pertinente pour `G_F`, mais elle n’est pas le concept central du cycle.

Le résultat le plus général est :

```text
fixité d’un coefficient
<
contrôle d’une description.
```

Dans une EFT, un coefficient peut courir, changer de base ou être raccordé à un seuil tout en participant à une prédiction stable.

Le véritable invariant méthodologique est plutôt :

```text
l’indépendance de l’observable physique
sous les choix auxiliaires,
à l’ordre de précision considéré.
```

Les dépendances d’échelle, de schéma et de base des composantes doivent se compenser dans la prédiction physique.

## 8. Dégagement conceptuel

Le cycle conduit à une distinction nouvelle pour la refondation :

### Fixité de composante

Un coefficient ou paramètre est tenu fixe dans une convention donnée.

### Stabilité de prédiction

Une observable demeure inchangée, à l’ordre calculé, lorsque les dépendances auxiliaires sont correctement compensées.

### Validité de description

Une troncature possède une erreur contrôlée dans un domaine donné.

Ces trois niveaux ne doivent pas être assimilés.

> Une théorie effective peut produire une prédiction stable avec des coefficients qui ne sont pas constants sous l’échelle ou le changement de base.

## 9. Gain pédagogique

Le gain pédagogique est substantiel parce que le dossier remplace l’image :

```text
basse énergie = version simplifiée de la théorie fondamentale
```

par une description pluraliste :

```text
basse énergie faible : localité effective ;
basse énergie QCD : non-perturbatif ;
basse énergie gravitationnelle : suppression hiérarchique.
```

Il rend également visibles :

- le rôle du matching ;
- le running ;
- le mélange d’opérateurs ;
- la dépendance de base ;
- le comptage en puissances ;
- la condition de rupture.

## 10. Test de transférabilité

| Critère | Résultat |
|---|---|
| Deux chaînes auparavant confondues | oui : raccordement théorique et accès expérimental, plus running |
| Relations typées sans nouvelles familles | oui |
| Contrefactuels | oui |
| Distinction expliqué / inféré / paramétré | oui |
| Refus de certains qualificatifs de constante | oui : `alpha_s(mu)`, `C_i(mu)` isolé, `Lambda` sans schéma |
| Gain indépendant du vocabulaire interne | oui : EFT, power counting, matching et RG |

## 11. Conditions maintenues

Le cycle ne permet pas encore de conclure que toute science physique repose sur une architecture de validité de type EFT.

Il ne permet pas non plus :

- de confondre « émergent » et « effectif » ;
- de considérer toute dépendance d’échelle comme un flot RG ;
- de traiter toute simplification comme une intégration de modes lourds ;
- de déduire une ontologie des constantes depuis le seul formalisme EFT.

## 12. Décision

```text
Cycle effectif basse énergie : concluant.
Ancienne taxonomie : non restaurée.
Résultat conservé : architecture méthodologique de validité.
```

Le cycle confirme que la question « qu’est-ce qu’une constante ? » peut faire apparaître une distinction qui n’était pas suffisamment explicite dans la présentation antérieure :

```text
ce qui reste fixe dans une formule
≠
ce qui court sous renormalisation
≠
ce qui demeure invariant dans une observable
≠
ce qui rend une description valide.
```

## 13. Décision de transfert

Le cycle autorise le passage au cas métrologique SI.

Ce cas devra tester un contraste maximal :

```text
EFT : coefficients et validité dépendants du régime
SI  : valeurs numériques exactes par définition
```

Le but sera de déterminer si le même vocabulaire de fixité éclaire réellement les deux domaines ou s’il masque leur différence de nature.

## 14. Formule de clôture

> À basse énergie, le pouvoir explicatif ne vient pas de la constance des coefficients pris isolément. Il vient de la maîtrise des dépendances, de la hiérarchie des corrections et de la stabilité de la prédiction dans un domaine de validité explicite.
