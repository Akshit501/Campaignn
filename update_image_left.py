with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start = html.find('<div class="hero-left"')
if start != -1:
    stats_start = html.find('<!-- Stats Row (with animation) -->', start)
    if stats_start != -1:
        tag_end = html.find('>', start) + 1
        old_left = html[tag_end:stats_start]
        
        new_left = """
          <!-- User requested exact image for the background/left graphic -->
          <img src="assets/images/hero_left_graphic.png" style="width: 100%; max-width: 580px; margin-bottom: 32px; display: block;" alt="Hero Graphic">
          
          """
        html = html.replace(old_left, new_left)
        
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print("Replaced left HTML with exact image crop!")
    else:
        print("stats_start not found")
else:
    print("hero_left not found")
