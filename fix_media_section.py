import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Delete id="media-slideshow"
idx_slideshow = html.find('<section id="media-slideshow"')
if idx_slideshow != -1:
    end_slideshow = html.find('</section>', idx_slideshow) + len('</section>')
    html = html[:idx_slideshow] + html[end_slideshow:]
    print("Deleted media-slideshow")

# 2. Update id="media"
# In id="media", replace the entire right hand column:
# We can find <!-- Right: Playcard & Image -->
idx_right = html.find('<!-- Right: Playcard & Image -->')
if idx_right != -1:
    # Find the start of the div right after the comment
    div_start = html.find('<div', idx_right)
    # We need to find the matching closing div for this right column
    count = 0
    div_end = -1
    pos = div_start
    while pos < len(html):
        next_open = html.find('<div', pos)
        next_close = html.find('</div>', pos)
        
        if next_open != -1 and next_open < next_close:
            count += 1
            pos = next_open + 4
        elif next_close != -1:
            count -= 1
            pos = next_close + 6
            if count == 0:
                div_end = pos
                break
        else:
            break
    
    if div_end != -1:
        old_right_col = html[div_start:div_end]
        
        new_right_col = """<div style="flex: 1; display: flex; flex-direction: column; gap: 24px;">
          <!-- Slideshow Card replacing the previous two playcards -->
          <div class="card" style="flex: 1; border-radius: var(--radius-lg); overflow: hidden; position: relative; min-height: 450px;">
            <div class="slideshow-images" style="width: 100%; height: 100%; position: absolute; top: 0; left: 0;">
              <img src="assets/images/event1.jpg" alt="Event 1" style="width: 100%; height: 100%; object-fit: cover; position: absolute; top: 0; left: 0; animation: crossfade 20s infinite 0s;">
              <img src="assets/images/event2.jpg" alt="Event 2" style="width: 100%; height: 100%; object-fit: cover; position: absolute; top: 0; left: 0; animation: crossfade 20s infinite 5s; opacity: 0;">
              <img src="assets/images/event3.jpg" alt="Event 3" style="width: 100%; height: 100%; object-fit: cover; position: absolute; top: 0; left: 0; animation: crossfade 20s infinite 10s; opacity: 0;">
              <img src="assets/images/event4.jpg" alt="Event 4" style="width: 100%; height: 100%; object-fit: cover; position: absolute; top: 0; left: 0; animation: crossfade 20s infinite 15s; opacity: 0;">
            </div>

            <div style="position: absolute; bottom: 0; left: 0; width: 100%; padding: 40px 32px 32px; background: linear-gradient(to top, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0.4) 60%, transparent 100%);">
              <span style="background: var(--primary-color); color: #fff; font-size: 12px; font-weight: bold; text-transform: uppercase; padding: 4px 12px; border-radius: 4px; display: inline-block; margin-bottom: 12px;">Live Highlights</span>
              <h3 style="color: #fff; font-size: 28px; font-weight: 800; margin: 0;">Experience the Energy</h3>
            </div>
          </div>
        </div>"""
        
        html = html.replace(old_right_col, new_right_col)
        print("Replaced right column in media section!")
        
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html)

