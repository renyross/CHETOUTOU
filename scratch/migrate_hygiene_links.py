import os
import re

def update_links():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    for filename in html_files:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        updated = False
        
        # 1. Update Megamenu/Nav link
        if 'href="index.html#hygiene"' in content:
            content = content.replace('href="index.html#hygiene"', 'href="hygiene.html"')
            updated = True
        
        # 2. Update Category Carousel links
        # Looking for <a href="gamelles.html" class="tag-item">
        # or any href="gamelles.html" that is part of a category navigation
        if 'href="gamelles.html"' in content:
            content = content.replace('href="gamelles.html"', 'href="hygiene.html"')
            updated = True
            
        if updated:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {filename}")

if __name__ == "__main__":
    update_links()
