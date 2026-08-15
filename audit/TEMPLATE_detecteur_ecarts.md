# Template — détecteur d'écart entre règle déclarée et règle suivie

## Pourquoi ce template

Dans un projet de recherche mixte humain + LLM, le risque principal n'est pas
l'absence de règles mais leur **non-application invisible** : une règle écrite
dans un beau cadre fait plaisir, présente bien, et n'est pas suivie — sans que
rien ne le signale. Un humain fait la part entre ce qui est dit et ce qui est
fait ; un LLM, lisant le corpus, prend l'affirmation d'état pour un état réel.

Ce template exporte le **détecteur**, pas les règles. Il ne dit pas « voici P27 /
P28 » ; il dit « voici comment une règle déclare sa condition d'application et
comment le système signale qu'elle n'a pas été suivie ».

## Principe directeur

> Transformer chaque règle en assertion testable, et rendre l'écart visible au
> lieu de l'interdire.

Une règle non instrumentée n'est pas une règle : c'est une résolution.

## Les trois pièces

### 1. Registre des règles actives (`audit/regles_actives.md`)

Pour chaque règle nommée, trois champs obligatoires :

```text
incident daté          : quel événement réel a motivé la règle, et quand ;
violation observable   : quel fait compterait comme un écart ;
mécanisme de détection : qui ou quoi rend cet écart visible.
```

Une règle qui ne peut remplir ces trois champs est une **formulation
exploratoire**, sans autorité normative. Le registre se remplit par incidents
réels, jamais par anticipation.

### 2. Journal des écarts (`audit/Journal_ecarts_gouvernance.md`)

Consigne les écarts **constatés** comme données datées, non comme fautes :

```text
règle concernée ; écart constaté ; date de constat ; preuve interne ; réparation.
```

Un écart consigné n'annule pas la règle : il la transforme de résolution en
règle instrumentée. L'absence d'écart détecté ne vaut pas preuve d'application —
elle signifie seulement que le mécanisme déclaré n'a pas signalé.

### 3. Script de détection (`audit/audit_ecarts_regles.py`) + étape CI

Contrôles faibles mais réels, exécutés à chaque PR :

- une carte/couche versionnée doit nommer la version qu'elle remplace ;
- un document de décision doit référencer une issue ou le registre d'arbitrages ;
- une règle nommée doit avoir une date d'instauration et un mécanisme déclaré ;
- le registre des règles doit exister et porter les trois champs par règle.

Le script **signale, ne juge pas** : sévérité WARNING par défaut, ERROR seulement
si un mécanisme déclaré est brisé (cible absente). Fail-weak : il ne bloque pas
sur une différence d'interprétation.

## Deux familles de règles — ne pas les confondre

```text
règles de gouvernement (comment le corpus est gouverné) :
    testées par audit d'écart — ce template ;
règles de verdict (comment une conclusion scientifique est qualifiée) :
    testées par cas adversariaux et relecture humaine — hors de ce template.
```

Ne jamais tester une règle de gouvernement par une règle de verdict, ni
l'inverse. Le détecteur d'écart n'affirme pas qu'une règle de verdict est
appliquée ; il rappelle seulement que son test est d'une autre famille.

## Ce que ce template n'est pas

- pas une taxonomie de statuts ;
- pas une couche STATUTS_ACTIFS déguisée ;
- pas une preuve que les règles sont suivies ;
- pas un blocage automatique : il libère l'humain du rôle d'auditeur manuel en
  *surfacant* les écarts, la décision restant humaine.

## Contre-factuel minimal

Sans ce mécanisme : les règles s'accumulent, les écarts dit/fait ne sont nulle
part enregistrés, et un lecteur (humain fatigué ou LLM) prend les déclarations
pour des faits. Avec : chaque écart devient une donnée datée, et la règle cesse
d'être une résolution pour devenir une assertion testable.
