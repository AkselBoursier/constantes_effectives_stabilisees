# Constantes physiques — refondation du domaine

Ce dépôt est un corpus de recherche consacré à une question directrice :

> **Qu’est-ce qu’une constante physique ?**

La question sert ici d’instruction d’enquête. Le projet distingue les formes de fixité, les objets qui les portent, les relations qu’elles maintiennent, leurs régimes de validité, leurs voies d’accès et les limites de leur pouvoir explicatif.

## Lire d’abord

1. [Cadre canonique de la refondation](01_CADRE_METHODOLOGIQUE/refondation-du-domaine.md)
2. [Synthèse transversale des cycles](05_CARTES_ET_SYNTHESES/synthese-refondation-des-cycles.md)
3. [Test des cinq cas sentinelles](01_CADRE_METHODOLOGIQUE/test-cas-sentinelles.md)
4. [Cadrage du cycle fine-tuning](02_CYCLES_PHYSIQUES/09_Cycle_fine_tuning/cadrage-cycle-fine-tuning.md)

## Dossiers actifs de la refondation

### Higgs–Yukawa

- [Architecture relationnelle](02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/architecture-relationnelle-higgs-yukawa.md)
- [Vérification physique](02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/verification-physique-higgs-yukawa.md)
- [Évaluation du gain explicatif](02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/evaluation-gain-explicatif-higgs-yukawa.md)

### Basse énergie

- [Architecture relationnelle](02_CYCLES_PHYSIQUES/06_Cycle_effectif_basse_energie/architecture-relationnelle-basse-energie.md)
- [Vérification physique](02_CYCLES_PHYSIQUES/06_Cycle_effectif_basse_energie/verification-physique-basse-energie.md)
- [Évaluation du gain explicatif](02_CYCLES_PHYSIQUES/06_Cycle_effectif_basse_energie/evaluation-gain-explicatif-basse-energie.md)

### Métrologie SI

- [Architecture relationnelle](02_CYCLES_PHYSIQUES/08_Cycle_metrologique_SI/architecture-relationnelle-metrologique-si.md)
- [Vérification métrologique](02_CYCLES_PHYSIQUES/08_Cycle_metrologique_SI/verification-metrologique-si.md)
- [Évaluation du gain explicatif](02_CYCLES_PHYSIQUES/08_Cycle_metrologique_SI/evaluation-gain-explicatif-metrologique-si.md)

### Cosmologie

- [Architecture relationnelle](02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/architecture-relationnelle-cosmologique.md)
- [Vérification physique](02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/verification-physique-cosmologique.md)
- [Évaluation du gain explicatif](02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/evaluation-gain-explicatif-cosmologique.md)

### Fine-tuning

- [Cadrage méthodologique](02_CYCLES_PHYSIQUES/09_Cycle_fine_tuning/cadrage-cycle-fine-tuning.md)
- [Hiérarchie électrofaible](02_CYCLES_PHYSIQUES/09_Cycle_fine_tuning/fiche-cas-hierarchie-electrofaible.md)
- [Univers sans interaction faible](02_CYCLES_PHYSIQUES/09_Cycle_fine_tuning/fiche-cas-univers-sans-interaction-faible.md)
- [Quarks légers et état de Hoyle](02_CYCLES_PHYSIQUES/09_Cycle_fine_tuning/fiche-cas-quarks-legers-etat-hoyle.md)
- [Constante cosmologique](02_CYCLES_PHYSIQUES/09_Cycle_fine_tuning/fiche-cas-constante-cosmologique.md)
- [Synthèse du premier lot](02_CYCLES_PHYSIQUES/09_Cycle_fine_tuning/synthese-premier-lot-fine-tuning.md)

## Résultat provisoire

Les cycles ne révèlent pas une espèce naturelle unique appelée « constante physique ». Ils distinguent au moins :

- une fixité physique ou structurelle ;
- une fixité effective relative à un domaine de validité ;
- une fixité métrologique issue d’une définition ;
- une robustesse inférentielle, qui porte sur l’accès et non sur la constance de l’objet.

Le terme `stabilisée` n’est plus utilisé comme explication générale. Il désigne éventuellement le résultat d’un test explicitant le régime, les transformations pertinentes et la tolérance admise.

Le cycle fine-tuning examine ensuite ce qui reste réellement à expliquer après retrait des grandeurs dérivées, corrélations théoriques, paramètres d’état et reconstructions inférentielles. Il distingue sensibilité structurelle, improbabilité sous une mesure, contrainte environnementale et interprétation explicative.

## Statut de l’ancien corpus

Les anciens fichiers versionnés restent disponibles comme archive de recherche et matériau de provenance. Leurs relations physiques, sources, distinctions de régime et limites explicatives sont réutilisables après contrôle. Leurs taxonomies et conclusions d’architecture ne sont plus considérées comme acquises.

Les nouveaux documents actifs portent des noms canoniques sans numéro de version. Leur évolution est enregistrée par l’historique Git.

## Workflow Git

Les travaux sont menés sur des branches thématiques, avec des commits séparant autant que possible :

- extraction et reprise du corpus ;
- vérification physique ou métrologique ;
- évaluation conceptuelle ;
- migration documentaire.

Branches actives :

```text
agent/refondation-domaine
agent/cycle-fine-tuning
```

Le cycle fine-tuning est développé comme branche empilée sur la refondation tant que celle-ci n’est pas fusionnée dans `main`.
