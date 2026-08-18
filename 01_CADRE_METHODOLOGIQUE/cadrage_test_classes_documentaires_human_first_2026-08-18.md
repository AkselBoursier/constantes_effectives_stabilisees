# Cadrage du test par classes documentaires

## Fonction et statut

Artefact interne de la phase 9. Ce cadrage precede la redaction et la
distribution des liens. Il vise a eviter qu'une restructuration future oblige a
recreer plusieurs fois les memes textes parce que leurs destinations ont ete
fixees trop tot.

```text
PHASE = 9 / NORMALISATION_DOCUMENTAIRE_HUMAN_FIRST
STATUT = SAS_DE_RESTRUCTURATION_A_TESTER
MUTATION_DES_SOURCES = NON
LIENS_VERS_DESTINATIONS_FUTURES = NON_REQUIS
PROMOTION_PUBLIQUE = NON
```

## Hypothese de travail

Une organisation par classes documentaires, fonctions et contrats de capacite
est plus stable qu'une organisation commencee par les chemins actuels. Elle
permet de rediger des documents autonomes, de les comparer aux sources et de
decider ensuite quelles relations et quelles destinations sont necessaires.

Cette hypothese reste falsifiable. Elle sera abandonnee ou limitee si les
classes masquent des dependances qui changent le sens, si elles imposent des
duplications ou si le cout de liaison ulterieur depasse le gain obtenu.

## Classes provisoires a tester

| Classe | Fonction dominante | Contenu a porter | Ce qu'elle ne porte pas par defaut |
|---|---|---|---|
| **Accueil du projet** | Donner l'objet, les questions et les premieres voies de lecture. | Description courante, portee, limites et vocabulaire minimal. | Journal, genealogie complete, etat mouvant ou preuve detaillee. |
| **Carte de domaine** | Montrer les terrains et leurs differences. | Classes de problemes, fonctions des terrains, distinctions necessaires au choix. | Maintenance des liens, dettes et tableau de bord operationnel. |
| **Synthese scientifique** | Exposer un resultat ou un etat qualifie dans son perimetre. | Cible, transformation, regime, acces, soutien, limites et conditions de reprise. | Histoire complete de fabrication et regles generales non demontrees. |
| **Contrat methodologique** | Rendre une regle utilisable et controlable. | Regle, fonction, portee, contre-test, condition d'amendement. | Resultat scientifique qu'elle ne qualifie pas elle-meme. |
| **Provenance et genealogie** | Permettre la reprise historique et l'audit. | Sources, versions, decisions, etats dates, relations et transformations. | Vue publique courante imposee au nouveau lecteur. |
| **Laboratoire editorial** | Conserver les essais et les comparaisons de formes. | Prototypes, tests, pertes detectees, variantes et decisions de promotion. | Autorite publique ou scientifique automatique. |

Ces classes sont des hypotheses de fonction, pas une nouvelle taxonomie
obligatoire du depot. Une piece peut relever de plusieurs classes pendant
l'inventaire ; la classe dominante ne sera decidee qu'apres examen du contenu
unique et des dependances.

## Contrat sans destination

Avant de creer un document migre, chaque piece candidate sera decrite par un
contrat qui ne depend pas d'un chemin :

```text
IDENTITE_DE_TRAVAIL
CLASSE_DOMINANTE
CONTRAT_SANS_DESTINATION
PUBLIC
QUESTION_SERVIE
CONTENU_UNIQUE
ENONCES_RECEVABLES
LIMITES_ET_REFUS
DEPENDANCES_SEMANTIQUES
PROVENANCE_RECUPERABLE
TAILLE_ET_REGISTRE
CRITERES_DE_MIGRABILITE
DECISION_HUMAINE_REQUISE
```

Le contenu du document est teste avant son emplacement. Les liens peuvent
ensuite etre generes ou rediges a partir d'un registre de destinations
stabilise ; ils ne constituent pas le contrat de sens.

## Test discriminant

Comparer, sur un petit lot homogene :

1. une description liee aux chemins actuels ;
2. un contrat sans destination ;
3. un document autonome produit a partir de ce contrat ;
4. la migration conceptuelle vers deux organisations possibles, sans modifier
   les sources.

Le test cherchera notamment :

- le nombre de reformulations necessaires lorsque la destination change ;
- les contenus uniques perdus ou rendus ambigus ;
- les dependances que la classe ne peut pas isoler ;
- le cout de construire les liens apres stabilisation ;
- la lisibilite pour un nouveau lecteur ;
- la recuperabilite pour le laboratoire.

Le test peut conclure que certains liens sont constitutifs du sens et doivent
etre traites comme dependances semantiques, tandis que d'autres ne sont que de
la distribution actuelle et doivent rester remplaçables.

## Regle d'arret

On arrete ce sas si le contrat sans destination ne permet pas de preserver le
rang, la limite ou la dependance qui change le verdict. Dans ce cas, on ouvre
une triangulation locale sur le contenu concerne ; on ne revient pas
automatiquement a une reconstruction globale des chemins.

```text
RESULTAT_ATTENDU = DOCUMENTS_PLUS_STABLES_AVANT_LIAISON
ARCHITECTURE_FINALE = NON_DECIDEE
RESTRUCTURATION_EFFECTIVE = NON_OUVERTE
```