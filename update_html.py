import re
import os

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Hero Stats Row
hero_stats_new = """
          <div class="hero-stats-row">
            <div class="hero-stat-item">
              <span class="hero-stat-num"><span class="counter" data-target="5000">0</span>+</span>
              <span class="hero-stat-label">Builders</span>
            </div>
            <div class="hero-stat-divider"></div>
            <div class="hero-stat-item">
              <span class="hero-stat-num"><span class="counter" data-target="100">0</span>+</span>
              <span class="hero-stat-label">Colleges</span>
            </div>
            <div class="hero-stat-divider"></div>
            <div class="hero-stat-item">
              <span class="hero-stat-num">₹<span class="counter" data-target="40">0</span>L+</span>
              <span class="hero-stat-label">Prize Pool</span>
            </div>
            <div class="hero-stat-divider"></div>
            <div class="hero-stat-item">
              <span class="hero-stat-num"><span class="counter" data-target="50">0</span>M+</span>
              <span class="hero-stat-label">ET Readers</span>
            </div>
          </div>
"""
html = re.sub(r'<div class="hero-stats-row">.*?</div>\s*</div>\s*</div>\s*</div>', hero_stats_new + '\n          </div>\n        </div>\n      </div>', html, flags=re.DOTALL, count=1)

# 2. Add Marquee Section right after Hero
marquee_html = """
  <!-- ==========================================================================
       02 SCALE, REACH & NATIONAL IMPACT (MARQUEE)
       ========================================================================== -->
  <section class="marquee-section" style="background: var(--bg-surface-elevated); padding: 40px 0; border-bottom: 1px solid var(--border-subtle); overflow: hidden;">
    <div class="container" style="text-align: center; margin-bottom: 24px;">
      <h2 style="font-size: 24px; font-weight: 800; color: var(--text-highlight); text-transform: uppercase;">Scale, Reach & National Impact</h2>
      <p style="font-size: 16px; color: var(--text-muted);">Backed by India's most authoritative financial media powerhouse and trusted by industry titans.</p>
    </div>
    <div class="marquee-wrapper" style="position: relative; width: 100%; display: flex; white-space: nowrap;">
      <div class="marquee-track" style="display: flex; gap: 40px; animation: scroll-left 20s linear infinite;">
        <!-- Track 1 -->
        <div class="marquee-item"><span style="font-weight: 800; font-size: 28px; color: var(--primary-color);">5,000+</span> <span style="font-size: 16px; color: var(--text-main); text-transform: uppercase; margin-left: 8px; font-weight: 600;">Builders & Students</span></div>
        <div class="marquee-item"><span style="font-weight: 800; font-size: 28px; color: var(--primary-color);">100+</span> <span style="font-size: 16px; color: var(--text-main); text-transform: uppercase; margin-left: 8px; font-weight: 600;">Colleges Reached</span></div>
        <div class="marquee-item"><span style="font-weight: 800; font-size: 28px; color: var(--primary-color);">200+</span> <span style="font-size: 16px; color: var(--text-main); text-transform: uppercase; margin-left: 8px; font-weight: 600;">AI Solutions Built</span></div>
        <div class="marquee-item"><span style="font-weight: 800; font-size: 28px; color: var(--primary-color);">50+</span> <span style="font-size: 16px; color: var(--text-main); text-transform: uppercase; margin-left: 8px; font-weight: 600;">Industry Mentors</span></div>
        <div class="marquee-item"><span style="font-weight: 800; font-size: 28px; color: var(--primary-color);">20+</span> <span style="font-size: 16px; color: var(--text-main); text-transform: uppercase; margin-left: 8px; font-weight: 600;">Cities Represented</span></div>
        <div class="marquee-item"><span style="font-weight: 800; font-size: 28px; color: var(--primary-color);">10+</span> <span style="font-size: 16px; color: var(--text-main); text-transform: uppercase; margin-left: 8px; font-weight: 600;">Winning Teams Funded</span></div>
        <!-- Duplicate for infinite effect -->
        <div class="marquee-item"><span style="font-weight: 800; font-size: 28px; color: var(--primary-color);">5,000+</span> <span style="font-size: 16px; color: var(--text-main); text-transform: uppercase; margin-left: 8px; font-weight: 600;">Builders & Students</span></div>
        <div class="marquee-item"><span style="font-weight: 800; font-size: 28px; color: var(--primary-color);">100+</span> <span style="font-size: 16px; color: var(--text-main); text-transform: uppercase; margin-left: 8px; font-weight: 600;">Colleges Reached</span></div>
        <div class="marquee-item"><span style="font-weight: 800; font-size: 28px; color: var(--primary-color);">200+</span> <span style="font-size: 16px; color: var(--text-main); text-transform: uppercase; margin-left: 8px; font-weight: 600;">AI Solutions Built</span></div>
        <div class="marquee-item"><span style="font-weight: 800; font-size: 28px; color: var(--primary-color);">50+</span> <span style="font-size: 16px; color: var(--text-main); text-transform: uppercase; margin-left: 8px; font-weight: 600;">Industry Mentors</span></div>
        <div class="marquee-item"><span style="font-weight: 800; font-size: 28px; color: var(--primary-color);">20+</span> <span style="font-size: 16px; color: var(--text-main); text-transform: uppercase; margin-left: 8px; font-weight: 600;">Cities Represented</span></div>
        <div class="marquee-item"><span style="font-weight: 800; font-size: 28px; color: var(--primary-color);">10+</span> <span style="font-size: 16px; color: var(--text-main); text-transform: uppercase; margin-left: 8px; font-weight: 600;">Winning Teams Funded</span></div>
      </div>
    </div>
  </section>
"""

# Insert Marquee right after Hero Section
html = html.replace('  <!-- ==========================================================================\n       04 ABOUT THE HACKATHON', marquee_html + '\n  <!-- ==========================================================================\n       04 ABOUT THE HACKATHON')

# 3. Change About heading
html = html.replace("India's Definitive AI Innovation Catalyst", "Where India's Enterprise AI Future is Written")

# 4. Make "Why Sponsor" cards colorful. 
# We'll replace the existing sponsor cards with bright gradients.
for i in range(1, 7):
    # Using vibrant gradients based on index
    gradients = [
        "linear-gradient(135deg, #FF9A9E 0%, #FECFEF 100%)",
        "linear-gradient(135deg, #a18cd1 0%, #fbc2eb 100%)",
        "linear-gradient(135deg, #84fab0 0%, #8fd3f4 100%)",
        "linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%)",
        "linear-gradient(135deg, #cfd9df 0%, #e2ebf0 100%)",
        "linear-gradient(135deg, #fbc2eb 0%, #a6c1ee 100%)"
    ]
    grad = gradients[i-1]
    
    # We find the sponsor card structure and inject inline styles. We'll replace '<div class="sponsor-benefit-card card" style="position: relative;">' 
    # but currently we don't know the exact class. Let's look up how sponsor cards were defined.
    # Actually, they might be '<div class="sponsor-benefit-card card">' or have inline style.
    pass

# We will let a CSS append handle the sponsor cards and How It Works instead of regex string replacements to avoid breakage.

# Add custom CSS and JS at the end of body/head
custom_style = """
<style>
/* Counter animation */
.counter { display: inline-block; }
/* Marquee */
@keyframes scroll-left {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}
.marquee-item { display: inline-flex; align-items: center; background: var(--bg-surface); padding: 12px 32px; border-radius: 100px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); border: 1px solid var(--border-subtle); }

/* Colorful Sponsor Play Cards */
.sponsor-benefits-grid .card:nth-child(1) { background: linear-gradient(135deg, #FFE2E2 0%, #FFF3F3 100%); border-color: #FFA4A4; box-shadow: 0 10px 30px rgba(255, 164, 164, 0.2); }
.sponsor-benefits-grid .card:nth-child(2) { background: linear-gradient(135deg, #E2F0FF 0%, #F3F8FF 100%); border-color: #A4D1FF; box-shadow: 0 10px 30px rgba(164, 209, 255, 0.2); }
.sponsor-benefits-grid .card:nth-child(3) { background: linear-gradient(135deg, #E2FFE9 0%, #F3FFF6 100%); border-color: #A4FFBE; box-shadow: 0 10px 30px rgba(164, 255, 190, 0.2); }
.sponsor-benefits-grid .card:nth-child(4) { background: linear-gradient(135deg, #F3E2FF 0%, #F9F3FF 100%); border-color: #D1A4FF; box-shadow: 0 10px 30px rgba(209, 164, 255, 0.2); }
.sponsor-benefits-grid .card:nth-child(5) { background: linear-gradient(135deg, #FFF5E2 0%, #FFFBF3 100%); border-color: #FFDDA4; box-shadow: 0 10px 30px rgba(255, 221, 164, 0.2); }
.sponsor-benefits-grid .card:nth-child(6) { background: linear-gradient(135deg, #FFE2F0 0%, #FFF3F8 100%); border-color: #FFA4D1; box-shadow: 0 10px 30px rgba(255, 164, 209, 0.2); }

/* Horizontal How It Works */
.how-it-works-grid {
  display: flex !important;
  flex-direction: row !important;
  align-items: stretch;
  gap: 16px !important;
  overflow-x: auto;
  padding-bottom: 24px;
}
.how-it-works-grid > div {
  flex: 1;
  min-width: 250px;
  position: relative;
}
/* Arrow */
.how-it-works-grid > div:not(:last-child)::after {
  content: '➔';
  position: absolute;
  top: 50%;
  right: -20px;
  transform: translateY(-50%);
  font-size: 24px;
  color: var(--primary-color);
  z-index: 10;
}
@media (max-width: 768px) {
  .how-it-works-grid { flex-direction: column !important; overflow-x: visible; }
  .how-it-works-grid > div:not(:last-child)::after {
    content: '↓';
    top: auto;
    bottom: -20px;
    right: 50%;
    transform: translateX(50%);
  }
}
</style>
"""
html = html.replace('</head>', custom_style + '\n</head>')

custom_js = """
<script>
document.addEventListener('DOMContentLoaded', () => {
  const counters = document.querySelectorAll('.counter');
  const speed = 200; // The lower the slower
  
  const animateCounters = (entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const counter = entry.target;
        const target = +counter.getAttribute('data-target');
        const updateCount = () => {
          const count = +counter.innerText;
          const inc = target / speed;
          if (count < target) {
            counter.innerText = Math.ceil(count + inc);
            setTimeout(updateCount, 15);
          } else {
            counter.innerText = target;
          }
        };
        updateCount();
        observer.unobserve(counter);
      }
    });
  };

  const observer = new IntersectionObserver(animateCounters, { threshold: 0.5 });
  counters.forEach(counter => {
    observer.observe(counter);
  });
});
</script>
"""
html = html.replace('</body>', custom_js + '\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
