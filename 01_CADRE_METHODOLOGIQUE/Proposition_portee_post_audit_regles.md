# Proposition de portée post-audit — delta minimal à soumettre

## Fonction

Ce document prépare une **décision humaine de portée** après l’audit #139. Il compare les fonctions suffisamment soutenues par la matrice à ce que `AGENTS.md` sur `main` porte déjà.

Il ne modifie pas `AGENTS.md` et ne vaut pas ratification.

La proposition a été requalifiée après confrontation au matériau empirique conversationnel fourni par l’auteur et aux pièces du dépôt dans `Contre_test_empirique_delta_P1_P5.md`.

Question testée :

> Si l’on retire la formulation candidate parce qu’une règle actuelle porte déjà sa fonction, l’agent perd-il un déclencheur, une distinction, une limite d’autorité ou une protection contre un incident réellement observé ?

Une seconde question est désormais ajoutée :

> Si la fonction est réelle, exige-t-elle une **nouvelle unité textuelle autonome**, ou peut-elle être portée plus sobrement par une formulation déjà existante ou par un mécanisme technique ?

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
- une partie importante de `R-038` — branche/worktree, PR bornée, pas de `main` direct, CI ≠ merge.

Verdict : **ne pas recopier ces fonctions par principe**. Les écarts doivent être traités seulement là où un incident, une sous-application ou une lacune de déclenchement est établi.

## 2. Delta fonctionnel requalifié

Le contre-test soutient toujours **cinq fonctions utiles**, mais plus cinq nouvelles règles autonomes.

### P1 — R-033 : provenance apparente ≠ ratification humaine effective

**Couverture actuelle : partielle.**

Le dispositif permet à un agent d’écrire sur GitHub via le compte connecté. L’identité apparente du compte auteur ne suffit donc pas, par construction, à établir que l’acte a été directement posé ou ratifié par l’humain.

Le matériau empirique montre effectivement des actions « ajoutées sur GitHub via l’outil dédié » ; en revanche, aucun épisode n’a encore été isolé où **cette ambiguïté seule** aurait produit un verdict scientifique erroné. Le soutien est donc structurel fort, mais le dommage historique direct est moins net que pour P2/P5.

Formulation candidate, volontairement étroite :

> Pour une décision scientifique, irréversible ou de forte autorité, ne pas inférer une ratification humaine de la seule identité du compte GitHub auteur lorsqu’un agent peut agir via ce compte ; exiger une intervention humaine explicite ou une provenance qui l’établit réellement.

**Condition de silence :** commentaire informatif/technique sans effet d’autorité, ou provenance humaine déjà établie.

**Statut : `CANDIDAT_PROMOTION_FORTE_MAIS_ETROITE / DECISION_HUMAINE_REQUISE`.**

### P2 — R-034 : portée exacte d’une décision

**Couverture actuelle : partielle.**

`AGENTS.md` énumère les frontières humaines, mais n’explicite pas assez la non-transitivité d’une décision vers un acte d’une autre nature.

Le soutien est désormais particulièrement fort :

- le matériau conversationnel contient des autorisations GitHub correctement utilisées localement sans en déduire une autorisation générale de restructuration ;
- α3–α5 autorisent une clôture locale sans propagation ni fusion ;
- #117 fournit un contre-cas causal : un diagnostic de déclassement a été converti trop vite en suppression matérielle.

Formulation candidate :

> Une décision ou autorisation ne couvre que la nature d’acte, l’objet et la portée qu’elle explicite. Qualifier, clore, valider ou fusionner une étape n’autorise pas automatiquement une exécution, propagation, mutation ou étape suivante d’une autre nature.

**Condition de silence :** une autorisation peut couvrir plusieurs micro-actes techniques si cette séquence appartient explicitement à la même opération bornée.

**Statut : `CANDIDAT_PROMOTION_TRES_FORTE / DECISION_HUMAINE_REQUISE`.**

### P3 — R-032 : non-détection discriminante

**Couverture actuelle : insuffisamment explicite.**

L’indexation cible/régime/tolérance et la séparation résultat/soutien/verdict ne suffisent pas logiquement à établir qu’une absence de signal est informative.

α4 et α5 fournissent des épreuves scientifiques directes :

- une dérive linéaire lente et une modulation annuelle compatibles avec zéro peuvent constituer une non-détection discriminante **dans les familles et domaines déclarés** ;
- elles n’autorisent ni invariance temporelle universelle, ni extension aux oscillations/transitoires non testés ;
- une non-détection locale spectroscopique ne se généralise pas à tout le ciel ni indépendamment des calibrations et systématiques.

Formulation candidate :

> Une non-détection ne soutient un maintien ou une exclusion que pour une famille de variations effectivement testable par le dispositif dans le domaine déclaré. Une borne sur une valeur ne devient pas automatiquement une borne sur sa variation.

**Statut : `CANDIDAT_PROMOTION_SCIENTIFIQUE_FORTE / DECISION_HUMAINE_REQUISE`.**

### P4 — R-025 : constance ≠ stabilisation

**Fonction scientifique : fortement soutenue.**

D1 distingue explicitement :

```text
constance de l’objet
!= stabilisation de l’accès
!= mode de constitution
```

C10 fournit en outre un cas matériel : `v(t)` peut devenir pratiquement fixe alors que le système qui produit cette quasi-fixité reste énergétiquement inadmissible. La stabilité de la quantité accessible ne suffit donc pas à qualifier le mécanisme qui la porte.

Cependant, `AGENTS.md` porte déjà deux protections proches :

- expliciter cible/transformation/régime pour les énoncés de constance ou stabilisation ;
- ne pas confondre propriété de la cible, qualité de l’accès et mode de constitution.

Le contre-test réduit donc le **gain marginal d’une nouvelle ligne autonome**.

Proposition : **ne pas créer une règle supplémentaire**. Si une promotion est décidée, intégrer une courte précision à la formulation scientifique existante, par exemple :

> Ne pas identifier constance de la cible, stabilisation de l’accès/régime et maintien produit par un mécanisme.

**Statut : `FONCTION_FORTE / AMENDEMENT_DU_NOYAU_EXISTANT_PREFERE`.**

### P5 — R-038 : pré-vol des mutations dépendant de l’état courant

**Couverture actuelle : partielle.**

La branche/PR et la séparation CI/merge sont déjà présentes. Le manque empirique concerne le pré-vol au point d’écriture.

Deux familles d’incidents l’établissent :

- le 19 août, une mauvaise invocation a créé un fichier parasite `__invalid__`; la correction correcte a exigé suspension des mutations, relecture, suppression et contrôle terminal ;
- pendant #139, deux appels avec SHA invalide ont été répétés avant retour strict en lecture ; les `409` n’ont pas muté le dépôt mais ont reproduit la sous-application du pré-vol.

La formulation doit rester bornée : un commentaire append-only n’exige pas le même contrat qu’un remplacement de fichier ou une mutation de ref.

Formulation candidate :

> Avant une mutation de fichier, ref ou autre objet dont l’écriture dépend de son état courant : identifier cible et fonction, relire l’état/SHA applicable, choisir l’action de la bonne classe, éviter une mutation sans effet, puis contrôler l’état terminal.

**Support complémentaire :** mécaniser read-back/no-op lorsque l’interface le permet, sans transformer un contrôle technique en autorité scientifique.

**Statut : `CANDIDAT_PROMOTION_OPERATIONNELLE_FORTE / MECANISATION_PARTIELLE_PREFERABLE`.**

## 3. Lacunes réelles mais support racine non démontré

### R-009 — représentation de la science vivante

La fonction est fortement soutenue, mais une règle racine détaillée risquerait de transformer un problème de reprise en taxonomie générale.

**Proposition :** lorsqu’un support prétend représenter l’état d’un domaine, exiger localement qu’il expose question actuelle, investigation, acquis/négatifs, blocages, décision ouverte et condition de reprise.

**Statut : `SUPPORT_LOCAL_A_DECIDER`.**

### R-039 — Human-First

Le besoin est réel, mais une nouvelle ligne racine n’est pas encore démontrée comme supérieure à une bonne conception des surfaces elles-mêmes.

**Proposition :** poursuivre le test dans les nouveaux supports et dans le prototype 2D avant promotion durable.

**Statut : `CANDIDAT_BORNE / PAS_PROMOTION_IMMEDIATE`.**

### R-019 — interventions humaines typées

La fonction est bien soutenue par le matériau empirique : les propositions ne doivent pas être transformées automatiquement en ordres. Mais son inscription textuelle peut produire le défaut inverse et conduire l’agent à contester une instruction claire.

**Proposition :** si promotion ultérieure, formulation très courte et déclenchée seulement lorsque le type d’intervention change réellement l’action.

**Statut : `CANDIDAT_BORNE / DECISION_HUMAINE_REQUISE`.**

## 4. Unités à laisser hors du delta `AGENTS.md`

Ne pas promouvoir à partir de #139 :

- `R-006` — instrument documentaire régional ;
- `R-010` — audit de second ordre, événementiel ;
- `R-011` — contre-audit indépendant pour audits globaux ;
- `R-012` — exhaustivité dans corpus auditable défini ;
- `R-013` — triangulation ciblée ;
- `R-014` — requalification contextuelle d’audits antérieurs ;
- `R-015` — symétrie critique, portée par le programme d’audit ;
- `R-017` — non-prolifération déjà présente sous une forme suffisante ;
- `R-018` — capture légère en shadow ;
- `R-021` — mieux porté par read-back/mécanisme que par une ligne supplémentaire ;
- `R-022` — mécanisme CI local ;
- `R-024` — critère de phase outillage, non règle quotidienne.

## 5. Test de compression

### P1 et P2 restent distinctes

`R-033` demande : **qu’est-ce que la provenance prouve ?**  
`R-034` demande : **qu’est-ce que cette décision autorise ?**

Une provenance correcte n’empêche pas une sur-propagation de la portée.

### P3 reste distincte de R-026/R-031

Un résultat nul peut être correctement indexé et correctement classé comme résultat tout en restant non discriminant si le dispositif ne pouvait pas voir l’alternative pertinente.

### P4 est fonctionnellement distincte mais textuellement absorbable

La distinction constance/stabilisation est réelle. Ce qui n’est plus soutenu est la nécessité d’en faire **une nouvelle ligne autonome**, car le noyau actuel contient déjà les deux prémisses nécessaires.

### P5 ne doit pas devenir une seconde doctrine Git

La branche, la PR, `main` et le merge sont déjà couverts. Seul le pré-vol de la mutation dépendant de l’état courant apporte un gain marginal.

## 6. Delta minimal requalifié à soumettre

Le résultat du contre-test est :

```text
DELTA_FONCTIONNEL = 5 fonctions

AJOUTS_TEXTUELS_AUTONOMES_CANDIDATS =
  P1 provenance apparente != ratification humaine effective
  P2 autorisation bornée à nature d'acte / objet / portée
  P3 non-détection seulement si dispositif discriminant
  P5 pré-vol des mutations dépendant de l'état courant

AMENDEMENT_DU_NOYAU_EXISTANT =
  P4 constance de cible != stabilisation d'accès/régime/mécanisme
```

La recommandation reste **plus petite que #138**. Aucun `AGENTS.md` local supplémentaire n’est nécessaire pour porter ce delta.

## 7. Options de décision humaine requalifiées

### Option A — aucun delta maintenant

Conserver `main` tel quel et observer.

Avantage : aucun coût documentaire.  
Limite : P2 et P5 ont déjà des contre-cas/incidents suffisamment directs pour que l’attente apporte peu d’information sur leur utilité.

### Option B — protections agentiques P1/P2/P5

Ajouter seulement les trois protections de gouvernance/mutation.

Avantage : delta très court et centré sur l’action.  
Limite : laisse hors noyau la protection scientifique P3.

### Option C requalifiée — quatre ajouts + un amendement

- ajouter P1, P2, P3 et P5 sous leurs formes bornées ;
- intégrer P4 à la formulation scientifique déjà présente plutôt que créer une ligne supplémentaire.

Avantage : conserve les cinq fonctions démontrées en minimisant la sédimentation textuelle.  
Limite : P1 repose davantage sur une ambiguïté structurelle démontrée que sur un dommage historique isolé.

### Option D — architecture locale plus large

Créer/promouvoir plusieurs `AGENTS.md` locaux.

#139 ne démontre toujours pas cette nécessité. Cette option ajoute une décision architecturale indépendante et reste **non recommandée comme premier mouvement**.

## 8. Recommandation actuelle de l’audit

```text
RECOMMANDATION = OPTION_C_REQUALIFIEE
SOUS_CONDITION = décision humaine explicite de promotion
```

Motif :

- P2 et P5 ont des incidents/contre-cas directs ;
- P3 a des épreuves scientifiques explicites et un gain logique non redondant ;
- P1 protège une ambiguïté réelle de provenance à haute autorité mais doit rester étroite ;
- P4 est scientifiquement solide mais ne justifie plus une nouvelle unité textuelle autonome.

Cette recommandation **n’est pas une autorisation** de modifier `AGENTS.md`.

## Statut

```text
PROPOSITION_PORTEE = REQUALIFIEE_APRES_CONTRE_TEST_EMPIRIQUE
DELTA_FONCTIONNEL = P1-P5
AJOUTS_AUTONOMES_MAX = P1 + P2 + P3 + P5
P4 = AMENDEMENT_NOYAU_EXISTANT
AGENTS_MODIFIE = NON
DECISION_HUMAINE = REQUISE
OPTION_LOCALE_LARGE = NON_RECOMMANDEE_EN_PREMIER_MOUVEMENT
MERGE_#139 = NON_AUTORISE
```
