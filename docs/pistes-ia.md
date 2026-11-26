# Pistes – L'intelligence artificielle avec Tartaruga

**Idée directrice :** ne pas ajouter une IA « magique » au robot, mais **faire comprendre aux élèves comment une IA apprend**, en la fabriquant eux-mêmes. Les élèves collectent des exemples, entraînent un modèle, le testent et découvrent ses erreurs.

**Pourquoi c'est réaliste :** le micro:bit V2 de Tartaruga sait déjà faire tourner un petit modèle d'apprentissage automatique. Il en a la puissance de calcul et l'accéléromètre. Pour les pistes 2 et 4, il n'y a **rien à acheter** ; la piste 1 demande un micro:bit de plus par groupe.

**Date du relevé :** novembre 2026. Les points marqués *à vérifier* doivent être testés sur le prototype.

---

## Vue d'ensemble

| N° | Piste | Ce que les élèves font | Notion d'IA | Matériel en plus | Durée |
|---|---|---|---|---|---|
| 1 | **Télécommande par gestes** | apprendre à un micro:bit à reconnaître leurs gestes pour piloter la tortue | apprentissage supervisé : données, entraînement, test | 1 micro:bit V2 par groupe (≈ 20 €) | 2 séances de 1 h |
| 2 | **La tortue qui ressent** | apprendre à la tortue à reconnaître comment on la manipule | même notion, sur le robot lui-même | aucun | 1 séance de 1 h |
| 3 | **Pourquoi l'IA ne me comprend pas ?** | constater qu'un modèle entraîné sur une seule personne se trompe avec les autres | les biais et la qualité des données | aucun | 20 à 30 min, dans la piste 1 ou 2 |
| 4 | **La tortue qui apprend le labyrinthe** (débranché) | jouer le rôle d'une machine qui apprend par essais et erreurs, avec des gobelets et des jetons | apprentissage par renforcement | gobelets, jetons, une grille | 1 séance de 1 h |

**Progression conseillée :** piste 4 (comprendre sans écran), puis la piste 2 ou 1 (fabriquer un modèle), puis la piste 3 (porter un regard critique).

---

## L'outil commun aux pistes 1 à 3 : micro:bit CreateAI

[micro:bit CreateAI](https://microbit.org/createai/) est un outil **gratuit**, conçu par la fondation micro:bit pour l'école. Il fonctionne en quatre étapes :

1. **Collecter** : on bouge le micro:bit plusieurs fois pour chaque geste, et l'outil enregistre les mesures de l'accéléromètre.
2. **Entraîner** : un clic, et l'outil construit le modèle.
3. **Tester** : on refait les gestes et on regarde si le modèle les reconnaît.
4. **Programmer** : le modèle part dans **MakeCode**, sous forme de blocs du type « quand le geste *avancer* est reconnu ». Le modèle tourne ensuite **sur le micro:bit lui-même**, sans ordinateur.

**Conditions d'utilisation :**

| Condition | Détail |
|---|---|
| Carte | **micro:bit V2** pour faire tourner le modèle ; c'est celle de Tartaruga |
| Poste | un ordinateur (ou une tablette avec l'application CreateAI), navigateur **Chrome ou Edge** |
| Liaison | Bluetooth ; **si l'ordinateur n'en a pas, il faut un micro:bit V2 de plus par binôme** qui sert de relais |
| Internet | **nécessaire** : c'est un outil web, contrairement à MakeCode qui existe hors ligne |
| Téléphones | non pris en charge |

**À vérifier sur le prototype :**
- L'éditeur MakeCode ouvert depuis CreateAI accepte-t-il l'**extension de la carte d'extension** choisie (moteurs, servo) ?
- Accepte-t-il les blocs **radio**, nécessaires à la piste 1 ?

---

## Piste 1 : la télécommande par gestes ⭐

### Le principe

Chaque groupe a **deux micro:bit** : celui de Tartaruga et un second, tenu dans la main. Les élèves apprennent au micro:bit de la main à reconnaître **leurs propres gestes**. Quand un geste est reconnu, il envoie un ordre par radio à la tortue.

```
  [ micro:bit dans la main ]            radio            [ Tartaruga ]
  modèle entraîné par les élèves   ─────────────────►   reçoit l'ordre
  geste « pencher en avant »        envoie « A »         et avance
  geste « tourner le poignet »      envoie « G »         et tourne à gauche
  geste « secouer »                 envoie « S »         et lève ou baisse le stylo
```

### Déroulé proposé (2 séances de 1 h)

**Séance 1 : fabriquer le modèle**
1. Choisir 3 ou 4 gestes en groupe, et leur donner un nom.
2. Enregistrer chaque geste **une dizaine de fois** dans CreateAI.
3. Entraîner, puis tester. Quel geste est mal reconnu ? Pourquoi ? Les gestes se ressemblent-ils trop ?
4. Ajouter des exemples ou changer de geste, puis réentraîner.

**Séance 2 : piloter la tortue**
1. Dans MakeCode, associer chaque geste reconnu à l'envoi d'un message radio.
2. Charger le programme récepteur dans Tartaruga.
3. Défi : faire dessiner à la tortue une **figure imposée**, uniquement par gestes.

### Ce que les élèves apprennent
- Une IA **apprend à partir d'exemples**. Elle ne suit pas des règles écrites par un programmeur.
- **Plus les exemples sont nombreux et variés, meilleur est le modèle.**
- Un modèle **peut se tromper**, et on peut mesurer ses erreurs.
- La communication **radio** entre deux objets.

### Coût
Un micro:bit V2 de plus par groupe, soit environ 20 € (prix en pack de 10). Pour un kit de 8 robots, cela fait **environ 160 €**, qui peuvent aussi servir de relais Bluetooth. À ajouter au [chiffrage du kit](chiffrage-kit-classe.md) si la piste est retenue.

---

## Piste 2 : la tortue qui ressent

### Le principe

On utilise **le micro:bit déjà présent dans Tartaruga**. Les élèves apprennent à la tortue à reconnaître **ce qu'on lui fait**, et elle réagit sur son visage de LED, comme un animal de compagnie.

| On la… | Elle affiche… |
|---|---|
| soulève doucement | un sourire |
| secoue | un visage surpris ou en colère |
| retourne sur le dos | un visage triste, et elle agite les roues |
| laisse posée tranquillement | des yeux qui clignent |

> Une caresse sur la carapace bouge trop peu le micro:bit pour être reconnue de façon fiable par l'accéléromètre. Pour « caresser » la tortue, on peut utiliser le **logo tactile** du micro:bit, mais c'est un simple capteur et non de l'IA. *À tester.*

### Déroulé proposé (1 h)
1. Retirer la carapace et le couvercle, et relier le micro:bit de la tortue à CreateAI.
2. Enregistrer chaque manipulation une dizaine de fois, **avec le robot entier**.
3. Entraîner, tester, puis programmer les réactions dans MakeCode.
4. Remettre la carapace : la tortue est « vivante ».

### Ce que les élèves apprennent
Les mêmes notions que la piste 1, **sans aucun matériel en plus**. C'est la piste la plus simple à proposer en CM2. Elle renforce aussi le côté « animal » de Tartaruga.

### Point d'attention
Pendant l'entraînement, le micro:bit doit rester sur le robot, pour que les mesures correspondent aux vrais mouvements de la tortue. *Vérifier* que les piles et les moteurs ne gênent pas la liaison Bluetooth.

---

## Piste 3 : « Pourquoi l'IA ne me comprend pas ? »

### Le principe

C'est une courte expérience à glisser dans la piste 1 ou 2. Elle montre qu'**une IA ne vaut que par ses données**.

### Déroulé (20 à 30 min)
1. **Un seul élève** enregistre tous les exemples de gestes.
2. On entraîne le modèle, et cet élève le teste : ça marche très bien.
3. **Un camarade** essaie à son tour, avec sa façon à lui de faire les gestes : le modèle se trompe souvent.
4. On compte les erreurs de chaque élève, sur 10 essais, dans un tableau au tableau.
5. On réentraîne avec les exemples de **tout le groupe**, et on refait les tests : les résultats s'équilibrent.

| | Erreurs sur 10 (modèle d'un seul élève) | Erreurs sur 10 (modèle de tout le groupe) |
|---|---|---|
| Élève qui a entraîné | | |
| Camarade 1 | | |
| Camarade 2 | | |

### Questions pour le débat
- Pourquoi le modèle reconnaît-il mieux celui qui l'a entraîné ?
- Que se passerait-il si une IA de reconnaissance de visages n'avait été entraînée qu'avec certaines personnes ?
- Qui choisit les données d'une IA ? Peut-on lui faire confiance les yeux fermés ?

### Ce que les élèves apprennent
La notion de **biais** : une IA reproduit les limites de ses exemples. C'est de l'**éducation au numérique et à l'esprit critique**, à partir d'une expérience vécue plutôt que d'un discours.

---

## Piste 4 : la tortue qui apprend le labyrinthe (débranché)

### Le principe

Cette activité reprend l'idée de **MENACE** : en 1961, le chercheur Donald Michie avait construit une « machine » faite de **boîtes d'allumettes et de perles**, qui apprenait à jouer au morpion. Ici, les élèves sont la machine, et la tortue apprend à sortir d'un labyrinthe.

### Le matériel
- Un **labyrinthe** sur une grille, dessiné au sol ou sur une feuille A3, avec 3 ou 4 carrefours, une sortie et des culs-de-sac.
- Un **gobelet par carrefour**.
- Des **jetons de couleur** : par exemple rouge pour « gauche », bleu pour « droite », vert pour « tout droit ». Au départ, chaque gobelet contient 2 jetons de chaque direction possible.
- Une figurine de tortue, ou Tartaruga elle-même, déplacée à la main ou par programme.

### Les règles
1. La tortue part de l'entrée.
2. À chaque carrefour, un élève **tire un jeton au hasard** dans le gobelet : la tortue va dans cette direction. On pose le jeton à côté du gobelet.
3. **Si la tortue atteint la sortie** : récompense. On remet chaque jeton tiré dans son gobelet, **avec un jeton de la même couleur en plus**.
4. **Si elle tombe dans un cul-de-sac** : punition. Les jetons tirés **ne sont pas remis**. On garde au moins un jeton par couleur dans chaque gobelet.
5. On recommence une dizaine de fois, en notant à chaque partie si la tortue a réussi.

### Ce qu'on observe
Au fil des parties, les gobelets se remplissent de la **bonne couleur**. La tortue trouve la sortie de plus en plus souvent, **sans que personne ne lui ait donné le chemin**. On peut tracer au tableau la courbe des réussites au fil des parties.

### Ce que les élèves apprennent
- L'**apprentissage par renforcement** : récompense, punition, et amélioration par l'essai et l'erreur.
- Le rôle du **hasard** au début, puis des **probabilités** qui changent. Cela fait le lien avec les mathématiques.
- La machine **ne comprend pas** le labyrinthe : elle a seulement accumulé des statistiques.

### Prolongement
Une fois les gobelets « entraînés », les élèves écrivent dans MakeCode le chemin que la machine a trouvé, et Tartaruga le **trace au feutre** sur le labyrinthe.

---

## Ce que nous déconseillons

| Idée | Pourquoi l'écarter |
|---|---|
| Un chatbot ou une IA générative utilisés par les élèves | conditions d'âge des services (souvent 13 à 15 ans au minimum), données personnelles, besoin d'Internet. L'enseignant peut en revanche s'en servir pour préparer ses séances. |
| Une caméra sur le robot | coût, fragilité, et prise d'images d'enfants |
| La reconnaissance vocale | données vocales des élèves, bruit de la classe, peu fiable sur une petite carte |

## Données personnelles

Les pistes 1 à 3 n'enregistrent que des **mesures de mouvement** : pas d'image, pas de voix, pas de nom. CreateAI s'utilise **sans compte élève**. Il reste à informer les familles de l'outil en ligne utilisé, comme pour tout service numérique, et à faire confirmer par le DPD académique.

## Questions pour Canopé

- Les postes des écoles ont-ils **Chrome ou Edge**, et le **Bluetooth** ?
- L'accès à Internet est-il suffisant pour un outil web comme CreateAI ? Sinon, les pistes 2 à 4 peuvent être préparées à l'avance, et la piste 4 n'a besoin de rien.
- L'IA fait-elle partie des thèmes que Canopé souhaite mettre en avant dans le kit ?

---

## Sources

- [micro:bit CreateAI : présentation](https://microbit.org/createai/) et [guide d'utilisation](https://microbit.org/get-started/user-guide/microbit-createai/)
- [L'IA avec le micro:bit (microbit.org)](https://microbit.org/get-started/features/ai/)
- [Premières séances avec CreateAI](https://microbit.org/teach/lessons/first-lessons-with-microbit-createai/)
- [Lancement de CreateAI, novembre 2024](https://microbit.org/news/2024-11-20/microbit-CreateAI-launch)
- [Projet « AI light switch »](https://microbit.org/projects/make-it-code-it/ai-light-switch/)
- [Tutoriel DigiKey : MakeCode, CreateAI et le micro:bit](https://www.digikey.com/en/maker/tutorials/2026/exploring-ai-with-makecode-createai-and-the-bbc-microbit)
- MENACE (Donald Michie, 1961) : la machine à boîtes d'allumettes qui apprenait le morpion. Référence historique, à citer avec une source au choix.
