import os
import re

# --- Data Definition ---

COUCHAGE_SIDEBAR = """                    <div class="filter-group active">
                        <button class="filter-group-header">Disponibilité <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg></button>
                        <div class="filter-group-content">
                            <div class="checkbox-list">
                                <label class="checkbox-item"><input type="checkbox"> En stock <span>(84)</span></label>
                                <label class="checkbox-item"><input type="checkbox"> Épuisé <span>(5)</span></label>
                            </div>
                        </div>
                    </div>
                    <div class="filter-group active">
                        <button class="filter-group-header">Catégories <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg></button>
                        <div class="filter-group-content">
                            <ul class="category-filter-list">
                                <li><a href="couchage.html">Tout le Couchage</a></li>
                                <li><a href="panier-chien.html">Panier Chien</a></li>
                                <li><a href="lit-chien.html">Lit Chien</a></li>
                                <li><a href="coussin-chien.html">Coussin Chien</a></li>
                                <li><a href="canape-chien.html">Canapé Luxe</a></li>
                                <li><a href="couverture-chien.html">Couvertures</a></li>
                                <li><a href="panier-xxl-chien.html">Format XXL</a></li>
                                <li><a href="panier-orthopedique-chien.html">Orthopédique</a></li>
                                <li><a href="panier-voiture-chien.html">Pour Voiture</a></li>
                            </ul>
                        </div>
                    </div>"""

COUCHAGE_PRODUCTS = """                        <!-- Product 1 -->
                        <div class="product-item">
                            <div class="product-img-wrapper">
                                <img src="panier_velvet_main.png" alt="Panier Velvet">
                                <span class="status-badge">Best-seller</span>
                            </div>
                            <div class="product-info">
                                <h3>Panier "Royal Velvet" Apaisant</h3>
                                <p class="product-price">129 €</p>
                            </div>
                        </div>
                        <!-- Product 2 -->
                        <div class="product-item">
                            <div class="product-img-wrapper">
                                <img src="couchage_apaisant_1775487819875.png" alt="Coussin Apaisant">
                                <span class="status-badge">Sommeil Profond</span>
                            </div>
                            <div class="product-info">
                                <h3>Coussin Anti-Stress "Cloud"</h3>
                                <p class="product-price">65 €</p>
                            </div>
                        </div>
                        <!-- Product 3 -->
                        <div class="product-item">
                            <div class="product-img-wrapper">
                                <img src="incontournable_panier_xxl_1775493488210.png" alt="Panier XXL">
                                <span class="status-badge">Format Géant</span>
                            </div>
                            <div class="product-info">
                                <h3>Panier "Titanic" XXL Luxe</h3>
                                <p class="product-price">189 €</p>
                            </div>
                        </div>
                        <!-- Product 4 -->
                        <div class="product-item">
                            <div class="product-img-wrapper">
                                <img src="cat_panier_chien_visual.png" alt="Panier Classique">
                            </div>
                            <div class="product-info">
                                <h3>Panier "Classic Comfort" Déhoussable</h3>
                                <p class="product-price">49 €</p>
                            </div>
                        </div>"""

def update_couchage_pages():
    patterns = ['panier-', 'lit-', 'coussin-', 'canape-', 'couverture-']
    html_files = [f for f in os.listdir('.') if any(f.startswith(p) for p in patterns) and f.endswith('.html')]
    html_files.append('couchage.html')
    
    for filename in html_files:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 1. Update Sidebar
        content = re.sub(r'<aside class="sidebar" id="collection-sidebar">.*?</aside>', 
                         r'<aside class="sidebar" id="collection-sidebar">\n                    <div class="sidebar-header-mobile">\n                        <button id="close-filters" aria-label="Fermer les filtres">\n                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>\n                        </button>\n                    </div>\n' + COUCHAGE_SIDEBAR + '\n                </aside>', 
                         content, flags=re.DOTALL)
        
        # 2. Update Product Grid
        content = re.sub(r'<div class="collection-grid">.*?</div>', 
                         r'<div class="collection-grid">\n' + COUCHAGE_PRODUCTS + '\n                    </div>', 
                         content, flags=re.DOTALL)
        
        # 3. Highlight current category in sidebar
        content = content.replace(f'href="{filename}"', f'href="{filename}" class="active"')

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")

update_couchage_pages()
