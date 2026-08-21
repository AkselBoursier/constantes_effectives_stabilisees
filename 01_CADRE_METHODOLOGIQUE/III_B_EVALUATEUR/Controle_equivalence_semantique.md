# Contrôle d'équivalence sémantique — Phase III-B

## Statut

Contrôle pré-expérimental. Ne pas fournir aux agents testés. Fonction : vérifier que, pour une même tâche, les conditions diffèrent par **organisation documentaire** et non par contenu fonctionnel disponible.

```text
PHASE_III_B = NON_LANCEE
VARIABLE_INDEPENDANTE = ORGANISATION_DE_LA_MATRICE_ASSIGNEE
DIFFERENCE_DE_CORPUS_FONCTIONNEL = INTERDITE
IDENTITE_VERBATIM = NON_REQUISE
EQUIVALENCE_SEMANTIQUE = REQUISE
```

Une égalité stricte de longueur n'est pas recherchée : la capacité de compression et de structuration fait partie de la variable testée. En revanche, aucune condition ne peut posséder une règle, une relation, un déclencheur, une condition de silence ou une permission décisionnelle absente de l'autre.

## 1. Tâche S

### Unités présentes dans les deux conditions

```text
R-004
R-005
R-001
R-025
R-026
R-027
R-028
R-029
R-030
R-031
R-034
R-037
R-040
```

### Relations présentes dans les deux conditions

```text
R-004 -> R-005 : composition autorité courante / validité historique
R-025 -> R-026 : complément nature du maintien / indexation
R-027 <-> R-029 : indépendance couches / chemins
R-028 -> R-031 : complément portée / rang probatoire
R-031 -> R-001 : spécialisation machine -> science
R-031 <-> R-037 : indépendance qualification / conservation des négatifs
```

### Parité fonctionnelle contrôlée

Pour chaque unité, les deux surfaces contiennent :

- fonction protégée ;
- déclencheur matériel ;
- contrôle ou opération attendue ;
- condition de silence/arrêt ;
- qualification/décision autorisée ou garde équivalente.

La condition 9C regroupe plusieurs unités dans un parcours `autorité -> qualification du maintien -> couches et chemins -> rang/portée -> négatifs -> autorisation`, tandis que 7A conserve les unités séparées. Le rôle transversal attribué à `R-040` dans 9C dérive de sa formulation source et n'ajoute aucun déclencheur nouveau.

### Fuites de solution contrôlées

Aucune des deux matrices ne contient :

- le chemin du cadre canonique actuel ;
- la liste des documents que l'agent doit considérer comme autorités ;
- le verdict attendu sur les phases 2, 3 ou 4 du Cycle 10 ;
- l'énoncé qu'un résultat particulier doit être conservé ou déclassé ;
- une autorisation de nouvelle opération scientifique.

## 2. Tâche M

### Unités présentes dans les deux conditions

```text
R-004
R-005
R-006
R-008
R-009
R-010
R-011
R-014
R-015
R-017
R-039
R-040
R-041
```

### Relations présentes dans les deux conditions

```text
R-004 -> R-005 : composition
R-005 -> R-006 : contrôle
R-008 -> R-009 : support
R-009 -> R-010 : déclenchement
R-010 -> R-011 : contrôle du contrôle
R-014 -> R-010 : déclenchement conditionnel
R-015 -> R-011 : insuffisance
R-008 -> R-004 : dépendance routage/ancrage
R-009 -> R-015 : insuffisance de sélection
R-040 <-> R-039 : indépendance Human-First / intégrité de représentation
R-040 -> R-010 : déclenchement conditionnel
R-041 -> R-010 : gouverne le statut
R-041 -> R-015 : composition statut / symétrie
```

### Parité fonctionnelle contrôlée

Les deux surfaces contiennent les mêmes contrôles sur :

- autorité et statut courant ;
- correction documentaire bornée ;
- ancrage/checkpoints ;
- représentation de science vivante ;
- second ordre et suffisance contextuelle d'un audit antérieur ;
- contrôle de sélection et symétrie critique ;
- proportionnalité documentaire ;
- Human-First ;
- intégrité d'une transformation de représentation ;
- statut probatoire d'une pratique.

La condition 9C compose ces fonctions en niveaux et boucles. La condition 7A les expose comme unités autonomes puis relations. Aucune condition n'informe l'agent que la branche expérimentale a été ouverte avant ou après une requalification des témoins : cette chronologie doit être reconstruite depuis les sources du cas.

## 3. Différences admises

```text
ORDRE_DE_PRESENTATION = PEUT_DIFFERER
REGROUPEMENT_DE_FONCTIONS = PEUT_DIFFERER
VOLUME_REDONDANT = PEUT_DIFFERER
VISIBILITE_DES_BOUCLES = PEUT_DIFFERER
NOMBRE_DE_FONCTIONS = IDENTIQUE_PAR_TACHE
NOMBRE_DE_RELATIONS = IDENTIQUE_PAR_TACHE
CONTENU_DECISIONNEL_DISPONIBLE = EQUIVALENT
CAS_SCIENTIFIQUE_OU_HISTORIQUE_INJECTE = AUCUN
```

## 4. Conditions d'invalidation avant lancement

Ne pas lancer III-B si une relecture montre :

1. une unité absente d'une condition ;
2. une relation source absente ou inversée ;
3. un déclencheur rendu plus large dans une seule condition ;
4. une condition de silence/arrêt perdue ;
5. une condition contenant un indice documentaire vers la solution que l'autre n'a pas ;
6. une conclusion attendue encodée dans le vocabulaire d'une seule surface.

Verdict de la présente passe :

```text
EQUIVALENCE_TACHE_S = SUFFISANTE_POUR_PREVOL
EQUIVALENCE_TACHE_M = SUFFISANTE_POUR_PREVOL
LANCEMENT = ENCORE_CONDITIONNE_AU_CONTROLE_D_ACCES_MATERIEL
```
