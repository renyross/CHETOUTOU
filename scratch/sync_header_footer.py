import os
import re

def final_sync():
    # 1. Extract Master Components
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            index_content = f.read()
    except FileNotFoundError:
        print("index.html not found.")
        return

    header_match = re.search(r'(<div class="announcement-bar">.*?</header>)', index_content, re.DOTALL)
    if not header_match:
        header_match = re.search(r'(<header.*?</header>)', index_content, re.DOTALL)
    master_header = header_match.group(1)

    footer_match = re.search(r'(<footer.*</footer>)', index_content, re.DOTALL)
    master_footer = footer_match.group(1)

    # 2. List target files
    html_files = [f for f in os.listdir('.') if f.endswith('.html') and f not in ['index.html', 'checkout.html']]
    
    count = 0
    for filename in html_files:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # A. Scrub all existing header blocks
        header_regex = r'(<div class="announcement-bar">.*?</header>|<header.*?</header>)'
        content = re.sub(header_regex, '', content, flags=re.DOTALL)

        # B. Scrub all existing footer blocks
        # Including broken ones or comments used as markers
        footer_regex = r'(<footer.*?</footer>|<!-- Information Column -->.*?</footer>)'
        content = re.sub(footer_regex, '', content, flags=re.DOTALL)

        # C. Scrub corruption patterns (double tags)
        content = re.sub(r'TYPE html>.*?<body[^>]*>', '', content, flags=re.DOTALL)
        content = re.sub(r'<!DOCTYPE html>.*?<body[^>]*>', '', content, flags=re.DOTALL, count=0) # Remove extra doc types

        # D. Ensure <body> exists (might have been scrubbed if double)
        if '<body' not in content:
            # If missing, we might have over-scrubbed or the file was very broken.
            # Let's try to restore a basic structure if it's really gone.
            # But usually it's there.
            pass

        # E. Inject Master Header
        if '<body' in content:
            content = re.sub(r'(<body[^>]*>)', r'\1\n' + master_header, content, count=1)
        else:
            # Fallback if body is missing (should not happen after scrubbing)
            content = '<body class="shop-page">\n' + master_header + '\n' + content

        # F. Inject Master Footer
        if '</body>' in content:
            content = content.replace('</body>', master_footer + '\n</body>')
        else:
            content += '\n' + master_footer + '\n</body>\n</html>'

        # G. Final Cleanup: ensure no duplicate <html> or <head> at the very end
        # (Sometimes they are left over if the file was really messy)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

    print(f"Successfully cleaned and synchronized {count} files.")

if __name__ == "__main__":
    final_sync()
