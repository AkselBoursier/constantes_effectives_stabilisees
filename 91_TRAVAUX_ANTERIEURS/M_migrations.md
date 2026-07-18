# M_migrations.md

Statut : registre de migration conceptuelle de phase 7.

Date : 2026-06-25.

Portée : ce fichier documente les trajectoires entre les formulations antérieures du cadre, les audits, les consolidations, les sections v13 A-J, K, L et l'annexe. Il ne remplace aucun terme automatiquement.

Sources directrices :

- `../PROJECT_BRIEF.md`
- `Architecture_v13.md`
- `Definitions_v13_travail.md`
- `K_registre_conceptuel.md`
- `L_voisinages.md`
- `Annexe_genealogique.md`
- `../00_sources_originales/Definitions_cadre_coupes_v12.md`
- `../01_conversation_et_audits/Consolidation_A_C.md`
- `../01_conversation_et_audits/Consolidation_D_H.md`
- `../01_conversation_et_audits/Audits_A_M.md`
- `../02_registres_de_travail/DECISION_LEDGER.md`
- `../02_registres_de_travail/CONCEPT_STATUS.md`

## 1. Fonction de M

M est un registre de provenance et de migration.

Il sert à :

- indiquer comment un terme ou une thèse antérieure doit être traité dans la v13 ;
- distinguer migration conceptuelle, simple renommage, restriction, fragmentation, suspension ou abandon ;
- empêcher les remplacements globaux dans le manuscrit ;
- préparer l'audit transversal et la future synchronisation du manuscrit.

M ne sert pas à :

- produire une table de synonymie ;
- remplacer automatiquement un mot par un autre ;
- effacer la mémoire de v12 ;
- réintroduire sous un autre nom une thèse retirée ;
- garantir qu'un concept migré possède le même statut dans tous les terrains.

## 2. Principe de non-substitution

Aucune ligne de ce registre ne vaut instruction de remplacement global.

Lorsqu'un terme ancien apparaît dans un texte à synchroniser, il faut :

1. identifier la fonction locale de l'occurrence ;
2. vérifier son statut dans `K_registre_conceptuel.md` ;
3. vérifier la décision correspondante dans `DECISION_LEDGER.md` ;
4. choisir le type de migration applicable à cette occurrence ;
5. conserver l'ancien terme seulement s'il joue un rôle historique, critique, généalogique ou citationnel ;
6. réécrire localement si le terme porte encore une thèse retirée ;
7. documenter les cas ambigus comme questions d'audit.

## 3. Catégories de migration

| Catégorie | Définition | Effet sur l'usage |
|---|---|---|
| conservation active | le terme reste utilisable avec statut clarifié | employer selon K |
| conservation historique | le terme reste lisible comme trace d'un état antérieur | mention historique, généalogique ou critique seulement |
| renommage | le terme change de nom sans changement majeur de fonction | vérifier que le sens local ne change pas |
| restriction | la portée d'un terme est réduite | employer seulement dans les conditions fixées |
| élargissement | la fonction devient plus générale ou plus méthodologique | contrôler le coût conceptuel |
| fragmentation | un terme ancien se divise en plusieurs notions | choisir la notion locale, ne pas remplacer en bloc |
| fusion | plusieurs termes anciens convergent vers un outil unique | vérifier qu'aucune différence utile n'est effacée |
| régionalisation | un terme reste valable dans certains terrains seulement | produire terrain, mécanisme et cas négatif |
| requalification modale | le terme passe de thèse à hypothèse, critère, terrain, analogie ou question | indiquer le statut modal |
| suspension | le terme ne doit pas servir de prémisse | mention critique ou hypothèse à instruire |
| abandon | la thèse ou le terme sort du noyau actuel | ne pas réintroduire sauf mémoire négative |

## 4. Format de lecture des lignes

Chaque ligne de migration indique :

- l'ancien terme, l'ancienne thèse ou l'ancien usage ;
- son traitement v13 ;
- le type principal de migration ;
- les décisions de contrôle ;
- la consigne d'usage.

Plusieurs types peuvent s'appliquer à une même entrée. Le type principal indique la décision dominante.

## 5. Migrations architecturales

| ID | Ancien terme ou ancienne thèse | Traitement v13 | Type principal | Décisions | Consigne d'usage |
|---|---|---|---|---|---|
| M-001 | v12 comme source canonique actuelle | v12 devient source à refondre et archive conceptuelle contrôlée | conservation historique | D-001 | citer v12 comme provenance, non comme norme |
| M-002 | cadre comme théorie générale des coupes constitutives | programme comparatif sur les différenciations, médiations, effets, histoires et critères d'échec | requalification modale | D-031, D-038 | présenter le cadre comme enquête, non doctrine générale |
| M-003 | question directrice : comment toute coupe produit-elle les termes qu'elle sépare ? | question directrice pluralisée : que fait une différenciation déterminée, selon quels mécanismes, asymétries et persistances ? | fragmentation | D-002, D-038, D-043 | reformuler localement selon terrain et mécanisme |
| M-004 | auto-application déduite de "toute coupe est constitutive" | auto-application critique comme obligation méthodologique | requalification modale | D-039 | ne jamais l'utiliser comme preuve de validité |
| M-005 | posture de méta-langage non neutre par circularité constitutive | contrôle de reconstruction, modalité et auto-application | restriction | D-039, D-061 | expliciter l'effet critique sans circularité forte |
| M-006 | table de concordance terminologique fractale | registre de migration conceptuelle et de provenance | abandon / reconstruction | D-027, D-081 | ne pas reprendre la logique de remappage automatique |
| M-007 | migration fractale comme principe général d'harmonisation | migrations locales : conservation, restriction, fragmentation, régionalisation, suspension, abandon, etc. | fragmentation | D-027, D-082 | classifier chaque occurrence séparément |
| M-008 | section M comme appendice de concordance | M comme registre de contrôle avant audit et synchronisation du manuscrit | requalification modale | D-027, D-081 | utiliser M pour préparer la phase 8, pas pour réécrire le manuscrit |

## 6. Migrations des concepts de base

| ID | Ancien terme ou ancienne thèse | Traitement v13 | Type principal | Décisions | Consigne d'usage |
|---|---|---|---|---|---|
| M-009 | coupe comme toute opération de distinction | coupe comme famille candidate de situations où une différence devient pertinente, opératoire, identifiable, stabilisée ou effective | restriction | D-002, D-012, D-082 | employer avec terrain, effet et possibilité d'échec |
| M-010 | toute coupe est constitutive | thèse retirée ; constitution devient hypothèse forte locale | abandon | D-003, D-005 | ne jamais en faire une prémisse |
| M-011 | coupe constitutive comme expression centrale | dissociation entre "coupe" et "constitution" | fragmentation | D-002, D-003, D-005 | vérifier si l'occurrence exige "coupe", "distinction", "frontière", "couplage" ou "constitution" |
| M-012 | distinction, différenciation et coupe comme quasi-équivalents | différenciation, distinction, frontière, interaction, couplage, constitution et coupe distingués | fragmentation | D-004, D-041 | choisir le terme localement nécessaire |
| M-013 | constitutif comme qualificatif analytique non restrictif | constitution comme effet fort à démontrer | restriction | D-003, D-005 | exiger objet, mécanisme, régime, asymétries et persistance |
| M-014 | deux registres ontologique/processuel et épistémique/pratique comme deux perspectives d'un même processus | registres physique, épistémique et pratique distingués sans fusion | fragmentation | D-011, D-042, D-060 | ne pas déduire l'ontologique de l'épistémique ni l'inverse |
| M-015 | toute coupe épistémique a des effets ontologiques | effet pratique ou institutionnel à démontrer localement | restriction | D-011, D-042, D-060 | identifier l'effet, son support et son régime |
| M-016 | coupe paramétrique / coupe effective | distinction à reprendre seulement si le terrain l'exige ; sinon profil de cas, statut modal et conditions de réalisation | requalification modale | D-013, D-043, D-056 | ne pas l'utiliser comme axe transversal acquis |
| M-017 | voie médiane du cadre | issue possible seulement si le test de gain la produit | abandon comme programme | D-014, D-061 | ne pas annoncer une solution intermédiaire avant enquête |

## 7. Migrations de la taxonomie et des gradients

| ID | Ancien terme ou ancienne thèse | Traitement v13 | Type principal | Décisions | Consigne d'usage |
|---|---|---|---|---|---|
| M-018 | taxonomie des coupes physiques, chimiques, biologiques, pré-thématiques, méthodologiques et réflexives | matrice multidimensionnelle et profil de cas | abandon / fragmentation | D-007, D-043, D-044 | décrire les dimensions du cas, ne pas classer dans une cascade |
| M-019 | passage général du physique au réflexif | architecture non hiérarchique A-J et dimensions indépendantes | abandon | D-007, D-010, D-031 | éviter toute narration progressive unique |
| M-020 | degré de thématisation comme axe taxonomique | statut d'explicitation situé | restriction | D-009, D-043 | préciser agent, pratique, moment et disponibilité |
| M-021 | pré-thématique comme type permanent de coupe | non-thématisation, routinisation, tacitation, boîte noire, oubli historique, naturalisation à distinguer | fragmentation | D-009, D-057 | choisir le devenir épistémique pertinent |
| M-022 | gradient des rapports à soi | capacités de retour distinguées : rétroaction, autorégulation, modification de paramètres, modification de règles, représentation, critique réflexive | fragmentation | D-010, D-043 | ne pas transformer ces capacités en hiérarchie unique |
| M-023 | coupe réflexive comme sommet du gradient | réflexivité critique validée restreint ; réflexivité conditionnelle suspendue ou régionale | restriction / suspension | D-010, D-060, D-072 | préciser opération de révision ou statut suspendu |
| M-024 | transversalité différentielle acquise | transversalité candidate sous invariant, règles de traduction, cas négatifs, seuil et gain | requalification modale | D-012, D-063 | traiter toute extension comme hypothèse à tester |
| M-025 | variation locale comme signature d'un même concept | variation, analogie, homonymie, fragmentation ou perte d'identité à distinguer | fragmentation | D-012, D-063 | appliquer un seuil de rupture |

## 8. Migrations des relations

| ID | Ancien terme ou ancienne thèse | Traitement v13 | Type principal | Décisions | Consigne d'usage |
|---|---|---|---|---|---|
| M-026 | co-constitution comme relation générale terrain-indépendante | co-constitution comme hypothèse forte maximale | restriction | D-005, D-045, D-082 | n'employer qu'après exclusion d'interaction, dépendance, couplage, co-détermination ou co-stabilisation |
| M-027 | co-constitution asymétrique comme propriété transversale | asymétries multiples : causale, dépendance, matérielle, contrôle, temporelle, vulnérabilité, épistémique, institutionnelle | fragmentation | D-046 | analyser l'axe précis d'asymétrie |
| M-028 | couplage structurel comme instanciation biologique élargissable de la co-constitution | couplage structurel régionalisé dans la tradition Maturana/Varela | régionalisation | D-006, D-047, D-084 | ne pas l'utiliser comme preuve générale |
| M-029 | régime de couplage comme principe taxonomique | structure de dépendance et type de relation dans le profil de cas | requalification modale | D-043, D-045 | décrire la relation sans taxonomie substantielle |
| M-030 | réversibilité comme texture locale du concept transversal | réversibilité relationnelle à préciser par régime | suspension / fragmentation | D-048 | ne pas utiliser comme variable unique |
| M-031 | trace de l'autre dans chaque terme co-constitué | trace relationnelle comme indice reconstructible, sans preuve automatique | restriction | D-045 | exiger trace, effet ou reste identifiable |
| M-032 | relation forte présumée par la coupe | série relationnelle graduée : covariation, interaction, dépendance, couplage, co-détermination, co-stabilisation, co-individuation, co-constitution | fragmentation | D-005, D-045, D-082 | choisir le niveau minimal suffisant |

## 9. Migrations des temporalités, persistances et devenirs

| ID | Ancien terme ou ancienne thèse | Traitement v13 | Type principal | Décisions | Consigne d'usage |
|---|---|---|---|---|---|
| M-033 | destins d'une coupe | temporalités, modes de persistance, stabilité, héritage et effets à distinguer | fragmentation | D-015, D-049, D-082 | ne pas attribuer un destin à une entité unique appelée coupe |
| M-034 | sédimentation comme processus général de toute coupe | sédimentation régionalisée, surtout historique, phénoménologique, épistémique, institutionnelle ou documentaire | restriction / régionalisation | D-017, D-051, D-065 | exiger support, transmission, disponibilité et effet |
| M-035 | sédimentation cumulative | héritage sélectif, contrainte cumulative, test de cumulativité | fragmentation | D-051, D-066, D-067 | préciser pertes, filtrages, supports et effets ultérieurs |
| M-036 | solidification comme destin transversal | stabilisation, stabilité dynamique, robustesse, conditions de réalisation ou conservation selon le cas | fragmentation | D-019, D-049, D-055 | ne pas employer "solidification" comme catégorie active |
| M-037 | porosité de transition comme phase commune | concept suspendu ou usage régional à justifier | suspension | D-018, D-052 | préférer transition, perméabilité, fluctuation, métastabilité, indétermination, plasticité ou flou selon le cas |
| M-038 | porosité structurelle comme trait diagnostique transversal | maintien actif, état stationnaire hors équilibre, perméabilité, flux ou conditions de réalisation selon terrain | fragmentation / restriction | D-018, D-055, D-056 | ne pas l'utiliser comme nom commun de la stabilité par flux |
| M-039 | dormance comme destin de coupe | dormance régionalisée ; latence validée restreint hors biologie | régionalisation / renommage | D-052 | employer "latence" si le mécanisme n'est pas biologique |
| M-040 | saturation comme destin général | concept suspendu, réouvrable seulement par mécanisme local | suspension | D-016, D-052 | ne pas l'utiliser comme temporalité transversale |
| M-041 | retournement comme destin général | retiré du noyau ; certains mécanismes locaux peuvent être décrits autrement | abandon | D-016, D-052, D-069 | choisir rupture, transformation, réouverture ou mécanisme local |
| M-042 | triade terminer / tenir / suspendre | modes pluralisés de stabilité, maintien, latence, rupture et transformation | abandon / fragmentation | D-016, D-055 | ne pas reconstruire une classification fondamentale |
| M-043 | dé-sédimentation générale | réouverture critique, rupture, oubli, transformation ou perte selon terrain | fragmentation | D-017, D-069 | ne pas l'utiliser comme envers automatique de la sédimentation |

## 10. Migrations épistémiques et réflexives

| ID | Ancien terme ou ancienne thèse | Traitement v13 | Type principal | Décisions | Consigne d'usage |
|---|---|---|---|---|---|
| M-044 | chaîne distinction consciente -> sédimentation -> oubli -> réification | devenirs épistémiques pluralisés | fragmentation | D-020, D-021, D-057, D-059 | distinguer routinisation, tacitation, boîte noire, oubli, naturalisation, objectivation et réification |
| M-045 | opacification | recouvrement cognitif, mais seulement avec médiation opérante et effet sur l'analyse | restriction / renommage | D-020, D-058 | ne pas assimiler toute opacité à un recouvrement |
| M-046 | recouvrement méthodologique | non stabilisé comme catégorie active ; peut devenir cas local de médiation opérante ou question d'audit | suspension / requalification | D-020, D-058, D-083 | ne pas l'employer comme concept sans fiche locale |
| M-047 | recouvrement cognitif comme devenir fréquent de la coupe | diagnostic restreint exigeant ré-explicitation modifiant l'analyse | restriction | D-020, D-057 | échec si la ré-explicitation ne change rien |
| M-048 | objectivation et réification comme chaîne quasi continue | objectivation et réification strictement distinguées | fragmentation | D-021, D-059 | ne pas moraliser l'objectivation |
| M-049 | distinction ontologie / épistémologie comme coupe auto-diagnostiquée | distinction méthodologique maintenue ; onto-épistémologie forte suspendue | restriction / suspension | D-011, D-060 | ne pas fusionner accès, être, preuve et usage |
| M-050 | inséparabilité onto-épistémique comme posture du cadre | question philosophique possible, non définition de base | requalification modale | D-011, D-060, D-084 | signaler comme hypothèse forte si reprise |
| M-051 | réflexivité conditionnelle | hypothèse régionale ou suspendue selon terrain et mécanisme | suspension / régionalisation | D-010, D-072 | ne pas la réintroduire comme cran général du vivant |
| M-052 | mécanismes de correction implicites | mécanismes de correction comme critère méthodologique explicite | élargissement | D-057 | préciser contrainte empirique, technique, institutionnelle ou critique |

## 11. Migrations méthodologiques

| ID | Ancien terme ou ancienne thèse | Traitement v13 | Type principal | Décisions | Consigne d'usage |
|---|---|---|---|---|---|
| M-053 | variabilité opératoire comme souplesse du même motif | protocole H : reconstruction de référence, balisage modal, gain, coût, cas négatif, non-redondance | fragmentation / requalification | D-024, D-061, D-062 | mesurer le gain plutôt que constater la variation |
| M-054 | retrait comme souplesse du cadre | retrait, suspension, fragmentation, inapplicabilité, déformation et réfutation locale distingués | fragmentation | D-022, D-061 | documenter le résultat négatif |
| M-055 | condition stengersienne comme exigence générale d'irréduction | condition de non-réduction et condition de comparabilité | requalification modale | D-061, D-063 | appliquer au profil de cas et au test de gain |
| M-056 | originalité par synthèse de voisins | originalité méthodologique provisoire ; originalité théorique forte suspendue | restriction / suspension | D-076, D-078, D-084 | accepter correction, concurrence ou redondance locale |
| M-057 | voisinage comme confirmation du motif du cadre | voisinage comme test de dette, concurrence, correction, incompatibilité ou redondance | requalification modale | D-076, D-077 | reconstruire le voisin dans ses termes |
| M-058 | convergence indépendante comme argument d'autorité | constellation problématique sans preuve de validité | restriction | D-077 | distinguer filiation, convergence et problème commun |

## 12. Migrations régionales et terrains d'épreuve

| ID | Ancien terme ou ancienne thèse | Traitement v13 | Type principal | Décisions | Consigne d'usage |
|---|---|---|---|---|---|
| M-059 | alpha comme matrice majeure de confirmation possible | alpha comme terrain d'épreuve régional | requalification modale | D-029, D-061, D-074 | reconstruire métrologie, modèles et seuils avant application |
| M-060 | mécanique quantique comme preuve de non-recouvrement ou de constitution | terrain limite différé et suspendu hors reconstruction disciplinaire | suspension | D-023, D-073 | ne pas utiliser le quantum comme preuve du noyau |
| M-061 | coupe intra-régime / inter-régime | concept suspendu faute de critères explicites de régime et passage | suspension | D-073, D-083 | rouvrir seulement par fiche régionale |
| M-062 | gradient quantique de stabilisation | suspendu | suspension | D-023, D-073 | ne pas résoudre verbalement le problème de la mesure |
| M-063 | légifération universelle | abandonnée ; hypothèse de légifération seulement suspendue ou métaphysique balisée | abandon / suspension | D-073 | distinguer résultat scientifique, modèle et métaphysique |
| M-064 | régime de légalité effective comme preuve physique du cadre | hypothèse régionale à tester | requalification modale | D-073 | préciser domaine, variables, relations et statut modal |
| M-065 | pluralité constitutive du vivant | pluralité opérationnelle des individuations comme hypothèse régionale | renommage / restriction | D-072 | reconstruire les mécanismes biologiques locaux |
| M-066 | retournement constitutif biologique | sélection d'échappement sous pression protectrice | renommage / régionalisation | D-072 | éviter le retournement constitutif général |
| M-067 | plasticité comme preuve de réflexivité vivante | plasticité régulée et révisabilité adaptative, hypothèses régionales | fragmentation / restriction | D-072 | distinguer changement d'état, paramètres et règles |
| M-068 | autopoïèse comme métaphore d'auto-organisation générale | autopoïèse régionalisée dans sa tradition biologique | régionalisation | D-006, D-084 | ne pas exporter sans traduction |
| M-069 | membrane biologique comme symbole général de porosité | membrane biologique comme terrain d'épreuve de frontière, maintien, renouvellement et régulation | requalification modale | D-018, D-070 | reconstruire les mécanismes cellulaires |
| M-070 | classification institutionnelle comme preuve que toute distinction produit son objet | terrain d'épreuve pour distinction, naturalisation, réification et asymétrie institutionnelle | requalification modale | D-021, D-042, D-070 | identifier acteurs, médiations et effets |
| M-071 | double effacement | opacité de second ordre comme hypothèse régionale | restriction / régionalisation | D-074 | exiger traces, mécanisme de disparition et effets |
| M-072 | éclairement | gain de lisibilité comme critère évaluatif secondaire | requalification modale | D-074 | ne pas traiter comme validation suffisante |

## 13. Migrations des relations aux voisins

| ID | Ancien terme ou ancienne thèse | Traitement v13 | Type principal | Décisions | Consigne d'usage |
|---|---|---|---|---|---|
| M-073 | Barad comme source d'un motif repris et étendu | Barad comme voisin et correctif critique sur intra-action, apparatus et onto-épistémologie | requalification modale | D-076, D-077, D-084 | reconstruire Barad sans la réduire au cadre |
| M-074 | Simondon comme quasi-préfiguration de la sédimentation cumulative | Simondon comme voisin/concurrent sur individuation, métastabilité et transduction | requalification modale | D-076, D-077 | tester la redondance ou la correction possible |
| M-075 | Malabou comme distribution interne de la plasticité dans le cadre | Malabou comme voisin/correctif sur forme, transformation et destruction | requalification modale | D-076, D-077 | éviter de dissoudre sa plasticité en catégories du cadre |
| M-076 | Maturana/Varela comme instanciation biologique de la co-constitution | source/voisin régional sur autopoïèse et couplage structurel | restriction / régionalisation | D-006, D-076, D-077 | ne pas en faire preuve transversale |
| M-077 | Spencer-Brown, Bateson, von Foerster comme convergences du motif | constellation distinction, information, observation | requalification modale | D-077, D-084 | distinguer indication, observation et réflexivité |
| M-078 | épistémologie historique française comme confirmation du recouvrement | constellation historique et critique à reconstruire par sources | restriction | D-077, D-084 | distinguer Bachelard, Canguilhem, Foucault, Kuhn et Hacking |
| M-079 | tournant ontologique comme allié contre corrélationnisme | voisinage à contrôler sans inflation métaphysique | requalification modale | D-077, D-084 | ne pas importer verticalité ou matérialité sans test |

## 14. Liste de contrôle pour synchronisation future du manuscrit

Avant toute modification du manuscrit :

1. repérer l'occurrence ;
2. vérifier si elle appartient à une citation, une généalogie, une formulation historique ou un argument actuel ;
3. consulter K pour le statut du concept ;
4. consulter M pour la trajectoire ;
5. consulter L ou l'annexe si un voisin peut absorber le gain ;
6. choisir la migration locale ;
7. refuser tout remplacement global ;
8. signaler les occurrences ambiguës à l'audit transversal.

## 15. Cas qui exigent un audit avant réécriture

Les occurrences suivantes ne doivent pas être réécrites mécaniquement :

- "coupe", lorsque le texte ne permet pas de savoir s'il s'agit d'une distinction, d'une frontière, d'une interaction, d'une constitution ou d'un motif historique ;
- "constitutif", lorsque le terme peut être une trace v12 ou une hypothèse locale forte ;
- "sédimentation", lorsque le terrain n'est ni historique, ni phénoménologique, ni épistémique, ni institutionnel ;
- "porosité", lorsque le terme peut désigner transition, perméabilité, métastabilité, fluctuation, plasticité ou simple flou ;
- "réflexivité", lorsque le niveau de retour n'est pas spécifié ;
- "co-constitution", lorsque le mécanisme et l'asymétrie ne sont pas démontrés ;
- "légifération", lorsque le texte mélange résultat scientifique, modèle et métaphysique ;
- "originalité", lorsque le voisinage n'a pas été reconstruit.

## 16. Points ouverts après phase 7

M stabilise les catégories de migration, mais ne clôt pas :

- l'invariant minimal de "coupe" ;
- le tri entre occurrences historiques et occurrences argumentatives dans le manuscrit ;
- les cas où un voisin absorbe complètement un gain du cadre ;
- les dossiers scientifiques alpha, quantique, vivant et institutionnel ;
- les preuves par sources primaires pour certains voisins ;
- l'audit transversal de cohérence entre A-J, K, L, annexe et M.

## 17. Règle d'arrêt

La phase 7 produit M. Elle n'autorise pas :

- la réécriture du manuscrit ;
- l'audit transversal complet ;
- la promotion d'un concept régional ;
- la preuve d'originalité théorique forte ;
- la création d'une table de remplacement automatique.
