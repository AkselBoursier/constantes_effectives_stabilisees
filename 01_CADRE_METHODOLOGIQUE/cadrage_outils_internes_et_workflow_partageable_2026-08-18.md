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
| **Outil éditorial** | Relire, réécrire et comparer une pièce selon sa classe, son public, sa portée et ses limites | `Reecriture_positive_vocabulaire_v0_3.md` et `Protocole_travail_redaction_post_philosophie_v0_1.md` | Réduire le polissage à un changement de ton ou affaiblir un refus |

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

L'outil éditorial est mobilisé avec ce premier lot. Il ne s'agit pas d'un
simple lissage stylistique : la pièce est relue dans son ensemble, sa fonction,
son public, son contenu unique, ses limites et sa provenance sont rappelés,
puis la rédaction positive est appliquée sans retirer les refus ni les
conditions de portée.

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

## Mobilisation sélective sur pièce

Le fil outils et workflow ne fait pas l'objet d'un nouvel inventaire abstrait.
Les outils déjà fabriqués sont toutefois mobilisés sur les pièces de la
reconstruction lorsque leur fonction, leur classe et leur contrat le justifient.
Cette utilisation directe sur pièce est désormais le mode principal de
qualification restant : elle permet de vérifier la robustesse, la
fonctionnalité et la transportabilité dans une opération réelle.

```text
FIL_OUTILS = MOBILISATION_SELECTIVE_SUR_PIECE
RESULTATS_LOCAUX = CONSERVES
PROMOTION = NON_OUVERTE
TEST_DIRECT_SUR_PIECE = MODE_DE_TRAVAIL_ACTIF
TEMPLATE = NON_DECIDE
NOUVEL_OUTIL = NON_REQUIS_SANS_DEFICIT
```

Chaque opération doit déclarer l'outil mobilisé, sa fonction, ses entrées, ses
sorties, ses garanties effectives et ses limites. Un résultat technique reste
séparé de la lecture humaine et de la décision de promotion. Le changelog n'est
donc pas seulement une archive : il conserve la mémoire opératoire nécessaire
pour reprendre et appliquer les transformations qualifiées, sans devenir une
autorité scientifique ni un registre exhaustif.

## Contrat local de l'outil d'écriture

Pour chaque pièce reconstruite, l'outil d'écriture suit le circuit :

```text
RELECTURE_COMPLETE_DE_LA_PIECE
-> CLASSE + PUBLIC + FONCTION + PORTEE + PROVENANCE
-> RESULTATS, ACQUIS ET LIMITES A_CONSERVER
-> REECRITURE_POSITIVE_STRUCTURELLE_ET_LEXICALE
-> COMPARAISON_AVANT_APRES
-> CONTROLE_DE_PERTE_ET_DE_PORTÉE
-> LECTURE_HUMAINE
-> DECISION_DE_PROMOTION
```

La règle positive v0.3 et le protocole de rédaction sont les références
actuelles de ce circuit. Une future skill ne sera envisagée qu'après plusieurs
usages sur des pièces de classes différentes, si un gain de continuité et de
charge cognitive est effectivement observé. Son existence ne sera pas déduite
de la seule répétition du protocole.
