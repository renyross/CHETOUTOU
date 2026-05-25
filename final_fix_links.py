
import os
import re

def fix_file_properly(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = ""
    pos = 0
    while True:
        start_idx = content.find('<div class="product-item">', pos)
        if start_idx == -1:
            new_content += content[pos:]
            break
        
        new_content += content[pos:start_idx]
        
        # Find the matching closing </div>
        depth = 0
        i = start_idx
        while i < len(content):
            if content[i:i+5] == '<div ':
                depth += 1
                i += 5
            elif content[i:i+6] == '</div>':
                depth -= 1
                i += 6
                if depth == 0:
                    break
            else:
                i += 1
        
        full_item = content[start_idx:i]
        first_gt = full_item.find('>')
        last_lt = full_item.rfind('<')
        inner = full_item[first_gt+1:last_lt]
        
        # Clean inner from any <a> tags we added
        inner = re.sub(r'<a[^>]*>', '', inner)
        inner = re.sub(r'</a>', '', inner)
        
        # Determine the best link
        link = "produit-detail.html"
        lower_inner = inner.lower()
        if "stormguard" in lower_inner or "jaune iconique" in lower_inner:
            link = "produit-impermeable.html"
        elif "velvet ortho" in lower_inner or "panier velvet" in lower_inner:
            link = "panier-orthopedique-velvet.html"
        elif "harnais anti-traction" in lower_inner or "steadywalk" in lower_inner:
            link = "harnais-anti-traction-chien.html"
            
        new_item = f'<div class="product-item"><a class="product-link-wrapper" href="{link}">{inner}</a></div>'
        new_content += new_item
        pos = i

    if new_content != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Properly fixed links in {filename}")

def main():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    for f in html_files:
        # Don't process actual product pages or scripts
        if any(x in f for x in ["produit-", "panier-orthopedique-velvet", "sync", "fix", "clean"]):
            continue
        fix_file_properly(f)

if __name__ == "__main__":
    main()
