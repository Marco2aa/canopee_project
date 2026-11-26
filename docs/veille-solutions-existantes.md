# Veille – Les solutions qui existent déjà

**Objectif :** savoir ce qui existe déjà en robotique éducative (robots du commerce, projets libres, actions en Corse), pour situer notre projet Tartaruga et éviter de refaire ce qui existe.

**Étapes concernées :** 2 (recherches) et 3 (document de veille).

**Date du relevé :** novembre 2026. Les prix viennent de revendeurs en ligne, souvent sans date et parfois dans d'autres monnaies : ce sont des **ordres de grandeur, à revérifier** avant de s'en servir dans la grille de comparaison.

---

## 1. Les robots éducatifs du commerce

| Robot | Public visé | Programmation | Prix indicatif | Points forts | Points faibles |
|---|---|---|---|---|---|
| **Blue-Bot** (TTS) | maternelle, cycle 2 | boutons sur le robot, tablette, cartes | ≈ 117 à 140 € pièce ; ≈ 880 € le pack de 6 avec station | très simple, sans écran, robuste, déjà connu des écoles | trop limité pour le CM2 et la 5e (pas de capteurs, pas de vraie programmation par blocs) |
| **Thymio II** (Mobsya, EPFL) | du primaire au lycée | VPL (blocs visuels), Scratch, Python | ≈ 100 € à son lancement, prix actuel non trouvé | très répandu dans les écoles suisses et françaises, nombreux capteurs | prix plus élevé, coque fermée qu'on ne peut pas réparer soi-même |
| **mBot / mBot2** (Makeblock) | cycle 3, collège | mBlock (basé sur Scratch), Python | mBot ≈ 96 € (prix de 2018) ; mBot2 ≈ 155 € | proche de Scratch, **déjà utilisé en Corse** (Digi Botti) | logiciel ou pilote à installer, prix du mBot2 |
| **Maqueen Plus V3** (DFRobot) | cycle 3, collège | MakeCode, Python (micro:bit) | ≈ 70 $ **sans micro:bit ni piles** | basé sur micro:bit, nombreux capteurs | micro:bit en plus, châssis du commerce non réparable |
| **Cutebot Pro** (ELECFREAKS) | cycle 3, collège | MakeCode, Python (micro:bit) | ≈ 50 $ sans micro:bit ; ≈ 72 $ avec | basé sur micro:bit, compact, moins cher | piles non fournies, châssis du commerce non réparable |

**Ce qu'on retient :**
- Les robots les plus simples (Blue-Bot) s'adressent aux plus jeunes. Pour le CM2 et la 5e, ce sont plutôt **mBot, Thymio ou les robots micro:bit** qui conviennent.
- Les robots micro:bit du commerce (Maqueen, Cutebot) coûtent environ **70 € une fois le micro:bit ajouté**. C'est assez proche de la version « de marque » de Tartaruga (≈ 60 € avec le lève-stylo) : **l'avantage de prix de Tartaruga est réel mais modeste** face à eux. Il est beaucoup plus net face au Blue-Bot, au Thymio ou au mBot2.
- Aucun de ces robots ne se **répare en imprimant une pièce** : une coque cassée oblige à racheter la pièce chez le fabricant, ou le robot entier.

---

## 2. Les projets libres et imprimables : les « tortues qui dessinent »

L'idée d'un robot qui trace des figures avec un feutre **n'est pas nouvelle**. Elle remonte au langage **Logo**, créé dans les années 1960, dont la « tortue » était un robot muni d'un crayon.

| Projet | Description | Intérêt pour nous |
|---|---|---|
| **Mirobot** (Ben Pirt) | Robot dessinateur libre, à monter soi-même, basé sur Arduino, présenté comme une version moderne de Logo. Financé sur Kickstarter vers 2014. | Il a inventé le principe **deux roues + feutre au centre**, celui que nous avons repris. Il ne semble plus vendu aujourd'hui. |
| **OSTR – Open Source Turtle Robot** (Ken Olsen) | Robot tortue **imprimé en 3D**, inspiré de Mirobot, certifié matériel libre par l'OSHWA, avec ses fichiers de conception publiés. | C'est le projet le plus proche du nôtre : à étudier pour comparer nos choix. |
| **Tortue de l'Université de Rochester** | Version dérivée d'OSTR, utilisée en atelier, programmable en Logo ou en CircuitPython. | Montre qu'on peut programmer la même tortue dans plusieurs langages. |
| **mDrawBot** (Makeblock) | Kit du commerce qui peut se monter en robot dessinateur, entre autres. | Autre exemple d'usage « dessin » de la robotique éducative. |

**Ce qu'on retient :**
- Ces projets utilisent surtout Arduino ou des cartes à programmer en texte. **Aucun n'est pensé pour le micro:bit et la programmation par blocs** utilisée du CM2 à la 5e.
- La plupart des tortues Logo ont un **lève-stylo** (un petit servomoteur qui lève et baisse le feutre). Cela permet de se déplacer sans tracer. **Il a été ajouté à Tartaruga** après cette veille (voir partie 5).

---

## 3. Ce qui se fait déjà en Corse

| Action | Ce qu'on en sait |
|---|---|
| **Digi Botti** (2026) | Huit écoles corses préparent des rencontres de robotique entre classes, en avril et mai 2026. Robots utilisés : **Blue-Bot, Loti-bot et mBot2**. Les ERUN et les conseillers pédagogiques numériques accompagnent les enseignants, et Canopé Corse a partagé des ressources sur le Loti-bot et le mBot2. |
| **Résidences Digi Scontri** | Des formateurs Canopé et la DRANE animent des ateliers dans les écoles primaires, notamment en robotique éducative. |
| **École Charles Andreï, Bastia** | Projet d'une année avec de petits robots programmables, mené avec la DANE de Corse et Réseau Canopé. |
| **« FabLab à l'école »** (Canopé Corse et Universcience) | Prêt aux écoles d'un kit de cinq machines de fabrication, pour concevoir, programmer et prototyper. Information tirée d'une publication de Canopé Corse sur Facebook (mai 2026), à confirmer. |
| **Prêt national de Canopé** | Le catalogue national de prêt propose des Blue-Bot et des kits de robotique. Nous n'avons pas trouvé de liste publiée du matériel prêté **en Corse**. |

**Ce qu'on retient :**
- La robotique est **déjà présente** dans les écoles corses, avec des robots du commerce. Tartaruga ne part pas de zéro : il peut **compléter** ce qui existe.
- Le **mBot2** est déjà utilisé : les enseignants connaissent donc les blocs de style Scratch. Les blocs MakeCode ou Vittascience de Tartaruga leur seront familiers.
- Le programme **« FabLab à l'école »** pourrait être une piste pour **imprimer les pièces en Corse**, si son kit comprend une imprimante 3D. À demander à Canopé.

---

## 4. Où se situe Tartaruga ?

| Critère | Blue-Bot | Thymio | mBot2 | Robot micro:bit du commerce | Tortue libre (OSTR) | **Tartaruga** |
|---|---|---|---|---|---|---|
| Prix par robot | ≈ 120-140 € | ≈ 100 € et plus | ≈ 155 € | ≈ 70 € | faible (à chiffrer) | **≈ 43 à 60 €** |
| Adapté du CM2 à la 5e | non | oui | oui | oui | moyen | **oui** |
| Blocs de style Scratch | non | oui | oui | oui | non | **oui** (MakeCode, Vittascience) |
| Aucun logiciel à installer | oui | non | non | oui | non | **oui** |
| Dessine des figures | non | non | non | non | oui | **oui** |
| Réparable en imprimant une pièce | non | non | non | non | oui | **oui** |
| Personnalisable par les élèves | coques à clipser | non | non | non | possible | **oui** (carapace aimantée, couvercle plat) |
| Lien avec la Corse | non | non | non | non | non | **oui** (tortue d'Hermann) |

**Ce qui est vraiment nouveau dans Tartaruga**, ce n'est pas chaque idée prise seule. C'est leur **combinaison** :
1. **Une tortue qui dessine, comme en Logo**, mais avec un **micro:bit programmé en blocs**, sans rien installer : cela n'existe pas dans les projets libres que nous avons trouvés.
2. **Une carapace aimantée et un couvercle plat**, que chaque classe peut redessiner et imprimer.
3. **Une fabrication et une réparation locales**, grâce à l'impression 3D.
4. **Une identité corse**, avec la tortue d'Hermann.

**À ne pas surestimer :**
- Face aux robots micro:bit du commerce, Tartaruga est **un peu moins cher**, mais l'écart n'est pas énorme. Ses vrais atouts sont la réparation, le dessin et la personnalisation, pas seulement le prix.
- Tartaruga **n'a pas encore été imprimé ni testé** : sa robustesse reste à prouver, alors que les robots du commerce ont fait leurs preuves en classe.
- Le prix de Tartaruga ne compte ni l'imprimante 3D, ni le temps de montage (environ 8 h d'impression par robot).

---

## 5. Pistes d'amélioration tirées de la veille

1. ~~Ajouter un lève-stylo~~ **Fait.** Un micro-servomoteur SG90 (environ 2 à 3 €) soulève le feutre, comme sur les tortues Logo. Voir le [README de Tartaruga](../modeles-3d/README.md).
2. **Étudier les fichiers d'OSTR** pour comparer : fixation du feutre, précision des déplacements, type de moteurs.
3. **Vérifier la précision des moteurs TT** : ils sont moins précis que des moteurs pas à pas. Une étoile peut mal se refermer. Il faudra tester, et prévoir un réglage dans le programme (calibrage des virages).
4. **Prévoir une passerelle avec le mBot2**, déjà connu en Corse : des fiches d'activités proches, pour que les enseignants s'y retrouvent.

---

## 6. Questions à ajouter pour Canopé

- Quels robots Canopé Corse prête-t-il aujourd'hui, et combien d'exemplaires ?
- Quels retours avez-vous sur le Blue-Bot, le Loti-bot et le mBot2 utilisés pendant Digi Botti ?
- Le kit « FabLab à l'école » comprend-il une imprimante 3D ? Pourrait-il servir à imprimer et réparer des pièces de Tartaruga ?
- Un robot qui dessine, qui relie la robotique à la géométrie, vous semble-t-il utile pour les enseignants ?

---

## Sources

**Robots du commerce**
- Thymio : [Wikipédia](https://en.wikipedia.org/wiki/Thymio), [EPFL – Thymio dans les écoles françaises](https://actu.epfl.ch/news/the-robot-thymio-is-finding-its-niche-in-french-sc/), [IEEE Spectrum](https://spectrum.ieee.org/automaton/robotics/diy/your-kid-wants-a-thymio-ii-education-robot)
- mBot : [catalogue allnet 2018](https://distribution.allnet.de/fileadmin/marketing/kataloge/2018/MakeB_allnetfrweb.pdf), [mBot2 sur Galaxus](https://www.galaxus.fr/fr/s1/product/makeblock-mbot2-kit-robotique-22613336)
- Maqueen Plus V3 : [Switch Science](https://www.switch-science.com/products/10544), [The Pi Hut](https://thepihut.com/collections/micro-bit-store/products/maqueen-plus-v3-advanced-matrix-laser-navigation-stem-robot-for-competitions-aa-battery)
- Cutebot Pro : [ELECFREAKS](https://elecfreaks.com/product/elecfreaks-smart-cutebot-pro-programming-robot-car-for-micro-bit), [Purdue INSPIRE](https://engineering.purdue.edu/INSPIRE/smart-cutebot-pro)
- Blue-Bot : [PcComponentes](https://www.pccomponentes.fr/robot-programmable-au-sol-tts-blue-bot), [fiche Éduscol](https://primabord.eduscol.education.fr/IMG/pdf/carte_mentale_blue-bot.pdf), [Learning Space](https://learningspace.ie/products/tts-blue-bot-bluetooth-programmable-floor-robot)

**Tortues libres**
- Mirobot : [interview de Ben Pirt (DesignSpark)](https://www.rs-online.com/designspark/an-interview-with-ben-pirt-creator-of-the-mirobot-diy-robot), [Designboom](https://www.designboom.com/technology/mirobot-drawing-robot-05-16-2015/), [test dans le Raspberry Pi Magazine](https://magazine.raspberrypi.com/articles/mirobot-review)
- OSTR : [Instructables](https://instructables.com/OSTR), [Tindie](https://www.tindie.com/products/MakersBox/open-source-turtle-robot-ostr/)
- Tortue de Rochester : [fiche d'atelier](https://www.cs.rochester.edu/~sree/ubturtle/handout2024.pdf)
- mDrawBot : [test sur RobotShop](https://community.robotshop.com/forum/t/review-makeblock-mdrawbot-mcar)

**Corse et Canopé**
- [Digi Botti (TNE 2A, avril 2026)](https://sites.ac-corse.fr/tne2a/2026/04/15/les-robots-en-classe-les-eleves-se-preparent-pour-digi-botti/)
- [Résidences Digi Scontri](https://sites.ac-corse.fr/tne2a/2024/04/19/lancement-des-residences-digi-scontri/)
- [École Charles Andreï, Bastia](https://www.ac-corse.fr/robotique-et-algorithmie-pour-les-eleves-de-l-ecole-charles-andrei-de-bastia-121802)
- [Canopé Académie de Corse (Facebook)](https://fetchrss.com/feed/1iIaFxGYM4cZ1oSZWj7bvCYd.rss)
- [Prêt de matériel – Réseau Canopé](https://www.reseau-canope.fr/index.php?id=4857)
- [Initiation à la programmation et à la robotique en cycle 3 – Réseau Canopé](https://www.reseau-canope.fr/notice/initiation-a-la-programmation-et-a-la-robotique-en-cycle-3.html)
