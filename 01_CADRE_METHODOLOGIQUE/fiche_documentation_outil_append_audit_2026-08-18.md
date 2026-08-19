# Fiche documentaire — outil append-only du changelog

## Fonction et statut

Fiche de test du contrat de documentation technique sur un outil transversal du
laboratoire.

```text
PROFIL = OUTIL_DE_CONSERVATION
OBJET = tools/append_audit_changelog.py
STATUT = OUTIL_LOCAL_UTILISE
RESULTAT_SCIENTIFIQUE = NON
PUBLICATION = NON_DECIDEE
```

## Fonction

L'outil ajoute un bloc Markdown à un changelog sous contrôles append-only. Il
protège une opération documentaire ; il ne qualifie pas le contenu ajouté et ne
décide pas de la valeur scientifique de l'entrée.

## Entrées

```text
TARGET
ADDITION
REPO_ROOT
EXPECTED_SHA256
REQUIRED_TAIL
GIT_EXECUTABLE_OPTIONNEL
```

La cible doit rester dans le dépôt, être Markdown et ne pas se trouver sous
`data_external`. Le SHA attendu et le marqueur de fin doivent correspondre à
l'état avant écriture.

## Opérations garanties

- résolution de cible à l'intérieur du dépôt ;
- refus des extensions non Markdown et de `data_external` ;
- vérification SHA-256 avant mutation ;
- vérification du marqueur de fin ;
- ajout en fin de fichier uniquement ;
- écriture temporaire et remplacement atomique ;
- vérification du préfixe avant et après remplacement ;
- lecture de contrôle après écriture ;
- contrôle `git diff --check` ;
- signalement de l'ajout éventuel d'une nouvelle ligne finale.

## Ce que l'outil établit

```text
OPERATION_APPEND = CONTROLEE_DANS_SON_PERIMETRE
PREFIXE_EXISTANT = CONSERVE
CIBLE = RESTE_DANS_LES_CONTRAINTES_TECHNIQUES
DIFF_CHECK = EXECUTE
```

Il établit seulement que l'opération technique contrôlée a respecté ses
préconditions et contrôles. Il n'établit pas :

- que le bloc ajouté est exact ;
- que le changelog est exhaustif ;
- que la décision consignée est valide ;
- que le résultat scientifique mentionné est qualifié ;
- qu'une promotion ou une migration est autorisée.

## Dépendances et environnement

L'outil utilise la bibliothèque standard Python et Git. Il prévoit la présence
de Git dans le PATH et un chemin Windows standard de repli. Cette connaissance
est une dépendance d'exécution, pas une garantie de portabilité universelle.

## Échecs et refus

L'outil refuse notamment :

```text
CIBLE_HORS_DEPOT
EXTENSION_NON_MARKDOWN
DATA_EXTERNAL
CIBLE_ABSENTE
ADDITION_ABSENTE_OU_VIDE
SHA_INCORRECT
MARQUEUR_DE_FIN_ABSENT
PREFIXE_NON_CONSERVE
READBACK_INCORRECT
DIFF_CHECK_EN_ECHEC
```

Un refus technique ne constitue pas un refus scientifique. Il signale qu'une
opération documentaire n'a pas satisfait le contrat local.

## Relation avec le workflow global

```text
DECISION_HUMAINE
-> BLOC_MARKDOWN_PREPARE
-> OUTIL_APPEND_CONTROLE
-> DIFF_ET_LECTURE_HUMAINE
-> COMMIT_EVENTUEL
```

L'outil allège la vérification mécanique de l'opération. Il ne remplace ni la
préparation du bloc, ni la lecture humaine, ni la décision de commit ou de
promotion.

## Niveau de partage possible

L'outil pourrait devenir une proposition publique de workflow si son contrat,
son comportement de refus et ses limites sont suffisamment documentés pour un
autre dépôt. Cette possibilité n'est pas établie par la présente fiche.

```text
DOCUMENTATION_VISIBLE = POSSIBLE
REUTILISATION = A_TESTER_SUR_UN_AUTRE_DEPOT
GARANTIE_SCIENTIFIQUE = AUCUNE
PROMOTION_PUBLIQUE = NON_DECIDEE
```

## Verdict de la fiche

```text
CONTRAT_DOCUMENTAIRE = SUFFISANT_POUR_CE_PROFIL
GARANTIES_TECHNIQUES = DISTINCTES_DU_CONTENU
CHARGE_COGNITIVE = REDUITE_SUR_L_OPERATION_APPEND
DECISION_HUMAINE = CONSERVEE
TEMPLATE_GENERAL = NON_DEDUIT
PROCHAINE_ETAPE = COMPARER_A_UN_OUTIL_D_AUDIT_STRUCTUREL
```
