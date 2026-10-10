import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace all gtv-videos-bucket URLs with working MDN/W3C demo videos
videos = [
    'https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4',
    'https://interactive-examples.mdn.mozilla.net/media/cc0-videos/friday.mp4',
    'https://www.w3schools.com/html/mov_bbb.mp4'
]

# Find all source tags and replace their src
def replacer(match):
    global count
    url = videos[count % len(videos)]
    count += 1
    return f'src="{url}"'

count = 0
html = re.sub(r'src="https://storage\.googleapis\.com/gtv-videos-bucket[^"]+"', replacer, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
