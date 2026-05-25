import os
import re

def heal_site():
    # 1. Donor Components (cleaned)
    with open('faq.html', 'r', encoding='utf-8') as f:
        donor_content = f.read()

    # Extract clean Header and Footer
    header_match = re.search(r'(<div class="announcement-bar">.*?</header>)', donor_content, re.DOTALL)
    master_header = header_match.group(1)

    footer_match = re.search(r'(<footer.*</footer>)', donor_content, re.DOTALL)
    master_footer = footer_match.group(1)

    html_files = [f for f in os.listdir('.') if f.endswith('.html') and f not in ['checkout.html', 'index.html']]
    
    count = 0
    for filename in html_files:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract Title
        title_match = re.search(r'<title>(.*?)</title>', content)
        title = title_match.group(1) if title_match else filename.replace('.html', '').replace('-', ' ').title() + " | Chetoutou"

        # Extract Main
        main_match = re.search(r'<main>(.*?)</main>', content, re.DOTALL)
        main_content = main_match.group(1) if main_match else "<h2>Contenu en cours de restauration</h2>"

        # Construct new page
        new_content = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="Découvrez la collection {title.split('|')[0].strip()} sur Chetoutou, votre boutique premium d'accessoires pour chiens.">
    <link rel="stylesheet" href="styles.css">
</head>
<body class="shop-page">
    {master_header}
    <main>
        {main_content}
    </main>
    {master_footer}
    <script src="main.js"></script>
</body>
</html>"""
        
        # Final cleanup of any potential leftover garbage
        new_content = new_content.replace('<!DOC', '')
        new_content = new_content.replace('TYPE html>', '')

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1

    print(f"Healed {count} files with v3 script.")

if __name__ == "__main__":
    heal_site()
