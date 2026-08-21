# Matrice assignée — Tâche S — condition 9C

## Statut

Surface expérimentale de contrôle. Les identifiants servent de pointeurs ; ils ne sont pas des autorités scientifiques et ne donnent aucune réponse sur le Cycle 10.

## Parcours fonctionnel

| Niveau / fonctions | Déclencheur matériel | Objet à distinguer | Contrôle / opération | Qualification ou décision permise | Silence / arrêt |
|---|---|---|---|---|---|
| **Autorité courante** (`R-004`, `R-005`) | Plusieurs documents/états peuvent prétendre gouverner la tâche ; une pièce datée peut être prise pour le courant | Point d'entrée / autorité applicable / contenu localement valide / état courant | Le point d'entrée route vers l'autorité : date, titre, numéro et visibilité ne suffisent pas. Un document ancien peut rester valide sans représenter le courant ; ne pas réécrire rétroactivement son corps | Justifier la surface qui gouverne aujourd'hui tout en conservant, si nécessaire, un résultat historique/local valide | Si le point d'entrée est explicitement aussi la décision applicable, pas de détour ; document clairement historique sans risque de lecture courante = silence |
| **Signal technique → science** (`R-001`) | Sortie machine, vert CI, scan, convergence numérique ou contrôle technique utilisé pour soutenir une propriété scientifique | Propriété directement observée / qualification technique / résultat scientifique | Le signal technique n'établit que ce que le dispositif a réellement observé | Distinguer sortie machine, qualification technique et éventuel résultat scientifique | Aucune prétention au-delà de la propriété directement observée |
| **Nature et domaine du maintien** (`R-025`, `R-026`) | Vocabulaire de stabilité, maintien, quasi-fixité ou stabilisation utilisé pour parler de constance ; proposition qu'une cible tient/varie/ne varie pas | Constance de la cible / stabilisation d'accès-estimateur-régime / maintien produit par mécanisme ; puis cible, transformation, régime, échelle-schéma-modèle, tolérance, rupture | Distinguer d'abord la nature du maintien ; indexer ensuite l'énoncé par les coordonnées réellement pertinentes du domaine | Dire explicitement quel maintien est établi et dans quel domaine réfutable | Si le vocabulaire disciplinaire distingue déjà les niveaux ; ne pas remplir mécaniquement un champ sans sens disciplinaire |
| **Cible, accès, constitution et chemins** (`R-027`, `R-029`) | Objet/cible, mesure/reconstruction et mécanisme sont reliés ; le type de chemin change comparabilité, causalité ou portée | Cible / accès / constitution ; chemin physique, inférentiel, computationnel, représentationnel, historique/de réalisation ou autre catégorie disciplinaire justifiée | Maintenir les trois dimensions distinctes sans ordre universel ; typer seulement les chemins qui changent l'argument | Dire quelle dimension le résultat modifie ; refuser de convertir un chemin de scan, représentation ou inférence en trajectoire physique sans argument | Une seule couche matériellement en jeu ; chemin sans effet = `NON_PERTINENT`, chemin indéterminé = `NON_ETABLI` |
| **Portée et rang probatoire** (`R-028`, `R-031`) | Formation, constitution, accès, histoire, mécanisme ou comparaison servent de base à une conclusion ; résultat utilisé pour soutenir un verdict | Dimension étudiée / portée physique-épistémique-interprétative/non engagée ; résultat / soutien / verdict / interprétation-décision | Borner la portée indépendamment du rang ; conserver résultat, soutien et verdict comme niveaux distincts | Un résultat local peut rester solide avec un verdict ou une portée plus étroits qu'auparavant | Aucune extrapolation ; un seul niveau explicitement revendiqué sans transfert |
| **Vocabulaire du domaine** (`R-030`) | Terme transversal du projet utilisé pour qualifier le phénomène | Notion disciplinaire / terme transverse | Décrire d'abord dans le vocabulaire du domaine ; garder le terme transverse seulement s'il ajoute une discrimination réelle | Retirer ou déclasser un ancien label sans effacer phénomène ni résultat | Le terme interne n'ajoute aucune fonction ou écrase une notion disciplinaire plus précise |
| **Autorisation d'agir** (`R-034`) | Changement de nature d'acte ou de portée : qualifier→calculer, dette→opération, clôturer→propager, proposer→exécuter | Acte, objet et portée réellement couverts | Une décision n'autorise que ce qu'elle couvre explicitement | Une dette ou un mécanisme restant à instruire ne vaut pas autorisation de lancer une nouvelle opération | L'autorisation couvre explicitement l'enchaînement technique borné |
| **Négatifs, refus, suspensions** (`R-037`) | Résultat négatif, voie non productive, suspension ou limite modifie un choix futur ou borne une prétention | Négatif local / hypothèses / portée / valeur de reprise | Conserver le négatif à son rang exact avec provenance ; ne pas le convertir en verdict global | Refuser de répéter une stratégie localement non productive sans conclure contre toute une famille | Incident technique trivial sans valeur discriminante pour la reprise |
| **Raccord ancien → qualification actuelle** (`R-040`) | Synthèse, réduction, traduction ou ancien cadrage devient entrée d'une nouvelle qualification ou prétend représenter le courant | Delta source→représentation : conservé / perdu / ajouté / requalifié | Tester si le delta change prémisse, sélection ou portée aval | `localement juste` peut coexister avec `insuffisant ou trop large pour l'usage actuel`, sans réécriture destructive | Différence sans perte pertinente ; arrêt lorsque delta et effet aval sont qualifiés |

## Boucles et relations utiles

1. **Autorité / statut** — `R-004 → R-005` : trouver la surface courante ne signifie pas invalider le contenu local d'une pièce datée.
2. **Nature / indexation** — `R-025 → R-026` : nature du maintien et domaine de validité sont indépendamment nécessaires.
3. **Dimensions / chemins** — `R-027 ↔ R-029` : séparer cible-accès-constitution ne remplace pas le typage de la dépendance qui les relie.
4. **Portée / rang** — `R-028 → R-031` : un énoncé peut être au bon rang mais de portée trop large, ou inversement.
5. **Machine / résultat** — `R-031 → R-001` : machine→science est une spécialisation de résultat→soutien→verdict.
6. **Négatif / mémoire** — `R-031 ↔ R-037` : qualifier correctement un négatif et le conserver sont deux fonctions distinctes.

## Lecture transversale

`source courante → qualification du maintien → cible/accès/constitution → chemin pertinent → rang probatoire → portée → conservation des négatifs → autorisation éventuelle`

À chaque transition, `R-040` peut contrôler un ancien cadrage ou une synthèse devenue entrée du raisonnement, mais uniquement si le delta change réellement l'usage aval.

## Garde générale

Aucune fonction n'impose une conclusion positive. `NON_ETABLI`, maintien local d'un résultat, réduction de portée et absence d'autorisation nouvelle sont des sorties recevables.
