import re

# --- UPDATE STYLES.CSS ---
with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

new_root = """:root {
  --primary-color: #f43f5e;
  --primary-glow: rgba(244, 63, 94, 0.4);
  --primary-light: #fb7185;
  --primary-dark: #e11d48;
  
  --secondary-color: #FFCC00; /* Yellow from image */
  --secondary-glow: rgba(255, 204, 0, 0.3);
  
  --bg-deep: #FAF8F5;
  --bg-dark: #F3F0EB;
  --bg-surface: #FFFFFF;
  --bg-surface-elevated: #FFFFFF;
  --bg-surface-hover: #F9F6F0;
  
  --border-subtle: rgba(0, 0, 0, 0.06);
  --border-medium: rgba(0, 0, 0, 0.12);

  --text-main: #1e293b;
  --text-muted: #475569;
  --text-dim: #94a3b8;
  --text-highlight: #0f172a;

  --font-sans: 'Space Grotesk', 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-mono: 'JetBrains Mono', 'IBM Plex Mono', ui-monospace, monospace;

  --radius-sm: 6px;
  --radius-md: 10px;
  --radius-lg: 16px;
  --radius-xl: 24px;
  --radius-full: 9999px;

  --shadow-card: 0 10px 40px -10px rgba(0, 0, 0, 0.08);
  --shadow-modal: 0 25px 50px -12px rgba(0, 0, 0, 0.15);
  
  --transition-fast: 0.18s cubic-bezier(0.16, 1, 0.3, 1);
  --transition-smooth: 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}"""

css = re.sub(r':root\s*\{.*?\}', new_root, css, flags=re.DOTALL)

# Let's add some utility classes for the new hero styles and logo grid
custom_css = """
/* Hero Blob Glow */
.hero-glow-blob {
  position: absolute;
  top: 0;
  left: 0;
  width: 500px;
  height: 500px;
  background: radial-gradient(circle, rgba(244,63,94,0.15) 0%, rgba(244,63,94,0) 70%);
  z-index: -1;
  pointer-events: none;
}
.hero-title-gradient {
  background: linear-gradient(90deg, #f43f5e 0%, #fb7185 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.hero-badge-pink {
  display: inline-block;
  padding: 6px 16px;
  border-radius: 100px;
  background: #FFF0F2;
  border: 1px solid #FFD1DA;
  color: #F43F5E;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 1px;
  margin-bottom: 24px;
}
.partner-grid-yellow {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 40px;
  align-items: center;
  justify-items: center;
  padding: 60px 0;
}
.partner-grid-yellow .logo-text {
  font-size: 32px;
  font-weight: 900;
  color: #111;
  letter-spacing: -1px;
  text-transform: lowercase;
}
"""
css += custom_css

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

# --- UPDATE INDEX.HTML ---
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace body background style if any, though it uses css vars now
# Ensure hero section uses the new cream background and the exact layout
hero_replacement = """  <section class="hero-section" style="position: relative; background-color: var(--bg-deep); z-index: 1;">
    <div class="hero-glow-blob"></div>
    <div class="container">
      <div class="hero-split">
        <!-- Left Side — Branding & Content -->
        <div class="hero-left" style="position: relative;">
          <!-- Superbadge -->
          <div class="hero-badge-pink">
            <span>✦</span> INDIA'S LARGEST ENTERPRISE & DEVELOPER GENERATIVE AI MARATHON <span>✦</span>
          </div>

          <!-- Main Title -->
          <h1 class="hero-title" style="color: var(--text-highlight); font-size: 80px; line-height: 1; letter-spacing: -2px; margin-bottom: 24px;">
            ET AI <span class="hero-title-gradient">HACKATHON</span><br>2026
          </h1>

          <!-- Subtitle / Tagline -->
          <p class="hero-tagline" id="hero-tagline" style="color: var(--text-muted); font-size: 18px; max-width: 500px;">
            Where India's sharpest AI builders meet the enterprise challenges that matter — and build what's next. 
            Powered by <strong style="color: var(--text-highlight);">The Economic Times</strong>, Fortune 500 partners, and 50M+ national reader reach.
          </p>

          <div class="hero-stats-row">
            <div class="hero-stat-item">
              <span class="hero-stat-num" style="color: var(--text-highlight);"><span class="counter" data-target="5000">0</span>+</span>
              <span class="hero-stat-label">Builders</span>
            </div>
            <div class="hero-stat-divider"></div>
            <div class="hero-stat-item">
              <span class="hero-stat-num" style="color: var(--text-highlight);"><span class="counter" data-target="100">0</span>+</span>
              <span class="hero-stat-label">Colleges</span>
            </div>
            <div class="hero-stat-divider"></div>
            <div class="hero-stat-item">
              <span class="hero-stat-num" style="color: var(--text-highlight);">₹<span class="counter" data-target="40">0</span>L+</span>
              <span class="hero-stat-label">Prize Pool</span>
            </div>
            <div class="hero-stat-divider"></div>
            <div class="hero-stat-item">
              <span class="hero-stat-num" style="color: var(--text-highlight);"><span class="counter" data-target="50">0</span>M+</span>
              <span class="hero-stat-label">ET Readers</span>
            </div>
          </div>
        </div>

        <!-- Right Side — Enquiry Form -->
        <div class="hero-right" style="flex: 1; min-width: 320px; background: #fff; padding: 40px; border-radius: 16px; box-shadow: var(--shadow-card); position: relative; overflow: hidden;">
          <div style="position: absolute; top: 0; left: 0; width: 100%; height: 4px; background: linear-gradient(90deg, #06b6d4, #f43f5e);"></div>
          
          <div style="display: inline-block; padding: 4px 12px; background: #F0F9FF; color: #0284C7; border-radius: 100px; font-size: 11px; font-weight: 700; margin-bottom: 16px;">
            🚀 Limited Sponsor Slots Available
          </div>
          
          <h3 style="font-size: 24px; color: var(--text-highlight); margin-bottom: 8px; font-weight: 800;">Become a Sponsor Partner</h3>
          <p style="font-size: 14px; color: var(--text-muted); margin-bottom: 24px; line-height: 1.5;">Get the sponsor deck & connect with our partnerships team. Takes 30 seconds.</p>
          
          <form id="hero-enquiry-form" style="display: flex; flex-direction: column; gap: 16px;">
            <div>
              <label style="display: block; font-size: 10px; font-weight: 700; color: var(--text-dim); text-transform: uppercase; margin-bottom: 6px; letter-spacing: 1px;">Full Name *</label>
              <input type="text" placeholder="Priya Sharma" required style="width: 100%; padding: 12px 16px; border-radius: 8px; border: 1px solid var(--border-medium); background: #fafafa; color: var(--text-main); font-size: 15px;">
            </div>
            <div>
              <label style="display: block; font-size: 10px; font-weight: 700; color: var(--text-dim); text-transform: uppercase; margin-bottom: 6px; letter-spacing: 1px;">Work Email *</label>
              <input type="email" placeholder="priya@company.com" required style="width: 100%; padding: 12px 16px; border-radius: 8px; border: 1px solid var(--border-medium); background: #fafafa; color: var(--text-main); font-size: 15px;">
            </div>
            <div>
              <label style="display: block; font-size: 10px; font-weight: 700; color: var(--text-dim); text-transform: uppercase; margin-bottom: 6px; letter-spacing: 1px;">Phone Number *</label>
              <input type="text" placeholder="+91 98765 43210" required style="width: 100%; padding: 12px 16px; border-radius: 8px; border: 1px solid var(--border-medium); background: #fafafa; color: var(--text-main); font-size: 15px;">
            </div>
            <button type="submit" class="btn btn-primary" style="margin-top: 8px; width: 100%; padding: 14px; border-radius: 8px; font-weight: 700; background: var(--primary-color); border: none;">Submit Details</button>
          </form>
        </div>

      </div>
  </section>"""

# Find the entire hero section and replace it
html = re.sub(r'<section class="hero-section">.*?</section>', hero_replacement, html, flags=re.DOTALL)

# Insert the Yellow Partners Section directly after the Marquee Section
yellow_partners = """
  <!-- ==========================================================================
       TECH PARTNERS (YELLOW GRID)
       ========================================================================== -->
  <section style="background-color: var(--secondary-color); padding: 80px 0;">
    <div class="container">
      <div style="text-align: center; margin-bottom: 40px;">
        <h2 style="font-size: 32px; font-weight: 900; color: #111;">Strategic Tech Partners</h2>
      </div>
      <div class="partner-grid-yellow">
        <div class="logo-text" style="font-family: Arial, sans-serif;">accenture</div>
        <div class="logo-text" style="font-family: 'Segoe UI', sans-serif;">Microsoft</div>
        <div class="logo-text" style="font-family: 'Product Sans', sans-serif;">Google</div>
        <div class="logo-text" style="font-family: 'Amazon Ember', sans-serif; font-weight: 700;">aws</div>
        <div class="logo-text" style="font-family: Arial, sans-serif;">IBM</div>
        <div class="logo-text" style="font-family: Helvetica, sans-serif; letter-spacing: 2px; text-transform: uppercase;">Intel</div>
        <div class="logo-text" style="font-family: 'Helvetica Neue', sans-serif;">Meta</div>
        <div class="logo-text" style="font-family: Arial, sans-serif; font-style: italic;">NVIDIA</div>
      </div>
      <div style="text-align: center; margin-top: 20px;">
        <button style="background: #111; color: #fff; border: none; padding: 12px 32px; font-size: 14px; font-weight: 700; letter-spacing: 1px; text-transform: uppercase; cursor: pointer;">Load More</button>
      </div>
    </div>
  </section>
"""

# Insert after marquee section
html = re.sub(r'(</section>\s*)(<!-- ==========================================================================\s*04 ABOUT)', r'\1' + yellow_partners + r'\n\2', html, flags=re.DOTALL)


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
