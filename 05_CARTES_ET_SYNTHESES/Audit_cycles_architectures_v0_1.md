# Audit cycles et architectures v0.1

## 0. Statut documentaire

```text
statut : audit de rang 1 ;
fonction : verifier l'equilibre entre cycles, architectures et cartes actives ;
portee : cycles physiques, cercle 2 architectural, cartes consolidees recentes ;
sortie : diagnostic, matrice de centres, corrections ciblees.
```

Cet audit suit l'ordonnancement des chantiers croises :

```text
1. stabiliser les centres ;
2. qualifier ensuite les limites ;
3. trier seulement apres les ouvertures philosophiques et les livrables.
```

Il ne produit pas encore une reecriture transversale du corpus.

Il decide ce qu'il faut reprendre pour que les architectures ne deviennent ni
un tableau juxtapose, ni une nouvelle couche taxonomique autonome.

## 1. Documents actifs consultes

Cycles et syntheses de cycles :

```text
02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/Synthese_cycle_saveur_Higgs_v0_1.md
02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/Synthese_CP1_seuil_electrofaible_v0_1.md
02_CYCLES_PHYSIQUES/06_Cycle_effectif_basse_energie/Synthese_cycle_effectif_basse_energie_v0_1.md
02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Synthese_cycle_cosmologique_v0_1.md
02_CYCLES_PHYSIQUES/08_Cycle_metrologique_SI/Cycle_metrologique_SI_v0_1_c_h_e.md
02_CYCLES_PHYSIQUES/04_Cycle_thermo_metrologique/Synthese_recuperation_thermo_metrologique_SI_v0_1.md
```

Architectures actives :

```text
04_ARCHITECTURES_INTER_FAMILLES/Cercle2_architectures_actives_v0_1.md
04_ARCHITECTURES_INTER_FAMILLES/Cercle2_lot2A_Saveur_Higgs_v0_1.md
04_ARCHITECTURES_INTER_FAMILLES/Cercle2_lot2B_Metrologique_SI_v0_1.md
04_ARCHITECTURES_INTER_FAMILLES/Cercle2_lot2C_Effective_basse_energie_v0_1.md
04_ARCHITECTURES_INTER_FAMILLES/Cercle2_lot2D_Cosmologique_v0_1.md
04_ARCHITECTURES_INTER_FAMILLES/Cercle2_lot2E_Synthese_transverse_architectures_v0_1.md
```

Cartes et notes de controle :

```text
05_CARTES_ET_SYNTHESES/Carte_dependances_architectures_v0_1.md
05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_3_post_cercle2.md
05_CARTES_ET_SYNTHESES/Mise_a_jour_intellectuelle_v0_2.md
01_CADRE_METHODOLOGIQUE/Note_situation_effective_et_equilibrage_SI_v0_1.md
01_CADRE_METHODOLOGIQUE/Audit_terminologique_actif_v0_1.md
```

## 2. Diagnostic general

Le corpus est globalement solide au niveau architectural.

Les cycles ne sont plus de simples listes de grandeurs. Ils portent chacun un
centre de gravite identifiable :

```text
constitution ;
seuil d'entree ;
validite de description ;
definition et realisation ;
inference et reconstruction ;
borne et acces heterogenes.
```

Le risque principal n'est donc pas l'absence de structure.

Le risque principal est un deplacement de proportion :

```text
1. le SI est plus dense que les autres cycles et peut attirer la definition
   generale vers l'acces definitionnel ;
2. le vocabulaire "situe" peut encore etre lu comme un primat de l'acces ;
3. les architectures peuvent paraitre toutes equivalentes si leurs
   temporalites propres ne restent pas visibles ;
4. le vocabulaire historique peut revenir comme premier nom au lieu de rester
   en controle de rang.
```

Decision de l'audit :

```text
les architectures actives sont confirmees,
mais les cartes doivent renforcer la proportion entre centres locaux.
```

## 3. Matrice des centres de gravite

| Ensemble | Centre de gravite | Type de stabilisation | Acces | Limite conservee | Decision |
|---|---|---|---|---|---|
| Saveur-Higgs | Constitution du regime brise | Echelle, textures, diagonalisation, spectres, orientations | Mesures faibles, Higgs, fits, oscillations | Origine des Yukawa, hierarchies, nature neutrino | Centre robuste |
| Seuil electrofaible | Entree de regime | Constance de seuil autour de `v` | `G_F`, masses faibles, ajustements electroweak | Secteur scalaire, jauge, historicite cosmique | Raccord local confirme |
| Effective basse energie | Validite de description | Regime limite, non-resolution, couplage ou echelle | Extractions faibles, QCD, rapports d'echelle | Completion, non-perturbatif, gravitation quantique | Centre robuste |
| Metrologique SI | Definition et realisation | Valeurs definissantes, compositions exactes, realisations | Definitions et procedures metrologiques | Roles physiques non epuises | Cas local dense |
| Cosmologique | Inference et reconstruction | Modele global, sous-reseaux, observables reconstruites | CMB, BAO, SNe, distances, lensing, amas | Tensions, energie noire, microphysique primordiale | Macro-architecture robuste |
| Neutrinos | Bornes et acces heterogenes | Ecart spectral, orientation, ancrage absolu borne | Oscillations, beta, cosmologie, double beta selon hypotheses | Nature Dirac/Majorana, masse absolue | Interface sensible |

Lecture :

```text
aucun centre ne doit devenir le modele unique des autres.
```

Le SI donne la grammaire la plus forte de definition et de realisation.

La cosmologie donne la grammaire la plus forte d'inference et de reconstruction.

Saveur-Higgs et le seuil electrofaible donnent la grammaire la plus forte de
constitution et d'entree de regime.

L'effectivite basse energie donne la grammaire la plus forte de validite de
description.

Les neutrinos donnent la grammaire la plus forte des bornes et des acces
heterogenes.

## 4. Dependances entre cycles et architectures

### 4.1. Seuil electrofaible vers Saveur-Higgs

Dependance stabilisee :

```text
seuil BEH -> `v` -> architecture Saveur-Higgs.
```

Cette dependance est saine.

Elle evite deux erreurs :

```text
1. faire commencer Saveur-Higgs sans amont de regime ;
2. transformer le seuil electrofaible en architecture concurrente.
```

Le seuil electrofaible doit rester :

```text
un raccord local de seuil,
non un nouveau centre taxonomique general.
```

### 4.2. SI vers definition generale

Dependance utile :

```text
SI -> distinction valeur definissante / realisation / role physique conserve.
```

Mais cette dependance doit rester locale.

Elle ne doit pas devenir :

```text
SI -> modele general de toute constance.
```

Le SI sert a montrer comment une valeur peut etre fixee et rendue operatoire.

Il ne doit pas forcer les autres cycles a etre lus comme des cas d'acces
definitionnel.

### 4.3. Effective basse energie vers limites

Dependance stabilisee :

```text
validite de description -> domaine -> limite -> retrait.
```

Ce cycle prepare directement l'audit des limites.

Il fournit un bon langage pour distinguer :

```text
borne de validite ;
seuil de validite ;
completion absente ;
changement de description ;
suppression par hierarchie d'echelle.
```

### 4.4. Cosmologie vers audit des tensions

Dependance stabilisee :

```text
modele global -> sous-reseau -> acces -> reconstruction -> tension.
```

La cosmologie prepare directement l'audit des limites, mais sous une forme
distincte de l'effectivite basse energie.

Ici la limite prend souvent la forme :

```text
discordance d'acces ;
dependance de modele ;
reconstruction tardive ;
tension transversale.
```

### 4.5. Neutrinos comme interface sensible

Les neutrinos relient plusieurs zones :

```text
Saveur-Higgs ;
cosmologie ;
borne ;
orientation ;
ancrage spectral.
```

Ils doivent rester une interface sensible, non un appendice du cycle
Saveur-Higgs ni une simple projection cosmologique.

Ce point doit etre repris dans l'audit des limites.

## 5. Points robustes

### 5.1. La logique positive fonctionne

Le cercle 2 a reussi son deplacement principal :

```text
decrire ce que chaque architecture fait
avant de dire ce qu'elle n'est pas.
```

Les formulations positives sont plus lisibles et plus fecondes que les
formulations defensives.

### 5.2. Les temporalites sont presentes

Les cycles ne sont plus des tableaux plats.

Chaque architecture porte une trajectoire :

```text
Saveur-Higgs : brisure -> textures -> diagonalisation -> spectres -> orientations ;
seuil electrofaible : seuil -> echelle -> temoins -> acces -> architecture ;
SI : stabilisation empirique -> absorption definitionnelle -> realisation ;
effective : description plus complete -> regime limite -> grandeur stabilisee ;
cosmologie : modele -> inference -> reconstruction -> comparaison des acces.
```

Ces trajectoires doivent rester visibles dans les cartes.

### 5.3. Le test de retrait est devenu transversal

Le test de retrait sert bien a verifier qu'une architecture n'est pas une
simple collection.

Il ne doit pas etre transforme en preuve absolue.

Il doit rester un test de solidarite :

```text
si le retrait d'un noeud dissout le statut local,
alors le niveau architectural est actif.
```

### 5.4. L'ancrage realiste est conserve

Les notes recentes corrigent le risque de lecture derealisante.

Formule a conserver :

```text
l'acces qualifie le statut de constance ;
il ne produit pas l'objet physique ou operationnel.
```

Cette formule doit rester visible dans les cartes et les livrables.

## 6. Frictions actives

### 6.1. Densite excessive du SI

Le SI est necessaire, mais son volume documentaire peut suggerer une
hierarchie implicite.

Risque :

```text
la definition generale se laisse attirer par le cas ou l'acces definitionnel
est le plus fort.
```

Correction :

```text
signaler dans les cartes que le SI est un cas local dense,
non le patron de toute stabilisation.
```

### 6.2. Ambiguite residuelle de "situe"

Le terme reste utile, mais doit etre accompagne.

Risque :

```text
situe = seulement relatif a un acces.
```

Correction :

```text
situe = regime d'effectuation + acces + qualification limitee.
```

Dans les formulations directes, preferer souvent :

```text
dans un regime determine ;
qualifiee par des acces explicites ;
avec limites conservees.
```

### 6.3. "Validite situee" dans l'architecture effective

La formule est comprehensible apres definition, mais elle peut etre trop
compacte.

Correction recommandee :

```text
validite de description dans un regime determine.
```

Cette formulation est plus descriptive et moins exposee au malentendu.

### 6.4. Vocabulaire historique encore present dans les titres ou cadres

Les dossiers gardent leur genealogie.

Ce n'est pas un probleme en soi.

Risque :

```text
le lecteur croit que les anciens termes commandent encore la methode active.
```

Correction :

```text
conserver les anciens termes dans les titres historiques et les sections de
controle, mais ouvrir les documents actifs par regime, solidarite, acces,
trajectoire et limite.
```

### 6.5. Carte des dependances encore trop genealogique

La carte des dependances est utile, mais elle doit etre alignee avec la v1.3.

Deux points a reprendre :

```text
1. expliciter plus nettement que la dependance n'est pas une dependance de
   connaissance seulement ;
2. remplacer les formulations trop genealogiques par une lecture de
   solidarisation active lorsque le contexte le permet.
```

### 6.6. Neutrinos et bornes encore disperses

La masse absolue des neutrinos est correctement traitee avec prudence.

Mais son statut transversal doit etre mieux signale :

```text
ancrage spectral borne ;
interface Saveur-Higgs / cosmologie ;
cas test pour l'audit des limites.
```

## 7. Corrections ciblees recommandees

### 7.1. Carte consolidee v1.3

Reprise ciblee :

```text
ajouter ou renforcer une phrase de proportion sur le SI ;
eviter que "situee" soit lu comme primat de l'acces ;
maintenir l'ancrage physique ou operationnel dans la definition courte.
```

Statut :

```text
necessaire, mais courte.
```

### 7.2. Synthese transverse des architectures

Reprise ciblee :

```text
remplacer "Validite situee" par "Validite de description" ou
"validite de description dans un regime determine" ;
ajouter la regle : le regime d'effectuation vient avant l'acces,
sauf cas definitionnels ou reconstructifs explicitement nommes.
```

Statut :

```text
utile avant l'audit des limites.
```

### 7.3. Carte des dependances architecturales

Reprise ciblee :

```text
aligner le titre et la fonction sur "architectures actives" ;
renforcer la lecture par centres de gravite ;
ajouter les dependances de proportion entre SI, cosmologie et autres cycles ;
signaler les neutrinos comme interface sensible.
```

Statut :

```text
priorite haute dans le prochain paquet de corrections.
```

### 7.4. Index et notes de methode

Reprise ciblee :

```text
pointer cet audit comme controle des centres ;
ne pas ouvrir encore un plan de publication ;
preparer l'audit des regimes de limite.
```

Statut :

```text
a faire apres les corrections des cartes, si necessaire.
```

## 8. Ordre de reprise applique

L'ordre de reprise reste leger :

```text
1. synthese transverse des architectures : "validite de description" ;
2. carte des dependances : centres de gravite et proportion ;
3. carte consolidee v1.3 : regle de proportion pres de la definition ;
4. ouvrir ensuite l'audit des regimes de limite.
```

Justification :

```text
la synthese transverse donne la grammaire commune ;
la carte des dependances donne la structure ;
la carte consolidee donne la definition visible ;
l'audit des limites depend de ces trois appuis.
```

## 9. Decision

Decision de l'audit :

```text
les cycles et architectures sont suffisamment robustes pour poursuivre ;
la prochaine action immediate est une correction ciblee des cartes actives,
non une reecriture generale du corpus.
```

Le chantier suivant reste bien :

```text
audit des regimes de limite.
```

Mais il doit etre precede d'un court paquet de synchronisation :

```text
synthese transverse ;
carte des dependances ;
carte consolidee v1.3.
```

Raccords executes dans la meme passe :

```text
04_ARCHITECTURES_INTER_FAMILLES/Cercle2_lot2E_Synthese_transverse_architectures_v0_1.md
05_CARTES_ET_SYNTHESES/Carte_dependances_architectures_v0_1.md
05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_3_post_cercle2.md
```

Ces raccords ne changent pas la decision generale.

Ils stabilisent les appuis necessaires avant l'audit des regimes de limite.

## 10. Formule de cloture

```text
Les architectures tiennent lorsqu'elles gardent leur centre :
Saveur-Higgs constitue,
le seuil ouvre,
le SI definit et realise,
l'effectivite borne une validite de description,
la cosmologie reconstruit,
les neutrinos testent les bornes et les acces heterogenes.
```
