import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Define the new grid HTML with black cards and white text
new_grid = """<div class="how-it-works-grid" style="display: flex; gap: 32px; align-items: stretch; justify-content: space-between;">
        
        <div style="flex: 1; padding: 32px 24px; background: #0F172A; border: 1px solid rgba(255,255,255,0.1); border-radius: 16px; position: relative; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.15);">
          <strong style="color: #fff; font-size: 20px; display: block; margin-bottom: 12px;">You Bring the Challenge</strong>
          <p style="font-size: 15px; color: rgba(255,255,255,0.7); margin: 0; line-height: 1.5;">Define a real business problem worth solving.</p>
          <div class="arrow-right" style="position: absolute; right: -28px; top: 50%; transform: translateY(-50%); font-size: 32px; color: var(--primary-color);">➔</div>
        </div>

        <div style="flex: 1; padding: 32px 24px; background: #0F172A; border: 1px solid rgba(255,255,255,0.1); border-radius: 16px; position: relative; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.15);">
          <strong style="color: #fff; font-size: 20px; display: block; margin-bottom: 12px;">Builders Compete on Your Platform</strong>
          <p style="font-size: 15px; color: rgba(255,255,255,0.7); margin: 0; line-height: 1.5;">Top AI minds use your stack to build what they ship.</p>
          <div class="arrow-right" style="position: absolute; right: -28px; top: 50%; transform: translateY(-50%); font-size: 32px; color: var(--primary-color);">➔</div>
        </div>

        <div style="flex: 1; padding: 32px 24px; background: #0F172A; border: 1px solid rgba(255,255,255,0.1); border-radius: 16px; position: relative; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.15);">
          <strong style="color: #fff; font-size: 20px; display: block; margin-bottom: 12px;">You Hire or Acquire the Best</strong>
          <p style="font-size: 15px; color: rgba(255,255,255,0.7); margin: 0; line-height: 1.5;">Shortlist top teams for direct hiring or acquire their solutions.</p>
        </div>

      </div>"""

# Replace the old grid
html = re.sub(
    r'<div class="how-it-works-grid" style="display: flex; gap: 32px; align-items: stretch; justify-content: space-between;">.*?</div>\s*</div>\s*</div>',
    new_grid + '\n    </div>\n',
    html,
    flags=re.DOTALL
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
