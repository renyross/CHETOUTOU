import os
import re

# --- Data Definition ---

PROMENADE_SIDEBAR = """                    <div class="filter-group active">
                        <button class="filter-group-header">Disponibilité <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg></button>
                        <div class="filter-group-content">
                            <div class="checkbox-list">
                                <label class="checkbox-item"><input type="checkbox"> En stock <span>(312)</span></label>
                                <label class="checkbox-item"><input type="checkbox"> Épuisé <span>(24)</span></label>
                            </div>
                        </div>
                    </div>
                    <div class="filter-group active">
                        <button class="filter-group-header">Catégories <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg></button>
                        <div class="filter-group-content">
                            <ul class="category-filter-list">
                                <li><a href="promenade.html">Toute la Promenade</a></li>
                                <li><a href="laisse-chien.html">Laisse Chien</a></li>
                                <li><a href="laisses-classiques.html">Laisse Classique</a></li>
                                <li><a href="laisse-enrouleur-chien.html">Laisse Enrouleur</a></li>
                                <li><a href="laisse-longe-chien.html">Longes</a></li>
                                <li><a href="laisse-cuir-chien.html">Laisse en Cuir</a></li>
                                <li><a href="sac-chien.html">Sacs de Transport</a></li>
                                <li><a href="sac-a-dos-chien.html">Sacs à Dos</a></li>
                                <li><a href="bottine-chien.html">Bottines</a></li>
                                <li><a href="impermeables.html">Imperméables</a></li>
                            </ul>
                        </div>
                    </div>"""

PROMENADE_PRODUCTS = """                        <!-- Product 1 -->
                        <div class="product-item">
                            <div class="product-img-wrapper">
                                <img src="dog_leash_elegant_1775487863541.png" alt="Laisse Cuir">
                                <span class="status-badge">Best-seller</span>
                            </div>
                            <div class="product-info">
                                <h3>Laisse Cuir "Oxford" Tressée</h3>
                                <p class="product-price">45 €</p>
                            </div>
                        </div>
                        <!-- Product 2 -->
                        <div class="product-item">
                            <div class="product-img-wrapper">
                                <img src="laisse_enrouleur_visual.png" alt="Laisse Enrouleur">
                                <span class="status-badge">Pratique</span>
                            </div>
                            <div class="product-info">
                                <h3>Laisse Enrouleur "Flexi-Guard" 5m</h3>
                                <p class="product-price">35 €</p>
                            </div>
                        </div>
                        <!-- Product 3 -->
                        <div class="product-item">
                            <div class="product-img-wrapper">
                                <img src="sac_transport_visual.png" alt="Sac Transport">
                                <span class="status-badge">Voyage</span>
                            </div>
                            <div class="product-info">
                                <h3>Sac de Transport "Urban Wanderer"</h3>
                                <p class="product-price">85 €</p>
                            </div>
                        </div>
                        <!-- Product 4 -->
                        <div class="product-item">
                            <div class="product-img-wrapper">
                                <img src="incontournable_imper_premium_yellow_1775493418425.png" alt="Imperméable">
                            </div>
                            <div class="product-info">
                                <h3>Imperméable "StormGuard" Jaune Flash</h3>
                                <p class="product-price">75 €</p>
                            </div>
                        </div>"""

def update_promenade_pages():
    patterns = ['laisse-', 'longe-', 'sac-', 'bottine-', 'impermeables-']
    html_files = [f for f in os.listdir('.') if any(f.startswith(p) for p in patterns) and f.endswith('.html')]
    html_files.append('promenade.html')
    html_files.append('laisses-classiques.html')
    
    for filename in html_files:
        if not os.path.exists(filename): continue
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 1. Update Sidebar
        content = re.sub(r'<aside class="sidebar" id="collection-sidebar">.*?</aside>', 
                         r'<aside class="sidebar" id="collection-sidebar">\n                    <div class="sidebar-header-mobile">\n                        <button id="close-filters" aria-label="Fermer les filtres">\n                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>\n                        </button>\n                    </div>\n' + PROMENADE_SIDEBAR + '\n                </aside>', 
                         content, flags=re.DOTALL)
        
        # 2. Update Product Grid
        content = re.sub(r'<div class="collection-grid">.*?</div>', 
                         r'<div class="collection-grid">\n' + PROMENADE_PRODUCTS + '\n                    </div>', 
                         content, flags=re.DOTALL)
        
        # 3. Highlight current category in sidebar
        content = content.replace(f'href="{filename}"', f'href="{filename}" class="active"')

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")

update_promenade_pages()
