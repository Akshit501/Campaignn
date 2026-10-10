with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start = html.find('<section id="audience"')
end = html.find('</section>', start) + 10

if start != -1 and end != -1:
    with open('debug_audience.txt', 'w', encoding='utf-8') as f:
        f.write(html[start:end])
    print("Dumped audience section")
else:
    print("Section not found")
