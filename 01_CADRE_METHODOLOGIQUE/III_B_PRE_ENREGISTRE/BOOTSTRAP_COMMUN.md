# Bootstrap commun — Phase III-B

## Statut

Instruction expérimentale commune aux quatre chats III-B. Ce fichier impose l'ordre de reprise ; il ne constitue ni une autorité scientifique, ni une source de résultat.

```text
PHASE = III-B
MUTATION_DEPOT = INTERDITE
WEB_EXTERNE = INTERDIT_SAUF_SI_MISSION_LE_DEMANDE_EXPLICITEMENT
MEMOIRE_EXTERIEURE_DU_PROJET = NE_PAS_UTILISER_COMME_SOURCE
BRANCHE_AUDIT = VEHICULE_DU_PAQUET_SEULEMENT
```

## Ordre obligatoire avant tout travail substantiel

1. Lire **entièrement** le fichier de matrice assigné indiqué dans le message de lancement.
2. Ne pas commencer l'analyse du dépôt avant la fin de cette lecture.
3. Lire ensuite la mission indiquée dans le message de lancement.
4. Examiner seulement après cela les sources du dépôt nécessaires à la mission.
5. La matrice assignée est une **surface expérimentale de contrôle**. Elle dit comment contrôler le raisonnement ; elle ne prouve aucun fait scientifique, historique ou décisionnel du cas.
6. N'activer que les fonctions dont le déclencheur est matériellement établi par le cas. Une fonction voisine plausible mais non déclenchée doit rester silencieuse.
7. Retrouver vous-même dans les branches et surfaces autorisées par la mission les sources, décisions et autorités courantes nécessaires. Ne pas utiliser la branche d'audit, la PR #139 ou ses fichiers voisins comme raccourci documentaire hors des trois fichiers explicitement fournis pour ce paquet.
8. Si l'information nécessaire n'est pas retrouvée, écrire `NON_ETABLI` ou `INFORMATION_MANQUANTE` au lieu de compléter par plausibilité.
9. Ne créer, modifier, supprimer, déplacer, fusionner, commenter ou pousser aucun objet Git/GitHub.

## Format de sortie obligatoire

### A. Réponse principale

Texte destiné à un humain qui doit pouvoir comprendre :

- ce que vous avez établi ;
- ce que vous n'avez pas établi ;
- les dépendances qui changent réellement le verdict ;
- la décision ou qualification finale ;
- les conditions de réouverture lorsque pertinentes.

Le langage naturel porte le sens. Les codes, chemins et identifiants sont secondaires.

### B. Trace de contrôle compacte

Après la réponse principale seulement, fournir :

```text
MATRICE_LUE = OUI/NON
SOURCES_REELLEMENT_UTILISEES = ...
FONCTIONS_ACTIVEES = fait concret -> déclencheur -> fonction -> effet sur décision
FONCTIONS_VOISINES_LAISSEES_SILENCIEUSES = ...
INFORMATIONS_MANQUANTES_BLOQUANTES = ...
INFORMATIONS_MANQUANTES_NON_BLOQUANTES = ...
AUCUNE_MUTATION_EFFECTUEE = OUI/NON
```

Ne pas transformer cette trace en deuxième réponse argumentative.
