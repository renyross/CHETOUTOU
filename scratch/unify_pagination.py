import os
import re

target_dir = "/Users/renelrosene/Desktop/boutique chien"

standard_pagination = """                <nav class="collection-pagination" aria-label="Pagination">
                    <a href="#" class="page-btn active" aria-current="page">1</a>
                    <a href="#" class="page-btn">2</a>
                    <a href="#" class="page-btn">3</a>
                    <span class="page-divider">...</span>
                    <a href="#" class="page-btn">10</a>
                    <a href="#" class="page-btn" aria-label="Suivant">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="m9 18 6-6-6-6" />
                        </svg>
                    </a>
                </nav>"""

# Regex to find the entire <nav class="collection-pagination" ...> </nav> block
pagination_regex = re.compile(r'<nav class="collection-pagination".*?</nav>', re.DOTALL)

for filename in os.listdir(target_dir):
    if filename.endswith(".html"):
        filepath = os.path.join(target_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if '<nav class="collection-pagination"' in content:
            new_content = pagination_regex.sub(standard_pagination, content)
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {filename}")
