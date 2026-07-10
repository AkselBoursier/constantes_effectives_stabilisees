# Carte consolidee v1.2 - refonte

## Carte de reference apres methode v1.3 et dependances architecturales

### 1. Fonction de la v1.2

Cette carte consolide l'etat du projet apres :

```text
la note methodologique v1.3,
la matrice de criblage taxonomique,
la note d'architecture Saveur-Higgs,
et la carte des dependances architecturales.
```

Elle remplace la carte v1.1 comme carte de reference active.

Elle ne supprime pas la v1.1.

La v1.1 reste utile comme carte historique :

```text
avant rang de forme logique,
avant requalification des liaisons stabilisees,
avant roles contextuels,
avant representation des architectures comme reseaux.
```

La modification principale est :

```text
la carte n'est plus d'abord un tableau de classes fonctionnelles ;
elle devient une grammaire de stabilisation par rangs, roles, acces,
architectures et trajectoires.
```

### 2. Definition consolidee v1.2

Definition de reference :

> Une constante effective stabilisee est une grandeur dont une valeur, une forme, une liaison qualifiee, un role ou une dependance devient robuste dans un regime donne, selon un acces determine, avec un mode et une trajectoire de stabilisation explicites, sans que cette robustesse implique necessairement une constance absolue, une universalite hors contexte ou un statut fondamental.

Formule courte :

```text
constance effective stabilisee =
forme stabilisee
+ fonction dans un regime
+ acces determine
+ role eventuel
+ architecture possible
+ trajectoire explicite
+ limites conservees.
```

Consequence :

```text
avant d'attribuer une fonction directrice a une grandeur,
il faut identifier sa forme logique,
son regime,
son acces,
son role,
son eventuelle dependance architecturale,
et sa trajectoire de stabilisation.
```

### 3. Ce qui change depuis la v1.1

| Point | v1.1 | v1.2 refonte |
|---|---|---|
| Point de depart | Classes fonctionnelles englobantes | Rang de forme logique puis fonctions directrices |
| Liaison non qualifiee | Classe ordinaire mais surveillee | Fonction faible sous audit |
| Fonctions transversales | Niveau secondaire | Roles contextuels avec portee |
| Fonctions architecturales | Niveau distinct | Roles contextuels architecturaux |
| Architecture | Niveau inter-fonctions reconnu | Reseau de dependances soumis a stress test |
| Temporalite | Peu explicite | Axe transversal de trajectoire |
| Acces | Regime obligatoire | Couplage modele-acces et robustesse de l'acces |
| Carte | Tableau consolide | Carte de rangs et de dependances |

Decision :

```text
la v1.2 garde le noyau acquis,
mais change l'ordre des questions.
```

### 4. Table des rangs actifs

| Rang | Niveau | Question directrice |
|---|---|---|
| 0 | Forme logique de stabilisation | Quelle forme est stabilisee avant tout classement fonctionnel ? |
| 1 | Fonction directrice puis famille fonctionnelle controlee | Que fait principalement la grandeur ? |
| 2 | Role contextuel | Quel role prend-elle dans un regime, un acces ou une architecture ? |
| 3 | Axes physique / acces | Ou opere-t-elle et comment est-elle connue ? |
| 4 | Architecture / reseau | Quelles fonctions deviennent solidaires ? |
| 5 | Temporalite / trajectoire | Comment son statut s'installe, varie, persiste ou se reconstruit ? |

Ordre obligatoire :

```text
forme -> fonction -> role -> acces -> architecture -> trajectoire.
```

### 5. Rang 0 : formes logiques

Le rang 0 evite de transformer trop vite une forme d'ecriture en fonction directrice.

| Forme logique | Question | Exemples |
|---|---|---|
| Valeur | Une valeur robuste est-elle stabilisee ? | masse, echelle, constante definissante |
| Rapport | Un quotient est-il stabilise ? | m_p / m_e, Omega_i |
| Ecart | Un ecart spectral ou de regime est-il stabilise ? | Delta m^2 |
| Composition | Une grandeur est-elle composee d'autres grandeurs ? | R, K_J, R_K |
| Equation d'etat | Une loi entre variables d'etat est-elle stabilisee ? | w |
| Fonction d'echelle | Une dependance en echelle est-elle stabilisee ? | alpha_s(Q^2), alpha_G(E) |
| Matrice | Une structure matricielle est-elle stabilisee ? | CKM, PMNS, Yukawa |
| Phase | Une orientation complexe est-elle stabilisee ? | delta_CP, phases CKM |
| Observable reconstruite | Une grandeur est-elle inferee par modele et donnees ? | sigma_8, S_8 |
| Condition initiale | Une donnee initiale de scenario est-elle stabilisee ? | A_s, n_s |
| Convention definissante | Une valeur est-elle fixee par definition ? | k_B, N_A, c, h, e |
| Borne | Un domaine ou une limite est-il stabilise ? | masse absolue neutrino |

Regle :

```text
une liaison d'ecriture n'impose pas une fonction directrice de liaison.
```

### 6. Rang 1 : fonction directrice et familles fonctionnelles

La v1.2 conserve cinq familles fonctionnelles fortes.

La fonction directrice est la question operative.

La famille fonctionnelle est la sortie taxonomique,
si le test de resistance est passe.

| Famille fonctionnelle | Statut v1.2 | Fonction principale | Exemples |
|---|---|---|---|
| Couplage | Forte | Parametrer une intensite d'interaction ou de liaison | alpha, alpha_s(Q^2), alpha_G(E), Y_f |
| Echelle | Forte | Fixer ou reveler un ordre de grandeur structurant | v, M_W, Lambda_QCD, M_Pl |
| Raccordement | Forte | Relier deux descriptions, niveaux ou regimes | G_F |
| Orientation | Forte | Stabiliser un desalignement entre bases, champs ou secteurs | theta_W, CKM, PMNS, delta_CP |
| Convention | Forte | Recevoir une valeur exacte dans un systeme de definition | k_B, N_A, c, h, e |
| Liaison stabilisee | Faible sous audit | Stabiliser une liaison irreductible entre grandeurs | Cas a justifier un par un |

Decision :

```text
La liaison stabilisee n'est plus une famille fonctionnelle par defaut.
```

Elle ne peut etre conservee que si la liaison est vraiment la fonction principale et ne se reduit pas a :

```text
une forme logique,
un role contextuel,
une normalisation,
une composition,
ou une architecture.
```

### 7. Re-traitement des liaisons stabilisees

| Cas | Ancienne tentation | Lecture v1.2 |
|---|---|---|
| `m_f = y_f v / sqrt(2)` | Liaison constitutive | Architecture Saveur-Higgs |
| `R = N_A k_B` | Composition exacte | Architecture SI + composition exacte |
| `K_J = 2 e / h` | Composition exacte | Architecture SI + realisation electrique |
| `R_K = h / e^2` | Composition exacte | Architecture SI + realisation electrique |
| `Omega_i = rho_i / rho_crit` | Rapport normalise | Densite normalisee cosmologique |
| `w = p / rho` | Equation d'etat | Role contextuel d'etat |
| `Delta m^2` | Liaison spectrale | Ecart spectral + dephasage oscillatoire |

Formule :

```text
La liaison stabilisee cesse d'etre une case ;
elle devient une question a tester.
```

### 8. Rang 2 : roles contextuels

Un role contextuel indique ce qu'une grandeur fait dans un regime determine.

Il peut etre :

```text
local,
transversal,
architectural,
documentaire.
```

| Role | Question | Portee typique |
|---|---|---|
| Seuil | Marque-t-il une transition ou une limite d'activation ? | Locale / transversale |
| Borne | Fixe-t-il une limite inferieure, superieure ou effective ? | Locale / transversale |
| Validite | Delimite-t-il un domaine de description ? | Transversale / architecturale |
| Dephasage | Stabilise-t-il une evolution de phase observable ? | Locale / transversale |
| Hierarchie | Organise-t-il des ordres de grandeur ? | Transversale |
| Fond | Structure-t-il l'etat global d'un modele ? | Architecturale |
| Parametre d'etat | Decrit-il un etat dans un modele ou a une epoque ? | Architecturale |
| Densite normalisee | Normalise-t-il une composante dans un budget global ? | Architecturale |
| Equation d'etat | Decrit-il le comportement d'une composante ? | Architecturale |
| Condition initiale | Fixe-t-il un etat ou spectre initial ? | Architecturale |
| Observable reconstruite | Est-il infere par un reseau modele-donnees ? | Architecturale |

Regle :

```text
un role peut etre indispensable sans devenir une famille fonctionnelle.
```

### 9. Rang 3 : regime physique et regime d'acces

Toute fiche doit distinguer :

```text
regime physique : ou la grandeur opere ;
regime d'acces : comment la grandeur est connue.
```

La v1.2 ajoute deux champs obligatoires lorsque l'acces est non trivial :

```text
couplage modele-acces,
robustesse de l'acces.
```

| Type d'acces | Description | Risque |
|---|---|---|
| Direct | Acces proche de l'operation definissante | Surestimer l'independance |
| Operationnel | Acces par procedure stabilisee | Confondre procedure et essence |
| Reconstruit | Acces par chaine d'inference | Effacer le modele |
| Combine | Plusieurs routes d'acces agregees | Masquer les tensions |
| Conventionnel | Valeur fixee par definition | Confondre exactitude et role physique |
| Modele-dependant fort | Extraction conditionnee par un modele | Naturaliser un parametre reconstruit |

Regle :

```text
une grandeur n'est pas seulement ce qu'elle vaut ;
elle est aussi ce qui la rend accessible.
```

### 10. Rang 4 : architectures actives

Quatre architectures sont actives.

| Architecture | Forme dominante | Document actif | Statut |
|---|---|---|---|
| Saveur-Higgs | Constitutive | `04_ARCHITECTURES_INTER_FAMILLES/Architecture_saveur_Higgs_notes.md` | Confirmee |
| Metrologique SI | Definitionnelle / operationnelle | `04_ARCHITECTURES_INTER_FAMILLES/Architecture_metrologique_SI_notes.md` | Confirmee etendue |
| Effective basse energie | Validite | `04_ARCHITECTURES_INTER_FAMILLES/Architecture_effective_basse_energie_notes.md` | Confirmee |
| Cosmologique | Inferentielle / reconstructive | `04_ARCHITECTURES_INTER_FAMILLES/Architecture_cosmologique_notes.md` + stress test | Macro-architecture confirmee avec sous-reseaux |

Regle de rang :

```text
une architecture inter-fonctions n'est pas un niveau de classement superieur.
```

Definition :

```text
une architecture est une solidarite de fonctions dans un regime,
stabilisee par un reseau de dependances.
```

### 11. Les quatre reseaux de dependance

| Architecture | Noeud critique | Dependances principales | Limite conservee |
|---|---|---|---|
| Saveur-Higgs | `v + Y_f + diagonalisation` | Echelle, couplage, spectres, orientations | Origine des Yukawa et hierarchies |
| SI | Constantes definissantes | Convention, compositions exactes, realisations | Origine physique de c, h, e |
| Effective basse energie | Echelle de validite | Raccordement, couplage, seuil, domaine | Completion profonde |
| Cosmologique | Couplage modele-acces | Fond-expansion, budget, etat, primordial, croissance-reconstruction | Tensions H_0 / S_8 et nature de Lambda |

La carte de dependances stabilise une regle :

```text
un regroupement devient architecture seulement si le retrait d'un noeud central
modifie le reseau de fonctions.
```

### 12. Rang 5 : temporalite et trajectoires

La temporalite n'est pas une famille fonctionnelle.

Elle n'est pas une architecture.

Elle decrit comment le statut se stabilise.

| Trajectoire | Sens | Exemples |
|---|---|---|
| Constitution | Un statut devient lisible apres une transformation de regime | Saveur-Higgs apres brisure |
| Absorption conventionnelle | Une valeur devient definissante | k_B, N_A, c, h, e dans le SI |
| Validite / transition | Une grandeur vaut dans un domaine limite | G_F, M_W, Lambda_QCD, M_Pl |
| Flot | Une grandeur depend d'une echelle controlee | alpha_s(Q^2), alpha_G(E) |
| Reconstruction modele-dependante | Une valeur est inferee par modele et donnees | H_0, sigma_8, S_8 |
| Divergence inter-acces | Des routes d'acces restent tendues | H_0, S_8 |
| Stabilisation bornee | La grandeur reste connue par limites | masse absolue neutrino |

Formule :

```text
le temps expose la trajectoire de stabilisation,
pas une nouvelle categorie taxonomique.
```

### 13. Tensions de donnees

La v1.2 conserve la prudence suivante :

```text
une tension de donnees n'est pas une famille fonctionnelle.
```

Elle peut toutefois devenir un signal actif pour tester :

```text
un regime d'acces,
une dependance de modele,
une architecture,
ou une limite de validite.
```

| Niveau de tension | Action |
|---|---|
| Locale | Documenter sans reclasser |
| Inter-acces | Comparer les routes d'acces |
| Persistante | Ajouter un stress test |
| Modele-dependante | Expliciter le modele |
| Candidate a rupture | Ne pas trancher sans dossier propre |

### 14. Matrice canonique v1.2

Toute nouvelle fiche devrait contenir au minimum :

| Champ | Question |
|---|---|
| Grandeur | De quoi parle-t-on exactement ? |
| Forme logique | Quelle forme est stabilisee ? |
| Fonction directrice candidate | Quelle fonction principale semble dominante ? |
| Famille fonctionnelle obtenue | La fonction resiste-t-elle comme sortie taxonomique ? |
| Test de resistance | La fonction resiste-t-elle au criblage ? |
| Role contextuel | Quel role local, transversal ou architectural prend-elle ? |
| Portee du role | Ou ce role vaut-il ? |
| Regime physique | Dans quel domaine opere-t-elle ? |
| Regime d'acces | Comment est-elle connue ? |
| Couplage modele-acces | Quel modele conditionne l'acces ? |
| Robustesse de l'acces | Directe, reconstruite, combinee, fragile, conventionnelle ? |
| Manifestation phenomenologique | Comment le role apparait-il ? |
| Trajectoire de stabilisation | Comment le statut s'installe ou varie ? |
| Tension eventuelle | Quel type de tension doit etre documente ? |
| Architecture eventuelle | Quel reseau de dependance est implique ? |
| Test de retrait | Que perd-on si la grandeur est retiree ? |
| Limite | Ce que le classement ne dit pas |

### 15. Protocole de classement

Ordre de travail :

```text
1. Identifier la grandeur.
2. Identifier la forme logique.
3. Identifier le regime physique.
4. Identifier le regime d'acces.
5. Proposer une fonction directrice candidate.
6. Tester si cette fonction devient famille fonctionnelle.
7. Tester si la fonction est irreductible au rang 0.
8. Tester si la fonction est irreductible a un role contextuel.
9. Tester si une liaison stabilisee est vraiment necessaire.
10. Identifier les roles contextuels.
11. Verifier les dependances de modele et d'acces.
12. Tester l'existence d'une architecture.
13. Appliquer le test de retrait.
14. Decrire la trajectoire de stabilisation.
15. Nommer les limites.
```

Sorties possibles :

```text
classement confirme,
classement confirme avec role contextuel,
classement conserve sous audit,
classement deplace vers rang 0,
classement deplace vers role contextuel,
classement deplace vers architecture,
classement refuse,
dossier a produire avant decision.
```

### 16. Decisions stabilisees par la v1.2

La v1.2 stabilise les decisions suivantes.

```text
1. Les cinq familles fonctionnelles Couplage, Echelle, Raccordement, Orientation et Convention sont fortes.
2. La liaison stabilisee est conservee seulement comme famille fonctionnelle faible sous audit.
3. Seuil, Borne, Validite, Dephasage et Hierarchie sont des roles contextuels, non des familles fonctionnelles.
4. Fond, Parametre d'etat, Densite normalisee, Equation d'etat, Condition initiale et Observable reconstruite sont des roles architecturaux.
5. Saveur-Higgs, SI, effective basse energie et cosmologie sont des architectures, non des familles fonctionnelles.
6. Une architecture doit etre decrite comme reseau de dependances.
7. La temporalite est une trajectoire de stabilisation, non une famille fonctionnelle.
8. Une tension de donnees appartient d'abord au regime d'acces.
9. Toute nouvelle fiche doit appliquer le criblage avant consolidation.
```

### 17. Carte active du corpus apres v1.2

Methode active :

```text
01_CADRE_METHODOLOGIQUE/Note_synthese_methodologique_v1_3_pre_familial_et_temporalite.md
```

Protocole actif :

```text
01_CADRE_METHODOLOGIQUE/Matrice_criblage_taxonomique_v0_1.md
01_CADRE_METHODOLOGIQUE/Workflow_GitHub_v0_1.md
```

Carte de reference active :

```text
05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_2_refonte.md
```

Carte historique recente :

```text
05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_1.md
```

Carte de dependances active :

```text
05_CARTES_ET_SYNTHESES/Carte_dependances_architectures_v0_1.md
```

Architectures actives :

```text
04_ARCHITECTURES_INTER_FAMILLES/Architecture_saveur_Higgs_notes.md
04_ARCHITECTURES_INTER_FAMILLES/Architecture_metrologique_SI_notes.md
04_ARCHITECTURES_INTER_FAMILLES/Architecture_effective_basse_energie_notes.md
04_ARCHITECTURES_INTER_FAMILLES/Architecture_cosmologique_notes.md
04_ARCHITECTURES_INTER_FAMILLES/Architecture_cosmologique_stress_test_v0_1.md
```

Cycles physiques actifs :

```text
02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/Synthese_cycle_saveur_Higgs_v0_1.md
02_CYCLES_PHYSIQUES/06_Cycle_effectif_basse_energie/Synthese_cycle_effectif_basse_energie_v0_1.md
02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Synthese_cycle_cosmologique_v0_1.md
02_CYCLES_PHYSIQUES/08_Cycle_metrologique_SI/Cycle_metrologique_SI_v0_1_c_h_e.md
```

### 18. Points ouverts apres v1.2

La v1.2 ne ferme pas le projet.

Elle ouvre des chantiers plus nets.

| Chantier | Document | Statut |
|---|---|---|
| Stress test cosmologique | `04_ARCHITECTURES_INTER_FAMILLES/Architecture_cosmologique_stress_test_v0_1.md` | Produit |
| Plan de reprise du cycle cosmologique | `02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Plan_reprise_cycle_cosmologique_v0_1.md` | Produit |
| Reprise des cycles physiques | `02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/` + cycles 06, 07, 08 | Produite sur branche |
| Audit de resynchronisation theorique | `05_CARTES_ET_SYNTHESES/Audit_resynchronisation_theorique_v0_1.md` | Produit |
| Application de la matrice aux fiches sensibles | `01_CADRE_METHODOLOGIQUE/Application_matrice_fiches_sensibles_v0_1.md` | Produit |
| Fiche prudente masse absolue neutrino | `02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/Fiche_masse_absolue_neutrinos_v0_1.md` | Produit |
| Matrice temporelle autonome | `01_CADRE_METHODOLOGIQUE/Matrice_temporelle_v0_1.md` | Produit |
| Application temporelle aux fiches sensibles | `01_CADRE_METHODOLOGIQUE/Application_matrice_temporelle_fiches_sensibles_v0_1.md` | Produit |
| Reecriture positive du vocabulaire actif | `01_CADRE_METHODOLOGIQUE/Reecriture_positive_vocabulaire_v0_1.md` | Cercle 1 produit puis corrige ; cercle 2 a ouvrir |
| Remontee des sources DOCX primaires | `05_CARTES_ET_SYNTHESES/Plan_remontee_sources_docx_markdown_v0_1.md` + `05_CARTES_ET_SYNTHESES/Table_remontee_sources_docx_v0_1.md` | Table produite avant conversion |
| Workflow GitHub provisoire | `01_CADRE_METHODOLOGIQUE/Workflow_GitHub_v0_1.md` + `README.md` | Produit |
| Normalisation physique des archives | Seulement apres remontee Markdown et table de correspondance | Plus tard |

Decision :

```text
la prochaine etape logique porte sur la qualite du vocabulaire actif
et sur les roles stabilises.
```

Elle peut etre :

```text
soit la table de remontee des sources DOCX primaires,
soit la reecriture positive du cercle 2 des architectures actives apres lecture des sources utiles,
soit des addenda locaux si l'application de la matrice revele un conflit dans une fiche source,
soit une carte consolidee superieure si les nouvelles couches doivent etre stabilisees ensemble,
soit la normalisation physique des archives apres remontee et verification.
```

### 19. Documents integres

Documents methodologiques :

```text
01_CADRE_METHODOLOGIQUE/Note_synthese_methodologique_v1_1.md
01_CADRE_METHODOLOGIQUE/Note_synthese_methodologique_v1_2.md
01_CADRE_METHODOLOGIQUE/Revision_de_fond_v0_1_temporalite.md
01_CADRE_METHODOLOGIQUE/Fiche_criblage_critiques_v0_1.md
01_CADRE_METHODOLOGIQUE/Note_synthese_methodologique_v1_3_pre_familial_et_temporalite.md
01_CADRE_METHODOLOGIQUE/Matrice_criblage_taxonomique_v0_1.md
01_CADRE_METHODOLOGIQUE/Matrice_temporelle_v0_1.md
01_CADRE_METHODOLOGIQUE/Application_matrice_temporelle_fiches_sensibles_v0_1.md
01_CADRE_METHODOLOGIQUE/Reecriture_positive_vocabulaire_v0_1.md
01_CADRE_METHODOLOGIQUE/Workflow_GitHub_v0_1.md
```

Cartes et syntheses :

```text
05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_1.md
05_CARTES_ET_SYNTHESES/Synthese_architectures_inter_familles_v1_0.md
05_CARTES_ET_SYNTHESES/Carte_dependances_architectures_v0_1.md
05_CARTES_ET_SYNTHESES/Index_raisonne_du_corpus_v1_0.md
```

Architectures :

```text
04_ARCHITECTURES_INTER_FAMILLES/Architecture_saveur_Higgs_notes.md
04_ARCHITECTURES_INTER_FAMILLES/Architecture_metrologique_SI_notes.md
04_ARCHITECTURES_INTER_FAMILLES/Architecture_effective_basse_energie_notes.md
04_ARCHITECTURES_INTER_FAMILLES/Architecture_cosmologique_notes.md
04_ARCHITECTURES_INTER_FAMILLES/Architecture_cosmologique_stress_test_v0_1.md
```

Cycle cosmologique :

```text
02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Synthese_cycle_cosmologique_v0_1.md
02_CYCLES_PHYSIQUES/07_Cycle_cosmologique/Plan_reprise_cycle_cosmologique_v0_1.md
```

Cycles physiques synchronises :

```text
02_CYCLES_PHYSIQUES/05_Cycle_saveur_Higgs/Synthese_cycle_saveur_Higgs_v0_1.md
02_CYCLES_PHYSIQUES/06_Cycle_effectif_basse_energie/Synthese_cycle_effectif_basse_energie_v0_1.md
02_CYCLES_PHYSIQUES/08_Cycle_metrologique_SI/Cycle_metrologique_SI_v0_1_c_h_e.md
```

### 20. Formule de cloture

La v1.2 peut etre resumee par une correction d'ordre.

Formule :

```text
ne pas classer d'abord ;
stabiliser d'abord la forme, le regime, l'acces, le role,
le reseau et la trajectoire.
```

Formule finale :

> Une carte consolidee robuste ne juxtapose pas des constantes ; elle montre comment des formes stabilisees deviennent fonctions, comment des fonctions prennent role, comment des roles deviennent reseaux, et comment ces reseaux se stabilisent dans le temps.
