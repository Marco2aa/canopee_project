# Veille – Énergie, matériaux et programmation

**Thèmes :** Énergie (thème 5), Structure (thème 3) et Programmation (thème 2) du [document de questions](questions-recherche-canope.md).

**Date du relevé :** novembre 2026. Les valeurs techniques varient selon les fabricants : ce sont des **ordres de grandeur, à vérifier** sur les fiches des produits achetés.

---

## 1. Énergie : piles, accus ou batterie lithium ?

### Ce que demandent les composants

| Composant | Tension utile | Remarque |
|---|---|---|
| Moteur TT | 3 à 6 V | environ 200 tr/min à 6 V, mais seulement 90 tr/min à 3 V ; le couple diminue aussi |
| Servo SG90 | ≈ 4,8 à 6 V | valeur courante des fiches, à vérifier sur le modèle acheté |
| micro:bit V2 | ≈ 3 V | en général alimenté par la carte d'extension, qui abaisse la tension |

### Les solutions comparées

| Solution | Tension (4 éléments) | Avantages | Inconvénients | Pour le kit |
|---|---|---|---|---|
| **Piles AA alcalines** | ≈ 6 V (6,4 V neuves) | partout, pas cher à l'achat, rien à recharger | déchets, coût sur la durée ; la tension baisse au fil de l'usure, donc le robot ralentit | en dépannage |
| **Accus AA NiMH** | ≈ 4,8 V | rechargeables des centaines de fois ; tension plus stable ; même boîtier que les piles | robot un peu plus lent (4,8 V au lieu de 6 V) ; il faut un chargeur et quelqu'un pour recharger | **recommandé** |
| **Batterie Li-ion 18650** | ≈ 3,7 V par élément | légère, beaucoup d'énergie | chargeur et circuit de protection spécifiques ; risque d'incendie si elle est abîmée ; règles d'envoi postal strictes | à éviter pour des élèves |
| **Batterie externe USB** | 5 V | rechargeable sur n'importe quel chargeur USB | lithium aussi ; plus lourde ; certaines se coupent quand la consommation est faible | possible, mais peu adaptée aux moteurs |

### Ce qu'on retient

- **Les accus NiMH sont le meilleur compromis** pour l'école : rechargeables, même format que les piles, sans les contraintes du lithium. C'est l'option chiffrée dans le [kit de classe](chiffrage-kit-classe.md).
- **Le passage des piles aux accus change la vitesse du robot** (4,8 V au lieu de 6 V). Il faudra **refaire le calibrage** (voir le [programme de calibrage](../programmes/README.md)). Mieux vaut choisir une seule solution par kit.
- **Le lithium complique le transport.** La Poste limite les batteries lithium-ion à 20 Wh par élément et 100 Wh par batterie, et Colissimo limite leur nombre par colis. Un kit voyageant par la poste a donc intérêt à ne pas en contenir.
- **À vérifier :** des piles alcalines neuves donnent environ 6,4 V, un peu au-dessus des 6 V du servo. Cela dépend de la façon dont la carte d'extension alimente le servo.

---

## 2. Matériaux : quel plastique imprimer ?

### Le problème de la chaleur

Le kit circulera **en voiture**, entre les écoles. En été en Corse, l'intérieur d'une voiture garée au soleil peut dépasser 50 à 60 °C.

| Matériau | Ramollissement | Résistance aux chocs | Facilité d'impression | Pour Tartaruga |
|---|---|---|---|---|
| **PLA** | commence vers **50 à 60 °C** | rigide mais cassant | très facile | ⚠️ risque de **déformation dans une voiture chaude** |
| **PETG** | vers **70 à 80 °C** | plus souple, moins cassant | facile (un peu plus de fils et de bavures) | **recommandé** |
| **ABS / ASA** | vers 90 à 100 °C | bonne | plus difficile : déformations, odeurs, imprimante fermée conseillée | trop contraignant pour une école ou un FabLab |

### Ce qu'on retient

- **Il vaut mieux imprimer Tartaruga en PETG**, surtout le châssis et la carapace. C'est un changement par rapport au README actuel, qui conseille le PLA ou le PETG sans les départager.
- Le PETG reste limite au-delà de 70 à 75 °C : **il ne faut pas laisser la mallette sur une plage arrière en plein soleil.** À écrire sur la fiche de la mallette.
- Les pièces de Tartaruga ont été dessinées sans supports, avec des pentes de 50° au plus : elles devraient aussi s'imprimer en PETG. **À confirmer** sur le premier prototype, en particulier le jeu de 0,4 mm entre les pièces.
- Le **PLA** reste bien adapté aux pièces **imprimées par les élèves** (couvercles personnalisés) : plus facile à imprimer, et un couvercle déformé coûte peu à refaire.

---

## 3. Programmation : quel éditeur choisir ?

Contrainte retenue : des blocs de style Scratch, du CM2 à la 5e (voir la [veille sur les cartes](veille-cartes-electroniques.md)).

| Éditeur | Blocs → texte | Sans Internet | Installation | Données des élèves | Pour le kit |
|---|---|---|---|---|---|
| **MakeCode** (Microsoft) | blocs, JavaScript, Python | **oui** : application Windows hors ligne (Microsoft Store), ou éditeur web gardé en cache | aucune en ligne ; application facultative | pas de compte nécessaire | **éditeur principal** |
| **Vittascience** (éditeur français) | blocs → Python | non confirmé | aucune (navigateur) | hébergement en Europe (OVH) d'après une présentation tierce ; accessible par le **GAR** | **alternative**, utile pour aller vers Python au collège |
| **Scratch 3** + extension micro:bit | blocs | non (extension) | *Scratch Link* à installer | — | ❌ le robot reste relié au PC et l'extension ne pilote pas les moteurs |
| **Éditeur Python micro:bit** | Python seulement | non vérifié | aucune | — | pour la 4e-3e, au-delà du public visé |

### Ce qu'on retient

- **MakeCode est le meilleur choix d'éditeur principal**, parce qu'il **fonctionne sans Internet**. C'est important pour les écoles de montagne à la connexion faible (question 0.7). Le [programme de calibrage](../programmes/calibrage.ts) est d'ailleurs écrit pour MakeCode.
- **Vittascience est un bon complément** : éditeur français, accessible par le GAR, avec un passage des blocs à Python. Il faudra vérifier qu'il prend en charge la carte d'extension choisie.
- **Dans tous les cas, vérifier que la carte d'extension a une extension MakeCode.** Sinon, il faudra garder l'approche « broches » du programme de calibrage, moins simple pour les enseignants.
- **Données personnelles :** la CNIL demande d'informer les élèves et leurs parents des outils en ligne utilisés. MakeCode s'utilise sans compte, ce qui simplifie les choses. Le DPD académique pourra confirmer.

---

## 4. Synthèse des choix proposés

| Thème | Choix proposé | À confirmer |
|---|---|---|
| Énergie | **4 accus AA NiMH**, chargeurs dans la mallette, piles alcalines en dépannage | autonomie réelle (test du prototype), tension du servo |
| Matériau | **PETG** pour le châssis, la carapace et les pièces mécaniques ; PLA pour les couvercles des élèves | impression et jeu des pièces en PETG |
| Éditeur | **MakeCode** (avec l'application hors ligne), **Vittascience** en complément | extension MakeCode de la carte d'extension choisie |

---

## 5. Questions à ajouter pour Canopé

- Les écoles peuvent-elles installer l'**application MakeCode hors ligne** sur leurs postes, ou faut-il rester dans le navigateur ?
- Les enseignants utilisent-ils déjà **Vittascience** par le GAR ?
- Où le kit sera-t-il stocké entre deux prêts, et risque-t-il de rester dans une **voiture chaude** ?
- Qui rechargera les accus entre deux séances ?

---

## Sources

**Énergie**
- Moteur TT : [fiche SunFounder](https://docs.sunfounder.com/projects/3in1-kit-v2/fr/latest/components/component_tt_motor.html)
- micro:bit et piles : [FAQ micro:bit (CATEDU)](https://libros.catedu.es/books/escuela-40-bbc-microbit-en-el-aula/page/preguntas-frecuentes-sobre-microbit/export/pdf)
- Batteries pour la robotique : [ENSTA Bretagne](https://www.ensta-bretagne.fr/lebars/robots_batteries.pdf), [Didel – sources d'énergie](https://www.didel.com/profsTM/SourcesEnergie.pdf)
- Piles ou accus : [Test-Achats](https://www.test-achats.be/hightech/piles/dossier/piles-rechargeables-ou-a-usage-unique)
- Envoi de batteries lithium : [La Poste](https://www.laposte.fr/conseils-pratiques/marchandises-dangereuses-interdites), [Colissimo](https://www.colissimo.entreprise.laposte.fr/en/practical-advice/right-packaging/almost-perfect-parcel-web-series/lithium-batteries), [notice du ministère de la Transition écologique](https://www.ecologie.gouv.fr/sites/default/files/notice_information_piles_batteries_lithium.pdf)

**Matériaux**
- [Guide des matériaux Prusa](https://help.prusa3d.com/fr/filament-material-guide)
- [PLA ou PETG (Slice-Lab)](https://slice-lab.com/fr/guide-pla-vs-petg)
- [Résistance du PETG à la température (JLC3DP)](https://jlc3dp.com/fr/blog/petg-temperature-resistance)
- [Données techniques Polymaker](https://wiki.polymaker.com/polymaker-wiki-fr/produits-polymaker/filaments-polymaker/donnees-techniques-en-un-coup-doeil)

**Programmation**
- MakeCode hors ligne : [MakeCode](https://makecode.microbit.org/offline), [microbit.org](https://microbit.org/get-started/user-guide/offline/), [fin de l'ancienne application Windows](https://makecode.microbit.org/windows-app)
- Vittascience : [présentation (PromptFacile)](https://promptfacile.fr/outils/vittascience)
- Données des élèves : [CNIL – outils collaboratifs](https://cnil.fr/fr/enseignement-bonnes-pratiques-outils-collaboratifs)
