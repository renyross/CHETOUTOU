with open('styles.css', 'r', encoding='utf-8') as f:
    content = f.read()

line_num = 1
col_num = 1
stack = []
in_comment = False

for i, char in enumerate(content):
    if char == '\n':
        line_num += 1
        col_num = 1
    else:
        col_num += 1

    if in_comment:
        if content[i:i+2] == '*/':
            in_comment = False
        continue
    
    if content[i:i+2] == '/*':
        in_comment = True
        continue
        
    if char == '{':
        stack.append((line_num, col_num, char))
    elif char == '}':
        if not stack:
            print(f"Extra closing brace '}}' at line {line_num}, column {col_num}")
        else:
            stack.pop()

if stack:
    print(f"Found {len(stack)} unclosed opening braces. Unclosed ones starting at:")
    for item in stack[-10:]:
        print(f"  Line {item[0]}, Column {item[1]}")
else:
    print("No unclosed braces found! CSS braces are syntax-clean.")
