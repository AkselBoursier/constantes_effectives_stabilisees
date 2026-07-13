# constantes_effectives_stabilisees

Corpus de travail sur les constantes effectives stabilisees.

**Question directrice** : dans quelle mesure une grandeur peut-elle etre dite
constante ?

> Une constante effective stabilisee est une grandeur dont une valeur, une
> forme, une liaison qualifiee, un role ou une dependance devient robuste dans
> un regime donne, selon un acces determine, avec un mode et une trajectoire de
> stabilisation explicites, sans que cette robustesse implique necessairement
> une constance absolue, une universalite hors contexte ou un statut
> fondamental.

## Entree rapide

Commencer par :

1. [Grille de lecture des 8 modes](05_CARTES_ET_SYNTHESES/Grille_lecture_8_modes_v0_1.md)
   pour qualifier toute grandeur.
2. [Index raisonne du corpus v1.0](05_CARTES_ET_SYNTHESES/Index_raisonne_du_corpus_v1_0.md)
   pour la navigation physique et methodologique.
3. [Supplement d'index du pan philosophique](05_CARTES_ET_SYNTHESES/Index_supplement_pan_philosophique_v0_1.md)
   pour la couche philosophique, les tests et les livrables recents.
4. [Workflow GitHub v0.2](01_CADRE_METHODOLOGIQUE/Workflow_GitHub_v0_2.md)
   pour le statut de `main`, `travail` et des branches thematiques.

Puis suivre, selon le besoin :

| Priorite | Document | Role |
|---|---|---|
| 1 | [Note methodologique courte](01_CADRE_METHODOLOGIQUE/Note_methodologique_courte_post_v1_3.md) | Criblage pratique des cas litigieux |
| 2 | [Carte consolidee v1.3](05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_3_post_cercle2.md) | Etat transversal du pan physique |
| 3 | [Matrice des acquis theoriques](05_CARTES_ET_SYNTHESES/Matrice_acquis_theoriques_v0_1.md) | Acquis argumentables et limites |
| 4 | [Synthese de la refondation](05_CARTES_ET_SYNTHESES/synthese-refondation-des-cycles.md) | Resultats des cycles relationnels |
| 5 | [README philosophique](06_PHILOSOPHIE/README.md) | Charte, genres et ordre de lecture du pan philosophique |
| 6 | [Audit de taxonomie](05_CARTES_ET_SYNTHESES/Audit_taxonomie_v0_1.md) | Diagnostic et decisions sur la genealogie taxonomique |

## Organisation du depot

```text
constantes_effectives_stabilisees/
|
|-- 01_CADRE_METHODOLOGIQUE/    methode, protocoles et sources de methode
|-- 02_CYCLES_PHYSIQUES/        fiches, cycles, calculs et syntheses locales
|-- 03_TESTS_TAXONOMIQUES/      genealogie et tests des anciennes familles
|-- 04_ARCHITECTURES/           architectures actives et raccords transversaux
|-- 05_CARTES_ET_SYNTHESES/     cartes, index, audits et syntheses globales
|-- 06_PHILOSOPHIE/             exploration philosophique, situations et tests
|-- 90_Critiques_.../           sources de critiques constructives
|-- audit/                       controles documentaires
|-- GLOSSAIRE.md                 termes de reference
`-- CONVENTION_PLACEHOLDERS.md  statut des extractions et limites de conversion
```

## Couches documentaires

| Couche | Point d'entree | Statut |
|---|---|---|
| Methode | [Note methodologique v1.3](01_CADRE_METHODOLOGIQUE/Note_synthese_methodologique_v1_3_pre_familial_et_temporalite.md) | Reference active |
| Refonte des cycles | [Cadre canonique](01_CADRE_METHODOLOGIQUE/refondation-du-domaine.md) | Consolidation relationnelle |
| Cycles physiques | [02_CYCLES_PHYSIQUES](02_CYCLES_PHYSIQUES/) | Preuves locales et syntheses de cycle |
| Fine-tuning | [Cadrage du cycle](02_CYCLES_PHYSIQUES/09_Cycle_fine_tuning/cadrage-cycle-fine-tuning.md) | Cycle transversal de test |
| Fixite electroweak dynamique | [Cadrage du cycle](02_CYCLES_PHYSIQUES/10_Cycle_fixite_electrofaible_dynamique/cadrage-cycle-fixite-electrofaible-dynamique.md) | Cycle de test dynamique |
| Tests taxonomiques | [README des tests](03_TESTS_TAXONOMIQUES/README.md) | Genealogie controlee des categories |
| Architectures | [Cercle 2](04_ARCHITECTURES/Cercle2_architectures_actives_v0_1.md) | Architectures actives |
| Cartes et syntheses | [Carte consolidee v1.3](05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_3_post_cercle2.md) | Navigation transverse |
| Philosophie | [README philosophique](06_PHILOSOPHIE/README.md) | Exploration active en amont des degagements |

Les statuts documentaires de reference sont : **reference active**,
**protocole actif**, **consolidation**, **preuve locale**, **source primaire
historique** et **archive future**. Voir la
[convention des placeholders](CONVENTION_PLACEHOLDERS.md) pour leur usage.

## Sources primaires DOCX

Les DOCX et le fichier texte historique sont des sources primaires, non des
archives prematures. Ils sont conserves sans modification; leur extraction
Markdown, leur rattachement et leur verification sont pilotes par :

- [Plan de remontee des sources](05_CARTES_ET_SYNTHESES/Plan_remontee_sources_docx_markdown_v0_1.md)
- [Table de remontee des sources](05_CARTES_ET_SYNTHESES/Table_remontee_sources_docx_v0_1.md)

Les fichiers `Source_docx_*` sont des extractions de travail. Une formule,
un tableau ou une image insuffisamment restituee doit etre signale par la
convention de placeholder et verifie dans le DOCX original.

## Workflow GitHub

Le depot emploie le modele de
[Workflow GitHub v0.2](01_CADRE_METHODOLOGIQUE/Workflow_GitHub_v0_2.md) :

```text
main     : etat valide du corpus ;
travail  : integration quotidienne des chantiers ;
branches : chantiers thematiques, conserves jusqu'a leur integration validee.
```

Le [registre des branches](01_CADRE_METHODOLOGIQUE/Registre_branches_corpus_v0_1.md)
situe les chantiers historiques et leur presence dans l'integration courante.

Les decisions conceptuelles restent soumises a validation explicite. Les
reorganisations documentaires, controles et commits peuvent etre delegues une
fois le contenu stabilise.

## Audits documentaires

Les controles existants sont dans [`audit/`](audit/).

```bash
bash audit/audit_placeholders.sh
bash audit/audit_liens.sh
bash audit/audit_encodage.sh
```

## Regles de contribution et de reprise

1. Ne pas modifier le contenu scientifique des sources historiques DOCX.
2. Ne pas supprimer les DOCX ni les extractions `Source_docx_*`.
3. Ne pas restaurer les anciennes familles comme premier niveau de classement.
4. Ne pas fabriquer de references scientifiques absentes des sources.
5. Conserver le francais et les conventions lexicales du corpus.
6. Signaler les passages incomplets avec la convention de placeholder.
7. Valider explicitement toute decision conceptuelle.
8. Privilegier des commits lisibles, coherents et reversibles.
