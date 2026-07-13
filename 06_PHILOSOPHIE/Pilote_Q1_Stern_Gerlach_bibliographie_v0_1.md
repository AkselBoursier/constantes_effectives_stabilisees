# Pilote Q1 — Bibliographie raisonnée v0.1

## 0. Statut

```text
statut : bibliographie de première passe ;
fonction : distinguer source historique, reconstruction physique, analyse de mesure,
           séquences, cohérence, histoire/philosophie et recherche pédagogique ;
limite : antériorité non exhaustive avant toute publication.
```

## 1. Expérience historique

### Gerlach, W., & Stern, O. (1922)

**Der experimentelle Nachweis der Richtungsquantelung im Magnetfeld.** *Zeitschrift für Physik*, 9, 349–352.

Rôle : source primaire du dispositif, du dépôt sur plaque, des deux bandes et de la conclusion de quantification spatiale.

Contrôle utilisé dans le pilote : l'expérience accessible était cumulative ; les auteurs ne disposaient pas du concept moderne de spin électronique.

### Bauer, M. (2023)

**The Stern-Gerlach Experiment. Translation of “Der experimentelle Nachweis der Richtungsquantelung im Magnetfeld”.** arXiv:2301.11343.

Rôle : traduction anglaise proche du texte original, utilisée pour contrôler les dimensions du montage, la durée d'exposition et la description des résultats.

### Schmidt-Böcking, H., Schmidt, L., Lüdde, H. J., Trageser, W., & Sauer, T. (2016)

**The Stern-Gerlach Experiment Revisited.** *European Physical Journal H*, 41, 327–364. DOI: `10.1140/epjh/e2016-70053-2` ; arXiv:1609.09311.

Rôle : reconstruction historique et physique de la pluralité des résultats associés rétrospectivement à l'expérience ; contrôle de la formule « presque découverte du spin ».

## 2. Modélisation quantique du dispositif

### Potel, G., Barranco, F., Cruz-Barrios, S., & Gómez-Camacho, J. (2005)

**Quantum mechanical description of Stern-Gerlach experiments.** *Physical Review A*, 71, 052106. DOI: `10.1103/PhysRevA.71.052106` ; arXiv:quant-ph/0409206.

Rôle : traitement quantique du mouvement dans un champ inhomogène, comparaison aux approximations semi-classiques, prédiction de focalisation et de retournements de spin, évaluation de la fiabilité de la mesure de projection.

Gain pour Q1 : `mesure de S_z` est un statut de régime et d'approximation, non une identité indépendante du montage.

### Fonseca-Romero, K. M. (2024, version révisée)

**A quantum treatment of the Stern-Gerlach experiment.** arXiv:2402.14930.

Rôle : dérivation accessible de l'opérateur d'évolution, distinction espace physique / espace de spin et mise en évidence de la corrélation ou intrication position–spin.

Gain pour Q1 : la trajectoire newtonienne est une approximation pédagogique possible, mais un traitement complet doit faire évoluer conjointement les degrés spatial et de spin.

### Reddy, A., Samuel, J., Shivam, K., & Sinha, S. (2016)

**Coarse Quantum Measurement: An analysis of the Stern Gerlach experiment.** *Physics Letters A*, 380, 1135–1140. DOI: `10.1016/j.physleta.2016.01.032` ; arXiv:1509.09024.

Rôle : traitement unitaire du spin et de la position avec résolution finie des sondes de position.

Gain pour Q1 : la partition des positions et la résolution de détection participent à l'information effectivement obtenue sur le spin.

## 3. Séquences, changements d'axe et reconstruction d'état

### Tekin, B. (2015)

**Stern-Gerlach Experiment with Higher Spins.** arXiv:1506.04632.

Rôle : probabilités de séquences idéalisées selon l'angle entre analyseurs et clarification de confusions fréquentes autour du spin 1/2.

Gain pour Q1 : permet de séparer changement d'axe, probabilités conditionnelles et image d'un vecteur classique complet.

### Amiet, J.-P., & Weigert, S. (1998)

**Reconstructing a pure state of a spin s through three Stern-Gerlach measurements.** arXiv:quant-ph/9809018.

Rôle : reconstruction d'un état pur à partir de probabilités obtenues selon plusieurs directions.

Gain pour Q1 : une seule distribution terminale ne suffit pas à déterminer l'état ou la préparation.

## 4. Cohérence, séparation et recombinaison

### Margalit, Y., et al. (2018)

**Realization of a complete Stern-Gerlach interferometer.** arXiv:1801.02708.

### Margalit, Y., et al. (2020)

**Realization of a complete Stern-Gerlach interferometer: Towards a test of quantum gravity.** arXiv:2011.10928.

Rôle : séparation et recombinaison cohérentes à l'aide de gradients magnétiques contrôlés sur puce atomique.

Gain pour Q1 : empêche d'identifier automatiquement séparation spatiale et mélange classique ; rend l'accès à la phase expérimentalement pertinent.

### Amit, O., et al. (2019)

**T^3-Stern-Gerlach Matter-Wave Interferometer.** arXiv:1908.03879.

Rôle : architecture en boucle complète utilisant plusieurs impulsions de gradient pour séparer et recombiner les paquets.

### Paraniak, M. M., & Englert, B.-G. (2021)

**Quantum Dynamical Simulation of a Transversal Stern-Gerlach Interferometer.** arXiv:2106.00205.

Rôle : étude numérique des difficultés de recombinaison dans le montage transversal idéal.

Contrôle : ne pas confondre ce schéma avec les réalisations sur puce atomique, qui utilisent une architecture et un contrôle différents.

## 5. Concepts classiques et fonction de l'expérience

### Camilleri, K., & Schlosshauer, M. (2015)

**Niels Bohr as Philosopher of Experiment: Does Decoherence Theory Challenge Bohr's Doctrine of Classical Concepts?** *Studies in History and Philosophy of Modern Physics*, 49, 73–83. DOI: `10.1016/j.shpsb.2015.01.005` ; arXiv:1502.06547.

Rôle : analyse historique et philosophique de la doctrine des concepts classiques comme thèse principalement fonctionnelle et épistémologique.

Contrôle pour Q1 : distinguer nécessité fonctionnelle d'une description et émergence dynamique du classique ; ne pas conclure de la première à une ontologie fondamentale.

### Schlosshauer, M., & Camilleri, K. (2008)

**The quantum-to-classical transition: Bohr's doctrine of classical concepts, emergent classicality, and decoherence.** arXiv:0804.1609.

Rôle : distinction entre plusieurs formulations de la doctrine des concepts classiques et analyse de son rapport à la décohérence.

Gain pour Q1 : empêcher que `classique` soit traité comme une catégorie univoque.

## 6. Recherche pédagogique

### Zhu, G., & Singh, C. (2011/2016)

**Improving Students' Understanding of Quantum Mechanics via the Stern-Gerlach Experiment.** *American Journal of Physics* ; version accessible arXiv:1602.06367.

Rôle : enquête sur les difficultés d'étudiants et usage de Stern–Gerlach pour enseigner préparation d'état, évolution, mesure, bases, espace physique / espace de Hilbert et différence entre mélange et superposition.

Gain pour Q1 : les catégories pédagogiques ne sont pas neutres ; elles peuvent faciliter une opération tout en créant une confusion à une étape ultérieure.

## 7. Sources différées

Une seconde passe devra examiner :

```text
théorie des instruments quantiques et règle de Lüders ;
mesures sélectives et non sélectives ;
modèles complets de l'appareil et de la détection ;
POVM appliquées au cas ;
décohérence de chemin et états réduits ;
philosophie de la préparation comme opération ;
littérature sur contextualité, propriété et attribution ;
comparaison avec interférence et information de chemin.
```

## 8. Règle d'usage

Aucune source ne porte seule la thèse du pilote. Les sources historiques fixent ce qui a été fait et observé ; les modèles physiques reconstruisent des chaînes différentes ; les analyses philosophiques distinguent leurs fonctions ; les travaux pédagogiques documentent les confusions possibles.

> La bibliographie empêche trois raccourcis : identifier l'expérience historique au schéma de manuel, identifier séparation et détection, ou identifier perte locale d'accès à une phase et disparition ontologique de la cohérence.
