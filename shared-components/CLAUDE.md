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

## What NOT to do

- Do not modify violation CSS (heights, overflow, colours, line-heights) without updating expected results.
- Do not add `aria-label` to `.newsletter-input` on pages 1–5 or remove it from pages 16–18 — this breaks the "element present but no violation" scenario.
- Do not add `#toast-region` to pages 1–5 or 12–25 — it belongs only on pages 6–11.
- Do not add `#product-modal` to pages outside 6–10.
- Do not remove the `aria-controls="nonexistent-id-X"` attributes from `.tooltip-btn` — they are the ARIA violation mechanism.
- Do not fix the `closeModal()` JS to restore focus — the focus loss is intentional.
- Do not change `user-scalable=no` in the viewport meta — it is the viewport-scaling violation.
- Do not add `aria-label` to `nav.site-nav` or `nav.footer-nav` — the missing label is the landmark-unique violation.
