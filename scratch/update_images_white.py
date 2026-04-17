import os
import re

MAPPING = {
    "Promenade": "cat_promenade.png",
    "Couchage": "cat_couchage.png",
    "Jouets": "cat_jouets.png",
    "Hygiène & Soins": "cat_hygiene.png",
    "Accessoires": "cat_accessoires.png"
}

def update_images():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    exclude = ['index.html', 'blog.html', 'coordonnees.html', 'faq.html', 'guide-tailles.html', 'politique-confidentialite.html', 'politique-expedition.html', 'politique-remboursement.html', 'conditions-utilisation.html', 'preferences-cookies.html', 'checkout.html']
    
    for filename in html_files:
        if filename in exclude:
            continue
            
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        changed = False
        for label, new_img in MAPPING.items():
            # Target the specific structure: 
            # <div class="tag-icon"><img src="..."></div><span>LABEL</span>
            # OR <div class="tag-icon"><img src="..."></div> <span>LABEL</span>
            pattern = rf'(<div class="tag-icon"><img src=")[^"]+(" alt=""></div>\s*<span>{label}</span>)'
            if re.search(pattern, content):
                content = re.sub(pattern, rf'\1{new_img}\2', content)
                changed = True
                
        if changed:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated images in {filename}")

if __name__ == "__main__":
    update_images()
