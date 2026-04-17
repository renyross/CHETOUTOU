import os
import re

# Regex to match the Google Fonts block
font_block_regex = re.compile(r'<!-- Fonts -->.*?<link rel="preconnect" href="https://fonts\.googleapis\.com">.*?<link rel="preconnect" href="https://fonts\.gstatic\.com" crossorigin>.*?<link\s+href="https://fonts\.googleapis\.com/css2\?family=Inter:wght@300;400;600&family=Playfair\+Display:ital,wght@0,400;0,700;1,400&display=swap"\s+rel="stylesheet">', re.DOTALL)

for filename in os.listdir('.'):
    if filename.endswith('.html'):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove the block if found
        new_content = font_block_regex.sub('', content)
        
        if new_content != content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Removed Google Fonts from {filename}")
        else:
            # Try a slightly more flexible regex if the exact match fails
            flex_regex = re.compile(r'<link rel="preconnect" href="https://fonts\.googleapis\.com">.*?<link rel="preconnect" href="https://fonts\.gstatic\.com" crossorigin>.*?<link.*?fonts\.googleapis\.com/css2.*?family=Inter.*?family=Playfair.*?rel="stylesheet">', re.DOTALL)
            new_content = flex_regex.sub('', content)
            if new_content != content:
                 with open(filename, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                 print(f"Removed Google Fonts (flexible match) from {filename}")
