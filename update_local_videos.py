import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the three videos with the local ones
videos = [
    'assets/videos/vid1.mp4',
    'assets/videos/vid2.mp4',
    'assets/videos/vid3.mp4'
]

# The current videos are:
# https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4
# https://interactive-examples.mdn.mozilla.net/media/cc0-videos/friday.mp4
# https://www.w3schools.com/html/mov_bbb.mp4

# Because I might have multiple of these in the page, I will replace them one by one in the gallery section.
match = re.search(r'<section id="photos".*?</section>', html, re.DOTALL)
if match:
    section = match.group(0)
    
    # replace all src="" in this section
    def replacer(m):
        global count
        url = videos[count % len(videos)]
        count += 1
        return f'src="{url}"'

    count = 0
    new_section = re.sub(r'src="[^"]+"', replacer, section)
    
    html = html.replace(section, new_section)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Updated gallery videos!")
