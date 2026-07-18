# Audit de pré-fusion de la PR nº 14 v0.1

## 0. Statut

```text
date : 18 juillet 2026 ;
branche : agent/contribution-q1-information-chemin ;
base : main ;
objet : contrôler la consolidation cumulative avant fusion ;
périmètre : intégrité Git, droits de redistribution, données externes,
            portes d'entrée, statuts documentaires, archives, scripts et CI ;
ne vaut pas : relecture scientifique proposition par proposition des 526 fichiers.
```

## 1. Verdict synthétique

```text
arbre final de la branche : recevable ;
cohérence documentaire : recevable ;
audits automatisés renforcés : réussis ;
données DESI brutes suivies par Git : aucune ;
PDF éditeurs dans l'arbre final : aucun ;
conflit avec main : aucun ;
méthode de fusion ordinaire : refusée ;
méthode recommandée : squash and merge, après acceptation explicite de sa limite historique.
```

La branche peut devenir le nouveau tronc validé sans attendre la clôture de toutes les
dettes scientifiques. Elle ne doit cependant pas être fusionnée par commit de fusion ni
par rebase, car son historique de travail contient deux commits publics ayant porté des
PDF éditeurs ensuite retirés.

## 2. Contrôles accomplis

### 2.1 Topologie Git et PR

Au moment du contrôle :

```text
main : ancêtre exact de la branche ;
branche en avance : 325 commits avant le lot final d'audit ;
branche en retard : 0 commit ;
PR nº 14 : ouverte, en brouillon, fusionnable ;
threads de revue non résolus : aucun.
```

Il n'existe donc ni divergence avec `main`, ni conflit de contenu à résoudre. La taille
de la PR impose toutefois de distinguer un audit de consolidation d'une validation
scientifique exhaustive.

### 2.2 Retrait des PDF et données externes

Le commit `7ef9da17b95d7d445dc13d0c6d21881fcaccc96a` retire de l'arbre courant :

```text
93_LABORATOIRE_EDITORIAL_EXPERIMENTAL/ESSAI_tentative/sources/
  Eran_Tal_2022_1-s2.0-S0263224117305730-main.pdf

93_LABORATOIRE_EDITORIAL_EXPERIMENTAL/ESSAI_tentative/sources/
  N_de_Courtenay_SI_2022posc_a_00397.pdf
```

Les fiches de lecture, références bibliographiques, DOI et contrôle de redistribution
restent conservés. Le workflow vérifie désormais qu'aucun PDF n'est suivi dans le
laboratoire éditorial.

Le chemin `data_external/` est ignoré par Git. Le workflow échoue si un fichier situé
sous ce chemin entre dans l'index. Les chaînes DESI DR2, archives et caches locaux ne
font pas partie de la PR.

### 2.3 Portes d'entrée et statuts

Les portes d'entrée actives sont cohérentes entre :

- `README.md` ;
- `02_CYCLES_PHYSIQUES/README.md` ;
- `Vue_recente_chantiers_16_18_juillet_2026_v0_1.md` ;
- `Vue_ensemble_globale_v0_4.md` ;
- `Feuille_route_post_consolidation_v0_1.md` ;
- `Index_raisonne_du_corpus_v1_3.md`.

Le cycle 3 possède une synthèse active après `N5`. Sa dette documentaire, empirique et
comparative est déclarée levée ; `C2` reste correctement ouverte. Les fichiers
`resultats_c2.json` et `quantiles_c2.csv` ne contiennent aucun quantile présenté comme
reproduit sans lecture des chaînes officielles.

Le pan philosophique reste disponible en réserve. Le laboratoire éditorial expérimental
est distingué du corpus scientifique et n'a pas autorité pour clore une dette ouverte.

### 2.4 Archives conversationnelles

Le contrôle technique retire ou détecte :

- adresses électroniques ;
- liens privés de conversation ;
- URL signées ou internes ;
- identifiants techniques ;
- chemins locaux et temporaires.

Le script a été corrigé afin de recontrôler également un export Qwen déjà normalisé ; il
échoue désormais lorsqu'un fichier est absent ou nécessiterait encore une modification.

Ce contrôle est devenu bloquant dans GitHub Actions. Il valide l'assainissement technique,
non la totalité du contenu humain conservé.

La décision documentaire antérieure est maintenue : les exports assainis restent une
source consultable de provenance ; le corpus actif n'en reçoit que des extractions
sélectives et le registre court des arbitrages. L'export intégral n'est pas transformé en
journal continu et ne reçoit aucune autorité scientifique ou doctrinale.

### 2.5 Scripts et reproduction minimale

Le workflow renforcé exécute désormais :

```text
audit structurel Markdown ;
contrôle des liens ;
contrôle UTF-8 ;
assainissement conversationnel en lecture seule ;
absence de données externes et de PDF éditeurs ;
compilation des scripts Python ;
installation des dépendances de la reprise N1–N3 ;
test synthétique du lecteur C2 ;
inventaire informatif des placeholders.
```

L'exécution nº 124 du workflow `Audit du corpus` réussit sur le commit
`32e7b27431c8558c5c8c52fb3b7f08b9fbfe4b38`. Le rapport lui-même est soumis au même
workflow avant verdict final.

## 3. Point bloquant — historique des deux PDF

Le retrait du dernier arbre ne supprime pas les objets de l'historique Git déjà poussé.
GitHub précise qu'un commit de fusion ajoute tous les commits de la branche à la branche
de base, tandis qu'un squash produit un seul commit consolidé à partir de l'état final.

Documentation :

- https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/about-merge-methods-on-github
- https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository

Conséquences :

```text
Create a merge commit : interdit pour cette consolidation ;
Rebase and merge       : interdit pour cette consolidation ;
Squash and merge       : recommandé pour garder les PDF hors de l'ascendance de main.
```

Le squash ne constitue pas une purge complète de GitHub. Les anciens commits peuvent
rester accessibles par leur SHA, par les références de la PR ou dans d'éventuelles copies.
Une purge complète demanderait une réécriture coordonnée de l'historique et, pour les
vues conservées par GitHub, une intervention de l'hébergeur. La documentation GitHub
précise que son assistance de purge est réservée aux données sensibles ; aucune garantie
de purge serveur ne peut donc être donnée ici pour des fichiers relevant du droit
d'auteur.

La solution pratique recommandée est :

```text
1. fusionner la PR nº 14 exclusivement par squash ;
2. supprimer ensuite la branche distante cumulative ;
3. fermer comme remplacées les PR empilées déjà incluses ;
4. repartir du nouveau main pour C2 et les dettes suivantes ;
5. conserver hors dépôt les PDF éditeurs.
```

## 4. Gouvernance du corpus public

### 4.1 Archives consultables — décision maintenue

Le dépôt est public. Les dossiers `91_TRAVAUX_ANTERIEURS/` et
`92_ARCHIVES_CONVERSATIONNELLES/` conservent volontairement le contenu de plusieurs
échanges après retrait des métadonnées techniques.

Le régime déjà choisi est conservé :

```text
archives assainies : consultables comme source de provenance ;
corpus actif : seulement cartes sélectives, décisions et résultats validés ;
registre futur : traces courtes des arbitrages, sans export continu ;
autorité des archives : aucune autorité scientifique ou doctrinale automatique.
```

Ce choix rend la provenance plus complète tout en évitant que la conversation ne commande
le parcours scientifique. Il implique d'accepter que les formulations exploratoires et
certains éléments personnels maintenus après assainissement soient publiquement lisibles.

### 4.2 Licence du corpus — point non bloquant

Aucun fichier `LICENSE` n'est présent. En l'absence de licence, le droit d'auteur par
défaut s'applique : la consultation et le fork permis par GitHub ne valent pas permission
générale de réutilisation, modification ou redistribution.

Documentation :

- https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository

Ce point n'empêche pas la fusion. Le régime actuel peut être compris comme une réserve
provisoire de tous les droits. Une décision ultérieure pourra distinguer, si nécessaire,
le code, les textes de recherche, les archives et les matériaux de tiers plutôt que
d'imposer une licence unique inadéquate à l'ensemble.

## 5. Limites de l'audit

L'audit ne valide pas individuellement :

- les 191 000 lignes ajoutées ;
- toutes les affirmations physiques des dix cycles ;
- toutes les licences ou autorisations attachées aux DOCX historiques ;
- chaque mention de tiers dans les archives ;
- la reproductibilité des chaînes DESI DR2, puisque `C2` reste ouverte.

Il établit que ces limites sont visibles, que les documents directeurs ne les masquent
pas et que les mécanismes techniques de contrôle sont suffisants pour une consolidation
prudente.

## 6. Verdict de pré-fusion

```text
verdict documentaire et technique : favorable ;
verdict scientifique global : non requis pour la consolidation ;
condition d'intégration à main : squash and merge exclusivement ;
archives conversationnelles : décision antérieure maintenue et assainissement validé ;
licence : absence explicite, réserve de droits par défaut, non bloquante ;
statut recommandé de la PR : rester en brouillon jusqu'à acceptation de la limite
                              historique du squash, puis passer en prête pour revue.
```
