with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update .hero-right card styling
old_hero_right = 'style="background: #ffffff; padding: 48px 40px; border-radius: 16px; box-shadow: 0 20px 60px rgba(244,63,94,0.08); position: relative;"'
new_hero_right = 'style="background: #ffffff; padding: 48px 40px; border-radius: 16px; box-shadow: 0 20px 60px rgba(244,63,94,0.08); position: relative; border: 2px solid transparent; background-image: linear-gradient(#fff, #fff), linear-gradient(90deg, #E11D48, #F97316); background-origin: border-box; background-clip: padding-box, border-box;"'

html = html.replace(old_hero_right, new_hero_right)

# Update form button and add disclaimer
old_button = """<button type="submit" class="form-submit" style="margin-top: 16px; width: 100%; padding: 16px; border-radius: 8px; font-weight: 700; font-size: 15px; color: #fff; background: linear-gradient(90deg, #f43f5e 0%, #f97316 100%); border: none; cursor: pointer; transition: transform 0.2s, opacity 0.2s;">
              Register Now &rarr;
            </button>"""

new_button = """<button type="submit" class="form-submit" style="margin-top: 16px; width: 100%; padding: 16px; border-radius: 8px; font-weight: 700; font-size: 15px; color: #fff; background: #e52b66; border: none; cursor: pointer; transition: transform 0.2s, opacity 0.2s;">
              Get the Sponsor Deck &rarr;
            </button>
            <p style="font-size: 10px; color: #475569; font-weight: 500; text-align: left; margin-top: 12px; line-height: 1.5;">
              Your information will be used to contact you regarding sponsorship opportunities.
            </p>"""

html = html.replace(old_button, new_button)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated form design!")
