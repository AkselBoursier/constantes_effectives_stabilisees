# S1 — Relation structurelle entre masse électronique, Yukawa électronique et échelle électrofaible v0.1

## 0. Statut

```text
statut : résultat scientifique local du lot Saveur–Higgs S1–S3 ;
date : 27 juillet 2026 ;
issue : #55 ;
bloc : S1 — relation structurelle ;
fonction : fixer la cible, les notations et les relations de passage
           entre masse physique de l’électron, paramètre de Yukawa,
           échelle électrofaible et interaction Higgs–électron ;
base interne : R1–R3 du dossier m_p/m_e, D6–D8,
               Dette_active_masse_electron_Yukawa_v0_1.md ;
ne vaut pas : mesure directe de y_e,
               instruction des accès expérimentaux S2,
               verdict final S3,
               traité général de renormalisation,
               explication de l’origine des Yukawa,
               réouverture du cycle 1,
               ni modification de la synthèse active Saveur–Higgs.
```

## 1. Question exacte de S1

> Que signifie exactement la relation `m_e = y_e v / sqrt(2)` selon que l’on parle de paramètres nus, de paramètres renormalisés ou de masse physique, et quelles conclusions cette relation autorise-t-elle avant toute comparaison expérimentale des accès ?

S1 ne demande pas encore combien vaut directement le couplage Higgs–électron ni quelle expérience le contraint le mieux. Il demande d’abord quels objets sont reliés et par quelle opération.

## 2. Verrouillage des notations

Le dossier distingue quatre cibles.

```text
M_e : masse physique ou masse on-shell de l’électron,
      engagée dans le réseau métrologique et dans le raccordement
      à un observable de masse ;

m_e^S(mu) : paramètre de masse renormalisé dans un schéma S
            et à une échelle mu ;

y_e^S(mu) : paramètre de Yukawa électronique renormalisé
            dans le même schéma et à la même échelle ;

v^S(mu) : paramètre d’échelle électrofaible renormalisé
          selon une définition déclarée ;

v_F : référence dérivée du couplage de Fermi,
      v_F = (sqrt(2) G_F)^(-1/2),
      utilisée comme paramètre d’entrée opérationnel de basse énergie ;

g_hee : coefficient physique ou effectif de l’interaction
        entre un boson de Higgs et une paire électron–positron,
        défini par l’amplitude ou la convention considérée.
```

Règle de notation : `m_e` sans indice ne doit être utilisé que lorsque le contexte rend impossible la confusion. Dans les relations de passage, S1 emploie `M_e` pour la masse physique et `m_e^S(mu)` pour un paramètre courant.

## 3. Quatre objets, quatre fonctions

| Objet | Fonction | Dépendance de schéma ou d’échelle | Accès principal à instruire |
|---|---|---:|---|
| `M_e` | masse physique de référence | non comme paramètre on-shell du raccordement perturbatif | métrologie et chaînes de masses |
| `m_e^S(mu)` | paramètre renormalisé | oui | calcul et conversion depuis `M_e` |
| `y_e^S(mu)` | coefficient de l’opérateur de Yukawa | oui | inférence dans un cadre ou contrainte d’amplitude |
| `v^S(mu)` | paramètre du secteur électrofaible brisé | oui selon définition et schéma | raccordement électrofaible |
| `v_F` | échelle dérivée de `G_F` | dépend du cadre lors du raccordement au Lagrangien | désintégration du muon et corrections électrofaibles |
| `g_hee` | interaction Higgs–électron dans une amplitude | dépend de la convention et du modèle | processus impliquant directement le Higgs |

Le premier résultat de S1 est donc négatif : **la présence d’une même lettre de masse dans plusieurs formules ne suffit pas à identifier un objet unique**.

## 4. Niveau nu — identité structurelle exacte

Dans le Modèle standard minimal, le terme de Yukawa électronique nu peut être écrit sous la forme :

```text
L_Y,e = - y_e,0  Lbar_e H e_R + h.c.
```

Après brisure électrofaible, en développant le doublet autour de sa valeur moyenne,

```text
H = (0, (v_0 + h_0)/sqrt(2))^T
```

on obtient deux termes issus du même opérateur :

```text
terme de masse :
  - (y_e,0 v_0 / sqrt(2)) ebar e ;

interaction avec un Higgs :
  - (y_e,0 / sqrt(2)) h_0 ebar e.
```

Il en résulte, au niveau des paramètres nus :

```text
m_e,0 = y_e,0 v_0 / sqrt(2) ;

g_hee,0 = y_e,0 / sqrt(2) = m_e,0 / v_0.
```

À ce niveau, la proportionnalité est une identité de construction du Lagrangien minimal après développement du champ. Elle ne constitue pas une mesure et n’explique pas la valeur numérique de `y_e,0`.

## 5. Niveau d’arbre renormalisé — relation de paramétrisation

À l’ordre d’arbre, dans une paramétrisation renormalisée déclarée, on écrit :

```text
m_e^S(mu) = y_e^S(mu) v^S(mu) / sqrt(2).
```

Cette relation signifie :

1. le paramètre de masse du fermion dans le régime brisé provient du produit du coefficient de Yukawa et du paramètre d’échelle du champ de Higgs ;
2. les trois quantités doivent appartenir au même cadre, au même schéma et au même point de définition ;
3. la relation ne détermine pas séparément `y_e` et `v` à partir de la seule existence de la masse ;
4. elle ne transforme pas automatiquement un paramètre du Lagrangien en observable directement mesuré.

Le terme « provient » est recevable ici au sens de **relation structurelle dans le Modèle standard minimal**. Il ne vaut pas comme explication de l’origine de la petite valeur du Yukawa électronique.

## 6. Niveau physique — raccordement corrigé

La masse physique `M_e` n’est pas identique sans qualification au paramètre renormalisé `m_e^S(mu)` ni au produit renormalisé `y_e^S(mu) v^S(mu) / sqrt(2)`.

La relation de passage possède la forme générique :

```text
M_e
=
[y_e^S(mu) v^S(mu) / sqrt(2)]
× [1 + Delta_e^S(mu)],
```

ou une forme algébriquement équivalente selon la convention choisie pour `Delta_e^S(mu)`.

`Delta_e^S(mu)` regroupe les corrections finies nécessaires pour raccorder les paramètres courants à la masse physique : auto-énergies, contre-termes, choix de schéma, choix de l’échelle et traitement cohérent du secteur électrofaible. La littérature calcule explicitement la relation entre masse au pôle d’un fermion et Yukawa courant dans le Modèle standard.

Le signe, la distribution et même la localisation de certaines contributions dépendent de la convention de raccordement. S1 ne promeut donc aucune écriture particulière de `Delta_e` comme identité universelle.

Verdict intermédiaire :

```text
m_e = y_e v / sqrt(2)

est :
  exacte pour les paramètres nus du modèle minimal après développement ;
  relation d’arbre pour des paramètres renormalisés cohérents ;
  insuffisante seule pour relier un Yukawa courant à M_e ;
  corrigée lors du raccordement à une masse physique.
```

## 7. Le rôle exact de `v`

### 7.1 `v` n’est pas un objet unique sans définition

Trois usages doivent être séparés :

```text
v_0 : valeur moyenne nue du champ dans le Lagrangien ;

v^S(mu) : paramètre renormalisé dans un schéma et à une échelle ;

v_F = (sqrt(2) G_F)^(-1/2) : échelle dérivée du couplage de Fermi.
```

À l’ordre d’arbre, ces usages sont souvent rapprochés et donnent l’échelle familière d’environ `246.22 GeV`. Au-delà de l’ordre d’arbre, leur raccordement mobilise les corrections électrofaibles à la désintégration du muon, traditionnellement organisées notamment par `Delta r`.

### 7.2 `G_F` fournit une ancre opérationnelle, pas une identité sans correction

`G_F` est extrait de la durée de vie du muon après séparation des corrections relevant de la théorie effective de Fermi. Dans le Modèle standard, le passage de cette grandeur à des paramètres électrofaibles dépend des corrections radiatives.

La bonne écriture méthodologique est donc :

```text
G_F
→ v_F comme échelle dérivée de basse énergie
→ raccordement à v^S(mu) dans un schéma électrofaible déclaré.
```

Il faut refuser :

```text
v_F = v^S(mu)
```

comme identité générale indépendante du schéma et de l’ordre perturbatif.

### 7.3 La renormalisation de `v` exige un traitement explicite

La renormalisation de la valeur moyenne du champ est liée au traitement des tadpoles et peut faire apparaître des dépendances de jauge ou de grandes corrections selon le schéma. Des propositions récentes introduisent précisément des schémas destinés à rendre ce raccordement à la fois indépendant de jauge et perturbativement stable.

S1 n’ouvre pas la comparaison complète de ces schémas. Il en conserve seulement la conséquence nécessaire : **un énoncé quantitatif sur `y_e` doit déclarer quelle définition de `v` il utilise**.

## 8. Ce que la précision de `M_e` permet à ce stade

La masse physique de l’électron est déterminée par le réseau CODATA à partir de chaînes métrologiques et d’un ajustement cohérent. R1 a déjà instruit ce statut ; S1 le réutilise par référence sans rouvrir la détermination complète.

En combinant illustrativement `M_e` avec `v_F` à l’ordre d’arbre, on obtient un Yukawa électronique d’ordre :

```text
y_e^(arbre, F) ≈ sqrt(2) M_e / v_F ≈ 2.94 × 10^(-6).
```

Cette valeur est une **inférence conditionnelle** :

```text
M_e mesurée
+ G_F mesuré
+ Modèle standard minimal
+ relation d’arbre
→ valeur de référence pour y_e.
```

Elle n’est pas :

```text
une observation directe du vertex H–e–e ;
une détermination indépendante de y_e et de v ;
une valeur sans schéma au-delà de l’ordre d’arbre ;
une explication de la hiérarchie des Yukawa.
```

La très faible incertitude relative de `M_e` ne se transfère donc pas mécaniquement à une mesure expérimentale directe de `g_hee`.

## 9. Pourquoi masse et interaction peuvent être découplées hors du modèle minimal

Dans le Modèle standard minimal, masse et couplage à un Higgs proviennent du même opérateur de dimension quatre. Cette corrélation peut être modifiée par des opérateurs de dimension supérieure.

Un exemple de la base de Varsovie est l’opérateur de type :

```text
O_eH = (H†H) (Lbar_e H e_R) + h.c.
```

Après brisure électrofaible, cet opérateur contribue à la masse électronique et au vertex à un Higgs avec des coefficients différents. Une mesure précise de `M_e` ne fixe alors pas à elle seule le couplage `H–e–e`.

Ce point ne prouve pas l’existence d’un tel opérateur. Il fixe la condition de portée de la relation minimale :

```text
proportionnalité masse–couplage du Higgs
=
conclusion du Modèle standard minimal à l’ordre déclaré,
non identité modèle-indépendante.
```

## 10. Matrice des relations admissibles

| Proposition | Statut S1 | Qualification |
|---|---|---|
| `m_e,0 = y_e,0 v_0 / sqrt(2)` | admise | identité au niveau nu dans le modèle minimal |
| `m_e^S(mu) = y_e^S(mu) v^S(mu) / sqrt(2)` | admise sous convention | relation de paramétrisation cohérente dans un schéma déclaré |
| `M_e = y_e^S(mu) v^S(mu) / sqrt(2)` sans correction | refusée comme relation générale | le raccordement physique exige des corrections |
| `v_F = (sqrt(2) G_F)^(-1/2)` | admise | définition d’une échelle dérivée de basse énergie |
| `v_F = v^S(mu)` sans qualification | refusée | corrections électrofaibles et schéma omis |
| précision de `M_e` = précision directe de `y_e` | refusée | inférence conditionnelle confondue avec un accès au vertex |
| `g_hee = M_e / v_F` modèle-indépendamment | refusée | valable seulement dans le modèle minimal et à l’ordre déclaré |
| `m_e = y_e v / sqrt(2)` explique la hiérarchie | refusée | la relation distribue l’échelle, elle ne fixe pas la valeur de `y_e` |
| opérateurs nouveaux peuvent décorréler masse et vertex | admise comme possibilité de modèle | ne constitue pas une détection de nouvelle physique |

## 11. Résultat local S1

### 11.1 Admission

```text
- le terme de Yukawa électronique produit, après brisure,
  un terme de masse et un vertex à un Higgs ;

- au niveau nu du Modèle standard minimal,
  m_e,0 = y_e,0 v_0 / sqrt(2) est une identité structurelle ;

- au niveau renormalisé, m_e^S(mu), y_e^S(mu) et v^S(mu)
  peuvent être reliés dans une paramétrisation cohérente ;

- la masse physique M_e exige un raccordement radiatif
  aux paramètres courants ;

- v_F fournit une ancre opérationnelle issue de G_F,
  mais ne s’identifie pas sans correction à tout v renormalisé ;

- la précision de M_e permet une inférence très précise de référence
  pour y_e dans le Modèle standard et sous conventions déclarées.
```

### 11.2 Refus

```text
- masse physique, masse courante, Yukawa et vertex direct
  comme objets expérimentalement équivalents ;

- m_e = y_e v / sqrt(2) sans déclaration du niveau,
  du schéma, de l’échelle et des corrections ;

- précision métrologique de M_e présentée comme mesure directe de y_e ;

- v présenté comme valeur unique indépendante du schéma
  au-delà de l’ordre d’arbre ;

- relation de masse transformée en explication de l’origine
  ou de la hiérarchie des Yukawa ;

- proportionnalité g_hee = M_e/v comme identité
  indépendante du modèle.
```

### 11.3 Suspension

```text
- valeur numérique finale de y_e dans un schéma précis ;

- choix du meilleur schéma de renormalisation pour le dossier ;

- taille détaillée de toutes les corrections électrofaibles et QED ;

- présence d’opérateurs au-delà du Modèle standard ;

- comparaison entre contraintes directes et indirectes ;

- verdict sur l’observation du couplage Higgs–électron ;

- origine de la petite valeur et de la hiérarchie de y_e.
```

## 12. Conséquence pour S2

S2 ne devra pas demander simplement « quelle est la meilleure valeur de `y_e` ? ».

Il devra comparer trois opérations :

```text
1. déterminer M_e par une chaîne métrologique ;

2. inférer y_e^S(mu) depuis M_e, G_F et le Modèle standard
   avec raccordement déclaré ;

3. contraindre g_hee ou une modification de couplage
   par des processus impliquant directement ou indirectement le Higgs.
```

Ces opérations peuvent porter des nombres reliés. Elles ne possèdent ni la même cible immédiate, ni la même dépendance au modèle, ni le même rang probatoire.

## 13. Sources de verrouillage

### 13.1 Sources internes

- `Dette_active_masse_electron_Yukawa_v0_1.md` ;
- `Synthese_cycle_saveur_Higgs_v0_1.md` ;
- `R1_Cible_determinations_rapport_proton_electron_v0_1.md` ;
- `R3_Constitution_minimale_et_verdict_rapport_proton_electron_v0_1.md` ;
- `D6_Transfert_dette_autonome_me_vers_Saveur_Higgs_v0_1.md` ;
- `D8_Arbitrage_prochaine_dette_apres_cloture_cycle_1_v0_1.md`.

### 13.2 Sources primaires externes

- Tiesinga, Mohr, Newell et Taylor, *CODATA recommended values of the fundamental physical constants: 2022*, Reviews of Modern Physics 97, 025002 (2025) ;
- Hempfling et Kniehl, *On the relation between the fermion pole mass and MSbar Yukawa coupling in the standard model*, Physical Review D 51, 1386 (1995), arXiv:hep-ph/9408313 ;
- Ferroglia, Ossola et Sirlin, *Considerations Concerning the Radiative Corrections to Muon Decay in the Fermi and Standard Theories*, Nuclear Physics B 560, 23 (1999), arXiv:hep-ph/9905442 ;
- Dittmaier et Rzehak, *Electroweak renormalization based on gauge-invariant vacuum expectation values of non-linear Higgs representations: 1. Standard Model*, Journal of High Energy Physics 05 (2022) 125, arXiv:2203.07236 ;
- Grzadkowski, Iskrzyński, Misiak et Rosiek, *Dimension-six terms in the Standard Model Lagrangian*, Journal of High Energy Physics 10 (2010) 085, arXiv:1008.4884.

## 14. Condition locale de sortie

S1 est localement achevé lorsque :

```text
- la distinction M_e / m_e^S(mu) / y_e^S(mu) / v^S(mu) / v_F / g_hee
  est acceptée ;

- les trois rangs de la relation sont conservés :
  identité nue / relation d’arbre / raccordement physique corrigé ;

- l’inférence depuis M_e est séparée d’un accès direct au Higgs ;

- S2 peut être ouvert sans rouvrir la détermination complète de M_e.
```
