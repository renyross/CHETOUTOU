import os
import re

SOURCE_FILE = 'collier-chien.html'

def get_source_blocks():
    with open(SOURCE_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract Nav
    nav_match = re.search(r'(<nav[^>]*id="nav-menu"[^>]*>.*?</nav>)', content, re.DOTALL)
    if not nav_match:
        raise ValueError("Nav menu not found in source file")
    nav_html = nav_match.group(1)
    
    # Extract Footer
    footer_match = re.search(r'(<footer[^>]*class="footer"[^>]*>.*?</footer>)', content, re.DOTALL)
    if not footer_match:
        raise ValueError("Footer not found in source file")
    footer_html = footer_match.group(1)
    
    return nav_html, footer_html

def update_file(filepath, nav_html, footer_html):
    if not filepath.endswith('.html') or filepath == SOURCE_FILE:
        return
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update Navigation Menu
    nav_pattern = re.compile(r'<nav[^>]*id="nav-menu"[^>]*>.*?</nav>', re.DOTALL)
    if nav_pattern.search(content):
        content = nav_pattern.sub(nav_html, content)
    else:
        print(f"Nav menu not found in {filepath}")
        
    # 2. Update Footer
    footer_pattern = re.compile(r'<footer[^>]*class="footer"[^>]*>.*?</footer>', re.DOTALL)
    if footer_pattern.search(content):
        content = footer_pattern.sub(footer_html, content)
    else:
        print(f"Footer not found in {filepath}")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

if __name__ == "__main__":
    try:
        nav, footer = get_source_blocks()
        files = [f for f in os.listdir('.') if f.endswith('.html')]
        for f in files:
            update_file(f, nav, footer)
    except Exception as e:
        print(f"Error: {e}")
