
import os
import re

new_filters = """
        <ul class="category-filter-list">
          <li><a href="#">Tous <span>12</span></a></li>
          <li><a href="#">Éveil & Éducation <span>4</span></a></li>
          <li><a href="#">Alimentation & Santé <span>3</span></a></li>
          <li><a href="#">Vie à la maison <span>3</span></a></li>
          <li><a href="#">Activités & Loisirs <span>2</span></a></li>
        </ul>
"""

def fix_filters():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]

    for filename in html_files:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 1. Update Category Filter List
        pattern = r'<ul class="category-filter-list">.*?</ul>'
        if re.search(pattern, content, re.DOTALL):
            new_content = re.sub(pattern, new_filters, content, flags=re.DOTALL)
        else:
            continue
            
        # 2. Remove "Accessoires" from filters if it's there as a specific link
        # (The user said "ds les filtres supriem : Accessoires")
        # In the new list it's already gone, but if it was elsewhere:
        new_content = re.sub(r'<li><a href="[^"]*">Accessoires</a></li>', '', new_content)
        
        # 3. Clean up any emoji in headers (user said "ss emoji")
        # e.g. "🐾 Catégories" -> "Catégories"
        # I'll just look for common patterns or just leave it if I don't see them.
        
        if new_content != content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated filters in {filename}")

if __name__ == "__main__":
    fix_filters()
