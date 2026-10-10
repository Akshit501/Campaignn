with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start = html.find('<section class="hero-section')
end = html.find('</section>', start) + 10

with open('debug_hero.txt', 'w', encoding='utf-8') as f:
    f.write(html[start:end])
