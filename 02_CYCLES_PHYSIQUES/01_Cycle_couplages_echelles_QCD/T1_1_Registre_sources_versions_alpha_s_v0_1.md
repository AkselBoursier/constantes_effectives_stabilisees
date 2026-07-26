# T1.1 — Registre des sources et versions pour les déterminations de `alpha_s` v0.1

## 0. Statut

```text
statut : verrouillage bibliographique du premier lot T1 ;
date de contrôle : 21 juillet 2026 ;
branche : agent/cycle-1-qcd-t1 ;
fonction : fixer les autorités textuelles utilisées par les fiches d’extraction ;
ne vaut pas : validation de la méthode de chaque article, reproduction numérique,
               moyenne mondiale ou verdict de compatibilité.
```

Le registre distingue la **version de référence** — publication évaluée par les pairs
lorsqu’elle existe — et la **version de travail** — prépublication accessible, versionnée
et parfois postérieure à la publication. Une correction postérieure est conservée lorsqu’elle
modifie un signe, une formule ou un détail utile, même si elle ne change pas le résultat
numérique principal.

## 1. Règle d’autorité

Pour chaque chaîne :

```text
métadonnées et citation : version de revue ;
lecture détaillée et historique des révisions : dernière version arXiv contrôlée ;
écart entre les deux : déclaré, jamais harmonisé silencieusement ;
données ou code : dépôt explicitement fourni par les auteurs seulement ;
synthèse PDG ou FLAG : contrôle de paysage, non substitut à la chaîne primaire.
```

## 2. Chaîne tau — fonction spectrale vectorielle non étrange

### 2.1 Version de référence

Diogo Boito, Aaron Eiben, Maarten Golterman, Kim Maltman, Lucas M. Mansur et
Santiago Peris, « Strong coupling from hadronic tau-decay data including
`tau -> pi- pi0 nu_tau` from Belle », *Physical Review D* **111**, 074010 (2025),
publié le 9 avril 2025.

```text
identifiant de revue : PhysRevD.111.074010 ;
DOI : 10.1103/PhysRevD.111.074010 ;
statut : article publié et évalué par les pairs ;
rôle T1 : chaîne primaire basse énergie.
```

### 2.2 Version de travail verrouillée

```text
arXiv : 2502.08147v2 [hep-ph] ;
v1 : 12 février 2025 ;
v2 : 16 décembre 2025 ;
commentaire de version : correction du signe de C_10, sans autre changement annoncé ;
résultat abstrait inchangé : alpha_s(m_Z^2) = 0.1159(14).
```

La v2 est postérieure à la publication. Elle sert donc de texte de travail pour la
correction déclarée du signe de `C_10`, sans être interprétée comme une nouvelle analyse
ou une nouvelle valeur de `alpha_s`.

## 3. Chaîne PDF globale — ajustement simultané de `alpha_s` et des distributions partoniques

### 3.1 Version de référence

NNPDF Collaboration, « A determination of `alpha_s(m_Z)` at
`aN3LO_QCD x NLO_QED` accuracy from a global PDF analysis », *European Physical
Journal C* **85**, article 1001 (2025), publié le 16 septembre 2025.

```text
DOI : 10.1140/epjc/s10052-025-14676-y ;
statut : article publié, ouvert et évalué par les pairs ;
rôle T1 : chaîne primaire d’ajustement global multi-processus.
```

### 3.2 Version de travail verrouillée

```text
arXiv : 2506.13871v2 [hep-ph] ;
v1 : 16 juin 2025 ;
v2 : 9 septembre 2025 ;
commentaire de version : version finale destinée à l’EPJC, ajouts de contrôles sans
                         positivité et clarifications ;
résultat principal : alpha_s(m_Z) = 0.1194^{+0.0007}_{-0.0014}.
```

Le texte publié constitue l’autorité. La v2 sert à suivre l’historique des contrôles de
biais, des méthodes CRM et TCM et des modifications intervenues avant publication.

## 4. Chaîne formes d’événements — annihilation électron-positron

### 4.1 Version de référence

Paolo Nason et Giulia Zanderighi, « Fits of `alpha_s` from event-shapes in the
three-jet region: extension to all energies », *Journal of High Energy Physics*
**2025**, article 200 (juin 2025), publié le 20 juin 2025.

```text
DOI : 10.1007/JHEP06(2025)200 ;
statut : article publié, ouvert et évalué par les pairs ;
rôle T1 : chaîne primaire multi-échelles avec paramètre non perturbatif conjoint.
```

### 4.2 Version de travail verrouillée

```text
arXiv : 2501.18173v1 [hep-ph] ;
date : 30 janvier 2025 ;
aucune révision arXiv ultérieure contrôlée au 21 juillet 2026 ;
résultat principal : alpha_s(M_Z) = 0.1181
                       ^{+0.0002+0.0018}_{-0.0005-0.0021}.
```

La publication JHEP prime sur la v1 pour les métadonnées et le texte final. La v1 reste
utile pour la traçabilité de la soumission initiale.

## 5. Contrôles de paysage

### 5.1 Particle Data Group

Particle Data Group, « Quantum Chromodynamics », *Review of Particle Physics 2025*,
section 9, dans S. Navas et al., *Physical Review D* **110**, 030001 (2024) et mise à
jour 2025.

```text
rang : synthèse de paysage ;
usage : conventions, running, raccordements, familles de déterminations et moyenne
        de contexte ;
interdit : traiter la moyenne comme cible d’ajustement ou comme chaîne primaire.
```

### 5.2 FLAG Review 2024

Flavour Lattice Averaging Group, « FLAG Review 2024 », arXiv:2411.04268.

```text
rang : synthèse lattice composite ;
usage : cartographier les familles admissibles et sélectionner une chaîne primaire ;
interdit : traiter l’estimation agrégée comme une extraction individuelle.
```

## 6. État de T1.1

```text
source tau : verrouillée ;
source PDF globale : verrouillée ;
source formes d’événements : verrouillée ;
contrôle PDG : verrouillé comme synthèse ;
contrôle FLAG : verrouillé comme synthèse ;
prochaine opération : produire les trois fiches primaires T1.2 ;
point ouvert : choisir ensuite une détermination lattice primaire distincte pour T1.3.
```

Aucune divergence bibliographique ne bloque T1.2. Le seul écart de version notable est
la correction post-publication du signe de `C_10` dans arXiv:2502.08147v2 ; elle doit
être signalée dans la fiche tau mais ne modifie pas la valeur finale annoncée.