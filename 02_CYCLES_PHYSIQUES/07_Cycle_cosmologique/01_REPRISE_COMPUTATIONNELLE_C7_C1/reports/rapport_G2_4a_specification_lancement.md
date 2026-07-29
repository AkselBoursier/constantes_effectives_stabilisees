# G2.4a — spécification opérationnelle du premier lot MCMC X(z)

Issue directrice : #63.

Base : G2.3a fusionnée dans `main` au commit
`0ffd4da0c7e6ab378812fafc09cf1439c430793c`.

Pré-enregistrement directeur :
`reports/rapport_G2_2a_preregistration.md`, décisions D3-A à D3-H gelées.

Configurations qualifiées :

```text
configs/xz/g2_3_m2a_n.yaml
configs/xz/g2_3_m2a_k.yaml
configs/xz/g2_3_m2b_n.yaml
configs/xz/g2_3_m2b_k.yaml
```

## 1. Statut de cette porte

Ce document spécifie le lanceur et les diagnostics du premier lot `P_WS`.
Il ne contient ni code exécutable de production, ni chaîne, ni résultat.

```text
G2.3a : close ;
G2.4a : spécification documentaire ouverte ;
MCMC réelle : NON LANCÉE ;
minimisation / posterior / comparaison : interdits ;
lecture cosmologique : interdite.
```

Une validation humaine distincte de D4-A à D4-H est requise avant la création
du lanceur de production. Une seconde validation sera requise après sa
qualification et avant le premier lancement réel.

## 2. Principe directeur

Les quatre YAML G2.3 restent des descripteurs immuables et qualifiés. Ils ne
seront ni copiés manuellement dans quatre configurations Cobaya parallèles, ni
modifiés pour remplacer `inference.autorisee: false`.

Le futur lanceur construira en mémoire l'information Cobaya à partir du
YAML qualifié, après validation stricte par `validate_config`. Cette règle évite
quatre duplications susceptibles de dériver silencieusement.

Le lot porte uniquement sur le prior directeur :

```text
P_WS : chaque X_i libre ~ U[-2, 4].
```

Les analyses `P_CS`, `P_W+`, `P_C+` et la contingence `P_XL` restent fermées.

## 3. Architecture future autorisable

La porte suivante pourra créer au maximum les quatre fichiers suivants :

```text
scripts/xz_cobaya_g2_4.py
scripts/run_mcmc_xz_g2_4.py
scripts/diagnose_mcmc_xz_g2_4.py
reports/rapport_G2_4b_qualification_lanceur.md
```

Aucun nouveau YAML de modèle ne sera créé. Le futur code devra :

1. charger l'un des quatre descripteurs G2.3 ;
2. appliquer `validate_config` sans tolérance ni correction implicite ;
3. traduire en mémoire les paramètres et priors vers Cobaya ;
4. utiliser l'instrument `XZEvaluator` et le traitement acoustique `corrected` ;
5. ajouter le bloc MCMC G1 gelé ;
6. appliquer les gardes de provenance, sortie et autorisation ;
7. écrire toutes les chaînes et tous les manifestes d'exécution hors Git.

## 4. Information Cobaya construite en mémoire

### 4.1 Paramètres libres communs

```text
H0    ~ U[20, 100] ;
ombh2 ~ U[0.005, 0.1] ;
omm   ~ U[0.01, 0.99] ;
X_i   ~ U[-2, 4] pour chaque amplitude libre du descripteur.
```

La coordonnée dérivée reste :

```text
omch2 = omm*(H0/100)^2 - mnu/93.14 - ombh2 ;
contrainte dure : omch2 > 0.
```

Les paramètres fixes restent ceux de G1/G2.3 :

```text
mnu = 0.06 ; nnu = 3.044 ; tau = 0.0544 ;
ns = 0.9649 ; logA = 3.036 ; géométrie plate.
```

### 4.2 Vraisemblance

Le futur adaptateur Cobaya retournera :

```text
logp = -0.5 * (chi2_BAO + chi2_CMB)
```

lorsque le point est valide, et `-inf` lorsque le support uniforme, `omch2`,
la finitude ou `H_X^2 > 0` échouent.

Les contributions BAO et CMB devront être exposées séparément comme quantités
dérivées ou blocs de vraisemblance auditables. Aucune constante normalisante
ne sera ajoutée à l'une sans l'être à l'autre ; les comparaisons utiliseront
les chi carrés déjà définis dans G1–G2.3.

### 4.3 Bloc sampler hérité de G1

```text
drag: false
over_sample_power / oversample_power: 0.4 selon la clé Cobaya validée
proposal_scale: 1.9
covmat: null
temperature: 1
Rminus1_stop: 0.01
Rminus1_cl_stop: 0.02
max_tries: 1000
resume: true, sous conditions de provenance strictes
```

La qualification devra vérifier la clé exacte acceptée par Cobaya 3.5 et
interdire une correction silencieuse du nom de champ.

## 5. Matrice de production pré-déclarée

Le premier lot contient exactement :

```text
4 variantes × 8 chaînes indépendantes = 32 chaînes.
```

Graines :

```text
M2a-N : 630101, 630102, 630103, 630104, 630105, 630106, 630107, 630108
M2a-K : 630201, 630202, 630203, 630204, 630205, 630206, 630207, 630208
M2b-N : 630301, 630302, 630303, 630304, 630305, 630306, 630307, 630308
M2b-K : 630401, 630402, 630403, 630404, 630405, 630406, 630407, 630408
```

La règle de dérivation est transparente : `100 × graine_G2.3 + index_chaîne`.
Aucune graine ne pourra être remplacée après inspection d'un résultat.

Ordre recommandé afin de répartir les effets de machine et de calendrier :

```text
ronde 1 : chaîne 1 des quatre variantes ;
ronde 2 : chaîne 2 des quatre variantes ;
...
ronde 8 : chaîne 8 des quatre variantes.
```

L'exécution simultanée est autorisée seulement si les ressources sont isolées
et si la concurrence ne modifie pas les versions, données ou préfixes.

## 6. Arborescence de sortie hors Git

Variable obligatoire : `C7C1_XZ_OUT_DIR`.

```text
${C7C1_XZ_OUT_DIR}/g2_4/P_WS/
  M2a-N/s630101/chain
  ...
  M2a-K/s630201/chain
  ...
  M2b-N/s630301/chain
  ...
  M2b-K/s630401/chain
  ...
```

Chaque répertoire de chaîne contiendra, hors Git :

```text
sorties Cobaya ;
manifest.json ;
commande exacte ;
SHA du dépôt et du descripteur ;
SHA-256 des octets BAO ;
versions Python, Cobaya, CAMB, NumPy et SciPy ;
graine, variante, convention et grille ;
heure de début/fin et statut de reprise.
```

Le manifeste ne contiendra aucun résumé posterior interprétatif.

## 7. Pré-vol obligatoire

Avant chaque lancement, le futur lanceur devra échouer avec un code non nul si
l'une des conditions suivantes manque :

```text
qualification G2.3a complète : exit 0 ;
HEAD autorisé et arbre suivi propre ;
SHA du descripteur conforme au manifeste autorisé ;
C7C1_DATA_DIR présent ;
octets BAO et covariance conformes aux SHA épinglés G1 ;
environnement directeur exact :
  Python 3.12.0, Cobaya 3.5, CAMB 1.5.4,
  NumPy 1.26.4, SciPy 1.13.1 ;
C7C1_XZ_OUT_DIR hors de tout ancêtre Git ;
variante, graine et préfixe correspondant exactement à la matrice ;
absence de collision avec une autre chaîne ;
autorisation de production présente et correspondant au SHA du lanceur.
```

## 8. Reprise et immutabilité

`resume=True` n'est autorisé que si le manifeste existant possède exactement :

```text
même variante ; même graine ; même SHA de code ;
même SHA des quatre descripteurs qualifiés ;
mêmes SHA des données ; mêmes versions ;
même bloc sampler ; même préfixe.
```

Sinon le lanceur doit refuser la reprise. Il ne doit ni écraser ni déplacer
silencieusement une chaîne existante.

Une chaîne interrompue peut être reprise ; une chaîne invalidée doit être
conservée sous son préfixe et marquée comme telle. Son remplacement éventuel
exige un amendement documenté, jamais une substitution invisible.

## 9. Qualification de performance avant production

La future qualification G2.4b comportera un banc déterministe de points fixes
et de points prédéclarés dans `P_WS`, sans échantillonnage. Il rapportera
uniquement :

```text
temps médian et quantiles de l'évaluation ;
taux de points valides / rejetés par les contraintes ;
reproductibilité numérique ;
usage mémoire ;
projection de charge pour 32 chaînes.
```

Les valeurs de chi carré de ce banc ne seront pas utilisées pour choisir un
point initial, une variante ou un prior. Si la charge rend le plan irréalisable,
la porte est suspendue pour optimisation purement computationnelle ; aucun
résultat partiel ne peut être interprété.

## 10. Points initiaux et propositions

Les distributions `ref` et `proposal` sont des paramètres d'efficacité, non des
priors scientifiques.

Avant production, G2.4b devra fixer une règle identique entre conventions d'une
même grille. Proposition à qualifier :

```text
H0, ombh2, omm : références G1 ;
X_i : ref uniforme ou normale centrée en 1, strictement contenue dans P_WS ;
propositions X_i : identiques pour tous les nœuds d'une même grille ;
aucune initialisation depuis un minimum, un MAP ou un posterior X(z).
```

Les huit chaînes doivent recevoir des tirages initiaux distincts produits par
leur graine. Un point initial invalide est retiré selon une règle automatique
pré-déclarée, sans ajustement manuel à partir des résultats.

## 11. Diagnostics externes de convergence

Le diagnostic portera sur tous les paramètres libres :

```text
H0, ombh2, omm, X1...X5 pour M2a ;
H0, ombh2, omm, X1...X4 pour M2b.
```

Reconstruction temporelle :

1. vérifier que la colonne `weight` est finie, positive et entière à la
   tolérance numérique ;
2. reconstruire les tirages chronologiques en répétant chaque état selon son
   poids entier ;
3. concaténer correctement les segments de reprise ;
4. retirer les premiers 30 % des tirages reconstruits de chaque chaîne ;
5. ne pas amincir pour les diagnostics ;
6. calculer le R-hat scindé et normalisé par rang, l'ESS bulk et l'ESS tail.

Critères gelés :

```text
R-hat rang <= 1.01 pour chaque paramètre libre ;
ESS bulk >= 1000 pour chaque paramètre libre ;
ESS tail >= 1000 pour chaque paramètre libre ;
8 chaînes présentes et contributrices pour la variante.
```

L'implémentation diagnostique devra être comparée sur cas synthétiques à une
bibliothèque de référence reconnue. La bibliothèque et sa version seront
figées en G2.4b après inventaire local, avant production.

## 12. Embargo d'interprétation

Pendant l'exécution, seules les informations suivantes peuvent être consultées :

```text
état du processus ;
absence d'erreur ;
progression des fichiers ;
acceptation et diagnostics techniques Cobaya ;
R-hat et ESS sans valeur centrale des paramètres ;
statut valide / invalide de chaque chaîne.
```

Jusqu'à convergence des quatre variantes, sont interdits :

```text
moyennes, médianes et intervalles des paramètres ;
tracés posterior ou profils X(z) ;
minimum de chi carré rencontré ;
comparaison ou classement des variantes ;
écarts à X=1 ;
significativité locale ou globale ;
choix d'une variante à poursuivre ou abandonner.
```

Si trois variantes convergent et une échoue, aucune interprétation des trois
premières n'est autorisée. L'échec est d'abord un problème de méthode.

## 13. Condition d'arrêt et reprise méthodologique

La production est suspendue si :

```text
une garde de provenance échoue ;
T8–T12 cessent de passer ;
un descripteur ou une donnée change ;
une chaîne produit des fichiers non lisibles ou des paramètres non finis ;
le diagnostic ne peut reconstruire l'ordre temporel ;
le lanceur ou l'adaptateur est modifié après le premier lancement.
```

Une correction de bogue après lancement suit la règle d'amendement D3-H :
version datée, résultats déjà visibles déclarés, conservation de l'ancien lot
et ré-exécution des quatre variantes affectées.

## 14. Autorisation à deux clés

Le futur lanceur sera verrouillé par défaut. Il exigera deux éléments :

```text
1. un manifeste d'autorisation versionné, portant le SHA exact du lanceur,
   des descripteurs et du pré-enregistrement ;
2. une option explicite de ligne de commande confirmant le lancement de la
   chaîne prévue dans la matrice.
```

G2.4b qualifiera le lanceur avec une autorisation factice refusée. Le vrai
manifeste ne pourra être créé qu'après validation humaine de G2.4b.

## 15. Livrables après production

Avant toute analyse cosmologique, un rapport de provenance et de convergence
devra publier :

```text
inventaire des 32 chaînes ;
manifestes et SHA ;
incidents et reprises ;
R-hat rang, ESS bulk et ESS tail par paramètre ;
verdict de convergence par variante ;
aucune moyenne, intervalle, courbe X(z) ou comparaison de modèles.
```

Une nouvelle décision humaine ouvrira ensuite seulement l'analyse posterior.
La minimisation, AIC/AICc/BIC et simulations restent des portes ultérieures.

## 16. Décisions humaines proposées

```text
D4-A — architecture sans duplication : les YAML G2.3 restent immuables ;
       l'information Cobaya est construite en mémoire : À RATIFIER.

D4-B — matrice de 32 chaînes, graines 630101–630408 et ordre par rondes :
       À RATIFIER.

D4-C — sorties, manifestes et reprises strictement hors Git avec identité
       complète des entrées : À RATIFIER.

D4-D — bloc sampler G1, pré-vol auto-bloquant et points initiaux sans
       posterior X(z) : À RATIFIER.

D4-E — reconstruction par poids, burn-in 30 %, R-hat rang <= 1.01,
       ESS bulk/tail >= 1000 sur tous les paramètres libres : À RATIFIER.

D4-F — embargo d'interprétation jusqu'à convergence des quatre variantes :
       À RATIFIER.

D4-G — banc de performance sans exploitation des chi carrés et suspension
       en cas d'irréalisabilité : À RATIFIER.

D4-H — autorisation à deux clés et validation humaine supplémentaire avant
       le premier lancement réel : À RATIFIER.
```

## 17. Condition de sortie de G2.4a

G2.4a peut être close lorsque :

```text
D4-A à D4-H ont été validées ou amendées humainement ;
le document ratifié est fusionné ;
aucun code de production et aucune chaîne n'ont précédé cette décision.
```

La porte suivante sera G2.4b : implémentation et qualification adversariale du
lanceur, toujours sans MCMC réelle.