# Cycle 7 — Cosmologie

Ce README est la porte d'entrée locale vivante du cycle cosmologique. Il présente
les deux lignes de recherche, leur question, leur état courant borné et leur
route d'autorité. Les rapports scientifiques, les pièces locales et les issues
conservent chacun leur fonction propre ; cette porte les rend accessibles sans
fusionner leurs statuts.

## Deux lignes actives, deux états scientifiques

Le cycle 7 contient actuellement deux lignes indépendantes :

```text
C7-C1 / X(z) / SCI-1
≠
C7-GAL / C0
```

Elles peuvent partager une infrastructure ou des contraintes logistiques. Chaque
ligne conserve son état scientifique, son autorisation, ses blocages et ses
verdicts ; la lecture d'une ligne reste donc indépendante de l'autre.

Ne jamais désigner `C7-GAL` comme « C7-C1 GAL » : `C7-C1` désigne la ligne `X(z)`.

## C7-C1 / X(z) / SCI-1

**Question de fond.** Les mauvaises propriétés d’exploration de `X(z)` proviennent-elles principalement de la configuration du sampler, de la paramétrisation ou de la géométrie effective du posterior ?

- dossier computationnel local : [01_REPRISE_COMPUTATIONNELLE_C7_C1](01_REPRISE_COMPUTATIONNELLE_C7_C1/README.md) ;
- ancrage opérationnel actif : [issue #119 — audit de persistance post-EXP-1B RUN1](https://github.com/AkselBoursier/constantes_effectives_stabilisees/issues/119) ;
- provenance principale antérieure : `#102`, puis `#63` pour les portes historiques G0–G2 et la construction initiale du dossier.

État courant borné :

```text
PERSISTENCE_DELTA_6_CAUSE = REPRODUITE_SOURCE_LEVEL
CLASSIFICATION_#119 = A / SEMANTIQUE_COBAYA_ATTENDUE_REPRODUITE
PERSISTENCE_CONTRACT_WEIGHT_SUM_EQ_BUDGET = TROP_FORT
RUN1_DISK_LOSS = NON_ETABLI
RUN1_ARTIFACT_SET_BYTE_AUDIT = ENCORE_OUVERT
RUN1_SCIENTIFIC_QUALIFICATION = NON
SCI1 = NON_QUALIFIABLE
B1 = NON_AUTORISEE
NEW_SAMPLING = NON_AUTORISE
```

La cause du rouge de persistance est donc qualifiée au niveau source/contrat ; cela ne qualifie pas scientifiquement RUN1 et n’autorise aucun nouveau sampling.

## C7-GAL / C0

**Question de fond.** Étudier la discordance masse/dynamique galactique sans présupposer qu’une seule classe d’explication doive être retenue, en commençant par les situations dynamiques hors équilibre et par la distinction entre reconstruction observable et référence gravitationnelle.

- ancrage opérationnel actif : [issue #120 — fermeture C0-A et préparation G2](https://github.com/AkselBoursier/constantes_effectives_stabilisees/issues/120) ;
- provenance principale antérieure : `#83`, `#86`, `#88`, `#89`, `#98`, `#112`.

État courant borné :

```text
PROGRAMME_C7_GAL = OUVERT
LOT_C = ROUTE_ACTIVE
C0_A_MATERIAL_CLOSURE = OUVERTE
C0_A = BLOQUEE_PAR_ACCES_MATERIEL_AUX_HDF5
PT2_CONTRACT = DEFAUT_REPRODUIT_ET_CORRECTION_SPECIFIEE
G1 = INDISPONIBLE
G2 = NON_OUVERTE
```

L’absence d’accès matériel actuel aux deux snapshots HDF5 empêche de calculer honnêtement leurs SHA-256, de vérifier une ingestion canonique et de fermer C0-A. Le défaut `PartType2` du script historique a été reproduit ; sa correction doit être portée dans un outil actif futur, sans réécrire la provenance `#89`.

Aucun potentiel reconstruit, gradient, courbe de rotation, verdict matière sombre / gravité modifiée ou exécution G2 n’est autorisé par cet état.

## Provenance et reprise du cycle

Les fichiers `Cycle_cosmologique_v0_1_*` à `v0_7_*`, les architectures,
vérifications, évaluations et plans antérieurs restent des pièces de cadrage,
de résultat ou de provenance. Leur fonction historique reste accessible tandis
que ce README porte l'orientation courante.

Pour reprendre une ligne active, suivre ce circuit :

```text
README du cycle 7
→ issue active de la ligne
→ pièce locale nécessaire
→ provenance seulement si une décision ou une contradiction l’exige
```

Le noyau racine porte les règles d'intervention applicables au cycle. Les états
mouvants, autorisations et blocages sont gouvernés par les issues `#119` et
`#120`, chacune dans sa ligne ; ce README en donne la route sans reconstruire
leur contenu à partir de l'historique.
