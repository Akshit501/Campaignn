import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

match = re.search(r'<section id="sponsor".*?</section>', html, re.DOTALL)
if match:
    print(match.group(0).encode('ascii', 'ignore').decode('ascii'))
else:
    print('Not found')
