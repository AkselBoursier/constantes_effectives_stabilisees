# Journal des écarts de gouvernance

## 0. Statut et fonction

```text
statut : journal de données, ouvert le 15 août 2026 ;
fonction : consigner les écarts constatés entre règles déclarées et règles
           suivies, comme données datées — non comme fautes à censurer ;
ne vaut pas : sanction, réécriture rétroactive des états antérieurs, ni preuve
              que les écarts non listés n'existent pas ;
distinct de : Registre_court_arbitrages (décisions) — ici ce sont des écarts.
```

Principe : « état normatif ≠ état documentaire appliqué », étendu à
« **règle déclarée ≠ règle suivie** ». Un écart consigné n'annule pas la règle ;
il la transforme de résolution en règle instrumentée en la rendant observable.

Chaque entrée nomme : la règle, l'écart constaté, la date de constat, la preuve
interne, et la réparation éventuelle.

---

## Écarts consignés

### 15 août 2026 — P27 et P28 déclarées « appliquées » sans acte d'instauration

```text
règle : P27, P28 (gouvernement et verdict) ;
écart : l'index raisonné v2.3 §2 déclare « P27 : close, appliquée et amendée »
        et « P28 : close, appliquée et amendée », mais aucune des deux règles
        n'a de document de décision daté et séparé, et aucune n'a d'entrée dans
        le Registre_court_arbitrages (seuil d'inscription : « règle
        méthodologique validée ») — contrairement à P24–P26, datées du
        26 juillet 2026 dans Ajustements_directeurs_D1_D5 ;
preuve : P27/P28 n'apparaissent que dans les notes méthodologiques v1.7/v1.8 ;
         le registre des arbitrages (créé le 17 juillet) ne les mentionne pas ;
constat par : lecture croisée des dates d'instauration et des contenus, à
              l'occasion de la question d'export d'un template ;
réparation : création de audit/regles_actives.md (méta-règle) et du présent
             journal ; P28 reçoit désormais un mécanisme de détection.
```

### 15 août 2026 — Accumulation de cartes consolidées sans remplacement (P28)

```text
règle : P28 (ablation documentaire) ;
écart : 05_CARTES_ET_SYNTHESES/Carte_consolidee_v0_9.md, v1_0, v1_1,
        v1_2_refonte, v1_3_post_cercle2 coexistent ; bien que certaines versions
        nomment leur prédécesseur (« conserve la v… », « après v1_2 »),
        l'accumulation de cinq états sans retrait illustre le symptôme que P28
        vise ; aucun mécanisme ne signalait cette accumulation avant ce jour ;
preuve : cinq fichiers Carte_consolidee_* présents simultanément ;
réparation : check_versioned_maps_replacement dans audit_ecarts_regles.py
             signale désormais toute version sans déclaration de remplacement.
```

### 15 août 2026 — Provenance non vérifiable par Git (shallow)

```text
règle : règle temporelle et normative (dater, ne pas réécrire) ;
écart : la chaîne de provenance repose sur des déclarations datées internes et
        des blocs sha256, car l'historique Git cloné est peu profond ; les dates
        d'instauration réelles des règles ne sont pas vérifiables par `git log` ;
preuve : `git rev-list --count HEAD` = 3 ; premier commit visible = 4 août 2026,
         postérieur à de nombreuses décisions de juillet ;
réparation : hors périmètre de ce journal (relève de l'hébergement du dépôt) ;
             consigné comme limite du mécanisme de vérification.
```

---

## Seuil d'inscription

Un écart est consigné lorsqu'il est constaté sur un fait interne vérifiable et
qu'il concerne une règle nommée. Les écarts potentiels non confirmés, les
différences d'interprétation et les violations des règles de verdict (P27) — qui
relèvent d'une épreuve par cas, non d'un audit — ne sont pas inscrits ici.
