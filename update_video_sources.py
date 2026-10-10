import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx_start = html.find('<section id="photos"')
if idx_start != -1:
    idx_end = html.find('</section>', idx_start) + len('</section>')
    
    section = html[idx_start:idx_end]
    
    # Replace the sources
    section = section.replace('assets/videos/vid1.mp4', 'assets/videos/genai_vid1.mp4')
    section = section.replace('assets/videos/vid2.mp4', 'assets/videos/genai_vid2.mp4')
    section = section.replace('assets/videos/vid3.mp4', 'assets/videos/genai_vid3.mp4')
    
    html = html[:idx_start] + section + html[idx_end:]
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Updated video sources in photos section!")
else:
    print("Could not find photos section.")
