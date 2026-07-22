# T1.5 — Rapport de blocage de la reproduction lattice ALPHA 2026 v0.1

## 0. Statut

```text
statut : blocage d’exécution caractérisé ;
date : 21 juillet 2026 ;
étape atteinte : acquisition du paquet de réplication ;
fonction : distinguer indisponibilité scientifique, lacune documentaire et obstacle
           propre à l’environnement d’exécution ;
ne vaut pas : échec de réplication, critique du paquet, invalidation du résultat publié
               ou impossibilité générale de reproduire l’analyse.
```

## 1. Objet de la tentative

La reproduction prioritaire de T1.5 doit commencer par le paquet associé à :

Mattia Dalla Brida et al., « High-precision calculation of the quark–gluon coupling from
lattice QCD », *Nature* **652**, 328–334 (2026).

Les auteurs déclarent que le paquet public contient un jeu réduit des simulations,
suffisant pour reproduire l’analyse et les nombres finaux. Les données sont annoncées
sous le dossier `data`, au format BDIO, avec le code d’analyse fondé sur la méthode Gamma
et la différentiation automatique.

## 2. Disponibilité vérifiée

Le projet public a été identifié sans ambiguïté :

```text
hôte : GitLab de l’IFIC ;
projet : alramos/replication-package-2501.06633 ;
identifiant GitLab : 457 ;
branche : main ;
commits visibles : 3 ;
taille annoncée des fichiers : 236 Ko ;
référence associée : arXiv:2501.06633 et article Nature 2026.
```

La page du projet, la commande de clonage HTTPS et le lien d’archive ZIP sont visibles.
L’article et sa déclaration de disponibilité confirment également la fonction du paquet.

Conclusion :

```text
existence du paquet : établie ;
caractère public : établi ;
taille compatible avec une reproduction locale : établie ;
contenu exact de l’arborescence : non acquis dans l’environnement courant.
```

## 3. Tentatives exécutées

### 3.1 Accès Git

Une tentative de clonage HTTPS a échoué avant tout échange avec le dépôt :

```text
cause observée : résolution DNS impossible pour igit.ific.uv.es.
```

### 3.2 Téléchargement direct de l’archive

Le lien ZIP exposé par GitLab a été demandé par l’outil de téléchargement disponible.
Le téléchargement a échoué sans produire d’archive exploitable.

### 3.3 Lecture par l’interface web

```text
page du projet : lisible ;
page de l’arborescence : chargée, mais GitLab signale une erreur de récupération ;
README : lien identifié, contenu non récupéré par le cache ;
archive ZIP : lien identifié, contenu non récupéré par le cache ;
API GitLab publique : URL construite, mais non ouverte par la politique de sûreté du
                       moteur faute de résultat indexé exact.
```

### 3.4 Résolution forcée vers l’adresse du serveur

L’adresse publique `147.156.49.79`, associée à `igit.ific.uv.es`, a été utilisée avec une
résolution forcée du nom d’hôte pour conserver le contrôle TLS.

```text
résultat : connexion au port 443 impossible depuis le conteneur ;
conséquence : l’obstacle n’est plus réductible à la seule résolution DNS.
```

## 4. Diagnostic du blocage

```text
type : accès réseau de l’environnement ;
niveau : acquisition des matériaux ;
scientifique : non ;
documentaire du projet source : non établi ;
computationnel interne au paquet : non encore testé ;
résolution par reformulation : impossible ;
résolution par donnée locale ou nouvelle route réseau : possible.
```

Le blocage ne permet pas de conclure que le paquet est incomplet ou difficile à exécuter.
Il empêche seulement de lire son README, de verrouiller ses dépendances, d’établir une
empreinte de l’archive et de lancer les scripts.

## 5. Condition exacte de reprise

T1.5 reprend dès qu’une des conditions suivantes est satisfaite :

1. l’archive du projet est placée localement sous un chemin ignoré par Git, par exemple
   `data_external/QCD/replication-package-2501.06633/` ;
2. le dépôt est cloné dans cet espace par un agent disposant d’un accès réseau au serveur ;
3. le contenu du README, du manifeste de dépendances et des scripts d’entrée est fourni
   dans un support accessible.

À la reprise, l’ordre obligatoire sera :

```text
R1 enregistrer URL, commit ou archive et empreinte SHA-256 ;
R2 inventorier l’arborescence sans exécuter de code ;
R3 lire README, licence, manifestes et scripts d’entrée ;
R4 créer un environnement isolé avec versions déclarées ;
R5 exécuter d’abord les contrôles ou exemples minimaux ;
R6 reproduire séparément la route directe, la route découplage et leur combinaison ;
R7 vérifier Lambda_MSbar^(3), alpha_s^(5)(m_Z) et le budget d’erreur ;
R8 comparer les sorties aux nombres publiés et documenter tout écart.
```

Les données externes et environnements ne seront pas versionnés. Git ne conservera que
le manifeste, les empreintes, les scripts auxiliaires propres au corpus et les sorties
dérivées raisonnables.

## 6. État du protocole au blocage

```text
T1.1 — sources et versions : close ;
T1.2 — trois fiches phénoménologiques : close au niveau structurel ;
T1.3 — sélection et fiche lattice : close ;
T1.4 — matrice de comparabilité : close ;
T1.5 — reproduction : bloquée à l’acquisition du paquet ;
T1.6 — classification finale des écarts : non ouverte ;
T1.7 — verdict physique local : non ouvert ;
T1.8 — propagation : non ouverte.
```

Le protocole n’autorise pas à contourner T1.5 en transformant la description publiée du
paquet en reproduction accomplie. Le prochain mouvement scientifique dépend donc d’un
accès effectif aux matériaux de réplication.