import os

files = [
    'blog.html',
    'article-marche-liberte.html',
    'article-adaptation-ville.html',
    'article-sommeil-chien.html',
    'article-alimentation-flair.html'
]

outfit_link = '<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">'

for filename in files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = content.replace(outfit_link, '')
        
        if new_content != content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Removed Outfit font from {filename}")
        else:
            print(f"Outfit font not found in {filename}")
