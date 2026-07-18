# Réservoir conceptuel — Session T_MQ-S2 du 20 mai 2026

## Note de cadrage

Ce document consigne les développements conceptuels issus de la session du 20 mai 2026 consacrée à l'esquisse de T_MQ-S2. Il n'est pas un manuscrit ni un plan, mais un réservoir de matière à laquelle puiser, classée selon la typologie posée par Aksel en fin de session :

- **Notes froides** : matière tenue, formulée avec la rigueur nécessaire pour être intégrée à un article sans retravail majeur. Publiable en l'état (sous réserve d'adaptation contextuelle).
- **Notes tièdes** : matière conceptuellement claire mais qui doit encore être éprouvée, articulée à d'autres pièces du cadre, ou tempérée par des refus explicites. À prolonger avant intégration.
- **Notes chaudes** : matière brute, en émergence, qu'il ne faut pas réduire trop vite. À laisser respirer ; toute formulation prématurée risquerait d'en figer la fécondité.

Le tri viendra plus tard. L'exhaustivité prime sur la sélection à ce stade.

---

## I. Notes froides

### F1. Stern-Gerlach comme coupe constitutive en acte (matière de §2)

L'expérience de Stern-Gerlach sépare un faisceau de particules de spin demi-entier en deux taches sur un écran, lorsque le faisceau traverse un gradient de champ magnétique inhomogène. Les étiquettes *spin up* et *spin down* ne nomment aucune propriété intrinsèque attachée à la particule : elles sont entièrement relatives à l'orientation de l'appareil. Retourner le dispositif inverse les étiquettes sans rien changer à la particule. Tourner le dispositif d'un quart de tour pour aligner le gradient sur un autre axe produit à nouveau une distribution équiprobable selon le nouvel axe.

La distinction up/down n'existe comme distinction qu'à travers l'axe sélectionné par le dispositif. Avant ce choix, il n'y a pas de up ni de down ; après, il y a deux taches sur l'écran et un protocole de classification qui les distingue. L'opération qui institue la distinction est entièrement présente, à la portée de tout expérimentateur, et pourtant elle ne se laisse pas traiter comme l'occasion d'une révélation de propriété préexistante.

Cette coupe est *contemporaine, répétable, modifiable* — à la différence du crossover électrofaible mobilisé dans T0, qui institue ses termes dans un processus cosmologique terminé. La constitutivité n'a pas besoin d'être reconstruite par un travail d'archéologie épistémologique : elle est lisible dans la pratique expérimentale même.

### F2. La structure de réduction de groupe (matière de note technique)

À toute rotation R ∈ SO(3) correspond un opérateur unitaire U(R) sur l'espace de Hilbert de la particule. Pour les particules de spin demi-entier, la représentation pertinente est celle du recouvrement universel SU(2). Cette structure garantit que les probabilités prédites par le formalisme sont invariantes sous rotation globale du système, et que les transitions entre bases liées à des axes différents sont régies par des amplitudes qui ne dépendent que des angles relatifs.

L'introduction du gradient de champ magnétique sélectionne un axe (disons z) et brise la symétrie SO(3) en U(1)_z. Cette brisure de symétrie par le dispositif est la traduction technique de la coupe constitutive : passage d'un groupe G à un sous-groupe H, le quotient G/H mesurant l'espace des coupes alternatives exclues mais non détruites par la mesure (elles redeviennent accessibles si l'on tourne l'appareil).

### F3. La coupe est relationnelle, pas attachée à un terme

Ce qui détermine le résultat d'une mesure de Stern-Gerlach, ce n'est ni l'orientation absolue du dispositif, ni l'orientation absolue de la particule, ni la position de l'observateur dans l'espace. C'est uniquement l'angle relatif entre l'état préparé de la particule et l'axe sélectionné par le dispositif. Rotation du dispositif, rotation de la particule (techniquement réalisable par précession dans un champ magnétique entre deux mesures), rotation de l'observateur (qui peut avoir la tête en bas), sont structurellement équivalentes.

Cette équivalence n'est pas un détail formel sans conséquence philosophique. Elle révèle que la coupe constitutive opérée par Stern-Gerlach n'est attachée à aucun des termes de la situation pris isolément. Elle n'est pas une imposition de l'appareil sur la particule, ni une révélation par l'appareil d'une propriété de la particule, ni une catégorisation par l'observateur d'un événement extérieur. Elle est la stabilisation opératoire d'une décomposition à partir d'un angle relatif entre des termes qui se co-spécifient dans l'interaction.

Cette précision est importante pour éviter que la lecture en termes de coupe constitutive ne se réinterprète, par habitude philosophique, comme un acte d'un sujet sur un objet — ce qui rétablirait précisément la dissymétrie que le cadre cherche à diagnostiquer.

### F4. La non-commutativité comme incompatibilité de coupes

Si l'on mesure d'abord selon z, puis selon x sur les particules sorties up, on obtient à nouveau une équiprobabilité. Si l'on remesure ensuite selon z, on n'obtient pas la valeur up initialement obtenue mais à nouveau une équiprobabilité. La mesure selon x n'a pas seulement ajouté une information à la mesure selon z — elle a défait ce que la première mesure avait stabilisé.

Le formalisme rend compte de cette situation par la relation [Ŝ_z, Ŝ_x] = iℏŜ_y. En termes structurels : deux coupes constitutives ne peuvent pas opérer simultanément si les axes qu'elles sélectionnent ne sont pas compatibles. La complémentarité bohrienne, sous cette lecture, ne nomme pas un mystère ontologique sur la nature de la particule, mais une contrainte de structure sur les coupes simultanément actives — certaines coupes s'excluent mutuellement comme opérations, et cette exclusion est inscrite dans la structure mathématique du formalisme lui-même.

### F5. Note sur Young pour intégration en bas de page de §2

Une structure de coupe analogue, opérant non sur le choix d'axe à l'intérieur d'un régime descriptif unifié mais sur la sélection entre régimes descriptifs mutuellement exclusifs, peut être identifiée dans l'expérience des fentes de Young et dans les expériences à choix retardé qui en prolongent l'analyse (Wheeler 1978 ; Jacques et al. 2007). Son examen excède le cadre du présent article.

---

## II. Notes tièdes

### T1. La situation expérimentale comme densification de coupes co-constitutives

La séparation opératoire des trois termes habituellement traités ensemble — observé, dispositif, observateur — révèle que la situation expérimentale n'est pas une coupe constitutive unique, mais une *densification* de coupes co-constitutives. Aucune coupe n'opère seule : les conditions a priori (les coupes déjà stabilisées, les régimes d'intelligibilité, les protocoles de préparation) co-constituent la nouvelle coupe avec les autres éléments impliqués. La trame des coupes se densifie au fur et à mesure que de nouvelles opérations s'y ajoutent, sans que cette densification soit un simple empilement géométrique : chaque coupe nouvelle reconfigure la trame existante en s'y inscrivant, et la trame existante conditionne ce que la coupe nouvelle peut stabiliser.

*L'observé* entre dans le dispositif avec un état préparé. Cet état n'est pas une donnée brute : il est lui-même densifié par des coupes antérieures (préparation, sélection, peut-être mesure préalable). L'observé est une zone densifiée de coupes de préparation.

*Le dispositif* sélectionne l'axe, le régime descriptif, ou plus généralement le type de coupe qui sera opérée. Il a sa propre épaisseur historique : il a été conçu, calibré, validé selon des protocoles qui présupposent une théorie. Le dispositif n'est jamais neutre — il est l'incarnation matérielle d'une coupe théorique antérieure (celle qui dit que tel type de phénomène est intéressant à mesurer, selon tel type d'observable). Le dispositif est une zone densifiée de coupes théoriques.

*L'observateur* lit, inscrit, classifie le résultat. Mais l'observateur est lui-même situé dans un régime de catégorisation qui présuppose des coupes antérieures (qu'est-ce qu'un résultat, qu'est-ce qu'une donnée, qu'est-ce qui compte comme observation).

Ce qui se passe dans la mesure n'est pas l'imposition d'une coupe sur un donné neutre. C'est l'articulation, au point de la mesure, de trois zones densifiées qui se rencontrent et co-constituent un événement nouveau. La coupe constitutive en jeu dans la mesure n'est pas une coupe isolée : elle est le moment où la densification locale produit un résultat stabilisable, à partir de termes déjà tous co-constitués par des coupes antérieures.

**Tension à tempérer** : cette notion de densification risque de tomber dans une régression à l'infini (chaque coupe en présuppose d'autres, et ainsi de suite). Aksel précise : « On ne peut pas dire tout est coupe parce qu'il faut que ça reste opératoire. L'idée, ce n'est pas que de dire que tout est coupe, ça n'a pas de sens, mais c'est pouvoir se servir de cet outil, des coupes conceptuelles, des coupes constitutives, pour pouvoir décrire le monde d'une autre manière peut-être. » La régression doit être bornée par le critère d'opérationnalité : on ne creuse les coupes antérieures que tant que cela déplace quelque chose dans la description du présent. C'est une expression de la variabilité opératoire appliquée à la densification elle-même.

**Note sur le choix terminologique** : « densification » est privilégié sur « empilement » (trop géométrique et statique), « enchevêtrement » (descriptif d'un état plutôt que d'un processus) et « co-constitutivité » (qui reste comme mécanisme interne mais redonde avec « coupe constitutive » si pris comme désignation globale). « Densification » est cohérent avec le vocabulaire des Définitions §5, porte une dimension processuelle, et capte phénoménologiquement le fait que la situation expérimentale est une trame qui s'épaissit plutôt qu'une superposition de strates.

### T2. La coupe dispositif/observateur n'est pas donnée — elle est elle-même une coupe

La frontière entre dispositif et observateur n'est pas évidente. Dans Stern-Gerlach, l'observateur peut être un humain qui lit l'écran, un appareil photographique qui enregistre l'impact, un détecteur électronique qui produit un signal, un système de traitement de données qui inscrit le résultat dans une mémoire. Le basculement du dispositif à l'observateur est lui-même un choix de coupe — la fameuse coupe de Heisenberg, que la note du 6 avril identifiait comme l'artefact spécifique de Copenhague.

Cette frontière mobile est précisément le symptôme d'une coupe qui ne se laisse pas naturaliser. On peut la placer entre la particule et le détecteur, ou entre le détecteur et l'enregistrement, ou entre l'enregistrement et la lecture humaine — aucune de ces positions n'est intrinsèquement bonne, et le choix est lui-même une opération constitutive.

**Précision d'Aksel à intégrer** : « Classique ou quantique, ça n'a pas d'importance. C'est toujours, de toute manière, la coupe de Copenhague, mais peu importe en fait. Ce qui importe pour notre description du monde, c'est de savoir dans quelle coupe nous nous situons et pas savoir ce que fait tel ou tel coupe. Alors bien sûr que si, c'est utile, mais ce qui est nécessaire, c'est de savoir dans quel régime on opère. »

Cette précision déplace le geste : le cadre ne propose pas de résoudre où placer la coupe de Heisenberg (problème insoluble dans le cadre où il se pose), mais de rendre opératoire la question de savoir depuis quel régime on parle. C'est un déplacement de la question elle-même, pas une réponse à la question d'origine.

### T3. Le régime classique d'intelligibilité opère à plusieurs niveaux dans l'expérience

La séparation opératoire des trois termes révèle que le régime classique d'intelligibilité opère à plusieurs niveaux dans l'expérience. Il opère dans la préparation de l'observé (qui présuppose qu'on peut parler d'un « état » de la particule). Il opère dans la conception du dispositif (qui présuppose qu'on peut isoler un sous-système et le coupler à un instrument). Il opère dans la fonction de l'observateur (qui présuppose qu'il y a un « résultat » à lire).

Le régime classique d'intelligibilité, dans la mesure quantique, n'est pas une présupposition unique qui pèserait sur toute la situation — c'est un faisceau d'opérations qui structurent chacun des trois termes de manière différente. C'est cela qui rend la non-opacification si tenace : il ne suffirait pas de corriger un seul des points d'appui classiques pour que la difficulté disparaisse ; il faudrait corriger les trois simultanément, ce qui n'est précisément pas faisable depuis l'intérieur du régime classique.

**Articulation possible avec §3 de T_MQ-S2** : le révélateur-limite ne se contente pas de signaler qu'une coupe résiste à l'opacification. Il signale que cette résistance opère simultanément sur trois niveaux de la situation expérimentale, et qu'aucun des trois ne peut être stabilisé sans laisser les autres en suspens. Cela renforce le diagnostic et lui donne une structure plus précise.

### T4. Le geste central : savoir depuis quel régime on parle

Aksel : « Nous devons cesser de penser que lorsque nous observons le monde, c'est une observation directe du réel, que ce soit dans le monde classique ou quantique. Peu importe le niveau de perception, il faut toujours savoir — je pense que ce n'est pas seulement souhaitable, mais nécessaire — de savoir depuis où on parle. »

Cette formulation est plus large que ce que T_MQ-S2 traite. Elle énonce une thèse épistémologique générale, qui pourrait constituer le geste de fond du cadre des coupes constitutives dans son ensemble — la nécessité de tenir explicitement la position depuis laquelle on parle, classique ou quantique, perceptive ou théorique.

**À tempérer** : formulée telle quelle, cette thèse risque de paraître soit triviale (« évidemment qu'on parle depuis quelque part »), soit excessive (« on ne peut jamais parler du monde, seulement de notre position »). La force du geste tient à la précision avec laquelle on caractérise *ce que* la position fait — quelles opérations elle stabilise, quelles distinctions elle rend opératoires, quelles autres elle exclut. La thèse n'est pas que toute connaissance est située (banalité), mais que la position est constitutive de ce qui peut compter comme connaissance (geste plus fort).

### T5. Articulation avec d'autres traditions

Aksel : « Alors ça rejoint les philosophies situées, même l'écoféminisme. Mais bon, là, ça déborde. »

À garder en mémoire comme territoire de convergence non encore explicitement articulé. Les épistémologies situées (Haraway 1988, *Situated Knowledges*), les théories du standpoint (Harding, Hartsock), les épistémologies écoféministes, partagent avec le cadre des coupes constitutives la thèse que la position est constitutive de ce qui peut compter comme connaissance. Mais elles l'ancrent dans une analyse du pouvoir et de la subjectivation que le cadre des coupes constitutives ne mobilise pas explicitement.

L'articulation est possible mais demande prudence : ne pas annexer ces traditions, ne pas les réduire à des cas particuliers du cadre, mais reconnaître la parenté structurelle tout en respectant leurs engagements propres. C'est un chantier ultérieur, pas une matière pour T_MQ-S2.

### T6. L'expérience de Young comme coupe inter-régime (développement examinatif)

L'expérience des fentes de Young, dans sa version quantique, fait passer des particules une par une à travers un dispositif à deux fentes. Selon que l'on dispose ou non d'une information sur la fente effectivement traversée, on observe soit deux taches distinctes (régime « trajectoire »), soit une figure d'interférence (régime « onde »). Le facteur déterminant n'est pas la lecture humaine de l'information mais sa disponibilité physique : si l'information est inscrite quelque part dans l'environnement, même si personne ne la consulte, les interférences disparaissent.

**Structure différente de Stern-Gerlach.** Là où Stern-Gerlach met en jeu une coupe constitutive qui sélectionne *un axe de décomposition* à l'intérieur d'un régime descriptif unifié (le spin), Young met en jeu une coupe constitutive qui sélectionne *un régime descriptif* parmi plusieurs incompatibles (onde ou trajectoire). Ce ne sont pas deux décompositions d'une même observable, ce sont deux modes d'apparition du phénomène qui ne peuvent coexister.

Cette différence suggère que le cadre des coupes constitutives, dans son application à la mécanique quantique, devrait probablement distinguer deux niveaux de coupe :
- *coupe intra-régime* : choix d'axe à l'intérieur d'un cadre descriptif déjà fixé (Stern-Gerlach) ;
- *coupe inter-régime* : choix entre cadres descriptifs incompatibles (Young, et plus largement la complémentarité bohrienne au sens strict).

Les deux sont constitutives au sens du cadre, mais elles n'opèrent pas au même niveau de la situation expérimentale.

**Trois éléments structurels que Young rend particulièrement saillants** (par rapport à Stern-Gerlach) :

*Le rôle de l'inscription.* La disparition des interférences ne demande pas qu'un observateur humain *lise* l'information de chemin — il suffit qu'elle soit physiquement disponible, inscrite dans l'environnement. Cela répond par anticipation à toute lecture du cadre qui voudrait y voir un constructivisme centré sur la conscience. La coupe constitutive opère par inscription physique, pas par conscience d'un sujet. Young est le cas où cela devient le plus visible, et cette matière est précieuse pour répondre aux objections constructivistes que le cadre rencontrera nécessairement.

*Le caractère contrefactuel de la coupe.* Dans les expériences à choix retardé (Wheeler 1978, réalisées notamment par Jacques et al. 2007), l'information de chemin peut être effacée *après* le passage de la particule mais avant qu'elle n'atteigne l'écran. Si l'on efface l'information, les interférences réapparaissent ; si on la conserve, elles ne se forment pas. La coupe n'a donc pas la structure temporelle qu'on lui attribuerait naïvement — elle n'est pas une opération qui précède son résultat, elle est une opération dont la stabilisation peut être différée. Cela complique sérieusement toute lecture qui voudrait faire de la coupe un acte ponctuel survenant à un instant déterminé.

*La non-localité de la coupe.* La figure d'interférence est globale ; aucune particule individuelle ne porte la figure. La coupe constitutive porte sur une distribution statistique qui n'est pas attachée à un événement singulier. Cela diffère de Stern-Gerlach, où chaque particule produit individuellement une déflexion mesurable. Young met en scène une coupe dont le résultat n'est lisible qu'au niveau statistique, ce qui ouvre une question structurelle sur le rapport entre la coupe individuelle et la coupe collective.

**Tensions à éprouver avant intégration.**

*Première tension.* La distinction intra-régime / inter-régime est conceptuellement utile mais demande à être éprouvée sur d'autres cas avant d'être stabilisée. Est-elle bien une distinction structurelle, ou un effet de la manière dont nous classons les expériences ? Les régimes onde et trajectoire sont-ils vraiment des régimes au même sens que le serait une décomposition spectrale, ou la distinction se brouille-t-elle quand on la creuse ? À vérifier avec la littérature technique sur la complémentarité bohrienne (Bohr, Faye, Bitbol).

*Deuxième tension.* Le choix retardé pose un problème de temporalité que le cadre n'a pas encore explicitement traité. Si la coupe peut être stabilisée après l'événement qu'elle constitue, alors la chronologie linéaire « préparation → mesure → résultat » est insuffisante. Il faut une notion de stabilisation rétroactive, ou plus exactement de stabilisation dont la temporalité ne coïncide pas avec celle de l'événement physique sous-jacent. Cela demande un travail conceptuel qui n'est pas encore fait.

*Troisième tension.* Le caractère statistique de la figure d'interférence interroge la notion de coupe constitutive individuelle. Si la coupe ne se manifeste qu'au niveau statistique, alors elle n'opère pas sur une particule particulière mais sur une distribution. Comment articuler cela avec la formulation actuelle du cadre, qui semble présupposer que la coupe opère dans chaque événement de mesure ? À creuser.

**Décision provisoire.** Young ne sera pas déployé comme cas principal dans T_MQ-S2 (Stern-Gerlach suffit pour le geste de §2). Une mention en note de bas de page suffit dans l'article (voir D1 dans les décisions de session). Mais la matière de cette note T6 — distinction intra-régime / inter-régime, rôle de l'inscription, choix retardé, non-localité statistique — peut nourrir un travail ultérieur, possiblement le T_MQ-D1 sur les interprétations comme coupes concurrentes (où Young serait un cas central), ou un article spécifique sur la complémentarité bohrienne.

---

## III. Notes chaudes

### C1. L'extension à l'expérience en général

Aksel : « J'ai dit effectivement dans la séparation opératoire, nous pourrions déceler d'autres éléments relatifs à l'expérience, à l'expérience en général. Oui, mais je ne sais pas exactement encore quoi. Mais moi aussi ce mot expérience en général, il me parle. Ce que je voulais dire dans un premier temps, c'était au-delà de l'expérience scientifique en général, au-delà du cas quantique, c'était encore au-delà de ça. »

À ne pas réduire prématurément. L'intuition est que la séparation opératoire observé/dispositif/observateur, qui rend visible la structure constitutive de la mesure quantique, pourrait avoir une portée bien au-delà de l'expérience scientifique. Mais cette portée n'est pas encore tenue, et la formuler trop vite risquerait de la rabattre soit sur une thèse phénoménologique générale, soit sur une thèse anthropologique de la perception, soit sur autre chose qui n'est pas encore clair.

À laisser respirer. Pistes possibles (à ne pas privilégier l'une sur l'autre tant que la matière n'est pas mûre) :
- L'expérience perceptive ordinaire (voir, entendre, toucher) comme situation où observé, dispositif (corps sensoriel) et observateur (sujet percevant) se distinguent opératoirement de manière différente du cas scientifique.
- L'expérience vécue dans son sens phénoménologique large, où la distinction entre ce qui est éprouvé et celui qui éprouve est elle-même une coupe à interroger.
- Le rapport au monde dans son sens le plus ample, incluant les modes non-cognitifs (affects, ambiances, attentes).
- Les pratiques contemplatives, qui mettent en jeu précisément la question de savoir depuis où l'on perçoit.

### C2. Prudence pour ne pas mélanger les régimes

Aksel : « Mais il faut tout de suite changer les régimes de perception, bien définir ce qu'on dit pour ne pas mélanger entre physique et phénoménologie. »

Cette prudence est essentielle. Si l'extension à l'expérience perceptive ou phénoménologique est faite, elle doit être faite avec un signalement explicite du changement de régime. La structure formelle qui opère dans Stern-Gerlach (SU(2), non-commutativité, etc.) ne se transporte pas telle quelle dans la phénoménologie perceptive — ce serait une analogie structurelle, pas une identité.

La force du cadre des coupes constitutives, telle qu'elle est tenue dans T0, est précisément de reconnaître des parentés structurelles entre registres irréductibles sans les fusionner. Cette discipline doit être maintenue si l'extension à l'expérience générale est entreprise.

À garder en mémoire comme garde-fou méthodologique, pas comme contenu à intégrer maintenant.

### C3. La co-constitution comme phénomène général

Aksel : « En réalité, chaque phénomène, c'est la constitution, la co-constitution on pourrait dire, de plusieurs autres branches de phénomènes. D'autres coupes donc. »

Formulation brute mais féconde. Elle suggère que la co-constitution n'est pas un trait particulier de la mesure quantique mais une structure générique de tout phénomène. Chaque phénomène serait la rencontre de plusieurs branches de coupes constitutives, dont l'articulation singulière fait advenir ce phénomène-ci plutôt qu'un autre.

À ne pas formuler trop vite. La tentation serait de poser cela comme thèse métaphysique générale (« tout phénomène est co-constitué »), ce qui retomberait dans le piège que T1 évite déjà — la généralisation totalisante. Mais l'intuition est plus précise : il ne s'agit pas de dire que tout est co-constitution, mais que l'outil de la co-constitution permet de décrire des phénomènes que d'autres outils décrivent moins bien.

À tenir comme piste ouverte vers une caractérisation plus fine des modes de co-constitution (intra-régime, inter-régime, transversale, etc.) sans encore l'arrêter.

### C4. L'observation directe du réel comme illusion stabilisée

Aksel : « Fondamentalement ce que je souhaite dire, c'est que nous devons cesser de penser que lorsque nous observons le monde, c'est une observation directe du réel. »

Cette formulation, prise hors contexte, ressemble à du constructivisme épistémologique standard. Mais dans le contexte du cadre, elle dit quelque chose de plus fin : ce n'est pas que nous n'avons pas accès au réel (thèse sceptique), c'est que cet accès passe toujours par des opérations constitutives qui co-spécifient ce qui peut compter comme observation et ce qui peut compter comme réel.

À laisser chaude parce que la formulation publique demande une précision considérable pour ne pas être reçue comme du constructivisme relâché. Le geste qu'elle porte est précis (le réel n'est pas observable sans médiation constitutive ; cette médiation n'est pas un voile mais une condition d'apparition), mais sa formulation est encore trop directe pour un article. Elle gagnera à être tenue plus longtemps avant d'être fixée.

### C5. Le rapport entre « depuis où on parle » et la position du sujet connaissant

Si la nécessité de savoir « depuis où on parle » devient un geste central du cadre, alors une question se pose : que devient la position du sujet connaissant ?

T0 §4 esquisse cette position comme « celle d'un sujet connaissant immanent au processus qu'il décrit », mais sans la déployer. Si T_MQ-S2 ou un texte ultérieur mobilise pleinement la nécessité de savoir depuis quel régime on parle, alors cette position de sujet connaissant immanent demande à être caractérisée plus précisément.

Pistes brutes à laisser respirer :
- La position du sujet connaissant n'est pas un point d'observation extérieur. Elle est elle-même constituée par les coupes qu'elle pratique.
- Cette position est mobile : elle se déplace selon les coupes qu'elle adopte, et reconnaît ses propres déplacements comme partie de son opération.
- Tenir cette position demande une discipline réflexive particulière, qui n'est pas la réflexivité standard de la philosophie (un sujet qui se prend lui-même pour objet) mais une réflexivité opératoire (un sujet qui tient explicitement la coupe depuis laquelle il opère).

Ces pistes ne sont pas mûres. À ne pas formuler avant un travail conceptuel plus poussé.

---

## IV. Décisions de session à reporter dans T_MQ-S2

### D1. Intégration en note dans §2 — Mention Young

À intégrer comme note de bas de page en fin de §2 de T_MQ-S2, formulation :

> Une structure de coupe analogue, opérant non sur le choix d'axe à l'intérieur d'un régime descriptif unifié mais sur la sélection entre régimes descriptifs mutuellement exclusifs, peut être identifiée dans l'expérience des fentes de Young et dans les expériences à choix retardé qui en prolongent l'analyse (Wheeler 1978 ; Jacques et al. 2007). Son examen excède le cadre du présent article.

### D2. La matière sur l'empilement des coupes n'est pas intégrée à T_MQ-S2

Décision d'Aksel : ne pas intégrer la séparation opératoire observé/dispositif/observateur dans le plan actuel de T_MQ-S2. La matière est consignée dans ce réservoir (notes T1, T2, T3, T4) pour usage ultérieur.

Cela laisse T_MQ-S2 avec son plan en six sections tel qu'il a été stabilisé en session.

### D3. La matière sur l'extension à l'expérience en général reste en réserve

Toute la matière des notes chaudes (C1 à C5) reste en réserve. Aucune intégration à T_MQ-S2. Elle pourra nourrir un travail ultérieur — peut-être un article spécifique sur la transversalité de la structure de coupe à l'expérience non scientifique, peut-être une révision du cadre lui-même, peut-être autre chose.

---

## V. Statut du document

Document de travail interne. Rédigé à l'issue de la session du 20 mai 2026. À reprendre, modifier, augmenter selon les besoins du travail.

Les notes froides peuvent être intégrées telles quelles dans T_MQ-S2 ou un autre texte, avec adaptation contextuelle minimale. Les notes tièdes demandent un travail conceptuel supplémentaire avant intégration. Les notes chaudes doivent être laissées respirer ; toute intégration prématurée risque de figer leur fécondité.

La typologie chaud/tiède/froid elle-même est un outil de travail, pas une catégorisation fixée. Une note peut migrer entre catégories au fil du temps : tiédir en gagnant en précision, refroidir en étant testée par d'autres terrains, ou au contraire chauffer à nouveau si elle ouvre des questions imprévues.
