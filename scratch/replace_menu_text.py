import os

directory = "/Users/renelrosene/Desktop/boutique chien"
target_text = '<li><a href="tapis-fouille.html">Tapis de fouille Chien</a></li>'
replacement_text = '<li><a href="tapis-fouille.html">jouet d’occupation chien</a></li>'

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if target_text in content:
            new_content = content.replace(target_text, replacement_text)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
