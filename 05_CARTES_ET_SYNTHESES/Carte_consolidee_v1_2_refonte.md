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
avant rang pre-familial,
avant refonte de Relation,
avant roles contextuels,
avant representation des architectures comme reseaux.
```

La modification principale est :

```text
la carte n'est plus d'abord un tableau de familles ;
elle devient une grammaire de stabilisation par rangs, roles, acces,
architectures et trajectoires.
```

### 2. Definition consolidee v1.2

Definition de reference :

> Une constante effective stabilisee est une grandeur dont une valeur, une forme, une relation, un role ou une dependance devient robuste dans un regime donne, selon un acces determine, avec un mode et une trajectoire de stabilisation explicites, sans que cette robustesse implique necessairement une constance absolue, une universalite hors contexte ou un statut fondamental.

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
avant de classer une grandeur dans une famille,
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
| Point de depart | Familles superieures | Rang pre-familial puis familles |
| Relation | Famille ordinaire mais surveillee | Famille faible sous audit |
| Fonctions transversales | Niveau secondaire | Roles contextuels avec portee |
| Fonctions architecturales | Niveau distinct | Roles contextuels architecturaux |
| Architecture | Niveau inter-familles reconnu | Reseau de dependances soumis a stress test |
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
| 1 | Famille fonctionnelle | Que fait principalement la grandeur ? |
| 2 | Role contextuel | Quel role prend-elle dans un regime, un acces ou une architecture ? |
| 3 | Axes physique / acces | Ou opere-t-elle et comment est-elle connue ? |
| 4 | Architecture / reseau | Quelles fonctions deviennent solidaires ? |
| 5 | Temporalite / trajectoire | Comment son statut s'installe, varie, persiste ou se reconstruit ? |

Ordre obligatoire :

```text
forme -> famille -> role -> acces -> architecture -> trajectoire.
```

### 5. Rang 0 : formes logiques

Le rang 0 evite de transformer trop vite une forme d'ecriture en famille.

| Forme logique | Question | Exemples |
|---|---|---|
| Valeur | Une valeur robuste est-elle stabilisee ? | masse, echelle, constante definissante |
| Rapport | Un quotient est-il stabilise ? | m_p / m_e, Omega_i |
| Ecart | Un ecart spectral ou de regime est-il stabilise ? | Delta m^2 |
| Composition | Une grandeur est-elle composee d'autres grandeurs ? | R, K_J, R_K |
| Relation d'etat | Une loi entre variables d'etat est-elle stabilisee ? | w |
| Fonction d'echelle | Une dependance en echelle est-elle stabilisee ? | alpha_s(Q^2), alpha_G(E) |
| Matrice | Une structure matricielle est-elle stabilisee ? | CKM, PMNS, Yukawa |
| Phase | Une orientation complexe est-elle stabilisee ? | delta_CP, phases CKM |
| Observable reconstruite | Une grandeur est-elle inferee par modele et donnees ? | sigma_8, S_8 |
| Condition initiale | Une donnee initiale de scenario est-elle stabilisee ? | A_s, n_s |
| Convention definissante | Une valeur est-elle fixee par definition ? | k_B, N_A, c, h, e |
| Borne | Un domaine ou une limite est-il stabilise ? | masse absolue neutrino |

Regle :

```text
une relation d'ecriture n'impose pas la famille Relation.
```

### 6. Rang 1 : familles fonctionnelles

La v1.2 conserve cinq familles fortes et une famille faible sous audit.

| Famille | Statut v1.2 | Fonction principale | Exemples |
|---|---|---|---|
| Couplage | Forte | Parametrer une intensite d'interaction ou de liaison | alpha, alpha_s(Q^2), alpha_G(E), Y_f |
| Echelle | Forte | Fixer ou reveler un ordre de grandeur structurant | v, M_W, Lambda_QCD, M_Pl |
| Raccordement | Forte | Relier deux descriptions, niveaux ou regimes | G_F |
| Orientation | Forte | Stabiliser un desalignement entre bases, champs ou secteurs | theta_W, CKM, PMNS, delta_CP |
| Convention | Forte | Recevoir une valeur exacte dans un systeme de definition | k_B, N_A, c, h, e |
| Relation | Faible sous audit | Stabiliser une liaison irreductible entre grandeurs | Cas a justifier un par un |

Decision :

```text
Relation n'est plus une famille par defaut.
```

Elle ne peut etre conservee que si la liaison est vraiment la fonction principale et ne se reduit pas a :

```text
une forme logique,
un role contextuel,
une normalisation,
une composition,
ou une architecture.
```

### 7. Re-traitement de Relation

| Cas | Ancienne tentation | Lecture v1.2 |
|---|---|---|
| `m_f = y_f v / sqrt(2)` | Relation constitutive | Architecture Saveur-Higgs |
| `R = N_A k_B` | Relation exacte | Architecture SI + composition exacte |
| `K_J = 2 e / h` | Relation exacte | Architecture SI + realisation electrique |
| `R_K = h / e^2` | Relation exacte | Architecture SI + realisation electrique |
| `Omega_i = rho_i / rho_crit` | Rapport relationnel | Densite normalisee cosmologique |
| `w = p / rho` | Relation | Role contextuel d'etat |
| `Delta m^2` | Relation spectrale | Ecart spectral + dephasage oscillatoire |

Formule :

```text
Relation cesse d'etre une case ;
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
| Relation d'etat | Decrit-il le comportement d'une composante ? | Architecturale |
| Condition initiale | Fixe-t-il un etat ou spectre initial ? | Architecturale |
| Observable reconstruite | Est-il infere par un reseau modele-donnees ? | Architecturale |

Regle :

```text
un role peut etre indispensable sans devenir une famille.
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
une architecture inter-familles n'est pas une famille superieure.
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

La temporalite n'est pas une famille.

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
une tension de donnees n'est pas une famille.
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
| Famille candidate | Quelle fonction principale semble dominante ? |
| Test de famille | La famille resiste-t-elle au criblage ? |
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
5. Proposer une famille candidate.
6. Tester si la famille est irreductible au rang 0.
7. Tester si la famille est irreductible a un role contextuel.
8. Tester si Relation est vraiment necessaire.
9. Identifier les roles contextuels.
10. Verifier les dependances de modele et d'acces.
11. Tester l'existence d'une architecture.
12. Appliquer le test de retrait.
13. Decrire la trajectoire de stabilisation.
14. Nommer les limites.
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
1. Les cinq familles Couplage, Echelle, Raccordement, Orientation et Convention sont fortes.
2. Relation est conservee seulement comme famille faible sous audit.
3. Seuil, Borne, Validite, Dephasage et Hierarchie sont des roles contextuels, non des familles.
4. Fond, Parametre d'etat, Densite normalisee, Relation d'etat, Condition initiale et Observable reconstruite sont des roles architecturaux.
5. Saveur-Higgs, SI, effective basse energie et cosmologie sont des architectures, non des familles.
6. Une architecture doit etre decrite comme reseau de dependances.
7. La temporalite est une trajectoire de stabilisation, non une famille.
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

### 18. Points ouverts apres v1.2

La v1.2 ne ferme pas le projet.

Elle ouvre des chantiers plus nets.

| Chantier | Document | Statut |
|---|---|---|
| Stress test cosmologique | `04_ARCHITECTURES_INTER_FAMILLES/Architecture_cosmologique_stress_test_v0_1.md` | Produit |
| Application de la matrice aux fiches sensibles | Addenda ou revisions locales | Prochaine suite possible |
| Matrice temporelle autonome | `01_CADRE_METHODOLOGIQUE/Matrice_temporelle_v0_1.md` | Possible |
| Workflow GitHub provisoire | `01_CADRE_METHODOLOGIQUE/Workflow_GitHub_v0_1.md` + `README.md` | Produit |
| Normalisation physique des archives | Audit de dependances et table de correspondance | Plus tard |

Decision :

```text
la prochaine etape logique n'est pas une nouvelle famille.
```

Elle peut etre :

```text
soit l'application de la matrice v1.2 a quelques fiches sensibles,
soit une matrice temporelle autonome,
soit un addendum cosmologique par sous-reseaux.
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
