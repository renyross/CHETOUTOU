import os
import re

# The new footer from index.html (Source of Truth)
NEW_FOOTER = """    <footer class="footer">
        <button aria-label="Retour en haut" class="back-to-top" id="back-to-top">
            <svg fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"
                stroke-width="3" viewbox="0 0 24 24" width="24">
                <polyline points="18 15 12 9 6 15">
                </polyline>
            </svg>
        </button>
        <div class="container footer-grid">
            <!-- Brand Info Column -->
            <div class="footer-col brand-col">
                <a class="footer-logo" href="index.html">
                    Chetoutou
                </a>
                <div class="brand-desc">
                    <p>
                        Chetoutou, c'est le rendez-vous des passionnés de leurs compagnons à quatre pattes : un vaste
                        catalogue de modèles intemporels, élégants et reconnus, sélectionnés avec soin.
                    </p>
                </div>
                <div class="brand-contact">
                    <p>
                        contact@cheztoutou.com
                    </p>
                    <p>
                        0783066021
                    </p>
                </div>
            </div>
            <!-- Main Menu Column -->
            <div class="footer-col">
                <h4>
                    Service clients
                </h4>
                <ul class="footer-links">
                    <li>
                        <a href="a-propos.html">
                            À propos
                        </a>
                    </li>
                    <li>
                        <a href="blog.html">
                            Blog
                        </a>
                    </li>

                    <li>
                        <a href="faq.html">
                            FAQ / Centre d'aide
                        </a>
                    </li>
                    <li>
                        <a href="suivre-commande.html">
                            Suivre ma commande
                        </a>
                    </li>
                    <li>
                        <a href="guide-tailles.html">
                            Guide de tailles
                        </a>
                    </li>
                    <li>
                        <a href="coordonnees.html">
                            Coordonnées
                        </a>
                    </li>
                </ul>
            </div>
            <!-- Information Column -->
            <div class="footer-col">
                <h4>
                    Informations
                </h4>
                <ul class="footer-links">
                    <li>
                        <a href="politique-confidentialite.html">
                            Politique de confidentialité
                        </a>
                    </li>
                    <li>
                        <a href="politique-remboursement.html">
                            Politique de remboursement
                        </a>
                    </li>
                    <li>
                        <a href="conditions-utilisation.html">
                            Conditions d'utilisation
                        </a>
                    </li>
                    <li>
                        <a href="politique-expedition.html">
                            Politique d'expédition
                        </a>
                    </li>
                    <li>
                        <a href="preferences-cookies.html">
                            Préférences en matière de cookies
                        </a>
                    </li>
                </ul>
            </div>
            <!-- Newsletter Column -->
            <div class="footer-col">
                <h4>
                    Cercle Privé
                </h4>
                <p class="footer-newsletter-text">
                    Rejoignez-nous et bénéficiez de -10% sur votre première commande.
                </p>
                <div class="footer-newsletter">
                    <form class="footer-newsletter-form">
                        <div class="input-group">
                            <input aria-label="Votre adresse email" placeholder="Adresse email" type="email" />
                            <button class="submit-btn" type="submit">
                                <svg fill="none" height="20" stroke="currentColor" stroke-width="2" viewbox="0 0 24 24"
                                    width="20">
                                    <path d="M5 12h14M12 5l7 7-7 7">
                                    </path>
                                </svg>
                            </button>
                        </div>
                    </form>
                </div>
                <div class="footer-socials-container">
                    <h4>
                        Nous suivre
                    </h4>
                    <div class="footer-socials">
                        <a aria-label="Facebook" class="social-link" href="#">
                            <svg viewbox="0 0 24 24">
                                <path
                                    d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z">
                                </path>
                            </svg>
                        </a>
                        <a aria-label="Instagram" class="social-link" href="#">
                            <svg viewbox="0 0 24 24">
                                <path
                                    d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4.162 4.162 0 110-8.324 4.162 4.162 0 010 8.324zM18.406 4.331a1.44 1.44 0 100 2.88 1.44 1.44 0 000-2.88z">
                                </path>
                            </svg>
                        </a>
                        <a aria-label="X" class="social-link" href="#">
                            <svg viewbox="0 0 24 24">
                                <path
                                    d="M18.901 1.153h3.68l-8.04 9.19L24 22.846h-7.406l-5.8-7.584-6.638 7.584H.474l8.6-9.83L0 1.154h7.594l5.243 6.932ZM17.61 20.644h2.039L6.486 3.24H4.298Z">
                                </path>
                            </svg>
                        </a>
                        <a aria-label="YouTube" class="social-link" href="#">
                            <svg viewbox="0 0 24 24">
                                <path
                                    d="M23.498 6.186a3.016 3.016 0 00-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505a3.017 3.017 0 00-2.122 2.136C0 8.055 0 12 0 12s0 3.945.501 5.814a3.017 3.017 0 002.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 002.122-2.136C24 15.945 24 12 24 12s0-3.945-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z">
                                </path>
                            </svg>
                        </a>
                        <a aria-label="Pinterest" class="social-link" href="#">
                            <svg viewbox="0 0 24 24">
                                <path
                                    d="M12.017 0C5.396 0 .029 5.367.029 11.987c0 5.079 3.158 9.417 7.618 11.162-.105-.949-.199-2.403.041-3.439.219-.937 1.406-5.965 1.406-5.965s-.359-.719-.359-1.782c0-1.668.967-2.914 2.171-2.914 1.023 0 1.518.769 1.518 1.69 0 1.029-.655 2.568-.994 3.995-.283 1.194.599 2.169 1.777 2.169 2.133 0 3.772-2.249 3.772-5.495 0-2.873-2.064-4.882-5.012-4.882-3.414 0-5.418 2.561-5.418 5.207 0 1.031.397 2.138.893 2.738.098.119.112.224.083.345l-.333 1.36c-.053.22-.174.267-.402.161-1.499-.698-2.436-2.889-2.436-4.649 0-3.785 2.75-7.259 7.929-7.259 4.164 0 7.398 2.967 7.398 6.93 0 4.136-2.607 7.464-6.227 7.464-1.216 0-2.359-.631-2.75-1.378l-.748 2.853c-.271 1.043-1.002 2.35-1.492 3.146 1.124.347 2.317.535 3.554.535 6.607 0 11.985-5.365 11.985-11.987C24.02 5.367 18.633 0 12.017 0z">
                                </path>
                            </svg>
                        </a>
                        <a aria-label="TikTok" class="social-link" href="#">
                            <svg viewbox="0 0 24 24">
                                <path
                                    d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-5.2 1.74 2.89 2.89 0 0 1 2.31-4.64 2.93 2.93 0 0 1 .88.13V9.4a6.84 6.84 0 0 0-1-.05A6.33 6.33 0 0 0 5 20.1a6.34 6.34 0 0 0 10.86-4.43v-7a8.16 8.16 0 0 0 4.77 1.52v-3.4a4.85 4.85 0 0 1-1.04-.1z">
                                </path>
                            </svg>
                        </a>
                    </div>
                </div>
            </div>
        </div>
        <!-- Bottom Bar: Payments & Copyright -->
        <div class="footer-bottom">
            <div class="container bottom-flex">
                <div class="payment-icons">
                    <img alt="Visa" class="pm-card" src="https://img.icons8.com/color/48/visa.png" />
                    <img alt="Mastercard" class="pm-card" src="https://img.icons8.com/color/48/mastercard.png" />
                    <img alt="Maestro" class="pm-card" src="https://img.icons8.com/color/48/maestro.png" />
                    <img alt="Apple Pay" class="pm-card pm-apple" src="https://img.icons8.com/color/48/apple-pay.png" />
                    <img alt="Google Pay" class="pm-card" src="https://img.icons8.com/color/48/google-pay.png" />
                    <img alt="PayPal" class="pm-card" src="https://img.icons8.com/color/48/paypal.png" />
                </div>
                <div class="copyright">
                    <p>
                        © 2026 Chetoutou
                    </p>
                </div>
            </div>
        </div>
        <div class="search-overlay" id="search-overlay">
            <button aria-label="Fermer la recherche" class="close-search" id="close-search">
                <svg fill="none" height="30" stroke="currentColor" stroke-width="1.5" viewbox="0 0 24 24" width="30">
                    <line x1="18" x2="6" y1="6" y2="18">
                    </line>
                    <line x1="6" x2="18" y1="6" y2="18">
                    </line>
                </svg>
            </button>
            <div class="search-container">
                <div class="search-bar-glass">
                    <div class="search-icon-inside">
                        <svg fill="none" height="24" stroke="currentColor" stroke-width="2" viewbox="0 0 24 24"
                            width="24">
                            <circle cx="11" cy="11" r="8">
                            </circle>
                            <path d="m21 21-4.3-4.3">
                            </path>
                        </svg>
                    </div>
                    <input autocomplete="off" id="search-input" placeholder="Recherche..." type="text" />
                </div>
            </div>
        </div>
        <div class="cart-drawer" id="cart-drawer">
            <div class="cart-header">
                <h3>
                    Panier
                </h3>
                <button aria-label="Fermer le panier" class="close-cart-btn" id="close-cart">
                    <svg fill="none" height="24" stroke="currentColor" stroke-width="1.5" viewbox="0 0 24 24"
                        width="24">
                        <line x1="18" x2="6" y1="6" y2="18">
                        </line>
                        <line x1="6" x2="18" y1="6" y2="18">
                        </line>
                    </svg>
                </button>
            </div>
            <div class="cart-body">
                <!-- Items list (Dynamic) -->
                <div class="cart-items-container">
                    <!-- JS will inject items here -->
                </div>
                <!-- Empty state -->
                <div class="cart-empty-state" style="padding-top: 20px;">
                    <div class="empty-icon">
                        <svg fill="none" height="60" stroke="currentColor" stroke-width="1" viewbox="0 0 24 24"
                            width="60">
                            <path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z">
                            </path>
                            <path d="M3 6h18">
                            </path>
                            <path d="M16 10a4 4 0 0 1-8 0">
                            </path>
                        </svg>
                    </div>
                    <h4>
                        Votre panier est vide
                    </h4>
                    <p>
                        Découvrez nos collections pour gâter votre compagnon.
                    </p>
                </div>
                <!-- Promo Code -->
                <div class="cart-promo-v3">
                    <input placeholder="Code de réduction" type="text" />
                    <button class="btn-promo-apply">
                        Appliquer
                    </button>
                </div>
            </div>
            <!-- Footer Section -->
            <div class="cart-footer-v3">
                <div class="cart-total-row">
                    <span class="total-label">
                        Total estimé
                    </span>
                    <span id="cart-total-amount">
                        0,00 €
                    </span>
                </div>
                <a class="btn-checkout-v3" href="checkout.html"
                    style="text-decoration: none; display: block; text-align: center; line-height: 1;">
                    Commander
                </a>
                <div class="cart-trust-badges">
                    <img alt="Visa" src="https://img.icons8.com/color/48/visa.png" />
                    <img alt="Mastercard" src="https://img.icons8.com/color/48/mastercard.png" />
                    <img alt="Maestro" src="https://img.icons8.com/color/48/maestro.png" />
                    <img alt="Apple Pay" src="https://img.icons8.com/color/48/apple-pay.png" />
                    <img alt="Google Pay" src="https://img.icons8.com/color/48/google-pay.png" />
                    <img alt="PayPal" src="https://img.icons8.com/color/48/paypal.png" />
                </div>
            </div>
        </div>
        <div class="cart-overlay" id="cart-overlay">
        </div>
    </footer>"""

def update_file(filepath):
    if not filepath.endswith('.html') or filepath == 'index.html':
        return
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update Footer
    footer_pattern = re.compile(r'<footer[^>]*class="footer"[^>]*>.*?</footer>', re.DOTALL)
    if footer_pattern.search(content):
        content = footer_pattern.sub(NEW_FOOTER, content)
        print(f"Updated footer in {filepath}")
    else:
        print(f"Footer not found in {filepath}")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    for root, dirs, files in os.walk('.'):
        for f in files:
            if f.endswith('.html'):
                update_file(os.path.join(root, f))
