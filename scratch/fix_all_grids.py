import os
import re

# --- Product Data ---
HARNAIS_PR = """                        <div class="product-item">
                            <div class="product-img-wrapper"><img src="harnais_anti_traction_main_1775840455761.png" alt="Harnais"></div>
                            <div class="product-info"><h3>Harnais SteadyWalk</h3><p class="product-price">49 €</p></div>
                        </div>
                        <div class="product-item">
                            <div class="product-img-wrapper"><img src="incontournable_harnais_anti_traction_1775493366267.png" alt="Harnais"></div>
                            <div class="product-info"><h3>Harnais Pro-Expert</h3><p class="product-price">75 €</p></div>
                        </div>"""

COLLIER_PR = """                        <div class="product-item">
                            <div class="product-img-wrapper"><img src="cat_collier_pure_v2.png" alt="Collier Pure"></div>
                            <div class="product-info"><h3>Collier Pure Comfort</h3><p class="product-price">25 €</p></div>
                        </div>
                        <div class="product-item">
                            <div class="product-img-wrapper"><img src="collier_cuir_visual.png" alt="Collier Cuir"></div>
                            <div class="product-info"><h3>Collier Cuir Elegance</h3><p class="product-price">45 €</p></div>
                        </div>"""

TAPIS_PR = """                        <div class="product-item">
                            <div class="product-img-wrapper"><img src="tapis_rafraichissant_visual.png" alt="Tapis"></div>
                            <div class="product-info"><h3>Tapis Fraîcheur Premium</h3><p class="product-price">35 €</p></div>
                        </div>"""

COUCHAGE_PR = """                        <div class="product-item">
                            <div class="product-img-wrapper"><img src="panier_velvet_main.png" alt="Panier Velvet"></div>
                            <div class="product-info"><h3>Panier Royal Velvet</h3><p class="product-price">129 €</p></div>
                        </div>"""

PROMENADE_PR = """                        <div class="product-item">
                            <div class="product-img-wrapper"><img src="dog_leash_elegant_1775487863541.png" alt="Laisse"></div>
                            <div class="product-info"><h3>Laisse Oxford Cuir</h3><p class="product-price">45 €</p></div>
                        </div>"""

def fix_everything(filename, products):
    if not os.path.exists(filename): return
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix Triple Class Attribute
    content = re.sub(r'class="active"\s+class="active"\s+class="category-visual-card active"', 
                     r'class="category-visual-card active"', content)

    # 2. Fix Broken Grid and Div Closures
    # Match the collection-main div and replace its content to be clean
    main_match = re.search(r'<div class="collection-main">.*?</div>\s*</div>\s*</section>', content, flags=re.DOTALL)
    if main_match:
        main_html = main_match.group(0)
        # Construct clean collection-main
        clean_main = f"""<div class="collection-main">
                    <div class="filter-sort-bar">
                        <div class="product-count">6 produits</div>
                    </div>
                    <div class="collection-grid">
{products}
                    </div>
                </div>
            </div>
        </section>"""
        content = content.replace(main_match.group(0), clean_main)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

# Execution groups
groups = [
    ('harnais', HARNAIS_PR),
    ('collier', COLLIER_PR),
    ('tapis', TAPIS_PR),
    ('panier', COUCHAGE_PR),
    ('lit-', COUCHAGE_PR),
    ('coussin', COUCHAGE_PR),
    ('promenade', PROMENADE_PR),
    ('laisse', PROMENADE_PR),
    ('sac-', PROMENADE_PR)
]

for pattern, prds in groups:
    files = [f for f in os.listdir('.') if pattern in f and f.endswith('.html')]
    for f in files:
        fix_everything(f, prds)
        print(f"Fixed {f}")
