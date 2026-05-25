import os
import re

def heal_site():
    # 1. Donor file (faq.html is currently the most 'complete' and stable)
    try:
        with open('faq.html', 'r', encoding='utf-8') as f:
            donor_content = f.read()
    except FileNotFoundError:
        print("faq.html not found. Using panier-chien.html.")
        with open('panier-chien.html', 'r', encoding='utf-8') as f:
            donor_content = f.read()

    # Clean the donor content from garbage first
    donor_content = donor_content.replace('<!DOC', '')
    donor_content = donor_content.replace('TYPE html>', '')

    # Extract Master Components
    header_match = re.search(r'(<div class="announcement-bar">.*?</header>)', donor_content, re.DOTALL)
    master_header = header_match.group(1)

    footer_match = re.search(r'(<footer.*</footer>)', donor_content, re.DOTALL)
    master_footer = footer_match.group(1)

    # Generic head from donor
    head_match = re.search(r'(<head>.*?</head>)', donor_content, re.DOTALL)
    master_head = head_match.group(1)

    # 2. List target files
    html_files = [f for f in os.listdir('.') if f.endswith('.html') and f not in ['checkout.html']]
    
    count = 0
    for filename in html_files:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract Title
        title_match = re.search(r'<title>(.*?)</title>', content)
        if title_match:
            title = title_match.group(1)
        else:
            name = filename.replace('.html', '').replace('-', ' ').title()
            title = f"{name} | Chetoutou"

        # Extract Main Content
        main_match = re.search(r'<main>(.*?)</main>', content, re.DOTALL)
        if main_match:
            main_content = main_match.group(1)
        else:
            # If <main> is missing (like in index.html right now), try to find anything between the old header/footer
            # or just leave it for manual restoration if it's index.html
            if filename == 'index.html':
                main_content = "<!-- HOMEPAGE_PLACEHOLDER -->"
            else:
                # Fallback: take everything after the first </header> and before the first <footer
                parts = re.split(r'</header>|<footer', content)
                if len(parts) > 1:
                    main_content = parts[1]
                else:
                    main_content = "<h2>Contenu en cours de restauration</h2>"

        # Rebuild file structure
        current_head = master_head
        if title:
            current_head = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', current_head)

        new_content = f"""<!DOCTYPE html>
<html lang="fr">
{current_head}
<body class="{"homepage" if filename == "index.html" else "shop-page"}">
    {master_header}
    <main>
        {main_content}
    </main>
    {master_footer}
    <script src="main.js"></script>
</body>
</html>"""
        
        # Final scrub of common corruption patterns
        new_content = new_content.replace('<!DOC', '')
        new_content = new_content.replace('TYPE html>', '')

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1

    print(f"Healed and synchronized {count} files.")

if __name__ == "__main__":
    heal_site()
