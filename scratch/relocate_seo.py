import os
import re

def relocate_seo():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    for filename in html_files:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find the seo-page-section
        seo_section_match = re.search(r'(<section class="seo-page-section">.*?</section>)', content, re.DOTALL)
        if not seo_section_match:
            continue
            
        seo_section = seo_section_match.group(1)
        
        # Extract the parts we want to move
        # We want to move everything inside seo-page-section EXCEPT breadcrumb and h1
        # But wait, looking at the user's request, they might want the title moved too.
        # I'll stick to moving Intro + Body.
        
        intro_match = re.search(r'(<div class="intro-large">.*?</div>)', seo_section, re.DOTALL)
        body_match = re.search(r'(<div class="seo-body.*?">.*?</div>)', seo_section, re.DOTALL)
        
        if not (intro_match and body_match):
            continue
            
        intro_html = intro_match.group(1)
        body_html = body_match.group(1)
        
        # Remove these from the top section
        new_top_seo = seo_section
        new_top_seo = new_top_seo.replace(intro_html, "")
        new_top_seo = new_top_seo.replace(body_html, "")
            
        # Clean up empty space in top section
        new_top_seo = re.sub(r'\n\s*\n', '\n', new_top_seo)
        
        # Create the bottom section
        bottom_seo = f"""
        <!-- SEO Content Bottom -->
        <section class="seo-bottom-content">
            <div class="container text-content">
                {intro_html}
                {body_html}
            </div>
        </section>
"""
        
        # Replace the top section in the main content
        content = content.replace(seo_section, new_top_seo)
        
        # Insert bottom section before unified-newsletter or fallback before footer
        if '<section class="unified-newsletter">' in content:
            content = content.replace('<section class="unified-newsletter">', bottom_seo + '\n        <section class="unified-newsletter">')
        elif '<!-- Unified Newsletter Section' in content:
             content = content.replace('<!-- Unified Newsletter Section', bottom_seo + '\n        <!-- Unified Newsletter Section')
        elif '<footer' in content:
            content = content.replace('<footer', bottom_seo + '\n    <footer')
        else:
            content = content.replace('</main>', bottom_seo + '\n    </main>')

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")

if __name__ == "__main__":
    relocate_seo()
