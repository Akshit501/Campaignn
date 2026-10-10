import sys
import re

sys.stdout.reconfigure(encoding='utf-8')
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

sections = re.findall(r'<section.*?</section>', html, re.DOTALL | re.IGNORECASE)
for i, s in enumerate(sections):
    id_match = re.search(r'id=[\'"]([^\'"]+)[\'"]', s)
    sec_id = id_match.group(1) if id_match else 'no-id'
    title_match = re.search(r'<h2.*?>(.*?)</h2>', s, re.DOTALL)
    title = title_match.group(1).strip() if title_match else 'no-title'
    title = re.sub(r'<.*?>', '', title).replace('\n', ' ')
    print(f'Section {i}: id={sec_id}, title={title[:50]}')
