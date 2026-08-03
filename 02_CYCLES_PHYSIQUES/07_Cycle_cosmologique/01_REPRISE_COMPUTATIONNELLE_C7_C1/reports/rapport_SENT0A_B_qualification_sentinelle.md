# SENT-0A/B — chemin de production sentinelle : implémentation et qualification

**Porte SENT-0A/B — issues #94 et #63 — 4 août 2026**
**Branche `comp/c7-c1-sent0-production-path`, base `4a1ec649e2072d5de501700b4351e56fc5948166` (origin/main)**

```text
M2a-N / 630101 = PROPOSÉ, NON AUTORISÉ
production réelle = FERMÉE
```

Cette porte implémente le chemin réel de production (étape 9) et le qualifie
**sous verrou**, sans MCMC réelle. Elle ne lance rien, n'autorise rien et
n'interprète rien.

```text
AUCUNE MCMC — AUCUN VRAI cobaya.run D'ÉCHANTILLONNAGE — AUCUNE MINIMISATION
AUCUN POSTERIOR — AUCUNE AUTORISATION RÉELLE
AUCUN MANIFESTE RÉEL SOUS LE PRÉFIXE DE PRODUCTION
VERROU_PRODUCTION_G2_4D = True, INCHANGÉ — AUCUN MERGE
```

---

## 1. Fichiers modifiés

```text
scripts/run_mcmc_xz_g2_4.py                                  (SENT-0A)
scripts/qualify_xz_sentinel_sent0.py                         (nouveau, SENT-0B)
reports/rapport_SENT0A_B_qualification_sentinelle.md         (nouveau, ce rapport)
```

Aucun autre fichier. En particulier, les quatre YAML G2.3,
`xz_background_g2_1.py`, `xz_likelihood_g2_3.py`, `xz_cobaya_g2_4.py`,
`xz_fast_g2_4c.py`, `qualify_xz_launcher_g2_4d.py`,
`qualify_xz_capacity_cap1.py`, les priors, grilles, graines, données, seuils
de convergence et le contrat public sont **intacts** (vérifié sur le diff).

## 2. SENT-0A — confinement sentinelle (garde 4 bis)

```python
SENTINELLE_SENT0_VARIANTE = "M2a-N"
SENTINELLE_SENT0_GRAINE = 630101
```

`garde_perimetre_sentinelle` est appelée dans `produire` en **4 bis** — après
HEAD et arbre propre, avant l'autorisation :

```text
1  injections            2  confirmation explicite
3  preflight complet     4  HEAD + arbre propre
4b garde du périmètre sentinelle          <- SENT-0A
5  autorisation          6  budget + admission capacité
7  plan pur + observateur 8 VERROU_PRODUCTION_G2_4D
9  chemin réel                            <- SENT-0A
```

Les 31 autres couples de la matrice sont refusés sur la cause exacte
« hors périmètre sentinelle », même si toutes les autres gardes étaient
satisfaites — prouvé par énumération automatique des 31 couples (31/31 refus
exacts) et par un test d'intégration où `produire("M2a-K", 630201)`, gardes
amont satisfaites, s'arrête sur cette cause **avant** l'autorisation.

Le confinement s'applique au mode `produire` seulement : le **pré-vol des
quatre variantes reste ouvert** (vérifié statiquement : `preflight` ne
référence pas la garde). Aucun privilège scientifique n'est accordé à
M2a-N — commentaire explicite dans le code ; les quatre variantes restent
co-primaires (G2.2a).

## 3. SENT-0A — étape 9 réelle

Le squelette « chemin de production non ouvert » est remplacé par
`executer_production_sentinelle(manifeste_initial, info_cobaya, prefixe)`,
qui reste **matériellement inatteignable** tant que le verrou vaut `True`
(le `raise` de l'étape 8 précède l'appel).

### 9.1 Répertoire

Re-contrôle de `garde_prefixe` et `garde_collision` au moment de l'exécution
(le temps a pu passer depuis le pré-vol), puis création. Jamais d'écrasement
ni de déplacement silencieux. **Sur échec après création, les traces —
répertoire, manifeste, sorties partielles — sont conservées pour audit,
jamais supprimées automatiquement.**

### 9.2 Manifeste initial

Écrit par `ecrire_manifeste_atomique` (la seule voie de création, qui refuse
tout écrasement non identique — **non détendue**), au statut initial
`PLANIFIE_NON_LANCE`, avec l'identité complète déjà définie : HEAD, SHA
lanceur/adaptateur/chemin rapide/descripteur/données, encodage scientifique,
sampler, environnement, autorisation, capacité, support, politique CAP-1,
référence de ratification. Aucun champ affaibli (contrôle :
`CHAMPS_MANIFESTE_RUN` au complet, `sha256_encodage_scientifique` identique
au recalcul indépendant).

### 9.3 Information Cobaya

Exclusivement le constructeur directeur `build_cobaya_info` ; aucun prior,
aucune vraisemblance, aucun fond réimplémentés. L'observateur de capacité est
injecté par le seul mécanisme qualifié (`garde_injection_observateur`, qui
refuse toute différence autre que `callback_function` et `callback_every`).
Le seul ajout opérationnel est `output` (le préfixe), postérieur au gel de
l'encodage scientifique — `sha256_encodage_scientifique` inchangé, vérifié.

### 9.4 Appel Cobaya

Point d'appel **unique** `_lancer_cobaya_production`, qui applique la
convention G1 ratifiée telle quelle après inspection de l'API 3.5
(`run(info_or_yaml_or_file, ..., resume=None, ...) -> (InputDict, Sampler)`) :

```python
cobaya_run(info, resume=True)
```

Aucune nouvelle sémantique de reprise : sous la garde de collision le
répertoire est toujours neuf, `resume=True` est inerte au premier lancement
et REC-1 reste inchangée. La qualification vérifie que l'appel transmet bien
`resume=True` et le préfixe exact.

### 9.5 Statuts de sortie — classement strict

```text
sampler.converged is True            -> CONVERGE
retour normal sans ce drapeau exact  -> FIN_SANS_CONVERGENCE
ArretCapaciteC7C1                    -> NON_CONVERGE_INTERRUPTION_CAPACITE
toute autre exception                -> NON_CONVERGE_ECHEC_TECHNIQUE
```

`CONVERGE` n'est **jamais** déduit d'un simple retour sans exception :
l'exigence est littéralement `converged_brut is True`. Un booléen non
canonique (entier 1, chaîne, numpy) classe le run `FIN_SANS_CONVERGENCE` —
direction conservatrice assumée et documentée. Aucune exception ne peut
écrire `CONVERGE` ; une exception non-capacité reste un échec technique
distinct, jamais reclassée.

### 9.6 Mise à jour atomique du manifeste

Nouvelle fonction dédiée `mettre_a_jour_manifeste_runtime`, limitée à :

```python
CHAMPS_RUNTIME_AUTORISES = ("statut_run", "date_fin_utc",
                            "detail_fin", "converged_cobaya")
```

Règles bloquantes : manifeste existant lisible ET conforme (schéma reconnu,
identité complète) sinon refus ; transitions uniquement de
`PLANIFIE_NON_LANCE` vers un statut final ; un statut final n'est jamais
réécrit — une interruption ne devient donc jamais une convergence ;
`CONVERGE` exige `converged_cobaya is True` dans la même mise à jour ;
défense en profondeur : chaque champ non runtime est **vérifié** inchangé
avant écriture. L'écriture est atomique (temporaire frère, fsync,
`os.replace`, fsync du répertoire). `ecrire_manifeste_atomique` n'est pas
détendue : l'écriture brute interne est privée au seul chemin déjà validé.

### 9.7 Checkpoints

Aucun checkpoint écrit ni fabriqué : seuls ceux de Cobaya existent. REC-1
(dette conditionnelle sur la fraîcheur du checkpoint à l'interruption) reste
inchangée. Aucune deuxième graine ni variante n'est lancée automatiquement.

## 4. SENT-0B — qualification sans MCMC réelle

`scripts/qualify_xz_sentinel_sent0.py` — passe complète et mode `--faute`.

### Substitut Cobaya

Le chemin post-verrou est exercé **exclusivement** via `SubstitutCobaya`, en
mémoire, qui simule : retour avec `converged=True` ; retour avec
`converged=False` ; absence d'attribut `converged` ; `ArretCapaciteC7C1` ;
exception technique. Aucun échantillonnage ; **aucune valeur de paramètre,
chi2 ou posterior générée ou publiée**. Les répertoires de test vivent sous
`%TEMP%`, hors Git, marqués `_QUALIFICATION_ONLY`, supprimés en fin de test.

### Preuves de la passe (sortie normalisée)

```text
statique   : VERROU_PRODUCTION_G2_4D = True (source AST + module chargé) ;
             couple sentinelle déclaré = (M2a-N, 630101) ;
verrou     : gardes amont satisfaites -> arrêt EXACT sur « VERROU G2.4d » ;
             AUCUNE sentinelle d'écriture (mkdir, makedirs, open-écriture,
             os.replace, cobaya.run) atteinte ; QUALIFICATION_ONLY rejeté ;
confinement: 31/31 couples non sentinelles refusés sur la cause exacte ;
             couple sentinelle admis par la garde ; preflight non contaminé ;
étape 9    : nominal simulé -> CONVERGE, converged_cobaya=true, objets créés
             = [manifest.json] exactement, 1 appel du substitut,
             resume=True transmis, output = préfixe exact, identité intacte,
             date de création conservée, encodage scientifique identique ;
sorties    : converged=False -> FIN_SANS_CONVERGENCE ;
             ArretCapaciteC7C1 -> NON_CONVERGE_INTERRUPTION_CAPACITE ;
             RuntimeError -> NON_CONVERGE_ECHEC_TECHNIQUE, traces conservées ;
observateur: injection minimale re-prouvée (exactement les deux champs) ;
confidentialité : aucune fuite (motifs CAP-1a réutilisés) sur les trois
             fichiers SENT-0.
```

### Fautes adversariales — 23, toutes détectées

```text
sentinelle_630102_acceptee            sentinelle_m2ak_acceptee
sentinelle_m2bn_acceptee              sentinelle_m2bk_acceptee
garde_sentinelle_vacante              produire_hors_sentinelle_atteint_l_autorisation
retour_sans_exception_classe_converge converged_non_canonique_classe_converge
capacite_reclassee                    echec_technique_reclasse
traces_supprimees_apres_echec         converge_sans_drapeau_explicite
interruption_reclassee                champ_scientifique_modifie
champ_runtime_inconnu                 manifeste_corrompu_mis_a_jour
manifeste_non_conforme_mis_a_jour     statut_final_reecrase
collision_prefixe_etape9              manifeste_existant_non_identique_etape9
verrou_retire                         cobaya_reel_appele
ecriture_sous_verrou_atteinte
```

`garde_sentinelle_vacante` est la mutation exigée : la garde neutralisée fait
disparaître le refus « hors périmètre » pour un couple non sentinelle, ce qui
prouve que les tests de confinement mordent sur la garde réelle et ne sont
pas vacants. `cobaya_reel_appele` prouve que le point d'appel réel est bien
intercepté par les sentinelles — la preuve « aucun cobaya.run » n'est pas
vacante non plus.

### Défaut de harnais trouvé et corrigé pendant la porte

La première passe complète a **échoué** (exit 1), et la cause est consignée
plutôt que corrigée en silence : le harnais substituait
`_lancer_cobaya_production` en entier, court-circuitant précisément la
convention `resume=True` qu'il prétendait vérifier — le contrôle rendait
`resume_kwarg: null`. La substitution a été déplacée **un niveau plus bas**
(`cobaya.run.run`), si bien que le vrai point d'appel du lanceur, avec sa
convention G1, est réellement exercé par la qualification. Après correction :
`resume_kwarg: true`, double passe verte.

## 5. Rejeux

```text
qualification SENT-0 (2 passes)  : exit 0 / exit 0, diff normalisé VIDE
qualify_xz_launcher_g2_4d.py     : exit 0   (67/67 fautes)
qualify_xz_configs_g2_3.py       : exit 0   (porte.echecs = [])
qualify_xz_optim_g2_4c.py        : exit 0   (porte.echecs = [])
qualify_xz_capacity_cap1.py      : exit 0   (57/57 fautes)
```

Aucun fichier scientifique gelé modifié ; verdicts scientifiques inchangés.

## 6. Limites restantes

```text
1. REC-1 inchangée : la fraîcheur du checkpoint Cobaya au moment d'une
   interruption n'est toujours pas garantie ; la reprise automatique peut
   être impossible et la garde refuse — rien n'est fabriqué ;
2. FIN_SANS_CONVERGENCE : dans Cobaya 3.5 mono-processus, la boucle ne rend
   la main normalement qu'à convergence ou à max_samples (infini ici) ; ce
   statut couvre donc surtout le cas défensif d'un converged non canonique.
   Il existe pour qu'aucun retour sans drapeau exact ne soit jamais promu ;
3. le chemin réel n'a jamais rencontré Cobaya réel : c'est l'objet du run
   sentinelle lui-même, après SENT-0C et décision humaine ;
4. la cadence réelle des checkpoints, la consommation disque réelle et le
   comportement de l'observateur en conditions réelles restent à mesurer
   (SENT-0E/F).
```

## 7. Verdict

```text
SENT-0A/B : chemin réel implémenté et qualifié SOUS VERROU
M2a-N / 630101 = PROPOSÉ, NON AUTORISÉ
production réelle = FERMÉE
prochaine étape : audit indépendant de la PR, puis SENT-0C, puis décision
humaine distincte sur le run réel
```
