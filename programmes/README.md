# Programmes Tartaruga

## `calibrage.ts` : régler sa tortue

Les moteurs « jaunes » (TT) de Tartaruga sont bon marché mais **imprécis** : ils n'ont pas de capteur qui compte les tours de roue. Pour tourner de 90°, le robot fait donc tourner ses moteurs pendant une certaine **durée**. Cette durée change d'un robot à l'autre, et aussi selon l'usure des piles et la surface.

Ce programme sert à trouver les bonnes valeurs pour **chaque robot**, avant de dessiner des figures.

> ⚠️ **Non testé sur un vrai robot.** Ce programme a été écrit en même temps que le modèle 3D, avant le premier prototype. Les broches des moteurs et du servo (partie 1 du programme) **dépendent de la carte d'extension choisie** et devront être adaptées.

### Charger le programme dans MakeCode

1. Ouvrez [makecode.microbit.org](https://makecode.microbit.org) et créez un **nouveau projet**.
2. En haut, passez de **Blocs** à **JavaScript**.
3. Effacez tout, puis collez le contenu de `calibrage.ts`.
4. Repassez en **Blocs** : le programme s'affiche en blocs.
5. Branchez le micro:bit en USB et cliquez sur **Télécharger**.

### Adapter le programme à la carte d'extension

Dans la partie 1 du programme, trois fonctions parlent directement à la carte :
- `moteurs(gauche, droite)` : fait tourner les deux moteurs, de -100 à 100 ;
- `arreter()` : arrête les moteurs ;
- `stylo(baisse)` : lève ou baisse le feutre avec le servo.

L'exemple fourni suppose un pont en H simple sur les broches P13 à P16, et le servo sur P1. Si la carte choisie a sa propre extension MakeCode (*Extensions*, puis le nom de la carte), remplacez le contenu de ces trois fonctions par ses blocs. **Le reste du programme ne change pas.**

### Les commandes

| Action | Effet |
|---|---|
| Toucher le **logo** | change de réglage : **V** = virage, **L** = ligne droite |
| Bouton **A** | diminue la valeur |
| Bouton **B** | augmente la valeur |
| **A + B** ensemble | lance le test, feutre baissé : un carré en mode V, une ligne droite en mode L |
| **Secouer** | affiche les valeurs trouvées, à recopier |

---

## Fiche d'activité : « Ma tortue tourne-t-elle bien ? »

**Niveau :** CM2 à 5e. **Durée :** 45 min environ. **Groupes :** 2 ou 3 élèves par robot.

**Objectifs :**
- Comprendre qu'un robot n'est pas parfait et qu'il faut le **régler**.
- Utiliser les **angles** : un carré, c'est 4 virages de 90°.
- Mener une démarche d'essai et d'erreur, et **noter ses résultats**.

**Matériel :** un robot Tartaruga avec le programme de calibrage, une grande feuille, un feutre, une règle et un rapporteur.

### Étape 1 : la ligne droite (mode L)

1. Touchez le logo jusqu'à voir **L**.
2. Posez la tortue sur la feuille et appuyez sur **A + B**.
3. Le trait est-il droit ?
   - Il part vers la **gauche** : appuyez sur **B** pour augmenter la correction.
   - Il part vers la **droite** : appuyez sur **A** pour la diminuer.
4. Recommencez jusqu'à obtenir un trait bien droit.

### Étape 2 : le virage (mode V)

1. Touchez le logo jusqu'à voir **V**.
2. Appuyez sur **A + B** : la tortue dessine un carré.
3. Le carré se referme-t-il ?
   - La tortue **ne tourne pas assez** (le carré reste ouvert vers l'extérieur) : appuyez sur **B** pour allonger la durée.
   - Elle **tourne trop** (le dernier côté rentre dans le carré) : appuyez sur **A** pour la raccourcir.
4. Mesurez un angle du carré au rapporteur. Est-il proche de 90° ?

### Étape 3 : noter les résultats

Secouez le micro:bit et recopiez les valeurs :

| Robot n° | Essai | TEMPS_90 (ms) | CORRECTION | Angle mesuré | Le carré se referme ? |
|---|---|---|---|---|---|
| | 1 | | | | |
| | 2 | | | | |
| | 3 | | | | |

### Pour aller plus loin (discussion en classe)

- Pourquoi deux robots identiques n'ont-ils pas les mêmes valeurs ?
- Que se passe-t-il quand les piles s'usent ? Et sur une table, une moquette ou du carton ?
- Si 90° demandent `TEMPS_90` millisecondes, combien en faut-il pour 45° ? Pour 144°, l'angle d'une branche d'étoile ? C'est un exercice de **proportionnalité**.

**À retenir :** il faut refaire le calibrage quand on **change les piles** ou **de surface**. Les valeurs trouvées se recopient en haut des autres programmes (carré, triangle, étoile…).
