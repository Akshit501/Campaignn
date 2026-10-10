import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

match = re.search(r'<section id="sponsor".*?</section>', html, re.DOTALL)
if match:
    new_section = """<!-- ==========================================================================
       WHY SPONSOR
       ========================================================================== -->
  <section id="sponsor" class="section-pad" style="background: #4F46E5; color: #fff;">
    <div class="container" style="display: flex; flex-wrap: wrap; gap: 40px; align-items: center;">
      
      <!-- Left: Grid of Cards -->
      <div style="flex: 1.5; min-width: 320px;">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px;">
          
          <div class="card" style="background: #fff; border-radius: 12px; padding: 24px; color: #111; box-shadow: 0 10px 25px rgba(0,0,0,0.1);">
            <div style="font-size: 28px; margin-bottom: 12px;">📢</div>
            <h3 style="font-size: 18px; color: #111; margin-bottom: 8px;">Co-Branded Visibility</h3>
            <p style="font-size: 14px; color: #555; line-height: 1.5; margin: 0;">Media creatives, newsletters, and hackathon microsite visibility across all digital co-branded assets.</p>
          </div>
          
          <div class="card" style="background: #fff; border-radius: 12px; padding: 24px; color: #111; box-shadow: 0 10px 25px rgba(0,0,0,0.1);">
            <div style="font-size: 28px; margin-bottom: 12px;">⚙️</div>
            <h3 style="font-size: 18px; color: #111; margin-bottom: 8px;">Platform Adoption</h3>
            <p style="font-size: 14px; color: #555; line-height: 1.5; margin: 0;">Platform, APIs, or tools used during the hackathon driving real-world usage from India's top builders.</p>
          </div>

          <div class="card" style="background: #fff; border-radius: 12px; padding: 24px; color: #111; box-shadow: 0 10px 25px rgba(0,0,0,0.1);">
            <div style="font-size: 28px; margin-bottom: 12px;">🎙️</div>
            <h3 style="font-size: 18px; color: #111; margin-bottom: 8px;">Podcast Leadership</h3>
            <p style="font-size: 14px; color: #555; line-height: 1.5; margin: 0;">Dedicated episode on ET's YouTube and social channels putting your voice at the centre of AI conversation.</p>
          </div>

          <div class="card" style="background: #fff; border-radius: 12px; padding: 24px; color: #111; box-shadow: 0 10px 25px rgba(0,0,0,0.1);">
            <div style="font-size: 28px; margin-bottom: 12px;">🎯</div>
            <h3 style="font-size: 18px; color: #111; margin-bottom: 8px;">Hiring Access</h3>
            <p style="font-size: 14px; color: #555; line-height: 1.5; margin: 0;">Direct pipeline to India's top AI talent. Validated builders shortlisted through rigorous evaluation.</p>
          </div>

          <div class="card" style="background: #fff; border-radius: 12px; padding: 24px; color: #111; box-shadow: 0 10px 25px rgba(0,0,0,0.1);">
            <div style="font-size: 28px; margin-bottom: 12px;">🤝</div>
            <h3 style="font-size: 18px; color: #111; margin-bottom: 8px;">Candidate Workshop</h3>
            <p style="font-size: 14px; color: #555; line-height: 1.5; margin: 0;">Direct engagement session with shortlisted participants to explore collaboration or recruitment.</p>
          </div>

          <div class="card" style="background: #fff; border-radius: 12px; padding: 24px; color: #111; box-shadow: 0 10px 25px rgba(0,0,0,0.1);">
            <div style="font-size: 28px; margin-bottom: 12px;">💻</div>
            <h3 style="font-size: 18px; color: #111; margin-bottom: 8px;">Website Banners</h3>
            <p style="font-size: 14px; color: #555; line-height: 1.5; margin: 0;">Prime placement on The Economic Times homepage and landing pages reaching 50M+ readers.</p>
          </div>

        </div>
      </div>

      <!-- Right: Text Content -->
      <div style="flex: 1; min-width: 320px; padding: 20px;">
        <h2 style="font-size: 48px; font-weight: 800; color: #fff; line-height: 1.2; margin-bottom: 16px;">Why Sponsor<br>the ET AI Hackathon?</h2>
        <p style="font-size: 18px; color: rgba(255,255,255,0.9); line-height: 1.6;">
          Co-create India's premier AI milestone with The Economic Times. Drive real-world developer platform adoption, acquire top 1% engineering talent, and position your brand leadership at the forefront of the generative revolution.
        </p>
      </div>
      
    </div>
  </section>"""
    
    html = html.replace(match.group(0), new_section)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('Updated sponsor section!')
else:
    print('Not found')
