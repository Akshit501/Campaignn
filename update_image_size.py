with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('grid-template-columns: 1.15fr 0.85fr; gap: 60px;', 'grid-template-columns: 1.35fr 0.65fr; gap: 40px;')
html = html.replace('grid-template-columns: 1.1fr 0.9fr; gap: 60px;', 'grid-template-columns: 1.35fr 0.65fr; gap: 40px;')

html = html.replace('style="width: 100%; max-width: 100%; margin-left: -20px; display: block;"', 'style="width: 125%; max-width: 125%; margin-left: -12%; margin-top: -20px; display: block;"')
html = html.replace('style="width: 100%; max-width: 100%; margin-left: -20px; display: block;"', 'style="width: 125%; max-width: 125%; margin-left: -12%; margin-top: -20px; display: block;"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated grid layout and image style")
