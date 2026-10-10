with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('<section id="lead"')
end = html.find('<form', idx)
print(html[idx:end])
