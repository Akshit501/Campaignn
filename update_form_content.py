with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the heading
old_heading = 'Be a Part of<br>The AI Hackathon 2.0'
new_heading = 'Become a Sponsor Partner'

html = html.replace(old_heading, new_heading)

# The user image also shows the gradient button, let's restore it if it's currently solid pink
old_button_style = 'background: #e52b66;'
new_button_style = 'background: linear-gradient(90deg, #f43f5e 0%, #f97316 100%);'
html = html.replace(old_button_style, new_button_style)

# The labels in the image are slightly different color (#475569), but they're basically the same. I'll leave them alone as per "only content".

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated form content!")
