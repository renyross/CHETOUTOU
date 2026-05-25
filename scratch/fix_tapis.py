import os
import re

tapis_files = [
    "tapis-chien.html",
    "tapis-rafraichissant-chien.html",
    "tapis-fouille.html",
    "tapis-lechage.html",
    "tapis-absorbant-chien.html",
    "tapis-xxl-chien.html",
    "tapis-gamelle-chien.html",
    "tapis-fraicheur-chien.html",
    "tapis-refrigerant-chien.html"
]

tapis_carousel = """                    <div class="category-visual-list">
                        <a href="tapis-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper">
                                <img src="cat_tapis_chien_visual.png" alt="Tapis pour Chien">
                            </div>
                            <div class="category-visual-info"><h3>Classique</h3></div>
                        </a>
                        <a href="tapis-rafraichissant-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper">
                                <img src="cat_tapis_rafraichissant_visual.png" alt="Tapis Rafraîchissant">
                            </div>
                            <div class="category-visual-info"><h3>Rafraîchissant</h3></div>
                        </a>
                        <a href="tapis-fouille.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper">
                                <img src="cat_tapis_fouille_visual.png" alt="Tapis de Fouille">
                            </div>
                            <div class="category-visual-info"><h3>Jeu de Fouille</h3></div>
                        </a>
                        <a href="tapis-lechage.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper">
                                <img src="cat_tapis_lechage_visual.png" alt="Tapis de Léchage">
                            </div>
                            <div class="category-visual-info"><h3>Léchage</h3></div>
                        </a>
                        <a href="tapis-absorbant-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper">
                                <img src="cat_tapis_chien_visual.png" alt="Tapis Absorbant">
                            </div>
                            <div class="category-visual-info"><h3>Absorbant</h3></div>
                        </a>
                        <a href="tapis-xxl-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper">
                                <img src="cat_tapis_xxl_visual.png" alt="Tapis XXL">
                            </div>
                            <div class="category-visual-info"><h3>Format XXL</h3></div>
                        </a>
                        <a href="tapis-gamelle-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper">
                                <img src="cat_tapis_gamelle_visual.png" alt="Tapis Gamelle">
                            </div>
                            <div class="category-visual-info"><h3>Tapis Gamelle</h3></div>
                        </a>
                        <a href="tapis-fraicheur-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper">
                                <img src="cat_tapis_rafraichissant_visual.png" alt="Tapis Fraîcheur">
                            </div>
                            <div class="category-visual-info"><h3>Fraîcheur</h3></div>
                        </a>
                        <a href="tapis-refrigerant-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper">
                                <img src="cat_tapis_rafraichissant_visual.png" alt="Tapis Réfrigérant">
                            </div>
                            <div class="category-visual-info"><h3>Réfrigérant</h3></div>
                        </a>
                    </div>"""

def update_file(filename):
    if not os.path.exists(filename):
        print(f"Skipping {filename}: Not found")
        return
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    pattern = r'<div class="category-visual-list">.*?</div>\s*</div>'
    replacement = tapis_carousel + "\n                </div>"
    
    content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename}")

for f in tapis_files:
    update_file(f)
