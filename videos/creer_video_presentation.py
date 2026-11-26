# Construit la scène Blender de la vidéo de présentation de Tartaruga.
#
# Utilisation (depuis un terminal) :
#   blender -b --python videos/creer_video_presentation.py -- build
#   blender -b modeles-3d/tartaruga_presentation.blend -a
#
# Option « stills <dossier> <images...> » : rend quelques images de contrôle.

import bpy, math, os, random, sys

ICI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(ICI)
MODELE = os.path.join(REPO, "modeles-3d", "tartaruga.blend")
SORTIE_BLEND = os.path.join(REPO, "modeles-3d", "tartaruga_presentation.blend")
IMAGES = os.path.join(REPO, "images")
POLICE = r"C:\Windows\Fonts\segoeuib.ttf"

argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []

bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
random.seed(7)

# ---------------------------------------------------------------- couleurs
def hexc(h):
    h = h.lstrip("#")
    def lin(c):
        c /= 255.0
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    return (lin(int(h[0:2], 16)), lin(int(h[2:4], 16)), lin(int(h[4:6], 16)), 1.0)

TEAL, CREME, JAUNE, CORAIL = "0B6E79", "FFF3D6", "FFC531", "F26B5B"
NUIT, ORANGE, VERT, GRIS, BLANC = "1D2B36", "E8902C", "3E8E5A", "6B7A86", "FFFFFF"

_mats = {}
def emat(h):
    if h in _mats:
        return _mats[h]
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
    return m

def imat(fichier):
    m = bpy.data.materials.new("photo_" + fichier)
    try:
        m.use_nodes = True
    except Exception:
        pass
    nt = m.node_tree
    nt.nodes.clear()
    tex = nt.nodes.new("ShaderNodeTexImage")
    tex.image = bpy.data.images.load(os.path.join(IMAGES, fichier))
    em = nt.nodes.new("ShaderNodeEmission")
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    nt.links.new(tex.outputs["Color"], em.inputs["Color"])
    nt.links.new(em.outputs[0], out.inputs["Surface"])
    return m

# ---------------------------------------------------------------- formes (plan XZ, face à la caméra)
def mesh_obj(nom, verts, faces, mat, loc, parent=None):
    me = bpy.data.meshes.new(nom)
    me.from_pydata(verts, [], faces)
    me.update()
    ob = bpy.data.objects.new(nom, me)
    sc.collection.objects.link(ob)
    me.materials.append(mat)
    ob.location = loc
    if parent:
        ob.parent = parent
    return ob

def rect(nom, w, h, r, couleur, loc, parent=None, bas=False):
    z0, z1 = (0, h) if bas else (-h / 2, h / 2)
    v = [(-w / 2, 0, z0), (w / 2, 0, z0), (w / 2, 0, z1), (-w / 2, 0, z1)]
    ob = mesh_obj(nom, v, [[0, 1, 2, 3]], emat(couleur) if isinstance(couleur, str) else couleur, loc, parent)
    if r > 0:
        b = ob.modifiers.new("arrondi", "BEVEL")
        b.affect = "VERTICES"
        b.width = r
        b.segments = 8
    return ob

def disque(nom, r, couleur, loc, n=64):
    v = [(r * math.cos(2 * math.pi * i / n), 0, r * math.sin(2 * math.pi * i / n)) for i in range(n)]
    return mesh_obj(nom, v, [list(range(n))], emat(couleur), loc)

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

def photo(fichier, w, loc, angle=0.0):
    h = w * 1000 / 1600
    cadre = rect("cadre " + fichier, w + 8, h + 8, 3, BLANC, loc)
    mesh_obj("photo " + fichier,
             [(-w / 2, -1, -h / 2), (w / 2, -1, -h / 2), (w / 2, -1, h / 2), (-w / 2, -1, h / 2)],
             [[0, 1, 2, 3]], imat(fichier), (0, 0, 0), cadre)
    me = cadre.children[0].data
    uv = me.uv_layers.new()
    for i, c in enumerate([(0, 0), (1, 0), (1, 1), (0, 1)]):
        uv.data[i].uv = c
    cadre.rotation_euler = (0, math.radians(angle), 0)
    return cadre

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

# ---------------------------------------------------------------- découpage (30 images/s)
SECTIONS = [0, 150, 330, 600, 870, 1110, 1290, 1410]
FONDS = [TEAL, CREME, "BFE6F0", CREME, NUIT, VERT, TEAL]
COINS = [(0, 0), (-200, 112), (200, -112), (200, 112), (-200, -112), (0, 0), (200, 0)]

for k, (coul, (cx, cz)) in enumerate(zip(FONDS, COINS)):
    d = disque("fond %d" % k, 520, coul, (cx, 400 - 10 * k, cz))
    if k > 0:
        f = SECTIONS[k] - 6
        cle(d, "scale", f, (0, 0, 0), "EXPO", "EASE_IN_OUT")
        cle(d, "scale", f + 22, (1, 1, 1))

def fin(k):
    return SECTIONS[k + 1] - 2

Y = -150  # profondeur des textes (devant le robot)

def confettis(n, f0, f_out):
    for i in range(n):
        while True:
            x, z = random.uniform(-190, 190), random.uniform(-105, 105)
            if abs(x) > 130 or abs(z) > 55:
                break
        c = disque("confetti", random.uniform(3, 7), random.choice([JAUNE, CORAIL, CREME, "7FD1AE"]), (x, Y + 5, z), 24)
        pop(c, f0 + 3 * i, f_out)

# ---------- 1. Titre
f0, f1 = SECTIONS[0], fin(0)
pop(texte("Projet Canopé", 30, CREME, (0, Y, 22)), f0 + 8, f1)
barre = rect("souligne", 150, 5, 2.5, JAUNE, (0, Y, 0))
cle(barre, "scale", f0 + 18, (0, 1, 1), "EXPO", "EASE_OUT")
cle(barre, "scale", f0 + 36, (1, 1, 1))
cle(barre, "scale", f1 - 8, (1, 1, 1), "EXPO", "EASE_IN")
cle(barre, "scale", f1, (0, 1, 1))
pop(texte("Un kit de robotique pour les écoles de Corse", 14, CREME, (0, Y, -22)), f0 + 28, f1)
confettis(14, f0 + 12, f1)

# ---------- 2. Le problème
f0, f1 = SECTIONS[1], fin(1)
pop(texte("Les robots éducatifs du commerce sont souvent…", 13, NUIT, (0, Y, 78)), f0 + 14, f1)
cartes = [("Chers", "80 à 150 €\nle robot", CORAIL),
          ("Fragiles", "l'électronique\ncraint les chocs", ORANGE),
          ("Encombrants", "difficiles\nà faire voyager", "2B4A63")]
for i, (mot, detail, coul) in enumerate(cartes):
    c = rect("carte", 118, 74, 8, coul, (-127 + 127 * i, Y + 10, 8))
    texte(mot, 17, BLANC, (0, -1, 12), c)
    texte(detail, 10, BLANC, (0, -1, -16), c)
    pop(c, f0 + 40 + 18 * i, f1)
q = rect("question", 250, 26, 13, JAUNE, (0, Y + 10, -72))
texte("Et si on imprimait notre robot en 3D ?", 13, NUIT, (0, -1, 0), q)
pop(q, f0 + 115, f1, duree=14)

# ---------- 3. Tartaruga en 3D
f0, f1 = SECTIONS[2], fin(2)
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

inclinaison = bpy.data.objects.new("rig inclinaison", None)
rotation = bpy.data.objects.new("rig rotation", None)
sc.collection.objects.link(inclinaison)
sc.collection.objects.link(rotation)
rotation.parent = inclinaison
for ob in robot:
    ob.hide_render = False
    if ob.parent is None or ob.parent not in robot:
        ob.parent = rotation
        ob.matrix_parent_inverse.identity()
inclinaison.location = (0, 0, -54)
inclinaison.rotation_euler = (math.radians(24), 0, 0)

pop(rotation, f0 + 15, f1, s=0.85, duree=16)
cle(rotation, "rotation_euler", f0 + 15, (0, 0, math.radians(215 - 360)), "QUART", "EASE_OUT")
cle(rotation, "rotation_euler", f0 + 140, (0, 0, math.radians(215)))
cle(inclinaison, "location", f0 + 140, (0, 0, -54), "SINE", "EASE_IN_OUT")
cle(inclinaison, "location", f0 + 165, (-88, 0, -58))

carapace = bpy.data.objects["Carapace"]
couvercle = bpy.data.objects["Couvercle"]
cle(carapace, "delta_location", f0 + 150, (0, 0, 0), "BACK", "EASE_OUT")
cle(carapace, "delta_location", f0 + 172, (0, 0, 36))
lev_couv = 14 if couvercle.parent == carapace else 56
cle(couvercle, "delta_location", f0 + 155, (0, 0, 0), "BACK", "EASE_OUT")
cle(couvercle, "delta_location", f0 + 177, (0, 0, lev_couv))

pop(texte("Voici Tartaruga !", 24, NUIT, (0, Y, 90)), f0 + 10, f1)
pop(texte("une tortue robot à imprimer en 3D", 13, NUIT, (0, Y, 68)), f0 + 24, f0 + 146)
pop(texte("Ce qu'il y a dedans :", 13, NUIT, (95, Y, 60)), f0 + 165, f1)
for i, ligne in enumerate(["micro:bit V2 : le cerveau", "2 moteurs et leurs roues",
                           "4 piles AA rechargeables", "un servo qui lève le stylo"]):
    p = rect("puce", 150, 20, 10, BLANC, (95, Y + 10, 36 - 25 * i))
    texte(ligne, 10, NUIT, (0, -1, 0), p)
    pop(p, f0 + 172 + 12 * i, f1)

# ---------- 4. Elle dessine
f0, f1 = SECTIONS[3], fin(3)
pop(texte("Elle dessine ce que les élèves programment !", 13, NUIT, (0, Y, 92)), f0 + 12, f1)
blocs = [("au démarrage", "FFBF00", NUIT, 0),
         ("répéter 5 fois", "FFAB19", BLANC, 0),
         ("avancer de 100", "4C97FF", BLANC, 16),
         ("tourner de 144°", "4C97FF", BLANC, 16),
         ("lever le stylo", "9966FF", BLANC, 0)]
for i, (libelle, coul, ctexte, retrait) in enumerate(blocs):
    w = 112
    b = rect("bloc", w, 20, 5, coul, (-175 + retrait + w / 2, Y + 10, 52 - 26 * i))
    texte(libelle, 11, ctexte, (0, -1, 0), b)
    pop(b, f0 + 28 + 12 * i, f1)

# étoile tracée à la manière de la tortue Logo
L, cap, p = 118, 0.0, [0.0, 0.0]
pts = [tuple(p)]
for _ in range(5):
    p = [p[0] + L * math.cos(cap), p[1] + L * math.sin(cap)]
    pts.append(tuple(p))
    cap += math.radians(144)
xs, zs = [q[0] for q in pts], [q[1] for q in pts]
cx, cz = 92 - (max(xs) + min(xs)) / 2, -12 - (max(zs) + min(zs)) / 2
pts = [(x + cx, z + cz) for x, z in pts]
cu = bpy.data.curves.new("etoile", "CURVE")
cu.dimensions = "2D"
sp = cu.splines.new("POLY")
sp.points.add(len(pts) - 1)
for pt, (x, z) in zip(sp.points, pts):
    pt.co = (x, z, 0, 1)
cu.bevel_depth = 2.4
cu.bevel_resolution = 4
cu.bevel_factor_mapping_end = "SPLINE"
etoile = bpy.data.objects.new("Etoile", cu)
sc.collection.objects.link(etoile)
cu.materials.append(emat(CORAIL))
etoile.location = (0, Y + 20, 0)
etoile.rotation_euler = (math.pi / 2, 0, 0)
D0, D1 = f0 + 95, f0 + 225
cle(cu, "bevel_factor_end", D0 - 1, 0.0)
cle(cu, "bevel_factor_end", D1, 1.0)
pop(etoile, D0 - 2, f1, duree=1)
stylo = disque("pointe", 7, VERT, (0, Y + 15, 0), 32)

for i, (x, z) in enumerate(pts):
    cle(stylo, "location", D0 + (D1 - D0) * i / 5, (x, Y + 15, z))
pop(stylo, D0 - 10, f1)

# ---------- 5. Le coût
f0, f1 = SECTIONS[4], fin(4)
pop(texte("Combien coûte un kit de 8 robots pour une classe ?", 13, CREME, (0, Y, 92)), f0 + 12, f1)
barres = [("Tartaruga\néco", 510, JAUNE), ("Tartaruga", 740, "FFD66B"),
          ("Cutebot", 560, GRIS), ("Blue-Bot", 1170, GRIS), ("mBot2", 1240, GRIS)]
BASE, HMAX = -72, 120
for i, (nom, prix, coul) in enumerate(barres):
    x = -140 + 70 * i
    h = HMAX * prix / 1240
    b = rect("barre", 46, h, 4, coul, (x, Y + 10, BASE), bas=True)
    f = f0 + 30 + 12 * i
    cle(b, "scale", f, (1, 1, 0), "EXPO", "EASE_OUT")
    cle(b, "scale", f + 30, (1, 1, 1))
    cle(b, "scale", f1 - 8, (1, 1, 1), "EXPO", "EASE_IN")
    cle(b, "scale", f1, (1, 1, 0))
    pop(texte(nom, 10, CREME, (x, Y, BASE - 15)), f + 4, f1)
    pop(texte(("%d €" % prix).replace("1170", "1 170").replace("1240", "1 240"), 10, CREME,
              (x, Y, BASE + h + 9)), f + 26, f1)
bandeau = rect("bandeau", 156, 40, 12, CORAIL, (-105, Y + 10, 46))
texte("Environ 2 fois moins cher\nqu'un Blue-Bot ou un mBot2", 10, BLANC, (0, -1, 0), bandeau)
pop(bandeau, f0 + 120, f1, duree=14)
pop(texte("Kit avec rechanges, prix relevés en novembre 2026, à revérifier.", 7.5, "8C9AA6", (0, Y, -106)),
    f0 + 40, f1)

# ---------- 6. Personnalisation
f0, f1 = SECTIONS[5], fin(5)
pop(texte("Chaque classe personnalise sa tortue", 13, CREME, (0, Y, 92)), f0 + 12, f1)
pop(photo("tartaruga_4_famille.png", 180, (-80, Y + 20, -8), angle=-3), f0 + 22, f1, duree=16)
for i, ligne in enumerate(["Carapace aimantée, sans outil", "Couvercle à dessiner soi-même",
                           "Pièces cassées ? On les réimprime"]):
    p = rect("puce", 172, 24, 12, CREME, (108, Y + 10, 34 - 32 * i))
    texte(ligne, 9.5, NUIT, (0, -1, 0), p)
    pop(p, f0 + 50 + 14 * i, f1)

# ---------- 7. Fin
f0, f1 = SECTIONS[6], SECTIONS[7] + 50
pop(texte("Tartaruga", 40, CREME, (0, Y, 22)), f0 + 12)
barre = rect("souligne fin", 170, 5, 2.5, JAUNE, (0, Y, -2))
cle(barre, "scale", f0 + 22, (0, 1, 1), "EXPO", "EASE_OUT")
cle(barre, "scale", f0 + 40, (1, 1, 1))
pop(texte("Projet Canopé · la robotique pour les écoles de Corse", 13, CREME, (0, Y, -22)), f0 + 30)
pop(texte("github.com/Marco2aa/canopee_project", 11, JAUNE, (0, Y, -52)), f0 + 44)
confettis(14, f0 + 14, None)

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

def reglages_video(chemin):
    try:
        r.image_settings.media_type = "VIDEO"
    except Exception:
        pass
    r.image_settings.file_format = "FFMPEG"
    r.ffmpeg.format = "MPEG4"
    r.ffmpeg.codec = "H264"
    r.ffmpeg.constant_rate_factor = "HIGH"
    r.ffmpeg.audio_codec = "NONE"
    r.filepath = chemin

reglages_video(os.path.join(ICI, "frames", "presentation_"))
bpy.ops.wm.save_as_mainfile(filepath=SORTIE_BLEND)
print("SCENE ENREGISTREE", SORTIE_BLEND)

if argv and argv[0] == "stills":
    dossier = argv[1]
    try:
        r.image_settings.media_type = "IMAGE"
    except Exception:
        pass
    r.image_settings.file_format = "PNG"
    r.resolution_percentage = 50
    for f in argv[2:]:
        sc.frame_set(int(f))
        r.filepath = os.path.join(dossier, "test_%04d.png" % int(f))
        bpy.ops.render.render(write_still=True)
        print("RENDU", r.filepath)
