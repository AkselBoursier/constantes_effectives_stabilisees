# Passerelle d'escalade des tensions cosmologiques v0.1

## De la divergence d'acces au test de substitution

### 0. Statut documentaire

```text
statut : protocole actif ;
fonction : qualifier les tensions cosmologiques sans les convertir trop vite en anomalies ;
sources :
  01_CADRE_METHODOLOGIQUE/Fiche_criblage_critiques_lot2_v0_1.md ;
  01_CADRE_METHODOLOGIQUE/Addendum_matrice_criblage_lot2_v0_1.md ;
  01_CADRE_METHODOLOGIQUE/Matrice_temporelle_v0_2.md ;
  04_ARCHITECTURES/Architecture_cosmologique_stress_test_v0_1.md.
```

Cette passerelle ne tranche aucune tension cosmologique.

Elle fixe une procedure :

```text
divergence -> tension qualifiee -> stress test -> substitution controlee
-> dossier autonome eventuel.
```

### 1. Principe

Une tension cosmologique n'est pas :

```text
une famille taxonomique ;
une preuve de nouvelle physique ;
une erreur instrumentale par defaut ;
un verdict global contre une architecture.
```

Elle peut devenir :

```text
un signal methodologique actif.
```

Pour cela, elle doit passer des seuils d'escalade explicites.

### 2. Echelle d'escalade

| Niveau | Statut | Question | Action |
|---|---|---|---|
| 0 | Dispersion ordinaire | Les ecarts restent-ils compatibles avec les incertitudes et choix d'analyse ? | Documenter seulement |
| 1 | Divergence locale | Un acces ou une calibration produit-il un ecart local ? | Comparer la route d'acces |
| 2 | Tension inter-acces | Des routes independantes ou quasi independantes divergent-elles ? | Appliquer matrice temporelle v0.2 |
| 3 | Tension persistante | La divergence resiste-t-elle aux corrections usuelles ? | Ouvrir stress test de modele, acces et systematiques |
| 4 | Point de bascule candidat | Les hypotheses requises deviennent-elles incompatibles ou trop couteuses ? | Tester une substitution controlee |
| 5 | Anomalie candidate | Plusieurs substitutions echouent-elles tout en conservant le signal ? | Dossier autonome, sans conclusion prematuree |

Regle :

```text
le corpus peut monter d'un niveau ;
il ne doit pas sauter directement de tension a anomalie.
```

### 3. Conditions minimales avant escalade

Une tension ne monte pas de niveau sans controle de :

| Controle | Question |
|---|---|
| Routes d'acces | Quels acces produisent chaque valeur ? |
| Independance | Les routes partagent-elles donnees, calibrations, priors ou modele ? |
| Degenerescences | Quelles grandeurs peuvent compenser l'effet observe ? |
| Systematiques | Les corrections experimentales et astrophysiques sont-elles documentees ? |
| Modele | Le desaccord depend-il du modele de fond ? |
| Temporalite | La divergence porte-t-elle sur constitution physique ou acces epistemique ? |
| Substitution | Existe-t-il une alternative controlee a tester ? |

### 4. Matrice de degenerescences cosmologiques

| Tension ou zone | Noeuds impliques | Degenerescences typiques | Risque methodologique |
|---|---|---|---|
| `H_0` | Expansion actuelle, distance ladder, CMB, BAO, calibrations | `Omega_m`, `r_d`, calibration des distances, modele de fond | Lire une divergence d'acces comme variation de `H` |
| `S_8` | Croissance tardive, lensing, CMB, amas, `Omega_m` | `sigma_8`, `Omega_m`, biais, baryons, calibrations de masse | Transformer une coordonnee de degenerescence en constante |
| `w` / `Lambda` | Etat de composante, expansion, BAO, SNe, CMB | `Omega_k`, `H_0`, `Omega_m`, choix de parametrisation | Lire une extension phenomenologique comme microphysique |
| `A_s` / `sigma_8` | Primordial, CMB, croissance tardive | `tau`, croissance, neutrinos, modele de transfert | Identifier condition initiale et amplitude tardive |
| Masse des neutrinos | Spectre neutrino, croissance, CMB, beta, double beta | `Sigma_m_nu`, `A_s`, `H_0`, hierarchie, modele cosmologique | Fusionner bornes non equivalentes |

Cette matrice n'est pas un modele cosmologique.

Elle sert a empecher l'isolement premature d'une constante.

### 5. Test de degradation

Question :

```text
comment le signal change-t-il quand on relache progressivement un noeud,
un seuil, une calibration ou une hypothese de modele ?
```

Sorties possibles :

| Sortie | Interpretation |
|---|---|
| Degradation locale | Le signal depend surtout d'une route ou calibration |
| Degradation distribuee | Plusieurs noeuds contribuent sans point unique |
| Stabilite sous degradation | Le signal resiste aux relachements controles |
| Dissolution | La tension disparait quand une hypothese precise est modifiee |

### 6. Test de substitution

Question :

```text
quelle alternative controlee remplace le noeud ou le modele teste,
et que devient la tension ?
```

Exemples de substitutions prudentes :

| Zone | Substitution controlee |
|---|---|
| `H_0` | Changer calibration, route locale, ancre BAO, modele de fond |
| `S_8` | Changer sonde de croissance, traitement baryonique, covariance, definition `S_8` |
| `w` | Comparer `w = -1`, `w` constant, `w0-wa`, courbure libre |
| `A_s` / `sigma_8` | Tester `tau`, neutrinos, croissance tardive, transfert primordial-tardif |
| Masse neutrino | Comparer beta, double beta, cosmologie, hierarchie, sommes de masses |

La substitution ne prouve pas une these.

Elle mesure la dependance du signal a une architecture d'acces et de modele.

### 7. Sorties normalisees

Une fiche de tension doit finir par l'une des sorties suivantes :

```text
tension documentee sans escalade ;
tension inter-acces sous surveillance ;
tension persistante sous stress test ;
test de degradation requis ;
test de substitution ouvert ;
point de bascule candidat ;
dossier autonome requis ;
anomalie candidate non conclue.
```

### 8. Formulaire court

```text
Tension :
Grandeurs impliquees :
Sous-reseau cosmologique :

Routes d'acces :
Independance des routes :
Degenerescences :
Systematiques principales :
Modele de fond :

Niveau d'escalade :
Justification du niveau :
Test de degradation :
Test de substitution :

Sortie normalisee :
Limite conservee :
```

### 9. Effet sur les cartes

Cette passerelle ne modifie pas encore la carte consolidee.

Test traversant produit :

```text
03_TESTS_TAXONOMIQUES/Test_traversant_H0_passerelle_tensions_v0_1.md
```

La carte ne devra integrer une nouvelle formulation qu'apres verification sur un cas :

```text
H_0 ;
S_8 ;
masse absolue des neutrinos ;
ou raccord A_s / sigma_8.
```

### 10. Formule de cloture

```text
Une tension cosmologique devient utile quand elle cesse d'etre un mot de
prudence et devient une question d'escalade : quel acces diverge, quel
modele porte la divergence, quel noeud se degrade, quelle substitution
controlee reste possible ?
```
