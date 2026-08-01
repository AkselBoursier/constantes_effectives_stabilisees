# Rapport G2.4d — raccord qualifié au lanceur, sans production

Porte G2.4d (issue #63). Base `840f5d81`, branche
`comp/c7-c1-xz-launcher-integration`, exécutée exclusivement depuis le clone
directeur qualifié hors dossier synchronisé (INFRA-1).

**Aucune MCMC, aucune minimisation, aucun posterior, aucune chaîne, aucun
manifeste réel, aucune autorisation réelle, aucun budget inventé.**

## 1. Base et périmètre

```text
fichiers modifiés (périmètre autorisé) :
  scripts/xz_cobaya_g2_4.py
  scripts/run_mcmc_xz_g2_4.py
  scripts/qualify_xz_launcher_g2_4d.py      (nouveau)
  reports/rapport_G2_4d_raccord_lanceur.md  (nouveau)

cinquième fichier, sur impossibilité technique DÉMONTRÉE et PUBLIÉE
AVANT modification (commentaire dédié dans #63) :
  scripts/qualify_xz_optim_g2_4c.py — deux lignes, faute graphe_un_bloc

fichiers gelés, vérifiés intouchés :
  xz_fast_g2_4c.py ; xz_background_g2_1.py ; xz_likelihood_g2_3.py ;
  qualify_xz_configs_g2_3.py ; diagnose_mcmc_xz_g2_4.py ;
  configs/xz/g2_3_*.yaml ; priors, graines, données et rapports
  historiques.
```

### 1 bis. Impossibilité technique déclarée

La faute gelée `graphe_un_bloc` de `qualify_xz_optim_g2_4c.py` construisait
son cas via `build_cobaya_info`, dont l'intention était l'architecture
MONOBLOC. Ce nom désignant désormais l'architecture directrice à deux blocs,
la faute n'injectait plus rien :

```text
build_cobaya_info (directeur) -> 2 blocs ; faute détectée = False
build_cobaya_info_legacy      -> 1 bloc  ; faute détectée = True
```

Les deux exigences — « `build_cobaya_info` devient directeur » et « G2.4c
rejoué sans modification en exit 0 » — étaient donc incompatibles. Aucun
contournement n'était admissible : un repli implicite vers le legacy est
explicitement interdit. La modification minimale, publiée avant application,
fait porter la faute sur `build_cobaya_info_legacy` : son intention est
préservée à l'identique, aucun seuil, prior, graine, donnée ni autre faute
n'est touché.

## 2. Architecture avant / après

```text
AVANT (G2.4b)  : une vraisemblance externe monobloc recevant
                 H0, ombh2, omm ET les X_i, adossée à XZEvaluator.

APRÈS (G2.4d)  : theory     ReferenceLenteXZ      [H0, ombh2, omm]
                 likelihood VraisemblanceRapideXZ [X_i seuls]
                            requirements = {etat_lent_xz}
```

Le constructeur directeur `build_cobaya_info` **délègue** la construction à
`xz_fast_g2_4c.build_info_optimisee` : aucune seconde implémentation du chemin
rapide n'est recopiée. Il vérifie ensuite structurellement le graphe produit
(noms des composants, `input_params` de chaque côté, `requirements`) et
refuse toute déviation.

L'ancien constructeur est conservé sous `build_cobaya_info_legacy`, au contenu
scientifique **strictement identique** à G2.4b ; il ne sert plus que d'oracle
de régression et de référence de performance.

Bloc méta interne, jamais transmis à Cobaya :

```text
backend = optimized ; acoustic_mode = corrected-v1.1 ;
architecture = slow-theory/fast-likelihood ;
oracle_regression = build_cobaya_info_legacy
```

## 3. Parité de l'information Cobaya

`comparer_parite` compare, pour les quatre variantes à leur graine gelée, tout
ce qui doit être identique : ordre des paramètres échantillonnés, priors,
refs, propositions, latex des échantillonnés **et des dérivés**, dérivés et
leur ordre, prior joint `omch2 > 0`, bloc sampler complet, graine, noms et
ordre des X_i, variante, grille, convention, liste des paramètres libres, et
enfin le **bloc `params` intégral** — de sorte qu'aucun champ ne puisse
diverger en silence.

Défaut corrigé au cours de cette porte, signalé par la revue adversariale :
`build_info_optimisee` ne déclare que `derived: True` pour les trois χ², là où
l'encodage gelé G2.4b leur associe une étiquette LaTeX. Le bloc `params` du
directeur différait donc réellement du legacy, et l'ancienne signature de
parité était aveugle à ce champ. Le constructeur directeur ré-injecte
désormais les trois étiquettes (fichier autorisé ; le chemin rapide reste
gelé) et la signature compare le bloc entier. Trois fautes nouvelles
(`parite_latex_derive_perdu`, `parite_prior_altere`,
`parite_proposal_altere`) prouvent que le comparateur mord.

```text
M2a-N, M2a-K, M2b-N, M2b-K : PARITÉ EXACTE (0 différence)
seule différence : le graphe
  legacy    theory=[]                       likelihood=[xz_g2_4]
  directeur theory=[reference_lente_xz]     likelihood=[xz_rapide]
```

Matrice complète des 32 couples variante/graine, au niveau construction et
métadonnées : **32/32 conformes** (graine propagée au sampler, backend
`optimized`, mode `corrected-v1.1`, graphe à deux composants).

`verifier_bloc_sampler` teste désormais le constructeur **directeur** :
`oversample_power` est acceptée, `over_sample_power` est rejetée — aucune
correction silencieuse.

## 4. Mode acoustique

```text
corrected (nom nu du descripteur validé) -> corrected-v1.1  (résolution explicite)
corrected-legacy  : REFUSÉ comme mode directeur
fixed             : REFUSÉ comme mode directeur
mode inconnu      : REFUSÉ (ValueError)
```

La résolution passe par `resolve_acoustic_mode` (oracle amendé G2.4c-iii) puis
vérifie l'égalité au mode directeur. Le chemin rapide est contrôlé : si son
`MODE_ACOUSTIQUE_DIRECTEUR` divergeait, la construction échouerait. Aucun
repli, aucune variable implicite ne peut ramener l'ancien chemin.

## 5. Contrat local privé consommé par le lanceur

`garde_contrat_local` exige : variable `C7C1_CONTRAT_LOCAL` présente ; JSON
valide ; version de schéma `1.2.0` ; statut `PREPARATION_ONLY` ;
`python_directeur` égal à `sys.executable` après résolution canonique ;
environnement, données et runs identiques aux variables du processus ;
empreinte d'environnement conforme ; SHA BAO conformes. Le schéma périmé ne
contenant que `seuil_minimal_Gio` est **explicitement refusé**.

Fermeture G2.4d-a — l'empreinte globale des paquets ne remplace plus les
comparaisons explicites :

```text
versions déclarées au contrat confrontées une à une aux versions CHARGÉES :
  python, cobaya, camb, numpy, scipy, et getdist lorsqu'il est déclaré ;
garde_technique_minimale_Gio du contrat == constante qualifiée (40 Gio) —
  toute divergence contrat/code échoue ;
<CACHE> déclaré par le contrat : canoniquement distinct de DATA, RUNS,
  TEMP et TMP ; hors Git (aucun ancêtre .git) ; hors dossier synchronisé.
  Aucun cache n'est créé ni déplacé par cette porte.
```

Les comparaisons de chemins Windows utilisent `os.path.realpath` puis
`normcase` : insensibles à la casse et aux liens, sans jamais rendre égaux
deux chemins distincts. Aucune valeur du contrat n'est publiée.

## 6. Gardes de chemins

```text
dépôt courant == dépôt directeur du contrat        (le checkout historique
                                                    est refusé comme base)
HEAD exact ; arbre suivi propre exigé en production
racine du dépôt hors dossier synchronisé
C7C1_XZ_OUT_DIR existe et est un répertoire
C7C1_XZ_OUT_DIR hors Git — aucun ancêtre .git, même vide
C7C1_XZ_OUT_DIR hors dossier synchronisé
C7C1_DATA_DIR distinct de C7C1_XZ_OUT_DIR
TEMP et TMP distincts de DATA et de RUNS
```

Le checkout historique n'a été ni modifié, ni utilisé, ni supprimé.

## 7. Threads et environnement

Les quatre plafonds doivent **exister** et valoir exactement la chaîne `"1"` :
une absence, une valeur vide, `0`, `2`, `auto` ou un espace échouent — les six
cas sont testés par injection. S'y ajoutent `PYTHONNOUSERSITE == "1"`,
interpréteur 64 bits, `sys.prefix` distinct de `sys.base_prefix`, site
utilisateur désactivé, versions exactes du contrat et empreinte normalisée
exacte des paquets.

```text
Python 3.12.0 | Cobaya 3.5 | CAMB 1.5.4 | NumPy 1.26.4 | SciPy 1.13.1
empreinte SHA-256 de l'inventaire normalisé : b6414d94…b74f4  (35 paquets)
```

## 8. Mesure de capacité et distinction garde / budget

`espace_libre_gio` appelle `shutil.disk_usage` sur le **répertoire cible
réel**, ou sur son plus proche parent existant — jamais sur `Path(cible).anchor`,
jamais sur une racine abstraite. La qualification **espionne l'argument
transmis** et prouve qu'il s'agit de la cible :

```text
argument observé est la cible  : True
argument observé est l'ancre   : False
```

Deux contrôles désormais séparés :

```text
garde technique  : >= 40 Gio ; autorise SEULEMENT la poursuite des tests
                   et de la préparation ;
budget production: budget_production_requis_Gio non nul, positif et
                   RATIFIÉ, comparé à l'espace libre de la cible ;
                   NON_ETABLI bloque toute production.
```

`--preflight` sort donc avec succès sous le verdict

```text
PREPARATION OK — PRODUCTION NON AUTORISABLE
```

lorsque la garde technique passe alors que le budget reste `NON_ETABLI`.
**Aucun budget de production n'a été inventé.**

## 9. Schéma d'autorisation futur

```text
sha256_lanceur ; sha256_adaptateur ; sha256_chemin_rapide (OBLIGATOIRE) ;
sha256_descripteurs ; sha256_preenregistrement ; sha256_donnees ;
empreinte_environnement ; version_contrat_local ; head_autorise ;
racine_runs_canonique ; variantes_graines_autorisees ;
budget_production_requis_Gio ; budget_production_ratification ;
cle_humaine_1 ; cle_humaine_2 ; type
```

Huit fautes d'autorisation prouvent qu'une autorisation ne peut jamais valider
un ancien adaptateur, un chemin rapide modifié ou absent, un contrat d'une
autre version, un budget absent, un HEAD différent, une autre racine de runs
ni une autre empreinte d'environnement.

Fermeture G2.4d-a — trois verrous supplémentaires :

```text
usage : la garde RÉELLE n'accepte que « PRODUCTION ». Les manifestes de
  qualification portent « QUALIFICATION_ONLY » et sont REJETÉS
  systématiquement — un fichier éphémère ne peut jamais servir
  d'autorisation réelle ;
budget : égalité NUMÉRIQUE EXACTE entre le budget de l'autorisation et
  celui du contrat, après validation du type. Une autorisation à 50 Gio
  et un contrat à 80 Gio sont refusés ensemble, même si l'espace libre
  dépasse 80 Gio ;
ratification : la référence de ratification doit être identique entre le
  contrat, l'autorisation et le manifeste de run.
```

Les manifestes de qualification sont **éphémères**, sous `%TEMP%`, marqués
`QUALIFICATION_ONLY` par leur champ `usage`, puis supprimés. **Aucune
autorisation réelle n'existe** : aucune n'a été créée, et la garde réelle
refuse par construction tout fichier de qualification.

## 10. Écriture atomique et identité de reprise

`ecrire_manifeste_atomique` : temporaire frère → JSON canonique UTF-8 → flush
→ `fsync` du fichier → `os.replace` atomique → `fsync` du répertoire quand la
plate-forme le permet ; nettoyage du temporaire en cas d'échec ; refus
d'écraser un manifeste existant non identique ; réécriture à l'identique
tolérée.

Éprouvée avec une **identité complète** (les 27 champs), et non plus avec un
manifeste réduit :

```text
écriture initiale            : OK
relecture identique          : OK
réécriture identique tolérée : OK
refus d'une identité différente : OK
échec avant os.replace       : aucun partiel, aucun temporaire résiduel
date_creation_utc conservée exactement       : OK
sha256_encodage_scientifique conservé exactement : OK
tous les champs obligatoires présents après relecture : OK
testé EXCLUSIVEMENT sous %TEMP% ; aucun manifest.json dans <RUNS>
```

### 10 bis. Identité de reprise — fermeture G2.4d-a

L'identité de reprise compte désormais **27 champs obligatoires**, tous
présents et aucun remplacé par une valeur implicite :

```text
schema ; variante ; graine ; backend optimized ; mode corrected-v1.1 ;
date_creation_utc (AAAA-MM-JJTHH:MM:SSZ, TRANSMISE explicitement — jamais
  fabriquée par identite_run ; valeur fixe en qualification, générée une
  seule fois puis propagée en production) ;
head ; sha256_lanceur ; sha256_adaptateur ; sha256_chemin_rapide ;
sha256_descripteur ; sha256_donnees ; sha256_autorisation ;
versions ; empreinte_environnement ; version_contrat_local ;
racine_runs_canonique ;
params ; prior_joint ; sampler ; ordre_parametres_echantillonnes ;
ordre_parametres_derives ; meta_variante_grille_convention ;
sha256_encodage_scientifique ;
budget_production_requis_Gio ; reference_ratification_budget ;
statut_run = PLANIFIE_NON_LANCE.
```

L'encodage scientifique gelé (`params`, prior joint, sampler, ordres,
métadonnées) provient du **constructeur directeur**, après retrait du graphe
externe et du bloc `_xz_meta` non publiable ; il est entièrement sérialisable
et son empreinte `sha256_encodage_scientifique` porte sur son JSON canonique.
Les deux clés humaines de l'autorisation **ne sont jamais reproduites** : seul
le SHA-256 du fichier d'autorisation est consigné.

## 11. Verrou dur de production

`VERROU_PRODUCTION_G2_4D = True`. Ordre effectif de `produire` : refus des
injections de test → confirmation explicite → contrat, environnement, données,
threads et chemins → HEAD et arbre propre → autorisation à deux clés → budget
ratifié → construction **pure** du plan → **VERROU** → (porte future
seulement : création du répertoire, écriture atomique, `cobaya.run`).

Préalable exigé par G2.4d-a : la **vraie garde** est d'abord confrontée à un
manifeste de qualification et doit le **rejeter** sur son champ `usage`. Ce
n'est qu'ensuite, et dans le seul scénario « amont satisfait », que la garde
d'autorisation est remplacée par une fonction du harnais — les gardes de
contrat, de chemins, d'environnement et de threads restant les vraies — la
substitution étant restaurée dans un `finally`. Aucun fichier éphémère de
qualification n'est donc jamais accepté comme autorisation réelle.

Preuve dynamique, en **deux scénarios**, avec sentinelles installées sur
`Path.mkdir`, `os.makedirs`, `os.replace`, `open` en écriture et `cobaya.run`.

Un appel nu à `produire` s'arrêterait bien en amont — arbre sale, ou
autorisation absente — et « aucune sentinelle atteinte » serait alors vrai
pour une raison **sans rapport avec le verrou**. Défaut signalé par la revue
adversariale et corrigé : les gardes amont sont désormais rendues
satisfaites (autorisation `QUALIFICATION_ONLY` structurellement valide, arbre
déclaré propre, budget déclaré ratifié) afin que l'exécution parvienne
réellement à l'étape 8, et l'on **exige** que l'exception levée soit celle du
verrou.

```text
QUALIFICATION_ONLY rejeté par la vraie garde : True (sur le champ usage)
amont satisfait : arrêt = « GardeErreur: VERROU G2.4d : raccord qualifié
                  SANS production … »   -> verrou_atteint = True
                  sentinelles atteintes : AUCUNE
amont réel      : arrêt = « GardeErreur: arbre Git non propre : production
                  refusée »              (refus plus précoce)
                  sentinelles atteintes : AUCUNE
```

Deux fautes de contournement prouvent en outre que ces sentinelles
**détectent réellement** un franchissement : injectées, elles se déclenchent
(exit 1).

## 12. Construction Cobaya réelle et graphe

```text
cobaya.run(info, test=True) : PASSE pour les 4 variantes
composants réels            : ReferenceLenteXZ + VraisemblanceRapideXZ
H0/ombh2/omm dans la likelihood : ABSENTS
X_i dans la Theory              : ABSENTS
blocs Cobaya                    : [H0, ombh2, omm] + [X1..Xn] — deux blocs

variation X_i seule              : 0 nouvel appel CAMB
variation du fond                : 1 nouvel état lent
retour au triplet caché          : 0 nouvel appel CAMB
changement de variante           : aucun partage de cache
historique A,B,C,A vs C,A,B,A    : identique point à point
```

## 13. Comparaisons numériques (P0–P3, quatre variantes)

Fermeture G2.4d-a — les quatre dérivés runtime `omch2`, `chi2_BAO`,
`chi2_CMB` et `chi2_total` sont **exigés présents** : plus aucun test
conditionnel sur leur existence, plus aucun repli sur une valeur de secours.
Leur absence est une faute de porte, prouvée par deux fautes injectées.

```text
classification valide/invalide : 16/16 identiques entre les trois voies
dérivés runtime présents       : 4/4 sur tous les points évalués
Cobaya optimisé vs EvaluateurRapide : IDENTITÉ BIT À BIT
  (omch2, chi2_BAO, chi2_CMB, chi2_total, et logp == -0.5*chi2_total,
   tous comparés par égalité exacte)
contre l'oracle legacy, seuils déjà qualifiés, aucun relâchement :
  chi2_BAO   0.0  (seuil 1e-10)     chi2_CMB   0.0 (seuil 1e-3)
  chi2_total 0.0  (seuil 1e-3)      logp       0.0 (seuil 5e-4)
  omch2      0.0  (seuil 1e-12)
```

## 14. Rejeux des portes scientifiques gelées

```text
python scripts/qualify_xz_configs_g2_3.py : exit 0
  T8, T9, T10, T11, T12-legacy-régression et T12-A1-numérique : tous vrais.

python scripts/qualify_xz_optim_g2_4c.py  : exit 0 (après le correctif
  d'une ligne déclaré en §1 bis ; premier rejeu : exit 1, échec unique
  « faute NON détectée : graphe_un_bloc », publié avant modification)
  couverture 331/306/25 inchangée ; classification identique ;
  23/23 fautes détectées ; contrôle acoustique GL 16/16 ; alias exact ;
  corrected-legacy bit-identique ; audit des règles sans violation ;
  pire écart : correction acoustique 1,416e-14 (seuil 1e-13) ;
  corrected-v1.1 directeur ; corrected-legacy en régression seulement.
```

## 15. Fautes adversariales

**62 fautes injectées, 62 détectées** (code non nul), en sous-processus :

```text
identité de run (G2.4d-a) : date absente ; date mal formée ; params
  absents ; prior joint absent ; empreinte scientifique fausse ;
  sampler altéré ;
dérivés runtime (G2.4d-a) : omch2 omis ; chi2_BAO omis ;
liaison budget (G2.4d-a) : budget autorisation != contrat ; ratification
  différente ; contrat RATIFIE sans valeur de ratification ;
usage (G2.4d-a) : autorisation QUALIFICATION_ONLY présentée en production ;
contrat étendu (G2.4d-a) : version de paquet déclarée fausse ; garde
  technique != 40 ; CACHE == DATA ; CACHE == RUNS ; CACHE sous Git ;
  CACHE non déclaré ;
parité : latex d'un dérivé perdu ; prior altéré ; proposition altérée
  (ces trois-là qualifient le comparateur de parité lui-même) ;
graphe et mode : directeur retournant le legacy ; mode corrected-legacy ;
  mode fixed ; mode inconnu ; Theory dépendant d'un X_i ; Likelihood
  dépendant de H0 ; graphe réduit à un bloc ; appel CAMB sur variation
  X_i ; cache partagé entre variantes ;
contrat : absent ; schéma périmé seuil_minimal_Gio ; python différent de
  sys.executable ; empreinte fausse ; JSON invalide ;
threads : plafond absent ; =2 ; vide ; auto ; espace ; PYTHONNOUSERSITE
  absent ;
chemins : runs sous Git ; runs sous dossier synchronisé ; DATA == RUNS ;
capacité : mesure sur l'ancre du volume ; budget NON_ETABLI accepté ;
  budget supérieur à l'espace ; budget nul ;
autorisation : SHA du chemin rapide absent ; SHA du chemin rapide faux ;
  ancien adaptateur ; contrat d'une autre version ; budget absent ; HEAD
  différent ; autre racine de runs ; empreinte d'environnement fausse ;
manifeste : écrasement non identique ; temporaire partiel conservé ;
reprise : sans manifeste ; identité partielle ;
verrou : cobaya.run atteint ; écriture réelle atteinte.
```

## 16. Déterminisme

```text
qualificateur G2.4d exécuté DEUX FOIS : exit 0 / exit 0 ;
sorties normalisées bit à bit identiques (diff vide) ;
temps, mémoire et espace libre : section séparée, hors diff.
```

## 17. Performance

Mesures indicatives de cette passe (machine partagée) :

```text
évaluation legacy monobloc (réchauffée)  : ~1,1 s
évaluation optimisée directe             : ~0,04-0,06 s
via le modèle Cobaya, variation X_i      : ~0,04-0,06 s
via le modèle Cobaya, variation du fond  : ~0,11-0,15 s
construction initiale du modèle          : ~0,05 s
séquence mixte représentative (78 évaluations, 3 cycles)
  -> 3 appels CAMB pour 3 cycles (0 sur les variations X_i)
mémoire du cache lent : bornée (taille observée 1, borne 8)

SPEEDUP REPRÉSENTATIF INTÉGRÉ : 18,0x à 22,3x selon les passes,
  contre le legacy RÉCHAUFFÉ
  obligatoire >= 5x : ATTEINT ; cible >= 10x : ATTEINTE
```

Référence historique distincte, non mélangée : contre le coût de production
mesuré en G2.4b (~0,38 s/évaluation, CAMB froid à chaque pas dans le bloc
unique), le même mélange restait de l'ordre de plusieurs dizaines de fois plus
rapide. Les deux références ne sont pas additionnées : la première mesure le
gain d'architecture à environnement égal, la seconde le gain contre le lot
historique.

Aucune régression scientifique, aucune croissance non bornée du cache, aucune
sursouscription de threads (les quatre plafonds sont exigés à 1).

## 18. Limites

```text
- la parité est démontrée sur les 4 variantes à leur graine gelée et sur les
  32 couples au niveau construction/métadonnées, pas sur le prior continu ;
- les comparaisons numériques portent sur P0-P3 des 4 variantes ; la
  couverture large reste celle de G2.4c (331 points), rejouée ici ;
- les mesures de performance sont indicatives : seuls les rapports et les
  comptages d'appels CAMB sont stables ;
- l'écriture atomique et le manifeste ne sont éprouvés que sous %TEMP% :
  leur comportement sur la racine réelle sera exercé à la première
  production autorisée, sous manifeste réel ;
- le budget de production reste NON_ETABLI : aucune projection de volume
  n'est adoptée par cette porte.
```

## 19. Risques ouverts

```text
- budget de production non établi : bloque toute production réelle ;
- l'ancien checkout synchronisé et les worktrees historiques restent des
  dettes séparées, interdits comme base de calcul ;
- la réécriture de l'historique sensible reste une porte distincte ;
- la première production exigera : budget ratifié, autorisation à deux clés
  au schéma étendu, et levée explicite du verrou.
```

## Verdict

```text
G2.4d PASSÉE — raccord qualifié, production fermée
```

Le chemin Cobaya directeur est désormais l'architecture qualifiée
`ReferenceLenteXZ` + `VraisemblanceRapideXZ` en `corrected-v1.1`, à parité
exacte de priors, refs, propositions, dérivés, prior joint, sampler et
graines avec l'oracle de régression. Les dettes du lanceur relevées par
INFRA-0/1 sont corrigées : contrat local consommé, threads exigés, capacité
mesurée sur la cible, garde technique séparée du budget, manifeste
atomiquement écrivable, identité de reprise complète, SHA du chemin rapide
obligatoire. Le verrou dur interdit toute écriture et tout `cobaya.run`, ce
qui est prouvé dynamiquement.

Cette validation **n'autorise toujours pas les chaînes**.
