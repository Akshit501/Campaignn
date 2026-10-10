with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start = html.find('<section id="about"')
end = html.find('</section>', start) + 10

if start != -1 and end != -1:
    html = html[:start] + html[end:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Removed about section!")
else:
    print("about section not found")
