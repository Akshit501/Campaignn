import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Find the section
match = re.search(r'<!-- ==========================================================================\s*05 WHO SHOULD BUILD.*?</section>', html, flags=re.DOTALL | re.IGNORECASE)

if match:
    # 2. Replace it with the new horizontal 3-card layout
    new_section = """<!-- ==========================================================================
       05 WHO SHOULD BUILD IN ET AI HACKATHON?
       ========================================================================== -->
  <section id="who-should-build" class="section-pad">
    <div class="container">
      <div class="section-head centered">
        <h2 class="section-title">Who Should Build in ET AI Hackathon?</h2>
        <p class="section-desc">Whether you write low-level CUDA kernels or design high-converting multi-modal agent workflows, there is a place for you.</p>
      </div>

      <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; margin-top: 40px;">
        
        <!-- Card 1 -->
        <div class="card" style="background: linear-gradient(145deg, #1A1F2E 0%, #0F121C 100%); border: 1px solid rgba(255,255,255,0.1); border-radius: 24px; padding: 32px; display: flex; flex-direction: column; position: relative; overflow: hidden;">
          <div style="font-size: 48px; margin-bottom: 20px;">💻</div>
          <h3 style="color: #fff; font-size: 22px; font-weight: 800; margin-bottom: 12px; line-height: 1.3;">AI Developers & Hackers</h3>
          <p style="color: rgba(255,255,255,0.7); font-size: 15px; line-height: 1.6; margin-bottom: 24px; flex-grow: 1;">Full-stack AI engineers, PyTorch researchers, LLM fine-tuners, and backend builders wanting to benchmark against enterprise-grade datasets.</p>
          <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 12px; color: rgba(255,255,255,0.9); font-size: 14px;">
            <li style="display: flex; gap: 12px;"><span style="color: #4ade80;">✓</span> Build on real Fortune 500 API sandboxes</li>
            <li style="display: flex; gap: 12px;"><span style="color: #4ade80;">✓</span> Direct recruitment fast-track by sponsor CTOs</li>
            <li style="display: flex; gap: 12px;"><span style="color: #4ade80;">✓</span> GPU cluster compute credits for all finalists</li>
          </ul>
        </div>

        <!-- Card 2 -->
        <div class="card" style="background: linear-gradient(145deg, #1A1F2E 0%, #0F121C 100%); border: 1px solid rgba(255,255,255,0.1); border-radius: 24px; padding: 32px; display: flex; flex-direction: column; position: relative; overflow: hidden;">
          <div style="font-size: 48px; margin-bottom: 20px;">🎓</div>
          <h3 style="color: #fff; font-size: 22px; font-weight: 800; margin-bottom: 12px; line-height: 1.3;">Students & Researchers</h3>
          <p style="color: rgba(255,255,255,0.7); font-size: 15px; line-height: 1.6; margin-bottom: 24px; flex-grow: 1;">Undergraduate, graduate, and PhD scholars from IITs, BITS, IIITs, NITs, and top engineering universities eager to gain national acclaim.</p>
          <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 12px; color: rgba(255,255,255,0.9); font-size: 14px;">
            <li style="display: flex; gap: 12px;"><span style="color: #60a5fa;">✓</span> Verified Certificate of Excellence signed by ET leadership</li>
            <li style="display: flex; gap: 12px;"><span style="color: #60a5fa;">✓</span> 1-on-1 mentorship from seasoned industry architects</li>
            <li style="display: flex; gap: 12px;"><span style="color: #60a5fa;">✓</span> Campus spotlight & resume accreditation</li>
          </ul>
        </div>

        <!-- Card 3 -->
        <div class="card" style="background: linear-gradient(145deg, #1A1F2E 0%, #0F121C 100%); border: 1px solid rgba(255,255,255,0.1); border-radius: 24px; padding: 32px; display: flex; flex-direction: column; position: relative; overflow: hidden;">
          <div style="font-size: 48px; margin-bottom: 20px;">🧠</div>
          <h3 style="color: #fff; font-size: 22px; font-weight: 800; margin-bottom: 12px; line-height: 1.3;">Product Thinkers & Designers</h3>
          <p style="color: rgba(255,255,255,0.7); font-size: 15px; line-height: 1.6; margin-bottom: 24px; flex-grow: 1;">Product managers, domain specialists, and UI/UX designers who transform raw foundational models into intuitive, defensible customer products.</p>
          <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 12px; color: rgba(255,255,255,0.9); font-size: 14px;">
            <li style="display: flex; gap: 12px;"><span style="color: #f472b6;">✓</span> Test user journey and commercial viability</li>
            <li style="display: flex; gap: 12px;"><span style="color: #f472b6;">✓</span> Pitch directly to venture capitalists and angel funds</li>
            <li style="display: flex; gap: 12px;"><span style="color: #f472b6;">✓</span> Featured in ET Startup & Product showcases</li>
          </ul>
        </div>

      </div>
      
      <!-- Responsive styling embedded -->
      <style>
        @media (max-width: 900px) {
          #who-should-build > .container > div {
            grid-template-columns: 1fr !important;
          }
        }
      </style>
      
    </div>
  </section>"""
    
    html = html.replace(match.group(0), new_section)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully replaced Who Should Build section!")
else:
    print("Could not find section.")
