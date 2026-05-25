import os
import re

directory = "/Users/renelrosene/Desktop/boutique chien"

# We want to remove the entry from the Gamelles column
pattern = re.compile(
    r'(<h3>Gamelles</h3>\s*<ul>.*?)\s*<li><a href="tapis-gamelle-chien.html">Tapis de Gamelle Chien</a></li>',
    re.DOTALL | re.IGNORECASE
)

replacement = r'\1'

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if "Gamelles" in content:
            new_content = pattern.sub(replacement, content)
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {filename}")
