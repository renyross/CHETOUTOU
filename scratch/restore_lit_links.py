import os
import re

target_dir = "/Users/renelrosene/Desktop/boutique chien"

# Restore Lit Chien links
# Pattern: href="panier-chien.html">Lit Chien
# Pattern: href="panier-chien.html">Lit XXL
# etc.

restore_map = {
    'href="panier-chien.html">Lit Chien': 'href="lit-chien.html">Lit Chien',
    'href="panier-chien.html">Lit XXL': 'href="lit-xxl-chien.html">Lit XXL', # Just in case
    'href="panier-chien.html">Lit Surélevé': 'href="lit-sureleve-chien.html">Lit Surélevé',
    'href="panier-chien.html">Canapé Luxe Chien': 'href="canape-chien.html">Canapé Luxe Chien',
}

for root, dirs, files in os.walk(target_dir):
    for file in files:
        if file.endswith(".html"):
            path = os.path.join(root, file)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            
            new_content = content
            for old, new in restore_map.items():
                new_content = new_content.replace(old, new)
            
            if new_content != content:
                print(f"Restoring links in {file}")
                with open(path, "w", encoding="utf-8") as f:
                    f.write(new_content)
