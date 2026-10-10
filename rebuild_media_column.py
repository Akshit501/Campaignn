import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# The right column of the media section has:
# <div style="flex: 1; display: flex; flex-direction: column; gap: 24px;">
#   <!-- Slideshow Card replacing the previous two playcards -->
#   <div class="card" style="flex: 1; border-radius: var(--radius-lg); overflow: hidden; position: relative; min-height: 450px;">
# ... up to the closing </div> of that column.

# Let's find the start of the right column:
col_start_str = '<div style="flex: 1; display: flex; flex-direction: column; gap: 24px;">\n          <!-- Slideshow Card'
idx_start = html.find(col_start_str)

if idx_start != -1:
    # Find the closing div of the column
    # Since we know the next thing after this column is `</div>\n    </div>\n  </section>`
    # We can just search for the end of the section
    idx_end = html.find('</section>', idx_start)
    # The end of our column is actually a bit before </section>. Let's do string search for the exact end:
    idx_end = html.rfind('</div>', idx_start, html.find('</div>\n    </div>\n  </section>', idx_start) + len('</div>'))
    
    old_col = html[idx_start:idx_end+6]
    
    new_col = """<div style="flex: 1; display: flex; flex-direction: column; gap: 24px;">
          <!-- Slideshow Card -->
          <div class="card" style="flex: 1; border-radius: var(--radius-lg); overflow: hidden; position: relative; min-height: 450px; background: #000;">
            
            <img id="live-highlights-img" src="assets/images/slide1.jpg" alt="Event" style="width: 100%; height: 100%; position: absolute; top: 0; left: 0; object-fit: cover; transition: opacity 0.8s ease-in-out;">
            
            <div style="position: absolute; bottom: 0; left: 0; width: 100%; padding: 40px 32px 32px; background: linear-gradient(to top, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0.4) 60%, transparent 100%);">
              <div style="display: flex; justify-content: space-between; align-items: flex-end;">
                <div>
                  <span style="background: var(--primary-color); color: #fff; font-size: 12px; font-weight: bold; text-transform: uppercase; padding: 4px 12px; border-radius: 4px; display: inline-block; margin-bottom: 12px;">Live Highlights</span>
                  <h3 style="color: #fff; font-size: 28px; font-weight: 800; margin: 0;">Experience the Energy</h3>
                </div>
                
                <!-- Pagination Dots -->
                <div style="display: flex; gap: 8px; margin-bottom: 8px;">
                  <div class="slide-dot" style="width: 10px; height: 10px; border-radius: 50%; background: #fff; transition: background 0.3s ease;"></div>
                  <div class="slide-dot" style="width: 10px; height: 10px; border-radius: 50%; background: rgba(255,255,255,0.4); transition: background 0.3s ease;"></div>
                  <div class="slide-dot" style="width: 10px; height: 10px; border-radius: 50%; background: rgba(255,255,255,0.4); transition: background 0.3s ease;"></div>
                </div>
              </div>
            </div>
            
            <script>
              document.addEventListener('DOMContentLoaded', function() {
                const img = document.getElementById('live-highlights-img');
                const dots = document.querySelectorAll('.slide-dot');
                const images = [
                  'assets/images/slide1.jpg',
                  'assets/images/slide2.jpg',
                  'assets/images/slide3.jpg'
                ];
                let currentIndex = 0;
                
                setInterval(() => {
                  // Fade out
                  img.style.opacity = 0;
                  
                  setTimeout(() => {
                    currentIndex = (currentIndex + 1) % images.length;
                    img.src = images[currentIndex];
                    // Fade in
                    img.style.opacity = 1;
                    
                    // Update dots
                    dots.forEach((dot, index) => {
                      if (index === currentIndex) {
                        dot.style.background = '#fff';
                      } else {
                        dot.style.background = 'rgba(255,255,255,0.4)';
                      }
                    });
                  }, 800); // Wait for fade out to complete before changing source
                  
                }, 4000); // Change image every 4 seconds
              });
            </script>
          </div>
        </div>"""

    html = html.replace(old_col, new_col)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Rebuilt right column cleanly!")
else:
    print("Could not find start of right column.")
