
import os
import re

def fix_carousel_links(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    def replace_link(match):
        full_tag = match.group(0)
        inner_content = match.group(2)
        lower_inner = inner_content.lower()
        
        link = match.group(1)
        
        if "stormguard" in lower_inner:
            link = "produit-impermeable.html"
        elif "velvet ortho" in lower_inner:
            link = "panier-orthopedique-velvet.html"
        elif "harnais anti-traction" in lower_inner:
            link = "harnais-anti-traction-chien.html"
            
        return f'<a href="{link}" class="rec-link">{inner_content}</a>'

    # Pattern for rec-link in carousels
    new_content = re.sub(r'<a href="([^"]*)" class="rec-link">(.*?)</a>', replace_link, content, flags=re.DOTALL)
    
    if new_content != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed carousel links in {filename}")

def main():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    for f in html_files:
        fix_carousel_links(f)

if __name__ == "__main__":
    main()
