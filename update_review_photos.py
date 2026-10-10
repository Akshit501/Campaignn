import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# The avatar div looks like this:
# <div style="position: absolute; top: -30px; left: 24px; width: 60px; height: 60px; border-radius: 50%; overflow: hidden; border: 3px solid #fff; box-shadow: 0 4px 10px rgba(0,0,0,0.1);">
#   <img src="https://ui-avatars.com/api/?name=Rohit+Deshmukh&background=0F172A&color=fff&bold=true" alt="Avatar" style="width: 100%; height: 100%; object-fit: cover;">
# </div>

# Let's replace the avatar container style to center it
# old style: top: -30px; left: 24px;
# new style: top: -30px; left: 50%; transform: translateX(-50%);

html = html.replace(
    'top: -30px; left: 24px; width: 60px; height: 60px;',
    'top: -30px; left: 50%; transform: translateX(-50%); width: 60px; height: 60px;'
)

# Also let's increase the size slightly to match the reference image better (it looks like maybe 70px)
html = html.replace(
    'top: -30px; left: 50%; transform: translateX(-50%); width: 60px; height: 60px;',
    'top: -35px; left: 50%; transform: translateX(-50%); width: 70px; height: 70px;'
)

# Now let's replace the image URLs
# We have 5 reviewers in the marquee. Let's find them and replace the ui-avatars URL with randomuser faces.
# Reviewer 1: Rohit Deshmukh (Man) -> men/32.jpg
# Reviewer 2: Priya Sharma (Woman) -> women/44.jpg
# Reviewer 3: Vikram Singh (Man) -> men/46.jpg
# Reviewer 4: Ananya Gupta (Woman) -> women/68.jpg
# Reviewer 5: Siddharth Rao (Man) -> men/22.jpg

html = re.sub(r'https://ui-avatars\.com/api/\?name=[^&]+&background=[A-Z0-9]+&color=fff&bold=true',
              lambda m: 'https://randomuser.me/api/portraits/men/32.jpg' if 'Rohit' in m.group(0) else
                        'https://randomuser.me/api/portraits/women/44.jpg' if 'Priya' in m.group(0) else
                        'https://randomuser.me/api/portraits/men/46.jpg' if 'Vikram' in m.group(0) else
                        'https://randomuser.me/api/portraits/women/68.jpg' if 'Ananya' in m.group(0) else
                        'https://randomuser.me/api/portraits/men/22.jpg', html)

# Wait, the marquee tracks are duplicated (for infinite scroll).
# So the re.sub should replace all occurrences properly!

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated review cards with real photos and centered them!")
