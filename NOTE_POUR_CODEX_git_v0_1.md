# Note pour Codex - report Git v0.1

## Divergence entre les branches sandbox (Cowork/Claude) et l'etat sur disque (Codex)

### 1. Resume en une phrase

```text
les branches Git creees par la session Cowork contiennent des
versions perimees de 16 fichiers que Codex a edites ensuite ; les
pousser ou les merger ecraserait le travail de Codex. La source de
verite est le repertoire de travail sur disque (versions Codex).
```

### 2. Contexte technique

```text
- la session Cowork a cree ses branches par plomberie Git
  (GIT_INDEX_FILE + commit-tree), a cause de conflits de verrous et
  d'index provoques par la synchronisation OneDrive du dossier .git ;
- branches locales de la session (sandbox) : methodologie,
  philosophie, travail, arborescence ; plus agent/reprise-cycle-
  cosmologique (pre-existante) ;
- ces branches ont ete construites AVANT et INDEPENDAMMENT des
  editions ulterieures de Codex ; elles portent donc les versions
  d'origine des fichiers que Codex a repris.
```

### 3. Consigne principale

```text
NE PAS pousser ni fast-forward ni merger les branches sandbox de
Cowork (methodologie, philosophie, travail, arborescence) vers main
ou vers le remote : elles reverteraient les 16 editions de Codex.
Traiter le repertoire de travail sur disque comme la source de
verite, et committer depuis le disque.
```

### 4. Les 16 fichiers edites par Codex (a preserver)

```text
01_CADRE_METHODOLOGIQUE/Protocole_horodatage_tests_v0_1.md
04_ARCHITECTURES/Architecture_metrologique_SI_notes.md
05_CARTES_ET_SYNTHESES/Index_supplement_pan_philosophique_v0_1.md
05_CARTES_ET_SYNTHESES/Mise_a_jour_intellectuelle_v0_1.md
05_CARTES_ET_SYNTHESES/Plan_livrable_papier_A_v0_1.md
05_CARTES_ET_SYNTHESES/Premier_degagement_these_v0_1.md
06_PHILOSOPHIE/Carte_philosophie_implicite_corpus_v0_1.md
06_PHILOSOPHIE/Programme_deuxieme_cycle_v0_1.md
06_PHILOSOPHIE/README.md
06_PHILOSOPHIE/Situation_03_SI_2019_convention_vecue_v0_1.md
06_PHILOSOPHIE/Synthese_phase_de_test_v0_1.md
06_PHILOSOPHIE/Test_C5_2_constantes_stabilite_v0_1.md
06_PHILOSOPHIE/Test_C5_constante_solaire_v0_1.md
06_PHILOSOPHIE/Test_covariance_architectures_v0_1.md
06_PHILOSOPHIE/Voisinage_02_Coordination_v0_1.md
README.md
```

### 5. Nouveau livrable de la derniere session, a committer

```text
06_PHILOSOPHIE/Releve_paysage_brisure_electrofaible_v0_1.md
(cree apres la resynchronisation Codex ; releve de paysage
philosophique du chantier brisure electrofaible - voir la note de
resume de session pour son contenu.)
c'est le seul fichier de contenu produit apres la reprise Codex qui
peut ne pas encore etre dans l'etat Git canonique.
```

### 6. Fichiers Codex deja sur disque (pour information)

```text
Codex a cree, entre autres :
05_CARTES_ET_SYNTHESES/Audit_integration_branche_philosophique_v0_1.md
01_CADRE_METHODOLOGIQUE/Protocole_travail_redaction_post_philosophie_v0_1.md
ils sont sur disque et references dans l'index supplement ; ils
appartiennent a l'etat Codex, rien a faire de special.
```

### 7. Recommandation de fond

```text
1. committer depuis le repertoire de travail (source de verite),
   en incluant le releve brisure electrofaible ;
2. abandonner les branches sandbox de Cowork (elles ont servi de
   brouillon local, leurs arbres sont perimes) ;
3. envisager d'exclure .git de la synchronisation OneDrive : c'est
   la cause des verrous et de la corruption d'index rencontres
   pendant la session.
```
