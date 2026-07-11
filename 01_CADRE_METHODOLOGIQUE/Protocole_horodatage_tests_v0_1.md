# Protocole d'horodatage des tests v0.1

## L'anteriorite des predictions etablie par pushs separes

### 1. Fonction

```text
un test a predictions verrouillees ne vaut que si l'anteriorite des
predictions sur les donnees est etablie publiquement. Un commit
local ne suffit pas ; un push separe donne l'horodatage opposable.
```

### 2. Sequence obligatoire

```text
1. redaction du protocole et des predictions, sans aucune
   acquisition ;
2. commit des predictions seules ; le redacteur signale : "predictions
   commitees - push" et attend ;
3. push par l'auteur : horodatage public des predictions ;
4. acquisition des donnees, application, verdict ;
5. commit des resultats, push.

regle : aucune acquisition avant confirmation du push de l'etape 3.
```

### 3. Etat des tests anterieurs

```text
covariance CODATA : predictions commitees avant toute donnee
(sequence de commits probante), pushs non intercales ;
C5-1 (solaire) et C5-2 (stabilite) : predictions et resultats dans
le meme commit - anteriorite etablie par l'ordre de conversation
seulement. Notes d'horodatage ajoutees aux deux fiches ; leur
valeur probante est reduite d'autant. Le present protocole
s'applique a tous les tests suivants, re-executions comprises.
```
