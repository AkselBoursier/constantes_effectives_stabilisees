# Glossaire des termes cles du projet

Ce glossaire recense les termes methodologiques fondamentaux du corpus.

Il ne remplace pas les documents de methode actifs ; il evite les repetitions
et sert de reference rapide pour la terminologie interne.

Document de methode de reference :
[Note methodologique v1.3](01_CADRE_METHODOLOGIQUE/Note_synthese_methodologique_v1_3_pre_familial_et_temporalite.md)

---

## Termes de forme logique

### Constante effective stabilisee

Definition de reference (v1.3) :

> Une grandeur dont une valeur, une forme, une liaison qualifiee, un role ou
> une dependance devient robuste dans un regime donne, selon un acces determine,
> avec un mode et une trajectoire de stabilisation explicites, sans que cette
> robustesse implique necessairement une constance absolue, une universalite
> hors contexte ou un statut fondamental.

Formule courte : **constance = robustesse fonctionnelle situee**

### Forme logique de stabilisation (rang 0)

La question : qu'est-ce qui est stabilise formellement ?

C'est la premiere question methodologique, anterieure a l'attribution d'une
famille ou d'un role.

---

## Termes de role contextuel (rang 2)

### Seuil

Role contextuel d'une grandeur qui separe deux regimes ou delimite une zone de
validite.

Usage : une grandeur a role de Seuil marque une frontiere au-dela de laquelle
le comportement physique change qualitativement.

Elle n'est pas une famille : elle est un role que peut jouer une grandeur dans
un contexte donne.

Source : [Tests taxonomiques — famille Seuil](03_TESTS_TAXONOMIQUES/Source_docx_Test_famille_Seuil_v0_1.md)

### Fond

Role contextuel d'une grandeur qui fixe un niveau de reference ou une echelle
de base dans un regime.

Usage : une grandeur a role de Fond fournit un arriere-plan stable par rapport
auquel d'autres grandeurs sont definies ou mesurees.

Elle n'est pas une famille : elle est un role architectural de reference de
niveau.

Source : [Tests taxonomiques — famille Fond](03_TESTS_TAXONOMIQUES/Source_docx_Test_famille_Fond_v0_1.md)

### Relation

Role contextuel d'une grandeur qui encode une liaison qualifiee entre deux
secteurs ou deux regimes.

Usage : une grandeur a role de Relation ne se reduit pas a un ratio numerique ;
elle porte une structure de dependance entre au moins deux objets du corpus.

Elle n'est pas une famille : elle est un role de liaison qualifiee.

Source : [Tests taxonomiques — famille Relation](03_TESTS_TAXONOMIQUES/Source_docx_Test_famille_Relation_v0_1.md)

---

## Termes d'architecture (rang 4)

### Architecture inter-familles

Reseau de solidarite entre plusieurs grandeurs appartenant a des familles
fonctionnelles differentes, soumis a un stress test de validite.

Une architecture n'est pas une famille : c'est un reseau de dependances
structurelles, au-dessus du niveau de la fiche individuelle.

Documents de reference :
- [Cercle 2 — architectures actives](04_ARCHITECTURES_INTER_FAMILLES/Cercle2_architectures_actives_v0_1.md)
- [Synthese architectures inter-familles v1.0](05_CARTES_ET_SYNTHESES/Synthese_architectures_inter_familles_v1_0.md)

### Mode de solidarisation

Facon dont plusieurs grandeurs deviennent solidaires dans une architecture :
par couplage, par contrainte mutuelle, par co-stabilisation, ou par dependance
hierarchique.

Le mode de solidarisation est a distinguer du simple co-placement dans une
meme famille.

### Architecture cosmologique

Reseau de solidarite entre les grandeurs du regime cosmologique :
Lambda, H_0, Omega_i, w, A_s, n_s, sigma_8, S_8.

Document : [Architecture cosmologique — notes](04_ARCHITECTURES_INTER_FAMILLES/Architecture_cosmologique_notes.md)

### Architecture Saveur-Higgs

Reseau de solidarite entre les grandeurs du secteur Higgs/Yukawa/saveur :
v (VEV), masses de fermions, couplages de Yukawa, matrice CKM, parametres de Wolfenstein.

Document : [Architecture Saveur-Higgs — notes](04_ARCHITECTURES_INTER_FAMILLES/Architecture_saveur_Higgs_notes.md)

### Architecture Metrologique SI

Reseau de solidarite entre les constantes fondamentales fixees par le SI 2019 :
c, h, e, k_B, N_A, ainsi que leurs contraintes metriques.

Document : [Architecture metrologique SI — notes](04_ARCHITECTURES_INTER_FAMILLES/Architecture_metrologique_SI_notes.md)

### Architecture Effective basse energie

Reseau de solidarite entre les grandeurs effectives du regime de basse energie :
G_F, M_W, m_f, alpha_G, M_Pl.

Document : [Architecture effective basse energie — notes](04_ARCHITECTURES_INTER_FAMILLES/Architecture_effective_basse_energie_notes.md)

---

## Modes de stabilisation

Les huit modes de stabilisation sont la grille de lecture principale du corpus.

Ils repondent directement a la question directrice :
dans quelle mesure une grandeur peut-elle etre dite constante ?

| Mode | Description | Exemples |
|---|---|---|
| Valeur mesuree ou ajustee | Une valeur robuste est etablie dans un regime | masses, `M_W`, `Lambda_QCD` |
| Couplage courant ou situe | Une intensite depend d'une echelle ou d'un schema | `alpha_s(Q^2)`, `alpha_G(E)`, Yukawa |
| Composition exacte | Une grandeur derivee herite d'une exactitude definitionnelle | `R`, `K_J`, `R_K` |
| Convention definissante | Une valeur fixe une unite | `k_B`, `N_A`, `c`, `h`, `e` |
| Orientation | Une relation entre bases ou secteurs est stabilisee | CKM, PMNS |
| Validite limitee | Une description vaut dans un domaine determine | `G_F`, Fermi, gravitation effective |
| Inference reconstruite | Une grandeur est stabilisee par modele et donnees | `sigma_8`, `S_8`, `H_0` selon acces |
| Borne ou contrainte | Une limite remplace une mesure positive directe | masse absolue neutrino, tensions cosmologiques |

Ces modes peuvent se croiser.

Ils ne sont pas des classes exclusives.

---

## Termes de methode

### Regime physique / regime d'acces

Deux axes orthogonaux de la methode v1.3 :

- **Regime physique** : le domaine d'echelle ou de contexte dans lequel la
  grandeur opere (basse energie, electrofaible, cosmologique, etc.).
- **Regime d'acces** : la facon dont la grandeur est mesuree ou contrainte
  (mesure directe, inference, couplage indirect, etc.).

### Trajectoire de stabilisation (rang 5)

Comment le statut de la grandeur s'installe, varie, persiste ou se transforme
dans le temps ou en fonction du regime.

### Famille fonctionnelle controlee (terme historique controle)

Regroupement de grandeurs partageant une meme fonction directrice dans un regime
physique donne.

Ce terme reste disponible comme sortie taxonomique apres test de resistance.

Il ne doit pas etre utilise comme point de depart d'une analyse.

Voir : [Audit de taxonomie v0.1](05_CARTES_ET_SYNTHESES/Audit_taxonomie_v0_1.md)

### Cercle 2

Phase du projet consistant a tester les architectures actives par des
stress tests de validite.

Dossier : [04_ARCHITECTURES_INTER_FAMILLES/](04_ARCHITECTURES_INTER_FAMILLES/)

---

## Convention d'ecriture des termes

- `Lambda` designe la constante cosmologique.
- `H_0` designe la constante de Hubble.
- `Omega_i` designe les parametres de densite cosmique.
- `sigma_8` designe l'amplitude des fluctuations de matiere.
- `S_8` designe le parametre de tension cosmologique.
- `v` ou `v_Higgs` designe la valeur d'attente dans le vide du champ de Higgs.
- `G_F` designe la constante de Fermi effective.
- `alpha_G` designe le couplage gravitationnel adimensionne.
- `M_Pl` designe la masse de Planck.

Voir aussi :
[Reecriture positive du vocabulaire](01_CADRE_METHODOLOGIQUE/Reecriture_positive_vocabulaire_v0_1.md)
