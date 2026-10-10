import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's replace the slideshow part in the media section
old_slideshow = """<img id="live-highlights-img" src="assets/images/slide1.jpg" alt="Event" style="width: 100%; height: 100%; position: absolute; top: 0; left: 0; object-fit: cover; transition: opacity 0.8s ease-in-out;">
            
            <div style="position: absolute; bottom: 0; left: 0; width: 100%; padding: 56px 32px 32px; background: linear-gradient(to top, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0.4) 60%, transparent 100%);">
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
                ];"""

new_slideshow = """<img id="live-highlights-img" src="assets/images/reach/reach_1.png" alt="Event" style="width: 100%; height: 100%; position: absolute; top: 0; left: 0; object-fit: cover; transition: opacity 0.8s ease-in-out;">
            
            <div style="position: absolute; bottom: 0; left: 0; width: 100%; padding: 56px 32px 32px; background: linear-gradient(to top, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0.4) 60%, transparent 100%);">
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
                  <div class="slide-dot" style="width: 10px; height: 10px; border-radius: 50%; background: rgba(255,255,255,0.4); transition: background 0.3s ease;"></div>
                </div>
              </div>
            </div>
            
            <script>
              document.addEventListener('DOMContentLoaded', function() {
                const img = document.getElementById('live-highlights-img');
                const dots = document.querySelectorAll('.slide-dot');
                const images = [
                  'assets/images/reach/reach_1.png',
                  'assets/images/reach/reach_2.png',
                  'assets/images/reach/reach_3.png',
                  'assets/images/reach/reach_4.png'
                ];"""

if old_slideshow in html:
    html = html.replace(old_slideshow, new_slideshow)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Updated slideshow with 4 new images!")
else:
    print("Could not find exact old slideshow text. Trying regex.")
    
    # Fallback to a looser match if exact match fails
    start_str = '<img id="live-highlights-img"'
    end_str = '];'
    
    idx_start = html.find(start_str)
    if idx_start != -1:
        idx_end = html.find(end_str, idx_start) + len(end_str)
        html = html[:idx_start] + new_slideshow + html[idx_end:]
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print("Updated via fallback!")
    else:
        print("Could not find even the start string.")
