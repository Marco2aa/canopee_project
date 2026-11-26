# Construit la scène Blender de la vidéo « Tartaruga apprend » (les 4 pistes d'IA).
#
# Utilisation :
#   blender -b --python videos/creer_video_ia.py -- build
#   blender -b modeles-3d/tartaruga_ia.blend -a
# Option « stills <dossier> <images...> » : rend quelques images de contrôle.

import bpy, math, os, random, sys

ICI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(ICI)
MODELE = os.path.join(REPO, "modeles-3d", "tartaruga.blend")
SORTIE_BLEND = os.path.join(REPO, "modeles-3d", "tartaruga_ia.blend")
POLICE = r"C:\Windows\Fonts\segoeuib.ttf"

argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []

bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
random.seed(11)

# ---------------------------------------------------------------- couleurs et matériaux
def hexc(h):
    h = h.lstrip("#")
    def lin(c):
        c /= 255.0
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    return (lin(int(h[0:2], 16)), lin(int(h[2:4], 16)), lin(int(h[4:6], 16)), 1.0)

TEAL, CREME, JAUNE, CORAIL = "0B6E79", "FFF3D6", "FFC531", "F26B5B"
NUIT, VIOLET, BLEU, VERT, BLANC = "1D2B36", "4B3A8C", "4C97FF", "3FB37F", "FFFFFF"
ROUGE_LED, LED_ETEINTE = "FF4D4D", "34404A"

_mats = {}
def emat(h):
    if h not in _mats:
        m = bpy.data.materials.new("aplat_" + h)
        try:
            m.use_nodes = True
        except Exception:
            pass
        nt = m.node_tree
        nt.nodes.clear()
        em = nt.nodes.new("ShaderNodeEmission")
        em.inputs["Color"].default_value = hexc(h)
        out = nt.nodes.new("ShaderNodeOutputMaterial")
        nt.links.new(em.outputs[0], out.inputs["Surface"])
        _mats[h] = m
    return _mats[h]

# ---------------------------------------------------------------- formes (plan XZ, face à la caméra)
def mesh_obj(nom, verts, faces, couleur, loc, parent=None):
    me = bpy.data.meshes.new(nom)
    me.from_pydata(verts, [], faces)
    me.update()
    ob = bpy.data.objects.new(nom, me)
    sc.collection.objects.link(ob)
    me.materials.append(emat(couleur))
    ob.location = loc
    if parent:
        ob.parent = parent
    return ob

def rect(nom, w, h, r, couleur, loc, parent=None, ancre="centre"):
    x0, x1, z0, z1 = -w / 2, w / 2, -h / 2, h / 2
    if ancre == "bas":
        z0, z1 = 0, h
    if ancre == "gauche":
        x0, x1 = 0, w
    v = [(x0, 0, z0), (x1, 0, z0), (x1, 0, z1), (x0, 0, z1)]
    ob = mesh_obj(nom, v, [[0, 1, 2, 3]], couleur, loc, parent)
    if r > 0:
        b = ob.modifiers.new("arrondi", "BEVEL")
        b.affect = "VERTICES"
        b.width = r
        b.segments = 8
    return ob

def disque(nom, r, couleur, loc, n=48, parent=None):
    v = [(r * math.cos(2 * math.pi * i / n), 0, r * math.sin(2 * math.pi * i / n)) for i in range(n)]
    return mesh_obj(nom, v, [list(range(n))], couleur, loc, parent)

def anneau(nom, r, e, couleur, loc, n=64):
    v = []
    for i in range(n):
        a = 2 * math.pi * i / n
        v += [((r + e / 2) * math.cos(a), 0, (r + e / 2) * math.sin(a)),
              ((r - e / 2) * math.cos(a), 0, (r - e / 2) * math.sin(a))]
    f = [[2 * i, 2 * ((i + 1) % n), 2 * ((i + 1) % n) + 1, 2 * i + 1] for i in range(n)]
    return mesh_obj(nom, v, f, couleur, loc)

def trapeze(nom, haut, bas, h, couleur, loc):
    v = [(-bas / 2, 0, -h / 2), (bas / 2, 0, -h / 2), (haut / 2, 0, h / 2), (-haut / 2, 0, h / 2)]
    return mesh_obj(nom, v, [[0, 1, 2, 3]], couleur, loc)

police = bpy.data.fonts.load(POLICE)

def texte(corps, taille, couleur, loc, parent=None, align="CENTER"):
    cu = bpy.data.curves.new("txt", "FONT")
    cu.body = corps
    cu.font = police
    cu.size = taille
    cu.align_x = align
    cu.align_y = "CENTER"
    ob = bpy.data.objects.new("T " + corps[:20], cu)
    sc.collection.objects.link(ob)
    cu.materials.append(emat(couleur))
    ob.rotation_euler = (math.pi / 2, 0, 0)
    ob.location = loc
    if parent:
        ob.parent = parent
    return ob

def pilule(corps, w, h, taille, fond, coul_txt, loc):
    p = rect("pilule", w, h, h / 2 - 0.5, fond, loc)
    texte(corps, taille, coul_txt, (0, -1, 0), p)
    return p

# ---------------------------------------------------------------- animation
def fcourbes(idb):
    ad = idb.animation_data
    act = ad.action
    try:
        return list(act.fcurves)
    except AttributeError:
        from bpy_extras import anim_utils
        return list(anim_utils.action_get_channelbag_for_slot(act, ad.action_slot).fcurves)

def cle(idb, chemin, image, valeur, interp="LINEAR", easing="AUTO"):
    setattr(idb, chemin, valeur)
    idb.keyframe_insert(chemin, frame=image)
    for fc in fcourbes(idb):
        if fc.data_path == chemin:
            for kp in fc.keyframe_points:
                if abs(kp.co.x - image) < 0.01:
                    kp.interpolation = interp
                    kp.easing = easing

def pop(ob, f_in, f_out=None, s=1.0, duree=12):
    S = (s, s, s)
    cle(ob, "scale", f_in, (0, 0, 0), "BACK", "EASE_OUT")
    cle(ob, "scale", f_in + duree, S)
    if f_out:
        cle(ob, "scale", f_out - 8, S, "EXPO", "EASE_IN")
        cle(ob, "scale", f_out, (0, 0, 0))

def trajet(ob, points, y):
    """points : liste de (image, x, z, interpolation)."""
    for f, x, z, interp in points:
        cle(ob, "location", f, (x, y, z), interp, "EASE_IN_OUT" if interp == "SINE" else "AUTO")

# ---------------------------------------------------------------- découpage (30 images/s)
SECTIONS = [0, 150, 330, 610, 870, 1170, 1470, 1800, 1980]
FONDS = [VIOLET, CREME, "BFE6F0", NUIT, "CDEBD3", CREME, TEAL, VIOLET]
COINS = [(0, 0), (-200, 112), (200, -112), (200, 112), (-200, -112), (0, 0), (-200, 0), (200, 0)]
for k, (coul, (cx, cz)) in enumerate(zip(FONDS, COINS)):
    d = disque("fond %d" % k, 520, coul, (cx, 400 - 10 * k, cz), 96)
    if k > 0:
        f = SECTIONS[k] - 6
        cle(d, "scale", f, (0, 0, 0), "EXPO", "EASE_IN_OUT")
        cle(d, "scale", f + 22, (1, 1, 1))

def fin(k):
    return SECTIONS[k + 1] - 2

Y = -150

def titre(corps, couleur, f0, f1):
    pop(texte(corps, 15, couleur, (0, Y, 94)), f0 + 10, f1)

def confettis(n, f0, f_out):
    for i in range(n):
        while True:
            x, z = random.uniform(-190, 190), random.uniform(-105, 105)
            if abs(x) > 150 or abs(z) > 60:
                break
        c = disque("confetti", random.uniform(3, 7), random.choice([JAUNE, CORAIL, CREME, "7FD1AE", BLEU]), (x, Y + 5, z), 24)
        pop(c, f0 + 3 * i, f_out)

# ---------------------------------------------------------------- robot (réutilisé dans les parties 1 et 3)
with bpy.data.libraries.load(MODELE, link=False) as (src, dst):
    dst.collections = [c for c in src.collections if c.startswith("Tartaruga")]
    dst.objects = ["LED sourire"]
robot = []
for col in dst.collections:
    col.hide_render = False
    sc.collection.children.link(col)
    robot += list(col.objects)
for ob in dst.objects:
    sc.collection.objects.link(ob)
    robot.append(ob)

base = bpy.data.objects.new("rig base", None)        # position à l'écran et roulis
incl = bpy.data.objects.new("rig inclinaison", None)  # vue de 3/4 dessus
spin = bpy.data.objects.new("rig rotation", None)     # cap du robot et taille
for e in (base, incl, spin):
    sc.collection.objects.link(e)
incl.parent, spin.parent = base, incl
for ob in robot:
    ob.hide_render = False
    if ob.parent is None or ob.parent not in robot:
        ob.parent = spin
        ob.matrix_parent_inverse.identity()
incl.location = (0, 0, -45)
incl.rotation_euler = (math.radians(24), 0, 0)
cle(spin, "scale", 0, (0, 0, 0), "CONSTANT")

# ---------- 0. Titre
f0, f1 = SECTIONS[0], fin(0)
pop(texte("Tartaruga apprend !", 30, CREME, (0, Y, 22)), f0 + 8, f1)
barre = rect("souligne", 170, 5, 2.5, JAUNE, (0, Y, 0))
cle(barre, "scale", f0 + 18, (0, 1, 1), "EXPO", "EASE_OUT")
cle(barre, "scale", f0 + 36, (1, 1, 1))
cle(barre, "scale", f1 - 8, (1, 1, 1), "EXPO", "EASE_IN")
cle(barre, "scale", f1, (0, 1, 1))
pop(texte("4 activités pour comprendre l'intelligence artificielle", 12, CREME, (0, Y, -22)), f0 + 28, f1)
confettis(14, f0 + 12, f1)

# ---------- 1. L'idée
f0, f1 = SECTIONS[1], fin(1)
titre("Une IA, ça ne se programme pas comme d'habitude", NUIT, f0, f1)
for i, (haut, bas, coul) in enumerate([
        ("Programme classique", "on écrit les règles :\n« si penché, alors avance »", NUIT),
        ("Intelligence artificielle", "on montre des exemples :\nelle trouve les règles seule", "6A4FC4")]):
    c = rect("carte", 170, 84, 10, coul, (-92 + 184 * i, Y + 10, 12))
    texte(haut, 14, JAUNE if i else CREME, (0, -1, 20), c)
    texte(bas, 10, BLANC, (0, -1, -14), c)
    pop(c, f0 + 30 + 25 * i, f1)
pop(pilule("Avec Tartaruga, 4 activités pour le découvrir", 300, 26, 12, JAUNE, NUIT, (0, Y + 10, -72)),
    f0 + 110, f1, duree=14)

# ---------- 2. Piste 1 : la télécommande par gestes
f0, f1 = SECTIONS[2], fin(2)
titre("1 · La télécommande par gestes", NUIT, f0, f1)
carte = rect("micro:bit", 74, 58, 6, NUIT, (-120, Y + 10, -5))
rect("connecteur", 74, 8, 2, "D4A72C", (0, -0.5, -29), carte)
fleche = ["..#..", ".###.", "#.#.#", "..#..", "..#.."]
for li, ligne in enumerate(fleche):
    for co, ch in enumerate(ligne):
        rect("led", 5, 5, 0, ROUGE_LED if ch == "#" else LED_ETEINTE,
             (-16 + 8 * co, -1, 23 - 8 * li), carte)
texte("micro:bit", 6, CREME, (0, -1, -16), carte)
pop(carte, f0 + 22, f1)
pop(texte("dans la main", 9, NUIT, (-120, Y, -48)), f0 + 30, f1)

# robot, vu de profil, qui avance vers la droite
cle(base, "location", f0, (75, 0, -5), "CONSTANT")
cle(base, "rotation_euler", f0, (0, 0, 0), "CONSTANT")
cle(spin, "rotation_euler", f0, (0, 0, math.radians(-90)), "CONSTANT")
pop(spin, f0 + 26, f1, s=0.62, duree=16)

gestes = [("pencher en avant  →  avancer", "pencher"),
          ("tourner le poignet  →  tourner", "tourner"),
          ("secouer  →  lever le stylo", "secouer")]
feutre = bpy.data.objects["Feutre"]
bague = bpy.data.objects["Bague feutre"]
for gi, (libelle, geste) in enumerate(gestes):
    g = f0 + 60 + 70 * gi
    pop(pilule(libelle, 230, 24, 11, BLANC, NUIT, (0, Y + 10, 62)), g, g + 66)
    if geste == "pencher":
        cle(carte, "rotation_euler", g + 2, (0, 0, 0), "BACK", "EASE_OUT")
        cle(carte, "rotation_euler", g + 12, (0, math.radians(28), 0), "LINEAR")
        cle(carte, "rotation_euler", g + 34, (0, math.radians(28), 0), "SINE", "EASE_IN_OUT")
        cle(carte, "rotation_euler", g + 44, (0, 0, 0))
        cle(base, "location", g + 18, (75, 0, -5), "SINE", "EASE_IN_OUT")
        cle(base, "location", g + 50, (115, 0, -5))
    elif geste == "tourner":
        for j, a in enumerate([0, -22, 22, -22, 0]):
            cle(carte, "rotation_euler", g + 2 + 6 * j, (0, math.radians(a), 0), "SINE", "EASE_IN_OUT")
        cle(spin, "rotation_euler", g + 18, (0, 0, math.radians(-90)), "BACK", "EASE_OUT")
        cle(spin, "rotation_euler", g + 42, (0, 0, math.radians(0)))
    else:
        for j in range(9):
            dx = 0 if j in (0, 8) else (7 if j % 2 else -7)
            cle(carte, "location", g + 2 + 3 * j, (-120 + dx, Y + 10, -5))
        for ob in (feutre, bague):
            if ob.parent in robot and ob.parent is not spin:
                continue
            cle(ob, "delta_location", g + 18, (0, 0, 0), "BACK", "EASE_OUT")
            cle(ob, "delta_location", g + 30, (0, 0, 14))
        texte_stylo = texte("stylo levé !", 10, CORAIL, (120, Y, -70))
        pop(texte_stylo, g + 26, g + 66)
    for k in range(3):
        o = anneau("onde", 12, 3, BLEU, (-60, Y + 5, -5))
        t = g + 10 + 6 * k
        cle(o, "scale", 0, (0, 0, 0), "CONSTANT")
        cle(o, "scale", t, (0.2, 0.2, 0.2), "QUAD", "EASE_OUT")
        cle(o, "scale", t + 16, (1.6, 1.6, 1.6), "CONSTANT")
        cle(o, "scale", t + 17, (0, 0, 0), "CONSTANT")
for ob in (feutre, bague):
    if ob.animation_data:
        cle(ob, "delta_location", f1, (0, 0, 0), "CONSTANT")
cle(base, "location", f1, (-55, 0, -5), "CONSTANT")
cle(spin, "rotation_euler", f1, (0, 0, math.radians(215)), "CONSTANT")
cle(carte, "rotation_euler", f1, (0, 0, 0), "CONSTANT")

# ---------- 3. Comment l'IA apprend
f0, f1 = SECTIONS[3], fin(3)
titre("Comment l'IA apprend-elle ?", CREME, f0, f1)
etapes = [("1. Collecter des exemples", f0 + 18), ("2. Entraîner le modèle", f0 + 95),
          ("3. Tester un geste nouveau", f0 + 145), ("4. Programmer la tortue", f0 + 195)]
for i, (lib, t) in enumerate(etapes):
    pop(pilule(lib, 136, 22, 9.5, CREME, NUIT, (-128, Y + 10, 52 - 30 * i)), t, f1)
CX, CZ = 60, -5
amas = [("avancer", CORAIL, (-48, 30), (-98, 30)), ("tourner", BLEU, (52, 25), (106, 25)),
        ("stylo", VERT, (5, -55), (55, -55))]
points = []
for nom, coul, (ax, az), _ in amas:
    for j in range(10):
        points.append((coul, CX + ax + random.gauss(0, 8), CZ + az + random.gauss(0, 7)))
random.shuffle(points)
for j, (coul, x, z) in enumerate(points):
    pop(disque("point", 3.6, coul, (x, Y + 5, z), 24), f0 + 25 + 2 * j, f1, duree=8)
for nom, coul, (ax, az), (lx, lz) in amas:
    pop(anneau("modele " + nom, 26, 2.5, coul, (CX + ax, Y + 6, CZ + az)), f0 + 100, f1, duree=16)
    pop(texte(nom, 10, coul, (CX + lx, Y, CZ + lz + (0 if nom != "stylo" else 0))), f0 + 108, f1)
nouveau = disque("geste nouveau", 6, BLANC, (CX - 50, Y + 2, 112), 32)
cle(nouveau, "location", f0 + 150, (CX - 30, Y + 2, 112), "EXPO", "EASE_OUT")
cle(nouveau, "location", f0 + 170, (CX - 48, Y + 2, CZ + 30))
pop(nouveau, f0 + 148, f1)
pop(pilule("Geste reconnu : avancer !", 170, 22, 10, JAUNE, NUIT, (CX + 40, Y + 10, 70)), f0 + 172, f1)
bloc = rect("bloc", 136, 34, 5, BLEU, (-128, Y + 10, -88))
texte("quand « avancer » est reconnu\n   avancer de 100", 8.5, BLANC, (0, -1, 0), bloc)
pop(bloc, f0 + 205, f1)

# ---------- 4. Piste 2 : la tortue qui ressent
f0, f1 = SECTIONS[4], fin(4)
titre("2 · La tortue qui ressent", NUIT, f0, f1)
pop(spin, f0 + 20, f1, s=0.8, duree=16)
panneau = rect("visage", 104, 104, 10, NUIT, (110, Y + 15, -2))
for li in range(5):
    for co in range(5):
        rect("led eteinte", 13, 13, 2, LED_ETEINTE, (-36 + 18 * co, -1, 36 - 18 * li), panneau)
pop(panneau, f0 + 24, f1)
VISAGES = {
    "calme":    [".....", ".#.#.", ".....", ".....", "....."],
    "sourire":  [".....", ".#.#.", ".....", "#...#", ".###."],
    "surprise": [".#.#.", ".....", "..#..", ".#.#.", "..#.."],
    "triste":   [".....", ".#.#.", ".....", ".###.", "#...#"],
}
t1, t2, t3 = f0 + 55, f0 + 125, f0 + 195
cle(base, "location", f0, (-55, 0, -14), "CONSTANT")
programme = [(f0 + 34, "calme"), (t1 + 6, "sourire"), (t2 + 4, "surprise"),
             (t3 + 8, "triste"), (t3 + 72, "calme"), (f1 - 8, None)]
for li in range(5):
    for co in range(5):
        led = rect("led", 13, 13, 2, ROUGE_LED, (110 - 36 + 18 * co, Y + 10, -2 + 36 - 18 * li))
        cle(led, "scale", 0, (0, 0, 0), "CONSTANT")
        for t, v in programme:
            allume = v is not None and VISAGES[v][li][co] == "#"
            cle(led, "scale", t, (1, 1, 1) if allume else (0, 0, 0), "CONSTANT")
actions = [(t1, "On la soulève…", "elle sourit"), (t2, "On la secoue…", "elle est surprise"),
           (t3, "On la retourne…", "elle est triste")]
for t, action, emotion in actions:
    pop(pilule(action, 170, 24, 11, BLANC, NUIT, (-60, Y + 10, 68)), t, t + 66)
    pop(texte(emotion, 11, NUIT, (110, Y, -70)), t + 8, t + 66)
# mouvements du robot
cle(base, "location", t1, (-55, 0, -14), "BACK", "EASE_OUT")
cle(base, "location", t1 + 14, (-55, 0, 6), "LINEAR")
cle(base, "location", t1 + 40, (-55, 0, 6), "BOUNCE", "EASE_OUT")
cle(base, "location", t1 + 56, (-55, 0, -14), "LINEAR")
for j in range(9):
    dx = 0 if j in (0, 8) else (9 if j % 2 else -9)
    cle(base, "location", t2 + 3 * j, (-55 + dx, 0, -14), "SINE", "EASE_IN_OUT")
cle(base, "rotation_euler", t3, (0, 0, 0), "BACK", "EASE_OUT")
cle(base, "rotation_euler", t3 + 18, (0, math.pi, 0), "LINEAR")
cle(base, "rotation_euler", t3 + 52, (0, math.pi, 0), "BACK", "EASE_OUT")
cle(base, "rotation_euler", t3 + 70, (0, 0, 0))
pop(pilule("Rien à acheter : le micro:bit est déjà dans la tortue", 300, 24, 11, JAUNE, NUIT, (0, Y + 10, 68)),
    t3 + 70, f1)

# ---------- 5. Piste 3 : les biais
f0, f1 = SECTIONS[5], fin(5)
titre("3 · Pourquoi l'IA ne me comprend pas ?", NUIT, f0, f1)
eleves = [("Léa", CORAIL, 10, 0.9, 0.9), ("Sami", BLEU, -40, 0.3, 0.8)]
for nom, coul, z, a, b in eleves:
    av = disque("tete", 10, coul, (-168, Y + 10, z + 9), 32)
    rect("corps", 30, 16, 8, coul, (0, 0, -19), av)
    texte(nom, 9, NUIT, (26, -1, -6), av)
    pop(av, f0 + 22, f1)
    rect("fond barre", 240, 22, 8, "E6D9BC", (-112, Y + 12, z), ancre="gauche")
    barre = rect("barre", 240, 22, 8, coul, (-112, Y + 10, z), ancre="gauche")
    cle(barre, "scale", 0, (0, 1, 1), "CONSTANT")
    cle(barre, "scale", f0 + 50, (0, 1, 1), "EXPO", "EASE_OUT")
    cle(barre, "scale", f0 + 78, (a, 1, 1), "CONSTANT")
    cle(barre, "scale", f0 + 170, (a, 1, 1), "EXPO", "EASE_OUT")
    cle(barre, "scale", f0 + 196, (b, 1, 1), "CONSTANT")
    cle(barre, "scale", f1 - 8, (b, 1, 1), "EXPO", "EASE_IN")
    cle(barre, "scale", f1, (0, 1, 1))
    if a == b:
        pop(texte("%d / 10" % round(a * 10), 11, NUIT, (-112 + 240 * a + 24, Y, z)), f0 + 80, f1)
    else:
        pop(texte("%d / 10" % round(a * 10), 11, NUIT, (-112 + 240 * a + 24, Y, z)), f0 + 80, f0 + 168)
        pop(texte("%d / 10" % round(b * 10), 11, NUIT, (-112 + 240 * b + 24, Y, z)), f0 + 198, f1)
# fonds gris des barres : apparition avec les avatars
for ob in [o for o in sc.objects if o.name.startswith("fond barre")]:
    pop(ob, f0 + 26, f1)
pop(texte("Gestes reconnus sur 10 essais, avec un modèle entraîné par…", 10, NUIT, (0, Y, 66)), f0 + 30, f1)
pop(pilule("Léa toute seule", 150, 22, 10, CORAIL, BLANC, (0, Y + 10, 46)), f0 + 40, f0 + 165)
pop(pilule("tout le groupe", 150, 22, 10, "6A4FC4", BLANC, (0, Y + 10, 46)), f0 + 165, f1)
pop(pilule("Une IA ne vaut que par ses exemples", 260, 26, 12, JAUNE, NUIT, (0, Y + 10, -78)), f0 + 230, f1)
pop(texte("Chiffres donnés pour illustrer", 7, "8C7F66", (0, Y, -104)), f0 + 60, f1)

# ---------- 6. Piste 4 : le labyrinthe débranché
f0, f1 = SECTIONS[6], fin(6)
titre("4 · Le labyrinthe, sans écran", CREME, f0, f1)
S, A, D1, B, D2, E = (-160, -20), (-80, -20), (-80, 52), (20, -20), (20, -88), (115, -20)
couloirs = [rect("couloir", 299, 26, 13, "128A96", (-22.5, Y + 30, -20)),
            rect("couloir", 26, 98, 13, "128A96", (-80, Y + 30, 16)),
            rect("couloir", 26, 94, 13, "128A96", (20, Y + 30, -54))]
for c in couloirs:
    pop(c, f0 + 20, f1)
pop(texte("départ", 9, CREME, (-160, Y, -44)), f0 + 26, f1)
pop(texte("sortie", 10, JAUNE, (115, Y, -44)), f0 + 26, f1)
pop(texte("jeton rouge : monter ou descendre     jeton bleu : tout droit", 8.5, CREME, (0, Y, 77)), f0 + 30,
    f0 + 282)

def gobelet(cx, cz, lettre):
    g = trapeze("gobelet", 44, 32, 40, "F2C14E", (cx, Y + 20, cz))
    pop(g, f0 + 34, f1)
    pop(texte("gobelet " + lettre, 8, CREME, (cx, Y, cz - 28)), f0 + 38, f1)
    jetons = []
    for j, coul in enumerate([CORAIL, CORAIL, BLEU, BLEU]):
        jt = disque("jeton", 4, coul, (cx - 13.5 + 9 * j, Y + 15, cz - 12), 24)
        jetons.append(jt)
    return jetons

jA = gobelet(-140, 38, "A")
jB = gobelet(70, -70, "B")
for jt in jA + jB:
    pop(jt, f0 + 42, f1, duree=8)
pop(texte("A", 11, CREME, (-80, Y + 5, -20)), f0 + 30, f0 + 50)
pop(texte("B", 11, CREME, (20, Y + 5, -20)), f0 + 30, f0 + 50)

def ajouter_jetons(cx, cz, t, couleurs, rang):
    for j, coul in enumerate(couleurs):
        jt = disque("jeton gagné", 4, coul, (cx - 13.5 + 9 * j, Y + 15, cz - 12 + 9 * rang), 24)
        pop(jt, t + 4 * j, f1, duree=10)

tortue = disque("tortue", 8, VERT, (S[0], Y + 10, S[1]), 32)
rect("tete", 7, 7, 3.4, VERT, (8, 0, 0), tortue)
pop(tortue, f0 + 44, f1)
p1 = f0 + 60
trajet(tortue, [(p1, *S, "LINEAR"), (p1 + 16, *A, "LINEAR"), (p1 + 32, *D1, "CONSTANT"),
                (p1 + 62, *S, "CONSTANT")], Y + 10)
cle(jA[0], "scale", p1 + 14, (1, 1, 1), "EXPO", "EASE_IN")
cle(jA[0], "scale", p1 + 22, (0, 0, 0), "CONSTANT")
cle(jA[0], "scale", f1 - 8, (0, 0, 0), "CONSTANT")
croix = texte("×", 34, CORAIL, (-80, Y, 52))
pop(croix, p1 + 32, p1 + 62)
pop(pilule("Partie 1 : cul-de-sac\nle jeton rouge est perdu", 120, 36, 8.5, CORAIL, BLANC, (136, Y + 10, 30)),
    p1 + 30, p1 + 92)
p2 = f0 + 160
trajet(tortue, [(p2, *S, "LINEAR"), (p2 + 14, *A, "LINEAR"), (p2 + 30, *B, "LINEAR"),
                (p2 + 46, *E, "CONSTANT"), (p2 + 90, *S, "CONSTANT")], Y + 10)
etoile = anneau("bravo", 16, 4, JAUNE, (115, Y + 5, -20))
pop(etoile, p2 + 46, p2 + 90)
pop(pilule("Partie 2 : la sortie !\non gagne un jeton bleu", 120, 36, 8.5, JAUNE, NUIT, (136, Y + 10, 30)),
    p2 + 44, p2 + 88)
ajouter_jetons(-140, 38, p2 + 56, [BLEU], 1)
ajouter_jetons(70, -70, p2 + 60, [BLEU], 1)
p3 = f0 + 252
ajouter_jetons(-140 + 9, 38, p3 - 6, [BLEU, BLEU], 1)
ajouter_jetons(70 + 9, -70, p3 - 2, [BLEU, BLEU], 1)
trajet(tortue, [(p3, *S, "LINEAR"), (p3 + 10, *A, "LINEAR"), (p3 + 20, *B, "LINEAR"),
                (p3 + 30, *E, "CONSTANT")], Y + 10)
pop(pilule("Partie 10 : elle trouve\nla sortie à chaque fois", 120, 36, 8.5, VERT, BLANC, (136, Y + 10, 30)),
    p3, f1)
pop(pilule("Récompense et punition : l'apprentissage par renforcement", 330, 24, 10.5, CREME, NUIT,
           (0, Y + 10, 74)), p3 + 32, f1)

# ---------- 7. Fin
f0 = SECTIONS[7]
pop(texte("Les élèves ne se contentent pas d'utiliser l'IA :", 13, CREME, (0, Y, 40)), f0 + 12)
pop(texte("ils la fabriquent, la testent et la questionnent.", 13.5, JAUNE, (0, Y, 16)), f0 + 26)
barre = rect("souligne fin", 170, 4, 2, JAUNE, (0, Y, -8))
cle(barre, "scale", f0 + 36, (0, 1, 1), "EXPO", "EASE_OUT")
cle(barre, "scale", f0 + 54, (1, 1, 1))
pop(texte("Tartaruga · Projet Canopé", 12, CREME, (0, Y, -30)), f0 + 44)
pop(texte("github.com/Marco2aa/canopee_project", 9, "CBB8FF", (0, Y, -52)), f0 + 54)
confettis(14, f0 + 20, None)

# les aplats ne doivent pas se refléter sur la carapace brillante du robot
for ob in sc.objects:
    if ob not in robot and ob.type in {"MESH", "FONT", "CURVE"}:
        ob.visible_glossy = False
        ob.visible_shadow = False

# ---------------------------------------------------------------- caméra, lumière, rendu
cam_data = bpy.data.cameras.new("Camera")
cam_data.type = "ORTHO"
cam_data.ortho_scale = 400
cam_data.clip_start = 1
cam_data.clip_end = 5000
cam = bpy.data.objects.new("Camera", cam_data)
sc.collection.objects.link(cam)
cam.location = (0, -1000, 0)
cam.rotation_euler = (math.pi / 2, 0, 0)
sc.camera = cam

for nom, energie, rot in [("Soleil", 4.0, (50, 0, -30)), ("Contre-jour", 1.5, (-60, 0, 150))]:
    ld = bpy.data.lights.new(nom, "SUN")
    ld.energy = energie
    lo = bpy.data.objects.new(nom, ld)
    sc.collection.objects.link(lo)
    lo.rotation_euler = tuple(math.radians(a) for a in rot)

monde = bpy.data.worlds.new("Monde")
sc.world = monde
try:
    monde.use_nodes = True
except Exception:
    pass
fond = next(n for n in monde.node_tree.nodes if n.type == "BACKGROUND")
fond.inputs[0].default_value = (0.55, 0.55, 0.55, 1)

r = sc.render
try:
    r.engine = "BLENDER_EEVEE"
except TypeError:
    r.engine = "BLENDER_EEVEE_NEXT"
sc.eevee.taa_render_samples = 24
sc.view_settings.view_transform = "Standard"
sc.view_settings.look = "None"
r.resolution_x, r.resolution_y, r.resolution_percentage = 1280, 720, 100
r.fps = 30
sc.frame_start, sc.frame_end = 1, SECTIONS[-1]
try:
    r.image_settings.media_type = "VIDEO"
except Exception:
    pass
r.image_settings.file_format = "FFMPEG"
r.ffmpeg.format = "MPEG4"
r.ffmpeg.codec = "H264"
r.ffmpeg.constant_rate_factor = "HIGH"
r.ffmpeg.audio_codec = "NONE"
r.filepath = os.path.join(ICI, "frames", "ia_")

bpy.ops.wm.save_as_mainfile(filepath=SORTIE_BLEND)
print("SCENE ENREGISTREE", SORTIE_BLEND)

if argv and argv[0] == "stills":
    try:
        r.image_settings.media_type = "IMAGE"
    except Exception:
        pass
    r.image_settings.file_format = "PNG"
    r.resolution_percentage = 50
    for f in argv[2:]:
        sc.frame_set(int(f))
        r.filepath = os.path.join(argv[1], "ia_%04d.png" % int(f))
        bpy.ops.render.render(write_still=True)
        print("RENDU", r.filepath)
