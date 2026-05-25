import os
import re

def clean_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix Visual Carousel Duplication (Lines 358-431 in harnais-chien.html)
    # Match from first <div class="category-visual-container"> to the last one before <section class="collection-section">
    content = re.sub(r'(<div class="category-visual-container">.*?)<div class="category-visual-container">.*?</div>\s*</div>\s*</div>', 
                     r'\1', content, flags=re.DOTALL)

    # 2. Fix Grid Duplication
    # Sometimes there's garbage after the first </div> of collection-grid
    # We want to keep ONLY the grid we just injected and remove any trailing product-item stuff before the section closes.
    content = re.sub(r'(<div class="collection-grid">.*?</div>)\s*(<div class="product-info">.*?</div>\s*)*\s*</div>\s*</div>\s*</section>',
                     r'\1\n                    </div>\n                </div>\n            </section>',
                     content, flags=re.DOTALL)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

# Apply to all category files
files = [f for f in os.listdir('.') if f.endswith('.html') and ('collier' in f or 'harnais' in f or 'panier' in f or 'lit' in f or 'coussin' in f or 'tapis' in f or 'promenade' in f or 'jouet' in f or 'hygiene' in f)]

for f in files:
    clean_file(f)
    print(f"Cleaned {f}")
