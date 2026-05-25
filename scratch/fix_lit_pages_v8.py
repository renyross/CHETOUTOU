import os
import re

def standardize_page(filename, category_name, breadcrumb_path, products_list, visual_cards):
    with open('collier-chien.html', 'r', encoding='utf-8') as f:
        master = f.read()

    # Extract clean Header and Footer
    header_match = re.search(r'(<div class="announcement-bar">.*?</header>)', master, re.DOTALL)
    master_header = header_match.group(1)

    footer_match = re.search(r'(<footer.*</footer>)', master, re.DOTALL)
    master_footer = footer_match.group(1)

    # Sidebar components (standardized for the department)
    sidebar_match = re.search(r'(<aside class="sidebar".*?</aside>)', master, re.DOTALL)
    master_sidebar = sidebar_match.group(1)
    
    # Update sidebar categories for Couchage
    new_cats = """<ul class="category-filter-list">
                                <li><a href="panier-chien.html">Paniers</a></li>
                                <li><a href="lit-chien.html">Lits & Canapés</a></li>
                                <li><a href="coussin-chien.html">Coussins</a></li>
                                <li><a href="tapis-chien.html">Tapis</a></li>
                            </ul>"""
    master_sidebar = re.sub(r'<ul class="category-filter-list">.*?</ul>', new_cats, master_sidebar, flags=re.DOTALL)

    # Reconstruct the page
    new_content = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{category_name} | Chetoutou</title>
    <meta name="description" content="Découvrez notre collection de {category_name} sur Chetoutou, votre boutique premium d'accessoires pour chiens.">
    <link rel="stylesheet" href="styles.css">
</head>
<body class="shop-page">
    {master_header}
    <main>
        <section class="premium-category-header">
            <div class="container">
                <div class="breadcrumb">
                    {breadcrumb_path}
                </div>
                <div class="product-count">{len(products_list)} Produits</div>
                <h1>{category_name}</h1>
                <div class="hero-description-wrapper">
                    <p class="hero-description" id="hero-desc">
                        Offrez à votre compagnon le repos qu'il mérite avec notre collection exclusive de {category_name.lower()} haut de gamme.
                        <span class="hero-description-extra">
                            Conçus avec des matériaux nobles et une ergonomie pensée pour le bien-être canin, nos couchages allient esthétique et confort absolu.
                        </span>
                        <button class="voir-plus-btn" id="voir-plus-toggle">Voir plus</button>
                    </p>
                </div>
                <div class="visual-carousel-wrapper">
                    <div class="visual-carousel-nav">
                        <button class="nav-btn-circular prev" id="visual-prev"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 18 9 12 15 6"></polyline></svg></button>
                        <button class="nav-btn-circular next" id="visual-next"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg></button>
                    </div>
                    <div class="visual-carousel-track-container">
                        <div class="visual-carousel-track" id="visual-track">
                            {visual_cards}
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section class="collection-section">
            <div class="container collection-flex">
                {master_sidebar}
                <div class="collection-main">
                    <div class="filter-sort-bar">
                        <div class="product-count">{len(products_list)} produits</div>
                        <div class="sort-dropdown-container">
                            <button class="sort-btn" id="sort-dropdown-btn">
                                <span class="current-sort">En vedette</span>
                                <svg class="sort-arrow" viewbox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
                            </button>
                            <div class="sort-menu" id="sort-menu">
                                <div class="sort-option active" data-sort="featured">En vedette</div>
                                <div class="sort-option" data-sort="best-selling">Meilleures ventes</div>
                                <div class="sort-option" data-sort="price-ascending">Prix: faible à élevé</div>
                                <div class="sort-option" data-sort="price-descending">Prix: élevé à faible</div>
                            </div>
                        </div>
                    </div>
                    <div class="collection-grid">
                        {products_list_html(products_list)}
                    </div>
                    
                    <!-- Pagination requested by user -->
                    <div class="pagination-v2">
                        <span class="p-arrow disabled">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 18 9 12 15 6"></polyline></svg>
                        </span>
                        <a href="#" class="p-num active">1</a>
                        <a href="#" class="p-num">2</a>
                        <a href="#" class="p-arrow">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg>
                        </a>
                    </div>
                </div>
            </div>
        </section>
        
        <!-- Recommendations Section -->
        {re.search(r'(<section class="recommendations-section">.*?</section>)', master, re.DOTALL).group(1)}
    </main>
    {master_footer}
    <script src="main.js"></script>
</body>
</html>"""
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)

def products_list_html(products):
    html = ""
    for p in products:
        html += f"""
                        <div class="product-item">
                            <div class="product-img-wrapper">
                                <img alt="{p['name']}" src="{p['img']}" />
                                {"" if not p.get('badge') else f'<span class="status-badge">{p["badge"]}</span>'}
                            </div>
                            <div class="product-info">
                                <h3>{p['name']}</h3>
                                <p class="product-price">{p['price']}</p>
                            </div>
                        </div>"""
    return html

# Corrected Visuals as per User Request
lit_visuals = """
                            <a href="lit-chien.html" class="visual-card">
                                <div class="visual-card-img-box"><img src="dog_bed_premium_1775489579429.png" alt="Lit Chien"></div>
                                <span class="visual-card-label">Lit Chien</span>
                            </a>
                            <a href="lit-xxl-chien.html" class="visual-card">
                                <div class="visual-card-img-box"><img src="cat_coussin_xxl_visual.png" alt="Lit XXL"></div>
                                <span class="visual-card-label">Lit XXL</span>
                            </a>
                            <a href="lit-sureleve-chien.html" class="visual-card">
                                <div class="visual-card-img-box"><img src="dog_bed_premium_1775489579429.png" alt="Lit Surélevé"></div>
                                <span class="visual-card-label">Lit Surélevé</span>
                            </a>
                            <a href="canape-chien.html" class="visual-card">
                                <div class="visual-card-img-box"><img src="cat_protection_canape.png" alt="Canapé Luxe Chien"></div>
                                <span class="visual-card-label">Canapé Luxe Chien</span>
                            </a>
                            <a href="couverture-chien.html" class="visual-card">
                                <div class="visual-card-img-box"><img src="cat_coussin.png" alt="Couvertures Chien"></div>
                                <span class="visual-card-label">Couvertures Chien</span>
                            </a>
                            <a href="protection-canape-chien.html" class="visual-card">
                                <div class="visual-card-img-box"><img src="cat_protection_canape.png" alt="Protection canapé chien"></div>
                                <span class="visual-card-label">Protection canapé chien</span>
                            </a>"""

lit_xxl_products = [
    {"name": "Lit XXL Orthopédique 'Giant Comfort'", "price": "225,00 €", "img": "cat_coussin_xxl_visual.png", "badge": "Premium"},
    {"name": "Lit Scandinave XXL - Gris Anthracite", "price": "199,00 €", "img": "dog_bed_premium_1775489579429.png"},
    {"name": "Matelas XXL Mémoire de Forme - Bleu Nuit", "price": "145,00 €", "img": "cat_tapis_xxl_visual.png", "badge": "Top Vente"},
    {"name": "Coussin XXL Ultra-Moelleux 'Cloud'", "price": "115,00 €", "img": "panier_velvet_main.png"},
    {"name": "Canapé pour Chien XXL - Velours Royal", "price": "299,00 €", "img": "cat_protection_canape.png", "badge": "Luxe"},
    {"name": "Panier XXL Tressé 'Héritage'", "price": "135,00 €", "img": "cat_panier.png"},
    {"name": "Tapis de Couchage XXL - Imperméable", "price": "89,00 €", "img": "cat_tapis_xxl_visual.png"},
    {"name": "Lit Surélevé XXL 'Breezy' - Anti-Chaleur", "price": "155,00 €", "img": "dog_bed_premium_1775489579429.png"},
    {"name": "Coussin Orthopédique XXL - Déhoussable", "price": "165,00 €", "img": "panier_velvet_main.png", "badge": "Nouveau"},
    {"name": "Lit XXL 'Soft Touch' - Rose Poudré", "price": "145,00 €", "img": "cat_coussin.png"},
    {"name": "Matelas de Repos XXL - Garnissage Ergonomique", "price": "125,00 €", "img": "cat_tapis_xxl_visual.png"},
    {"name": "Lit XXL Design Scandinave - Chêne Clair", "price": "245,00 €", "img": "dog_bed_premium_1775489579429.png", "badge": "Exclusif"},
]

# Execute
standardize_page(
    'lit-xxl-chien.html', 
    'Lits XXL pour Chien', 
    '<a href="index.html">Accueil</a> / <a href="panier-chien.html">Couchage</a> / <span>Lits XXL</span>',
    lit_xxl_products,
    lit_visuals.replace('lit-xxl-chien.html" class="visual-card"', 'lit-xxl-chien.html" class="visual-card active"')
)
