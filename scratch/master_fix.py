import os
import re

# Master Fix: One script to rule them all and fix all duplications.

def fix_page(filename, sidebar_content, product_content):
    if not os.path.exists(filename): return
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix SEO Hero section (remove duplication of category-visual-container)
    # We look for <section class="seo-page-section"> ... </section>
    # and ensure it has only ONE visual carousel.
    hero_match = re.search(r'<section class="seo-page-section">.*?</section>', content, flags=re.DOTALL)
    if hero_match:
        hero_html = hero_match.group(0)
        # If there are two containers, keep only the first one.
        if hero_html.count('<div class="category-visual-container">') > 1:
            hero_html = re.sub(r'(<div class="category-visual-container">.*?</div>\s*</div>\s*</div>).*?<div class="category-visual-container">.*?</section>', 
                               r'\1\n        </section>', hero_html, flags=re.DOTALL)
            content = content.replace(hero_match.group(0), hero_html)

    # 2. Fix Sidebar
    content = re.sub(r'<aside class="sidebar" id="collection-sidebar">.*?</aside>', 
                     f'<aside class="sidebar" id="collection-sidebar">\n                    <div class="sidebar-header-mobile">\n                        <button id="close-filters" aria-label="Fermer les filtres">\n                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>\n                        </button>\n                    </div>\n{sidebar_content}\n                </aside>', 
                     content, flags=re.DOTALL)

    # 3. Fix Product Grid (Extremely robust)
    # We find the start of collection-main and the end of the collection-section.
    main_match = re.search(r'<div class="collection-main">.*?</div>\s*</div>\s*</section>', content, flags=re.DOTALL)
    if main_match:
        main_html = main_match.group(0)
        # Replace the entire collection-grid part inside main_html
        new_grid_html = f'<div class="collection-grid">\n{product_content}\n                    </div>'
        main_html = re.sub(r'<div class="collection-grid">.*?</div>(\s*<div class="product-info">.*?</div>)*', new_grid_html, main_html, flags=re.DOTALL)
        content = content.replace(main_match.group(0), main_html)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Fixed {filename}")

# --- Sidebars ---
HARNAIS_SB = """                    <div class="filter-group active">
                        <button class="filter-group-header">Catégories <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg></button>
                        <div class="filter-group-content">
                            <ul class="category-filter-list">
                                <li><a href="harnais-chien.html">Tous les Harnais</a></li>
                                <li><a href="harnais-anti-traction-chien.html">Anti-Traction</a></li>
                                <li><a href="harnais-petit-chien.html">Petit Chien</a></li>
                                <li><a href="harnais-chien-course.html">Running / Canicross</a></li>
                                <li><a href="harnais-tactique-chien.html">Tactique / K9</a></li>
                                <li><a href="harnais-cuir-chien.html">Cuir Luxe</a></li>
                                <li><a href="harnais-personnalise-chien.html">Personnalisé</a></li>
                            </ul>
                        </div>
                    </div>"""

TAPIS_SB = """                    <div class="filter-group active">
                        <button class="filter-group-header">Catégories <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg></button>
                        <div class="filter-group-content">
                            <ul class="category-filter-list">
                                <li><a href="tapis-chien.html">Tapis pour Chien</a></li>
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

# --- Products ---
HARNAIS_PR = """                        <div class="product-item">
                            <div class="product-img-wrapper"><img src="harnais_anti_traction_main_1775840455761.png" alt="Harnais"></div>
                            <div class="product-info"><h3>Harnais SteadyWalk</h3><p class="product-price">49 €</p></div>
                        </div>
                        <div class="product-item">
                            <div class="product-img-wrapper"><img src="incontournable_harnais_anti_traction_1775493366267.png" alt="Harnais"></div>
                            <div class="product-info"><h3>Harnais Pro-Expert</h3><p class="product-price">75 €</p></div>
                        </div>"""

TAPIS_PR = """                        <div class="product-item">
                            <div class="product-img-wrapper"><img src="tapis_rafraichissant_visual.png" alt="Tapis"></div>
                            <div class="product-info"><h3>Tapis Fraîcheur Premium</h3><p class="product-price">35 €</p></div>
                        </div>"""

# EXECUTE
h_files = [f for f in os.listdir('.') if 'harnais' in f and f.endswith('.html')]
for f in h_files: fix_page(f, HARNAIS_SB, HARNAIS_PR)

t_files = [f for f in os.listdir('.') if 'tapis' in f and f.endswith('.html')]
for f in t_files: fix_page(f, TAPIS_SB, TAPIS_PR)
