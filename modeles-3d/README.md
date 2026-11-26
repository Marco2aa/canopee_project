# Tartaruga – robot tortue imprimable

Robot inspiré de la **tortue d'Hermann**, une espèce emblématique de Corse. Il est conçu pour le **micro:bit V2** avec une carte d'extension robot, et se programme en blocs de style Scratch (MakeCode, Vittascience), du CM2 à la 5e.

## Ce qui le rend ludique

- **Elle dessine.** Un feutre se place au centre, entre les deux roues. La tortue trace ses déplacements comme la tortue du langage Logo : carré, triangle, étoile… C'est de la géométrie de cycle 3 et 4.
- **Elle a un visage.** Une fenêtre à l'avant laisse voir les LED du micro:bit, qui affichent des émotions ou des flèches.
- **On change sa carapace.** La carapace tient par des aimants et s'enlève sans outil. Le couvercle est plat, donc les élèves peuvent dessiner le leur, par exemple dans Tinkercad.
- **On voit l'intérieur.** En enlevant la carapace, on découvre les moteurs, les piles et la carte.

## Pièces à imprimer

Les fichiers STL sont déjà orientés pour l'impression. Toutes les pièces tiennent sur un plateau de 220 × 220 mm.

| Fichier | Dimensions (mm) | Orientation | Supports |
|---|---|---|---|
| `tartaruga_chassis.stl` | 99 × 180 × 44 | posé sur sa face plate (le dessus du châssis) | non |
| `tartaruga_carapace.stl` | 105 × 180 × 56 | posée sur son bord | non (pente de 50° au plus) |
| `tartaruga_couvercle.stl` | 81 × 130 × 6,5 | face gravée contre le plateau | non |

**Réglages conseillés :** PLA ou PETG, buse de 0,4 mm, couches de 0,2 mm, 3 périmètres, remplissage de 20 %. Pour le châssis, 4 périmètres rendent les berceaux moteurs plus solides.

`tartaruga.blend` contient le modèle complet, avec les composants de référence (moteurs, roues, piles, carte) dans une collection à part.

## Matériel à acheter

| Composant | Quantité |
|---|---|
| BBC micro:bit V2 | 1 |
| Carte d'extension robot pour micro:bit (pilote 2 moteurs, avec extension MakeCode ou Vittascience) | 1 |
| Moteur TT jaune avec réducteur, et sa roue de 65 mm | 2 |
| Bloc 4 piles AA (format 2 × 2, environ 63 × 58 × 16 mm) | 1 |
| Aimants néodyme 6 × 3 mm | 12 (6 dans le châssis, 6 dans la carapace) |
| Vis M3 × 8 et entretoises nylon M3 × 8 | 4 pour la carte, 2 pour les piles |
| Vis M3 × 10 pour serrer le feutre | 1 |
| Colliers de serrage, 3 mm de large | 4 (2 par moteur) |
| Feutre, 12 mm de diamètre au plus | 1 |

## Coût estimé par robot

Estimation faite en novembre 2026, à partir de prix relevés en ligne, TTC. **Les prix changent souvent : à revérifier avant toute commande.**

| Composant | Version de marque | Version économique |
|---|---|---|
| micro:bit V2 (prix en pack de 10) | 20 € | 20 € |
| Carte d'extension moteur | 15 € (Kitronik) | 8 € (générique) |
| 2 moteurs TT avec roues de 65 mm | 11 € | 5 € |
| Boîtier 4 piles AA et 4 piles alcalines | 4,50 € | 3 € |
| 12 aimants néodyme 6 × 3 mm | 1,50 € | 1 € |
| Vis, entretoises, colliers | 1,20 € | 0,70 € |
| Feutre | 1 € | 0,50 € |
| Filament PLA (≈ 125 g à 20 €/kg) | 2,50 € | 2,50 € |
| **Total par robot** | **≈ 57 €** | **≈ 41 €** |

**D'où viennent les chiffres :**
- **Filament :** les 3 pièces font 135 cm³ si elles étaient pleines (mesuré dans Blender). Avec 20 % de remplissage et des parois fines, il faut compter environ 110 à 130 g de PLA.
- **Temps d'impression :** environ 8 h par robot. C'est une estimation, à confirmer avec le logiciel d'impression (le « slicer »).

**Ce qui n'est pas compté :**
- la livraison vers la Corse (certains vendeurs facturent environ 18 € sous 50 € de commande) ;
- l'achat d'une imprimante 3D ;
- des piles rechargeables (environ 10 € les 4, plus un chargeur), si on les préfère aux piles jetables.

**Pour comparer :** les robots éducatifs du commerce (mBot, Thymio) coûtent plutôt 80 à 150 € pièce. Cet ordre de grandeur reste à vérifier pendant la veille sur le budget. Tartaruga reviendrait donc environ 2 à 3 fois moins cher.

**Pour faire baisser le prix :** commander les micro:bit en pack Club de 10, et les moteurs et cartes génériques en lot. Une pièce imprimée cassée se refait pour quelques dizaines de centimes.

**Sources :**
- [micro:bit V2 à l'unité (RS France)](https://fr.rs-online.com/web/p/bbc-micro-bit/2336797) et [pack Club](https://fr.rs-online.com/web/p/bbc-micro-bit/2336795)
- [Kitronik Compact Motor Driver (RS)](https://befr.rs-online.com/web/p/bbc-micro-bit-add-ons/2048223)
- [Waveshare Driver Breakout for micro:bit](https://www.waveshare.com/product/mcu-tools/development-boards/motors-interface/motor-driver-for-micro-bit.htm)
- [Dagu : 2 roues de 65 mm et 2 moteurs TT (RobotShop)](https://eu.robotshop.com/products/dagu-65mm-wheel-pair-tt-3-6v-dc-gear-motor)
- [Roues de 65 mm (Kiwi Electronics)](https://www.kiwi-electronics.com/en/robotics-kits-parts-177/wheel-65mm-rubber-tire-pair-3243)

## Montage

1. Glissez chaque moteur dans son berceau, sous le châssis, et serrez-le avec 2 colliers passés dans les fentes.
2. Vissez le bloc de piles sous l'arrière du châssis (2 vis M3) et faites passer les fils par la fente.
3. Fixez la carte d'extension sur le dessus avec 4 entretoises M3, puis insérez le micro:bit, LED vers l'avant.
4. Collez les aimants dans le châssis et dans les pattes de la carapace. **Vérifiez les pôles** : chaque paire doit s'attirer.
5. Posez la carapace, puis le couvercle.
6. Glissez le feutre par le haut, jusqu'à ce que la pointe touche le papier, et bloquez-le avec la vis M3 latérale.

## À vérifier avant d'imprimer

Ces cotes viennent de valeurs courantes. **Mesurez vos composants au pied à coulisse.** Si une cote diffère, le modèle doit être régénéré avec la bonne valeur :

- **Moteur TT :** 70 × 22,5 × 19 mm, axe à 11 mm du bout.
- **Entraxe des trous de la carte d'extension :** 58 × 40 mm, valeur provisoire à adapter à la carte choisie.
- **Bloc de piles :** 63 × 58 × 16 mm.
- **Diamètre du feutre :** le trou fait 13 mm.
- **Jeu d'impression :** 0,4 mm. Réduisez-le si les pièces flottent, augmentez-le si elles forcent.
