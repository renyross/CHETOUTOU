import os
import re

# --- Data Definition ---

CAT_CARDS = {
    "collier": """                        <a href="collier-chien.html" class="category-visual-card">
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
    "harnais": """                        <a href="harnais-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper"><img src="cat_harnais_pure.png" alt="Harnais Chien"></div>
                            <div class="category-visual-info"><h3>Harnais Chien</h3></div>
                        </a>
                        <a href="harnais-anti-traction-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper"><img src="harnais_anti_traction_visual.png" alt="Harnais Anti-Traction"></div>
                            <div class="category-visual-info"><h3>Anti-Traction</h3></div>
                        </a>
                        <a href="harnais-petit-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper"><img src="harnais_petit_chien_visual.png" alt="Harnais Petit Chien"></div>
                            <div class="category-visual-info"><h3>Petit Chien</h3></div>
                        </a>
                        <a href="harnais-chien-course.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper"><img src="harnais_running_visual.png" alt="Harnais Course"></div>
                            <div class="category-visual-info"><h3>Running / Canicross</h3></div>
                        </a>
                        <a href="harnais-tactique-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper"><img src="harnais_tactique_visual.png" alt="Harnais Tactique"></div>
                            <div class="category-visual-info"><h3>Tactique / K9</h3></div>
                        </a>
                        <a href="harnais-cuir-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper"><img src="harnais_cuir_visual.png" alt="Harnais Cuir"></div>
                            <div class="category-visual-info"><h3>Cuir Luxe</h3></div>
                        </a>
                        <a href="harnais-personnalise-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper"><img src="harnais_perso_visual.png" alt="Harnais Personnalisé"></div>
                            <div class="category-visual-info"><h3>Personnalisé</h3></div>
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
                        </a>""",
    "couchage": """                        <a href="panier-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper"><img src="cat_panier.png" alt="Panier Chien"></div>
                            <div class="category-visual-info"><h3>Paniers</h3></div>
                        </a>
                        <a href="lit-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper"><img src="cat_couchage.png" alt="Lit Chien"></div>
                            <div class="category-visual-info"><h3>Lits & Canapés</h3></div>
                        </a>
                        <a href="coussin-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper"><img src="cat_coussin.png" alt="Coussin Chien"></div>
                            <div class="category-visual-info"><h3>Coussins</h3></div>
                        </a>
                        <a href="panier-orthopedique-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper"><img src="cat_coussin_orthopedique_visual.png" alt="Orthopédique"></div>
                            <div class="category-visual-info"><h3>Orthopédique</h3></div>
                        </a>
                        <a href="coussin-anti-stress-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper"><img src="cat_coussin_antistress_visual.png" alt="Anti-Stress"></div>
                            <div class="category-visual-info"><h3>Anti-Stress</h3></div>
                        </a>
                        <a href="couverture-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper"><img src="cat_couverture.png" alt="Couverture Chien"></div>
                            <div class="category-visual-info"><h3>Couvertures</h3></div>
                        </a>
                        <a href="protection-canape-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper"><img src="cat_protection_canape.png" alt="Protection Canapé"></div>
                            <div class="category-visual-info"><h3>Protection</h3></div>
                        </a>""",
    "promenade": """                        <a href="laisse-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper"><img src="cat_laisse_pure.png" alt="Laisse Chien"></div>
                            <div class="category-visual-info"><h3>Laisses</h3></div>
                        </a>
                        <a href="laisse-longe-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper"><img src="cat_laisse.png" alt="Longe Chien"></div>
                            <div class="category-visual-info"><h3>Longes</h3></div>
                        </a>
                        <a href="sac-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper"><img src="cat_sac_citadin_visual.png" alt="Sac Chien"></div>
                            <div class="category-visual-info"><h3>Sacs Citadins</h3></div>
                        </a>
                        <a href="sac-transport-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper"><img src="cat_sac_transport_visual.png" alt="Sac de Transport"></div>
                            <div class="category-visual-info"><h3>Transport</h3></div>
                        </a>
                        <a href="sac-a-dos-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper"><img src="cat_sac_a_dos_visual.png" alt="Sac à Dos"></div>
                            <div class="category-visual-info"><h3>Sacs à Dos</h3></div>
                        </a>""",
    "jouets": """                        <a href="jouets.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper"><img src="cat_jouets.png" alt="Jouets Chien"></div>
                            <div class="category-visual-info"><h3>Tous les Jouets</h3></div>
                        </a>
                        <a href="jouet-occupation-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper"><img src="cat_jouet_occupation.png" alt="Jouet Occupation"></div>
                            <div class="category-visual-info"><h3>Occupation</h3></div>
                        </a>
                        <a href="balles-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper"><img src="cat_balle.png" alt="Balles Chien"></div>
                            <div class="category-visual-info"><h3>Balles</h3></div>
                        </a>
                        <a href="peluches-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper"><img src="cat_peluche.png" alt="Peluches Chien"></div>
                            <div class="category-visual-info"><h3>Peluches</h3></div>
                        </a>""",
    "hygiene": """                        <a href="hygiene.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper"><img src="cat_hygiene.png" alt="Hygiène Chien"></div>
                            <div class="category-visual-info"><h3>Gamelles</h3></div>
                        </a>
                        <a href="gamelle-surelevee-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper"><img src="gamelle_surelevee_visual.png" alt="Gamelle Surélevée"></div>
                            <div class="category-visual-info"><h3>Surélevée</h3></div>
                        </a>
                        <a href="tapis-gamelle-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper"><img src="cat_tapis_gamelle_visual.png" alt="Tapis Gamelle"></div>
                            <div class="category-visual-info"><h3>Tapis Gamelle</h3></div>
                        </a>
                        <a href="tapis-lechage.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper"><img src="cat_tapis_lechage_visual.png" alt="Tapis de Léchage"></div>
                            <div class="category-visual-info"><h3>Léchage</h3></div>
                        </a>""",
    "accessoires": """                        <a href="accessoires.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper"><img src="cat_accessoires_pure.png" alt="Accessoires"></div>
                            <div class="category-visual-info"><h3>Médailles</h3></div>
                        </a>
                        <a href="museliere.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper"><img src="cat_museliere_visual.png" alt="Muselière"></div>
                            <div class="category-visual-info"><h3>Muselières</h3></div>
                        </a>
                        <a href="bottine-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper"><img src="uploaded_image_1775488059049.png" alt="Bottines"></div>
                            <div class="category-visual-info"><h3>Bottines</h3></div>
                        </a>"""
}

# --- Templates ---
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

FILTER_GROUP_CATEGORIES = """                    <div class="filter-group active">
                        <button class="filter-group-header">Catégories <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg></button>
                        <div class="filter-group-content">
                            <ul class="category-filter-list">
                                <li><a href="tapis-chien.html">Tous les Tapis</a></li>
                                <li><a href="tapis-rafraichissant-chien.html">Tapis Rafraîchissant</a></li>
                                <li><a href="tapis-fouille.html">Tapis de Fouille</a></li>
                                <li><a href="tapis-lechage.html">Tapis de Léchage</a></li>
                                <li><a href="tapis-absorbant-chien.html">Tapis Absorbant</a></li>
                                <li><a href="tapis-xxl-chien.html">Tapis Chien XXL</a></li>
                                <li><a href="tapis-gamelle-chien.html">Tapis Gamelle Chien</a></li>
                                <li><a href="tapis-fraicheur-chien.html">Tapis Fraîcheur</a></li>
                                <li><a href="tapis-refrigerant-chien.html">Tapis Réfrigérant</a></li>
                            </ul>
                        </div>
                    </div>"""

# --- Logic ---

def heal_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Standardize the Visual Carousel Container
    # Delete ALL existing versions of the container or list
    content = re.sub(r'<div class="category-visual-container">.*?</div>\s*</div>(\s*</div>)?', 'TEMP_VISUAL_MARKER', content, flags=re.DOTALL)
    content = re.sub(r'<div class="category-visual-list">.*?</div>', '', content, flags=re.DOTALL)
    
    # Identify Category
    category = None
    if "collier" in filename: category = "collier"
    elif "harnais" in filename: category = "harnais"
    elif "tapis" in filename: category = "tapis"
    elif any(x in filename for x in ["panier", "lit-", "coussin", "couverture", "canape", "couchage"]): category = "couchage"
    elif any(x in filename for x in ["laisse", "longe", "sac-", "promenade"]): category = "promenade"
    elif any(x in filename for x in ["jouet", "peluches", "balles", "frisbee", "lanceur"]): category = "jouets"
    elif any(x in filename for x in ["gamelle", "hygiene", "brosses", "boite-croquettes"]): category = "hygiene"
    elif any(x in filename for x in ["impermeables", "manteaux", "bottine", "museliere", "accessoires"]): category = "accessoires"

    if category and category in CAT_CARDS:
        new_visual = HEADER_TEMPLATE.format(cards=CAT_CARDS[category])
        if 'TEMP_VISUAL_MARKER' in content:
            content = content.replace('TEMP_VISUAL_MARKER', new_visual + "\n            </div>")
        else:
            # Fallback injection after intro
            content = re.sub(r'(<div class="intro-large">.*?</div>)', r'\1\n\n' + new_visual, content, flags=re.DOTALL)

    # 2. Fix Tapis Sidebar Filters
    if "tapis" in filename:
        # Remove any existing Category filter group
        content = re.sub(r'<div class="filter-group active">\s*<button class="filter-group-header">Catégories.*?</button>\s*<div class="filter-group-content">.*?</ul>\s*</div>\s*</div>', '', content, flags=re.DOTALL)
        content = re.sub(r'<ul class="category-filter-list">.*?</ul>', '', content, flags=re.DOTALL)
        
        # Inject at the end of the sidebar
        content = content.replace('</aside>', FILTER_GROUP_CATEGORIES + '\n                </aside>')
        
        # Mark active
        content = content.replace(f'href="{filename}"', f'href="{filename}" class="active"')
        
    # 3. Final cleanup of potential duplication markers and double classes
    content = content.replace('TEMP_VISUAL_MARKER', '')
    content = re.sub(r'class="active" class="category-visual-card"', 'class="category-visual-card active"', content)
    content = re.sub(r'class="category-visual-card" class="active"', 'class="category-visual-card active"', content)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

# Process all files
html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'index.html' and 'produit-' not in f]
for f in html_files:
    heal_file(f)
    print(f"Healed {f}")
