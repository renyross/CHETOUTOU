import os

def restore_heads():
    # Only target files that were modified by the previous aggressive script
    html_files = [f for f in os.listdir('.') if f.endswith('.html') and f not in ['index.html', 'checkout.html']]
    
    count = 0
    for filename in html_files:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if '<head>' in content:
            continue
            
        # Generate title from filename
        name = filename.replace('.html', '').replace('-', ' ').title()
        if name == "Index": name = "Accueil"
        
        head = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} | Chetoutou</title>
    <meta name="description" content="Découvrez notre collection de {name} sur Chetoutou, la boutique premium d'accessoires pour chiens.">
    <!-- Styles -->
    <link rel="stylesheet" href="styles.css">
</head>
"""
        new_content = head + content
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1

    print(f"Restored heads for {count} files.")

if __name__ == "__main__":
    restore_heads()
