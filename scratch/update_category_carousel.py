import os
import re

def update_carousel_html():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    # Skip main non-category pages if needed, but usually categories are the ones with tags
    exclude = ['checkout.html']
    
    for filename in html_files:
        if filename in exclude:
            continue
            
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        if 'category-tags-row' not in content:
            continue

        # Find the tags row block
        # We also want to wrap the text in <span> for each tag-item if not already done
        pattern_row = r'(<div class="category-tags-row">.*?</div>)'
        match_row = re.search(pattern_row, content, re.DOTALL)
        
        if match_row:
            row_html = match_row.group(1)
            
            # Wrap text in span within tags
            # e.g. <div class="tag-icon">...</div> Promenade -> ... <span>Promenade</span>
            tags_pattern = r'(<a.*?class="tag-item".*?>\s*<div class="tag-icon">.*?</div>\s*)([^\s<].*?)(\s*</a>)'
            new_row_html = re.sub(tags_pattern, r'\1<span>\2</span>\3', row_html, flags=re.DOTALL)
            
            # Create the carousel wrapper
            carousel_wrapper = f"""
                <div class="category-carousel-wrapper">
                    <button class="carousel-nav prev" id="cat-prev" aria-label="Précédent">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"></polyline></svg>
                    </button>
                    <div class="category-carousel">
                        {new_row_html}
                    </div>
                    <button class="carousel-nav next" id="cat-next" aria-label="Suivant">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"></polyline></svg>
                    </button>
                </div>"""
            
            content = content.replace(row_html, carousel_wrapper)
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated carousel in {filename}")

if __name__ == "__main__":
    update_carousel_html()
