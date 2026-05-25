import os
import re

# --- Data Definition ---

CAT_CARDS = {
    "tapis": """                        <a href="tapis-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper"><img src="cat_tapis_chien_visual.png" alt="Tapis pour Chien"></div>
                            <div class="category-visual-info"><h3>Classique</h3></div>
                        </a>
                        <a href="tapis-rafraichissant-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper"><img src="cat_tapis_rafraichissant_visual.png" alt="Tapis Rafraîchissant"></div>
                            <div class="category-visual-info"><h3>Rafraîchissant</h3></div>
                        </a>
                        <a href="tapis-fouille.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper"><img src="cat_tapis_fouille_visual.png" alt="Tapis de Fouille"></div>
                            <div class="category-visual-info"><h3>Jeu de Fouille</h3></div>
                        </a>
                        <a href="tapis-lechage.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper"><img src="cat_tapis_lechage_visual.png" alt="Tapis de Léchage"></div>
                            <div class="category-visual-info"><h3>Léchage</h3></div>
                        </a>
                        <a href="tapis-absorbant-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper"><img src="cat_tapis_chien_visual.png" alt="Tapis Absorbant"></div>
                            <div class="category-visual-info"><h3>Absorbant</h3></div>
                        </a>
                        <a href="tapis-xxl-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper"><img src="cat_tapis_xxl_visual.png" alt="Tapis XXL"></div>
                            <div class="category-visual-info"><h3>Format XXL</h3></div>
                        </a>
                        <a href="tapis-gamelle-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper"><img src="cat_tapis_gamelle_visual.png" alt="Tapis Gamelle"></div>
                            <div class="category-visual-info"><h3>Espace Repas</h3></div>
                        </a>
                        <a href="tapis-fraicheur-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper"><img src="cat_tapis_rafraichissant_visual.png" alt="Tapis Fraîcheur"></div>
                            <div class="category-visual-info"><h3>Fraîcheur</h3></div>
                        </a>
                        <a href="tapis-refrigerant-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper"><img src="cat_tapis_rafraichissant_visual.png" alt="Tapis Réfrigérant"></div>
                            <div class="category-visual-info"><h3>Réfrigérant</h3></div>
                        </a>"""
}

HEADER_TEMPLATE = """                <div class="category-visual-container">
                    <div class="category-visual-header">
                        <h2>Parcourir par type</h2>
                        <div class="category-carousel-nav">
                            <button class="nav-arrow nav-prev" id="cat-prev" aria-label="Précédent">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m15 18-6-6 6-6"/></svg>
                            </button>
                            <button class="nav-arrow nav-next" id="cat-next" aria-label="Suivant">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>
                            </button>
                        </div>
                    </div>
                    <div class="category-visual-list">
{cards}
                    </div>
                </div>"""

def clean_and_heal(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Step 1: Remove EVERYTHING between intro-large and collection-section
    new_lines = []
    skip = False
    found_intro_end = False
    for line in lines:
        if '</div>' in line and found_intro_end == False and any('intro-large' in l for l in new_lines[-10:]):
             # This is a bit risky, let's use a better marker
             pass
        
        if '<div class="category-visual-container">' in line or '<div class="category-visual-list">' in line:
            skip = True
            continue
        
        if '</section>' in line and skip:
            skip = False
            # Inject the new section here
            new_lines.append(HEADER_TEMPLATE.format(cards=CAT_CARDS["tapis"]) + "\n            </div>\n        </section>\n")
            continue
            
        if not skip:
            new_lines.append(line)

    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

# clean_and_heal('tapis-fouille.html')
