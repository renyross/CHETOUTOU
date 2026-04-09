import os
import re

def get_header_from_index():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
        # Find header block
        match = re.search(r'(<header class="navbar".*?</header>)', content, re.DOTALL)
        if match:
            return match.group(1)
    return None

def sync_headers():
    header_content = get_header_from_index()
    if not header_content:
        print("Could not find header in index.html")
        return

    # Header for non-homepage pages should have 'scrolled' class
    subpage_header = header_content.replace('class="navbar"', 'class="navbar scrolled"')

    for filename in os.listdir('.'):
        if filename.endswith('.html') and filename != 'index.html':
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Replace header block
            new_content = re.sub(r'<header class="navbar.*?">.*?</header>', subpage_header, content, flags=re.DOTALL)
            
            if new_content != content:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated header in {filename}")

if __name__ == "__main__":
    sync_headers()
