import os
import re

new_newsletter_html = """        <!-- Unified Newsletter Section -->
        <section class="unified-newsletter">
            <div class="container">
                <div class="newsletter-card">
                    <h2>Économisez 10% sur votre première commande</h2>
                    <p>Inscrivez-vous à notre Newsletter et recevez 10% de réduction immédiate sur votre première acquisition.</p>
                    <div class="newsletter-form-container">
                        <form class="modern-newsletter-form">
                            <input type="email" placeholder="Votre adresse email" required>
                            <button type="submit" class="modern-submit-btn" aria-label="S'inscrire">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <line x1="5" y1="12" x2="19" y2="12"></line>
                                    <polyline points="12 5 19 12 12 19"></polyline>
                                </svg>
                            </button>
                        </form>
                    </div>
                </div>
            </div>
        </section>"""

# More flexible regex to catch various structures using the class names
promo_regex = re.compile(r'<section class="promo-newsletter">.*?</section>', re.DOTALL)
shop_regex = re.compile(r'<div class="shop-newsletter-section">.*?</div>', re.DOTALL)

for filename in os.listdir('.'):
    if filename.endswith('.html'):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = promo_regex.sub(new_newsletter_html, content)
        new_content = shop_regex.sub(new_newsletter_html, new_content)
        
        if new_content != content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
