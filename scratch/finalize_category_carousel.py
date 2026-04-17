import os
import re

CAROUSEL_HTML = """                <div class="category-carousel-wrapper">
                    <button class="carousel-nav prev" id="cat-prev" aria-label="Précédent">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"></polyline></svg>
                    </button>
                    <div class="category-carousel">
                        <div class="category-tags-row">
                            <a href="promenade.html" class="tag-item">
                                <div class="tag-icon"><img src="dog_harness_premium_1775487844838.png" alt=""></div>
                                <span>Promenade</span>
                            </a>
                            <a href="couchage.html" class="tag-item">
                                <div class="tag-icon"><img src="dog_bed_premium_1775489579429.png" alt=""></div>
                                <span>Couchage</span>
                            </a>
                            <a href="jouets.html" class="tag-item">
                                <div class="tag-icon"><img src="dog_toys_premium_1775489913031.png" alt=""></div>
                                <span>Jouets</span>
                            </a>
                            <a href="index.html#hygiene" class="tag-item">
                                <div class="tag-icon"><img src="dog_hygiene_premium_set_1775490826943.png" alt=""></div>
                                <span>Hygiène & Soins</span>
                            </a>
                            <a href="index.html#accessoires" class="tag-item">
                                <div class="tag-icon"><img src="dog_accessories_premium_collection_1775492773834.png" alt=""></div>
                                <span>Accessoires</span>
                            </a>
                        </div>
                    </div>
                    <button class="carousel-nav next" id="cat-next" aria-label="Suivant">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"></polyline></svg>
                    </button>
                </div>"""

def finalize_carousel():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    exclude = ['index.html', 'blog.html', 'coordonnees.html', 'faq.html', 'guide-tailles.html', 'politique-confidentialite.html', 'politique-expedition.html', 'politique-remboursement.html', 'conditions-utilisation.html', 'preferences-cookies.html', 'checkout.html']
    
    for filename in html_files:
        if filename in exclude:
            continue
            
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Identify the broken/current seo-page-section
        # We target from h1 to the end of that section
        pattern = r'(<h1>.*?</h1>).*?</section>'
        if re.search(pattern, content, re.DOTALL):
            new_section_content = r'\1\n' + CAROUSEL_HTML + "\n            </div>\n        </section>"
            content = re.sub(pattern, new_section_content, content, flags=re.DOTALL)
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Finalized carousel in {filename}")

if __name__ == "__main__":
    finalize_carousel()
