with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx_start = html.find('<section id="lead"')
idx_end = html.find('</section>', idx_start) + len('</section>')

old_section = html[idx_start:idx_end]
form_start = old_section.find('<form')
form_end = old_section.find('</form>') + len('</form>')
form_html = old_section[form_start:form_end]

# We need to construct the original section
original_lead = f"""<section id="lead" class="section-pad lead-section" aria-labelledby="lead-heading">
    <div class="container lead-grid">

      <div class="lead-intro">
        <h2 id="lead-heading" class="section-title">Partner with ET AI Hackathon 2026</h2>
        <p class="lead-intro-text">
          Tell us what you're looking for and we'll send the sponsor deck with tier pricing,
          deliverables and audience data. Our partnerships team will follow up to shape a package around your goals.
        </p>

        <ol class="lead-next-steps">
          <li><strong>Send the enquiry.</strong> Takes under a minute.</li>
          <li><strong>Get the deck by email.</strong> Tier pricing, deliverables and audience data.</li>
          <li><strong>Talk to the partnerships team.</strong> We shape the track, media and hiring package with you.</li>
        </ol>

        <div class="lead-alt-contact">
          <p class="lead-alt-title">Prefer to talk first?</p>
          <!-- Links are filled from CONFIG in app.js; any left unset are hidden automatically. -->
          <a href="#" class="btn btn-secondary btn-sm" data-config-link="meetingsUrl" data-track="book_call_click" target="_blank" rel="noopener">Book a 15-minute call</a>
          <a href="#" class="btn btn-ghost btn-sm" data-config-link="whatsappUrl" data-track="whatsapp_click" target="_blank" rel="noopener">Message us on WhatsApp</a>
          <a href="mailto:hackathon@economictimes.com?subject=ET%20AI%20Hackathon%202026%20partnership" class="btn btn-ghost btn-sm" data-track="email_click">hackathon@economictimes.com</a>
        </div>
      </div>

      <div class="lead-card">
        {form_html}
      </div>

    </div>
  </section>"""

html = html.replace(old_section, original_lead)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Reverted lead section to original!")
