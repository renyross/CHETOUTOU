import os
import re

new_newsletter_html = """        <!-- Unified Newsletter Section (Premium Minimal) -->
        <section class="unified-newsletter">
            <div class="container">
                <div class="newsletter-inner">
                    <div class="newsletter-header">
                        <h2>Rejoignez-nous</h2>
                        <p>et bénéficiez de -10% sur votre première commande.</p>
                    </div>
                    <form class="newsletter-form-minimal">
                        <div class="input-group-underline">
                            <input type="email" placeholder="Entrez votre adresse e-mail" required>
                        </div>
                        <div class="checkbox-group-minimal">
                            <input type="checkbox" id="newsletter-consent" required>
                            <label for="newsletter-consent">J’ai plus de 16 ans et j’ai lu et j’accepte la <a href="conditions-utilisation.html">Termes et conditions générales</a> et <a href="politique-confidentialite.html">Politique de confidentialité</a></label>
                        </div>
                        <button type="submit" class="btn-newsletter-black">Inscrivez-vous</button>
                    </form>
                    <p class="newsletter-legal-text">
                        Ce site est protégé par reCAPTCHA et les <a href="politique-confidentialite.html">Politique de confidentialité</a> et <a href="conditions-utilisation.html">Conditions de service</a> s'appliquent.
                    </p>
                </div>
            </div>
        </section>"""

# Target the unified-newsletter section
news_regex = re.compile(r'<!-- Unified Newsletter Section.*?<section class="unified-newsletter">.*?</section>', re.DOTALL)

for filename in os.listdir('.'):
    if filename.endswith('.html'):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = news_regex.sub(new_newsletter_html, content)
        
        if new_content != content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
