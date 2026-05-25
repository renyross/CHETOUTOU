import os

def link_about():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    for filename in html_files:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace common variations of the link
        new_content = content.replace('href="#about"', 'href="a-propos.html"')
        new_content = new_content.replace('href="#apropos"', 'href="a-propos.html"')
        
        # Also ensure "À propos" or "A propos" links to the new page if it was pointing to #
        if 'À propos' in new_content or 'A propos' in new_content:
            # We want to catch things like <a href="#">À propos</a>
            import re
            new_content = re.sub(r'href="#"([^>]*?>\s*(À|A)\s*propos)', r'href="a-propos.html"\1', new_content, flags=re.IGNORECASE)

        if new_content != content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated link in {filename}")

if __name__ == "__main__":
    link_about()
