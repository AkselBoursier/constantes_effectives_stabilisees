# Proposition de portée post-audit — état après second ordre empirique

## Fonction

Ce document prépare une **décision humaine de portée** après intégration de l’étude exhaustive de second ordre du matériau empirique. Il ne modifie pas `AGENTS.md`, ne vaut pas ratification et ne vaut pas autorisation de merge.

L’ancienne proposition P1–P5 est conservée comme étape probatoire antérieure, mais elle n’est plus le delta terminal : le matériau empirique a fait émerger trois fonctions supplémentaires `R-040–R-042`.

État analytique : 39 unités de base + 3 unités de second ordre = 42 unités ; 44 relations de base + 8 relations de second ordre = 52 relations.

## 1. Test de portée appliqué

Pour chaque fonction candidate, quatre questions doivent être séparées :

1. la fonction est-elle réellement soutenue ?
2. le support actuel la porte-t-il déjà suffisamment ?
3. une formulation directe dans `AGENTS.md` apporterait-elle un déclencheur ou une borne réellement manquants ?
4. faut-il encore une exposition dans un régime indépendant avant toute promotion ?

Une fonction peut donc être forte sans appeler de nouvelle ligne agentique.

## 2. Fonctions anciennement P1–P5

### R-033 — provenance apparente ≠ ratification humaine

**Preuve :** ambiguïté structurelle forte ; dommage direct isolé non établi.

**Portée recommandée si promotion décidée :** seulement décisions scientifiques, irréversibles ou de forte autorité. Ne pas exiger une archéologie de provenance pour les commentaires ordinaires.

**Statut : `DECISION_HUMAINE_REQUISE / PORTEE_ETROITE`.**

### R-034 — portée exacte d’une décision

**Preuve : très forte.** α3–α5 fournissent des cas positifs ; #117 fournit un contre-cas causal.

Formulation fonctionnelle candidate : une décision n’autorise que la nature d’acte, l’objet et la portée qu’elle couvre ; qualification, clôture, exécution, propagation, mutation et merge ne sont pas transitifs par défaut.

**Statut : `CANDIDATE_PROMOTION_TRES_FORTE`.**

### R-032 — non-détection discriminante

**Preuve scientifique : forte.** Une absence de signal ne soutient une exclusion ou un maintien que pour les familles réellement accessibles au dispositif dans le domaine déclaré.

**Statut : `CANDIDATE_PROMOTION_SCIENTIFIQUE_FORTE`.**

### R-025 — constance ≠ stabilisation

**Fonction : forte**, mais le noyau scientifique actuel porte déjà une grande partie de la distinction via cible/accès/constitution et indexation du maintien.

**Recommandation :** amendement minimal du noyau existant si nécessaire, pas nouvelle ligne autonome.

### R-038 — pré-vol des mutations dépendant de l’état courant

**Preuve : très forte** par incidents directs et sous-application reproduite.

**Portée :** mutations de fichier/ref ou objets dont l’écriture dépend de l’état courant ; pas tous les appels append-only.

**Statut : `CANDIDATE_PROMOTION_OPERATIONNELLE_FORTE / MECANISATION_PARTIELLE`.**

## 3. Trois fonctions révélées par le second ordre empirique

### R-040 — intégrité des transformations de représentation

**Preuve : forte dans le matériau et reproduite dans le dépôt.**

Le besoin est distinct : contrôler le raccord lorsqu’une représentation devient l’entrée d’une autre étape.

```text
justesse locale de la représentation
!=
suffisance pour l’usage aval
```

**Mais** le matériau montre aussi le risque de sur-extension : toute traduction ou reformulation ne justifie pas un audit de transmission.

**Recommandation actuelle : `PAS_DE_PROMOTION_AGENTIQUE_IMMEDIATE`.** Conserver la fonction dans l’audit et l’exposer sur le prochain raccord réel avant décision de portage quotidien.

### R-041 — statut probatoire d’une règle

**Preuve : très forte et répétée.**

La fonction protège précisément l’audit des règles : `formulée`, `appliquée`, `observée`, `mise à l’épreuve`, `soutenue/falsifiée`, `ratifiée`, `promue` ne sont pas équivalents.

**Recommandation :** la fonction peut gouverner immédiatement les audits et décisions de promotion. Son inscription dans `AGENTS.md` quotidien reste une décision de support distincte ; une formulation locale méthodologique peut suffire si elle est nécessaire.

**Statut : `FONCTION_PROMOUVABLE_DANS_REGIME_AUDIT / SUPPORT_AGENTIQUE_A_DECIDER`.**

### R-042 — remontée de résolution

**Preuve : forte localement, transport partiel seulement.**

Après résolution : solution locale ≠ connaissance causale ≠ apprentissage transférable. La fonction évite que le pourquoi causal soit perdu tout en refusant de transformer chaque correctif en règle.

**Recommandation actuelle : `PAS_DE_PROMOTION_TRANSVERSE`.** Exposer la fonction sur la prochaine résolution substantielle hors C7 ; si elle réduit réellement la répétition d’enquête sans produire de méta-travail disproportionné, réévaluer son portage.

## 4. Fonctions à ne pas transformer en nouvelles lignes

Le régime d’une règle est déjà l’architecture de la matrice ; ne pas créer une règle auto-référentielle supplémentaire.

Le cycle de vie d’une candidate est une trajectoire horizontale du dispositif, pas une nouvelle règle : émergence → exposition → contre-cas → qualification → décision de portée → promotion/amendement/régionalisation/abandon.

La procédure prospective C10 reste locale ; aucune prérégistration générale n’est soutenue.

## 5. Delta de portée requalifié

Le résultat n’est plus « quatre ajouts + un amendement ».

```text
CANDIDATS_DIRECTS_LES_PLUS_FORTS = R-034, R-032, R-038
CANDIDAT_ETROIT = R-033
AMENDEMENT_NUCLEUS_PREFERABLE = R-025
FONCTION_AUDIT_FORTE_SUPPORT_A_DECIDER = R-041
EXPOSITION_SUPPLEMENTAIRE_AVANT_PROMOTION = R-040, R-042
```

Cette hiérarchie est plus fidèle aux preuves qu’une promotion groupée.

## 6. Options de décision humaine

### Option A — ne promouvoir aucune règle maintenant

Conserver l’état 42/52 comme résultat d’audit et observer les prochaines expositions.

Avantage : sédimentation minimale. Limite : R-034/R-032/R-038 disposent déjà d’éléments assez forts pour que l’attente n’apporte peut-être que peu d’information marginale.

### Option B — delta minimal à preuve très forte

Examiner seulement R-034, R-032 et R-038 pour une formulation directe, avec R-025 comme amendement éventuel du noyau scientifique.

R-033, R-040, R-041 et R-042 restent hors promotion quotidienne.

### Option C — ajouter R-041 dans son régime méthodologique

Option B + portage explicite du statut probatoire des règles dans la surface méthodologique appropriée, sans en faire un protocole lourd de chaque tâche.

### Option D — architecture agentique plus large

Créer plusieurs nouveaux `AGENTS.md` ou une couche de gouvernance dédiée.

**Non soutenue par #139 comme premier mouvement.** Les fonctions étudiées ne justifient pas à elles seules cette sédimentation.

## 7. Recommandation de l’audit après second ordre

L’audit ne recommande plus une promotion groupée P1–P5.

La recommandation la plus défendable est maintenant :

```text
INSTRUIRE_OPTION_B_COMME_DELTA_MINIMAL
+
EXAMINER_SEPAREMENT_R-041_DANS_LE_REGIME_METHODOLOGIQUE
+
MAINTENIR_R-040_ET_R-042_EN_EXPOSITION_AVANT_PROMOTION
```

Cette recommandation reste une **proposition d’audit**, pas une décision humaine.

## 8. Condition avant toute mutation de `AGENTS.md`

Avant écriture normative :

- vérifier une dernière fois la couverture exacte de chaque fonction sur `main` ;
- formuler le delta sans duplication ;
- préserver les conditions de silence ;
- ne pas étendre la portée depuis le seul fait que la fonction est forte ;
- soumettre explicitement la promotion à décision humaine.

```text
AGENTS_MODIFIE = NON
PROMOTION = NON_EFFECTUEE
DECISION_HUMAINE = REQUISE
MERGE_#139 = NON_AUTORISE
```
