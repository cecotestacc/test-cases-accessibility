# shared-components — Folder Instructions for Claude

This file overrides the repo-level `CLAUDE.md` rules for everything inside `shared-components/`. Read this file **instead of** the parent rules when working here.

---

## What this folder is

A controlled test set for QualiBooth's **shared components** feature — the portal view that groups accessibility issues by CSS selector across pages and shows per-component statistics. The 25 pages simulate a fictional e-commerce site (Lumino). Every violation is intentional and engineered to produce predictable, verifiable counts.

**These are not accessibility test cases in the `behaviour-feature/` sense.** They are realistic site pages whose violations are carefully placed to test a specific portal feature.

---

## What this folder is NOT

- Do **not** add QA panels (`<div class="qa-panel">`) — these pages must look like real site pages.
- Do **not** assign case numbers (`Case #N`) — the sequential case numbering system does not apply here.
- Do **not** apply the parent CLAUDE.md file template (no `qa-panel` CSS, no `qa-error-tag`, no `qa-pass-tag`).
- Do **not** add `CustomHTMLElements.html` — that convention belongs to `behaviour-feature/`.

---

## The four reference files — always keep in sync

Every change to the test pages or component design must be reflected in the reference files **in the same commit**. Never commit a page change without also updating the affected reference files. The table below maps change type to which files need updating and what specifically changes.

| Change type | README.md | summary.html | expected-results.html | test-coverage.html |
|---|---|---|---|---|
| **New page added** | Page inventory matrix row | Page inventory table row | Per-page table row | — |
| **Page removed** | Remove row | Remove row | Remove row | — |
| **New shared component added** | Component overview table row, gap-coverage table if applicable | Component architecture table row, issue types table row if new type, supplementary table if gap-coverage | Component card block, acceptance criteria card | Component inventory row, issue types table row if new type, page count range table row, severity coverage, scan depth matrix row |
| **Component removed** | Remove row | Remove row | Remove component card | Remove rows |
| **Component page count changes** | Update pages column | Update pages/coverage/issues/share columns | Update component card metrics and acceptance criteria | Update component inventory row and page count range table |
| **Violation severity corrected** | Update severity column | Update severity badge | Update impact pill in component card | Update severity in issue types table and component inventory |
| **Violation mechanism changes** (e.g. static → JS) | — | Update issue types table description | Update component card description | Update scan depth matrix notes |
| **aria-controls value, tooltip ID, or other ARIA fix** | — | Update component description in issue types table | — | — |
| **New issue type introduced** | Update "Accessibility issue types" count in quick stats | Update "All N issue types" count, add row to issue types table | Update run-level baseline "Distinct issue types" metric | Update "All N types covered" scorecard, add row to issue types table, update heading |
| **Total violation count changes** | Update "Estimated total violations" | Update ~N metric | Update run-level baseline and all share% values | Update ~N in metrics |
| **Scan results available (new scan run)** | — | — | Update all baseline values, add uncertainty notes | — |

### Specific fields to update per file

**README.md** — update when: page count changes, component count changes, violation count changes, severity changes, new gap-coverage component added.
- Quick stats table: Pages, Shared components, Accessibility issue types, Severity levels, Estimated total violations
- Component overview table: all rows (pages/%, severity, issue types count)
- Pages at a glance matrix: add/remove rows
- Gap-coverage component table: add/remove rows, update violation/pass page lists

**summary.html** — update when: anything in the component or page structure changes.
- Header meta line: component count, issue type count
- TL;DR text: component count, issue type count, coverage range (min → max %)
- Coverage Statistics metrics: component count, issue type count, total violations
- Component Architecture table: all rows, share percentages (recalculate against new total)
- Issue Types Covered table: heading count, rows
- Page Inventory table: add/remove rows
- Gap Coverage Components supplementary table: add/remove rows, update violation/pass columns

**expected-results.html** — update when: a new scan run completes OR expected values change.
- Run-Level Baseline metrics
- Each component card: pages, %, issues, share, types, sub-issue occurrences/pages
- Per-page table: add/remove rows, update violation columns
- Regression Acceptance Criteria scorecard: update expected values and tolerances

**test-coverage.html** — update when: component count, issue type count, severity labels, scan depth, or page count range changes.
- Coverage at a glance metrics: component count, issue type count, severity level count, total violations
- "Issue types per component" scorecard note: update the "(N components)" with 1 type
- "Issue type names + severities" scorecard: update "All N types covered"
- All N components table: add/remove rows, update severity/issues columns
- Severity level coverage findings: update component lists per severity
- All N accessibility issue types table: heading, add/remove rows, fix severity labels
- Page count range table: add/remove rows
- Scan depth matrix: add/remove rows, fix axe-core/behavioral classification
- Scan depth footnote: update component counts

---

## Component assignment — the authoritative table

This table defines exactly which components appear on which pages. Do not deviate from it without also updating all four reference files and the QualiBooth scan config.

| Page | promo-bar | cookie-btn | hero | tooltip | toast | modal | h3-skip | ghost-cta | newsletter (violation) | newsletter (pass) |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| home.html | ✓ | ✓ | ✓ | ✓ | | | ✓ | ✓ | ✓ | |
| shop-all.html | ✓ | ✓ | ✓ | ✓ | | | ✓ | ✓ | ✓ | |
| sale.html | ✓ | ✓ | ✓ | ✓ | | | ✓ | ✓ | ✓ | |
| new-arrivals.html | ✓ | ✓ | ✓ | ✓ | | | ✓ | ✓ | ✓ | |
| trending.html | ✓ | ✓ | ✓ | ✓ | | | ✓ | ✓ | ✓ | |
| product-running-shoes.html | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | | |
| product-training-shoes.html | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | | |
| product-shirts.html | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | | |
| product-jackets.html | ✓ | ✓ | ✓ | | ✓ | ✓ | ✓ | ✓ | | |
| product-accessories.html | ✓ | ✓ | ✓ | | ✓ | ✓ | ✓ | ✓ | | |
| mens.html | ✓ | ✓ | | | ✓ | | ✓ | ✓ | | |
| womens.html | ✓ | ✓ | | | | | ✓ | ✓ | | |
| kids.html | ✓ | ✓ | | | | | ✓ | ✓ | | |
| brands.html | ✓ | ✓ | | | | | ✓ | ✓ | | |
| collections.html | ✓ | ✓ | | | | | ✓ | ✓ | | |
| blog.html | | ✓ | | | | | ✓ | ✓ | | ✓ |
| blog-post-performance.html | | ✓ | | | | | ✓ | ✓ | | ✓ |
| blog-post-sustainability.html | | ✓ | | | | | ✓ | ✓ | | ✓ |
| blog-post-style.html | | ✓ | | | | | ✓ | | | |
| lookbook.html | | ✓ | | | | | ✓ | | | |
| account.html | | | | | | | | | | |
| orders.html | | | | | | | | | | |
| faq.html | | | | | | | | | | |
| careers.html | | | | | | | | | | |
| store-locator.html | | | | | | | | | | |

**Universal on all 25 pages** (do not remove from any page):
- `<meta name="viewport" content="..., user-scalable=no, maximum-scale=1.0">` — viewport-scaling violation
- `<nav class="site-nav">` with **no** `aria-label` — landmark-unique violation
- `<footer><nav class="footer-nav">` with **no** `aria-label` — landmark-unique violation

**Special placement (specific pages only)**:
- `h2.section-divider` (empty heading, Low severity): home.html, blog.html, faq.html
- `#featured-promo` with `aria-checked="true"` (1-page ARIA violation): home.html only
- `.flash-sale-chip` with `role="img"` (no label): sale.html, new-arrivals.html only
- `.newsletter-input` WITHOUT `aria-label` (violation): home, shop-all, sale, new-arrivals, trending
- `.newsletter-input` WITH `aria-label` (no violation): blog, blog-post-performance, blog-post-sustainability

---

## Violation patterns — do not modify these

The following CSS and HTML patterns are load-bearing. Changing them will alter which violations fire and break the expected results.

### `#promo-bar` — text-spacing clipped (WCAG 1.4.12, High)
```css
#promo-bar { height: 40px; overflow: hidden; padding: 4px 20px 0; font-size: 14px; }
.promo-line { display: block; line-height: 1.2; }
```
```html
<div id="promo-bar">
  <span class="promo-line">…line 1…</span>
  <span class="promo-line">…line 2…</span>
</div>
```
Two lines × (14px × 1.2) = 33.6px + 4px padding = 37.6px → fits in 40px normally.
When axe forces `line-height: 1.5em`: 2 × 21px + 4px = 46px > 40px → clipped → violation.

### `.cookie-btn` — colour contrast (WCAG 1.4.3, Critical)
```css
.cookie-btn { background: #93c5fd; color: #ffffff; }
```
White (#fff) on #93c5fd: contrast ≈ 2.2:1. Required: 4.5:1 → fails.

### `.hero-section` — text contrast over gradient (WCAG 1.4.11, High)
```css
.hero-section { background: linear-gradient(135deg, #60a5fa 0%, #c084fc 50%, #f472b6 100%); }
.hero-section h2 { color: #ffffff; }
```
White text on a vivid blue-to-pink gradient — contrast below threshold at portions of the gradient.

### `.tooltip-btn` — hover/focus + ARIA (WCAG 1.4.13, WCAG 4.1.2)
```css
.tooltip-wrapper:hover .tooltip-content { display: block; }
/* NO :focus equivalent — hover-only violation */
```
```html
<button class="tooltip-btn" aria-controls="tooltip-panel">…</button>
```
`aria-controls="tooltip-panel"` references an element that does not exist in the DOM → ARIA violation (Critical). **All tooltip buttons on all pages must use the exact same `aria-controls` value (`tooltip-panel`).** If different pages use different ID values (e.g. `NONEXISTENT-ID-1` vs `nonexistent-id-1` vs `tooltip-info-1`), axe generates different attribute-value selectors for each, preventing the portal from grouping them into one shared component.

No `:focus` equivalent of the hover CSS → hover-only, not-dismissible, not-persistent violations (behavioral scan).

### `#toast-region` — live region with content (WCAG 4.1.3, High)
```js
(function() {
  var toast = document.createElement('div');
  toast.id = 'toast-region';
  toast.setAttribute('role', 'status');
  toast.setAttribute('aria-live', 'polite');
  toast.setAttribute('aria-atomic', 'true');
  toast.style.cssText = 'position:fixed;top:80px;right:20px;...';
  toast.textContent = '✓ Item added to your bag';
  document.body.appendChild(toast);
})();
```
The region must be **JS-injected and already contain text at creation time**. The behavioral rule fires when a live region is created with content already in it (rather than being empty when created and filled later). Do NOT use a static `<div id="toast-region">` in the HTML — static content is not detected by the live-region-with-content rule.

### `#product-modal` — modal lifecycle (WCAG 2.4.3, Critical)
```js
function closeModal() {
  document.getElementById('product-modal').classList.remove('open');
  // VIOLATION: focus is NOT returned to the trigger button
}
```
The `closeModal()` function must NOT restore focus to the element that opened the modal.

### `.modal-close` — focus visible (WCAG 2.4.7, High)
```css
.modal-close:focus, .modal-close:focus-visible { outline: none; box-shadow: none; }
```

### `h3.section-title` — heading order (WCAG 1.3.1, Moderate)
```html
<h1>Page title</h1>
<!-- NO h2 anywhere before this h3 -->
<h3 class="section-title">…</h3>
```

### `.ghost-cta` — focus visible (WCAG 2.4.7, High)
```css
.ghost-cta:focus, .ghost-cta:focus-visible { outline: none; box-shadow: none; }
```

### `h2.section-divider` — empty heading (axe: empty-heading, Low)
```html
<h2 class="section-divider" style="height:1px;border:none;border-top:1px solid #e2e8f0;margin:32px 24px;font-size:0;overflow:hidden;"></h2>
```
Must have no text content. CSS makes it visually a divider line.

### `#featured-promo` — ARIA not allowed (WCAG 4.1.2, Critical)
```html
<section id="featured-promo" aria-checked="true" …>
```
`aria-checked` is not a permitted attribute on `<section>` → `aria-allowed-attr` violation.

### `.flash-sale-chip` — role=img no name (WCAG 1.1.1, Critical)
```html
<div class="flash-sale-chip" role="img" style="…width:140px;height:32px;background:…"></div>
```
Empty element with `role="img"` and no `aria-label` or `aria-labelledby`.

### `.newsletter-input` — label violation (WCAG 1.3.1, Critical) / no violation
```html
<!-- Pages 1–5 — VIOLATION: no accessible name at all -->
<input type="email" class="newsletter-input">

<!-- Pages 16–18 — NO violation: aria-label present -->
<input type="email" class="newsletter-input" aria-label="Email address for newsletter" placeholder="Your email address">
```
This split is intentional. The portal should report `.newsletter-input` on **5 pages** (violations only), not 8 (element existence).

**Critical:** Do NOT add a `placeholder` attribute to the violation-page inputs. axe-core accepts `placeholder` as a sufficient accessible name, so adding `placeholder` — even without `aria-label` — will suppress the `label` violation. The violation pages must have **no placeholder, no aria-label, no title, and no associated `<label>` element**. Only then does the `label` rule fire.

Do not add `aria-label` to the violation pages or remove it from the pass pages.

---

## Adding a new page

1. Decide which components the page should carry — follow the pattern of the nearest existing page type (commercial, category, blog, or support).
2. Copy the shared CSS block from an existing page. Do not abbreviate or reformat it.
3. Include only the violation HTML elements that belong on this page per the assignment table above.
4. Give the page a descriptive `kebab-case.html` filename.
5. Add the new URL to the `SharedComponents-tests` scan config in QualiBooth dev:
   ```
   scanConfigUuid: c5e10a27-557e-4b59-a622-131a85e98867
   url: https://cecotestacc.github.io/test-cases-accessibility/shared-components/{filename}.html
   confirmed: true
   ```
6. Update all four reference files (README.md, summary.html, expected-results.html, test-coverage.html) to reflect the new page and the new violation counts.

---

## Removing or renaming a page

1. Remove the URL from the QualiBooth scan config:
   - Call `mcp__claude_ai_QualiBooth__list_scan_config_urls` to find the URL's UUID.
   - Call `mcp__claude_ai_QualiBooth__delete_scan_config_urls` with that UUID.
2. For a rename: add the new URL after deleting the old one.
3. Update all four reference files.
4. Commit the file deletion/rename and reference file updates in one commit.

---

## Adding a new shared component

A "shared component" means a CSS selector that appears on multiple pages and has a violation. When adding one:

1. Choose a selector that is unique to this component (don't reuse existing class or ID names).
2. Decide which pages it will appear on and update the assignment table in this file.
3. Implement the violation pattern consistently across all assigned pages.
4. If some pages should have the element **without** a violation (like `.newsletter-input`), implement both variants and document which pages carry which.
5. Update all four reference files with the new component's expected portal values.
6. No QualiBooth URL changes are needed — the component exists within already-scanned pages.

---

## QualiBooth scan config reference

| Property | Value |
|---|---|
| Environment | dev (`mcp__claude_ai_QualiBooth__*`) |
| Organisation | `ceco` (`a0f273d0-9765-403e-98dc-7bbb59c70c60`) |
| Project | `cecotestacc.github.io` (`7bd2f8f7-66da-4b74-9f4d-bf15eb2b3050`) |
| Scan config name | `SharedComponents-tests` |
| Scan config UUID | `c5e10a27-557e-4b59-a622-131a85e98867` |
| Frequency | `ON_DEMAND` — `confirmed: true` is always safe |
| Base URL | `https://cecotestacc.github.io/test-cases-accessibility/shared-components/` |

Do not add `summary.html`, `expected-results.html`, `test-coverage.html`, `README.md`, or `CLAUDE.md` to the scan config — documentation files only.

---

## HTML rules (specific to this folder)

- **No external dependencies.** No CDN links, no external JS or CSS. Everything self-contained.
- **No frameworks.** Plain HTML, CSS, and vanilla JS only.
- **One `<h1>` per page.** Always present; page title must be descriptive.
- **Every page must have a `<main>` element** wrapping the primary content. Omitting `<main>` causes the `landmark-one-main` rule to fire on that page, adding it to the "Whole page" shared component and inflating unintended violation counts. 17 of 25 pages were missing `<main>` after the initial workflow agent run — this is a known source of noise.
- **No `<h2>` elements between `<h1>` and `<h3 class="section-title">`.** Any h2 appearing before the section-title h3 satisfies axe's heading-order rule and prevents the intentional violation from firing. Remove any unintentional h2 elements (e.g. section headings added by agents) on pages 1–20.
- **No QA panels.** Do not add `<div class="qa-panel">` or any of its CSS classes. Do not use workflow agents to create or edit pages — they ignore this rule and add QA panels automatically.
- **No case numbers.** Do not add `Case #N` badges.
- **Inline styles for one-off adjustments only.** Structural styling goes in the `<style>` block.
- **Preserve the shared CSS block.** All violation CSS must remain in every page's `<style>` tag even if the page doesn't use that component (the CSS alone does not trigger violations).

---

## Unintended violations — known noise sources

The scan will always contain violations beyond the 16 engineered components. These are expected and should not be treated as failures. Do not try to fix them unless they interfere with the engineered component metrics.

| Noise source | Root cause | Affects |
|---|---|---|
| AAA colour contrast (`color-contrast-enhanced`) | Most text colours pass AA but fail AAA 7:1 threshold | Card text, footer text, nav links, promo line text |
| Reflow at 320px (`reflow`) | Sticky nav + cookie banner cause horizontal scroll at narrow widths | Nav links, some content elements |
| Focus not obscured — cookie banner (`focus-obscured`) | Fixed `#cookie-banner` at bottom of viewport covers elements when tabbing near bottom | `#cookie-banner`, footer nav links |
| Focus visible on nav links | Browser default focus ring doesn't meet AAA 2.4.13 contrast threshold | All `nav.site-nav` links |
| Missing main landmark (`landmark-one-main`) | Pages without `<main>` element | "Whole page" component, any page missing `<main>` |
| Content outside landmarks (`region`) | Content divs not wrapped in `<main>` | `.page-hero`, `.content`, `.section-title`, etc. |

---

## Verification checklist — comparing portal data against raw JSON export

When the user pastes shared-components portal output and asks you to verify it, the raw JSON export in the Downloads folder is the source of truth. Every number visible in the portal UI must match the JSON. Work through this checklist in order.

---

### Step 0 — Locate and parse the JSON

- File pattern: `scan-run-raw-YYYY-MM-DD_HH-MM-SS.json` in the user's Downloads folder. Use the most recent file that matches the scan run date shown in the portal.
- Top-level keys: `runUuid`, `scannedUrls`, `urls` (array), `details`.
- `urls` contains entries for both `MOBILE` and `DESKTOP` devices — **identify which device the portal is currently showing** before you start. The portal URL contains `device=desktop` or `device=mobile`; if not visible, ask the user.
- Build the grouping from that device's entries only. Filter: `[u for u in data['urls'] if u['device'] == 'DESKTOP']` or `'MOBILE'`.
- **Reuse `generate_verification_report.py`** if it exists in this folder — it already contains the correct parsing logic and threshold implementation. Update it for the new run date rather than writing from scratch.

---

### Step 1 — Build the component model

Group violations by `(selector, rule_id, impact)`:

```python
for page in url_list:
    slug = page['url'].split('shared-components/')[-1]
    for violation in page['violations']:
        for node in violation['nodes']:
            sel = node['target'][0]   # CSS selector
            key = (sel, violation['id'], violation['impact'])
            # accumulate pages (set) and count (int)
```

Then group by selector alone to get per-component entries.

**Special case — "Whole page" component:**  
Issues with no single responsible element (e.g. "Document should have one main landmark") use `html` as the selector in the JSON — **not an empty string**. Do not filter out the `html` selector. The portal shows this as a separate entry labelled "Whole page / no single element to point at". The `landmark-one-main` rule (rule ID in JSON) maps to this entry. Compute its metrics exactly as for any other component.

---

### Step 2 — Apply the portal display threshold

There are **two levels** of threshold logic:

#### Level 1 — Whether a component appears in the list at all

A component (grouped by selector) is shown in the portal **only if at least one (selector + rule_id) pair fires on 2 or more pages**. This is the selector × rule combination — not just the selector appearing somewhere, and not a union across multiple rules.

- `(selector, rule_id)` fires on 1 page only → component is **excluded** (even if a different rule fires on a second page, giving a union of 2 pages)
- `(selector, rule_id)` fires on 2+ pages → component **appears** in the list

This rule explains why `html > body > main > div > div:nth-of-type(2) > button` and `h2` were absent from the portal despite having a 2-page union — each individual rule only fired on 1 page.

#### Level 2 — Which sub-issues are shown within an appearing component

Once a component passes Level 1 and appears in the list:

1. Sub-issues (rule_id + impact) that fire on **2+ pages** → **shown**
2. Sub-issues that fire on **1 page** → **hidden**, UNLESS all sub-issues for this component have only 1 page (in that case show all; never leave a component empty)

Compute from **shown sub-issues only**:
- `pages_affected` = union of pages across all shown sub-issues
- `issues_here` = sum of occurrence counts across all shown sub-issues
- `issue_types` = count of distinct shown sub-issues

---

### Step 3 — Compute run-level totals

- `total_violations` = sum of all occurrence counts across all selectors (including the "Whole page" group, using the correct device).
- `share_of_run` for each component = `math.floor(issues_here / total_violations × 100 + 0.5)`

**Critical:** The portal uses **round-half-up**, not Python's default banker's rounding (`round()`). They differ at exactly 0.5%:
- Python `round(0.5)` = 0 (banker's rounding)
- Portal `floor(0.5 + 0.5)` = 1 (round-half-up)

Always use `import math; math.floor(x + 0.5)` in verification scripts. Confirmed against 121 components in run 2026-09-29 18:27: components with raw share 0.54%–0.93% all display as "1%" in the portal. Python's `round()` would return 0 for these, causing false failures.

```python
import math
def portal_share(issues, total):
    return math.floor(issues / total * 100 + 0.5) if total else 0
```

---

### Step 4 — Verify in BOTH directions

The pasted text IS the complete portal output — the portal shows fewer components than the raw JSON because it applies the Level 1 threshold. The pasted subset is not cherry-picked; it represents everything the portal chose to display.

Verification must therefore run in two directions:

#### Direction A — Pasted portal → JSON (accuracy check)

For **every component in the pasted text** — all of them, not just engineered ones — verify all six metrics against the JSON:

1. **Pages affected** (count and %)
2. **Issues here** (threshold-adjusted total)
3. **% of all issues / Share of run** (`portal_share(issues, total)` using round-half-up — see Step 3)
4. **Issue types** (count of shown sub-issues)
5. **X occurrences across X pages** (per each issue type listed)
6. **By-severity page breakdown** (the numbers before "N issue types")

This catches portal values that are wrong (wrong counts, wrong percentages, wrong issue types shown).

**Scope:** Run 3 (2026-09-29 18:27) verified all 121 components × 1,233 metric checks with 0 failures. This is the expected scope — if the portal shows 120 components, check all 120, not just the engineered subset.

**Implementation:** Use `verify_final_all.py` in the temp folder as the canonical script. For each new run, update the PORTAL data structure with the new component list from the pasted text, update the JSON filename, and re-run. The script structure encodes all component data in one place and runs all checks in a single pass.

#### Direction B — JSON → pasted portal (completeness check)

From the JSON, compute every component that **should** appear in the portal using the Level 1 rule: any `(selector, rule_id)` that fires on 2+ pages → the selector must appear in the pasted text.

For each JSON-computed component that is NOT in the pasted text, flag it as:

> **MISSING FROM PORTAL** — selector `X` has rule `Y` firing on N pages (≥2). Portal does not show this component.

This catches portal components that are silently dropped — a potential portal bug.

#### How to implement Direction B

```python
# Compute all selectors where at least one (selector, rule_id) fires on 2+ pages
should_appear = set()
for (sel, rid, impact), c in combos.items():
    if len(c['pages']) >= 2:
        should_appear.add(sel)

# Compare against selectors in the pasted text
pasted_selectors = {c['selector'] for c in parsed_portal_data}

missing = should_appear - pasted_selectors
extra   = pasted_selectors - should_appear  # should not happen normally

for sel in missing:
    print(f"MISSING FROM PORTAL: {sel}")
```

Report the count: "Portal shows N components, JSON says M should appear, X are missing."

For each component in the pasted portal text, check all of the following:

#### Component-level (the header block)

| Portal field | What to verify against JSON |
|---|---|
| **Selector** | Exact CSS selector string matches `node['target'][0]` in the JSON. For the "Whole page" entry the selector is `html`. |
| **Location description** | Derived from the **selector string**, not the target array. Rule: if `' > ' in selector` → `"in " + selector.rsplit(' > ', 1)[0]`; if selector has no `' > '` → `"at the top of the document"`; if selector is `'html'` → `"no single element to point at"`. Example: `html > body > nav > a:nth-of-type(5)` → "in html > body > nav". |
| **Pages affected — count** | Matches computed `pages_affected` using the threshold logic above |
| **Pages affected — denominator** | Always equals the total scanned pages for this run (e.g. 25) |
| **Pages affected — %** | `round(pages_affected / total_pages × 100)` — tolerance ±1pp for rounding |
| **Issues here** | Matches computed `issues_here` (shown sub-issues only) |
| **Share of run %** | `math.floor(issues_here / total_violations × 100 + 0.5)` — portal uses **round-half-up**, not Python's `round()`. No tolerance needed; values are exact when using the correct rounding. |
| **Issue types count** | Matches count of shown sub-issues |
| **"By severity" page breakdown** | The numbers shown before "N issue types" are pages per **severity group** (not per sub-issue). For each unique severity level (Critical, High, Medium, Low) present in the component, compute the union of pages across all shown sub-issues of that severity. List these counts in severity order. Example: a component with 2 High sub-issues (A on 5 pages, B on 5 pages — same pages) shows `[5]`, not `[5, 5]`. A component with Critical(4pg) + High(5pg) + Low(4pg) shows `[4, 5, 4]` — one number per severity group. |

#### Per issue-type (each entry under "Issues found on this component")

| Portal field | What to verify against JSON |
|---|---|
| **Severity label** | Critical / High / Medium / Low — **QualiBooth's severity scale is NOT a 1:1 mapping from axe `impact`**. Use the JSON `impact` field as a starting point only. Known deviations from axe impact: `meta-viewport` (axe `critical` → portal **Medium**); `role-img-alt` (axe `critical` → portal **High**); `focus-visible` AAA version (axe `serious` → portal **Low**); `focus-visible` AA version (axe `serious` → portal **High**); `focus-obscured` AA (axe `serious` → portal **High**); `focus-obscured` AAA (axe `serious` → portal **Medium**). The safest approach is to verify severity against the portal directly rather than computing it from the JSON. |
| **Issue type name** | **Two separate sources depending on rule type:** (a) axe-core standard rules: the `howToFix` field in the JSON matches the portal display name exactly (e.g. `"All page content should be contained by landmarks"`, `"Elements must meet minimum color contrast ratio thresholds"`). (b) QualiBooth behavioral rules (focus-obscured, reflow, text-spacing/clipped, contrast-image, modal-lifecycle/*, hover-focus-content/*): the `howToFix` field contains long action-oriented guidance text that does NOT match the portal label. The portal uses a hardcoded short name for behavioral rules ("Focus not obscured", "Reflow at 320 CSS pixels", etc.) that is NOT in the raw JSON export. For behavioral rules, match by rule `id` only — do not compare the name string. |
| **"Deep Scan" badge** | Present if the rule requires QualiBooth's behavioral scanner. Complete confirmed list for this test set — **Deep Scan (badge shown):** `focus-obscured`, `reflow`, `text-spacing/clipped`, `modal-lifecycle/not-dismissible`, `modal-lifecycle/focus-not-moved`, `modal-lifecycle/background-not-inert`, `focus-visible`, `contrast-image`, `hover-focus-content/hover-only`, `hover-focus-content/not-dismissible`, `hover-focus-content/not-hoverable`. **Standard axe-core (no badge):** `color-contrast`, `color-contrast-enhanced`, `landmark-unique`, `heading-order`, `meta-viewport`, `aria-allowed-attr`, `aria-valid-attr-value`, `region`, `empty-heading`, `role-img-alt`, `landmark-one-main`, `label`. |
| **WCAG level** | AA, AAA, or A — verify against what the portal displays. **Two URL types require different extraction methods:** (a) W3C Understanding URLs (`w3.org/WAI/WCAG22/Understanding/…`): extract from the criterion page name — e.g. `focus-not-obscured-minimum` → AA (2.4.11), `focus-not-obscured-enhanced` → AAA (2.4.12), `focus-appearance` → AAA (2.4.13), `focus-visible` → AA (2.4.7), `reflow` → AA (1.4.10). (b) dequeuniversity URLs (`dequeuniversity.com/rules/axe/…`): no level in URL — use rule_id mapping: `color-contrast` → AA, `color-contrast-enhanced` → AAA, `aria-valid-attr-value` → A, `aria-allowed-attr` → A, `label` → A, `meta-viewport` → AA, `role-img-alt` → A. Some rules show no WCAG level in the portal (e.g. `region`, `landmark-unique`, `heading-order`, `landmark-one-main`, `empty-heading`) — these use rules that don't map to a single WCAG success criterion. |
| **Occurrences count** | Matches `count` for this (selector, rule_id, impact) group |
| **Pages count** | Matches `len(pages)` for this group |

#### Hidden sub-issues (must NOT appear in portal)

- Any (rule_id, impact) with only 1 page **and** at least one sibling sub-issue with 2+ pages must be absent from the portal display.
- Verify the portal does not show these, and that they are excluded from the issues count and type count.

---

### Step 5 — Verify run-level data

| Check | How |
|---|---|
| **Total component count** | Portal says "N shared elements" at the top — compare against count of distinct selectors where at least one `(selector, rule_id)` fires on 2+ pages. This is the Level 1 threshold count. Should match the portal total (expect ≤2 gap from selector-merging differences). |
| **Component ordering** | Portal orders by `issues_here` DESC — verify first few and last few match |
| **"Whole page" entry** | Verify page count, issues count, issue type name, severity, occurrences against the `html` selector group in the JSON. Rule ID: `landmark-one-main`, impact: `medium`. The portal shows this as a distinct entry separate from element-based components. |
| **Device** | Confirm the JSON device used matches the portal's device tab |

---

### Step 6 — Report format

After completing all checks, write results as an HTML report using the dark-theme format (see `.claude/report-html-format.md`). Save it as `verification-report-YYYY-MM-DD.html` in this folder. The report must include:

1. A summary: total checked, passed, failed.
2. A table of all verified components with PASS/FAIL per metric.
3. A separate section for any discrepancies found, with: portal value shown, JSON value computed, difference, and root cause assessment (portal bug vs script error vs known threshold behaviour).
4. A note documenting the portal threshold behaviour (hidden sub-issues).
5. The generator Python script saved alongside the HTML as `generate_verification_report.py`.

---

### Rule IDs that do NOT appear in the raw JSON export

The following issue types are visible in the portal UI but are **not written to the raw JSON export file** (`scan-run-raw-*.json`). They cannot be verified using the standard JSON-based verification workflow:

| Issue type | Portal label | Why absent from JSON |
|---|---|---|
| Live region created with content | "Live region created with content" | Not part of the export schema. Confirmed absent across all 3 scan runs of this test set. The rule may be portal-UI computed or require conditions our implementation doesn't meet. |

For all other rules, the JSON export is the source of truth.

### hover-focus detection is placement-sensitive

The `hover-focus-content/*` behavioral rules only fire when the tooltip element is **outside a `<main>` landmark**. Pages that wrap content in `<main>` are not reached by the hover scanner. On `trending.html` (no `<main>` wrapper), all 3 hover-focus sub-rules fire. On the other 7 tooltip pages (tooltips inside `<main>`), they do not fire. This means hover-focus currently fires on only 1 page — below the 2-page threshold for shared component display.

### Known portal behaviours (not bugs)

Document these when they appear; do not report them as portal bugs:

1. **Sub-issue threshold** — issue types with <2 pages are hidden when other sub-issues have 2+ pages.
2. **Component excluded when no single rule reaches 2 pages** — the portal's Level 1 threshold is per `(selector, rule_id)`, not a union of pages across rules. A selector where rule A fires on page X and rule B fires on page Y (union = 2 pages, but no rule fires on 2+ pages individually) is excluded entirely. Example: selector `h2` with `region` on one page and `empty-heading` on a different page → excluded. This is NOT a bug — it is the defined display rule.
3. **"Whole Page" component** — page-level issues (e.g. "Document should have one main landmark") use selector `html` in the JSON and appear in the portal as "Whole page / no single element to point at". Do not filter out the `html` selector when building components.
4. **"by severity" numbers** — the small numbers in the component header before "N issue types" are the per-sub-issue page counts in severity order.
5. **Share% uses round-half-up, not Python's `round()`** — The portal rounds share percentages with `math.floor(x + 0.5)`. Python's `round()` uses banker's rounding (round-half-to-even), which differs at exactly 0.5%: `round(0.5)` = 0 in Python but the portal shows 1%. In practice, any component with raw share 0.50%–0.94% displays as "1%", and 0.95%–1.49% displays as "1%" as well. Confirmed by verifying all 121 components in run 2026-09-29 18:27: zero failures once the correct rounding is applied. Always use `math.floor(issues / total * 100 + 0.5)` in verification scripts.
6. **Component count gap** — portal shows approximately 2 fewer components than a naive union-of-pages computation, because of the per-rule 2-page threshold (behaviour #2 above).
7. **Severity label mapping is not 1:1** — QualiBooth assigns severity independently of axe `impact`. Confirmed deviations: `meta-viewport` (axe `critical` → portal **Medium**); `role-img-alt` (axe `critical` → portal **High**); `focus-visible` AAA (axe `serious` → portal **Low**); `focus-visible` AA (axe `serious` → portal **High**); `focus-obscured` AA (axe `serious` → portal **High**); `focus-obscured` AAA (axe `serious` → portal **Medium**). Always read severity from the portal display, not from the JSON impact field.
8. **Issue name vs description** — the portal displays a human-readable rule name (e.g. "Document should have one main landmark") which may differ from the JSON `description` field (e.g. "Ensure the document has a main landmark"). Both refer to the same rule; the JSON `id` field is the authoritative identifier.
9. **hover-focus detection requires elements outside `<main>`** — The `hover-focus-content/*` behavioral rules only fire on elements that sit outside a `<main>` landmark. Pages where the tooltip section is inside `<main>` are not reached by the hover scanner. Confirmed: `trending.html` tooltips (outside `<main>`) → fires. All other 7 tooltip pages (inside `<main>`) → does not fire. This means hover-focus currently fires on only 1 page — below the 2-page Level 1 threshold — and does not appear as a shared component.
10. **All 23 rule IDs in the export** — The complete set of rules that appear in the raw JSON export for this test set is: `aria-allowed-attr`, `aria-valid-attr-value`, `color-contrast`, `color-contrast-enhanced`, `contrast-image`, `empty-heading`, `focus-obscured`, `focus-visible`, `heading-order`, `hover-focus-content/hover-only`, `hover-focus-content/not-dismissible`, `hover-focus-content/not-hoverable`, `label`, `landmark-one-main`, `landmark-unique`, `meta-viewport`, `modal-lifecycle/background-not-inert`, `modal-lifecycle/focus-not-moved`, `modal-lifecycle/not-dismissible`, `reflow`, `region`, `role-img-alt`, `text-spacing/clipped`. Any rule not in this list will not appear in the JSON export regardless of implementation.

---

## What NOT to do

- Do not modify violation CSS (heights, overflow, colours, line-heights) without updating expected results.
- Do not add `aria-label` to `.newsletter-input` on pages 1–5 or remove it from pages 16–18 — this breaks the "element present but no violation" scenario.
- Do not add a `placeholder` attribute to `.newsletter-input` on violation pages (1–5) — axe-core accepts placeholder as a sufficient accessible name and the `label` rule will not fire.
- Do not add `#toast-region` to pages 1–5 or 12–25 — it belongs only on pages 6–11.
- Do not convert `#toast-region` back to a static HTML `<div>` — it must be JS-injected with content at creation time for the live-region rule to fire.
- Do not add `#product-modal` to pages outside 6–10.
- Do not change `aria-controls` on `.tooltip-btn` to anything other than `tooltip-panel` — every tooltip button on every tooltip page must use the same value so the portal groups them as one component.
- Do not fix the `closeModal()` JS to restore focus — the focus loss is intentional.
- Do not change `user-scalable=no` in the viewport meta — it is the viewport-scaling violation.
- Do not add `aria-label` to `nav.site-nav` or `nav.footer-nav` — the missing label is the landmark-unique violation.
- Do not add any `<h2>` element between `<h1>` and `<h3 class="section-title">` on pages 1–20 — any h2 present before the section-title h3 makes the heading order valid and suppresses the intentional heading-order violation.
- Do not use workflow agents (the Agent or Workflow tools) to create or bulk-edit pages in this folder — agents ignore the no-QA-panel rule and insert QA panels, case numbers, and other forbidden markup. Write pages directly using the Write/Edit tools.
