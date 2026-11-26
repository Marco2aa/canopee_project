# Veille – Cartes électroniques

**Thème :** Électronique – quels composants choisir ? (voir [questions de recherche](questions-recherche-canope.md), thème 1)

**Enjeux concernés :** Coût, Robustesse, Autonomie (et Pédagogie pour le choix du langage).

**Date du relevé :** novembre 2026. Les prix viennent de distributeurs en ligne, ils changent souvent et les ruptures de stock sont fréquentes : **à revérifier avant toute commande.**

---

## 1. Les cartes comparées

| | BBC micro:bit V2 | Arduino Uno R4 Minima | Raspberry Pi Pico 2 W | ESP32 DevKit |
|---|---|---|---|---|
| **Prix indicatif (TTC, à l'unité)** | ≈ 19 à 21 € | ≈ 17 à 21 € | ≈ 7 à 8 € | ≈ 8 à 17 € (selon la variante) |
| **Prix en lot** | ≈ 17 € HT la carte en pack de 10 | remises dès 25 pièces | — | — |
| **Tension de travail** | 3,3 V | 5 V | 3,3 V | 3,3 V |
| **Capteurs intégrés** | oui : 25 LED, 2 boutons, accéléromètre, boussole, micro, haut-parleur, température, lumière | aucun | aucun | aucun |
| **Sans fil** | Bluetooth, radio entre cartes | non | Wi-Fi, Bluetooth | Wi-Fi, Bluetooth |
| **Branchement sur PC** | apparaît comme une clé USB, **aucun pilote** | pilote parfois nécessaire | apparaît comme une clé USB | **pilote souvent nécessaire** (CH340, CP2102) |
| **Soudure** | aucune | aucune | broches à souder (sauf version « H ») | souvent livré soudé |
| **Programmation par blocs** | MakeCode, Vittascience, Scratch | Vittascience, mBlock | limitée | limitée |
| **Programmation texte** | MicroPython | C/C++ (Arduino IDE) | MicroPython, C/C++ | MicroPython, C/C++ |
| **Tablettes** | oui (application micro:bit, Bluetooth) | non | non | possible mais complexe |
| **Pilotage direct de moteurs** | non, il faut une carte d'extension | non, il faut un shield moteur | non, il faut un pont en H | non, il faut un pont en H |

---

## 2. Analyse par enjeu

### Coût
- La **Pico 2 W** est de loin la moins chère, autour de 7 €. Mais il faut ajouter un pont en H, des capteurs et un support : l'écart réel avec les autres cartes se réduit.
- Le **micro:bit** est plus cher à l'unité, mais il contient déjà des LED, des boutons et des capteurs qu'il faudrait acheter séparément pour les autres cartes.
- Les **ESP32** génériques sont bon marché, mais il en existe de nombreuses variantes pas toujours compatibles entre elles : c'est risqué pour un kit qui doit être identique d'une école à l'autre.

### Robustesse
- Aucune carte n'est robuste « nue » : il faut un **boîtier ou un carter** (voir le thème Structure).
- Le micro:bit et l'Arduino Uno se branchent sans soudure ; la Pico et certaines ESP32 ont des broches fines, fragiles si on manipule souvent les fils.
- Le **connecteur latéral** du micro:bit s'emboîte dans une carte d'extension robot : moins de fils, donc moins de faux contacts.

### Autonomie (pour l'enseignant)
- C'est le critère qui sépare le plus les cartes. Sur les postes des écoles, on ne peut souvent **pas installer de pilote** :
  - le micro:bit fonctionne depuis le navigateur, sans rien installer ;
  - l'ESP32 et beaucoup d'Arduino compatibles demandent un pilote USB, donc les droits d'administrateur.
- Le micro:bit est le seul à pouvoir être programmé **depuis une tablette**, ce qui compte si les écoles sont équipées de tablettes (question 0.7 à poser à Canopé).

### Pédagogie
- Le micro:bit est déjà très présent dans l'Éducation nationale, avec beaucoup de ressources gratuites (MakeCode, Vittascience). On peut passer des **blocs à Python** sans changer de carte, ce qui assure la continuité avec le collège.
- L'Arduino est pertinent au collège ou au lycée, moins en primaire.
- La Pico et l'ESP32 sont plutôt adaptées au lycée ou aux clubs : peu d'outils par blocs simples pour le primaire.

---

## 3. Notes par critère (1 = faible, 5 = excellent)

Notes provisoires, à pondérer selon les réponses de Canopé (étape 5).

| Critère | micro:bit V2 | Arduino Uno R4 | Pico 2 W | ESP32 |
|---|---|---|---|---|
| Coût | 3 | 3 | 5 | 4 |
| Robustesse | 4 | 4 | 2 | 3 |
| Autonomie (installation, utilisation) | 5 | 3 | 3 | 2 |
| Pédagogie (primaire) | 5 | 3 | 2 | 2 |
| Pédagogie (collège) | 4 | 4 | 3 | 3 |
| **Total** | **21** | **17** | **15** | **14** |

---

## 4. Contrainte retenue : programmation en Scratch, du CM2 à la 5e

Le public visé va de la fin du cycle 3 (CM2, 6e) au début du cycle 4 (5e). Le langage retenu est **Scratch**, ou des blocs de même style.

**Attention à la différence entre « Scratch » et « blocs de type Scratch » :**

| Outil | Le programme tourne… | Robot autonome ? | Installation |
|---|---|---|---|
| **Scratch 3** + extension micro:bit | sur l'ordinateur, le micro:bit reste relié en Bluetooth | **non** : le robot s'arrête si on s'éloigne du PC | logiciel *Scratch Link* à installer, Bluetooth obligatoire |
| **MakeCode** (blocs de style Scratch) | sur la carte, après téléversement | **oui** | aucune (navigateur) |
| **Vittascience** (blocs de style Scratch, passage à Python) | sur la carte, après téléversement | **oui** | aucune (navigateur) |
| **mBlock** (basé sur Scratch, pour Arduino ou mBot) | sur la carte ou en direct | oui | logiciel ou version web avec un pilote |

**Conséquences pour le kit :**
- L'extension micro:bit officielle de Scratch ne gère que les LED, les boutons et l'inclinaison. Elle **ne pilote pas les moteurs** d'une carte d'extension robot : elle ne suffit pas pour un robot qui roule.
- Pour un robot autonome, il faut un éditeur **de blocs de style Scratch qui téléverse sur la carte** : MakeCode ou Vittascience. Les élèves qui connaissent Scratch retrouvent les mêmes blocs (boucles, conditions, variables, événements).
- Vittascience permet en plus le passage **des blocs à Python**, utile pour la 5e et la suite du collège.
- **Cela renforce le choix du micro:bit** : ces deux éditeurs le prennent bien en charge, alors que la Pico et l'ESP32 n'ont pas d'éditeur par blocs simple et éprouvé.

**À vérifier :** la carte d'extension robot choisie doit avoir une **extension MakeCode et/ou Vittascience**, sinon les élèves ne pourront pas piloter les moteurs avec des blocs.

---

## 5. Première conclusion

**Piste principale : BBC micro:bit V2 + une carte d'extension robot** (pont en H pour 2 moteurs, connecteurs pour capteurs).
- Aucune installation sur les postes, utilisable sur tablette.
- Les capteurs intégrés permettent de commencer sans câbler.
- Même carte du cycle 2 au collège, des blocs jusqu'à Python.

**Piste « petit budget » : Raspberry Pi Pico 2 W** (version avec broches déjà soudées) pour le collège ou un club, si le coût devient le critère décisif.

**À écarter pour le primaire :** l'ESP32 (pilotes, variantes) et l'Arduino Uno (pas de capteurs intégrés, moins adapté aux jeunes élèves).

---

## 6. Informations utiles pour la modélisation 3D

Dimensions approximatives à intégrer au châssis et au boîtier. **À vérifier sur la fiche technique officielle** avant d'imprimer.

| Carte | Dimensions (mm) | Fixation |
|---|---|---|
| micro:bit V2 | ≈ 52 × 42 | connecteur latéral (fente sur la carte d'extension) |
| Arduino Uno | ≈ 68,6 × 53,4 | 4 trous de ≈ 3,2 mm (vis M3) |
| Raspberry Pi Pico 2 W | ≈ 51 × 21 | 4 trous de ≈ 2,1 mm (vis M2) |
| ESP32 DevKitC | ≈ 55 × 28 (variable) | dépend de la variante |

---

## 7. Points à confirmer

- Compatibilité de **Vittascience** avec la Pico et l'ESP32 : le site mentionne micro:bit, Arduino, mBot et STM32, mais pas ces deux cartes.
- Choix de la **carte d'extension robot** pour le micro:bit (prix, robustesse, disponibilité en France).
- Délais et frais de livraison vers la Corse (certains distributeurs facturent le port sous 50 € de commande).
- Équipement réel des écoles : tablettes ou ordinateurs, droits d'installation (questions 0.7 et 2.3).

---

## Sources

- RS Components France – micro:bit V2 [à l'unité](https://fr.rs-online.com/web/p/bbc-micro-bit/2336797), [kit Go](https://fr.rs-online.com/web/p/bbc-micro-bit/2336796), [pack Club](https://fr.rs-online.com/web/p/bbc-micro-bit/2336795)
- leDénicheur – [micro:bit V2 Go](https://ledenicheur.fr/product.php?p=13201096)
- Arduino Store – [Uno R4 Minima](https://store.arduino.cc/en-de/products/uno-r4-minima)
- Jameco – [Uno R4 Minima (prix en lot)](https://www.jameco.com/z/ABX00080-Arduino-Arduino-Uno-R4-Minima-Genuine-Microcontroller_2333871.html)
- TME – [Raspberry Pi Pico 2 W](https://www.tme.eu/lu/en/details/sc1633/raspberry-pi-embedded/raspberry-pi/raspberry-pi-pico-2-w/)
- Hackster – [lancement de la Pico 2 W](https://www.hackster.io/news/raspberry-pi-launches-the-radio-equipped-raspberry-pi-pico-2-w-for-just-7-4073d1130363)
- DFRobot – [cartes ESP32](https://www.dfrobot.com/search-esp32%20devkit.html)
- Waveshare – [cartes ESP32](https://www.waveshare.com/product/esp32-related/boards-kits.htm)
- Vittascience – [page d'accueil](https://fr.vittascience.com/)
