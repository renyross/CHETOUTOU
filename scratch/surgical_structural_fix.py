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

def fix_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 1. Standardized Headers
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

        # 2. Extract ONLY the items (<a> tags) from the visual list
        # We look for all <a> tags that look like category cards
        items = re.findall(r'<a href=".*?" class="category-visual-card">.*?</a>', content, flags=re.DOTALL)
        if items:
            # Take first 8 unique items (or however many there are)
            seen = set()
            unique_items = []
            for item in items:
                href = re.search(r'href="(.*?)"', item).group(1)
                if href not in seen:
                    seen.add(href)
                    unique_items.append(item)
            
            list_content = '\n                        '.join(unique_items[:12]) # Up to 12
            
            # Now replace the whole container with a CLEAN version
            # We look for the start of the container until we hit the end of the whole visual section
            # Pattern: start of container until the first sidebar or collection-section
            section_pattern = r'<div class="category-visual-container">.*?</section>'
            # This is too broad. Let's find the container block specifically.
            # We'll use a placeholder and then replace it.
            
            new_container = f"""<div class="category-visual-container">
{vis_header}
                    <div class="category-visual-list">
                        {list_content}
                    </div>
                </div>"""

            # Surgical replacement of the broken mess
            # Find the start of the container and the end of any visual list
            content = re.sub(r'<div class="category-visual-container">.*?<div class="category-visual-list">.*?</div>\s*</div>\s*</div>\s*</div>', new_container + '\n            </div>\n        </section>', content, flags=re.DOTALL)
            # Fallback for different nesting
            content = re.sub(r'<div class="category-visual-container">.*?<div class="category-visual-list">.*?</div>\s*</div>', new_container, content, flags=re.DOTALL)

        # 3. Recommendations
        if '<div class="recommendations-carousel-header"' in content:
            content = re.sub(r'<div class="recommendations-carousel-header".*?</div>\s*</div>', rec_header + "\n                </div>", content, flags=re.DOTALL)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        return False

for filename in files_to_update:
    fix_file(os.path.join(directory, filename))
print("Final fix complete.")
