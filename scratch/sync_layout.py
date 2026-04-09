import os
import re

# The new navigation menu from index.html (Source of Truth)
NEW_NAV = """            <nav class="nav-links" id="nav-menu">
                <div class="mobile-menu-header">
                    <button class="menu-close-btn" id="menu-close-btn" aria-label="Fermer le menu">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <line x1="18" y1="6" x2="6" y2="18"></line>
                            <line x1="6" y1="6" x2="18" y2="18"></line>
                        </svg>
                    </button>
                </div>
                <!-- Sorties -->
                <div class="nav-item has-megamenu">
                    <a href="promenade.html" class="nav-link">Promenade <svg width="10" height="6" viewBox="0 0 10 6"
                            fill="none">
                            <path d="M1 1L5 5L9 1" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"
                                stroke-linejoin="round" />
                        </svg></a>
                    <div class="megamenu">
                        <div class="container">
                            <div class="megamenu-visual-grid">
                                <!-- Colliers -->
                                <a href="colliers-classiques.html" class="megamenu-card">
                                    <div class="card-image"><img src="dog_collar_classic_1775487825692.png"
                                             alt="Colliers Classiques"></div>
                                    <span>Colliers Classiques</span>
                                </a>
                                <a href="colliers-personnalises.html" class="megamenu-card">
                                    <div class="card-image"><img src="dog_collar_classic_1775487825692.png"
                                             alt="Colliers Personnalisés"></div>
                                    <span>Colliers Personnalisés</span>
                                </a>
                                <a href="colliers-anti-fugue.html" class="megamenu-card">
                                    <div class="card-image"><img src="dog_collar_classic_1775487825692.png"
                                             alt="Colliers Anti-Fugue"></div>
                                    <span>Colliers Anti-Fugue</span>
                                </a>
                                <a href="colliers-etrangleurs.html" class="megamenu-card">
                                    <div class="card-image"><img src="dog_collar_classic_1775487825692.png"
                                             alt="Colliers Étrangleurs"></div>
                                    <span>Colliers Étrangleurs</span>
                                </a>
                                <a href="colliers-cuir.html" class="megamenu-card">
                                    <div class="card-image"><img src="dog_collar_classic_1775487825692.png"
                                             alt="Colliers Cuir"></div>
                                    <span>Colliers Cuir</span>
                                </a>

                                <!-- Harnais -->
                                <a href="harnais-personnalises.html" class="megamenu-card">
                                    <div class="card-image"><img src="dog_harness_premium_1775487844838.png"
                                             alt="Harnais Personnalisés"></div>
                                    <span>Harnais Personnalisés</span>
                                </a>
                                <a href="harnais-anti-traction.html" class="megamenu-card">
                                    <div class="card-image"><img src="dog_harness_premium_1775487844838.png"
                                             alt="Harnais Anti-Traction"></div>
                                    <span>Harnais Anti-Traction</span>
                                </a>
                                <a href="harnais-canicross.html" class="megamenu-card">
                                    <div class="card-image"><img src="dog_harness_premium_1775487844838.png"
                                             alt="Harnais Canicross"></div>
                                    <span>Harnais Canicross</span>
                                </a>

                                <!-- Laisses -->
                                <a href="longes.html" class="megamenu-card">
                                    <div class="card-image"><img src="dog_leash_elegant_1775487863541.png" alt="Longes">
                                    </div>
                                    <span>Longes</span>
                                </a>
                                <a href="laisses-classiques.html" class="megamenu-card">
                                    <div class="card-image"><img src="dog_leash_elegant_1775487863541.png"
                                             alt="Laisses Classiques"></div>
                                    <span>Laisses Classiques</span>
                                </a>
                                <a href="laisses-enrouleur.html" class="megamenu-card">
                                    <div class="card-image"><img src="dog_leash_elegant_1775487863541.png"
                                             alt="Laisses Enrouleur"></div>
                                    <span>Laisses Enrouleur</span>
                                </a>
                                <a href="medailles.html" class="megamenu-card">
                                    <div class="card-image"><img src="dog_id_tag_premium_1775537721480.png"
                                             alt="Médailles"></div>
                                    <span>Médailles</span>
                                </a>
                                <a href="museliere.html" class="megamenu-card">
                                    <div class="card-image"><img src="dog_muzzle_premium_1775537807415.png"
                                             alt="Muselière"></div>
                                    <span>Muselière</span>
                                </a>
                                <a href="sac-a-crottes.html" class="megamenu-card">
                                    <div class="card-image"><img src="dog_waste_bag_holder_premium_1775537881838.png"
                                             alt="Sac à Crottes"></div>
                                    <span>Sac à Crottes</span>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Couchage -->
                <div class="nav-item has-megamenu">
                    <a href="couchage.html" class="nav-link">Couchage <svg width="10" height="6" viewBox="0 0 10 6"
                            fill="none">
                            <path d="M1 1L5 5L9 1" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"
                                stroke-linejoin="round" />
                        </svg></a>
                    <div class="megamenu">
                        <div class="container">
                            <div class="megamenu-visual-grid">
                                <a href="panier-chien.html" class="megamenu-card">
                                    <div class="card-image"><img src="dog_bed_premium_1775489579429.png"
                                             alt="Panier pour Chien"></div>
                                    <span>Panier pour Chien</span>
                                </a>
                                <a href="#" class="megamenu-card">
                                    <div class="card-image"><img src="dog_bed_premium_1775489579429.png"
                                             alt="Canapé pour Chien"></div>
                                    <span>Canapé pour Chien</span>
                                </a>
                                <a href="#" class="megamenu-card">
                                    <div class="card-image"><img src="dog_bed_premium_1775489579429.png"
                                             alt="Panier Chien Voiture"></div>
                                    <span>Panier Chien Voiture</span>
                                </a>
                                <a href="#" class="megamenu-card">
                                    <div class="card-image"><img src="dog_blanket_premium_1775538439218.png"
                                             alt="Couverture pour Chien"></div>
                                    <span>Couverture pour Chien</span>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Jouets -->
                <div class="nav-item has-megamenu">
                    <a href="jouets.html" class="nav-link">Jouets <svg width="10" height="6" viewBox="0 0 10 6"
                            fill="none">
                            <path d="M1 1L5 5L9 1" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"
                                stroke-linejoin="round" />
                        </svg></a>
                    <div class="megamenu">
                        <div class="container">
                            <div class="megamenu-visual-grid">
                                <a href="#" class="megamenu-card">
                                    <div class="card-image"><img src="dog_toys_premium_1775489913031.png"
                                             alt="Tapis de Fouille"></div>
                                    <span>Tapis de Fouille</span>
                                </a>
                                <a href="#" class="megamenu-card">
                                    <div class="card-image"><img src="dog_toys_premium_1775489913031.png" alt="Balles">
                                    </div>
                                    <span>Balles</span>
                                </a>
                                <a href="#" class="megamenu-card">
                                    <div class="card-image"><img src="dog_toys_premium_1775489913031.png"
                                             alt="Peluches"></div>
                                    <span>Peluches</span>
                                </a>
                                <a href="#" class="megamenu-card">
                                    <div class="card-image"><img src="dog_toys_premium_1775489913031.png"
                                             alt="Jeux d'Occupation Chien"></div>
                                    <span>Jeux d'Occupation Chien</span>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Hygiène et Soins -->
                <div class="nav-item has-megamenu">
                    <a href="index.html#hygiene" class="nav-link">Hygiène & Soins <svg width="10" height="6"
                            viewBox="0 0 10 6" fill="none">
                            <path d="M1 1L5 5L9 1" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"
                                stroke-linejoin="round" />
                        </svg></a>
                    <div class="megamenu">
                        <div class="container">
                            <div class="megamenu-visual-grid">
                                <a href="#" class="megamenu-card">
                                    <div class="card-image"><img src="dog_hygiene_premium_set_1775490826943.png"
                                             alt="Gamelle Anti-Glouton"></div>
                                    <span>Gamelle Anti-Glouton</span>
                                </a>
                                <a href="#" class="megamenu-card">
                                    <div class="card-image"><img src="dog_hygiene_premium_set_1775490826943.png"
                                             alt="Gamelles"></div>
                                    <span>Gamelles</span>
                                </a>
                                <a href="#" class="megamenu-card">
                                    <div class="card-image"><img src="dog_hygiene_premium_set_1775490826943.png"
                                             alt="Tapis de Léchage"></div>
                                    <span>Tapis de Léchage</span>
                                </a>
                                <a href="#" class="megamenu-card">
                                    <div class="card-image"><img src="dog_hygiene_premium_set_1775490826943.png"
                                             alt="Brosses"></div>
                                    <span>Brosses</span>
                                </a>
                                <a href="#" class="megamenu-card">
                                    <div class="card-image"><img src="dog_hygiene_premium_set_1775490826943.png"
                                             alt="Boîte à Croquettes"></div>
                                    <span>Boîte à Croquettes</span>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="nav-item has-megamenu">
                    <a href="index.html#accessoires" class="nav-link">Accessoires <svg width="10" height="6"
                            viewBox="0 0 10 6" fill="none">
                            <path d="M1 1L5 5L9 1" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"
                                stroke-linejoin="round" />
                        </svg></a>
                    <div class="megamenu">
                        <div class="container">
                            <div class="megamenu-visual-grid">
                                <a href="produit-impermeable.html" class="megamenu-card">
                                    <div class="card-image"><img src="pawluxe_hero_lifestyle_1775474451027.png"
                                             alt="Imperméable"></div>
                                    <span>Imperméable</span>
                                </a>
                                <a href="#" class="megamenu-card">
                                    <div class="card-image"><img src="pawluxe_hero_lifestyle_1775474451027.png"
                                             alt="Manteaux"></div>
                                    <span>Manteaux</span>
                                </a>
                                <a href="#" class="megamenu-card">
                                    <div class="card-image"><img src="pawluxe_hero_lifestyle_1775474451027.png"
                                             alt="Pull et sweat"></div>
                                    <span>Pull et sweat</span>
                                </a>
                                <a href="#" class="megamenu-card">
                                    <div class="card-image"><img src="pawluxe_hero_lifestyle_1775474451027.png"
                                             alt="T-shirt et Polo"></div>
                                    <span>T-shirt et Polo</span>
                                </a>
                                <a href="#" class="megamenu-card">
                                    <div class="card-image"><img src="pawluxe_hero_lifestyle_1775474451027.png"
                                             alt="Bottine"></div>
                                    <span>Bottine</span>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </nav>"""

# The new footer from index.html (Source of Truth)
NEW_FOOTER = """    <footer class="footer">
        <button id="back-to-top" class="back-to-top" aria-label="Retour en haut">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"
                stroke-linecap="round" stroke-linejoin="round">
                <polyline points="18 15 12 9 6 15"></polyline>
            </svg>
        </button>
        <div class="container footer-grid">
            <!-- Brand Info Column -->
            <div class="footer-col brand-col">
                <a href="index.html" class="footer-logo">Chetoutou</a>
                <div class="brand-desc">
                    <p>Chetoutou, c'est le rendez-vous des passionnés de leurs compagnons à quatre pattes : un vaste
                        catalogue de modèles intemporels, élégants et reconnus, sélectionnés avec soin.</p>
                </div>
                <div class="brand-contact">
                    <p>contact@cheztoutou.com</p>
                    <p>0783066021</p>
                </div>
            </div>

            <!-- Main Menu Column -->
            <div class="footer-col">
                <h4>Menu principal</h4>
                <ul class="footer-links">
                    <li><a href="#about">À propos</a></li>
                    <li><a href="blog.html">Blog</a></li>
                    <li><a href="#promenade">Promenade</a></li>
                    <li><a href="couchage.html">Couchage</a></li>
                    <li><a href="jouets.html">Jouets</a></li>
                    <li><a href="#">Accessoires</a></li>
                </ul>
            </div>

            <!-- Information Column -->
            <div class="footer-col">
                <h4>Informations</h4>
                <ul class="footer-links">
                    <li><a href="guide-tailles.html">Guide de tailles</a></li>
                    <li><a href="politique-confidentialite.html">Politique de confidentialité</a></li>
                    <li><a href="politique-remboursement.html">Politique de remboursement</a></li>
                    <li><a href="conditions-utilisation.html">Conditions d'utilisation</a></li>
                    <li><a href="coordonnees.html">Coordonnées</a></li>
                    <li><a href="politique-expedition.html">Politique d'expédition</a></li>
                    <li><a href="preferences-cookies.html">Préférences en matière de cookies</a></li>
                </ul>
            </div>

            <!-- Newsletter Column -->
            <div class="footer-col">
                <h4>Cercle Privé</h4>
                <p class="footer-newsletter-text">Rejoignez-nous et bénéficiez de -10% sur votre première commande.</p>
                <div class="footer-newsletter">
                    <form class="footer-newsletter-form">
                        <div class="input-group">
                            <input type="email" placeholder="Adresse email" aria-label="Votre adresse email">
                            <button type="submit" class="submit-btn">
                                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                                    stroke-width="2">
                                    <path d="M5 12h14M12 5l7 7-7 7" />
                                </svg>
                            </button>
                        </div>
                    </form>
                </div>
                <div class="footer-socials">
                    <a href="#" class="social-link" aria-label="Facebook">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg>
                    </a>
                    <a href="#" class="social-link" aria-label="Instagram">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
                    </a>
                    <a href="#" class="social-link" aria-label="Twitter">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 4s-.7 2.1-2 3.4c1.6 10-9.4 17.3-18 11.6 2.2.1 4.4-.6 6-2C3 15.5.5 9.6 3 5c2.2 2.6 5.6 4.1 9 4-.9-4.2 4-6.6 7-3.8 1.1 0 3-1.2 3-1.2z"></path></svg>
                    </a>
                    <a href="#" class="social-link" aria-label="Pinterest">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><path d="M8 20l4-9"></path><path d="M10.7 14c.4.1 1.2.1 1.5-.2.6-.5.4-1.7-.1-2.2-.7-.8-2-.3-2.1.8-.1.7.3 1.2.7 1.6z"></path><path d="M12 11c1-1 2.5-.5 3 1s-.5 4-2 4.5c-1.2.3-2.5-.2-3-1.5"></path></svg>
                    </a>
                    <a href="#" class="social-link" aria-label="TikTok">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M9 12a4 4 0 1 0 4 4V4a5 5 0 0 0 5 5"></path>
                        </svg>
                    </a>
                </div>
            </div>
        </div>

        <!-- Bottom Bar: Payments & Copyright -->
        <div class="footer-bottom">
            <div class="container bottom-flex">
                <div class="payment-icons">
                    <img src="https://img.icons8.com/color/48/visa.png" alt="Visa" class="pm-card">
                    <img src="https://img.icons8.com/color/48/mastercard.png" alt="Mastercard" class="pm-card">
                    <img src="https://img.icons8.com/color/48/maestro.png" alt="Maestro" class="pm-card">
                    <img src="https://img.icons8.com/color/48/apple-pay.png" alt="Apple Pay" class="pm-card pm-apple">
                    <img src="https://img.icons8.com/color/48/google-pay.png" alt="Google Pay" class="pm-card">
                    <img src="https://img.icons8.com/color/48/paypal.png" alt="PayPal" class="pm-card">
                </div>
                <div class="copyright">
                    <p>&copy; 2026 Chetoutou</p>
                </div>

            </div>
        </div>
        <div id="search-overlay" class="search-overlay">
            <button id="close-search" class="close-search" aria-label="Fermer la recherche">
                <svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                    <line x1="18" y1="6" x2="6" y2="18"></line>
                    <line x1="6" y1="6" x2="18" y2="18"></line>
                </svg>
            </button>
            <div class="search-container">
                <div class="search-bar-glass">
                    <div class="search-icon-inside">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <circle cx="11" cy="11" r="8" />
                            <path d="m21 21-4.3-4.3" />
                        </svg>
                    </div>
                    <input type="text" id="search-input" placeholder="Recherche..." autocomplete="off">
                </div>
            </div>
        </div>
        <div id="cart-drawer" class="cart-drawer">
            <div class="cart-header">
                <h3>Vérifiez votre panier</h3>
                <button id="close-cart" class="close-cart-btn" aria-label="Fermer le panier">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <line x1="18" y1="6" x2="6" y2="18"></line>
                        <line x1="6" y1="6" x2="18" y2="18"></line>
                    </svg>
                </button>
            </div>
            <div class="cart-body">
                <div class="cart-empty-state">
                    <div class="empty-icon">
                        <svg width="60" height="60" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                            <path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z"></path>
                            <path d="M3 6h18"></path>
                            <path d="M16 10a4 4 0 0 1-8 0"></path>
                        </svg>
                    </div>
                    <h4>Votre panier est vide</h4>
                    <p>Remplissez votre panier avec des articles incroyables</p>
                    <a href="index.html#collections" class="btn-black btn-full">Acheter maintenant</a>
                </div>
                <div class="cart-items-container" style="display: none;"></div>
            </div>
        </div>
        <div id="cart-overlay" class="cart-overlay"></div>
    </footer>"""

def update_file(filepath):
    if not filepath.endswith('.html') or filepath == 'index.html':
        return
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update Navigation Menu
    nav_pattern = re.compile(r'<nav[^>]*id="nav-menu"[^>]*>.*?</nav>', re.DOTALL)
    if nav_pattern.search(content):
        content = nav_pattern.sub(NEW_NAV, content)
    else:
        print(f"Nav menu not found in {filepath}")
        
    # 2. Update Footer
    footer_pattern = re.compile(r'<footer[^>]*class="footer"[^>]*>.*?</footer>', re.DOTALL)
    if footer_pattern.search(content):
        content = footer_pattern.sub(NEW_FOOTER, content)
    else:
        print(f"Footer not found in {filepath}")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

if __name__ == "__main__":
    files = [f for f in os.listdir('.') if f.endswith('.html')]
    for f in files:
        update_file(f)
