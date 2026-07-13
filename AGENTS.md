# Guide d'amorcage pour agents

Ce fichier complete le [README](README.md). Lire les deux avant toute
modification substantielle.

## Mission du depot

Le corpus etudie la question :

> Dans quelle mesure une grandeur peut-elle etre dite constante ?

Une conclusion ne doit jamais transformer une stabilisation situee en
constance absolue. Distinguer systematiquement le regime physique, l'acces
epistemique, le mode de stabilisation, la trajectoire et les limites.

## Premier parcours

1. Lire le [README](README.md), puis l'
   [index raisonne](05_CARTES_ET_SYNTHESES/Index_raisonne_du_corpus_v1_0.md).
2. Identifier le statut du document cible : reference active, protocole,
   consolidation, preuve locale ou source primaire historique.
3. Ne lire ensuite que la couche necessaire :
   methode, cycle physique, test taxonomique, architecture, synthese ou
   philosophie.
4. Consulter le [glossaire](GLOSSAIRE.md) avant de modifier un terme de rang
   theorique.

Les entrees philosophiques et les travaux recents sont reperes par le
[supplement d'index](05_CARTES_ET_SYNTHESES/Index_supplement_pan_philosophique_v0_1.md).

## Architecture documentaire

| Dossier | Fonction | Point d'entree |
|---|---|---|
| `01_CADRE_METHODOLOGIQUE` | Methode, protocoles, cadres de lecture | `Note_methodologique_courte_post_v1_3.md` |
| `02_CYCLES_PHYSIQUES` | Fiches, calculs, preuves et syntheses de cycle | le sous-dossier du cycle concerne |
| `03_TESTS_TAXONOMIQUES` | Genealogie et tests des anciennes familles | `README.md` du dossier |
| `04_ARCHITECTURES` | Architectures actives et raccords transversaux | `Cercle2_architectures_actives_v0_1.md` |
| `05_CARTES_ET_SYNTHESES` | Index, cartes, audits et syntheses globales | `Index_raisonne_du_corpus_v1_0.md` |
| `06_PHILOSOPHIE` | Exploration philosophique et tests de situations | `README.md` du dossier |
| `90_Critiques_ constantes_effectives_stabilisees` | Sources de critiques constructives | documents actifs avant sources |

Les documents de reference active priment sur les documents de consolidation.
Les preuves locales justifient une decision sans remplacer la methode ou la
carte. Les sources historiques servent a la provenance et a la verification.

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
```

La branche `agent/cycle-fixite-electrofaible-dynamique` est un sommet
historique de la chaine refondation -> fine-tuning -> fixite electrofaible.
Son contenu est inclus dans la branche de consolidation. Si un agent est
place sur cette branche historique, son README ne contient pas a lui seul la
nouvelle carte du depot : utiliser plutot le checkout consolide ou `main`
apres fusion, sauf demande explicite de travailler sur l'historique.

## Travail sur la fixite electrofaible dynamique

Pour une tache dans
`02_CYCLES_PHYSIQUES/10_Cycle_fixite_electrofaible_dynamique`, suivre cet
ordre :

1. `cadrage-cycle-fixite-electrofaible-dynamique.md`
2. `synthese-phase1-fixite-electrofaible-dynamique.md`
3. `resultats-phase2-modele-minimal.md`
4. `resultats-phase3-regime-quartique.md`
5. `resultats-phase4-toy-model-dissipatif.md`

Lire les fiches de typologie, mecanismes et contraintes seulement selon le
probleme traite. Les scripts dans `calculs/` sont des outils de calcul ; ne
modifier ni leur interpretation ni les fichiers de resultats sans relire la
synthese de phase correspondante.

## Mode de travail attendu

1. Delimiter la question et les documents de rang actif concernes.
2. Distinguer clairement fait source, inference, hypothese et proposition.
3. Modifier un ensemble coherent de documents, sans changement opportuniste.
4. Pour une modification documentaire, lancer les audits adaptes dans
   `audit/` et verifier les liens touches.
5. Produire des commits lisibles ; reserver push et pull request aux jalons
   substantiels ou a une demande explicite.
