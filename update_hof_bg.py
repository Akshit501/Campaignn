import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the section opening tag
html = html.replace(
    '<section id="impact" class="section-pad">',
    '<section id="impact" class="section-pad" style="background-color: #0f172a; background-image: radial-gradient(circle at 50% 0%, rgba(245, 158, 11, 0.15) 0%, transparent 60%), linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px); background-size: 100% 100%, 30px 30px, 30px 30px;">'
)

# Replace the title and description to be readable on dark background
old_head = """<div class="section-head centered">
        <h2 class="section-title">Hall of Fame: Previous Edition Winners</h2>
        <p class="section-desc">Projects that began as 48-hour hackathon commits and scaled into real enterprise pilots and venture-backed startups.</p>
      </div>"""

new_head = """<div class="section-head centered">
        <h2 class="section-title" style="color: #fff;">Hall of Fame: Previous Edition Winners</h2>
        <p class="section-desc" style="color: rgba(255,255,255,0.7);">Projects that began as 48-hour hackathon commits and scaled into real enterprise pilots and venture-backed startups.</p>
      </div>"""

html = html.replace(old_head, new_head)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated Hall of Fame background!")
