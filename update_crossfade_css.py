import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

crossfade_css = """
/* Slideshow Crossfade Animation */
@keyframes crossfade {
  0% { opacity: 0; }
  10% { opacity: 1; }
  25% { opacity: 1; }
  35% { opacity: 0; }
  100% { opacity: 0; }
}

.media-card-hover:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 25px rgba(0,0,0,0.1);
}
"""

if '@keyframes crossfade' not in css:
    with open('styles.css', 'a', encoding='utf-8') as f:
        f.write('\n' + crossfade_css + '\n')
    print("Added crossfade CSS!")
else:
    print("CSS already exists!")
