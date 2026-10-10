with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('Everything You Need to Know')
if idx != -1:
    start = html.rfind('<section', 0, idx)
    end = html.find('</section>', idx) + 10
    
    html = html[:start] + html[end:]
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Removed FAQ section!")
else:
    print("Section not found.")
