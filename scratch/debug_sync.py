import re
with open('tapis-chien.html', 'r', encoding='utf-8') as f:
    content = f.read()
    match = re.search(r'(<div class="announcement-bar".*?</header>)', content, re.DOTALL)
    if match:
        print("Source header found")
    else:
        print("Source header NOT found")
        # Print a bit of content to see why
        print(content[:500])
