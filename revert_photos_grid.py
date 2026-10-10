import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx_start = html.find('<section id="photos"')
if idx_start != -1:
    idx_end = html.find('</section>', idx_start) + len('</section>')
    
    old_section = html[idx_start:idx_end]
    
    new_section = """<section id="photos" class="section-pad" style="background: var(--bg-surface-elevated); border-top: 1px solid var(--border-subtle); border-bottom: 1px solid var(--border-subtle);">
    <div class="container">
      <div class="section-head centered">
        <h2 class="section-title">Moments from Previous Editions</h2>
        <p class="section-desc">The energy, innovation, and community spirit captured in motion.</p>
      </div>

      <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px;">
        
        <!-- Video 1 -->
        <div class="card" style="border-radius: var(--radius-lg); overflow: hidden; position: relative; aspect-ratio: 9/16; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
          <video autoplay loop muted playsinline style="width: 100%; height: 100%; object-fit: cover;">
            <source src="assets/videos/vid1.mp4" type="video/mp4">
          </video>
        </div>

        <!-- Video 2 -->
        <div class="card" style="border-radius: var(--radius-lg); overflow: hidden; position: relative; aspect-ratio: 9/16; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
          <video autoplay loop muted playsinline style="width: 100%; height: 100%; object-fit: cover;">
            <source src="assets/videos/vid2.mp4" type="video/mp4">
          </video>
        </div>

        <!-- Video 3 -->
        <div class="card" style="border-radius: var(--radius-lg); overflow: hidden; position: relative; aspect-ratio: 9/16; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
          <video autoplay loop muted playsinline style="width: 100%; height: 100%; object-fit: cover;">
            <source src="assets/videos/vid3.mp4" type="video/mp4">
          </video>
        </div>

      </div>
    </div>
  </section>"""
    
    html = html.replace(old_section, new_section)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Reverted photos section to 3-column video grid!")
else:
    print("Could not find photos section.")
