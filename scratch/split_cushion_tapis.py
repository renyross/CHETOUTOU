import os
import re

def update_megamenu_structure(directory):
    coussins_html = """                                    <div class="megamenu-column">
                                        <h3>Coussins</h3>
                                        <ul>
                                            <li><a href="coussin-chien.html">Coussin Chien</a></li>
                                            <li><a href="coussin-xxl-chien.html">Coussin Chien XXL</a></li>
                                            <li><a href="coussin-dehoussable-chien.html">Coussin Chien Déhoussable</a></li>
                                            <li><a href="coussin-anti-stress-chien.html">Coussin Anti-Stress Chien</a></li>
                                            <li><a href="coussin-indestructible-chien.html">Coussin Chien Indestructible</a></li>
                                            <li><a href="coussin-orthopedique-chien.html">Coussin Chien Orthopédique</a></li>
                                            <li><a href="grand-coussin-chien.html">Grand Coussin Chien</a></li>
                                            <li><a href="panier-coussin-chien.html">Panier Coussin Chien</a></li>
                                            <li><a href="coussin-voiture-chien.html">Coussin Chien Voiture</a></li>
                                            <li><a href="coussin-lavable-chien.html">Coussin Chien Lavable</a></li>
                                        </ul>
                                    </div>
                                    <div class="megamenu-column">
                                        <h3>Tapis</h3>
                                        <ul>
                                            <li><a href="tapis-chien.html">Tapis pour Chien</a></li>
                                            <li><a href="tapis-rafraichissant-chien.html">Tapis Rafraîchissant</a></li>
                                            <li><a href="tapis-fouille.html">Tapis de Fouille</a></li>
                                            <li><a href="tapis-lechage.html">Tapis de Léchage</a></li>
                                            <li><a href="tapis-absorbant-chien.html">Tapis Absorbant</a></li>
                                            <li><a href="tapis-xxl-chien.html">Tapis Chien XXL</a></li>
                                            <li><a href="tapis-gamelle-chien.html">Tapis Gamelle Chien</a></li>
                                            <li><a href="tapis-fraicheur-chien.html">Tapis Fraîcheur</a></li>
                                            <li><a href="tapis-refrigerant-chien.html">Tapis Réfrigérant</a></li>
                                        </ul>
                                    </div>"""

    # Matches the entire Coussins & Tapis column
    pattern = re.compile(r'<div class="megamenu-column">\s*<h3>Coussins & Tapis</h3>.*?</div>', re.DOTALL)

    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if "<h3>Coussins & Tapis</h3>" in content:
                new_content = pattern.sub(coussins_html, content)
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Split megamenu columns in {filename}")

if __name__ == "__main__":
    update_megamenu_structure("/Users/renelrosene/Desktop/boutique chien")
