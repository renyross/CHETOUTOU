import os
import re

directory = "/Users/renelrosene/Desktop/boutique chien"

pattern = re.compile(
    r'(<li><a href="sac-chien-moto.html">Sac Chien Moto</a></li>)',
    re.MULTILINE
)

replacement = r'\1\n                                            <li><a href="sac-transport-chien.html">cage de transport chien</a></li>'

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if "sac-chien-moto.html" in content:
            new_content = pattern.sub(replacement, content)
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {filename}")
