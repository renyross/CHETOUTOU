import os
import re

directory = "/Users/renelrosene/Desktop/boutique chien"

# Define the target block to replace
# We use a regex to handle potential slight variations in whitespace
pattern = re.compile(
    r'(<h3>Balles & Lancer</h3>\s*<ul>\s*<li><a href="balles-chien.html">Balles pour chien</a></li>\s*<li><a href="frisbee-chien.html">Frisbee chien</a></li>\s*<li><a href="lanceur-balle-chien.html">Lanceur de balle Chien</a></li>\s*</ul>)',
    re.MULTILINE
)

replacement = """<h3>Balles & Lancer</h3>
                                        <ul>
                                            <li><a href="balles-chien.html">Balles pour chien</a></li>
                                            <li><a href="frisbee-chien.html">Frisbee chien</a></li>
                                            <li><a href="lanceur-balle-chien.html">Lanceur de balle Chien</a></li>
                                            <li><a href="lanceur-balle-chien.html">lanceur de balle pour chien</a></li>
                                            <li><a href="lanceur-balle-chien.html">lance balle pour chien</a></li>
                                            <li><a href="balles-chien.html">balle pour chien</a></li>
                                            <li><a href="balles-chien.html">balle chien</a></li>
                                            <li><a href="jouets-indestructibles.html">balle pour chien indestructible</a></li>
                                        </ul>"""

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if "Balles & Lancer" in content:
            new_content = pattern.sub(replacement, content)
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {filename}")
            else:
                print(f"Pattern not found in {filename}")
