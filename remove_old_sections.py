with open('index.html', 'r') as f:
    lines = f.readlines()

# Find the start of the old orphan block: "<!-- Section: Team -->" that comes after line 700
# and the end: the line just before "<!-- Section: Team -->" for the NEW team section
# We know from the view that:
#   line 707 (index 706): <!-- Section: Team -->  <-- OLD, to remove
#   ...
#   line 993 (index 992): </section>              <-- end of old Lab "Sanctity" section
#   line 994 (index 993): (blank)
#   line 995 (index 994): <!-- Section: Team -->  <-- NEW (the good one)

# Strategy: find line indices
old_team_start = None
new_team_start = None

for i, line in enumerate(lines):
    stripped = line.strip()
    if stripped == '<!-- Section: Team -->' or stripped == '<!-- Section: Team  -->':
        if old_team_start is None:
            old_team_start = i
            print(f"Found OLD team comment at line {i+1}: {line.rstrip()}")
        else:
            new_team_start = i
            print(f"Found NEW team comment at line {i+1}: {line.rstrip()}")
            break

if old_team_start is not None and new_team_start is not None:
    # Remove lines from old_team_start up to (not including) new_team_start
    # Also remove the blank line right before new_team_start if it exists
    # Find the first blank/comment before new_team_start to include in deletion
    cut_end = new_team_start
    # walk back to include trailing blank lines that belong to the old block
    while cut_end > old_team_start and lines[cut_end-1].strip() == '':
        cut_end -= 1
    cut_end += 1  # include blank line

    new_lines = lines[:old_team_start] + lines[new_team_start:]
    with open('index.html', 'w') as f:
        f.writelines(new_lines)
    print(f"Removed lines {old_team_start+1} to {new_team_start} ({new_team_start - old_team_start} lines deleted)")
else:
    print(f"ERROR: Could not find both markers. old={old_team_start}, new={new_team_start}")
    # Print lines around 700 for debugging
    for i in range(700, min(720, len(lines))):
        print(f"{i+1}: {lines[i].rstrip()}")
