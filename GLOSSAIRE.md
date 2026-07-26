# Glossaire des termes clés du projet

Ce glossaire recense les termes méthodologiques fondamentaux du corpus. Il ne
remplace pas les décisions et protocoles actifs ; il sert de référence rapide.

Documents directeurs :

- [Décision de rang — constance, accès et constitution](01_CADRE_METHODOLOGIQUE/Decision_statuts_constance_acces_constitution_v0_1.md) ;
- [Ajustements directeurs D1–D5](01_CADRE_METHODOLOGIQUE/Ajustements_directeurs_D1_D5_regimes_constance_v0_1.md) ;
- [Verdict final de l’audit de portée](05_CARTES_ET_SYNTHESES/Verdict_final_audit_portee_regimes_constance_v0_1.md).

La [note méthodologique v1.3](01_CADRE_METHODOLOGIQUE/Note_synthese_methodologique_v1_3_pre_familial_et_temporalite.md)
reste un état généalogique important, mais elle ne commande plus seule la
terminologie active.

---

## Termes directeurs

### Constance

> Attribution conditionnée d’un maintien à une cible explicitement identifiée.

Un énoncé de constance doit préciser le `porteur du test`, la transformation, le
régime, l’échelle et la tolérance pertinents. Il ne vaut pas hors de ce domaine
déclaré et conserve une condition de rupture.

La cible peut être une grandeur, une relation, une observable, une prédiction ou une
structure. La constance n’est pas nécessairement produite par une trajectoire
temporelle.

### Stabilisation

> Terme méthodologique de second ordre désignant l’établissement, la consolidation ou
> le maintien de conditions déterminées grâce auxquelles un état, un régime, une
> réalisation, une estimation ou une attribution devient ou demeure opératoire,
> reproductible ou soutenable selon un critère déclaré.

La stabilisation peut concerner l’accès, l’estimation, la réalisation, la chaîne de
preuve, le régime de description ou un mécanisme de maintien. Elle ne désigne ni la
constance de la cible, ni sa constitution, ni la seule robustesse constatée, et elle
ne fournit pas à elle seule une explication.

Forme de contrôle :

```text
stabilisation de X
par Y
dans le régime R
selon le critère C
jusqu’à la rupture E.
```

### Porteur du test

> Cible explicitement identifiée à laquelle un énoncé attribue, refuse ou suspend un
> maintien ou une variation sous des transformations déclarées.

Le `porteur du test` est une fonction analytique relative à une question et à un
régime. Il ne désigne ni un substrat, ni une catégorie ontologique, ni nécessairement
un objet physique individuel. Il peut être une grandeur, une relation, une
observable, un coefficient, un secteur, une prédiction ou une description.

Contrôle minimal :

```text
porteur du test : P ;
transformation : T ;
régime : R ;
tolérance : epsilon ;
verdict : admission, refus ou suspension.
```

### Transformation déclarée

Variation relativement à laquelle un maintien est évalué : temps, échelle physique,
symétrie, changement de régime, convention, unité, schéma, raccordement, voie
d’accès ou condition expérimentale.

### Régime et tolérance

Le régime délimite le domaine physique ou probatoire dans lequel l’énoncé est
soutenu. La tolérance précise la résolution, l’incertitude ou l’ordre d’approximation
auquel le maintien est affirmé.

### Constance effective

> Statut analytique d’un énoncé indexé dans lequel une cible est traitée comme
> maintenue dans une approximation contrôlée, à un ordre et une tolérance déclarés,
> avec corrections et condition de rupture explicites.

`Constance effective` ne désigne pas une espèce d’objets. Le statut ne s’applique pas
automatiquement aux coefficients de Wilson, aux couplages courants, aux constantes de
basse énergie, aux bornes, aux reconstructions, aux valeurs définissantes du Système
international d’unités (SI) ou aux quasi-stationnarités dynamiques.

Les appellations disciplinaires restent premières : constante de Fermi, constante de
basse énergie, constante de couplage, coefficient de Wilson, etc. Leur présence ne
préjuge pas le verdict du cadre.

---

## Dimensions de l’enquête

### Objet

Ce qui est attribué à la grandeur, relation ou secteur lui-même. Exemple : constance
physique, quasi-stationnarité ou validité d’une relation.

### Accès

Les opérations par lesquelles une valeur, une borne ou un domaine admissible sont
établis : mesure, reconstruction, ajustement, inférence, comparaison ou réalisation.

### Constitution

Les structures ou mécanismes par lesquels une relation, un secteur ou un régime
deviennent opératoires : symétrie, seuil, architecture, dynamique, couplage ou
organisation.

Les trois dimensions sont distinctes mais non indépendantes. Aucun ordre universel
n’est imposé.

---

## Portée de l’énoncé

### Portée physique

Le résultat porte sur une grandeur, une relation, un mécanisme ou une prédiction
physique dans un domaine déclaré.

### Portée épistémologique

Le résultat porte sur les conditions de preuve, de reconstruction, de comparabilité
ou de légitimité d’une inférence.

### Portée ontologique

Le résultat engage explicitement une proposition sur le statut de réalité ou le mode
d’être de ce qui est étudié. Cette portée exige un argument distinct et n’est jamais
déduite automatiquement d’un résultat physique ou d’accès.

### Portée non engagée

Verdict positif de contrôle : le résultat n’exige pas de conclusion supplémentaire
sur un plan donné. `Non engagée` ne signifie ni oubli ni insuffisance ; elle borne ce
que l’enquête autorise à conclure.

La question de portée (`Q3`) reste un contrôle interne non public.

---

## Dépendance de chemin

Une dépendance de chemin n’est recevable qu’après typage.

### Chemin ou trajectoire physique

Évolution d’un porteur physique selon une variable et des lois ou conditions
déterminées.

### Chemin historique

Séquence institutionnelle, technique ou conceptuelle par laquelle un statut s’est
installé ou transformé.

### Chaîne expérimentale ou métrologique

Suite de préparation, interaction, détection, étalonnage, correction, réalisation et
comparaison qui produit une trace ou une valeur.

### Chemin computationnel

Suite de calcul, simulation, discrétisation, approximation, évolution numérique ou
traitement de données.

### Chemin inférentiel

Suite reliant données, modèle, vraisemblance, prior, nuisance et conclusion.

### Choix de représentation, de schéma ou de raccordement

Dépendance à une base, une convention, un schéma de renormalisation, un seuil ou une
opération de matching. Elle ne devient pas par elle-même une histoire physique.

Les verdicts `non pertinente` et `non établie` restent disponibles.

---

## Expression historique du projet

### Nom historique : `constantes_effectives_stabilisees`

Le nom du dépôt conserve la formulation exploratoire qui a initié le projet. Il est
un identifiant historique et technique, non une proposition théorique active.

Il ne désigne plus une classe générale de « constantes effectives stabilisées » et
ne crée aucune obligation de conserver les termes `effective` ou `stabilisée` dans
les publications ou dans les analyses locales.

Le syntagme a servi d’échafaudage avant que le projet sache distinguer suffisamment :

```text
constance ;
effectivité ;
stabilisation ;
régime ;
accès ;
constitution ;
portée de l’énoncé.
```

Son utilité passée est reconnue sans droit à la conservation canonique. Sa propagation
est relue prudemment comme l’effet conjoint d’une permissivité exploratoire humaine,
de la traduction et de la généralisation par les grands modèles de langage (LLM), de
la répétition documentaire et de l’absence initiale d’un seuil explicite de
ratification.

### Forme logique de stabilisation

Ancienne question méthodologique : qu’est-ce qui est stabilisé formellement ? Elle
reste utile comme interrogation locale, mais ne précède plus nécessairement toute
enquête. Le point d’entrée dépend du terrain.

---

## Rôles contextuels historiques contrôlés

### Seuil

Rôle d’une grandeur qui sépare des régimes ou délimite une zone de validité. Un seuil
n’est pas une famille universelle ni nécessairement une frontière physique dure.

### Fond

Rôle d’une grandeur qui fournit un niveau de référence dans un régime. Un fond n’est
pas une famille de premier niveau.

### Relation

Rôle d’une grandeur ou structure qui encode une liaison qualifiée entre objets ou
secteurs. Une relation ne se réduit pas à un quotient numérique.

Ces termes restent disponibles comme rôles locaux après test ; ils ne commandent pas
la taxonomie du corpus.

---

## Architecture

### Architecture

Réseau de dépendances, contraintes ou solidarités entre plusieurs grandeurs,
relations ou secteurs. Une architecture décrit une organisation ; elle n’explique
pas automatiquement l’origine des valeurs qu’elle relie.

### Mode de solidarisation

Façon dont plusieurs éléments deviennent solidaires : couplage, contrainte mutuelle,
relation de secteur, hiérarchie, raccordement ou dynamique. Le terme doit être
localisé à un cas.

Les anciennes architectures cosmologique, Saveur–Higgs, métrologique et effective à
basse énergie restent des dossiers de travail ; leur titre ne leur confère pas un
rang ontologique commun.

---

## Huit modes de stabilisation — statut requalifié

La grille des huit modes conserve une valeur heuristique et généalogique. Elle n’est
plus la grille principale ni une classification canonique.

| Mode historique | Usage encore recevable | Confusion à éviter |
|---|---|---|
| valeur mesurée ou ajustée | décrire une estimation robuste dans un régime | estimation robuste = constance de l’objet |
| couplage courant ou situé | nommer une dépendance d’échelle ou de schéma | running = variation temporelle |
| composition exacte | distinguer exactitude algébrique ou définitionnelle | exactitude = mesure infiniment précise |
| convention définissante | décrire une valeur fixée pour une unité | fixation = invariance physique |
| orientation | décrire une relation entre bases ou secteurs | orientation = famille autonome |
| validité limitée | décrire un domaine contrôlé | domaine = processus physique |
| inférence reconstruite | décrire un paramètre obtenu par modèle et données | reconstruction = propriété directement observée |
| borne ou contrainte | décrire une limite ou un domaine admissible | borne = valeur positive de l’objet |

Ces modes peuvent être utilisés localement lorsque leur retrait ferait perdre une
distinction utile. Ils ne remplacent ni D1–D5 ni les preuves propres aux cycles.

Document généalogique : [Grille de lecture des huit modes](05_CARTES_ET_SYNTHESES/Grille_lecture_8_modes_v0_1.md).

---

## Termes de méthode complémentaires

### Régime physique

Domaine d’échelle, d’énergie, de phase ou de contexte dans lequel une description ou
une grandeur opère.

### Régime d’accès

Ensemble des conditions expérimentales, inférentielles, computationnelles ou
métrologiques dans lesquelles une valeur ou une contrainte devient disponible.

### Trajectoire de stabilisation

Terme à employer seulement après typage. Il peut désigner une trajectoire physique,
un chemin historique, expérimental, computationnel ou inférentiel. Il ne doit plus
être utilisé seul comme s’il désignait nécessairement une évolution temporelle de
l’objet.

### Famille fonctionnelle contrôlée

Terme historique pour un regroupement partageant une fonction locale. Il reste une
sortie possible après test de résistance, jamais un point de départ.

### Régime exploratoire

Phase dans laquelle des mots provisoires, analogies et regroupements peuvent être
employés pour rendre l’enquête possible. Leur propagation significative exige un
marquage : statut provisoire, fonction recherchée, cas d’origine, portée locale,
confusions connues et condition de réexamen.

### Régime de ratification

Phase dans laquelle un terme stratégique doit subir des tests de nécessité,
d’ablation, de voisinage lexical, de cas positifs et négatifs, de rang et de portée,
puis une validation humaine et une application documentaire distincte.

La fécondité exploratoire n’équivaut jamais à une ratification rétroactive.

---

## Convention d’écriture

- `Lambda` désigne la constante cosmologique.
- `H_0` désigne la constante de Hubble dans l’usage disciplinaire ; le cadre le qualifie comme paramètre d’état actuel.
- `Omega_i` désigne les paramètres de densité cosmique.
- `sigma_8` désigne l’amplitude des fluctuations de matière.
- `S_8` désigne le paramètre de tension cosmologique.
- `v` ou `v_Higgs` désigne la valeur d’attente dans le vide du champ de Higgs.
- `G_F` désigne la constante de Fermi ; à basse énergie et sous indexation stricte, l’énoncé peut recevoir un statut de constance effective.
- `alpha_G` désigne le couplage gravitationnel adimensionné.
- `M_Pl` désigne la masse de Planck.
- `alpha_s(mu)` désigne le couplage fort dans un schéma et à une échelle déclarés ; il est refusé comme constant sous variation de `mu`.