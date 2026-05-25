import os

files_to_update = [
    "laisse-lasso-chien.html",
    "laisses-classiques.html",
    "longue-laisse-chien.html",
    "laisse-longe-chien.html",
    "laisse-chien-velo.html",
    "double-laisse-chien.html",
    "laisse-enrouleur-chien.html",
    "laisse-cuir-chien.html",
    "laisse-corde-chien.html",
    "laisse-main-libre-chien.html"
]

replacements = {
    'img src="laisse_cuir_visual.png"': 'img src="laisse_cuir_visual_1777054118454.png"',
    'img src="laisse_enrouleur_visual.png"': 'img src="laisse_enrouleur_visual_1777054133507.png"',
    'img src="laisse_lasso_visual.png"': 'img src="laisse_lasso_visual_1777054149251.png"',
    'img src="laisse_longe_visual.png"': 'img src="laisse_longe_visual_1777054184718.png"',
    'img src="laisse_velo_visual.png"': 'img src="laisse_velo_visual_1777054197328.png"',
    'img src="laisse_mains_libres_visual.png"': 'img src="laisse_mains_libres_visual_1777054211458.png"',
    'img src="longue_laisse_visual.png"': 'img src="longue_laisse_visual_1777054223972.png"'
}

directory = "/Users/renelrosene/Desktop/boutique chien"

for filename in files_to_update:
    path = os.path.join(directory, filename)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        for old, new in replacements.items():
            content = content.replace(old, new)
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")
    else:
        print(f"File not found: {filename}")
