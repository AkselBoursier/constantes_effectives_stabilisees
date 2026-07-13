# Guide d'amorcage pour agents

Ce fichier complete le [README](README.md). Lire les deux avant toute
modification substantielle.

## Mission du depot

Le corpus etudie la question :

> Dans quelle mesure une grandeur peut-elle etre dite constante ?

Une conclusion ne doit jamais transformer une stabilisation d'acces ou une
architecture de constitution en constance de l'objet sans test supplementaire.
Distinguer systematiquement :

```text
constance de l'objet ;
stabilisation de l'acces ou de l'estimation ;
mode de constitution ou d'organisation.
```

La decision active est :

- [Decision de rang — constance, acces et constitution](01_CADRE_METHODOLOGIQUE/Decision_statuts_constance_acces_constitution_v0_1.md)

## Premier parcours

1. Lire le [README](README.md).
2. Lire le [cadre canonique](01_CADRE_METHODOLOGIQUE/refondation-du-domaine.md).
3. Lire la [decision de rang](01_CADRE_METHODOLOGIQUE/Decision_statuts_constance_acces_constitution_v0_1.md).
4. Consulter l'[index raisonne](05_CARTES_ET_SYNTHESES/Index_raisonne_du_corpus_v1_0.md).
5. Identifier le statut du document cible : reference active, decision
   canonique, protocole, consolidation, preuve locale, exploration ou source.
6. Ne lire ensuite que la couche necessaire : methode, cycle physique, test
   taxonomique, architecture, synthese ou philosophie.
7. Consulter le [glossaire](GLOSSAIRE.md) avant de modifier un terme de rang
   theorique.

Les entrees philosophiques et les travaux recents sont reperes par le
[supplement d'index](05_CARTES_ET_SYNTHESES/Index_supplement_pan_philosophique_v0_1.md).

Les jonctions entre chantiers sont explicitees par la
[carte des frottements](05_CARTES_ET_SYNTHESES/Carte_frottements_chantiers_v0_1.md).

## Architecture documentaire

| Dossier | Fonction | Point d'entree |
|---|---|---|
| `01_CADRE_METHODOLOGIQUE` | Methode, protocoles, cadres et decisions de rang | `refondation-du-domaine.md` |
| `02_CYCLES_PHYSIQUES` | Fiches, calculs, preuves et syntheses de cycle | le sous-dossier du cycle concerne |
| `03_TESTS_TAXONOMIQUES` | Genealogie et tests des anciennes familles | `README.md` du dossier |
| `04_ARCHITECTURES` | Architectures actives et raccords transversaux | `Cercle2_architectures_actives_v0_1.md` |
| `05_CARTES_ET_SYNTHESES` | Index, cartes, audits et syntheses globales | `Index_raisonne_du_corpus_v1_0.md` |
| `06_PHILOSOPHIE` | Exploration philosophique, situations, voisinages et tests | `README.md` du dossier |
| `90_Critiques_ constantes_effectives_stabilisees` | Sources de critiques constructives | documents actifs avant sources |

Ordre de precedence :

```text
cadre canonique et decisions de rang
> protocoles actifs
> syntheses validees de cycle
> cartes et consolidations
> explorations et programmes
> sources historiques et extractions.
```

Les preuves locales justifient une decision sans remplacer le cadre. Les
sources historiques servent a la provenance et a la verification.

## Regles de niveau

Avant toute conclusion, identifier ce qui est affirme :

| Niveau | Question | Exemple de sortie correcte |
|---|---|---|
| Objet | qu'est-ce qui tient fixe sous quelles transformations ? | constante physique, effective ou metrologique |
| Acces | comment la valeur ou le domaine admissible sont-ils etablis ? | mesure, reconstruction, borne, tension |
| Constitution | comment la relation ou le regime deviennent-ils operatoires ? | secteur, seuil, architecture, dynamique |
| Interpretation | quelle portee philosophique attribuer au resultat ? | hypothese ou argument explicitement modalise |

Ne pas employer `mode de constance` pour une borne, une reconstruction ou une
architecture sans preciser le niveau.

## Sources primaires et extractions

- Les DOCX et `Ecriture.txt` sont des sources primaires : ne pas les
  supprimer, les renommer ou les reecrire.
- Ils sont ranges dans les dossiers thematiques `00_Sources_docx`.
- Les fichiers `Source_docx_*` et `Source_txt_*` sont des extractions de
  travail, non des sources scientifiques autonomes.
- Avant de reprendre une formule, un tableau, une image ou un passage
  incomplet, verifier le DOCX original.
- Ne jamais inventer un contenu absent ni effacer un placeholder sans cette
  verification.
- Le
  [registre des sources primaires](05_CARTES_ET_SYNTHESES/Registre_sources_primaires_v0_1.md)
  associe chaque source a son extraction et a son SHA-256.
- La [convention des placeholders](CONVENTION_PLACEHOLDERS.md) fixe les
  avertissements et les statuts a conserver.

## Regles intellectuelles

1. Ne pas restaurer les anciennes familles taxonomiques comme classement de
   premier niveau.
2. Ne pas presenter une hypothese, une piste ou une preuve locale comme une
   conclusion generale.
3. Ne pas fabriquer de references scientifiques absentes du corpus.
4. Conserver le francais et le vocabulaire stabilise du projet.
5. Toute decision conceptuelle, changement de rang documentaire ou conclusion
   physique nouvelle requiert une validation humaine explicite.
6. Ne pas convertir une borne, une tension ou une reconstruction en constance
   de l'objet.
7. Ne pas convertir un toy model en histoire cosmique realisee.
8. Ne pas convertir une ouverture ontologique en resultat physique.

## Git et genealogie

Lire le
[workflow GitHub v0.2](01_CADRE_METHODOLOGIQUE/Workflow_GitHub_v0_2.md)
et le
[registre des branches](01_CADRE_METHODOLOGIQUE/Registre_branches_corpus_v0_1.md)
avant une intervention multi-documents.

Regle pratique :

```text
main                 = etat valide apres revue
travail              = integration quotidienne a resynchroniser depuis main
branche thematique   = chantier borne
branche historique   = provenance, pas point de depart implicite
branche recuperation = union exceptionnelle, non canonique avant validation
```

La branche `agent/cycle-fixite-electrofaible-dynamique` est un sommet
historique de la chaine refondation -> fine-tuning -> fixite electrofaible.
Son contenu est inclus dans la branche de consolidation. Utiliser le checkout
consolide ou `main` apres fusion, sauf demande explicite de travailler sur
l'historique.

Les nouvelles corrections de consolidation doivent partir d'une branche
bornee, puis etre revues avant d'etre integrees a la branche de recuperation.

## Travail sur la fixite electrofaible dynamique

Pour une tache dans
`02_CYCLES_PHYSIQUES/10_Cycle_fixite_electrofaible_dynamique`, suivre cet
ordre :

1. `cadrage-cycle-fixite-electrofaible-dynamique.md`
2. `synthese-phase1-fixite-electrofaible-dynamique.md`
3. `resultats-phase2-modele-minimal.md`
4. `resultats-phase3-regime-quartique.md`
5. `resultats-phase4-toy-model-dissipatif.md`

Lire ensuite la decision de rang et la carte des frottements avant de tirer une
consequence philosophique du cycle.

Les scripts dans `calculs/` sont des outils de calcul ; ne modifier ni leur
interpretation ni les fichiers de resultats sans relire la synthese de phase
correspondante.

## Travail sur le pan philosophique

Le dossier `06_PHILOSOPHIE` est une exploration active, non une doctrine deja
integree au noyau.

Avant de promouvoir une proposition philosophique :

1. verifier son statut dans le README philosophique ;
2. consulter l'audit d'integration philosophique ;
3. identifier le niveau concerne : qualification, constitution ou ontologie ;
4. rechercher les contre-exemples dans les cycles physiques ;
5. inscrire la jonction dans la carte des frottements.

## Mode de travail attendu

1. Delimiter la question et les documents de rang actif concernes.
2. Distinguer clairement fait source, inference, hypothese et proposition.
3. Modifier un ensemble coherent de documents, sans changement opportuniste.
4. Pour une modification documentaire, lancer les audits adaptes dans
   `audit/` et verifier les liens touches.
5. Verifier les references de version, les fichiers annonces et les blocs non
   fermes avant un jalon.
6. Produire des commits lisibles ; reserver push et pull request aux jalons
   substantiels ou a une demande explicite.
