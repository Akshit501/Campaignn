import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# We need to replace 4 occurrences of <div class="visual-mock" ...> ... </div>
# The visual-mock spans multiple lines because it contains an emoji.
# e.g.:
# <div class="visual-mock" style="background: radial-gradient(...)">
#   🛡️
# </div>

# Let's find them one by one
images = ['assets/images/team1.jpg', 'assets/images/team2.jpg', 'assets/images/team3.jpg', 'assets/images/team1.jpg'] # 4th card uses team1 again if only 3 were provided

for i in range(4):
    start_tag = '<div class="visual-mock"'
    idx_start = html.find(start_tag)
    
    if idx_start != -1:
        idx_end = html.find('</div>', idx_start) + len('</div>')
        
        old_block = html[idx_start:idx_end]
        # Replace the div with an img tag that behaves exactly the same but loads the photo
        # .visual-mock is typically styled as a block. We can just use a div with a background image,
        # or an img tag with object-fit: cover. A div with background image is safest so it matches exactly the bounds.
        new_block = f'<div class="visual-mock" style="background: url(\'{images[i]}\') center/cover no-repeat;"></div>'
        
        # Replace only the first occurrence found
        html = html[:idx_start] + new_block + html[idx_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Replaced visual-mocks with team photos!")
