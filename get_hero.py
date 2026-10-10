with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('<section class="hero-section">')
if idx != -1:
    end = html.find('</section>', idx) + 10
    print(html[idx:end])
else:
    print("Could not find hero-section")
