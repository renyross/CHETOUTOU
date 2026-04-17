import os
import re

TAGS_HTML = """                <div class="category-tags-row">
                    <a href="promenade.html" class="tag-item">
                        <div class="tag-icon"><img src="dog_harness_premium_1775487844838.png" alt=""></div>
                        Promenade
                    </a>
                    <a href="couchage.html" class="tag-item">
                        <div class="tag-icon"><img src="dog_bed_premium_1775489579429.png" alt=""></div>
                        Couchage
                    </a>
                    <a href="jouets.html" class="tag-item">
                        <div class="tag-icon"><img src="dog_toys_premium_1775489913031.png" alt=""></div>
                        Jouets
                    </a>
                    <a href="index.html#hygiene" class="tag-item">
                        <div class="tag-icon"><img src="dog_hygiene_premium_set_1775490826943.png" alt=""></div>
                        Hygiène & Soins
                    </a>
                    <a href="index.html#accessoires" class="tag-item">
                        <div class="tag-icon"><img src="dog_accessories_premium_collection_1775492773834.png" alt=""></div>
                        Accessoires
                    </a>
                </div>"""

def restore_tags():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    # Skip non-category pages
    exclude = ['index.html', 'blog.html', 'coordonnees.html', 'faq.html', 'guide-tailles.html', 'politique-confidentialite.html', 'politique-expedition.html', 'politique-remboursement.html', 'conditions-utilisation.html', 'preferences-cookies.html', 'checkout.html']
    
    for filename in html_files:
        if filename in exclude:
            continue
            
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find the truncated category-tags-row and replace it
        # The truncated version looks like: <div class="category-tags-row"> ... </div> </section>
        
        pattern = r'(<div class="category-tags-row">.*?)</div>\s*</section>'
        if re.search(pattern, content, re.DOTALL):
            new_content = re.sub(pattern, TAGS_HTML + "\n            </div>\n        </section>", content, flags=re.DOTALL)
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Restored tags in {filename}")

if __name__ == "__main__":
    restore_tags()
