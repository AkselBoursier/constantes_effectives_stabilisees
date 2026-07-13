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

> **Hierarchie philosophique active** :
> `constance de l'objet > constitution > acces`.
> L'acces reste indispensable comme condition probatoire et critique, mais il
> n'est pas le centre philosophique actuel du projet.

## Entree rapide

Commencer par :

1. [Cadre canonique de refondation](01_CADRE_METHODOLOGIQUE/refondation-du-domaine.md)
   pour les criteres d'admission et de refus.
2. [Decision de rang](01_CADRE_METHODOLOGIQUE/Decision_statuts_constance_acces_constitution_v0_1.md)
   pour separer objet, acces et constitution.
3. [Synthese methodologique v1.4](01_CADRE_METHODOLOGIQUE/Note_synthese_methodologique_v1_4.md)
   pour l'ordre actif : objet, constitution, acces.
4. [Index raisonne du corpus v1.1](05_CARTES_ET_SYNTHESES/Index_raisonne_du_corpus_v1_1.md)
   pour la navigation courante.
5. [Premier degagement de these v0.2](05_CARTES_ET_SYNTHESES/Premier_degagement_these_v0_2.md)
   pour la these-noyau.
6. [Carte des frottements](05_CARTES_ET_SYNTHESES/Carte_frottements_chantiers_v0_1.md)
   pour les jonctions entre refondation, philosophie, fine-tuning et fixite dynamique.
7. [Workflow GitHub v0.2](01_CADRE_METHODOLOGIQUE/Workflow_GitHub_v0_2.md)
   pour le statut de `main`, `travail` et des branches thematiques.

Puis suivre, selon le besoin :

| Priorite | Document | Role |
|---|---|---|
| 1 | [Matrice des degagements v0.2](05_CARTES_ET_SYNTHESES/Matrice_degagements_theoriques_v0_2.md) | Classe les propositions selon objet, constitution et acces |
| 2 | [Mise a l'epreuve v0.2](05_CARTES_ET_SYNTHESES/Mise_epreuve_degagements_theoriques_exemples_porteurs_v0_2.md) | Admissions, refus et cas negatifs |
| 3 | [Plan du papier A v0.2](05_CARTES_ET_SYNTHESES/Plan_livrable_papier_A_v0_2.md) | Premier article centre sur le critere de constance |
| 4 | [Note methodologique courte](01_CADRE_METHODOLOGIQUE/Note_methodologique_courte_post_v1_3.md) | Criblage pratique sous le controle de la v1.4 |
| 5 | [README philosophique](06_PHILOSOPHIE/README.md) | Charte, situations, voisinages et programmes |
| 6 | [Audit d'integration philosophique](05_CARTES_ET_SYNTHESES/Audit_integration_branche_philosophique_v0_1.md) | Tri entre apports actifs, hypotheses et reserves |

## Organisation du depot

```text
constantes_effectives_stabilisees/
|
|-- 01_CADRE_METHODOLOGIQUE/    methode, protocoles et decisions de rang
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
| Methode | [Synthese methodologique v1.4](01_CADRE_METHODOLOGIQUE/Note_synthese_methodologique_v1_4.md) | Reference active |
| These-noyau | [Premier degagement v0.2](05_CARTES_ET_SYNTHESES/Premier_degagement_these_v0_2.md) | Degagement actif |
| Cycles physiques | [02_CYCLES_PHYSIQUES](02_CYCLES_PHYSIQUES/) | Preuves locales et syntheses de cycle |
| Fine-tuning | [Cadrage du cycle](02_CYCLES_PHYSIQUES/09_Cycle_fine_tuning/cadrage-cycle-fine-tuning.md) | Cycle transversal de test |
| Fixite electroweak dynamique | [Cadrage du cycle](02_CYCLES_PHYSIQUES/10_Cycle_fixite_electrofaible_dynamique/cadrage-cycle-fixite-electrofaible-dynamique.md) | Cycle de test dynamique |
| Architectures | [Cercle 2](04_ARCHITECTURES/Cercle2_architectures_actives_v0_1.md) | Modes de constitution et de maintien |
| Cartes et syntheses | [Index v1.1](05_CARTES_ET_SYNTHESES/Index_raisonne_du_corpus_v1_1.md) | Navigation transverse |
| Jonctions | [Carte des frottements](05_CARTES_ET_SYNTHESES/Carte_frottements_chantiers_v0_1.md) | Dialogue controle entre chantiers |
| Philosophie | [README philosophique](06_PHILOSOPHIE/README.md) | Exploration active en amont des decisions de rang |

Les versions remplacees restent dans Git et dans le depot comme couches
genealogiques. Elles ne commandent plus l'usage courant lorsque leur successeur
est explicitement indique.

## Sources primaires DOCX

Les DOCX et le fichier texte historique sont des sources primaires, non des
archives prematures. Ils sont conserves sans modification; leur extraction
Markdown, leur rattachement et leur verification sont pilotes par :

- [Plan de remontee des sources](05_CARTES_ET_SYNTHESES/Plan_remontee_sources_docx_markdown_v0_1.md)
- [Table de remontee des sources](05_CARTES_ET_SYNTHESES/Table_remontee_sources_docx_v0_1.md)
- [Registre des sources primaires](05_CARTES_ET_SYNTHESES/Registre_sources_primaires_v0_1.md)

Les fichiers `Source_docx_*` sont des extractions de travail. Une formule, un
tableau ou une image insuffisamment restituee doit etre signale par la convention
de placeholder et verifie dans le DOCX original.

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

## Audits documentaires

Les controles existants sont dans [`audit/`](audit/).

```bash
bash audit/audit_placeholders.sh
bash audit/audit_liens.sh
bash audit/audit_encodage.sh
python audit/audit_structure_corpus.py
```

Avant fusion, verifier :

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
9. Appliquer la hierarchie philosophique active : objet, constitution, acces.
10. Privilegier des commits lisibles, coherents et reversibles.
