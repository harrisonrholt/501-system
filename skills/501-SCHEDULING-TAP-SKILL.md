---
name: 501-scheduling-tap
description: >
  Use this skill whenever Harrison asks about adding a scheduling feature, calendar
  tap, booking button, GHL calendar integration, or appointment booking to a BluePage.
  Also triggers for: "add a booking tap", "scheduling tap", "how do I add the calendar",
  "book an estimate button", "GHL calendar on the BluePage", "appointment tap", or any
  request involving letting customers schedule through a client's BluePage. This skill
  produces the complete tap row + full-screen overlay component with the GHL calendar
  widget embedded, plus a configurable label and optional badge. Always ask Harrison
  for the label text, badge preference, and client's GHL calendar URL before building.
---

# 501 Scheduling Tap Skill

Adds a GHL calendar booking tap to any BluePage. Opens as a full-screen overlay
on top of the BluePage — no new tab, no page navigation. Customer taps, books,
closes. One component: tap row + overlay + close button.

---

## How It Works

1. Customer taps the scheduling row
2. Full-screen overlay slides up from the bottom (iOS sheet style)
3. GHL calendar widget loads inside the overlay via iframe
4. Customer picks a time and books
5. They tap the close button (or swipe down) to return to the BluePage

No new tab opened. No navigation away from the BluePage. Keeps the customer
in the client's branded experience the entire time.

---

## Variables Per Client

| Variable | What it is | Example |
|---|---|---|
| `{{CAL_URL}}` | GHL calendar widget URL | `https://api.leadconnectorhq.com/widget/booking/...` |
| `{{TAP_LABEL}}` | Main tap row title | "Book an Estimate" |
| `{{TAP_SUB}}` | Subtitle line | "Pick a time · No phone tag" |
| `{{BADGE_TEXT}}` | Badge label — leave blank to hide | "FREE", "FREE ESTIMATE", "" |
| `{{SLUG}}` | Client slug for function naming | `mikes-plumbing` |

### How to get the GHL calendar URL per client:
1. GHL → client sub-account → Calendars
2. Click the calendar → Settings → Integrations
3. Copy the **Widget URL** (starts with `https://api.leadconnectorhq.com/widget/booking/`)
4. That's `{{CAL_URL}}`

---

## Label Options — Pick Per Client

Harrison picks the label when building. Common options:

| Business type | TAP_LABEL | TAP_SUB |
|---|---|---|
| Contractor / trades | "Book an Estimate" | "Pick a time · No phone tag" |
| Service call business | "Schedule a Service Call" | "Available same week" |
| Consulting / agency | "Book a Strategy Call" | "Free · 20 minutes · No pitch" |
| High ticket work | "Request a Quote" | "Free consultation · We come to you" |
| Any | "Schedule Online" | "Pick a time that works for you" |

---

## Badge Options — Pick Per Client

| Input | What shows |
|---|---|
| `FREE` | Green pill: **FREE** |
| `FREE ESTIMATE` | Green pill: **FREE ESTIMATE** |
| `FREE CONSULTATION` | Green pill: **FREE CONSULTATION** |
| `FREE QUOTE` | Green pill: **FREE QUOTE** |
| Any custom text | Green pill with that text |
| *(blank)* | No badge shown |

---

## The Full Component

Drop this entire block into the `Book & Pay` card on the BluePage.
Replace all `{{VARIABLES}}` before deploying.

```html
<!-- ── GHL SCHEDULING TAP + OVERLAY ──────────────────────────
     Skill: 501-scheduling-tap
     Variables: CAL_URL, TAP_LABEL, TAP_SUB, BADGE_TEXT, SLUG
     Place inside the Book & Pay .card.glass div
──────────────────────────────────────────────────────────── -->

<!-- TAP ROW -->
<button onclick="openCal_{{SLUG}}()" class="tap-row">
  <div class="row-icon ri-blue">📅</div>
  <div class="row-text">
    <div class="row-title">{{TAP_LABEL}}</div>
    <div class="row-sub">{{TAP_SUB}}</div>
  </div>
  <!-- BADGE — remove this span entirely if no badge needed -->
  <span id="cal-badge-{{SLUG}}" class="badge b-green">{{BADGE_TEXT}}</span>
  <div class="row-arrow">›</div>
</button>

<!-- FULL-SCREEN OVERLAY -->
<div id="cal-overlay-{{SLUG}}" style="
  display:none;
  position:fixed;
  inset:0;
  z-index:9999;
  background:rgba(5,8,16,0.96);
  backdrop-filter:blur(20px);
  -webkit-backdrop-filter:blur(20px);
  flex-direction:column;
  animation:calSlideUp .32s cubic-bezier(.32,0,.67,0) both;
">

  <!-- Header bar -->
  <div style="
    display:flex;
    align-items:center;
    justify-content:space-between;
    padding:16px 20px 12px;
    border-bottom:0.5px solid rgba(255,255,255,0.08);
    flex-shrink:0;
  ">
    <div style="font-size:15px;font-weight:800;color:#fff;">{{TAP_LABEL}}</div>
    <button onclick="closeCal_{{SLUG}}()" style="
      background:rgba(255,255,255,0.08);
      border:1px solid rgba(255,255,255,0.12);
      border-radius:50%;
      width:32px;height:32px;
      display:flex;align-items:center;justify-content:center;
      cursor:pointer;color:rgba(255,255,255,0.6);
      font-size:16px;font-family:inherit;
      transition:background .15s;
    " onmouseenter="this.style.background='rgba(255,255,255,0.14)'"
       onmouseleave="this.style.background='rgba(255,255,255,0.08)'">
      ✕
    </button>
  </div>

  <!-- Calendar iframe -->
  <iframe
    id="cal-frame-{{SLUG}}"
    src=""
    data-src="{{CAL_URL}}"
    style="
      flex:1;
      width:100%;
      border:none;
      background:transparent;
    "
    allow="camera; microphone; geolocation"
    loading="lazy"
  ></iframe>

</div>

<style>
@keyframes calSlideUp {
  from { transform: translateY(100%); opacity: 0; }
  to   { transform: translateY(0);    opacity: 1; }
}
@keyframes calSlideDown {
  from { transform: translateY(0);    opacity: 1; }
  to   { transform: translateY(100%); opacity: 0; }
}
</style>

<script>
/* ── SCHEDULING TAP FUNCTIONS ── */
/* Named with slug to prevent conflicts across multiple clients */

function openCal_{{SLUG}}() {
  const overlay = document.getElementById('cal-overlay-{{SLUG}}');
  const frame   = document.getElementById('cal-frame-{{SLUG}}');

  /* Lazy-load the iframe src on first open only */
  if (!frame.src || frame.src === window.location.href) {
    frame.src = frame.dataset.src;
  }

  overlay.style.display = 'flex';
  document.body.style.overflow = 'hidden'; /* prevent page scroll behind overlay */
}

function closeCal_{{SLUG}}() {
  const overlay = document.getElementById('cal-overlay-{{SLUG}}');
  overlay.style.animation = 'calSlideDown .28s cubic-bezier(.33,1,.68,1) both';
  setTimeout(() => {
    overlay.style.display = 'none';
    overlay.style.animation = 'calSlideUp .32s cubic-bezier(.32,0,.67,0) both';
    document.body.style.overflow = '';
  }, 260);
}

/* Close on backdrop tap (outside iframe) */
document.getElementById('cal-overlay-{{SLUG}}')
  .addEventListener('click', function(e) {
    if (e.target === this) closeCal_{{SLUG}}();
  });

/* iOS: hide badge if blank */
(function() {
  const b = document.getElementById('cal-badge-{{SLUG}}');
  if (b && !b.textContent.trim()) b.style.display = 'none';
})();
</script>

<!-- ── END SCHEDULING TAP ─────────────────────────────────── -->
```

---

## Placement in BluePage

```
[Quick Action Strip]
[About Section]
[Share Section]
[Connect Section]
[Book & Pay Section]  ← scheduling tap goes here, FIRST row
  ├── 📅 {{TAP_LABEL}}   ← THIS
  └── 💳 Pay Your Invoice
[Reviews Section]
```

---

## Output Format When This Skill Triggers

1. Ask for: client slug, GHL calendar URL, desired label, desired subtitle, badge text (or blank)
2. Show the filled component — all `{{VARIABLES}}` replaced with real values
3. Remind placement: first row inside `Book & Pay` card
4. Note: the iframe lazy-loads on first tap — GHL calendar won't load until the customer actually opens the overlay, keeping the BluePage fast on initial load

---

## Quality Checklist

- [ ] `{{SLUG}}` replaced in ALL four places (openCal, closeCal, overlay ID, frame ID, badge ID)
- [ ] `{{CAL_URL}}` in `data-src` attribute — NOT in `src` (lazy loading)
- [ ] Badge span removed entirely if no badge needed (not just left blank)
- [ ] `body.style.overflow = 'hidden'` set on open, cleared on close
- [ ] Animation names don't conflict with other page animations
- [ ] GHL calendar URL tested before deploying — open it in a browser tab first
