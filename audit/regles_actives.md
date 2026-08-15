# Registre des règles actives — déclaration d'écart

## 0. Statut et fonction

```text
statut : support de gouvernement instrumenté, créé le 15 août 2026 ;
fonction : déclarer, pour chaque règle nommée du corpus, l'incident daté qui
           la motive, l'événement observable qui compterait comme sa violation
           et le mécanisme qui détecte cet écart ;
ne vaut pas : nouvelle taxonomie de statuts, ni couche STATUTS_ACTIFS déguisée,
              ni preuve que les règles sont effectivement suivies ;
instrumenté par : audit/audit_ecarts_regles.py, exécuté dans audit-corpus.yml.
```

Ce registre applique la méta-règle du 15 août 2026 : **une règle non
instrumentée est une résolution, pas une règle.** Il ne déclare pas la
conformité ; il rend l'écart *observable*. L'absence d'écart détecté ne vaut
pas preuve d'application (contrôle réflexif P27 amendé) : elle signifie seulement
que le mécanisme déclaré n'a pas signalé.

Le registre répond, par règle, à trois champs obligatoires :

```text
incident daté        : quel événement réel a motivé la règle, et quand ;
violation observable : quel fait compterait comme un écart ;
mécanisme de détection : qui ou quoi rend cet écart visible.
```

Une règle qui ne peut remplir ces trois champs est rangée comme
**formulation exploratoire** (P28 amendée), sans autorité normative, et le
détecteur la signale.

Distinction des familles (point 3) :

```text
règles de gouvernement (P28, P29, méta-règle) :
    testées par audit d'écart — ce registre + audit_ecarts_regles.py ;
règles de verdict (P27 et le corpus physique) :
    testées par cas adversariaux (note méthodologique v1.7 §5),
    hors de ce registre ; ici n'est déclaré que leur mécanisme d'épreuve.
```

---

## Règles de gouvernement

### P28 — ablation documentaire

```text
énoncé : l'appareil de rigueur ne doit pas devenir un second projet dont la
         croissance concurrence la recherche qu'il doit protéger ; une couche
         durable exige incident établi, gain discriminant, remplacement d'une
         couche existante, validation humaine.
incident daté : inflation documentaire constatée fin juillet 2026 (versions
                successives de cartes consolidées v0.9→v1.3 accumulées sans
                remplacement déclaré ; couches STATUTS_ACTIFS envisagées).
violation observable : une nouvelle couche versionnée (ex. Carte_consolidee_vX)
                       créée sans déclarer la version qu'elle remplace ou
                       conserve, ou sans incident motivant.
mécanisme de détection : audit_ecarts_regles.py::check_versioned_maps_replacement
                         (signale l'accumulation) + revue humaine à la création.
```

### P29 — traçabilité des instructions scientifiques par issues

```text
énoncé : tout arbitrage, instruction scientifique bornée, validation
         intermédiaire et décision de sortie est consigné dans une issue GitHub
         avant propagation durable ; une PR ne remplace pas la généalogie.
incident daté : arbitrage D9 et étapes A0–A3 conduits hors issue puis réparés
                rétrospectivement (issue #62, 27 juillet 2026).
violation observable : un document Decision_* ou une instruction scientifique
                       sans référence à une issue (#n) ni au registre des
                       arbitrages ; une étape substantielle absente des
                       commentaires de l'issue active.
mécanisme de détection : audit_ecarts_regles.py::check_decisions_traced
                         (référence absente) + synchronisation de la checklist
                         d'issue (revue humaine, P29 point 5).
```

### Méta-règle — déclaration d'écart (15 août 2026)

```text
énoncé : toute règle nommée du corpus doit déclarer un incident daté, une
         violation observable et un mécanisme de détection ; à défaut elle est
         une formulation exploratoire sans autorité normative.
incident daté : 15 août 2026 — constat que P27 et P28 sont énoncées dans les
                notes méthodologiques sans acte d'instauration daté ni entrée
                dans le registre des arbitrages, et que l'index les déclare
                « appliquées » sans élément vérifiable (écart dit/fait non
                enregistré).
violation observable : une règle nommée (P2x, P3x…) mentionnée dans le corpus
                       actif sans occurrence datée ni référence d'issue/registre,
                       ou une section de ce registre privée d'un des trois champs.
mécanisme de détection : audit_ecarts_regles.py::check_rules_instantiated et
                         ::check_rule_mechanism_declared (auto-appliquée).
```

---

## Règles de verdict (déclaration du mécanisme d'épreuve seulement)

### P27 — résultat, soutien probatoire et verdict

```text
énoncé : distinguer résultat quantitatif, mode de soutien probatoire et verdict
         de constance ; une borne sur la valeur ne produit pas une valeur
         positive ; une non-détection n'est probante que sous conditions.
incident daté : non établi dans une issue ou un registre daté — voir l'écart
                consigné dans Journal_ecarts_gouvernance.md (P27 déclarée sans
                acte d'instauration séparé des notes v1.7/v1.8).
violation observable : un verdict de constance qui convertit une borne ou une
                       non-détection en valeur positive sans déclarer famille
                       de variations, sensibilité, modèle de conversion,
                       systématiques, domaine et tolérance.
mécanisme de détection : NON automatisable — règle de verdict éprouvée par cas
                         adversariaux (note méthodologique v1.7 §5) et par la
                         relecture humaine des synthèses de cycle, non par
                         audit d'écart. Ce registre n'affirme pas son
                         application ; il rappelle que son test est d'une
                         autre famille que celle de P28/P29.
```

---

## Registre vide au départ — remplissage par incidents

Conformément à P28, ce registre ne se remplit que par incidents réels et datés.
Toute nouvelle règle nommée y est inscrite *avant* de faire autorité, avec ses
trois champs. Une règle du corpus actif qui n'y figure pas encore est, par
défaut, une formulation exploratoire jusqu'à inscription.

Le journal des écarts effectivement constatés est tenu séparément :
[Journal des écarts de gouvernance](Journal_ecarts_gouvernance.md).
