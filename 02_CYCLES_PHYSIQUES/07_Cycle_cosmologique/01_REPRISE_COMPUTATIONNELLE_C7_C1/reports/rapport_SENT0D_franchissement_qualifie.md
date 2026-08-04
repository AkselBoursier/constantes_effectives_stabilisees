# SENT-0D1 — franchissement technique borné du verrou, qualifié sans MCMC

**Porte SENT-0D1 — issues #94 et #63 — 4 août 2026**
**Branche `comp/c7-c1-sent0d-franchissement`,
base `69155b38f90b09ccedd91f1c90224e44cd10b99c` (origin/main)**

```text
référence de ratification : SENT0D-2026-08-04-issue94-rat1   (publique)
VERROU_PRODUCTION_G2_4D   : True — INCHANGÉ
couple sentinelle         : M2a-N / 630101, seul couple pouvant franchir
production réelle         : FERMÉE — aucune écriture, aucun cobaya.run,
                            aucune autorisation privée réelle
```

Cette porte qualifie le **contrôle de flux** du franchissement, pas la
production. La séquence ultérieure reste : audit indépendant → merge
éventuel → nouveau pré-vol court → création privée de l'autorisation liée au
HEAD final → contrôle final → une seule MCMC `M2a-N/630101` → SENT-0F.

---

## 1. Fichiers modifiés

```text
scripts/run_mcmc_xz_g2_4.py                       (franchissement SENT-0D)
scripts/qualify_xz_sent0d_unlock.py               (nouveau)
reports/rapport_SENT0D_franchissement_qualifie.md (nouveau, ce rapport)
```

Rien d'autre : YAML G2.3, priors, grilles, graines, données, seuils,
background, likelihood, adaptateur, chemin rapide, qualificateurs G2.4d /
SENT-0B / CAP-1 existants et contrat local privé — tous **intacts**.

## 2. Architecture du franchissement

La constante n'est PAS remplacée par `False` :

```python
VERROU_PRODUCTION_G2_4D = True          # inchangé

# étape 8 :
if VERROU_PRODUCTION_G2_4D:
    garde_franchissement_sent0d(reference_franchissement, variante, graine)
```

`garde_franchissement_sent0d` refuse tout sauf le cas ratifié :

```text
VERROU=True + aucun franchissement demandé
    -> refus HISTORIQUE, même cause, même message « VERROU G2.4d : … »
VERROU=True + franchissement incorrect (référence, couple)
    -> refus SENT-0D sur cause exacte
VERROU=True + couple exact + autorisation privée exacte + référence exacte
    -> l'étape 9 peut être atteinte
```

Aucune variable d'environnement secrète, aucun fichier « unlock » mutable,
aucun comportement dépendant de l'heure ou de la date.

### Triple confinement

**A. Couple codé.** La garde 4 bis (`garde_perimetre_sentinelle`) reste
inchangée et bloquante : les 31 autres couples restent impossibles.
`garde_franchissement_sent0d` re-vérifie le couple en défense en profondeur.

**B. Autorisation privée exacte.** Deux contraintes OPTIONNELLES sont
ajoutées au validateur pur existant (`perimetre_exact_attendu`,
`reference_sentinelle_attendue`) — le validateur n'est pas dupliqué, et la
validation se fait **dans la même lecture/parsing** que la validation
existante : aucune fenêtre TOCTOU entre deux lectures du fichier. Pour un
franchissement, l'autorisation doit déclarer EXACTEMENT :

```json
{"variantes_graines_autorisees": {"M2a-N": [630101]},
 "reference_ratification_sentinelle": "SENT0D-2026-08-04-issue94-rat1"}
```

Toute extension — couple sentinelle PLUS un autre couple, deux graines,
autre variante — est refusée. Le champ `reference_ratification_sentinelle`
est une clé **optionnelle** du schéma (`CLES_MANIFESTE_OPTIONNELLES`) :
exigée pour le franchissement seulement, tolérée sinon — la qualification
générale G2.4d n'est pas cassée rétrospectivement, et toute AUTRE clé
étrangère reste refusée (« clés inexactes »).

**C. Intention opératoire explicite.** Le CLI exige exactement une
occurrence de :

```text
--franchissement-sent0d SENT0D-2026-08-04-issue94-rat1
```

Cette référence est PUBLIQUE : elle matérialise l'intention, elle n'est pas
un secret — la véritable seconde protection reste l'autorisation privée liée
au HEAD. Refusés sur cause exacte : flag absent (→ verrou historique), flag
dupliqué, valeur absente (fin d'arguments ou option à sa place), référence
vide, référence incorrecte. Le flag est analysé TÔT (étape 2 bis), pour que
tout défaut soit refusé sur sa propre cause et non par une garde fortuite.

## 3. Aucune écriture pendant cette passe

Le franchissement positif est prouvé PAR SENTINELLES (celles de G2.4d :
`mkdir`, `makedirs`, `open` en écriture, `os.replace`, `cobaya.run`) : avec
gardes amont satisfaites par le harnais minimal (arbre Git, budget déclaré,
autorisation substituée — les gardes réelles de contrat, environnement,
données, threads, chemins, support et admission de capacité restant
actives), le chemin **franchit réellement l'étape 8** et la première
opération filesystem post-verrou est interceptée par la sentinelle
`Path.mkdir` — **cela prouve le franchissement de l'étape 8 avant toute
écriture réelle**. Dans `_acquerir_repertoire_run`, ce premier appel peut
être celui du parent (`exist_ok=True`) ; **l'acquisition exclusive du
répertoire final demeure l'appel ultérieur `exist_ok=False`, déjà qualifié
par SENT-0B/B1** — la preuve de franchissement n'en dépend pas et B1 n'est
en rien affaibli.

```text
franchissement de contrôle : PROUVÉ   (sentinelle atteinte : [Path.mkdir],
                                       exactement une, la première)
écriture réelle            : AUCUNE
cobaya.run réel            : AUCUN
répertoire réel de run     : AUCUN
manifest.json réel         : AUCUN
autorisation privée réelle : AUCUNE
```

`produire()` n'est pas substitué : seul le trio minimal du harnais G2.4d
l'est, à l'identique de la preuve de verrou déjà ratifiée — le test n'est
pas vacant.

## 4. Qualification (`qualify_xz_sent0d_unlock.py`)

### Sections de la passe

```text
statique      : VERROU=True (AST + module) ; référence et périmètre exacts
                déclarés ; l'étape 8 appelle bien la garde (contrôle AST) ;
verrou hist.  : sans flag -> arrêt exact « VERROU G2.4d », zéro sentinelle ;
franchissement: avec flag exact -> étape 8 franchie, première opération
                filesystem post-verrou interceptée = exactement
                [Path.mkdir] (le parent, exist_ok=True — l'acquisition
                exclusive finale reste l'appel exist_ok=False, B1) ;
flag erroné   : refus « référence incorrecte », zéro sentinelle ;
autorisation  : nominale sentinelle admissible (groupes perimetre_sentinelle
                et reference_sentinelle traversés) ; le MÊME manifeste reste
                admissible par le validateur général, avec ou sans la clé
                optionnelle — rétro-compatibilité G2.4d prouvée.
```

### Fautes — 19, toutes détectées

```text
flag_errone_accepte                     flag_sans_valeur_accepte
flag_duplique_accepte                   flag_vide_accepte
sans_flag_ne_declenche_pas_le_verrou_historique
franchissement_hors_couple_accepte      garde_franchissement_neutralisee
perimetre_deux_graines_accepte          perimetre_couple_plus_variante_accepte
perimetre_autre_variante_seule_acceptee reference_sentinelle_absente_acceptee
reference_sentinelle_erronee_acceptee   perimetre_exact_neutralise
cle_etrangere_acceptee                  verrou_retire
etape8_sans_garde_franchissement
--- B3, correction après audit de PR #96 ---
autorisation_sha_seconde_lecture        autorisation_utf8_invalide_acceptee
autorisation_json_invalide_acceptee
```

### B3 — identité de l'autorisation liée aux octets validés (audit #96)

L'audit a identifié un bloqueur d'intégrité : `garde_autorisation` validait
le contenu parsé puis retournait `sha256_fichier(chemin)` — une **seconde
lecture**. Une mutation concurrente entre les deux pouvait produire
« contenu A validé, SHA de contenu B enregistré », cassant la provenance
que `sha256_autorisation` est censé attester.

Corrigé par **lecture unique** : les octets sont lus une fois, leur SHA-256
est calculé sur ces octets, puis ces mêmes octets sont décodés (UTF-8),
parsés (JSON) et validés — le SHA retourné est celui des octets
effectivement consommés et validés, sans aucune relecture du chemin.
Fichier absent, erreur de lecture, UTF-8 invalide et JSON invalide sont
refusés sur cause exacte.

L'épreuve `autorisation_sha_seconde_lecture` est non vacante : un fichier A
est écrit sous `%TEMP%` (marqué QUALIFICATION_ONLY — la validation profonde
est substituée par un espion précisément pour ne jamais produire une
autorisation réelle ; la chaîne lecture → SHA → décodage → parsing → appel
du validateur → retour du SHA reste la vraie, et `sha256_fichier` n'est pas
mocké). L'espion vérifie que l'objet validé est exactement celui parsé des
octets A, puis remplace le fichier par un contenu B **avant** le retour.
Attendus vérifiés : SHA retourné = SHA(A) ≠ SHA(B), fichier sur disque = B.
L'ancienne implémentation à double lecture aurait retourné SHA(B) : la
faute échouerait.

**Non-vacuité.** `garde_franchissement_neutralisee` neutralise la garde :
SANS flag, le chemin atteint alors la sentinelle post-verrou — preuve que la
garde réelle est ce qui bloque normalement. `perimetre_exact_neutralise`
montre que le même manifeste élargi, sans la contrainte, devient admissible
— la contrainte est ce qui refuse, pas un contrôle fortuit.
`etape8_sans_garde_franchissement` prouve par mutation de source que le
contrôle statique détecte un bloc d'étape 8 privé de la garde.

Cas « autre variante seule » : refusé en amont par la couverture du couple
demandé (`variantes_graines_autorisees`) — cause exacte consignée telle
quelle plutôt que maquillée en refus de périmètre.

## 5. Double passe et rejeux

```text
double passe SENT-0D : exit 0 / exit 0 — diff normalisé VIDE
qualify_xz_launcher_g2_4d.py : exit 0    (67/67)   — non modifié
qualify_xz_sentinel_sent0.py : exit 0    (30/30)   — non modifié
qualify_xz_capacity_cap1.py  : exit 0    (57/57)   — non modifié
qualify_xz_configs_g2_3.py   : exit 0               — non modifié
qualify_xz_optim_g2_4c.py    : exit 0               — non modifié
```

Aucun qualificateur antérieur n'a été réécrit pour « passer » : le refus
historique du verrou conserve sa cause et son message exacts, si bien que
les preuves de verrou de G2.4d et SENT-0B valent inchangées.

## 6. Ce que cette porte NE fait PAS

```text
aucun nouveau pré-vol ; aucune autorisation privée réelle ;
aucune commande de production ; aucun manifeste réel ; aucun run sentinelle.
```

La séquence reste : audit indépendant de cette PR → merge éventuel → pré-vol
court sur le HEAD final → création privée de l'autorisation liée à ce HEAD
exact → contrôle final → une seule MCMC `M2a-N/630101` → SENT-0F avant toute
seconde chaîne.
