import os
import re

target_dir = "/Users/renelrosene/Desktop/boutique chien"
old_link = "lit-chien.html"
new_link = "panier-chien.html"

for root, dirs, files in os.walk(target_dir):
    for file in files:
        if file.endswith(".html"):
            path = os.path.join(root, file)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            
            if old_link in content:
                print(f"Updating links in {file}")
                new_content = content.replace(old_link, new_link)
                with open(path, "w", encoding="utf-8") as f:
                    f.write(new_content)
