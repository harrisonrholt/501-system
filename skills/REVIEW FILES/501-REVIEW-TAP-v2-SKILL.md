---
name: 501-review-tap-page
description: >
  Use this skill whenever Harrison asks about review pages, getting more Google reviews,
  building a star rating page for a client, targeting businesses with low reviews,
  "review tap", "star rating flow", "private feedback page", "how do I send customers
  to leave a review", "build a review page", or any request involving a review collection
  page. Also triggers for: prospecting businesses with low star ratings, writing the cold
  pitch for review services, setting up the GHL master webhook for feedback, or generating
  the BluePage tap row snippet. This skill produces the complete two-file build (review
  page + BluePage tap row) plus the Python build script, GHL automation setup, and
  prospecting pitches. Always use this skill — never guess the URL formats for Google,
  Yelp, Facebook, or Trustpilot review links.
---

# 501 Review Tap Page Skill v2

Produces a compliant 5-star rating page for any Central Arkansas client.
4–5 stars → platform picker (Google, Yelp, Facebook, Trustpilot — only platforms client has).
1–2–3 stars → private text feedback → master 501 GHL webhook → thank you screen.
Google link always remains accessible. Fully compliant with Google + FTC policy.

---

## The Legal Line — Never Cross It

**COMPLIANT (what this page does):**
- Everyone sees both paths — no one is blocked from Google
- 1–3 stars: private form is the primary path, but Google is not hidden
- 4–5 stars: platform picker is primary, no private form needed

**PROHIBITED (never build this):**
- Hiding the Google link from 1–3 star customers
- Pre-filtering who gets sent the review request at all
- Incentivizing reviews (gift cards, discounts for leaving a review)

---

## Flow Summary

```
[Star tap]
    ├── 4 or 5 ★ → Platform Picker screen
    │              Google (always) + Yelp/FB/Trustpilot (if client has them)
    │              → customer taps platform → opens review site in new tab
    │
    └── 1, 2, or 3 ★ → Private Feedback screen
                       Text box (max 600 chars)
                       Submit → POST to master 501 webhook → Thank You screen
```

---

## Review Platform Deep-Link Formats

### Google (Required — always include)
**How to get it:** GBP dashboard → "Ask for reviews" → copy the `g.page/...` link
**OR** build it manually: `https://search.google.com/local/writereview?placeid=PLACE_ID`
- Get Place ID from Google Maps URL when viewing the business listing
- Format: `https://search.google.com/local/writereview?placeid=ChIJ...`
- Opens review box directly. Permanent link.

### Yelp (Optional)
**How to get it:** Go to yelp.com → find business → click "Write a Review" → copy URL
- Format: `https://www.yelp.com/writeareview/biz/[YELP_BUSINESS_ID]`
- Note: Yelp discourages soliciting reviews. Use only if client already has a Yelp presence.

### Facebook (Optional)
**How to get it:** Go to their Facebook Page → click Reviews tab → copy URL
- Format: `https://www.facebook.com/[PAGE_SLUG]/reviews/`
- If no Reviews tab: reviews are disabled — skip this platform

### Trustpilot (Optional)
**How to get it:** Find or create business profile on Trustpilot → click "Write a review"
- Format: `https://www.trustpilot.com/evaluate/[BUSINESSDOMAIN.COM]`
- No account needed to generate the link — just replace domain

---

## Webhook Setup — One Time, Ever

Set up ONE master webhook in GHL. All clients use the same URL forever.

**GHL Setup:**
1. GHL → Automations → New Workflow → Webhook Trigger
2. Name it: `501 Private Review Feedback`
3. Copy the webhook URL — this is `MASTER_WEBHOOK_URL` in the build script

**The payload that arrives per submission:**
```json
{
  "business_slug": "mikes-plumbing",
  "business_name": "Mike's Plumbing",
  "star_rating": 2,
  "feedback": "The tech was late and didn't explain the cost",
  "page_url": "https://501.business/mikes-plumbing-review",
  "timestamp": "2026-03-26T14:23:00Z"
}
```

**GHL Automation Actions (build once, applies to all clients):**
1. Create/update contact — use `business_name` field to tag
2. Add tag: `private-feedback-received`
3. Add tag: `{{business_slug}}-feedback`
4. Assign task: "Follow up on private feedback" → due in 24 hours
5. Send SMS to owner: "⚠️ Private feedback received from a customer of {{business_name}}. Check GHL tasks."

No second email to customer. No follow-up asking them to reconsider Google. Done.

---

## Build Process — Both Files at Once

**Template files live at:** `~/501-dashboard/review-templates/`
- `[SLUG]-review.html` — the review tap page template
- `build_review_page.py` — the build script

**To deploy a new client:**
1. Open `build_review_page.py` in any text editor
2. Edit the `CLIENT` dict at the top — 8 fields
3. Set platforms to `None` for any they don't have
4. Run: `python3 ~/501-dashboard/review-templates/build_review_page.py`
5. Two files drop to `~/Desktop/[slug]-deploy/`:
   - `[slug]-review.html` → upload to Cloudflare → connects to `501.business/[slug]-review`
   - `bluepage-tap-row.html` → paste the one tap row into their existing BluePage Reviews card

**That's it. Build time: under 5 minutes per client.**

---

## How to Find Low-Review Businesses to Target

### Method 1 — GHL Prospecting Tool (Best)
GHL → Agency → Prospecting Tool → search "[trade] Conway AR"
Filter by review count. Export leads. Send the audit report directly from GHL.

### Method 2 — Google Maps
Search "[trade] Conway AR" → sort results by rating
Target: under 4.0 stars OR under 20 reviews

### Method 3 — Facebook Groups
Search "Conway Arkansas" or "Central AR Home Owners" groups
Find posts asking for contractor recommendations — missing businesses are leads

### Method 4 — Google Operator
`site:google.com "Conway AR" "plumber"` — surfaces GBP listings with low ratings

---

## Cold Pitch Texts

**SMS (under 100 words):**
> "Hey [FirstName] — found [BusinessName] on Google. You've got [X] reviews right now.
> Most people won't call a business under 20 reviews, no matter how good the work is.
> I build a one-tap page that makes it dead easy for happy customers to leave you a
> review right after the job. Takes about a day. Want to see what it looks like?
> — Harrison, 501 Digital (501) 772-8275"

**In-person (30 sec):**
> "I noticed your Google reviews. 68% of people won't hire a business under 4 stars.
> I build a one-tap page you text to customers right after a job — they tap a star,
> happy ones go straight to Google, unhappy ones go straight to you privately.
> Most clients triple their review count in 60 days. Want me to show you?"

---

## SEO Claims for This Service

**To the client:**
> "Google reviews are the #3 local ranking factor. More reviews = higher placement
> in the map pack = more calls. This page makes it frictionless for happy customers
> to follow through, and routes unhappy ones to you privately so you can fix it before
> it goes public."

**On 501 listings:**
> "Review acceleration system — 5-star tap page that routes happy customers to Google,
> Yelp, Facebook, or Trustpilot and captures private feedback from unhappy ones.
> Clients average 3–5× more reviews in 90 days."

---

## Output Format When This Skill Triggers

When triggered, Claude should:
1. Confirm: business name, slug, owner first name, brand color, logo emoji
2. Confirm: which platforms does this client actually have? (Google always yes)
3. Confirm: their Google Place ID or review link (most important)
4. Output the filled `CLIENT` dict ready to paste into the build script
5. Output the GHL webhook automation steps (if not already built)
6. Output the cold pitch texts customized for this specific business
