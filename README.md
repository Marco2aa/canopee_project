# Projet Canopé – Kit de robotique pour les écoles de Corse

**Problématique :** comment concevoir un kit de robotique à faible coût, robuste et transportable pour les écoles de Corse ?

Le kit doit permettre aux enseignants de proposer des activités de découverte de la robotique, même sans laboratoire spécialisé ni budget important.

![Tartaruga, le robot tortue imprimable du projet](images/tartaruga_1_heros.png)

🎬 **[Vidéo de présentation du projet (47 s)](videos/tartaruga_presentation.mp4)** · **[Tartaruga dessine une étoile (23 s)](videos/tartaruga_dessine_une_etoile.mp4)**

## Étapes du projet

1. **Comprendre le besoin** : étudier les écoles corses, les contraintes des enseignants et les besoins des élèves.
2. **Effectuer les recherches** : étudier les robots existants, les composants, les matériaux et les prix.
3. **Réaliser le document de veille** : classer les informations et comparer les solutions techniques.
4. **Imaginer plusieurs concepts** : dessiner plusieurs robots, boîtiers et mallettes.
5. **Comparer les résultats** : évaluer le prix, la solidité, le poids, la facilité d'utilisation et la pédagogie.
6. **Améliorer et finaliser** : choisir la meilleure solution et concevoir le kit définitif.

## Les 5 enjeux

| Enjeu | Question |
|---|---|
| Coût | Comment réduire le prix sans sacrifier la qualité des composants ? |
| Robustesse | Comment protéger l'électronique contre les chocs, les manipulations répétées et l'usure ? |
| Transport | Comment concevoir un kit compact, léger et facile à déplacer ? |
| Pédagogie | Comment rendre la robotique accessible aux élèves et aux enseignants ? |
| Autonomie | Comment utiliser le kit sans matériel coûteux ni connaissances techniques avancées ? |

## Où en est le projet ?

| Étape | État | Documents |
|---|---|---|
| 1. Comprendre le besoin | questions prêtes, réponses de Canopé attendues | [Questions de recherche pour le Réseau Canopé](docs/questions-recherche-canope.md) |
| 2-3. Recherches et veille | cartes, solutions existantes, énergie, matériaux et programmation faits | [Cartes électroniques](docs/veille-cartes-electroniques.md) · [Solutions existantes](docs/veille-solutions-existantes.md) · [Énergie, matériaux et programmation](docs/veille-energie-materiaux-programmation.md) |
| 4. Concepts | un robot conçu (Tartaruga) ; autres robots et mallette à faire | [Tartaruga : robot tortue imprimable en 3D](modeles-3d/README.md) · [Pistes pour l'intelligence artificielle](docs/pistes-ia.md) |
| 5. Comparaison | chiffrage fait ; grille de comparaison à faire | [Chiffrage d'un kit pour une classe](docs/chiffrage-kit-classe.md) |
| 6. Finalisation | protocole de test prêt, prototype à imprimer | [Protocole de test du prototype](docs/protocole-tests-prototype.md) · [Programme de calibrage et fiche d'activité](programmes/README.md) |

## Plan du dépôt

```
canopee_project/
├── README.md                  ce fichier
├── docs/                      documents de recherche, de veille et de chiffrage
│   ├── questions-recherche-canope.md
│   ├── veille-cartes-electroniques.md
│   ├── veille-solutions-existantes.md
│   ├── veille-energie-materiaux-programmation.md
│   ├── chiffrage-kit-classe.md
│   ├── protocole-tests-prototype.md
│   └── pistes-ia.md
├── modeles-3d/                robot Tartaruga
│   ├── README.md              présentation, pièces, matériel, coût, montage
│   ├── tartaruga_*.stl        5 pièces à imprimer, déjà orientées
│   ├── tartaruga.blend        modèle Blender complet
│   ├── tartaruga_animation.blend   scène de la vidéo de l'étoile
│   └── tartaruga_presentation.blend   scène de la vidéo de présentation
├── programmes/                programmes MakeCode pour le micro:bit
│   ├── README.md              mode d'emploi et fiche d'activité
│   └── calibrage.ts
├── images/                    rendus 3D de présentation
├── videos/                    vidéos de démonstration et de présentation
│   └── creer_video_presentation.py   script Blender qui construit la vidéo de présentation
├── .mcp.json                  connexion entre Claude Code et Blender
└── .gitignore                 fichiers que Git ignore (sauvegardes de Blender…)
```

## Modélisation 3D (Blender)

Le fichier `.mcp.json` déclare le serveur MCP [blender-mcp](https://github.com/ahujasid/blender-mcp). Il permet à Claude Code de piloter Blender pour modéliser les robots et les mallettes. Il ne fonctionne qu'en local, sur l'ordinateur où Blender est ouvert :

1. Installer `uv` (qui fournit la commande `uvx`).
2. Dans Blender, installer l'extension `addon.py` du dépôt blender-mcp (*Edit > Preferences > Add-ons > Install*), puis l'activer.
3. Dans la barre latérale de la vue 3D (touche `N`), onglet **BlenderMCP**, cliquer sur **Connect to Claude**.
4. Lancer Claude Code dans ce dossier et accepter le serveur MCP `blender`.
