import os
import re

tapis_files = [
    "tapis-chien.html",
    "tapis-rafraichissant-chien.html",
    "tapis-fouille.html",
    "tapis-lechage.html",
    "tapis-absorbant-chien.html",
    "tapis-xxl-chien.html",
    "tapis-gamelle-chien.html",
    "tapis-fraicheur-chien.html",
    "tapis-refrigerant-chien.html"
]

seo_data = {
    "tapis-chien.html": {
        "h1": "Tapis pour Chien",
        "intro": "Alliez propreté et confort avec notre gamme de tapis pour chiens. Qu'il s'agisse de protéger vos sols, de rafraîchir votre animal ou de le stimuler par le jeu, nos tapis premium répondent à toutes les exigences du quotidien."
    },
    "tapis-rafraichissant-chien.html": {
        "h1": "Tapis Rafraîchissant Chien",
        "intro": "Protégez votre chien des coups de chaleur avec nos tapis rafraîchissants haute performance. Activés par pression, ils offrent une sensation de fraîcheur immédiate et durable sans besoin d'eau ni d'électricité."
    },
    "tapis-fouille.html": {
        "h1": "Tapis de Fouille pour Chien",
        "intro": "Stimulez l'odorat et l'intelligence de votre compagnon avec nos tapis de fouille. Cachez ses friandises préférées dans les recoins du tapis pour transformer le goûter en une activité ludique et apaisante."
    },
    "tapis-lechage.html": {
        "h1": "Tapis de Léchage Chien",
        "intro": "Le tapis de léchage est l'accessoire idéal pour réduire l'anxiété et favoriser une alimentation lente. Étalez-y de la nourriture humide pour occuper votre chien sainement durant vos absences ou les soins."
    },
    "tapis-absorbant-chien.html": {
        "h1": "Tapis Absorbant Chien",
        "intro": "Gardez votre intérieur propre même par temps de pluie. Nos tapis absorbants retiennent l'humidité et les impuretés dès le passage des pattes, offrant une barrière efficace contre la boue et les saletés."
    },
    "tapis-xxl-chien.html": {
        "h1": "Tapis Chien XXL",
        "intro": "Un espace de repos géant pour les chiens de grande race. Nos tapis XXL offrent une surface confortable et résistante, idéale pour les siestes impromptues sur le sol tout en isolant du froid."
    },
    "tapis-gamelle-chien.html": {
        "h1": "Tapis Gamelle Chien",
        "intro": "Protégez votre sol des éclaboussures et des miettes avec nos tapis de gamelle antidérapants. En silicone alimentaire facile à nettoyer, ils maintiennent l'espace repas de votre chien propre et organisé."
    },
    "tapis-fraicheur-chien.html": {
        "h1": "Tapis Fraîcheur pour Chien",
        "intro": "Un tapis léger et respirant conçu pour les mois d'été. Sa structure technique permet une circulation d'air optimale sous le corps de votre animal, garantissant un repos frais et agréable sans humidité."
    },
    "tapis-refrigerant-chien.html": {
        "h1": "Tapis Réfrigérant Chien",
        "intro": "Technologie de pointe pour un refroidissement maximal. Nos tapis réfrigérants utilisent des matériaux innovants pour absorber la chaleur corporelle et offrir une zone de repos ultra-fraîche durant les canicules."
    }
}

tapis_carousel = """                    <div class="category-visual-list">
                        <a href="tapis-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper">
                                <img src="cat_tapis_chien_visual.png" alt="Tapis pour Chien">
                            </div>
                            <div class="category-visual-info"><h3>Classique</h3></div>
                        </a>
                        <a href="tapis-rafraichissant-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper">
                                <img src="cat_tapis_rafraichissant_visual.png" alt="Tapis Rafraîchissant">
                            </div>
                            <div class="category-visual-info"><h3>Rafraîchissant</h3></div>
                        </a>
                        <a href="tapis-fouille.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper">
                                <img src="cat_tapis_fouille_visual.png" alt="Tapis de Fouille">
                            </div>
                            <div class="category-visual-info"><h3>Jeu de Fouille</h3></div>
                        </a>
                        <a href="tapis-lechage.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper">
                                <img src="cat_tapis_lechage_visual.png" alt="Tapis de Léchage">
                            </div>
                            <div class="category-visual-info"><h3>Léchage</h3></div>
                        </a>
                        <a href="tapis-absorbant-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper">
                                <img src="cat_tapis_chien_visual.png" alt="Tapis Absorbant">
                            </div>
                            <div class="category-visual-info"><h3>Absorbant</h3></div>
                        </a>
                        <a href="tapis-xxl-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper">
                                <img src="cat_tapis_xxl_visual.png" alt="Tapis XXL">
                            </div>
                            <div class="category-visual-info"><h3>Format XXL</h3></div>
                        </a>
                        <a href="tapis-gamelle-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper">
                                <img src="cat_tapis_gamelle_visual.png" alt="Tapis Gamelle">
                            </div>
                            <div class="category-visual-info"><h3>Tapis Gamelle</h3></div>
                        </a>
                        <a href="tapis-fraicheur-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper">
                                <img src="cat_tapis_rafraichissant_visual.png" alt="Tapis Fraîcheur">
                            </div>
                            <div class="category-visual-info"><h3>Fraîcheur</h3></div>
                        </a>
                        <a href="tapis-refrigerant-chien.html" class="category-visual-card">
                            <div class="category-visual-img-wrapper">
                                <img src="cat_tapis_rafraichissant_visual.png" alt="Tapis Réfrigérant">
                            </div>
                            <div class="category-visual-info"><h3>Réfrigérant</h3></div>
                        </a>
                    </div>"""

def update_file(filename):
    if not os.path.exists(filename):
        print(f"Skipping {filename}: Not found")
        return
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update Carousel
    content = re.sub(r'<div class="category-visual-list">.*?</div>', tapis_carousel, content, flags=re.DOTALL)
    
    # 2. Update SEO Intro
    if filename in seo_data:
        h1_text = seo_data[filename]["h1"]
        intro_text = seo_data[filename]["intro"]
        
        content = re.sub(r'<h1>.*?</h1>', f'<h1>{h1_text}</h1>', content)
        intro_pattern = r'(<div class="intro-large">.*?<p>).*?(</p>)'
        content = re.sub(intro_pattern, f'\\1{intro_text}\\2', content, flags=re.DOTALL)

    # 3. Fix Breadcrumb (Accueil / Couchage / Tapis / [Subpage])
    # Except for tapis-chien.html which should be Accueil / Couchage / Tapis
    if filename == "tapis-chien.html":
        breadcrumb = '<div class="breadcrumb">\n                    <a href="index.html">Accueil</a> / <a href="couchage.html">Couchage</a> / <span>Tapis Chien</span>\n                </div>'
    else:
        breadcrumb = f'<div class="breadcrumb">\n                    <a href="index.html">Accueil</a> / <a href="couchage.html">Couchage</a> / <a href="tapis-chien.html">Tapis</a> / <span>{seo_data[filename]["h1"]}</span>\n                </div>'
    
    content = re.sub(r'<div class="breadcrumb">.*?</div>', breadcrumb, content, flags=re.DOTALL)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename}")

for f in tapis_files:
    update_file(f)
