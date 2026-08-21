# Consigne évaluateur — Phase III-B prospective

## Statut

À utiliser seulement après réception et gel d'une réponse brute. Ne pas fournir aux agents testés. La clé des conditions reste cachée jusqu'au gel des quatre réponses et des scores Human-First primaires.

## 1. Unité d'évaluation

Chaque réponse comporte :

- `A. Réponse principale` : objet de l'évaluation intellectuelle et Human-First ;
- `B. Trace de contrôle compacte` : matériau de vérification pour déclencheurs, sources, silences et informations manquantes.

La trace ne donne aucun point Human-First par sa longueur ou sa technicité.

## 2. Ordre de scoring

Pour chaque réponse, avant toute comparaison entre conditions :

1. conserver le texte brut inchangé ;
2. attribuer les flags critiques ;
3. scorer les axes communs `E/S/P/M` ;
4. scorer la couche fonctionnelle `F1-F4` ;
5. pour la tâche S, scorer `RC1-RC4` et `QS1-QS6` ;
6. pour la tâche M, scorer `QM1-QM6` ;
7. enregistrer les mesures descriptives d'efficacité ;
8. faire scorer Human-First indépendamment sur la réponse principale.

Ne pas construire de total global unique. Conserver les profils par axe.

## 3. Human-First

La grille `Grille_Human_First_III_B.csv` est distincte.

Le jugement humain de l'auteur est la mesure primaire. Un évaluateur LLM peut fournir un second scoring aveugle, sans remplacer ce jugement.

Avant scoring Human-First :

- anonymiser le nom de la condition ;
- masquer le fichier de matrice assigné et la clé ;
- ne pas récompenser la longueur, les codes ou le nombre de chemins ;
- juger si la réponse principale seule permet réellement de comprendre l'objet, la chaîne de raisonnement, le verdict, les limites et la réouverture.

## 4. Règles anti-biais

- comparer directement seulement les réponses de la même tâche ;
- ne pas corriger un score après révélation de la condition sauf erreur matérielle documentée ;
- ne pas attribuer un avantage parce qu'une réponse reprend davantage de mots de la matrice ;
- `nombre de règles citées` n'est pas un critère ;
- une fonction non citée peut avoir été correctement appliquée implicitement ;
- une règle citée sans ancrage factuel peut recevoir un faible score `F2` ;
- longueur et exhaustivité de forme ne valent pas profondeur ;
- `NON_ETABLI` correctement justifié peut être supérieur à une conclusion plus ambitieuse ;
- une erreur critique ne doit pas être masquée par un profil élevé ailleurs.

## 5. Efficacité descriptive — hors score principal

Enregistrer :

```text
nombre_de_sources_ouvertes
nombre_de_detours_identifiables
volume_de_la_reponse_principale
volume_de_la_trace
nombre_d_affirmations_fortes_insuffisamment_soutenues
retours_inutiles_aux_memes_sources
```

Ces mesures ne récompensent pas automatiquement la brièveté.

## 6. Références évaluateur

Tâche S :

- `../Reference_evaluateur_cadre_canonique_III_B.md` ;
- sources réelles du Cycle 10 sur `main@c9deaf1f...`.

Tâche M :

- `Reference_evaluateur_tache_M.md` ;
- `main@c9deaf1f...` ;
- `test/human-first-reprise-blind-20260819` ;
- issue #136 et commentaires pertinents.

Ces références servent à vérifier les faits, pas à imposer une rédaction identique.

## 7. Comparaison après quatre réponses

Seulement après scoring individuel et Human-First :

1. comparer `S_7A` à `S_9C` ;
2. comparer `M_7A` à `M_9C` ;
3. rechercher classes d'avantage/perte, pas seulement différences numériques ;
4. révéler ensuite la clé 7A/9C ;
5. interpréter en regard des Phases I-II et de III-A sans réécrire leurs scores.

## 8. Réplication

Une réplication supplémentaire n'est ouverte que si un signal discriminant apparaît :

- différence substantielle sur un axe primaire ;
- erreur critique dans une seule condition ;
- récupération canonique nettement différente ;
- compromis Human-First / profondeur opposé ;
- divergence méthodologique susceptible de provenir de la représentation plutôt que du cas.

Aucune réplication automatique si les profils restent substantiellement indiscernables.
