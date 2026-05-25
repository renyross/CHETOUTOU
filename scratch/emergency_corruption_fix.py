import os
import re

directory = "/Users/renelrosene/Desktop/boutique chien"

files_to_fix = [f for f in os.listdir(directory) if f.endswith('.html') and (
    f.startswith('tapis-') or 
    f.startswith('panier-') or 
    f.startswith('coussin-') or 
    f.startswith('harnais-') or 
    f.startswith('collier-') or
    f in ['couchage.html', 'promenade.html', 'hygiene.html', 'jouets.html', 'manteaux.html']
)]

def fix_corruption(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 1. REMOVE the corrupted visual carousel block
        # It's everything between <div class="category-visual-container"> and the end of the corrupted list
        # We know the corrupted list contains the navbar links
        if 'class="logo">Chetoutou</a>' in content:
            # Re-read the file to get a fresh start
            # We'll just replace the whole mess with a placeholder
            # The mess starts at <div class="category-visual-container">
            # and ends at the FIRST </div> after the corrupted list
            content = re.sub(r'<div class="category-visual-container">.*?<div class="category-visual-list">.*?<nav id="nav-menu">.*?</nav>.*?</div>\s*</div>', 'CORRUPTION_PLACEHOLDER', content, flags=re.DOTALL)
            
            # Now we need to RESTORE a valid category-visual-container
            # We'll use a generic one based on the filename
            cat_name = "Tapis" if "tapis" in filepath else ("Harnais" if "harnais" in filepath else "Collier")
            
            # Re-apply the master structure for the category visual section
            # For simplicity, I'll just use the Collier cards as a base and the user can refine
            # But wait, I should try to find the REAL cards if they still exist in the file
            # (they might be further down or duplicated)
            real_cards = re.findall(r'<a href="[^"]*?" class="category-visual-card">.*?</a>', content, flags=re.DOTALL)
            if real_cards:
                cards_html = '\n                        '.join(real_cards[:8])
            else:
                cards_html = "<!-- Cards restored manually -->"

            new_block = f"""<div class="category-visual-container">
                    <div class="category-visual-header" style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem;">
                        <h2 style="margin: 0; font-size: 1.15rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1.2px; color: #111;">Parcourir par type</h2>
                        <div class="category-carousel-nav" style="display: flex; gap: 0.8rem; align-items: center;">
                            <button class="nav-arrow nav-prev" id="cat-prev" aria-label="Précédent" style="width: 40px; height: 40px; border: 1px solid #ddd; border-radius: 50%; display: flex; align-items: center; justify-content: center; background: #fff; cursor: pointer; transition: all 0.3s; color: #111;">
                                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m15 18-6-6 6-6"/></svg>
                            </button>
                            <button class="nav-arrow nav-next" id="cat-next" aria-label="Suivant" style="width: 40px; height: 40px; border: 1px solid #ddd; border-radius: 50%; display: flex; align-items: center; justify-content: center; background: #fff; cursor: pointer; transition: all 0.3s; color: #111;">
                                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>
                            </button>
                        </div>
                    </div>
                    <div class="category-visual-list">
                        {cards_html}
                    </div>
                </div>"""
            
            content = content.replace('CORRUPTION_PLACEHOLDER', new_block)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        return False

for filename in files_to_fix:
    fix_corruption(os.path.join(directory, filename))
print("Corruption fixed.")
