import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove lead-open-pill
idx = html.find('<a href="#hero-enquiry-form" id="lead-open-pill"')
if idx != -1:
    end = html.find('</a>', idx) + 4
    html = html[:idx] + html[end:]

# 2. Add glowing animation to header button
html = html.replace(
    '<a href="#hero-enquiry-form" class="btn btn-secondary btn-sm" data-track="header_partner_click">Partner with us</a>',
    '<a href="#hero-enquiry-form" class="btn btn-secondary btn-sm partner-glow-btn" data-track="header_partner_click">Partner with us</a>'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated HTML!")
