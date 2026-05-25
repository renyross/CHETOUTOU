
import os
import re

recommendation_block = """
        <!-- Recommendations Section -->
        <section class="recommendations-section">
            <div class="container">
                <h2 class="section-title-left">Vous aimerez aussi</h2>
                <div class="recommendations-carousel-wrapper">
                    <button class="slider-arrow prev" id="rec-prev" aria-label="Précédent">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 18 9 12 15 6"></polyline></svg>
                    </button>
                    <div class="recommendations-grid" id="rec-grid">
                        <div class="rec-card">
                            <a href="harnais-anti-traction-chien.html" class="rec-link">
                                <div class="rec-img-box"><img src="harnais_anti_traction_main_1775840455761.png" alt="Harnais"></div>
                                <h3>Harnais SteadyWalk</h3>
                                <div class="rec-price">49,00 €</div>
                            </a>
                        </div>
                        <div class="rec-card">
                            <a href="collier-cuir-chien.html" class="rec-link">
                                <div class="rec-img-box"><img src="collier_cuir_visual.png" alt="Collier Cuir"></div>
                                <h3>Collier Cuir Heritage</h3>
                                <div class="rec-price">125,00 €</div>
                            </a>
                        </div>
                        <div class="rec-card">
                            <a href="laisse-chien.html" class="rec-link">
                                <div class="rec-img-box"><img src="dog_leash_elegant_1775487863541.png" alt="Laisse"></div>
                                <h3>Laisse Cuir Elegance</h3>
                                <div class="rec-price">45,00 €</div>
                            </a>
                        </div>
                        <div class="rec-card">
                            <a href="panier-chien.html" class="rec-link">
                                <div class="rec-img-box"><img src="incontournable_panier_velvet_ortho_1775493402134.png" alt="Panier"></div>
                                <h3>Panier Velvet Ortho</h3>
                                <div class="rec-price">145,00 €</div>
                            </a>
                        </div>
                        <div class="rec-card">
                            <a href="jouets.html" class="rec-link">
                                <div class="rec-img-box"><img src="incontournable_jouet_snuffle_mat_1775493547836.png" alt="Jouet"></div>
                                <h3>Tapis de Fouille Snuffle</h3>
                                <div class="rec-price">34,00 €</div>
                            </a>
                        </div>
                        <div class="rec-card">
                            <a href="hygiene.html" class="rec-link">
                                <div class="rec-img-box"><img src="gamelle_surelevee_visual.png" alt="Gamelle"></div>
                                <h3>Gamelle Surélevée Design</h3>
                                <div class="rec-price">29,00 €</div>
                            </a>
                        </div>
                    </div>
                    <div class="carousel-dots" id="rec-dots"></div>
                    <button class="slider-arrow next" id="rec-next" aria-label="Suivant">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg>
                    </button>
                </div>
            </div>
        </section>
"""

def standardize_recommendations():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]

    for filename in html_files:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern to find the recommendations section
        pattern = r'<!-- Recommendations Section -->\s*<section class="recommendations-section">.*?</section>'
        # Also handle cases without the comment
        pattern_no_comment = r'<section class="recommendations-section">.*?</section>'
        
        if re.search(pattern, content, re.DOTALL):
            new_content = re.sub(pattern, recommendation_block, content, flags=re.DOTALL)
        elif re.search(pattern_no_comment, content, re.DOTALL):
            new_content = re.sub(pattern_no_comment, recommendation_block, content, flags=re.DOTALL)
        else:
            continue
            
        if new_content != content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Standardized recommendations in {filename}")

if __name__ == "__main__":
    standardize_recommendations()
