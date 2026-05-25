import os
import re

directory = "/Users/renelrosene/Desktop/boutique chien"
files = [
    "tapis-fouille.html",
    "tapis-lechage.html",
    "tapis-absorbant-chien.html",
    "tapis-xxl-chien.html",
    "tapis-gamelle-chien.html",
    "tapis-fraicheur-chien.html",
    "tapis-refrigerant-chien.html"
]

# The pattern to look for is the end of the first carousel followed by orphaned category-visual-info/cards
# We want to keep everything up to the first </div> that closes the category-visual-list, 
# then the </div> that closes category-visual-container, 
# then the </div> that closes container text-content,
# then the </section> that closes seo-page-section.

def clean_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Look for the visual list start
    list_start_idx = content.find('<div class="category-visual-list" id="cat-carousel">')
    if list_start_idx == -1:
        # Try without ID if needed, but they should have it
        list_start_idx = content.find('<div class="category-visual-list">')
    
    if list_start_idx == -1:
        print(f"Could not find carousel list in {filepath}")
        return

    # Find the end of this list (the first </div> after the start)
    # Actually, the list has many <a> tags inside.
    # The structure we want is:
    # <div class="category-visual-list" ...>
    #    ... cards ...
    # </div> <!-- This one closes the list -->
    
    # Let's find the 9th </a> (since there are 9 categories) and then the next </div>
    links = list(re.finditer('</a>', content[list_start_idx:]))
    if len(links) < 9:
        print(f"Not enough links in {filepath}")
        return
    
    ninth_link_end = list_start_idx + links[8].end()
    list_end_div_idx = content.find('</div>', ninth_link_end)
    
    if list_end_div_idx == -1:
        print(f"Could not find list end in {filepath}")
        return
    
    list_end_div_full = list_end_div_idx + 6
    
    # Now we want to find where the NEXT section starts
    next_section_idx = content.find('<section class="collection-section">', list_end_div_full)
    
    if next_section_idx == -1:
        print(f"Could not find next section in {filepath}")
        return

    # The content between list_end_div_full and next_section_idx should only contain 3 closing tags:
    # </div> (closes container)
    # </div> (closes seo-page-section inner) - wait, let's check structure
    
    # Correct structure from tapis-chien.html:
    # 365:                     <div class="category-visual-list" id="cat-carousel">
    # ...
    # 402:                     </div>
    # 403:                 </div>
    # 404:             </div>
    # 405:         </section>
    # 406: 
    # 407:         <section class="collection-section">
    
    replacement_block = "\n                </div>\n            </div>\n        </section>\n\n        "
    
    new_content = content[:list_end_div_full] + replacement_block + content[next_section_idx:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Cleaned {filepath}")

for filename in files:
    clean_file(os.path.join(directory, filename))
