import os
import re

directory = "/Users/renelrosene/Desktop/boutique chien"

pattern = re.compile(
    r'(<h3>Sécurité</h3>\s*<ul>\s*<li><a href="museliere.html">Muselière</a></li>\s*<li><a href="accessoires.html">Médailles & Sécurité</a></li>\s*</ul>)',
    re.MULTILINE
)

replacement = """<h3>Sécurité</h3>
                                        <ul>
                                            <li><a href="museliere.html">Muselière</a></li>
                                            <li><a href="accessoires.html">Médailles & Sécurité</a></li>
                                            <li><a href="accessoires.html">Ceinture de sécurité pour chien</a></li>
                                            <li><a href="harnais-chien-voiture.html">Attache voiture chien</a></li>
                                            <li><a href="collier-gps-chien.html">Tracker pour chien</a></li>
                                            <li><a href="accessoires.html">Licol pour chien</a></li>
                                        </ul>"""

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if "Sécurité" in content:
            new_content = pattern.sub(replacement, content)
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {filename}")
