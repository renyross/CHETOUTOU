import os
import re

# --- Data Definition ---

HARNAIS_SIDEBAR = """                    <div class="filter-group active">
                        <button class="filter-group-header">Disponibilité <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg></button>
                        <div class="filter-group-content">
                            <div class="checkbox-list">
                                <label class="checkbox-item"><input type="checkbox"> En stock <span>(154)</span></label>
                                <label class="checkbox-item"><input type="checkbox"> Épuisé <span>(12)</span></label>
                            </div>
                        </div>
                    </div>
                    <div class="filter-group active">
                        <button class="filter-group-header">Taille <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg></button>
                        <div class="filter-group-content">
                            <div class="checkbox-list">
                                <label class="checkbox-item"><input type="checkbox"> XS/S <span>(45)</span></label>
                                <label class="checkbox-item"><input type="checkbox"> M/L <span>(82)</span></label>
                                <label class="checkbox-item"><input type="checkbox"> XL/XXL <span>(27)</span></label>
                            </div>
                        </div>
                    </div>
                    <div class="filter-group active">
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

HARNAIS_PRODUCTS = """                        <!-- Product 1 -->
                        <div class="product-item">
                            <div class="product-img-wrapper">
                                <img src="harnais_anti_traction_main_1775840455761.png" alt="Harnais SteadyWalk">
                                <span class="status-badge">Best-seller</span>
                            </div>
                            <div class="product-info">
                                <h3>Harnais "SteadyWalk" Anti-Traction</h3>
                                <p class="product-price">49 €</p>
                            </div>
                        </div>
                        <!-- Product 2 -->
                        <div class="product-item">
                            <div class="product-img-wrapper">
                                <img src="incontournable_harnais_anti_traction_1775493366267.png" alt="Harnais Expert">
                                <span class="status-badge">Expert</span>
                            </div>
                            <div class="product-info">
                                <h3>Harnais "Pro-Control" Expert</h3>
                                <p class="product-price">75 €</p>
                            </div>
                        </div>
                        <!-- Product 3 -->
                        <div class="product-item">
                            <div class="product-img-wrapper">
                                <img src="dog_harness_premium_1775487844838.png" alt="Harnais Elite">
                                <span class="status-badge">Premium</span>
                            </div>
                            <div class="product-info">
                                <h3>Harnais "Elite" Personnalisable</h3>
                                <p class="product-price">115 €</p>
                            </div>
                        </div>
                        <!-- Product 4 -->
                        <div class="product-item">
                            <div class="product-img-wrapper">
                                <img src="harnais_anti_traction_lifestyle_1_1775840493345.png" alt="Harnais Sport">
                            </div>
                            <div class="product-info">
                                <h3>Harnais "Active Sport" Mesh</h3>
                                <p class="product-price">39 €</p>
                            </div>
                        </div>
                        <!-- Product 5 -->
                        <div class="product-item">
                            <div class="product-img-wrapper">
                                <img src="harnais_cuir_visual.png" alt="Harnais Cuir">
                                <span class="status-badge">Artisanal</span>
                            </div>
                            <div class="product-info">
                                <h3>Harnais Cuir "Heritage"</h3>
                                <p class="product-price">95 €</p>
                            </div>
                        </div>
                        <!-- Product 6 -->
                        <div class="product-item">
                            <div class="product-img-wrapper">
                                <img src="harnais_running_visual.png" alt="Harnais Running">
                            </div>
                            <div class="product-info">
                                <h3>Harnais Canicross Ultra-Light</h3>
                                <p class="product-price">55 €</p>
                            </div>
                        </div>"""

def update_harnais_pages():
    html_files = [f for f in os.listdir('.') if f.startswith('harnais-') and f.endswith('.html')]
    html_files.append('harnais-chien.html') # The root one
    
    for filename in html_files:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 1. Update Sidebar
        # Find everything between <aside class="sidebar" id="collection-sidebar"> and </aside>
        content = re.sub(r'<aside class="sidebar" id="collection-sidebar">.*?</aside>', 
                         r'<aside class="sidebar" id="collection-sidebar">\n                    <div class="sidebar-header-mobile">\n                        <button id="close-filters" aria-label="Fermer les filtres">\n                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>\n                        </button>\n                    </div>\n' + HARNAIS_SIDEBAR + '\n                </aside>', 
                         content, flags=re.DOTALL)
        
        # 2. Update Product Grid
        content = re.sub(r'<div class="collection-grid">.*?</div>', 
                         r'<div class="collection-grid">\n' + HARNAIS_PRODUCTS + '\n                    </div>', 
                         content, flags=re.DOTALL)
        
        # 3. Highlight current category in sidebar
        content = content.replace(f'href="{filename}"', f'href="{filename}" class="active"')

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")

update_harnais_pages()
