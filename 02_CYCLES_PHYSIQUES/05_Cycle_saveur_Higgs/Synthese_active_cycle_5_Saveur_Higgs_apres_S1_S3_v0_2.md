# Synthèse active du cycle 5 — Saveur–Higgs après S1–S3 v0.2

## 0. Statut

```text
statut : synthèse active validée du cycle Saveur–Higgs ;
date scientifique : 27 juillet 2026 ;
issue de propagation : #57 — close / completed ;
validation documentaire : P5-1 à P5-5 validées, propagation fusionnée par la PR #58 ;
base scientifique : S1, S2 et S3 validés et fusionnés par la PR #56 ;
fonction : porter de manière bornée le verdict local du cas électronique
           dans l’orientation active du cycle ;
autorité : point d’entrée courant du cycle 5 pour le périmètre S1–S3,
            selon P5-2 et la fusion de la PR #58 ;
remplace pour l’usage courant :
  Synthese_cycle_saveur_Higgs_v0_1.md ;
conserve la v0.1 : comme état architectural antérieur ;
ne vaut pas : réécriture de S1–S3,
               mesure directe acquise du Yukawa électronique,
               ajustement global SMEFT,
               explication de la hiérarchie fermionique,
               nouvelle taxonomie,
               ni arbitrage courant de la prochaine dette scientifique.
```

Les sections 17 et 19 conservent l’état procédural **avant** la validation et la fusion de la propagation. Elles documentent la séparation qui devait être préservée entre propagation et arbitrage de la dette suivante ; elles ne doivent plus être lues comme des décisions encore en attente. L’arbitrage post-S1–S3 a été conduit séparément par D9 (#60). Cette mise à jour de statut ne réécrit aucun résultat scientifique de S1–S3 et ne sélectionne aucune nouvelle dette actuelle.

## 1. Pourquoi une propagation est nécessaire

La synthèse v0.1 a établi que Saveur–Higgs est un pont architectural reliant :

```text
échelle de brisure ;
couplages de Yukawa ;
matrices et paramètres de masse ;
diagonalisation ;
spectres physiques ;
orientations CKM et PMNS.
```

Ce résultat demeure valide. Il est cependant devenu incomplet après le lot S1–S3.

Le cas électronique montre désormais que la solidarité architecturale doit être accompagnée d’une reconstruction des passages probatoires. Sans cette propagation, la couche active continuerait à juxtaposer « masse », « Yukawa » et « accès » sans porter les distinctions validées entre détermination, inférence et test du vertex.

Test d’ablation :

```text
sans v0.2 :
  pont architectural conservé,
  mais chaîne probatoire absente
  et dette m_e présentée à tort comme non instruite ;

avec v0.2 :
  architecture conservée,
  chaîne probatoire rendue active,
  dette électronique localement close,
  prochaine priorité laissée à un arbitrage distinct.
```

## 2. Continuité et gain par rapport à la v0.1

La décision centrale de la v0.1 était :

```text
Saveur–Higgs = pont architectural documenté,
                gain explicatif conditionnel.
```

La v0.2 ajoute :

```text
Saveur–Higgs = pont architectural documenté
                + réseau de passages probatoires indexés.
```

Cette addition ne transforme pas le cycle en théorie générale de la preuve. Elle indique seulement que, dans le cas électronique instruit, chaque flèche entre échelle, couplage, masse et observable correspond à une opération distincte.

## 3. Question directrice active

> Comment l’échelle électrofaible, les couplages de Yukawa, les paramètres de masse, les masses physiques et les orientations deviennent-ils solidaires dans le régime brisé, et par quelles opérations distinctes cette solidarité devient-elle déterminable, inférable ou testable ?

La question comporte désormais deux dimensions inséparables mais non réductibles :

```text
architecture : quels objets et relations forment le réseau ?
preuve : quelle opération soutient chaque énoncé sur ce réseau ?
```

## 4. Décision de rang après S1–S3

```text
Saveur–Higgs :
  pont architectural documenté ;
  réseau probatoire partiellement instruit ;
  explication d’origine refusée ;
  généralisation au-delà des cas instruits suspendue.
```

Le lot électronique constitue un cas positif de reconstruction du réseau probatoire. Il ne suffit pas à attribuer automatiquement le même profil aux autres fermions, matrices ou orientations du cycle.

## 5. Cas électronique — cibles distinctes

Le cycle distingue désormais activement :

```text
M_e : masse physique ou on-shell de l’électron ;

m_e^S(mu) : paramètre de masse renormalisé
            dans un schéma S et à une échelle mu ;

y_e^S(mu) : paramètre de Yukawa électronique renormalisé ;

v^S(mu) : paramètre électrofaible renormalisé ;

v_F : échelle dérivée de G_F ;

g_hee : interaction Higgs–électron
        dans une amplitude ou convention déclarée.
```

Ces cibles sont reliées. Elles ne sont ni identiques ni expérimentalement interchangeables.

## 6. Trois rangs de la relation masse–Yukawa

La formule commune

```text
m_e = y_e v / sqrt(2)
```

doit être indexée à son niveau.

### 6.1 Paramètres nus

Dans le Modèle standard minimal, après développement du doublet de Higgs :

```text
m_e,0 = y_e,0 v_0 / sqrt(2)
```

est une identité structurelle du Lagrangien nu.

### 6.2 Paramètres renormalisés

Dans un schéma et à une échelle déclarés :

```text
m_e^S(mu) = y_e^S(mu) v^S(mu) / sqrt(2)
```

est une relation de paramétrisation à l’ordre considéré.

### 6.3 Masse physique

Le raccordement à la masse physique exige des corrections radiatives :

```text
M_e
=
[y_e^S(mu) v^S(mu) / sqrt(2)]
× [1 + Delta_e^S(mu)]
```

ou une écriture équivalente selon la convention.

Règle active :

```text
identité nue
≠ paramétrisation renormalisée
≠ raccordement à une masse physique.
```

## 7. Chaîne probatoire du cas électronique

```text
mesures de rapports et fréquences
→ ajustement métrologique
→ M_e déterminée
→ sélection du Modèle standard minimal
→ définition de v et du schéma
→ raccordement radiatif
→ y_e^S(mu) inféré
→ observables indirectes
→ recherche directe du vertex H–e–e.
```

Chaque flèche possède une fonction propre : mesure, ajustement, sélection du cadre, renormalisation, calcul de boucle ou reconstruction collisionnelle.

## 8. Résultats actifs du lot S1–S3

### 8.1 Masse physique

```text
M_e : masse physique très précisément déterminée
      par un réseau métrologique ajusté.
```

Cette précision soutient l’usage de `M_e` comme entrée de calcul et de raccordement. Elle ne se transfère pas automatiquement aux autres cibles.

### 8.2 Yukawa standard

```text
y_e standard : inféré avec grande précision
               depuis M_e, G_F et le cadre minimal,
               sous schéma, échelle et corrections déclarés.
```

Le rang est celui d’une inférence théorique fortement contrainte par des données précises, non d’une mesure indépendante du paramètre.

### 8.3 Accès indirects

```text
eEDM : borne directe sur d_e,
       contrainte indirecte sur certaines composantes CP-impaires ;

a_e : observable directement mesurée,
      contrainte indirecte sur y_e dans un modèle déclaré.
```

Leur sensibilité peut dépasser celle d’un accès collisionnel pour certaines composantes. Leur portée demeure dépendante du modèle de passage.

### 8.4 Recherche directe

```text
CMS : B(H → e+e−) < 3.0 × 10^(-4)
      à 95 % de confiance ;
      aucun signal significatif observé.
```

La branche est directement bornée. Une conversion en `kappa_e` ou en Yukawa exige des hypothèses sur la production, la largeur totale, la structure CP et les opérateurs autorisés.

### 8.5 Perspective résonante

```text
e+e− → H : accès direct futur possible,
           actuellement étude de faisabilité,
           non résultat acquis.
```

## 9. Règle comparative des accès

Le cas électronique établit :

```text
sensibilité numérique élevée
≠ proximité probatoire de la cible ;

proximité probatoire élevée
≠ sensibilité numérique supérieure ;

direct
≠ modèle-indépendant ;

indirect
≠ probatoirement négligeable.
```

Les accès sont complémentaires sans être combinables numériquement hors d’un modèle et d’une vraisemblance communs.

## 10. Ce que le cycle établit désormais

```text
1. Échelle, couplages, masses et orientations forment un réseau de dépendances.
2. Une architecture commune ne produit pas une équivalence entre les preuves.
3. Masse physique, paramètre renormalisé, Yukawa et vertex doivent être séparés.
4. Une grandeur très précisément déterminée peut soutenir une inférence précise
   sans constituer une mesure directe de la cible inférée.
5. Les accès directs et indirects doivent être ordonnés par leur cible,
   leur modèle de passage et leur rang probatoire.
6. Le cas électronique transforme un pont architectural
   en réseau de passages probatoires explicitables.
```

## 11. Ce que le cycle ne confirme pas

```text
- observation directe du couplage H–e–e à la valeur standard ;
- équivalence entre précision de M_e et précision directe de y_e ;
- valeur unique de v indépendante du schéma au-delà de l’arbre ;
- borne globale modèle-indépendante sur kappa_e ou tilde_kappa_e ;
- absence d’opérateurs nouveaux ;
- explication de la petite valeur de y_e ;
- explication de la hiérarchie fermionique ;
- extension automatique du verdict électronique à tous les Yukawa ;
- nouvelle famille ou nouveau statut de constance.
```

## 12. Formulation active sur « la masse vient du Higgs »

> Dans le Modèle standard minimal, la masse électronique est reliée au Yukawa électronique et à l’échelle électrofaible après brisure ; cette relation permet une inférence précise du Yukawa depuis la masse, mais le couplage direct au Higgs n’est pas encore observé à la valeur standard et l’origine de sa petitesse demeure inexpliquée.

Cette formulation remplace, pour le cas électronique, les formulations non qualifiées qui confondent relation structurelle, mesure et explication d’origine.

## 13. Effet sur les questions directrices

### 13.1 Q1 — frontière entre variation et maintien

Ce qui tient dans le cas électronique porte sur des cibles différentes :

```text
M_e : référence métrologique très précise ;
relation minimale : structure maintenue dans le cadre déclaré ;
raccordement : cohérence conditionnelle du calcul ;
H → e+e− : absence de signal dans la sensibilité atteinte.
```

La stabilité de `M_e` ne suffit pas à établir une constance modèle-indépendante de `y_e` ou du vertex.

### 13.2 Q2 — opérations de détermination

Le cas montre qu’un maintien devient affirmable au moyen d’une chaîne d’opérations hétérogènes. Reconstruire cette chaîne déplace la question :

```text
non seulement : quelle valeur ?
mais : quelle opération produit l’énoncé,
       quelle cible le porte,
       et quelles hypothèses autorisent son transfert ?
```

## 14. Statut du lot et du cycle

```text
lot S1–S3 m_e / y_e / v :
  validé ;
  localement clos ;
  propagé après validation de la présente synthèse ;

dette m_e transférée par D6 :
  résolue dans son premier périmètre ;

cycle Saveur–Higgs :
  ouvert ;
  pont architectural conservé ;
  premier cas probatoire électronique intégré ;
  autres dettes non closes par ce lot.
```

Le cycle n’est ni clos ni suspendu par cette propagation.

## 15. Conditions de réouverture du cas électronique

Le lot n’est rouvert que si un matériau modifie son verdict, notamment :

```text
- observation directe de H → e+e− ou e+e− → H ;
- résultat Run 3 dédié modifiant substantiellement la borne ;
- ajustement global fournissant covariances et hypothèses communes ;
- nouveau raccordement modifiant le rang de l’inférence ;
- résultat établissant ou excluant une décorrélation masse–vertex ;
- matériau nouveau sur l’origine ou la hiérarchie du Yukawa.
```

Une simple amélioration numérique qui ne change ni cible, ni rang, ni verdict ne suffit pas à rouvrir le lot.

## 16. Ce qui reste local à S1–S3

Ne sont pas recopiés dans la couche active :

```text
- le détail complet des schémas de renormalisation ;
- les développements opérateur par opérateur ;
- les calculs détaillés de conversion vers kappa_e ;
- les scénarios complets d’eEDM et de a_e ;
- les études instrumentales détaillées du canal résonant ;
- les tableaux bibliographiques complets.
```

S1, S2 et S3 demeurent les preuves locales.

## 17. Prochaine décision distincte

La propagation ne sélectionne pas automatiquement la prochaine dette. Après intégration, une nouvelle décision devra comparer :

```text
- un autre cas borné du cycle Saveur–Higgs ;
- un sous-cas borné du cycle 7 ;
- les dettes actives des cycles 4, 6, 8, 9 ou 10 ;
- les travaux T2 parallèles du cycle 3.
```

## 18. Documents de preuve

```text
S1_Relation_structurelle_masse_electron_Yukawa_v0_1.md ;
S2_Acces_metrologiques_indirects_directs_Yukawa_electron_v0_1.md ;
S3_Verdict_local_masse_electron_Yukawa_acces_Higgs_v0_1.md ;
D6_Transfert_dette_autonome_me_vers_Saveur_Higgs_v0_1.md ;
D8_Arbitrage_prochaine_dette_apres_cloture_cycle_1_v0_1.md.
```

## 19. Décisions soumises à validation humaine

```text
P5-1 — valider la nécessité de la propagation bornée ;

P5-2 — valider la synthèse active v0.2
       comme point d’entrée courant du cycle 5 ;

P5-3 — déclarer la dette m_e localement résolue
       dans son premier périmètre ;

P5-4 — autoriser la synchronisation des points d’entrée,
       le contrôle final puis la fusion ;

P5-5 — maintenir distinct l’arbitrage
       de la prochaine dette scientifique.
```