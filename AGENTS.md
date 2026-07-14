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
| `02_CYCLES_PHYSIQUES` | Fiches, calculs, preuves et syntheses de cycle | `README.md` du dossier, puis le sous-dossier concerne |
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

- Les documents Microsoft Word (`DOCX`) et `Ecriture.txt` sont des sources primaires : ne pas les
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
  associe chaque source a son extraction et a son empreinte produite par
  l'algorithme de hachage securise sur 256 bits (`SHA-256`).
- La [convention des placeholders](CONVENTION_PLACEHOLDERS.md) fixe les
  avertissements et les statuts a conserver.
- Les exports de conversation `ChatGPT-Recherche sur les constantes.json` et
  `ChatGPT-Recherche sur les constantes.md` sont des sources brutes de
  provenance. Ne pas les normaliser ni corriger leurs titres repetes ; ces
  repetitions peuvent produire des avertissements d'audit attendus.
- Lire leur extraction raisonnee dans
  `05_CARTES_ET_SYNTHESES/Extraction_questions_conversation_cycles_1_a_3_v0_1.md`
  plutot que de tirer directement une attribution intellectuelle des roles de
  conversation.

## Archive des travaux anterieurs

Le dossier `91_TRAVAUX_ANTERIEURS` est une archive genealogique placee a la
racine. Ce n'est ni une branche Git, ni un cadre actif, ni un reservoir a
reinjecter automatiquement.

Regles :

1. lire d'abord son `README.md` ;
2. employer les documents pour reperer des antecedents, bifurcations, abandons
   et reformulations ;
3. ne restaurer aucun concept, resultat ou vocabulaire sans comparaison avec
   l'etat actif, verification scientifique et validation humaine ;
4. ne pas inferer la chronologie d'origine depuis la seule date du commit Git ;
5. ne pas reproduire les identifiants, adresses, liens de conversation ou URL
   signees contenus dans les exports bruts ;
6. traiter les notes anciennes sur la mesure comme antecedents en quarantaine,
   non comme cadrage actuel du futur chantier.

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

## Provenance humaine et modeles de langage

Le role affiche dans une conversation renseigne la provenance textuelle d'une
phrase, pas sa propriete intellectuelle complete.

Regles :

1. Ne pas inferer, depuis l'alternance `Prompt` / `Response`, qui a fourni seul
   l'intuition, l'orientation ou la rigueur d'une question.
2. Distinguer la formulation visible, les recherches et intuitions anterieures,
   la selection des pistes, la redirection, la redaction et la validation.
3. Lorsque l'archive ne permet pas une attribution fine, parler de construction
   distribuee ou de co-construction, non d'invention exclusive.
4. Ne pas reduire l'auteur a l'approbation de propositions, ni attribuer a
   l'auteur toute phrase produite par un modele.
5. Limiter les indications de provenance aux endroits ou elles eclairent une
   decision, une bifurcation ou une responsabilite scientifique. Ne pas ajouter
   de didascalies d'attribution dans chaque fiche.
6. Une attribution juridique ou editoriale exige un protocole propre et ne
   doit pas etre deduite d'une extraction de conversation.
7. Appliquer une condition d'arret : lorsque les traces suffisent a eviter une
   fausse attribution et a comprendre la decision, ne pas poursuivre la fouille
   pour etablir une propriete intellectuelle. La genealogie n'est rouverte que
   pour une question scientifique, editoriale ou historique determinee.

## Lisibilite des sigles et des codes

Un sigle ou un code reste utile pour naviguer, mais il ne doit jamais etre le
seul moyen de comprendre une phrase.

Regle de redaction : a la premiere occurrence dans un document, donner le nom
ou la fonction en toutes lettres, directement dans la phrase, puis le code
entre parentheses. Exemples : `mecanisme Brout-Englert-Higgs (BEH)`, `Systeme
international d'unites (SI)` ou `question de qualification (Q-qual)`.

Les conventions actives sont la question de qualification de la constance
(`Q-qual`), la question de formation, de maintien ou de dissolution d'un statut
(`Q-form`), le chantier sur les categories, les acces et les inferences en
microphysique (`chantier Q`) et les niveaux de maturite d'une contribution
(`C0-C4`).

Les noms de fichiers historiques peuvent conserver leurs anciens codes. Dans
le texte actif, expliciter leur fonction et eviter les formules comme `Q2 est
acquis` lorsqu'elles ne permettent pas de savoir de quelle serie il s'agit.

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
   substantiels ou a une demande explicite, sauf dans l'environnement ChatGPT
   classic vise par l'exception stricte decrite dans le workflow GitHub v0.2.
