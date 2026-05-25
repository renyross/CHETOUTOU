import os
import re

coussin_files = [
    "coussin-chien.html",
    "coussin-xxl-chien.html",
    "coussin-dehoussable-chien.html",
    "coussin-anti-stress-chien.html",
    "coussin-indestructible-chien.html",
    "coussin-orthopedique-chien.html",
    "grand-coussin-chien.html",
    "panier-coussin-chien.html",
    "coussin-voiture-chien.html",
    "coussin-lavable-chien.html"
]

coussin_carousel = """                    <div class="category-visual-list">
                        <a href="coussin-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper">
                                <img src="cat_coussin_pure.png" alt="Coussin Chien">
                            </div>
                            <div class="category-visual-info"><h3>Classique</h3></div>
                        </a>
                        <a href="coussin-xxl-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper">
                                <img src="cat_coussin_xxl_visual.png" alt="Coussin XXL">
                            </div>
                            <div class="category-visual-info"><h3>Format XXL</h3></div>
                        </a>
                        <a href="coussin-dehoussable-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper">
                                <img src="cat_coussin_dehoussable_visual.png" alt="Coussin Déhoussable">
                            </div>
                            <div class="category-visual-info"><h3>Déhoussable</h3></div>
                        </a>
                        <a href="coussin-anti-stress-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper">
                                <img src="cat_coussin_antistress_visual.png" alt="Coussin Anti-Stress">
                            </div>
                            <div class="category-visual-info"><h3>Anti-Stress</h3></div>
                        </a>
                        <a href="coussin-indestructible-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper">
                                <img src="cat_coussin_indestructible_visual.png" alt="Coussin Indestructible">
                            </div>
                            <div class="category-visual-info"><h3>Indestructible</h3></div>
                        </a>
                        <a href="coussin-orthopedique-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper">
                                <img src="cat_coussin_orthopedique_visual.png" alt="Coussin Orthopédique">
                            </div>
                            <div class="category-visual-info"><h3>Orthopédique</h3></div>
                        </a>
                        <a href="grand-coussin-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper">
                                <img src="cat_coussin_grand_visual.png" alt="Grand Coussin">
                            </div>
                            <div class="category-visual-info"><h3>Grand Format</h3></div>
                        </a>
                        <a href="panier-coussin-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper">
                                <img src="cat_panier_pure.png" alt="Panier Coussin">
                            </div>
                            <div class="category-visual-info"><h3>Panier Coussin</h3></div>
                        </a>
                        <a href="coussin-voiture-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper">
                                <img src="cat_coussin_voiture_visual.png" alt="Coussin Voiture">
                            </div>
                            <div class="category-visual-info"><h3>Pour Voiture</h3></div>
                        </a>
                        <a href="coussin-lavable-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper">
                                <img src="cat_coussin_lavable_visual.png" alt="Coussin Lavable">
                            </div>
                            <div class="category-visual-info"><h3>Lavable</h3></div>
                        </a>
                    </div>"""

def update_file(filename):
    if not os.path.exists(filename):
        print(f"Skipping {filename}: Not found")
        return
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Improved regex to match the entire visual container and its list, including the broken residue
    # We match from <div class="category-visual-list"> until the end of the container </div>\s*</div>
    pattern = r'<div class="category-visual-list">.*?</div>\s*</div>'
    
    # We want to replace the list but keep the container's closing tag
    replacement = coussin_carousel + "\n                </div>"
    
    content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename}")

for f in coussin_files:
    update_file(f)
