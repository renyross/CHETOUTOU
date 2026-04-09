import os
import re

def get_block_from_index(tag, class_name=None):
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
        if class_name:
            pattern = rf'(<{tag} class="{class_name}"[^>]*>.*?</{tag}>)'
        else:
            pattern = rf'(<{tag}[^>]*>.*?</{tag}>)'
        match = re.search(pattern, content, re.DOTALL)
        if match:
            return match.group(1)
    return None

def sync_layout():
    header_content = get_block_from_index('header', 'navbar')
    footer_content = get_block_from_index('footer', 'footer')

    if not header_content:
        print("Could not find header in index.html")
    if not footer_content:
        print("Could not find footer in index.html")
    
    if not header_content or not footer_content:
        return

    print(f"Header found ({len(header_content)} bytes)")
    print(f"Footer found ({len(footer_content)} bytes)")

    # Subpages should have the 'scrolled' class on the navbar by default
    subpage_header = header_content.replace('class="navbar"', 'class="navbar scrolled"')

    # List of all HTML files except index.html
    html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'index.html']

    for filename in html_files:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 1. Replace Header
        new_content = re.sub(r'<header class="navbar.*?">.*?</header>', subpage_header, content, flags=re.DOTALL)
        
        # 2. Replace Footer
        new_content = re.sub(r'<footer class="footer.*?">.*?</footer>', footer_content, new_content, flags=re.DOTALL)
        
        if new_content != content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated header and footer in {filename}")

if __name__ == "__main__":
    sync_layout()
