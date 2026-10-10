with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('<footer class="premium-footer">')
print(html[idx-500:idx])
