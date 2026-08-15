# Template — application de l'ensemble des règles au workflow (test et export)

## 0. Statut et fonction

```text
statut : support de gouvernement en évaluation, créé le 15 août 2026 ;
         N'EST PAS une couche ratifiée : ce document applique les trois champs
         (incident daté / violation observable / mécanisme de détection) à
         toutes les règles nommées et à chaque étape du workflow, afin de
         (a) tester le dispositif, (b) produire un template exportable ;
fonction : généraliser audit/TEMPLATE_detecteur_ecarts.md (qui ne formalisait
           que la méta-règle) à l'ensemble des règles et du workflow ;
           consigner le bilan du test d'exécution locale du workflow et les
           incohérences révélées ;
ne vaut pas : modification du corpus, extension du registre actif, nouveau
              mécanisme automatisé, ni application des réparations proposées ;
distinct de : audit/regles_actives.md (registre actif, trois règles) —
              ici c'est le TEST et le TEMPLATE, pas la promotion ;
              toute promotion exige validation humaine + réparation distincte
              (méta-règle, appliquée à ce document lui-même).
```

Relation aux pièces existantes :

```text
TEMPLATE_detecteur_ecarts.md : formalise UNE règle (la méta-règle) ;
ce document                  : applique la méthode à TOUTES les règles et au
                               workflow, puis expose le template exportable ;
regles_actives.md            : n'est PAS modifié ici — la promotion d'une règle
                               vers le registre actif est une décision séparée.
```

---

## 1. Rappel des trois champs et des deux familles

Toute règle nommée doit déclarer :

```text
incident daté          : quel événement réel a motivé la règle, et quand ;
violation observable   : quel fait compterait comme un écart ;
mécanisme de détection : qui ou quoi rend cet écart visible.
```

Deux familles — ne pas les confondre :

```text
règles de gouvernement (P28, P29, méta-règle, étapes CI) :
    testées par audit d'écart — ici ;
règles de verdict (P23–P27 et le corpus physique) :
    testées par cas adversariaux + relecture humaine — hors d'un audit ;
    ici n'est déclaré que leur mécanisme d'épreuve.
```

---

## 2. Application aux règles nommées (P23–P29 + méta-règle)

Légende d'évaluation de la testabilité :

```text
[AUTO]   mécanisme automatisable exécutable en CI ;
[HUMAIN] mécanisme de relecture humaine bornée, script non décideur ;
[CAS]    règle de verdict : épreuve par cas adversariaux, non automatisable.
```

### P23 — granularité discriminante

```text
énoncé : subdiviser seulement si la subdivision change le verdict, le rang
         probatoire, la cible ou la décision scientifique suivante ;
         proportionner la profondeur au gain discriminant.
incident daté : dossier alpha à haute résolution puis lots compacts m_p/m_e et
                m_e/y_e/v (juillet 2026) — la structure compacte a suffi lorsque
                les distinctions étaient réutilisées.
violation observable : une subdivision documentaire dont le retrait ne changerait
                       ni verdict, ni rang, ni cible, ni décision — ou
                       l'inverse (un cas non subdivisé alors que le verdict
                       en dépend).
mécanisme de détection : [HUMAIN] arbitrage à la création d'un lot ; signal faible
                         automatisable : un nouveau lot sans phrase de
                         « gain discriminant » dans son accueil.
évaluation : partiellement automatisable ; la substance reste humaine.
```

### P24 — porteur du test et conditions de contrôle

```text
énoncé : rendre contrôlables porteur du test, transformation, régime, échelle /
         schéma / modèle, tolérance, rupture ; le porteur du test est une
         fonction analytique, non un substrat.
incident daté : instauré dans Ajustements_directeurs_D1_D5 (26 juillet 2026) —
                D1/D2/D3.
violation observable : un verdict de constance sans déclaration des six
                       coordonnées de contrôle.
mécanisme de détection : [CAS] relecture humaine des verdicts ; signal faible
                         automatisable : une synthèse de cycle sans les six
                         mots-champs du contrôle minimal.
évaluation : non automatisable sans faux positifs massifs ; épreuve par cas.
```

### P25 — énoncés indexés, non grandeurs nues

```text
énoncé : qualifier des énoncés indexés (régime, échelle, schéma, tolérance),
         non des grandeurs nues.
incident daté : Ajustements_directeurs_D1_D5 (26 juillet 2026).
violation observable : un statut de constance attribué à une grandeur sans
                       indexation explicite.
mécanisme de détection : [CAS] relecture humaine ; pas de signal automatique
                         fiable (le marqueur serait stylistique).
évaluation : non automatisable ; épreuve par cas.
```

### P26 — vocabulaire disciplinaire local avant verdict analytique

```text
énoncé : ordre rédactionnel : vocabulaire disciplinaire local → description du
         cas → conditions du test → verdict analytique éventuel ; « constante
         effective » n'est plus une classe transversale.
incident daté : Ajustements_directeurs_D1_D5 (26 juillet 2026) ; discipline
                réaffirmée dans AGENTS.md §7.
violation observable : une catégorie transversale de type « constante effective »
                       réintroduite sans ratification, ou un verdict analytique
                       précédant la description du cas.
mécanisme de détection : [HUMAIN] relecture ; signal automatisable : réapparition
                         de la catégorie dans un document actif hors archives.
évaluation : partiellement automatisable (détection lexicale), verdict humain.
```

### P27 — résultat ≠ soutien probatoire ≠ verdict

```text
énoncé : distinguer résultat quantitatif, mode de soutien probatoire et verdict ;
         une borne sur la valeur ne produit pas une valeur positive ; une
         non-détection n'est probante que sous conditions déclarées.
incident daté : NON établi dans une issue ou un registre daté — écart consigné
                au Journal_ecarts_gouvernance.md (15 août 2026) ; déclarée dans
                les notes v1.7/v1.8 sans acte séparé.
violation observable : un verdict qui convertit une borne ou une non-détection en
                       valeur positive sans déclarer famille de variations,
                       sensibilité, modèle de conversion, systématiques, domaine,
                       tolérance.
mécanisme de détection : [CAS] NON automatisable — épreuve par cas adversariaux
                         (note v1.7 §5) + relecture humaine des synthèses.
                         Ce template n'affirme pas son application.
évaluation : non automatisable ; famille des règles de verdict.
```

### P28 — ablation documentaire

```text
énoncé : l'appareil de rigueur ne doit pas devenir un second projet ; une couche
         durable exige incident établi, gain discriminant, remplacement d'une
         couche existante, validation humaine ; l'exploration peut créer, seule
         la ratification autorise à conserver durablement.
incident daté : inflation documentaire fin juillet 2026 (Carte_consolidee v0.9→
                v1.3 accumulées sans remplacement déclaré) — registre actif.
violation observable : une couche versionnée créée sans déclarer la version
                       remplacée ou conservée, ou sans incident motivant.
mécanisme de détection : [AUTO] audit_ecarts_regles.py::check_versioned_maps_replacement
                         + [HUMAIN] revue à la création.
évaluation : AUTOMATISÉE (règle de gouvernement) — dans le registre actif.
```

### P29 — traçabilité des instructions par issues

```text
énoncé : tout arbitrage, instruction scientifique bornée, validation
         intermédiaire et décision de sortie est consigné dans une issue avant
         propagation durable ; une PR ne remplace pas la généalogie.
incident daté : arbitrage D9 et étapes A0–A3 conduits hors issue puis réparés
                rétrospectivement (issue #62, 27 juillet 2026) — registre actif.
violation observable : un document Decision_* ou une instruction scientifique
                       sans référence à une issue (#n) ni au registre des
                       arbitrages.
mécanisme de détection : [AUTO] audit_ecarts_regles.py::check_decisions_traced
                         + [HUMAIN] synchronisation de la checklist d'issue.
évaluation : AUTOMATISÉE — dans le registre actif.
```

### Méta-règle — déclaration d'écart (15 août 2026)

```text
énoncé : toute règle nommée déclare incident daté, violation observable et
         mécanisme de détection ; à défaut elle est une formulation exploratoire.
incident daté : 15 août 2026 — P27/P28 énoncées sans acte d'instauration daté ni
                entrée au registre des arbitrages, l'index les déclarant
                « appliquées » sans élément vérifiable.
violation observable : une règle nommée sans occurrence datée ni référence
                       d'issue/registre, ou une section du registre privée d'un
                       des trois champs.
mécanisme de détection : [AUTO] audit_ecarts_regles.py::check_rules_instantiated
                         et ::check_rule_mechanism_declared (auto-appliquée).
évaluation : AUTOMATISÉE — dans le registre actif.
```

### Bilan de testabilité des règles

```text
AUTOMATISÉES (registre actif, CI) : P28, P29, méta-règle ;
PARTIELLEMENT automatisable      : P23 (signal de lot), P26 (signal lexical) ;
NON automatisables (règles de verdict) : P24, P25, P27 — épreuve par cas.
```

Conclusion de gouvernance : **ne pas automatiser P24/P25/P27.** Ce sont des
règles de verdict ; leur test est une épreuve par cas, non un audit d'écart.
Les promouvoir dans le script produirait des faux positifs massifs et
transformerait l'appareil de rigueur en second projet (violation de P28).

---

## 3. Application au workflow (`audit-corpus.yml`), étape par étape

Pour chaque étape : la règle qu'elle protège, sa violation observable, son
mécanisme, et sa sévérité déclarée vs effective.

| # | Étape (workflow) | Règle protégée | Violation observable | Sévérité déclarée | Sévérité effective | Cohérence |
|---|------------------|----------------|----------------------|-------------------|--------------------|-----------|
| 1 | structure (`audit_structure_corpus.py`) | intégrité documentaire | marqueur de conflit, bloc ``` non fermé, lien relatif absent | ERROR bloquant | ERROR bloquant | cohérent |
| 2 | liens (`audit_liens.sh`) | navigabilité | cible .md relative absente | bloquant (exit 1) | NON bloquant en pratique | **incohérent** |
| 3 | encodage (`audit_encodage.sh`) | lisibilité / unicité des titres | fichier non-UTF-8 ; titres H1/H2 dupliqués | encodage bloquant ; titres non bloquants | idem | partiel |
| 4 | assainissement archives (`sanitize_conversation_exports.mjs`) | vie privée / secrets | archive avec identité, lien privé ou URL signée résiduelle | bloquant (exit 1) | bloquant | cohérent |
| 5 | écarts de règles (`audit_ecarts_regles.py`) | méta-règle + P28 + P29 | registre absent (ERROR) ; règle non instrumentée, carte sans remplacement, décision sans issue (WARNING) | ERROR bloquant, WARNING non bloquant | idem | cohérent |
| 6 | données externes / PDF | hygiène de dépôt | `data_external` suivi ; PDF éditeur dans `93_…` | bloquant (exit 1) | bloquant | cohérent |
| 7 | compilation Python | exécutabilité des scripts | syntaxe Python invalide | bloquant | bloquant | cohérent |
| 8 | dépendances test C2 | reproductibilité | échec d'installation | bloquant | bloquant | cohérent |
| 9 | test synthétique C2 | non-régression computationnelle | écart au résultat de référence (`--self-test --allow-missing`) | bloquant | bloquant | cohérent |
| 10 | placeholders (`audit_placeholders.sh`) | complétude d'extraction | placeholder `[  ]`, `[ X= ]` résiduel | **NON bloquant** (`continue-on-error: true`) | NON bloquant | **incohérent** avec la sortie du script (exit 1) |
| 11 | inventaire placeholders | (même étape) | — | — | — | — |

### Incohérences révélées par le test (15 août 2026)

```text
I1 — audit_liens.sh : le script signale « BRISE » par lien absent mais son
     compteur BROKEN est confiné dans des sous-shells (pipes) ; il reste 0 à la
     sortie, donc l'étape ne bloque JAMAIS même avec des liens brisés.
     La sévérité déclarée (bloquant) diverge de la sévérité effective (jamais
     bloquant). Heureusement l'étape 1 (audit_structure_corpus.py) détecte les
     liens absents en ERROR : la protection est assurée, mais par un autre
     mécanisme que celui déclaré. Redondance non assumée = écart dit/fait.

I2 — audit_placeholders.sh : le script sort en exit 1 dès qu'un placeholder
     existe (1064 comptés), mais le workflow l'exécute avec
     `continue-on-error: true` : l'étape est informative, jamais bloquante.
     Le script et le workflow déclarent deux sévérités opposées pour la même
     règle. Il faut choisir : soit la règle est informative (le script sort 0 et
     inventorie), soit elle est bloquante (on retire continue-on-error).

I3 — audit_encodage.sh : les titres H1/H2 dupliqués sont signalés mais n'entrent
     pas dans le calcul de sortie (seul l'encodage fait échouer). Le script
     « vérifie » des doublons sans conséquence : la règle « unicité des titres »
     est instrumentée en détection mais pas en sévérité. Acceptable si assumé
     (détection sans blocage), à déclarer explicitement.

I4 — avertissements structurels massifs : audit_structure_corpus.py émet 1865
     WARNING « titre sans contenu », dont la majorité sont structurels (blocs de
     statut `text` sous un titre de section, titres H1 de garde). Le seuil de
     « titre vide » est trop sensible ; le bruit masque le signal. Le mécanisme
     déclaré (titres vides) est réel mais sa tolérance n'est pas calibrée.
```

---

## 4. Bilan du test d'exécution locale (15 août 2026)

Commandes exécutées à la racine du dépôt (équivalent des étapes CI) :

```text
python audit/audit_structure_corpus.py      -> 526 fichiers, 0 erreur, 1865 avertissements
bash   audit/audit_liens.sh                 -> exit 0 (mais voir I1 : ne bloque jamais)
bash   audit/audit_encodage.sh              -> exit 0, doublons H1/H2 signalés (non bloquants)
node   audit/sanitize_conversation_exports.mjs -> exit 0, 12 fichiers clean
python audit/audit_ecarts_regles.py         -> exit 0, 7 règles nommées, 2 écarts P29
bash   audit/audit_placeholders.sh          -> exit 1 en interne, 1064 placeholders (étape CI non bloquante)
python -m compileall -q audit 02_CYCLES_PHYSIQUES -> OK
```

Écarts concrets détectés par le détecteur d'écarts (déjà actif) :

```text
E1 — P29 : 01_CADRE_METHODOLOGIQUE/Decision_statuts_constance_acces_constitution_v0_1.md
     sans référence à une issue ni au registre des arbitrages.
E2 — P29 : 05_CARTES_ET_SYNTHESES/Decision_statut_fixite_dynamique_v0_1.md
     sans référence à une issue ni au registre des arbitrages.
```

Ces deux écarts sont des **données**, non des fautes : ils doivent être consignés
au Journal_ecarts_gouvernance.md puis réparés (ajout d'une référence d'issue ou
mention explicite de la généalogie), par une action distincte de ce template.

---

## 5. Propositions de réparation (à arbitrer, non appliquées ici)

```text
R1 (P29)  : ajouter une référence d'issue / registre aux deux documents Decision_*
            listés en E1/E2 ; consigner l'écart au journal avant réparation.
R2 (I1)   : corriger audit_liens.sh (propager le compteur hors des sous-shells,
            ex. fichier temporaire ou réécriture sans pipe) OU déclarer
            explicitement que l'étape est redondante avec
            audit_structure_corpus.py et la passer en informatif.
R3 (I2)   : aligner script et workflow : soit placeholders = inventaire
            (script exit 0), soit règle bloquante (retirer continue-on-error).
            Recommandation : inventaire informatif (les placeholders sont un
            état d'extraction connu, pas une violation).
R4 (I3)   : déclarer dans audit_encodage.sh que les doublons de titres sont
            détectés sans blocage (sévérité informative assumée).
R5 (I4)   : calibrer check_empty_headings (ex. ignorer les titres suivis
            immédiatement d'un bloc ```text de statut) pour réduire le bruit.
R6        : ne PAS automatiser P24/P25/P27 (règles de verdict) ; les maintenir
            à l'épreuve par cas. Automatiser P23/P26 seulement comme signaux
            faibles informatifs si le besoin est établi (P28).
```

---

## 6. Template exportable (pour un futur dépôt, et éventuellement celui-ci)

Structure minimale à copier :

```text
audit/
  regles_actives.md            # 3 champs par règle : incident / violation / mécanisme
  Journal_ecarts_gouvernance.md # écarts constatés = données datées
  audit_ecarts_regles.py       # détecteur faible : signale, ne juge pas
.github/workflows/audit-corpus.yml  # exécute le détecteur à chaque PR
```

Principes à exporter (indépendants du contenu du corpus) :

```text
1. Méta-règle : une règle non instrumentée est une résolution, pas une règle.
2. Trois champs obligatoires par règle : incident daté, violation observable,
   mécanisme de détection.
3. Deux familles séparées : règles de gouvernement (audit d'écart) vs règles de
   verdict (épreuve par cas) — ne jamais tester l'une par l'autre.
4. Le détecteur signale, ne juge pas : WARNING par défaut, ERROR seulement si un
   mécanisme déclaré est brisé (cible absente). Fail-weak.
5. Un écart consigné n'annule pas la règle : il la transforme de résolution en
   règle instrumentée. L'absence d'écart détecté ne vaut pas preuve d'application.
6. Aligner la sévérité déclarée et la sévérité effective de chaque étape CI
   (leçons I1/I2/I3) : une étape informative doit être déclarée informative.
7. Ne pas automatiser les règles de verdict ; proportionner la détection au gain
   discriminant (P28) pour éviter le bruit (I4).
8. Le registre se remplit par incidents réels et datés, jamais par anticipation.
```

Contre-factuel minimal : sans ce dispositif, les règles s'accumulent et les
écarts dit/fait ne sont nulle part enregistrés ; un lecteur (humain fatigué ou
LLM) prend les déclarations d'état pour des faits. Avec : chaque écart devient
une donnée datée, et la règle cesse d'être une résolution pour devenir une
assertion testable.

---

## 7. Sortie de ce template

```text
statut : ÉVALUATION — ce document est un test et un template, non une couche
         ratifiée ;
condition de sortie : validation humaine de la méthode, puis arbitrage sur
                      R1–R6 (réparations) et sur la promotion éventuelle de
                      certaines déclarations vers audit/regles_actives.md ;
non-application : aucune règle supplémentaire n'est promue ici ; aucune
                  réparation du corpus n'est effectuée ; le registre actif et
                  le journal ne sont pas modifiés par ce document.
```
