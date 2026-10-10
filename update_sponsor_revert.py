import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

match = re.search(r'<section id="sponsor".*?</section>', html, re.DOTALL)
if match:
    new_section = """<section id="sponsor" class="section-pad sponsor-section" style="background: #4F46E5; color: #fff;">
    <div class="container">
      <div class="section-head centered">
        <div class="sponsor-highlight-badge" style="color: #fff; background: rgba(255,255,255,0.2); border: 1px solid rgba(255,255,255,0.3); display: inline-block; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: 700; margin-bottom: 16px;"> Enterprise Partnership Invitational 2026</div>
        <h2 class="section-title" style="color: #fff;">Why Sponsor the ET AI Hackathon?</h2>
        <p class="section-desc" style="max-width: 760px; color: rgba(255,255,255,0.9); margin: 0 auto;">
          Co-create India's premier AI milestone with The Economic Times. Drive real-world developer platform adoption, acquire top 1% engineering talent, and position your brand leadership at the forefront of the generative revolution.
        </p>
      </div>

      <div class="sponsor-benefits-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 24px; margin-top: 40px;">
        
        <div class="sponsor-benefit-card card" style="background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: var(--radius-md); padding: 24px; display: flex; gap: 16px; align-items: flex-start; transition: all var(--transition-smooth);">
          <div style="font-family: Georgia, serif; font-size: 24px; color: var(--primary-color); font-weight: bold; line-height: 1;">01</div>
          <div>
            <h3 style="font-size: 16px; color: var(--text-highlight); margin-bottom: 8px;">Co-Branded Visibility</h3>
            <p style="font-size: 14px; color: var(--text-muted); line-height: 1.5; margin: 0;">Media creatives, newsletters, and hackathon microsite visibility across all digital co-branded assets.</p>
          </div>
        </div>
        
        <div class="sponsor-benefit-card card" style="background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: var(--radius-md); padding: 24px; display: flex; gap: 16px; align-items: flex-start; transition: all var(--transition-smooth);">
          <div style="font-family: Georgia, serif; font-size: 24px; color: var(--primary-color); font-weight: bold; line-height: 1;">02</div>
          <div>
            <h3 style="font-size: 16px; color: var(--text-highlight); margin-bottom: 8px;">Platform Adoption</h3>
            <p style="font-size: 14px; color: var(--text-muted); line-height: 1.5; margin: 0;">Platform, APIs, or tools used during the hackathon driving real-world usage from India's top builders.</p>
          </div>
        </div>

        <div class="sponsor-benefit-card card" style="background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: var(--radius-md); padding: 24px; display: flex; gap: 16px; align-items: flex-start; transition: all var(--transition-smooth);">
          <div style="font-family: Georgia, serif; font-size: 24px; color: var(--primary-color); font-weight: bold; line-height: 1;">03</div>
          <div>
            <h3 style="font-size: 16px; color: var(--text-highlight); margin-bottom: 8px;">Podcast Leadership</h3>
            <p style="font-size: 14px; color: var(--text-muted); line-height: 1.5; margin: 0;">Dedicated episode on ET's YouTube and social channels putting your voice at the centre of AI conversation.</p>
          </div>
        </div>

        <div class="sponsor-benefit-card card" style="background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: var(--radius-md); padding: 24px; display: flex; gap: 16px; align-items: flex-start; transition: all var(--transition-smooth);">
          <div style="font-family: Georgia, serif; font-size: 24px; color: var(--primary-color); font-weight: bold; line-height: 1;">04</div>
          <div>
            <h3 style="font-size: 16px; color: var(--text-highlight); margin-bottom: 8px;">Hiring Access</h3>
            <p style="font-size: 14px; color: var(--text-muted); line-height: 1.5; margin: 0;">Direct pipeline to India's top AI talent. Validated builders shortlisted through rigorous evaluation.</p>
          </div>
        </div>

        <div class="sponsor-benefit-card card" style="background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: var(--radius-md); padding: 24px; display: flex; gap: 16px; align-items: flex-start; transition: all var(--transition-smooth);">
          <div style="font-family: Georgia, serif; font-size: 24px; color: var(--primary-color); font-weight: bold; line-height: 1;">05</div>
          <div>
            <h3 style="font-size: 16px; color: var(--text-highlight); margin-bottom: 8px;">Candidate Workshop</h3>
            <p style="font-size: 14px; color: var(--text-muted); line-height: 1.5; margin: 0;">Direct engagement session with shortlisted participants to explore collaboration or recruitment.</p>
          </div>
        </div>

        <div class="sponsor-benefit-card card" style="background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: var(--radius-md); padding: 24px; display: flex; gap: 16px; align-items: flex-start; transition: all var(--transition-smooth);">
          <div style="font-family: Georgia, serif; font-size: 24px; color: var(--primary-color); font-weight: bold; line-height: 1;">06</div>
          <div>
            <h3 style="font-size: 16px; color: var(--text-highlight); margin-bottom: 8px;">Website Banners</h3>
            <p style="font-size: 14px; color: var(--text-muted); line-height: 1.5; margin: 0;">Prime placement on The Economic Times homepage and landing pages reaching 50M+ readers.</p>
          </div>
        </div>
      </div>
    </div>
  </section>"""
    
    html = html.replace(match.group(0), new_section)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('Reverted sponsor section layout but kept blue background!')
else:
    print('Not found')
