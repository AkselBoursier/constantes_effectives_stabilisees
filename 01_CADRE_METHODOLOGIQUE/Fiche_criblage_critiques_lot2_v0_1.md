# Fiche de criblage des critiques lot 2 v0.1

## Extraction, recoupement et transformation prudente des cinq nouvelles critiques

### 1. Fonction de la fiche

Cette fiche traite les cinq nouvelles critiques du dossier :

```text
90_Critiques_ constantes_effectives_stabilisees/
```

Elle prolonge :

```text
01_CADRE_METHODOLOGIQUE/Fiche_criblage_critiques_v0_1.md
01_CADRE_METHODOLOGIQUE/Matrice_criblage_taxonomique_v0_1.md
01_CADRE_METHODOLOGIQUE/Matrice_temporelle_v0_1.md
05_CARTES_ET_SYNTHESES/Carte_dependances_architectures_v0_1.md
```

Regle de lecture :

```text
prendre chaque objection au serieux ;
extraire aussi les propositions trop fortes ;
retenir les micro-suggestions discretes ;
transformer les formulations risquees en contraintes testables.
```

Cette fiche ne decide pas encore les modifications du corpus.

Elle produit une extraction articulee et une liste de chantiers.

### 2. Corpus critique lu

Documents sources :

```text
Architecture_fonctionnelle_des_constantes_physiques-Summary.docx
Le_statut_ontologique_des_constantes_physiques-Summary.docx
Mathematiser_la_classification_des_constantes_physiques-Summary.docx
Restructurer_la_matrice_des_constantes_physiques-Summary.docx
Transformer_les_tensions_en_anomalies_cosmologiques-Summary.docx
```

Ces cinq documents ont un profil commun :

```text
moins de dialogue diffus ;
plus de synthese operatoire ;
plus de propositions directes ;
plus de risque de formulations trop fortes.
```

### 3. Resultat central

Les cinq critiques convergent vers un meme diagnostic :

```text
le corpus a gagne en prudence,
mais cette prudence peut devenir neutralisante si elle ne produit pas
de seuils, de tests dynamiques et de procedures de bascule.
```

La cible principale n'est donc pas la taxonomie seule.

La cible est :

```text
la procedure de decision.
```

### 4. Methode de criblage

Chaque critique est lue selon cinq filtres.

| Filtre | Question |
|---|---|
| Objection | Quel probleme est signale ? |
| Proposition | Quelle solution brute est proposee ? |
| Micro-suggestion | Quelle idee discrete peut etre extraite ? |
| Remaniement | Quelle version prudente est compatible avec le corpus ? |
| Chantier | Quelle piece active pourrait recevoir cette idee ? |

Statuts utilises :

| Statut | Sens |
|---|---|
| A integrer | Compatible avec le corpus et deja assez stabilise |
| A remanier | Idee feconde mais formulation excessive |
| A tester | Hypothese interessante demandant un cas d'epreuve |
| A tenir en reserve | Idee prematuree mais a ne pas perdre |
| A refuser comme telle | Proposition trop forte, tout en gardant le probleme signale |

### 5. Critique 1 : architecture fonctionnelle des constantes

Source :

```text
Architecture_fonctionnelle_des_constantes_physiques-Summary.docx
```

Objections principales :

| Objection | Extraction |
|---|---|
| Frontiere transversal / architectural | Borne, validite, fond et parametre d'etat peuvent se superposer sans regle de priorite |
| Tensions cosmologiques | `H_0` et `S_8` restent trop souvent des diagnostics passifs |
| Observables reconstruites | Pour `S_8`, regime physique et regime d'acces sont fortement couples |
| Temporalites | Les temporalites sont juxtaposees sans ordre genetique explicite |

Propositions brutes :

```text
axe Z orthogonal pour les fonctions transversales ;
priorite de la borne jusqu'a convergence empirique ;
tensions comme poutres porteuses ou ressorts entre sous-reseaux ;
derogation pour les observables reconstruites ;
indicateur de couplage fort ;
filtre genetique et champs de dependance temporelle.
```

Extraction utile :

```text
une fonction transversale ne doit pas etre noyee dans le reseau local ;
une tension persistante doit avoir une fonction structurante ;
une observable reconstruite peut demander un marquage de couplage fort ;
une temporalite doit indiquer ses dependances amont.
```

Remaniement prudent :

```text
ne pas ajouter un axe Z comme jargon graphique obligatoire ;
introduire plutot un champ "contrainte transversale active".
```

Statut :

```text
A integrer pour le champ de contrainte transversale.
A tester pour l'indicateur de couplage fort.
A remanier pour la representation par ressorts ou poutres.
```

Micro-suggestions a conserver :

```text
demander pour chaque proposition : critere d'activation, cas test,
effet attendu, sortie documentaire.
```

### 6. Critique 2 : statut ontologique des constantes

Source :

```text
Le_statut_ontologique_des_constantes_physiques-Summary.docx
```

Objections principales :

| Objection | Extraction |
|---|---|
| Separation regime / acces | Pour certaines constantes effectives, l'acces ne revele pas seulement l'objet : il participe a sa definition effective |
| Tensions cosmologiques | Les tensions persistantes sont trop protegees de toute portee physique possible |
| Test de retrait | Le test binaire de retrait ne decrit pas la degradation progressive d'un regime |

Propositions brutes :

```text
zone de couplage ontologique ;
statut ontologique provisoire des tensions ;
test de destabilisation genetique ;
gradient physique de dissolution.
```

Extraction utile :

```text
le corpus doit distinguer separation methodologique et decouplage reel ;
une tension persistante peut avoir un statut heuristique sans etre
naturalisee ;
un seuil physique se teste souvent par degradation progressive,
pas seulement par retrait logique.
```

Remaniement prudent :

```text
remplacer "zone de couplage ontologique" par "couplage fort regime-acces" ;
remplacer "statut ontologique provisoire" par "statut heuristique probatoire" ;
ajouter au test de retrait un test de degradation ou de substitution.
```

Statut :

```text
A integrer pour le couplage fort regime-acces.
A remanier pour le statut des tensions.
A tester pour le test de degradation genetique.
```

Micro-suggestions a conserver :

```text
`alpha_s` : le schema d'extraction appartient au regime effectif ;
`G_F` : la masse du W borne le domaine de validite ;
seuil electrofaible et QCD demandent des gradients plutot que de
simples retraits.
```

### 7. Critique 3 : mathematiser la classification

Source :

```text
Mathematiser_la_classification_des_constantes_physiques-Summary.docx
```

Objections principales :

| Objection | Extraction |
|---|---|
| Formalisme insuffisant | La distinction famille / architecture peut rester editoriale |
| Cosmologie | Les crises `H_0` et `S_8` peuvent etre maintenues trop longtemps comme tensions d'acces |
| Matrice non decisionnelle | La matrice decrit beaucoup mais tranche peu les conflits de criteres |
| Reproductibilite | Deux lecteurs peuvent classer differemment un cas limite |

Propositions brutes :

```text
theorie des graphes ;
matrices de dependance fonctionnelle ;
seuil d'architecture par retrait de trois noeuds ;
points de rupture cosmologiques ;
arbre booleen hierarchise ;
verrouillages et exclusions mutuelles ;
protocole de fracture.
```

Extraction utile :

```text
la matrice doit reduire l'arbitraire des cas litigieux ;
les architectures doivent recevoir des criteres de dependance plus
explicites ;
les tensions cosmologiques demandent des seuils de bascule documentes ;
la reproductibilite devient un critere de qualite methodologique.
```

Remaniement prudent :

```text
ne pas transformer tout le corpus en algorithme ;
introduire une couche decisionnelle pour les cas de conflit.
```

Statut :

```text
A tester pour la matrice de dependance en graphe.
A remanier pour le seuil "trois noeuds".
A integrer pour les verrouillages d'options incompatibles.
```

Micro-suggestions a conserver :

```text
si la variable d'evolution est une echelle dynamique `Q`,
la lecture conventionnelle doit etre verrouillee ;
si la fonction est "fond", la relation locale doit passer un test
restrictif avant d'etre promue ;
produire trois cas worked-out.
```

### 8. Critique 4 : restructurer la matrice

Source :

```text
Restructurer_la_matrice_des_constantes_physiques-Summary.docx
```

Objections principales :

| Objection | Extraction |
|---|---|
| Biais d'ancrage | Placer la famille fonctionnelle trop tot force le lecteur a classer avant d'analyser |
| Cas limites | `H_0` et masse de Planck demandent un protocole d'escalade |
| Temporalite unique | Le temps physique de constitution et le temps epistemique d'acces sont melanges |
| Neutrinos | La masse absolue neutrino montre que l'acces et l'architecture doivent preceder la sortie taxonomique |

Propositions brutes :

```text
deplacer la famille fonctionnelle en sortie finale ;
protocole d'escalade statistique et conceptuel ;
scinder la temporalite en deux matrices orthogonales ;
produire un cas d'usage traversant.
```

Extraction utile :

```text
la classification doit etre une decision de sortie ;
les tensions et limites conceptuelles doivent avoir des paliers ;
la temporalite du monde et la temporalite de l'acces ne doivent pas
etre confondues.
```

Remaniement prudent :

```text
le corpus a deja subordonne la famille ;
il faut maintenant rendre cette subordination procedurale dans les
gabarits de fiche.
```

Statut :

```text
A integrer pour la classification en sortie.
A tester pour les deux matrices temporelles.
A remanier pour les seuils statistiques universels.
```

Micro-suggestions a conserver :

```text
un protocole d'escalade peut avoir un volet statistique et un volet
conceptuel ;
la masse de Planck demande des declencheurs conceptuels, pas seulement
des seuils sigma ;
la masse absolue des neutrinos est un bon cas traversant.
```

### 9. Critique 5 : tensions en anomalies cosmologiques

Source :

```text
Transformer_les_tensions_en_anomalies_cosmologiques-Summary.docx
```

Objections principales :

| Objection | Extraction |
|---|---|
| Tensions neutralisees | `H_0` et `S_8` perdent leur portee heuristique si elles restent de simples divergences |
| Test de retrait tautologique | Retirer `Lambda` de LambdaCDM prouve peu de choses sur la resilience du cadre |
| Sous-reseaux trop propres | Les degenerescences inter-reseaux sont moins visibles que les compartiments |
| Puissance predictive | La carte doit devenir un laboratoire de substitution, pas seulement une exposition |

Propositions brutes :

```text
passerelle d'escalade tension -> anomalie candidate ;
point de bascule theorique ;
test de substitution ;
`Lambda` -> quintessence ;
`w` -> `w0-wa` ;
matrice de degenerescence inter-reseaux.
```

Extraction utile :

```text
une tension persistante doit pouvoir declencher un protocole ;
le test de retrait doit etre complete par un test de substitution ;
la cosmologie demande une carte des degenerescences :
`A_s` / `sigma_8`, `w` / `Omega_k`, neutrinos / croissance.
```

Remaniement prudent :

```text
ne pas promouvoir automatiquement une tension en anomalie ;
definir un statut intermediaire :
point de bascule theorique a examiner.
```

Statut :

```text
A integrer pour le test de substitution comme complement.
A tester pour la matrice de degenerescence cosmologique.
A remanier pour les seuils d'escalade quantitatifs.
```

Micro-suggestions a conserver :

```text
`S_8` : exigence de plusieurs sondes independantes avant bascule ;
`w` variable : tester les effets de cascade sur les observables tardives ;
neutrinos massifs : expliciter leur effet sur la croissance ;
porosite `w` / `Omega_k` : a inscrire dans la carte cosmologique.
```

### 10. Convergences fortes du lot 2

| Convergence | Documents sources | Forme recuperable |
|---|---|---|
| Classification en sortie | Restructurer, Mathematiser | Le rang taxonomique doit etre conclusion, pas point de depart |
| Couplage fort regime-acces | Architecture fonctionnelle, Statut ontologique | Ajouter un indicateur de couplage fort sans fusion ontologique generale |
| Tensions comme objets de protocole | Architecture fonctionnelle, Statut ontologique, Mathematiser, Transformer tensions | Creer une passerelle prudente : divergence -> tension persistante -> point de bascule |
| Test dynamique | Statut ontologique, Transformer tensions | Ajouter degradation et substitution au test de retrait |
| Temporalite scindee | Architecture fonctionnelle, Restructurer | Distinguer constitution physique et acces epistemique |
| Formalisation prudente | Mathematiser, Restructurer | Reduire l'arbitraire par verrous, arbres de decision et cas worked-out |
| Degenerescences cosmologiques | Transformer tensions, Architecture fonctionnelle, Mathematiser | Produire une matrice inter-reseaux cosmologique |

### 11. Points a ne pas adopter tels quels

| Proposition brute | Risque | Remaniement |
|---|---|---|
| Fusionner regime et acces | Perte de la distinction methodologique centrale | Couplage fort signale, local et argumente |
| Donner un statut ontologique provisoire aux tensions | Naturalisation prematuree | Statut heuristique probatoire |
| Seuil universel `>5 sigma` | Faux automatisme inter-domaines | Seuils par domaine, avec justification |
| Seuil "trois noeuds" pour architecture | Quantification arbitraire | Test de dependance explicite, pas seuil unique |
| Remplacer le test de retrait | Perte d'un acquis utile | Ajouter test de degradation et de substitution |
| Mathematisation totale | Transformation du corpus en machine trop rigide | Formalisation locale des cas litigieux |

### 12. Chantiers proposes

#### 12.1 Matrice v1.4 ou addendum v1.3

Objet :

```text
transformer la subordination de la famille en procedure visible.
```

Taches :

```text
mettre la sortie taxonomique en fin de fiche ;
ajouter un champ "contrainte transversale active" ;
ajouter un champ "couplage fort regime-acces" ;
ajouter des verrous d'options incompatibles.
```

#### 12.2 Passerelle d'escalade des tensions

Objet :

```text
ne plus laisser les tensions en simple statut passif.
```

Taches :

```text
divergence d'acces ;
tension persistante ;
point de bascule theorique ;
ouverture conditionnelle d'un test de substitution.
```

#### 12.3 Test de retrait elargi

Objet :

```text
garder le test de retrait,
mais lui ajouter deux epreuves.
```

Epreuves :

```text
test de degradation : comment un regime se dissout progressivement ;
test de substitution : que devient le reseau avec une alternative controlee.
```

#### 12.4 Matrice temporelle v0.2

Objet :

```text
separer la constitution physique et l'acces epistemique.
```

Taches :

```text
matrice de constitution : seuils, regimes, transitions physiques ;
matrice d'acces : mesures, conventions, institutions, reconstructions ;
cas traversant : masse absolue des neutrinos ou seuil electrofaible.
```

#### 12.5 Addendum cosmologique de degenerescences

Objet :

```text
cartographier les dependances inter-reseaux qui rendent les tensions
methodologiquement actives.
```

Cas minimaux :

```text
`A_s` / `sigma_8` ;
`S_8` / lensing / croissance ;
`w` / `Omega_k` / CMB ;
masse des neutrinos / croissance tardive ;
`Lambda` / quintessence ;
`w` constant / `w0-wa`.
```

### 13. Matrice enrichie issue du lot 2

Champs a ajouter ou expliciter dans les prochaines fiches sensibles :

| Champ | Question |
|---|---|
| Sortie taxonomique | Quelle classification reste apres analyse des regimes, acces, architecture et temporalite ? |
| Contrainte transversale active | Une borne, validite ou limite prime-t-elle localement sur la fonction locale ? |
| Couplage fort regime-acces | Le mode d'acces participe-t-il a la definition effective de la grandeur ? |
| Degre de tension | Divergence simple, tension persistante, point de bascule, anomalie candidate ? |
| Test de degradation | Comment le regime se dissout-il quand le seuil ou l'echelle varie ? |
| Test de substitution | Quelle alternative controlee remplace le noeud ou le modele teste ? |
| Dependances temporelles | Quelles dependances de constitution et d'acces doivent etre ordonnees ? |
| Verrous d'options | Quelles classifications deviennent incompatibles apres certains diagnostics ? |

### 14. Decision de criblage

Decision :

```text
le lot 2 ne demande pas une nouvelle taxonomie.
```

Il demande :

```text
une couche decisionnelle plus explicite.
```

Formule :

```text
la prudence du corpus doit produire des seuils d'action,
pas seulement des reserves.
```

### 15. Suite logique

Ordre recommande :

```text
1. produire un addendum court a la matrice de criblage ;
2. ouvrir une matrice temporelle v0.2 scindee ;
3. produire une passerelle d'escalade des tensions cosmologiques ;
4. tester le dispositif sur un cas traversant ;
5. seulement ensuite modifier la carte consolidee.
```

Cas traversants possibles :

```text
masse absolue des neutrinos ;
`S_8` ;
seuil electrofaible ;
`G_F` ;
echelle de Planck.
```

### 16. Formule de cloture

Les cinq critiques sont plus directives que le premier lot.

Leur force doit etre filtree.

Mais leur apport principal est robuste :

```text
un cadre prudent reste fecond s'il sait dire quand une reserve devient
un test, quand une tension devient un signal, et quand une classification
peut enfin etre prononcee.
```
