import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('<section class="hero-section"')
end = html.find('</section>', idx) + 10

old_hero = html[idx:end]

new_hero = """<section class="hero-section dark-hero" style="position: relative; background-color: #050508; z-index: 1; overflow: hidden; padding-top: 60px; padding-bottom: 80px;">
    <!-- Decorative Glowing Stars -->
    <div style="position: absolute; bottom: -100px; left: -100px; width: 400px; height: 400px; background: radial-gradient(circle, rgba(0,255,255,0.4) 0%, rgba(0,255,255,0) 60%); z-index: -1;"></div>
    <div style="position: absolute; bottom: 0; left: 0; width: 250px; height: 250px; z-index: -1; opacity: 0.8; filter: drop-shadow(0 0 40px #00ffff);">
      <svg viewBox="0 0 100 100" style="width: 100%; height: 100%;"><path d="M50 0 Q50 50 100 50 Q50 50 50 100 Q50 50 0 50 Q50 50 50 0 Z" fill="#00f0ff"/></svg>
    </div>

    <div style="position: absolute; top: -100px; right: -100px; width: 500px; height: 500px; background: radial-gradient(circle, rgba(255,100,50,0.3) 0%, rgba(255,50,150,0.1) 40%, rgba(0,0,0,0) 70%); z-index: -1;"></div>
    <div style="position: absolute; top: 0; right: 0; width: 300px; height: 300px; z-index: -1; opacity: 0.8; filter: drop-shadow(0 0 40px #ff5a00);">
      <svg viewBox="0 0 100 100" style="width: 100%; height: 100%;"><path d="M50 0 Q50 50 100 50 Q50 50 50 100 Q50 50 0 50 Q50 50 50 0 Z" fill="#ff7300"/></svg>
    </div>

    <div class="container">
      <div class="hero-split" style="display: grid; grid-template-columns: 1.15fr 0.85fr; gap: 60px; align-items: center;">
        
        <!-- Left Side: Content -->
        <div class="hero-left" style="position: relative; color: #fff;">
          
          <!-- Box Logo -->
          <div style="display: inline-block; border: 2px solid #fff; padding: 12px 24px; margin-bottom: 32px; border-radius: 4px; text-align: center; position: relative; background: rgba(255,255,255,0.02);">
            <div style="font-size: 11px; font-weight: 700; letter-spacing: 1px; color: #fff; margin-bottom: 8px; display: flex; align-items: center; justify-content: center; gap: 8px;">
              <span style="background: #f43f5e; color: #fff; padding: 2px 6px; border-radius: 2px; font-size: 10px;">ET</span>
              <span>The Economic Times</span>
            </div>
            
            <div style="font-size: 42px; font-weight: 900; line-height: 1; letter-spacing: -1px; display: flex; align-items: center; justify-content: center; gap: 12px; margin-bottom: 8px;">
              <span style="color: #00f0ff;">&lt;</span>
              <span>AI HACKATHON</span>
              <span style="color: #00f0ff;">&lt;</span>
              <span>2.0</span>
              <span style="color: #ff7300;">&gt;</span>
            </div>

            <div style="font-size: 10px; font-weight: 700; letter-spacing: 3px; color: #a1a1aa; text-transform: uppercase;">
              Think AI. Build with GenAI.
            </div>
          </div>

          <!-- Main Title -->
          <h1 style="font-size: 64px; line-height: 1.1; font-weight: 900; letter-spacing: -2px; margin-bottom: 24px;">
            <span style="background: linear-gradient(90deg, #00f0ff 0%, #3b82f6 50%, #8b5cf6 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">BUILD. INNOVATE.<br></span>
            <span style="color: #fff;">MAKE AN IMPACT.</span>
          </h1>

          <!-- Description -->
          <p style="font-size: 18px; line-height: 1.6; color: #d1d5db; max-width: 500px; margin-bottom: 40px;">
            Join India's largest GenAI Hackathon and turn your ideas into real-world solutions. Build, collaborate and create the future with AI.
          </p>

          <!-- Partners -->
          <div style="display: flex; gap: 48px; align-items: center;">
            <div>
              <div style="font-size: 11px; color: #a1a1aa; font-weight: 600; margin-bottom: 8px; text-transform: uppercase;">Industry Partner</div>
              <div style="display: flex; align-items: center; gap: 8px;">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zm-2-12.5A2.5 2.5 0 0 0 7.5 10c0 1.38 1.12 2.5 2.5 2.5s2.5-1.12 2.5-2.5S11.38 7.5 10 7.5zm4 4A2.5 2.5 0 0 0 11.5 14c0 1.38 1.12 2.5 2.5 2.5s2.5-1.12 2.5-2.5S15.38 11.5 14 11.5z"></path></svg>
                <span style="font-weight: 800; font-size: 18px; letter-spacing: 1px; color: #fff;">OCTAVE</span>
              </div>
            </div>
            
            <!-- Separator -->
            <div style="width: 1px; height: 40px; background: rgba(255,255,255,0.2);"></div>

            <div>
              <div style="font-size: 11px; color: #a1a1aa; font-weight: 600; margin-bottom: 8px; text-transform: uppercase;">Associate Partner</div>
              <div style="display: flex; align-items: center; gap: 8px;">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path><path d="M2 12h20"></path></svg>
                <div style="display: flex; flex-direction: column; line-height: 1.1;">
                  <span style="font-weight: 800; font-size: 16px; letter-spacing: 1px; color: #fff;">POSSPOLE</span>
                  <span style="font-weight: 600; font-size: 12px; letter-spacing: 2px; color: #fff;">CATALYST</span>
                </div>
              </div>
            </div>
          </div>

        </div>

        <!-- Right Side: Form Card -->
        <div class="hero-right" style="background: #ffffff; padding: 48px 40px; border-radius: 16px; box-shadow: 0 20px 50px rgba(0,0,0,0.5); position: relative;">
          
          <h3 style="font-size: 26px; color: #0b0f19; margin-bottom: 12px; font-weight: 800; line-height: 1.2;">Be a Part of<br>The AI Hackathon 2.0</h3>
          <p style="font-size: 14px; color: #64748b; margin-bottom: 32px; line-height: 1.6;">Get the chance to build innovative solutions, collaborate with industry experts and win exciting opportunities.</p>
          
          <form id="hero-enquiry-form" class="js-lead-form" data-form-type="builder" style="display: flex; flex-direction: column; gap: 16px;" novalidate>
            <div>
              <label style="display: block; font-size: 10px; font-weight: 700; color: #64748b; text-transform: uppercase; margin-bottom: 8px; letter-spacing: 1px;">Full Name *</label>
              <input type="text" name="full_name" placeholder="Your Name" required style="width: 100%; padding: 14px 16px; border-radius: 8px; border: 1px solid #e2e8f0; background: #fafafa; color: #0f172a; font-size: 15px; outline: none;">
            </div>
            <div>
              <label style="display: block; font-size: 10px; font-weight: 700; color: #64748b; text-transform: uppercase; margin-bottom: 8px; letter-spacing: 1px;">Work Email *</label>
              <input type="email" name="email" placeholder="you@company.com" required style="width: 100%; padding: 14px 16px; border-radius: 8px; border: 1px solid #e2e8f0; background: #fafafa; color: #0f172a; font-size: 15px; outline: none;">
            </div>
            <div>
              <label style="display: block; font-size: 10px; font-weight: 700; color: #64748b; text-transform: uppercase; margin-bottom: 8px; letter-spacing: 1px;">Phone Number *</label>
              <input type="tel" name="phone" placeholder="+91 98765 43210" required style="width: 100%; padding: 14px 16px; border-radius: 8px; border: 1px solid #e2e8f0; background: #fafafa; color: #0f172a; font-size: 15px; outline: none;">
            </div>
            
            <!-- Hidden honeypot -->
            <input type="text" name="website" style="display:none" tabindex="-1">
            <div class="js-attribution-fields"></div>
            <p class="form-error" role="alert" style="color: #ef4444; font-size: 13px; font-weight: 500;"></p>

            <button type="submit" class="form-submit" style="margin-top: 16px; width: 100%; padding: 16px; border-radius: 8px; font-weight: 700; font-size: 15px; color: #fff; background: linear-gradient(90deg, #f43f5e 0%, #f97316 100%); border: none; cursor: pointer; transition: transform 0.2s, opacity 0.2s;">
              Register Now &rarr;
            </button>
          </form>
        </div>

      </div>
    </div>
  </section>"""

html = html.replace(old_hero, new_hero)

# We should also ensure the header (navbar) has a dark theme so it blends with the dark hero section.
# The user wants this "hero page" meaning the very top part. Let's make sure the .site-header is dark.
# Right now, site-header might have a light background. We can inject a <style> block to override header on this page.
style_override = """
<style>
  .site-header {
    background: transparent !important;
    border-bottom: none !important;
  }
  .site-header .et-crest { background: #f43f5e !important; color: #fff !important; }
  .site-header .et-main { color: #fff !important; }
  .site-header .nav-link { color: #d1d5db !important; }
  .site-header .nav-link:hover { color: #fff !important; }
</style>
"""

# Let's insert style override before </head>
head_end = html.find('</head>')
if head_end != -1 and "dark-hero" not in html[:head_end]:
    html = html[:head_end] + style_override + html[head_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated Hero section!")
