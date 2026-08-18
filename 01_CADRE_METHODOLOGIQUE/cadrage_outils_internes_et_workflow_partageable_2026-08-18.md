# Cadrage des outils internes et du workflow partageable

## Fonction et statut

Artefact interne de la reconception du workflow global. Il n'ouvre pas un
nouveau projet autonome : il fournit une règle de tri pour les outils déjà
mobilisés ou créés dans le laboratoire.

```text
OBJET = OUTILS_INTERNES_DU_WORKFLOW
STATUT = INVENTAIRE_SELECTIF_A_TESTER
PROLIFERATION = REFUSEE
NOUVEL_OUTIL = JUSTIFICATION_PAR_GAIN_DISCRIMINANT
PUBLICATION = NON_DECIDEE
```

## Principe de non-prolifération

Un outil n'est pas documenté, généralisé ou rendu public parce qu'il existe ou
parce qu'il a été utile une fois. Il devient un candidat de workflow partageable
seulement si son usage est répétable, son périmètre compréhensible et son gain
supérieur au coût de documentation, maintenance et apprentissage.

```text
OUTIL_EXISTANT = OBJET_A_EVALUER
OUTIL_REUTILISABLE = HYPOTHESE_A_TESTER
OUTIL_PUBLIC = DECISION_HUMAINE_SEPAREE
NOUVELLE_COUCHE = NON_JUSTIFIEE_PAR_DEFAUT
```

## Profils d'outils à distinguer

| Profil | Fonction | Exemple local | Risque |
|---|---|---|---|
| **Outil de conservation** | Préserver l'intégrité ou la provenance d'une opération documentaire | Append contrôlé du changelog | Confondre intégrité technique et validité du contenu |
| **Outil d'audit** | Détecter des défauts structurels ou des risques bornés | Audit structurel du corpus | Transformer un contrôle partiel en audit exhaustif |
| **Outil computationnel** | Exécuter ou analyser une opération scientifique locale | Scripts neutrino ou cosmologiques | Confondre exécution et résultat scientifique |
| **Outil de coordination** | Aider aux passages entre humain, LLM, GitHub et dépôt | Routes d'issues, journaux et contrats | Créer une plomberie plus lourde que le gain humain |
| **Outil éditorial** | Tester, comparer ou documenter une forme | Prototypes et matrices Human-First | Promouvoir un essai par simple réutilisation |

Ces profils peuvent se recouper. Ils ne constituent pas une taxonomie fermée.
Un outil peut rester transversal ou non classé si cette description est plus
fidèle.

## Contrat minimal d'un outil candidat

```text
NOM_DE_TRAVAIL
FONCTION
UTILISATEURS = HUMAIN, LLM, GITHUB, MACHINE_OU_COMBINAISON
ENTREES
SORTIES
GARANTIES_EFFECTIVES
LIMITES
DEPENDANCES
EFFETS_SUR_LA_CHARGE_COGNITIVE
RISQUES_DE_FAUSSE_AUTORITE
CONDITIONS_DE_REUTILISATION
NIVEAU_DE_DOCUMENTATION
DECISION_DE_PROMOTION
```

Le champ `GARANTIES_EFFECTIVES` doit décrire ce que l'outil contrôle réellement.
Le champ `RISQUES_DE_FAUSSE_AUTORITE` doit empêcher qu'un résultat vert, un
rapport ou une route soit lu comme validation scientifique ou autorisation.

## Critères de passage vers un workflow partageable

Un outil peut devenir une proposition publique d'amélioration de workflow si
les tests montrent :

- une fonction stable et compréhensible ;
- une réduction mesurable ou qualitativement claire de la charge cognitive ;
- des entrées et sorties contrôlables ;
- des refus et limites explicitement documentés ;
- une dépendance raisonnable à l'environnement ;
- une séparation nette entre contrôle technique et décision humaine ;
- une réutilisation possible sans imposer la généalogie complète du projet ;
- une maintenance moins coûteuse que l'opération manuelle qu'il remplace.

La publication peut rester une proposition de workflow, et non un paquet logiciel
ou une norme générale. Le partage peut porter sur une idée, un contrat, un
exemple ou un outil, selon ce que le test justifie.

## Premier inventaire sélectif

Le premier lot d'outils à examiner peut rester limité à :

1. `tools/append_audit_changelog.py` — conservation append-only ;
2. `audit/audit_structure_corpus.py` — audit structurel borné ;
3. un script computationnel local — analyse scientifique située ;
4. un contrat ou une matrice éditoriale — coordination de rédaction.

Ce lot couvre les interfaces machine, dépôt, LLM et humain sans créer de nouveau
répertoire fonctionnel. Aucun inventaire exhaustif de tous les outils n'est
requis avant de tester ces profils.

## Décisions réservées

```text
INVENTAIRE_GLOBAL = NON_LANCE
PREMIER_LOT = SELECTIF
PROMOTION_PUBLIQUE = NON_OUVERTE
NOUVEAU_PROJET = NON_CREE
CI = PARTIE_DU_WORKFLOW_GLOBAL
DECISIONS_HUMAINES = CONSERVEES
```
