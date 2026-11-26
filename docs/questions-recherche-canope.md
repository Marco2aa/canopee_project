# Questions de recherche – Réseau Canopé

**Problématique :** comment concevoir un kit de robotique à faible coût, robuste et transportable pour les écoles de Corse ?

**Reformulation :** le kit doit permettre aux enseignants de proposer des activités de découverte de la robotique, même sans laboratoire spécialisé ni budget important.

Ce document découpe la problématique en questions précises à poser au Réseau Canopé (ateliers Canopé de Corse, médiateurs numériques, conseillers pédagogiques). Chaque thème contient :

- **la question centrale** ;
- **les questions à poser à Canopé** : ce que seuls les enseignants et les médiateurs peuvent nous dire, à partir de leur expérience du terrain ;
- **ce qu'on cherchera nous-mêmes** : les informations qu'on trouvera pendant la veille (étapes 2 et 3) ;
- **les enjeux concernés** parmi les cinq : Coût, Robustesse, Transport, Pédagogie, Autonomie.

---

## Vue d'ensemble

| Thème | Question centrale | Enjeux concernés |
|---|---|---|
| Électronique | Quels composants choisir ? | Coût, Robustesse, Autonomie |
| Programmation | Quel langage utiliser ? | Pédagogie, Autonomie |
| Structure | Quel matériau résiste le mieux ? | Robustesse, Coût, Transport |
| Transport | Quelle forme de rangement adopter ? | Transport, Robustesse |
| Énergie | Batterie rechargeable ou piles ? | Coût, Autonomie, Transport |
| Utilisation | Combien d'élèves peuvent utiliser un kit ? | Pédagogie, Coût |
| Budget | Quel coût maximal viser ? | Coût |
| Pédagogie | Quels exercices proposer aux élèves ? | Pédagogie, Autonomie |

---

## 0. Questions générales sur le contexte (étape 1 : comprendre le besoin)

À poser en premier, parce que les réponses conditionnent tous les autres thèmes.

1. Quels niveaux faut-il viser en priorité : maternelle, cycle 2 (CP-CE2), cycle 3 (CM1-6e) ou cycle 4 (collège) ?
2. Combien d'écoles corses ont déjà du matériel de robotique ? Lequel, et est-il réellement utilisé ?
3. Qu'est-ce qui empêche aujourd'hui les enseignants de faire de la robotique : le manque de matériel, de temps, de formation ou de confiance ?
4. Les ateliers Canopé de Corse prêtent-ils déjà des kits ou des mallettes ? Comment se passent le prêt, la réservation et le retour ?
5. Quelles remarques reviennent le plus souvent quand un enseignant rend un kit emprunté (pièces perdues, matériel cassé, notice peu claire…) ?
6. Combien d'écoles sont des petites écoles rurales ou de montagne, avec des classes multi-niveaux ou à classe unique ?
7. Les écoles ont-elles toutes un accès Internet fiable, et de quel équipement disposent-elles (tablettes, ordinateurs, TNI) ?

---

## 1. Électronique : quels composants choisir ?

**Questions à poser à Canopé**

1. Quelles cartes ou quels robots avez-vous déjà vus en classe (micro:bit, Arduino, Thymio, mBot, Bee-Bot…) ? Lesquels ont bien marché et lesquels ont posé problème ?
2. Quelles pannes reviennent le plus souvent : câbles arrachés, connecteurs abîmés, capteurs cassés, moteurs bloqués ?
3. Les enseignants acceptent-ils de brancher des fils eux-mêmes ou faut-il du « tout prêt » (connecteurs détrompés, aucune soudure) ?
4. Quels capteurs sont les plus utiles pédagogiquement : distance, suivi de ligne, lumière, son, boutons ?
5. Le matériel doit-il respecter une norme ou une liste de référence de l'Éducation nationale (marquage CE, sécurité des jouets pour les plus jeunes) ?

**Ce qu'on cherchera nous-mêmes**

- Un comparatif de cartes : micro:bit, Arduino Uno/Nano, ESP32, Raspberry Pi Pico (prix, simplicité, robustesse, disponibilité).
- Les moteurs : moteurs à courant continu avec réducteur (« moteurs jaunes ») ou servomoteurs à rotation continue.
- La connectique sans soudure : Grove, JST, borniers.
- Les fournisseurs et les délais de livraison vers la Corse.

---

## 2. Programmation : quel langage utiliser ?

**Questions à poser à Canopé**

1. Quels outils les enseignants connaissent-ils déjà : Scratch, ScratchJr, Vittascience, MakeCode, Blockly, Python ?
2. Faut-il prévoir une programmation **sans écran** (cartes, boutons sur le robot) pour la maternelle et le cycle 2 ?
3. Les postes des écoles permettent-ils d'installer des logiciels, ou faut-il une solution 100 % navigateur web ?
4. Sur quels appareils les élèves programment-ils le plus souvent : tablettes ou ordinateurs ?
5. Faut-il pouvoir passer des blocs au texte (Python) pour assurer la continuité avec le collège ?
6. Y a-t-il des contraintes RGPD sur les plateformes en ligne : comptes élèves, données hébergées hors de France ?

**Ce qu'on cherchera nous-mêmes**

- La liste des environnements gratuits compatibles avec chaque carte.
- Le fonctionnement hors ligne de chaque outil, car certaines écoles ont une connexion faible.
- Les programmes officiels de cycles 2, 3 et 4 sur l'algorithmique et la programmation.

---

## 3. Structure : quel matériau résiste le mieux ?

**Questions à poser à Canopé**

1. Quels chocs le matériel subit-il réellement : chutes de table, élèves qui marchent dessus, transport en voiture ?
2. Les écoles ou les ateliers Canopé ont-ils accès à une imprimante 3D ou à une découpeuse laser (FabLab, collège voisin) pour réparer ou refabriquer des pièces ?
3. Les élèves doivent-ils **monter eux-mêmes** le robot (et donc le démonter souvent) ou le recevoir déjà assemblé ?
4. Y a-t-il des matériaux à éviter pour des raisons de sécurité (arêtes coupantes, petites pièces pour les moins de 3 ans) ?

**Ce qu'on cherchera nous-mêmes**

- Un comparatif de matériaux : PLA, PETG, ABS (impression 3D), contreplaqué ou MDF (découpe laser), plaque PVC, carton renforcé, briques compatibles LEGO.
- Les critères à comparer : résistance aux chocs, poids, prix, facilité de fabrication et de réparation locale.
- Les solutions de protection : carter fermé, pare-chocs souple, électronique fixée sur des entretoises.

---

## 4. Transport : quelle forme de rangement adopter ?

**Questions à poser à Canopé**

1. Comment le kit circulera-t-il entre les établissements : navette Canopé, voiture de l'enseignant, conseiller pédagogique, La Poste ?
2. Quel poids maximal une personne seule peut-elle porter facilement, par exemple dans un escalier ou depuis un parking éloigné ?
3. Préférez-vous une grande mallette pour toute la classe ou plusieurs petites boîtes, une par groupe ?
4. Comment vérifiez-vous au retour qu'il ne manque rien : inventaire, photos, emplacements découpés dans la mousse ?
5. Les kits risquent-ils d'être stockés dans des conditions difficiles : chaleur dans une voiture l'été, humidité, sel en bord de mer ?

**Ce qu'on cherchera nous-mêmes**

- Les types de contenants : mallette à outils, valise rigide étanche, caisse empilable, sac à dos.
- Les mousses de calage prédécoupées et les étiquettes d'inventaire.
- Les dimensions compatibles avec un coffre de voiture et les tarifs postaux.

---

## 5. Énergie : batterie rechargeable ou piles ?

**Questions à poser à Canopé**

1. Les écoles ont-elles assez de prises pour recharger plusieurs robots en même temps ?
2. Qui gérerait la recharge entre deux séances : l'enseignant, l'atelier Canopé ?
3. Les batteries lithium posent-elles un problème de sécurité ou de transport selon vos règles internes ?
4. Les enseignants préfèrent-ils des piles AA (simples, achetées partout) malgré leur coût et les déchets ?
5. Combien de temps dure une séance, et donc combien d'autonomie faut-il au minimum ?

**Ce qu'on cherchera nous-mêmes**

- Une comparaison entre piles AA alcalines, accus NiMH rechargeables, batterie Li-ion 18650 et batterie externe USB : coût sur 3 ans, autonomie, sécurité, poids.
- La possibilité d'une recharge par USB, qui évite d'acheter un chargeur spécifique.

---

## 6. Utilisation : combien d'élèves peuvent utiliser un kit ?

**Questions à poser à Canopé**

1. Combien d'élèves y a-t-il par groupe de travail dans vos ateliers : 2, 3 ou 4 ?
2. Combien de robots faut-il pour une classe entière, sachant qu'une classe compte souvent 20 à 28 élèves mais que les petites écoles en ont moins ?
3. Combien de séances un enseignant enchaîne-t-il avec un kit emprunté, et pendant combien de semaines le garde-t-il ?
4. Le kit doit-il fonctionner avec un seul adulte dans la salle ?

**Ce qu'on cherchera nous-mêmes**

- Ce que dit la recherche sur la taille idéale des groupes en robotique éducative.
- Le calcul du nombre de robots par kit selon les scénarios (classe entière ou demi-groupe).

---

## 7. Budget : quel coût maximal viser ?

**Questions à poser à Canopé**

1. Quel budget une école ou une commune peut-elle consacrer à ce type de matériel ?
2. Qui finance habituellement : la commune, la collectivité de Corse, un appel à projets, Canopé ?
3. Vaut-il mieux un kit acheté par chaque école ou un kit mutualisé et prêté par Canopé ?
4. À partir de quel prix par robot le projet devient-il intéressant par rapport aux robots du commerce ?
5. Faut-il prévoir un budget de pièces de rechange et d'entretien chaque année ?

**Ce qu'on cherchera nous-mêmes**

- Les prix des robots éducatifs du commerce, qui serviront de référence.
- Le coût détaillé d'un robot fait maison : composants, structure, batterie et part de la mallette.
- Les économies possibles : achat groupé, composants génériques, fabrication locale.

---

## 8. Pédagogie : quels exercices proposer aux élèves ?

**Questions à poser à Canopé**

1. Quelles compétences des programmes les enseignants doivent-ils travailler en priorité : se repérer dans l'espace, écrire un algorithme, utiliser des boucles et des conditions ?
2. Quelles ressources pédagogiques Canopé propose-t-il déjà en robotique : fiches, vidéos, formations ?
3. Quel format de guide les enseignants préfèrent-ils : fiche papier dans la mallette, QR code vers une vidéo, site web ?
4. Comment former rapidement un enseignant débutant : en 1 h, en 3 h, par une animation en classe ?
5. Peut-on relier les activités à la Corse (carte de l'île, parcours de randonnée comme le GR20, langue corse) pour motiver les élèves ?
6. Faut-il prévoir une évaluation des élèves (grille de compétences, défis à valider) ?

**Ce qu'on cherchera nous-mêmes**

- Une progression d'exercices, du plus simple au plus avancé : avancer et tourner, suivre un parcours, éviter un obstacle, suivre une ligne, réaliser un défi en équipe.
- Les tapis et les parcours imprimables à glisser dans la mallette.
- Des exemples de séquences déjà publiées : Éduscol, Canopé, Fondation La main à la pâte.

---

## Après les réponses de Canopé

Les réponses serviront à :

1. **rédiger le cahier des charges** : budget maximal, poids maximal, nombre de robots, niveau visé ;
2. **construire la grille de comparaison** de l'étape 5, avec cinq critères (prix, solidité, poids, facilité d'utilisation, pédagogie) pondérés selon ce que Canopé juge le plus important ;
3. **orienter la veille** des étapes 2 et 3 sur les solutions qui respectent ces contraintes.
