import os
import re

# --- Jouets ---
JOUETS_SIDEBAR = """                    <div class="filter-group active">
                        <button class="filter-group-header">Catégories <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg></button>
                        <div class="filter-group-content">
                            <ul class="category-filter-list">
                                <li><a href="jouets.html">Tous les Jouets</a></li>
                                <li><a href="jouet-interactif-chien.html">Jouet interactif</a></li>
                                <li><a href="jouets-indestructibles.html">Jouets indestructibles</a></li>
                                <li><a href="peluches-chien.html">Peluches</a></li>
                                <li><a href="balles-chien.html">Balles</a></li>
                                <li><a href="frisbee-chien.html">Frisbee</a></li>
                                <li><a href="lanceur-balle-chien.html">Lanceur de balle</a></li>
                                <li><a href="jouet-occupation-chien.html">Occupation</a></li>
                            </ul>
                        </div>
                    </div>"""

JOUETS_PRODUCTS = """                        <!-- Product 1 -->
                        <div class="product-item">
                            <div class="product-img-wrapper">
                                <img src="dog_toys_premium_1775489913031.png" alt="Jouet">
                                <span class="status-badge">Indestructible</span>
                            </div>
                            <div class="product-info">
                                <h3>Os en Caoutchouc Naturel Ultra-Résistant</h3>
                                <p class="product-price">22 €</p>
                            </div>
                        </div>
                        <!-- Product 2 -->
                        <div class="product-item">
                            <div class="product-img-wrapper">
                                <img src="incontournable_jouet_snuffle_mat_1775493547836.png" alt="Tapis Fouille">
                                <span class="status-badge">Éveil</span>
                            </div>
                            <div class="product-info">
                                <h3>Tapis de Fouille "Flower Power"</h3>
                                <p class="product-price">45 €</p>
                            </div>
                        </div>"""

# --- Hygiène ---
HYGIENE_SIDEBAR = """                    <div class="filter-group active">
                        <button class="filter-group-header">Catégories <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg></button>
                        <div class="filter-group-content">
                            <ul class="category-filter-list">
                                <li><a href="hygiene.html">Tout l'Hygiène</a></li>
                                <li><a href="gamelle-anti-glouton.html">Gamelle Anti-Glouton</a></li>
                                <li><a href="gamelle-surelevee-chien.html">Gamelle Surélevée</a></li>
                                <li><a href="gamelle-ceramique-chien.html">Gamelle Céramique</a></li>
                                <li><a href="gamelle-personnalisee-chien.html">Gamelle Personnalisée</a></li>
                                <li><a href="brosses.html">Brosses & Soin</a></li>
                                <li><a href="sac-a-crottes.html">Hygiène Urbaine</a></li>
                            </ul>
                        </div>
                    </div>"""

HYGIENE_PRODUCTS = """                        <!-- Product 1 -->
                        <div class="product-item">
                            <div class="product-img-wrapper">
                                <img src="gamelle_surelevee_visual.png" alt="Gamelle">
                                <span class="status-badge">Orthopédique</span>
                            </div>
                            <div class="product-info">
                                <h3>Support Gamelles Surélevé en Bambou</h3>
                                <p class="product-price">65 €</p>
                            </div>
                        </div>
                        <!-- Product 2 -->
                        <div class="product-item">
                            <div class="product-img-wrapper">
                                <img src="dog_grooming_brush_1775489868725.png" alt="Brosse">
                            </div>
                            <div class="product-info">
                                <h3>Brosse de Toilettage Auto-Nettoyante</h3>
                                <p class="product-price">19 €</p>
                            </div>
                        </div>"""

def update_others():
    # Jouets
    jouets_files = [f for f in os.listdir('.') if (f.startswith('jouet') or f.startswith('balles-') or f.startswith('peluches-') or f.startswith('frisbee-') or f.startswith('lanceur-')) and f.endswith('.html')]
    for filename in jouets_files:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        content = re.sub(r'<aside class="sidebar" id="collection-sidebar">.*?</aside>', r'<aside class="sidebar" id="collection-sidebar">\n' + JOUETS_SIDEBAR + '\n                </aside>', content, flags=re.DOTALL)
        content = re.sub(r'<div class="collection-grid">.*?</div>', r'<div class="collection-grid">\n' + JOUETS_PRODUCTS + '\n                    </div>', content, flags=re.DOTALL)
        with open(filename, 'w', encoding='utf-8') as f: f.write(content)

    # Hygiène
    hygiene_files = [f for f in os.listdir('.') if (f.startswith('gamelle-') or f == 'hygiene.html' or f == 'brosses.html') and f.endswith('.html')]
    for filename in hygiene_files:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        content = re.sub(r'<aside class="sidebar" id="collection-sidebar">.*?</aside>', r'<aside class="sidebar" id="collection-sidebar">\n' + HYGIENE_SIDEBAR + '\n                </aside>', content, flags=re.DOTALL)
        content = re.sub(r'<div class="collection-grid">.*?</div>', r'<div class="collection-grid">\n' + HYGIENE_PRODUCTS + '\n                    </div>', content, flags=re.DOTALL)
        with open(filename, 'w', encoding='utf-8') as f: f.write(content)

update_others()
