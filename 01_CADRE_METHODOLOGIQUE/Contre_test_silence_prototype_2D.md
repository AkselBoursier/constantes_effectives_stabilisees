# Contre-test de silence — prototype 2D local

## Fonction

Tester le prototype contre des cas où ses boucles **ne doivent pas se déclencher**. Ce document complète `Test_gain_guidage_prototype_2D.md` afin d’éviter un test uniquement confirmatoire.

## S1 — transformation sans effet aval

Situation : un texte est reformulé pour lisibilité, sans sélection de contenu ni changement de fonction ; les dimensions nécessaires à l’usage aval sont conservées.

Attendu : `R-040` reste silencieuse après contrôle minimal du delta ; aucun `R-010` n’est ouvert.

Résultat prototype : la ligne « raccord de représentation » contient explicitement `silence si aucune perte pertinente` et conditionne la descente vers le second ordre à un effet sur prémisse, sélection ou capacité de détection.

**Verdict S1 = PASS.**

## S2 — propriété directement observable

Situation : une règle technique porte sur une identité directement observable, par exemple présence d’un SHA/version, sans prétention d’efficacité générale ni projet de promotion.

Attendu : `R-041` ne doit pas imposer un shadow adversarial lourd. L’observation directe peut suffire au statut borné correspondant ; aucun second ordre sans anomalie.

Résultat prototype : `R-041` se déclenche sur une prétention de test/validation/extension, et reste silencieuse pour l’usage ordinaire sans prétention probatoire. Le prototype ne contient aucune obligation d’expérimentation lourde universelle.

**Verdict S2 = PASS.**

## S3 — correctif local trivial

Situation : erreur locale déterministe, réversible, sans valeur de réutilisation distincte et dont la cause est immédiatement connue.

Attendu : ne pas déclencher `R-042` comme post-mortem systématique ; garder la correction locale.

Résultat prototype : `R-042` exige une résolution substantielle, coûteuse, récurrente ou causalement informative et s’arrête si aucune valeur de reprise distincte n’existe.

**Verdict S3 = PASS.**

## S4 — nouvel élément sans effet sur un ancien audit

Situation : une nouvelle publication ou information apparaît, mais elle ne change ni prémisse, ni exclusion, ni critère, ni portée de l’ancien audit.

Attendu : `R-014` ne déclenche pas `R-010`; l’audit antérieur reste conservé à son rang.

Résultat prototype : la ligne second ordre exige précisément un changement matériel de prémisse/exclusion/critère/portée et refuse la réflexivité permanente.

**Verdict S4 = PASS.**

## Résultat adversarial

```text
CAS_DE_SILENCE = 4
FAUX_DECLENCHEMENTS = 0
S1 = PASS
S2 = PASS
S3 = PASS
S4 = PASS
```

Le prototype réussit donc, dans cette passe contrôlée, à montrer non seulement quand monter d’un niveau mais aussi quand **ne pas monter**.

Cette réussite reste non aveugle et ne change pas le statut de sédimentation :

```text
GAIN_GUIDAGE_CONTROLE = SOUTENU
CONTRE_TEST_SILENCE = PASS
BLIND_TEST_AGENT_NEUF = REQUIS
PROMOTION_DURABLE = NON_ETABLIE
```
