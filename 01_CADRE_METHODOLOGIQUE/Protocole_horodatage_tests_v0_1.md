# Protocole d'horodatage des tests v0.1

## L'anteriorite des predictions etablie par ancrage externe de l'empreinte

### 1. Fonction

```text
un test a predictions verrouillees ne vaut que si l'anteriorite des
predictions sur les donnees est opposable a un lecteur soupconneux.
L'auto-horodatage (commits, pushs, dates de fichiers, mail a soi)
est circulaire : qui controle le depot controle son temps.
La circularite se brise en faisant certifier l'empreinte (hash
SHA-256) du fichier de predictions par un tiers que l'auteur ne
controle pas ; le contenu ne quitte pas la machine, seule
l'empreinte voyage.
```

### 2. Sequence obligatoire

```text
1. redaction du protocole et des predictions, sans aucune
   acquisition ;
2. commit des predictions seules ; le redacteur signale
   "predictions commitees - ancrage" et attend ;
3. ancrage externe par l'auteur :
   - tests de travail : OpenTimestamps (opentimestamps.org),
     glisser le fichier, conserver la preuve .ots aux cotes du
     fichier dans le depot ;
   - tests destines a un manuscrit : registration OSF du texte des
     predictions (preregistration academique standard, lisible par
     les rapporteurs) ;
   le push GitHub reste utile comme synchronisation, non comme
   preuve ;
4. confirmation de l'ancrage par l'auteur ; alors seulement,
   acquisition, application, verdict ;
5. commit des resultats, push.

regle : aucune acquisition avant confirmation de l'ancrage.
```

### 3. Etat des tests anterieurs

```text
covariance CODATA : predictions commitees avant toute donnee
(sequence de commits, non opposable au sens du present protocole) ;
C5-1 (solaire) et C5-2 (stabilite) : predictions et resultats dans
le meme commit - anteriorite etablie par l'ordre de conversation
seulement. Notes d'horodatage ajoutees aux deux fiches.
Aucun test anterieur ne satisfait le critere d'ancrage externe ;
rien de retroactif ne peut y remedier, et leurs statuts le disent.
Le present protocole s'applique a tous les tests suivants,
re-executions comprises.
```
