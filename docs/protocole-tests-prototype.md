# Protocole de test du premier prototype Tartaruga

**But :** vérifier, sur un vrai robot, ce que le modèle 3D ne peut pas prouver : que les pièces s'assemblent, que le robot dessine juste, qu'il résiste à une classe et qu'il tient une séance.

**Quand :** dès que le premier robot est imprimé et monté, puis après chaque modification importante.

**Les seuils de réussite proposés ici sont des objectifs de départ**, à ajuster avec Canopé et les enseignants.

---

## Vue d'ensemble

| N° | Test | Enjeu | Durée | Critère de réussite proposé |
|---|---|---|---|---|
| 1 | Ajustement des pièces | Robustesse | 30 min | tout s'assemble sans limer ni forcer |
| 2 | Montage par un débutant | Autonomie | 1 à 2 h | montage seul, avec la notice, en moins de 45 min |
| 3 | Précision du dessin | Pédagogie | 30 min | le carré se referme à moins de 1 cm près |
| 4 | Lève-stylo | Pédagogie | 20 min | 50 levées sans échec ; aucune trace quand le feutre est levé |
| 5 | Autonomie des piles | Autonomie, Coût | une demi-journée | au moins une séance de 1 h, idéalement 3 |
| 6 | Chutes | Robustesse | 20 min | 5 chutes de table sans casse ; au pire, la carapace se détache |
| 7 | Chaleur | Transport | une journée | aucune déformation après une journée en voiture au soleil |
| 8 | Transport en mallette | Transport | un trajet | rien de cassé ni de desserré à l'arrivée |
| 9 | Séance avec des élèves | Pédagogie | 1 h | les élèves dessinent un carré seuls ; noter les difficultés |

---

## Test 1 : ajustement des pièces

**Objectif :** vérifier les cotes et le jeu de 0,4 mm prévus dans le modèle.

**Méthode :** pour chaque assemblage, noter si ça entre **facilement**, **en forçant** ou **pas du tout**.

| Assemblage | Résultat | Remarque |
|---|---|---|
| Moteur TT dans son berceau (×2) | | |
| Feutre dans le tube (il doit coulisser librement) | | |
| Bague sur le feutre (elle doit serrer) | | |
| Servo SG90 sur son support | | |
| Aimants dans leurs logements (×12) | | |
| Carapace sur le châssis (les aimants s'alignent ?) | | |
| Couvercle sur la carapace | | |
| Vis de la carte d'extension en face des trous | | |
| Trous du bloc de piles en face de ceux du châssis | | |

**Si ça force :** augmenter le jeu dans le modèle. **Si ça flotte :** le diminuer. Noter aussi le **matériau** et l'**imprimante** utilisés.

## Test 2 : montage par un débutant

**Objectif :** savoir si un enseignant peut monter ou réparer le robot seul.

**Méthode :** donner les pièces et la notice (README de Tartaruga) à un adulte qui ne connaît pas le projet. Chronométrer et noter **chaque question posée** et **chaque erreur**.

| Étape de la notice | Temps | Questions ou erreurs |
|---|---|---|
| 1. Moteurs | | |
| 2. Piles et support du servo | | |
| 3. Servo | | |
| 4. Carte et micro:bit | | |
| 5. Aimants | | |
| 6-7. Feutre et bague | | |
| 8. Carapace et couvercle | | |
| **Total** | | |

**Après le test :** réécrire les étapes qui ont posé problème, et ajouter des photos.

## Test 3 : précision du dessin

**Objectif :** mesurer si les moteurs TT sont assez précis pour la géométrie.

**Méthode :**
1. Calibrer le robot avec le [programme de calibrage](../programmes/README.md).
2. Lui faire dessiner **10 carrés** de 15 cm de côté, sur la même feuille.
3. Pour chaque carré, mesurer l'**écart de fermeture**, c'est-à-dire la distance entre le point de départ et le point d'arrivée.
4. Recommencer avec une **étoile à 5 branches**.
5. Refaire la mesure sur une autre surface : table, sol, carton.

| Essai | Surface | Écart de fermeture (mm) | Angle mesuré au rapporteur |
|---|---|---|---|
| 1 | | | |
| … | | | |
| 10 | | | |
| **Moyenne** | | | |

**Si l'écart est trop grand :** essayer une vitesse plus faible, un patin qui frotte moins, ou des moteurs avec codeurs (plus chers).

## Test 4 : lève-stylo

**Objectif :** vérifier que le servo lève le feutre de façon fiable.

**Méthode :**
1. Mesurer la hauteur de levée au pied à coulisse, en mm.
2. Lancer un programme qui lève et baisse le feutre **50 fois**.
3. Faire avancer le robot, feutre levé : y a-t-il une trace ?
4. Vérifier que la bague n'a pas glissé sur le feutre.

| Levée (mm) | Échecs sur 50 | Trace feutre levé ? | Bague déplacée ? |
|---|---|---|---|
| | | | |

## Test 5 : autonomie des piles

**Objectif :** savoir combien de séances le robot tient, et comparer piles et accus.

**Méthode :**
1. Mettre des piles neuves ou des accus chargés.
2. Lancer un programme qui dessine des carrés en boucle, avec une pause de 5 s entre chaque, ce qui ressemble à une utilisation en classe.
3. Noter l'heure de départ, puis l'heure à laquelle **le carré ne se referme plus** (le robot ralentit) et celle à laquelle **il s'arrête**.
4. Recommencer avec l'autre type de piles.

| Alimentation | Départ | Le carré ne se referme plus | Arrêt | Durée utile |
|---|---|---|---|---|
| 4 piles alcalines | | | | |
| 4 accus NiMH | | | | |

**À retenir :** si le robot ralentit avec l'usure, il faut le **recalibrer**. Noter au bout de combien de temps.

## Test 6 : chutes

**Objectif :** vérifier que le robot survit à une chute de table, ce qui arrivera forcément en classe.

**Méthode :** laisser tomber le robot **5 fois** d'une table (environ 75 cm), sur un sol dur, dans des positions différentes : à plat, sur le côté, sur l'avant, à l'envers.

| Chute | Position | Dégâts | Le robot fonctionne encore ? |
|---|---|---|---|
| 1 | | | |
| … | | | |
| 5 | | | |

**Bon à savoir :** si la carapace se détache en tombant, ce n'est pas un défaut. Les aimants jouent le rôle de **fusible** : la carapace absorbe le choc et se remet en place d'un geste. Noter en revanche toute **pièce cassée** : patins, berceaux moteurs, tube du feutre, poteaux du servo.

## Test 7 : chaleur

**Objectif :** vérifier que les pièces ne se déforment pas dans une voiture en été (voir la [veille sur les matériaux](veille-energie-materiaux-programmation.md)).

**Méthode :**
1. Imprimer un châssis et une carapace en PLA, et les mêmes en PETG.
2. Les laisser une journée dans une voiture garée au soleil, avec un thermomètre.
3. Mesurer avant et après : longueur, largeur, planéité du châssis, et vérifier que la carapace se pose toujours.

| Pièce | Matériau | Température max relevée | Déformation ? | Se monte encore ? |
|---|---|---|---|---|
| Châssis | PLA | | | |
| Châssis | PETG | | | |
| Carapace | PLA | | | |
| Carapace | PETG | | | |

## Test 8 : transport en mallette

**Objectif :** vérifier que le kit arrive intact après un trajet.

**Méthode :** ranger le kit dans sa mallette, faire un vrai trajet en voiture (idéalement une route de montagne), puis tout vérifier à l'arrivée.

**À noter :** pièces cassées ou desserrées, aimants décollés, feutres secs, inventaire complet ou non.

**Ce test suppose que la mallette existe.** Elle n'est pas encore conçue.

## Test 9 : séance avec des élèves

**Objectif :** voir si le robot et les fiches marchent vraiment en classe.

**Méthode :** une séance de 1 h avec un groupe de CM2 ou de 6e, menée par un enseignant à partir des fiches. Un observateur note sans intervenir.

| À observer | Remarques |
|---|---|
| Les élèves comprennent-ils les consignes de la fiche ? | |
| Combien de temps pour dessiner le premier carré ? | |
| Quelles erreurs reviennent (programme, manipulation) ? | |
| Que cassent ou perdent-ils ? | |
| Qu'est-ce qui les motive ou les amuse ? | |
| Qu'en pense l'enseignant ? | |

---

## Après les tests

Les résultats serviront à :
1. **corriger le modèle 3D** : jeux, épaisseurs, renforts ;
2. **réécrire la notice de montage**, avec des photos ;
3. **remplir la grille de comparaison** de l'étape 5 avec des valeurs mesurées et non plus estimées ;
4. **ajuster le chiffrage**, avec le temps de montage et la consommation réelle de piles et de feutres.
