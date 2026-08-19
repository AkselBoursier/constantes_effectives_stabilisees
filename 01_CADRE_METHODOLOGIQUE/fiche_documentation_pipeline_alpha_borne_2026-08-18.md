# Fiche documentaire — pipeline ALPHA dans son périmètre borné

## Fonction et statut

Fiche de test de documentation computationnelle sur un pipeline de reprise dont
le périmètre est explicitement limité.

```text
PROFIL = PIPELINE_DE_REPRISE_COMPUTATIONNELLE_BORNE
OBJET = T1.5 ALPHA 2026
STATUT = RESULTAT_LOCAL_QUALIFIE_DANS_LE_PERIMETRE
CALCUL_NOUVEAU = NON_LANCE_PAR_CETTE_FICHE
PUBLICATION = NON_DECIDEE
```

## Question et périmètre

Le pipeline traite les produits condensés fournis par le paquet public associé
à l'analyse ALPHA. Il exécute les routes décrites dans le manifeste local,
leur combinaison et le transport vers `alpha_s^(5)(m_Z)`.

Le périmètre ne comprend pas :

- la génération de configurations lattice ;
- le calcul initial de `b_g` ;
- les calculs amont à zéro saveur ;
- la production indépendante des données condensées ;
- une validation générale de toutes les entrées du paquet.

## Documentation technique

### Matériaux et provenance

- archive locale et empreinte SHA-256 ;
- manifeste Julia et empreinte ;
- six fichiers de données condensées BDIO ;
- branche annoncée du paquet ;
- absence d'identifiant de commit du paquet distant ;
- environnement Julia 1.11.5 et manifeste de dépendances ;
- scripts d'entrée exécutés dans l'ordre.

La provenance identifie le matériau utilisé. Elle ne prouve pas que ce matériau
est la dernière version distante ni qu'il représente toute l'analyse publiée.

### Étapes exécutées

```text
nf0_parameters.jl
-> scale.jl
-> running_le.jl
-> lam_nf3.jl
-> lam_dec.jl
-> alphas.jl
```

Les sorties locales sont ignorées par Git et restent des objets de run, non des
résultats publics automatiquement attachés au dépôt.

## Chaîne de qualification

```text
PAQUET_IDENTIFIE
-> ENVIRONNEMENT_INSTANTIE
-> ENTREES_LUES
-> ROUTES_EXECUTEES
-> SORTIES_PRODUITES
-> COMBINAISON_CONTROLEE
-> QUALIFICATION_DU_PIPELINE
```

Le pipeline qualifie le traitement des produits condensés effectivement fournis
et exécutés. Il ne qualifie pas la génération amont ni une mesure indépendante.

```text
RESULTAT_MACHINE = SORTIES_DU_PIPELINE
QUALIFICATION_TECHNIQUE = COUVERTURE_DES_ETAPES_ET_LIMITES
RESULTAT_SCIENTIFIQUE = ENONCE_BORNE_SOUTENU_PAR_CE_PERIMETRE
```

Ces trois niveaux doivent rester séparés dans toute vue future.

## Ce que la fiche permet d'affirmer

- le matériau local utilisé est identifiable par son empreinte ;
- l'environnement et les dépendances de l'exécution sont déclarés ;
- les deux routes et leur combinaison ont été exécutées dans le périmètre du
  paquet ;
- la couverture exacte des opérations est documentée ;
- les éléments non reproduits restent visibles ;
- le résultat local peut soutenir une qualification bornée du pipeline.

## Ce qu'elle ne permet pas d'affirmer

- que l'analyse complète publiée est reproduite ;
- qu'une nouvelle mesure physique a été effectuée ;
- que les produits condensés sont indépendamment validés par cette exécution ;
- que l'absence de données amont est sans effet sur toute interprétation ;
- que le paquet est réutilisable sans son environnement et ses droits d'usage ;
- qu'un résultat technique autorise une nouvelle opération scientifique.

## Conditions de reprise

Une reprise doit réidentifier l'archive ou le paquet, vérifier son empreinte,
contrôler l'environnement et relire le manifeste avant toute exécution. Un
changement de paquet, de données, de dépendances ou de paramétrisation doit être
qualifié séparément s'il peut modifier la cible, le résultat ou la portée.

## Niveaux de partage possibles

```text
DOCUMENTATION_VISIBLE = OUI, SI_EXPURGEE_ET_BORNEE
REPRODUCTION_DU_PIPELINE_BORNE = ETABLIE_DANS_LE_PERIMETRE
REPRODUCTION_DE_L_ANALYSE_COMPLETE = NON_ETABLIE
REUTILISATION_EXTERNE = A_QUALIFIER_PAR_ENVIRONNEMENT_ET_LICENCE
RESULTAT_SCIENTIFIQUE_PUBLIC = DECISION_SEPAREE
```

La fiche peut servir de base à une documentation plus visible, mais ne vaut pas
publication du pipeline ni résultat scientifique public.

## Verdict de la fiche

```text
DOCUMENTATION_COMPUTATIONNELLE = SUFFISANTE_POUR_LE_PERIMETRE
CHAINES_CODE_ENVIRONNEMENT_RESULTAT = DISTINCTES_ET_RELIEES
LIMITES = CONSERVEES
RESULTAT_LOCAL = RECEVABLE_DANS_SON_PERIMETRE
PROMOTION = NON_OUVERTE
PROCHAINE_ETAPE = COMPARER_A_UN_SCRIPT_LOCAL
```
