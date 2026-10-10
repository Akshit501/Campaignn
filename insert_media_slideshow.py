import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

media_section = """
  <!-- ==========================================================================
       MEDIA COVERAGE & SLIDESHOW
       ========================================================================== -->
  <section id="media-slideshow" class="section-pad" style="background: var(--bg-deep);">
    <div class="container">
      <div style="display: flex; gap: 40px; align-items: stretch; flex-wrap: wrap;">
        
        <!-- Left Links Column -->
        <div style="flex: 1; min-width: 300px; display: flex; flex-direction: column; gap: 20px;">
          
          <a href="https://www.linkedin.com/company/the-economic-times/" target="_blank" style="background: #fff; border-radius: 12px; padding: 24px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); text-decoration: none; border-left: 5px solid #0077b5; display: block; transition: transform 0.3s ease;">
            <h3 style="color: #111; margin-bottom: 8px; font-size: 20px;">LinkedIn</h3>
            <p style="color: #666; font-size: 14px; margin-bottom: 16px; line-height: 1.5;">Featured across ET's LinkedIn with 10M+ professional followers. Hackathon highlights, winner stories, and sponsor spotlights.</p>
            <span style="color: #f43f5e; font-size: 14px; font-weight: 600;">View on LinkedIn →</span>
          </a>

          <a href="https://www.youtube.com/@EconomicTimes" target="_blank" style="background: #fff; border-radius: 12px; padding: 24px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); text-decoration: none; border-left: 5px solid #ff0000; display: block; transition: transform 0.3s ease;">
            <h3 style="color: #111; margin-bottom: 8px; font-size: 20px;">YouTube</h3>
            <p style="color: #666; font-size: 14px; margin-bottom: 16px; line-height: 1.5;">Full event recaps, keynote sessions, winner interviews, and CXO panel discussions on The Economic Times YouTube channel.</p>
            <span style="color: #f43f5e; font-size: 14px; font-weight: 600;">Watch on YouTube →</span>
          </a>

        </div>

        <!-- Right Slideshow Column -->
        <div style="flex: 1.5; min-width: 350px; position: relative; border-radius: 16px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.1); min-height: 380px;">
          
          <div class="slideshow-images" style="width: 100%; height: 100%; position: absolute; top: 0; left: 0;">
            <img src="assets/images/event1.jpg" alt="Event 1" style="width: 100%; height: 100%; object-fit: cover; position: absolute; top: 0; left: 0; animation: crossfade 20s infinite 0s;">
            <img src="assets/images/event2.jpg" alt="Event 2" style="width: 100%; height: 100%; object-fit: cover; position: absolute; top: 0; left: 0; animation: crossfade 20s infinite 5s; opacity: 0;">
            <img src="assets/images/event3.jpg" alt="Event 3" style="width: 100%; height: 100%; object-fit: cover; position: absolute; top: 0; left: 0; animation: crossfade 20s infinite 10s; opacity: 0;">
            <img src="assets/images/event4.jpg" alt="Event 4" style="width: 100%; height: 100%; object-fit: cover; position: absolute; top: 0; left: 0; animation: crossfade 20s infinite 15s; opacity: 0;">
          </div>

          <div style="position: absolute; bottom: 0; left: 0; width: 100%; padding: 40px 32px 32px; background: linear-gradient(to top, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0.4) 60%, transparent 100%);">
            <span style="background: #f43f5e; color: #fff; font-size: 12px; font-weight: 800; padding: 6px 12px; border-radius: 4px; text-transform: uppercase; letter-spacing: 1px; display: inline-block; margin-bottom: 12px;">Live Highlights</span>
            <h3 style="color: #fff; font-size: 28px; font-weight: 800; margin: 0;">Experience the Energy</h3>
          </div>

        </div>

      </div>
    </div>
  </section>
"""

# Insert right before <section id="photos"
idx = html.find('<section id="photos"')
if idx != -1:
    html = html[:idx] + media_section + '\n\n' + html[idx:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Inserted media slideshow section!")
else:
    print("Could not find insertion point!")

