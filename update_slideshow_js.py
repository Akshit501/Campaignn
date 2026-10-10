import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the crossfading images with a single image + JS
old_images_block = """<div class="slideshow-images" style="width: 100%; height: 100%; position: absolute; top: 0; left: 0;">
              <img src="assets/images/event1.jpg" alt="Event 1" style="width: 100%; height: 100%; object-fit: cover; position: absolute; top: 0; left: 0; animation: crossfade 20s infinite 0s;">
              <img src="assets/images/event2.jpg" alt="Event 2" style="width: 100%; height: 100%; object-fit: cover; position: absolute; top: 0; left: 0; animation: crossfade 20s infinite 5s; opacity: 0;">
              <img src="assets/images/event3.jpg" alt="Event 3" style="width: 100%; height: 100%; object-fit: cover; position: absolute; top: 0; left: 0; animation: crossfade 20s infinite 10s; opacity: 0;">
              <img src="assets/images/event4.jpg" alt="Event 4" style="width: 100%; height: 100%; object-fit: cover; position: absolute; top: 0; left: 0; animation: crossfade 20s infinite 15s; opacity: 0;">
            </div>"""

new_images_block = """<div class="slideshow-images" style="width: 100%; height: 100%; position: absolute; top: 0; left: 0; background: #000;">
              <img id="live-highlights-img" src="assets/images/event1.jpg" alt="Event" style="width: 100%; height: 100%; object-fit: cover; transition: opacity 0.8s ease-in-out;">
            </div>
            
            <script>
              document.addEventListener('DOMContentLoaded', function() {
                const img = document.getElementById('live-highlights-img');
                const images = [
                  'assets/images/event1.jpg',
                  'assets/images/event2.jpg',
                  'assets/images/event3.jpg',
                  'assets/images/event4.jpg'
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
                  }, 800); // Wait for fade out to complete before changing source
                  
                }, 4000); // Change image every 4 seconds
              });
            </script>"""

if old_images_block in html:
    html = html.replace(old_images_block, new_images_block)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Replaced CSS crossfade with JS slideshow.")
else:
    print("Could not find old images block.")
