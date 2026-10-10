import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx_start = html.find('<section id="lead"')
if idx_start != -1:
    idx_end = html.find('</section>', idx_start) + len('</section>')
    old_section = html[idx_start:idx_end]
    
    # We will grab everything from old_section starting at <form and keep it, but we'll wrap it in our new design.
    form_start = old_section.find('<form')
    form_end = old_section.find('</form>') + len('</form>')
    form_html = old_section[form_start:form_end]
    
    new_section = f"""<section id="lead" class="section-pad lead-section" aria-labelledby="lead-heading" style="background: linear-gradient(135deg, #020617 0%, #0f172a 100%); position: relative; overflow: hidden;">
    <!-- Decorative background elements -->
    <div style="position: absolute; top: -10%; left: -5%; width: 400px; height: 400px; background: radial-gradient(circle, rgba(244,63,94,0.15) 0%, transparent 70%); filter: blur(40px); border-radius: 50%; pointer-events: none;"></div>
    <div style="position: absolute; bottom: -10%; right: -5%; width: 400px; height: 400px; background: radial-gradient(circle, rgba(59,130,246,0.15) 0%, transparent 70%); filter: blur(40px); border-radius: 50%; pointer-events: none;"></div>

    <style>
      #lead .lead-intro-text {{ color: #94a3b8; font-size: 18px; line-height: 1.6; margin-bottom: 32px; }}
      #lead .lead-next-steps li {{ color: #cbd5e1; margin-bottom: 16px; font-size: 16px; display: flex; gap: 12px; }}
      #lead .lead-next-steps li::before {{ content: '✓'; color: var(--primary-color); font-weight: bold; font-size: 18px; }}
      #lead .lead-alt-title {{ color: #fff; margin-bottom: 16px; font-weight: 600; font-size: 18px; }}
      
      #lead .lead-card {{
        background: rgba(30, 41, 59, 0.7);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 24px;
        padding: 40px;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
      }}
      #lead .field-label {{ color: #94a3b8 !important; text-transform: uppercase; letter-spacing: 1px; font-size: 11px; margin-bottom: 8px; font-weight: 700; }}
      #lead .form-control {{
        background: rgba(15, 23, 42, 0.6) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        color: #fff !important;
        border-radius: 12px;
        padding: 14px 16px;
        transition: all 0.3s ease;
      }}
      #lead .form-control:focus {{
        border-color: var(--primary-color) !important;
        box-shadow: 0 0 0 4px rgba(244, 63, 94, 0.1) !important;
        outline: none;
      }}
      #lead .form-control::placeholder {{ color: #475569 !important; }}
      
      #lead .chip span {{
        background: rgba(15, 23, 42, 0.6);
        border: 1px solid rgba(255, 255, 255, 0.1);
        color: #cbd5e1;
        transition: all 0.2s ease;
      }}
      #lead .chip input:checked + span {{
        background: var(--primary-color);
        border-color: var(--primary-color);
        color: #fff;
      }}
      #lead .check-row span {{ color: #cbd5e1; }}
      #lead .check-row a {{ color: var(--primary-color); text-decoration: underline; }}
      
      #lead summary {{ color: #fff; font-weight: 600; padding: 12px 0; border-bottom: 1px solid rgba(255,255,255,0.1); cursor: pointer; }}
    </style>

    <div class="container lead-grid" style="display: grid; grid-template-columns: 1fr 1fr; gap: 64px; align-items: start; position: relative; z-index: 1;">

      <div class="lead-intro">
        <h2 id="lead-heading" class="section-title" style="color: #fff; font-size: 42px; font-weight: 800; line-height: 1.2; margin-bottom: 24px;">Ready to Supercharge Your Developer Brand?</h2>
        <p class="lead-intro-text">
          Skip the cold emails and generic marketing. Partnering with the ET AI Hackathon puts your platform directly in the hands of India's top 1% engineers. 
          Drop your details below to instantly receive our 2026 Sponsorship Prospectus. Let's build something incredible together.
        </p>

        <ul class="lead-next-steps" style="list-style: none; padding: 0; margin-bottom: 48px;">
          <li><span><strong>Drop your details:</strong> Fast, simple, and no commitment.</span></li>
          <li><span><strong>Instant Deck Access:</strong> Receive our full 2026 sponsor prospectus straight to your inbox.</span></li>
          <li><span><strong>Custom Strategy Call:</strong> We'll map out a tailored hiring and platform-adoption strategy for your brand.</span></li>
        </ul>

        <div class="lead-alt-contact">
          <p class="lead-alt-title">Prefer to talk first?</p>
          <div style="display: flex; gap: 16px; flex-wrap: wrap;">
            <a href="#" class="btn btn-secondary btn-sm" data-config-link="meetingsUrl" data-track="book_call_click" target="_blank" rel="noopener">Book a 15-minute call</a>
            <a href="mailto:hackathon@economictimes.com" class="btn btn-primary btn-sm" data-track="email_click" style="background: rgba(255,255,255,0.1); color: #fff;">Email Partnerships</a>
          </div>
        </div>
      </div>

      <div class="lead-card">
        {form_html}
      </div>

    </div>
  </section>"""
    
    html = html.replace(old_section, new_section)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Redesigned lead section!")
else:
    print("Could not find lead section.")
