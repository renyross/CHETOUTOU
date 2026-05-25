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
    f in ['tapis-chien.html', 'couchage.html', 'promenade.html', 'hygiene.html', 'jouets.html', 'manteaux.html']
)]

# FIXED FILENAMES
# 1. Harnais -> incontournable_harnais_anti_traction_1775493366267.png
# 2. Laisse -> collier_cuir_visual.png
# 3. Panier -> panier_velvet_main.png
# 4. Gamelle -> gamelle_surelevee_visual.png
# 5. Manteau -> manteau_hiver_premium.png

recommendation_block = """        <section class="recommendations-section" style="padding-top: 6rem; border-top: 1px solid #eee; margin-top: 4rem;">
            <div class="container">
                <div class="recommendations-carousel-header" style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 3rem;">
                    <h2 class="section-title-left" style="margin: 0; font-size: 2.2rem; font-weight: 700; letter-spacing: -0.5px;">Vous aimerez aussi</h2>
                    <div class="category-carousel-nav" style="display: flex; gap: 0.8rem;">
                        <button class="nav-arrow nav-prev" id="rec-prev" aria-label="Précédent" style="width: 40px; height: 40px; border: 1px solid #eee; border-radius: 50%; display: flex; align-items: center; justify-content: center; background: #fff; cursor: pointer; transition: all 0.3s; color: #111;">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m15 18-6-6 6-6"/></svg>
                        </button>
                        <button class="nav-arrow nav-next" id="rec-next" aria-label="Suivant" style="width: 40px; height: 40px; border: 1px solid #eee; border-radius: 50%; display: flex; align-items: center; justify-content: center; background: #fff; cursor: pointer; transition: all 0.3s; color: #111;">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>
                        </button>
                    </div>
                </div>
                <div class="recommendations-carousel-wrapper">
                    <div class="recommendations-grid" id="rec-grid">
                        <div class="rec-card">
                            <a href="harnais-anti-traction-chien.html" class="rec-link">
                                <div class="rec-img-box"><img src="incontournable_harnais_anti_traction_1775493366267.png" alt="Harnais Expert"></div>
                                <h3>Harnais Anti-Traction Expert</h3>
                                <div class="rec-price">75,00 €</div>
                            </a>
                        </div>
                        <div class="rec-card">
                            <a href="laisse-cuir-chien.html" class="rec-link">
                                <div class="rec-img-box"><img src="collier_cuir_visual.png" alt="Laisse Cuir"></div>
                                <h3>Laisse Cuir Assortie</h3>
                                <div class="rec-price">45,00 €</div>
                            </a>
                        </div>
                        <div class="rec-card">
                            <a href="panier-chien.html" class="rec-link">
                                <div class="rec-img-box"><img src="panier_velvet_main.png" alt="Panier Apaisant"></div>
                                <h3>Panier Apaisant Velvet</h3>
                                <div class="rec-price">129,00 €</div>
                            </a>
                        </div>
                        <div class="rec-card">
                            <a href="gamelle-surelevee-chien.html" class="rec-link">
                                <div class="rec-img-box"><img src="gamelle_surelevee_visual.png" alt="Gamelle Design"></div>
                                <h3>Gamelle Design Surélevée</h3>
                                <div class="rec-price">65,00 €</div>
                            </a>
                        </div>
                        <div class="rec-card">
                            <a href="manteaux.html" class="rec-link">
                                <div class="rec-img-box"><img src="manteau_hiver_premium.png" alt="Manteau Premium"></div>
                                <h3>Manteau d'Hiver Premium</h3>
                                <div class="rec-price">110,00 €</div>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </section>"""

def update_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update Recommendations
        if '<section class="recommendations-section"' in content:
            content = re.sub(r'<section class="recommendations-section".*?</section>', recommendation_block, content, flags=re.DOTALL)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"Error updating {filepath}: {e}")
        return False

count = 0
for filename in files_to_update:
    if update_file(os.path.join(directory, filename)):
        count += 1

print(f"Successfully fixed images and styles in {count} files.")
