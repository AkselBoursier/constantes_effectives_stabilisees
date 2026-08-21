# Comparaison des capacités natives, API et outils — après audit

## Fonction

Cette comparaison applique la séquence de #139 après la cartographie fonctionnelle. Elle part des fonctions P1/P2 de `Cartographie_fonctions_mecanisables.md` et compare :

```text
règle interprétée
vs mécanisme natif / infrastructure
vs combinaison
vs absence de changement
```

Aucune installation ni migration n’est autorisée par ce document.

État des informations externes contrôlé le **21 août 2026**.

## 1. Résultat exécutif

Pour les fonctions prioritaires F1/F2/F4/F5/F6, l’audit ne trouve **aucune justification actuelle pour adopter une plateforme externe supplémentaire**.

Le meilleur assemblage actuel est principalement :

```text
Git/GitHub natif
+ API avec SHA
+ workflow Actions existant
+ scripts locaux ciblés
+ règles interprétées uniquement aux frontières sémantiques
```

Deux outils externes ont été examinés comme primitives étroites :

- `pre-commit` : utile pour l’ergonomie locale, mais insuffisant comme contrôle principal des mutations API/agent ;
- Coverage.py branch coverage : diagnostic ponctuel possible pour des auditeurs Python complexes, mais insuffisant comme preuve de non-vacuité ou de succès pour la bonne cause.

Verdict global :

```text
NOUVELLE_PLATEFORME = NON_JUSTIFIEE
PRE_COMMIT = NE_PAS_ADOPTER_COMME_CONTROLE_PRINCIPAL
COVERAGE_PY = DIAGNOSTIC_OPTIONNEL_CONDITIONNEL
GITHUB_NATIF_ET_SCRIPTS_EXISTANTS = PRIORITAIRES
INSTALLATION = AUCUNE
```

## 2. F1 — Intégrité après écriture ambiguë

### Option A — règle interprétée seulement

Procédure actuelle : après erreur d’écriture ou état ambigu, relire l’objet avant de conclure au succès/échec.

Avantage : zéro infrastructure nouvelle.  
Limite : dépend du déclenchement correct par l’agent ; les incidents #131/#132 et le comportement 409 observé pendant #139 montrent que l’erreur humaine/agentique reste possible.

### Option B — API GitHub native

L’API `Create or update file contents` exige le `sha` du blob remplacé lors d’une mise à jour. Elle fournit donc déjà un contrôle d’état préalable de type verrou optimiste.

Source officielle :
`https://docs.github.com/en/rest/repos/contents`

Mais l’API ne résout pas seule le cas :

```text
requête envoyée
→ réponse réseau/service ambiguë
→ état réel inconnu
```

Le read-back reste nécessaire après une réponse indéterminée.

### Option C — wrapper dédié

Un wrapper pourrait imposer automatiquement :

```text
write
→ si succès explicite : contrôle terminal léger
→ si erreur ambiguë : read-back obligatoire
→ si contradiction : stop mutations
```

Gain potentiel élevé, mais aucun point d’extension stable du connecteur ChatGPT n’est actuellement matérialisé dans ce dépôt.

### Verdict

```text
F1 = COMBINAISON_ACTUELLE
API_SHA + REGLE_READ_BACK
WRAPPER = CANDIDAT_FUTUR_SI_POINT_D_EXTENSION_REEL
OUTIL_EXTERNE = NON
```

Ne pas créer maintenant un wrapper hypothétique qui ne contrôlerait pas effectivement le chemin d’écriture utilisé par les agents.

## 3. F2 — Pré-vol de mutation

### Capacité native déjà présente

Le `sha` requis pour remplacer un fichier empêche une écriture fondée sur un ancien blob. L’incident 409 de #139 a matériellement montré cette protection : les écritures avec SHA invalide ont été refusées et aucune mutation n’a eu lieu.

GitHub propose également des protections/rulesets capables, selon la configuration du dépôt, d’imposer une PR, des status checks, de bloquer force-push ou suppression de branches/tags.

Sources officielles :

- `https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets`
- `https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches`

Ces protections portent la frontière de branche/merge ; elles ne remplacent pas le pré-vol sémantique d’un fichier.

### Script ou hook local

Un hook local pourrait vérifier certains invariants avant commit. Mais la mutation via API/connecteur ne passe pas nécessairement par les hooks Git d’un clone local.

### Verdict

```text
F2_SHA_OBSOLETE = DEJA_PORTE_PAR_API
F2_NO_OP / CONTROLE_TERMINAL = SCRIPT_OU_DISCIPLINE_AGENTIQUE_LEGERE
F2_PROTECTION_MAIN = CAPACITE_GITHUB_A_EVALUER_SEPAREMENT_AVANT_CONFIGURATION
PRE_COMMIT = PAS_NECESSAIRE_POUR_CETTE_FONCTION
```

Aucune configuration de ruleset n’est autorisée ici ; son état réel doit être inspecté avant toute proposition de changement.

## 4. F3 — Diagnostic versus mutation destructive

Les rulesets GitHub peuvent protéger des branches/tags et exiger des PR/checks. Les push rulesets peuvent aussi restreindre certains chemins selon le plan et le type de dépôt. Ces mécanismes ne savent cependant pas décider qu’une suppression de fichier est scientifiquement légitime parce qu’un diagnostic de déclassement a été correctement conduit.

Le risque de #117 est sémantique :

```text
diagnostic de déclassement
≠
autorisation de suppression
```

### Verdict

```text
F3 = REGLE_INTERPRETEE + CONFINEMENT_GIT
BLOCAGE_STRUCTUREL_POSSIBLE = seulement si type d'acte explicitement déclaré
RULESET = NE_RESOUT_PAS_LA_FONCTION_SEMANTIQUE
OUTIL_EXTERNE = NON_JUSTIFIE
```

Le mécanisme technique doit empêcher une catastrophe simple ; la décision destructive reste humaine lorsqu’elle touche contenu scientifique/probatoire.

## 5. F4 — Routage de contrôles par pertinence

Le workflow courant `audit-corpus.yml` possède déjà :

- un prédicat local `c2_relevant_from_files` ;
- un test positif sur un chemin C2 ;
- un test négatif sur `README.md` ;
- une sortie `relevant=true/false` ;
- une installation/exécution C2 conditionnelle.

GitHub Actions offre nativement `paths` / `paths-ignore` au niveau du déclenchement du workflow.

Source officielle :
`https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax`

Mais GitHub documente une limite importante : lorsqu’un workflow entier est sauté par un filtre de branche/chemin et que son check est requis, le check peut rester `Pending` et bloquer le merge. À l’inverse, un **job** sauté par une condition dans un workflow déclenché remonte `Success`.

Sources officielles :

- `https://docs.github.com/en/actions/how-tos/manage-workflow-runs/skip-workflow-runs`
- `https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/troubleshooting-required-status-checks`

### Verdict

```text
F4_MECANISME_COURANT = CONSERVER
REMPLACER_PAR_PATHS_AU_NIVEAU_WORKFLOW = NON_JUSTIFIE
GENERALISER_ROUTEUR_A_TOUTE_CI = NON
```

Le mécanisme actuel constitue un cas positif où un contrôle local est mieux porté par l’infrastructure que par une règle prose répétée.

## 6. F5 — Non-vacuité des contrôles

### Mécanisme actuel

Le dépôt utilise déjà des tests positifs/négatifs explicites et des fautes ciblées. #82 a montré pourquoi la seule réussite agrégée est insuffisante : plusieurs fautes pouvaient être rejetées avant le contrôle visé et comptées comme succès.

La bonne preuve reste donc :

```text
contrôle ciblé réellement traversé
+ cause exacte du signal
+ contrôle nominal positif
```

### Coverage.py

Coverage.py sait mesurer les **branches** effectivement traversées par un programme Python (`--branch`) et signaler les destinations non exercées.

Source officielle :
`https://coverage.readthedocs.io/en/latest/branch.html`

Gain possible : vérifier structurellement que des branches d’un auditeur Python ont été exercées.

Limites :

- une branche traversée n’établit pas que l’assertion testée correspond à la propriété scientifique/technique voulue ;
- la couverture ne donne pas la cause exacte d’un succès ;
- imposer un pourcentage global recréerait un indicateur facilement vert mais peu discriminant.

### Verdict

```text
F5 = FIXTURES_CAUSALES_EXISTANTES_EN_PREMIER
COVERAGE_PY_BRANCH = DIAGNOSTIC_OPTIONNEL
SEUIL_GLOBAL_DE_COUVERTURE = NON_JUSTIFIE
INSTALLATION_MAINTENANT = NON
```

Déclencheur possible d’un essai Coverage.py : un futur auditeur Python suffisamment ramifié où l’on ne peut plus établir simplement, par fixtures ciblées, que chaque famille de contrôle est atteignable.

## 7. F6 — Sévérité du signal

Le script `audit_structure_corpus.py` possède déjà un objet `Finding(severity, ...)` et distingue `ERROR` / `WARNING`. Son code retour échoue sur les erreurs, et éventuellement sur les warnings avec `--strict`.

Le workflow des placeholders a déjà été corrigé pour qu’une dette connue soit informative sans produire une pseudo-erreur ensuite neutralisée.

### Verdict

```text
F6 = DEJA_PORTE_PAR_SCRIPT
NOUVEAU_LINTER_GENERAL = NON_JUSTIFIE
VALE_COMME_BLOCAGE_CI = NON_JUSTIFIE
```

Un nouveau moteur de règles ne serait utile que si plusieurs nouvelles propriétés purement rédactionnelles et mécaniques apparaissaient réellement, ce qui n’est pas démontré par les fonctions P1/P2 actuelles.

## 8. `pre-commit` — qualification comme primitive locale

`pre-commit` permet d’installer des hooks par clone, de filtrer les fichiers, d’exécuter des scripts locaux et de choisir les stages Git.

Source officielle :
`https://pre-commit.com/`

### Gain réel possible

- confort pour un travailleur local utilisant `git commit` / `git push` ;
- réutilisation simple d’un script local existant ;
- exécution rapide avant CI.

### Limites dans le projet actuel

- installation requise dans chaque clone ;
- ne protège pas le chemin d’écriture via API/connecteur ;
- un hook local est une ergonomie, pas une autorité de dépôt ;
- dupliquer un contrôle CI en hook peut augmenter maintenance et divergence.

### Verdict

```text
PRE_COMMIT = OPTION_ERGONOMIQUE_LOCALE_SEULEMENT
BESOIN_REPRODUIT_ACTUEL = NON
ADOPTION = NON_JUSTIFIEE
```

Réexaminer seulement si le travail local manuel produit un coût répétitif avant push que la CI corrige trop tard.

## 9. Rulesets / protection de branche

GitHub Rulesets peut notamment exiger une PR, des status checks, bloquer force-push et suppression de branches/tags ; les règles peuvent être combinées et les versions les plus restrictives s’appliquent lorsqu’elles se superposent.

Sources officielles :

- `https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets`
- `https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets`

### Fonction possible ici

Porter mécaniquement une partie de `R-038` :

```text
main protégée
+ PR requise
+ checks requis
+ force-push interdit
```

### Limites

- ne valide pas la science ;
- ne remplace pas la portée exacte des autorisations `R-034` ;
- ne protège pas par lui-même la signification d’une suppression de contenu ;
- une configuration trop stricte peut augmenter le coût des expériences réversibles.

### Verdict

```text
RULESETS = CANDIDAT_DE_CONTROLE_DE_FRONTIERE
ETAT_ACTUEL_DU_DEPOT = A_VERIFIER_AVANT_TOUTE_PROPOSITION
CONFIGURATION = DECISION_DISTINCTE
```

Cette inspection appartient à une éventuelle étape de mise en œuvre, pas à l’audit de règle lui-même.

## 10. Outils déjà évoqués dans #136

### ADR / MADR

Le schéma partiel contexte → décision → statut → conséquences reste une source d’idées de structuration. Un système `un ADR par règle/décision` créerait une nouvelle couche dont la nécessité n’est pas démontrée.

```text
SCHEMA_PARTIEL = UTILE_COMME_COMPARATEUR
ADOPTION_SYSTEME_COMPLET = NON
```

### Vale

Peut contrôler régionalement des propriétés rédactionnelles mécaniques. Il ne peut pas établir Human-First sémantique, rang probatoire ou adéquation disciplinaire.

```text
VALE = NON_PRIORITAIRE_APRES_CARTOGRAPHIE_P1_P2
BLOCAGE_CI_GENERAL = NON
```

### Log4brains

La navigation/timeline de décisions est intéressante conceptuellement, mais Git + issues + ancrages portent déjà la fonction principale.

```text
LOG4BRAINS = PAS_DE_GAIN_NET_ETABLI
```

### RO-Crate

Pertinent potentiellement pour données/provenance de recherche, mais hors fonctions P1/P2 actuelles. À réexaminer dans une tranche computation/données si une friction réelle apparaît.

```text
RO_CRATE = HORS_PERIMETRE_ACTUEL / NON_REFUTE_POUR_AUTRE_FONCTION
```

## 11. Comparaison synthétique

| Fonction | Règle seule | Git/GitHub natif | Script local | Outil externe | Verdict actuel |
|---|---|---|---|---|---|
| F1 écriture ambiguë | nécessaire | SHA partiel | wrapper futur possible | aucun gain distinct | règle + API ; pas d’outil |
| F2 pré-vol | insuffisante seule | **fort** | léger possible | pre-commit partiel | natif + contrôle terminal |
| F3 destructif | **sémantique nécessaire** | confinement seulement | garde possible | aucun outil adéquat | humain + Git |
| F4 routage CI | peu utile en prose | **déjà qualifié** | prédicat existant | aucun besoin | conserver actuel |
| F5 non-vacuité | critère nécessaire | CI exécute | **fixtures ciblées** | Coverage.py diagnostic | fixtures d’abord |
| F6 sévérité | contrat nécessaire | CI porte résultat | **déjà présent** | Vale non requis | conserver actuel |
| F7 point d’entrée | interprétation requise | liens/états | extension ciblée possible | linter général inadéquat | attendre incident |
| F8 ratification | **humaine** | métadonnées seulement | n/a | aucun verdict sûr | assistable seulement |
| F9 science vivante | **scientifique** | états GitHub partiels | agrégation possible | dashboard non justifié | ne pas automatiser verdict |
| F11 Human-First | jugement humain | structure partielle | lint informatif possible | Vale partiel | pas d’outil maintenant |

## 12. Décision technique provisoire

L’audit d’outillage aboutit pour l’instant à une **non-adoption informée** plutôt qu’à une installation.

```text
GARDER_WORKFLOW_ACTUEL = OUI
GARDER_SCRIPTS_LEGERS = OUI
AJOUTER_PRE_COMMIT = NON
AJOUTER_COVERAGE_PY = NON_MAINTENANT
AJOUTER_VALE = NON_MAINTENANT
ADOPTER_ADR_LOG4BRAINS_ROCRATE = NON_DANS_CETTE_TRANCHE
RULESET = CAPACITE_A_INSPECTER_AVANT_DECISION, PAS_CONFIGURER_ICI
NOUVELLE_PLATEFORME = NON
```

La prochaine action utile n’est donc pas une installation. Deux suites seulement sont justifiées :

1. **inspection bornée de la protection GitHub réellement configurée** si une décision d’enforcement de `main` doit être préparée ;
2. **prototype très léger de F1/F2** seulement si l’on dispose d’un point d’extension qui contrôle effectivement le chemin d’écriture utilisé par les agents.

Sans l’un de ces déclencheurs, `AUCUN_CHANGEMENT_OUTILLAGE` est la sortie préférable.

## 13. Références externes vérifiées

- GitHub REST — repository contents / SHA : `https://docs.github.com/en/rest/repos/contents`
- GitHub Rulesets — règles disponibles : `https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets`
- GitHub protected branches : `https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches`
- GitHub Actions — syntaxe et filtres : `https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax`
- GitHub Actions — checks sautés : `https://docs.github.com/en/actions/how-tos/manage-workflow-runs/skip-workflow-runs`
- GitHub — required status checks : `https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/troubleshooting-required-status-checks`
- pre-commit : `https://pre-commit.com/`
- Coverage.py branch coverage : `https://coverage.readthedocs.io/en/latest/branch.html`

## Statut

```text
COMPARAISON_CAPACITES = EFFECTUEE_POUR_PRIORITES_P1_P2
INSTALLATION = AUCUNE
MIGRATION = AUCUNE
NON_ADOPTIONS_DOCUMENTEES = OUI
DECISION_RULESET = NON_OUVERTE_PAR_CE_DOCUMENT
PROTOTYPE_WRAPPER_F1_F2 = CONDITIONNEL_A_UN_POINT_D_EXTENSION_REEL
MERGE_#139 = NON_AUTORISE
```
