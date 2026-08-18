# Matrice de capacite des documents Human-First

## Fonction et statut

Artefact interne de la phase 9. Cette matrice prepare un test editorial reversible ; elle n'autorise ni reecriture publique, ni fusion, ni deplacement, ni suppression.

```text
PHASE = 9 / NORMALISATION_DOCUMENTAIRE_HUMAN_FIRST
LOT = README_RACINE + README_CYCLES_PHYSIQUES
STATUT = MATRICE_DE_CAPACITE_REQUALIFIEE_APRES_TEST
PUBLICATION = NON
MUTATION_DES_SOURCES = NON
DECISION_HUMAINE_REQUISE = POUR_TOUTE_PROMOTION_PUBLIQUE
```

La matrice ne suppose pas que les deux documents doivent devenir un seul texte ni qu'une nouvelle porte doit etre creee. Elle teste ce que chaque document peut porter sans perdre de sens et quelle separation minimale rendrait la lecture plus claire. Le premier prototype a toutefois montre que cette matrice intervenait trop tard sur les destinations : elle decrivait des documents deja attaches a l'arborescence actuelle avant d'avoir teste les classes documentaires et leur stabilite.

## Regles de lecture de la matrice

- La capacite editoriale est locale au document, a son public et a sa fonction ; elle ne vaut pas comme regle generale pour les autres pieces.
- Une source peut rester necessaire meme si son contenu est repris dans un prototype : la reprise ne vaut ni declassement ni archivage.
- Une limite, une contradiction, un resultat negatif ou une condition de reouverture est un contenu a conserver, pas un defaut de style a attenuer.
- Le test peut conduire a conserver la forme actuelle, a proposer une separation, a demander une triangulation ou a amender la regle de depart.

## Matrice des cibles

| Champ | README racine | README de `02_CYCLES_PHYSIQUES` |
|---|---|---|
| **Fonction dominante** | Presenter l'objet du depot, ses deux questions, une distinction minimale et les routes de lecture. | Donner une carte lisible des dix terrains physiques et orienter vers le bon point d'entree scientifique pour chacun. |
| **Public principal** | Lecteur humain decouvrant le projet, collaborateur ou lecteur scientifique qui cherche une premiere orientation. | Lecteur humain qui veut comparer les cycles ou commencer une reprise scientifique localisee. |
| **Genre cible** | Accueil public conceptuel et routage court. | Carte publique scientifique avec liens de reprise ; pas un tableau de bord exhaustif. |
| **Etat actuel observe** | Porte publique courante deja compatible avec Human-First ; plomberie explicite faible. | Porte utile mais hybride : presentation des cycles, versions de syntheses, etat local et references d'issues. |
| **Ce que le document peut affirmer** | Objet du projet, questions, distinctions minimales, limites de portee et routes generales effectivement verifiees dans le depot. | Difference de fonction entre les cycles, question dominante de chaque terrain, point d'entree actuellement indique et independance par defaut des cycles. |
| **Ce qu'il ne doit pas etablir seul** | Verdict scientifique detaille, autorisation de calcul, etat mouvant d'une issue, genealogie complete ou doctrine philosophique. | Qualification scientifique complete d'un cycle, synchronisation automatique des etats, transfert de verdict entre cycles ou autorisation operationnelle. |
| **Elements a garder dans le flux principal** | Les deux questions, la distinction constance/stabilisation, les routes humaines essentielles et une formulation courte de l'etat du depot. | Une phrase d'orientation par cycle, les distinctions qui differencient les terrains, les liens vers les syntheses ou README locaux et l'avertissement sur l'independance des cycles. |
| **Elements a borner ou router** | Details des phases d'audit, dettes, blocages, issues, branches, provenance, agents et conditions de calcul. | Numeros d'issues quand ils ne sont pas necessaires a l'orientation, versions transitoires, portes materielles, journaux, dettes et etats de qualification detailles. |
| **Plomberie de laboratoire a exclure du flux principal** | Sequence des agents, outils d'append, changelogs, operations Git, etats dates et historique des decisions. | Historique de fabrication du tableau, maintenance des liens, journaux d'audit, detail des portes B1/G2, etat mouvant non necessaire au choix d'un cycle. |
| **Contenu unique a proteger** | Les deux questions formulees pour le projet, la distinction minimale, la separation entre objet public et routes de provenance. | La cartographie des dix cycles, leurs differences de fonction et les points d'entree concrets, y compris les limites propres a certains cycles. |
| **Dependances vivantes** | Les README locaux, le cadre methodologique, le glossaire, le volet philosophie et les routes explicitement maintenues. | Les syntheses et README de chaque cycle, les routes locales actives et, seulement lorsque cela change l'orientation, les issues identifiees par ces routes. |
| **Route de provenance** | Changelog et journaux de phase, Git, archives et sources locales ; route optionnelle, non requise pour la premiere lecture. | Syntheses locales, journaux et issues de chaque cycle ; provenance detaillee a suivre depuis le point d'entree du cycle concerne. |
| **Tension principale** | Rester precis sans transformer l'accueil en manuel methodologique ou en compte rendu de laboratoire. | Rester utile et actuel sans confondre carte scientifique, etat operationnel et historique de maintenance. |
| **Transformation candidate** | Polissage local et verification des routes ; pas de consolidation necessaire a ce stade. | Separation legere entre carte publique des cycles et details de routage vivant, a tester avant toute creation de document annexe. |
| **Risque de perte** | Effacer la nuance sur le nom historique, les limites de portee ou la distinction entre etat courant et provenance. | Perdre une difference entre cycles, un lien de reprise, une independance d'etat ou une limite scientifique en simplifiant le tableau. |
| **Test discriminant** | Une lecture sans consulter le laboratoire doit permettre d'identifier le projet, ses questions et la prochaine porte pertinente, sans attribuer un verdict non porte. | Une lecture doit permettre de choisir un cycle et de comprendre ce que son lien promet, sans croire que le tableau constitue un resultat transversal ou un tableau de bord. |
| **Critere de conservation de la forme actuelle** | Les retouches n'ameliorent pas substantiellement la comprehension ou risquent d'affaiblir une limite. | Une separation ajoute une route plus complexe sans gain net de lisibilite, de controle ou de recuperabilite. |
| **Decision humaine a reserver** | Promotion d'une nouvelle formulation publique ou modification de la route d'accueil. | Promotion d'une version separee, maintien des references d'issues, et eventuelle creation d'une route de laboratoire. |

## Contrat editorial provisoire

### README racine

Le document doit rester court, conceptuel et descriptif. Sa capacite maximale est un accueil public : il peut expliquer l'objet, les questions et les distinctions necessaires pour choisir une route. Il ne doit pas porter la qualification detaillee des cycles ni la fabrication de l'etat courant.

Le premier test ne cherchera donc pas a le consolider avec d'autres documents. Il servira de temoin de controle pour la stabilite des liens, la suffisance des limites et la possibilite de reduire la tuyauterie sans perte. La redaction de nouveaux contenus autonomes est reportee jusqu'a la definition des classes documentaires.

### README des cycles physiques

Le document peut porter une carte publique des terrains et leurs differences. Il peut renvoyer vers une profondeur scientifique locale, mais ne peut pas absorber les etats, dettes et decisions de chaque cycle sans devenir un tableau de bord de laboratoire.

Le premier test a compare deux options reversibles en pratique, mais cette comparaison est suspendue comme strategie de restructuration :

1. conserver la carte actuelle en retirant seulement les details qui n'aident pas a choisir un cycle ;
2. rediger sur copie une carte publique et une route de laboratoire separee, sans supprimer ni deplacer la source.

L'option 2 ne sera pas retenue comme architecture tant que les classes documentaires, leurs fonctions et leurs conditions de migration ne sont pas stabilisees. Un lien valide aujourd'hui ne constitue pas une garantie de migrabilite.

## Test adaptatif a appliquer

```text
LECTURE_HUMAINE = PRIORITAIRE
COMPARAISON_AUX_SOURCES = OBLIGATOIRE
CONTENU_UNIQUE = A_RETRACER
REGLES_DE_REFERENCE = LOCALES_AU_GENRE_ET_AU_PUBLIC
RETOUR_CIBLE = AUTORISE_SI_UNE_PREMISSE_EST_NON_QUALIFIEE
RESULTAT_POSSIBLE = CONSERVATION, POLISSAGE, SEPARATION_OU_AMENDEMENT_DE_LA_REGLE
PROMOTION = DECISION_HUMAINE_SEPAREE
```

La matrice elle-meme reste falsifiable : si le prototype montre que la separation public/laboratoire surcharge la lecture ou masque une route necessaire, cette hypothese sera requalifiee pour ce genre de document. Aucun resultat local ne sera generalise aux autres documents sans nouveau test.

## Requalification apres le premier prototype

```text
PROTOTYPE_LIE_AUX_CHEMINS_ACTUELS = TEMOIN_LIMITe
PROTOTYPE_COMME_ARCHITECTURE_CIBLE = SUSPENDU
REDACTION_AUTONOME_PAR_CLASSE = A_OUVRIR
LIENS_INTER_DOCUMENTAIRES = A_REPORTER_APRES_STABILISATION_DES_CLASSES
```

Le prototype n'est ni invalide comme essai de lecture ni recevable comme
architecture future. Il a montré que la correction des liens et la
preservation du contenu doivent etre testees separement : la premiere porte
sur l'etat present du depot, la seconde sur la capacite d'un document a migrer
vers une organisation encore undecidee.

## Sortie attendue du prochain palier

Produire un cadrage interne des classes documentaires et de leurs contrats de
capacite, sans imposer encore de chemins, de noms de destination ou de liens.
Le README racine et l'accueil des cycles deviennent des temoins, non les
premieres cibles de migration.
