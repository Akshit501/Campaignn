import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Change section background to orange gradient
# It currently has: style="background: var(--bg-deep); border-top: ...
html = re.sub(
    r'<section id="audience" class="section-pad" style="background: var\(--bg-deep\);',
    r'<section id="audience" class="section-pad" style="background: linear-gradient(135deg, #f97316 0%, #ea580c 100%);',
    html
)

# 2. Change title and description to white so it's readable on orange
html = html.replace(
    '<h2 class="section-title" style="color: var(--text-highlight);">Who Sees Your Brand</h2>',
    '<h2 class="section-title" style="color: #fff;">Who Sees Your Brand</h2>'
)
html = html.replace(
    '<p class="section-desc" style="color: var(--text-muted);">The Economic Times audience',
    '<p class="section-desc" style="color: rgba(255,255,255,0.9);">The Economic Times audience'
)

# 3. Revert playcards background to dark slate
html = html.replace(
    'background: linear-gradient(135deg, #f97316 0%, #ea580c 100%); padding: 32px; border-radius: 16px;',
    'background: #0F172A; padding: 32px; border-radius: 16px;'
)

# (The text inside the playcards was already set to white in the last step, which works perfectly on #0F172A)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
