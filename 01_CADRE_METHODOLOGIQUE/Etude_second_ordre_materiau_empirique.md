# Étude exhaustive de second ordre du matériau empirique
## 0. Statut et objet
Cette étude traite l’export conversationnel fourni comme **matériau empirique du dispositif humain–agent**. Il sert à observer des séquences de proposition, décision, action, correction, oubli, sous-application, sur-application, coût, arrêt et apprentissage. Il ne devient ni autorité normative, ni preuve scientifique des phénomènes physiques discutés.
```text
ETUDE_SECOND_ORDRE_MATERIAU_EMPIRIQUE = EFFECTUEE
COUVERTURE_EPISODES = 71/71
REPONSES_PRESENTES = 70
LECTURE_TEXTE_BRUT_CONTINUE = OUI
PASSE_INDEPENDANTE_MATERIAU_VERS_PHENOMENES = OUI
PASSE_INVERSE_PHENOMENES_VERS_EPISODES_ANTERIEURS = OUI
CONTRE_PASSE_MATRICE_139_VERS_MATERIAU = OUI
ABLATION_DES_LACUNES = OUI
SATURATION_DANS_CE_CORPUS_FIXE = ATTEINTE
SATURATION_UNIVERSELLE_DU_PROJET_OU_DES_INTERACTIONS_FUTURES = NON_REVENDIQUEE
PROMOTION_NORMATIVE = NON
MERGE = NON_AUTORISE
```
Source étudiée : `Laboratoire_d_instruction_et_d_application_regles_methodologiques_ et_epistemiques_depot.md`. Empreinte SHA-256 : `6f0f797b6ca4cdece53bc7099e5726325d2130e292625c246824cabaf59f03a3`. Le fichier contient 8560 lignes rendues. Aucune donnée d’identification issue de l’en-tête source n’est reproduite dans les sorties de codage.
## 1. Méthode de couverture
La procédure a été volontairement séparée de la matrice existante afin de permettre au matériau de produire des phénomènes que #139 n’avait pas déjà nommés.
1. **Segmentation naturelle** : 71 interventions utilisateur ont défini 71 épisodes `E01–E71`; 70 réponses sont présentes. Le cas où deux interventions précèdent une réponse et le dernier prompt sans réponse sont conservés comme propriétés du processus, non corrigés artificiellement.
2. **Première passe ouverte** : lecture linéaire et codage sans grille P1–P5 ni obligation de retrouver les 39 unités de #139.
3. **Passe inverse** : toute famille apparue tardivement a été recherchée dans les épisodes antérieurs pour distinguer nouvelle fonction, ancêtre moins explicite et simple spécialisation.
4. **Relecture brute continue** : l’intégralité du texte source a été relue par plages continues jusqu’à la dernière ligne pour rechercher épisodes non codés, rangs mal classés et familles manquantes.
5. **Compression fonctionnelle** : les phénomènes provisoires ont été fusionnés seulement lorsque l’ablation ne faisait perdre ni déclencheur propre, ni risque protégé, ni action distincte, ni contre-cas indépendant.
6. **Contre-passe avec #139** : les familles finales ont été comparées aux 39 unités et 44 relations de la matrice préexistante.
7. **Ablation des manques** : les candidats restants ont été explicitement testés contre les unités proches avant création de toute nouvelle ligne.
## 2. Hiérarchie des preuves dans le matériau
Le matériau n’a pas un statut probatoire uniforme. L’étude distingue :

- **interaction directement observable** : formulation, correction, décision, refus, changement de direction ou absence de réponse visible dans le texte ;
- **témoignage rétrospectif de l’utilisateur** : preuve directe de l’expérience rapportée, mais pas causalité générale automatique ;
- **état du dépôt médié par une réponse agentique** : preuve que l’agent a rapporté ou utilisé cet état ; toute décision matérielle dépendante exige confrontation au dépôt ;
- **rapport ou proposition d’un autre système intégré à la conversation** : preuve que la proposition est entrée dans le dispositif, pas preuve de sa vérité ;
- **résultat scientifique discuté** : son rang scientifique vient du dossier/source compétente, non du fait qu’il apparaît dans la conversation.
Cette hiérarchie interdit de transformer l’export en « vérité globale » tout en permettant d’en faire une véritable surface empirique pour les comportements du dispositif.
## 3. Familles finales issues du matériau
| Famille | Sens | Premier épisode | Dernier épisode | Occurrences | Sortie après comparaison à #139 |
|---|---|---:|---:|---:|---|
| `EF01_AUTHORITY_DECISION` | Autorité, provenance, intervention humaine et portée exacte des actes | E01 | E71 | 20 | Déjà distribué entre R-019, R-020, R-033 et R-034 ; pas de nouvelle ligne. |
| `EF02_REPRESENTATION_INTEGRITY` | Intégrité des transformations de représentation | E01 | E71 | 11 | Lacune autonome après ablation → R-040 candidate. |
| `EF03_HUMAN_AUDITABILITY` | Auditabilité sémantique humaine et réinstallation des référents | E04 | E71 | 12 | Enrichit R-039, notamment aux frontières de contexte ; pas de nouvelle ligne. |
| `EF04_CONTINUITY_RECOVERABILITY` | Continuité, matérialisation et récupérabilité | E03 | E71 | 19 | Déjà porté par R-007/R-008/R-018/R-021 ; renforcer les relations, pas créer une ligne. |
| `EF05_NONPROLIFERATION_FUNCTION` | Non-prolifération par fonction, gain et coût | E01 | E59 | 7 | Déjà porté par R-017 et sa spécialisation R-018. |
| `EF06_RULE_EVIDENCE_STATUS` | Statut probatoire d’une règle | E08 | E55 | 5 | Lacune autonome après ablation → R-041 candidate. |
| `EF07_RULE_REGIME_EVOLUTION` | Régime d’application, régionalisation et évolution d’une règle | E13 | E70 | 18 | Structure de colonnes de la matrice ; ne pas la réifier en règle récursive. |
| `EF08_SECOND_ORDER_SYMMETRY` | Second ordre, symétrie critique, contre-échantillon et confondeurs | E05 | E69 | 24 | Déjà porté par R-010/R-011/R-015. |
| `EF09_FUNCTION_MECHANISM_TOOLING` | Fonction d’une règle versus support, mécanisme et outillage | E07 | E68 | 14 | Déjà porté surtout par R-014/R-022/R-024 et la cartographie fonctionnelle. |
| `EF10_RULE_LIFECYCLE_EXPOSURE` | Cycle de vie expérimental d’une candidate | E08 | E64 | 20 | Trajectoire horizontale à représenter dans la vue 2D ; pas une nouvelle ligne. |
| `EF11_CAUSAL_PROOF` | Localisation causale et couplage dispositif–propriété | E50 | E65 | 9 | Déjà porté par R-002/R-003 ; les domaines de silence sont désormais bien documentés. |
| `EF12_RESOLUTION_UPLIFT` | Remontée de résolution et apprentissage transférable | E14 | E69 | 8 | Lacune autonome après ablation → R-042 candidate, promotion transverse non établie. |
| `EF13_LIVE_SCIENCE_PROGRAM` | Science vivante, négatifs, priorités et évolution des questions | E03 | E71 | 14 | Déjà porté par R-009/R-023/R-037 ; enrichir la dimension évolution des questions. |
| `EF14_REVERSIBLE_MUTATION` | Réversibilité et mutation versionnée | E01 | E57 | 7 | Déjà porté par R-035/R-038/R-021. |
| `EF15_PROSPECTIVE_INFORMATION_BOUNDARY` | Frontière informationnelle prospective et scellement avant résultat | E63 | E70 | 7 | Procédure scientifique locale C10 ; ne pas promouvoir transversalement à partir de ce corpus. |

Les 71 épisodes possèdent au moins une famille finale. La table de codage conserve les lignes source et les types de preuve sans recopier les prompts complets.
## 4. Preuve de saturation dans le corpus fixe
La première passe ouverte **n’était pas saturée** : des phénomènes provisoirement nouveaux apparaissaient encore dans les derniers épisodes. La saturation n’a donc pas été inférée de la simple fin du fichier.
La passe inverse a ensuite montré que plusieurs nouveautés tardives étaient des spécialisations ou reformulations de fonctions antérieures : réinstallation sémantique aux frontières de contexte, pré-déclaration d’issues scientifiques, distinction standard général/précaution locale, conservation des négatifs et diagnostic produit par un rapport courant.
Après cette compression :

- la dernière **famille méthodologique transverse** nouvelle apparaît à E50 (`EF11_CAUSAL_PROOF`) ;
- E63 introduit `EF15_PROSPECTIVE_INFORMATION_BOUNDARY`, conservée comme procédure scientifique locale et non comme règle transverse ;
- les épisodes E64–E71 n’imposent plus aucune nouvelle famille générale après recherche de leurs antécédents ;
- la relecture brute terminale ne produit aucun épisode sans rattachement et aucune nouvelle fonction indépendante ;
- l’ablation contre #139 réduit les manques à trois fonctions distinctes.
Le verdict recevable est donc : **saturation fonctionnelle pour la découverte de familles de second ordre dans ce matériau fixe**. Ce verdict doit être rouvert si un passage oublié, une nouvelle version du matériau, un contre-cas ou une interaction future modifie une famille, son régime ou sa relation.
## 5. Trois lacunes qui résistent à l’ablation
### R-040 — intégrité d’une transformation de représentation
Fonction : lorsqu’une sortie, synthèse, traduction ou réduction devient l’entrée d’une étape suivante ou prétend représenter l’état courant, vérifier ce qui a été conservé, perdu, ajouté ou requalifié. **Justesse locale du sous-ensemble transmis ≠ suffisance de la représentation pour l’usage aval.**

Cas empiriques principaux : passage phase 1 → phase 2, puis réévaluation des phases suivantes ; rapport courant de fin de conversation réintroduisant un ancien cadrage/question.

Ablation : `R-009` ne traite que la science vivante ; `R-010/R-011` contrôlent l’audit ; `R-039` traite l’intelligibilité humaine. Aucun ne protège le raccord général entre deux représentations localement plausibles.

Verdict : `NOUVELLE_UNITE_CANDIDATE_FORTE / PAS_DE_PROMOTION_NORMATIVE_AUTOMATIQUE`.
### R-041 — statut probatoire d’une règle
Fonction : distinguer `formulée`, `appliquée`, `observée`, `mise à l’épreuve`, `soutenue/falsifiée`, `ratifiée`, `promue`. Une application sans incident ne vaut pas test. Une prétention de test demande effet attendu, critère d’échec/coût, contre-cas ou comparaison et observation discriminante.

Cas empiriques : règles de #133 initialement qualifiées trop haut ; découverte ultérieure d’un vrai micro-pilote réflexif ; shadows historiques avec recherche volontaire de mauvais cas et domaines de silence.

Ablation : la matrice possédait déjà des colonnes de statut probatoire, mais aucune unité n’interdisait explicitement le saut `application → preuve d’efficacité`. Le schéma stocke le statut ; `R-041` gouverne la justification du changement de statut.

Verdict : `NOUVELLE_UNITE_CANDIDATE_FORTE / REGIME_AUDIT_ET_PROMOTION`.
### R-042 — remontée de résolution
Fonction : après une résolution substantielle, distinguer **solution locale**, **connaissance causale** et **apprentissage potentiellement transférable** ; ne faire remonter que ce qui résiste à un test de transport, dans le support récupérable le moins coûteux.

Cas empiriques : épisodes C7 réanalysés, oubli de matérialisation d’une connaissance pourtant identifiée, puis formulation explicite d’un apprentissage distribué du dispositif.

Ablation : `R-008` conserve un état/checkpoint ; `R-018` capture une idée ; `R-024` qualifie un outil. Aucun ne sélectionne la connaissance causale issue d’une résolution pour décider ce qui doit rester local ou remonter.

Verdict : `NOUVELLE_UNITE_CANDIDATE / FORTE_COMME_PROCESSUS_VERTICAL / PROMOTION_TRANSVERSE_NON_ETABLIE`.
## 6. Deux structures de second ordre à ne pas convertir en nouvelles lignes
### Régime d’application d’une règle
La distinction entre règle formulée, régime déclaré, ratification humaine, application de fait et régime justifié après audit est extrêmement soutenue par le matériau. Mais elle constitue déjà **l’architecture des colonnes de chaque ligne de la matrice**. En faire une nouvelle `R-043` transformerait le schéma qui qualifie les règles en règle auto-référentielle supplémentaire.
### Cycle de vie d’une candidate
Le matériau fait apparaître une trajectoire robuste :

```text
émergence
→ fonction/régime
→ autorité minimale ou shadow
→ effet attendu + échec + silence
→ exposition réelle / contre-cas
→ qualification probatoire
→ décision distincte de portée
→ promotion / amendement / régionalisation / abandon
→ surveillance légère ou réouverture sur événement
```

Cette structure doit être représentée **horizontalement** dans la vue 2D ou les relations, pas comme une règle supplémentaire qui aurait elle-même besoin d’un cycle de vie identique.
## 7. Conséquence pour la matrice 2D
Le matériau soutient deux axes différents.

**Horizontal — trajectoire d’un acte ou d’une règle :**
```text
déclencheur → proposition/candidate → exposition/opération → observable → qualification → décision de portée → action/silence/suspension/clôture → révision éventuelle
```

**Vertical — remontée systémique :**
```text
incident/objet local
↕ cause ou mécanisme
↕ connaissance causale
↕ candidate de règle/heuristique
↕ test ou enforcement
↕ contrôle du contrôle / sélection
↕ représentation courante et reprise
```

`R-040` protège les passages de représentation, `R-041` empêche les sauts probatoires horizontaux et `R-042` gouverne la remontée verticale d’une résolution.

Les flèches doivent rester typées : causalité opérationnelle, requalification épistémique, autorisation ou transformation de représentation. Une proximité graphique ne doit jamais être lue comme causalité.
## 8. Non-règles et limites explicites
- Le matériau ne justifie pas une réflexivité continue.
- Il ne justifie pas un seuil numérique universel de shadow, de nombre d’itérations ou d’appels API.
- Il ne justifie pas que toute solution locale remonte en règle.
- Il ne justifie pas qu’une prérégistration locale ou une garde temporelle devienne norme générale du dépôt.
- Il ne justifie pas de traiter toute intervention humaine comme décision, ni toute apparence de compte auteur comme ratification humaine.
- Il ne justifie pas de rouvrir l’étude historique générale en l’absence d’un indice discriminant.
- Il ne transforme pas les témoignages rétrospectifs en causalités universelles.
## 9. Delta proposé pour #139
```text
MATRICE_AVANT = 39 UNITES
NOUVELLES_UNITES_D_ETUDE = R-040, R-041, R-042
MATRICE_APRES_CANDIDATE = 42 UNITES
PROMOTION_DANS_AGENTS = NON
DECISION_DE_PORTEE = A_REINSTRUIRE_APRES_INTEGRATION_DU_SECOND_ORDRE
```
Le codage empirique et les trois unités nouvelles doivent d’abord être intégrés à la branche d’audit, puis la synthèse, le plan d’action et la proposition de portée antérieurs doivent être considérés comme **pré-second-ordre empirique** jusqu’à reconsolidation.
## 10. Condition de réouverture
Réouvrir cette étude si : nouvelle version du matériau ; épisode oublié ; famille sans rattachement ; contre-cas renversant un statut ; relation nouvelle qui empêche une fusion ; ou nouvelle interaction réelle produisant une fonction absente. Sans l’un de ces déclencheurs, recommencer une lecture générale du même fichier serait du coût sans information nouvelle démontrée.
