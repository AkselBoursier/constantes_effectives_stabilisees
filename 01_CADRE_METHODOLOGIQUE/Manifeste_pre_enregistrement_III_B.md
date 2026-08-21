# Manifeste de pré-enregistrement — Phase III-B

## Statut

Ce manifeste scelle le dispositif prospectif après contrôle d'équivalence et pré-vol d'accès, avant toute réponse d'agent III-B.

```text
PHASE_III_B = PRE_ENREGISTREE_NON_LANCEE
BASE_SUBSTANTIELLE = main@c9deaf1fe86b742d9227f0385e975809f64dc9bd
NOMBRE_TACHES = 2
NOMBRE_CONDITIONS_PAR_TACHE = 2
NOMBRE_CHATS_INITIAUX = 4
REPONSE_PROSPECTIVE_RECUE_A_CE_STADE = 0
MUTATION_MAIN = NON
MUTATION_SCIENTIFIQUE = NON
PROMOTION_TRIGGER = NON
MERGE_139 = NON_AUTORISE
```

Après ce manifeste, un changement de bootstrap, mission, matrice ou grille motivé par une réponse observée ne peut pas être présenté comme la même expérience pré-enregistrée. Il exige une version/amendement explicite et une qualification de son effet.

## 1. Paquet commun

`III_B_PRE_ENREGISTRE/BOOTSTRAP_COMMUN.md`

```text
blob = 77ca397554466952ba6be4460280f4b308246972
fonction = trigger pré-travail commun
```

Le bootstrap impose : matrice avant analyse substantielle, déclencheurs/silences matériels, recherche autonome des autorités du cas, `NON_ETABLI` plutôt qu'invention, réponse humaine séparée de la trace technique, aucune mutation.

## 2. Tâche S — Cycle 10

### Mission

`III_B_PRE_ENREGISTRE/TACHE_S/MISSION.md`

```text
blob = 64f7aae397dbe27ed0d3af489a2787f572bca59a
```

### Conditions documentaires

```text
MATRICE_7A.md
blob = ed653ab283142026da79a34731b05f619ea5733f

MATRICE_9C.md
blob = 81c4965c1772c3a85003ec977b0b8fe7ef5ea8c1
```

Les deux conditions contiennent les mêmes 13 unités fonctionnelles et les mêmes six relations qualifiées. Le contrôle d'équivalence est séparé côté évaluateur.

### Pré-vol d'accès

Sur la base substantielle gelée, ont été relus avec succès sans utiliser la référence évaluateur :

- cadrage du Cycle 10 ;
- résultats phases 2, 3 et 4 ;
- `01_CADRE_METHODOLOGIQUE/refondation-du-domaine.md` ;
- `Decision_statuts_constance_acces_constitution_v0_1.md` ;
- accueil courant des cycles.

La récupération autonome du cadre est donc matériellement possible ; son succès reste une variable du test.

## 3. Tâche M — prototype Human-First

### Mission

`III_B_PRE_ENREGISTRE/TACHE_M/MISSION.md`

```text
blob = 99c411efedf5bea90da4edaf62aca72276ffd630
```

### Conditions documentaires

```text
MATRICE_7A.md
blob = 88f8092a5e1a3756c9c25f6d8d8aef8c2d4cce9e

MATRICE_9C.md
blob = d7559440b98974bce9386eaeef7dc6f04a2f7580
```

Les deux conditions contiennent les mêmes 13 unités fonctionnelles et les mêmes treize relations qualifiées.

### Pré-vol d'accès

Sont récupérables :

- `main@c9deaf1f...` ;
- branche `test/human-first-reprise-blind-20260819` ;
- delta Git de la branche : 3 commits devant, 0 derrière, deux fichiers modifiés ;
- issue #136 et commentaires contenant test T0, requalification des environnements et ouverture ultérieure de la correction expérimentale.

Le cas est donc matériellement instructible sans fournir la référence évaluateur.

## 4. Évaluation gelée

### Grille qualitative/prospective

`III_B_EVALUATEUR/Grille_scoring_III_B_prospective.csv`

```text
blob = ed83282031859b9974d366f0dad9e5f439f8e05e
```

Profils séparés : profondeur, systématicité, probité, méthodologie, couche fonctionnelle ; récupération canonique + qualité scientifique pour S ; qualité méthodologique spécifique pour M ; flags critiques séparés. Aucun total global unique.

### Human-First

`Grille_Human_First_III_B.csv`

```text
blob = 578fd70cc2ddd2b86ab1afdfaf5bdd1214c44ed6
```

Le jugement humain sur la réponse principale est primaire. La trace technique ne donne aucun avantage Human-First.

### Contrôle d'équivalence

`III_B_EVALUATEUR/Controle_equivalence_semantique.md`

```text
blob = 3d00b983667cc265dd95d19f7c09d1b82228b560
EQUIVALENCE_TACHE_S = SUFFISANTE_POUR_LANCEMENT
EQUIVALENCE_TACHE_M = SUFFISANTE_POUR_LANCEMENT
```

### Références évaluateur-only

```text
Reference_evaluateur_cadre_canonique_III_B.md
blob = 623df5dbc76cc39ece9b15b843762f8a37f9a1fe

III_B_EVALUATEUR/Reference_evaluateur_tache_M.md
blob = 529b990c1dd7e6c463dc7106d229cd44fc3f0dcd
```

Ne pas fournir ces pièces aux agents.

### Consigne évaluateur

`III_B_EVALUATEUR/Consigne_evaluateur_III_B.md`

```text
blob = 18cc39674bf4177489c85725e94ae5c7cebf8878
```

## 5. Clé et ordre cachés

`III_B_EVALUATEUR/Cle_conditions_et_ordre.md`

```text
blob = da589414d3737885a03f120510c701952ca77604
```

La clé documentaire et l'ordre initial sont pré-enregistrés. Cette pièce ne doit être ni fournie aux agents ni révélée avant gel des quatre réponses brutes et des scorings Human-First primaires.

## 6. Règles de lancement

Chaque essai doit utiliser :

```text
UN_CHAT_EPHEMERE_NEUF
MEME_MODELE_SI_POSSIBLE
AUCUNE_MEMOIRE_DU_PROJET
AUCUN_CONTEXTE_DE_CETTE_CONVERSATION
ACCES_GITHUB_IDENTIQUE
UNE_SEULE_REPONSE_BRUTE
AUCUNE_RELANCE_AVANT_GEL
```

Le message de lancement contient seulement :

1. nom du dépôt ;
2. branche porteuse du paquet ;
3. chemins exacts du bootstrap, de la matrice assignée et de la mission ;
4. obligation de les lire dans cet ordre et de ne pas consulter les autres fichiers d'audit.

## 7. Gel des réponses

Après chaque chat :

1. copier/exporter la réponse brute sans correction ;
2. la remettre dans la conversation de contrôle ;
3. enregistrer son empreinte et son identité expérimentale ;
4. ne pas discuter substantiellement la réponse avec l'agent testé ;
5. ne pas révéler la condition historique ;
6. poursuivre l'ordre pré-enregistré.

Le scoring comparatif et la révélation de la clé n'interviennent qu'après les quatre réponses initiales.

## 8. État terminal du pré-vol

```text
PAQUETS = GELES
GRILLES = GELEES
REFERENCES_EVALUATEUR = GELEES
EQUIVALENCE_SEMANTIQUE = CONTROLEE
ACCES_TACHE_S = POSITIF
ACCES_TACHE_M = POSITIF
CLE_ET_ORDRE = GELES
PHASE_III_B = PRETE_A_LANCER
PREMIERE_REPONSE = NON_RECUE
```
