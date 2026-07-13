# constantes_effectives_stabilisees

Corpus de travail sur les constantes effectives stabilisees.

**Question directrice** : dans quelle mesure une grandeur peut-elle etre dite
constante ?

> **Pour un agent** : lire d'abord le
> [guide d'amorcage](AGENTS.md), puis ce README.

> **Decision de rang active** : distinguer la
> [constance de l'objet, la stabilisation de l'acces et le mode de constitution](01_CADRE_METHODOLOGIQUE/Decision_statuts_constance_acces_constitution_v0_1.md).
> Une borne, une reconstruction ou une tension peuvent stabiliser une
> qualification sans devenir, a elles seules, une constance de l'objet.

> Une constante effective stabilisee est une grandeur physiquement ou
> formellement identifiee dont la fixite est testee dans un regime et sous des
> transformations declares. Les modes d'acces et de constitution qualifient ou
> expliquent cette fixite sans etre automatiquement des statuts de constance.

## Entree rapide

Commencer par :

1. [Cadre canonique de refondation](01_CADRE_METHODOLOGIQUE/refondation-du-domaine.md)
   pour les criteres d'admission et de refus.
2. [Decision de rang](01_CADRE_METHODOLOGIQUE/Decision_statuts_constance_acces_constitution_v0_1.md)
   pour separer objet, acces et constitution.
3. [Grille de lecture des 8 modes](05_CARTES_ET_SYNTHESES/Grille_lecture_8_modes_v0_1.md)
   comme outil de qualification, sans promotion automatique en statuts de constance.
4. [Index raisonne du corpus v1.0](05_CARTES_ET_SYNTHESES/Index_raisonne_du_corpus_v1_0.md)
   pour la navigation physique et methodologique.
5. [Supplement d'index du pan philosophique](05_CARTES_ET_SYNTHESES/Index_supplement_pan_philosophique_v0_1.md)
   pour la couche philosophique, les tests et les livrables recents.
6. [Carte des frottements](05_CARTES_ET_SYNTHESES/Carte_frottements_chantiers_v0_1.md)
   pour les jonctions entre refondation, philosophie, fine-tuning et fixite dynamique.
7. [Workflow GitHub v0.2](01_CADRE_METHODOLOGIQUE/Workflow_GitHub_v0_2.md)
   pour le statut de `main`, `travail` et des branches thematiques.

Puis suivre, selon le besoin :

| Priorite | Document | Role |
|---|---|---|
| 1 | [Note methodologique courte](01_CADRE_METHODOLOGIQUE/Note_methodologique_courte_post_v1_3.md) | Criblage pratique des cas litigieux ; references en cours de resynchronisation |
| 2 | [Carte consolidee v1.3](05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_3_post_cercle2.md) | Etat transversal du pan physique |
| 3 | [Matrice des acquis theoriques](05_CARTES_ET_SYNTHESES/Matrice_acquis_theoriques_v0_1.md) | Acquis argumentables et limites |
| 4 | [Synthese de la refondation](05_CARTES_ET_SYNTHESES/synthese-refondation-des-cycles.md) | Resultats des cycles relationnels |
| 5 | [README philosophique](06_PHILOSOPHIE/README.md) | Charte, genres et ordre de lecture du pan philosophique |
| 6 | [Audit d'integration philosophique](05_CARTES_ET_SYNTHESES/Audit_integration_branche_philosophique_v0_1.md) | Tri entre apports actifs, hypotheses et reserves |

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
| Cadre canonique | [Refondation du domaine](01_CADRE_METHODOLOGIQUE/refondation-du-domaine.md) | Reference active |
| Decision de rang | [Objet, acces et constitution](01_CADRE_METHODOLOGIQUE/Decision_statuts_constance_acces_constitution_v0_1.md) | Arbitrage canonique actif |
| Methode | [Note methodologique v1.3](01_CADRE_METHODOLOGIQUE/Note_synthese_methodologique_v1_3_pre_familial_et_temporalite.md) | Reference active sous controle du cadre canonique |
| Cycles physiques | [02_CYCLES_PHYSIQUES](02_CYCLES_PHYSIQUES/) | Preuves locales et syntheses de cycle |
| Fine-tuning | [Cadrage du cycle](02_CYCLES_PHYSIQUES/09_Cycle_fine_tuning/cadrage-cycle-fine-tuning.md) | Cycle transversal de test |
| Fixite electroweak dynamique | [Cadrage du cycle](02_CYCLES_PHYSIQUES/10_Cycle_fixite_electrofaible_dynamique/cadrage-cycle-fixite-electrofaible-dynamique.md) | Cycle de test dynamique |
| Tests taxonomiques | [README des tests](03_TESTS_TAXONOMIQUES/README.md) | Genealogie controlee des categories |
| Architectures | [Cercle 2](04_ARCHITECTURES/Cercle2_architectures_actives_v0_1.md) | Architectures actives |
| Cartes et syntheses | [Carte consolidee v1.3](05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_3_post_cercle2.md) | Navigation transverse |
| Jonctions | [Carte des frottements](05_CARTES_ET_SYNTHESES/Carte_frottements_chantiers_v0_1.md) | Dialogue controle entre chantiers |
| Philosophie | [README philosophique](06_PHILOSOPHIE/README.md) | Exploration active en amont des decisions de rang |

Les statuts documentaires de reference sont : **reference active**,
**decision canonique**, **protocole actif**, **consolidation**, **preuve locale**,
**source primaire historique** et **archive future**. Voir la
[convention des placeholders](CONVENTION_PLACEHOLDERS.md) pour les extractions.

## Sources primaires DOCX

Les DOCX et le fichier texte historique sont des sources primaires, non des
archives prematures. Ils sont conserves sans modification; leur extraction
Markdown, leur rattachement et leur verification sont pilotes par :

- [Plan de remontee des sources](05_CARTES_ET_SYNTHESES/Plan_remontee_sources_docx_markdown_v0_1.md)
- [Table de remontee des sources](05_CARTES_ET_SYNTHESES/Table_remontee_sources_docx_v0_1.md)
- [Registre des sources primaires](05_CARTES_ET_SYNTHESES/Registre_sources_primaires_v0_1.md)

Les originaux sont ranges dans les dossiers thematiques `00_Sources_docx`;
le registre associe chaque original a son extraction et a son empreinte
SHA-256.

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

La branche de recuperation rassemble actuellement les chantiers historiques.
Elle reste soumise a audit et ne constitue pas encore le tronc valide.

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

Un audit de structure doit egalement verifier avant fusion :

```text
marqueurs de conflit ;
blocs Markdown non fermes ;
titres terminaux vides ;
references a des fichiers inexistants ;
anciennes versions encore declarees actives.
```

## Regles de contribution et de reprise

1. Ne pas modifier le contenu scientifique des sources historiques DOCX.
2. Ne pas supprimer les DOCX ni les extractions `Source_docx_*`.
3. Ne pas restaurer les anciennes familles comme premier niveau de classement.
4. Ne pas fabriquer de references scientifiques absentes des sources.
5. Conserver le francais et les conventions lexicales du corpus.
6. Signaler les passages incomplets avec la convention de placeholder.
7. Valider explicitement toute decision conceptuelle.
8. Distinguer constance de l'objet, stabilisation de l'acces et mode de constitution.
9. Privilegier des commits lisibles, coherents et reversibles.
