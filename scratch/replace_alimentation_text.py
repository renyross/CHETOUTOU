import os
import re

directory = "/Users/renelrosene/Desktop/boutique chien"

# We want to replace the entry in the Alimentation column
pattern = re.compile(
    r'(<h3>Alimentation</h3>\s*<ul>\s*<li><a href="tapis-lechage.html">)Tapis de Léchage Chien(</a></li>)',
    re.MULTILINE | re.IGNORECASE
)

replacement = r'\1distributeur croquette chien\2'

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if "Alimentation" in content:
            new_content = pattern.sub(replacement, content)
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {filename}")
