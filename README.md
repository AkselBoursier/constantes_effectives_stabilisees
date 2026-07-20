# constantes_effectives_stabilisees

Corpus de recherche sur ce que la physique appelle des constantes, sur les
différences que ce terme commun recouvre et sur les régimes, architectures, accès
et processus par lesquels certaines fixités deviennent opératoires ou affirmables.

> **Statut au 20 juillet 2026 :** `main` intègre la consolidation du corpus et la
> clôture computationnelle de `C2`. Les phases `P0` et `P1` sont closes. L’audit de
> portée des régimes de constance est validé sur une branche thématique bornée ; son
> lot de maintenance documentaire est en cours. Le cycle 1 — couplages, échelles et
> chromodynamique quantique — reste la prochaine dette scientifique prioritaire.

## Point d’entrée humain

Lire d’abord :

1. le [verdict final de l’audit de portée](05_CARTES_ET_SYNTHESES/Verdict_final_audit_portee_regimes_constance_v0_1.md), pour l’état décisionnel courant et la séquence autorisée ;
2. la [vue d’ensemble globale v0.4](05_CARTES_ET_SYNTHESES/Vue_ensemble_globale_v0_4.md), conservée comme architecture générale datée du 18 juillet 2026 ;
3. l’[accueil central des dix cycles physiques](02_CYCLES_PHYSIQUES/README.md), pour accéder aux résultats et dettes locales ;
4. l’[index raisonné v1.4](05_CARTES_ET_SYNTHESES/Index_raisonne_du_corpus_v1_4.md), pour la navigation actuelle et le rang des documents ;
5. la [feuille de route post-consolidation v0.1](05_CARTES_ET_SYNTHESES/Feuille_route_post_consolidation_v0_1.md), conservée comme état programmatique du 18 juillet et à lire avec le verdict final.

La [vue récente des chantiers du 16 au 18 juillet 2026](05_CARTES_ET_SYNTHESES/Vue_recente_chantiers_16_18_juillet_2026_v0_1.md), la [vue d’ensemble v0.3](05_CARTES_ET_SYNTHESES/Vue_ensemble_une_page_v0_3.md) et la vue globale v0.4 restent des états datés. Elles ne sont pas réécrites rétroactivement pour refléter la clôture ultérieure de `C2` ou le verdict de l’audit.

## Objet général

Le projet ne cherche pas principalement à dresser un catalogue des constantes ni à
produire une taxonomie universelle. Il examine ce que le terme commun « constante »
comprime lorsqu’il est appliqué à des objets, relations, observables, coefficients,
bornes, paramètres d’état et valeurs définissantes hétérogènes.

Deux questions organisent le travail :

1. Comment les sciences établissent-elles, utilisent-elles et déplacent-elles la
   frontière entre ce qui varie et ce qui tient ?
2. Que change pour l’enquête scientifique le fait de reconstruire certaines
   constances à travers leurs régimes, leurs modes de constitution, leurs accès et
   leurs transformations possibles ?

La qualification d’une grandeur comme constante reste une question locale utile.
Elle ne suffit plus, à elle seule, à définir le programme.

## Articulation heuristique

```text
objet : quel porteur, quelle relation ou quel secteur est étudié ?
constitution : qu’est-ce qui rend le régime ou la relation opératoire ?
accès : comment l’objet, la trace ou la preuve devient-il disponible ?
différenciation : quelles confusions doivent être défaites ?
qualification : quel statut et quelles limites peut-on soutenir ?
```

Le point d’entrée et l’ordre dépendent du terrain. Aucune dimension ne commande
uniformément les autres. La règle est de déclarer le niveau de chaque énoncé et
d’empêcher les migrations silencieuses entre objet, constitution, accès et
interprétation.

## Distinctions canoniques

Le corpus distingue au minimum :

```text
constance de l’objet ;
stabilisation ou robustesse de l’accès et de l’estimation ;
mode de constitution ou d’organisation ;
exactitude par définition ;
validité dans un régime ;
borne ou domaine admissible ;
paramètre d’état reconstruit ;
quasi-stationnarité dans une dynamique déterminée.
```

Une borne ne devient pas une propriété positive de l’objet. Une valeur exacte par
définition ne devient pas un résultat empirique infiniment précis. Une trajectoire
calculée ne devient pas une histoire réelle. Une pluralité d’accès ne devient une
validation croisée qu’après explicitation des hypothèses de conversion.

## Les dix cycles physiques

Les cycles sont organisés par cinq contrastes :

```text
1–6 : échelle, régime et validité ;
2–5 : fonction, architecture et explication ;
3–7 : accès, reconstruction et mesure ;
4–8 : mesure, définition et réalisation ;
9–10 : contrefactuel, dynamique et contingence.
```

Le cycle 3 — neutrinos — possède une [synthèse active après N5](02_CYCLES_PHYSIQUES/03_Cycle_neutrinos/Synthese_active_cycle_3_neutrinos_apres_N5_v0_2.md). Sa reprise computationnelle `N1–N3` est documentée dans :

- [C1 — planchers, frontière et priors](02_CYCLES_PHYSIQUES/03_Cycle_neutrinos/01_REPRISE_COMPUTATIONNELLE_N1_N3/C1_Resultats_planchers_frontiere_priors_v0_1.md) ;
- [C2 — cadrage des produits officiels DESI](02_CYCLES_PHYSIQUES/03_Cycle_neutrinos/01_REPRISE_COMPUTATIONNELLE_N1_N3/C2_Produits_officiels_quantiles_maxima_profils_v0_1.md) ;
- [C2 — résultats de l’ingestion locale DESI DR2 v0.2](02_CYCLES_PHYSIQUES/03_Cycle_neutrinos/01_REPRISE_COMPUTATIONNELLE_N1_N3/C2_Resultats_ingestion_locale_DESI_DR2_v0_2.md).

`C2` est close au niveau de l’ingestion contrôlée des produits distribués : les chaînes `base_mnu`, `base_mnu059` et `base_mnu_w_wa` ont été ingérées et comparées aux limites `margestats`. L’absence de `base_mnu_binary_3` dans la distribution vérifiée et l’absence de profils exacts restent des limites positives documentées. Le test de sensibilité `T2` peut être poursuivi en parallèle sans bloquer la suite du programme.

Le cycle 1 — couplages, échelles et chromodynamique quantique — est la dette scientifique prioritaire suivante. Le test local `T1` est intégré à cette reprise ; il ne constitue pas une condition préalable séparée qui retarderait son ouverture.

## Quatre espaces de travail

### Cadre méthodologique

`01_CADRE_METHODOLOGIQUE/` contient les décisions, protocoles, hiérarchies de
sources et règles de travail. Il sert de garde-fou ; il ne doit pas pré-écrire les
résultats des cas.

### Laboratoire scientifique

`02_CYCLES_PHYSIQUES/` contient les fiches, calculs, synthèses actives et dettes des
dix cycles.

### Laboratoire philosophique en réserve

`06_PHILOSOPHIE/` conserve les dossiers Stern–Gerlach, séquences d’axes,
interférence, coupes et accès. Ces matériaux sont disponibles sur question précise,
mais ne commandent pas la prochaine étape scientifique.

### Laboratoire éditorial expérimental

Le répertoire `93_LABORATOIRE_EDITORIAL_EXPERIMENTAL/` accueille plans, sources,
premiers jets, relectures et variantes. Son rôle est de tester le passage du corpus
à une écriture continue, sans transformer une dette ouverte en résultat acquis.

## Données externes et calculs

Les données scientifiques volumineuses restent hors de Git :

```text
data_external/
```

Ce chemin est ignoré par `.gitignore`. Les archives, chaînes MCMC, caches et
environnements locaux ne doivent pas être versionnés. Git conserve seulement :

```text
manifestes ;
sommes de contrôle ;
scripts ;
configurations utiles ;
sorties dérivées de taille raisonnable ;
rapports et limites de reproduction.
```

Une sortie numérique n’est déclarée reproduite que si ses entrées, ses poids, sa
provenance, son code et ses limites ont été effectivement contrôlés.

## Sources primaires et couches historiques

Les documents Microsoft Word (`DOCX`) et `Ecriture.txt` sont des sources primaires
conservées sans modification. Les fichiers `Source_docx_*` sont des extractions de
travail. Toute formule, image ou table insuffisamment restituée doit être vérifiée
dans l’original.

`91_TRAVAUX_ANTERIEURS/` conserve les matériaux antérieurs et leur généalogie.
`92_ARCHIVES_CONVERSATIONNELLES/` conserve les exports et le registre court des
arbitrages. Leur présence ne leur confère pas un rang canonique.

## État du pan philosophique antérieur

Le chantier Q a produit trois tests : Stern–Gerlach, séquences d’axes et
interférence avec marquage des voies. La coordination de couches est établie et une
contribution différenciée est plausible, mais le positionnement bibliographique
reste à instruire lorsqu’une question scientifique ou éditoriale le requiert.

Entrées :

- [programme Q1](06_PHILOSOPHIE/PROGRAMME_Q1_CONTRIBUTION_README.md) ;
- [dossier Stern–Gerlach](06_PHILOSOPHIE/PILOTE_Q1_STERN_GERLACH_README.md) ;
- [interférence — cadrage](06_PHILOSOPHIE/Pilote_Q1_interference_cadrage_v0_1.md) ;
- [interférence — fonctions](06_PHILOSOPHIE/Pilote_Q1_interference_fonctions_v0_1.md) ;
- [évaluation de contribution](06_PHILOSOPHIE/Pilote_Q1_interference_evaluation_contribution_v0_1.md).

## Workflow GitHub

```text
main : état validé et lisible du corpus ;
branches : chantiers thématiques bornés ;
PR : un objet, un résultat et ses limites ;
data_external : données locales hors Git ;
récupération : opération exceptionnelle soumise à revue.
```

`main` intègre désormais la consolidation cumulative et la clôture computationnelle de `C2`. La branche `agent/audit-portee-regimes-constance` est un chantier thématique borné, sans divergence avec `main`. Son intégration reste soumise à la revue du lot complet et à une décision explicite de l’auteur.

## Audits documentaires

```bash
python audit/audit_structure_corpus.py
bash audit/audit_liens.sh
bash audit/audit_encodage.sh
bash audit/audit_placeholders.sh
```

Les trois premiers contrôles sont bloquants dans GitHub Actions. L’inventaire des
placeholders est informatif : les lacunes connues des extractions ne sont pas
confondues avec une régression.

## Règles de contribution

1. Ne pas modifier les sources historiques DOCX.
2. Distinguer intention fondatrice, centre temporaire, acquis durable et orientation validée.
3. Ne pas transformer une correction locale en centre général.
4. Ne pas confondre ordre de recherche, ordre d’exposition et hiérarchie ontologique.
5. Revenir aux preuves locales pour toute affirmation sectorielle.
6. Conserver résultats, hypothèses, accès, provenance et conditions d’échec.
7. Reprendre les documents philosophiques par versions nouvelles et réversibles.
8. Choisir le point d’entrée selon l’objet sans imposer un ordre universel.
9. Ne pas transformer une analogie pédagogique en argument physique.
10. Ne pas transformer une quasi-stationnarité locale en théorie générale.
11. Ne jamais versionner les données scientifiques externes volumineuses.
12. Enregistrer les décisions seulement lorsqu’elles changent rang, portée, méthode ou ordre du programme.
