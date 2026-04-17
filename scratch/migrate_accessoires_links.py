import os

def update_links():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    for filename in html_files:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        updated = False
        
        # 1. Update Megamenu/Nav link
        if 'href="index.html#accessoires"' in content:
            content = content.replace('href="index.html#accessoires"', 'href="accessoires.html"')
            updated = True
        
        # 2. Update Category Carousel and other links
        if 'href="medailles.html"' in content:
            content = content.replace('href="medailles.html"', 'href="accessoires.html"')
            updated = True
            
        if updated:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {filename}")

if __name__ == "__main__":
    update_links()
