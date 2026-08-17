# Audit de pré-fusion de la PR nº 14 v0.2

## 0. Statut

```text
date : 18 juillet 2026 ;
dépôt : privé ;
accès du connecteur GitHub : vérifié ;
branche : agent/contribution-q1-information-chemin ;
base : main ;
PR : ouverte, en brouillon, fusionnable ;
objet : actualiser le verdict après refus du squash et validation d'une réécriture ciblée.
```

Cette version remplace comme document directeur le verdict opérationnel de la v0.1.
La v0.1 reste conservée comme état de l'audit ayant mis en évidence le problème des
PDF dans l'histoire de travail.

## 1. Décisions validées

```text
visibilité du dépôt : privée ;
archives conversationnelles assainies : maintenues consultables ;
squash de la PR nº 14 : refusé ;
granularité des commits : à conserver ;
méthode : réécriture ciblée de la branche avec git-filter-repo ;
main : ne doit pas être réécrite ;
force-push : limité à la branche cumulative avec lease explicite ;
fusion : seulement après réécriture, table de correspondance et nouvel audit.
```

Le connecteur conserve les permissions d'administration, lecture et écriture sur le
dépôt privé. Le changement de visibilité n'interrompt donc pas le travail connecté.

## 2. Pourquoi la réécriture remplace le squash

Le squash préserverait l'état final du corpus mais réduirait l'histoire de la branche à
un seul commit dans `main`. Ce résultat est incompatible avec la fonction généalogique
du dépôt.

La réécriture ciblée retire seulement quatre chemins historiques correspondant aux deux
PDF avant et après le renommage du laboratoire. Elle conserve :

- l'ordre des commits ;
- leurs messages ;
- leurs auteurs et dates ;
- leur topologie ;
- leurs étapes scientifiques et documentaires ;
- le SHA de l'arbre final, qui doit rester identique.

Les SHA des commits affectés changent nécessairement. La correspondance doit être
conservée dans une table versionnée après la réécriture.

## 3. Réduction du risque par le passage en privé

Le dépôt privé n'est plus accessible aux visiteurs ordinaires. Cette mesure réduit
immédiatement l'exposition des anciens commits et des archives, mais elle ne retire pas
les objets de l'histoire Git.

Le nettoyage reste nécessaire avant fusion parce que :

```text
une fusion normale de l'histoire actuelle rendrait les commits porteurs des PDF
ancêtres de main ;
une réécriture ciblée permet de conserver l'histoire détaillée sans ces objets ;
les clones privés ou caches antérieurs ne sont pas annulés automatiquement.
```

Aucune garantie de purge absolue des anciennes vues serveur n'est revendiquée. Le régime
retenu est une réduction proportionnée : dépôt privé, branche réécrite, branche distante
ancienne remplacée, puis suppression ou archivage privé des anciens clones.

## 4. Protocole autoritatif

L'opération locale doit suivre sans simplification :

`01_CADRE_METHODOLOGIQUE/Protocole_recriture_historique_PDF_PR14_v0_1.md`

Ce protocole impose notamment :

- un bundle privé complet avant modification ;
- un clone temporaire hors OneDrive ;
- le filtrage de la seule branche cumulative ;
- la conservation des commits vides pour préserver le jalon de retrait ;
- l'identité stricte du SHA de l'arbre final avant et après filtrage ;
- l'identité du nombre de commits et de commits de fusion ;
- la comparaison de la séquence des dates, auteurs et messages ;
- la recherche d'objets interdits dans toute l'ascendance ;
- la table ancien SHA → nouveau SHA ;
- un push avec lease explicite de la seule branche.

## 5. État technique avant réécriture

```text
PDF dans l'arbre final : aucun ;
données suivies sous data_external : aucune ;
conflit avec main : aucun ;
audits structure, liens et encodage : réussis ;
assainissement conversationnel bloquant : réussi ;
compilation Python : réussie ;
test synthétique C2 : réussi ;
reproduction DESI DR2 : non accomplie, C2 reste ouverte.
```

Le dernier workflow renforcé avant la décision de réécriture réussit intégralement.

## 6. Conditions de reprise après réécriture

La réécriture n'est validée que si le rapport local établit :

```text
ancien arbre final = nouvel arbre final ;
ancien nombre de commits = nouveau nombre de commits ;
ancienne séquence sémantique = nouvelle séquence sémantique ;
aucun des deux noms de PDF n'est atteignable depuis la branche réécrite ;
aucune autre branche ou tag n'a été poussé de force ;
workflow GitHub renforcé = réussite.
```

Les sorties attendues sont :

```text
05_CARTES_ET_SYNTHESES/Mapping_SHA_recriture_PDF_PR14_2026-07-18.tsv
05_CARTES_ET_SYNTHESES/Rapport_recriture_historique_PDF_PR14_v0_1.md
```

## 7. Verdict actuel

```text
arbre final : recevable ;
dépôt privé et accès connecté : validés ;
méthode de préservation de l'histoire : validée ;
PR nº 14 : ne pas fusionner dans son histoire actuelle ;
prochaine opération : exécuter le protocole de réécriture dans un clone local temporaire ;
méthode de fusion après réussite : Create a merge commit recommandé ;
squash : abandonné.
```
