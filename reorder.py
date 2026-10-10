import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove old Scale Reach section if it exists, leaving the new Marquee one.
# The new marquee section has class "marquee-section". The old one had: <section id="scale"... or similar.
# Let's find and remove the old one.
html = re.sub(r'<!-- ==========================================================================\s*03 SCALE, REACH & NATIONAL IMPACT\s*========================================================================== -->.*?<!-- ==========================================================================', '<!-- ==========================================================================', html, flags=re.DOTALL)

# 2. Extract "How it works" and reformat it
# Current "How it works" starts at <!-- How Enterprise Partnership Works (3 Steps) --> and ends at </div> </div> </section>
how_it_works_match = re.search(r'<!-- How Enterprise Partnership Works \(3 Steps\) -->(.*?)</div>\s*</div>\s*</section>', html, flags=re.DOTALL)
if how_it_works_match:
    how_it_works_inner = how_it_works_match.group(1)
    # Remove it from the Sponsor section
    html = html.replace(how_it_works_match.group(0), '</div>\n    </div>\n  </section>')
    
    # Reformat how it works to be horizontal with arrows
    how_it_works_new = """
  <!-- ==========================================================================
       HOW IT WORKS (HORIZONTAL)
       ========================================================================== -->
  <section id="how-it-works" class="section-pad" style="background: var(--bg-surface-elevated); border-top: 1px solid var(--border-subtle); border-bottom: 1px solid var(--border-subtle);">
    <div class="container">
      <div class="section-head centered">
        <h2 class="section-title">How it works</h2>
      </div>
      <div class="how-it-works-grid" style="display: flex; gap: 32px; align-items: stretch; justify-content: space-between;">
        
        <div style="flex: 1; padding: 24px; background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: 16px; position: relative; text-align: center;">
          <strong style="color: var(--text-highlight); font-size: 18px; display: block; margin-bottom: 12px;">You Bring the Challenge</strong>
          <p style="font-size: 15px; color: var(--text-muted); margin: 0;">Define a real business problem worth solving.</p>
          <div class="arrow-right" style="position: absolute; right: -24px; top: 50%; transform: translateY(-50%); font-size: 32px; color: var(--primary-color);">➔</div>
        </div>

        <div style="flex: 1; padding: 24px; background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: 16px; position: relative; text-align: center;">
          <strong style="color: var(--text-highlight); font-size: 18px; display: block; margin-bottom: 12px;">Builders Compete on Your Platform</strong>
          <p style="font-size: 15px; color: var(--text-muted); margin: 0;">Top AI minds use your stack to build what they ship.</p>
          <div class="arrow-right" style="position: absolute; right: -24px; top: 50%; transform: translateY(-50%); font-size: 32px; color: var(--primary-color);">➔</div>
        </div>

        <div style="flex: 1; padding: 24px; background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: 16px; position: relative; text-align: center;">
          <strong style="color: var(--text-highlight); font-size: 18px; display: block; margin-bottom: 12px;">You Hire or Acquire the Best</strong>
          <p style="font-size: 15px; color: var(--text-muted); margin: 0;">Shortlist top teams for direct hiring or acquire their solutions.</p>
        </div>

      </div>
    </div>
  </section>
"""

# 3. We need to reorder the sections:
# 1. Hero
# 2. Marquee (already there right after Hero)
# 3. About
# 4. Why Sponsor
# 5. Who Should Build
# 6. Who Sees Your Brand
# 7. How it works
#
# Let's extract them by splitting on the comments:
# We'll use a regex that matches `<section... </section>` robustly.
sections_dict = {}
def extract_and_remove(html, pattern, key):
    match = re.search(pattern, html, flags=re.DOTALL)
    if match:
        sections_dict[key] = match.group(0)
        return html.replace(match.group(0), f'<!-- INSERT {key} -->')
    return html

html = extract_and_remove(html, r'<!-- ==========================================================================\s*04 ABOUT THE HACKATHON.*?</section>', 'about')
html = extract_and_remove(html, r'<!-- ==========================================================================\s*05 WHO SHOULD BUILD IN ET AI HACKATHON\?.*?</section>', 'who-build')
html = extract_and_remove(html, r'<!-- ==========================================================================\s*06 WHY SPONSOR THE ET AI HACKATHON\?.*?</section>', 'why-sponsor')
html = extract_and_remove(html, r'<!-- ==========================================================================\s*08 WHO SEES YOUR BRAND.*?</section>', 'audience')

# Clean up any INSERT markers
for key in ['about', 'who-build', 'why-sponsor', 'audience']:
    html = html.replace(f'<!-- INSERT {key} -->', '')

# Now re-insert them in the correct order after the Marquee.
marquee_pattern = r'<!-- ==========================================================================\s*02 SCALE, REACH & NATIONAL IMPACT \(MARQUEE\).*?</section>'
marquee_match = re.search(marquee_pattern, html, flags=re.DOTALL)

if marquee_match:
    insertion_point = marquee_match.end()
    
    # Ordered text to insert
    ordered_html = ""
    if 'about' in sections_dict: ordered_html += '\n' + sections_dict['about']
    if 'why-sponsor' in sections_dict: ordered_html += '\n' + sections_dict['why-sponsor']
    if 'who-build' in sections_dict: ordered_html += '\n' + sections_dict['who-build']
    if 'audience' in sections_dict: ordered_html += '\n' + sections_dict['audience']
    if how_it_works_new: ordered_html += '\n' + how_it_works_new

    html = html[:insertion_point] + ordered_html + html[insertion_point:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
