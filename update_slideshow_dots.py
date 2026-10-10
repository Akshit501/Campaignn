import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the existing JS slideshow block
idx_start = html.find('<div class="slideshow-images"')
if idx_start != -1:
    idx_end = html.find('</script>', idx_start) + len('</script>')
    
    old_block = html[idx_start:idx_end]
    
    new_block = """<div class="slideshow-images" style="width: 100%; height: 100%; position: absolute; top: 0; left: 0; background: #000;">
              <img id="live-highlights-img" src="assets/images/slide1.jpg" alt="Event" style="width: 100%; height: 100%; object-fit: cover; transition: opacity 0.8s ease-in-out;">
            </div>
            
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
            </script>"""

    # Wait, the old_block actually includes the overlay div:
    # Let me check if the overlay is part of what I replace.
    # In my previous script `fix_media_section.py`, the structure was:
    # <div class="slideshow-images">...</div>
    # <div style="position: absolute; bottom: 0; left: 0... (overlay) ... </div>
    # So I need to replace from <div class="slideshow-images" to </script>.
    # Let's find the closing </div> of the overlay.
    overlay_end = html.find('</div>\n          </div>\n        </div>', idx_start)
    if overlay_end == -1:
        # Try to just string replace the known previous block
        # Actually I can just replace everything from <div class="slideshow-images" up to </script>
        pass

    html = html[:idx_start] + new_block + html[idx_end:]
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Replaced JS slideshow with dots.")
else:
    print("Could not find old images block.")
