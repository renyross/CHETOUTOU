import os
import re

new_sidebar = """<aside class="sidebar" id="collection-sidebar">
    <div class="sidebar-header-mobile">
        <button id="close-filters" aria-label="Fermer les filtres">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <line x1="18" y1="6" x2="6" y2="18"></line>
                <line x1="6" y1="6" x2="18" y2="18"></line>
            </svg>
        </button>
    </div>
    
    <!-- Disponibilité -->
    <div class="filter-group active">
        <button class="filter-group-header">
            Disponibilité
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
        </button>
        <div class="filter-group-content">
            <div class="checkbox-list">
                <label class="checkbox-item"><input type="checkbox"> En stock <span>(489)</span></label>
                <label class="checkbox-item"><input type="checkbox"> En rupture de stock <span>(47)</span></label>
            </div>
        </div>
    </div>

    <!-- Prix -->
    <div class="filter-group active">
        <button class="filter-group-header">
            Prix
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
        </button>
        <div class="filter-group-content">
            <p class="price-max-text">Le prix le plus élevé est 299,95€</p>
            <div class="price-slider-container" id="price-slider-root">
                <div class="price-track"></div>
                <div class="price-range-active" id="price-range-active"></div>
                <div class="slider-handle handle-left" id="price-min-handle" style="left: 0%;"></div>
                <div class="slider-handle handle-right" id="price-max-handle" style="left: 100%;"></div>
            </div>
            <div class="price-range-inputs">
                <div class="price-input-wrapper">
                    <span class="price-currency">€</span>
                    <input type="text" id="price-min-field" placeholder="0" class="price-field">
                </div>
                <div class="price-input-wrapper">
                    <span class="price-currency">€</span>
                    <input type="text" id="price-max-field" placeholder="299,95" class="price-field">
                </div>
            </div>
        </div>
    </div>

    <!-- Couleur -->
    <div class="filter-group active">
        <button class="filter-group-header">
            Couleur
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
        </button>
        <div class="filter-group-content">
            <div class="color-swatch-list">
                <div class="color-swatch" style="background: #f5f5dc;" title="Beige"></div>
                <div class="color-swatch white" style="background: #ffffff;" title="Blanc"></div>
                <div class="color-swatch" style="background: #0000ff;" title="Bleu"></div>
                <div class="color-swatch" style="background: #add8e6;" title="Bleu ciel"></div>
                <div class="color-swatch" style="background: #800000;" title="Bordeaux"></div>
                <div class="color-swatch" style="background: #a52a2a;" title="Marron"></div>
                <div class="color-swatch" style="background: #5d6d5d;" title="Vert d'eau"></div>
                <div class="color-swatch" style="background: #808080;" title="Gris"></div>
                <div class="color-swatch" style="background: #ffd700;" title="Or"></div>
                <div class="color-swatch" style="background: #ffff00;" title="Jaune"></div>
                <div class="color-swatch" style="background: #111111;" title="Noir"></div>
                <div class="color-swatch" style="background: #ff4500;" title="Orange"></div>
                <div class="color-swatch" style="background: #ffc0cb;" title="Rose"></div>
                <div class="color-swatch" style="background: #ff0000;" title="Rouge"></div>
                <div class="color-swatch" style="background: #00ff00;" title="Vert"></div>
                <div class="color-swatch" style="background: #ee82ee;" title="Violet"></div>
            </div>
        </div>
    </div>

    <!-- Taille du chien -->
    <div class="filter-group active">
        <button class="filter-group-header">
            Taille du chien
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
        </button>
        <div class="filter-group-content">
            <div class="checkbox-list">
                <label class="checkbox-item"><input type="checkbox"> S (Petit) <span>(12)</span></label>
                <label class="checkbox-item"><input type="checkbox"> M (Grand) <span>(84)</span></label>
                <label class="checkbox-item"><input type="checkbox"> L (Moyen/Large) <span>(28)</span></label>
                <label class="checkbox-item"><input type="checkbox"> XL (Très large) <span>(12)</span></label>
            </div>
        </div>
    </div>

    <!-- Matière -->
    <div class="filter-group active">
        <button class="filter-group-header">
            Matière
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
        </button>
        <div class="filter-group-content">
            <div class="checkbox-list">
                <label class="checkbox-item"><input type="checkbox"> Cuir Italien <span>(63)</span></label>
                <label class="checkbox-item"><input type="checkbox"> Nylon tressé <span>(95)</span></label>
                <label class="checkbox-item"><input type="checkbox"> Biothane <span>(14)</span></label>
                <label class="checkbox-item"><input type="checkbox"> Technique / Imperméable <span>(163)</span></label>
            </div>
        </div>
    </div>

    <!-- Catégories -->
    <div class="filter-group active">
        <button class="filter-group-header">
            Catégories
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
        </button>
        <div class="filter-group-content">
            <ul class="category-filter-list">
                <li><a href="collier-chien.html">Colliers</a></li>
                <li><a href="harnais-chien.html">Harnais</a></li>
                <li><a href="promenade.html">Laisses & Longes</a></li>
                <li><a href="impermeables.html">Vêtements (StormGuard)</a></li>
                <li><a href="index.html#accessoires">Accessoires</a></li>
            </ul>
        </div>
    </div>
</aside>"""

# List of files from grep
files = [
    "balles-chien.html", "boite-croquettes.html", "bottine-chien.html", "brosses.html", 
    "canape-chien.html", "collier-anti-aboiement-chien.html", "collier-anti-fugue-chien.html", 
    "collier-anti-puce-chien.html", "collier-chien.html", "collier-cuir-chien.html", 
    "collier-dressage-chien.html", "collier-electrique-chien.html", "collier-etrangleur-chien.html", 
    "collier-gps-chien.html", "collier-lumineux-chien.html", "collier-personnalise-chien.html", 
    "couchage.html", "coussin-chien.html", "couverture-chien.html", "double-laisse-chien.html", 
    "doudou-chien.html", "frisbee-chien.html", "gamelle-anti-glouton.html", 
    "gamelle-ceramique-chien.html", "gamelle-personnalisee-chien.html", 
    "gamelle-surelevee-chien.html", "gamelles.html", "harnais-anti-fugue-chien.html", 
    "harnais-anti-traction-chien.html", "harnais-canicross-chien.html", "harnais-chien-course.html", 
    "harnais-chien-voiture.html", "harnais-chien-y.html", "harnais-chien.html", 
    "harnais-cuir-chien.html", "harnais-gros-chien.html", "harnais-levage-chien.html", 
    "harnais-personnalise-chien.html", "harnais-petit-chien.html", "harnais-tactique-chien.html", 
    "harnais-traction-chien.html", "impermeables.html", "jeux-occupation.html", 
    "jouet-interactif-chien.html", "jouets-indestructibles.html", "jouets.html", 
    "laisse-chien-course.html", "laisse-chien-velo.html", "laisse-chien.html", 
    "laisse-corde-chien.html", "laisse-cuir-chien.html", "laisse-enrouleur-chien.html", 
    "laisse-lasso-chien.html", "laisse-longe-chien.html", "laisse-main-libre-chien.html", 
    "laisses-classiques.html", "lanceur-balle-chien.html", "lit-chien.html", 
    "lit-sureleve-chien.html", "lit-xxl-chien.html", "longue-laisse-chien.html", 
    "manteaux.html", "medailles.html", "museliere.html", "panier-chien.html", 
    "panier-dehoussable-chien.html", "panier-grand-chien.html", "panier-orthopedique-chien.html", 
    "panier-osier-chien.html", "panier-petit-chien.html", "panier-plastique-chien.html", 
    "panier-velo-chien.html", "panier-voiture-chien.html", "panier-xxl-chien.html", 
    "peluches-chien.html", "promenade.html", "pull-sweat.html", "sac-a-crottes.html", 
    "sac-a-dos-chien.html", "sac-chien.html", "sac-transport-chien.html", 
    "tapis-absorbant-chien.html", "tapis-fouille.html", "tapis-gamelle-chien.html", 
    "tapis-lechage.html", "tapis-rafraichissant-chien.html", "tapis-xxl-chien.html", 
    "tshirt-polo.html"
]

pattern = re.compile(r'<aside class="sidebar" id="collection-sidebar">.*?</aside>', re.DOTALL)

for filename in files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if pattern.search(content):
            new_content = pattern.sub(new_sidebar, content)
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
        else:
            print(f"Sidebar not found in {filename}")
    else:
        print(f"File {filename} not found")
