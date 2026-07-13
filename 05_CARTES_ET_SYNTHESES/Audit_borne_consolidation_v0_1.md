# Audit borne de la consolidation v0.1

## 0. Statut

```text
statut : audit transversal borne ;
branche auditee : akselboursier-cartographier-projet ;
branche de correction : agent/audit-consolidation-corpus ;
date : 13 juillet 2026 ;
portee : genealogie Git, documents actifs, cycle 10, extractions et workflow ;
exclusion : relecture ligne a ligne de toutes les sources historiques.
```

## 1. Question

```text
la consolidation a-t-elle perdu, tronque ou rendu incoherent le corpus,
et peut-elle devenir le prochain tronc valide ?
```

## 2. Verdict general

```text
genealogie Git saine ;
architecture documentaire amelioree ;
cycles scientifiques 9 et 10 intacts ;
validation conceptuelle et structurelle encore necessaire.
```

Le depot n'est pas casse. La branche de recuperation ne doit cependant pas etre
fusionnee telle quelle dans `main`.

## 3. Resultats confirmes

### 3.1 Genealogie

La branche de recuperation contient :

```text
travail ;
philosophie ;
methodologie ;
arborescence ;
refondation ;
fine-tuning ;
fixite electrofaible dynamique ;
navigabilite Copilot ;
audit de coherence.
```

Les branches de provenance restent conservees.

### 3.2 Pan philosophique

Le dossier `06_PHILOSOPHIE` est present dans la consolidation, avec son README,
ses situations, voisinages, tests et programmes.

Son accessibilite technique est donc acquise. Son rang reste celui d'une
exploration active en amont des decisions canoniques.

### 3.3 Cycle fine-tuning

Le cadrage et les quatre premiers cas sont complets. Le cas weakless est
correctement pondere comme stress test de possibilite et non comme refutation
generale du fine-tuning.

### 3.4 Cycle de fixite dynamique

Les quatre phases sont completes et leurs terminaisons sont presentes.

La reproduction des scripts confirme :

```text
phase 2 : 20 769 points, 0 solution complete ;
phase 3 : 2 077 061 points, 0 solution complete ;
phase 4 : seuils dissipatifs reproduits dans le CSV.
```

Le verdict de phase 4 reste phenomenologique, comme annonce.

### 3.5 Troncatures

Deux cas sont distingues :

```text
troncature d'affichage GitHub ou du connecteur :
le fichier complet existe ;

lacune d'extraction DOCX :
le placeholder est reel, documente, et l'original DOCX reste la reference.
```

Aucune mutilation manifeste n'a ete trouvee dans les documents centraux du
cycle 10.

## 4. Defauts identifies

### 4.1 Contradiction de rang

Le cadre canonique refusait qu'une borne, une reconstruction modele-dependante
ou une tension deviennent des constances de l'objet.

Plusieurs degagements ulterieurs les avaient reunis sous l'expression `modes de
constance`.

Correction adoptee :

```text
constance de l'objet
!=
stabilisation de l'acces
!=
mode de constitution.
```

Reference :

- [Decision de rang](../01_CADRE_METHODOLOGIQUE/Decision_statuts_constance_acces_constitution_v0_1.md)

### 4.2 References actives desynchronisees

Exemples identifies :

```text
Matrice_temporelle_v0_1 au lieu de v0_2 ;
Reecriture_positive_vocabulaire_v0_1 au lieu de v0_3 ;
Workflow GitHub v0.1 encore cite comme actif ;
Plan_livrable_theorique_v0_1 annonce mais absent ;
formule « Fonction situee » encore presente dans un canevas actif.
```

La note methodologique courte a ete corrigee. Les occurrences restantes doivent
etre traitees par le controle structurel et une passe ciblee, sans reecriture
generale.

### 4.3 Taille de la pull request

La PR de consolidation rassemble 170 commits et 282 fichiers. Elle est
techniquement fusionnable mais trop large pour constituer une unite de revue
conceptuelle.

Decision : la conserver en brouillon et integrer d'abord une petite PR de
correction bornee.

### 4.4 Absence de CI au sommet

Les controles annonces n'etaient pas associes a une execution GitHub Actions du
commit de tete.

Un script local de controle structurel est ajoute a `audit/` ; son integration
a une action GitHub reste une etape ulterieure.

## 5. Corrections executees dans le paquet borne

1. creation d'une decision canonique objet / acces / constitution ;
2. creation d'une carte des frottements entre chantiers ;
3. resynchronisation de `refondation-du-domaine.md` avec les cycles 9 et 10 ;
4. correction du README et du guide des agents ;
5. correction de la note methodologique courte et de ses versions actives ;
6. passage de la PR de consolidation en brouillon ;
7. ajout d'un controle automatique de structure.

## 6. Corrections differees mais bornees

Les documents suivants doivent recevoir une passe ciblee avant la fusion finale
vers `main` :

```text
05_CARTES_ET_SYNTHESES/Premier_degagement_these_v0_1.md
05_CARTES_ET_SYNTHESES/Matrice_degagements_theoriques_v0_1.md
05_CARTES_ET_SYNTHESES/Mise_epreuve_degagements_theoriques_exemples_porteurs_v0_1.md
05_CARTES_ET_SYNTHESES/Plan_livrable_papier_A_v0_1.md
05_CARTES_ET_SYNTHESES/Index_raisonne_du_corpus_v1_0.md
01_CADRE_METHODOLOGIQUE/Note_synthese_methodologique_v1_3_pre_familial_et_temporalite.md
```

La passe doit remplacer les promotions de borne ou reconstruction en constance
de l'objet par les formulations de niveau fixees dans la decision canonique.

Elle ne doit pas supprimer les analyses sur les acces, limites ou architectures.

## 7. Procedure de consolidation recommandee

```text
1. revoir la petite PR agent/audit-consolidation-corpus ;
2. l'integrer a akselboursier-cartographier-projet ;
3. executer audit_structure_corpus.py et les audits existants ;
4. effectuer la passe ciblee sur les six documents listes ;
5. retargeter la PR de consolidation vers main ;
6. revoir le diff des documents actifs ;
7. fusionner une seule fois la branche de recuperation ;
8. resynchroniser travail depuis le nouveau main ;
9. fermer les PR historiques comme integrees ou remplacees ;
10. ouvrir les nouveaux chantiers depuis main.
```

Aucune fusion n'est executee par le present audit.

## 8. Formule de cloture

> La consolidation a reuni les memoires du projet. L'audit borne lui ajoute ce
> qui manquait encore : une hierarchie de rang, des jonctions explicites et une
> condition de validation avant qu'elle ne devienne le tronc commun.
