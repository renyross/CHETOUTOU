
import os
import re

def clean_links(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Only remove product-link-wrapper and product-link-block within product-item
    def clean_item(match):
        item_inner = match.group(1)
        # Remove the tags I added
        item_inner = re.sub(r'<a class="product-link-wrapper" href="[^"]*">', '', item_inner)
        item_inner = re.sub(r'<a class="product-link-block" href="[^"]*">', '', item_inner)
        item_inner = re.sub(r'</a>', '', item_inner)
        return f'<div class="product-item">{item_inner}</div>'

    new_content = re.sub(r'<div class="product-item">(.*?)</div>', clean_item, content, flags=re.DOTALL)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)

def main():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    for f in html_files:
        if "sync" not in f and "fix" not in f and "produit" not in f:
            clean_links(f)

if __name__ == "__main__":
    main()
