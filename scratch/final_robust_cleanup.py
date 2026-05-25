import os
import re

directory = "/Users/renelrosene/Desktop/boutique chien"

files_to_update = [f for f in os.listdir(directory) if f.endswith('.html') and (
    f.startswith('tapis-') or 
    f.startswith('panier-') or 
    f.startswith('coussin-') or 
    f.startswith('harnais-') or 
    f.startswith('collier-') or
    f in ['couchage.html', 'promenade.html', 'hygiene.html', 'jouets.html', 'manteaux.html']
)]

def clean_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 1. Standardized headers with high-precision alignment
        vis_header = """                    <div class="category-visual-header" style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem;">
                        <h2 style="margin: 0; font-size: 1.15rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1.2px; color: #111;">Parcourir par type</h2>
                        <div class="category-carousel-nav" style="display: flex; gap: 0.8rem; align-items: center;">
                            <button class="nav-arrow nav-prev" id="cat-prev" aria-label="Précédent" style="width: 40px; height: 40px; border: 1px solid #ddd; border-radius: 50%; display: flex; align-items: center; justify-content: center; background: #fff; cursor: pointer; transition: all 0.3s; color: #111;">
                                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m15 18-6-6 6-6"/></svg>
                            </button>
                            <button class="nav-arrow nav-next" id="cat-next" aria-label="Suivant" style="width: 40px; height: 40px; border: 1px solid #ddd; border-radius: 50%; display: flex; align-items: center; justify-content: center; background: #fff; cursor: pointer; transition: all 0.3s; color: #111;">
                                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>
                            </button>
                        </div>
                    </div>"""

        rec_header = """                <div class="recommendations-carousel-header" style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2.5rem;">
                    <h2 class="section-title-left" style="margin: 0; font-size: 2.1rem; font-weight: 700; letter-spacing: -0.6px; color: #111; line-height: 1.1;">Vous aimerez aussi</h2>
                    <div class="category-carousel-nav" style="display: flex; gap: 1rem; align-items: center;">
                        <button class="nav-arrow nav-prev" id="rec-prev" aria-label="Précédent" style="width: 44px; height: 44px; border: 1px solid #ddd; border-radius: 50%; display: flex; align-items: center; justify-content: center; background: #fff; cursor: pointer; transition: all 0.3s; color: #111;">
                            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m15 18-6-6 6-6"/></svg>
                        </button>
                        <button class="nav-arrow nav-next" id="rec-next" aria-label="Suivant" style="width: 44px; height: 44px; border: 1px solid #ddd; border-radius: 50%; display: flex; align-items: center; justify-content: center; background: #fff; cursor: pointer; transition: all 0.3s; color: #111;">
                            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>
                        </button>
                    </div>
                </div>"""

        # 2. Re-apply Visual Carousel structure carefully
        # Locate the container and replace its content entirely to avoid nested-div issues
        if '<div class="category-visual-container">' in content:
            # Match the container AND its content up to the first closing tag that matches the depth
            # Since regex isn't great for nested tags, we'll try to find the list block specifically
            list_match = re.search(r'<div class="category-visual-list">.*?</a>\s*</div>', content, flags=re.DOTALL)
            if list_match:
                list_html = list_match.group(0)
                # Ensure the list_html doesn't have extra closing tags at the end
                list_html = re.sub(r'</div>\s*</div>\s*</div>$', '</div>', list_html)
                
                # Replace the entire container block
                # Looking for container start until it hits the list end + one more div
                pattern = r'<div class="category-visual-container">.*?<div class="category-visual-list">.*?</a>\s*</div>\s*</div>'
                replacement = '<div class="category-visual-container">\n' + vis_header + '\n                    ' + list_html + '\n                </div>'
                content = re.sub(pattern, replacement, content, flags=re.DOTALL)

        # 3. Re-apply Recommendations Header
        if '<div class="recommendations-carousel-header"' in content:
            content = re.sub(r'<div class="recommendations-carousel-header".*?</div>\s*</div>', rec_header + "\n                </div>", content, flags=re.DOTALL)

        # 4. Clean up any lingering duplicates from previous errors
        # If there's still a category-visual-list OUTSIDE a container, remove it.
        # Check if there's a </div> closed right before a floating list
        content = re.sub(r'</div>\s*</div>\s*</section>\s*<div class="category-visual-list">.*?</div>\s*</div>', '</div>\n            </div>\n        </section>', content, flags=re.DOTALL)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

for filename in files_to_update:
    clean_file(os.path.join(directory, filename))
print("Cleanup complete.")
