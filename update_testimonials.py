import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_section = """<div class="container" style="position: relative;">
      <div class="section-head centered" style="margin-bottom: 50px;">
        <p style="color: #f97316; font-size: 16px; margin-bottom: 8px; font-weight: 500;">Words of wisdom from</p>
        <h2 class="section-title" style="color: var(--text-highlight); font-size: 36px; margin: 0; font-weight: 800;">What Our Community Says</h2>
      </div>

      <div style="display: flex; align-items: center; justify-content: space-between; gap: 20px;">
        
        <!-- Left Arrow -->
        <button style="width: 40px; height: 40px; border-radius: 50%; background: #ea580c; border: none; color: #fff; display: flex; align-items: center; justify-content: center; cursor: pointer; flex-shrink: 0; box-shadow: 0 4px 12px rgba(234, 88, 12, 0.3);">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"></polyline></svg>
        </button>

        <div class="testimonials-grid" style="display: flex; gap: 32px; flex: 1;">
          
          <!-- Partner Testimonial -->
          <div style="background: #fff; border-radius: 12px; padding: 48px 24px 24px; position: relative; box-shadow: 0 10px 30px rgba(0,0,0,0.06); text-align: left; flex: 1; border: 1px solid rgba(0,0,0,0.05); margin-top: 20px;">
            <div style="position: absolute; top: -30px; left: 24px; width: 60px; height: 60px; border-radius: 50%; overflow: hidden; border: 3px solid #fff; box-shadow: 0 4px 10px rgba(0,0,0,0.1);">
              <img src="https://ui-avatars.com/api/?name=Rohit+Deshmukh&background=0F172A&color=fff&bold=true" alt="Avatar" style="width: 100%; height: 100%; object-fit: cover;">
            </div>
            
            <p style="color: #333; font-size: 15px; line-height: 1.7; margin-bottom: 24px;">
              "Partnering with the ET AI Hackathon gave our developer platform more production workloads in 48 hours than traditional B2B marketing achieved in six months. The caliber of solutions and national editorial coverage was unparalleled."
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

          <!-- Participant Testimonial -->
          <div style="background: #fff; border-radius: 12px; padding: 48px 24px 24px; position: relative; box-shadow: 0 10px 30px rgba(0,0,0,0.06); text-align: left; flex: 1; border: 1px solid rgba(0,0,0,0.05); margin-top: 20px;">
            <div style="position: absolute; top: -30px; left: 24px; width: 60px; height: 60px; border-radius: 50%; overflow: hidden; border: 3px solid #fff; box-shadow: 0 4px 10px rgba(0,0,0,0.1);">
              <img src="https://ui-avatars.com/api/?name=Sanya+Kapoor&background=f43f5e&color=fff&bold=true" alt="Avatar" style="width: 100%; height: 100%; object-fit: cover;">
            </div>
            
            <p style="color: #333; font-size: 15px; line-height: 1.7; margin-bottom: 24px;">
              "Winning Edition 2 completely transformed our lives. Within 48 hours of pitching on the ET Demo Day, we were profiled on ET Prime and received 4 term-sheet offers from angel investors. This is the real deal."
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

          <!-- Mentor Testimonial -->
          <div style="background: #fff; border-radius: 12px; padding: 48px 24px 24px; position: relative; box-shadow: 0 10px 30px rgba(0,0,0,0.06); text-align: left; flex: 1; border: 1px solid rgba(0,0,0,0.05); margin-top: 20px;">
            <div style="position: absolute; top: -30px; left: 24px; width: 60px; height: 60px; border-radius: 50%; overflow: hidden; border: 3px solid #fff; box-shadow: 0 4px 10px rgba(0,0,0,0.1);">
              <img src="https://ui-avatars.com/api/?name=Anand+Krishnamurthy&background=10b981&color=fff&bold=true" alt="Avatar" style="width: 100%; height: 100%; object-fit: cover;">
            </div>
            
            <p style="color: #333; font-size: 15px; line-height: 1.7; margin-bottom: 24px;">
              "The Economic Times brings unmatched gravitas. When students and engineers build here, they aren't building toy apps; they are solving real sovereign bottlenecks in Indian infrastructure, medicine, and finance."
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
          
        </div>

        <!-- Right Arrow -->
        <button style="width: 40px; height: 40px; border-radius: 50%; background: #ea580c; border: none; color: #fff; display: flex; align-items: center; justify-content: center; cursor: pointer; flex-shrink: 0; box-shadow: 0 4px 12px rgba(234, 88, 12, 0.3);">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"></polyline></svg>
        </button>
      </div>
      
      <!-- Paging dots -->
      <div style="display: flex; justify-content: center; gap: 8px; margin-top: 40px;">
        <div style="width: 10px; height: 10px; border-radius: 50%; background: #999;"></div>
        <div style="width: 10px; height: 10px; border-radius: 50%; background: #ddd;"></div>
      </div>
    </div>"""

# Find the start and end of the container div inside #testimonials
start_tag = '<div class="container">'
end_tag = '</div>\n  </section>'

match = re.search(r'<section id="testimonials".*?>\s*(<div class="container">.*?)</div>\s*</section>', html, re.DOTALL)
if match:
    old_container = match.group(1) + '</div>'
    html = html.replace(old_container, new_section)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Updated testimonials section!")
else:
    print("Testimonials section not found properly!")
