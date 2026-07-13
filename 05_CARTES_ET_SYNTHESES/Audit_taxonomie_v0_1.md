# Audit de taxonomie v0.1

## Etat, diagnostic et decisions de simplification

### 1. Fonction de ce document

Cet audit repond a la demande d'un regard critique sur la taxonomie actuelle.

Il ne reecrit pas les documents actifs.

Il pose trois questions :

```text
1. Qu'est-ce qui reste de la taxonomie dans la structure du corpus ?
2. Qu'est-ce qui bloque le developpement ?
3. Qu'est-ce qui peut etre simplifie, archive ou recentre ?
```

---

### 2. Inventaire des couches taxonomiques

Le corpus superpose six couches distinctes.

| Couche | Contenu | Statut actuel |
|---|---|---|
| Familles historiques | Seuil, Fond, Relation, familles fragiles | Abandonnees comme familles ; converties en roles et architectures depuis v1.3 |
| Fonctions directrices | Couplage, Echelle, Raccordement, Orientation, Convention | Utiles comme rangs 1 ; rarement citees comme telles dans les syntheses actives |
| Roles contextuels | Seuil, Fond, Relation comme roles | Actifs et utiles ; mais homonymes des familles abandonnees |
| Rangs 0-5 | Forme -> fonction -> role -> acces -> architecture -> trajectoire | Operationnel ; c'est la vraie methode de lecture |
| Architectures | Saveur-Higgs, SI, Effective basse energie, Cosmologique | Operationnel ; ce sont les unites structurantes actives |
| Modes de stabilisation | 8 modes | Central ; c'est le resultat theorique emergent |

Lecture :

```text
la methode a bien evolue depuis les familles historiques.
Mais les six couches coexistent dans les memes documents,
les memes noms de dossiers et les memes regles.
Le corpus reste organise autour de ce qu'il veut depasser.
```

---

### 3. Diagnostic : ce qui bloque le developpement

#### 3.1 La Matrice de criblage est un labyrinthe

Le document `01_CADRE_METHODOLOGIQUE/Matrice_criblage_taxonomique_v0_1.md`
compte 16 sections, 350 lignes et impose une procedure de 35 questions avant
de pouvoir dire quoi que ce soit sur une grandeur.

Ce document etait necessaire pour interdire le retour aux familles.

Il n'est plus necessaire pour travailler : la procedure courte
(`Note_methodologique_courte_post_v1_3.md`) remplit le meme role
en une page.

Decision :

```text
la Matrice de criblage passe en document de reference historique.
Elle n'est plus le protocole operatif obligatoire.
La procedure courte suffit pour tout travail actif.
```

#### 3.2 Le dossier 03_TESTS_TAXONOMIQUES est une archive mal signalee

Son README reconnaissait lui-meme que son contenu ne devient actif
"que si les conclusions passent la methode v1.3".

C'est une archive de travail antérieur, non un dossier de methode active.

Son existence comme dossier numerote au meme niveau que les cycles physiques
lui donne un statut qu'il n'a plus.

Decision :

```text
03_TESTS_TAXONOMIQUES est explicitement archive.
Il n'est pas supprime : il conserve la genealogie du travail.
Il n'est plus reference comme source active.
```

#### 3.3 Le dossier 04_ARCHITECTURES porte un nom obsolete

La Carte consolidee v1.3 dit explicitement :

> "inter-familles" : terme genealogique. Employer seulement pour rappeler l'histoire du corpus.

Mais c'est aussi le nom d'un dossier actif central.

Ce nom continue de faire croire que les architectures sont definies par
rapport aux familles, alors qu'elles sont definies par regime, solidarite,
acces et trajectoire.

Decision :

```text
Le dossier 04_ARCHITECTURES sera renomme 04_ARCHITECTURES
lors d'une prochaine session de reorganisation.
Cette operation necessite une mise a jour de tous les liens internes :
elle est signalee ici mais pas executee automatiquement.
```

#### 3.4 La regle 3 du README bloque les changements

La regle actuelle dit :

> Ne pas transformer les architectures en familles ni modifier la taxonomie de fond.

Cette regle avait du sens quand le risque etait de revenir aux familles.

Elle bloque maintenant la simplification de la taxonomie elle-meme.

Decision :

```text
La regle 3 est reformulee pour proteger les architectures physiques
sans bloquer l'evolution de la taxonomie methodologique.
```

#### 3.5 Les modes de stabilisation sont le resultat central, mais secondaires dans la structure

Les 8 modes de stabilisation (valeur mesuree, couplage courant, composition
exacte, convention definissante, orientation, validite limitee, inference
reconstruite, borne ou contrainte) sont la reponse la plus directe a la
question directrice du projet.

Ils apparaissent a la section 5 de la Carte v1.3, apres les rangs, les roles,
les acces, les architectures et les trajectoires.

Ce n'est pas leur bonne place.

Decision :

```text
Les modes de stabilisation doivent etre presentes comme la grille de lecture
principale du corpus, pas comme l'une des sections d'une carte methodologique.
```

---

### 4. Ce qui n'est pas un probleme taxonomique

Certains documents contiennent beaucoup d'occurrences de "famille"
sans que ce soit un probleme.

Cas 1 : documents genealogiques ou historiques.

```text
03_TESTS_TAXONOMIQUES/*
01_CADRE_METHODOLOGIQUE/00_Sources_docx/*
versions anterieures des cartes et notes
```

Ces documents sont des archives. Leur vocabulaire reflete l'etat anterieur.

Cas 2 : expressions techniques controlees.

```text
"famille fonctionnelle" comme sortie taxonomique apres test de resistance.
```

Ce terme reste disponible comme sortie possible, pas comme point de depart.

Son usage controle n'est pas un probleme.

Cas 3 : noms de roles contextuels homonymes.

```text
Seuil, Fond, Relation comme roles contextuels.
```

Ces roles sont actifs et utiles. Leur nom est malheureux car identique
aux anciennes familles, mais le sens est different.

---

### 5. Decisions actives issues de l'audit

| Decision | Portee | Statut |
|---|---|---|
| Matrice de criblage passe en archive | `01_CADRE_METHODOLOGIQUE/Matrice_criblage_taxonomique_v0_1.md` | Applique ici |
| 03_TESTS_TAXONOMIQUES passe en archive signalee | `03_TESTS_TAXONOMIQUES/README.md` | Applique ici |
| Regle 3 du README reformulee | `README.md` | Applique ici |
| Glossaire simplifie | `GLOSSAIRE.md` | Applique ici |
| Dossier 04 renomme | `04_ARCHITECTURES/` -> `04_ARCHITECTURES/` | A planifier |
| Modes de stabilisation recentres | Prochaine carte ou note | A produire |

---

### 6. Ce que la taxonomie actuelle autorise encore

Meme simplifiee, la methode conserve une structure taxonomique minimale.

Elle est necessaire pour qualifier les grandeurs.

Structure minimale conservee :

```text
1. Forme logique de stabilisation (rang 0)
2. Mode de stabilisation (valeur, composition, convention, orientation,
   validite, inference, couplage, borne)
3. Role contextuel si pertinent (Seuil, Fond, Relation)
4. Architecture si plusieurs grandeurs sont solidaires
5. Limite conservee
```

Ce qui disparait :

```text
- le criblage obligatoire en 6 rangs avant tout enonce
- la matrice de 35 questions comme protocole de travail
- la famille fonctionnelle comme case disponible par defaut
- le dossier de tests taxonomiques comme reference active
```

---

### 7. Reformulation positive apres audit

Ce que le corpus stabilise n'est pas un classement de grandeurs physiques
dans des familles.

C'est une methode de lecture des modes de stabilisation situes :

```text
une grandeur physique stabilise un mode de robustesse
dans un regime et par un acces determines,
avec une trajectoire explicite
et des limites conservees.
```

Les architectures montrent que certaines grandeurs ne se stabilisent
pas seules.

Les roles contextuels montrent que certaines fonctions ne valent que
dans un contexte.

Les familles n'ajoutent rien a ce que les modes, les roles et les
architectures disent deja.

---

### 8. Formule de cloture

```text
La taxonomie etait un outil de construction.
Le corpus n'en a plus besoin comme cadre.
Il en a besoin comme controle minimal contre la proliferation.
La matrice des modes de stabilisation remplace le bestiaire des familles.
```

Document de travail suivant recommande :

```text
Produire une version courte de la grille de lecture centree sur les 8 modes
de stabilisation, sans reference aux familles fonctionnelles.
```
