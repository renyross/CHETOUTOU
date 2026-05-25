import os
import re

def fix_duplication(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all occurrences of category-visual-container blocks
    # and keep only the first one found after intro-large
    parts = re.split(r'(<div class="category-visual-container">.*?</div>\s*</div>)', content, flags=re.DOTALL)
    
    if len(parts) > 2:
        # We have at least one match. parts[0] is everything before first match, parts[1] is first match, parts[2:] is the rest.
        # But we might have multiple matches. 
        # Actually split gives: [before, match1, after1, match2, after2, ...]
        new_content = parts[0] + parts[1]
        # Skip subsequent matches but keep the text between them? 
        # Usually the duplication is immediate.
        # Let's just remove any OTHER category-visual-container or list
        rest = "".join(parts[2:])
        rest = re.sub(r'<div class="category-visual-container">.*?</div>\s*</div>', '', rest, flags=re.DOTALL)
        rest = re.sub(r'<div class="category-visual-list">.*?</div>', '', rest, flags=re.DOTALL)
        new_content += rest
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
for f in html_files:
    if fix_duplication(f):
        print(f"Fixed duplication in {f}")
