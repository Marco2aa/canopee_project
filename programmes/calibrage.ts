// =====================================================================
// Tartaruga – programme de calibrage (MakeCode, micro:bit V2)
// Projet Canopé – kit de robotique pour les écoles de Corse
//
// But : régler le robot pour qu'il tourne bien de 90° et aille tout droit.
// Les moteurs TT n'ont pas de capteur de rotation : on règle des DURÉES.
//
// Commandes :
//   Logo (toucher)  : changer de réglage  V = virage, L = ligne droite
//   Bouton A        : diminuer la valeur
//   Bouton B        : augmenter la valeur
//   A + B           : lancer le test (carré ou ligne droite, feutre baissé)
//   Secouer         : afficher toutes les valeurs à recopier
// =====================================================================


// ---------------------------------------------------------------------
// 1. À ADAPTER À VOTRE CARTE D'EXTENSION
// Exemple pour un pont en H « 2 broches par moteur » (type DRV8833 ou
// L9110) câblé sur P13-P14 (moteur gauche) et P15-P16 (moteur droit),
// avec le servo du lève-stylo sur P1.
// Si votre carte a sa propre extension MakeCode, remplacez le contenu
// de moteurs(), arreter() et stylo() par les blocs de cette extension.
// ---------------------------------------------------------------------
let STYLO_BAS = 90      // angle du servo quand le feutre touche le papier
let STYLO_HAUT = 115    // angle du servo quand le feutre est levé

function moteurs(gauche: number, droite: number) {
    gauche = Math.max(-100, Math.min(100, gauche))
    droite = Math.max(-100, Math.min(100, droite))
    let pg = Math.round(Math.abs(gauche) * 1023 / 100)
    let pd = Math.round(Math.abs(droite) * 1023 / 100)
    if (gauche >= 0) {
        pins.analogWritePin(AnalogPin.P13, pg)
        pins.digitalWritePin(DigitalPin.P14, 0)
    } else {
        pins.digitalWritePin(DigitalPin.P13, 0)
        pins.analogWritePin(AnalogPin.P14, pg)
    }
    if (droite >= 0) {
        pins.analogWritePin(AnalogPin.P15, pd)
        pins.digitalWritePin(DigitalPin.P16, 0)
    } else {
        pins.digitalWritePin(DigitalPin.P15, 0)
        pins.analogWritePin(AnalogPin.P16, pd)
    }
}

function arreter() {
    pins.digitalWritePin(DigitalPin.P13, 0)
    pins.digitalWritePin(DigitalPin.P14, 0)
    pins.digitalWritePin(DigitalPin.P15, 0)
    pins.digitalWritePin(DigitalPin.P16, 0)
}

function stylo(baisse: boolean) {
    if (baisse) {
        pins.servoWritePin(AnalogPin.P1, STYLO_BAS)
    } else {
        pins.servoWritePin(AnalogPin.P1, STYLO_HAUT)
    }
    basic.pause(300)
}


// ---------------------------------------------------------------------
// 2. LES VALEURS À RÉGLER
// Une fois trouvées, recopiez-les en haut de vos autres programmes.
// ---------------------------------------------------------------------
let VITESSE = 60        // puissance des moteurs, en %
let TEMPS_90 = 600      // durée (ms) pour tourner de 90°
let CORRECTION = 0      // équilibre gauche/droite pour aller tout droit
let COTE = 1500         // durée (ms) d'un côté du carré de test
let mode = 0            // 0 = réglage du virage, 1 = réglage de la ligne droite


// ---------------------------------------------------------------------
// 3. LES DÉPLACEMENTS (réutilisables dans tous les programmes)
// ---------------------------------------------------------------------
function avancer(duree: number) {
    moteurs(VITESSE + CORRECTION, VITESSE - CORRECTION)
    basic.pause(duree)
    arreter()
    basic.pause(200)
}

function tournerGauche(degres: number) {
    moteurs(0 - VITESSE, VITESSE)
    basic.pause(TEMPS_90 * degres / 90)
    arreter()
    basic.pause(200)
}

function tournerDroite(degres: number) {
    moteurs(VITESSE, 0 - VITESSE)
    basic.pause(TEMPS_90 * degres / 90)
    arreter()
    basic.pause(200)
}


// ---------------------------------------------------------------------
// 4. L'INTERFACE DE RÉGLAGE
// ---------------------------------------------------------------------
function afficherMode() {
    if (mode == 0) {
        basic.showString("V")
    } else {
        basic.showString("L")
    }
}

function afficherValeur() {
    if (mode == 0) {
        basic.showNumber(TEMPS_90)
    } else {
        basic.showNumber(CORRECTION)
    }
}

input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    mode = 1 - mode
    afficherMode()
})

input.onButtonPressed(Button.A, function () {
    if (mode == 0) {
        TEMPS_90 = Math.max(100, TEMPS_90 - 10)
    } else {
        CORRECTION = Math.max(-30, CORRECTION - 1)
    }
    afficherValeur()
})

input.onButtonPressed(Button.B, function () {
    if (mode == 0) {
        TEMPS_90 = TEMPS_90 + 10
    } else {
        CORRECTION = Math.min(30, CORRECTION + 1)
    }
    afficherValeur()
})

input.onButtonPressed(Button.AB, function () {
    basic.showIcon(IconNames.Target)
    basic.pause(1000)                    // le temps de lâcher le robot
    stylo(true)
    if (mode == 0) {
        // Test du virage : un carré. S'il se referme bien, TEMPS_90 est bon.
        for (let i = 0; i < 4; i++) {
            avancer(COTE)
            tournerGauche(90)
        }
    } else {
        // Test de la ligne droite : 3 secondes tout droit.
        avancer(3000)
    }
    stylo(false)
    basic.showIcon(IconNames.Yes)
})

input.onGesture(Gesture.Shake, function () {
    basic.showString("V")
    basic.showNumber(TEMPS_90)
    basic.showString("C")
    basic.showNumber(CORRECTION)
})

// Au démarrage
arreter()
stylo(false)
basic.showIcon(IconNames.Happy)
basic.pause(800)
afficherMode()
