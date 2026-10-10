import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

marquee_css = """
/* Reviews Marquee Animation */
.reviews-marquee-wrapper {
  overflow: hidden;
  width: 100%;
  padding-top: 30px; /* Space for avatars */
}

.reviews-marquee-track {
  display: flex;
  gap: 32px;
  width: max-content;
  animation: marquee-reviews 40s linear infinite;
}

.reviews-marquee-wrapper:hover .reviews-marquee-track {
  animation-play-state: paused;
}

@keyframes marquee-reviews {
  0% { transform: translateX(0); }
  100% { transform: translateX(calc(-50% - 16px)); } /* -50% shifts by exactly one set of cards, -16px for half gap */
}

.review-card-item {
  width: 400px; /* Fixed width for marquee */
  flex-shrink: 0;
  background: #fff;
  border-radius: 12px;
  padding: 48px 24px 24px;
  position: relative;
  box-shadow: 0 10px 30px rgba(0,0,0,0.06);
  border: 1px solid rgba(0,0,0,0.05);
  margin-top: 20px;
  margin-bottom: 20px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.review-card-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 40px rgba(0,0,0,0.12);
}
"""

if '.reviews-marquee-wrapper' not in css:
    with open('styles.css', 'a', encoding='utf-8') as f:
        f.write('\n' + marquee_css + '\n')
    print("Added CSS!")
else:
    print("CSS already exists!")
