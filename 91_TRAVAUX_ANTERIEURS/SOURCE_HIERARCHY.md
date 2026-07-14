# SOURCE_HIERARCHY.md

Statut : registre de phase 1.

Ce fichier rend opérationnelle la hiérarchie des sources fixée par `PROJECT_BRIEF.md`.

## Règle de priorité

En cas de contradiction :

1. décisions explicites de l'auteur ;
2. consolidations provisoires ;
3. audits détaillés A-M ;
4. définitions v12 ;
5. manuscrit ;
6. conversation complète ;
7. littérature externe.

La v12 est une source à refondre, non la norme actuelle.

## Sources internes

| Niveau | Source dans la nouvelle arborescence | Source originale | Rôle | Autorité |
|---:|---|---|---|---|
| 1 | décision utilisateur du 2026-06-25 dans le fil actif | validation explicite de phase 1 | valide l'identité des sources, le manuscrit à notes cliquables et le démarrage de phase 1 | maximale pour cette opération |
| 1 | `PROJECT_BRIEF.md` | `C:/Users/admin/OneDrive/Documents/Principe_anthropique_et_coupes/project_brief.md` et `Projet de refondation du cadre des coupes constitutives.docx` | consigne de pilotage et arbitrage documentaire | maximale hors décisions ultérieures |
| 2 | `01_conversation_et_audits/Consolidation_A_C.md` | `Consolidation provisoire des sections A à C.docx` | consolidation opérationnelle après audits A-C | très forte |
| 2 | `01_conversation_et_audits/Consolidation_D_H.md` | `Consolidation provisoire des sections D à H.docx` | consolidation opérationnelle après audits D-H | très forte |
| 3 | `01_conversation_et_audits/Audits_A_M.md` | index tiré de `ChatGPT-refonte_cadre.md` | localisation des audits détaillés | forte, mais médiée par la conversation |
| 3 | `01_conversation_et_audits/Conversation_complete.md` | `ChatGPT-refonte_cadre.md` | archive complète des audits, hésitations, validations et formulations rejetées | forte pour retrouver les raisons, non prioritaire contre consolidation |
| 4 | `00_sources_originales/Definitions_cadre_coupes_v12.md` | `Definitions_cadre_coupes_v12.md` | état v12 à refondre | source historique, non normative |
| 5 | `00_sources_originales/Manuscrit_complet_2026-06-14.md` | `12_livre_grand_public/Manuscrit_complet_notes_cliquables_2026-06-14.md` | manuscrit source le plus récent, protégé | source originale immuable |
| dérivé | `04_manuscrit_v13/Manuscrit_v13_synchronise.md` | synchronisation contrôlée de phase 9 | base éditoriale de travail v13 | validée pour travail éditorial, non publiable |
| dérivé | `04_manuscrit_v13/ORIENTATION_EDITORIALE_POST_PHASE9.md` | suite validée après phase 9 | cadrage éditorial post-phase 9 | règle de travail éditoriale |
| dérivé | `04_manuscrit_v13/Manuscrit_v13_base_editoriale.md` | copie de `Manuscrit_v13_synchronise.md` | fichier de travail éditorial | modifiable sous contrôle |
| dérivé | `04_manuscrit_v13/SUIVI_EDITORIAL_MANUSCRIT.md` | suite post-phase 9 | suivi chapitre par chapitre | règle de travail éditoriale |
| dérivé | `04_manuscrit_v13/NOTES_REFERENCES_A_VERIFIER.md` | suite post-phase 9 | suivi des notes et références | règle documentaire |
| dérivé | `04_manuscrit_v13/CONTROLE_REGRESSION_MANUSCRIT.md` | suite post-phase 9 | garde-fou anti-régression | règle de contrôle |
| dérivé | `04_manuscrit_v13/AUDIT_VOILURE_LIVRE_POST_CADRE.md` | suite post-phase 9 | estimation de voilure et recommandations éditoriales | règle d'orientation |
| auxiliaire | non copié en phase 1 | `Matrice de recherche — La constante de structure fine.docx` | dossier régional de test sur alpha | autorité locale sur le cas alpha, non transversale |

## Conséquences pratiques

- Les fichiers de `00_sources_originales/` sont immuables.
- Les consolidations A-C et D-H gouvernent le travail courant.
- Les audits détaillés servent à arbitrer les ambiguïtés, les retours implicites de concepts abandonnés et les questions de justification.
- Le manuscrit source ne doit jamais être modifié directement ; toute synchronisation passe par `04_manuscrit_v13/`.
- La matrice alpha ne prouve pas la transversalité du cadre ; elle sert à tester le gain non redondant sur un terrain déterminé.

## Contrôle de provenance

Toute future révision conceptuelle doit indiquer :

- fichier source mobilisé ;
- décision du registre concernée ;
- concept affecté ;
- statut modal de la proposition ;
- risque de régression.
