import os
import re

directory = "/Users/renelrosene/Desktop/boutique chien"

# List of pages to update
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
        
        # 1. REMOVE ORPHAN category-visual-list blocks
        # These are usually followed by another category-visual-list inside a container, 
        # or they are leftovers from a failed previous edit.
        # Pattern: a category-visual-list that is NOT immediately preceded by a category-visual-header within the same container.
        
        # We can look for the specific pattern of my previous failure: 
        # </div>\s*</div>\s*</div>\s*<div class="category-visual-list">
        content = re.sub(r'</div>\s*</div>\s*</div>\s*<div class="category-visual-list">.*?</div>\s*</div>', '</div>\n            </div>\n        </section>', content, flags=re.DOTALL)
        
        # Another pattern: orphan list just floating
        # <div class="category-visual-list">...</div>
        # But only if it's not preceded by its header.
        
        # Let's be more surgical: If there are TWO category-visual-list, remove the second one if it's outside a container.
        lists = list(re.finditer(r'<div class="category-visual-list">', content))
        if len(lists) > 1:
            # Keep the first one if it has a header, or try to merge.
            # For now, let's just remove the one that is NOT inside a 'category-visual-container'
            pass # We'll use a more global approach

        # 2. Re-apply the CORRECT structure to ensure everything is perfect
        # This will also fix the alignment issue by standardizing the header style.
        
        # Fix alignment and structure for Visual Category Carousel
        if '<div class="category-visual-container">' in content:
            # Standardized Header
            new_header = """                    <div class="category-visual-header" style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem;">
                        <h2 style="margin: 0; font-size: 1.1rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; color: #111;">Parcourir par type</h2>
                        <div class="category-carousel-nav" style="display: flex; gap: 1rem; align-items: center;">
                            <button class="nav-arrow nav-prev" id="cat-prev" aria-label="Précédent" style="width: 40px; height: 40px; border: 1px solid #ddd; border-radius: 50%; display: flex; align-items: center; justify-content: center; background: #fff; cursor: pointer; transition: all 0.3s; color: #111;">
                                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m15 18-6-6 6-6"/></svg>
                            </button>
                            <button class="nav-arrow nav-next" id="cat-next" aria-label="Suivant" style="width: 40px; height: 40px; border: 1px solid #ddd; border-radius: 50%; display: flex; align-items: center; justify-content: center; background: #fff; cursor: pointer; transition: all 0.3s; color: #111;">
                                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>
                            </button>
                        </div>
                    </div>"""
            
            # Find the list content
            list_match = re.search(r'<div class="category-visual-list">.*?</div>', content, flags=re.DOTALL)
            if list_match:
                list_content = list_match.group(0)
                # Replace the whole container
                pattern = r'<div class="category-visual-container">.*?</div>\s*</div>'
                replacement = '<div class="category-visual-container">\n' + new_header + '\n                    ' + list_content + '\n                </div>'
                content = re.sub(pattern, replacement, content, flags=re.DOTALL)

        # 3. Fix Recommendation Header Alignment (Center arrows with title)
        if '<div class="recommendations-carousel-header"' in content:
            rec_header_fix = """                <div class="recommendations-carousel-header" style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 3rem;">
                    <h2 class="section-title-left" style="margin: 0; font-size: 2.2rem; font-weight: 700; letter-spacing: -0.5px; color: #111; line-height: 1.1;">Vous aimerez aussi</h2>
                    <div class="category-carousel-nav" style="display: flex; gap: 1rem; align-items: center;">
                        <button class="nav-arrow nav-prev" id="rec-prev" aria-label="Précédent" style="width: 44px; height: 44px; border: 1px solid #ddd; border-radius: 50%; display: flex; align-items: center; justify-content: center; background: #fff; cursor: pointer; transition: all 0.3s; color: #111;">
                            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m15 18-6-6 6-6"/></svg>
                        </button>
                        <button class="nav-arrow nav-next" id="rec-next" aria-label="Suivant" style="width: 44px; height: 44px; border: 1px solid #ddd; border-radius: 50%; display: flex; align-items: center; justify-content: center; background: #fff; cursor: pointer; transition: all 0.3s; color: #111;">
                            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>
                        </button>
                    </div>
                </div>"""
            content = re.sub(r'<div class="recommendations-carousel-header".*?</div>\s*</div>', rec_header_fix + "\n                </div>", content, flags=re.DOTALL)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"Error cleaning {filepath}: {e}")
        return False

count = 0
for filename in files_to_update:
    if clean_file(os.path.join(directory, filename)):
        count += 1

print(f"Successfully cleaned and aligned {count} files.")
