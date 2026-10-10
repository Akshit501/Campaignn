import re
import subprocess

result = subprocess.run(['git', 'show', 'HEAD:index.html'], capture_output=True, text=True, encoding='utf-8')
orig_html = result.stdout

match = re.search(r'<div class="hero-right">.*?(?=<!-- ==========================================================================)', orig_html, re.DOTALL)
if match:
    hero_right = match.group(0).strip()
    # Remove any trailing </div> </div> </section> from the match
    hero_right = hero_right.split('</section>')[0]
    hero_right = hero_right.rsplit('</div>', 2)[0] + '</div>'
    
    with open('index.html', 'r', encoding='utf-8') as f:
        curr_html = f.read()
        
    # In curr_html, find the end of hero-left
    left_end = r'(<div class="hero-stats-row">.*?</div>\s*</div>)\s*</div>\s*</div>\s*</section>'
    
    # Wait, my current HTML actually looks like:
    #           </div>
    #         </div>
    #       </div>
    #   </section>
    
    # Let's just find the closing tags of hero-left and replace it with hero_right
    curr_html = re.sub(r'(\s*</div>\s*</div>)\s*</div>\s*</section>', r'\1\n' + hero_right.replace('\\', '\\\\') + '\n      </div>\n    </div>\n  </section>', curr_html, flags=re.DOTALL)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(curr_html)
    print("Successfully restored hero-right!")
else:
    print("Could not find hero-right in git history")
