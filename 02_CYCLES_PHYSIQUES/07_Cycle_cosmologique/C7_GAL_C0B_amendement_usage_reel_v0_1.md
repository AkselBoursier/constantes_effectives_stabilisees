# C7-GAL-C0-B — amendement expérimental issu du test d'usage réel

Version : `v0.1-experimentale`
Date : `2026-08-16`
Objet parent : `C7_GAL_C0B_prespecification_G2_v0_2.md`
PR témoin : `#109`
Statut : `OVERLAY_EXPERIMENTAL_NON_CANONIQUE`

## 1. Fonction de cet amendement

Ce document ne remplace pas la v0.2 et ne modifie pas sa provenance. Il teste trois corrections apparues lors du premier test d'usage réel du protocole human-first / machine-verifiable :

1. distinguer la cible numérique FIRE effectivement reconstruite d'un continuum physique idéalise ;
2. conserver explicitement la dépendance azimutale avant toute reduction en profil radial ;
3. séparer ce qui doit être pre-enregistre scientifiquement de ce qui peut être qualifie techniquement hors resultat cible.

L'amendement n'a d'autorite que dans le banc experimental. S'il n'apporte pas un gain discriminant net, il doit etre retire plutot qu'integre.

## 2. Cible de reconstruction : ne pas appeler toute difference une erreur

La premiere cible de `G2-FIELD` est le champ gravitationnel instantane defini par la realisation FIRE publique effectivement disponible, avec ses masses discretes, son kernel, ses softenings et les conditions de bord qualifiees :

```text
snapshot discret + modele de masse/softening FIRE qualifie
-> champ vectoriel numerique cible
```

Par rapport a cette cible, une approximation de solveur, une mauvaise conversion d'unites, une condition de bord incorrecte ou une fermeture numerique defectueuse sont des erreurs d'acces/reconstruction.

En revanche, la granularite particulaire et le softening ne sont pas automatiquement des erreurs de reconstruction de cette cible : ils participent a la definition du systeme numerique simule. Ils deviennent des effets de resolution ou de modelisation seulement lorsque la question change et compare cette realisation a un continuum physique idealise ou a une limite non adoucie.

La chaine doit donc rester explicite :

```text
A. realisation FIRE discrete et adoucie
   -> reconstruire fidelement G2-FIELD

B. realisation FIRE reconstruite
   -> comparer, si scientifiquement pertinent, a une representation continue/non adoucie
```

Les niveaux S/D/K de la v0.2 restent utiles comme tests, mais leur interpretation depend de la cible :

- `S` qualifie directement l'acces numerique au meme objet discret ;
- `D` et `K` qualifient surtout le passage de la realisation simulee vers une representation continue ou une limite de resolution ;
- ils ne doivent pas etre additionnes sous l'etiquette generale « erreur de G2 » sans nommer l'objet auquel l'erreur est rapportee.

### Consequence pour le budget

Le budget futur doit distinguer au minimum :

```text
RECONSTRUCTION_DE_LA_CIBLE
= unites + solveur + bords + fermeture + fidelite de l'implementation

CHOIX_DE_REPERE_ET_DE_REDUCTION
= centre + vitesse systeme + orientation + projection/reduction

REPRESENTATION_ET_RESOLUTION
= discretisation + kernel/softening + passage eventuel au continuum

FIELD_VERS_EOM
= difference champ a point-test / equation du mouvement adaptative
```

Cette partition est fonctionnelle, pas une nouvelle taxonomie canonique.

## 3. Ne pas imposer l'axisymetrie avant de l'avoir testee

Le produit primaire ne doit pas etre reduit d'emblee a :

```text
g_R_FIELD(R,z), g_z_FIELD(R,z)
```

La sortie primaire doit conserver le champ vectoriel local avec sa dependance azimutale, par exemple :

```text
g_FIELD(x,y,z)
```

ou, apres fixation du repere :

```text
g_R_FIELD(R,phi,z)
g_phi_FIELD(R,phi,z)
g_z_FIELD(R,phi,z)
```

La reduction en un profil `g_R_FIELD(R,z)` devient une operation secondaire dont l'operateur doit etre declare : moyenne, mediane, secteur, harmonique ou autre reduction justifiee. Elle ne doit pas etre implicite.

Avant toute transformation en `v_grav(R)`, le dossier doit au minimum conserver :

- `g_phi` ;
- la dispersion ou structure azimutale de `g_R` et `g_z` ;
- un diagnostic preenregistre de non-axisymetrie adapte a la question scientifique ;
- la trace de l'operateur ayant produit le profil radial reduit.

Aucun ordre harmonique universel ni seuil d'axisymetrie n'est impose ici. Le critere doit etre choisi avant le residu scientifique cible et seulement a la granularite necessaire pour changer la decision suivante.

La transformation :

```text
v_grav(R) = sqrt(R |g_R(R,0)|)
```

n'est autorisee comme produit interpretable que si la reduction radiale et l'approximation de support circulaire ont ete qualifiees pour le regime considere. Sinon, le champ vectoriel et son heterogeneite azimutale restent le resultat pertinent.

Cette correction est directement motivee par la question parent de C7-GAL-C : l'enquete vise precisement a tester les mouvements non circulaires, les termes hors equilibre et les situations ou une courbe de rotation reduite cesse d'etre un acces fiable au support gravitationnel.

## 4. Pre-enregistrement scientifique versus qualification technique

Le principe anti-post-hoc est conserve, mais il ne doit pas transformer chaque parametre numerique en decision scientifique humaine distincte.

### 4.1 Doit etre gele avant exposition au residu cible

Tout choix capable de changer la signification ou le verdict scientifique doit etre preenregistre ou place dans une sensibilite symetrique definie a l'avance, notamment :

- objet scientifique compare ;
- echantillon et domaine analyse ;
- centre, vitesse systeme et orientation ;
- operateur de reduction azimutale/radiale ;
- selection du traceur ;
- conditions de bord retenues comme physiquement pertinentes ;
- niveau de fidelite FIELD/EOM requis ;
- masques affectant la region scientifique ;
- metrique et seuil qui changent un verdict ;
- regle de comparaison O1/G2.

### 4.2 Peut etre qualifie techniquement hors cible

Un parametre d'implementation peut etre choisi ou raffine sans ratification humaine valeur par valeur si :

1. la propriete qu'il doit proteger est deja declaree ;
2. un oracle, un test synthetique ou une convergence independante du residu cible permet de le qualifier ;
3. la tolerance est fixee avant lecture du resultat cible ;
4. les echecs et variantes pertinentes sont conserves ;
5. le reglage ne change ni la cible scientifique ni l'operateur de comparaison.

Exemples typiques : angle d'ouverture d'un arbre, resolution PM, ordre d'expansion, precision arithmetique, nombre de points d'un test synthetique, strategie de raffinement ou details equivalentement qualifies d'une implementation.

La valeur/version de `G` suit la meme logique : une convention explicite et coherente avec le systeme d'unites doit etre enregistree ; une decision scientifique supplementaire n'est necessaire que si l'ambiguite entre conventions devient non negligeable devant le budget pertinent.

### 4.3 Principe de controle

Pour chaque garde-fou candidate :

> Si cette contrainte disparait, quelle decision scientifique devient effectivement moins sure ?

Si aucune decision, aucun rang probatoire, aucune cible ou aucune reproductibilite pertinente ne change, la contrainte ne doit pas etre promue par precaution abstraite.

## 5. Effet attendu sur la v0.2

Si cet amendement survit au test, une version successeur devra integrer les changements sans conserver cet overlay comme couche durable :

- §8.1 : champ primaire vectoriel avec dependance azimutale conservee ;
- §8.3-8.4 : reduction vers `v_grav` explicitement conditionnelle ;
- §§10-12 : S/D/K conserves, mais rapportes a une cible nommee ;
- §11 : budget separe entre reconstruction, repere/reduction, representation-resolution et FIELD/EOM ;
- §§13-14 : retrait des ratifications humaines qui peuvent etre remplacees par une qualification technique independante ;
- §16 : dettes classees selon leur effet reel sur la prochaine decision scientifique.

Le successeur ne devra pas etre plus long par simple accumulation. La correction doit idealement reduire le nombre de statuts et de decisions prealables tout en augmentant la lisibilite de la chaine scientifique.

## 6. Falsificateurs de l'amendement

L'amendement doit etre rejete ou revise s'il produit l'un des effets suivants :

1. il permet de regler un choix scientifique apres lecture du residu cible ;
2. il rend la reconstruction moins reproductible ;
3. il conserve la dependance azimutale sans que cela puisse jamais changer une decision dans C7-GAL-C ;
4. il deplace simplement les memes dettes sous de nouveaux noms ;
5. il augmente durablement la complexite documentaire sans supprimer une ambiguite, une fausse obligation ou une possibilite de glissement inferentiel.

## 7. Verdict experimental attendu

```text
AMENDEMENT = A_TESTER
AUTORITE_CANONIQUE = AUCUNE
PR_98 = INCHANGEE
PR_109 = TEMOIN_INCHANGE
MERGE_MAIN = NON
```

Le test porte sur la question suivante :

> Cette correction rend-elle la future decision scientifique plus discriminante et plus lisible, sans fermer prematurement l'exploration ni rouvrir la porte au reglage post-hoc ?
