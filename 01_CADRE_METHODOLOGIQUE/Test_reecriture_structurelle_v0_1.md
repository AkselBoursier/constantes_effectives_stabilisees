# Test de la reecriture structurelle v0.1

## Mise a l'epreuve de la regle v0.2 sur trois genres difficiles

### 1. Fonction

Ce test decide si la regle structurelle de la v0.2 peut etre deployee
sur tout le corpus.

```text
appui : 01_CADRE_METHODOLOGIQUE/Reecriture_positive_vocabulaire_v0_2.md
objet : la regle structurelle (sections, titres, listes de discipline)
methode : reecriture sur copies, jamais en place ;
criteres et conditions d'echec fixes avant la reecriture ;
le test peut echouer, et un echec est un resultat.
```

### 2. Choix des objets

Trois genres, choisis parce que chacun fait travailler la regle la ou
elle risque le plus :

| Copie | Document source | Genre | Ce que le genre teste |
|---|---|---|---|
| A | `05_CARTES_ET_SYNTHESES/Fiche_limites_non_theses_v0_1.md` | Garde-fou : document negatif par fonction | La force prophylactique survit-elle a la positivisation du cadre ? |
| B | `04_ARCHITECTURES_INTER_FAMILLES/Architecture_cosmologique_stress_test_v0_1.md` (extraits 2, 4, 13, 16) | Protocole eliminatoire | La logique falsificatrice reste-t-elle lisible ? un test rate reste-t-il un resultat ? |
| C | `01_CADRE_METHODOLOGIQUE/Note_synthese_methodologique_v1_3_pre_familial_et_temporalite.md` (extraits 7, 12, 16) | Reference dense | Le cout de longueur reste-t-il acceptable sur un texte charge ? |

Portee des copies :

```text
copie A : document integral (genre le plus dur, mesure complete) ;
copies B et C : extraits cibles sur les sections porteuses de
structures negatives ; le test porte sur les structures, la mesure
d'extraits suffit.
```

Quatrieme genre identifie, a tester lors du deploiement :

```text
preuve locale a borne (exemple : fiche masse absolue des neutrinos) ;
genre distinct parce que la negation y est un resultat physique
(absence de detection). L'exception 2 de la v0.2 devrait le couvrir ;
le deploiement du cercle 3 le verifiera.
```

### 3. Criteres fixes avant reecriture

| Critere | Question | Mesure |
|---|---|---|
| C1 Conservation | Chaque garde-fou, chaque interdit, chaque limite du texte source se retrouve-t-il integralement dans la copie ? | Controle item par item |
| C2 Force prophylactique | La mauvaise lecture que le texte source bloquait reste-t-elle bloquee pour un lecteur presse ou hostile ? | Lecture adverse simulee sur les enonces cles |
| C3 Lisibilite de l'echec | Dans un protocole eliminatoire, une sortie negative ("non confirme", "test rate") reste-t-elle nommable et visible comme resultat ? | Controle des sorties de test |
| C4 Cout de longueur | La copie reste-t-elle d'une longueur comparable a la source ? | Comparaison approximative par section |

### 4. Conditions d'echec declarees avant reecriture

```text
E1 : un garde-fou du texte source manque ou s'affaiblit dans la copie
     (violation de C1 ou C2) -> echec du test sur ce genre ;
E2 : une sortie negative de protocole devient invisible ou euphemisee
     (violation de C3) -> echec sur le genre eliminatoire ;
E3 : la copie excede nettement la source (plus d'un quart de longueur
     ajoutee) sans gain de clarte (violation de C4) -> echec de cout ;
E4 : la reecriture exige de multiplier les exceptions au point que la
     regle ne gouverne plus que des cas triviaux -> echec de la regle
     elle-meme.
```

Sorties possibles du test :

```text
deploiement autorise ;
deploiement autorise avec clarification (v0.3 mineure) ;
exceptions elargies (v0.3 substantielle) ;
regle limitee aux nouveaux documents (echec partiel) ;
abandon de la regle structurelle (echec complet).
```

### 5. Emplacement des copies

```text
01_CADRE_METHODOLOGIQUE/Test_reecriture_structurelle/Copie_test_A_Fiche_limites.md
01_CADRE_METHODOLOGIQUE/Test_reecriture_structurelle/Copie_test_B_Stress_test_extraits.md
01_CADRE_METHODOLOGIQUE/Test_reecriture_structurelle/Copie_test_C_Note_v1_3_extraits.md
```

Les documents sources restent inchanges.

### 6. Resultats

#### 6.1 Copie A : genre garde-fou

```text
C1 : tenu. Les treize non-theses, les sept risques, les limites par
architecture et les six conditions de seuil sont integralement
presents.

C2 : tenu, avec un constat structurant : la force prophylactique est
portee par les exceptions controlees, non par la reecriture. La table
des non-theses (exception 1) et les contre-exemples de formulation
(exception 3) restent negatifs, et doivent le rester : "le projet ne
fournit pas une nouvelle theorie physique" bloque une lecture hostile
plus surement que toute paraphrase positive.

C4 : tenu, longueur equivalente.

constat principal : dans un genre negatif par fonction, la regle
opere par mise en cage, non par elimination. Elle positive le cadre
(titres, transitions, principe de lecture) et laisse le contenu
negatif dans ses conteneurs sanctionnes. Le gain est reel mais il est
un gain de cadrage : le document dit desormais d'abord ce qu'il
autorise, et garde ses refus a leur rang.
```

#### 6.2 Copie B : genre protocole eliminatoire

```text
C1 : tenu.

C3 : tenu, avec une clarification necessaire : les sorties negatives
du stress test ("regime d'acces non unique", "sous-architecture non
confirmee") sont des resultats factuels et relevent de l'exception 2.
La v0.2 formule cette exception pour les faits physiques (bornes,
chronologies) ; elle doit couvrir explicitement les sorties de
protocoles eliminatoires. Sans cette clarification, un reecrivain
zele pourrait euphemiser un "non confirme" en "reste a confirmer",
ce qui changerait le resultat.

C4 : tenu ; plusieurs passages raccourcissent.

constat principal : le genre eliminatoire survit bien parce que ses
negations sont majoritairement des resultats, non des cadres. La
regle amelioree les sections d'encadrement ("elle ne doit pas etre"
devient un enonce de rang avec lectures ecartees par le test) sans
toucher a la logique falsificatrice.
```

#### 6.3 Copie C : genre reference dense

```text
C1 : tenu.

C4 : gain net. Sur les trois sections testees, la reecriture
raccourcit ou egalise : "Interdit : classer une grandeur par liaison
seulement parce que..." devient "le classement par liaison requiert
le test de non-reduction passe ; la forme logique seule reste au
rang 0", plus court et sans ambiguite de portee.

constat principal : c'est le genre ou la regle rapporte le plus.
Dans un texte dense, la negation cumule ses ambiguites de portee ;
la prescription positive les dissout et raccourcit.
```

#### 6.4 Tableau de verdict

| Critere | A (garde-fou) | B (eliminatoire) | C (reference dense) |
|---|---|---|---|
| C1 Conservation | Tenu | Tenu | Tenu |
| C2 Prophylaxie | Tenu par exceptions | Sans objet | Sans objet |
| C3 Echec lisible | Sans objet | Tenu avec clarification | Sans objet |
| C4 Cout | Neutre | Neutre a favorable | Favorable |
| Condition d'echec declenchee | Aucune | Aucune (E2 evitee par clarification) | Aucune |

### 7. Verdict et suite

Verdict :

```text
deploiement autorise avec clarification (v0.3 mineure).
```

Contenu de la clarification v0.3 :

```text
1. etendre explicitement l'exception 2 aux sorties de protocoles
   eliminatoires : "non confirme", "test rate", "regime non unique"
   sont des resultats et se disent tels quels ;
2. consigner le constat de mise en cage : dans les genres negatifs
   par fonction, la regle positive le cadre et conserve le contenu
   negatif dans ses conteneurs ; c'est son mode d'action normal, et
   la proportion de contenu negatif d'un garde-fou reste un choix de
   genre, pas un defaut de reecriture ;
3. rappeler la garde contre l'euphemisation : la reecriture positive
   renforce les refus en les mettant a leur rang ; toute reecriture
   qui les affaiblit viole C2 et se corrige.
```

Ordre de deploiement propose (apres validation de la v0.3) :

```text
cercle 1 : methode active et references (traitement dedie) ;
cercle 2 : cartes, syntheses, fiches d'horizon ;
cercle 3 : architectures et cycles, a leur prochaine reprise
(y compris le quatrieme genre, preuve locale a borne) ;
cercle 4 : archives, conservees avec leur statut.
```

### 8. Formule de cloture

```text
Le test confirme et precise : la regle structurelle gouverne les
cadres, les exceptions gardent les contenus. Un corpus positif
n'est pas un corpus qui refuse de dire non ; c'est un corpus ou
chaque non tient un rang que le texte a d'abord affirme.
```
