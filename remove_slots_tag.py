with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('Limited Sponsor Slots Available')
if idx != -1:
    start = html.rfind('<div', 0, idx)
    end = html.find('</div>', idx) + 6
    html = html[:start] + html[end:]
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Removed limited sponsor slots tag!")
else:
    print("Could not find the tag.")
