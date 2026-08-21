# Mission III-B — Tâche M / qualification du prototype Human-First

## Base substantielle autorisée

Comparer :

- `main@c9deaf1fe86b742d9227f0385e975809f64dc9bd` ;
- la branche `test/human-first-reprise-blind-20260819`.

Vous pouvez consulter les issues et commentaires de `main` nécessaires pour reconstruire la genèse, les tests et leur statut courant, en particulier lorsque le routage du dépôt y conduit.

La branche d'audit qui transporte ce paquet n'est pas une source substantielle de la mission. Hors `BOOTSTRAP_COMMUN.md`, de votre matrice assignée et de ce fichier, n'utilisez pas les autres fichiers de cette branche ni la PR #139.

## Mission

La branche `test/human-first-reprise-blind-20260819` contient un prototype de correction Human-First produit après des essais de reprise.

Votre tâche est de déterminer **ce que cette branche mérite aujourd'hui**, compte tenu :

- du delta réel avec `main` ;
- de la fonction revendiquée par les modifications ;
- de la force probatoire réelle des essais qui les ont motivées ;
- des éventuelles requalifications ultérieures de ces essais ;
- des risques symétriques de sous-correction et de sur-correction ;
- du coût de maintenance d'une représentation d'état plus explicite ;
- des conditions d'arrêt et de réouverture.

Ne partez pas du principe que le prototype est bon parce qu'il existe, ni qu'il est invalide parce que ses premiers témoins seraient imparfaits. Reconstituez les preuves et leur rang.

## Décision demandée

Recommander **une seule opération bornée** parmi :

```text
RETESTER_INCHANGE
AMENDER_PUIS_RETESTER
ABANDONNER_OU_REDUCTION_FORTE
SUSPENDRE_NON_ETABLI
```

Expliquez quel fait matériel justifie cette décision, quel fait aurait pu conduire à l'alternative la plus proche, et ce qui ferait rouvrir la décision après le prochain test.

## Questions de contrôle

1. Quelles modifications exactes la branche apporte-t-elle à l'accueil racine et à l'accueil des cycles ?
2. Quelle erreur ou friction de reprise chaque ajout cherche-t-il à prévenir ?
3. Les tests disponibles établissent-ils réellement cette erreur dans un environnement suffisamment contrôlé ?
4. Une requalification ultérieure change-t-elle le statut d'une conclusion antérieure sans effacer l'observation initiale ?
5. Les ajouts risquent-ils de créer une surface périssable qui exige une resynchronisation permanente ?
6. Laisser `main` inchangé reproduirait-il un défaut déjà suffisamment observé ?
7. Une correction plus petite protégerait-elle la même fonction avec moins de coût ?
8. Quelle fonction voisine de la matrice pourrait sembler pertinente mais doit rester silencieuse ici ?

## Contraintes

- aucune modification de `main`, de la branche expérimentale, d'une issue ou d'une PR ;
- aucune recherche web externe ;
- aucun nouveau blind test dans cette réponse ;
- ne pas convertir une proposition historique en décision humaine sans preuve de ratification ;
- ne pas convertir une application favorable en règle testée ;
- ne pas confondre intelligibilité Human-First et fidélité de la représentation d'état ;
- si les preuves ne permettent pas de départager proprement, `SUSPENDRE_NON_ETABLI` est recevable.
