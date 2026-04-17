import os
import re

def cleanup_seo():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    for filename in html_files:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Fix the top section: seo-page-section
        # We want: <section> <div container> breadcrumb, h1, category-tags-row </div> </section>
        # Currently it has extra </div>
        
        # Regex to match the top section and normalize it
        pattern = r'(<section class="seo-page-section">.*?</section>)'
        match = re.search(pattern, content, re.DOTALL)
        if match:
            old_section = match.group(1)
            
            # Extract essential parts
            breadcrumb = re.search(r'(<div class="breadcrumb">.*?</div>)', old_section, re.DOTALL)
            h1 = re.search(r'(<h1>.*?</h1>)', old_section, re.DOTALL)
            # Use a more greedy match for tags to get all <a> items within the row
            tags = re.search(r'(<div class="category-tags-row">.*?</div>\s*</div>)', old_section, re.DOTALL)
            if not tags:
                # Fallback if the structure is slightly different
                tags = re.search(r'(<div class="category-tags-row">.*?</div>)', old_section, re.DOTALL)
            
            if breadcrumb and h1:
                tags_html = tags.group(1) if tags else ""
                new_section = f"""<section class="seo-page-section">
            <div class="container text-content">
                {breadcrumb.group(1)}
                {h1.group(1)}
                {tags_html}
            </div>
        </section>"""
                content = content.replace(old_section, new_section)

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Cleaned {filename}")

if __name__ == "__main__":
    cleanup_seo()
