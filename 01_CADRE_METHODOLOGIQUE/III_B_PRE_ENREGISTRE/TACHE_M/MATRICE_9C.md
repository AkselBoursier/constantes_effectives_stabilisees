# Matrice assignée — Tâche M — condition 9C

## Statut

Surface expérimentale de contrôle. Les identifiants servent de pointeurs ; ils ne sont pas des autorités et ne préjugent pas la valeur du prototype Human-First.

## Parcours fonctionnel

| Niveau / fonctions | Déclencheur matériel | Objet à examiner | Contrôle / opération | Qualification ou décision permise | Silence / arrêt |
|---|---|---|---|---|---|
| **Autorité et statut courant** (`R-004`, `R-005`) | Reprise où plusieurs surfaces peuvent gouverner ; formulation ancienne encore lisible comme courante | Point d'entrée / autorité applicable / contenu localement valide / état courant | Date, titre, numéro ou visibilité ne suffisent pas ; le point d'entrée route vers l'autorité. Un document daté peut rester valide sans représenter le courant ; ne pas réécrire rétroactivement son corps | Justifier la surface qui porte aujourd'hui l'état pertinent tout en conservant l'observation/preuve locale d'une pièce antérieure | Si le point d'entrée est explicitement l'autorité applicable ; pièce clairement historique sans risque de lecture courante |
| **Correction documentaire bornée** (`R-006`) | Une correction de statut, d'accueil ou de routage est envisagée | Erreur de lecture réelle / substance du contenu | Tester `CF_LECTURE` : la forme actuelle peut-elle induire une erreur ? Tester `CF_SUBSTANCE` : la correction modifie-t-elle la substance ? | Corriger le routage seulement si la fonction est réelle et la substance préservée | Aucune ambiguïté reproduite ; ne pas universaliser ce contrôle régional |
| **Ancrage de reprise** (`R-008`) | Changement d'état/portée/soutien/contre-cas/décision/prochaine opération, ou reprise échouant parce que l'ancrage est contradictoire | Ancrage principal / transitions substantielles / checkpoint | Conserver un état courant lisible et les transitions sans journal exhaustif ; un checkpoint ne doit pas devenir l'unique moyen de connaître le courant | Reconsolider seulement si l'ancrage ne porte plus l'état vivant nécessaire | Pas de checkpoint à chaque action ; arrêt lorsque l'état est récupérable et non contradictoire. Sous-application : corps/surfaces obsolètes malgré correctifs. Sur-application : chaîne de checkpoints sans reconsolidation |
| **Représentation de l'état scientifique vivant** (`R-009`) | Une porte/synthèse prétend représenter l'état réel d'un ensemble scientifique | Actif / vivant dormant / veille / clos-suspendu / résultats / blocages / décision / reprise | Distinguer seulement les états nécessaires à la fonction de reprise ; ne pas transformer dette ou question dormante en priorité | Dire si la surface est suffisante pour représenter l'état qu'elle revendique | Audit strictement local = pas de portefeuille global ; aucune hiérarchie scientifique créée par les statuts de reprise |
| **Second ordre** (`R-010`, `R-014`) | Angle mort réel, changement de corpus/régime ou nouveau contexte touchant prémisse, exclusion, critère ou portée | Ancien audit/test, ses preuves locales et sa suffisance pour l'usage nouveau | Tester d'abord la dépendance. Si elle existe, réexaminer ce que le dispositif pouvait manquer et sa sensibilité à ce qui était transmis/sélectionné | Conserver, requalifier ou borner ; un ancien audit peut rester localement valable | Nouveau contexte sans lien matériel = pas de réaudit. Aucun nouveau discriminant = retour au travail principal ; réflexivité continue refusée |
| **Contrôle de sélection** (`R-011`, `R-015`) | Audit/prototype de portée globale, conclusion sensible au choix des cas, ou évaluation positive/négative risquant une asymétrie | Sélection d'entrée / contre-échantillon / soutien et fragilité / sous-correction et sur-correction | Chercher ce qui soutient et fragilise ; chercher aussi ce qui n'a pas été sélectionné lorsqu'un biais de corpus peut changer la portée | Verdict seulement après charge de preuve symétrique et, si nécessaire, contre-échantillon indépendant | Population locale fermée = pas de contre-audit global ; arrêt après absence de nouvelle famille discriminante. Symétrie formelle seule ne corrige pas un corpus asymétrique |
| **Proportionnalité documentaire** (`R-017`) | Création, maintien ou promotion durable d'une couche/support | Fonction distincte / support existant / gain / coût de maintenance | Comparer fonction, gain discriminant-conservation-traçabilité et coût ; l'exploration peut créer temporairement | Conserver durablement seulement si une solution plus légère ne protège pas la même fonction | Support existant suffisant ; nombre brut de fichiers ou principe abstrait ne décide rien |
| **Interface Human-First** (`R-039`) | Point d'entrée, synthèse, décision ou instruction pour lecteur/agent nouveau | Sens humain / référent / codes secondaires / charge cognitive | Le langage humain porte le sens ; codes/IDs restent récupérables mais secondaires ; compacité permise si référent et fonction restent compris | Une surface peut être jugée plus ou moins intelligible sans préjuger sa fidélité d'état | Scripts/fixtures à identifiants fonctionnels ; ne pas réécrire tout l'historique pour lisibilité |
| **Intégrité de représentation** (`R-040`) | Synthèse, réduction ou accueil devient entrée d'une décision/reprise ou prétend représenter l'état courant | Delta source→sortie : conservé / perdu / ajouté / requalifié | Vérifier l'effet aval du delta, notamment sur prémisse, sélection ou portée | Une surface peut être lisible mais incomplète, ou complète mais coûteuse ; `localement correcte` n'implique pas `suffisante pour l'aval` | Différence sans perte pertinente = silence ; arrêt lorsque delta et effet aval sont qualifiés |
| **Statut probatoire d'une pratique** (`R-041`) | On affirme qu'une règle/pratique fonctionne, est testée/validée, ou on envisage extension/promotion | Formulée / appliquée / observée / mise à l'épreuve / soutenue-falsifiée / ratifiée / promue | Pour parler de test : effet attendu, échec/coût, contre-cas/comparaison, observation discriminante. Une première application favorable ne suffit pas | Le statut peut monter, descendre ou rester indécis sans effacer l'observation initiale | Usage ordinaire sans prétention probatoire ; pas de test lourd pour chaque propriété directement observable |

## Boucles et relations utiles

1. `R-004 → R-005` — **composition** : autorité courante ≠ validité historique.
2. `R-005 → R-006` — **contrôle** : correction de statut/routage bornée par lecture réelle et absence de mutation substantielle.
3. `R-008 → R-009` — **support** : un ancrage scientifique peut être lisible mais insuffisant s'il omet l'état vivant nécessaire.
4. `R-009 → R-010` — **déclenchement** : perte réelle de dimension → second ordre possible.
5. `R-010 → R-011` — **contrôle du contrôle** : audit global → tester aussi sélection d'entrée.
6. `R-014 → R-010` — **déclenchement conditionnel** : nouveau contexte seulement si dépendance démontrée.
7. `R-015 → R-011` — **insuffisance** : symétrie critique seule ≠ correction du biais de corpus.
8. `R-008 → R-004` — **dépendance** : checkpoint correctif sans routage courant peut laisser un agent reconstruire un état faux.
9. `R-009 → R-015` — **insuffisance de sélection** : ne représenter que les résultats porteurs peut rester symétrique tout en effaçant la science vivante.
10. `R-040 ↔ R-039` — **indépendance** : intelligibilité et fidélité du contenu transmis ne se remplacent pas.
11. `R-040 → R-010` — **déclenchement conditionnel** : delta matériel → second ordre seulement si effet aval.
12. `R-041 → R-010` — **gouverne le statut** : application favorable ≠ test.
13. `R-041 → R-015` — **composition** : succès, mauvais cas et coûts contribuent au statut sans auto-promotion.

## Lecture transversale

`autorité courante → ancrage → représentation d'état → delta source/sortie → qualification probatoire du test → second ordre si déclenché → contrôle de sélection → décision proportionnée → éventuel maintien/amendement/abandon du support`

`R-017` gouverne seulement la question de sédimentation durable ; il ne doit pas interdire l'existence temporaire du prototype expérimental.

## Garde générale

Le résultat recherché est une décision proportionnée, pas la maximisation du nombre de contrôles. Une fonction non déclenchée doit rester silencieuse.
