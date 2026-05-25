import os

directory = "/Users/renelrosene/Desktop/boutique chien"
duplicate_text = '<li><a href="jouet-occupation-chien.html">Jouet d\'occupation chien</a></li>'

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        new_lines = []
        skip_next = False
        for line in lines:
            if duplicate_text in line:
                print(f"Removed duplicate in {filename}")
                continue
            new_lines.append(line)
        
        if len(new_lines) != len(lines):
            with open(filepath, 'w', encoding='utf-8') as f:
                f.writelines(new_lines)
