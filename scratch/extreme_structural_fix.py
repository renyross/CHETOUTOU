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

def extreme_fix(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 1. Identify the mess
        # The mess is between the intro-large and the collection-section
        if 'class="logo">Chetoutou</a>' in content:
            # We need to extract the REAL category cards first
            # The real cards have class="category-visual-card"
            real_cards = re.findall(r'<a href="[^"]*?" class="category-visual-card">.*?</a>', content, flags=re.DOTALL)
            unique_cards = []
            seen = set()
            for c in real_cards:
                m = re.search(r'href="([^"]*?)"', c)
                if m:
                    href = m.group(1)
                    if href not in seen:
                        seen.add(href)
                        unique_cards.append(c)
            
            cards_html = '\n                        '.join(unique_cards[:10])
            
            new_visual_section = f"""
                <div class="category-visual-container">
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
                </div>
            </div>
        </section>
"""
            # Replace the whole mess from the start of the container to the start of the collection section
            content = re.sub(r'<div class="category-visual-container">.*?<section class="collection-section">', new_visual_section + '\n                <section class="collection-section">', content, flags=re.DOTALL)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception:
        return False

for filename in files_to_fix:
    extreme_fix(os.path.join(directory, filename))
print("Extreme fix complete.")
