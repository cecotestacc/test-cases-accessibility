# shared-components — QualiBooth Shared Element Grouping Test Set

This folder contains 25 HTML pages that form a controlled test environment for QualiBooth's **shared components** feature — the portal capability that groups accessibility issues by CSS selector across all pages in a scan run, then displays per-component statistics (pages affected, issue count, severity breakdown, share of run, issue types).

The pages simulate a fictional e-commerce site called **Lumino**. Every accessibility violation is intentional and precisely placed. Nothing in these pages should be changed without updating the three reference documents below.

---

## The three documents

| File | Purpose |
|---|---|
| [`summary.html`](summary.html) | What was built: all 16 shared components, the violations engineered into each, the page inventory, and the QualiBooth scan config used. Start here to understand the test set. |
| [`test-coverage.html`](test-coverage.html) | What is tested: every portal metric, severity level, selector type, issue type, and page-count range covered by this test set. Includes the scan-depth matrix (axe-core vs behavioral), the 3 gap scenarios that were added, and the key regression assertions. |
| [`expected-results.html`](expected-results.html) | The regression baseline: exact expected values for every component (pages affected, %, issues, share of run, issue types). Use this when comparing scan results against what the portal should show. |

---

## Quick stats

| Dimension | Value |
|---|---|
| Pages | 25 |
| Shared components | 16 |
| Accessibility issue types | 14 |
| Severity levels | Critical, High, Moderate, Low (all 4) |
| Estimated total violations | ~761 |
| Scan config | `SharedComponents-tests` (org: `ceco`, QualiBooth dev) |

---

## Component overview

| Selector | Pages affected | Severity | Issue types |
|---|---|---|---|
| `meta[name="viewport"]` | 25/25 (100%) | Critical | 1 |
| `nav.site-nav` | 25/25 (100%) | Moderate + High | 1–2 |
| `nav.footer-nav` | 25/25 (100%) | Moderate | 1 |
| `h3.section-title` | 20/25 (80%) | Moderate | 1 |
| `.cookie-btn` | 20/25 (80%) | Critical | 1 |
| `.ghost-cta` | 18/25 (72%) | High | 1 |
| `#promo-bar` | 15/25 (60%) | High | 1 |
| `.hero-section` | 10/25 (40%) | High | 1 |
| `.tooltip-btn` | 8/25 (32%) | Critical + High | 1–4 |
| `#toast-region` | 6/25 (24%) | High | 1 |
| `#product-modal` | 5/25 (20%) | Critical | 1 |
| `.modal-close` | 5/25 (20%) | High | 1 |
| `.newsletter-input` | **5/25** violations (element on 8/25) | Critical | 1 |
| `h2.section-divider` | 3/25 (12%) | **Low** | 1 |
| `.flash-sale-chip` | 2/25 (8%) | Critical | 1 |
| `#featured-promo` | 1/25 (4%) | Critical | 1 |

---

## How to run a regression test

1. Open QualiBooth dev portal → org `ceco` → project `cecotestacc.github.io`
2. Go to scan configs → **SharedComponents-tests**
3. Trigger a manual scan and wait for all 25 URLs to complete
4. Open the **Shared Components** tab in the run results
5. Compare every metric against [`expected-results.html`](expected-results.html)
6. Pay special attention to the three key assertions in that document:
   - `.newsletter-input` must show **5/25** pages, not 8/25
   - `#featured-promo` must show **1/25** pages
   - `h2.section-divider` must show **Low** severity

---

## Pages at a glance

| Pages | Has `#promo-bar` | Has `#cookie-banner` | Has `.hero-section` | Has `.tooltip-btn` | Has `#toast-region` | Has `#product-modal` | Has `h3.section-title` | Has `.ghost-cta` |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| home, shop-all, sale, new-arrivals, trending (1–5) | ✓ | ✓ | ✓ | ✓ | | | ✓ | ✓ |
| product-running-shoes, product-training-shoes, product-shirts (6–8) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| product-jackets, product-accessories (9–10) | ✓ | ✓ | ✓ | | ✓ | ✓ | ✓ | ✓ |
| mens (11) | ✓ | ✓ | | | ✓ | | ✓ | ✓ |
| womens, kids, brands, collections (12–15) | ✓ | ✓ | | | | | ✓ | ✓ |
| blog, blog-post-performance, blog-post-sustainability (16–18) | | ✓ | | | | | ✓ | ✓ |
| blog-post-style, lookbook (19–20) | | ✓ | | | | | ✓ | |
| account, orders, faq, careers, store-locator (21–25) | | | | | | | | |

Universal on all 25 pages: `meta[name="viewport"]` (violation), `nav.site-nav` (violation), `nav.footer-nav` (violation).

**Gap-coverage components** (not in the table above):

| Component | Pages with violation | Pages with element, no violation |
|---|---|---|
| `h2.section-divider` (Low severity) | home, blog, faq | — |
| `#featured-promo` (1-page minimum) | home only | — |
| `.flash-sale-chip` (2-page minimum) | sale, new-arrivals | — |
| `.newsletter-input` (element present, no violation test) | home, shop-all, sale, new-arrivals, trending | blog, blog-post-performance, blog-post-sustainability |

---

## GitHub Pages base URL

```
https://cecotestacc.github.io/test-cases-accessibility/shared-components/
```
