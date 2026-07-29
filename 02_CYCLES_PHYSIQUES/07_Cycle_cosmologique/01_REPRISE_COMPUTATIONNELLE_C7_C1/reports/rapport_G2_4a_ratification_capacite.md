# G2.4a — ratification humaine et addendum de capacité disque

Issue directrice : #63.

Base documentaire : `reports/rapport_G2_4a_specification_lancement.md`, commit
`156c27e8de6c1280eff13322958d9362dcb6da93`.

## 1. Ratification

Décision humaine d’Aksel reçue le 29 juillet 2026 : **D4-A à D4-H sont
ratifiées sans modification scientifique**.

```text
D4-A — architecture sans duplication des YAML : RATIFIÉE ;
D4-B — matrice de 32 chaînes et graines préassignées : RATIFIÉE ;
D4-C — sorties, manifestes et reprises hors Git : RATIFIÉE ;
D4-D — sampler G1, pré-vol et initialisations non informées : RATIFIÉE ;
D4-E — reconstruction des poids, burn-in et diagnostics : RATIFIÉE ;
D4-F — embargo d’interprétation : RATIFIÉE ;
D4-G — banc de performance et suspension en cas d’irréalisabilité : RATIFIÉE ;
D4-H — autorisation à deux clés avant production : RATIFIÉE.
```

Cette ratification autorise G2.4b, c’est-à-dire l’implémentation et la
qualification adversariale du lanceur. Elle n’autorise encore aucune chaîne
MCMC réelle.

## 2. Question de capacité disque

La règle arithmétique de premier ordre est correcte : 32 chaînes représentent
huit fois le nombre de chaînes d’un lot de quatre. Si un lot comparable de
quatre chaînes occupe 12 à 15 Go, l’extrapolation linéaire donne 96 à 120 Go.

Cette extrapolation n’est pas un plafond, car les modèles X(z) possèdent plus
de paramètres libres et peuvent exiger davantage d’états avant convergence.
Les fichiers de chaîne, sauvegardes de reprise, journaux et produits temporaires
peuvent donc porter le pic réel au-delà de la multiplication stricte par huit.

## 3. Complément obligatoire de G2.4b

Avant toute création du vrai manifeste d’autorisation, G2.4b devra mesurer et
publier, sans lire de valeur posterior :

```text
taille réelle des anciens répertoires G1 de quatre chaînes ;
taille moyenne, médiane et maximale par chaîne ;
nombre de lignes et largeur moyenne d’une ligne de chaîne ;
taille des fichiers de reprise, logs et métadonnées ;
espace libre sur le volume de C7C1_XZ_OUT_DIR ;
projection basse, centrale et haute pour les 32 chaînes ;
projection du pic temporaire avec reprises ;
```

Le pré-vol de production devra être auto-bloquant sur l’espace disque. La règle
numérique définitive sera gelée après ce banc, avant la première chaîne. La cible
de planification provisoire est :

```text
minimum prudent à préparer : 150 Go libres ;
cible confortable avant production : 200 Go libres ;
```

Ces valeurs sont des marges opérationnelles provisoires, non des mesures déjà
établies. Elles seront remplacées par la projection empirique de G2.4b.

## 4. Emplacement des sorties

`C7C1_XZ_OUT_DIR` doit rester hors Git. Pour la production active, un répertoire
local non synchronisé est préférable à un répertoire OneDrive ou Google Drive :
la synchronisation simultanée peut consommer de l’espace local, multiplier les
entrées-sorties et interférer avec les fichiers en cours d’écriture. Les espaces
cloud peuvent servir à l’archivage contrôlé après arrêt propre, checksums et
inventaire.

## 5. Statut

```text
G2.4a : RATIFIÉE ;
PR documentaire : fusionnable après audit ;
G2.4b : autorisable ;
première MCMC réelle : toujours FERMÉE ;
nettoyage immédiat de 120 Go : non exigé avant le banc de capacité ;
préparation de 150–200 Go libres : recommandée si disponible.
```
