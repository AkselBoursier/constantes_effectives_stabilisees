# Proposition de portée post-audit — état après second ordre empirique et tests agent neuf

## Fonction

Ce document prépare des **décisions humaines de portée** après intégration de l’étude exhaustive de second ordre du matériau empirique et des tests du prototype fonctionnel. Il ne modifie pas `AGENTS.md`, ne vaut pas ratification et ne vaut pas autorisation de merge.

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

Le risque de sur-extension reste réel : toute traduction ou reformulation ne justifie pas un audit de transmission.

Les tests agent neuf renforcent la fonction dans le cluster étudié : les agents ont correctement conservé la validité locale tout en refusant l’extrapolation cycle-wide, sans audit général automatique.

**Statut requalifié : `FONCTION_FORTE / EXPOSITION_ECOLOGIQUE_POSITIVE / PROMOTION_TRANSVERSE_NON_AUTORISEE`.**

### R-041 — statut probatoire d’une règle

**Preuve : très forte et répétée.**

La fonction protège précisément l’audit des règles : `formulée`, `appliquée`, `observée`, `mise à l’épreuve`, `soutenue/falsifiée`, `ratifiée`, `promue` ne sont pas équivalents.

Les six réponses agent neuf des Phases I et II ont toutes conservé la distinction centrale `application sans incident != test`, sans erreur critique.

**Recommandation :** la fonction peut gouverner immédiatement les audits et décisions de promotion. Son inscription dans `AGENTS.md` quotidien reste une décision de support distincte ; une formulation locale méthodologique peut suffire si elle est nécessaire.

**Statut : `FONCTION_PROMOUVABLE_DANS_REGIME_AUDIT / SUPPORT_AGENTIQUE_A_DECIDER`.**

### R-042 — remontée de résolution

**Preuve : forte localement, transport partiel seulement.**

Après résolution : solution locale ≠ connaissance causale ≠ apprentissage transférable. La fonction évite que le pourquoi causal soit perdu tout en refusant de transformer chaque correctif en règle.

Les tests agent neuf montrent que cette séparation est utilisable dans le dépôt réel sans provoquer une généralisation automatique ni une création d’outil par défaut.

**Statut requalifié : `FONCTION_DISTINCTE / EXPOSITION_ECOLOGIQUE_POSITIVE / TRANSPORT_TRANSVERSE_A_BORNER`.**

## 4. Fonctions à ne pas transformer en nouvelles lignes

Le régime d’une règle est déjà l’architecture de la matrice ; ne pas créer une règle auto-référentielle supplémentaire.

Le cycle de vie d’une candidate est une trajectoire horizontale du dispositif, pas une nouvelle règle : émergence → exposition → contre-cas → qualification → décision de portée → promotion/amendement/régionalisation/abandon.

La procédure prospective C10 reste locale ; aucune prérégistration générale n’est soutenue.

## 5. Résultat du prototype fonctionnel

### Phase I fermée

```text
D17 = 84/96
D61 = 82/96
ERREURS_CRITIQUES = 0
COMPRESSION_ENTREE_D17 = ~28.1_POURCENT
NON_INFERIORITE_D17 = REPRODUITE
SUPERIORITE_GENERALE = NON_ETABLIE
```

### Phase II écologique

```text
D17_FIDELITE = 48/48
D17_NAVIGATION = 20/20
D61_FIDELITE = 48/48
D61_NAVIGATION = 20/20
ERREURS_CRITIQUES = 0
CONTAMINATION = NON
FICHIERS_CONSULTES = 9_DANS_CHAQUE_CONDITION
```

Le prototype fonctionnel ne démontre ni une meilleure exactitude générale ni une navigation plus courte en nombre de fichiers. Il soutient en revanche une **compression documentaire sous qualité conservée** dans les tests exécutés.

Le résultat le plus défendable est :

> l’organisation fonctionnelle conserve la qualité décisionnelle et la discipline de navigation de la présentation fiches+relations avec une surface de guide sensiblement plus compacte, sans augmentation observée des erreurs critiques.

## 6. Portée proposée du prototype 2D

Le prototype ne doit pas devenir une nouvelle autorité ou remplacer la matrice et les relations sources.

### Option P2D-1 — essai réel local et ablable

Utiliser la représentation fonctionnelle comme surface de guidage locale sur un chantier réel borné, avec :
- sources 42/52 toujours récupérables ;
- aucun verdict normatif propre au prototype ;
- retour aux sources lorsque la qualification probatoire ou historique l’exige ;
- suppression possible sans perte d’autorité.

### Option P2D-2 — test sur un second sous-système

Construire une seconde vue fonctionnelle locale sur un cluster différent de reprise/audit afin de tester la transférabilité du gain de compression avant toute sédimentation transverse.

### Option P2D-3 — ne pas sédimenter

Conserver seulement les résultats de test dans #139 et ne pas introduire de surface fonctionnelle durable supplémentaire.

### Recommandation expérimentale

```text
RECOMMANDATION_PROTO_2D = P2D-1_OU_P2D-2
PREFERENCE_PRUDENTE = P2D-1_LOCAL_ABLABLE
SEDIMENTATION_TRANSVERSE = NON_JUSTIFIEE_A_CE_STADE
DECISION_HUMAINE = REQUISE
```

La préférence pour P2D-1 vient du fait que le gain a déjà survécu à un test écologique réel du dépôt, mais seulement sur un sous-système et quatre situations construites. Un essai réel local est donc plus discriminant qu’une nouvelle répétition des mêmes scénarios, tout en restant réversible.

## 7. Delta de portée normative requalifié

```text
CANDIDATS_DIRECTS_LES_PLUS_FORTS = R-034, R-032, R-038
CANDIDAT_ETROIT = R-033
AMENDEMENT_NUCLEUS_PREFERABLE = R-025
FONCTION_AUDIT_FORTE_SUPPORT_A_DECIDER = R-041
R-040 = EXPOSITION_ECOLOGIQUE_POSITIVE / PORTAGE_A_DECIDER
R-042 = EXPOSITION_ECOLOGIQUE_POSITIVE / TRANSPORT_A_BORNER
```

Cette hiérarchie reste plus fidèle aux preuves qu’une promotion groupée.

## 8. Options de décision humaine sur le noyau normatif

### Option A — ne promouvoir aucune règle maintenant

Conserver l’état 42/52 comme résultat d’audit et observer les prochaines expositions.

### Option B — delta minimal à preuve très forte

Examiner seulement R-034, R-032 et R-038 pour une formulation directe, avec R-025 comme amendement éventuel du noyau scientifique.

R-033, R-040, R-041 et R-042 restent hors promotion quotidienne.

### Option C — ajouter R-041 dans son régime méthodologique

Option B + portage explicite du statut probatoire des règles dans la surface méthodologique appropriée, sans en faire un protocole lourd de chaque tâche.

### Option D — architecture agentique plus large

Créer plusieurs nouveaux `AGENTS.md` ou une couche de gouvernance dédiée.

**Non soutenue par #139 comme premier mouvement.**

## 9. Recommandation normative de l’audit

```text
INSTRUIRE_OPTION_B_COMME_DELTA_MINIMAL
+
EXAMINER_SEPAREMENT_R-041_DANS_LE_REGIME_METHODOLOGIQUE
+
DECIDER_SEPAREMENT_DU_PORTAGE_R-040_R-042
```

Cette recommandation reste une **proposition d’audit**, pas une décision humaine.

## 10. Conditions avant mutation de `AGENTS.md`

Avant écriture normative :

- vérifier une dernière fois la couverture exacte de chaque fonction sur `main` ;
- formuler le delta sans duplication ;
- préserver les conditions de silence ;
- ne pas étendre la portée depuis le seul fait que la fonction est forte ;
- soumettre explicitement la promotion à décision humaine.

```text
AGENTS_MODIFIE = NON
PROMOTION = NON_EFFECTUEE
DECISION_PROTO_2D = OUVERTE
DECISION_PROMOTION_NORMATIVE = OUVERTE
DECISION_OUTILLAGE = NON_OUVERTE
MERGE_#139 = NON_AUTORISE
```