with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start = html.find('<section id="about"')
end = html.find('</section>', start) + 10

print(html[start:start+500])
