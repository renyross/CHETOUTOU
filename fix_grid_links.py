
import os
import re

def fix_links_in_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the collection-grid content
    grid_match = re.search(r'<div class="collection-grid">(.*?)</div>\s*</div>\s*</section>', content, re.DOTALL)
    if not grid_match:
        # Try a more flexible search for collection-grid
        grid_match = re.search(r'<div class="collection-grid">(.*?)</div>', content, re.DOTALL)
        if not grid_match:
            return

    grid_content = grid_match.group(1)
    new_grid_content = grid_content

    # Regex to find product-item content correctly
    # We match <div class="product-item"> and then anything until the next <!-- Product or <div class="product-item"
    # and we assume the last </div> before that is the end of the product-item.
    
    # Actually, let's use a simpler approach for these specific files:
    # Match <div class="product-item"> ... product-info ... </div>
    
    # Let's try to match each product-item individually
    items = re.split(r'(<!-- Product \d+ -->|<div class="product-item">)', grid_content)
    
    # The split will give us [prefix, tag, content, tag, content, ...]
    fixed_items = []
    i = 0
    while i < len(items):
        if items[i] == '<div class="product-item">':
            # This is the start of an item
            # The content is in items[i+1]
            if i + 1 < len(items):
                item_inner = items[i+1]
                # Check if it already has a link
                if 'product-link-wrapper' not in item_inner and 'product-link-block' not in item_inner:
                    # Guess link
                    link = "produit-detail.html"
                    if "harnais" in item_inner.lower():
                        link = "harnais-anti-traction-chien.html"
                    elif "collier" in item_inner.lower() and "collier-cuir" in item_inner.lower():
                        link = "collier-cuir-chien.html"
                    elif "collier" in item_inner.lower():
                        link = "collier-chien.html"
                    
                    # Find the last closing </div> in item_inner
                    last_div_index = item_inner.rfind('</div>')
                    if last_div_index != -1:
                        # Wrap everything BEFORE the last </div>
                        item_inner = f'<a class="product-link-wrapper" href="{link}">{item_inner[:last_div_index]}</a>{item_inner[last_div_index:]}'
                
                fixed_items.append(f'<div class="product-item">{item_inner}')
                i += 2
            else:
                fixed_items.append(items[i])
                i += 1
        else:
            fixed_items.append(items[i])
            i += 1
            
    new_grid_content = "".join(fixed_items)
    
    if new_grid_content != grid_content:
        new_content = content.replace(grid_content, new_grid_content)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed links in {filename}")

def main():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    for f in html_files:
        fix_links_in_file(f)

if __name__ == "__main__":
    main()
