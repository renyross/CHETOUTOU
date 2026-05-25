import os
import re

def update_megamenu(directory):
    new_links = """                                            <li><a href="coussin-chien.html">Coussin Chien</a></li>
                                            <li><a href="coussin-xxl-chien.html">Coussin Chien XXL</a></li>
                                            <li><a href="coussin-dehoussable-chien.html">Coussin Chien Déhoussable</a></li>
                                            <li><a href="coussin-anti-stress-chien.html">Coussin Anti-Stress Chien</a></li>
                                            <li><a href="coussin-indestructible-chien.html">Coussin Chien Indestructible</a></li>
                                            <li><a href="coussin-orthopedique-chien.html">Coussin Chien Orthopédique</a></li>
                                            <li><a href="grand-coussin-chien.html">Grand Coussin Chien</a></li>
                                            <li><a href="panier-coussin-chien.html">Panier Coussin Chien</a></li>
                                            <li><a href="coussin-voiture-chien.html">Coussin Chien Voiture</a></li>
                                            <li><a href="coussin-lavable-chien.html">Coussin Chien Lavable</a></li>
                                            <li><a href="tapis-xxl-chien.html">Tapis XXL Chien</a></li>
                                            <li><a href="tapis-absorbant-chien.html">Tapis Absorbant Chien</a></li>
                                            <li><a href="tapis-rafraichissant-chien.html">Tapis Rafraîchissant Chien</a></li>"""

    pattern = re.compile(r'(<h3>Coussins & Tapis</h3>\s*<ul>)(.*?)(\s*</ul>)', re.DOTALL)

    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if "<h3>Coussins & Tapis</h3>" in content:
                new_content = pattern.sub(r'\1\n' + new_links + r'\3', content)
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated {filename}")

if __name__ == "__main__":
    update_megamenu("/Users/renelrosene/Desktop/boutique chien")
