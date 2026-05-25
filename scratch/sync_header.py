import os

def sync_header():
    # 1. Get the reference header from index.html
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract announcement bar
    start_ann = content.find('<div class="announcement-bar">')
    end_ann = content.find('</div>', content.find('</div>', content.find('</div>', start_ann) + 1) + 1) + 6
    # Robust extraction: look for the next major tag like <header
    end_ann_robust = content.find('<header', start_ann)
    announcement_html = content[start_ann:end_ann_robust].strip()
    
    # Extract header (navbar)
    start_nav = content.find('<header class="navbar">')
    end_nav = content.find('</header>', start_nav) + 9
    header_html = content[start_nav:end_nav].strip()
    
    if not header_html:
        print("Could not find header in index.html")
        return

    # List all html files
    html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'index.html']
    
    for filename in html_files:
        with open(filename, 'r', encoding='utf-8') as f:
            file_content = f.read()
            
        # Replace announcement bar
        start_ann_target = file_content.find('<div class="announcement-bar">')
        if start_ann_target != -1:
            end_ann_target = file_content.find('<header', start_ann_target)
            if end_ann_target != -1:
                file_content = file_content[:start_ann_target] + announcement_html + "\n    " + file_content[end_ann_target:]

        # Replace header
        # Find any header starting with <header class="navbar
        start_nav_target = file_content.find('<header class="navbar')
        if start_nav_target != -1:
            end_nav_target = file_content.find('</header>', start_nav_target)
            if end_nav_target != -1:
                end_nav_target += 9
                
                # Prepare replacement header
                target_header_html = header_html.replace('class="navbar"', 'class="navbar scrolled"')
                target_header_html = target_header_html.replace('class="nav-link active"', 'class="nav-link"')
                
                # Add active class based on filename
                if filename == 'promenade.html':
                    target_header_html = target_header_html.replace('href="promenade.html" class="nav-link"', 'href="promenade.html" class="nav-link active"')
                elif filename == 'panier-chien.html':
                    target_header_html = target_header_html.replace('href="panier-chien.html" class="nav-link"', 'href="panier-chien.html" class="nav-link active"')
                elif filename == 'jouets.html':
                    target_header_html = target_header_html.replace('href="jouets.html" class="nav-link"', 'href="jouets.html" class="nav-link active"')
                elif filename == 'hygiene.html':
                    target_header_html = target_header_html.replace('href="hygiene.html" class="nav-link"', 'href="hygiene.html" class="nav-link active"')
                elif filename == 'blog.html' or filename.startswith('article-'):
                    target_header_html = target_header_html.replace('href="blog.html" class="nav-link"', 'href="blog.html" class="nav-link active"')

                file_content = file_content[:start_nav_target] + target_header_html + file_content[end_nav_target:]

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(file_content)
        print(f"Updated {filename}")

if __name__ == "__main__":
    sync_header()
