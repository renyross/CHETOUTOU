import sys

file_path = "produit-impermeable.html"
with open(file_path, "r") as f:
    lines = f.readlines()

reviews_start = -1
faq_start = -1
newsletter_start = -1

for i, line in enumerate(lines):
    if "<!-- Reviews Section -->" in line and reviews_start == -1:
        reviews_start = i
    if "<!-- Technical FAQ Section -->" in line and faq_start == -1:
        faq_start = i
    if "<!-- Unified Newsletter Section" in line and newsletter_start == -1:
        newsletter_start = i

print(f"Reviews start: {reviews_start}")
print(f"FAQ start: {faq_start}")
print(f"Newsletter start: {newsletter_start}")

if reviews_start != -1 and faq_start != -1 and newsletter_start != -1:
    new_lines = lines[:reviews_start] + lines[faq_start:newsletter_start] + lines[reviews_start:faq_start] + lines[newsletter_start:]
    with open(file_path, "w") as f:
        f.writelines(new_lines)
    print("Swapped successfully.")
else:
    print("Could not find all sections.")
