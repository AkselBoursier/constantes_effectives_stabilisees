# REJ-1 — hypothèses-monde des qualifications et durcissement opératoire

**Porte REJ-1 — issues #94 et #63 — 10 août 2026**
**Branche `comp/c7-c1-rej1-monde-production`,
base `05e13bb7c07d2d070d16574c3c58edf488bea8d0` (origin/main)**
**Ratification : `REJ1-2026-08-10-issue94-rat1`**

```text
AUCUNE MCMC — AUCUNE REPRISE — AUCUN OBJET SCIENTIFIQUE MODIFIÉ
INCIDENT I/O POST-GEL ANTÉRIEUR AUX CORRECTIONS, CONSERVÉ ET EMPREINTÉ
VERROU_PRODUCTION_G2_4D = True — AUCUN MERGE avant audit indépendant
```

## 1. Motivation (SENT-0F §8)

Depuis SENT-0E, la racine de runs porte LÉGITIMEMENT de la production
ratifiée : le run sentinelle gelé (statut PLANIFIE_NON_LANCE, reprenable)
et deux archives d'incidents. Deux hypothèses-monde des qualificateurs
antérieurs sont donc devenues fausses pour une raison légitime :

```text
« le préfixe sentinelle est libre »  -> les preuves de verrou et de
   franchissement, qui doivent PARVENIR à l'étape verrouillée, mordent
   désormais en amont sur garde_collision : preuve VACANTE ;
« l'occupation de production est nulle » -> l'assertion « zéro » de
   CAP-1 et le seuil initial 61,15 Gio ne décrivent plus le monde.
```

Et trois leçons opératoires payées par les incidents réels exigent un
durcissement : timeout de harnais (attempt1), gel console QuickEdit
(attempt3), absence de battement de vie positif de l'observateur.

### 1.1 Incident de qualification découvert pendant REJ-1

Avant le confinement ajouté par la présente correction, les exercices
nominal et mutants de CAP-1 appelaient le callback I/O avec la vraie
`C7C1_XZ_OUT_DIR`. Ils ont créé après le gel scientifique :

```text
<RUNS>/g2_4/P_WS/M2a-N/s630101/observateur.heartbeat
création UTC       : 2026-08-10T06:50:00.9731365Z
dernière écriture  : 2026-08-10T06:52:16.1533377Z
taille             : 666 octets, 7 lignes synthétiques
SHA-256            : F1525A29975C2AC6041B61DCE43D75E6C16C77BB7C643AE2BF421E287399C90C
```

La dernière écriture scientifique du run est antérieure
(2026-08-10T04:13:36Z). Cet ajout est donc une contamination
opérationnelle post-gel par qualification, non une sortie du sampler.
Il n'est ni supprimé ni corrigé rétroactivement : l'incident et son
empreinte sont conservés. Son allocation NTFS ajoute 4 096 octets à la
mesure CAP-1 (occupation courante : 355 397 632 octets). Après
confinement, tous les callbacks exercés par CAP-1 ciblent une racine
synthétique temporaire ; REJ-1 vérifie les sept sites d'appel par AST et
injecte la faute `qualification_callback_touche_run_reel`. Tous les
rejeux post-correction ont laissé taille, dates et SHA-256 ci-dessus
inchangés.

## 2. État rouge documenté AVANT adaptation

Rejeux des quatre qualificateurs avec le run gelé en place, avant toute
modification (captures conservées hors Git) — 9 échecs, tous imputés :

```text
G2.4d   (exit 1) : preuve du verrou vacante — collision au préfixe
                   <RUNS>/g2_4/P_WS/M2a-N/s630101 avant l'étape 8
SENT-0B (exit 1) : même cause unique (il importe _verrou_nominal)
CAP-1   (exit 1) : même preuve de verrou vacante ; « budget consommé non
                   nul alors qu'aucun run réel n'existe : 355 393 536
                   octets » ; « seuil initial 60,819... != 61,15 Gio »
                   (l'écart est EXACTEMENT l'occupation mesurée : la
                   mécanique d'admission déduit correctement le consommé)
SENT-0D (exit 1) : 4 échecs — franchissement n'atteignant pas l'étape 9,
                   refus historique masqué par la collision, première
                   opération post-verrou vide, faute
                   garde_franchissement_neutralisee non détectée
```

Constat central : la MESURE est partout irréprochable (l'inventaire
attribue exactement le run gelé et les deux archives) ; seules les
ATTENTES des qualificateurs supposaient un monde sans production.

## 3. Adaptations — chaque modification d'un qualificateur, justifiée

Principe : AUCUNE garde de production n'est modifiée ; seuls les
HARNAIS de preuve changent (une substitution de plus dans une famille
qui existait déjà), et chaque adaptation reçoit ses contrôles de
non-vacuité prouvant que la vraie garde mord toujours et que la
substitution ne fuit pas.

### 3.0 Constat préalable — la voie « racine synthétique » est fermée, et c'est une bonne nouvelle

La directive offrait deux voies. La première (pointer les preuves vers
une racine synthétique vide via la variable d'environnement) a été
implémentée puis REFUSÉE PAR LE DISPOSITIF LUI-MÊME :

```text
GardeErreur: C7C1_XZ_OUT_DIR diffère du contrat local (champ runs)
```

Le contrat privé INFRA-1 épingle la racine de runs, et cette garde ne
doit pas être affaiblie pour le confort d'une preuve. Constat d'audit
positif : l'épinglage fonctionne exactement comme conçu. La seconde voie
de la directive est donc retenue : substitution de `garde_collision`
dans le harnais déjà existant.

### 3.1 `qualify_xz_launcher_g2_4d.py` — `_verrou_nominal`, scénario 1

`garde_collision` rejoint, pour le SEUL scénario 1 (« amont satisfait »),
la famille des gardes que la qualification ne peut pas satisfaire
réellement — arbre Git propre, budget déclaré, autorisation privée — et
auxquelles ce harnais substitue déjà des doublures, restaurées dans le
même `finally`. Le monde occupé est exactement de cette famille : la
preuve doit PARVENIR à l'étape 8, or le préfixe réel est légitimement
pris. Le scénario 2 (« amont réel ») conserve TOUTES les vraies gardes :
son refus précoce est aujourd'hui la vraie `garde_collision` sur le
monde occupé — enregistré et ASSERTÉ comme tel par REJ-1. Un point
d'adaptation couvre TROIS qualificateurs (G2.4d, SENT-0B et CAP-1
importent la même preuve). Les sentinelles filesystem du harnais
interdisent par ailleurs TOUTE écriture réelle, préfixe réel compris.

### 3.2 `qualify_xz_sent0d_unlock.py` — `_produire_sous_sentinelles`

Même substitution, même `finally`, même justification. Les quatre échecs
SENT-0D (franchissement, refus historique, première opération
post-verrou, faute neutralisée) provenaient tous de cette unique
fonction. La vraie `garde_collision` reste qualifiée par SENT-0B
(`collision_prefixe_etape9`, acquisition exclusive B1 — rejoués verts)
et par le contrôle unitaire de REJ-1 (refus d'un préfixe synthétique
occupé, passage d'un préfixe libre), et la RESTAURATION de la
substitution après chaque harnais est assertée par REJ-1 (une fuite
neutraliserait la garde pour la suite du processus).

### 3.3 `qualify_xz_capacity_cap1.py` — occupation et seuil

```text
« zéro inconditionnel »   ->  COHÉRENCE occupation <-> manifestes :
  octets_production == 0  SSI aucun manifeste de production sous la
  racine (hors sous-arbres temporaires reconnus), incohérence signalée
  DANS LES DEUX SENS (mesure qui invente ou qui perd de la production) ;
  l'assertion « zéro » d'origine reste éprouvée TELLE QUELLE sur une
  racine synthétique vide (helpers _manifestes_production_reels et
  _verdict_occupation_monde, éprouvés par table de vérité complète).

« seuil == 61,15 »        ->  IDENTITÉ exacte : seuil courant ==
  61,15 Gio ratifiés MOINS l'occupation de production mesurée
  (tolérance 1e-9) ; et la valeur RATIFIÉE initiale 61,15 reste éprouvée
  TELLE QUELLE sur racine synthétique vide. L'occupation réelle est
  publiée comme MESURE, plus jamais comme échec.
```

Aucune autre ligne de CAP-1 n'est modifiée ; les probes d'admission
(seuil exact accepté, seuil − 1 octet refusé, 45 et 39 Gio refusés)
restent relatives au seuil courant et n'ont pas changé.

### 3.4 Ce qui n'a PAS été modifié

`qualify_xz_configs_g2_3.py`, `qualify_xz_optim_g2_4c.py` (gelés,
inchangés, rejoués), tous les objets scientifiques gelés, toutes les
gardes de production du lanceur, `qualify_xz_rec1_reprise.py` (branche
REC-1, intact).

## 4. Durcissement opératoire

### 4.1 `driver_production_c7c1.ps1` (nouveau, public)

Contrat, éprouvé statiquement ET dynamiquement :

```text
AUCUN timeout    : WaitForExit() sans argument ; les formes -Timeout,
                   TimeoutSec, WaitForExit(ms), Stop-Process, taskkill
                   sont INTERDITES par contrôle statique ;
AUCUNE console   : processus scientifique détaché, fenêtre cachée,
                   stdout/stderr redirigés vers fichiers — le gel
                   QuickEdit devient structurellement impossible ; le
                   driver lui-même n'écrit RIEN sur la console (toute
                   narration dans son journal fichier) ;
journal          : capté d'abord sous le sous-arbre temporaire reconnu,
                   puis AJOUTÉ (append prouvé, jamais d'écrasement) à
                   chain.console.log DANS le répertoire du run APRÈS la
                   fin du processus — jamais pendant, et jamais créé
                   avant l'acquisition exclusive B1 (un arrêt antérieur
                   à l'acquisition laisse les journaux en staging, tracé);
enregistrement   : heure UTC, PID, mode, méthode, code de sortie ;
AUCUNE relance   : le driver consigne et se termine ;
AUCUN chemin privé dans le fichier (enveloppe + paramètres seulement) ;
pwsh 7+ exigé    (leçon SENT-0F2 : PowerShell 5.1 a tué un driver muet).
```

### 4.2 Battement de vie de l'observateur (lanceur, seule modification)

Le callback est injecté uniquement dans
`sampler.mcmc.callback_function` avec `callback_every=1000`. Dans Cobaya
3.5 il est appelé sur une nouvelle acceptation lorsque le poids courant
vaut 1 et que `n() % callback_every == 0`. Il ajoute dans le répertoire
du run une ligne UTF-8 contenant timestamp UTC, numéro d'appel, nombre
de lignes et mesures d'espace (`free_gio`, `run_gio`, `lot_gio`). À
l'acceptance mesurée de la sentinelle (2,297 acceptés/s), la cadence
attendue est environ 7,25 min, soit environ 992 appels en 120 h — et non
la cadence de 2 min des contrôles/checkpoints.

```text
append SEULEMENT (mode « a » exigé statiquement) ;
AUCUNE surface d'injection nouvelle : differences_injection reste
  exactement [callback_every, callback_function] — prouvé ;
AUCUN champ nouveau du manifeste ; AUCUN objet scientifique touché ;
une `OSError` d'ouverture/append est avalée : une panne I/O ordinaire du
  heartbeat n'arrête pas la chaîne ; une exception de programmation
  d'une autre classe n'est pas avalée et peut remonter par le callback,
  donc interrompre la chaîne ;
le callback ne modifie ni l'état du sampler ni la cible scientifique :
  il est non-mutant vis-à-vis du sampler, mais PAS pur au sens
  opérationnel puisqu'il lit l'occupation et écrit un heartbeat ;
taille typique mesurée : 97 octets/ligne, soit environ 96 Kio/120 h ;
microbenchmark append (5 x 1000, répertoire temporaire) : médiane
  1 396,2 microsecondes par ouverture-ajout-fermeture (1,27–1,51 ms),
  soit environ 1,4 s/120 h ou 0,00032 % ;
scan CAP post-run, lecture seule, 50 appels : médiane 130,91 ms,
  P95 272,39 ms, maximum 286,0 ms, soit environ 130 s/120 h ou 0,030 %.
```

## 5. Qualification (`qualify_xz_rej1_monde.py`, nouveau)

Nominale : preuves de monde probantes SUR LE MONDE OCCUPÉ (verrou
atteint, franchissement jusqu'à l'acquisition exclusive, restauration de
la substitution assertée après chaque harnais, scénario 2 refusé par la
VRAIE collision, contrôle unitaire de la garde dans les deux sens, table
de vérité occupation/manifestes, exclusion des temporaires) ; battement
statique
(AST : fichier déclaré, append seul) et dynamique (2 appels = 2 lignes,
seul fichier ajouté, format, défaillance avalée, injection minimale) ;
driver statique (motifs interdits/requis) et dynamique (4 passages réels
sous pwsh sur charge inoffensive en monde synthétique : journal créé,
entêtes, stdout/stderr captés, append inter-passages prouvé, silence
console prouvé, arrêt avant acquisition tracé, code enfant 7 propagé par
le driver et journalisé) ; confidentialité des trois surfaces publiques
REJ-1.

### Fautes — 17, toutes détectées

```text
collision_reelle_neutralisee          substitution_collision_fuit
occupation_inventee_signalee          production_perdue_signalee
manifeste_sous_temporaire_ignore
heartbeat_retire                      heartbeat_ecrase
heartbeat_hors_du_run
qualification_callback_touche_run_reel
driver_timeout_introduit              driver_timeout_wait_process
driver_console_reintroduite           driver_narration_console
driver_journal_ecrase                 driver_tue_le_processus
driver_chemin_prive                   driver_masque_code_sortie
```

Les deux premières prouvent la NON-VACUITÉ de l'adaptation : une vraie
garde neutralisée est vue par le contrôle unitaire (un préfixe occupé
doit être refusé), et une substitution de harnais qui FUIRAIT (non
restaurée) est vue par le contrôle de restauration.
`heartbeat_hors_du_run` importe une COPIE falsifiée du lanceur (battement
détourné vers manifest.json) et vérifie que l'exercice dynamique détecte
le débordement.

## 6. Double passe et rejeux — TOUS avec le run gelé en place

```text
qualification REJ-1 : exit 0 / exit 0 — diff normalisé VIDE
SHA-256 normalisé   : 075dc0237d3fcd71f12856d9bbe1c54ffac87a316aaab079e4683275b863b37c
fautes              : 17 / 17
rejeux (ordre chronologique des portes) :
  G2.3a    (configs)       : exit 0, porte sans échec
  G2.4d    (lanceur)       : exit 0, 67/67 fautes
  CAP-1    (capacité)      : exit 0, 57/57 fautes
  SENT-0B  (sentinelle)    : exit 0, 30/30 fautes
  SENT-0D  (franchissement): exit 0, 19/19 fautes
  REC-1    (branche #100)  : exit 0, 27/27 fautes (replay directeur)
confidentialité     : aucune fuite (motifs CAP-1a, 3 fichiers REJ-1)
```

## 7. Limites restantes

```text
1. le driver n'est pas encore l'outil d'un lancement réel : la prochaine
   production/reprise réelle devra l'utiliser (protocole natif privé mis
   à jour), c'est une décision humaine distincte ;
2. le run gelé porte déjà le heartbeat synthétique décrit en §1.1 ; il
   reste conservé comme trace d'incident et ne constitue pas une mesure
   scientifique ni une preuve d'observation pendant attempt3 ;
3. la consolidation du journal est post-mortem : pendant le run, la
   sortie vit dans le sous-arbre temporaire reconnu (hors production,
   par construction CAP-1) — un kill du driver la laisse en staging,
   consignée, jamais perdue ;
4. REC-1 (PR #100) et REJ-1 restent non mergées. Leur ordre, leur rebase
   éventuel et tout merge sont des décisions humaines encore ouvertes.
```
