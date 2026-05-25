import os
import re

target_dir = "/Users/renelrosene/Desktop/boutique chien"

old_script_pattern = re.compile(r"// Visual Carousel\s+const track = document\.getElementById\('visual-track'\);\s+const nextBtn = document\.getElementById\('visual-next'\);\s+const prevBtn = document\.getElementById\('visual-prev'\);\s+if\(track && nextBtn && prevBtn\) \{[\s\S]+?\}\s+\}", re.MULTILINE)

new_script = """// Visual Carousel
        const visualTrackContainer = document.querySelector('.visual-carousel-track-container');
        const visualNextBtn = document.getElementById('visual-next');
        const visualPrevBtn = document.getElementById('visual-prev');
        
        if(visualTrackContainer && visualNextBtn && visualPrevBtn) {
            visualNextBtn.addEventListener('click', () => {
                visualTrackContainer.scrollBy({ left: 300, behavior: 'smooth' });
            });
            visualPrevBtn.addEventListener('click', () => {
                visualTrackContainer.scrollBy({ left: -300, behavior: 'smooth' });
            });
        }"""

for root, dirs, files in os.walk(target_dir):
    for file in files:
        if file.endswith(".html"):
            path = os.path.join(root, file)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            
            if "visual-track" in content:
                print(f"Updating carousel JS in {file}")
                # Simple replacement since the pattern might vary slightly
                # Actually, I'll just look for the specific block
                start_tag = "// Visual Carousel"
                if start_tag in content:
                    # Find the block and replace it
                    # Let's use a more robust search
                    try:
                        updated_content = old_script_pattern.sub(new_script, content)
                        if updated_content != content:
                            with open(path, "w", encoding="utf-8") as f:
                                f.write(updated_content)
                        else:
                            # If regex fails, do a manual search and replace
                            print(f"Regex failed for {file}, attempting manual fix")
                            # Manual fix logic if needed
                    except Exception as e:
                        print(f"Error processing {file}: {e}")
