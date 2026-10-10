import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx_start = html.find('<section id="audience"')
if idx_start != -1:
    idx_end = html.find('</section>', idx_start) + len('</section>')
    
    old_section = html[idx_start:idx_end]
    
    new_section = """<section id="audience" class="section-pad" style="background: var(--bg-surface-elevated); border-top: 1px solid var(--border-subtle); border-bottom: 1px solid var(--border-subtle);">
  <div class="container">
    <div class="section-head centered">
      <h2 class="section-title">Who Sees Your Brand</h2>
      <p class="section-desc">The Economic Times audience — India's most influential business readership.</p>
    </div>

    <div class="audience-block" style="display: flex; flex-wrap: wrap; gap: 32px; margin-top: 48px;">
      
      <div class="audience-col" style="flex: 1; min-width: 300px; background: linear-gradient(180deg, #1e293b 0%, #0f172a 100%); padding: 40px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.1); border-top: 4px solid var(--primary-color); box-shadow: 0 20px 40px rgba(0,0,0,0.1); transition: transform 0.3s ease;">
        <h3 class="audience-title" style="color: #fff; font-size: 26px; margin-bottom: 8px; font-weight: 700;">Who competes</h3>
        <p class="audience-sub" style="color: #94a3b8; margin-bottom: 32px; font-size: 15px;">Participant profile from previous editions</p>
        
        <dl class="audience-stats" style="display: grid; gap: 24px; margin: 0;">
          <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 16px;">
            <dt style="font-size: 16px; font-weight: 500; color: #cbd5e1;">Builders and students</dt><dd style="font-size: 22px; font-weight: 800; color: #fff; margin: 0;">5,000+</dd>
          </div>
          <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 16px;">
            <dt style="font-size: 16px; font-weight: 500; color: #cbd5e1;">Campuses</dt><dd style="font-size: 22px; font-weight: 800; color: #fff; margin: 0;">100+</dd>
          </div>
          <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 16px;">
            <dt style="font-size: 16px; font-weight: 500; color: #cbd5e1;">Working professionals</dt><dd style="font-size: 22px; font-weight: 800; color: #fff; margin: 0;">45%</dd>
          </div>
          <div style="display: flex; justify-content: space-between; align-items: center; padding-bottom: 4px;">
            <dt style="font-size: 16px; font-weight: 500; color: #cbd5e1;">3+ years of experience</dt><dd style="font-size: 22px; font-weight: 800; color: #fff; margin: 0;">30%</dd>
          </div>
        </dl>
      </div>

      <div class="audience-col" style="flex: 1; min-width: 300px; background: linear-gradient(180deg, #1e293b 0%, #0f172a 100%); padding: 40px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.1); border-top: 4px solid #3b82f6; box-shadow: 0 20px 40px rgba(0,0,0,0.1); transition: transform 0.3s ease;">
        <h3 class="audience-title" style="color: #fff; font-size: 26px; margin-bottom: 8px; font-weight: 700;">Who sees your brand</h3>
        <p class="audience-sub" style="color: #94a3b8; margin-bottom: 32px; font-size: 15px;">The Economic Times audience</p>
        
        <dl class="audience-stats" style="display: grid; gap: 24px; margin: 0;">
          <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 16px;">
            <dt style="font-size: 16px; font-weight: 500; color: #cbd5e1;">Monthly readers</dt><dd style="font-size: 22px; font-weight: 800; color: #fff; margin: 0;">50M+</dd>
          </div>
          <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 16px;">
            <dt style="font-size: 16px; font-weight: 500; color: #cbd5e1;">Cities represented</dt><dd style="font-size: 22px; font-weight: 800; color: #fff; margin: 0;">20+</dd>
          </div>
          <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 16px;">
            <dt style="font-size: 16px; font-weight: 500; color: #cbd5e1;">Manager level & above</dt><dd style="font-size: 22px; font-weight: 800; color: #fff; margin: 0;">65%</dd>
          </div>
          <div style="display: flex; justify-content: space-between; align-items: center; padding-bottom: 4px;">
            <dt style="font-size: 16px; font-weight: 500; color: #cbd5e1;">Readers in top 8 metros</dt><dd style="font-size: 22px; font-weight: 800; color: #fff; margin: 0;">70%</dd>
          </div>
        </dl>
      </div>

    </div>
  </div>"""
    
    html = html.replace(old_section, new_section)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Redesigned audience section!")
else:
    print("Could not find audience section.")
