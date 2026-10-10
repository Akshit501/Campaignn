import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Helper to extract a section block
def extract_section(html_content, section_id):
    start_tag = f'<section id="{section_id}"'
    start_idx = html_content.find(start_tag)
    if start_idx == -1:
        return -1, -1, None
    
    end_tag = '</section>'
    end_idx = html_content.find(end_tag, start_idx) + len(end_tag)
    return start_idx, end_idx, html_content[start_idx:end_idx]

# Extract lead, videos, photos
lead_s, lead_e, lead_html = extract_section(html, 'lead')
videos_s, videos_e, videos_html = extract_section(html, 'videos')
photos_s, photos_e, photos_html = extract_section(html, 'photos')

if not (lead_html and videos_html and photos_html):
    print("Failed to find one or more sections!")
    exit(1)

# Now we want to remove them from the original html (in reverse order to not mess up indices)
# Wait, they are contiguous or near contiguous.
# It is safer to find the start of lead and end of photos, and replace that entire block.
# Let's check their order in the document.
print("lead start:", lead_s)
print("videos start:", videos_s)
print("photos start:", photos_s)

# Assuming order is lead -> videos -> photos
# We will just replace all 3 with the new order: photos -> videos -> lead
start_block = min(lead_s, videos_s, photos_s)
end_block = max(lead_e, videos_e, photos_e)

block = html[start_block:end_block]

# Does the block contain anything else?
# Let's check what's between them.
between_1 = html[lead_e:videos_s]
between_2 = html[videos_e:photos_s]

# Let's just remove them individually and then insert them after media.
# Wait, let's just do text replacements. We replace them with empty strings.
html_clean = html.replace(lead_html, '').replace(videos_html, '').replace(photos_html, '')

# Now we find the end of the media section and insert them there
media_s, media_e, media_html = extract_section(html_clean, 'media')
if media_e == -1:
    print("Media section not found")
    exit(1)

new_order_html = '\n\n' + photos_html + '\n\n' + videos_html + '\n\n' + lead_html + '\n\n'

html_new = html_clean[:media_e] + new_order_html + html_clean[media_e:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_new)
print("Successfully reordered sections: media -> photos -> videos -> lead")
