import os
import re

def fix_navbar(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern to find the Accessoires megamenu closing tags with the extra div
    # We look for the part after "Médailles & Sécurité"
    pattern = r'(Médailles & Sécurité</a>\s*</li>\s*</ul>\s*</div>\s*</div>\s*)(</div>)(\s*</div>\s*</div>\s*</div>)'
    
    # Let's try a more robust pattern based on the observed structure
    # The structure has:
    # </div> (column)
    # </div> (grid)
    # </div> (EXTRA)
    # </div> (container)
    # </div> (megamenu)
    # </div> (nav-item)
    
    # We want to remove one </div> from a sequence of many </div>s that close the megamenu
    
    # Finding the Accessoires section
    if "Accessoires" in content and "Médailles & Sécurité" in content:
        # This regex looks for the specific sequence of 6 closing divs instead of 5
        # between the last link and the Blog section/nav end.
        
        # Original sequence:
        # </div> (col)
        # </div> (grid)
        # </div> (EXTRA)
        # </div> (container)
        # </div> (megamenu)
        # </div> (nav-item)
        
        new_content = re.sub(
            r'(<div class="megamenu-column">[^<]*<h3>Sécurité</h3>.*?</ul>\s*</div>\s*</div>)\s*</div>(\s*</div>\s*</div>\s*</div>)',
            r'\1\2',
            content,
            flags=re.DOTALL
        )
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
    return False

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
fixed_count = 0
for html_file in html_files:
    if fix_navbar(html_file):
        print(f"Fixed {html_file}")
        fixed_count += 1

print(f"Total files fixed: {fixed_count}")
