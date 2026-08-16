# Accueil des dix cycles physiques

Ce fichier indique **où entrer aujourd’hui** dans chaque cycle. Il ne cherche ni à résumer tout son historique, ni à imposer une structure identique aux dix programmes.

Les noms de fichiers hérités (`v0.x`, `N5`, `S1`, etc.) sont conservés pour la traçabilité. Leur présence ici ne signifie pas que ce mode de versionnage ou de découpage doit être reproduit dans les futurs travaux.

## Comment lire un cycle

1. Commencer par le point d’entrée courant indiqué ci-dessous.
2. Lire les pièces détaillées seulement si la question locale le demande.
3. Revenir aux documents méthodologiques transversaux uniquement lorsqu’un problème de rang, de provenance ou de vocabulaire l’exige.
4. Consulter les issues du cycle pour le travail mouvant, les reprises computationnelles et les décisions qui ne sont pas encore propagées dans les documents vivants.

Les cycles sont indépendants par défaut. Un passage vers un autre cycle ou un autre volet doit répondre à une question identifiable ; il ne propage jamais automatiquement un verdict.

## Deux questions communes

1. **Frontière** — Comment les sciences établissent-elles, utilisent-elles et déplacent-elles la frontière entre ce qui varie et ce qui tient ?
2. **Détermination et enquête** — Par quelles structures, opérations et chemins de détermination un maintien devient-il opératoire ou affirmable dans un régime, et que change cette reconstruction pour l’enquête scientifique ?

Ces questions n’obligent pas les cycles à adopter la même décomposition. Les usages disciplinaires locaux restent premiers.

## Points d’entrée courants

| Cycle | Entrée recommandée | Fonction actuelle du point d’entrée |
|---|---|---|
| **1 — Couplages, échelles et QCD** | [Clôture du premier périmètre v0.5](01_Cycle_couplages_echelles_QCD/Synthese_active_cycle_1_cloture_premier_perimetre_apres_D6_v0_5.md), puis si nécessaire [synthèse scientifique v0.4](01_Cycle_couplages_echelles_QCD/Synthese_active_cycle_1_couplages_echelles_QCD_apres_rapport_proton_electron_v0_4.md) | Le premier document donne le statut courant du périmètre ; le second porte la synthèse scientifique détaillée. Les versions antérieures sont généalogiques, pas des lectures préalables. |
| **2 — Secteur électrofaible structurant** | [Synthèse de récupération](02_Cycle_structurant_electrofaible/Synthese_recuperation_cycle_2_structuration_electrofaible_v0_1.md) | État récupéré et utilisable pour orientation, mais pas synthèse scientifique actuelle artificiellement reconstruite. Une reprise doit ré-instruire les objets nécessaires. |
| **3 — Neutrinos** | [Synthèse active après N5](03_Cycle_neutrinos/Synthese_active_cycle_3_neutrinos_apres_N5_v0_2.md) | Point d’entrée scientifique actif. Les quatre accès restent distincts ; la matrice N5 et les résultats computationnels C2 servent de preuves locales lorsqu’ils sont nécessaires. |
| **4 — Thermodynamique et métrologie** | [Synthèse de récupération](04_Cycle_thermo_metrologique/Synthese_recuperation_thermo_metrologique_SI_v0_1.md) | État de récupération. Il conserve les distinctions acquises sans prétendre intégrer toutes les évolutions métrologiques récentes. |
| **5 — Saveur–Higgs** | [Synthèse Saveur–Higgs après S1–S3 v0.2](05_Cycle_saveur_Higgs/Synthese_active_cycle_5_Saveur_Higgs_apres_S1_S3_v0_2.md) | Meilleure synthèse scientifique disponible. Les pièces S1–S3 restent les preuves locales. La resynchronisation de certains statuts d’en-tête est une correction documentaire séparée. |
| **6 — Théories effectives à basse énergie** | [Évaluation du gain explicatif](06_Cycle_effectif_basse_energie/evaluation-gain-explicatif-basse-energie.md) | Meilleure entrée human-first actuelle : elle expose la question et le gain du cycle. L’architecture et la vérification servent ensuite de support. |
| **7 — Cosmologie** | [Évaluation du gain explicatif](07_Cycle_cosmologique/evaluation-gain-explicatif-cosmologique.md) | Entrée conceptuelle stable du cycle. Les programmes scientifiques et computationnels en cours sont suivis par leurs issues et branches ; leurs diagnostics ne sont pas recopiés ici. |
| **8 — Système international** | [Évaluation du gain explicatif](08_Cycle_metrologique_SI/evaluation-gain-explicatif-metrologique-si.md) | Meilleure entrée actuelle. Elle distingue définition, rôle physique, réalisation et incertitude. Les évolutions métrologiques 2026 identifiées ultérieurement doivent être instruites séparément avant propagation locale. |
| **9 — Ajustement fin** | [Synthèse du premier lot](09_Cycle_fine_tuning/synthese-premier-lot-fine-tuning.md) | Synthèse locale la plus informative ; le cadrage reste disponible pour la question initiale et les conditions de portée. |
| **10 — Quasi-fixité électrofaible** | [Cadrage](10_Cycle_fixite_electrofaible_dynamique/cadrage-cycle-fixite-electrofaible-dynamique.md) | Le cycle demeure fragmenté entre cadrage et résultats de phases successives. Aucun document vivant supplémentaire n’est créé artificiellement tant qu’une reprise ne justifie pas une vraie synthèse. |

## Ce que cet accueil ne fait pas

Il ne reproduit pas :

- les historiques de versions ;
- les listes détaillées de dettes ;
- les diagnostics de runs en cours ;
- les anciennes comparaisons inter-cycles ;
- une hiérarchie de « force » entre cycles ;
- une doctrine philosophique générale.

Les états historiques, cartes comparatives et anciens index restent dans `05_CARTES_ET_SYNTHESES` pour les besoins de généalogie et d’audit. Ils ne sont plus des passages obligatoires avant une reprise locale.

## Contrôles communs minimaux

Une reprise doit seulement conserver les protections qui changent effectivement l’enquête :

```text
identifier la cible et la transformation testée ;
séparer propriété de la cible, accès et constitution ;
séparer résultat, soutien probatoire et verdict ;
borner la portée de la conclusion ;
employer d'abord le vocabulaire du domaine ;
conserver provenance, résultats négatifs et suspensions pertinentes.
```

Ces contrôles ne forment pas un formulaire universel.

## Passages entre cycles

Un cycle peut appeler un autre lorsqu’une question restante change réellement de forme ou de puissance d’instruction. Un transfert scientifique de dette exige une question reformulée, un accès ou discriminant différent, une provenance conservée et une condition de retour explicite. Sinon, la dette reste simplement différée ou suspendue.

Les liens entre cycles peuvent être rendus visibles dans les issues, les labels ou une future vue GitHub Project lorsqu’elle aura été matériellement éprouvée. Aucun reclassement rétroactif massif n’est requis pour cela.

## Versions futures

Les points d’entrée réellement vivants doivent à terme pouvoir évoluer sous un nom stable, leur histoire étant portée par Git. Cette règle est prospective : les fichiers historiques `v0.x` restent en place tant que leur reclassement, leurs dépendances et leur contenu unique n’ont pas été audités.
