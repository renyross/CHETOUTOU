import os

directory = "/Users/renelrosene/Desktop/boutique chien"

# Donor file
donor_path = os.path.join(directory, "accessoires.html")
with open(donor_path, 'r', encoding='utf-8') as f:
    donor_content = f.read()

# Extract the donor bottom (from collection-section to end)
donor_parts = donor_content.split('<section class="collection-section">')
if len(donor_parts) > 1:
    donor_bottom = '<section class="collection-section">' + donor_parts[1]
else:
    donor_bottom = ""

files_to_restore = [f for f in os.listdir(directory) if f.endswith('.html') and (
    f.startswith('tapis-') or 
    f.startswith('panier-') or 
    f.startswith('coussin-') or 
    f.startswith('harnais-') or 
    f.startswith('collier-') or
    f in ['couchage.html', 'promenade.html', 'hygiene.html', 'jouets.html', 'manteaux.html']
)]

def restore_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # If the file is truncated (missing the footer or main tags)
        if '</html>' not in content or 'footer' not in content:
            # We assume it ends at line 355 or similar
            # Let's find the last valid line (likely after intro-large)
            parts = content.split('<div class="intro-large">')
            if len(parts) > 1:
                # Keep the top part
                top = parts[0] + '<div class="intro-large">' + parts[1].split('</div>')[0] + '</div>\n'
                
                # Re-insert the visual carousel (clean version)
                visual_block = """
                <div class="category-visual-container">
                    <div class="category-visual-header" style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem;">
                        <h2 style="margin: 0; font-size: 1.15rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1.2px; color: #111;">Parcourir par type</h2>
                        <div class="category-carousel-nav" style="display: flex; gap: 0.8rem; align-items: center;">
                            <button class="nav-arrow nav-prev" id="cat-prev" aria-label="Précédent" style="width: 40px; height: 40px; border: 1px solid #ddd; border-radius: 50%; display: flex; align-items: center; justify-content: center; background: #fff; cursor: pointer; transition: all 0.3s; color: #111;">
                                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m15 18-6-6 6-6"/></svg>
                            </button>
                            <button class="nav-arrow nav-next" id="cat-next" aria-label="Suivant" style="width: 40px; height: 40px; border: 1px solid #ddd; border-radius: 50%; display: flex; align-items: center; justify-content: center; background: #fff; cursor: pointer; transition: all 0.3s; color: #111;">
                                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>
                            </button>
                        </div>
                    </div>
                    <div class="category-visual-list">
                        <!-- Items will be populated -->
                    </div>
                </div>
            </div>
        </section>
"""
                new_content = top + visual_block + donor_bottom
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                return True
        return False
    except Exception:
        return False

count = 0
for filename in files_to_restore:
    if restore_file(os.path.join(directory, filename)):
        count += 1
print(f"Restored {count} files with donor bottom.")
