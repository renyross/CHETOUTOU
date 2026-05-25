import os
import re

def radical_fix(filename, carousel_html, products_html, category_links_html):
    if not os.path.exists(filename): return
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Visual Carousel Fix
    carousel_pattern = r'<div class="category-visual-container">.*?</section>'
    carousel_replacement = f"""<div class="category-visual-container">
                    <div class="category-visual-header">
                        <div class="category-carousel-nav">
                            <button class="nav-arrow nav-prev" id="cat-prev" aria-label="Précédent"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m15 18-6-6 6-6"/></svg></button>
                            <button class="nav-arrow nav-next" id="cat-next" aria-label="Suivant"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m9 18 6-6-6-6"/></svg></button>
                        </div>
                    </div>
                    <div class="category-visual-list">
{carousel_html}
                    </div>
                </div>
            </div>
        </section>"""
    content = re.sub(carousel_pattern, carousel_replacement, content, flags=re.DOTALL)

    # 2. Sidebar + Grid Fix
    full_sidebar = f"""<aside class="sidebar" id="collection-sidebar">
                    <div class="sidebar-header-mobile">
                        <button id="close-filters" aria-label="Fermer les filtres"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg></button>
                    </div>
                    
                    <div class="filter-group active">
                        <button class="filter-group-header">Disponibilité <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg></button>
                        <div class="filter-group-content">
                            <div class="checkbox-list">
                                <label class="checkbox-item"><input type="checkbox"> En stock <span>(210)</span></label>
                                <label class="checkbox-item"><input type="checkbox"> Épuisé <span>(18)</span></label>
                            </div>
                        </div>
                    </div>

                    <div class="filter-group active">
                        <button class="filter-group-header">Prix <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg></button>
                        <div class="filter-group-content">
                            <p class="price-max-text">Le prix le plus élevé est 159,90€</p>
                            <div class="price-range-inputs">
                                <div class="price-input-wrapper"><span class="price-currency">€</span><input type="number" class="price-field" placeholder="0"></div>
                                <div class="price-input-wrapper"><span class="price-currency">€</span><input type="number" class="price-field" placeholder="159.90"></div>
                            </div>
                        </div>
                    </div>

                    <div class="filter-group active">
                        <button class="filter-group-header">Couleur <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg></button>
                        <div class="filter-group-content">
                            <div class="color-swatch-list">
                                <div class="color-swatch" style="background: #F5F5DC;" title="Beige"></div>
                                <div class="color-swatch" style="background: #FFFFFF;" title="Blanc"></div>
                                <div class="color-swatch" style="background: #0000FF;" title="Bleu"></div>
                                <div class="color-swatch" style="background: #8B4513;" title="Marron"></div>
                                <div class="color-swatch" style="background: #6B8E23;" title="Vert"></div>
                                <div class="color-swatch" style="background: #808080;" title="Gris"></div>
                                <div class="color-swatch" style="background: #FF0000;" title="Rouge"></div>
                                <div class="color-swatch" style="background: #FFFF00;" title="Jaune"></div>
                                <div class="color-swatch" style="background: #000000;" title="Noir"></div>
                                <div class="color-swatch" style="background: #FFC0CB;" title="Rose"></div>
                            </div>
                        </div>
                    </div>

                    <div class="filter-group active">
                        <button class="filter-group-header">Fonction <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg></button>
                        <div class="filter-group-content">
                            <div class="checkbox-list">
                                <label class="checkbox-item"><input type="checkbox"> Anti-traction <span>(12)</span></label>
                                <label class="checkbox-item"><input type="checkbox"> Réfléchissant <span>(24)</span></label>
                                <label class="checkbox-item"><input type="checkbox"> Rembourré <span>(18)</span></label>
                                <label class="checkbox-item"><input type="checkbox"> Personnalisable <span>(32)</span></label>
                                <label class="checkbox-item"><input type="checkbox"> Imperméable <span>(15)</span></label>
                            </div>
                        </div>
                    </div>

                    <div class="filter-group active">
                        <button class="filter-group-header">Catégories <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg></button>
                        <div class="filter-group-content">
                            <ul class="category-filter-list">
                                {category_links_html}
                            </ul>
                        </div>
                    </div>
                </aside>"""

    collection_pattern = r'<section class="collection-section">.*?</section>'
    collection_replacement = f"""<section class="collection-section">
            <div class="container collection-flex">
                {full_sidebar}
                <div class="collection-main">
                    <div class="filter-sort-bar">
                        <div class="product-count">12 produits</div>
                        <div class="sort-options">
                            <span>Trier par :</span>
                            <select>
                                <option>En vedette</option>
                                <option>Meilleures ventes</option>
                                <option>Prix croissant</option>
                                <option>Prix décroissant</option>
                            </select>
                        </div>
                    </div>
                    <div class="collection-grid">
{products_html}
                    </div>
                </div>
            </div>
        </section>"""
    content = re.sub(collection_pattern, collection_replacement, content, flags=re.DOTALL)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

# --- Data ---
COLLIER_C = """
                        <a href="collier-chien.html" class="category-visual-card active">
                            <div class="category-visual-img-wrapper"><img src="cat_collier_pure_v2.png" alt="Collier"></div>
                            <div class="category-visual-info"><h3>Tous les Colliers</h3></div>
                        </a>
                        <a href="collier-personnalise-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper"><img src="collier_perso_visual.png" alt="Collier"></div>
                            <div class="category-visual-info"><h3>Personnalisé</h3></div>
                        </a>
                        <a href="collier-cuir-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper"><img src="collier_cuir_visual.png" alt="Collier"></div>
                            <div class="category-visual-info"><h3>Cuir Artisanal</h3></div>
                        </a>
                        <a href="collier-lumineux-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper"><img src="collier_lumineux_visual.png" alt="Collier"></div>
                            <div class="category-visual-info"><h3>Lumineux</h3></div>
                        </a>
                        <a href="collier-gps-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper"><img src="collier_gps_visual.png" alt="Collier"></div>
                            <div class="category-visual-info"><h3>GPS Tracker</h3></div>
                        </a>
"""

COLLIER_L = """
                                <li><a href="collier-chien.html" class="active">Tous les Colliers</a></li>
                                <li><a href="collier-personnalise-chien.html">Personnalisé</a></li>
                                <li><a href="collier-cuir-chien.html">Cuir Artisanal</a></li>
                                <li><a href="collier-lumineux-chien.html">Lumineux / LED</a></li>
                                <li><a href="collier-gps-chien.html">Tracker GPS</a></li>
                                <li><a href="collier-anti-fugue-chien.html">Anti-Fugue</a></li>
                                <li><a href="collier-dressage-chien.html">Dressage</a></li>
                                <li><a href="collier-electrique-chien.html">Électrique</a></li>
                                <li><a href="collier-anti-aboiement-chien.html">Anti-Aboiement</a></li>
                                <li><a href="collier-etrangleur-chien.html">Étrangleur</a></li>
                                <li><a href="collier-anti-puce-chien.html">Anti-Parasitaire</a></li>
"""

COLLIER_P = """
                        <div class="product-item"><div class="product-img-wrapper"><img src="cat_collier_pure_v2.png" alt="Collier"></div><div class="product-info"><h3>Collier Pure Comfort</h3><p class="product-price">25 €</p></div></div>
                        <div class="product-item"><div class="product-img-wrapper"><img src="collier_cuir_visual.png" alt="Collier"></div><div class="product-info"><h3>Collier Cuir Elegance</h3><p class="product-price">45 €</p></div></div>
                        <div class="product-item"><div class="product-img-wrapper"><img src="collier_lumineux_visual.png" alt="Collier"></div><div class="product-info"><h3>Collier LED Night-Safe</h3><p class="product-price">19 €</p></div></div>
                        <div class="product-item"><div class="product-img-wrapper"><img src="collier_gps_visual.png" alt="Collier"></div><div class="product-info"><h3>Tracker GPS PawTrack</h3><p class="product-price">129 €</p></div></div>
                        <div class="product-item"><div class="product-img-wrapper"><img src="collier_dressage_visual.png" alt="Collier"></div><div class="product-info"><h3>Collier Training Pro</h3><p class="product-price">79 €</p></div></div>
                        <div class="product-item"><div class="product-img-wrapper"><img src="collier_anti_fugue_visual.png" alt="Collier"></div><div class="product-info"><h3>Kit Safe-Zone</h3><p class="product-price">149 €</p></div></div>
                        <div class="product-item"><div class="product-img-wrapper"><img src="collier_perso_visual.png" alt="Collier"></div><div class="product-info"><h3>Collier Personnalisé Luxe</h3><p class="product-price">55 €</p></div></div>
                        <div class="product-item"><div class="product-img-wrapper"><img src="collier_electrique_visual.png" alt="Collier"></div><div class="product-info"><h3>Collier Électrique Pro</h3><p class="product-price">95 €</p></div></div>
                        <div class="product-item"><div class="product-img-wrapper"><img src="collier_anti_aboiement_visual.png" alt="Collier"></div><div class="product-info"><h3>Collier Anti-Aboiement</h3><p class="product-price">39 €</p></div></div>
                        <div class="product-item"><div class="product-img-wrapper"><img src="collier_etrangleur_visual.png" alt="Collier"></div><div class="product-info"><h3>Collier Étrangleur Chrome</h3><p class="product-price">29 €</p></div></div>
                        <div class="product-item"><div class="product-img-wrapper"><img src="collier_anti_puce_visual.png" alt="Collier"></div><div class="product-info"><h3>Collier Seresto Anti-Puce</h3><p class="product-price">49 €</p></div></div>
                        <div class="product-item"><div class="product-img-wrapper"><img src="collier_biothane_visual.png" alt="Collier"></div><div class="product-info"><h3>Collier BioThane Waterproof</h3><p class="product-price">35 €</p></div></div>
"""

# Apply
files = [f for f in os.listdir('.') if f.endswith('.html')]
for f in files:
    if 'collier' in f: radical_fix(f, COLLIER_C, COLLIER_P, COLLIER_L)

print('Sidebar updated with all filters (Price, Color, Function) for Colliers.')
