import os

def update_megamenu():
    target_dir = "/Users/renelrosene/Desktop/boutique chien"
    search_text = '<li><a href="couverture-chien.html">Couvertures Chien</a></li>'
    new_text = '<li><a href="couverture-chien.html">Couvertures Chien</a></li>\n                                            <li><a href="protection-canape-chien.html">Protection canapé chien</a></li>'
    
    files_updated = 0
    
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    if search_text in content:
                        new_content = content.replace(search_text, new_text)
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        files_updated += 1
                        print(f"Updated: {file}")
                except Exception as e:
                    print(f"Error processing {file}: {e}")
                    
    print(f"\nTotal files updated: {files_updated}")

if __name__ == "__main__":
    update_megamenu()
