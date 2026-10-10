import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

marquee_css = """
/* Photos Marquee Animation */
.photos-marquee-wrapper {
  overflow: hidden;
  width: 100%;
  padding: 20px 0;
}

.photos-marquee-track {
  display: flex;
  gap: 24px;
  width: max-content;
  animation: marquee-photos 30s linear infinite;
}

.photos-marquee-wrapper:hover .photos-marquee-track {
  animation-play-state: paused;
}

@keyframes marquee-photos {
  0% { transform: translateX(0); }
  100% { transform: translateX(calc(-50% - 12px)); }
}

.photo-marquee-item {
  width: 500px;
  height: 350px;
  flex-shrink: 0;
  border-radius: 20px;
  overflow: hidden;
  position: relative;
  box-shadow: 0 10px 30px rgba(0,0,0,0.15);
  transition: transform 0.3s ease;
}

.photo-marquee-item:hover {
  transform: scale(1.02);
}

.photo-marquee-item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.photo-marquee-item:hover img {
  transform: scale(1.05);
}

.photo-overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  padding: 40px 24px 24px;
  background: linear-gradient(to top, rgba(0,0,0,0.8) 0%, transparent 100%);
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.photo-badge {
  background: #f43f5e;
  color: #fff;
  font-size: 11px;
  font-weight: 800;
  padding: 4px 10px;
  border-radius: 4px;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin-bottom: 8px;
}

.photo-title {
  color: #fff;
  font-size: 22px;
  font-weight: 700;
  margin: 0;
}
"""

if '.photos-marquee-wrapper' not in css:
    with open('styles.css', 'a', encoding='utf-8') as f:
        f.write('\n' + marquee_css + '\n')
    print("Added CSS!")
else:
    print("CSS already exists!")
