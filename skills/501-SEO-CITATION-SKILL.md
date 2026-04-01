---
name: 501-seo-citation-network
description: >
  Use this skill whenever Harrison asks about SEO, posting a client on multiple domains,
  maximizing citation coverage, writing domain-specific listings, building BluePage SEO
  strategy, or making SEO claims about 501 Digital Marketing's services. Also triggers
  for: "post this business everywhere", "how do I list a client", "what domains should
  I use", "SEO for my client", "citation network", "maximize rankings", "unique copy
  per domain", "canonical tags", or any question about Harrison's domain portfolio strategy.
  This skill operationalizes Harrison's self-owned citation network across his domain
  portfolio and shows him exactly what to build, write, and deploy per client.
---

# 501 Citation Network Skill

Harrison owns a self-built local SEO citation network. This skill tells Claude exactly
how to help him use it — from onboarding a new client to generating unique copy across
every domain to building the canonical tag structure to writing SEO claims he can sell.

---

## The Domain Portfolio

| Domain | Role | Niche |
|---|---|---|
| `501.business` | **Primary hub** — BluePage hosting, main agency site | All trades |
| `501.contractors` | Contractor-specific directory | General contractors, remodelers |
| `501.plumbing` | Hyper-niche directory | Plumbers only |
| `501.digital` | Agency brand / tech content | 501 brand |
| `501.marketing` | Marketing content / thought leadership | 501 brand |
| `harryslist.social` | Social-forward local discovery | All local businesses |
| `harryslist.pro` | Professional service provider listings | Service businesses |
| `turnsoutimprettygoodathis.com` | Personal brand / story / credibility content | Harrison's voice |

All client BluePage pages are **canonically hosted at** `501.business/[clientslug]`.
Every other domain listing points back to that as the canonical URL.

---

## Core Rules — Never Break These

1. **NAP must be identical everywhere** — Name, Address (or service area), Phone.
   Even "St." vs "Street" or "(501)" vs "501-" counts as a mismatch and hurts rankings.

2. **Every listing needs unique copy** — Minimum 50% different from every other domain.
   Same template, different sentences. This avoids Google's duplicate content filter.

3. **rel=canonical on every BluePage variant** pointing to `501.business/[slug]`.

4. **Never list a business on a domain where it doesn't fit the niche** — a plumber
   on `501.plumbing` is correct. A plumber on `501.marketing` is noise.

---

## Workflow: Onboarding a New Client to the Citation Network

### Step 1 — Gather NAP + Core Info

Collect and lock down before writing anything:

```
Business Name:     [exact, how it appears on their truck/sign]
Service Area:      [city, county, or "Central Arkansas"]
Primary Phone:     [formatted: (501) XXX-XXXX]
Secondary Phone:   [if any]
Email:             [contact email]
Website:           [their existing site if any]
GBP Link:          [Google Business Profile URL]
Google Review Link:[shortlink from GBP]
Trade Category:    [HVAC / Plumbing / Roofing / Electrical / Landscaping / etc]
Tagline:           [1 line, under 60 chars]
Year Founded:      [if known]
Owner First Name:  [for vCard and personal tone]
```

### Step 2 — Decide Which Domains Apply

Use this decision tree:

- Always: `501.business` (primary BluePage)
- Always: `harryslist.social` (social-forward discovery)
- Always: `harryslist.pro` (professional listing)
- If contractor/remodeler/handyman: `501.contractors`
- If plumber specifically: `501.plumbing`
- Optional for credibility: `turnsoutimprettygoodathis.com` (story format only)

Do NOT use `501.digital` or `501.marketing` for client listings — those are Harrison's brand.

### Step 3 — Generate Unique Copy Per Domain

For each applicable domain, write a **unique business description**. Each one must:
- Start with a different first sentence
- Emphasize a different value angle (see angle guide below)
- Be 60–150 words
- Include the trade, service area, and business name naturally
- End with a soft CTA

**Angle Guide — Use a different angle per domain:**

| Domain | Angle to Lead With |
|---|---|
| `501.business` | Full system — website, phone, reviews, app |
| `harryslist.social` | Community trust, word-of-mouth, local reputation |
| `harryslist.pro` | Professional credentials, reliability, licensing |
| `501.contractors` | Workmanship, project quality, service area coverage |
| `501.plumbing` | Speed, emergency availability, fair pricing |

**Example — Same plumber, two different domains:**

*501.business version:*
> "Mike's Plumbing is a Central Arkansas plumbing company serving Conway, Cabot, and
> Searcy. Mike runs a fully digital operation — customers can book online, pay instantly,
> and save his number directly to their phone. If you need a plumber who actually picks
> up, this is the guy."

*harryslist.social version:*
> "Ask anyone in Conway who they call for plumbing — Mike's name comes up every time.
> He's been fixing pipes in Central Arkansas for over a decade, and his Google reviews
> back it up. One tap books an estimate. One tap pays the invoice. Old-school trust,
> new-school convenience."

### Step 4 — Build the HTML Head Block (BluePage)

Every BluePage at `501.business/[slug]` must include this in `<head>`:

```html
<!-- Canonical — tells Google this is the primary version -->
<link rel="canonical" href="https://501.business/[clientslug]">

<!-- Open Graph — controls how it looks when shared on Facebook/text -->
<meta property="og:title" content="[Business Name] — [Trade] in [City], AR">
<meta property="og:description" content="[Tagline or first sentence of description]">
<meta property="og:url" content="https://501.business/[clientslug]">
<meta property="og:type" content="business.business">

<!-- Local Business Schema — the machine-readable citation Google loves most -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "[Business Name]",
  "telephone": "[raw: +1501XXXXXXX]",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "[City]",
    "addressRegion": "AR",
    "addressCountry": "US"
  },
  "areaServed": "[City, AR]",
  "description": "[60-word description]",
  "url": "https://501.business/[clientslug]"
}
</script>
```

### Step 5 — Build the Other Domain Listings

For each non-primary domain, create a simple listing page (HTML or markdown) with:

```html
<head>
  <!-- Point all variants back to the canonical source -->
  <link rel="canonical" href="https://501.business/[clientslug]">
  <title>[Business Name] | [Domain Name]</title>
</head>
```

Content structure per listing:
1. Business name + trade badge
2. Unique description (from Step 3 — angle matched to domain)
3. NAP block (exact same format every time)
4. Tap links: Call, Book, Pay, Review
5. "Full profile →" link pointing to `501.business/[slug]`

---

## SEO Claims Harrison Can Make to Clients

Once a client is live on the citation network, Harrison can legitimately say:

**Basic (1-2 domains):**
> "Your business is now indexed on multiple local web properties — each one sends a
> trust signal to Google that you're a real, established business in Central Arkansas."

**Mid (3-4 domains):**
> "You're listed across four local directories I own, all pointing back to your
> primary page. Google sees consistent business information from multiple sources —
> that's what pushes you up in 'near me' searches."

**Full network (5+ domains):**
> "Your business has a citation footprint across my entire Central Arkansas network.
> Every domain we're listed on adds a data point that Google uses to confirm your
> business is legitimate, active, and local. This is the same thing big companies pay
> Yext $999/year to do — you're getting it built into your monthly service."

**For the 501 agency itself (Harrison's own SEO pitch):**
> "501 Digital Marketing isn't just a vendor — we operate the largest local business
> citation network in Central Arkansas. When you're a client, your business gets listed
> across our owned properties, giving you organic citation coverage that most agencies
> can't offer because they don't own the infrastructure."

---

## Citation Tracking Template

When a client goes live, maintain this record:

```
CLIENT: [Business Name]
SLUG: [clientslug]
CANONICAL: 501.business/[slug]
NAP LOCKED: [Name · Phone · Service Area]

DOMAIN LISTING STATUS:
[ ] 501.business/[slug]          — PRIMARY (canonical)
[ ] harryslist.social/[slug]     — community angle
[ ] harryslist.pro/[slug]        — professional angle
[ ] 501.contractors/[slug]       — if applicable
[ ] 501.plumbing/[slug]          — if plumber

SCHEMA ADDED: [ ] Yes  [ ] No
CANONICAL TAG: [ ] Yes  [ ] No
OG TAGS: [ ] Yes  [ ] No
GBP CLAIMED: [ ] Yes  [ ] No

COPY UNIQUE PER DOMAIN: [ ] Verified
NAP CONSISTENT: [ ] Verified
```

---

## What to Build Per Domain Over Time

Priority order for deploying the network — don't try to do everything at once:

**Phase 1 (do first):**
- `501.business` — BluePage live, schema added, canonical set
- `harryslist.social` — simple listing with social angle copy

**Phase 2 (after first 3 clients are live):**
- `501.contractors` — build as a real directory page with 3+ listings
- `harryslist.pro` — professional directory format

**Phase 3 (as niche depth grows):**
- `501.plumbing` — launch only once you have 3+ plumbers to list
- `turnsoutimprettygoodathis.com` — story posts about specific clients (no-index or
  canonical to 501.business if re-using business copy)

The reason to wait: a directory with 1 listing has almost no SEO value. A directory
with 6–10 listings that Google can crawl as a category page starts to rank on its own.

---

## Quick Reference — Files to Read Next

- For building the BluePage HTML: see `bluepage-liquid-glass.html` template
- For referral tracking setup: GHL custom field `Referral Source` + URL param `?ref=`
- For Facebook posts about the citation network: use cognitive viology loop
  (attach → enter → replicate → defend → transmit) applied to local trust

---

## Output Format When Helping Harrison

When this skill triggers, Claude should:

1. Ask which client / which domain(s) if not specified
2. Confirm NAP is locked before writing any copy
3. Output copy in a clearly labeled block per domain
4. Include the full HTML `<head>` block ready to paste
5. Output a pre-filled citation tracking record
6. Suggest which SEO claim tier Harrison can make based on coverage

Always keep copy under 150 words per listing. Always verify NAP is word-for-word
identical across all outputs before presenting to Harrison.
