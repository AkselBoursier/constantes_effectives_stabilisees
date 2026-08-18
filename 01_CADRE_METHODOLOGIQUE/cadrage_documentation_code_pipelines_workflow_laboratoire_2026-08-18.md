# Cadrage de la documentation du code, des pipelines et du laboratoire

## Fonction et statut

Artefact interne de la reconception. Il ouvre une réflexion sur la documentation
computationnelle et le workflow général sans modifier les scripts, les résultats
ou les pipelines existants.

```text
CHANTIER = DOCUMENTATION_TECHNIQUE_ET_WORKFLOW_GLOBAL
STATUT = CADRAGE_A_TESTER
CODE_EXISTANT = INTACT
CALCUL_NOUVEAU = NON_LANCE
PUBLICATION_DE_PIPELINE = NON_DECIDEE
MIGRATION = NON_OUVERTE
```

## Problème distingué

Une chaîne computationnelle contient plusieurs objets qui ne doivent pas être
confondus :

```text
CODE
-> ENVIRONNEMENT
-> DONNEES_ET_ENTREES
-> EXECUTION
-> SORTIES_MACHINE
-> QUALIFICATION_TECHNIQUE
-> RESULTAT_SCIENTIFIQUE
-> VERDICT_ET_PORTEE
```

La documentation doit permettre de suivre cette chaîne, mais chaque niveau doit
conserver son propre statut. Documenter un script ne valide pas son résultat ;
exécuter un pipeline ne constitue pas une nouvelle mesure ; publier un manifeste
ne transforme pas les données en preuve indépendante.

## Quatre couches de documentation

| Couche | Fonction | Contenu minimal | Ce qu'elle n'établit pas |
|---|---|---|---|
| **Documentation du code** | Comprendre ce que fait le script ou le module | Entrées attendues, sorties produites, dépendances, paramètres, limites, version observée | Validité scientifique du modèle ou des données |
| **Documentation d'exécution** | Rendre une exécution identifiable et reproductible dans son périmètre | Environnement, versions, commande, configuration, empreintes, journaux, erreurs | Reproduction de ce qui n'a pas été exécuté |
| **Qualification technique** | Dire ce que les contrôles ont effectivement vérifié | Contrôles, écarts, diagnostics, couverture, conditions de réussite ou d'échec | Résultat scientifique général |
| **Résultat scientifique** | Exposer un énoncé qualifié et borné | Cible, transformation, régime, données, modèle, soutien, limites, portée, condition de rupture | Validité des scripts au-delà du périmètre instruit |

La relation entre ces couches doit être explicite, mais elles ne doivent pas
être fusionnées dans un seul README ou rapport.

## Documentation d'un pipeline destiné à être partagé publiquement

« Public » ne signifie pas nécessairement « prêt à être réutilisé par tous ».
Avant de rendre un pipeline public, il faut distinguer plusieurs niveaux :

```text
DOCUMENTATION_VISIBLE
DOCUMENTATION_REPRODUCTIBLE
PIPELINE_REUTILISABLE
PIPELINE_REPRODUCTIBLE_INDEPENDAMMENT
RESULTAT_SCIENTIFIQUE_PUBLIC
```

Un dépôt peut documenter un pipeline sans garantir sa portabilité. Un pipeline
peut être reproductible dans un environnement figé sans être réutilisable sur
d'autres données. Une publication devrait donc déclarer le niveau effectivement
atteint, plutôt que d'employer « reproductible » comme étiquette globale.

Contrat minimal pour un pipeline public potentiel :

```text
OBJET_ET_QUESTION
CODE_ET_VERSION
DEPENDANCES_ET_ENVIRONNEMENT
DONNEES_ET_PROVENANCE
PARAMETRES_ET_PRIORS_SI_APPLICABLES
COMMANDE_D_ENTREE
SORTIES_ATTENDUES
CONTROLES_EFFECTUES
LIMITES_ET_ELEMENTS_NON_REPRODUITS
LICENCE_ET_DROITS_D_USAGE
CONDITION_DE_REPRISE
```

Les chemins locaux, identifiants privés, données ignorées par Git et secrets ne
font pas partie d'une documentation publique. Ils peuvent être remplacés par
un manifeste expurgé et une procédure locale de reprise.

## Documentation du workflow général du laboratoire

Le workflow global du projet mérite une documentation locale distincte des
résultats scientifiques et du CI. Elle pourrait décrire :

- les plans et axes de travail ;
- les passages entre physique, computation, méthode, philosophie et éditorial ;
- les distinctions de statut et d'autorisation ;
- les conditions de retour, de suspension et de réouverture ;
- les règles de conservation, provenance et no-loss ;
- la différence entre proposition de laboratoire et décision promue ;
- les contrôles humains obligatoires ;
- les limites d'intervention des agents ;
- les liens avec le CI, sans lui déléguer le jugement sémantique ou scientifique.

Cette documentation doit rester un **contrat de fonctionnement local** avant de
pouvoir devenir une porte publique. Elle doit être versionnée, mais ne doit pas
être recopiée dans chaque document d'accueil.

Le CI appartient à ce workflow global comme composante technique. Il ne lui est
pas extérieur : il automatise certaines opérations du contrat de fonctionnement
et remonte des contrôles. Il ne doit toutefois pas absorber les décisions
humaines ni devenir le workflow complet par défaut.

```text
WORKFLOW_GLOBAL
 = SEMANTIQUE + RECHERCHE + PROVENANCE + DECISION_HUMAINE + CI
CI = COMPOSANTE_TECHNIQUE, NON_EQUIVALENT_DU_WORKFLOW_GLOBAL
AUTOMATISATION = ALLEGEMENT_COGNITIF_SELECTIF
```

L'amélioration ultérieure du CI devra donc partir des objets et transitions
déjà qualifiés : elle cherchera les opérations répétitives, contrôlables et
réversibles qui peuvent être automatisées, tout en laissant humaines les
questions de modèle, de portée, de promotion, d'autorisation et de décision.

## L'audit comme objet de travail potentiel

L'audit lui-même peut devenir un objet documentaire distinct : ses phases,
contre-tests, retours ciblés, décisions, résultats négatifs et effets sur la
transformation du projet constituent une trajectoire de travail, pas un
résultat scientifique à absorber dans les documents audités.

```text
AUDIT = OBJET_DE_WORKFLOW_ET_DE_PROVENANCE
RESULTATS_DE_L_AUDIT = QUALIFICATIONS_BORNEES
EFFETS_SUR_LE_PROJET = A_DOCUMENTer_SEPAREMENT
TEMPLATE = A_DECIDER_APRES_EVALUATION
```

La séparation éventuelle des phases ou la création d'un modèle réutilisable ne
sera justifiée qu'après comparaison entre :

- ce que l'audit a effectivement facilité dans la transformation du projet ;
- les éléments spécifiques à cette trajectoire et non transférables ;
- les contrôles qui ont réellement réduit les pertes ou les ambiguïtés ;
- le coût cognitif et documentaire du modèle lui-même ;
- le risque de transformer une généalogie locale en procédure obligatoire.

Pour l'instant, l'audit est conservé comme workflow local documenté. Sa
templateisation reste une possibilité ouverte, non une sortie attendue.

## Séparation des niveaux de résultat

```text
SCRIPT_DOCUMENTE
!= EXECUTION_IDENTIFIEE
!= SORTIE_MACHINE
!= QUALIFICATION_TECHNIQUE
!= RESULTAT_SCIENTIFIQUE
!= INTERPRETATION
```

Une vue computationnelle peut relier ces niveaux, mais doit afficher les
transitions et les ruptures. Elle doit notamment rendre visible :

- ce qui a réellement été exécuté ;
- ce qui a été fourni par une source externe ;
- ce qui est resté bloqué ou non reproduit ;
- ce qui relève d'une qualification technique ;
- ce qui est soutenu comme résultat scientifique ;
- ce qui demeure une interprétation ou une hypothèse.

## Recommandation provisoire

Ne pas lancer immédiatement une campagne de documentation de tous les scripts.
Commencer par un petit lot représentant trois profils :

1. un pipeline de reprise computationnelle borné ;
2. un script d'analyse ou de qualification locale ;
3. un outil transversal du laboratoire.

Pour chaque profil, construire une fiche de documentation sans déplacer le code,
puis vérifier si les mêmes champs sont réellement utiles. Le schéma doit rester
ouvert à un champ émergent et ne doit pas créer un registre central avant qu'un
besoin de contrôle soit démontré.

Le premier test de ces trois profils est consigné dans :
`01_CADRE_METHODOLOGIQUE/test_documentation_technique_trois_profils_2026-08-18.md`.

Les outils internes mobilisés au fil du projet relèvent du même workflow global.
Ils ne doivent pas provoquer une nouvelle couche de prolifération documentaire.
Un inventaire sélectif peut examiner leur fonction de conservation, d'audit,
de calcul, de coordination ou d'éditorialisation, puis décider au cas par cas
si un outil vaut seulement comme résultat local ou comme proposition de
workflow partageable entre humains, LLM, GitHub et machines.

Le cadrage dédié est consigné dans :
`01_CADRE_METHODOLOGIQUE/cadrage_outils_internes_et_workflow_partageable_2026-08-18.md`.

## Décision réservée

```text
DOCUMENTATION_TECHNIQUE = A_INSTRUIRE
DOCUMENTATION_WORKFLOW_GLOBAL = A_CONSERVER_LOCALEMENT
PIPELINES_PUBLICS = NIVEAUX_DE_PUBLICATION_A_DISTINGUER
CI = A_AMELIORER_PLUS_TARD
RESULTATS_SCIENTIFIQUES = SEPARES_DES_SCRIPTS_ET_SORTIES
MIGRATION = NON_OUVERTE
DECISION_HUMAINE = REQUISE_AVANT_PUBLICATION_OU_PARTAGE
```
