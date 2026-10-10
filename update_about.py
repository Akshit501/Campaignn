import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

about_match = re.search(r'<section id="about".*?</section>', html, flags=re.DOTALL | re.IGNORECASE)

if about_match:
    new_about = """<section id="about" class="section-pad" style="background: var(--bg-deep);">
    <div class="container">

      <div class="about-grid about-grid--single">
        <!-- Left: Narrative & Upgrades -->
        <div>
          <h2 class="section-title" style="margin-bottom: 18px; color: var(--text-highlight); font-size: 42px; font-weight: 800; letter-spacing: -1px;">Where India's Enterprise AI Future is Written</h2>
          <p style="font-size: 17px; line-height: 1.65; margin-bottom: 32px; color: var(--text-muted); max-width: 900px;">
            Across two blockbuster previous editions, the <strong>ET AI Hackathon</strong> has matured into India's most trusted pipeline for discovering breakout technical talent, stress-testing proprietary enterprise tech stacks, and incubating deployable, production-ready AI solutions.
          </p>

          <h4 style="font-size: 16px; font-family: var(--font-mono); text-transform: uppercase; color: var(--text-highlight); margin-bottom: 24px; letter-spacing: 2px;">
            What's New This Edition:
          </h4>

          <div class="about-features" style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 24px;">
            
            <div class="about-feat-card" style="background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 24px; box-shadow: 0 4px 20px rgba(0,0,0,0.03); display: flex; gap: 16px; align-items: flex-start;">
              <div class="feat-icon-box" style="background: #FFF1F2; color: #F43F5E; min-width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; border-radius: 8px; font-size: 18px;">⚡</div>
              <div>
                <strong style="color: var(--text-highlight); font-size: 16px; display: block; margin-bottom: 6px;">Deeper Industry Integration</strong>
                <p style="font-size: 14px; margin: 0; color: var(--text-muted); line-height: 1.5;">Real enterprise problem statements co-formulated with Fortune 500 CTOs and ET 500 business heads.</p>
              </div>
            </div>

            <div class="about-feat-card" style="background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 24px; box-shadow: 0 4px 20px rgba(0,0,0,0.03); display: flex; gap: 16px; align-items: flex-start;">
              <div class="feat-icon-box" style="background: #EFF6FF; color: #3B82F6; min-width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; border-radius: 8px; font-size: 18px;">🔄</div>
              <div>
                <strong style="color: var(--text-highlight); font-size: 16px; display: block; margin-bottom: 6px;">Stronger Solution Pipelines</strong>
                <p style="font-size: 14px; margin: 0; color: var(--text-muted); line-height: 1.5;">From GitHub repository to enterprise pilot testbed in under 60 days with dedicated sandbox environments.</p>
              </div>
            </div>

            <div class="about-feat-card" style="background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 24px; box-shadow: 0 4px 20px rgba(0,0,0,0.03); display: flex; gap: 16px; align-items: flex-start;">
              <div class="feat-icon-box" style="background: #FFF1F2; color: #F43F5E; min-width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; border-radius: 8px; font-size: 18px;">🚀</div>
              <div>
                <strong style="color: var(--text-highlight); font-size: 16px; display: block; margin-bottom: 6px;">Clearer Paths to Deployment & Seed Grants</strong>
                <p style="font-size: 14px; margin: 0; color: var(--text-muted); line-height: 1.5;">Pre-seed venture fast-track, GPU cloud credits, and direct enterprise sandbox deployment paths.</p>
              </div>
            </div>

            <div class="about-feat-card" style="background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 24px; box-shadow: 0 4px 20px rgba(0,0,0,0.03); display: flex; gap: 16px; align-items: flex-start;">
              <div class="feat-icon-box" style="background: #EFF6FF; color: #3B82F6; min-width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; border-radius: 8px; font-size: 18px;">🌐</div>
              <div>
                <strong style="color: var(--text-highlight); font-size: 16px; display: block; margin-bottom: 6px;">Agentic Workflows & Indic AI Focus</strong>
                <p style="font-size: 14px; margin: 0; color: var(--text-muted); line-height: 1.5;">Dedicated sub-tracks for multi-modal autonomous agents and regional language indic models.</p>
              </div>
            </div>

          </div>
          
          <style>
            @media (max-width: 768px) {
              .about-features {
                grid-template-columns: 1fr !important;
              }
            }
          </style>

        </div>
      </div>
    </div>
  </section>"""
    
    html = html.replace(about_match.group(0), new_about)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Updated About section!")
else:
    print("Could not find about section.")
