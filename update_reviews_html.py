import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Define the 5 unique review cards
reviews_html = """
          <!-- Review 1 -->
          <div class="review-card-item">
            <div style="position: absolute; top: -30px; left: 24px; width: 60px; height: 60px; border-radius: 50%; overflow: hidden; border: 3px solid #fff; box-shadow: 0 4px 10px rgba(0,0,0,0.1);">
              <img src="https://ui-avatars.com/api/?name=Rohit+Deshmukh&background=0F172A&color=fff&bold=true" alt="Avatar" style="width: 100%; height: 100%; object-fit: cover;">
            </div>
            <p style="color: #333; font-size: 15px; line-height: 1.7; margin-bottom: 24px;">
              "Partnering with the ET AI Hackathon gave our developer platform more production workloads in 48 hours than traditional B2B marketing achieved in six months. The caliber of solutions was unparalleled."
            </p>
            <hr style="border: 0; border-top: 1px solid #eaeaea; margin-bottom: 16px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <div>
                <div style="color: #111; font-weight: 700; font-size: 15px;">Rohit Deshmukh</div>
                <div style="color: #666; font-size: 13px;">VP & Chief AI Architect</div>
              </div>
              <div style="color: #f59e0b; font-size: 16px; letter-spacing: 2px;">★★★★★</div>
            </div>
          </div>

          <!-- Review 2 -->
          <div class="review-card-item">
            <div style="position: absolute; top: -30px; left: 24px; width: 60px; height: 60px; border-radius: 50%; overflow: hidden; border: 3px solid #fff; box-shadow: 0 4px 10px rgba(0,0,0,0.1);">
              <img src="https://ui-avatars.com/api/?name=Sanya+Kapoor&background=f43f5e&color=fff&bold=true" alt="Avatar" style="width: 100%; height: 100%; object-fit: cover;">
            </div>
            <p style="color: #333; font-size: 15px; line-height: 1.7; margin-bottom: 24px;">
              "Winning Edition 2 completely transformed our lives. Within 48 hours of pitching on the ET Demo Day, we were profiled on ET Prime and received 4 term-sheet offers from angel investors."
            </p>
            <hr style="border: 0; border-top: 1px solid #eaeaea; margin-bottom: 16px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <div>
                <div style="color: #111; font-weight: 700; font-size: 15px;">Sanya Kapoor</div>
                <div style="color: #666; font-size: 13px;">Lead Researcher, NeuroClaim AI</div>
              </div>
              <div style="color: #f59e0b; font-size: 16px; letter-spacing: 2px;">★★★★★</div>
            </div>
          </div>

          <!-- Review 3 -->
          <div class="review-card-item">
            <div style="position: absolute; top: -30px; left: 24px; width: 60px; height: 60px; border-radius: 50%; overflow: hidden; border: 3px solid #fff; box-shadow: 0 4px 10px rgba(0,0,0,0.1);">
              <img src="https://ui-avatars.com/api/?name=Anand+K.&background=10b981&color=fff&bold=true" alt="Avatar" style="width: 100%; height: 100%; object-fit: cover;">
            </div>
            <p style="color: #333; font-size: 15px; line-height: 1.7; margin-bottom: 24px;">
              "The Economic Times brings unmatched gravitas. When students and engineers build here, they aren't building toy apps; they are solving real sovereign bottlenecks in Indian infrastructure."
            </p>
            <hr style="border: 0; border-top: 1px solid #eaeaea; margin-bottom: 16px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <div>
                <div style="color: #111; font-weight: 700; font-size: 15px;">Dr. Anand K.</div>
                <div style="color: #666; font-size: 13px;">Partner, DeepTech Ventures</div>
              </div>
              <div style="color: #f59e0b; font-size: 16px; letter-spacing: 2px;">★★★★★</div>
            </div>
          </div>
          
          <!-- Review 4 -->
          <div class="review-card-item">
            <div style="position: absolute; top: -30px; left: 24px; width: 60px; height: 60px; border-radius: 50%; overflow: hidden; border: 3px solid #fff; box-shadow: 0 4px 10px rgba(0,0,0,0.1);">
              <img src="https://ui-avatars.com/api/?name=Vikram+Singh&background=3b82f6&color=fff&bold=true" alt="Avatar" style="width: 100%; height: 100%; object-fit: cover;">
            </div>
            <p style="color: #333; font-size: 15px; line-height: 1.7; margin-bottom: 24px;">
              "This platform allowed us to hire 15 top-tier full-stack AI engineers in one weekend. The environment is hyper-competitive, and the talent pool is absolute world-class."
            </p>
            <hr style="border: 0; border-top: 1px solid #eaeaea; margin-bottom: 16px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <div>
                <div style="color: #111; font-weight: 700; font-size: 15px;">Vikram Singh</div>
                <div style="color: #666; font-size: 13px;">CTO, Apex Technologies</div>
              </div>
              <div style="color: #f59e0b; font-size: 16px; letter-spacing: 2px;">★★★★★</div>
            </div>
          </div>
          
          <!-- Review 5 -->
          <div class="review-card-item">
            <div style="position: absolute; top: -30px; left: 24px; width: 60px; height: 60px; border-radius: 50%; overflow: hidden; border: 3px solid #fff; box-shadow: 0 4px 10px rgba(0,0,0,0.1);">
              <img src="https://ui-avatars.com/api/?name=Priya+Sharma&background=8b5cf6&color=fff&bold=true" alt="Avatar" style="width: 100%; height: 100%; object-fit: cover;">
            </div>
            <p style="color: #333; font-size: 15px; line-height: 1.7; margin-bottom: 24px;">
              "The mentor feedback was invaluable. We pivoted our generative AI pipeline midway through the hackathon based on their advice, which ultimately won us the Grand Prize!"
            </p>
            <hr style="border: 0; border-top: 1px solid #eaeaea; margin-bottom: 16px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <div>
                <div style="color: #111; font-weight: 700; font-size: 15px;">Priya Sharma</div>
                <div style="color: #666; font-size: 13px;">Student, BITS Pilani</div>
              </div>
              <div style="color: #f59e0b; font-size: 16px; letter-spacing: 2px;">★★★★★</div>
            </div>
          </div>
"""

new_section = f"""<section id="testimonials" class="section-pad" style="background: var(--bg-deep);">
    <div class="container-fluid" style="position: relative; max-width: 100%; overflow: hidden; padding-bottom: 40px;">
      <div class="section-head centered" style="margin-bottom: 30px;">
        <p style="color: #f97316; font-size: 16px; margin-bottom: 8px; font-weight: 500;">Words of wisdom from</p>
        <h2 class="section-title" style="color: var(--text-highlight); font-size: 36px; margin: 0; font-weight: 800;">What Our Community Says</h2>
      </div>

      <div class="reviews-marquee-wrapper">
        <div class="reviews-marquee-track">
{reviews_html}
          <!-- Duplicate for infinite seamless scroll -->
{reviews_html}
        </div>
      </div>
      
    </div>
  </section>"""

# Need to replace the entire <section id="testimonials"...> block again using exact string bounds
idx_start = html.find('<h2 class="section-title" style="color: var(--text-highlight); font-size: 36px; margin: 0; font-weight: 800;">What Our Community Says</h2>')
idx_start = html.rfind('<section id="testimonials"', 0, idx_start)
idx_end = html.find('</section>', idx_start) + len('</section>')

if idx_start != -1 and idx_end != -1:
    old_section = html[idx_start:idx_end]
    html = html.replace(old_section, new_section)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Updated testimonials HTML for Marquee!")
else:
    print("Could not find testimonials section bounds.")
