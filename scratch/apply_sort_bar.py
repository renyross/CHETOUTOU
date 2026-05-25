import os
import re

# The HTML block to insert
sort_bar_html = """                    <div class="filter-sort-bar">
                        <div class="product-count">12 produits</div>
                        <div class="sort-dropdown-container">
                            <button class="sort-btn" id="sort-dropdown-btn">
                                <span class="current-sort">En vedette</span>
                                <svg class="sort-arrow" viewbox="0 0 24 24" fill="none" stroke="currentColor"
                                    stroke-width="1.5">
                                    <polyline points="6 9 12 15 18 9"></polyline>
                                </svg>
                            </button>
                            <div class="sort-menu" id="sort-menu">
                                <div class="sort-option active" data-sort="featured">En vedette</div>
                                <div class="sort-option" data-sort="relevant">Le plus pertinent</div>
                                <div class="sort-option" data-sort="best-selling">Meilleures ventes</div>
                                <div class="sort-option" data-sort="title-ascending">Alphabétique, de A à Z</div>
                                <div class="sort-option" data-sort="title-descending">Alphabétique, de Z à A</div>
                                <div class="sort-option" data-sort="price-ascending">Prix: faible à élevé</div>
                                <div class="sort-option" data-sort="price-descending">Prix: élevé à faible</div>
                                <div class="sort-option" data-sort="created-ascending">Date, de la plus ancienne à la plus
                                    récente</div>
                                <div class="sort-option" data-sort="created-descending">Date, de la plus récente à la plus
                                    ancienne</div>
                            </div>
                        </div>
                    </div>"""

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already has sort bar
    if 'filter-sort-bar' in content:
        print(f"Skipping {filepath} (already has sort bar)")
        return

    # Check if it has collection-main
    if '<div class="collection-main">' in content:
        print(f"Updating {filepath}...")
        # Insert after <div class="collection-main">
        pattern = r'(<div class="collection-main">)'
        new_content = re.sub(pattern, r'\1\n' + sort_bar_html, content)
        
        # Also remove any old mobile-only triggers if they were meant to be replaced or combined
        # (Keeping them for now as the CSS hides the desktop one on mobile)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

root_dir = "/Users/renelrosene/Desktop/boutique chien"
for filename in os.listdir(root_dir):
    if filename.endswith(".html"):
        update_file(os.path.join(root_dir, filename))
