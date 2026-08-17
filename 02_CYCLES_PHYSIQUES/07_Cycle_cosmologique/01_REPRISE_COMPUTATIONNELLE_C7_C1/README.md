# C7-C1 / X(z) — reprise computationnelle

Ce dossier porte la reprise computationnelle du lot `C7-C1` du cycle cosmologique : comparaison commune `LambdaCDM` / CPL / `X(z)` sous la même vraisemblance DESI DR2 BAO et le même ancrage CMB comprimé.

Il contient à la fois des pièces historiques de la construction G0–G2 et les supports computationnels encore utiles. Son README doit être lu depuis l’autorité opérationnelle courante, non comme une permission de reprendre automatiquement les portes historiques.

## Autorité opérationnelle actuelle

- ancrage actif : [issue #119 — C7-C1 / X(z), audit de persistance post-EXP-1B RUN1](https://github.com/AkselBoursier/constantes_effectives_stabilisees/issues/119) ;
- provenance principale de EXP-1 et RUN1 : `#102` ;
- provenance plus ancienne de la construction C7-C1 : `#63`, `#60`, `#61`, `#62` ;
- archivage historique : `#64`.

`#63` n’est plus l’issue directrice de la reprise actuelle. Ses portes G0–G2 et les rapports du dossier restent des éléments de provenance et de qualification locale lorsqu’ils sont encore pertinents.

## Question scientifique de fond

> Les mauvaises propriétés d’exploration de `X(z)` proviennent-elles principalement de la configuration du sampler, de la paramétrisation ou de la géométrie effective du posterior ?

Cette question reste ouverte.

## État courant borné

```text
EXP1A_GEOMETRIC_AUDIT = CLOS_TECHNIQUEMENT
P = TECHNIQUEMENT_QUALIFIE_POUR_CONTRASTE
B1 = NON_AUTORISEE

EXP1B_CAMPAIGN = CONSOMMEE
REAL_MCMC_ATTEMPT = 1
RUNS_PLANIFIES = 12
RUNS_EXECUTES = 1

PERSISTENCE_DELTA_6_CAUSE = REPRODUITE_SOURCE_LEVEL
CLASSIFICATION_#119 = A / SEMANTIQUE_COBAYA_ATTENDUE_REPRODUITE
PERSISTENCE_CONTRACT_WEIGHT_SUM_EQ_BUDGET = TROP_FORT
RUN1_DISK_LOSS = NON_ETABLI
RUN1_ARTIFACT_SET_BYTE_AUDIT = ENCORE_OUVERT
RUN1_SCIENTIFIC_QUALIFICATION = NON
SCI1 = NON_QUALIFIABLE
NEW_SAMPLING = NON_AUTORISE
```

Le `delta=6` de RUN1 a été expliqué par la sémantique attendue de Cobaya au démarrage : six rejets avant la première acceptation rendent faux le contrat général `sum(weights) == raw_proposals`. Cette qualification corrige la cause du rouge de persistance ; elle ne transforme pas RUN1 en résultat scientifique et ne prouve pas que l’ensemble scellé des artefacts a été audité byte-à-byte.

## Interdits actifs

```text
NEW_SAMPLING = NON_AUTORISE
RUNS_RESTANTS_11 = NON_AUTORISES
B1_SCIENTIFIQUE = NON_AUTORISEE
SCI1_INTERPRETATION = NON_AUTORISEE
PHYSICAL_XZ_INFERENCE = NONE
```

Aucune ancienne autorisation de budget ni aucune porte historique de `#63` ne vaut permission implicite de poursuivre aujourd’hui.

## Contenu du dossier

```text
configs/     — transcriptions LambdaCDM et CPL, références et configurations historiques ;
manifests/   — provenance, versions, tailles et SHA-256 des pièces concernées ;
scripts/     — vraisemblances transcrites, acquisition, tests et outils computationnels ;
reports/     — rapports G1/G2 et qualifications locales, jamais une autorité automatique sur l’état courant ;
requirements-c7c1.txt et requirements-c7c1-secondaire.txt — environnements historiques/isolés du dossier.
```

Les données, chaînes, caches et environnements restent hors Git. `data_external` reste une source locale en lecture seule lorsqu’elle est utilisée.

## Historique G0–G2

La construction initiale a qualifié une vraisemblance commune, reproduit les références LambdaCDM/CPL et ouvert progressivement l’instrument `X(z)`. Les détails exacts des portes G0, G1 et G2 restent dans `#63` et les rapports locaux.

Ils sont à lire comme généalogie technique et scientifique du dossier. Pour toute action nouvelle, repartir de `#119`, puis remonter à ces pièces uniquement lorsque la question l’exige.
