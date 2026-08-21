# Matrice assignée — Tâche M — condition 7A

## Statut

Surface expérimentale de contrôle. Les identifiants servent de pointeurs ; ils ne sont pas des autorités et ne préjugent pas la valeur du prototype Human-First.

## Unités fonctionnelles

### R-004 — routage et autorité

**Fonction.** Empêcher confusion accueil/autorité et provenance/état courant.  
**Déclencheur.** Une reprise doit déterminer quelle surface gouverne réellement l'état ou la décision.  
**Contrôle.** Date, titre, numéro ou visibilité ne suffisent pas ; un point d'entrée route vers l'autorité applicable.  
**Silence/arrêt.** Si le point d'entrée est explicitement aussi l'autorité applicable.  
**Décision permise.** Justifier quelle surface porte aujourd'hui l'état pertinent.

### R-005 — statut documentaire

**Fonction.** Préserver provenance et validité locale sans confondre pièce datée et état courant.  
**Déclencheur.** Une formulation ancienne peut encore être lue comme actuelle.  
**Contrôle.** Un document daté peut rester valide ; corriger le routage ou le statut sans réécriture rétroactive du corps.  
**Silence/arrêt.** Pièce clairement historique sans risque de lecture courante.  
**Décision permise.** Conserver l'observation ou preuve locale tout en requalifiant son rôle présent.

### R-006 — contre-factuel documentaire borné

**Fonction.** Séparer réparation de routage et mutation substantielle.  
**Déclencheur.** Une correction de statut ou d'accueil est envisagée.  
**Contrôle.** Vérifier deux questions : la lecture actuelle peut-elle réellement induire une erreur (`CF_LECTURE`) ? La correction proposée change-t-elle la substance (`CF_SUBSTANCE`) ?  
**Silence/arrêt.** Aucune ambiguïté de lecture reproduite ; ne pas transformer ce contrôle régional en test universel.  
**Décision permise.** Une correction de routage est justifiée seulement si elle protège une fonction réelle sans réécrire la substance.

### R-008 — ancrage et checkpoints

**Fonction.** Rendre un chantier long récupérable sans journal exhaustif.  
**Déclencheur.** Changement substantiel d'état, portée, soutien, contre-cas, décision ou prochaine opération ; ou reprise qui échoue parce que l'ancrage est contradictoire.  
**Contrôle.** Ancrage principal lisible + transitions conservées ; les checkpoints ne doivent pas devenir l'unique moyen de connaître le courant.  
**Sous-application.** Corps d'issues ou surfaces d'accueil peuvent rester obsolètes malgré des checkpoints correctifs.  
**Sur-application/silence.** Pas de checkpoint à chaque action ; arrêter lorsque l'état courant est récupérable et non contradictoire.

### R-009 — représentation de l'état scientifique vivant

**Fonction.** Empêcher qu'une surface de reprise transforme un portefeuille scientifique en liste de seuls résultats ou de seules lignes actives.  
**Déclencheur.** Une synthèse/porte prétend représenter l'état scientifique réel d'un ensemble de cycles ou chantiers.  
**Contrôle.** Distinguer, si matériellement nécessaires : actif, vivant dormant, veille conditionnelle, clos/suspendu, résultats qualifiés, blocages, décision et condition de reprise.  
**Silence/arrêt.** Audit strictement local d'un résultat : aucune obligation de représenter tout le portefeuille.  
**Risque.** Une dette ou une question dormante ne devient pas automatiquement priorité.

### R-010 — audit de second ordre

**Fonction.** Examiner ce qu'un audit ou test pouvait structurellement manquer, pas seulement ses conclusions.  
**Déclencheur.** Angle mort réel, changement de corpus/régime, ou nouvelle information touchant prémisse, exclusion, critère ou portée.  
**Contrôle.** Réexaminer la sensibilité à ce qui était transmis ou sélectionné.  
**Silence/arrêt.** Aucun nouveau discriminant : pas d'audit de l'audit ; retourner au travail principal.  
**Risque.** Réflexivité continue et récursion infinie.

### R-011 — contre-audit indépendant

**Fonction.** Contrôler la sélection d'entrée d'un audit ou test global.  
**Déclencheur.** Audit/synthèse de portée globale ou conclusion qui dépend du choix des cas d'entrée.  
**Contrôle.** Chercher aussi ce qui n'a pas été sélectionné ; utiliser un contre-échantillon indépendant lorsque cela change la portée.  
**Silence/arrêt.** Contrôle local sur population fermée et connue ; arrêt après absence de nouvelle famille discriminante.  
**Risque.** Relecture totale sans saturation.

### R-014 — audit antérieur et nouveau contexte

**Fonction.** Préserver les preuves locales d'un audit sans valider automatiquement sa suffisance pour un nouveau programme.  
**Déclencheur.** Un contexte nouveau peut toucher prémisse, exclusion, critère ou portée.  
**Contrôle.** Tester la dépendance avant de réauditer.  
**Silence/arrêt.** Nouveau contexte sans lien matériel : l'audit antérieur reste localement valable.  
**Décision permise.** Réaudit ciblé, conservation inchangée ou requalification bornée.

### R-015 — symétrie critique

**Fonction.** Empêcher surpromotion et écrasement/sous-exploitation sous des charges de preuve asymétriques.  
**Déclencheur.** Audit qualifiant un résultat, un prototype, une critique ou une pratique.  
**Contrôle.** Chercher à la fois ce qui soutient et ce qui fragilise ; traiter aussi le risque de sous-correction et celui de sur-correction.  
**Limite.** Une symétrie formelle ne corrige pas un corpus d'entrée asymétrique : `R-011` peut alors devenir nécessaire.  
**Arrêt.** Pas de verdict par plausibilité ou simple absence de contre-exemple.

### R-017 — non-prolifération par fonction

**Fonction.** Éviter plomberie et artefacts durables inutiles sans interdire l'exploration.  
**Déclencheur.** Création, maintien ou promotion durable d'une couche/support.  
**Contrôle.** Comparer fonction distincte, support existant, gain discriminant/conservation/traçabilité et coût de maintenance ; l'exploration peut créer temporairement.  
**Silence/arrêt.** Support existant suffisant ; nombre brut de fichiers ou principe abstrait ne décident rien.  
**Décision permise.** Conserver durablement seulement si fonction/gain/coût justifient la couche.

### R-039 — intelligibilité sémantique Human-First

**Fonction.** Réduire le coût cognitif de reprise sans supprimer précision ni traçabilité.  
**Déclencheur.** Point d'entrée, synthèse, décision ou instruction destinée à un lecteur/agent nouveau.  
**Contrôle.** Le nom/formulation humaine porte le sens ; codes et IDs restent secondaires ; la compacité est permise si le référent et la fonction restent récupérables.  
**Silence/arrêt.** Scripts/fixtures où les identifiants compacts sont fonctionnels.  
**Limite.** Lisibilité et fidélité de l'état transmis sont deux fonctions différentes.

### R-040 — intégrité des transformations de représentation

**Fonction.** Empêcher qu'une surface localement correcte devienne une représentation aval incomplète ou contaminée.  
**Déclencheur.** Une synthèse, réduction ou accueil devient entrée d'une décision/reprise ou prétend représenter l'état courant.  
**Contrôle.** Delta source→sortie : dimensions conservées, perdues, ajoutées, requalifiées ; vérifier l'effet réel sur l'usage aval.  
**Silence/arrêt.** Différence sans perte pertinente ; arrêt lorsque delta et effet aval sont qualifiés.  
**Décision permise.** Une surface peut être lisible et pourtant incomplète, ou complète et coûteuse à lire.

### R-041 — statut probatoire d'une pratique

**Fonction.** Empêcher qu'une pratique gagne de l'autorité par répétition ou première application favorable.  
**Déclencheur.** On affirme qu'une règle/pratique fonctionne, est testée/validée, ou on envisage extension/promotion.  
**Contrôle.** Distinguer formulée, appliquée, observée, mise à l'épreuve, soutenue/falsifiée, ratifiée et promue ; pour parler de test, expliciter effet attendu, échec/coût, contre-cas/comparaison et observation discriminante.  
**Silence/arrêt.** Usage ordinaire sans prétention probatoire ; pas de test lourd pour chaque propriété directement observable.  
**Décision permise.** Le statut peut monter, descendre ou rester indécis sans effacer l'observation initiale.

## Relations à conserver

- `R-004 → R-005` — **composition** : autorité courante et validité historique sont distinctes.
- `R-005 → R-006` — **contrôle** : le double contre-factuel borne une correction de statut/routage.
- `R-008 → R-009` — **support** : un ancrage scientifique est insuffisant s'il omet l'état vivant nécessaire à sa fonction.
- `R-009 → R-010` — **déclenchement** : une perte réelle de dimension scientifique peut justifier un second ordre.
- `R-010 → R-011` — **contrôle du contrôle** : un audit global doit aussi tester la sélection d'entrée.
- `R-014 → R-010` — **déclenchement conditionnel** : réaudit seulement si le nouveau contexte touche réellement une dépendance.
- `R-015 → R-011` — **insuffisance** : symétrie critique seule ne corrige pas un corpus d'entrée asymétrique.
- `R-008 → R-004` — **dépendance** : un checkpoint correctif ne suffit pas si le point d'entrée courant ne route pas vers l'état corrigé.
- `R-009 → R-015` — **insuffisance de sélection** : une sélection de seuls résultats porteurs peut rester symétrique tout en perdant la science vivante.
- `R-040 ↔ R-039` — **indépendance fonctionnelle** : intelligibilité et intégrité du contenu transmis ne se remplacent pas.
- `R-040 → R-010` — **déclenchement conditionnel** : un delta matériel ne déclenche second ordre que s'il a eu un effet aval.
- `R-041 → R-010` — **gouverne le statut** : une application favorable ne suffit pas pour déclarer un contrôle testé.
- `R-041 → R-015` — **composition** : succès, mauvais cas et coûts alimentent la qualification probatoire sans auto-promotion.

## Garde générale

Le résultat recherché est une décision proportionnée, pas la maximisation du nombre de contrôles. Une fonction non déclenchée doit rester silencieuse.
