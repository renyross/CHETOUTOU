import os
import re

coussin_files = [
    "coussin-chien.html",
    "coussin-xxl-chien.html",
    "coussin-dehoussable-chien.html",
    "coussin-anti-stress-chien.html",
    "coussin-indestructible-chien.html",
    "coussin-orthopedique-chien.html",
    "grand-coussin-chien.html",
    "panier-coussin-chien.html",
    "coussin-voiture-chien.html",
    "coussin-lavable-chien.html"
]

seo_data = {
    "coussin-chien.html": {
        "h1": "Coussin pour Chien",
        "intro": "Offrez à votre compagnon un espace de repos doux et accueillant avec notre collection de coussins pour chiens. Conçus pour allier confort thermique et soutien moelleux, ils s'intègrent parfaitement dans tout intérieur moderne."
    },
    "coussin-xxl-chien.html": {
        "h1": "Coussin Chien XXL",
        "intro": "Parce que les grands gabarits méritent un confort à leur mesure, nos coussins XXL offrent une surface généreuse et un rembourrage haute densité pour soutenir les chiens de grande taille sans s'affaisser."
    },
    "coussin-dehoussable-chien.html": {
        "h1": "Coussin Chien Déhoussable",
        "intro": "L'hygiène est primordiale pour le bien-être de votre animal. Nos coussins déhoussables sont dotés de fermetures éclair robustes permettant un retrait facile de la housse pour un lavage fréquent en machine."
    },
    "coussin-anti-stress-chien.html": {
        "h1": "Coussin Anti-Stress Chien",
        "intro": "Inspirés par la sensation de sécurité maternelle, nos coussins anti-stress utilisent des rebords surélevés et des textures ultra-douces pour apaiser l'anxiété et favoriser un sommeil profond et réparateur."
    },
    "coussin-indestructible-chien.html": {
        "h1": "Coussin Chien Indestructible",
        "intro": "Pour les chiens aux mâchoires puissantes, nous avons conçu une gamme de coussins en tissus techniques ultra-résistants. Anti-griffures et anti-morsures, ils défient le temps et les comportements destructeurs."
    },
    "coussin-orthopedique-chien.html": {
        "h1": "Coussin Chien Orthopédique",
        "intro": "Idéal pour les chiens âgés ou souffrant de problèmes articulaires, nos coussins orthopédiques intègrent de la mousse à mémoire de forme pour soulager les points de pression et améliorer la qualité de vie."
    },
    "grand-coussin-chien.html": {
        "h1": "Grand Coussin pour Chien",
        "intro": "Un espace de liberté totale. Nos grands coussins permettent à votre chien de s'étirer de tout son long sur une surface premium, alliant design épuré et confort exceptionnel pour toutes les races."
    },
    "panier-coussin-chien.html": {
        "h1": "Panier Coussin Chien",
        "intro": "Le meilleur des deux mondes : la structure rassurante d'un panier associée au moelleux d'un coussin haut de gamme. Un hybride parfait pour les chiens qui aiment se blottir tout en restant au sol."
    },
    "coussin-voiture-chien.html": {
        "h1": "Coussin Chien pour Voiture",
        "intro": "Voyagez en toute sérénité avec nos coussins spécialement adaptés aux sièges de voiture. Ils offrent confort et stabilité durant vos trajets, protégeant vos sièges tout en sécurisant votre compagnon."
    },
    "coussin-lavable-chien.html": {
        "h1": "Coussin Chien Lavable",
        "intro": "Simplifiez-vous la vie avec nos coussins entièrement lavables. Conçus avec des matériaux qui ne perdent pas leur forme au fil des cycles, ils garantissent un couchage toujours frais et sain."
    }
}

coussin_carousel = """                    <div class="category-visual-list">
                        <a href="coussin-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper">
                                <img src="cat_coussin_pure.png" alt="Coussin Chien">
                            </div>
                            <div class="category-visual-info"><h3>Classique</h3></div>
                        </a>
                        <a href="coussin-xxl-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper">
                                <img src="cat_coussin_xxl_visual.png" alt="Coussin XXL">
                            </div>
                            <div class="category-visual-info"><h3>Format XXL</h3></div>
                        </a>
                        <a href="coussin-dehoussable-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper">
                                <img src="cat_coussin_dehoussable_visual.png" alt="Coussin Déhoussable">
                            </div>
                            <div class="category-visual-info"><h3>Déhoussable</h3></div>
                        </a>
                        <a href="coussin-anti-stress-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper">
                                <img src="cat_coussin_antistress_visual.png" alt="Coussin Anti-Stress">
                            </div>
                            <div class="category-visual-info"><h3>Anti-Stress</h3></div>
                        </a>
                        <a href="coussin-indestructible-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper">
                                <img src="cat_coussin_indestructible_visual.png" alt="Coussin Indestructible">
                            </div>
                            <div class="category-visual-info"><h3>Indestructible</h3></div>
                        </a>
                        <a href="coussin-orthopedique-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper">
                                <img src="cat_coussin_orthopedique_visual.png" alt="Coussin Orthopédique">
                            </div>
                            <div class="category-visual-info"><h3>Orthopédique</h3></div>
                        </a>
                        <a href="grand-coussin-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper">
                                <img src="cat_coussin_grand_visual.png" alt="Grand Coussin">
                            </div>
                            <div class="category-visual-info"><h3>Grand Format</h3></div>
                        </a>
                        <a href="panier-coussin-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper">
                                <img src="cat_panier_pure.png" alt="Panier Coussin">
                            </div>
                            <div class="category-visual-info"><h3>Panier Coussin</h3></div>
                        </a>
                        <a href="coussin-voiture-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper">
                                <img src="cat_coussin_voiture_visual.png" alt="Coussin Voiture">
                            </div>
                            <div class="category-visual-info"><h3>Pour Voiture</h3></div>
                        </a>
                        <a href="coussin-lavable-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper">
                                <img src="cat_coussin_lavable_visual.png" alt="Coussin Lavable">
                            </div>
                            <div class="category-visual-info"><h3>Lavable</h3></div>
                        </a>
                    </div>"""

def update_file(filename):
    if not os.path.exists(filename):
        print(f"Skipping {filename}: Not found")
        return
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update Carousel
    content = re.sub(r'<div class="category-visual-list">.*?</div>', coussin_carousel, content, flags=re.DOTALL)
    
    # 2. Update SEO Intro
    if filename in seo_data:
        h1_text = seo_data[filename]["h1"]
        intro_text = seo_data[filename]["intro"]
        
        # Replace H1
        content = re.sub(r'<h1>.*?</h1>', f'<h1>{h1_text}</h1>', content)
        
        # Replace Intro Paragraph (in intro-large)
        intro_pattern = r'(<div class="intro-large">.*?<p>).*?(</p>)'
        content = re.sub(intro_pattern, f'\\1{intro_text}\\2', content, flags=re.DOTALL)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename}")

for f in coussin_files:
    update_file(f)
