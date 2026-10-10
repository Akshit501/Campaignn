import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('<div class="faq-search-box">')
if idx != -1:
    end = html.find('</div>', idx) + 6
    html = html[:idx] + html[end:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("FAQ search removed!")
else:
    print("Could not find faq search box")
