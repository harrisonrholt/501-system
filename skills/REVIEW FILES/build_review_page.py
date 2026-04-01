#!/usr/bin/env python3
"""
501 Digital Marketing — Review Page + BluePage Builder
Run this in Terminal to generate both files at once.

Usage:
  1. Edit the CLIENT dict below with the client's info
  2. Run: python3 build_review_page.py
  3. Two files drop into ~/Desktop/[slug]-deploy/
     - [slug]-review.html   → upload to 501.business/[slug]-review
     - bluepage-tap-row.html → copy the tap row into their BluePage

Master webhook URL is set once at the top and never changes.
"""

import os, re, shutil
from datetime import datetime

# ── MASTER CONFIG — set once, never changes per client ──────────
MASTER_WEBHOOK = "https://services.leadconnectorhq.com/hooks/YOUR_HOOK_ID/webhook-trigger/YOUR_TRIGGER_ID"
TEMPLATES_DIR  = os.path.expanduser("~/501-dashboard/review-templates/")
OUTPUT_BASE    = os.path.expanduser("~/Desktop/")

# ── CLIENT CONFIG — edit this block per client ──────────────────
CLIENT = {
    "slug":          "mikes-plumbing",         # URL slug, no spaces
    "biz_name":      "Mike's Plumbing",         # Full business name
    "biz_first":     "Mike",                    # Owner first name
    "biz_category":  "Plumbing · Conway, AR",  # Trade + city tag
    "brand_color":   "#007AFF",                 # Brand hex color
    "logo_emoji":    "🔧",                      # Fallback emoji

    # Review platform links — paste the actual URL for each.
    # Set to None to hide that platform on the page.
    "google_url":     "https://search.google.com/local/writereview?placeid=PLACE_ID_HERE",
    "yelp_url":       "https://www.yelp.com/writeareview/biz/YELP_ID_HERE",  # or None
    "facebook_url":   "https://www.facebook.com/PAGE_SLUG/reviews/",          # or None
    "trustpilot_url": None,  # e.g. "https://www.trustpilot.com/evaluate/domain.com"
}
# ─────────────────────────────────────────────────────────────────


def build(client):
    slug = client["slug"]
    output_dir = os.path.join(OUTPUT_BASE, f"{slug}-deploy")
    os.makedirs(output_dir, exist_ok=True)

    # ── Read review page template ──
    tpl_path = os.path.join(TEMPLATES_DIR, "[SLUG]-review.html")
    with open(tpl_path, "r") as f:
        html = f.read()

    # ── Swap all variables ──
    html = html.replace("{{SLUG}}",             slug)
    html = html.replace("{{BIZ_NAME}}",         client["biz_name"])
    html = html.replace("{{BIZ_FIRST_NAME}}",   client["biz_first"])
    html = html.replace("{{BIZ_CATEGORY}}",     client["biz_category"])
    html = html.replace("{{BRAND_COLOR}}",      client["brand_color"])
    html = html.replace("{{LOGO_EMOJI}}",       client["logo_emoji"])
    html = html.replace("{{MASTER_WEBHOOK_URL}}", MASTER_WEBHOOK)
    html = html.replace("{{GOOGLE_REVIEW_URL}}", client["google_url"] or "#")

    # ── Handle optional platforms ──
    html = _inject_platform(html, "YELP",       client["yelp_url"])
    html = _inject_platform(html, "FACEBOOK",   client["facebook_url"])
    html = _inject_platform(html, "TRUSTPILOT", client["trustpilot_url"])

    # ── Write review page ──
    review_path = os.path.join(output_dir, f"{slug}-review.html")
    with open(review_path, "w") as f:
        f.write(html)
    print(f"✅ Review page: {review_path}")

    # ── Generate BluePage tap row snippet ──
    tap_row = f"""<!-- 501 REVIEW TAP ROW — paste into BluePage Reviews card -->
<!-- Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')} for {client['biz_name']} -->

<a href="https://501.business/{slug}-review" class="tap-row">
  <div class="row-icon ri-gold">⭐</div>
  <div class="row-text">
    <div class="row-title">Rate Your Experience</div>
    <div class="row-sub">Tap to leave a quick star rating</div>
  </div>
  <div class="row-arrow">›</div>
</a>

<!-- Deploy review page to: 501.business/{slug}-review -->
"""
    tap_path = os.path.join(output_dir, "bluepage-tap-row.html")
    with open(tap_path, "w") as f:
        f.write(tap_row)
    print(f"✅ BluePage tap row: {tap_path}")

    # ── Summary ──
    print(f"""
╔══════════════════════════════════════════════════════╗
║  BUILD COMPLETE — {client['biz_name']:<33} ║
╠══════════════════════════════════════════════════════╣
║  Deploy review page to:                              ║
║  501.business/{slug}-review{' '*(38-len(slug))}║
║                                                      ║
║  Then paste bluepage-tap-row.html content into       ║
║  the Reviews section of their BluePage.              ║
╚══════════════════════════════════════════════════════╝
""")


def _inject_platform(html, key, url):
    """Remove platform block if URL is None, else swap URL."""
    start_tag = f"{{{{#IF_{key}}}}}"
    end_tag   = f"{{{{/IF_{key}}}}}"
    if url is None:
        # Remove entire block including tags
        pattern = re.compile(
            re.escape(start_tag) + r".*?" + re.escape(end_tag),
            re.DOTALL
        )
        return pattern.sub("", html)
    else:
        html = html.replace(start_tag, "").replace(end_tag, "")
        return html.replace(f"{{{{{key}_REVIEW_URL}}}}", url)


if __name__ == "__main__":
    build(CLIENT)
