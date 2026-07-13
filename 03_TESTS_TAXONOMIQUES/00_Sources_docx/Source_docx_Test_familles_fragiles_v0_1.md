# Source DOCX - Test_familles_fragiles_v0_1

## Statut

```text
lot: 2 - tests taxonomiques
source physique: Test des familles fragiles.docx
source physique path: 03_TESTS_TAXONOMIQUES/00_Sources_docx/Test des familles fragiles.docx
sha256_source: a3a48a2e2c30f6a00516cf34db53a8a6a8780897997459462d654a3334552256
statut: extraction textuelle de travail
document actif concerne: Methode v1.3 ; reecriture positive
controle attendu: Extraction + controle des termes evacues
```

## Limite

```text
Cette extraction ne remplace pas le DOCX source.
Elle rend la matiere lisible en Markdown pour comparaison et integration.
La mise en page Word n'est pas reconstruite.
```

## Avertissement d'extraction

> Ce fichier contient des placeholders `[  ]` (et variants comme `[ X= ]`) correspondant
> a des passages incomplets dans le DOCX source : formules non rendues, tableaux mal convertis,
> elements graphiques ou equations complexes.
> Ne pas interpreter ces placeholders comme du contenu valide.
> Verifier le DOCX source avant toute reprise scientifique.
> Convention : [CONVENTION_PLACEHOLDERS.md](../../CONVENTION_PLACEHOLDERS.md)

## Extraction

### Test des familles fragiles v0.1

#### Relation, Fond, Seuil

#### 1. Fonction du test

Trois familles restent fragiles dans la carte méthodologique :

[  ]

[  ]

[  ]

Elles sont utiles, mais leur statut n’est pas encore aussi robuste que celui de :

[  ]

[  ]

[  ]

[  ]

[  ]

Le test consiste à vérifier si ces familles classent réellement plusieurs cas hétérogènes, ou si elles ne font que nommer une difficulté locale.

Une famille est conservée si elle remplit trois conditions :

[  ]

[  ]

[  ]

Une famille doit être rétrogradée si elle fonctionne plutôt comme un sous-type, une propriété transversale ou une architecture.

#### 2. Famille Relation : diagnostic

La famille Relation est la plus nécessaire et la plus dangereuse.

Elle est nécessaire parce que de nombreuses constantes ne sont pas des valeurs isolées. Elles mettent en rapport des grandeurs, des niveaux, des régimes ou des descriptions.

Exemples :

[  ]

[ R=N_Ak_B ]

[ m^2 ]

[ m_f= ]

Mais elle est dangereuse parce que presque toute constante pourrait être décrite comme relationnelle. Une famille trop large cesse de classer.

Le diagnostic est donc :

Relation doit être conservée, mais comme famille faible, toujours qualifiée par un sous-type.

Elle ne doit jamais être utilisée seule comme dernier mot du classement.

#### 3. Sous-types de Relation

La famille Relation devient robuste si elle est divisée en sous-types précis.

##### 3.1 Relation stratifiée

Une relation stratifiée relie des grandeurs issues de régimes physiques distincts.

Exemple :

[  ]

Le proton dépend principalement de la dynamique QCD non perturbative, tandis que l’électron dépend du régime électrofaible brisé via son Yukawa. Le rapport :

[  ]

condense donc plusieurs couches physiques.

Fonction :

[  ]

##### 3.2 Relation compositionnelle

Une relation compositionnelle est une grandeur obtenue par combinaison d’autres constantes.

Exemple :

[ R=N_Ak_B ]

La constante molaire des gaz n’est pas une constante définissante primaire. Elle devient exacte par composition de deux constantes définissantes.

Fonction :

[  ]

##### 3.3 Relation spectrale

Une relation spectrale exprime un écart ou un rapport entre valeurs propres d’un spectre.

Exemples :

[ m^2_{21} ]

[ m^2_{3} ]

Ces grandeurs ne donnent pas les masses absolues. Elles stabilisent des écarts entre états de masse.

Fonction :

[  ]

##### 3.4 Relation constitutive de régime

Une relation constitutive de régime exprime comment une grandeur stabilisée résulte de la combinaison d’une échelle et d’un couplage dans un régime donné.

Exemple :

[ m_f= ]

La masse fermionique est une valeur stabilisée du régime électrofaible brisé, mais elle n’est pas primitive : elle résulte de la relation entre (v) et (y_f).

Fonction :

[  ]

#### 4. Verdict sur Relation

La famille Relation est conservée, mais sous contrainte.

Elle n’est pas une famille forte au même sens que Couplage ou Orientation. Elle est une famille transversale, utile pour classer les constantes dont la fonction première est de mettre en rapport.

Nouvelle règle :

Relation doit toujours être qualifiée.

Formes acceptables :

[  ]

[  ]

[  ]

[  ]

Forme insuffisante :

[  ]

seule.

Conclusion :

[  =  ]

#### 5. Famille Seuil : diagnostic

La famille Seuil est apparue avec la masse absolue des neutrinos.

Elle désigne une grandeur qui fixe ou borne l’ancrage absolu d’un spectre, alors que les écarts internes du spectre sont déjà connus ou partiellement connus.

Cas principal :

[ m_,m_,m_{} ]

Ces trois grandeurs sont des projections différentes de la masse absolue des neutrinos.

Le problème est que Seuil risque de se confondre avec Échelle.

Une échelle structure un régime :

[ v ]

[ _{} ]

[ M_{} ]

Un seuil, lui, fixe une limite d’entrée, de borne ou d’ancrage dans un spectre ou un domaine.

La distinction est donc :

[  =  ]

[  =  ]

#### 6. Sous-types possibles de Seuil

La famille Seuil devient plus robuste si elle ne se limite pas à la masse absolue des neutrinos.

##### 6.1 Seuil spectral

C’est le cas déjà traité.

Exemple :

[ m_{} ]

ou ses projections :

[ m_,m_,m_{} ]

Fonction :

[  ]

##### 6.2 Seuil de validité effective

Une théorie effective possède souvent une limite au-delà de laquelle elle cesse d’être suffisante.

Exemples possibles :

[ M_W ]

pour la théorie de Fermi,

[ M_{} ]

pour la relativité générale comme théorie effective basse énergie,

[ _{} ]

comme seuil d’entrée dans le régime non perturbatif.

Mais ces cas chevauchent fortement la famille Échelle. Il faut donc être prudent.

La bonne formulation n’est pas :

[ M_W  ]

mais :

[ M_W  ]

Le seuil est ici une fonction secondaire, non le classement principal.

##### 6.3 Seuil observationnel

Certaines grandeurs sont connues par limite supérieure ou inférieure.

Exemples :

[ m_<  ]

[ m_{} <  ]

Dans ce cas, le seuil est moins une structure physique qu’un régime d’accès expérimental.

Il faut donc distinguer :

[  ]

et :

[  ]

#### 7. Verdict sur Seuil

La famille Seuil est conservée, mais avec statut provisoire.

Elle est utile pour la masse absolue des neutrinos, car celle-ci n’est pas simplement une échelle. Elle ancre un spectre dont les écarts sont déjà mesurés.

Mais la famille Seuil ne doit pas absorber toutes les échelles de transition.

Nouvelle règle :

Seuil est conservé lorsque la fonction principale est de fixer, borner ou ancrer une limite ; il devient sous-type secondaire lorsque la grandeur structure d’abord un régime comme échelle.

Conclusion :

[  =  ]

#### 8. Famille Fond : diagnostic

La famille Fond est la plus fragile.

Elle est actuellement portée presque entièrement par :

[  ]

La constante cosmologique joue bien un rôle particulier. Elle ne se laisse pas réduire facilement à Couplage, Échelle, Relation, Orientation ou Convention.

Elle intervient comme terme uniforme dans les équations gravitationnelles et comme composante de la dynamique cosmologique globale.

Mais une famille portée par un seul cas reste suspecte.

Le danger est double.

Premier danger :

[  ]

pourrait n’être qu’un nom donné à la singularité de ().

Deuxième danger :

[  ]

pourrait devenir une famille trop large absorbant tous les paramètres cosmologiques.

Il faut donc la tester sévèrement.

#### 9. Ce qui distingue Fond

Une constante de fond ne fixe pas seulement une échelle locale. Elle participe à la structure globale dans laquelle les autres processus prennent place.

Elle agit sur :

[  ]

[  ]

[  ]

[  ]

Dans le cas de (), la grandeur peut être lue comme :

[  ]

[  ]

[  ]

[  ]

Cette multiplicité est précisément ce qui rend la famille Fond intéressante, mais fragile.

#### 10. Candidats pour tester Fond

Plusieurs grandeurs pourraient être candidates, mais elles ne sont pas toutes du même type.

##### 10.1 (H_0)

[ H_0 ]

est le taux d’expansion actuel. Il structure la cosmologie observationnelle, mais ce n’est pas une constante fondamentale au même sens que (). C’est un paramètre d’état cosmologique actuel.

Il pourrait tester la famille Fond, mais il risque de déplacer l’enquête vers les paramètres de modèle.

##### 10.2 (m), ()

Ces grandeurs sont des paramètres de densité normalisés. Elles sont dépendantes du modèle cosmologique et du choix d’époque.

Elles appartiennent davantage à une architecture cosmologique qu’à une famille de constantes.

##### 10.3 (A_s), (n_s)

Ces paramètres décrivent le spectre primordial des perturbations. Ils structurent les conditions initiales cosmologiques, mais leur statut est encore différent de ().

Ils testeraient une architecture cosmologique, pas seulement la famille Fond.

##### 10.4 (w)

Le paramètre d’équation d’état de l’énergie noire :

[ w= ]

peut être constant ou dynamique selon les modèles. Il est un bon test conceptuel, car il oblige à distinguer :

[ w=-1 ]

et :

[  ]

Mais (w) est davantage un paramètre phénoménologique qu’une constante fondamentale.

#### 11. Verdict sur Fond

La famille Fond est conservée, mais comme famille monoplace provisoire.

Elle reste justifiée par la singularité fonctionnelle de (), qui structure la dynamique cosmologique globale.

Mais elle ne doit pas encore être étendue à tous les paramètres cosmologiques.

Nouvelle règle :

Fond est conservé pour les grandeurs qui structurent une dynamique globale de fond, mais l’architecture cosmologique doit être testée séparément avant d’élargir la famille.

Conclusion :

[  =  ]

#### 12. Résultat comparatif

| Famille fragile | Verdict | Statut |
|---|---|---|
| Relation | Conservée sous contrainte | Famille transversale qualifiée |
| Seuil | Conservée provisoirement | Famille à tester par nouveaux cas |
| Fond | Conservée provisoirement | Famille monoplace liée à () |

Le résultat est asymétrique.

[  ]

est trop large, mais nécessaire.

[  ]

est conceptuellement utile, mais encore peu testé.

[  ]

est fonctionnellement distinct, mais encore presque monoplace.

#### 13. Carte révisée après test

La carte ne doit pas supprimer ces familles, mais les marquer avec des statuts différents.

| Famille | Statut révisé | Règle d’usage |
|---|---|---|
| Couplage | Robuste | Usage direct possible |
| Échelle | Robuste | Usage direct possible |
| Raccordement | Robuste | Usage direct possible |
| Orientation | Robuste | Usage direct possible |
| Convention | Robuste | Usage direct possible |
| Relation | Transversale faible | Toujours qualifier |
| Seuil | Provisoire | Utiliser si fonction d’ancrage ou de borne |
| Fond | Provisoire monoplace | Ne pas généraliser sans cycle cosmologique |

#### 14. Conséquence méthodologique

La carte doit maintenant distinguer trois statuts de familles.

##### 14.1 Familles robustes

Ces familles peuvent être utilisées directement.

[  ]

[  ]

[  ]

[  ]

[  ]

##### 14.2 Famille transversale faible

Cette famille est utile, mais demande qualification.

[  ]

##### 14.3 Familles provisoires

Ces familles sont conservées, mais demandent de nouveaux tests.

[  ]

[  ]

Cette distinction évite de donner le même degré de maturité à toutes les familles.

#### 15. Prochaine étape logique

Le test appelle deux suites possibles.

Première suite :

[  ]

par un cas non neutrino, afin de voir si la famille peut accueillir autre chose que l’ancrage du spectre neutrino.

Deuxième suite :

[  ]

par une architecture cosmologique prudente, sans confondre constantes, paramètres de modèle et observables reconstruites.

Le choix dépend du risque que l’on veut attaquer en premier.

Le test de Seuil serait plus contrôlé.

Le test de Fond serait plus ambitieux, mais plus dangereux, car il ouvre directement le domaine cosmologique.

#### 16. Recommandation

La suite la plus sûre est de tester d’abord :

[  ]

parce que cette famille peut être éprouvée sans ouvrir toute la cosmologie.

Un bon candidat serait :

[ M_W ]

lu non comme simple échelle électrofaible, mais comme seuil de validité de la théorie de Fermi.

Autre candidat possible :

[ _{} ]

lu non seulement comme échelle dynamique, mais comme seuil de passage entre régime perturbatif et non perturbatif.

Mais ces deux cas sont précisément intéressants parce qu’ils risquent de montrer que “seuil” n’est pas une famille autonome : peut-être n’est-ce qu’une fonction secondaire de certaines échelles.

Le test doit donc être formulé ainsi :

Seuil est-il une famille autonome, ou seulement une fonction d’usage de certaines échelles ?

#### 17. Critère de réussite du prochain test

Le prochain test sera réussi si l’on peut décider clairement entre deux options.

Option A :

[  ]

reste une famille autonome, parce qu’il existe des grandeurs dont la fonction principale est l’ancrage ou la borne.

Option B :

[  ]

est rétrogradé en sous-type de la famille Échelle ou Relation, parce qu’il ne fonctionne jamais seul.

Dans les deux cas, le test sera utile.

Le mauvais résultat serait de conserver Seuil par habitude sans clarification.

#### 18. Formule de clôture

Les familles fragiles ne doivent pas être éliminées trop vite. Elles indiquent souvent un vrai problème.

Mais elles ne doivent pas être protégées non plus.

La règle devient :

une famille fragile doit être traitée comme une hypothèse de classement, non comme une case acquise.
