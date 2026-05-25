import os
import re

# Standardized pagination block to insert
PAGINATION_BLOCK = """
   <!-- Pagination Section -->
   <section class="collection-footer-elements">
    <div class="container">
     <nav aria-label="Pagination" class="collection-pagination">
      <a aria-label="Précédent" class="page-btn" href="#">
       <svg fill="none" stroke="currentColor" stroke-width="2" viewbox="0 0 24 24">
        <path d="m15 18-6-6 6-6">
        </path>
       </svg>
      </a>
      <a aria-current="page" class="page-btn active" href="#">
       1
      </a>
      <a class="page-btn" href="#">
       2
      </a>
      <a aria-label="Suivant" class="page-btn" href="#">
       <svg fill="none" stroke="currentColor" stroke-width="2" viewbox="0 0 24 24">
        <path d="m9 18 6-6-6-6">
        </path>
       </svg>
      </a>
     </nav>
    </div>
   </section>
"""

def fix_pagination(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Check if it's a collection page (has collection-grid)
    if 'collection-grid' not in content:
        return

    # 2. Check if it already has the standardized pagination
    if 'collection-pagination' in content:
        # If it has it but in a different format, we might want to update it.
        # For now, let's assume if it has the class, it's fine unless we find a specific old pattern.
        pass
    
    # 3. Look for old pagination patterns to replace
    # Pattern 1: <div class="pagination">...</div>
    content = re.sub(r'<!-- Pagination -->\s*<div class="pagination">.*?</div>', '', content, flags=re.DOTALL)
    content = re.sub(r'<div class="pagination">.*?</div>', '', content, flags=re.DOTALL)
    
    # Pattern 2: <section class="collection-footer-elements"> with old content
    # (Optional: remove existing one to re-insert clean)
    content = re.sub(r'<section class="collection-footer-elements">.*?</section>', '', content, flags=re.DOTALL)

    # 4. Find the end of collection-section and insert the new pagination
    # We look for the closing </section> of the collection-section
    # The collection section usually contains the collection-grid.
    
    # Let's find the closing tag of the section containing collection-grid
    parts = re.split(r'(<section class="collection-section">.*?</section>)', content, flags=re.DOTALL)
    
    if len(parts) > 1:
        new_content = ""
        for part in parts:
            new_content += part
            if 'class="collection-section"' in part:
                new_content += PAGINATION_BLOCK
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated pagination in {file_path}")

def main():
    files = [f for f in os.listdir('.') if f.endswith('.html')]
    for f in files:
        fix_pagination(f)

if __name__ == "__main__":
    main()
