import os
import re

# --- Data Definition ---

COLLIER_SIDEBAR = """                    <div class="filter-group active">
                        <button class="filter-group-header">Disponibilité <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg></button>
                        <div class="filter-group-content">
                            <div class="checkbox-list">
                                <label class="checkbox-item"><input type="checkbox"> En stock <span>(210)</span></label>
                                <label class="checkbox-item"><input type="checkbox"> Épuisé <span>(18)</span></label>
                            </div>
                        </div>
                    </div>
                    <div class="filter-group active">
                        <button class="filter-group-header">Catégories <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg></button>
                        <div class="filter-group-content">
                            <ul class="category-filter-list">
                                <li><a href="collier-chien.html">Tous les Colliers</a></li>
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
                            </ul>
                        </div>
                    </div>"""

COLLIER_PRODUCTS = """                        <!-- Product 1 -->
                        <div class="product-item">
                            <div class="product-img-wrapper">
                                <img src="cat_collier_pure_v2.png" alt="Collier Pure">
                                <span class="status-badge">Best-seller</span>
                            </div>
                            <div class="product-info">
                                <h3>Collier "Pure Comfort" Soft Touch</h3>
                                <p class="product-price">25 €</p>
                            </div>
                        </div>
                        <!-- Product 2 -->
                        <div class="product-item">
                            <div class="product-img-wrapper">
                                <img src="collier_cuir_visual.png" alt="Collier Cuir">
                                <span class="status-badge">Artisanal</span>
                            </div>
                            <div class="product-info">
                                <h3>Collier Cuir "Elegance" Couture Main</h3>
                                <p class="product-price">45 €</p>
                            </div>
                        </div>
                        <!-- Product 3 -->
                        <div class="product-item">
                            <div class="product-img-wrapper">
                                <img src="collier_perso_visual.png" alt="Collier Personnalisé">
                                <span class="status-badge">Sur Mesure</span>
                            </div>
                            <div class="product-info">
                                <h3>Collier Personnalisé "Identity"</h3>
                                <p class="product-price">35 €</p>
                            </div>
                        </div>
                        <!-- Product 4 -->
                        <div class="product-item">
                            <div class="product-img-wrapper">
                                <img src="collier_gps_visual.png" alt="Collier GPS">
                                <span class="status-badge">Innovation</span>
                            </div>
                            <div class="product-info">
                                <h3>Collier "SmartTracker" GPS 4G</h3>
                                <p class="product-price">89 €</p>
                            </div>
                        </div>
                        <!-- Product 5 -->
                        <div class="product-item">
                            <div class="product-img-wrapper">
                                <img src="collier_lumineux_visual.png" alt="Collier Lumineux">
                            </div>
                            <div class="product-info">
                                <h3>Collier LED "GlowGuard" Rechargeable</h3>
                                <p class="product-price">22 €</p>
                            </div>
                        </div>
                        <!-- Product 6 -->
                        <div class="product-item">
                            <div class="product-img-wrapper">
                                <img src="collier_dressage_visual.png" alt="Collier Dressage">
                            </div>
                            <div class="product-info">
                                <h3>Collier de Dressage "RemotePro"</h3>
                                <p class="product-price">129 €</p>
                            </div>
                        </div>"""

def update_collier_pages():
    html_files = [f for f in os.listdir('.') if f.startswith('collier-') and f.endswith('.html')]
    html_files.append('collier-chien.html')
    
    for filename in html_files:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 1. Update Sidebar
        content = re.sub(r'<aside class="sidebar" id="collection-sidebar">.*?</aside>', 
                         r'<aside class="sidebar" id="collection-sidebar">\n                    <div class="sidebar-header-mobile">\n                        <button id="close-filters" aria-label="Fermer les filtres">\n                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>\n                        </button>\n                    </div>\n' + COLLIER_SIDEBAR + '\n                </aside>', 
                         content, flags=re.DOTALL)
        
        # 2. Update Product Grid
        content = re.sub(r'<div class="collection-grid">.*?</div>', 
                         r'<div class="collection-grid">\n' + COLLIER_PRODUCTS + '\n                    </div>', 
                         content, flags=re.DOTALL)
        
        # 3. Highlight current category in sidebar
        content = content.replace(f'href="{filename}"', f'href="{filename}" class="active"')

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")

update_collier_pages()
