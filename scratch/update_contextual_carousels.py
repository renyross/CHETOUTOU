import os
import re

# Global Navigation Definition
GLOBAL_NAV = [
    ("Promenade", "promenade.html", "category_promenade_pure.png"),
    ("Couchage", "couchage.html", "category_couchage_pure.png"),
    ("Jouets", "jouets.html", "category_jouets_pure.png"),
    ("Hygiène", "gamelles.html", "category_hygiene_pure.png"),
    ("Accessoires", "medailles.html", "category_accessoires_pure.png")
]

def generate_carousel_html():
    items_html = ""
    for label, link, img in GLOBAL_NAV:
        items_html += f"""                            <a href="{link}" class="tag-item">
                                <div class="tag-icon"><img src="{img}" alt=""></div>
                                <span>{label}</span>
                            </a>\n"""
    
    return f"""                <div class="category-carousel-wrapper">
                    <button class="carousel-nav prev" id="cat-prev" aria-label="Précédent">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"></polyline></svg>
                    </button>
                    <div class="category-carousel">
                        <div class="category-tags-row">
{items_html.rstrip()}
                        </div>
                    </div>
                    <button class="carousel-nav next" id="cat-next" aria-label="Suivant">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"></polyline></svg>
                    </button>
                </div>"""

def update_carousels():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    exclude = ['index.html', 'blog.html', 'coordonnees.html', 'faq.html', 'guide-tailles.html', 'politique-confidentialite.html', 'politique-expedition.html', 'politique-remboursement.html', 'conditions-utilisation.html', 'preferences-cookies.html', 'checkout.html']
    
    new_carousel = generate_carousel_html()
    
    for filename in html_files:
        if filename in exclude:
            continue
            
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Target the entire carousel wrapper to replace it
        start_tag = '<div class="category-carousel-wrapper">'
        if start_tag in content:
            # We look for the closing button then the closing div of the wrapper
            # Structure we're looking for: <div class="category-carousel-wrapper">...<button class="carousel-nav next"...>...</button></div>
            end_marker = '</button>\s*</div>'
            pattern = re.escape(start_tag) + r'.*?' + end_marker
            
            new_content = re.sub(pattern, new_carousel, content, flags=re.DOTALL)
            
            if new_content != content:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated global carousel in {filename}")

if __name__ == "__main__":
    update_carousels()
