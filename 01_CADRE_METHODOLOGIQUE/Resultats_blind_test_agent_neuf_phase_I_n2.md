# Résultats — réplication Phase I du blind test agent neuf

## Statut expérimental

Réplication exécutée avec la consigne, les dossiers et la grille de scoring inchangés.

Ordre d'exécution indiqué par l'expérimentateur : D61 puis D17, conformément au contrebalancement prévu.

Les réponses ont été conservées verbatim avant scoring.

## Scores de la réplication

| Condition | Score | Erreurs critiques |
|---|---:|---:|
| D17 — organisation fonctionnelle | **42/48** | **0** |
| D61 — fiches + relations | **40/48** | **0** |

Les deux conditions restent au-dessus du seuil qualitatif principal : aucune erreur critique pré-enregistrée.

## Comparaison avec le pilote initial

| Condition | Série 1 | Série 2 | Total | Moyenne |
|---|---:|---:|---:|---:|
| D17 — organisation fonctionnelle | 42/48 | 42/48 | **84/96** | **42/48** |
| D61 — fiches + relations | 42/48 | 40/48 | **82/96** | **41/48** |

Différence moyenne : **+1 point sur 48** en faveur de D17.

Cette différence est trop faible et l'effectif trop petit pour soutenir une supériorité générale. En revanche, la non-infériorité de D17 est reproduite deux fois : D17 n'est inférieur à D61 dans aucune des deux séries.

## Compression documentaire

Les dossiers sont inchangés :

- D17 : 1065 mots d'entrée ;
- D61 : 1482 mots d'entrée ;
- réduction D17 : environ **28,1 %**.

Réponses de réplication :

- D17-R2 : 1082 mots ;
- D61-R2 : 1020 mots.

La compression porte donc sur la **surface d'entrée**, pas sur une réduction systématique de la longueur de sortie.

## Profil des écarts — réplication

### D17-R2

Points perdus :
- T1 raccord source→sortie : 1/2, car l'agent ne restitue pas explicitement les quatre catégories `conservé/perdu/ajouté/requalifié` ;
- T1 contrôle de sélection global : 0/2 ;
- T1 reconsolidation de reprise : 1/2 ;
- T3 capture/outillage : 1/2 ;
- T3 silence/arrêt : 1/2.

Point notable : contrairement au premier D17, la réplication restitue explicitement le contre-échantillon indépendant pour un audit global en T4.

### D61-R2

Points perdus :
- T1 raccord source→sortie : 1/2 ;
- T1 contrôle de sélection global : 0/2 ;
- T1 reconsolidation de reprise : 0/2 ;
- T3 capture/outillage : 1/2 ;
- T4 contrôle indépendant si portée globale : 0/2.

Le profil montre que D61 conserve bien les distinctions atomiques principales, mais continue de perdre plus facilement certaines relations transversales ou retours de niveau.

## Convergence des deux séries

Ce qui est reproduit :

1. **Aucune erreur critique** dans les quatre réponses indépendantes.
2. D17 atteint **42/48 dans les deux séries**.
3. D17 le fait avec **28,1 % de matière d'entrée en moins**.
4. Les deux organisations permettent une très bonne reconstruction des quatre cas.
5. Le point faible récurrent des deux conditions est la visibilité de la passe indépendante/contre-échantillon lorsqu'une situation locale change de portée et devient globale.
6. D17 rend plus régulièrement visibles les changements de niveau et conditions de retour ; D61 expose davantage de détail atomique, sans que cet avantage se transforme en meilleur score moyen.

## Verdict après n=2 par condition

```text
N_PAR_CONDITION = 2
ERREURS_CRITIQUES = 0_DANS_LES_4_REPONSES

D17_TOTAL = 84/96
D61_TOTAL = 82/96

GAIN_EXACTITUDE_GLOBAL = NON_DEMONTRE
SUPERIORITE_D17 = NON_ETABLIE

NON_INFERIORITE_D17 = REPRODUITE_DANS_2_SERIES
COMPRESSION_ENTREE_D17 = ~28.1_POURCENT
GAIN_EFFICACITE_DOCUMENTAIRE = SOUTENU_PLUS_FORTEMENT

SIGNAL_RELATIONNEL_VERTICAL = SOUTENU
PERTE_DETAIL_ATOMIQUE_D17 = PRESENTE_MAIS_NON_CRITIQUE

PHASE_I = SUFFISAMMENT_INSTRUITE_POUR_OUVRIR_PHASE_II_ECOLOGIQUE
SEDIMENTATION_DURABLE = TOUJOURS_NON_ETABLIE
```

## Conséquence méthodologique

Il ne serait plus très informatif de répéter indéfiniment le même test fermé avec le même modèle et les mêmes quatre cas.

Le prochain discriminant doit changer le **régime d'usage**, pas la grille :
- accès à un dépôt contrôlé ;
- navigation réelle depuis un point d'entrée ;
- mêmes tâches fonctionnelles ou tâches homologues ;
- deux environnements Git issus du même SHA ;
- une seule organisation expérimentale visible par agent ;
- mesure des chemins réellement empruntés, sources consultées, faux raccords, retours et coût documentaire.

La Phase II doit donc tester l'**efficacité écologique** de l'organisation fonctionnelle, non refaire une troisième fois le test d'extraction fermée.
