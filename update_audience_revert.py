import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Change the section background to light (cream)
html = html.replace(
    '<section id="audience" class="section-pad" style="background: #0F172A; color: #fff; border-top: 1px solid rgba(255,255,255,0.1); border-bottom: 1px solid rgba(255,255,255,0.1);">',
    '<section id="audience" class="section-pad" style="background: var(--bg-deep); border-top: 1px solid var(--border-subtle); border-bottom: 1px solid var(--border-subtle);">'
)

# Change the section title and description to dark text
html = html.replace(
    '<h2 class="section-title" style="color: #fff;">Who Sees Your Brand</h2>',
    '<h2 class="section-title" style="color: var(--text-highlight);">Who Sees Your Brand</h2>'
)
html = html.replace(
    '<p class="section-desc" style="color: rgba(255,255,255,0.7);">',
    '<p class="section-desc" style="color: var(--text-muted);">'
)

# Change the cards to be explicitly dark (#0F172A) instead of transparent
html = html.replace(
    'background: rgba(255,255,255,0.03);',
    'background: #0F172A;'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
