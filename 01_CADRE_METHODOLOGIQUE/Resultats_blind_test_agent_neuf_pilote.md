# Résultats — blind test agent neuf, pilote Phase I

## Statut expérimental

Deux chats éphémères neufs ont reçu exactement la même consigne et un seul dossier chacun. Les réponses ont été conservées verbatim avant scoring.

Le scoring ci-dessous a été effectué avec `Grille_scoring_agent_neuf.csv`, gelée avant toute réponse. La révélation de la clé d'assignation est postérieure au gel des scores.

```text
N_PAR_CONDITION = 1
MAX_SCORE_PAR_AGENT = 48
ERREUR_CRITIQUE_D17 = 0
ERREUR_CRITIQUE_D61 = 0

SCORE_D17 = 42/48
SCORE_D61 = 42/48
```

## Scores par tâche

| Tâche | D17 | D61 | Maximum |
|---|---:|---:|---:|
| T1 — représentation intermédiaire | 8 | 8 | 12 |
| T2 — pratique répétée sans incident | 10 | 10 | 10 |
| T3 — résolution difficile | 9 | 10 | 10 |
| T4 — ancien audit / nouveau contexte | 9 | 8 | 10 |
| Global | 6 | 6 | 6 |
| **Total** | **42** | **42** | **48** |

Aucune erreur critique pré-enregistrée n'a été détectée.

## Différences qualitatives avant interprétation par condition

### D17

Points relativement meilleurs :
- rend un retour vers la reprise courante visible dans T1 ;
- dans T4, voit que la sélection d'entrée devient pertinente si l'audit est global.

Points relativement moins complets :
- T1 ne restitue pas explicitement les quatre catégories `conservé / perdu / ajouté / requalifié` ;
- T3 formule moins explicitement la condition de silence pour le correctif local trivial.

### D61

Points relativement meilleurs :
- T1 conserve explicitement les quatre catégories du contrôle du raccord ;
- T3 conserve explicitement la condition de silence pour erreur locale déterministe sans valeur de réutilisation.

Points relativement moins complets :
- T1 ne reconsolide pas explicitement l'état courant après la requalification ;
- T4 ne remonte pas jusqu'au contre-échantillon indépendant lorsque la portée deviendrait globale.

## Révélation de l'assignation

Pré-enregistrement :
- `Dossier_17` = organisation fonctionnelle dérivée du prototype 2D ;
- `Dossier_61` = fiches + relations.

Le pilote ne montre donc **aucun gain d'exactitude globale** de l'organisation fonctionnelle : les deux conditions obtiennent 42/48.

Il ne montre pas non plus de dégradation globale : l'organisation fonctionnelle est non inférieure sur ce pilote et ne produit aucune erreur critique.

## Charge documentaire

Volume des dossiers remis :
- D17 : 1065 mots ;
- D61 : 1482 mots.

D17 contient environ **28,1 % de mots en moins**.

Volume des réponses :
- réponse D17 : 963 mots ;
- réponse D61 : 986 mots.

La longueur de sortie est donc presque identique, malgré une entrée sensiblement plus courte pour D17.

Ce résultat soutient provisoirement une **efficacité documentaire** de l'organisation fonctionnelle : même score global et zéro erreur critique avec moins de matériau d'entrée. Il ne prouve pas encore un gain cognitif, un gain temporel ni une supériorité robuste entre agents.

## Verdict pilote

```text
EXACTITUDE_GLOBALE_D17_VS_D61 = EGALITE_42_48
ERREURS_CRITIQUES = 0_VS_0
NON_INFERIORITE_FONCTIONNELLE = SOUTENUE_DANS_CE_PILOTE
REDUCTION_VOLUME_ENTREE = ~28.1_POURCENT
GAIN_EXACTITUDE = NON_ETABLI
GAIN_EFFICACITE_DOCUMENTAIRE = CANDIDAT_SOUTENU
GAIN_AGENTIQUE_ROBUSTE = NON_ETABLI
SEDIMENTATION_DURABLE = NON
```

## Interprétation

Le premier blind test falsifie une version trop forte de l'hypothèse : le prototype n'améliore pas ici le score global par rapport aux fiches+relations.

Il soutient une version plus étroite : l'organisation fonctionnelle peut préserver le niveau de guidage global tout en comprimant substantiellement le dossier.

Le profil croisé des omissions est également informatif : l'organisation fonctionnelle semble favoriser la visibilité des transitions verticales et des retours, alors que les fiches semblent mieux conserver certains détails atomiques locaux. Ce contraste doit être reproduit avant d'être traité comme un effet stable.

## Suite expérimentale

Avant toute sédimentation, exécuter au moins une réplication supplémentaire par condition avec les fichiers gelés, sans les modifier. La série doit donc viser `n=2` par condition.

Si la direction se reproduit — scores proches/non inférieurs pour D17, zéro erreur critique, mais volume d'entrée inférieur — le résultat devient suffisamment intéressant pour ouvrir ensuite une Phase II écologique dans un dépôt contrôlé.

Si les réplications divergent fortement, la variabilité inter-agent devient le résultat principal et le prototype doit rester expérimental.
