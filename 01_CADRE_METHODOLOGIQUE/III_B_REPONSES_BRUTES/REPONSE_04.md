### A. Réponse principale

Le verdict courant du Cycle 10 est plus étroit que certaines de ses formulations historiques, mais ses principaux résultats locaux ne disparaissent pas. Le cadre actif demande de distinguer la constance de la cible, la stabilisation de l’accès et le mode de constitution ; lorsqu’un mécanisme dynamique est invoqué, il faut encore établir la grandeur effectivement stabilisée, le bassin de conditions, la durée et la tolérance, les corrections, le coût en paramètres et en énergie et la condition d’échec. L’accueil vivant des cycles donne déjà le rang correct : les phases 2–4 sont des **tests de modèles bornés**, « non une histoire physique acquise ».

#### Verdict d’ensemble

Le Cycle 10 établit aujourd’hui trois résultats scientifiques locaux conditionnels :

1. **Phase 2 —** **`CONSERVER_COMME_RESULTAT_LOCAL`****.** Dans le modèle scalaire–Higgs `Z₂` homogène, stable, non dissipatif et quadratique étudié, une relaxation rapide du déplacement de `v` est compatible avec le filtre BBN simplifié, mais l’énergie du condensat se comporte ensuite comme de la matière et produit une relique inacceptable pour les déplacements initiaux électrofaibles significatifs définis par le scan. Le résultat utile n’est donc pas « une fixité électrofaible physiquement constituée », mais : **dans cette architecture conservatrice minimale, amortir le déplacement de** **`v`** **ne résout pas le bilan énergétique ; le coût réapparaît sous forme de relique cohérente.**
2. **Phase 3 —** **`CONSERVER_COMME_RESULTAT_LOCAL`****.** Ajouter une auto-interaction quartique ne suffit pas, dans le modèle homogène stable et non dissipatif testé. La dilution initiale de type rayonnement améliore le devenir énergétique, mais retarder la transition vers le régime quadratique exige une énergie quartique initiale croissante. Le scan stocké contient `2 077 061` points, `0` point acceptable selon ses critères et un meilleur cas significatif encore à `r_eq ≈ 6.0×10^7`. C’est un résultat négatif local fort : **la modification conservatrice quartique testée ne répare pas l’échec énergétique.**
3. **Phase 4 —** **`CONSERVER_COMME_RESULTAT_LOCAL`** **+** **`REQUALIFIER_RANG_OU_PORTEE`****.** Dans les équations homogènes moyennées avec un terme phénoménologique de transfert `Γφ ρφ`, il existe des paramètres qui satisfont simultanément les filtres internes de déplacement initial, sous-dominance énergétique, déplacement de `v` à la BBN, relique et entropie. Cela établit une **fenêtre phénoménologique non vide pour le bilan ouvert défini**, et non l’existence d’un mécanisme physique réalisant cette fenêtre. Le script dit explicitement qu’il « ne dérive aucun taux microscopique » et cartographie seulement le besoin phénoménologique.

C’est aussi le verdict déjà incorporé au cadre canonique : rendre une grandeur dynamique n’explique rien à lui seul ; les modèles conservatifs testés obtiennent la relaxation de `v` mais échouent sur son devenir énergétique, tandis qu’un bilan ouvert possède une fenêtre phénoménologique dont la réalisation microscopique reste à établir.

#### Ce qui est machine, calcul ou résultat scientifique

La séparation est importante ici.

**Phase 2.** Le script ne résout pas une cosmologie complète : il applique un fond radiatif, un `g_*` par paliers, une condition `H≈m_eff`, puis des lois analytiques de dilution `a^-3`. Le CSV conservé contient des points représentatifs et confirme notamment les énormes rapports `ρφ/ρrad` à l’égalité pour `q_i=0.1`. En revanche, le fichier de sortie conservé ne contient pas lui-même le tableau agrégé `20 769 points / 0 tous critères` ni la totalité du scan : ces nombres sont rapportés dans le document de résultats et le code permet leur reproduction. Sans relancer le calcul — ce que la mission interdit — leur statut est donc **résultat calculatoire rapporté et reproductible par le script**, pas sortie machine indépendante que j’aurais reproduite ici.

**Phase 3.** Le CSV est une sortie machine directe pour les grandeurs principales : taille du scan, zéro point acceptable et meilleur cas. Le script montre qu’il s’agit d’un balayage analytique d’une transition quartique→quadratique prescrite, pas d’un solveur de Boltzmann ou d’une intégration complète du potentiel thermique.

**Phase 4.** Le CSV stocke les minima de `γ_EW` trouvés sur des grilles pour seulement quatre `q_i` représentatifs. Le script calcule l’évolution moyenne de variables comobiles sous quatre prescriptions de `Γφ`; il ne dérive pas `Γφ` d’un lagrangien. La trajectoire obtenue est donc une **trajectoire calculée du toy model**, non une trajectoire empirique de notre Univers.

Un détail mérite d’être conservé : les lignes `φ²` du CSV satisfont elles aussi les filtres binaires du script, mais seulement pour `γ_EW ~ 10^9–10^11`. Le texte ne les exclut d’ailleurs pas algébriquement ; il les juge impropres à constituer un candidat naturel dans ce toy model. Il faut donc distinguer **« passe les filtres »** de **« profil physiquement plausible/naturel »**. La première proposition est calculatoire ; la seconde est une qualification interprétative qui reste à soutenir par une microphysique.

#### Requalification de la « quasi-fixité »

La cible réellement calculée est principalement `v`, via

`q = λ_Hφ φ²/μ_H²` puis `v² = v₀²(1-q)`.

`G_F`, les masses des bosons et les masses fermioniques n’ont pas des histoires indépendamment calculées : elles sont dérivées de `v` sous la coupe où couplages de jauge et Yukawa sont maintenus fixes.

Il faut donc requalifier plusieurs expressions :

- **« fixité locale constituée » →** **`REQUALIFIER_RANG_OU_PORTEE`** : ce qui est effectivement montré est une relaxation/quasi-stationnarité de `v` dans un modèle simplifié, sous un régime et des hypothèses déclarés.
- **« stabilisation cinématique » → formulation disciplinaire préférable : amortissement ou relaxation du condensat et du déplacement de** **`v`****.**
- **« stabilisation cosmologique complète » →** **`DECLASSER_FORMULATION_HISTORIQUE`** comme catégorie autonome : le problème testé est plutôt la **compatibilité du bilan énergétique cosmologique** avec les critères du modèle.
- **« fixité avant la BBN » →** **`REQUALIFIER_RANG_OU_PORTEE`** : le calcul montre que le déplacement reconstruit de `v` passe sous le filtre interne de 1 % à l’époque étiquetée BBN. Il ne calcule pas les abondances nucléaires et ne constitue pas une validation BBN complète. Le dossier observationnel lui-même précise que toute contrainte sur `v` dépend de corrélations avec masses, QCD et autres secteurs.
- **« relique supprimée » en phase 4 →** **`REQUALIFIER_RANG_OU_PORTEE`** : dans les équations effectives, l’énergie du mode homogène est transférée au bain relativiste. L’identité du récepteur, la thermalisation, les masses thermiques, le rayonnement caché et `ΔN_eff` ne sont pas calculés.
- **« histoire électrofaible/cosmologique » lorsqu’elle suggère notre histoire réelle →** **`DECLASSER_FORMULATION_HISTORIQUE`****.** La reprise comparative a déjà opéré exactement cette correction : un scan compare des paramètres, l’intégration donne une histoire possible dans le modèle, et seul un raccord à des preuves empiriques discriminantes permettrait de parler d’histoire physique établie.

Aucune de ces phases n’établit donc que `v`, `G_F` ou « la force faible » ont réellement varié dans l’Univers. La typologie locale refusait déjà de confondre dépendance RG, thermique, dynamique spatio-temporelle et inférentielle.

#### Ce que les phases perdent en portée, sans perdre leur résultat

Les formulations les plus larges du cadrage visaient un bassin de conditions initiales, une convergence de trajectoires, une réduction du fine-tuning et finalement une histoire physique discriminable. Ces objectifs ne sont pas tous réalisés par les calculs présents.

En particulier :

- **Attracteur ou bassin étendu :** **`NON_ETABLI`****.** Les phases 2–4 ne balayent pas un espace complet `{φ_i, \dot φ_i}` permettant d’établir un attracteur ; la phase 4 ne teste que quatre `q_i` représentatifs pour la recherche des taux minimaux.
- **Réduction de la contingence/fine-tuning :** **`NON_ETABLI`****.** Le problème se déplace successivement vers l’abondance du condensat puis, en phase 4, vers le profil et l’origine de `Γφ`, le canal récepteur et ses couplages. La reprise comparative dit explicitement que les paramètres nouveaux, la robustesse et la prise empirique restent insuffisamment établis.
- **Viabilité cosmologique générale :** **`NON_ETABLI`****.** Les fonds cosmologiques, transitions thermiques et critères observationnels utilisés sont simplifiés.
- **Probabilité ou naturalité d’une région :** **`NON_ETABLI`****.** Une densité de points de grille ou l’existence d’une fenêtre ne fournit aucune mesure physique ni probabilité.
- **Constance effective de** **`v`** **ou de** **`G_F`** **produite par le mécanisme :** **`NON_ETABLI`** **au sens du cadre courant.** Une quasi-stationnarité calculée ne reçoit pas automatiquement ce statut.

La perte de portée est donc substantielle, mais elle ne détruit pas les trois informations locales : deux architectures conservatrices testées échouent de façons précisément localisées ; l’ouverture phénoménologique du bilan énergétique élimine cet obstacle dans le système effectif considéré.

#### Résultats négatifs et limites à conserver

Ils ne doivent pas être comprimés en « Cycle 10 échoue » ni transformés en exclusion générale des portails scalaires.

- **Phase 2 :** le condensat cohérent `Z₂`, stable, quadratique et non dissipatif est écarté comme mécanisme autonome pour une variation initiale >1 % sous les critères retenus. Ce n’est pas l’exclusion de tout portail scalaire.
- **Phase 3 :** l’auto-interaction quartique seule, avec transition vers le terme massif induit et sans redistribution d’énergie, ne suffit pas dans le domaine scanné. Ce n’est pas l’exclusion de toute dynamique quartique, de toute fragmentation ou de toute phase thermique plus riche.
- **Phase 4 :** une dissipation qui s’auto-éteint comme `φ²` demande un taux initial gigantesque dans cette prescription ; cela ne démontre pas que tout couplage dépendant du champ échoue.
- Les filtres BBN, d’entropie, de domination et de relique sont des **critères exploratoires du toy model**, non des likelihoods observationnelles complètes.
- La phase 4 suppose notamment domination radiative, `g_*` constant, thermalisation instantanée visible, oscillations moyennées, absence de masses thermiques, fragmentation, statistique quantique et rétroaction microscopique.

Ces négatifs sont scientifiquement informatifs précisément parce qu’ils localisent l’obstacle : d’abord la dilution de l’énergie, puis son élimination/redistribution, enfin l’origine microscopique du transfert.

#### Ce qui reste ouvert et ce qui pourrait réellement changer le verdict

Le point d’ouverture scientifique le plus précis est maintenant la **réalisation microscopique de la fenêtre dissipative**. Les documents proposent brisure de `Z₂`/mélange Higgs–scalaire, Yukawa vers des fermions légers, second scalaire relativiste, annihilation ou évaporation thermique. Mais cette liste est un espace de candidats, pas une sélection acquise.

Pour faire monter le résultat de rang, il faudrait au minimum :

- une réalisation microscopique explicitement choisie et autorisée, avec lagrangien et paramètres définis ;
- une dérivation de `Γφ(φ,T,…)`, plutôt qu’une prescription choisie ;
- le traitement des seuils et blocages cinématiques, masses thermiques, `g_*(T)` et région QCD, rétroaction et, selon le canal, fragmentation/thermalisation ;
- la confrontation du taux **dérivé** à la fenêtre trouvée en phase 4 ;
- une analyse BBN réelle des abondances et des corrélations induites, puis les contraintes tardives pertinentes : mélange, cinquième force, horloges, rayonnement caché/`ΔN_eff`, etc. ;
- un vrai test de robustesse/bassin sur les conditions initiales et les paramètres, avec tolérance et domaine déclarés ;
- des observables discriminantes permettant de distinguer ce scénario d’une valeur simplement fixe.

Une réalisation microscopique qui n’atteint aucune des fenêtres de taux fermerait ou réduirait la phase 4. À l’inverse, une réalisation qui produit naturellement le bon profil, survit aux corrections thermiques et aux contraintes et montre une robustesse à un bassin non trivial permettrait une qualification plus forte. Même alors, elle resterait un modèle viable avant de devenir une histoire empirique de notre Univers.

#### Autorisation de la prochaine opération scientifique

Il faut distinguer deux actes.

**La réinstruction scientifique en lecture seule est ouverte.** Le corps initial de #130 disait encore `NON_OUVERT`, mais une décision ultérieure dans ses commentaires valide le cadrage et indique `AUDIT_SCIENTIFIQUE = OUVERT_SOUS_CE_CADRAGE`. La même décision précise toutefois que cette ouverture **n’autorise aucun calcul ni nouveau run sans instruction distincte**. Le méta-audit #135 a ensuite conclu qu’il n’existait plus de raison de maintenir un arrêt général de la science, sans convertir cette conclusion méthodologique en autorisation d’un acte scientifique particulier.

**La prochaine opération de fond du Cycle 10 — choisir et calculer une réalisation microscopique — n’est pas actuellement autorisée par les sources consultées :** **`NON_ETABLI`** **comme autorisation, donc ne pas l’exécuter.** La phase 4 la propose ; elle ne l’autorise pas. Aucun ancrage opérationnel Cycle 10 correspondant n’a été retrouvé dans les recherches ciblées des issues. En outre, choisir un nouveau modèle/canal et ses paramètres franchit une frontière scientifique ; `AGENTS.md` réserve précisément les décisions de modèle, paramétrisation, interprétation et seuil d’évidence à une décision humaine.

La prochaine décision recevable est donc : **maintenir ouvert le besoin de microphysique, sans sélectionner ni calculer un candidat par simple continuation de la phase 4.**

### Qualification finale

**Cycle 10 dans son état courant :**

- Phase 2 : **`CONSERVER_COMME_RESULTAT_LOCAL`** — échec énergétique du modèle stable quadratique, sous hypothèses explicites.
- Phase 3 : **`CONSERVER_COMME_RESULTAT_LOCAL`** — le régime quartique conservatif testé ne lève pas l’obstacle.
- Phase 4 : **`CONSERVER_COMME_RESULTAT_LOCAL`** **+** **`REQUALIFIER_RANG_OU_PORTEE`** — fenêtre non vide dans un toy model dissipatif effectif ; microphysique absente.
- « fixité constituée », « stabilisation cosmologique complète », « histoire électrofaible viable/réelle » lorsqu’elles dépassent ce contenu : **`DECLASSER_FORMULATION_HISTORIQUE`** ou réécrire en vocabulaire local borné.
- attracteur, réduction du réglage, probabilité de réalisation, compatibilité cosmologique complète, ancienne variation réelle de l’échelle faible, mécanisme microscopique : **`NON_ETABLI`**.
- réalisation microscopique et confrontation observationnelle complète : **`MAINTENIR_OUVERT`**.
- nouvelle opération scientifique/calculatoire C10 : **non autorisée par simple dette ou par la phrase « étape suivante » ; autorisation explicite encore requise.**

### B. Trace de contrôle compacte

```text
MATRICE_LUE = OUI

SOURCES_REELLEMENT_UTILISEES =
- branche audit/inventaire-regles-119-138-20260820 : uniquement
  BOOTSTRAP_COMMUN.md, MATRICE_9C.md, MISSION.md
- main@c9deaf1fe86b742d9227f0385e975809f64dc9bd :
  README.md ; AGENTS.md ; 02_CYCLES_PHYSIQUES/README.md ;
  refondation-du-domaine.md ;
  Decision_statuts_constance_acces_constitution_v0_1.md ;
  programme_audits.md ;
  intégralité du dossier Cycle 10 répertorié au commit
  (10 Markdown, 3 scripts Python, 3 CSV de résultats) ;
  Reprise_comparative_cycles_9_10_contrefactuel_dynamique_contingence_v0_1.md
- surfaces GitHub courantes : issue #130 et ses commentaires ;
  issue #135 et ses commentaires ; recherches ciblées d’issues Cycle 10 /
  dissipation / relique / phase 4
- aucune source web externe ; PR #139 non consultée

FONCTIONS_ACTIVEES =
- multiplicité des surfaces d’autorité -> autorité/rang courant ->
  refondation + décision de rang + routage vivant priment sur le vocabulaire ancien
- sorties CSV/scripts invoquées comme science -> machine/technique/science ->
  séparation sortie machine, modèle calculé, résultat local et interprétation
- quasi-fixité/stabilisation -> nature et indexation du maintien ->
  cible v + régime/modèle/tolérance distingués de la viabilité énergétique
- scan + trajectoires -> cible/accès/constitution + typage des chemins ->
  axe de paramètres et trajectoire calculée refusés comme histoire physique
- résultats positifs/négatifs locaux -> rang et portée ->
  conservation des phases 2–4 avec portée strictement bornée
- formulations historiques larges -> ancien vers courant ->
  requalification sans effacement des résultats locaux
- échecs et contrôle phi² -> négatifs/refus ->
  conservation au rang exact, sans exclusion de toute la famille
- “étape suivante” / dette microphysique -> autorisation d’agir ->
  dette et proposition ne valent pas autorisation de modèle ou calcul

FONCTIONS_VOISINES_LAISSEES_SILENCIEUSES =
aucune taxonomie nouvelle, aucune inférence probabiliste depuis la densité du scan,
aucune extrapolation ontologique ou philosophique, aucun verdict inter-cycle général

INFORMATIONS_MANQUANTES_BLOQUANTES =
pour toute promotion au-delà du toy model : réalisation microscopique de Gamma_phi,
traitement thermique/BBN/contraintes complet, test de bassin/robustesse et prise
empirique discriminante ; pour lancer la prochaine opération C10 :
autorisation scientifique explicite du modèle/canal à instruire

INFORMATIONS_MANQUANTES_NON_BLOQUANTES =
vérification externe fraîche des références bibliographiques et reproduction
numérique indépendante des runs historiques ; leur absence n’empêche pas de
qualifier les résultats internes comme résultats de modèles conditionnels,
mais interdit de les promouvoir en validation observationnelle actuelle

AUCUNE_MUTATION_EFFECTUEE = OUI
```
