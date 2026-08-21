# Contre-test empirique du delta P1–P5

## Fonction

Ce document confronte les cinq fonctions candidates proposées après l’audit #139 au **matériau empirique conversationnel fourni par l’auteur** (`ChatGPT-Diagnostic documentaire initial-20260820-1916.md`) et aux pièces du dépôt qui portent les épisodes scientifiques ou techniques correspondants.

Le matériau conversationnel est utilisé ici comme observation de trajectoires du dispositif humain–agent : propositions, décisions, mutations, corrections, hésitations, oublis, effets sur l’action suivante. Il n’est ni une autorité normative ni une preuve scientifique sur les objets physiques.

Le test est rétrospectif et discriminant, non causal. Pour chaque candidate on demande :

```text
1. Quel événement devait la déclencher ?
2. Quelle action différente aurait-elle demandé ?
3. Existe-t-il un épisode réel où son absence ou sa sous-application a produit un défaut ?
4. Existe-t-il un cas où elle doit rester silencieuse ?
5. La fonction est-elle déjà suffisamment portée par AGENTS.md ou un mécanisme existant ?
6. Quel est le gain marginal d'une inscription supplémentaire ?
```

Une candidate n’est pas promue parce qu’elle explique rétrospectivement un incident. Le contre-test peut conclure : promotion courte plausible, fusion dans une règle existante, support local, mécanisation, observation supplémentaire ou aucune action.

## P1 — R-033 : provenance apparente ≠ ratification humaine effective

### Déclencheur testé

Une décision scientifique, irréversible ou de forte autorité est reconstruite à partir d’un commentaire, commit ou PR dont l’auteur apparent est le compte GitHub de l’auteur.

### Observation empirique

Le matériau conversationnel documente explicitement plusieurs actions du type « ajouté un commentaire sur GitHub via l’outil dédié ». Le connecteur publie néanmoins les commentaires sous le compte GitHub `AkselBoursier`. La propriété technique suivante est donc établie par le dispositif lui-même :

```text
IDENTITE_DU_COMPTE_GITHUB
!=
PREUVE_SUFFISANTE_DE_L_ORIGINE_HUMAINE_DE_L_ACTE
```

Le problème n’est pas théorique : la provenance de l’écriture et l’identité affichée peuvent diverger par construction.

### Limite empirique

Le matériau fourni ne donne pas, à ce stade, un épisode aussi net que #117 où cette ambiguïté seule aurait produit une décision scientifique erronée. Le soutien est donc **structurel fort**, mais le dommage historique direct est moins documenté que pour P2 ou P5.

### Cas de silence

- commentaire purement informatif ou technique sans effet d’autorité ;
- provenance humaine déjà établie par une intervention explicite dans la conversation ;
- décision dont l’autorité ne dépend pas de l’identité du compte auteur.

Il serait nuisible de transformer P1 en obligation d’archéologie de provenance pour chaque commentaire GitHub.

### Verdict

```text
FONCTION_DISTINCTE = OUI
AMBIGUITE_STRUCTURELLE_REPRODUITE = OUI
DOMMAGE_DIRECT_ISOLE = NON_ETABLI
GAIN_MARGINAL = FORT_POUR_DECISIONS_HAUTE_AUTORITE
PORTEE = ETROITE
```

Action proposée : **conserver P1 comme candidate de promotion courte, mais uniquement aux décisions scientifiques, irréversibles ou de forte autorité.**

## P2 — R-034 : portée exacte d’une décision ou autorisation

### Déclencheur testé

Le travail passe d’un type d’acte à un autre : proposition → décision, qualification → exécution, clôture → propagation, diagnostic → suppression, merge technique → autorité scientifique, etc.

### Épisodes positifs

Le matériau conversationnel contient un cas où l’autorisation est correctement bornée : une autorisation explicite d’agir sur GitHub est utilisée pour une opération infrastructurelle faible et réversible, **sans en déduire une autorisation générale de restructurer le dépôt**.

Les dossiers α3–α5 fournissent le même motif dans la science : la délégation procédurale permet une clôture locale une fois la condition d’arrêt satisfaite, mais ne vaut ni propagation ni fusion. α4 l’énonce explicitement dans son verdict local.

### Contre-cas causal

PR #117 est le contre-cas principal : un ancien document avait été qualifié candidat au déclassement ; cette qualification a été transformée trop vite en suppression matérielle. La PR a été fermée sans fusion. L’audit #135 a ensuite qualifié cet épisode comme un problème d’effectivité : une distinction correcte existait déjà, mais n’a pas été disponible ou déclenchée au point d’action.

### Cas de silence

Une autorisation peut légitimement couvrir plusieurs micro-actes techniques lorsqu’ils appartiennent explicitement à la même opération bornée. P2 ne doit pas produire une validation humaine à chaque sous-commande.

### Verdict

```text
FONCTION_DISTINCTE = OUI
CAS_POSITIFS_INTERREGIMES = OUI
CONTRE_CAS_CAUSAL = OUI (#117)
GAIN_MARGINAL = TRES_FORT
PORTEE = TRANSVERSE_MAIS_DECLENCHEE_AUX_CHANGEMENTS_DE_NATURE_D_ACTE
```

Action proposée : **P2 reste le candidat de promotion agentique le mieux soutenu du delta.**

## P3 — R-032 : une non-détection n’est probante que si le test est discriminant

### Déclencheur testé

Une absence de signal, une compatibilité avec zéro ou une borne est utilisée pour soutenir un maintien, une exclusion ou une invariance.

### Épreuve scientifique α4

L’issue #39 demande explicitement quelles familles de variations de `alpha` sont effectivement testées par les comparaisons d’horloges et quelle portée donner à des résultats compatibles avec zéro. Son verdict local admet une non-détection discriminante pour la dérive linéaire lente et la modulation annuelle dans les domaines déclarés, mais refuse :

- l’invariance temporelle universelle ;
- l’extension aux oscillations, transitoires et formes non testées ;
- la portée hors du domaine et de la période observés.

### Épreuve scientifique α5

L’issue #40 applique la même structure à la spectroscopie de quasars : une mesure locale calibrée, notamment ESPRESSO, ne doit pas être transformée en verdict sur tout le ciel ni en preuve indépendante de la chaîne instrumentale. L’objet de l’instruction est précisément la portée d’une non-détection locale en présence d’accès et de systématiques différents.

### Ce que P3 ajoute réellement

`AGENTS.md` porte déjà l’indexation de l’énoncé et la distinction résultat/soutien/verdict. Mais ces deux protections ne suffisent pas logiquement : un énoncé peut être parfaitement indexé et correctement classé comme résultat tout en étant **non discriminant** si le dispositif ne pouvait pas voir l’alternative pertinente.

### Cas de silence

- résultat qui n’est pas utilisé pour soutenir une constance ou une exclusion ;
- mesure positive où la question n’est pas l’absence de signal ;
- dispositif dont le pouvoir discriminant pertinent est déjà explicitement établi dans le dossier.

### Verdict

```text
FONCTION_DISTINCTE = OUI
EPREUVES_SCIENTIFIQUES_DIRECTES = OUI
CAS_DE_REFUS_EXPLICITES = OUI
GAIN_MARGINAL = FORT
PORTEE = SCIENTIFIQUE_TRANSVERSE_SUR_NON_DETECTIONS
```

Action proposée : **P3 reste candidate de promotion scientifique courte.**

## P4 — R-025 : constance de la cible ≠ stabilisation d’un accès/régime/mécanisme

### Déclencheur testé

Un maintien, une stabilité ou une robustesse observée est utilisé pour qualifier la cible physique elle-même alors que le porteur réel du maintien peut être un accès, un estimateur, un régime ou un mécanisme.

### Épreuve historique D1

Le registre décisionnel de l’audit de portée formule explicitement D1 :

```text
constance : maintien sous transformations déclarées
stabilisation : établissement, consolidation ou maintien du régime dans lequel ce maintien devient opératoire ou affirmable

constance de l’objet
!= stabilisation de l’accès
!= mode de constitution
```

Le même registre refuse deux sur-extensions : toute constance n’est pas nécessairement produite par une dynamique temporelle ; les stabilisations physiques, métrologiques, inférentielles, computationnelles ou documentaires ne forment pas automatiquement une catégorie ontologique commune.

### Épreuve dans le matériau conversationnel C10

Le rapport scientifique du cycle 10 distingue explicitement la quasi-fixité très rapide de `v(t)` de l’admissibilité du système qui la porte. Une quantité accessible peut devenir pratiquement fixe alors que le porteur produit une catastrophe énergétique ; la stabilité de la quantité accessible ne suffit donc pas à établir la stabilité ou l’admissibilité du mécanisme.

### Gain marginal sur `main`

Contrairement à P3, P4 est déjà partiellement portée par deux phrases existantes de `AGENTS.md` :

- expliciter cible/transformation/régime pour un énoncé de constance ou stabilisation ;
- ne pas confondre propriété de la cible, qualité de l’accès et mode de constitution.

Le besoin scientifique est réel, mais une **nouvelle ligne autonome** serait en partie redondante. Le gain marginal vient surtout d’une phrase de raccord explicite entre ces deux instructions.

### Cas de silence

Lorsque le vocabulaire disciplinaire établit déjà sans ambiguïté ce qui est stable et ce qui est qualifié, ne pas imposer la taxonomie interne du projet.

### Verdict

```text
FONCTION_SCIENTIFIQUE = FORTE
GAIN_MARGINAL_D_UNE_NOUVELLE_REGLE_AUTONOME = MODERE
MEILLEUR_SUPPORT = AMENDEMENT_MINIMAL_D_UNE_FORMULATION_EXISTANTE
```

Action proposée : **ne pas ajouter P4 comme sixième principe autonome ; si promotion décidée, fusionner sa phrase dans le noyau scientifique déjà présent.**

## P5 — R-038 : pré-vol de mutation de fichier/ref et contrôle terminal

### Déclencheur testé

Une mutation versionnée de fichier, branche ou ref est envisagée via GitHub/API/connecteur.

### Incident empirique `__invalid__`

Le 19 août, une mauvaise invocation GitHub a créé un fichier parasite `__invalid__`. La réaction correcte a été : suspendre les mutations, relire l’état, supprimer la pièce accidentelle, vérifier son absence et conserver les commits de correction comme provenance.

L’incident montre que la réversibilité de Git ne remplace pas le pré-vol : elle a limité le dommage, mais n’a pas empêché le travail parasite.

### Incidents de #139

Pendant l’audit actuel, deux appels d’écriture ont été répétés avec un SHA invalide avant retour strict en lecture. Les deux `409` n’ont pas muté le dépôt, mais ils reproduisent la même sous-application : la règle de relecture de l’état/SHA était connue sans être suffisamment proche du point d’action.

### Antécédent fonctionnel

#134 avait déjà extrait un pré-vol agentique : classifier la cible, annoncer l’effet matériel, lire contenu/SHA lorsqu’il s’agit d’un fichier, refuser un diff vide, effectuer une mutation de la bonne classe, puis contrôler son effet.

### Borne nécessaire

Le SHA n’est pas pertinent pour tous les actes GitHub. Ajouter un commentaire append-only n’exige pas le même contrat que remplacer un fichier. La formulation doit donc viser les **mutations de fichier/ref ou autres opérations dont l’état courant conditionne l’écriture**, et non tout appel API indistinctement.

### Verdict

```text
FONCTION_DISTINCTE = OUI
INCIDENTS_DIRECTS = OUI
SOUS_APPLICATION_REPETEE = OUI
GAIN_MARGINAL = TRES_FORT_POUR_AGENT_MUTATEUR
MECANISATION_PARTIELLE = SOUHAITABLE
```

Action proposée : **P5 reste candidate forte, avec formulation bornée aux mutations qui dépendent de l’état courant ; mécaniser read-back/no-op lorsque l’interface le permet.**

## Comparaison finale

| Candidate | Preuve empirique | Gain marginal dans AGENTS | Risque de sur-extension | Verdict post-test |
|---|---|---:|---:|---|
| P1 / R-033 | ambiguïté structurelle directement démontrée ; dommage isolé moins net | fort aux décisions de haute autorité | moyen si appliqué à tout commentaire | conserver, portée étroite |
| P2 / R-034 | cas positifs + contre-cas causal #117 | très fort | faible si transition d’acte explicite | conserver fortement |
| P3 / R-032 | α4/α5, refus explicites de généralisation | fort | faible à moyen | conserver scientifiquement |
| P4 / R-025 | D1 + C10 ; fonction réelle | modéré car couverture déjà partielle | moyen si nouvelle taxonomie | fusionner dans formulation existante |
| P5 / R-038 | `__invalid__` + répétitions #139 | très fort | moyen si étendu à tout appel API | conserver, borner + mécaniser |

## Requalification de la recommandation

Le contre-test ne soutient plus exactement cinq **ajouts autonomes**. Il soutient cinq fonctions, mais quatre mouvements textuels seulement :

```text
A. ajouter P1 sous forme étroite pour décisions haute autorité ;
B. ajouter P2 comme règle de portée exacte des autorisations ;
C. ajouter P3 comme règle scientifique de non-détection discriminante ;
D. fusionner P4 dans la formulation scientifique déjà existante ;
E. ajouter P5 comme pré-vol borné des mutations dépendant de l'état courant,
   avec mécanisation partielle lorsque possible.
```

Ainsi :

```text
DELTA_FONCTIONNEL = 5 fonctions
NOUVELLES_UNITES_TEXTUELLES_AUTONOMES = 4 au plus
P4 = AMENDEMENT_DU_NOYAU_EXISTANT
ARCHITECTURE_LOCALE_LARGE = TOUJOURS_NON_JUSTIFIEE
AGENTS_MODIFIE = NON
DECISION_HUMAINE_DE_PROMOTION = TOUJOURS_REQUISE
```

## Statut

```text
CONTRE_TEST_EMPIRIQUE_P1_P5 = EFFECTUE
MATERIAU_CONVERSATIONNEL = UTILISE_COMME_DONNEE_DE_TRAJECTOIRE
VALIDATION_CAUSALE_RETROSPECTIVE = NON_REVENDIQUEE
RECOMMANDATION = DELTA_MINIMAL_REQUALIFIE
PROMOTION_NORMATIVE = NON_EFFECTUEE
MERGE_#139 = NON_AUTORISE
```
