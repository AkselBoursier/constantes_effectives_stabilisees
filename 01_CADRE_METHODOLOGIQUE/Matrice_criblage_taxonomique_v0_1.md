# Matrice de criblage taxonomique v0.1

## Protocole d'application de la methode v1.3

### 1. Fonction du document

Cette matrice transforme la note methodologique v1.3 en protocole de travail.

Elle sert a tester :

```text
une grandeur physique,
une fonction directrice candidate,
un role contextuel,
une architecture inter-fonctions,
ou une tension de classement.
```

Elle ne remplace pas :

```text
01_CADRE_METHODOLOGIQUE/Note_synthese_methodologique_v1_3_pre_familial_et_temporalite.md
01_CADRE_METHODOLOGIQUE/Matrice_temporelle_v0_1.md
```

Elle en donne l'ordre d'application.

Regle directrice :

```text
ne pas demander d'abord quelle fonction directrice attribuer a une grandeur ;
demander d'abord quelle forme stabilisee elle prend,
dans quel regime elle opere,
par quel acces elle est connue,
et quelle trajectoire elle suit.
```

### 2. Probleme vise

La methode anterieure risquait parfois de transformer des categories commodes en fonctions directrices trop vite.

Trois risques sont particulierement vises :

```text
liaison non qualifiee prise pour tiroir fourre-tout,
fonction contextuelle prise pour fonction directrice,
architecture prise pour niveau de solidarite englobant.
```

La matrice v0.1 impose donc un criblage par rangs.

### 3. Les six rangs a parcourir

| Rang | Niveau | Question |
|---|---|---|
| 0 | Forme logique de stabilisation | Quelle forme est stabilisee avant tout classement fonctionnel ? |
| 1 | Fonction directrice | Que fait principalement la grandeur ? |
| 2 | Role contextuel | Quel role prend-elle dans ce regime ou cette architecture ? |
| 3 | Axes physique / acces | Ou opere-t-elle et comment est-elle connue ? |
| 4 | Architecture / reseau | Entre-t-elle dans une solidarite de fonctions ? |
| 5 | Temporalite / trajectoire | Comment son statut s'installe, varie ou se reconstruit ? |

Ordre obligatoire :

```text
forme -> fonction -> role -> acces -> architecture -> trajectoire.
```

### 4. Matrice minimale

| Champ | Question | Sortie attendue |
|---|---|---|
| Grandeur | De quoi parle-t-on exactement ? | Nom, symbole, domaine |
| Forme logique | Quelle forme est stabilisee ? | Valeur, rapport, ecart, matrice, phase, loi d'etat, borne, observable |
| Fonction directrice candidate | Quelle fonction principale semble dominante ? | Couplage, Echelle, Raccordement, Orientation, Convention, liaison qualifiee sous audit |
| Test de fonction directrice | La fonction est-elle irreductible au rang 0 ou au role ? | Confirmee, qualifiee, deplacee, refusee |
| Role contextuel | Quel role local ou architectural prend la grandeur ? | Seuil, borne, fond, etat, validite, hierarchie, observable, condition initiale |
| Portee du role | Ou ce role vaut-il ? | Locale, transversale, architecturale, documentaire |
| Regime physique | Dans quel domaine la grandeur opere-t-elle ? | Electromagnetique, QCD, electrofaible, gravitationnel, cosmologique, SI |
| Regime d'acces | Comment la grandeur est-elle connue ? | Direct, reconstruit, combine, conventionnel, modele-dependant |
| Couplage modele-acces | Quel modele conditionne l'acces ? | Faible, explicite, fort, dominant |
| Robustesse de l'acces | L'acces est-il stable ? | Robuste, fragile, tendu, conventionnel, combine |
| Manifestation phenomenologique | Comment le role apparait-il physiquement ? | Spectrale, transitionnelle, oscillatoire, dynamique, operationnelle |
| Trajectoire de stabilisation | Comment le statut evolue-t-il ? | Convergence, divergence, reconstruction, absorption conventionnelle, blocage |
| Tension eventuelle | Quelle tension doit etre documentee ? | Locale, inter-acces, persistante, modele-dependante, candidate a rupture |
| Architecture eventuelle | Quelle solidarite de fonctions est impliquee ? | Aucune, locale, confirmee, sous stress test |
| Test de retrait | Que perd-on si la grandeur est retiree ? | Role isole, articulation, domaine, architecture |
| Limite | Ce que le classement ne dit pas | Limite physique, epistemique ou documentaire |

### 5. Test de resistance d'une fonction directrice

Une fonction directrice candidate ne doit etre conservee que si elle resiste aux questions suivantes.

| Question | Si oui | Si non |
|---|---|---|
| La grandeur a-t-elle une fonction principale claire ? | Continuer le test | Ne pas consolider le classement fonctionnel |
| Cette fonction est-elle plus qu'une forme logique ? | Fonction candidate possible | Revenir au rang 0 |
| Cette fonction est-elle plus qu'un role contextuel ? | Fonction candidate possible | Deplacer en role |
| Cette fonction reste-t-elle lisible hors d'une architecture particuliere ? | Fonction robuste possible | Role architectural ou architecture |
| Le retrait de cette fonction casse-t-il l'analyse locale ? | Fonction confirmee ou qualifiee | Etiquette faible ou refusee |

Sorties possibles :

```text
fonction robuste
fonction conservee mais qualifiee
fonction faible sous audit
role contextuel
forme logique seulement
architecture ou sous-architecture
classement refuse
```

### 6. Test special des liaisons stabilisees

La liaison stabilisee est une fonction faible sous audit.

Elle ne doit pas etre utilisee par defaut.

Questions obligatoires :

| Question | Effet |
|---|---|
| La liaison est-elle la fonction principale, ou seulement la forme logique ? | Si forme logique seulement, revenir au rang 0 |
| La grandeur peut-elle etre mieux decrite comme Couplage, Echelle, Raccordement, Orientation ou Convention ? | Si oui, reclasser |
| La liaison est-elle un role d'etat, une normalisation, une composition ou une observable reconstruite ? | Si oui, passer en role contextuel |
| Le cas exige-t-il une architecture pour etre compris ? | Si oui, traiter l'architecture avant la fonction directrice |
| Que perd-on si l'etiquette de liaison disparait ? | Si presque rien, la fonction de liaison est refusee |

Decisions possibles :

| Ancien usage de liaison | Decision v1.3 |
|---|---|
| Rapport pur | Rang 0 : rapport, puis fonction a tester |
| Equation d'etat | Role contextuel d'etat |
| Composition metrologique | Convention + role compositionnel |
| Liaison constitutive Saveur-Higgs | Architecture constitutive a expliciter |
| Normalisation cosmologique | Role contextuel de densite normalisee |

Formule :

```text
La fonction de liaison ne devient acceptable que si elle explique la fonction,
pas seulement la forme de l'ecriture.
```

### 7. Test de role contextuel

Un role contextuel n'est pas une fonction directrice.

Il decrit la fonction prise par une grandeur dans une situation donnee.

| Role | Question | Portee typique |
|---|---|---|
| Seuil | Marque-t-il une transition ou une limite d'activation ? | Locale ou transversale |
| Borne | Fixe-t-il une limite inferieure, superieure ou effective ? | Locale ou transversale |
| Validite | Delimite-t-il un domaine de description ? | Transversale ou architecturale |
| Hierarchie | Organise-t-il des ordres de grandeur ? | Transversale |
| Fond | Structure-t-il l'etat global d'un modele ? | Architecturale |
| Parametre d'etat | Decrit-il un etat de regime ? | Architecturale |
| Densite normalisee | Normalise-t-il une composante dans un budget global ? | Architecturale |
| Condition initiale | Fixe-t-il un etat de depart ou un spectre initial ? | Architecturale |
| Observable reconstruite | Est-il infere par un reseau modele-donnees ? | Architecturale |

Regle :

```text
le role peut etre indispensable sans devenir une fonction directrice.
```

### 8. Test d'architecture

Une architecture n'est pas un grand theme.

C'est une solidarite de fonctions dans un regime donne.

Questions de stress test :

| Question | Critere |
|---|---|
| Plusieurs fonctions ou roles sont-ils solidaires ? | Il faut plus qu'une simple liste |
| Le retrait d'un element modifie-t-il la configuration globale ? | Sinon, pas d'architecture |
| Le regime physique est-il explicite ? | Sinon, architecture trop vague |
| Le regime d'acces est-il explicite ? | Sinon, risque de tableau descriptif |
| Le couplage modele-acces est-il documente ? | Obligatoire pour cosmologie et reconstructions |
| La temporalite est-elle identifiable ? | Constitution, validite, convention, reconstruction ou tension |
| La structure resiste-t-elle a un contre-classement par fonction simple ? | Sinon, revenir au rang 1 ou 2 |

Sorties possibles :

```text
architecture confirmee
architecture confirmee mais a documenter
sous-architecture candidate
configuration locale
reseau de dependance a expliciter
architecture refusee
```

### 9. Couplage modele-acces

Le regime d'acces n'est jamais neutre quand une grandeur est reconstruite.

| Type | Description | Risque |
|---|---|---|
| Direct | Mesure ou acces proche de l'operation definissante | Surestimer l'independance |
| Operationnel | Acces par procedure stabilisee | Confondre procedure et essence physique |
| Reconstruit | Acces par chaine d'inference | Effacer la dependance au modele |
| Combine | Plusieurs acces ou donnees sont agreges | Masquer les tensions inter-acces |
| Conventionnel | Valeur fixee par definition | Confondre exactitude numerique et role physique |
| Modele-dependant fort | Le modele conditionne fortement la valeur extraite | Naturaliser un parametre reconstruit |

Question minimale :

```text
la grandeur est-elle stabilisee par la physique seule,
par l'acces,
par le modele,
ou par leur couplage ?
```

### 10. Trajectoires de stabilisation

La temporalite n'est pas une fonction directrice.

Elle decrit la trajectoire du statut.

| Trajectoire | Sens |
|---|---|
| Convergence empirique | Les acces convergent vers un statut robuste |
| Divergence inter-acces | Les acces restent incompatibles ou tendus |
| Stabilisation bornee | Le statut vaut dans un domaine limite |
| Reconstruction modele-dependante | La valeur depend d'un modele d'inference |
| Absorption conventionnelle | La valeur numerique est fixee par convention |
| Blocage par degenerescence | Plusieurs interpretations restent possibles |
| Tension candidate | La tension peut signaler une rupture ou une limite |

Regle :

```text
une trajectoire peut etre physique,
epistemique,
documentaire,
ou mixte.
```

Pour les cas ou le rang 5 devient structurant, utiliser le protocole autonome :

```text
01_CADRE_METHODOLOGIQUE/Matrice_temporelle_v0_1.md
```

### 11. Niveaux de tension

Une tension n'est pas automatiquement une anomalie.

Elle doit etre qualifiee.

| Niveau | Description | Action |
|---|---|---|
| Locale | Desaccord dans un cas limite | Documenter |
| Inter-acces | Desaccord entre routes d'acces | Comparer les regimes d'acces |
| Persistante | Tension stable malgre les corrections | Ajouter stress test |
| Modele-dependante | Tension sensible aux hypotheses | Expliciter le modele |
| Candidate a rupture | Tension possiblement structurante | Ne pas trancher sans dossier propre |

### 12. Formulaire court pour une fiche

```text
Grandeur :
Regime physique :
Regime d'acces :

Rang 0 - forme logique :
Rang 1 - fonction directrice candidate :
Test de resistance de fonction :
Rang 2 - role contextuel :
Portee du role :
Rang 3 - couplage modele-acces :
Robustesse de l'acces :
Rang 4 - architecture eventuelle :
Stress test d'architecture :
Rang 5 - trajectoire de stabilisation :
Tension eventuelle :

Test de retrait :
Decision de classement :
Limite conservee :
```

### 13. Mini-tests indicatifs

Ces exemples servent seulement a montrer le type de sortie attendu.

| Cas | Criblage attendu |
|---|---|
| `m_f = y_f v / sqrt(2)` | Composition constitutive ; architecture Saveur-Higgs a documenter avant de conclure a une fonction de liaison |
| `k_B` dans le SI | Convention definissante + role thermodynamique conserve ; exactitude numerique n'epuise pas la fonction |
| `H_0` | Parametre d'etat actuel, acces fortement modele-donnees, trajectoire avec tensions inter-acces |
| `sigma_8 / S_8` | Observable reconstruite, tension d'acces, stress test cosmologique requis |
| `Delta m^2` | Ecart spectral et dephasage oscillatoire ; tester Orientation, Echelle ou role de phase avant fonction de liaison |

### 14. Decisions normalisees

Chaque criblage doit finir par une decision courte.

Formats recommandes :

```text
classement confirme
classement confirme avec role contextuel explicite
classement conserve sous audit
classement deplace vers rang 0
classement deplace vers role contextuel
classement deplace vers architecture
classement refuse
dossier a produire avant decision
```

### 15. Usage dans le corpus

Cette matrice doit etre utilisee avant :

```text
une nouvelle fonction directrice,
une requalification des liaisons stabilisees,
une nouvelle carte consolidee,
un stress test cosmologique,
ou une note d'architecture manquante.
```

Elle doit aussi accompagner les futurs cas litigieux.

### 16. Formule de cloture

La matrice de criblage ne sert pas a multiplier les cases.

Elle sert a empecher qu'une case apparaisse trop tot.

Formule finale :

> Un classement robuste commence par retarder le classement : forme, fonction, role, acces, architecture et trajectoire doivent etre distingues avant toute consolidation.
