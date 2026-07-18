# Audit des regimes de limite v0.1

## 0. Statut documentaire

```text
statut : audit de rang 2 ;
fonction : distinguer les regimes de limite avant les livrables ;
portee : bornes, tensions, validites, non-detections, substitutions,
stress tests, retraits et non-theses ;
sortie : typologie operative, regles de lecture, reprises ciblees.
```

Cet audit intervient apres :

```text
05_CARTES_ET_SYNTHESES/Ordonnancement_chantiers_croises_v0_1.md
05_CARTES_ET_SYNTHESES/Audit_cycles_architectures_v0_1.md
```

Sa fonction est de clarifier ce que le corpus appelle `limite`.

Cette clarification donne aux prochains livrables une discipline de portee :
une borne garde son statut de borne, une tension son niveau d'escalade, une
non-detection son regime de suspension conditionnelle.

## 1. Documents actifs consultes

Documents de prudence et non-theses :

```text
05_CARTES_ET_SYNTHESES/Fiche_limites_non_theses_v0_1.md
05_CARTES_ET_SYNTHESES/Premier_degagement_these_v0_1.md
05_CARTES_ET_SYNTHESES/Matrice_degagements_theoriques_v0_1.md
05_CARTES_ET_SYNTHESES/Mise_epreuve_degagements_theoriques_exemples_porteurs_v0_1.md
```

Documents de test et d'escalade :

```text
05_CARTES_ET_SYNTHESES/Chantier_test_de_retrait_limites_v0_1.md
01_CADRE_METHODOLOGIQUE/Passerelle_escalade_tensions_cosmologiques_v0_1.md
03_TESTS_TAXONOMIQUES/Test_traversant_H0_passerelle_tensions_v0_1.md
```

Cas physiques porteurs :

```text
02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/Fiche_masse_absolue_neutrinos_v0_1.md
02_CYCLES_PHYSIQUES/06_Cycle_effectif_basse_energie/Synthese_cycle_effectif_basse_energie_v0_1.md
02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Synthese_cycle_cosmologique_v0_1.md
04_ARCHITECTURES/Architecture_cosmologique_stress_test_v0_1.md
```

## 2. Diagnostic general

Le corpus a correctement etabli que les limites conservees peuvent renforcer
la robustesse.

La formule est solide :

```text
une limite conservee fait partie de la qualification prudente du statut.
```

Le terme `limite` gagne en precision lorsqu'il est decompose.

Il recouvre au moins neuf regimes distincts :

```text
1. limite de validite ;
2. limite de completion ;
3. borne ou contrainte ;
4. non-detection ;
5. tension inter-acces ;
6. dependance de modele ;
7. substitution controlee ;
8. retrait ou dissolution ;
9. limite de realisation.
```

Decision de l'audit :

```text
la notion de limite est confirmee,
mais elle doit devenir une typologie operative avant tout plan de livrable.
```

## 3. Typologie des regimes de limite

| Regime de limite | Question directrice | Exemples | Regle de lecture | Sortie stabilisee |
|---|---|---|---|---|
| Validite | Dans quel domaine la description vaut-elle ? | `G_F`, `M_W`, `M_Pl` | Domaine explicite comme precision de portee | Validite de description |
| Completion | Que laisse ouverte la description locale ? | gravite quantique, origine des Yukawa, energie noire | Ouverture traitee comme horizon de completion | Completion ouverte |
| Borne | Quelle region admissible est stabilisee par contrainte ? | masse absolue neutrino, `m_beta`, `Sigma_m_nu` | Contrainte distincte d'une mesure positive | Stabilisation par contrainte |
| Non-detection | Quel statut porte l'absence de signal positif ? | double beta sans neutrino, masse positive non convergente | Signal, valeur nulle et statut physique distingues | Suspension conditionnelle |
| Tension | Quelles routes d'acces divergent ? | `H_0`, `S_8`, `A_s` / `sigma_8` | Divergence traitee par niveau d'escalade | Niveau d'escalade |
| Modele | Quel cadre conditionne l'inference ? | cosmologie, `Omega_i`, `w`, `Sigma_m_nu` | Modele et degenerescences indexes | Indexation de modele |
| Substitution | Que devient le signal si l'on remplace un noeud ? | calibrations, `r_d`, `w0-wa`, sondes de croissance | Dependances mesurees par test controle | Test controle |
| Retrait | Que perd le reseau si un noeud est retire ? | `v`, realisations SI, `w`, routes d'acces | Dissolution, degradation et substitution graduees | Retrait gradue |
| Realisation | Une exactitude formelle est-elle mise en oeuvre ? | SI, `R`, `K_J`, `R_K` | Definition et realisation distinguees | Limite operationnelle |

Cette typologie nomme les formes de prudence necessaires a la qualification.

Elle garde le rang d'un outil de lecture des limites.

## 4. Regimes confirmes par les cas porteurs

### 4.1. Validite de description

Le cycle effectif basse energie stabilise le regime le plus net :

```text
une grandeur peut etre robuste dans un domaine limite,
avec une completion ou un changement de description conserve comme horizon.
```

Cas :

```text
G_F : coefficient local dans le regime E << M_W ;
M_W : echelle ou la description de Fermi cesse d'etre suffisante ;
Lambda_QCD : changement de regime perturbatif / non perturbatif ;
M_Pl : echelle de validite attendue, non frontiere experimentale nette.
```

Decision :

```text
la limite de validite est une limite positive de domaine.
```

Elle conserve trois limites de portee :

```text
la grandeur reste reelle dans son regime ;
la description a un domaine de validite explicite ;
la completion haute energie demeure ouverte.
```

### 4.2. Borne ou contrainte

La masse absolue des neutrinos donne le cas central.

Elle stabilise :

```text
un ancrage spectral encore borne,
traverse par plusieurs projections d'acces.
```

Les trois voies portent des projections distinctes :

```text
m_beta : projection cinematique locale ;
Sigma_m_nu : contrainte cosmologique globale et modele-dependante ;
m_beta_beta : projection coherente conditionnelle sous hypothese Majorana.
```

Decision :

```text
une borne stabilise un domaine admissible
et laisse la mesure positive comme seuil ouvert.
```

Regle :

```text
dire toujours quelle grandeur est bornee,
par quelle voie,
dans quel modele ou sous quelle hypothese.
```

### 4.3. Non-detection

La non-detection forme un regime distinct de la borne.

Elle indique :

```text
aucun signal positif convergent dans le regime d'acces considere.
```

Sa lecture positive est :

```text
suspension conditionnelle ;
contrainte du regime d'acces ;
appel a distinguer absence de signal, valeur nulle et statut physique.
```

Cas sensibles :

```text
masse positive non determinee ;
double beta sans neutrino non observee ;
absence de detection conditionnelle dans une route d'acces particuliere.
```

Sortie correcte :

```text
stabilisation suspendue,
ou borne non convertie en detection.
```

### 4.4. Tension inter-acces

La passerelle cosmologique donne le protocole actif :

```text
divergence -> tension qualifiee -> stress test -> substitution controlee
-> dossier autonome eventuel.
```

Le test `H_0` confirme l'usage :

```text
H_0 reste un parametre d'etat actuel ;
la tension H_0 devient une tension persistante sous stress test,
avec test de substitution ouvert.
```

Decision :

```text
une tension a le statut d'un niveau d'escalade
dans un reseau d'acces et de modele.
```

Regle :

```text
passer par l'echelle d'escalade avant toute qualification d'anomalie.
```

### 4.5. Dependance de modele

La cosmologie impose un regime de limite propre.

Une grandeur peut etre fortement contrainte :

```text
dans un modele donne,
par des routes d'acces determinees,
avec des degenerescences identifiables.
```

Cela vaut pour :

```text
H_0 ;
Omega_i ;
w ;
A_s / n_s ;
sigma_8 / S_8 ;
Sigma_m_nu.
```

Decision :

```text
la dependance de modele qualifie la stabilisation.
```

Regle :

```text
une valeur cosmologique robuste doit toujours indiquer son modele d'inference.
```

### 4.6. Substitution controlee

La substitution fonctionne comme test applique a une limite active.

Question :

```text
que devient le signal si l'on remplace une calibration,
une route d'acces, une hypothese de modele ou une parametrisation ?
```

Exemples :

```text
changer la calibration locale de H_0 ;
tester une ancre BAO differente ;
comparer w = -1, w constant, w0-wa ou courbure libre ;
tester tau, neutrinos ou croissance tardive entre A_s et sigma_8.
```

Decision :

```text
la substitution mesure une dependance
et garde la these physique en attente de dossier propre.
```

### 4.7. Retrait et dissolution

Le test de retrait appelle une version graduee.

La note de chantier l'a formule clairement :

```text
presque tout reseau dense se dissout si l'on retire un noeud ;
il faut distinguer solidarite reelle et densite triviale.
```

Decision :

```text
le test de retrait doit devenir gradue.
```

Sorties a distinguer :

```text
dissolution en cascade ;
dissolution locale ;
non-dissolution ;
degradation distribuee ;
degradation reversible par substitution.
```

Cette evolution soutient la distinction entre solidarite reelle et densite
triviale.

### 4.8. Limite de realisation

Le SI donne un regime de limite distinct.

Dans le SI :

```text
une valeur peut etre exacte par definition,
mais sa realisation pratique conserve des incertitudes.
```

Cas :

```text
c, h, e, k_B, N_A ;
R = N_A k_B ;
K_J ;
R_K.
```

Decision :

```text
exactitude definitionnelle et realisation pratique restent deux niveaux
distincts.
```

Ce regime reste local a l'architecture definitionnelle et operationnelle.

## 5. Regles positives de lecture

| Glissement surveille | Point a preserver | Regle positive |
|---|---|---|
| Borne lue comme mesure | Statut de contrainte | Dire borne, voie d'acces, modele et hypothese |
| Tension lue comme anomalie conclue | Niveau d'escalade | Passer par l'echelle d'escalade |
| Non-detection lue comme absence | Suspension conditionnelle | Distinguer signal, valeur nulle et statut |
| Validite locale detachee de son domaine | Domaine de validite | Dire domaine, regime et portee |
| Modele-dependance lue comme arbitraire | Stabilisation indexee | Indexer le modele et les degenerescences |
| Retrait binaire lu comme demonstration globale | Solidarite graduee | Graduer dissolution, vitesse et profondeur |
| Exactitude SI lue comme mesure parfaite | Definition et realisation | Distinguer definition, realisation, role physique |
| Limite lue comme non-these seulement | Qualification positive du statut | Inscrire le regime de limite dans la qualification |

## 6. Matrice de traitement d'une limite

Toute limite active doit etre traitee selon l'ordre suivant :

```text
1. Objet : quelle grandeur, operation ou reconstruction est concernee ?
2. Regime : ou cette grandeur opere-t-elle ?
3. Type de limite : validite, borne, tension, modele, non-detection,
   substitution, retrait, realisation ou completion ?
4. Acces : quelle route produit ou contraint la limite ?
5. Modele ou hypothese : quel cadre porte l'inference ?
6. Niveau de maturite : documentee, bornee, persistante, sous stress test,
   substitution ouverte, anomalie candidate non conclue ?
7. Sortie : que peut-on affirmer en respectant le regime ?
8. Limite conservee : quelle conclusion reste reservee ?
```

Formule courte :

```text
nommer la limite,
nommer son regime,
nommer son acces,
puis seulement decider son statut.
```

## 7. Effet sur les degagements theoriques

L'audit confirme le degagement T6 :

```text
les limites conservees sont structurantes.
```

Mais il le precise.

T6 doit rester une these de qualification :

```text
une limite renforce la robustesse quand son regime est qualifie.
```

Formulation corrigee :

```text
une limite conservee renforce la robustesse lorsque son type,
son regime, son acces et son niveau de maturite sont explicites.
```

Effet sur les autres degagements :

| Degagement | Effet de l'audit |
|---|---|
| T0 | La qualification du statut doit toujours inclure le type de limite |
| T2 | La validite de description devient un regime de limite propre |
| T3 | L'acces qualifie differemment une borne, une tension ou une reconstruction |
| T4 | Les limites ont des temporalites : domaine, trajectoire de borne, escalation |
| T5 | L'architecture exige un test de retrait gradue |
| T8 | La reconstruction cosmologique doit declarer modele, acces et tension |

## 8. Reprises ciblees recommandees

### 8.1. Fiche limites et non-theses

Reprise executee :

```text
ajouter une typologie courte des regimes de limite ;
convertir les formulations trop generales en distinctions de regime :
validite / borne / tension / non-detection / modele / realisation.
```

Statut :

```text
execute dans la meme passe.
```

### 8.2. Matrice des degagements theoriques

Reprise executee :

```text
preciser T6 :
"limite comme robustesse" devient "limite qualifiee comme robustesse".
```

Statut :

```text
execute dans la meme passe.
```

### 8.3. Premier degagement de these

Reprise utile :

```text
garder la these-noyau legere ;
ajouter seulement une note de lecture renvoyant a la typologie des limites.
```

Statut :

```text
a faire si le livrable s'appuie directement sur ce document.
```

### 8.4. Chantier du test de retrait

Reprise utile :

```text
transformer le chantier differe en protocole court de retrait gradue.
```

Statut :

```text
utile, compatible avec l'audit des livrables.
```

## 9. Decision

Decision de l'audit :

```text
le chantier des limites est suffisamment stabilise pour servir de garde-fou
au prochain plan de livrable.
```

Raccord principal execute :

```text
05_CARTES_ET_SYNTHESES/Fiche_limites_non_theses_v0_1.md
05_CARTES_ET_SYNTHESES/Matrice_degagements_theoriques_v0_1.md
05_CARTES_ET_SYNTHESES/Mise_epreuve_degagements_theoriques_exemples_porteurs_v0_1.md
```

La prochaine action logique devient :

```text
audit philosophie / livrables.
```

Le plan de livrable resserre doit venir ensuite :

```text
apres le tri entre instrument, voisinage, hypothese et argument.
```

## 10. Formule de cloture

```text
Une limite tire sa valeur methodologique de son regime :
validite, borne, non-detection, tension, modele, substitution, retrait
ou realisation.
La prudence devient robuste lorsque le corpus sait dire quel type de limite
il conserve et quelle conclusion reste reservee.
```
