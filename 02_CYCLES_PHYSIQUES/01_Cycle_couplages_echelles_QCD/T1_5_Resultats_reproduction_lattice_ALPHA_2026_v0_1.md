# T1.5 — Reproduction du pipeline d'analyse ALPHA 2026 depuis les produits condensés v0.1

## 0. Statut

```text
statut : reproduction du pipeline d'analyse à partir des produits condensés fournis ;
date : 21 juillet 2026 ;
étape : jalon T1.5 clos dans le périmètre annoncé par le paquet ;
fonction : contrôler séparément les deux routes, leur combinaison et le transport
           vers alpha_s^(5)(m_Z) ;
ne vaut pas : nouvelle simulation lattice, nouvelle mesure, audit indépendant de
              b_g, validation générale de toutes les entrées condensées ou verdict T1.
```

Le paquet, son empreinte, son statut de licence générale non établi et son
environnement sont décrits dans le
[manifeste local](T1_5_Manifeste_local_paquet_ALPHA_2026_v0_1.md). Le
[rapport historique de blocage](T1_5_Rapport_blocage_reproduction_lattice_ALPHA_2026_v0_1.md)
reste inchangé et conserve l'état antérieur à l'acquisition locale.

## 1. Périmètre effectivement exécuté

Les opérations suivantes ont été exécutées, dans une copie ignorée par Git :

1. instanciation du manifeste Julia 1.11.5 dans un dépôt isolé ;
2. contrôle minimal `nf0_parameters.jl` : chargement des dépendances, lecture BDIO,
   impression des paramètres `N_f=0` et de leur covariance ;
3. `scale.jl` : fixation de `sqrt(t_0)`, `sqrt(t_0^*)` et `mu_ref` ;
4. `running_le.jl` : ajustement du step scaling GF et détermination de `mu_had`,
   `mu_dec` et `mu_0` ;
5. `lam_nf3.jl` : route directe en QCD à trois saveurs ;
6. `lam_dec.jl` : route par quarks lourds fictifs et découplage ;
7. `alphas.jl` : combinaison corrélée, raccordements `N_f=3 -> 4 -> 5` et budget
   d'erreur de `alpha_s^(5)(m_Z)`.

Le périmètre se sépare explicitement ainsi :

```text
reproduit : traitement des produits condensés fournis ;
            détermination d'échelle et running de basse énergie couverts par le paquet ;
            route directe ;
            route découplage ;
            combinaison corrélée ;
            raccordement perturbatif jusqu'à cinq saveurs ;
            budget final fourni par le pipeline ;
non reproduit : génération des configurations lattice ;
                calcul initial de b_g ;
                running Schrödinger fonctionnel depuis les configurations brutes ;
                calculs amont à zéro saveur ;
                production indépendante des données condensées.
```

Les commandes scientifiques, lancées depuis `main/`, sont :

```powershell
<julia-1.11.5>\bin\julia.exe --startup-file=no nf0_parameters.jl
<julia-1.11.5>\bin\julia.exe --startup-file=no scale.jl
<julia-1.11.5>\bin\julia.exe --startup-file=no running_le.jl
<julia-1.11.5>\bin\julia.exe --startup-file=no lam_nf3.jl
<julia-1.11.5>\bin\julia.exe --startup-file=no lam_dec.jl
<julia-1.11.5>\bin\julia.exe --startup-file=no alphas.jl
```

Pour chaque commande, `JULIA_DEPOT_PATH` pointait vers le dépôt isolé et
`JULIA_PKG_PRECOMPILE_AUTO=0` désactivait la précompilation automatique déclenchée
par le gestionnaire de paquets. Le manifeste fourni n'a pas été modifié.

Les sorties BDIO produites sont locales et non versionnées :

| Fichier | Taille | SHA-256 |
|---|---:|---|
| `muref_t0.bdio` | 5 235 octets | `ea431165eebd81ae64c97bc105af80fa45b1383da6195a3c0f59886eed581472` |
| `mu_le.bdio` | 24 223 octets | `9f1577f6d9f632b5e8990dc4cf2dcafb1e169d708c30164eb2033464f2a603b5` |
| `lam3_nf3.bdio` | 11 794 octets | `ac0df362f032e03992146cae710fefa6227cb2cccd191e2956b6a761ec8fc980` |
| `lam3_dec.bdio` | 18 498 octets | `37f3d6d8e473d6be4ddac4a821b86c7f1f5c55f0b1ec3f22631924b02701d8e0` |
| `lambdas_alphas.bdio` | 76 810 octets | `1fd07cda2c40312a56ce7c84981c1d04cdc4f15711c827ed4b9a6a8968657ea0` |

### 1.1 Incident d'environnement résolu

Une première extraction de la distribution Julia a été interrompue par le délai du
terminal après contrôle réussi du ZIP. L'exécutable existait, mais le fichier standard
`share/julia/test/testhelpers/FakePTYs.jl` manquait ; la précompilation de `REPL`, puis
de `Plots`, a donc échoué. L'archive officielle, dont l'empreinte était correcte, a été
réextraite intégralement. Le même contrôle minimal a ensuite réussi sans modification
du paquet ALPHA ni de son manifeste.

Deux avertissements GKS sur des plugins graphiques sont apparus pendant la
précompilation de `Plots`. Aucun script exécuté n'a demandé de rendu graphique et ces
avertissements n'ont affecté ni les lectures BDIO ni les sorties numériques.

## 2. R1 — Contrôle minimal

```text
instanciation du manifeste : réussie ;
quatre dépendances IFIC : acquises aux arbres verrouillés ;
chargement ADerrors / BDIO / ALPHAio / Utils : réussi ;
lecture de nf0_parameters.bdio : réussie ;
covariance N_f=0 : produite ;
test ou suite d'exemples dédiée : absente du paquet.
```

R1 établit l'exécutabilité de la pile et la lecture du format BDIO. Il ne vérifie pas
l'origine des valeurs `N_f=0` déjà réduites.

## 3. Fixation d'échelle et running basse énergie

| Sortie | Valeur reproduite |
|---|---:|
| `sqrt(t_0)` — valeur robuste employée | `0.143357 ± 0.0018 fm` |
| `sqrt(t_0^*)` | `0.14332 ± 0.0019 fm` |
| `mu_ref = 1/sqrt(8t_0^*)` | `486.717 ± 6.3 MeV` |
| `mu_had` | `200.625 ± 3.0 MeV` |
| `mu_dec` | `802.565 ± 14 MeV` |
| `mu_dec sqrt(t_0)` | `0.583138 ± 0.0071` |
| `mu_0` | `4385.1 ± 94 MeV` |

Les valeurs après `±` donnent l'incertitude totale affichée. La composante robuste sur
`sqrt(t_0)` est ajoutée après la moyenne pondérée de type Particle Data Group (PDG)
afin de couvrir la dispersion des déterminations.

`running_le.jl` lit 39 paires de couplages sur `L/a = 8, 12, 16, 20, 24, 32`, ajuste
une représentation de la fonction bêta avec extrapolation au continuum et compare le
fit complet au sous-ensemble `L/a > 8` :

```text
facteur central mu_dec/mu_had : 4.00032 ;
variante L/a > 8 : 4.02117 ;
systématique de continuum ajoutée : 0.0208495.
```

Le paquet réajuste cette partie basse énergie en schéma de flot de gradient (GF). La
continuation haute énergie en schéma Schrödinger fonctionnel (SF) n'est pas recomputée
depuis les configurations : son résultat condensé entre par `L0xLam3.bdio`.

## 4. R2 — Route directe en QCD à trois saveurs

```text
Lambda_MSbar^(3) / mu_dec = 0.432536 ± 0.011 (total) ;
Lambda_MSbar^(3)          = 347.139 ± 11 MeV.
```

Pour la valeur dimensionnée, le paquet affiche `8.8 MeV` statistiques, `5.6 MeV`
systématiques, `4.0 MeV` robustes et `11 MeV` au total.

La route directe est reproduite au niveau prévu par le paquet : fixation d'échelle,
running GF basse énergie et propagation de l'entrée haute énergie distribuée. Elle
n'est pas une nouvelle exécution des simulations `N_f=3` ni une reconstruction
complète du running SF à partir des configurations.

## 5. R3 — Route de découplage

Le script ajuste les couplages massifs réduits pour :

```text
z = M / mu_dec : 4, 6, 8, 10, 12 ;
coupe centrale : aM <= 0.4, soit (aM)^2 <= 0.16 ;
extrapolation de masse : termes en 1/z^2, avec variantes en puissances de alpha(M) ;
limite finale : M -> infini après extrapolation au continuum.
```

Les masses invariantes par renormalisation reproduites vont de
`3210.26 ± 56 MeV` pour `z=4` à `9630.78 ± 170 MeV` pour `z=12`. Les couplages
continus obtenus comprennent `g_GFT^2 = 5.2579 ± 0.0276` à `z=4` et
`5.7800 ± 0.0507` à `z=12`.

```text
Lambda_MSbar^(3) / mu_dec = 0.426380 ± 0.010 (total) ;
systématique des variantes continuum et M -> infini = 0.00152887 ;
Lambda_MSbar^(3) = 342.198 ± 10 MeV.
```

Pour la valeur dimensionnée, le paquet affiche `8.7 MeV` statistiques, `3.8 MeV`
systématiques, `4.0 MeV` robustes et `10 MeV` au total.

Le coefficient d'amélioration `b_g` n'est ni recalculé ni varié dans les scripts du
paquet réduit. Son rôle est en amont : les données massives distribuées sont déjà
préparées pour l'analyse améliorée qui supprime les effets linéaires dominants en
`aM`. La présente reproduction contrôle les extrapolations à partir de ces données,
pas la détermination non perturbative indépendante de `b_g`.

Les paramètres de théorie de jauge pure et leur covariance sont lus dans
`nf0_parameters.bdio`. Leur usage et leur propagation sont exécutés ; leur calcul
lattice amont n'est pas refait.

## 6. R4 — Combinaison et transport vers `m_Z`

### 6.1 Corrélations et combinaison

Pour les deux estimations dimensionnées de `Lambda_MSbar^(3)`, le paquet reproduit :

```text
Var(route directe)       = 124.739988 MeV^2 ;
Var(route découplage)    = 105.042023 MeV^2 ;
Cov(directe, découplage) = 37.833305 MeV^2 ;
corrélation de Pearson   = 0.330514 ;
chi^2 de l'ajustement à une constante = 0.158409 pour <chi^2> proche de 1.
```

La combinaison est donc corrélée. L'accord des valeurs ne vaut pas indépendance
statistique. Les entrées communes comprennent la fixation de l'échelle, `mu_dec` et
les sources propagées par les objets `ADerrors`.

```text
Lambda_MSbar^(3) combiné = 344.352 ± 8.7 MeV.
```

### 6.2 Matching des saveurs lourdes

```text
m_c = 1275 ± 5 MeV ;
m_b = 4171 ± 20 MeV ;
m_Z = 91187.6 ± 2.1 MeV.
```

Le code utilise la fonction bêta `MS-bar` avec cinq coefficients et les coefficients
de découplage `gdecMS` jusqu'au terme `gdecMS4` pour `N_f=3 -> 4` puis `4 -> 5`.
L'incertitude de troncature est estimée par la différence entre `nl=5` et `nl=4`.
Cette convention correspond à la fonction bêta à cinq boucles et au raccordement
incluant quatre corrections au-delà du terme arbre.

| Sortie | Valeur reproduite |
|---|---:|
| `Lambda_MSbar^(3)` | `344.352 ± 8.7 MeV` |
| `Lambda_MSbar^(4)` | `301.538 ± 8.7 MeV` |
| `Lambda_MSbar^(5)` | `217.585 ± 7.0 MeV` |
| `alpha_s^(5)(m_Z)` | `0.118755 ± 0.00058` |

Le commentaire d'en-tête de `alphas.jl` annonce `results/alphas.bdio`, tandis que le
code écrit effectivement `results/lambdas_alphas.bdio`. Cette divergence de nom est
documentaire et n'affecte pas la sortie.

## 7. Budget d'erreur final

Les pourcentages suivants sont des parts de variance de `alpha_s^(5)(m_Z)` imprimées
par le paquet :

| Famille | Part de variance |
|---|---:|
| route découplage — total | 28.79 % |
| route directe `N_f=3` — total | 18.78 % |
| sources communes — total | 52.42 % |
| statistique totale | 57.74 % |
| systématique totale | 19.22 % |
| robuste `t_0` | 20.88 % |
| perturbatif total | 2.09 % |
| entrées FLAG/PDG `m_c`, `m_b`, `m_Z` | 0.06 % |

Détail des parts perturbatives : `N_f=0` 0.55 %, `N_f=3` 0.45 %, ajout de charm et
bottom 1.09 %, rapports de Lambda arrondis à 0.00 %. La troncature perturbative est
donc sous-dominante dans le budget reproduit.

## 8. R5 — Comparaison aux valeurs publiées

| Sortie | Publiée | Reproduite | Écart absolu | Écart relatif | Écart / incertitude publiée | Niveau | Cause de l'écart |
|---|---:|---:|---:|---:|---:|---|---|
| route directe `Lambda_MSbar^(3)` | `347(11) MeV` | `347.139 ± 11 MeV` | `0.139 MeV` | `0.0401 %` | `0.0126` | reproduite à la précision d'affichage | chiffres supplémentaires imprimés par le paquet |
| route découplage `Lambda_MSbar^(3)` | `342(10) MeV` | `342.198 ± 10 MeV` | `0.198 MeV` | `0.0579 %` | `0.0198` | reproduite à la précision d'affichage | chiffres supplémentaires imprimés par le paquet |
| combinaison `Lambda_MSbar^(3)` | `344.4(8.7) MeV` | `344.352 ± 8.7 MeV` | `0.048 MeV` | `0.0139 %` | `0.00552` | reproduite à la précision d'affichage | arrondi à une décimale dans la publication |
| `alpha_s^(5)(m_Z)` | `0.11876(58)` | `0.118755 ± 0.00058` | `0.000005` | `0.00421 %` | `0.00862` | reproduite à la précision d'affichage | arrondi au cinquième chiffre décimal |

Les rapports sont explicitement `abs(347.139 - 347) / 11 = 0.0126`,
`abs(342.198 - 342) / 10 = 0.0198`,
`abs(344.352 - 344.4) / 8.7 = 0.00552` et
`abs(0.118755 - 0.11876) / 0.00058 = 0.00862`.

Les rapports à l'incertitude publiée ne sont donnés que comme contrôle d'arrondi :
les valeurs reproduites et publiées ne sont pas des estimations indépendantes. Ils ne
constituent donc ni un test de tension ni une mesure de compatibilité statistique.
Les décimales supplémentaires des valeurs reproduites proviennent de la sortie
computationnelle et ne représentent pas une précision physique supérieure à
l'incertitude publiée. Les sorties reproduisent les valeurs publiées à leur précision
d'affichage.

## 9. Porteurs, transformations et chemins

```text
porteurs : couplages de volume fini, relations de running, Lambda_MSbar^(3),
           raccordements entre nombres de saveurs et alpha_s^(5)(m_Z) ;
transformations : limite du continuum a -> 0, changement de volume et d'échelle,
                  M -> infini, changement de schéma et raccordement N_f ;
régime et échelle : QCD à trois saveurs aux échelles non perturbatives du paquet,
                    haute énergie condensée, seuils charm/bottom et m_Z ;
tolérance : incertitudes statistiques, systématiques, robustes et perturbatives,
            avec résultat final 0.00058 sur alpha_s ;
dimension objet : structure RG, Lambda_MSbar et couplage dans le schéma déclaré ;
dimension accès : observables BDIO réduites, ajustements, extrapolations et échelle ;
dimension constitution : dynamique QCD, continuum et secteurs à N_f distincts ;
chemin computationnel : scripts Julia, fits GF, continuum et limite M -> infini ;
chemin inférentiel : propagation ADerrors, variantes systématiques et fit corrélé ;
choix de schéma : GF, SF et MS-bar ;
raccordement : N_f = 0, 3, 4 et 5 ;
fixation d'échelle : sqrt(t_0), mu_ref, mu_had, mu_dec et mu_0 ;
évolution du groupe de renormalisation : relation d'échelle, non histoire temporelle ;
portée physique : détermination et transport dans les régimes déclarés ;
portée épistémologique : contrôlabilité de deux routes partiellement corrélées ;
portée ontologique : non engagée.
```

## 10. Statut final et limites positives

```text
T1.5 : clos au périmètre du paquet de réplication fondé sur les données réduites ;
pipeline d'analyse à partir des produits condensés : reproduit ;
simulations lattice amont : non reproduites, hors du paquet réduit ;
production indépendante des données condensées : non reproduite ;
commit du paquet : non établi ;
b_g et entrées condensées : utilisés en aval, non audités indépendamment ;
T1.6 et T1.7 : non ouverts par le seul présent résultat.
```

La limite sur les simulations amont borne positivement l'acquis : l'exécution remplit
la fonction déclarée de reproduction du pipeline d'analyse à partir des produits
condensés fournis. La prochaine opération recevable est une revue humaine de ce
jalon, avant toute classification T1.6, modification de la matrice T1.4 ou propagation
dans la synthèse du cycle.
