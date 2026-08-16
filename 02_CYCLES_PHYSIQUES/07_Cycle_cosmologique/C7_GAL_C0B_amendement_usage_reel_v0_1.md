# C7-GAL-C0-B — amendement expérimental issu du test d'usage réel

Version : `v0.2-experimentale`
Date : `2026-08-16`
Objet parent : `C7_GAL_C0B_prespecification_G2_v0_2.md`
PR témoin : `#109`
Statut : `OVERLAY_EXPERIMENTAL_NON_CANONIQUE`

## 1. Fonction de cet amendement

Ce document ne remplace pas la v0.2 et ne modifie pas sa provenance. Il teste trois corrections apparues lors du premier test d'usage réel du protocole human-first / machine-verifiable :

1. distinguer la cible numérique FIRE effectivement reconstruite d'un continuum physique idéalisé ;
2. conserver explicitement la dépendance azimutale avant toute réduction en profil radial ;
3. séparer ce qui doit être pré-enregistré scientifiquement de ce qui peut être qualifié techniquement hors résultat cible.

L'amendement n'a d'autorité que dans le banc expérimental. S'il n'apporte pas un gain discriminant net, il doit être retiré plutôt qu'intégré.

## 2. Cible de reconstruction : ne pas appeler toute différence une erreur

La première cible de `G2-FIELD` est le champ gravitationnel instantané défini par la réalisation FIRE publique effectivement disponible, avec ses masses discrètes, son kernel, ses softenings et les conditions de bord qualifiées :

```text
snapshot discret + modèle de masse/softening FIRE qualifié
-> champ vectoriel numérique cible
```

Par rapport à cette cible, une approximation de solveur, une mauvaise conversion d'unités, une condition de bord incorrecte ou une fermeture numérique défectueuse ne reçoivent pas toutes le même statut.

Certaines situations rendent la reconstruction invalide ou non qualifiée : mauvaise provenance, convention d'unités incohérente, couverture de sources insuffisante pour la cible annoncée, conditions de bord non établies lorsqu'elles sont constitutives de la cible, échec d'un oracle requis ou fermeture de composantes incompatible avec l'implémentation déclarée. Elles doivent produire un arrêt, une suspension ou une limitation explicite, pas une barre d'erreur qui rendrait le résultat artificiellement acceptable.

D'autres écarts peuvent être réellement bornés après qualification de la cible : erreur résiduelle du solveur, interpolation, discrétisation d'une grille d'évaluation ou sensibilité numérique à un raffinement. Ceux-là peuvent être traités comme erreurs ou incertitudes numériques lorsqu'un oracle ou une convergence indépendante permet de les mesurer.

Enfin, la granularité particulaire et le softening ne sont pas automatiquement des erreurs de reconstruction de la cible FIRE discrète : ils participent à la définition du système numérique simulé. Ils deviennent des effets de résolution ou de modélisation lorsque la question change et compare cette réalisation à un continuum physique idéalisé ou à une limite non adoucie.

La chaîne doit donc rester explicite :

```text
A. réalisation FIRE discrète et adoucie
   -> établir que la cible est reconstructible
   -> reconstruire fidèlement G2-FIELD

B. reconstruction qualifiée
   -> borner les erreurs numériques résiduelles

C. réalisation FIRE reconstruite
   -> comparer, si scientifiquement pertinent,
      à une représentation continue/non adoucie
```

Les niveaux S/D/K de la v0.2 restent utiles comme tests, mais leur interprétation dépend de la cible :

- `S` qualifie directement l'accès numérique au même objet discret ;
- `D` et `K` qualifient surtout le passage de la réalisation simulée vers une représentation continue ou une limite de résolution ;
- ils ne doivent pas être additionnés sous l'étiquette générale « erreur de G2 » sans nommer l'objet auquel l'écart est rapporté.

### 2.1 Quatre fonctions à ne pas confondre

Le futur successeur doit distinguer les fonctions suivantes sans nécessairement en faire quatre nouvelles catégories permanentes :

```text
CONDITIONS_DE_VALIDITE
= identité/provenance + conventions cohérentes + couverture requise
  + conditions de bord constitutives + oracles bloquants + fermeture

ERREURS_NUMERIQUES_BORNEES
= résidu solveur + interpolation + convergence/raffinement qualifiables

CHOIX_DE_REPERE_ET_DE_REDUCTION
= centre + vitesse système + orientation + réduction azimutale/radiale
  + projection éventuelle

REPRESENTATION_ET_RESOLUTION
= réalisation discrète + kernel/softening
  relativement à une autre cible physique ou continue

FIELD_VERS_EOM
= différence champ à point-test / équation du mouvement adaptative
```

La première ligne n'est pas un « budget d'incertitude » : lorsqu'une condition nécessaire échoue, elle change le statut de validité du produit. Les autres lignes peuvent produire sensibilités, enveloppes ou écarts uniquement lorsque leur sens est défini par rapport à une cible nommée.

## 3. Ne pas imposer l'axisymétrie avant de l'avoir testée

Le produit primaire ne doit pas être réduit d'emblée à :

```text
g_R_FIELD(R,z), g_z_FIELD(R,z)
```

La sortie primaire doit conserver le champ vectoriel local avec sa dépendance azimutale, par exemple :

```text
g_FIELD(x,y,z)
```

ou, après fixation du repère :

```text
g_R_FIELD(R,phi,z)
g_phi_FIELD(R,phi,z)
g_z_FIELD(R,phi,z)
```

La réduction en un profil `g_R_FIELD(R,z)` devient une opération secondaire dont l'opérateur doit être déclaré : moyenne, médiane, secteur, harmonique ou autre réduction justifiée. Elle ne doit pas être implicite.

Avant toute transformation en `v_grav(R)`, le dossier doit au minimum conserver :

- `g_phi` ;
- la dispersion ou structure azimutale de `g_R` et `g_z` ;
- un diagnostic pré-enregistré de non-axisymétrie adapté à la question scientifique ;
- la trace de l'opérateur ayant produit le profil radial réduit.

Aucun ordre harmonique universel ni seuil d'axisymétrie n'est imposé ici. Le critère doit être choisi avant le résidu scientifique cible et seulement à la granularité nécessaire pour changer la décision suivante.

La transformation :

```text
v_grav(R) = sqrt(R |g_R(R,0)|)
```

n'est autorisée comme produit interprétable que si la réduction radiale et l'approximation de support circulaire ont été qualifiées pour le régime considéré. Sinon, le champ vectoriel et son hétérogénéité azimutale restent le résultat pertinent.

Cette correction est directement motivée par la question parent de C7-GAL-C : l'enquête vise précisément à tester les mouvements non circulaires, les termes hors équilibre et les situations où une courbe de rotation réduite cesse d'être un accès fiable au support gravitationnel.

## 4. Pré-enregistrement scientifique versus qualification technique

Le principe anti-post-hoc est conservé, mais il ne doit pas transformer chaque paramètre numérique en décision scientifique humaine distincte.

### 4.1 Doit être gelé avant exposition au résidu cible

Tout choix capable de changer la signification ou le verdict scientifique doit être pré-enregistré ou placé dans une sensibilité symétrique définie à l'avance, notamment :

- objet scientifique comparé ;
- échantillon et domaine analysé ;
- centre, vitesse système et orientation ;
- opérateur de réduction azimutale/radiale ;
- sélection du traceur ;
- conditions de bord retenues comme physiquement pertinentes ;
- niveau de fidélité FIELD/EOM requis ;
- masques affectant la région scientifique ;
- métrique et seuil qui changent un verdict ;
- règle de comparaison O1/G2.

### 4.2 Peut être qualifié techniquement hors cible

Un paramètre d'implémentation peut être choisi ou raffiné sans ratification humaine valeur par valeur si :

1. la propriété qu'il doit protéger est déjà déclarée ;
2. un oracle, un test synthétique ou une convergence indépendante du résidu cible permet de le qualifier ;
3. la tolérance est fixée avant lecture du résultat cible ;
4. les échecs et variantes pertinentes sont conservés ;
5. le réglage ne change ni la cible scientifique ni l'opérateur de comparaison.

Exemples typiques : angle d'ouverture d'un arbre, résolution PM, ordre d'expansion, précision arithmétique, nombre de points d'un test synthétique, stratégie de raffinement ou détails équivalemment qualifiés d'une implémentation.

La valeur/version de `G` suit la même logique : une convention explicite et cohérente avec le système d'unités doit être enregistrée ; une décision scientifique supplémentaire n'est nécessaire que si l'ambiguïté entre conventions devient non négligeable devant le budget pertinent.

### 4.3 Principe de contrôle

Pour chaque garde-fou candidat :

> Si cette contrainte disparaît, quelle décision scientifique devient effectivement moins sûre ?

Si aucune décision, aucun rang probatoire, aucune cible, aucune condition de validité ou aucune reproductibilité pertinente ne change, la contrainte ne doit pas être promue par précaution abstraite.

## 5. Effet attendu sur la v0.2

Si cet amendement survit au test, une version successeur devra intégrer les changements sans conserver cet overlay comme couche durable :

- §8.1 : champ primaire vectoriel avec dépendance azimutale conservée ;
- §8.3-8.4 : réduction vers `v_grav` explicitement conditionnelle ;
- §§10-12 : S/D/K conservés, mais rapportés à une cible nommée ;
- §11 : remplacer le budget unique par la distinction validité / erreur numérique / repère-réduction / représentation-résolution / FIELD-EOM ;
- §§13-14 : retirer les ratifications humaines qui peuvent être remplacées par une qualification technique indépendante ;
- §16 : classer les dettes selon leur effet réel sur la prochaine décision scientifique.

Le successeur ne devra pas être plus long par simple accumulation. La correction doit idéalement réduire le nombre de statuts et de décisions préalables tout en augmentant la lisibilité de la chaîne scientifique.

## 6. Falsificateurs de l'amendement

L'amendement doit être rejeté ou révisé s'il produit l'un des effets suivants :

1. il permet de régler un choix scientifique après lecture du résidu cible ;
2. il rend la reconstruction moins reproductible ;
3. il conserve la dépendance azimutale sans que cela puisse jamais changer une décision dans C7-GAL-C ;
4. il déplace simplement les mêmes dettes sous de nouveaux noms ;
5. il transforme des échecs de validité en incertitudes absorbables ;
6. il augmente durablement la complexité documentaire sans supprimer une ambiguïté, une fausse obligation ou une possibilité de glissement inférentiel.

## 7. Verdict expérimental attendu

```text
AMENDEMENT = A_TESTER
AUTORITE_CANONIQUE = AUCUNE
PR_98 = INCHANGEE
PR_109 = TEMOIN_INCHANGE
MERGE_MAIN = NON
```

Le test porte sur la question suivante :

> Cette correction rend-elle la future décision scientifique plus discriminante et plus lisible, sans fermer prématurément l'exploration ni rouvrir la porte au réglage post-hoc ?
