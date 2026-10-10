import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx_start = html.find('<footer class="site-footer">')
if idx_start != -1:
    idx_end = html.find('</footer>', idx_start) + len('</footer>')
    old_footer = html[idx_start:idx_end]
    
    new_footer = """<style>
    .premium-footer {
      background: #0B0F19;
      color: #fff;
      padding: 80px 0 40px;
      position: relative;
      overflow: hidden;
    }
    .premium-footer::before {
      content: '';
      position: absolute;
      top: 0; left: 0; right: 0;
      height: 1px;
      background: linear-gradient(90deg, transparent, rgba(244,63,94,0.5), transparent);
    }
    .premium-footer .footer-top {
      display: grid;
      grid-template-columns: 2fr 1fr 1fr 1fr;
      gap: 48px;
      margin-bottom: 64px;
    }
    @media (max-width: 900px) {
      .premium-footer .footer-top {
        grid-template-columns: 1fr;
        gap: 32px;
      }
    }
    .premium-footer .et-text-brand .et-sub,
    .premium-footer .et-text-brand .et-main {
      color: #fff !important;
    }
    .premium-footer .footer-col-title {
      font-size: 13px;
      text-transform: uppercase;
      letter-spacing: 1.5px;
      color: #94A3B8;
      margin-bottom: 24px;
      font-weight: 700;
    }
    .premium-footer .footer-links {
      list-style: none;
      padding: 0;
      margin: 0;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }
    .premium-footer .footer-links a {
      color: #CBD5E1;
      text-decoration: none;
      font-size: 14px;
      transition: all 0.3s ease;
      display: inline-block;
    }
    .premium-footer .footer-links a:hover {
      color: #fff;
      transform: translateX(4px);
    }
    .premium-footer .footer-bottom {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-top: 32px;
      border-top: 1px solid rgba(255,255,255,0.1);
      font-size: 13px;
      color: #94A3B8;
    }
    @media (max-width: 768px) {
      .premium-footer .footer-bottom {
        flex-direction: column;
        gap: 16px;
        text-align: center;
      }
    }
    .social-links {
      display: flex;
      gap: 16px;
    }
    .social-links a {
      color: #94A3B8;
      transition: color 0.3s ease;
      display: flex;
      align-items: center;
      justify-content: center;
      width: 36px;
      height: 36px;
      border-radius: 50%;
      background: rgba(255,255,255,0.05);
    }
    .social-links a:hover {
      color: #fff;
      background: var(--primary-color);
    }
  </style>

  <footer class="premium-footer">
    <div class="container">
      <div class="footer-top">
        <div class="footer-brand">
          <div class="et-logo-badge" style="margin-bottom: 24px;">
            <div class="et-crest" style="background: var(--primary-color); color: #fff;">ET</div>
            <div class="et-text-brand">
              <span class="et-sub">The Economic Times</span>
              <span class="et-main">AI HACKATHON 2026</span>
            </div>
          </div>
          <p style="font-size: 15px; max-width: 320px; line-height: 1.6; color: #94A3B8; margin-bottom: 24px;">
            India's flagship enterprise and developer artificial intelligence marathon. Connecting elite builders with sovereign challenges.
          </p>
          <div style="font-size: 14px; color: #94A3B8; font-family: var(--font-mono);">
            Official Inquiries: <br>
            <a href="mailto:hackathon@economictimes.com" style="color: #fff; text-decoration: none; font-weight: 600; font-size: 15px; margin-top: 8px; display: inline-block;">hackathon@economictimes.com</a>
          </div>
        </div>

        <div>
          <h4 class="footer-col-title">Navigation</h4>
          <ul class="footer-links">
            <li><a href="#about">About Edition 3.0</a></li>
            <li><a href="#who-should-build">Who Should Build</a></li>
            <li><a href="#sponsor">Why Sponsor</a></li>
            <li><a href="#impact">Previous Winners</a></li>
            <li><a href="#faq">Frequently Asked Questions</a></li>
          </ul>
        </div>

        <div>
          <h4 class="footer-col-title">For Partners</h4>
          <ul class="footer-links">
            <li><a href="#sponsor">Why Sponsor</a></li>
            <li><a href="#audience">Who Sees Your Brand</a></li>
            <li><a href="#lead">Partnership Enquiry</a></li>
            <li><a href="#hero-enquiry-form">Quick Sponsor Form</a></li>
            <li><a href="#lead">Sponsor deck & media kit</a></li>
          </ul>
        </div>

        <div>
          <h4 class="footer-col-title">Legal & Guidelines</h4>
          <ul class="footer-links">
            <li><a href="#">Code of Conduct</a></li>
            <li><a href="#">Rules & Evaluation Rubric</a></li>
            <li><a href="#">Privacy Policy</a></li>
            <li><a href="#">Terms & Conditions</a></li>
            <li><a href="#">IP & Compliance Policy</a></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <div>
          &copy; 2026 The Economic Times &middot; Bennett, Coleman & Co. Ltd. (BCCL). All rights reserved.
        </div>
        <div class="social-links">
          <a href="https://www.linkedin.com/company/the-economic-times/" target="_blank" rel="noopener" aria-label="LinkedIn">
            <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 448 512" height="18" width="18" xmlns="http://www.w3.org/2000/svg"><path d="M100.28 448H7.4V148.9h92.88zM53.79 108.1C24.09 108.1 0 83.5 0 53.8a53.79 53.79 0 0 1 107.58 0c0 29.7-24.1 54.3-53.79 54.3zM447.9 448h-92.68V302.4c0-34.7-.7-79.2-48.29-79.2-48.29 0-55.69 37.7-55.69 76.7V448h-92.78V148.9h89.08v40.8h1.3c12.4-23.5 42.69-48.3 87.88-48.3 94 0 111.28 61.9 111.28 142.3V448z"></path></svg>
          </a>
          <a href="https://x.com/EconomicTimes" target="_blank" rel="noopener" aria-label="X (Twitter)">
            <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 512 512" height="16" width="16" xmlns="http://www.w3.org/2000/svg"><path d="M389.2 48h70.6L305.6 224.2 487 464H345L233.7 318.6 106.5 464H35.8L200.7 275.5 26.8 48H172.4L272.9 180.9 389.2 48zM364.4 421.8h39.1L151.1 88h-42L364.4 421.8z"></path></svg>
          </a>
          <a href="https://www.youtube.com/@EconomicTimes" target="_blank" rel="noopener" aria-label="YouTube">
            <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 576 512" height="18" width="18" xmlns="http://www.w3.org/2000/svg"><path d="M549.655 124.083c-6.281-23.65-24.787-42.276-48.284-48.597C458.781 64 288 64 288 64S117.22 64 74.629 75.486c-23.497 6.322-42.003 24.947-48.284 48.597-11.412 42.867-11.412 132.305-11.412 132.305s0 89.438 11.412 132.305c6.281 23.65 24.787 41.5 48.284 47.821C117.22 448 288 448 288 448s170.78 0 213.371-11.486c23.497-6.321 42.003-24.171 48.284-47.821 11.412-42.867 11.412-132.305 11.412-132.305s0-89.438-11.412-132.305zm-317.51 213.508V175.185l142.739 81.205-142.739 81.201z"></path></svg>
          </a>
        </div>
      </div>
    </div>
  </footer>"""
    
    html = html.replace(old_footer, new_footer)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Replaced footer with premium dark mode footer!")
else:
    print("Could not find footer tag.")
