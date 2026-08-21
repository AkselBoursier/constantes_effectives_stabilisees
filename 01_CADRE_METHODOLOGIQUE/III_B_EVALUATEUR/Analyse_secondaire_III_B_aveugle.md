# Analyse secondaire III-B — avant révélation de la clé

## Statut

Cette analyse est produite après gel des quatre réponses brutes et du jugement Human-First primaire qualitatif de l'utilisateur, mais **avant révélation de la correspondance historique des conditions**.

Elle compare uniquement les réponses de même tâche. Aucun total global unique n'est calculé.

```text
CLE_HISTORIQUE = NON_REVELEE
HUMAN_FIRST_PRIMAIRE = GELE_QUALITATIF
HUMAN_FIRST_NUMERIQUE = NON_PROJETE
SCORING_SECONDAIRE = EFFECTUE
FLAGS_C1_C8B = AUCUN_DETECTE
TRACE_COMPACTE_R3 = ABSENTE
```

## 1. Profils secondaires

### Tâche M — réponses R1 et R3

| Famille | R1 | R3 |
|---|---:|---:|
| Profondeur E1-E7 | 28/28 | 28/28 |
| Systématicité S1-S4 | 15/16 | 16/16 |
| Probité P1-P5 | 19/20 | 18/20 |
| Méthodologie M1-M5 | 24/24 | 24/24 |
| Fonctionnel F1-F4 | 15/16 | 15/16 |
| Qualité méthodologique QM1-QM6 | 20/24 | 24/24 |

La différence décisive est concentrée sur `QM1` et `QM3`.

R1 reconstruit très bien le delta, les coûts de maintenance, la symétrie sous-correction/sur-correction et une correction plus petite. Son verdict `AMENDER_PUIS_RETESTER` est méthodologiquement défendable. Mais la réponse ne reconstruit pas explicitement le point probatoire crucial : requalification des environnements T0, puis ouverture de la branche expérimentale comme lot à retester. Elle ne différencie pas non plus clairement la force des quatre témoins T0. Son argumentation se déplace vers des objections ultérieures de maintenance et en fait le discriminant principal.

R3 reconstruit explicitement l'hétérogénéité des quatre environnements, le changement de rang de preuve, puis le fait que la branche a été ouverte **après** cette requalification. Elle en tire la conséquence probatoire attendue : le coût de la table est réel mais son bénéfice n'a pas encore été testé, et une correction plus petite n'est pas encore démontrée équivalente. Son verdict `RETESTER_INCHANGE` est donc mieux raccordé à la chronologie gelée de la tâche M.

R3 omet toutefois la trace compacte terminale exigée par le bootstrap. Cette omission est enregistrée comme défaut procédural, sans flag critique C1-C8B et sans annuler la qualité de sa réponse principale.

**Signal aveugle M : différence substantielle de reconstruction probatoire et divergence de verdict.** Ce signal satisfait a priori le critère pré-enregistré de réplication potentielle, sous réserve de l'interprétation après révélation de la clé.

## 2. Tâche S — réponses R2 et R4

| Famille | R2 | R4 |
|---|---:|---:|
| Profondeur E1-E7 | 28/28 | 28/28 |
| Systématicité S1-S4 | 14/16 | 15/16 |
| Probité P1-P5 | 19/20 | 20/20 |
| Méthodologie M1-M5 | 20/24 | 23/24 |
| Fonctionnel F1-F4 | 13/16 | 16/16 |
| Récupération canonique RC1-RC4 | 16/16 | 16/16 |
| Qualité scientifique QS1-QS6 | 24/24 | 24/24 |

Les deux réponses récupèrent correctement le noyau canonique utile au Cycle 10 et conservent les mêmes bornes scientifiques principales : phases 2-3 négatives mais locales, phase 4 phénoménologique, scan distinct de trajectoire et d'histoire physique, quasi-fixité distincte de constance acquise, dette microphysique non convertible en autorisation de calcul.

R4 se distingue surtout par la qualité de séparation entre sortie stockée, résultat calculatoire rapporté, trajectoire du toy model et résultat scientifique ; par une composition plus explicite des contrôles ; et par une meilleure explicitation des silences et des frontières d'autorisation. Le détail sur la prescription `phi²` est matériellement compatible avec le CSV : les lignes stockées respectent les filtres numériques au prix de valeurs initiales de `Gamma/H` énormes, tandis que le rapport précise que cette prescription n'est pas algébriquement exclue mais cesse d'être un candidat naturel dans le toy model.

R2 reste scientifiquement très solide. Son déficit relatif porte davantage sur la couche méthodologique/fonctionnelle : les fonctions voisines laissées silencieuses sont indiquées de manière générique et les arbitrages coût/proportionnalité sont moins développés.

Le jugement humain brut signale cependant une erreur ressentie dans la « deuxième » réponse sur deux questions, tout en indiquant ensuite une confusion partielle entre les réponses 3 et 4. Cette discordance **n'est pas effacée par le scoring secondaire**. Elle doit rester un point à réexaminer, soit comme erreur réelle non captée par la référence évaluateur, soit comme effet d'identification/ordre de lecture.

**Signal aveugle S : avantage méthodologique/fonctionnel modéré de R4, sans différence secondaire détectée sur récupération canonique ou qualité scientifique.**

## 3. Human-First : ce que le jugement brut ajoute que la grille ne capturait pas

Le retour humain primaire décrit :

- R1 et R2 comme bons mais légèrement moins convaincants ;
- R3 et R4 comme plus sévères, plus justes et plus fluides ;
- une sycophancie résiduelle ressentie en R1-R2, non ressentie en R3-R4 ;
- très peu de confusion historique/courant et pas d'effacement notable des négatifs ;
- un effet d'habituation du lecteur au fil des quatre réponses.

Deux conséquences méthodologiques :

1. **effet d'ordre humain** : la fluidité ressentie de R3-R4 est partiellement confondue par l'habituation à la structure et au vocabulaire ; une prochaine évaluation Human-First comparative devrait idéalement anonymiser et randomiser l'ordre de lecture ;
2. **dimension non prévue** : la grille Human-First ne possède pas d'axe explicite pour indépendance critique / sur-accommodation / sycophancie. Ce signal ne doit pas être ajouté rétroactivement au scoring III-B, mais il mérite d'être conservé comme candidat de révision future de l'instrument.

## 4. Réserve de validité écologique

Le point principal soulevé par l'utilisateur n'est pas un biais interne de ces quatre essais. Il concerne leur **domaine de validité**.

Les quatre missions testent un régime contrôlé :

```text
mission bornée
+ objet nommé
+ paquet explicite
+ déclencheur commun
+ absence de mutation
+ une seule tâche dominante
```

L'usage réel du dépôt peut présenter un régime différent :

```text
conversation longue agent-agent
+ changement de domaine non parfaitement annoncé
+ accumulation d'état
+ déplacement des autorités pertinentes
+ passage physique -> méthodologie -> infrastructure -> physique
+ risque de transport automatique de conclusions ou de règles
```

La bonne qualification est donc :

```text
PERFORMANCE_III_B_DANS_MISSIONS_BORNEES = SOUTENUE
ROBUSTESSE_AUX_TRANSITIONS_DE_DOMAINE = NON_ETABLIE_PAR_III_B
```

Ce n'est pas une raison pour invalider III-B. C'est une dette de **validité externe / transport**. Elle est particulièrement importante parce que les incidents récents rapportés se concentrent précisément dans les changements de régime, notamment vers l'infrastructure.

Un futur test écologique ne devrait pas simplement rendre les missions « plus vagues ». Il devrait isoler la transition elle-même : même agent, contexte accumulé, changement de type d'objet et d'autorité, puis mesure de la capacité à ré-instruire le nouveau domaine sans propager automatiquement les verdicts du précédent. Ce test n'est pas ouvert ici comme nouvelle expérience ; il est seulement identifié comme dette distincte.

## 5. Ce que les quatre essais permettent déjà de dire sans clé

1. Le dispositif expérimental commun produit quatre réponses globalement de haut niveau ; aucun flag critique C1-C8B n'a été détecté dans l'évaluation secondaire.
2. L'amélioration ressentie par rapport à des reprises antérieures est compatible avec le matériau présent, mais **III-B ne permet pas d'attribuer causalement cette amélioration à la PR #136** : les quatre essais actuels partagent la même base documentaire et ne constituent pas un pré/post contrôlé.
3. La paire S est substantiellement proche sur le résultat scientifique ; la différence se situe surtout dans l'explicitation fonctionnelle et méthodologique.
4. La paire M présente une divergence plus forte : même matériau, deux opérations différentes, avec avantage net de R3 sur la chronologie probatoire gelée.
5. La divergence M suffit à justifier qu'on n'interprète pas les deux représentations comme interchangeables sur la seule base de ces quatre réponses.
6. La réserve de validité écologique est indépendante de la comparaison 7A/9C : même la meilleure condition de III-B pourrait échouer lors d'un changement de domaine non borné.

## 6. État avant révélation

```text
REPONSES_BRUTES = 4/4_GELEES
JUGEMENT_HUMAIN_PRIMAIRE_QUALITATIF = GELE
SCORING_SECONDAIRE_AVEUGLE = EFFECTUE
CLE_7A_9C = NON_REVELEE
COMPARAISON_HISTORIQUE_D17_D61 = NON_EFFECTUEE
REPLICATION = SIGNAL_PRESENT_MAIS_NON_OUVERTE
VALIDITE_ECOLOGIQUE_TRANSITIONS = DETTE_IDENTIFIEE_NON_TESTEE
```
