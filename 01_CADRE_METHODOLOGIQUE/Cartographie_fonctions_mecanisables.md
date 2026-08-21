# Cartographie fonctionnelle des fonctions mécanisables

## Fonction

Cette cartographie vient **après** la matrice, les relations, la synthèse exécutive et le plan d’action de #139. Elle ne choisit encore aucun outil.

Son but est de déterminer, pour chaque fonction candidate, ce qu’une machine peut réellement observer et porter sans déplacer silencieusement une décision scientifique ou humaine vers l’infrastructure.

Chaque fonction est décrite par la chaîne :

```text
risque ou charge à protéger
→ propriété réellement observable
→ signal possible
→ action automatique admissible
→ autorité humaine résiduelle
```

Une fonction n’est pas mécanisable simplement parce qu’elle est répétitive. Elle doit posséder un observable suffisamment défini et un mécanisme dont les faux positifs/faux négatifs sont contrôlables.

## 1. Classes de mécanisation

```text
MECANISABLE_DIRECT
= propriété et action techniques suffisamment observables ;

MECANISABLE_PARTIEL
= la machine peut détecter/préparer mais pas qualifier le fond ;

ASSISTABLE_SEULEMENT
= la machine peut rassembler ou signaler, la décision reste interprétative ;

NON_MECANISABLE_COMME_VERDICT
= automatiser la sortie déplacerait un jugement scientifique/humain hors de son autorité.
```

## 2. F1 — Intégrité après écriture ambiguë

Sources : `R-021`, `R-038`.

**Risque protégé** : croire qu’une mutation a réussi ou échoué après une réponse 5xx, un timeout ou une réponse de persistance ambiguë.

**Observable machine** :

- code/réponse de l’écriture ;
- SHA ou contenu attendu avant l’opération ;
- SHA/contenu/ref effectivement lisible après l’opération.

**Signal** :

```text
WRITE_STATE = CONFIRME
WRITE_STATE = NON_EFFECTUE
WRITE_STATE = AMBIGU
WRITE_STATE = CONTRADICTOIRE
```

**Action automatique admissible** :

- read-back immédiat ;
- comparaison de l’état ;
- suspension des mutations suivantes si l’état reste ambigu/contradictoire ;
- journalisation de l’incident technique.

**Autorité humaine résiduelle** : décision de reprise lorsqu’une divergence de contenu ou une implication substantielle apparaît.

**Classe** : `MECANISABLE_DIRECT`.

**Test minimal** : simuler succès, erreur sans écriture, erreur après écriture, état contradictoire ; vérifier que le mécanisme ne suppose jamais le résultat de l’appel.

## 3. F2 — Pré-vol d’une mutation versionnée

Sources : `R-038`, partiellement `R-034`.

**Risque protégé** : agir sur un état obsolète, produire un no-op, viser la mauvaise branche ou répéter une mutation déjà refusée.

**Observable machine** :

- branche/ref cible ;
- SHA/blob courant ;
- existence du chemin ;
- différence entre état courant et contenu/action demandée ;
- résultat terminal de l’écriture.

**Signal** :

```text
PREFLIGHT = OK
PREFLIGHT = SHA_OBSOLETE
PREFLIGHT = PATH_MISMATCH
PREFLIGHT = NO_OP
PREFLIGHT = WRONG_TARGET_CLASS_DECLARED
```

Le dernier signal n’est disponible que si le type d’acte est déclaré explicitement ; la machine ne doit pas inventer la nature scientifique de l’acte.

**Action automatique admissible** : refuser l’écriture sur SHA obsolète, éviter no-op/diff vide, exiger read-back terminal.

**Autorité humaine résiduelle** : légitimité de la mutation, portée scientifique/documentaire et autorisation de merge.

**Classe** : `MECANISABLE_DIRECT` pour les invariants techniques ; `MECANISABLE_PARTIEL` pour la classe d’acte.

## 4. F3 — Séparer diagnostic et mutation destructive

Sources : `R-034`, `R-035`, contre-cas #117.

**Risque protégé** : transformer un diagnostic de redondance/déclassement en suppression, déplacement ou purge sans autorisation correspondante.

**Observable machine possible** :

- type d’opération déclaré : lecture, commentaire, modification, déplacement, suppression, purge ;
- présence d’un fichier dans un ensemble de dépendances mécaniques connues ;
- caractère destructif ou non de l’opération Git.

**Non-observable automatiquement** :

- contenu scientifique unique ;
- fonction probatoire ;
- perte sémantique ;
- adéquation de l’autorisation humaine si elle n’est pas structurée explicitement.

**Action automatique admissible** :

- avertir ou bloquer une action destructive lorsque la session/tâche est explicitement en lecture seule ou en diagnostic ;
- exiger un pré-vol sémantique déclaré avant delete/move/purge.

**Autorité humaine résiduelle** : toute décision destructive portant un contenu scientifique/probatoire ou un changement de portée.

**Classe** : `MECANISABLE_PARTIEL`.

## 5. F4 — Routage de contrôles par pertinence

Source : `R-022`, cas C2 #121–#123.

**Risque/charge protégée** : exécuter des contrôles coûteux qui ne peuvent pas être affectés par un changement, ou au contraire manquer un changement indirect pertinent.

**Observable machine** :

- fichiers/chemins modifiés ;
- dépendances explicites ;
- prédicat de déclenchement versionné ;
- résultats positifs et négatifs du routeur.

**Signal** : `RUN`, `SKIP_JUSTIFIE`, `ROUTE_AMBIGUE`.

**Action automatique admissible** : déclencher ou ignorer un contrôle technique spécifique.

**Autorité humaine résiduelle** : définition de la dépendance scientifique/fonctionnelle couverte par le prédicat ; décision qu’un skip est acceptable après changement d’architecture.

**Classe** : `MECANISABLE_DIRECT` dans un régime local qualifié ; généralisation seulement après test des dépendances indirectes.

## 6. F5 — Non-vacuité d’un contrôle

Sources : `R-003`, #82, #105–#107.

**Risque protégé** : un test paraît vert alors que le chemin censé exercer la propriété est inatteignable, court-circuité ou validé pour la mauvaise cause.

**Observable machine** selon le cas :

- branche/contrôle effectivement traversé ;
- cause exacte de l’exception ou du signal ;
- contrôle positif nominal ;
- groupe de fautes réellement exercé ;
- couverture de branches pertinente.

**Signal** :

```text
PROPERTY_EXERCISED = YES/NO/UNKNOWN
SUCCESS_CAUSE = EXPECTED/OTHER/UNKNOWN
```

**Action automatique admissible** : invalider une qualification technique si le contrôle n’exerce pas la propriété qu’il prétend tester.

**Autorité humaine résiduelle** : décider que la propriété exercée est scientifiquement suffisante pour le résultat revendiqué.

**Classe** : `MECANISABLE_PARTIEL`.

## 7. F6 — Sévérité alignée sur le risque protégé

Sources : `R-003`, #106/#107.

**Risque protégé** : traiter une dette connue comme invalidité globale, ou au contraire réduire un défaut bloquant à un simple message.

**Observable machine** : type de détection ; catégorie de risque déclarée ; mapping versionné `détection → sévérité`.

**Action automatique admissible** : code retour, warning, information ou blocage selon un contrat explicitement qualifié.

**Autorité humaine résiduelle** : définition initiale du risque protégé et changement de sévérité lorsqu’il modifie le gouvernement du dépôt.

**Classe** : `MECANISABLE_DIRECT` une fois le contrat humain établi.

## 8. F7 — Détection de contradiction de point d’entrée

Sources : `R-004`, `R-005`, `R-008`.

**Risque protégé** : un README/ancrage affiche un état courant explicitement incompatible avec l’issue ou la décision vers laquelle il route.

**Observables potentiels** :

- liens vers issue/PR ;
- état open/closed ;
- références de branche/numéro ;
- marqueurs structurés simples (`ACTIF`, `SUSPENDU`, etc.) lorsqu’ils existent.

**Non-observable de façon générale** : la signification intellectuelle du « courant » ou la validité scientifique du contenu.

**Action automatique admissible** : signaler une contradiction structurelle ou un lien mort ; ne pas réécrire automatiquement la synthèse scientifique.

**Autorité humaine résiduelle** : requalification de l’état et contenu du document vivant.

**Classe** : `ASSISTABLE_SEULEMENT` à `MECANISABLE_PARTIEL` selon la structure disponible.

## 9. F8 — Provenance matérielle et ratification

Source : `R-033`.

**Risque protégé** : confondre auteur apparent, provenance textuelle, autorité normative et intervention humaine réelle.

**Observable machine** :

- acteur GitHub apparent ;
- date, commit, issue, PR ;
- canal de création ;
- liens entre décision et matérialisation lorsque structurés.

**Non-observable automatiquement dans le régime actuel** : déterminer qu’un commentaire sous le compte auteur a été écrit directement par l’humain plutôt que par un agent connecté.

**Action automatique admissible** : conserver la provenance disponible et signaler `RATIFICATION_HUMAINE_NON_ETABLIE` lorsque la preuve requise manque.

**Autorité humaine résiduelle** : confirmer une décision humaine à forte autorité.

**Classe** : `ASSISTABLE_SEULEMENT`.

## 10. F9 — Représentation de la science vivante

Sources : `R-009`, `R-023`, `R-037`.

**Risque protégé** : réduire l’état scientifique aux résultats qualifiés et perdre recherches actives, dormantes, suspendues, négatifs, blocages et conditions de reprise.

**Observables partiels** : états GitHub, liens, dates, issues ouvertes/fermées, marqueurs explicitement structurés.

**Non-observable automatiquement** : priorité scientifique, effet attendu, validité d’une condition de reprise, statut scientifique d’un résultat.

**Action automatique admissible** : agréger des pointeurs et signaler des incohérences structurelles ; ne jamais attribuer automatiquement `prioritaire`, `qualifié`, `réouvert` ou `clos scientifiquement`.

**Autorité humaine résiduelle** : état scientifique, priorité et décisions programmatiques.

**Classe** : `ASSISTABLE_SEULEMENT`.

## 11. F10 — Conservation des négatifs sans accumulation brute

Source : `R-037`.

**Risque protégé** : perdre un négatif discriminant ou, inversement, transformer tout incident technique en dette durable.

**Observable machine** : présence d’un statut/refus explicite, lien vers résultat ou décision, réutilisation éventuelle.

**Non-observable automatiquement** : valeur discriminante future et rang scientifique.

**Action automatique admissible** : faciliter l’indexation/recherche et détecter une référence cassée.

**Autorité humaine résiduelle** : décider si le négatif mérite conservation active, archivage ou sortie de la surface de reprise.

**Classe** : `ASSISTABLE_SEULEMENT`.

## 12. F11 — Human-First et charge cognitive

Sources : `R-039`, distinct de `R-030`.

**Risque protégé** : surfaces de reprise opaques, identifiants locaux qui portent le sens à la place du langage humain, nécessité de lire une généalogie entière pour comprendre une tâche actuelle.

**Observables faibles/indirects** :

- densité de références non définies ;
- présence d’un libellé humain avec un ID ;
- liens vers le point d’entrée courant ;
- taille/structure d’une surface.

Ces métriques ne suffisent pas à mesurer l’intelligibilité.

**Action automatique admissible** : lint informatif ou test d’accessibilité structurelle, jamais verdict `lisible/illisible` automatique.

**Autorité humaine résiduelle** : compréhension réelle, choix du niveau de détail, adéquation sémantique.

**Classe** : `ASSISTABLE_SEULEMENT`.

## 13. F12 — Vocabulaire disciplinaire prioritaire

Source : `R-030`.

**Risque protégé** : un vocabulaire interne remplace abusivement une notion disciplinaire ou crée un faux concept transverse.

**Observable machine** : lexiques déclarés et occurrences, au mieux.

**Non-observable automatiquement** : adéquation scientifique d’un terme dans un argument.

**Action automatique admissible** : aucune correction sémantique automatique ; éventuellement repérage de termes internes connus pour revue.

**Autorité humaine résiduelle** : qualification scientifique et choix terminologique.

**Classe** : `NON_MECANISABLE_COMME_VERDICT`.

## 14. F13 — Passage inter-domaines et réinstruction

Source : `R-036`.

**Risque protégé** : copier une dette, un vocabulaire ou un verdict dans un autre domaine sans reconstruire la question.

**Observable machine** : liens entre dossiers, provenance, présence de champs de transfert si formalisés.

**Non-observable automatiquement** : existence d’un discriminant réellement nouveau dans le domaine d’accueil, reformulation correcte de la question, valeur scientifique du transfert.

**Action automatique admissible** : fournir une checklist/prompt ou rassembler les pièces ; ne jamais valider le transfert.

**Autorité humaine résiduelle** : décision scientifique de transfert/réouverture.

**Classe** : `ASSISTABLE_SEULEMENT`.

## 15. F14 — Portée exacte d’une autorisation

Source : `R-034`.

**Risque protégé** : transitivité implicite `qualifier → exécuter → propager → muter → merger`.

**Observable machine** : seulement si la portée de l’autorisation est structurée explicitement par type d’acte/objet.

**Action automatique admissible** : empêcher un type d’acte absent d’une autorisation structurée ; demander/escalader à la frontière.

**Limite majeure** : dans le corpus historique libre, interpréter automatiquement la portée d’une phrase humaine serait précisément déplacer le jugement que la règle cherche à protéger.

**Autorité humaine résiduelle** : interprétation/confirmation de toute autorisation substantielle ambiguë.

**Classe** : `MECANISABLE_PARTIEL` prospectivement, `ASSISTABLE_SEULEMENT` rétrospectivement.

## 16. Fonctions explicitement hors verdict automatique

Ne pas chercher un outil qui prétend décider automatiquement :

- `R-025` constance vs stabilisation dans un cas scientifique ;
- `R-026` choix des transformations/régimes pertinents lorsque non explicités ;
- `R-027` cible/accès/constitution ;
- `R-028` portée scientifique/épistémique/ontologique d’une conclusion ;
- `R-029` signification physique ou inférentielle d’une dépendance ;
- `R-030` adéquation disciplinaire du vocabulaire ;
- `R-031` verdict scientifique à partir d’un soutien ;
- `R-032` pouvoir discriminant d’un dispositif lorsque non calculablement défini ;
- `R-036` fécondité d’un passage inter-domaines ;
- priorité de recherche, ouverture/réouverture scientifique, choix de modèle/données/prior, interprétation et merge.

Une machine peut assister la provenance, le calcul, la vérification ou la collecte de ces décisions ; elle ne doit pas leur attribuer un verdict par convention.

## 17. Matrice de priorité fonctionnelle pour la phase outils

| Priorité | Fonction | Classe | Pourquoi maintenant |
|---|---|---|---|
| P1 | F1 intégrité après écriture | MECANISABLE_DIRECT | incidents réels ; invariant simple ; forte réduction du risque |
| P1 | F2 pré-vol mutation | MECANISABLE_DIRECT/PARTIEL | incident 409 récent ; propriétés Git observables |
| P1 | F5 non-vacuité contrôle | MECANISABLE_PARTIEL | échec réel #82 ; effet direct sur validité technique |
| P1 | F6 sévérité du signal | MECANISABLE_DIRECT après contrat | #106/#107 montrent gain sans automatiser la science |
| P2 | F4 routage pertinence | MECANISABLE_DIRECT local | cas positif C2 ; généralisation non requise |
| P2 | F3 diagnostic vs destructif | MECANISABLE_PARTIEL | contre-cas #117 ; fort enjeu de réversibilité |
| P2 | F7 contradiction point d’entrée | ASSISTABLE/PARTIEL | utile pour reprise mais sémantique partiellement non observable |
| P3 | F8 provenance/ratification | ASSISTABLE | métadonnées utiles, verdict humain non automatisable |
| P3 | F9 science vivante | ASSISTABLE | risque important mais état scientifique non calculable |
| P3 | F11 Human-First | ASSISTABLE | métriques indirectes seulement |
| P3 | F13 passage inter-domaines | ASSISTABLE | préparation possible, verdict scientifique humain |
| P3 | F14 portée autorisation | PARTIEL prospectif | mécanisable seulement si autorisations structurées |

Cette priorité est une priorité **d’étude d’outillage**, pas une priorité scientifique du projet.

## 18. Comparaison à exiger pour chaque candidat technique

Pour chaque fonction P1/P2, la phase suivante doit comparer explicitement :

| Option | Question |
|---|---|
| règle prose seulement | suffit-elle réellement dans l’usage agentique ? |
| mécanisme natif/infrastructure seul | porte-t-il la fonction sans perte de contexte ? |
| combinaison | la prose garde-t-elle le jugement tandis que la machine porte l’invariant observable ? |
| aucun changement | le coût d’intégration est-il supérieur au risque réellement observé ? |

Évaluer au minimum :

- couverture de la fonction ;
- faux positifs/faux négatifs ;
- réversibilité ;
- dépendance à un fournisseur ;
- maintenance ;
- coût cognitif ;
- visibilité pour l’humain ;
- possibilité de désactivation ;
- effet sur l’autorité scientifique.

## 19. Sortie vers la recherche d’outils

La cartographie permet maintenant d’ouvrir la recherche de capacités **sans partir du nom d’un outil**.

Ordre de recherche :

1. capacités natives Git/GitHub déjà disponibles ;
2. capacités du connecteur/API utilisées dans le projet ;
3. petits scripts locaux ou hooks simples ;
4. seulement si gain non couvert : outils open source maintenus et gratuits/directement accessibles.

Aucune installation ou migration n’est autorisée par cette cartographie.

## Statut

```text
CARTOGRAPHIE_FONCTIONNELLE = PRESENTE
OUTIL_SELECTIONNE = AUCUN
INSTALLATION = NON_AUTORISEE_PAR_CE_DOCUMENT
MIGRATION = NON_AUTORISEE_PAR_CE_DOCUMENT
PRIORITE_OUTILLAGE = F1/F2/F5/F6 PUIS F4/F3/F7
PROCHAINE_OPERATION = COMPARAISON_CAPACITES_NATIVES_API_OUTILS
MERGE_#139 = NON_AUTORISE
```
