
import os
import re

def clean_double_links(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove any </a> tags that are not immediately followed by </div> in a product-item context
    # Actually, let's just remove ALL <a> and </a> tags within product-item first.
    
    def clean_item(match):
        inner = match.group(1)
        # Remove all <a> and </a> tags
        inner = re.sub(r'<a[^>]*>', '', inner)
        inner = re.sub(r'</a>', '', inner)
        # Re-add the link correctly
        link = "produit-detail.html"
        if "harnais" in inner.lower():
            link = "harnais-anti-traction-chien.html"
        elif "collier" in inner.lower() and "collier-cuir" in inner.lower():
            link = "collier-cuir-chien.html"
        elif "collier" in inner.lower():
            link = "collier-chien.html"
        
        return f'<div class="product-item"><a class="product-link-wrapper" href="{link}">{inner}</a></div>'

    new_content = re.sub(r'<div class="product-item">(.*?)</div>', clean_item, content, flags=re.DOTALL)
    
    if new_content != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Deep cleaned and fixed links in {filename}")

def main():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    for f in html_files:
        if "sync" not in f and "fix" not in f and "produit" not in f:
            clean_double_links(f)

if __name__ == "__main__":
    main()
