import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

images = ['assets/images/team1.jpg', 'assets/images/team2.jpg', 'assets/images/team3.jpg', 'assets/images/team1.jpg']

# Let's find them properly by searching from the last found index
pos = 0
for i in range(4):
    start_tag = '<div class="visual-mock"'
    # We must only replace the original ones with emoji/gradient.
    # The originals have `style="background: radial-gradient`
    idx_start = html.find('style="background: radial-gradient', pos)
    if idx_start != -1:
        # Move back to the start of the div
        div_start = html.rfind('<div class="visual-mock"', pos, idx_start)
        div_end = html.find('</div>', idx_start) + len('</div>')
        
        old_block = html[div_start:div_end]
        new_block = f'<div class="visual-mock" style="background: url(\'{images[i+1 if i < 3 else 0]}\') center/cover no-repeat;"></div>'
        
        html = html[:div_start] + new_block + html[div_end:]
        pos = div_start + len(new_block)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Replaced all visual-mocks correctly!")
