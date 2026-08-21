# Proposition de portée post-audit — delta minimal à soumettre

## Fonction

Ce document prépare une **décision humaine de portée** après l’audit #139. Il compare les fonctions suffisamment soutenues par la matrice à ce que `AGENTS.md` sur `main` porte déjà.

Il ne modifie pas `AGENTS.md` et ne vaut pas ratification.

Question testée :

> Si l’on retire la formulation candidate parce qu’une règle actuelle porte déjà sa fonction, l’agent perd-il un déclencheur, une distinction, une limite d’autorité ou une protection contre un incident réellement observé ?

Si la réponse est non, aucune nouvelle inscription n’est proposée.

## 1. Fonctions déjà suffisamment portées sur `main`

Le `AGENTS.md` courant porte déjà substantiellement :

- `R-001` — vert machine ≠ validation scientifique ;
- `R-002` — reproduire la cause d’un rouge avant attribution ;
- `R-004` — point d’entrée ≠ autorité ;
- `R-005` — ne pas réécrire un état historique pour simuler le courant ;
- `R-007` — nom stable + Git, avec pièces probatoires distinctes ;
- `R-016` — ne pas propager automatiquement un état entre chantiers ;
- `R-020` — frontières scientifiques/irréversibles humaines et opérations techniques autorisées ;
- `R-023` — activité et permissions C7 distinctes ;
- `R-026` — cible/transformation/régime/échelle-modèle/tolérance/rupture ;
- `R-027` — cible / accès / constitution ;
- `R-028` — conclusions bornées au domaine instruit ;
- `R-029` — typage des chemins lorsqu’il change l’argument ;
- `R-030` — vocabulaire disciplinaire prioritaire ;
- `R-031` — résultat / soutien / verdict ;
- `R-035` — contrôle avant suppression/déplacement/déclassement ;
- `R-036` — passage inter-domaines par réinstruction, sans propagation du verdict ;
- `R-037` — conservation des négatifs/refus/suspensions ;
- une partie importante de `R-038` — branche/worktree, PR bornée, pas de main direct, CI ≠ merge.

Verdict : **ne pas recopier ces fonctions par principe**. Les éventuels écarts doivent être traités seulement là où un incident ou une lacune de déclenchement est établi.

## 2. Lacunes marginales fortes

### P1 — R-033 : provenance, garantie, autorité, ratification humaine

**Couverture actuelle : partielle.**

Le routage documentaire est présent, mais la protection suivante manque :

```text
un commentaire/commit sous le compte auteur
≠ preuve suffisante de ratification humaine
lorsqu'un agent peut écrire via ce compte
```

Cette lacune a un effet réel sur les décisions de forte autorité.

**Gain marginal : fort.**

Formulation minimale candidate :

> Ne pas inférer une ratification humaine de la seule identité du compte GitHub auteur lorsqu’un agent peut agir via ce compte. Pour une décision scientifique, irréversible ou de forte autorité, exiger une intervention humaine explicite ou une provenance qui l’établit réellement.

**Support candidat :** noyau gouvernance agentique, probablement racine.

**Statut : `CANDIDAT_PROMOTION_FORTE / DECISION_HUMAINE_REQUISE`.**

### P2 — R-034 : portée exacte d’une décision

**Couverture actuelle : partielle.**

`AGENTS.md` énumère les frontières humaines, mais n’explicite pas suffisamment la non-transitivité : une qualification ou clôture locale ne vaut pas propagation, exécution, mutation ou merge.

#117 fournit un contre-cas causal ; α3–α5 fournissent les cas positifs.

**Gain marginal : fort.**

Formulation minimale candidate :

> Une décision ou autorisation ne couvre que la nature d’acte, l’objet et la portée qu’elle explicite. Qualifier, clore, valider ou fusionner une étape n’autorise pas automatiquement une exécution, propagation, mutation ou étape suivante d’une autre nature.

**Support candidat :** racine, proche des frontières d’autorité.

**Statut : `CANDIDAT_PROMOTION_FORTE / DECISION_HUMAINE_REQUISE`.**

### P3 — R-032 : non-détection discriminante

**Couverture actuelle : insuffisamment explicite.**

Le noyau impose cible/régime/tolérance et rang probatoire, mais ne dit pas explicitement qu’une absence de signal n’est informative que si le test pouvait voir la famille d’alternatives pertinente.

**Gain marginal : scientifique réel.**

Formulation minimale candidate :

> Une non-détection ne soutient un maintien ou une exclusion que pour une famille de variations effectivement testable par le dispositif dans le domaine déclaré. Une borne sur une valeur ne devient pas automatiquement une borne sur sa variation.

**Support candidat :** règle scientifique, racine ou support scientifique local selon décision d’architecture.

**Statut : `CANDIDAT_PROMOTION_SCIENTIFIQUE_FORTE / DECISION_HUMAINE_REQUISE`.**

### P4 — R-025 : constance ≠ stabilisation

**Couverture actuelle : proche mais non explicite.**

Le `AGENTS.md` demande de qualifier un énoncé de constance ou stabilisation, mais ne formule pas directement la distinction qui a motivé D1.

**Gain marginal : modéré à fort.**

Formulation minimale candidate :

> Ne pas confondre constance de la cible, stabilisation d’un accès/estimateur/régime et maintien produit par un mécanisme ; préciser lequel est effectivement soutenu.

**Support candidat :** section scientifique existante.

**Statut : `CANDIDAT_PROMOTION_SCIENTIFIQUE / DECISION_HUMAINE_REQUISE`.**

### P5 — R-038 : pré-vol SHA / no-op / contrôle terminal

**Couverture actuelle : partielle.**

La discipline de branche/PR est présente, mais le comportement empirique de #139 montre une lacune opérationnelle : l’agent peut tenter plusieurs écritures sans relire le SHA ou répéter une action refusée.

**Gain marginal : fort pour les agents mutateurs.**

Formulation minimale candidate :

> Avant une mutation versionnée : identifier cible et fonction, relire l’état/SHA courant, choisir l’action correspondant à la classe de cible, éviter une mutation sans effet, puis contrôler l’état terminal.

**Support candidat :** section Git/mutations ; à combiner avec mécanisation éventuelle plutôt qu’à multiplier en prose.

**Statut : `CANDIDAT_PROMOTION_OPERATIONNELLE / MECANISATION_PARTIELLE_PREFERABLE`.**

## 3. Lacunes réelles mais support racine non démontré

### R-009 — représentation de la science vivante

La fonction est fortement soutenue, mais une règle racine détaillée risquerait de transformer un problème de reprise en taxonomie générale.

**Proposition :** ne pas promouvoir en racine à ce stade. Lorsqu’un support prétend représenter l’état d’un domaine, exiger localement qu’il expose question actuelle, investigation, acquis/négatifs, blocages, décision ouverte et condition de reprise.

**Statut : `SUPPORT_LOCAL_A_DECIDER`.**

### R-039 — Human-First

Le besoin est réel, mais `AGENTS.md` actuel est déjà largement lisible et le test aveugle #137 est confondu.

Le principe minimal :

```text
intitulé humain porte le sens
code/ID reste secondaire
```

peut produire un gain, mais l’audit ne démontre pas encore qu’une nouvelle ligne racine change davantage le comportement qu’une bonne rédaction des surfaces elles-mêmes.

**Proposition :** tester dans les nouveaux supports et dans la vue 2D avant promotion durable.

**Statut : `CANDIDAT_BORNE / PAS_PROMOTION_IMMEDIATE`.**

### R-019 — interventions humaines typées

La fonction est fortement soutenue dans les conversations et A3. Cependant, son inscription textuelle peut elle-même créer un risque : un agent pourrait sur-interpréter toute phrase humaine et contester une instruction claire.

**Proposition :** si promotion, garder une formulation très courte et déclenchée seulement lorsque le type d’intervention change réellement l’action.

**Statut : `CANDIDAT_BORNE / DECISION_HUMAINE_REQUISE`.**

## 4. Unités à laisser hors du delta `AGENTS.md`

Ne pas promouvoir à partir de #139 :

- `R-006` — instrument documentaire régional ;
- `R-010` — audit de second ordre, à garder événementiel dans les protocoles d’audit ;
- `R-011` — contre-audit indépendant pour audits globaux ;
- `R-012` — exhaustivité dans corpus auditable défini ;
- `R-013` — triangulation ciblée ;
- `R-014` — requalification contextuelle d’audits antérieurs ;
- `R-015` — symétrie critique, déjà portée par le programme d’audit ;
- `R-017` — principe de non-prolifération déjà présent sous une forme suffisante ;
- `R-018` — capture légère en shadow ;
- `R-021` — mieux porté par mécanisme/read-back que par nouvelle prose ;
- `R-022` — mécanisme CI local ;
- `R-024` — critère de phase outillage, non règle d’intervention quotidienne.

## 5. Test de compression du delta

La liste brute des candidats P1–P5 peut encore être comprimée.

### P1 + P2 ne fusionnent pas

`R-033` demande : **qu’est-ce que la provenance prouve ?**  
`R-034` demande : **qu’est-ce que cette décision autorise ?**

Un agent peut connaître correctement la provenance humaine et néanmoins sur-propager la portée de la décision. Les deux fonctions doivent rester distinctes.

### P3 ne se réduit pas à R-026/R-031

Un énoncé nul peut être correctement indexé et son rang probatoire correctement séparé, tout en restant non discriminant si le dispositif ne pouvait pas voir l’alternative. La non-détection conserve donc sa fonction propre.

### P4 ne se réduit pas à R-026

L’indexation ne corrige pas une confusion entre l’objet et le processus qui stabilise son accès. D1 garde donc un gain propre.

### P5 ne doit pas devenir une seconde doctrine Git

Le delta utile est le **pré-vol opérationnel** manquant. Branche, PR, main et merge sont déjà couverts ; ne pas les répéter.

## 6. Delta minimal recommandé à soumettre

Si une décision humaine devait aujourd’hui autoriser un delta dans `AGENTS.md`, la proposition la plus compacte issue de #139 serait de considérer seulement cinq ajouts/fusions ciblés :

```text
1. provenance apparente != ratification humaine effective        [R-033]
2. autorisation bornée à nature d'acte / objet / portée          [R-034]
3. non-détection seulement si test discriminant                  [R-032]
4. constance de cible != stabilisation d'accès/mécanisme         [R-025]
5. pré-vol SHA / no-op / contrôle terminal pour mutation         [R-038]
```

Et trois décisions secondaires, non nécessaires au même moment :

```text
R-009 science vivante -> support local à décider
R-039 Human-First -> poursuivre test par usage
R-019 intervention humaine typée -> formulation courte seulement si gain confirmé
```

Cette recommandation est **plus petite** que le prototype #138. #138 reste un témoin expérimental utile, mais n’est pas utilisé ici comme autorité normative.

## 7. Options de décision humaine

### Option A — aucun delta maintenant

Conserver `main` tel quel et observer si les cinq lacunes reproduisent encore des erreurs.

Avantage : coût documentaire nul.  
Risque : P1/P2/P5 ont déjà des incidents ou conditions matérielles assez fortes pour que l’attente apporte peu d’information nouvelle.

### Option B — delta minimal P1/P2/P5 seulement

Promouvoir uniquement les trois protections agentiques les plus directement reliées à des incidents : provenance/ratification, portée exacte des autorisations, pré-vol de mutation.

Avantage : très faible augmentation de charge cognitive ; cible les défaillances d’action.

Limite : ne traite pas les deux lacunes scientifiques P3/P4.

### Option C — delta minimal complet P1–P5

Ajouter les trois protections agentiques + les deux protections scientifiques D1/P27.

Avantage : couvre les lacunes marginales fortes démontrées par l’audit.

Limite : augmente légèrement le noyau racine ; nécessite vérifier la meilleure localisation des deux règles scientifiques.

### Option D — architecture locale plus large

Créer/promouvoir des `AGENTS.md` locaux et distribuer davantage les règles.

Cette option a été expérimentée dans #138, mais #139 ne démontre pas qu’elle soit nécessaire pour porter les cinq lacunes marginales. Elle introduit une décision d’architecture supplémentaire et n’est donc **pas recommandée comme premier mouvement**.

## 8. Recommandation de l’audit

La meilleure balance gain/coût issue de la matrice est :

```text
RECOMMANDATION = OPTION_C
SOUS_CONDITION = décision humaine explicite de promotion
```

Motif : P1/P2/P5 protègent des erreurs d’action déjà observées ; P3/P4 ajoutent deux fonctions scientifiques non réductibles aux formulations présentes ; le tout reste un delta court et évite une nouvelle architecture documentaire.

Cette recommandation **n’est pas une autorisation** de modifier `AGENTS.md`.

## Statut

```text
PROPOSITION_PORTEE = INSTRUITE
DELTA_RECOMMANDE = P1-P5
AGENTS_MODIFIE = NON
DECISION_HUMAINE = REQUISE
OPTION_LOCALE_LARGE = NON_RECOMMANDEE_EN_PREMIER_MOUVEMENT
MERGE_#139 = NON_AUTORISE
```
