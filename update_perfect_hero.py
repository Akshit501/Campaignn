import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('<section class="hero-section')
end = html.find('</section>', idx) + 10

old_hero = html[idx:end]

new_hero = """<section class="hero-section" style="position: relative; background: #FEF6F5; z-index: 1; overflow: hidden; padding-top: 60px; padding-bottom: 80px;">
    <!-- Background elements -->
    <div style="position: absolute; bottom: -50px; left: -100px; width: 500px; height: 500px; background: radial-gradient(circle, rgba(244,63,94,0.15) 0%, rgba(244,63,94,0) 70%); z-index: -1;"></div>
    <div style="position: absolute; top: -50px; right: 0; width: 800px; height: 800px; background: radial-gradient(circle, rgba(254,205,211,0.6) 0%, rgba(254,205,211,0) 70%); z-index: -1;"></div>

    <!-- Decorative stars -->
    <svg style="position: absolute; right: 4%; top: 40%; width: 28px; opacity: 1;" viewBox="0 0 100 100"><path d="M50 0 Q50 50 100 50 Q50 50 50 100 Q50 50 0 50 Q50 50 50 0 Z" fill="#A855F7"/></svg>
    <svg style="position: absolute; right: 8%; top: 52%; width: 20px; opacity: 1;" viewBox="0 0 100 100"><path d="M50 0 Q50 50 100 50 Q50 50 50 100 Q50 50 0 50 Q50 50 50 0 Z" fill="#F97316"/></svg>
    <svg style="position: absolute; left: 45%; bottom: 15%; width: 16px; opacity: 1;" viewBox="0 0 100 100"><path d="M50 0 Q50 50 100 50 Q50 50 50 100 Q50 50 0 50 Q50 50 50 0 Z" fill="#8B5CF6"/></svg>

    <div class="container">
      <div class="hero-split" style="display: grid; grid-template-columns: 1.1fr 0.9fr; gap: 60px; align-items: center;">
        
        <!-- Left Side: Content -->
        <div class="hero-left" style="position: relative;">
          
          <!-- Box Logo with broken top border -->
          <div style="display: inline-block; border: 3px solid #111827; padding: 24px 32px; margin-bottom: 24px; text-align: center; position: relative; margin-top: 16px; background: transparent;">
            
            <!-- Logo overlapping top border -->
            <div style="position: absolute; top: -14px; left: 50%; transform: translateX(-50%); background: #FEF6F5; padding: 0 12px; display: flex; align-items: center; gap: 8px; white-space: nowrap;">
              <span style="background: #ef4444; color: #fff; padding: 2px 6px; font-size: 13px; font-weight: 800; border-radius: 2px;">ET</span>
              <span style="font-family: 'Times New Roman', serif; font-size: 16px; font-weight: 800; color: #111;">The Economic Times</span>
            </div>
            
            <div style="font-size: 42px; font-weight: 900; line-height: 1; display: flex; align-items: center; justify-content: center; gap: 12px; margin-bottom: 8px;">
              <span style="color: #06B6D4; transform: scaleY(1.5);">&lt;</span>
              <span style="color: #111827; font-family: sans-serif; letter-spacing: -1px; display: flex; align-items: center;">
                AI HACKATH
                <svg width="24" height="24" viewBox="0 0 100 100" style="margin: 0 2px;"><path d="M50 0 Q50 50 100 50 Q50 50 50 100 Q50 50 0 50 Q50 50 50 0 Z" fill="#111827"/></svg>
                N 2.0
              </span>
              <span style="color: #F97316; transform: scaleY(1.5);">&gt;</span>
            </div>

            <div style="font-size: 11px; font-weight: 700; letter-spacing: 4px; color: #111827; text-transform: uppercase;">
              Think AI. Build with GenAI.
            </div>
          </div>
          <br>

          <!-- Pill -->
          <div style="display: inline-block; padding: 6px 16px; border-radius: 100px; background: #FFF0F2; color: #F43F5E; font-size: 11px; font-weight: 800; letter-spacing: 1px; margin-bottom: 24px; border: 1px solid #FFE4E6;">
            <span>✦</span> INDIA'S LARGEST AI HACKATHON <span>✦</span>
          </div>

          <!-- Main Title -->
          <h1 style="font-size: 68px; line-height: 1.1; font-weight: 900; letter-spacing: -2px; margin-bottom: 24px;">
            <span style="color: #111827;">Build. Innovate.<br></span>
            <span style="background: linear-gradient(90deg, #F43F5E 0%, #A855F7 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Shape the Future.</span>
          </h1>

          <!-- Description -->
          <p style="font-size: 17px; line-height: 1.6; color: #64748B; max-width: 480px; margin-bottom: 40px; font-weight: 500;">
            Join India's biggest GenAI Hackathon and turn your ideas into real-world solutions. Build, collaborate and create the future with AI.
          </p>

          <!-- Stats Row (with animation) -->
          <div style="display: flex; gap: 24px; align-items: center; flex-wrap: wrap;">
            
            <!-- Builder Stat -->
            <div style="display: flex; align-items: center; gap: 12px;">
              <div style="width: 40px; height: 40px; border-radius: 50%; background: #FFE4E6; display: flex; align-items: center; justify-content: center;">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#F43F5E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
              </div>
              <div style="display: flex; flex-direction: column;">
                <span style="font-weight: 900; font-size: 18px; color: #111827;"><span class="counter" data-target="500">0</span>+</span>
                <span style="font-size: 10px; font-weight: 800; color: #94A3B8; text-transform: uppercase;">Builders</span>
              </div>
            </div>

            <!-- Divider -->
            <div style="width: 1px; height: 32px; background: #E2E8F0;"></div>

            <!-- Colleges Stat -->
            <div style="display: flex; align-items: center; gap: 12px;">
              <div style="width: 40px; height: 40px; border-radius: 50%; background: #F3E8FF; display: flex; align-items: center; justify-content: center;">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#A855F7" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 10v6M2 10l10-5 10 5-10 5z"></path><path d="M6 12v5c3 3 9 3 12 0v-5"></path></svg>
              </div>
              <div style="display: flex; flex-direction: column;">
                <span style="font-weight: 900; font-size: 18px; color: #111827;"><span class="counter" data-target="100">0</span>+</span>
                <span style="font-size: 10px; font-weight: 800; color: #94A3B8; text-transform: uppercase;">Colleges</span>
              </div>
            </div>

            <!-- Divider -->
            <div style="width: 1px; height: 32px; background: #E2E8F0;"></div>

            <!-- Prize Stat -->
            <div style="display: flex; align-items: center; gap: 12px;">
              <div style="width: 40px; height: 40px; border-radius: 50%; background: #FEF3C7; display: flex; align-items: center; justify-content: center;">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#D97706" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 21h8M12 17v4M7 4h10M6 4h12v9a6 6 0 0 1-12 0V4z"></path></svg>
              </div>
              <div style="display: flex; flex-direction: column;">
                <span style="font-weight: 900; font-size: 18px; color: #111827;">₹<span class="counter" data-target="40">0</span>L+</span>
                <span style="font-size: 10px; font-weight: 800; color: #94A3B8; text-transform: uppercase;">Prize Pool</span>
              </div>
            </div>

            <!-- Divider -->
            <div style="width: 1px; height: 32px; background: #E2E8F0;"></div>

            <!-- Readers Stat -->
            <div style="display: flex; align-items: center; gap: 12px;">
              <div style="width: 40px; height: 40px; border-radius: 50%; background: #D1FAE5; display: flex; align-items: center; justify-content: center;">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#059669" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"></rect><path d="M6 8h12M6 12h12M6 16h6"></path></svg>
              </div>
              <div style="display: flex; flex-direction: column;">
                <span style="font-weight: 900; font-size: 18px; color: #111827;"><span class="counter" data-target="50">0</span>M+</span>
                <span style="font-size: 10px; font-weight: 800; color: #94A3B8; text-transform: uppercase;">ET Readers</span>
              </div>
            </div>

          </div>
        </div>

        <!-- Right Side: Form Card -->
        <div class="hero-right" style="background: #ffffff; padding: 48px 40px; border-radius: 16px; box-shadow: 0 20px 60px rgba(244,63,94,0.08); position: relative;">
          
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

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated Hero section to perfectly match screenshot!")
