# CAP-1 — matérialisation et qualification de la politique de capacité

**Portes CAP-1 (2 août 2026) et CAP-1a (3 août 2026) — issues #90 et #63**
**Branche `comp/c7-c1-capacity-policy`, base `ef0623b8`**

CAP-1a ferme les deux constats de l'audit de PR #92 : le support ratifié est
lié **explicitement au volume C** (constante normative, jamais
`%SystemDrive%`), et la valeur réelle de l'empreinte de volume est retirée de
toute surface publique — présence et conformité seules restent publiées. La
politique de capacité passe en version `cap1-1.1.0` ; les valeurs ratifiées
20 / 1,15 / 40 / `CAP0-2026-08-02-issue90-rat1` sont strictement inchangées.

CAP-0 a **mesuré**. La ratification humaine du 2 août 2026 a **décidé**. CAP-1
**matérialise** cette décision et vérifie qu'elle produit les gardes attendues.
Aucune valeur ratifiée n'est réévaluée ici.

```text
AUCUNE MCMC — AUCUNE MINIMISATION — AUCUN POSTERIOR
AUCUNE AUTORISATION RÉELLE — AUCUN MANIFESTE DE RUN RÉEL
AUCUNE CHAÎNE CRÉÉE — AUCUN PRIOR, GRAINE OU CRITÈRE R−1 MODIFIÉ
AUCUN max_samples AJOUTÉ — VERROU_PRODUCTION_G2_4D RESTE True
AUCUNE SUPPRESSION, AUCUNE MIGRATION, AUCUN CHANGEMENT DE SUPPORT
```

---

## 1. Contrat privé — schéma 1.3.0

Le contrat local privé, hors dépôt, passe de `1.2.0` à `1.3.0`. La section
`racine_runs` porte désormais :

```text
garde_technique_minimale_Gio  : 40                             (inchangé)
budget_production_requis_Gio  : 20
budget_production_statut      : RATIFIE
reference_ratification_budget : CAP0-2026-08-02-issue90-rat1
reserve_reprise_Gio           : 1.15
reserve_volume_minimale_Gio   : 40
politique_capacite_version    : cap1-1.1.0
volume_ratifie                : C                              (CAP-1a)
```

Le statut **global** reste `PREPARATION_ONLY`. La ratification du budget ne
vaut donc pas autorisation de production : elle borne une enveloppe de
stockage, rien de plus.

La racine `runs` du contrat est vérifiée sur le volume ratifié — lettre
comparée à la constante `C`, lecteur fixe, NTFS — à chaque appel de
`garde_contrat_local`, qui exige en outre que le contrat **déclare**
`volume_ratifie = "C"`. La qualification **matérielle**, plus coûteuse,
appartient au pré-vol (`garde_support_actif`), conformément au §6 de la
directive.

Aucun chemin privé n'est publié. L'enveloppe locale privée a été mise à
niveau en conséquence : elle exige à son tour `1.3.0`, `RATIFIE`, et les
quatre valeurs de capacité, comparées en décimal exact.

## 2. Sémantique exacte des réserves

```text
budget_total          = 20 Gio                     (ratifié)
budget_deja_consomme  = octets réellement alloués aux produits de runs
                        C7-C1 présents sous <RUNS>, hors sous-arbres
                        temporaires reconnus et hors produits non
                        attribués à un manifeste de run
allocation_run_actif  = enveloppe S8 conservatrice du type de run courant
budget_restant_alloue = max(0, budget_total − budget_deja_consomme
                                            − allocation_run_actif)
reserve_reprise       = 1.15 Gio                   (ratifiée)
reserve_volume        = 40 Gio                     (ratifiée)
```

**`budget_restant_alloue` est ce qui reste du budget total UNE FOIS le run
courant provisionné.** C'est pourquoi la règle d'admission le ré-ajoute
explicitement : il n'y a pas de double comptage, parce que l'allocation a été
soustraite en amont.

### Allocations S8 — recalculées, non recopiées

Depuis les constantes de mesure publiées en CAP-0 :

```text
lignes S8 par run = 8 × 219 400 = 1 755 200
octets par ligne (borne empirique, 18,36 o/colonne) : M2a 349 | M2b 331
enveloppe auxiliaire = pire ratio mesuré 0,845 %
```

| grille | chaîne S8 | auxiliaire | `allocation_run_actif` |
|---|---:|---:|---:|
| M2a | 612 564 800 o = 0,570495427 Gio | 0,004820686 Gio | **0,575316113 Gio** |
| M2b | 580 971 200 o = 0,541071594 Gio | 0,004572055 Gio | **0,545643649 Gio** |

Contrôles croisés avec le rapport CAP-0 publié, tous concordants :

```text
B_chain(S8) = 16 × M2a + 16 × M2b = 17,785 Gio        (publié : 17,785)
B_aux(S8)   = 0,845 % de B_chain  =  0,150 Gio        (publié : 0,150)
B_actif(S8) = B_chain + B_aux + 1,0 Gio = 18,94 Gio   (publié : 18,94)
plus gros run seul (chaîne M2a S8)      = 0,570 Gio   (publié : 0,570)
2 × allocation M2a = 1,1506 Gio  ->  reserve_reprise ratifiée 1,15 Gio
```

### Règle d'admission

```text
espace_libre >= budget_restant_alloue + allocation_run_actif
              + reserve_reprise + reserve_volume
```

Au début du lot, `budget_deja_consomme = 0`, donc

```text
seuil = (20 − 0 − 0,575316113) + 0,575316113 + 1,15 + 40 = 61,15 Gio
```

exactement la réservation ratifiée. La garde mesurée rend
`seuil_admission_gio = 61.15`.

### Note d'honnêteté sur la troisième condition de refus

La directive exige aussi le refus quand
`espace_libre − allocation_run_actif < reserve_volume`. Elle est implémentée.
Mais, sous les constantes ratifiées, elle est **arithmétiquement inatteignable** :

```text
seuil − allocation = budget_restant_alloue + reserve_reprise + reserve_volume
                   >= reserve_volume        (car les deux premiers sont >= 0)
```

Tout `espace_libre` qui franchit le seuil satisfait donc déjà cette condition.
Elle subsiste en défense en profondeur, au cas où une porte future modifierait
la définition du seuil ou annulerait la réserve de reprise. **Ce fait est
publié plutôt que masqué par un test de complaisance** : la qualification
vérifie l'implication, elle ne prétend pas déclencher une branche morte.

## 3. Budget consommé — mesure sûre

`mesurer_occupation_lot` :

```text
reste strictement sous la racine canonique de runs ;
refuse toute entrée dont l'identité canonique (realpath + normcase) sort
  de <RUNS> — un point d'analyse sortant fait échouer la mesure ;
ne suit JAMAIS un lien ni une jonction : les liens internes sont
  enregistrés et non parcourus, donc jamais comptés deux fois ;
mesure les octets ALLOUÉS (taille logique arrondie au cluster réel du
  volume, obtenu par GetDiskFreeSpaceW — 4 096 octets ici) ;
refuse une taille négative, non entière ou forgée ;
n'ouvre aucun fichier en écriture, n'efface rien, ne modifie rien.
```

**Attribution.** Un répertoire compte comme production seulement s'il porte un
`manifest.json` lisible, au schéma reconnu, non marqué `_QUALIFICATION_ONLY`.
Tout le reste est classé `temporaires_reconnus` (premier composant dans
`_tmp`, `g2_4_qualification`) ou `non_attribues`, et **n'entre jamais dans le
budget**. Les répertoires temporaires de qualification ne peuvent donc pas
être comptés comme production.

En l'absence de run réel, `budget_deja_consomme = 0` — mesuré, pas supposé.

**Contrôle de stabilité.** La mesure d'admission effectue **deux parcours** et
refuse si l'inventaire budgété a changé entre les deux : c'est ainsi qu'un
fichier apparaissant pendant le scan est détecté. Le contrôle porte sur ce qui
est budgété, à l'exclusion des sous-arbres temporaires reconnus — le TEMP
scientifique vit sous la racine et son activité est attendue ; l'y inclure
produirait un faux positif permanent. L'observateur périodique, lui, mesure en
un seul parcours : sa mesure est instantanée par nature et bornée par la marge
d'anticipation.

## 4. Garde de contrat — comparaison exacte

`garde_contrat_local` exige exactement `1.3.0`, `20`, `RATIFIE`,
`CAP0-2026-08-02-issue90-rat1`, `1.15`, `40`, `cap1-1.1.0`.

La comparaison passe par `Decimal(str(valeur))`. Ce n'est pas une tolérance :
c'est l'égalité de la valeur **telle qu'elle est écrite**. `20` et `20.0`
passent ; `19.999` et `20.001` sont refusés au même titre que `19` et `21`.
Les valeurs doivent en outre être numériques, non booléennes et finies.

## 5. Garde de capacité de production

`garde_capacite_production` calcule et publie :

```text
libre | budget_total | budget_consomme | allocation_run_actif
budget_restant_alloue | reserve_reprise | reserve_volume
seuil_admission | marge_apres_admission
```

et refuse si : le budget est déjà dépassé ; l'espace libre est sous le seuil ;
l'espace libre moins l'allocation passe sous la réserve de volume ; une donnée
de capacité n'est pas finie ; le support réel n'est plus celui ratifié.

`garde_capacite` (≥ 40 Gio) **n'est pas supprimée** : elle reste une garde
technique indépendante, avec son alerte à 15 Gio.

`garde_budget_production` survit comme **condition nécessaire subsumée** — elle
compare encore l'espace libre au budget — mais elle n'est plus le critère
d'admission. La différence est prouvée au §13 : 45 Gio libres satisfont encore
l'ancienne paire et sont désormais refusés.

## 6. Support actif

Preuve dynamique, à chaque pré-vol :

```text
volume RATIFIÉ (lettre comparée à la constante « C »)
                                                   source normative unique
lecteur FIXE (DRIVE_FIXED = 3)                     API : GetDriveTypeW
NTFS                                               API : GetVolumeInformationW
média SSD, bus NVMe, état sain                     API : MSFT_PhysicalDisk
hors Git (aucun ancêtre .git, même vide)           refuser_sortie_sous_git
hors OneDrive / synchronisation                    chemin canonique
```

La détection média/bus exige une API système locale : elle est donc faite au
pré-vol et **retourne une preuve booléenne expurgée**. Si elle devient
indisponible — pilote muet, requête en échec, réponse illisible — le lancement
est **refusé**, jamais supposé.

### Le support ratifié est **C:**, pas « le volume système » (CAP-1a)

La source normative est une constante unique :

```python
SUPPORT_ACTIF_VOLUME_RATIFIE = "C"
```

`%SystemDrive%` **ne définit jamais** la ratification. Il n'est lu que comme
fait système supplémentaire, hors de toute décision et hors de l'identité de
reprise. Conséquences, toutes éprouvées :

```text
SystemDrive = D:  et  <RUNS> = C:   -> C reste le support ratifié : ACCEPTÉ
SystemDrive = D:  et  <RUNS> = D:   -> REFUSÉ : D n'est pas ratifié
SystemDrive = C:  et  <RUNS> = D:   -> REFUSÉ : D n'est pas ratifié
%SystemDrive% absent                -> décision inchangée
```

Déplacer `<RUNS>` vers un autre volume exigera une **nouvelle ratification
humaine** et une nouvelle version de politique de capacité. Le contrat privé
déclare `volume_ratifie = "C"`, vérifié exactement ; une déclaration absente
ou divergente est un refus.

### Identité du support — publique et privée séparées

L'identité porte l'empreinte **réelle** du volume : c'est elle qui empêche une
substitution silencieuse. Elle est **obligatoire en interne** (contrat privé,
manifeste de run, autorisation, garde de reprise) et **jamais publiée**.

Forme diffusable, la seule qui sorte sur une surface publique :

```json
{"volume_ratifie": "C", "lettre_volume": "C", "type_lecteur": "FIXE",
 "systeme_fichiers": "NTFS", "media": "SSD", "bus": "NVMe",
 "empreinte_volume": "<EMPREINTE_VOLUME_PRIVEE>",
 "empreinte_volume_presente": true, "empreinte_volume_conforme": true,
 "hors_git": true, "hors_synchronisation": true}
```

Aucun modèle, aucun numéro de série, aucun chemin. Un harnais de
confidentialité (§13) bloque la porte si la valeur réelle de l'empreinte — ou
un nom de machine, un nom d'utilisateur, un chemin utilisateur absolu, un UUID
de session ou un numéro de série — apparaît dans l'un des six fichiers publics
du périmètre.

### Rectification des surfaces déjà publiées (CAP-1a)

La valeur réelle de l'empreinte a été recherchée — par sa **valeur exacte**,
pas seulement par mots-clés — sur toutes les surfaces publiées :

```text
fichiers suivis de la branche : 1 occurrence (ce rapport, §6) -> EXPURGÉE
corps de la PR #92            : 0 occurrence
commentaires de la PR #92     : 0 occurrence
issue #90 (corps+commentaires): 0 occurrence
issue #63 (corps+commentaires): 0 occurrence
```

Surfaces rectifiées : **1** (le présent rapport). Aucun commentaire GitHub à
éditer : la valeur n'y a jamais figuré.

Point laissé explicite : la valeur reste lisible dans l'**historique Git** de
la branche (commit `034d105`, antérieur à cette rectification). Conformément
à la politique de secrets du contrat public (§4), l'expurgation de la version
visible et la réécriture éventuelle de l'historique sont **deux décisions
distinctes** ; aucune réécriture d'historique n'est faite dans cette porte.

## 7. Observateur de capacité

Branché en `callback_function` de Cobaya. Il **lit** l'espace libre,
l'occupation du lot, celle du run courant et les réserves ratifiées. Il n'écrit
aucun attribut : ni `params`, ni priors, ni propositions, ni `Rminus1_stop`,
ni `Rminus1_cl_stop`, ni poids, ni samples, ni `converged`.

Deux preuves indépendantes :

```text
DYNAMIQUE : une doublure de sampler enregistre toute écriture d'attribut et
            compare les valeurs avant/après. Liste d'écritures vide, aucune
            valeur changée — y compris au moment où l'exception est levée.
STATIQUE  : l'AST du lanceur ne contient AUCUNE affectation d'attribut
            « converged », ni aucune affectation d'attribut sur le paramètre
            « sampler ».
```

La faute `callback_modifie_converged` injecte un observateur fautif qui écrit
`sampler.converged = True` : la doublure le détecte, ce qui prouve que la
preuve dynamique n'est pas vacante.

Sur franchissement de la haute-eau, l'observateur lève `ArretCapaciteC7C1`,
qui porte `statut_run = NON_CONVERGE_INTERRUPTION_CAPACITE`. Positionner
`converged = True` est proscrit : cela ferait passer une interruption de
capacité pour une convergence scientifique.

**Observabilité.** Si la collection du sampler devient illisible, l'observateur
lève également `ArretCapaciteC7C1` — refuser plutôt que d'estimer.

## 8. Seuil de haute-eau et fréquence

Règle appliquée pendant un run, avec zone d'anticipation :

```text
ARRÊT si espace_libre        <  reserve_volume + marge          (40,25 Gio)
ARRÊT si occupation_lot      >  budget_total + reserve_reprise − marge
                                                                (20,90 Gio)
ARRÊT si une donnée de capacité n'est pas finie
ARRÊT si la capacité n'est plus observable
```

Les deux bornes minimales exigées par la directive — `libre >= reserve_volume`
et `occupation_lot <= budget_total + reserve_reprise` — sont donc franchies
**strictement avant** d'être atteintes.

### Justification de `callback_every = 1000`

```text
écriture maximale entre deux observations, chaîne de poids 1 écrivant à
  chaque itération : 1000 × 349 o = 349 000 o ≈ 0,000325 Gio
  soit 0,03 % de la réserve de reprise ratifiée (1,15 Gio)
facteur de sécurité 4 (observation manquée + vidages auxiliaires) :
  ≈ 0,0013 Gio
plancher retenu : 0,25 Gio — ce que le RESTE du système peut consommer sur
  un volume système dans la même fenêtre (≈ 20 s à ~50 évaluations/s)
marge d'anticipation effective : max(0,25 ; 0,0013) = 0,25 Gio
```

Un intervalle très long est exclu : 1 000 itérations représentent quelques
dizaines de secondes, pour un coût d'observation purement métadonnées.

**Décalage disque / mémoire.** Cobaya ne vide la chaîne sur disque que toutes
les `output_every` (60 s par défaut) : la taille sur disque retarde sur la
réalité. L'observateur lit donc `len(sampler.collection)` et retient
`max(taille sur disque, en-tête + lignes × octets par ligne + auxiliaire)`.
Le décalage est supprimé par construction, pas couvert par une marge.

`callback_every` est **opérationnel, non scientifique** : il n'entre pas dans
`sha256_encodage_scientifique`, il est injecté après le gel de l'encodage, et
il est consigné séparément au manifeste comme part de l'identité de reprise.
`garde_injection_observateur` refuse si l'injection modifie autre chose que
`sampler.mcmc.callback_function` et `sampler.mcmc.callback_every`.

## 9. Reprise après arrêt de capacité

Un run interrompu reste `NON_CONVERGE_INTERRUPTION_CAPACITE`, jamais
`CONVERGE`. `garde_reprise_apres_capacite` exige **cumulativement** :

```text
manifest.json présent, lisible et identique sur tous les champs d'identité ;
statut différent de CONVERGE ;
checkpoint Cobaya présent, non vide, analysable, portant un bloc sampler ;
politique de capacité identique (budget, réserves, allocation, version,
  callback_every, support, référence de ratification) ;
nouvelle admission de capacité réussie.
```

### Limite bloquante — vérifiée dans le code installé

Dans Cobaya 3.5 (`samplers/mcmc/mcmc.py`), `write_checkpoint()` n'est appelé
qu'à deux endroits : une fois à l'initialisation (« initial dummy
checkpoint »), et à la fin de `check_convergence_and_learn_proposal`, qui
n'est atteinte que lorsque `check_ready()` est vrai, c'est-à-dire
`n % learn_every == 0`. **Il n'existe pas de `checkpoint_every`.**

Le callback, lui, se déclenche sur `n % callback_every == 0`. Rien ne garantit
donc qu'un checkpoint **récent** — ni même un checkpoint utile — existe au
moment où l'exception de capacité est levée.

```text
LIMITE BLOQUANTE : la reprise automatique après arrêt de capacité n'est pas
garantie. La garde le constate et REFUSE. Aucun checkpoint n'est fabriqué.
```

Deux voies pour lever cette limite dans une porte future, aucune ouverte ici :
aligner `callback_every` sur `learn_every`, ou faire écrire un checkpoint par
le lanceur avant de propager l'exception. Les deux ont des effets à qualifier.

## 10. Manifeste de run — schéma `c7c1-run-manifest-2`

Sept champs ajoutés, tous part de l'identité de reprise :

```text
budget_total_Gio | reserve_reprise_Gio | reserve_volume_minimale_Gio
allocation_run_actif_Gio | politique_capacite_version | callback_every
support_actif_identite_expurgee
```

`reference_ratification_budget` y figurait déjà. Une reprise sous un autre
budget, une autre réserve, une autre politique, une autre fréquence
d'observation ou un autre support est donc refusée.

Les manifestes de qualification restent **éphémères et sous %TEMP%**, marqués
`_QUALIFICATION_ONLY`. Aucun manifeste réel n'est écrit dans `<RUNS>`.

## 11. Autorisation — cinq groupes de contrôle ajoutés

`CLES_MANIFESTE` gagne `reserve_reprise_Gio`,
`reserve_volume_minimale_Gio`, `politique_capacite_version` et
`support_actif_identite_expurgee`. Le validateur pur traverse désormais
24 groupes, dont cinq nouveaux :

```text
budget_ratifie | reserve_reprise | reserve_volume
politique_capacite | support_actif
```

Une autorisation ne peut donc plus valider un autre budget, une autre réserve
de reprise, une autre réserve de volume, une autre référence CAP-0, une autre
politique de capacité ni un autre support. Les tests emploient exclusivement
le validateur pur, en mémoire : **aucune autorisation réelle n'existe**.

## 12. Pré-vol

Le pré-vol annonce désormais, sans rien autoriser :

```text
BUDGET RATIFIE                    : true
SUPPORT QUALIFIE                  : true
POLITIQUE DE CAPACITE QUALIFIEE   : true
PRODUCTION TOUJOURS VERROUILLEE   : true
```

et publie l'espace libre, le seuil d'admission, la marge, le budget consommé,
l'allocation du run testé, la réserve de reprise et la réserve de volume. Les
chemins restent expurgés. Le verrou prime sur toute autre annonce :
`production_autorisable` vaut `false` tant qu'il tient.

## 13. Qualification

`scripts/qualify_xz_capacity_cap1.py` — passe complète et mode `--faute`.
Double passe : `exit 0 / exit 0`, **diff normalisé vide**.

### Admission

```text
seuil_admission_gio             : 61.15
libre = seuil exact             : ACCEPTÉ   (marge = 0.0 Gio)
libre = seuil − 1 octet         : REFUSÉ
libre = 45 Gio (budget 20)      : REFUSÉ
libre = 39 Gio                  : REFUSÉ
budget consommé = 0             : ACCEPTÉ
budget consommé = 25 Gio > 20   : REFUSÉ
ancienne paire de gardes à 45 Gio : ACCEPTAIT  <- preuve du changement
```

La dernière ligne est la preuve exigée au §13 : `garde_capacite` (45 ≥ 40) et
`garde_budget_production` (45 ≥ 20) acceptaient toutes deux 45 Gio libres.
La nouvelle admission les refuse. La faute de mutation
`ancienne_regle_acceptait_45_gio` rétablit l'ancienne sémantique et n'est
tenue pour détectée que si l'ancienne accepte **et** la nouvelle refuse.

### Occupation

```text
racine de runs réelle    : production 0 octet, non attribué 0 octet,
                           aucun lien, stabilité vérifiée -> budget consommé 0
arborescence synthétique : production 8 192 | temporaires 8 192 |
                           non attribués 4 096 octets
                           run détecté : g2_4/P_WS/M2a-N/s630101
                           jonction INTERNE plantée : enregistrée dans
                           liens_non_suivis, NON parcourue — l'occupation
                           reste 8 192 (pas de double comptage)
cluster réel du volume   : 4 096 octets
```

### Observateur

```text
écritures d'attribut du sampler        : []          (aucune)
mutations de valeur                    : []          (aucune)
au-dessus de la haute-eau              : retour None, aucune exception
sous la haute-eau (39 Gio)             : ArretCapaciteC7C1,
                                         statut NON_CONVERGE_INTERRUPTION_CAPACITE
plafond du lot (21,3056 > 21,15 − 0,25): ArretCapaciteC7C1
écritures au moment de l'arrêt         : []          (aucune)
contrôle statique AST                  : 0 affectation « converged »,
                                         0 affectation sur « sampler »
```

### Injection

```text
différences avant/après : ["sampler.mcmc.callback_every",
                           "sampler.mcmc.callback_function"]   (exactement)
callback absent de l'encodage scientifique : oui
sha256_encodage_scientifique : e86dc462d47ba922efe197418198d7a77649a75a94ac0a324577f6b831d5026d
```

### Reprise

```text
reprise nominale (manifeste + checkpoint valide + admission)  : ACCEPTÉE
statut repris                       : NON_CONVERGE_INTERRUPTION_CAPACITE
reprise sans checkpoint             : REFUSÉE explicitement
reprise avec checkpoint vide        : REFUSÉE
reprise avec checkpoint illisible   : REFUSÉE
reprise d'un manifeste CONVERGE     : REFUSÉE
reprise sous une autre politique    : REFUSÉE
```

### Manifeste et autorisation

```text
schéma            : c7c1-run-manifest-2, 34 champs, aucun manquant
politique portée  : budget 20 | reprise 1,15 | volume 40 | allocation
                    0,5753161130100489 | cap1-1.1.0 | callback_every 1000 |
                    identité expurgée du support | référence CAP-0
autorisation      : 24 groupes traversés, 0 manquant, dont les cinq
                    nouveaux (budget_ratifie, reserve_reprise,
                    reserve_volume, politique_capacite, support_actif)
```

### Fautes adversariales — 57 sur 57 détectées

```text
ancienne_regle_acceptait_45_gio        anticipation_absente_laisse_saturer
autorisation_budget_non_ratifie        autorisation_politique_autre
autorisation_reference_autre           autorisation_reserve_reprise_autre
autorisation_reserve_volume_autre      autorisation_support_autre
budget_deja_depasse                    callback_lot_au_dela_du_plafond
callback_mesure_impossible_non_marquee callback_modifie_converged
callback_observabilite_perdue          callback_sous_haute_eau_sans_arret
contrat_ancienne_version_1_2_0         contrat_budget_19_999
contrat_budget_20_001                  contrat_politique_autre
contrat_reference_autre                contrat_reprise_1_14
contrat_reprise_1_16                   contrat_statut_non_etabli
contrat_volume_39                      contrat_volume_41
fichier_apparait_pendant_le_scan       grille_inconnue_allouee_par_defaut
identite_canonique_hors_racine         injection_modifie_le_sampler
libre_45_gio_refuse                    libre_seuil_moins_un_octet
lien_interne_suivi_double_compte       point_analyse_sortant
reprise_checkpoint_illisible
reprise_checkpoint_vide                reprise_politique_differente
reprise_sans_checkpoint                reprise_statut_converge
support_autre_volume                   support_bus_usb
support_indisponible                   support_media_hdd
support_non_fixe                       support_non_ntfs
support_sante_degradee                 support_sous_git
support_sous_onedrive                  taille_forgee
taille_negative                        temporaire_qualification_compte_comme_production
verrou_retire
--- CAP-1a : support ratifié C et confidentialité ---
systemdrive_D_redefinit_la_ratification
systemdrive_D_runs_D_accepte_par_ancienne_regle
runs_D_systemdrive_C_refuse            constante_ratifiee_mutee_C_vers_D
contrat_volume_ratifie_absent          contrat_volume_ratifie_D
empreinte_publiee_en_clair
```

Les quatre fautes `systemdrive_*`/`constante_*` prouvent le sens de la
liaison : `SystemDrive=D:` avec `<RUNS>` sur C: reste **accepté** (l'ancienne
règle, réinjectée, refusait) ; `SystemDrive=D:` avec `<RUNS>` sur D: est
**refusé** (l'ancienne règle acceptait) ; `<RUNS>` sur D: avec
`SystemDrive=C:` est refusé sur la cause exacte ; et la mutation de la
constante `C -> D` fait basculer la décision, ce qui prouve qu'elle est bien
la source normative unique — la valeur nominale lue dans la source restant
« C ». Un contrôle statique AST vérifie de plus que `_garde_volume_ratifie`
compare à la constante et ne lit jamais `%SystemDrive%`, dont la lecture est
confinée au fait système informatif.

### Trois défauts trouvés et corrigés pendant la porte

La première passe de qualification a échoué. Les trois causes sont
consignées ici plutôt que corrigées en silence.

**a. Preuve du verrou redevenue vacante.** Le harnais G2.4d simulait un
budget de 50 Gio. Le nouveau contrôle de cohérence de `identite_run` le
rejetait, et l'exécution s'arrêtait à l'étape 7 au lieu d'atteindre le verrou
à l'étape 8 : « aucune sentinelle atteinte » redevenait vrai pour une raison
sans rapport. Le budget simulé est désormais le budget **ratifié**.

**b. Faute `support_autre_volume` non attribuable.** Le refus survenait bien,
mais à l'échec de l'API de volume sur un lecteur inexistant, pas au contrôle
de support. La comparaison de lettre est passée **avant** toute interrogation
système (`_garde_volume_ratifie`), de sorte que la cause exacte est celle
qu'on prétend éprouver.

**c. Qualification matérielle intermittente — défaut réel du dispositif.**
La requête au sous-système de stockage échoue transitoirement sous charge :
mesuré 1 échec sur 4 exécutions consécutives. Deux conséquences ont été
corrigées :

```text
- le lanceur réessaie un nombre BORNÉ de fois (3) avant de refuser :
  toujours « refus plutôt que supposition », mais plus sur un unique aléa ;
- le qualificateur mesure le support HORS de la fonction éprouvée, pour
  qu'une indisponibilité matérielle ne puisse plus se déguiser en
  « faute non détectée » — c'est ce déguisement qui rendait la passe 2
  différente de la passe 1.
```

Après correction : 8 exécutions consécutives stables sur la faute concernée.
Cette intermittence est un **fait opérationnel à retenir** : un lancement de
production peut être refusé pour indisponibilité matérielle transitoire. Le
refus est le comportement voulu ; la reprise manuelle est la réponse.

### Revue adversariale — 42 constats, 41 réfutés, 1 confirmé

Une revue indépendante à cinq lentilles (arithmétique et unités, vacuité des
tests, conformité à la directive, sûreté de la mesure sous Windows,
observateur et sémantique Cobaya) a produit 42 constats, chacun soumis à un
vérificateur chargé de le **réfuter** par exécution. Quarante et un sont
tombés. Deux ont conduit à un changement.

**d. Défaillance de mesure non marquée.** Une panne de mesure pendant un run
sortait par une `GardeErreur` nue, sans porter le statut d'interruption. Elle
sort désormais par `ArretCapaciteC7C1`, éprouvée par la faute
`callback_mesure_impossible_non_marquee`.

**e. Le non-suivi des liens n'était éprouvé par aucun test — constat confirmé.**
Les fautes `identite_canonique_hors_racine` et `point_analyse_sortant`
exécutaient **le même code** : une unique jonction sortante. Or une jonction
sortante est refusée par le contrôle d'identité canonique **avant** que
`_est_lien` ne soit atteint. La propriété que ce rapport revendique au §3 —
« ne suit jamais un lien, les liens internes sont enregistrés et jamais
comptés deux fois » — n'était donc vérifiée par rien, et `liens_non_suivis`
était publié sans aucune assertion.

Le vérificateur l'a établi par mutation exécutée : en neutralisant
`_est_lien`, les deux fautes restaient vertes, tandis qu'une jonction
**interne** faisait passer l'occupation de 8 192 à 16 384 octets avec
apparition d'un run fantôme. La direction de l'erreur est non conservatrice :
une occupation sur-comptée **abaisse** le seuil d'admission.

Trois corrections, toutes dans le qualificateur (le lanceur est inchangé) :

```text
- identite_canonique_hors_racine éprouve désormais une cause distincte :
  une entrée ordinaire dont l'identité canonique résout hors de la racine,
  sans dépendre d'un privilège de création de lien ;
- point_analyse_sortant conserve la jonction sortante ;
- lien_interne_suivi_double_compte, NOUVELLE faute, est le seul test qui
  exerce _est_lien : il crée une jonction interne, neutralise _est_lien, et
  n'est tenu pour détecté que si l'occupation double ET que la liste des
  liens non suivis se vide ;
- la section 3 plante une jonction interne dans l'arborescence synthétique
  et ASSERTE que liens_non_suivis la contient et que l'occupation reste
  celle du seul run réel.
```

## 14. Non-régression

```text
python scripts/qualify_xz_launcher_g2_4d.py   -> exit 0   67/67 fautes
python scripts/qualify_xz_configs_g2_3.py     -> exit 0   porte.echecs = []
python scripts/qualify_xz_optim_g2_4c.py      -> exit 0   porte.echecs = []
```

Verdicts scientifiques **inchangés** : identité bit à bit optimisé/rapide
conservée, et les cinq écarts au legacy restent exactement nuls.

```text
chi2_BAO_abs   0.0  (seuil 1e-10)      logp_abs    0.0  (seuil 5e-4)
chi2_CMB_abs   0.0  (seuil 1e-3)       omch2_abs   0.0  (seuil 1e-12)
chi2_total_abs 0.0  (seuil 1e-3)
```

**Aucune garde scientifique n'a été détendue.** Trois adaptations du
qualificateur G2.4d ont été nécessaires, toutes de nature à *renforcer* le
test, jamais à l'affaiblir :

```text
- budget_non_etabli_accepte : le contrat réel étant désormais ratifié, la
  faute injecte explicitement l'ancien statut NON_ETABLI, qui doit rester
  bloquant. Sans cela, la faute aurait été satisfaite par le nouveau
  contrat au lieu d'éprouver la garde ;
- autorisation_budget_different_du_contrat et
  autorisation_ratification_differente : l'autorisation porte maintenant la
  valeur RATIFIÉE et c'est le CONTRAT qui diverge. La faute éprouve donc
  toujours la LIAISON contrat <-> autorisation, et non le nouveau contrôle
  de valeur ratifiée qui, sinon, l'aurait masquée ;
- les fixtures d'autorisation portent les quatre nouveaux champs de
  capacité, sans quoi elles seraient rejetées sur « clés inexactes ».
```

## 15. Verrou

```text
VERROU_PRODUCTION_G2_4D                     : True (constante et source AST)
sentinelles atteintes (mkdir, makedirs,
  os.replace, open en écriture, cobaya.run) : AUCUNE
arrêt avec budget ratifié, support qualifié,
  capacité suffisante et autorisation simulée :
  « GardeErreur: VERROU G2.4d : raccord qualifié SANS production ... »
manifeste QUALIFICATION_ONLY rejeté par la vraie garde : oui
```

La preuve n'est **pas vacante** : l'exécution atteint réellement l'étape
verrouillée — toutes les gardes amont étant satisfaites, y compris la
nouvelle admission de capacité — et c'est bien l'exception du verrou qui
l'arrête, avant toute création de répertoire, toute écriture et tout
`cobaya.run`. La faute `verrou_retire` prouve que le contrôle statique
détecte un abaissement du verrou.

## 16. Périmètre Git

Fichiers touchés, tous dans le périmètre autorisé :

```text
scripts/run_mcmc_xz_g2_4.py
scripts/qualify_xz_capacity_cap1.py                        (nouveau)
scripts/qualify_xz_launcher_g2_4d.py
reports/rapport_CAP1_capacite.md                           (nouveau)
99_DOCUMENTATION_ENVIRONNEMENTS_LOCAUX/CONTRAT_PUBLIC_C7_C1.md
99_DOCUMENTATION_ENVIRONNEMENTS_LOCAUX/contrat_local.example.json
```

Les deux documents publics ont été modifiés parce que le nouveau schéma les
rendait faux : le modèle de contrat déclarait encore `1.0.0` et
`NON_ETABLI`, et le contrat public ne décrivait aucune politique de capacité.

Fichiers scientifiques **gelés et non modifiés** : `xz_cobaya_g2_4.py`,
`xz_fast_g2_4c.py`, `xz_background_g2_1.py`, `xz_likelihood_g2_3.py`,
`configs/xz/*`, priors, graines, données.

## 17. Verdict

```text
CAP-1 PASSÉE — budget et support matérialisés, production toujours fermée
```

La décision humaine ratifiée est désormais **effectivement bloquante** : elle
est inscrite au contrat privé en version 1.3.0, comparée exactement par le
lanceur, portée par le manifeste de run et par le schéma d'autorisation, et
appliquée par une règle d'admission qui exige 61,15 Gio au début du lot là où
l'ancienne paire de gardes se contentait de 40. Le support est qualifié
dynamiquement et refuse plutôt que de supposer. Un observateur purement
lecteur surveille la haute-eau et interrompt en `NON_CONVERGE_INTERRUPTION_
CAPACITE`, jamais en convergence.

```text
double passe CAP-1        : exit 0 / exit 0, diff normalisé vide
fautes adversariales      : 57 / 57 détectées
rejeux                    : G2.4d 0 (67/67) | G2.3a 0 | G2.4c 0
verdicts scientifiques    : inchangés, écarts au legacy exactement nuls
VERROU_PRODUCTION_G2_4D   : True — atteint, jamais franchi
support ratifié           : C, par constante normative — %SystemDrive%
                            sans aucun pouvoir de redéfinition
confidentialité           : aucune valeur locale réelle sur les surfaces
                            publiques (harnais bloquant, 7 motifs)
autorisation réelle       : AUCUNE
manifeste de run réel     : AUCUN
chaîne créée              : AUCUNE
```

### Ce qui reste ouvert

```text
1. reprise automatique après arrêt de capacité : LIMITE BLOQUANTE — Cobaya
   ne garantit pas l'existence d'un checkpoint récent au moment de
   l'interruption. La garde refuse ; rien n'est fabriqué. Décision de
   conception à prendre dans une porte ultérieure.
2. archive indépendante : NON SATISFAITE — un seul support physique.
3. qualification matérielle intermittente : un lancement peut être refusé
   pour indisponibilité transitoire du sous-système de stockage. Trois
   tentatives, puis refus. Comportement voulu, à connaître.
4. B_diag reste une allocation déclarée (1 Gio), non une mesure : les
   diagnostics du lot n'écrivent toujours rien sur disque.
5. la troisième condition de refus exigée au §5 est implémentée mais
   arithmétiquement inatteignable sous les constantes ratifiées (§2).
```

Aucun merge. L'ouverture de la production reste une décision humaine
distincte, non prise ici.
