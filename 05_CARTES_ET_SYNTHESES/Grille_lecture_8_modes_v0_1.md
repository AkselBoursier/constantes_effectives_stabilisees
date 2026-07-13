# Grille de lecture des 8 modes de stabilisation v0.1

## Point d'entree pratique du corpus

### 1. Fonction de ce document

Cette grille est le point d'entree pratique pour lire n'importe quelle
grandeur du corpus.

Elle repond directement a la question directrice :

> Dans quelle mesure une grandeur peut-elle etre dite constante ?

Elle ne remplace pas les cycles physiques ni les architectures.

Elle donne l'ordre de lecture avant de les consulter.

Procedure courte :

```text
1. Identifier le mode de stabilisation dominant.
2. Identifier le regime et l'acces.
3. Identifier l'architecture eventuelle.
4. Nommer la limite conservee.
```

---

### 2. Les 8 modes de stabilisation

#### Mode 1 — Valeur mesuree ou ajustee

```text
Quoi : une valeur robuste etablie par mesure directe ou ajustement global.
Quand : la grandeur converge vers une valeur stable dans un regime.
Prudence : le schema et le contexte experimental font partie du statut.
```

Exemples : masses de fermions, `M_W`, `Lambda_QCD`

---

#### Mode 2 — Couplage courant ou situe

```text
Quoi : une intensite de couplage qui depend d'une echelle ou d'un schema.
Quand : la grandeur n'a pas de valeur absolue ; elle a une trajectoire de flot.
Prudence : ne pas figer la valeur hors de son echelle de definition.
```

Exemples : `alpha_s(Q^2)`, `alpha_G(E)`, couplages de Yukawa

---

#### Mode 3 — Composition exacte

```text
Quoi : une grandeur derivee qui herite de l'exactitude d'une definition.
Quand : la valeur est calculable exactement a partir de valeurs definissantes.
Prudence : distinguer exactitude de la composition et role physique propre.
```

Exemples : `R = N_A k_B`, `K_J = 2e/h`, `R_K = h/e^2`

---

#### Mode 4 — Convention definissante

```text
Quoi : une valeur fixee par convention pour definir une unite.
Quand : la valeur numerique est exacte par decision metrologique.
Prudence : l'exactitude conventionnelle n'epuise pas le role physique.
```

Exemples : `k_B`, `N_A`, `c`, `h`, `e` (SI 2019)

---

#### Mode 5 — Orientation

```text
Quoi : une relation entre bases ou secteurs stabilisee par la structure du modele.
Quand : la grandeur encode une rotation, une diagonalisation ou un melange.
Prudence : l'orientation ne se reduit pas a un rapport numerique.
```

Exemples : matrice CKM, matrice PMNS (angles de melange)

---

#### Mode 6 — Validite limitee

```text
Quoi : une grandeur qui vaut dans un domaine de description determine.
Quand : la description est robuste dans ce domaine, incomplete ou absente ailleurs.
Prudence : ne pas etendre la valeur hors de son domaine de validite.
```

Exemples : `G_F` (theorie de Fermi), `M_W` comme seuil, gravitation effective

---

#### Mode 7 — Inference reconstruite

```text
Quoi : une grandeur stabilisee par chaine d'inference modele-donnees.
Quand : l'acces est indirect, le modele conditionne la valeur extraite.
Prudence : dependance au modele et tensions inter-acces doivent rester visibles.
```

Exemples : `H_0` (selon acces), `sigma_8`, `S_8`, `A_s`, `n_s`

---

#### Mode 8 — Borne ou contrainte

```text
Quoi : une limite qui remplace une mesure positive directe.
Quand : la valeur n'est pas mesuree directement, mais un domaine est exclu.
Prudence : ne pas transformer une borne en mesure positive.
```

Exemples : masse absolue des neutrinos, tensions cosmologiques comme bornes

---

### 3. Table de correspondance mode / architecture

Les modes ne sont pas independants des architectures.

| Architecture | Modes dominants | Ce qui les relie |
|---|---|---|
| Saveur-Higgs | Valeur ajustee, Composition exacte, Orientation | Constitution apres brisure electrofaible |
| Metrologique SI | Convention definissante, Composition exacte | Definitions SI 2019 et realisations pratiques |
| Effective basse energie | Validite limitee, Couplage courant | Domaine, raccordement, echelle effective |
| Cosmologique | Inference reconstruite, Borne | Modele Lambda-CDM, acces pluriels, tensions |

Un mode peut apparaitre dans plusieurs architectures.

Une architecture peut impliquer plusieurs modes.

---

### 4. Roles contextuels associes

Certaines grandeurs prennent un role dans un contexte donne.

| Role | Sens | Quand l'utiliser |
|---|---|---|
| Seuil | Marque une transition ou une limite d'activation | Quand la grandeur separe deux regimes |
| Fond | Structure le cadre global d'un modele | Quand la grandeur est un parametre d'arriere-plan |
| Relation | Encode une liaison qualifiee entre secteurs | Apres test de non-reduction au mode 3 ou 5 |

Ces roles sont secondaires par rapport aux modes.

Ils precisent la fonction locale d'une grandeur sans creer de nouvelle categorie.

---

### 5. Formulaire court

Pour toute grandeur, remplir ce formulaire avant de consulter les documents detailles.

```text
Grandeur :
Regime physique :
Regime d'acces :

Mode de stabilisation dominant : (1 a 8)
Mode secondaire eventuel :

Architecture concernee : (Saveur-Higgs / SI / Effective / Cosmologique / aucune)
Role contextuel eventuel : (Seuil / Fond / Relation / aucun)

Limite conservee :
```

---

### 6. Exemples rapides

| Grandeur | Mode dominant | Architecture | Limite |
|---|---|---|---|
| `k_B` | 4 Convention definissante | Metrologique SI | Role thermodynamique distinct de la valeur exacte |
| `alpha_s(M_Z)` | 2 Couplage courant | Effective basse energie | Flot perturbatif, seuils de saveur |
| `R = N_A k_B` | 3 Composition exacte | Metrologique SI | Realisation experimentale distincte |
| CKM | 5 Orientation | Saveur-Higgs | Origine des textures non expliquee |
| `G_F` | 6 Validite limitee | Effective basse energie | Hors validite au-dessus de `M_W` |
| `H_0` | 7 Inference reconstruite | Cosmologique | Tension inter-acces persistante |
| masse absolue neutrino | 8 Borne | Saveur-Higgs / Cosmologique | Interface oscillatoire / cosmologique sous prudence |
| `M_W` | 1 Valeur mesuree | Saveur-Higgs + Effective | Seuil de validite Fermi, precision electrofaible |

---

### 7. Ce que cette grille ne remplace pas

```text
- les fiches de cycle pour le contenu physique detaille ;
- les notes d'architecture pour les solidarites entre grandeurs ;
- la Carte consolidee v1.3 pour la vue d'ensemble theorique ;
- la procedure courte post-v1.3 pour les cas litigieux.
```

---

### 8. Documents lies

```text
Point d'entree :
05_CARTES_ET_SYNTHESES/Grille_lecture_8_modes_v0_1.md  <- ce document

Vue d'ensemble :
05_CARTES_ET_SYNTHESES/Carte_consolidee_v1_3_post_cercle2.md

Procedure courte :
01_CADRE_METHODOLOGIQUE/Note_methodologique_courte_post_v1_3.md

Architectures detaillees :
04_ARCHITECTURES/Cercle2_architectures_actives_v0_1.md

Audit taxonomique :
05_CARTES_ET_SYNTHESES/Audit_taxonomie_v0_1.md
```
