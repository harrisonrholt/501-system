---
name: 501-call-tap
description: >
  Use this skill whenever Harrison asks about adding a call button, phone tap, call
  function, or any tap that lets a customer call a client from their BluePage. Also
  triggers for: "add a call tap", "phone tap", "how do I add calling", "call button
  on BluePage", "Oracle call tap", "business line tap", "cell number tap", or any
  request involving phone call functionality on a BluePage. This skill produces a
  single tap row that opens a bottom-sheet call menu with up to three options:
  Business Line, Owner Cell, and AI Oracle — Harrison picks which are enabled per
  client. Always ask for label text, which numbers to show, and whether Oracle is
  active before building.
---

# 501 Call Tap Skill

Single tap row → bottom sheet slides up → customer chooses which number to call.
Up to three options per client: Business Line, Owner Cell, AI Oracle.
Harrison enables only what the client has. Everything else is hidden.

---

## How It Works

1. Customer taps the call row
2. Bottom sheet slides up (same animation as scheduling overlay)
3. Shows only the enabled call options as large tap targets
4. Customer taps their choice → phone app opens immediately
5. Sheet closes automatically after tap, or customer swipes/taps backdrop to dismiss

---

## Variables Per Client

| Variable | What it is | Example |
|---|---|---|
| `{{SLUG}}` | Client slug for function naming | `mikes-plumbing` |
| `{{TAP_LABEL}}` | Main row label text | "Call Mike", "Call the Business" |
| `{{TAP_SUB}}` | Subtitle — auto-set based on Oracle | see below |
| `{{BIZ_PHONE}}` | Business/work line | `5015050001` |
| `{{BIZ_PHONE_DISPLAY}}` | Formatted business number | `(501) 505-0001` |
| `{{CELL_PHONE}}` | Owner cell | `5017728275` |
| `{{CELL_PHONE_DISPLAY}}` | Formatted cell | `(501) 772-8275` |
| `{{ORACLE_PHONE}}` | AI Oracle line | `5015054995` |
| `{{ORACLE_PHONE_DISPLAY}}` | Formatted Oracle number | `(501) 505-4995` |
| `{{BIZ_FIRST_NAME}}` | Owner first name | `Mike` |
| `{{ORACLE_ENABLED}}` | true or false | `true` |

### Subtitle auto-logic:
- Oracle enabled → `"AI answers after hours"`
- Oracle disabled, has business hours → `"[Hours] · [Days]"`
- Oracle disabled, no hours → `"Tap to call"`

---

## The Three Call Options

Harrison enables any combination per client. Remove the entire option block for
any number that doesn't apply. Never show a number that isn't real and active.

| Option | When to enable |
|---|---|
| **Business Line** | Client has a dedicated business number (GHL local number) |
| **Owner Cell** | Client is comfortable showing personal cell — usually for smaller/personal businesses |
| **AI Oracle** | Client has Oracle active — show as a 24/7 option |

---

## Full Component

Drop the tap row into the Connect card. The overlay goes anywhere on the page
outside the card — directly before `</div><!-- /page -->` is cleanest.

```html
<!-- ── CALL TAP ROW ─────────────────────────────────────────
     Skill: 501-call-tap
     Place inside the Connect .card.glass div, first row
     Variables: SLUG, TAP_LABEL, TAP_SUB, BIZ_FIRST_NAME
──────────────────────────────────────────────────────────── -->
<button onclick="openCall_{{SLUG}}()" class="tap-row">
  <div class="row-icon ri-green">📞</div>
  <div class="row-text">
    <div class="row-title">{{TAP_LABEL}}</div>
    <div class="row-sub">{{TAP_SUB}}</div>
  </div>
  <div class="row-arrow">›</div>
</button>
<!-- ── END CALL TAP ROW ──────────────────────────────────── -->


<!-- ── CALL BOTTOM SHEET ─────────────────────────────────────
     Place this just before </div><!- /page -> at bottom of page
──────────────────────────────────────────────────────────── -->
<div id="call-overlay-{{SLUG}}" style="
  display:none;
  position:fixed;
  inset:0;
  z-index:9998;
  background:rgba(0,0,0,0.55);
  backdrop-filter:blur(6px);
  -webkit-backdrop-filter:blur(6px);
  align-items:flex-end;
  justify-content:center;
">

  <!-- Sheet panel -->
  <div id="call-sheet-{{SLUG}}" style="
    width:100%;
    max-width:430px;
    background:rgba(14,18,34,0.97);
    border:1px solid rgba(255,255,255,0.10);
    border-bottom:none;
    border-radius:22px 22px 0 0;
    padding:0 16px 32px;
    animation:callSheetUp .30s cubic-bezier(.32,0,.67,0) both;
    backdrop-filter:blur(30px);
    -webkit-backdrop-filter:blur(30px);
    box-shadow:0 -8px 40px rgba(0,0,0,0.5),
               inset 0 1px 0 rgba(255,255,255,0.12);
  ">

    <!-- Drag handle -->
    <div style="
      width:36px;height:4px;
      background:rgba(255,255,255,0.18);
      border-radius:2px;
      margin:12px auto 20px;
    "></div>

    <!-- Sheet title -->
    <div style="
      font-size:13px;font-weight:700;
      color:rgba(255,255,255,0.35);
      text-transform:uppercase;letter-spacing:1.5px;
      text-align:center;margin-bottom:16px;
    ">How would you like to reach us?</div>

    <!-- ── OPTION A: BUSINESS LINE ──────────────────────────
         Remove this entire block if client has no business line
    ─────────────────────────────────────────────────────── -->
    <a href="tel:{{BIZ_PHONE}}" onclick="closeFast_{{SLUG}}()" style="
      display:flex;align-items:center;gap:14px;
      padding:16px 18px;border-radius:16px;
      background:rgba(48,209,88,0.12);
      border:1.5px solid rgba(48,209,88,0.25);
      text-decoration:none;margin-bottom:10px;
      backdrop-filter:blur(10px);
      box-shadow:inset 0 1px 0 rgba(255,255,255,0.10);
      transition:background .15s;
    " ontouchstart="this.style.background='rgba(48,209,88,0.22)'"
       ontouchend="this.style.background='rgba(48,209,88,0.12)'">
      <div style="
        width:42px;height:42px;border-radius:50%;
        background:rgba(48,209,88,0.20);
        border:1px solid rgba(48,209,88,0.30);
        display:flex;align-items:center;justify-content:center;
        font-size:20px;flex-shrink:0;
      ">📞</div>
      <div style="flex:1;">
        <div style="font-size:15px;font-weight:800;color:#fff;">Business Line</div>
        <div style="font-size:12px;color:rgba(255,255,255,0.45);margin-top:2px;">{{BIZ_PHONE_DISPLAY}}</div>
      </div>
      <div style="font-size:18px;color:rgba(255,255,255,0.25);">›</div>
    </a>
    <!-- ── END BUSINESS LINE ──────────────────────────────── -->

    <!-- ── OPTION B: OWNER CELL ────────────────────────────
         Remove this entire block if not showing personal cell
    ─────────────────────────────────────────────────────── -->
    <a href="tel:{{CELL_PHONE}}" onclick="closeFast_{{SLUG}}()" style="
      display:flex;align-items:center;gap:14px;
      padding:16px 18px;border-radius:16px;
      background:rgba(0,122,255,0.12);
      border:1.5px solid rgba(0,122,255,0.25);
      text-decoration:none;margin-bottom:10px;
      backdrop-filter:blur(10px);
      box-shadow:inset 0 1px 0 rgba(255,255,255,0.10);
      transition:background .15s;
    " ontouchstart="this.style.background='rgba(0,122,255,0.22)'"
       ontouchend="this.style.background='rgba(0,122,255,0.12)'">
      <div style="
        width:42px;height:42px;border-radius:50%;
        background:rgba(0,122,255,0.20);
        border:1px solid rgba(0,122,255,0.30);
        display:flex;align-items:center;justify-content:center;
        font-size:20px;flex-shrink:0;
      ">📱</div>
      <div style="flex:1;">
        <div style="font-size:15px;font-weight:800;color:#fff;">{{BIZ_FIRST_NAME}}'s Cell</div>
        <div style="font-size:12px;color:rgba(255,255,255,0.45);margin-top:2px;">{{CELL_PHONE_DISPLAY}} · Personal</div>
      </div>
      <div style="font-size:18px;color:rgba(255,255,255,0.25);">›</div>
    </a>
    <!-- ── END OWNER CELL ─────────────────────────────────── -->

    <!-- ── OPTION C: AI ORACLE ─────────────────────────────
         Remove this entire block if Oracle is not active
    ─────────────────────────────────────────────────────── -->
    <a href="tel:{{ORACLE_PHONE}}" onclick="closeFast_{{SLUG}}()" style="
      display:flex;align-items:center;gap:14px;
      padding:16px 18px;border-radius:16px;
      background:rgba(191,90,242,0.10);
      border:1.5px solid rgba(191,90,242,0.22);
      text-decoration:none;margin-bottom:10px;
      backdrop-filter:blur(10px);
      box-shadow:inset 0 1px 0 rgba(255,255,255,0.08);
      transition:background .15s;
    " ontouchstart="this.style.background='rgba(191,90,242,0.20)'"
       ontouchend="this.style.background='rgba(191,90,242,0.10)'">
      <div style="
        width:42px;height:42px;border-radius:50%;
        background:rgba(191,90,242,0.18);
        border:1px solid rgba(191,90,242,0.28);
        display:flex;align-items:center;justify-content:center;
        font-size:20px;flex-shrink:0;
      ">🤖</div>
      <div style="flex:1;">
        <div style="font-size:15px;font-weight:800;color:#fff;">AI Assistant</div>
        <div style="font-size:12px;color:rgba(255,255,255,0.45);margin-top:2px;">{{ORACLE_PHONE_DISPLAY}} · Answers 24/7</div>
      </div>
      <div style="font-size:18px;color:rgba(255,255,255,0.25);">›</div>
    </a>
    <!-- ── END AI ORACLE ───────────────────────────────────── -->

    <!-- Cancel button -->
    <button onclick="closeCall_{{SLUG}}()" style="
      width:100%;padding:14px;border-radius:50px;
      background:rgba(255,255,255,0.06);
      border:1px solid rgba(255,255,255,0.10);
      color:rgba(255,255,255,0.45);
      font-size:14px;font-weight:700;
      font-family:inherit;cursor:pointer;
      margin-top:4px;
    ">Cancel</button>

  </div>
</div>

<style>
@keyframes callSheetUp {
  from { transform: translateY(100%); }
  to   { transform: translateY(0); }
}
@keyframes callSheetDown {
  from { transform: translateY(0); }
  to   { transform: translateY(100%); }
}
</style>

<script>
function openCall_{{SLUG}}() {
  const overlay = document.getElementById('call-overlay-{{SLUG}}');
  const sheet   = document.getElementById('call-sheet-{{SLUG}}');
  overlay.style.display = 'flex';
  sheet.style.animation = 'callSheetUp .30s cubic-bezier(.32,0,.67,0) both';
  document.body.style.overflow = 'hidden';
}

function closeCall_{{SLUG}}() {
  const overlay = document.getElementById('call-overlay-{{SLUG}}');
  const sheet   = document.getElementById('call-sheet-{{SLUG}}');
  sheet.style.animation = 'callSheetDown .25s cubic-bezier(.33,1,.68,1) both';
  setTimeout(() => {
    overlay.style.display = 'none';
    document.body.style.overflow = '';
  }, 230);
}

/* Close immediately after number tap — phone app takes over */
function closeFast_{{SLUG}}() {
  const overlay = document.getElementById('call-overlay-{{SLUG}}');
  overlay.style.display = 'none';
  document.body.style.overflow = '';
}

/* Tap backdrop to dismiss */
document.getElementById('call-overlay-{{SLUG}}')
  .addEventListener('click', function(e) {
    if (e.target === this) closeCall_{{SLUG}}();
  });
</script>
<!-- ── END CALL BOTTOM SHEET ─────────────────────────────── -->
```

---

## Which Options to Enable Per Client

| Client situation | Enable |
|---|---|
| Has GHL local number, no Oracle | Business Line only |
| Solo operator, personal cell, no GHL number | Cell only |
| Has GHL number + Oracle active | Business Line + Oracle |
| Comfortable showing cell + has Oracle | Cell + Oracle |
| Full setup — GHL number, cell, Oracle | All three |
| Just getting started, call-only | Business Line only |

**Rule:** Never show a number that isn't actively monitored or answered.
A ringing number that goes unanswered is worse than no call option.

---

## Placement in BluePage

```
[Connect Section]
  ├── 📞 {{TAP_LABEL}}   ← CALL TAP — first row
  ├── 💬 Send a Text
  └── 👤 Save to My Phone
```

---

## Output Format When This Skill Triggers

1. Ask for: slug, tap label, which options to enable (Business/Cell/Oracle — any combo)
2. Ask for each enabled number: raw digits + formatted display version
3. Ask for owner first name (for "Mike's Cell" label)
4. Ask if Oracle is active — if yes, `TAP_SUB` = "AI answers after hours"
5. Output the filled component — all variables replaced, disabled option blocks removed
6. Remind placement: first row in Connect card, overlay before `</div><!-- /page -->`

---

## Quality Checklist

- [ ] `{{SLUG}}` replaced in ALL instances (openCall, closeCall, closeFast, overlay ID, sheet ID)
- [ ] Disabled option blocks removed entirely — not commented out
- [ ] Phone numbers in `href` are digits only: `tel:5015050001`
- [ ] Display numbers formatted: `(501) 505-0001`
- [ ] `body.overflow` cleared on both close paths
- [ ] Oracle block only present if Oracle is actually active for this client
- [ ] Cancel button always present regardless of options shown
