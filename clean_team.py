
with open('index.html', 'r') as f:
    content = f.read()

# Find start of the orphan: the old grid wrapper div that follows the new </section>
# The new section ends with </section>\n\n\n and then the orphan starts with a <div class="max-w-screen-xl...
# We need to find and remove it

# The orphan starts after the doubled </section> and ends before <!-- Editorial Section -->
import re

# Find the orphan block: a stray <div class="max-w-screen-xl... that is NOT inside a <section>
# Pattern: after </section>\n\n  <div class="max-w-screen-xl...up to </section>
pattern = r'(</section>\n)\n\n  <div class="max-w-screen-xl mx-auto grid grid-cols-1 lg:grid-cols-12 gap-16 items-center">.*?</section>\n'
new_content = re.sub(pattern, r'\1\n', content, flags=re.DOTALL)

if new_content != content:
    with open('index.html', 'w') as f:
        f.write(new_content)
    print("Cleaned! Orphan block removed.")
else:
    print("Pattern not found, trying manual line removal...")
    lines = content.split('\n')
    # find line with the orphan div
    start_idx = None
    end_idx = None
    for i, line in enumerate(lines):
        if start_idx is None and 'max-w-screen-xl mx-auto grid grid-cols-1 lg:grid-cols-12 gap-16 items-center' in line:
            # check if this is inside a section tag
            # look back 5 lines to see if there's a <section
            context = '\n'.join(lines[max(0,i-5):i])
            if '<section' not in context:
                start_idx = i - 1  # include the blank line before
                print(f"Found orphan div at line {i+1}")
        if start_idx is not None and end_idx is None and i > start_idx:
            if '</section>' in line:
                end_idx = i
                print(f"Found orphan end at line {i+1}: {line}")
                break
    
    if start_idx is not None and end_idx is not None:
        new_lines = lines[:start_idx] + lines[end_idx+1:]
        with open('index.html', 'w') as f:
            f.write('\n'.join(new_lines))
        print(f"Removed lines {start_idx+1} to {end_idx+1}")
    else:
        print(f"Could not find bounds: start={start_idx}, end={end_idx}")
