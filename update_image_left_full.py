import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start = html.find('<div class="hero-left"')
if start != -1:
    end = html.find('<!-- Right Side: Form Card -->', start)
    if end != -1:
        old_left = html[start:end]
        
        new_left = """<div class="hero-left" style="position: relative;">
          
          <!-- User requested exact image for the ENTIRE left side (NO HTML animation for numbers) -->
          <img src="assets/images/hero_left_full.png" style="width: 100%; max-width: 100%; margin-left: -20px; display: block;" alt="Hero Graphic">
          
        </div>

        """
        html = html.replace(old_left, new_left)
        
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print("Replaced left HTML completely with full image crop!")
    else:
        print("Right Side: Form Card not found")
else:
    print("hero_left not found")
