import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

photos_html = """
          <!-- Photo 1 -->
          <div class="photo-marquee-item">
            <img src="assets/images/event1.jpg" alt="Event Photo 1">
            <div class="photo-overlay">
              <span class="photo-badge">Live Highlights</span>
              <h3 class="photo-title">Experience the Energy</h3>
            </div>
          </div>

          <!-- Photo 2 -->
          <div class="photo-marquee-item">
            <img src="assets/images/event2.jpg" alt="Event Photo 2">
            <div class="photo-overlay">
              <span class="photo-badge">Builder Space</span>
              <h3 class="photo-title">Where Ideas Take Shape</h3>
            </div>
          </div>

          <!-- Photo 3 -->
          <div class="photo-marquee-item">
            <img src="assets/images/event3.jpg" alt="Event Photo 3">
            <div class="photo-overlay">
              <span class="photo-badge">Expert Mentorship</span>
              <h3 class="photo-title">Guidance from the Best</h3>
            </div>
          </div>
          
          <!-- Photo 4 -->
          <div class="photo-marquee-item">
            <img src="assets/images/event4.jpg" alt="Event Photo 4">
            <div class="photo-overlay">
              <span class="photo-badge">Demo Day</span>
              <h3 class="photo-title">Pitching to Industry Titans</h3>
            </div>
          </div>
"""

new_section = f"""<section id="photos" class="section-pad" style="background: var(--bg-surface-elevated); border-top: 1px solid var(--border-subtle); border-bottom: 1px solid var(--border-subtle); overflow: hidden;">
    <div class="container-fluid" style="padding: 0;">
      <div class="section-head centered" style="margin-bottom: 40px; padding: 0 20px;">
        <h2 class="section-title">Moments from Previous Editions</h2>
        <p class="section-desc">The energy, innovation, and community spirit captured in pictures.</p>
      </div>

      <div class="photos-marquee-wrapper">
        <div class="photos-marquee-track">
{photos_html}
          <!-- Duplicate for infinite seamless scroll -->
{photos_html}
        </div>
      </div>
    </div>
  </section>"""

idx_start = html.find('<h2 class="section-title">Moments from Previous Editions</h2>')
idx_start = html.rfind('<section id="photos"', 0, idx_start)
idx_end = html.find('</section>', idx_start) + len('</section>')

if idx_start != -1 and idx_end != -1:
    old_section = html[idx_start:idx_end]
    html = html.replace(old_section, new_section)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Updated photos HTML for Marquee!")
else:
    print("Could not find photos section bounds.")
