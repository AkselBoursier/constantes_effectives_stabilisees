# α1 — Matrice initiale des cibles, transformations et accès pour `alpha` v0.1

## 0. Statut

```text
statut : matrice exploratoire issue du verrouillage α1 ;
date : 26 juillet 2026 ;
appui : A1_Registre_sources_versions_alpha_v0_1.md ;
fonction : empêcher l’identification de quatre énoncés hétérogènes désignés par
           « alpha est constante » ;
autorité : descriptive et préparatoire ;
ne vaut pas : verdict de constance, combinaison statistique, classement de robustesse
               définitif ou propagation dans la synthèse du cycle 1.
```

## 1. Matrice principale

| Cible | Objet effectivement reconstruit | Transformation déclarée | Accès du premier lot | Résultat quantitatif attendu | Mode de soutien probatoire à instruire | Limite constitutive |
|---|---|---|---|---|---|---|
| **A. valeur de référence de basse énergie** | valeur recommandée ou détermination de `alpha` dans une convention de basse énergie, issue d’une chaîne de mesure et de relations auxiliaires | changement de méthode, de données d’entrée, de relations théoriques, de corrélations ou d’ajustement | CODATA 2022 ; recul `133Cs` ; recul `87Rb` ; moment magnétique de l’électron + QED | valeurs et incertitudes publiées, résidus ou tensions entre chaînes, poids dans l’ajustement | ajustement cohérent ; mesure de recul et propagation métrologique ; inférence conditionnelle par théorie | stabilité entre résultats ou versions ≠ invariance physique ; les routes ne sont pas automatiquement indépendantes |
| **B. couplage courant `alpha(Q²)`** | fonction de couplage renormalisée dans un schéma et un domaine de transfert d’impulsion déclarés | changement d’échelle ou de `Q²` | diffusion Bhabha L3 à LEP | paramètre de running `C`, domaine en `Q²`, incertitudes statistique et systématique | détection positive de la dépendance d’échelle attendue en QED | une dépendance à l’échelle n’est pas une variation temporelle ; `alpha(0)` n’est pas numériquement maintenue sous la transformation testée |
| **C. variation temporelle** | dérive ou modulation de `Delta alpha/alpha` dans une famille de modèles déclarée | temps, fréquence de modulation ou variation du potentiel gravitationnel | rapports de transitions et fréquences d’horloges `171Yb+` rapportées à des références atomiques | pente temporelle, amplitude annuelle ou coefficient de couplage, avec covariance des paramètres | contrainte sensible sur une variation ; non-détection discriminante si la famille et la sensibilité sont établies | dépendance aux coefficients de sensibilité, aux autres paramètres ajustés et au spectre temporel accessible ; aucune invariance universelle |
| **D. variation spatiale ou cosmologique** | `Delta alpha/alpha` selon direction, ligne de visée, redshift ou modèle spatial | position, direction, époque cosmologique ou environnement | Keck/HIRES et VLT/UVES historiques ; supercalibrations ; ESPRESSO vers HE 0515−4414 | amplitude dipolaire ou valeur locale, erreurs statistique et systématique | prétention positive historique ; repondération après systématiques ; non-détection locale calibrée | domaines, échantillons, calibrations et modèles d’absorption non identiques ; une ligne de visée ne porte pas le verdict global |

## 2. Non-identités obligatoires

```text
valeur recommandée CODATA
≠
détermination expérimentale individuelle ;

alpha(0)
≠
alpha(Q²) ;

variation avec Q²
≠
variation avec le temps ;

dérive linéaire
≠
modulation périodique ou transitoire ;

variation selon le redshift
≠
variation spatiale dipolaire ;

compatibilité locale avec zéro
≠
invariance cosmologique globale ;

désaccord entre déterminations
≠
variation physique de la cible.
```

## 3. Cibles analytiques et porteur du test

Le symbole `alpha` ne suffit pas à identifier le porteur du test. Chaque sous-dossier doit formuler son attribution.

### A — attribution à une sortie de chaîne

```text
cible analytique : valeur recommandée ou détermination publiée ;
transformation : changement de chaîne ou d’ajustement ;
question autorisée : les chaînes sont-elles comparables, indépendantes et cohérentes
                     dans les relations déclarées ?
question interdite : alpha varie-t-elle physiquement parce que deux déterminations diffèrent ?
```

### B — attribution à une relation d’évolution

```text
cible analytique : fonction alpha(Q²) ou paramètre de running ;
transformation : Q² ;
question autorisée : la variation prédite avec l’échelle est-elle détectée dans le domaine ?
question interdite : alpha est-elle constante sous une transformation dont la théorie prédit le running ?
```

### C — attribution à une famille temporelle

```text
cible analytique : pente, modulation ou coefficient de couplage de Delta alpha/alpha ;
transformation : temps ou potentiel ;
question autorisée : le dispositif aurait-il détecté la famille de variations déclarée ?
question interdite : la compatibilité avec zéro prouve-t-elle une invariance exacte ?
```

### D — attribution à un domaine observationnel

```text
cible analytique : valeur locale, tendance en redshift ou amplitude spatiale paramétrée ;
transformation : direction, position ou époque ;
question autorisée : quel modèle est soutenu après contrôle des calibrations et systématiques ?
question interdite : une mesure locale ou un conflit historique fixe-t-il un statut universel ?
```

## 4. Modes de soutien probatoire pressentis

| Sous-dossier | Mode principal | Modes secondaires | Contrôle P27 |
|---|---|---|---|
| A | mesure et ajustement de chaînes hétérogènes | intercomparaison de méthodes ; inférence théorique conditionnelle | ne pas convertir un désaccord en variation ; auditer corrélations et dépendances communes |
| B | mesure positive d’une dépendance à l’échelle | comparaison au modèle QED ; contrôle d’hypothèse `C=0` | la transformation est discriminante et le maintien numérique n’est pas le résultat attendu |
| C | contrainte sensible sur une famille temporelle | comparaison de rapports ; ajustement conjoint ; modulation annuelle | déclarer famille, sensibilité, domaine fréquentiel, tolérance et paramètres simultanés |
| D | conflit entre accès puis repondération après systématiques | mesure locale calibrée ; couverture partielle du domaine | distinguer prétention positive, affaiblissement probatoire et suspension hors des domaines testés |

Aucun de ces modes n’est un statut supplémentaire de constance.

## 5. Suffisance documentaire du premier lot

### A — suffisance conditionnelle

Le premier lot identifie l’ajustement directeur et trois chaînes majeures. Il est suffisant pour ouvrir **α2**, à condition d’extraire du CODATA les données d’entrée, corrélations et décisions d’ajustement portant effectivement sur `alpha`.

```text
source disponible : oui ;
chaînes distinguables : oui ;
corrélations extraites : non ;
reproduction possible : non décidée ;
verdict : non ouvert.
```

### B — suffisance locale

La mesure L3 fournit un cas positif borné et une hypothèse nulle explicitement testée. Elle est suffisante pour ouvrir **α3** comme fiche locale du running, sans prétendre couvrir toute l’histoire expérimentale de `alpha(Q²)`.

```text
source disponible : oui ;
transformation déclarée : oui ;
domaine déclaré : oui ;
modèle radiatif détaillé extrait : non ;
verdict : non ouvert.
```

### C — suffisance pour la dérive lente

Lange et al. fournit une contrainte actuelle du premier lot sur une dérive lente et un couplage annuel au potentiel. Le matériau est suffisant pour ouvrir **α4** sur ces deux familles seulement.

```text
source disponible : oui ;
familles déclarées : dérive linéaire et modulation annuelle ;
coefficients de sensibilité à extraire : oui ;
recherches oscillatoires larges : différées ;
verdict : non ouvert.
```

### D — suffisance historique et locale

Le triptyque Webb / Whitmore–Murphy / ESPRESSO permet d’instruire une trajectoire probatoire : prétention positive, découverte d’une systématique majeure, puis contrainte locale mieux calibrée. Il est suffisant pour ouvrir **α5**, mais non pour un verdict cosmologique global.

```text
prétention historique : documentée ;
systématique instrumentale : documentée ;
mesure récente locale : documentée ;
reconstruction de tous les échantillons : absente ;
modèle dipolaire global actualisé : absent ;
verdict global : suspendu par construction à ce stade.
```

## 6. Comparabilité entre sous-dossiers

Les quatre sous-dossiers peuvent être comparés selon une structure commune :

```text
cible ;
transformation ;
accès ;
modèle de passage ;
résultat quantitatif ;
mode de soutien probatoire ;
systématiques ;
domaine ;
condition d’échec.
```

Ils ne peuvent pas être combinés numériquement. Les unités statistiques, modèles, observables et transformations sont hétérogènes.

La comparaison finale devra porter sur la forme des attributions :

```text
A : une valeur est recommandée ou déterminée par une chaîne ;
B : une relation d’évolution est positivement observée ;
C : certaines variations temporelles sont contraintes ;
D : certaines variations spatiales sont prétendues, repondérées ou localement contraintes.
```

## 7. Dettes transversales avant α2–α5

1. vérifier les versions publiées et éventuels errata ;
2. extraire les équations et définitions directement des sources primaires ;
3. déclarer le schéma de renormalisation lorsque pertinent ;
4. identifier les paramètres associés et covariances ;
5. séparer erreurs statistiques, systématiques et théoriques ;
6. identifier les données et produits publics disponibles ;
7. conserver les anciennes fiches DOCX comme sources généalogiques, sans leur vocabulaire déclassé ;
8. ne produire aucun verdict commun avant les fiches locales.

## 8. Décision préparatoire d’α1

```text
quatre sous-dossiers : scientifiquement instruisibles ;
matériaux primaires du premier lot : suffisants pour ouvrir α2–α5 de manière bornée ;
comparaison numérique transversale : non pertinente ;
verdict général « alpha est constante » : interdit à ce stade ;
prochaine décision requise : choisir l’ordre d’exécution des fiches α2–α5
                              et leur profondeur respective ;
propagation vers la synthèse du cycle : non ouverte.
```

La matrice sera révisée si l’extraction détaillée d’une source révèle que la cible ou la famille de transformations a été mal identifiée.