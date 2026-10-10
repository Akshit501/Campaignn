import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

match = re.search(r'<section id="audience".*?</section>', html, re.DOTALL)
if match:
    new_section = """<section id="audience" class="section-pad" style="background: #0F172A; color: #fff; border-top: 1px solid rgba(255,255,255,0.1); border-bottom: 1px solid rgba(255,255,255,0.1);">
  <div class="container">
    <div class="section-head centered">
      <h2 class="section-title" style="color: #fff;">Who Sees Your Brand</h2>
      <p class="section-desc" style="color: rgba(255,255,255,0.7);">The Economic Times audience — India's most influential business readership.</p>
    </div>

    <div class="audience-block" style="display: flex; flex-wrap: wrap; gap: 30px; margin-top: 40px;">
      
      <div class="audience-col" style="flex: 1; min-width: 300px; background: rgba(255,255,255,0.03); padding: 32px; border-radius: 16px; border: 1px solid rgba(255,255,255,0.05); box-shadow: 0 10px 30px rgba(0,0,0,0.2);">
        <h3 class="audience-title" style="color: var(--primary-light); font-size: 24px; margin-bottom: 8px;">Who competes</h3>
        <p class="audience-sub" style="color: rgba(255,255,255,0.5); margin-bottom: 24px; font-size: 14px;">Participant profile from previous editions</p>
        
        <dl class="audience-stats" style="display: grid; gap: 20px; margin: 0;">
          <div style="display: flex; justify-content: space-between; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 12px;">
            <dt style="font-size: 16px; font-weight: 500;">Builders and students</dt><dd style="font-size: 18px; font-weight: 800; color: #fff;">5,000+</dd>
          </div>
          <div style="display: flex; justify-content: space-between; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 12px;">
            <dt style="font-size: 16px; font-weight: 500;">Campuses</dt><dd style="font-size: 18px; font-weight: 800; color: #fff;">100+</dd>
          </div>
          <div style="display: flex; justify-content: space-between; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 12px;">
            <dt style="font-size: 16px; font-weight: 500;">Working professionals</dt><dd style="font-size: 18px; font-weight: 800; color: #fff;">45%</dd>
          </div>
          <div style="display: flex; justify-content: space-between; padding-bottom: 4px;">
            <dt style="font-size: 16px; font-weight: 500;">3+ years of experience</dt><dd style="font-size: 18px; font-weight: 800; color: #fff;">30%</dd>
          </div>
        </dl>
      </div>

      <div class="audience-col" style="flex: 1; min-width: 300px; background: rgba(255,255,255,0.03); padding: 32px; border-radius: 16px; border: 1px solid rgba(255,255,255,0.05); box-shadow: 0 10px 30px rgba(0,0,0,0.2);">
        <h3 class="audience-title" style="color: var(--primary-light); font-size: 24px; margin-bottom: 8px;">Who sees your brand</h3>
        <p class="audience-sub" style="color: rgba(255,255,255,0.5); margin-bottom: 24px; font-size: 14px;">The Economic Times audience</p>
        
        <dl class="audience-stats" style="display: grid; gap: 20px; margin: 0;">
          <div style="display: flex; justify-content: space-between; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 12px;">
            <dt style="font-size: 16px; font-weight: 500;">Monthly readers</dt><dd style="font-size: 18px; font-weight: 800; color: #fff;">50M+</dd>
          </div>
          <div style="display: flex; justify-content: space-between; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 12px;">
            <dt style="font-size: 16px; font-weight: 500;">Cities represented</dt><dd style="font-size: 18px; font-weight: 800; color: #fff;">20+</dd>
          </div>
          <div style="display: flex; justify-content: space-between; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 12px;">
            <dt style="font-size: 16px; font-weight: 500;">Manager level and above</dt><dd style="font-size: 18px; font-weight: 800; color: #fff;">65%</dd>
          </div>
          <div style="display: flex; justify-content: space-between; padding-bottom: 4px;">
            <dt style="font-size: 16px; font-weight: 500;">Readers in top 8 metros</dt><dd style="font-size: 18px; font-weight: 800; color: #fff;">70%</dd>
          </div>
        </dl>
      </div>

    </div>
    
    <div style="text-align: center; margin-top: 24px;">
      <span class="audience-source" style="font-size: 12px; color: rgba(255,255,255,0.4);">* Source: internal analytics, previous edition registrations</span>
    </div>
  </div>
</section>"""
    
    html = html.replace(match.group(0), new_section)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('Updated Audience section with Slate background!')
else:
    print('Audience section not found!')
