import os
import re

def extract_block(content, tag_name, class_attr):
    pattern = re.compile(f'<{tag_name}[^>]*class="{class_attr}"[^>]*>.*?</{tag_name}>', re.DOTALL)
    match = pattern.search(content)
    return match.group(0) if match else None

def sync():
    source_path = 'index.html'
    if not os.path.exists(source_path):
        print("index.html not found")
        return

    with open(source_path, 'r', encoding='utf-8') as f:
        source_content = f.read()

    # Extract source blocks
    new_header = extract_block(source_content, 'header', 'navbar')
    new_footer = extract_block(source_content, 'footer', 'footer')

    if not new_header:
        print("Could not extract header (navbar) from index.html")
    if not new_footer:
        print("Could not extract footer from index.html")
        
    if not new_header or not new_footer:
        return

    for root, dirs, files in os.walk('.'):
        for f in files:
            if f.endswith('.html') and f != 'index.html' and 'node_modules' not in root:
                filepath = os.path.join(root, f)
                with open(filepath, 'r', encoding='utf-8') as file:
                    content = file.read()

                # Replace header
                header_pattern = re.compile(r'<header[^>]*class="navbar"[^>]*>.*?</header>', re.DOTALL)
                if header_pattern.search(content):
                    content = header_pattern.sub(new_header, content)
                
                # Replace footer
                footer_pattern = re.compile(r'<footer[^>]*class="footer"[^>]*>.*?</footer>', re.DOTALL)
                if footer_pattern.search(content):
                    content = footer_pattern.sub(new_footer, content)

                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(content)
                print(f"Synced {filepath}")

if __name__ == "__main__":
    sync()
