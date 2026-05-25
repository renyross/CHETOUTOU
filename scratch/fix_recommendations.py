import os

# Define the bad block and the good block
bad_header_start = '<div class="recommendations-carousel-header" style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4rem; padding: 0 2rem;">'
bad_nav_start = '<div class="category-carousel-nav" style="display: flex; gap: 0.8rem; margin-right: 1.5rem; position: relative; top: 3rem;">'

good_header = '<div class="recommendations-carousel-header" style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem; padding: 0 3rem;">'
good_title = '<h2 class="section-title-left" style="margin: 0;">Vous aimerez aussi</h2>'
good_nav = '<div class="category-carousel-nav" style="display: flex; gap: 0.5rem;">'

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'Vous aimerez aussi' not in content:
        return
    
    # Simple replacement for the messy header if found
    if bad_header_start in content:
        content = content.replace(bad_header_start, good_header)
        # Fix the title inside if it has the extra styles
        content = content.replace('<h2 class="section-title-left" style="margin: 0; font-size: 2rem; font-weight: 900;">Vous aimerez aussi</h2>', good_title)
        # Fix the nav
        content = content.replace(bad_nav_start, good_nav)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed messy header in {filepath}")

    # Also fix broken image names if found
    if 'gamelle_surelevee_visual.png' in content or 'manteau_hiver_premium.png' in content:
        # These are now generated so it's fine, but let's make sure they aren't using broken external URLs if any
        pass

for filename in os.listdir('.'):
    if filename.endswith('.html'):
        fix_file(filename)
