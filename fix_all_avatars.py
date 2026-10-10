import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's see what ui-avatars URLs exist
urls = re.findall(r'https://ui-avatars\.com[^"]+', html)
unique_urls = set(urls)

print("Found URLs:")
for u in unique_urls:
    print(u)

# Now let's replace all ui-avatars URLs with randomuser portraits
# I will just replace them safely.
mapping = {
    'Sanya': 'https://randomuser.me/api/portraits/women/12.jpg',
    'Anand': 'https://randomuser.me/api/portraits/men/33.jpg',
    'Vikram': 'https://randomuser.me/api/portraits/men/46.jpg',
    'Priya': 'https://randomuser.me/api/portraits/women/44.jpg',
    'Rohit': 'https://randomuser.me/api/portraits/men/32.jpg'
}

for u in unique_urls:
    new_url = 'https://randomuser.me/api/portraits/lego/1.jpg' # fallback
    for name, replacement in mapping.items():
        if name in u:
            new_url = replacement
            break
    
    html = html.replace(u, new_url)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Replaced all remaining ui-avatars URLs with photos!")
