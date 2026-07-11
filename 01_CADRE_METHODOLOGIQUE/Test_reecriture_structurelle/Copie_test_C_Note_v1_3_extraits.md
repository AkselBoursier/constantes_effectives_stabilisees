# COPIE DE TEST C - Note methodologique v1.3, extraits (reecriture structurelle)

## Statut de la copie

```text
copie de test produite pour Test_reecriture_structurelle_v0_1.md ;
source : 01_CADRE_METHODOLOGIQUE/Note_synthese_methodologique_v1_3_pre_familial_et_temporalite.md ;
extraits reecrits : sections 7, 12 et 16 ;
la source reste le document actif.
Genre teste : reference dense ; mesure principale : cout de longueur
et levee des ambiguites de portee.
```

### Extrait 7 - Statut des liaisons stabilisees (version test)

La critique principale est acceptee :

```text
toute constante engage des dependances d'une certaine maniere ;
une simple mise en rapport reste donc en deca d'une fonction
directrice.
```

Decision v1.3 :

```text
la liaison stabilisee devient famille fonctionnelle faible
apres le test de non-reduction, et par lui seulement.
```

Conditions d'usage :

```text
1. la liaison stabilisee est l'objet principal de la grandeur ;
2. elle excede la simple forme logique du rang 0 ;
3. elle se decrit mieux ainsi que comme role contextuel, fonction
   architecturale ou architecture.
```

Regle de rang :

```text
le classement par liaison requiert le test de non-reduction passe ;
la forme logique seule (rapport, ecart, composition, equation,
normalisation) reste au rang 0.
```

[source : "Interdit : classer une grandeur par liaison seulement
parce qu'elle est un rapport, un ecart, une composition, une equation,
ou une normalisation." La version positive est plus courte et fixe la
portee : c'est le rang 0 qui recueille ces formes.]

### Extrait 12 - Tensions de donnees (version test)

La v1.3 conserve la prudence de la v1.2 :

```text
Tension = propriete d'acces.
```

Et elle ajoute :

```text
une tension persistante peut devenir un signal actif pour tester la
validite d'une architecture.
```

Circuit de reclassification :

```text
la tension signale ;
le stress test documente ;
la decision reclasse.
Toute reclassification suit ce circuit, dans cet ordre.
```

[source : "aucune tension ne reclassifie automatiquement une
grandeur. Mais : une tension persistante oblige a documenter le
stress test correspondant." La version positive remplace l'interdit
et l'obligation par un circuit nomme ; longueur egale, ambiguite de
"automatiquement" levee.]

### Extrait 16 - Test de passage vers une famille fonctionnelle (version test)

Avant de transformer une fonction directrice en famille fonctionnelle,
poser huit questions.

```text
1. La categorie nomme-t-elle une fonction principale ?
2. Cette fonction est-elle irreductible a une forme logique ?
3. Est-elle irreductible a un role contextuel ?
4. Est-elle irreductible a une architecture ?
5. Peut-elle classer plusieurs cas heterogenes sans les ecraser ?
6. Peut-on donner un contre-exemple qui la ferait devenir fourre-tout ?
7. Que perd-on si on la supprime ?
8. Que gagne-t-on si on la retrograde ?
```

[controle : ce test est un protocole eliminatoire au coeur d'une
reference dense. Les questions 6 a 8 travaillent par contre-exemple,
perte et retrogradation : ce sont des operations du test, couvertes
par l'exception 2. Conservees telles quelles. La reecriture
structurelle laisse les protocoles eliminatoires intacts meme quand
ils sont enchasses dans un document de reference.]

### Bilan local de la copie C

```text
C1 tenu ; C4 favorable : deux extraits sur trois raccourcissent, le
troisieme reste identique parce qu'il est un protocole eliminatoire
enchasse.
Constat : dans une reference dense, la regle rapporte le plus la ou
la negation encadrait ; elle laisse intact ce qui teste.
```
