/**
 * ET AI HACKATHON 2026 – page logic
 *
 * What this file does:
 *  - CONFIG: every ID, URL and endpoint the campaign needs, in one place
 *  - Tracking: loads GA4 / Google Ads / Meta Pixel / LinkedIn Insight only when their IDs are set,
 *    and sends the same named events to all of them through track()
 *  - Attribution: stores UTM parameters and ad click IDs (first and last touch) and attaches them to every form
 *  - Forms: partner enquiry + builder registration, validated and sent to HubSpot or your own endpoint,
 *    then redirected to thank-you.html so ad platforms can count conversions
 *  - Page: fixed-date countdown, ?audience=partner hero variant, challenge carousel and briefs,
 *    real YouTube video modal, FAQ search, sticky partner button
 */

/* ==========================================================================
   00. CONFIG — fill these in before launch
   ========================================================================== */
const CONFIG = {
  // Where form submissions go. Set EITHER hubspot (portalId + form GUIDs) OR leadEndpoint.
  // HubSpot: create two forms (partner, builder) whose field names match the `name`
  // attributes in index.html, or rename the mapping in toHubSpotFields() below.
  hubspot: {
    portalId: '',             // e.g. '1234567'
    partnerFormGuid: '',      // e.g. 'a1b2c3d4-....'
    builderFormGuid: ''
  },
  leadEndpoint: '',           // alternative: your own API that accepts JSON POST

  // Pages and links
  thankYouUrl: 'thank-you.html',
  deckUrl: '',                // public URL of the sponsor deck PDF (shown on the thank-you page)
  meetingsUrl: '',            // HubSpot Meetings / Calendly link for "Book a 15-minute call"
  whatsappUrl: '',            // e.g. 'https://wa.me/9198XXXXXXXX?text=Hi%2C%20I%27m%20interested%20in%20partnering'

  // Tracking IDs (leave blank to skip loading that tag)
  ga4MeasurementId: '',       // 'G-XXXXXXX'
  googleAdsId: '',            // 'AW-XXXXXXXXX'
  googleAdsLeadLabel: '',     // conversion label for partner leads
  googleAdsRegisterLabel: '', // conversion label for builder registrations
  metaPixelId: '',
  linkedinPartnerId: '',
  linkedinLeadConversionId: '',

  // Personal email domains rejected on the partner form's work-email field
  freeEmailDomains: ['gmail.com', 'yahoo.com', 'yahoo.co.in', 'hotmail.com', 'outlook.com', 'live.com',
    'rediffmail.com', 'icloud.com', 'aol.com', 'proton.me', 'protonmail.com', 'ymail.com', 'gmx.com', 'zoho.com']
};

document.addEventListener('DOMContentLoaded', () => {
  loadTrackingTags();
  captureAttribution();
  applyAudienceVariant();
  initCountdownTimer();
  initChallengesCarousel();
  initModals();
  initBuilderTrackOptions();
  initLeadForms();
  initDeckRequests();
  initConfigLinks();
  initVideos();
  initFaqAccordion();
  initStickyPill();
  initClickTracking();
  initThankYouPage();
});

/* ==========================================================================
   01. TRACKING
   ========================================================================== */
function loadScript(src) {
  const s = document.createElement('script');
  s.async = true;
  s.src = src;
  document.head.appendChild(s);
}

function loadTrackingTags() {
  const gtagIds = [CONFIG.ga4MeasurementId, CONFIG.googleAdsId].filter(Boolean);
  if (gtagIds.length) {
    loadScript(`https://www.googletagmanager.com/gtag/js?id=${gtagIds[0]}`);
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    gtag('js', new Date());
    gtagIds.forEach(id => gtag('config', id));
  }

  if (CONFIG.metaPixelId) {
    /* eslint-disable */
    !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?
    n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;
    n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
    t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,
    document,'script','https://connect.facebook.net/en_US/fbevents.js');
    /* eslint-enable */
    fbq('init', CONFIG.metaPixelId);
    fbq('track', 'PageView');
  }

  if (CONFIG.linkedinPartnerId) {
    window._linkedin_partner_id = CONFIG.linkedinPartnerId;
    window._linkedin_data_partner_ids = window._linkedin_data_partner_ids || [];
    window._linkedin_data_partner_ids.push(CONFIG.linkedinPartnerId);
    window.lintrk = window.lintrk || function (a, b) { (window.lintrk.q = window.lintrk.q || []).push([a, b]); };
    loadScript('https://snap.licdn.com/li.lms-analytics/insight.min.js');
  }
}

/**
 * Sends one named event to every loaded tag.
 * Event names used on this page:
 *  cta_click, form_start, form_submit_error, generate_lead (partner), sign_up (builder),
 *  deck_request, challenge_view, video_play, faq_search
 */
function track(name, params = {}) {
  try {
    if (window.gtag) gtag('event', name, params);
    if (window.fbq) {
      if (name === 'generate_lead') fbq('track', 'Lead', params);
      else if (name === 'sign_up') fbq('track', 'CompleteRegistration', params);
      else fbq('trackCustom', name, params);
    }
    if (window.lintrk && name === 'generate_lead' && CONFIG.linkedinLeadConversionId) {
      lintrk('track', { conversion_id: Number(CONFIG.linkedinLeadConversionId) });
    }
    if (window.gtag && CONFIG.googleAdsId) {
      const label = name === 'generate_lead' ? CONFIG.googleAdsLeadLabel
        : name === 'sign_up' ? CONFIG.googleAdsRegisterLabel : '';
      if (label) gtag('event', 'conversion', { send_to: `${CONFIG.googleAdsId}/${label}` });
    }
  } catch (err) {
    // A blocked tag must never break the page
  }
  if (!CONFIG.ga4MeasurementId && !CONFIG.metaPixelId && !CONFIG.linkedinPartnerId) {
    console.info('[track]', name, params);
  }
}

function initClickTracking() {
  document.addEventListener('click', (e) => {
    const el = e.target.closest('[data-track]');
    if (el) track('cta_click', { cta: el.dataset.track });
  });
}

/* ==========================================================================
   02. ATTRIBUTION (UTMs + click IDs, first and last touch)
   ========================================================================== */
const ATTR_KEYS = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term', 'gclid', 'fbclid', 'li_fat_id'];

function safeStorage(kind) {
  try { const s = window[kind]; s.setItem('__t', '1'); s.removeItem('__t'); return s; } catch { return null; }
}

function captureAttribution() {
  const params = new URLSearchParams(location.search);
  const touch = {};
  ATTR_KEYS.forEach(k => { if (params.get(k)) touch[k] = params.get(k); });

  const local = safeStorage('localStorage');
  const session = safeStorage('sessionStorage');
  const hasCampaign = Object.keys(touch).length > 0;

  const stamp = { ...touch, landing_page: location.href, referrer: document.referrer || '', ts: new Date().toISOString() };

  if (local && !local.getItem('et_hack_first_touch')) local.setItem('et_hack_first_touch', JSON.stringify(stamp));
  if (session && (hasCampaign || !session.getItem('et_hack_last_touch'))) {
    session.setItem('et_hack_last_touch', JSON.stringify(stamp));
  }
}

function getAttribution() {
  const read = (store, key) => { try { return JSON.parse(store?.getItem(key) || '{}'); } catch { return {}; } };
  const first = read(safeStorage('localStorage'), 'et_hack_first_touch');
  const last = read(safeStorage('sessionStorage'), 'et_hack_last_touch');
  const out = {};
  ATTR_KEYS.forEach(k => { out[k] = last[k] || ''; out[`first_${k}`] = first[k] || ''; });
  out.landing_page = last.landing_page || location.href;
  out.referrer = last.referrer || document.referrer || '';
  out.first_landing_page = first.landing_page || '';
  out.page_url = location.href;
  out.device = /Mobi|Android/i.test(navigator.userAgent) ? 'mobile' : 'desktop';
  out.submitted_at = new Date().toISOString();
  return out;
}

function fillAttributionFields(form) {
  const box = form.querySelector('.js-attribution-fields');
  if (!box) return;
  box.innerHTML = '';
  Object.entries(getAttribution()).forEach(([k, v]) => {
    const input = document.createElement('input');
    input.type = 'hidden';
    input.name = k;
    input.value = v;
    box.appendChild(input);
  });
}

/* ==========================================================================
   03. AUDIENCE VARIANT  (?audience=partner → sponsor-first hero for B2B campaigns)
   ========================================================================== */
function applyAudienceVariant() {
  const audience = new URLSearchParams(location.search).get('audience');
  if (audience !== 'partner') return;

  const tagline = document.getElementById('hero-tagline');
  const group = document.getElementById('hero-cta-group');
  const builderBtn = document.getElementById('hero-cta-builder');
  const partnerBtn = document.getElementById('hero-cta-partner');

  if (tagline) {
    tagline.innerHTML = 'Put your platform, brand and hiring team in front of 5,000+ AI builders and ' +
      '<strong style="color:#fff;">The Economic Times</strong>\u2019 50M+ monthly readers. ' +
      'Co-create a challenge track and walk away with working prototypes, vetted talent and national coverage.';
  }
  if (group && builderBtn && partnerBtn) {
    partnerBtn.classList.replace('btn-secondary', 'btn-primary');
    partnerBtn.textContent = 'Get the sponsor deck';
    partnerBtn.setAttribute('data-deck-request', '');
    builderBtn.classList.replace('btn-primary', 'btn-secondary');
    builderBtn.textContent = 'Register as a builder (free)';
    group.prepend(partnerBtn);
  }
  document.body.dataset.audience = 'partner';
}

/* ==========================================================================
   04. COUNTDOWN (fixed deadline from data-deadline)
   ========================================================================== */
function initCountdownTimer() {
  const strip = document.querySelector('.countdown-strip[data-deadline]');
  if (!strip) return;
  const deadline = new Date(strip.dataset.deadline).getTime();
  const els = ['days', 'hours', 'mins', 'secs'].map(u => document.getElementById(`timer-${u}`));
  if (els.some(e => !e) || Number.isNaN(deadline)) return;

  let timer;
  function update() {
    const distance = deadline - Date.now();
    if (distance <= 0) {
      els.forEach(e => (e.textContent = '00'));
      const label = strip.querySelector('.countdown-label');
      if (label) label.textContent = 'Registration is closed';
      clearInterval(timer);
      return;
    }
    const parts = [
      Math.floor(distance / 86400000),
      Math.floor((distance % 86400000) / 3600000),
      Math.floor((distance % 3600000) / 60000),
      Math.floor((distance % 60000) / 1000)
    ];
    parts.forEach((v, i) => (els[i].textContent = String(v).padStart(2, '0')));
  }
  update();
  timer = setInterval(update, 1000);
}

/* ==========================================================================
   05. CHALLENGES DATA & CAROUSEL
   ========================================================================== */
// TODO VERIFY: partner names on each track must be confirmed sponsors before launch.
const challengesData = [
  {
    id: 'ch-1',
    category: 'fintech',
    tag: 'Razorpay & ET BFSI',
    title: 'Autonomous Fraud Sentinel',
    desc: 'Engineer a sub-second graph-reasoning multi-agent system to flag synthetic fraud across high-throughput UPI and cross-border payment gateways.',
    prize: '₹6,00,000 + API Grants',
    difficulty: 'Hard',
    stack: ['LangGraph', 'Gemini 1.5 Pro', 'Neo4j', 'FastAPI'],
    partner: 'Razorpay AI Labs',
    problem: 'Traditional rule-based fraud engines suffer from high false-positive rates on emerging mule accounts and synthetic identity fraud. Teams must build an agentic graph model that dynamically audits transactional graphs in under 200ms.',
    deliverables: ['Working API endpoint with latency <250ms', 'Graph representation visualizer', 'Evaluation report on synthetic test vector dataset of 5M transactions']
  },
  {
    id: 'ch-2',
    category: 'indic',
    tag: 'Google Cloud & AI4Bharat',
    title: 'IndicVoice Multi-Modal Agent',
    desc: 'Deploy voice-native conversational AI supporting 14 Indian languages for tier-2/3 public services and banking advisory with low latency.',
    prize: '₹5,50,000 + Cloud Grants',
    difficulty: 'Medium-Hard',
    stack: ['Whisper Finetuned', 'Bhashini APIs', 'vLLM', 'WebRTC'],
    partner: 'Google Cloud India',
    problem: 'Over 600M citizens struggle with English-only digital interfaces. Build an end-to-end multi-turn voice assistant that handles code-mixed Hindi, Tamil, Telugu, and Bengali for critical welfare or banking services.',
    deliverables: ['Real-time audio streaming pipeline', 'ASR + LLM + TTS round-trip <900ms', 'Demo scenario for agricultural crop insurance claim']
  },
  {
    id: 'ch-3',
    category: 'enterprise',
    tag: 'Infosys & ET Prime',
    title: 'Self-Healing Enterprise DevOps Agent',
    desc: 'Create an autonomous agent network that ingests distributed OpenTelemetry logs, pinpoints root-cause bugs, and generates validated pull requests.',
    prize: '₹5,00,000 + Pilot Access',
    difficulty: 'Hard',
    stack: ['AutoGPT', 'Claude 3.5 Sonnet', 'Kubernetes', 'Tree-sitter'],
    partner: 'Infosys Topaz',
    problem: 'Large microservice clusters create millions of log alerts daily. Build an agentic diagnostic tool that autonomously traces stack traces, reproduces failures in a sandboxed container, and submits regression-tested PRs.',
    deliverables: ['Telemetry log ingestor & RAG memory store', 'Docker sandbox execution runner', 'Verified benchmark on 20 synthetic outage scenarios']
  },
  {
    id: 'ch-4',
    category: 'health',
    tag: 'Apollo Hospitals & NVIDIA',
    title: 'Clinical Diagnostics & Radiology Assistant',
    desc: 'Multi-modal diagnostic co-pilot analyzing DICOM chest X-rays and unstructured physician notes to generate structured clinical risk assessments.',
    prize: '₹5,00,000 + NVIDIA Jetson Pods',
    difficulty: 'Hard',
    stack: ['MONAI', 'BioMistral', 'PyTorch', 'NVIDIA TensorRT'],
    partner: 'Apollo HealthTech',
    problem: 'Radiologist burnout leads to delayed triage in rural ICUs. Design an edge-compatible computer vision & NLP model that detects acute pneumothorax and cardiomegaly within 5 seconds with verifiable citations.',
    deliverables: ['DICOM inference web viewer', 'Heatmap CAM explainability layer', 'HIPAA/NABH compliant privacy scrubber demo']
  },
  {
    id: 'ch-5',
    category: 'cyber',
    tag: 'Tech Mahindra & CERT-In',
    title: 'Quantum-Safe Zero-Day Shield',
    desc: 'Real-time firmware and smart contract vulnerability analyzer using neuro-symbolic reasoning to discover zero-day attack vectors.',
    prize: '₹4,50,000 + Fast-Track Hiring',
    difficulty: 'Expert',
    stack: ['Slither', 'Symbolic Exec', 'Rust', 'CodeLlama-70b'],
    partner: 'Tech Mahindra CyberLabs',
    problem: 'Automated exploits in DeFi and enterprise API endpoints drain billions annually. Build a static + dynamic symbolic execution agent that discovers re-entrancy and memory corruption bugs prior to mainnet deploy.',
    deliverables: ['Automated bytecode scanner CLI', 'Fuzzing generator agent', 'Benchmark audit on 50 historically exploited smart contracts']
  },
  {
    id: 'ch-6',
    category: 'green',
    tag: 'Tata Power & ET Energy',
    title: 'Microgrid Renewable Energy Dispatcher',
    desc: 'Reinforcement learning model optimizing solar-wind-battery storage dispatch against volatile spot-electricity market prices.',
    prize: '₹4,00,000 + Incubation',
    difficulty: 'Medium',
    stack: ['Ray RLlib', 'Prophet', 'FastAPI', 'Pandas'],
    partner: 'Tata Cleantech',
    problem: 'Intermittent renewable energy generation creates peak-load instability. Train a reinforcement learning agent to maximize grid arbitrage and battery lifespan under fluctuating weather and grid demand.',
    deliverables: ['24-hour lookahead dispatch simulator', 'Real-time telemetry dashboard', 'Backtesting engine tested on 2 years of IEX exchange data']
  }
];

let currentChallengeIdx = 0;
let filteredChallenges = [...challengesData];
let openChallengeId = null;

function initChallengesCarousel() {
  const track = document.getElementById('challenge-carousel-track');
  const dotsContainer = document.getElementById('carousel-dots-container');
  const prevBtn = document.getElementById('carousel-prev-btn');
  const nextBtn = document.getElementById('carousel-next-btn');
  const filterTabs = document.querySelectorAll('.filter-tab');
  if (!track) return;

  function getCardsPerView() {
    if (window.innerWidth <= 640) return 1;
    if (window.innerWidth <= 980) return 2;
    return 3;
  }

  function maxIndex() {
    return Math.max(0, filteredChallenges.length - getCardsPerView());
  }

  function renderCarousel() {
    track.innerHTML = '';
    filteredChallenges.forEach(ch => {
      const card = document.createElement('div');
      card.className = 'challenge-card card';
      card.innerHTML = `
        <div class="challenge-banner">
          <div class="challenge-sponsor-tag">${ch.tag}</div>
          <div style="font-size: 32px; filter: drop-shadow(0 0 12px var(--primary-glow));">⚡</div>
          <div class="challenge-prize-pill">${ch.prize}</div>
        </div>
        <div class="challenge-card-body">
          <div class="mono" style="font-size: 11px; color: var(--primary-light); text-transform: uppercase;">
            ${ch.category.toUpperCase()} TRACK · ${ch.difficulty}
          </div>
          <h3 class="challenge-card-title">${ch.title}</h3>
          <p class="challenge-card-desc">${ch.desc}</p>
          <div class="challenge-stack-pills">
            ${ch.stack.map(st => `<span class="stack-pill">${st}</span>`).join('')}
          </div>
          <div style="margin-top: auto; padding-top: 14px;">
            <button type="button" class="btn btn-secondary btn-sm" style="width: 100%;" data-challenge-id="${ch.id}">
              View challenge brief
            </button>
          </div>
        </div>`;
      track.appendChild(card);
    });
    renderDots();
    updateSlidePosition();
  }

  function renderDots() {
    if (!dotsContainer) return;
    dotsContainer.innerHTML = '';
    for (let i = 0; i <= maxIndex(); i++) {
      const dot = document.createElement('button');
      dot.type = 'button';
      dot.className = `carousel-dot ${i === currentChallengeIdx ? 'active' : ''}`;
      dot.setAttribute('aria-label', `Go to slide ${i + 1}`);
      dot.addEventListener('click', () => {
        currentChallengeIdx = i;
        updateSlidePosition();
        renderDots();
      });
      dotsContainer.appendChild(dot);
    }
  }

  function updateSlidePosition() {
    currentChallengeIdx = Math.min(Math.max(currentChallengeIdx, 0), maxIndex());
    const pct = 100 / getCardsPerView();
    track.style.transform = `translateX(calc(-${currentChallengeIdx * pct}% - ${currentChallengeIdx * 20}px))`;
  }

  prevBtn?.addEventListener('click', () => {
    currentChallengeIdx = currentChallengeIdx > 0 ? currentChallengeIdx - 1 : maxIndex();
    updateSlidePosition();
    renderDots();
  });

  nextBtn?.addEventListener('click', () => {
    currentChallengeIdx = currentChallengeIdx < maxIndex() ? currentChallengeIdx + 1 : 0;
    updateSlidePosition();
    renderDots();
  });

  filterTabs.forEach(tab => {
    tab.addEventListener('click', () => {
      filterTabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');
      const category = tab.dataset.filter;
      filteredChallenges = category === 'all' ? [...challengesData] : challengesData.filter(ch => ch.category === category);
      currentChallengeIdx = 0;
      renderCarousel();
    });
  });

  track.addEventListener('click', (e) => {
    const btn = e.target.closest('[data-challenge-id]');
    if (btn) openChallengeModal(btn.dataset.challengeId);
  });

  window.addEventListener('resize', () => {
    updateSlidePosition();
    renderDots();
  });

  renderCarousel();
}

function openChallengeModal(id) {
  const ch = challengesData.find(c => c.id === id);
  if (!ch) return;
  openChallengeId = id;

  const set = (elId, text) => { const el = document.getElementById(elId); if (el) el.textContent = text; };
  set('cm-title', ch.title);
  set('cm-partner', `${ch.partner} (${ch.tag})`);
  set('cm-prize', ch.prize);
  set('cm-problem', ch.problem);

  const deliverablesEl = document.getElementById('cm-deliverables');
  if (deliverablesEl) {
    deliverablesEl.innerHTML = ch.deliverables
      .map(d => `<li style="display:flex; gap:10px; margin-bottom:8px;"><span>✓</span><span>${d}</span></li>`).join('');
  }
  const stackEl = document.getElementById('cm-stack');
  if (stackEl) stackEl.innerHTML = ch.stack.map(s => `<span class="stack-pill">${s}</span>`).join('');

  openModal('challenge-modal');
  track('challenge_view', { challenge: ch.title });
}

/* ==========================================================================
   06. MODALS (shared open/close, Esc key, backdrop click, focus return)
   ========================================================================== */
let lastFocused = null;

function openModal(id) {
  const modal = document.getElementById(id);
  if (!modal) return;
  document.querySelectorAll('.modal-backdrop.open').forEach(m => m.classList.remove('open'));
  lastFocused = document.activeElement;
  modal.classList.add('open');
  document.body.style.overflow = 'hidden';
  const focusTarget = modal.querySelector('input:not([type=hidden]):not([tabindex="-1"]), select, .modal-close-btn');
  setTimeout(() => focusTarget?.focus(), 50);
}

function closeModal(modal) {
  if (!modal) return;
  modal.classList.remove('open');
  document.body.style.overflow = '';
  if (modal.id === 'video-modal') {
    const frame = document.getElementById('vm-frame');
    if (frame) frame.innerHTML = '';
  }
  lastFocused?.focus?.();
}

function initModals() {
  document.querySelectorAll('.modal-backdrop').forEach(modal => {
    modal.addEventListener('click', (e) => {
      if (e.target === modal || e.target.closest('.modal-close-btn, [data-close-modal]')) closeModal(modal);
    });
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeModal(document.querySelector('.modal-backdrop.open'));
  });

  document.querySelectorAll('.open-builder-modal-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const fromChallenge = btn.id === 'cm-enroll-btn' && openChallengeId;
      openModal('builder-reg-modal');
      if (fromChallenge) {
        const ch = challengesData.find(c => c.id === openChallengeId);
        const select = document.getElementById('b-track');
        if (ch && select) select.value = ch.title;
      }
    });
  });
}

function initBuilderTrackOptions() {
  const select = document.getElementById('b-track');
  if (!select) return;
  select.innerHTML = challengesData
    .map(ch => `<option value="${ch.title}">${ch.title}</option>`)
    .join('') + '<option value="Undecided">Not decided yet</option>';
}

/* ==========================================================================
   07. FORMS: validation, submission, redirect
   ========================================================================== */
function initLeadForms() {
  document.querySelectorAll('form.js-lead-form').forEach(form => {
    let started = false;
    form.addEventListener('focusin', () => {
      if (started) return;
      started = true;
      track('form_start', { form_type: form.dataset.formType });
    });

    form.addEventListener('input', (e) => {
      if (e.target.getAttribute('aria-invalid') === 'true') e.target.removeAttribute('aria-invalid');
    });

    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const errorEl = form.querySelector('.form-error');
      const error = validateForm(form);
      if (error) {
        if (errorEl) errorEl.textContent = error;
        track('form_submit_error', { form_type: form.dataset.formType, error });
        return;
      }
      if (errorEl) errorEl.textContent = '';

      // Honeypot filled → silently pretend success
      if (form.querySelector('[name="website"]')?.value) {
        form.reset();
        return;
      }

      fillAttributionFields(form);
      const data = collectFormData(form);
      const submitBtn = form.querySelector('.form-submit');
      const originalLabel = submitBtn?.textContent;
      if (submitBtn) { submitBtn.disabled = true; submitBtn.textContent = 'Sending…'; }

      try {
        await submitLead(form.dataset.formType, data);
        const isPartner = form.dataset.formType === 'partner';
        track(isPartner ? 'generate_lead' : 'sign_up', {
          form_type: form.dataset.formType,
          interest: data.interest || data.preferred_track || '',
          utm_campaign: data.utm_campaign || ''
        });
        if (isPartner && data.wants_deck === 'yes') track('deck_request', { source: 'form' });

        const session = safeStorage('sessionStorage');
        session?.setItem('et_hack_submission', JSON.stringify({
          type: form.dataset.formType,
          first_name: (data.full_name || '').split(' ')[0],
          company: data.company || ''
        }));

        const url = new URL(CONFIG.thankYouUrl, location.href);
        url.searchParams.set('type', form.dataset.formType);
        if (isPartner && data.wants_deck === 'yes') url.searchParams.set('deck', '1');
        setTimeout(() => { location.href = url.toString(); }, 400); // let tags send before leaving
      } catch (err) {
        console.error(err);
        if (errorEl) {
          errorEl.textContent = 'We couldn\u2019t send your details. Check your connection and try again, or email hackathon@economictimes.com.';
        }
        if (submitBtn) { submitBtn.disabled = false; submitBtn.textContent = originalLabel; }
      }
    });
  });
}

function validateForm(form) {
  const markInvalid = (el, msg) => { el?.setAttribute('aria-invalid', 'true'); el?.focus(); return msg; };

  for (const el of form.querySelectorAll('[required]')) {
    if (el.type === 'checkbox') continue;
    if (!el.value.trim()) {
      const label = form.querySelector(`label[for="${el.id}"]`)?.textContent.replace('*', '').trim() || 'This field';
      return markInvalid(el, `${label} is required.`);
    }
  }

  const email = form.querySelector('input[type="email"]');
  if (email && !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email.value.trim())) {
    return markInvalid(email, 'Enter a valid email address, like name@company.com.');
  }
  if (email?.hasAttribute('data-work-email')) {
    const domain = email.value.trim().split('@')[1]?.toLowerCase();
    if (CONFIG.freeEmailDomains.includes(domain)) {
      return markInvalid(email, 'Use your work email so our partnerships team can reach the right person.');
    }
  }

  const phone = form.querySelector('input[type="tel"]');
  if (phone && phone.value.trim()) {
    const digits = phone.value.replace(/\D/g, '');
    if (digits.length < 7 || digits.length > 15) return markInvalid(phone, 'Enter a valid phone number.');
  }

  const url = form.querySelector('input[type="url"]');
  if (url && url.value.trim() && !/^https?:\/\/\S+\.\S+/.test(url.value.trim())) {
    return markInvalid(url, 'Enter the full link, starting with https://');
  }

  if (form.dataset.formType === 'partner' && !form.querySelector('input[name="interest"]:checked')) {
    return markInvalid(form.querySelector('input[name="interest"]'), 'Choose at least one area you\u2019re interested in.');
  }

  const consent = form.querySelector('input[name="consent"]');
  if (consent && !consent.checked) return markInvalid(consent, 'Tick the consent box so we can contact you.');

  return '';
}

function collectFormData(form) {
  const data = {};
  new FormData(form).forEach((value, key) => {
    if (key === 'website') return;
    data[key] = data[key] ? `${data[key]}; ${value}` : value; // multi-select checkboxes joined
  });
  if (data.phone && data.phone_country_code) data.phone = `${data.phone_country_code} ${data.phone}`;
  data.form_type = form.dataset.formType;
  return data;
}

async function submitLead(formType, data) {
  const hs = CONFIG.hubspot;
  const guid = formType === 'partner' ? hs.partnerFormGuid : hs.builderFormGuid;

  if (hs.portalId && guid) {
    const hutk = document.cookie.match(/hubspotutk=([^;]+)/)?.[1];
    const res = await fetch(`https://api.hsforms.com/submissions/v3/integration/submit/${hs.portalId}/${guid}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        fields: toHubSpotFields(data),
        context: { pageUri: location.href, pageName: document.title, ...(hutk ? { hutk } : {}) }
      })
    });
    if (!res.ok) throw new Error(`HubSpot returned ${res.status}`);
    return;
  }

  if (CONFIG.leadEndpoint) {
    const res = await fetch(CONFIG.leadEndpoint, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });
    if (!res.ok) throw new Error(`Lead endpoint returned ${res.status}`);
    return;
  }

  // Nothing configured yet: log the payload so the flow can be tested end to end.
  console.warn('[lead form] No endpoint configured in CONFIG. Payload that would be sent:', data);
}

// Maps form field names to HubSpot property names. Standard properties: firstname, lastname,
// email, company, jobtitle, phone. Everything else must exist as a custom property in HubSpot.
function toHubSpotFields(data) {
  const [firstname, ...rest] = (data.full_name || '').trim().split(/\s+/);
  const mapped = { ...data, firstname, lastname: rest.join(' '), jobtitle: data.designation };
  delete mapped.full_name;
  delete mapped.designation;
  delete mapped.phone_country_code;
  return Object.entries(mapped)
    .filter(([, v]) => v !== undefined && v !== '')
    .map(([name, value]) => ({ name, value: String(value) }));
}

/* ==========================================================================
   08. DECK REQUESTS → always go through the enquiry form
   ========================================================================== */
function initDeckRequests() {
  document.querySelectorAll('[data-deck-request]').forEach(btn => {
    btn.addEventListener('click', (e) => {
      const form = document.getElementById('enterprise-lead-form');
      if (!form) return;
      e.preventDefault();
      const deckBox = form.querySelector('input[name="wants_deck"]');
      if (deckBox) deckBox.checked = true;
      document.getElementById('lead')?.scrollIntoView({ behavior: 'smooth', block: 'start' });
      setTimeout(() => document.getElementById('lead-name')?.focus({ preventScroll: true }), 500);
      track('deck_request', { source: btn.dataset.track || 'link' });
    });
  });
}

function initConfigLinks() {
  document.querySelectorAll('[data-config-link]').forEach(link => {
    const url = CONFIG[link.dataset.configLink];
    if (url) link.href = url;
    else link.hidden = true;
  });
}

/* ==========================================================================
   09. VIDEOS (real YouTube embeds; hidden until IDs are added)
   ========================================================================== */
function initVideos() {
  const section = document.getElementById('videos');
  const cards = [...document.querySelectorAll('.video-card[data-youtube-id]')];
  if (!section || !cards.length) return;

  const validId = id => /^[\w-]{11}$/.test(id || '');
  let playable = 0;

  cards.forEach(card => {
    const id = card.dataset.youtubeId;
    if (!validId(id)) { card.hidden = true; return; }
    playable++;
    const thumb = card.querySelector('.video-thumb');
    if (thumb) {
      thumb.style.backgroundImage = `url(https://i.ytimg.com/vi/${id}/hqdefault.jpg)`;
      thumb.style.backgroundSize = 'cover';
      thumb.style.backgroundPosition = 'center';
    }
    const play = () => {
      const title = card.querySelector('h3')?.textContent.trim() || 'Video';
      const frame = document.getElementById('vm-frame');
      frame.innerHTML = '';
      const iframe = document.createElement('iframe');
      iframe.title = title;
      iframe.allow = 'autoplay; encrypted-media; picture-in-picture';
      iframe.allowFullscreen = true;
      iframe.src = `https://www.youtube-nocookie.com/embed/${id}?autoplay=1&rel=0`;
      frame.appendChild(iframe);
      document.getElementById('vm-title').textContent = title;
      openModal('video-modal');
      track('video_play', { video: title });
    };
    card.addEventListener('click', play);
    card.addEventListener('keydown', (e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); play(); } });
  });

  if (!playable) section.hidden = true;
}

/* ==========================================================================
   10. FAQ SEARCH
   ========================================================================== */
function initFaqAccordion() {
  const searchInput = document.getElementById('faq-search-input');
  const faqItems = document.querySelectorAll('.faq-item');
  if (!searchInput) return;

  let searchTimer;
  searchInput.addEventListener('input', (e) => {
    const query = e.target.value.toLowerCase().trim();
    faqItems.forEach(item => { item.style.display = item.textContent.toLowerCase().includes(query) ? '' : 'none'; });
    clearTimeout(searchTimer);
    if (query.length > 2) searchTimer = setTimeout(() => track('faq_search', { query }), 800);
  });
}

/* ==========================================================================
   11. STICKY PARTNER BUTTON (after the hero, hidden while the form is visible)
   ========================================================================== */
function initStickyPill() {
  const pill = document.getElementById('lead-open-pill');
  const hero = document.querySelector('.hero-section');
  const lead = document.getElementById('lead');
  if (!pill || !hero || !lead || !('IntersectionObserver' in window)) return;

  let heroVisible = true;
  let leadVisible = false;
  const update = () => { pill.hidden = heroVisible || leadVisible; };

  new IntersectionObserver(([entry]) => { heroVisible = entry.isIntersecting; update(); }).observe(hero);
  new IntersectionObserver(([entry]) => { leadVisible = entry.isIntersecting; update(); }, { threshold: 0.15 }).observe(lead);

  pill.addEventListener('click', () => setTimeout(() => document.getElementById('lead-name')?.focus({ preventScroll: true }), 500));
}

/* ==========================================================================
   12. THANK-YOU PAGE
   ========================================================================== */
function initThankYouPage() {
  if (document.body.dataset.page !== 'thank-you') return;
  const params = new URLSearchParams(location.search);
  const type = params.get('type') === 'builder' ? 'builder' : 'partner';
  let stored = {};
  try { stored = JSON.parse(safeStorage('sessionStorage')?.getItem('et_hack_submission') || '{}'); } catch { /* ignore */ }

  document.querySelectorAll('[data-for]').forEach(el => { el.hidden = el.dataset.for !== type; });
  ['ty-name', 'ty-name-b'].forEach(id => {
    const el = document.getElementById(id);
    if (el && stored.first_name) el.textContent = `, ${stored.first_name}`;
  });

  const deckLink = document.getElementById('ty-deck-link');
  if (deckLink) {
    if (type === 'partner' && params.get('deck') === '1' && CONFIG.deckUrl) {
      deckLink.href = CONFIG.deckUrl;
      deckLink.hidden = false;
      deckLink.addEventListener('click', () => track('deck_download', { source: 'thank_you' }));
    } else {
      deckLink.hidden = true;
    }
  }
}

/* ==========================================================================
   13. TOAST UTILITY
   ========================================================================== */
function showToast(msg) {
  let container = document.getElementById('toast-container');
  if (!container) {
    container = document.createElement('div');
    container.id = 'toast-container';
    container.className = 'toast-container';
    document.body.appendChild(container);
  }
  const toast = document.createElement('div');
  toast.className = 'toast';
  toast.setAttribute('role', 'status');
  toast.textContent = msg;
  container.appendChild(toast);
  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transition = 'opacity 0.3s ease';
    setTimeout(() => toast.remove(), 300);
  }, 4000);
}
