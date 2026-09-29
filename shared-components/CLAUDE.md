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

After any change that affects component distribution, violation counts, or page inventory, update all four of these files in the same commit:

| File | What to update |
|---|---|
| `README.md` | Page inventory table, component overview table, quick stats |
| `summary.html` | Component architecture table, page inventory table, issue type list |
| `expected-results.html` | Component cards (pages, %, issues, share), per-page table, acceptance criteria |
| `test-coverage.html` | Component inventory table, page count range table, severity coverage, scan depth matrix |

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
<button class="tooltip-btn" aria-controls="nonexistent-id-X">…</button>
```
`aria-controls` referencing a non-existent element ID → ARIA violation (Critical).
No `:focus` equivalent of the hover CSS → hover-only, not-dismissible, not-persistent violations (behavioral scan).

### `#toast-region` — live region with content (WCAG 4.1.3, High)
```html
<div id="toast-region" role="status" aria-live="polite" aria-atomic="true">
  Message already present on load
</div>
```
Content must be in the DOM at page load — do not make it dynamically injected.

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
<!-- Pages 1–5 — VIOLATION: no label -->
<input type="email" class="newsletter-input" placeholder="…">

<!-- Pages 16–18 — NO violation: aria-label present -->
<input type="email" class="newsletter-input" aria-label="Email address for newsletter" placeholder="…">
```
This split is intentional. The portal should report `.newsletter-input` on **5 pages** (violations only), not 8 (element existence). Do not add `aria-label` to the violation pages or remove it from the pass pages.

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
- **No QA panels.** Do not add `<div class="qa-panel">` or any of its CSS classes.
- **No case numbers.** Do not add `Case #N` badges.
- **Inline styles for one-off adjustments only.** Structural styling goes in the `<style>` block.
- **Preserve the shared CSS block.** All violation CSS must remain in every page's `<style>` tag even if the page doesn't use that component (the CSS alone does not trigger violations).

---

## Verification checklist — comparing portal data against raw JSON export

When the user pastes shared-components portal output and asks you to verify it, the raw JSON export in the Downloads folder is the source of truth. Every number visible in the portal UI must match the JSON. Work through this checklist in order.

---

### Step 0 — Locate and parse the JSON

- File pattern: `scan-run-raw-YYYY-MM-DD_HH-MM-SS.json` in the user's Downloads folder.
- Top-level keys: `runUuid`, `scannedUrls`, `urls` (array), `details`.
- `urls` contains entries for both `MOBILE` and `DESKTOP` devices — **identify which device the portal is currently showing** before you start (the portal URL includes `device=desktop` or `device=mobile`).
- Build the grouping from that device's entries only.

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
Issues with no specific element (e.g. "Document should have one main landmark") produce an **empty or null selector**. Do not filter these out. Collect them under the label `"Whole page"`. The portal shows them as a separate entry with the label "no single element to point at".

---

### Step 2 — Apply the portal display threshold

The threshold is applied per **(selector + rule_id)** pair, not on the union across all rules for a selector.

For each component (grouped by selector):

1. Identify sub-issues (rule_id + impact pairs) that appear on **2+ pages** → these are **shown**.
2. Sub-issues that appear on only **1 page** → **hidden**, UNLESS all sub-issues for this component have only 1 page (in that case show all; a component is never left empty).
3. **Component-level exclusion**: if NO sub-issue for a selector fires on 2+ pages, AND all sub-issues fire on different single pages (union gives 2+ pages but no individual rule reaches 2), the component is **excluded from the list entirely**. This is different from case 2: case 2 is "every rule fires on the same 1 page"; this case is "each rule fires on a different 1 page, union is 2+ but per-rule it is always 1".
4. Compute from **shown sub-issues only**:
   - `pages_affected` = union of pages across all shown sub-issues
   - `issues_here` = sum of occurrence counts across all shown sub-issues
   - `issue_types` = count of distinct shown sub-issues

---

### Step 3 — Compute run-level totals

- `total_violations` = sum of all occurrence counts across all selectors (including the "Whole page" group, using the correct device).
- `share_of_run` for each component = `issues_here / total_violations × 100`, rounded to nearest integer.

---

### Step 4 — Verify every metric for every component

For each component in the pasted portal text, check all of the following:

#### Component-level (the header block)

| Portal field | What to verify against JSON |
|---|---|
| **Selector** | Exact CSS selector string matches the `target[0]` value in the JSON nodes |
| **Location description** | "at the top of the document" vs "in [parent selector]" — derived from `target` array; if `target` has >1 element the last item is the parent context |
| **Pages affected — count** | Matches computed `pages_affected` using the threshold logic above |
| **Pages affected — denominator** | Always equals the total scanned pages for this run (e.g. 25) |
| **Pages affected — %** | `round(pages_affected / total_pages × 100)` — tolerance ±1pp for rounding |
| **Issues here** | Matches computed `issues_here` (shown sub-issues only) |
| **Share of run %** | `round(issues_here / total_violations × 100)` — tolerance ±1pp |
| **Issue types count** | Matches count of shown sub-issues |
| **"By severity" page breakdown** | The numbers shown before "N issue types" are the page counts per shown sub-issue, ordered critical → high → medium → low |

#### Per issue-type (each entry under "Issues found on this component")

| Portal field | What to verify against JSON |
|---|---|
| **Severity label** | Critical / High / Medium / Low — maps from axe `impact`: `critical`→Critical, `serious`→High, `moderate`→Medium, `minor`→Low |
| **Issue type name** | Human-readable description from `violation.description` in the JSON |
| **"Deep Scan" badge** | Present if the rule is a QualiBooth behavioral check (not a standard axe-core rule). Known behavioral rules: `focus-obscured`, `reflow`, `text-spacing/clipped`, `modal-lifecycle/*`, `focus-visible` (Deep Scan version), `role-img-alt` (when behavioral). Absent for standard axe rules: `color-contrast`, `landmark-unique`, `heading-order`, `meta-viewport`, `aria-*`, `region`, `empty-heading`. |
| **WCAG level** | AA, AAA, or A — derived from the `helpUrl` or rule metadata. Verify it matches what the portal displays. |
| **Occurrences count** | Matches `count` for this (selector, rule_id, impact) group |
| **Pages count** | Matches `len(pages)` for this group |

#### Hidden sub-issues (must NOT appear in portal)

- Any (rule_id, impact) with only 1 page **and** at least one sibling sub-issue with 2+ pages must be absent from the portal display.
- Verify the portal does not show these, and that they are excluded from the issues count and type count.

---

### Step 5 — Verify run-level data

| Check | How |
|---|---|
| **Total component count** | Portal says "N shared elements" at the top — compare against count of selectors with `pages_affected >= 2` (using threshold logic) plus any 1-page components where all sub-issues have <2 pages |
| **Component ordering** | Portal orders by `issues_here` DESC — verify first few and last few match |
| **"Whole page" entry** | Verify page count, issues count, issue type name, severity, occurrences against the empty-selector group in the JSON |
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

### Known portal behaviours (not bugs)

Document these when they appear; do not report them as portal bugs:

1. **Sub-issue threshold** — issue types with <2 pages are hidden when other sub-issues have 2+ pages.
2. **Component excluded when no rule reaches 2 pages** — if a selector has multiple rules each firing on a different single page (union = 2+ pages, but no individual rule hits 2), the component is excluded from the list entirely. Example: selector `h2` with `region` on page A and `empty-heading` on page B → excluded.
3. **"Whole Page" component** — page-level issues (e.g. "Document should have one main landmark") use selector `html` in the JSON and appear in the portal as "Whole page / no single element to point at". Do not filter out the `html` selector when building components.
4. **"by severity" numbers** — the small numbers in the component header before "N issue types" are the per-sub-issue page counts in severity order.
5. **Share rounding** — portal rounds share% to the nearest integer; differences of ±1pp are expected.
6. **Component count gap** — portal shows approximately 2 fewer components than a naive union-of-pages computation, because of the per-rule 2-page threshold (behaviour #2 above).
7. **Severity label mapping** — axe `serious` maps to portal `High`; axe `moderate` maps to portal `Medium`. Never use axe impact names in the report — always convert.
8. **Issue name vs description** — the portal displays a human-readable rule name (e.g. "Document should have one main landmark") which may differ from the JSON `description` field (e.g. "Ensure the document has a main landmark"). Both refer to the same rule; the JSON `id` field is the authoritative identifier.

---

## What NOT to do

- Do not modify violation CSS (heights, overflow, colours, line-heights) without updating expected results.
- Do not add `aria-label` to `.newsletter-input` on pages 1–5 or remove it from pages 16–18 — this breaks the "element present but no violation" scenario.
- Do not add `#toast-region` to pages 1–5 or 12–25 — it belongs only on pages 6–11.
- Do not add `#product-modal` to pages outside 6–10.
- Do not remove the `aria-controls="nonexistent-id-X"` attributes from `.tooltip-btn` — they are the ARIA violation mechanism.
- Do not fix the `closeModal()` JS to restore focus — the focus loss is intentional.
- Do not change `user-scalable=no` in the viewport meta — it is the viewport-scaling violation.
- Do not add `aria-label` to `nav.site-nav` or `nav.footer-nav` — the missing label is the landmark-unique violation.
