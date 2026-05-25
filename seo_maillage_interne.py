#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de maillage interne SEO — Chetoutou
Injecte des blocs de liens contextuels dans les pages catégories,
les pages produit et les articles de blog.
"""

import re
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ─────────────────────────────────────────────────────────────────────────────
# CSS du bloc maillage interne (injecté une seule fois si absent)
# ─────────────────────────────────────────────────────────────────────────────
INTERNAL_LINKS_CSS = """
/* ===== SEO Internal Links Block ===== */
.internal-links-seo {
    background: #f7f7f7;
    padding: 3.5rem 0;
    border-top: 1px solid #eee;
}
.internal-links-seo .ils-inner {
    max-width: 1500px;
    margin: 0 auto;
    padding: 0 10rem;
}
.internal-links-seo h3 {
    font-size: 1rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #888;
    margin-bottom: 1.5rem;
}
.ils-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 0.75rem;
}
.ils-link {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    padding: 0.55rem 1.1rem;
    background: #fff;
    border: 1px solid #ddd;
    border-radius: 999px;
    font-size: 0.85rem;
    font-weight: 500;
    color: #111;
    text-decoration: none;
    transition: border-color 0.2s, background 0.2s, color 0.2s;
    white-space: nowrap;
}
.ils-link:hover {
    border-color: #e69c1a;
    background: #e69c1a;
    color: #fff;
}
.ils-link svg {
    flex-shrink: 0;
}
@media (max-width: 768px) {
    .internal-links-seo .ils-inner { padding: 0 1.5rem; }
}
"""

ARROW_SVG = '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>'

def make_ils_block(title, links):
    """Generate an internal links section HTML block."""
    items = "\n".join(
        f'            <a href="{href}" class="ils-link">{ARROW_SVG} {label}</a>'
        for href, label in links
    )
    return f"""
        <!-- SEO Internal Linking Block -->
        <section class="internal-links-seo">
            <div class="ils-inner">
                <h3>{title}</h3>
                <div class="ils-grid">
{items}
                </div>
            </div>
        </section>"""

def inject_css_if_needed(content):
    """Inject ILS CSS into <style> block inside <head> if not already present."""
    if 'internal-links-seo' in content:
        return content  # already injected
    # inject before </head>
    return content.replace('</head>', f'<style>{INTERNAL_LINKS_CSS}</style>\n</head>', 1)

def inject_before_footer(content, block):
    """Insert block right before the <footer> tag."""
    if 'class="internal-links-seo"' in content:
        # Replace existing block
        content = re.sub(
            r'\s*<!-- SEO Internal Linking Block -->.*?</section>',
            block,
            content,
            flags=re.DOTALL
        )
        return content
    # Insert before footer
    return re.sub(r'(\s*<footer\b)', block + r'\n\1', content, count=1)

def inject_in_article(content, insertions):
    """
    For blog articles: inject contextual links directly into existing paragraphs.
    insertions = list of (search_phrase, link_html) tuples.
    The search_phrase is replaced by link_html only once.
    """
    for phrase, link_html in insertions:
        if phrase in content and link_html not in content:
            content = content.replace(phrase, link_html, 1)
    return content

def process_file(filename, block, article_insertions=None):
    filepath = os.path.join(BASE_DIR, filename)
    if not os.path.exists(filepath):
        print(f"  ⚠️  SKIP (fichier manquant): {filename}")
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    content = inject_css_if_needed(content)
    content = inject_before_footer(content, block)
    if article_insertions:
        content = inject_in_article(content, article_insertions)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✅  MODIFIÉ : {filename}")
    else:
        print(f"  ℹ️  INCHANGÉ (déjà à jour): {filename}")


# ─────────────────────────────────────────────────────────────────────────────
# CORRECTIONS LIENS MORTS DANS LE MÉGAMENU
# ─────────────────────────────────────────────────────────────────────────────
DEAD_LINKS = {
    # (page_inexistante → redirection vers page existante)
    'href="collier-lumineux-chien.html"': 'href="collier-chien.html"',
    'href="collier-gps-chien.html"': 'href="collier-chien.html"',
    'href="collier-anti-fugue-chien.html"': 'href="collier-chien.html"',
    'href="collier-dressage-chien.html"': 'href="collier-chien.html"',
    'href="collier-electrique-chien.html"': 'href="collier-chien.html"',
    'href="collier-anti-aboiement-chien.html"': 'href="collier-chien.html"',
    'href="collier-anti-puce-chien.html"': 'href="collier-chien.html"',
    'href="collier-etrangleur-chien.html"': 'href="collier-chien.html"',
    'href="harnais-petit-chien.html"': 'href="harnais-chien.html"',
    'href="harnais-chien-voiture.html"': 'href="harnais-chien.html"',
    'href="harnais-chien-course.html"': 'href="harnais-chien.html"',
    'href="harnais-traction-chien.html"': 'href="harnais-chien.html"',
    'href="harnais-chien-y.html"': 'href="harnais-chien.html"',
    'href="laisse-enrouleur-chien.html"': 'href="laisse-chien.html"',
    'href="laisse-main-libre-chien.html"': 'href="laisse-chien.html"',
    'href="laisse-corde-chien.html"': 'href="laisse-chien.html"',
    'href="laisse-lasso-chien.html"': 'href="laisse-chien.html"',
    'href="laisse-longe-chien.html"': 'href="laisse-chien.html"',
    'href="laisse-chien-velo.html"': 'href="laisse-chien.html"',
    'href="laisse-chien-course.html"': 'href="laisse-chien.html"',
    'href="longue-laisse-chien.html"': 'href="laisse-chien.html"',
    'href="sac-a-dos-chien.html"': 'href="sac-chien.html"',
    'href="panier-voiture-chien.html"': 'href="sac-transport-chien.html"',
    'href="panier-velo-chien.html"': 'href="sac-chien.html"',
    'href="museliere.html"': 'href="promenade.html"',
    'href="accessoires.html"': 'href="promenade.html"',
    'href="panier-dehoussable-chien.html"': 'href="panier-chien.html"',
    'href="panier-plastique-chien.html"': 'href="panier-chien.html"',
    'href="panier-osier-chien.html"': 'href="panier-chien.html"',
    'href="panier-petit-chien.html"': 'href="panier-chien.html"',
    'href="panier-grand-chien.html"': 'href="panier-chien.html"',
    'href="panier-xxl-chien.html"': 'href="panier-chien.html"',
    'href="tapis-xxl-chien.html"': 'href="tapis-rafraichissant-chien.html"',
    'href="tapis-absorbant-chien.html"': 'href="tapis-rafraichissant-chien.html"',
    'href="jouet-interactif-chien.html"': 'href="jeux-occupation.html"',
    'href="tapis-fouille.html"': 'href="jeux-occupation.html"',
    'href="jouets-indestructibles.html"': 'href="jouets.html"',
    'href="peluches-chien.html"': 'href="jouets.html"',
    'href="doudou-chien.html"': 'href="jouets.html"',
    'href="balles-chien.html"': 'href="jouets.html"',
    'href="frisbee-chien.html"': 'href="jouets.html"',
    'href="lanceur-balle-chien.html"': 'href="jouets.html"',
    'href="gamelle-anti-glouton.html"': 'href="hygiene.html"',
    'href="gamelle-surelevee-chien.html"': 'href="hygiene.html"',
    'href="gamelle-ceramique-chien.html"': 'href="hygiene.html"',
    'href="gamelle-personnalisee-chien.html"': 'href="hygiene.html"',
    'href="tapis-gamelle-chien.html"': 'href="hygiene.html"',
    'href="tapis-lechage.html"': 'href="hygiene.html"',
    'href="boite-croquettes.html"': 'href="hygiene.html"',
    'href="brosses.html"': 'href="hygiene.html"',
    'href="sac-a-crottes.html"': 'href="hygiene.html"',
    'href="impermeables.html"': 'href="produit-impermeable.html"',
    'href="manteaux.html"': 'href="pull-sweat.html"',
    'href="bottine-chien.html"': 'href="promenade.html"',
    'href="hygiene.html"': 'href="guide-tailles.html"',
    'href="couchage.html"': 'href="panier-chien.html"',
}

def fix_dead_links_in_file(filename):
    """Fix all dead links in nav/footer of a given file."""
    filepath = os.path.join(BASE_DIR, filename)
    if not os.path.exists(filepath):
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    # Only fix links to pages that actually don't exist
    existing_pages = set(os.listdir(BASE_DIR))
    for dead, fixed in DEAD_LINKS.items():
        # Extract target page from dead link
        m = re.search(r'href="([^"]+\.html)"', dead)
        if m:
            target = m.group(1)
            if target not in existing_pages:
                content = content.replace(dead, fixed)
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✅  Liens morts corrigés : {filename}")

# ─────────────────────────────────────────────────────────────────────────────
# DÉFINITION DES BLOCS DE MAILLAGE INTERNE
# ─────────────────────────────────────────────────────────────────────────────

PAGES_CONFIG = {

    # ── SILO 1 : PROMENADE ──────────────────────────────────────────────────

    "collier-chien.html": make_ils_block("Explorer nos collections de promenade", [
        ("collier-cuir-chien.html", "Collier en cuir pour chien"),
        ("collier-personnalise-chien.html", "Collier personnalisé"),
        ("harnais-chien.html", "Harnais pour chien"),
        ("harnais-anti-traction-chien.html", "Harnais anti-traction"),
        ("laisse-chien.html", "Laisse pour chien"),
        ("laisse-cuir-chien.html", "Laisse en cuir"),
        ("guide-tailles.html", "Guide des tailles"),
        ("promenade.html", "Tous les accessoires de promenade"),
    ]),

    "collier-cuir-chien.html": make_ils_block("Complétez votre équipement", [
        ("collier-chien.html", "Tous les colliers chien"),
        ("collier-cuir-heritage.html", "Collier Cuir Heritage — Notre bestseller"),
        ("collier-personnalise-chien.html", "Collier personnalisé"),
        ("laisse-cuir-chien.html", "Laisse en cuir assortie"),
        ("laisse-chien.html", "Toutes les laisses"),
        ("guide-tailles.html", "Guide des tailles"),
        ("promenade.html", "Collection Promenade"),
    ]),

    "collier-personnalise-chien.html": make_ils_block("À découvrir aussi", [
        ("collier-chien.html", "Tous les colliers chien"),
        ("collier-cuir-chien.html", "Collier en cuir"),
        ("harnais-personnalise-chien.html", "Harnais personnalisé"),
        ("laisse-chien.html", "Laisse pour chien"),
        ("guide-tailles.html", "Guide des tailles"),
        ("a-propos.html", "Notre engagement qualité"),
    ]),

    "harnais-chien.html": make_ils_block("Complétez l'équipement de promenade", [
        ("harnais-anti-traction-chien.html", "Harnais anti-traction"),
        ("harnais-cuir-chien.html", "Harnais en cuir"),
        ("harnais-gros-chien.html", "Harnais grand chien"),
        ("harnais-tactique-chien.html", "Harnais tactique"),
        ("harnais-personnalise-chien.html", "Harnais personnalisé"),
        ("collier-chien.html", "Collier pour chien"),
        ("laisse-chien.html", "Laisse pour chien"),
        ("guide-tailles.html", "Guide des tailles"),
        ("promenade.html", "Collection Promenade"),
    ]),

    "harnais-anti-traction-chien.html": make_ils_block("Dans la même collection", [
        ("harnais-chien.html", "Tous les harnais"),
        ("harnais-cuir-chien.html", "Harnais en cuir"),
        ("harnais-tactique-chien.html", "Harnais tactique"),
        ("laisse-chien.html", "Laisse pour chien"),
        ("collier-chien.html", "Collier pour chien"),
        ("guide-tailles.html", "Guide des tailles"),
    ]),

    "harnais-cuir-chien.html": make_ils_block("Voir aussi dans notre boutique", [
        ("harnais-chien.html", "Tous les harnais"),
        ("harnais-anti-traction-chien.html", "Harnais anti-traction"),
        ("collier-cuir-chien.html", "Collier en cuir"),
        ("laisse-cuir-chien.html", "Laisse en cuir"),
        ("guide-tailles.html", "Guide des tailles"),
    ]),

    "harnais-gros-chien.html": make_ils_block("Voir aussi dans notre boutique", [
        ("harnais-chien.html", "Tous les harnais"),
        ("harnais-anti-traction-chien.html", "Harnais anti-traction"),
        ("harnais-tactique-chien.html", "Harnais tactique"),
        ("collier-chien.html", "Collier chien"),
        ("guide-tailles.html", "Guide des tailles"),
    ]),

    "harnais-tactique-chien.html": make_ils_block("Dans la même collection", [
        ("harnais-chien.html", "Tous les harnais"),
        ("harnais-anti-traction-chien.html", "Harnais anti-traction"),
        ("harnais-gros-chien.html", "Harnais grand chien"),
        ("collier-chien.html", "Collier chien"),
        ("laisse-chien.html", "Laisse chien"),
    ]),

    "harnais-personnalise-chien.html": make_ils_block("À explorer", [
        ("harnais-chien.html", "Tous les harnais"),
        ("collier-personnalise-chien.html", "Collier personnalisé"),
        ("laisse-chien.html", "Laisse chien"),
        ("guide-tailles.html", "Guide des tailles"),
    ]),

    "harnais-anti-fugue-chien.html": make_ils_block("À explorer", [
        ("harnais-chien.html", "Tous les harnais"),
        ("harnais-anti-traction-chien.html", "Harnais anti-traction"),
        ("collier-chien.html", "Collier chien"),
        ("laisse-chien.html", "Laisse chien"),
    ]),

    "harnais-levage-chien.html": make_ils_block("À explorer", [
        ("harnais-chien.html", "Tous les harnais"),
        ("harnais-gros-chien.html", "Harnais grand chien"),
        ("harnais-anti-traction-chien.html", "Harnais anti-traction"),
        ("laisse-chien.html", "Laisse chien"),
    ]),

    "laisse-chien.html": make_ils_block("Complétez votre équipement", [
        ("laisse-cuir-chien.html", "Laisse en cuir"),
        ("laisses-classiques.html", "Laisses classiques"),
        ("double-laisse-chien.html", "Double laisse"),
        ("harnais-chien.html", "Harnais pour chien"),
        ("collier-chien.html", "Collier pour chien"),
        ("sac-transport-chien.html", "Sac de transport chien"),
        ("promenade.html", "Collection Promenade"),
    ]),

    "laisse-cuir-chien.html": make_ils_block("Dans la même collection", [
        ("laisse-chien.html", "Toutes les laisses"),
        ("laisses-classiques.html", "Laisses classiques"),
        ("collier-cuir-chien.html", "Collier en cuir"),
        ("collier-cuir-heritage.html", "Collier Cuir Heritage"),
        ("harnais-chien.html", "Harnais chien"),
    ]),

    "laisses-classiques.html": make_ils_block("À explorer", [
        ("laisse-chien.html", "Toutes les laisses"),
        ("laisse-cuir-chien.html", "Laisse en cuir"),
        ("double-laisse-chien.html", "Double laisse"),
        ("harnais-chien.html", "Harnais chien"),
        ("collier-chien.html", "Collier chien"),
    ]),

    "double-laisse-chien.html": make_ils_block("À explorer", [
        ("laisse-chien.html", "Toutes les laisses"),
        ("laisses-classiques.html", "Laisses classiques"),
        ("harnais-chien.html", "Harnais chien"),
        ("collier-chien.html", "Collier chien"),
    ]),

    # ── SILO 2 : COUCHAGE ───────────────────────────────────────────────────

    "panier-chien.html": make_ils_block("Explorer nos solutions de couchage", [
        ("panier-orthopedique-chien.html", "Panier orthopédique chien"),
        ("panier-velvet-detail.html", "Panier Velvet Orthopédique — Bestseller"),
        ("lit-chien.html", "Lit pour chien"),
        ("lit-xxl-chien.html", "Lit XXL chien"),
        ("canape-chien.html", "Canapé luxe pour chien"),
        ("coussin-chien.html", "Coussin pour chien"),
        ("couverture-chien.html", "Couverture pour chien"),
    ]),

    "panier-orthopedique-chien.html": make_ils_block("Dans la même collection", [
        ("panier-chien.html", "Tous les paniers chien"),
        ("panier-velvet-detail.html", "Panier Velvet Orthopédique"),
        ("lit-chien.html", "Lit pour chien"),
        ("coussin-chien.html", "Coussin pour chien"),
        ("coussin-anti-stress-chien.html", "Coussin anti-stress"),
    ]),

    "lit-chien.html": make_ils_block("À découvrir aussi", [
        ("lit-xxl-chien.html", "Lit XXL pour chien"),
        ("lit-sureleve-chien.html", "Lit surélevé pour chien"),
        ("canape-chien.html", "Canapé pour chien"),
        ("panier-chien.html", "Panier pour chien"),
        ("coussin-chien.html", "Coussin pour chien"),
        ("protection-canape-chien.html", "Protection canapé"),
        ("tapis-rafraichissant-chien.html", "Tapis rafraîchissant"),
    ]),

    "lit-xxl-chien.html": make_ils_block("Dans la même collection", [
        ("lit-chien.html", "Tous les lits chien"),
        ("lit-sureleve-chien.html", "Lit surélevé"),
        ("canape-chien.html", "Canapé luxe pour chien"),
        ("panier-chien.html", "Panier chien"),
        ("coussin-chien.html", "Coussin chien"),
    ]),

    "lit-sureleve-chien.html": make_ils_block("À explorer", [
        ("lit-chien.html", "Tous les lits chien"),
        ("lit-xxl-chien.html", "Lit XXL chien"),
        ("canape-chien.html", "Canapé luxe pour chien"),
        ("panier-chien.html", "Panier chien"),
        ("tapis-rafraichissant-chien.html", "Tapis rafraîchissant"),
    ]),

    "coussin-chien.html": make_ils_block("Voir aussi", [
        ("coussin-anti-stress-chien.html", "Coussin anti-stress chien"),
        ("couverture-chien.html", "Couverture pour chien"),
        ("panier-chien.html", "Panier pour chien"),
        ("lit-chien.html", "Lit pour chien"),
        ("protection-canape-chien.html", "Protection canapé"),
    ]),

    "coussin-anti-stress-chien.html": make_ils_block("Dans la même collection", [
        ("coussin-chien.html", "Tous les coussins chien"),
        ("panier-orthopedique-chien.html", "Panier orthopédique"),
        ("panier-velvet-detail.html", "Panier Velvet Orthopédique"),
        ("couverture-chien.html", "Couverture pour chien"),
        ("lit-chien.html", "Lit pour chien"),
    ]),

    "couverture-chien.html": make_ils_block("À découvrir", [
        ("coussin-chien.html", "Coussin pour chien"),
        ("panier-chien.html", "Panier pour chien"),
        ("lit-chien.html", "Lit pour chien"),
        ("protection-canape-chien.html", "Protection canapé"),
    ]),

    "canape-chien.html": make_ils_block("À explorer dans notre boutique", [
        ("lit-chien.html", "Lit pour chien"),
        ("lit-xxl-chien.html", "Lit XXL"),
        ("panier-chien.html", "Panier pour chien"),
        ("protection-canape-chien.html", "Protection canapé"),
        ("coussin-chien.html", "Coussin pour chien"),
    ]),

    "protection-canape-chien.html": make_ils_block("Dans la même collection", [
        ("canape-chien.html", "Canapé pour chien"),
        ("couverture-chien.html", "Couverture pour chien"),
        ("lit-chien.html", "Lit pour chien"),
        ("panier-chien.html", "Panier pour chien"),
        ("coussin-chien.html", "Coussin pour chien"),
    ]),

    "tapis-rafraichissant-chien.html": make_ils_block("Voir aussi", [
        ("lit-sureleve-chien.html", "Lit surélevé"),
        ("lit-chien.html", "Lit pour chien"),
        ("panier-chien.html", "Panier pour chien"),
        ("coussin-chien.html", "Coussin pour chien"),
    ]),

    # ── SILO 3 : JOUETS & ACCESSOIRES ───────────────────────────────────────

    "jouets.html": make_ils_block("Explorer nos accessoires", [
        ("jeux-occupation.html", "Jeux d'occupation et intelligence"),
        ("tapis-rafraichissant-chien.html", "Tapis rafraîchissant"),
        ("sac-chien.html", "Sac pour chien"),
        ("sac-transport-chien.html", "Sac de transport"),
        ("panier-chien.html", "Panier pour chien"),
        ("blog.html", "Nos conseils pour votre chien"),
    ]),

    "jeux-occupation.html": make_ils_block("À explorer", [
        ("jouets.html", "Tous les jouets"),
        ("panier-chien.html", "Panier pour chien"),
        ("lit-chien.html", "Lit pour chien"),
        ("blog.html", "Conseils et bien-être canin"),
    ]),

    "sac-chien.html": make_ils_block("Complétez l'équipement", [
        ("sac-transport-chien.html", "Sac de transport chien"),
        ("laisse-chien.html", "Laisse pour chien"),
        ("harnais-chien.html", "Harnais pour chien"),
        ("promenade.html", "Collection Promenade"),
    ]),

    "sac-transport-chien.html": make_ils_block("Voir aussi", [
        ("sac-chien.html", "Sac pour chien"),
        ("laisse-chien.html", "Laisse pour chien"),
        ("harnais-chien.html", "Harnais pour chien"),
        ("promenade.html", "Collection Promenade"),
    ]),

    # ── PAGES PRODUIT (liens vers catégories + produits complémentaires) ────

    "collier-cuir-heritage.html": make_ils_block("Voir aussi dans notre boutique", [
        ("collier-cuir-chien.html", "Tous les colliers en cuir"),
        ("collier-chien.html", "Tous les colliers chien"),
        ("laisse-cuir-chien.html", "Laisse en cuir assortie"),
        ("harnais-cuir-chien.html", "Harnais en cuir"),
        ("guide-tailles.html", "Guide des tailles"),
        ("promenade.html", "Collection Promenade"),
    ]),

    "panier-velvet-detail.html": make_ils_block("À découvrir aussi", [
        ("panier-orthopedique-chien.html", "Paniers orthopédiques"),
        ("panier-chien.html", "Tous les paniers chien"),
        ("coussin-anti-stress-chien.html", "Coussin anti-stress"),
        ("lit-chien.html", "Lit pour chien"),
        ("couverture-chien.html", "Couverture pour chien"),
    ]),

    "produit-detail.html": make_ils_block("Voir aussi dans notre boutique", [
        ("harnais-chien.html", "Tous les harnais chien"),
        ("harnais-anti-traction-chien.html", "Harnais anti-traction"),
        ("laisse-chien.html", "Laisse pour chien"),
        ("collier-chien.html", "Collier pour chien"),
        ("guide-tailles.html", "Guide des tailles"),
        ("promenade.html", "Collection Promenade"),
    ]),

    "produit-impermeable.html": make_ils_block("Voir aussi", [
        ("pull-sweat.html", "Pull & Sweat pour chien"),
        ("tshirt-polo.html", "T-shirt & Polo pour chien"),
        ("harnais-chien.html", "Harnais pour chien"),
        ("laisse-chien.html", "Laisse pour chien"),
    ]),

    "pull-sweat.html": make_ils_block("Dans la même collection", [
        ("produit-impermeable.html", "Imperméable chien"),
        ("tshirt-polo.html", "T-shirt & Polo pour chien"),
        ("harnais-chien.html", "Harnais pour chien"),
        ("laisse-chien.html", "Laisse pour chien"),
    ]),

    "tshirt-polo.html": make_ils_block("À explorer", [
        ("pull-sweat.html", "Pull & Sweat pour chien"),
        ("produit-impermeable.html", "Imperméable chien"),
        ("collier-chien.html", "Collier pour chien"),
    ]),

    # ── PAGES SERVICE ────────────────────────────────────────────────────────

    "guide-tailles.html": make_ils_block("Prêt à choisir votre produit ?", [
        ("collier-chien.html", "Colliers pour chien"),
        ("harnais-chien.html", "Harnais pour chien"),
        ("laisse-chien.html", "Laisses pour chien"),
        ("panier-chien.html", "Paniers pour chien"),
        ("faq.html", "Questions fréquentes"),
    ]),

    "faq.html": make_ils_block("Parcourir nos collections", [
        ("collier-chien.html", "Colliers pour chien"),
        ("harnais-chien.html", "Harnais pour chien"),
        ("panier-chien.html", "Paniers pour chien"),
        ("guide-tailles.html", "Guide des tailles"),
        ("politique-expedition.html", "Politique d'expédition"),
        ("suivre-commande.html", "Suivre ma commande"),
    ]),

    "a-propos.html": make_ils_block("Découvrez nos collections", [
        ("collier-chien.html", "Colliers pour chien"),
        ("harnais-chien.html", "Harnais pour chien"),
        ("panier-chien.html", "Paniers pour chien"),
        ("blog.html", "Notre blog canin"),
    ]),

    "promenade.html": make_ils_block("Explorer par catégorie", [
        ("collier-chien.html", "Colliers pour chien"),
        ("collier-cuir-chien.html", "Colliers en cuir"),
        ("harnais-chien.html", "Harnais pour chien"),
        ("harnais-anti-traction-chien.html", "Harnais anti-traction"),
        ("laisse-chien.html", "Laisses pour chien"),
        ("sac-chien.html", "Sacs pour chien"),
        ("sac-transport-chien.html", "Sacs de transport"),
        ("guide-tailles.html", "Guide des tailles"),
    ]),

}

# ─────────────────────────────────────────────────────────────────────────────
# INSERTIONS CONTEXTUELLES DANS LES ARTICLES DE BLOG
# ─────────────────────────────────────────────────────────────────────────────

ARTICLE_INSERTIONS = {

    "article-marche-liberte.html": [
        (
            "harnais",
            '<a href="harnais-chien.html" style="color:#e69c1a;font-weight:600;text-decoration:underline;">harnais</a>'
        ),
        (
            "laisse",
            '<a href="laisse-chien.html" style="color:#e69c1a;font-weight:600;text-decoration:underline;">laisse</a>'
        ),
        (
            "collier",
            '<a href="collier-chien.html" style="color:#e69c1a;font-weight:600;text-decoration:underline;">collier</a>'
        ),
    ],

    "article-adaptation-ville.html": [
        (
            "laisse",
            '<a href="laisse-chien.html" style="color:#e69c1a;font-weight:600;text-decoration:underline;">laisse</a>'
        ),
        (
            "sac de transport",
            '<a href="sac-transport-chien.html" style="color:#e69c1a;font-weight:600;text-decoration:underline;">sac de transport</a>'
        ),
        (
            "harnais",
            '<a href="harnais-chien.html" style="color:#e69c1a;font-weight:600;text-decoration:underline;">harnais</a>'
        ),
    ],

    "article-alimentation-flair.html": [
        (
            "jouets",
            '<a href="jouets.html" style="color:#e69c1a;font-weight:600;text-decoration:underline;">jouets</a>'
        ),
        (
            "jeux d'occupation",
            '<a href="jeux-occupation.html" style="color:#e69c1a;font-weight:600;text-decoration:underline;">jeux d\'occupation</a>'
        ),
    ],

    "article-sommeil-chien.html": [
        (
            "panier",
            '<a href="panier-chien.html" style="color:#e69c1a;font-weight:600;text-decoration:underline;">panier</a>'
        ),
        (
            "coussin",
            '<a href="coussin-chien.html" style="color:#e69c1a;font-weight:600;text-decoration:underline;">coussin</a>'
        ),
        (
            "lit",
            '<a href="lit-chien.html" style="color:#e69c1a;font-weight:600;text-decoration:underline;">lit</a>'
        ),
    ],
}

# Bloc ILS pour les articles de blog (en plus des liens contextuels inline)
BLOG_ARTICLE_ILS = {
    "article-marche-liberte.html": make_ils_block("Produits évoqués dans cet article", [
        ("harnais-chien.html", "Harnais pour chien"),
        ("harnais-anti-traction-chien.html", "Harnais anti-traction"),
        ("laisse-chien.html", "Laisses pour chien"),
        ("collier-chien.html", "Colliers pour chien"),
        ("guide-tailles.html", "Guide des tailles"),
        ("blog.html", "← Retour au Blog"),
    ]),
    "article-adaptation-ville.html": make_ils_block("Produits évoqués dans cet article", [
        ("laisse-chien.html", "Laisses pour chien"),
        ("sac-transport-chien.html", "Sac de transport chien"),
        ("sac-chien.html", "Sac pour chien"),
        ("harnais-chien.html", "Harnais pour chien"),
        ("blog.html", "← Retour au Blog"),
    ]),
    "article-alimentation-flair.html": make_ils_block("Produits évoqués dans cet article", [
        ("jouets.html", "Jouets pour chien"),
        ("jeux-occupation.html", "Jeux d'occupation"),
        ("panier-chien.html", "Paniers pour chien"),
        ("blog.html", "← Retour au Blog"),
    ]),
    "article-sommeil-chien.html": make_ils_block("Produits évoqués dans cet article", [
        ("panier-chien.html", "Paniers pour chien"),
        ("panier-velvet-detail.html", "Panier Velvet Orthopédique"),
        ("lit-chien.html", "Lits pour chien"),
        ("coussin-chien.html", "Coussins pour chien"),
        ("coussin-anti-stress-chien.html", "Coussin anti-stress"),
        ("blog.html", "← Retour au Blog"),
    ]),
}

# ─────────────────────────────────────────────────────────────────────────────
# EXÉCUTION
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("\n" + "="*60)
    print("  MAILLAGE INTERNE SEO — Chetoutou")
    print("="*60)

    print("\n[1/3] Injection des blocs de liens internes...")
    for filename, block in PAGES_CONFIG.items():
        process_file(filename, block)

    print("\n[2/3] Liens contextuels dans les articles de blog...")
    for filename, ils_block in BLOG_ARTICLE_ILS.items():
        insertions = ARTICLE_INSERTIONS.get(filename, [])
        process_file(filename, ils_block, article_insertions=insertions)

    print("\n[3/3] Correction des liens morts dans la navigation...")
    html_files = [f for f in os.listdir(BASE_DIR) if f.endswith('.html')]
    for filename in sorted(html_files):
        fix_dead_links_in_file(filename)

    print("\n" + "="*60)
    print("  ✅  Maillage interne SEO terminé !")
    print("="*60 + "\n")
