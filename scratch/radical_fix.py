import os
import re

# --- Data Definition ---
CAT_CARDS = {
    "collier": """                        <a href="collier-chien.html" class="category-visual-card active">
                            <div class="category-visual-img-wrapper"><img src="cat_collier_pure_v2.png" alt="Collier Chien"></div>
                            <div class="category-visual-info"><h3>Collier Chien</h3></div>
                        </a>
                        <a href="collier-personnalise-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper"><img src="collier_perso_visual.png" alt="Collier Personnalisé"></div>
                            <div class="category-visual-info"><h3>Personnalisé</h3></div>
                        </a>
                        <a href="collier-cuir-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper"><img src="collier_cuir_visual.png" alt="Collier en Cuir"></div>
                            <div class="category-visual-info"><h3>Cuir Artisanal</h3></div>
                        </a>
                        <a href="collier-lumineux-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper"><img src="collier_lumineux_visual.png" alt="Collier Lumineux"></div>
                            <div class="category-visual-info"><h3>Lumineux / LED</h3></div>
                        </a>
                        <a href="collier-gps-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper"><img src="collier_gps_visual.png" alt="Collier GPS Chien"></div>
                            <div class="category-visual-info"><h3>Tracker GPS</h3></div>
                        </a>
                        <a href="collier-anti-fugue-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper"><img src="collier_anti_fugue_visual.png" alt="Collier Anti-Fugue"></div>
                            <div class="category-visual-info"><h3>Anti-Fugue</h3></div>
                        </a>
                        <a href="collier-dressage-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper"><img src="collier_dressage_visual.png" alt="Collier de Dressage"></div>
                            <div class="category-visual-info"><h3>Dressage</h3></div>
                        </a>
                        <a href="collier-electrique-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper"><img src="collier_electrique_visual.png" alt="Collier Électrique"></div>
                            <div class="category-visual-info"><h3>Électrique</h3></div>
                        </a>""",
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

VISUAL_SECTION = """                <div class="category-visual-container">
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
                </div>
            </div>
        </section>"""

def radical_fix(filename, category):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Identify the section between gymshark-title and collection-section
    # Actually, let's look for the end of intro-large
    pattern = r'(<div class="intro-large">.*?</div>).*?<section class="collection-section">'
    match = re.search(pattern, content, flags=re.DOTALL)
    if match:
        intro_part = match.group(1)
        new_visual = VISUAL_SECTION.format(cards=CAT_CARDS[category])
        if filename in content: # Just to handle active class in visual cards
             new_visual = new_visual.replace(f'href="{filename}" class="category-visual-card"', f'href="{filename}" class="category-visual-card active"')

        replacement = intro_part + "\n\n" + new_visual + "\n\n        <section class=\"collection-section\">"
        new_content = content[:match.start()] + replacement + content[match.end():]
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Radically fixed {filename}")

radical_fix('collier-chien.html', 'collier')
radical_fix('tapis-chien.html', 'tapis')
radical_fix('tapis-fouille.html', 'tapis')
