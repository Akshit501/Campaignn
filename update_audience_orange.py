import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove the source text div entirely
source_div_pattern = r'<div style="text-align: center; margin-top: 24px;">\s*<span class="audience-source"[^>]*>\* Source: internal analytics, previous edition registrations</span>\s*</div>'
html = re.sub(source_div_pattern, '', html)

# 2. Change the background of the cards from #0F172A to an Orange color
# I'll use a premium deep orange/coral gradient to make it look highly aesthetic
html = html.replace('background: #0F172A;', 'background: linear-gradient(135deg, #f97316 0%, #ea580c 100%);')

# 3. I should also change the title accent colors inside the orange card, because pink (`var(--primary-light)`) on orange might clash.
# I'll change `color: var(--primary-light);` to `color: #fff;` or `color: #FFEEDD;` for those specific cards.
# Wait, it's safer to just change it in the audience-col block.
audience_col_pattern = r'<h3 class="audience-title" style="color: var\(--primary-light\);'
html = re.sub(audience_col_pattern, '<h3 class="audience-title" style="color: #fff;', html)

# Also the dt/dd numbers which were var(--primary-light):
html = html.replace('color: var(--primary-light);', 'color: #fff;')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
