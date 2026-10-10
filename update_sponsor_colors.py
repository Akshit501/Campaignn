import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the section wrapper to be cream background
# Change: <section id="sponsor" class="section-pad sponsor-section" style="background: #4F46E5; color: #fff;">
# To: <section id="sponsor" class="section-pad sponsor-section" style="background: var(--bg-deep);">
html = re.sub(
    r'<section id="sponsor" class="section-pad sponsor-section" style="background: #4F46E5; color: #fff;">',
    r'<section id="sponsor" class="section-pad sponsor-section" style="background: var(--bg-deep);">',
    html
)

# 2. Revert the title color
# Change: <h2 class="section-title" style="color: #fff;">
# To: <h2 class="section-title" style="color: var(--text-highlight);">
html = re.sub(
    r'<h2 class="section-title" style="color: #fff;">',
    r'<h2 class="section-title" style="color: var(--text-highlight);">',
    html
)

# 3. Revert the description color
# Change: <p class="section-desc" style="max-width: 760px; color: rgba(255,255,255,0.9); margin: 0 auto;">
# To: <p class="section-desc" style="max-width: 760px; color: var(--text-muted); margin: 0 auto;">
html = re.sub(
    r'<p class="section-desc" style="max-width: 760px; color: rgba\(255,255,255,0\.9\); margin: 0 auto;">',
    r'<p class="section-desc" style="max-width: 760px; color: var(--text-muted); margin: 0 auto;">',
    html
)

# 4. Update the badge color
# Change: <div class="sponsor-highlight-badge" style="color: #fff; background: rgba(255,255,255,0.2); border: 1px solid rgba(255,255,255,0.3); display: inline-block; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: 700; margin-bottom: 16px;"> Enterprise Partnership Invitational 2026</div>
# To a nice dark/colorful badge:
new_badge = '<div class="sponsor-highlight-badge" style="color: var(--primary-color); background: rgba(244, 63, 94, 0.1); border: 1px solid rgba(244, 63, 94, 0.2); display: inline-block; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: 700; margin-bottom: 16px;"> Enterprise Partnership Invitational 2026</div>'
html = re.sub(
    r'<div class="sponsor-highlight-badge" style="color: #fff; background: rgba\(255,255,255,0\.2\); border: 1px solid rgba\(255,255,255,0\.3\); display: inline-block; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: 700; margin-bottom: 16px;"> Enterprise Partnership Invitational 2026</div>',
    new_badge,
    html
)

# 5. Remove 'background: var(--bg-surface);' from the inline style of the cards so the external CSS gradients work
# Change: style="background: var(--bg-surface); border: 1px solid var(--border-subtle);
# To: style="border: 1px solid var(--border-subtle);
html = html.replace(
    'style="background: var(--bg-surface); border: 1px solid var(--border-subtle);',
    'style="border: 1px solid var(--border-subtle);'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
