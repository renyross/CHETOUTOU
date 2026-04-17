import os
import re

def remove_vetements_filter():
    # Match the sidebar filter list item for Vêtements
    # Pattern looks for <li><a href="impermeables.html">Vêtements (StormGuard)</a></li>
    # and variations with different whitespace or brackets.
    pattern = re.compile(r'<li><a href="impermeables\.html">Vêtements.*?</a></li>\s*', re.IGNORECASE)
    
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    for filename in html_files:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = pattern.sub('', content)
        
        if new_content != content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Removed Vêtements filter from {filename}")

if __name__ == "__main__":
    remove_vetements_filter()
