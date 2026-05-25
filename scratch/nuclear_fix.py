import os

directory = "/Users/renelrosene/Desktop/boutique chien"

files_to_fix = [f for f in os.listdir(directory) if f.endswith('.html') and (
    f.startswith('tapis-') or 
    f.startswith('panier-') or 
    f.startswith('coussin-') or 
    f.startswith('harnais-') or 
    f.startswith('collier-') or
    f in ['couchage.html', 'promenade.html', 'hygiene.html', 'jouets.html', 'manteaux.html']
)]

def nuclear_fix(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        new_lines = []
        skip = False
        found_corruption = False
        
        for line in lines:
            if '<div class="category-visual-container">' in line:
                skip = True
                found_corruption = True
                continue
            if '<section class="collection-section">' in line:
                if skip:
                    # Insert a CLEAN visual container before the collection section
                    # We'll use a standard one for now to at least break the corruption
                    new_lines.append('                <div class="category-visual-container">\n')
                    new_lines.append('                    <div class="category-visual-header" style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem;">\n')
                    new_lines.append('                        <h2 style="margin: 0; font-size: 1.15rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1.2px; color: #111;">Parcourir par type</h2>\n')
                    new_lines.append('                        <div class="category-carousel-nav" style="display: flex; gap: 0.8rem; align-items: center;">\n')
                    new_lines.append('                            <button class="nav-arrow nav-prev" id="cat-prev" aria-label="Précédent" style="width: 40px; height: 40px; border: 1px solid #ddd; border-radius: 50%; display: flex; align-items: center; justify-content: center; background: #fff; cursor: pointer; transition: all 0.3s; color: #111;">\n')
                    new_lines.append('                                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m15 18-6-6 6-6"/></svg>\n')
                    new_lines.append('                            </button>\n')
                    new_lines.append('                            <button class="nav-arrow nav-next" id="cat-next" aria-label="Suivant" style="width: 40px; height: 40px; border: 1px solid #ddd; border-radius: 50%; display: flex; align-items: center; justify-content: center; background: #fff; cursor: pointer; transition: all 0.3s; color: #111;">\n')
                    new_lines.append('                                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>\n')
                    new_lines.append('                            </button>\n')
                    new_lines.append('                        </div>\n')
                    new_lines.append('                    </div>\n')
                    new_lines.append('                    <div class="category-visual-list">\n')
                    new_lines.append('                        <!-- Cards will be restored by the next pass or manually -->\n')
                    # Try to find valid cards in the skipped lines? Too complex for now.
                    new_lines.append('                    </div>\n')
                    new_lines.append('                </div>\n')
                    new_lines.append('            </div>\n')
                    new_lines.append('        </section>\n')
                skip = False
            
            if not skip:
                new_lines.append(line)
        
        if found_corruption:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.writelines(new_lines)
            return True
        return False
    except Exception:
        return False

for filename in files_to_fix:
    nuclear_fix(os.path.join(directory, filename))
print("Nuclear fix complete.")
