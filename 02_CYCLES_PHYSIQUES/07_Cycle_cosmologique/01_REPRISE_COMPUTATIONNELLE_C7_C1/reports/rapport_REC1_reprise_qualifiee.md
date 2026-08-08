# REC-1 — la reprise d'un run interrompu, implémentée et qualifiée

**Porte REC-1 — issues #94 et #63 — 8 août 2026**
**Branche `comp/c7-c1-rec1-reprise`,
base `05e13bb7c07d2d070d16574c3c58edf488bea8d0` (origin/main)**
**Ratification : `REC1-2026-08-07-issue94-rat1`**

```text
AUCUNE REPRISE RÉELLE — AUCUNE MCMC — AUCUNE AUTORISATION DE REPRISE RÉELLE
LE RUN SENTINELLE EN COURS N'A JAMAIS ÉTÉ TOUCHÉ (préfixe réel non visité)
VERROU_PRODUCTION_G2_4D = True — AUCUN MERGE avant clôture de SENT-0F
```

Motivation empirique (SENT-0E/F) : checkpoints Cobaya toutes les
~2-3,5 minutes ; deux interruptions externes reprenables mais non reprises
(~17 h de CPU perdues) ; reprise structurellement interdite jusqu'ici.

---

## 1. Fichiers modifiés

```text
scripts/run_mcmc_xz_g2_4.py               (mode --reprendre + gardes REC-1)
scripts/qualify_xz_rec1_reprise.py        (nouveau)
reports/rapport_REC1_reprise_qualifiee.md (nouveau, ce rapport)
```

Objets scientifiques gelés, qualificateurs antérieurs, contrats public et
privé : **intacts**.

## 2. Architecture

### États reprenables — et eux seuls

```text
PLANIFIE_NON_LANCE                  (kill externe : aucun handler n'a pu
                                     finaliser — cas réels attempt1/2)
NON_CONVERGE_INTERRUPTION_CAPACITE  (arrêt propre par l'observateur)
```

Refusés sur cause exacte : `CONVERGE` (« un run convergé n'est JAMAIS
repris »), `NON_CONVERGE_ECHEC_TECHNIQUE` et `FIN_SANS_CONVERGENCE`
(« audit humain préalable obligatoire »), `EN_REPRISE` (reprise déjà en
cours ou non clôturée), statut inconnu, manifeste absent/corrompu/non
conforme.

### Mode CLI `--reprendre`

```text
--reprendre M2a-N 630101 --je-confirme-la-reprise
    --autorisation <fichier privé>
    --franchissement-sent0d <référence publique SENT-0D>
    --ratification-reprise <référence publique REC-1>
```

Mêmes verrou, franchissement SENT-0D et confinement sentinelle que la
production (garde 4 bis inchangée : 31 autres couples impossibles tant que
SENT-0 n'est pas close). La reprise est toujours une commande humaine : le
flag `--ratification-reprise` est OBLIGATOIRE, unique, à valeur non vide.
`--produire` continue de refuser tout préfixe occupé (B1 non détendu) :
seul `--reprendre` accepte un run existant, sous les gardes ci-dessous.

### `garde_reprise_rec1` — exigences cumulatives, lecture seule

```text
manifeste conforme (schéma -1/-2/-3 reconnu, identité complète) ;
statut REPRENABLE (voir ci-dessus) ;
checkpoint Cobaya présent, non vide, analysable, bloc sampler —
  JAMAIS fabriqué ni réparé ;
identité scientifique STRICTE, RECALCULÉE (jamais crue sur parole) :
  sha256_encodage_scientifique recalculé == manifeste ;
  descripteur, données, empreinte d'environnement == manifeste ;
  racine de runs canonique identique ;
politique de capacité == valeurs RATIFIÉES courantes (comparaison exacte
  Decimal : budget 20, reprise 1,15, volume 40, cap1-1.1.0, référence) ;
admission CAP-1 rejouée À L'INSTANT de la reprise.
```

### Transition de HEAD — règle centrale (§5 de la directive)

La garde détecte `manifeste.head != HEAD courant` et la signale ; c'est le
**validateur d'autorisation** — dans la même lecture que tout le reste du
fichier, sans fenêtre TOCTOU — qui exige alors une entrée EXACTE dans
`transitions_head_autorisees` (`{origine, reprise}`) portée par
l'autorisation privée, en plus de `reference_ratification_reprise`. Sans
ratification : refus « transition de HEAD non ratifiée », même à science
identique. Les deux champs sont des clés OPTIONNELLES du schéma
d'autorisation : exigés en reprise seulement — le validateur général et
toutes les qualifications antérieures restent inchangés (prouvé).

### Manifeste — schéma `c7c1-run-manifest-3`

La CRÉATION d'un run reste au schéma `-2` ; c'est la première reprise qui
promeut le manifeste en `-3` :

```text
statut EN_REPRISE (transitoire, posé par la SEULE fonction dédiée
  enregistrer_reprise) ;
historique_reprises APPEND-ONLY — événements aux champs EXACTS :
  {date_utc, head_origine, head_reprise, reference_ratification_reprise,
   sha256_autorisation_reprise, sha256_checkpoint_au_moment_de_la_reprise} ;
enregistrer_reprise vérifie champ par champ que SEULS schema, statut_run
  et historique_reprises changent, que l'historique existant est un
  préfixe intact du nouveau, et que head_origine == head du manifeste ;
la finalisation B2 (mettre_a_jour_manifeste_runtime) accepte désormais
  EN_REPRISE comme état PRÉ-FINAL, au même titre que PLANIFIE_NON_LANCE —
  rien d'autre ne change : ensemble complet exigé d'un coup, statut final
  jamais réécrit, invariant CONVERGE <=> converged_cobaya is True ;
les archives -2 (attempt1/2) restent valides et ne sont jamais réécrites.
```

### Acquisition exclusive de reprise

Même primitive que B1 : `mkdir(exist_ok=False)` d'un répertoire
`.reprise.actif` dans le répertoire du run — au plus un processus reprend
un run donné. La clôture se fait par **renommage** en `.reprise.NNN.clos`
(trace conservée, jamais de suppression) ; un verrou résiduel d'une
reprise tuée BLOQUE toute nouvelle reprise — fail-closed, levée humaine
après audit.

### Exécution (`executer_reprise_sentinelle`)

```text
verrou -> enregistrer_reprise (EN_REPRISE, atomique) -> Cobaya par le
point d'appel UNIQUE existant, run(info, resume=True) sur le préfixe
EXISTANT (convention G1 inchangée) -> classification STRICTE identique à
la production (CONVERGE ssi sampler.converged is True) -> finalisation
monotone -> clôture du verrou. Sur exception : finalisation
INTERRUPTION_CAPACITE ou ECHEC_TECHNIQUE, verrou clos, traces conservées,
exception propagée. Un run retombé en INTERRUPTION est reprenable À
NOUVEAU (cycle prouvé).
```

## 3. Qualification (`qualify_xz_rec1_reprise.py`)

Tout en SYNTHÉTIQUE sous `%TEMP%` : manifestes construits par la vraie
`identite_run` (marqués QUALIFICATION_ONLY), checkpoints d'essai,
substitut contrôlé de `cobaya.run` substitué SOUS le point d'appel réel —
la convention `resume=True` est réellement exercée et vérifiée. **Le
préfixe réel du run sentinelle en cours n'est jamais visité.**

Substitution déclarée : `mesurer_occupation_lot` est remplacée par un stub
déterministe (occupation nulle) pendant la qualification — un run réel
ratifié écrit actuellement sous la racine de runs, et la fonction réelle
est l'objet de CAP-1, pas de cette porte.

### Preuves de la passe

```text
statique   : VERROU=True ; états reprenables exacts ; schéma -3 reconnu ;
             création restée au schéma -2 ; clés optionnelles REC-1 ;
nominale   : garde passe (même HEAD) -> EN_REPRISE -> substitut
             (resume=True, output=préfixe existant) -> CONVERGE avec
             converged_cobaya=true -> schéma promu -3, historique de
             longueur 1 aux champs exacts, verrou clos .reprise.001.clos,
             identité intacte ;
cycle      : INTERRUPTION -> reprise -> ArretCapaciteC7C1 (substitut) ->
             INTERRUPTION à nouveau -> seconde reprise -> CONVERGE ;
             historique longueur 2, premier événement intact
             (append-only), verrous .001.clos et .002.clos ;
transition : manifeste créé sous un autre HEAD -> la garde détecte ;
             sans entrée ratifiée -> refus sur cause exacte ; avec
             l'entrée exacte -> admise (groupes reference_reprise et
             transition_head traversés) ;
rétro-comp : le validateur général (sans contraintes REC-1) accepte
             toujours une autorisation SENT-0D nominale — les
             qualifications antérieures ne sont pas cassées.
```

### Fautes — 27, toutes détectées

```text
checkpoint_absent / checkpoint_vide / checkpoint_corrompu
statut_converge_repris / statut_echec_technique_repris /
statut_fin_sans_convergence_repris / reprise_deja_en_cours
manifeste_absent / manifeste_corrompu
identite_scientifique_differente / donnees_differentes /
environnement_different
head_different_sans_ratification
reference_reprise_absente / ratification_reprise_cli_absente /
ratification_reprise_cli_dupliquee / reprise_hors_couple_sentinelle
evenement_reprise_incomplet / evenement_head_origine_different /
historique_non_liste / reprise_concurrente
double_finalisation_apres_reprise / admission_cap1_refusee_en_reprise
reprise_sans_checkpoint_ne_fabrique_rien
production_sur_prefixe_occupe_toujours_refusee
garde_reprise_neutralisee (mutation de non-vacuité) / verrou_retire
```

`garde_reprise_neutralisee` prouve la non-vacuité : la garde neutralisée
fait disparaître le refus d'un run CONVERGE — c'est bien elle qui bloque.
`reprise_sans_checkpoint_ne_fabrique_rien` vérifie qu'après le refus le
checkpoint est TOUJOURS absent : rien n'est fabriqué.

## 4. Séquencement des rejeux — publié avant exécution

Le run sentinelle attempt3 (ratifié SENT0F2) tourne pendant cette porte.
Sa seule existence rend deux hypothèses-monde des qualificateurs
antérieurs légitimement fausses : le préfixe sentinelle est OCCUPÉ (les
preuves de verrou G2.4d/SENT-0B/SENT-0D s'arrêteraient sur « collision »)
et l'occupation de production n'est plus nulle (assertion « zéro » de
CAP-1 sans objet). Décision publiée dans #94/#63 AVANT exécution :

```text
les rejeux des six qualificateurs antérieurs sont DIFFÉRÉS à la fin
d'attempt3 et seront exécutés et publiés AVANT tout merge — le merge
étant de toute façon interdit avant la clôture de SENT-0F.
```

Aucun qualificateur gelé n'a été modifié.

## 5. Double passe

```text
qualification REC-1 : exit 0 / exit 0 — diff normalisé VIDE
fautes              : 27 / 27
confidentialité     : aucune fuite (motifs CAP-1a, 3 fichiers)
```

## 6. Limites restantes

```text
1. la levée d'un verrou de reprise résiduel (.reprise.actif orphelin)
   est volontairement manuelle — fail-closed ;
2. la reprise réelle exigera : merge post-audit + autorisation privée
   portant les champs REC-1, créée à ce moment-là, liée au HEAD final,
   sur décision humaine distincte ;
3. la fraîcheur du checkpoint reste celle que Cobaya offre (learn_every,
   ~2-3,5 min mesurées) : la perte maximale à l'interruption est bornée
   par ce cycle — mesuré, non garanti par contrat.
```
