import os
import re

def final_polish(filename):
    if not os.path.exists(filename): return
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove the fragmented duplication in hero section
    # We look for the closing </div> of the first carousel and then the broken stuff
    content = re.sub(r'(<div class="category-visual-container">.*?</div>\s*</div>\s*</div>)\s*<div class="category-visual-info">.*?</div>\s*</a>.*?</section>', 
                     r'\1\n        </section>', content, flags=re.DOTALL)

    # 2. Ensure only ONE category-visual-container exists
    # If there are still two full ones, this will catch them.
    parts = content.split('<div class="category-visual-container">')
    if len(parts) > 2:
        # Keep only part 0 and part 1
        content = parts[0] + '<div class="category-visual-container">' + parts[1] + parts[2].split('</section>')[1] if '</section>' in parts[2] else parts[0] + '<div class="category-visual-container">' + parts[1]

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

# Apply
files = [f for f in os.listdir('.') if f.endswith('.html') and ('harnais' in f or 'collier' in f or 'tapis' in f or 'panier' in f or 'lit' in f or 'coussin' in f or 'promenade' in f or 'jouet' in f or 'hygiene' in f)]
for f in files:
    final_polish(f)
    print(f"Polished {f}")
