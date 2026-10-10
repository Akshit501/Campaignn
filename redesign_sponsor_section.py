import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx_start = html.find('<section id="sponsor"')
if idx_start != -1:
    idx_end = html.find('</section>', idx_start) + len('</section>')
    
    old_section = html[idx_start:idx_end]
    
    new_section = """<section id="sponsor" class="section-pad sponsor-section" style="background: linear-gradient(135deg, #0F172A 0%, #1E1B4B 100%); color: #fff; position: relative; overflow: hidden;">
    <!-- Abstract glow -->
    <div style="position: absolute; top: -20%; left: -10%; width: 50%; height: 50%; background: radial-gradient(circle, rgba(99,102,241,0.15) 0%, transparent 70%); border-radius: 50%; pointer-events: none;"></div>
    <div style="position: absolute; bottom: -20%; right: -10%; width: 50%; height: 50%; background: radial-gradient(circle, rgba(236,72,153,0.15) 0%, transparent 70%); border-radius: 50%; pointer-events: none;"></div>
    
    <div class="container" style="position: relative; z-index: 1;">
      <div class="section-head centered">
        <div class="sponsor-highlight-badge" style="color: #fff; background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); backdrop-filter: blur(8px); display: inline-block; padding: 6px 16px; border-radius: 20px; font-size: 12px; font-weight: 700; margin-bottom: 24px; letter-spacing: 1px; text-transform: uppercase;"> Enterprise Partnership Invitational 2026</div>
        <h2 class="section-title" style="color: #fff; font-size: 42px; font-weight: 800; margin-bottom: 24px;">Why Sponsor the ET AI Hackathon?</h2>
        <p class="section-desc" style="max-width: 760px; color: rgba(255,255,255,0.7); margin: 0 auto; font-size: 18px; line-height: 1.6;">
          Co-create India's premier AI milestone with The Economic Times. Drive real-world developer platform adoption, acquire top 1% engineering talent, and position your brand leadership at the forefront of the generative revolution.
        </p>
      </div>

      <style>
        .premium-card {
          background: rgba(255, 255, 255, 0.03);
          border: 1px solid rgba(255, 255, 255, 0.08);
          border-radius: 20px;
          padding: 32px;
          position: relative;
          overflow: hidden;
          transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
          backdrop-filter: blur(12px);
          display: flex;
          flex-direction: column;
          height: 100%;
        }
        .premium-card:hover {
          transform: translateY(-8px);
          background: rgba(255, 255, 255, 0.06);
          border-color: rgba(255, 255, 255, 0.2);
          box-shadow: 0 20px 40px rgba(0,0,0,0.4);
        }
        .premium-card::before {
          content: '';
          position: absolute;
          top: 0; left: 0; width: 100%; height: 2px;
          background: linear-gradient(90deg, transparent, rgba(255,255,255,0.5), transparent);
          opacity: 0;
          transition: opacity 0.4s ease;
        }
        .premium-card:hover::before {
          opacity: 1;
        }
        .card-number {
          position: absolute;
          top: -10px;
          right: 10px;
          font-size: 120px;
          font-weight: 900;
          color: rgba(255,255,255,0.03);
          line-height: 1;
          pointer-events: none;
          transition: color 0.4s ease;
        }
        .premium-card:hover .card-number {
          color: rgba(255,255,255,0.06);
        }
      </style>

      <div class="sponsor-benefits-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 32px; margin-top: 60px;">
        
        <div class="premium-card">
          <div class="card-number">01</div>
          <div style="width: 48px; height: 48px; border-radius: 12px; background: rgba(99,102,241,0.2); color: #818cf8; display: flex; align-items: center; justify-content: center; margin-bottom: 24px; font-size: 24px;">
            <svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height="24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg>
          </div>
          <h3 style="font-size: 22px; color: #fff; margin-bottom: 12px; font-weight: 700;">Co-Branded Visibility</h3>
          <p style="font-size: 15px; color: rgba(255,255,255,0.6); line-height: 1.6; margin: 0;">Media creatives, newsletters, and hackathon microsite visibility across all digital co-branded assets.</p>
        </div>
        
        <div class="premium-card">
          <div class="card-number">02</div>
          <div style="width: 48px; height: 48px; border-radius: 12px; background: rgba(236,72,153,0.2); color: #f472b6; display: flex; align-items: center; justify-content: center; margin-bottom: 24px; font-size: 24px;">
            <svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height="24" width="24" xmlns="http://www.w3.org/2000/svg"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg>
          </div>
          <h3 style="font-size: 22px; color: #fff; margin-bottom: 12px; font-weight: 700;">Platform Adoption</h3>
          <p style="font-size: 15px; color: rgba(255,255,255,0.6); line-height: 1.6; margin: 0;">Platform, APIs, or tools used during the hackathon driving real-world usage from India's top builders.</p>
        </div>

        <div class="premium-card">
          <div class="card-number">03</div>
          <div style="width: 48px; height: 48px; border-radius: 12px; background: rgba(16,185,129,0.2); color: #34d399; display: flex; align-items: center; justify-content: center; margin-bottom: 24px; font-size: 24px;">
            <svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height="24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"></path><path d="M19 10v2a7 7 0 0 1-14 0v-2"></path><line x1="12" y1="19" x2="12" y2="23"></line><line x1="8" y1="23" x2="16" y2="23"></line></svg>
          </div>
          <h3 style="font-size: 22px; color: #fff; margin-bottom: 12px; font-weight: 700;">Podcast Leadership</h3>
          <p style="font-size: 15px; color: rgba(255,255,255,0.6); line-height: 1.6; margin: 0;">Dedicated episode on ET's YouTube and social channels putting your voice at the centre of AI conversation.</p>
        </div>

        <div class="premium-card">
          <div class="card-number">04</div>
          <div style="width: 48px; height: 48px; border-radius: 12px; background: rgba(245,158,11,0.2); color: #fbbf24; display: flex; align-items: center; justify-content: center; margin-bottom: 24px; font-size: 24px;">
            <svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height="24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
          </div>
          <h3 style="font-size: 22px; color: #fff; margin-bottom: 12px; font-weight: 700;">Hiring Access</h3>
          <p style="font-size: 15px; color: rgba(255,255,255,0.6); line-height: 1.6; margin: 0;">Direct pipeline to India's top AI talent. Validated builders shortlisted through rigorous evaluation.</p>
        </div>

        <div class="premium-card">
          <div class="card-number">05</div>
          <div style="width: 48px; height: 48px; border-radius: 12px; background: rgba(56,189,248,0.2); color: #38bdf8; display: flex; align-items: center; justify-content: center; margin-bottom: 24px; font-size: 24px;">
            <svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height="24" width="24" xmlns="http://www.w3.org/2000/svg"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="3" y1="9" x2="21" y2="9"></line><line x1="9" y1="21" x2="9" y2="9"></line></svg>
          </div>
          <h3 style="font-size: 22px; color: #fff; margin-bottom: 12px; font-weight: 700;">Candidate Workshop</h3>
          <p style="font-size: 15px; color: rgba(255,255,255,0.6); line-height: 1.6; margin: 0;">Direct engagement session with shortlisted participants to explore collaboration or recruitment.</p>
        </div>

        <div class="premium-card">
          <div class="card-number">06</div>
          <div style="width: 48px; height: 48px; border-radius: 12px; background: rgba(167,139,250,0.2); color: #a78bfa; display: flex; align-items: center; justify-content: center; margin-bottom: 24px; font-size: 24px;">
            <svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height="24" width="24" xmlns="http://www.w3.org/2000/svg"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline></svg>
          </div>
          <h3 style="font-size: 22px; color: #fff; margin-bottom: 12px; font-weight: 700;">Website Banners</h3>
          <p style="font-size: 15px; color: rgba(255,255,255,0.6); line-height: 1.6; margin: 0;">Prime placement on The Economic Times homepage and landing pages reaching 50M+ readers.</p>
        </div>
      </div>
    </div>
  </section>"""
    
    html = html.replace(old_section, new_section)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Replaced Sponsor section with premium cards!")
else:
    print("Could not find sponsor section.")
