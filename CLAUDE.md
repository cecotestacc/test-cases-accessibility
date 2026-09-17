# Test Case Authoring Rules

This file is read automatically by Claude Code when working in this repo.
Follow every rule here when creating or editing test cases.

---

## Repo layout

```
behaviour-feature/
  {rule-id}/
    {descriptive-name}.html       ← one file per scenario; name = what it tests
    CustomHTMLElements.html       ← custom-element variant (one per rule)
Custom-HTML-Elements/             ← standalone custom-element demos
ScreenReader/                     ← screen-reader focused cases
```

---

## Filename rules

- **One concept per file.** Each file covers exactly one scenario (one failure mode, one pass, or one false positive).
- **Filename = the test case subject.** Use `kebab-case.html`. The name must describe the specific scenario so that reading the filename alone tells you what is being tested — e.g. `popup-over-page.html`, `sticky-header-obscures-link.html`, `missing-label-on-search-input.html`.
  - `CustomHTMLElements.html` — reserved for the custom-element variant of the same rule (one per rule folder).
- **No generic names.** Do not use names like `test1.html`, `case-a.html`, `standard-elements.html`, or any `StandardHTMLElements-*.html` pattern.

---

## Case number

- Every case carries a sequential integer badge: `Case #02`, `Case #03`, …
- **Check the highest case number already used across the entire `behaviour-feature/` tree** and increment by 1. Case numbers are globally unique across all rule folders.
- Case #01 is reserved (do not use).

---

## File template

Every test file must follow this structure exactly — no exceptions:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{rule-id} – {short description} ({W3C ref if applicable})</title>
  <style>
    /* page-specific styles first */

    /* ── QA Info Panel ── (copy verbatim, do not modify) */
    .qa-panel { font-family: system-ui,-apple-system,sans-serif; background: #0f172a; color: #e2e8f0; border-left: 4px solid #818cf8; padding: 16px 20px; margin: 0 0 24px; font-size: 0.875rem; line-height: 1.6; }
    .qa-panel-header { display: flex; align-items: center; gap: 10px; margin-bottom: 12px; flex-wrap: wrap; }
    .qa-case-num { background: #818cf8; color: #0f172a; font-weight: 700; padding: 2px 10px; border-radius: 20px; font-size: 0.75rem; white-space: nowrap; }
    .qa-rule-id { font-weight: 700; font-size: 1rem; color: #a5b4fc; font-family: monospace; }
    .qa-panel dl { margin: 0; display: grid; grid-template-columns: max-content minmax(0,1fr); gap: 6px 16px; align-items: start; }
    .qa-panel dd, .qa-panel a { overflow-wrap: break-word; min-width: 0; }
    .qa-panel dt { font-weight: 600; color: #7dd3fc; white-space: nowrap; }
    .qa-panel dd { margin: 0; }
    .qa-panel code { background: #1e293b; padding: 1px 5px; border-radius: 3px; font-size: 0.8rem; color: #f9a8d4; font-family: monospace; }
    .qa-panel ul { margin: 4px 0 0; padding-left: 18px; }
    .qa-panel li { margin-bottom: 3px; }
    .qa-error-tag { display: inline-block; background: #7f1d1d; color: #fca5a5; border-radius: 3px; padding: 1px 6px; font-size: 0.75rem; font-weight: 600; margin-right: 4px; white-space: nowrap; }
    .qa-pass-tag { display: inline-block; background: #14532d; color: #86efac; border-radius: 3px; padding: 1px 6px; font-size: 0.75rem; font-weight: 600; margin-right: 4px; }
    .qa-source-tag { display: inline-block; background: #1e3a5f; color: #93c5fd; border-radius: 3px; padding: 1px 6px; font-size: 0.75rem; font-weight: 600; margin-right: 4px; }
    .qa-fp-tag { display: inline-block; background: #78350f; color: #fde68a; border-radius: 3px; padding: 1px 6px; font-size: 0.75rem; font-weight: 600; margin-right: 4px; white-space: nowrap; }
  </style>
</head>
<body>

<div class="qa-panel">
  <div class="qa-panel-header">
    <span class="qa-case-num">Case #{N}</span>
    <span class="qa-rule-id">{rule-id}</span>
    <!-- add qa-source-tag or qa-fp-tag here if applicable -->
  </div>
  <dl>
    <dt>WCAG criteria</dt>
    <dd>{criterion number} {criterion name} — {level}</dd>
    <!-- include only when case maps to a W3C technique or failure: -->
    <dt>W3C technique</dt>
    <dd><a href="{url}" style="color:#93c5fd;">{code}: {title}</a></dd>
    <dt>Elements with errors</dt>  <!-- or "Elements under test" for pass/FP cases -->
    <dd>...</dd>
    <dt>Issues</dt>  <!-- or "Expected result" for pass/FP cases -->
    <dd><ul>
      <li><span class="qa-error-tag">ERROR {criterion}</span> ...</li>
    </ul></dd>
    <!-- for false positive cases only: -->
    <dt>Why a scanner may false-positive</dt>
    <dd><ul>
      <li><span class="qa-fp-tag">FALSE POSITIVE RISK</span> ...</li>
    </ul></dd>
  </dl>
</div>

<!-- test HTML starts here — one clear h1, then the scenario -->
<h1>{Descriptive heading matching the title}</h1>
...

</body>
</html>
```

---

## QA panel rules

- **Copy the panel CSS verbatim.** Do not reformat, reorder, or abbreviate it.
- **Panel comes first** in `<body>`, before any test HTML.
- **Header tags to use:**

| Tag class | When to use |
|---|---|
| `qa-case-num` | Always — the globally unique case number |
| `qa-rule-id` | Always — matches the `behaviour-feature/` subfolder name |
| `qa-source-tag` | When the case maps to a specific W3C technique or failure (e.g. `W3C F44 — Example A`) |
| `qa-fp-tag` in header | When the whole case is a false positive scenario |

- **DL rows to include:**

| Row | Required when |
|---|---|
| `WCAG criteria` | Always |
| `W3C technique` | Case maps to a W3C documented technique/failure |
| `Elements with errors` | Violation or error case |
| `Elements under test` | Pass or false positive case |
| `Issues` | Violation case — use `qa-error-tag` per issue |
| `Expected result` | Pass or false positive case — use `qa-pass-tag` |
| `Why a scanner may false-positive` | False positive case only — use `qa-fp-tag` per reason |
| `Root cause of real issue (separate)` | False positive case where a real issue exists elsewhere on the same page |

- **Inline tags inside `<dd>`:**

| Tag class | Colour | Meaning |
|---|---|---|
| `qa-error-tag` | Red | A confirmed accessibility violation |
| `qa-pass-tag` | Green | Expected pass — no violation |
| `qa-fp-tag` | Amber | A false positive finding or risk |
| `qa-source-tag` | Blue | A W3C reference (also used in header) |

---

## Test HTML rules

- **No external dependencies.** No CDN links, no external JS, no external CSS. Everything must work offline from the file alone.
- **No frameworks.** Plain HTML, CSS, and vanilla JS only.
- **Minimal markup.** Include only what is needed to demonstrate the scenario. Do not add unrelated content.
- **One `<h1>` per page.** It must describe the scenario in plain language, matching the `<title>`.
- **Inline styles on the QA panel link** only: `style="color:#93c5fd;"` on `<a>` inside the panel. Everywhere else use classes.
- **Custom element cases** (`CustomHTMLElements.html`) must define all custom elements via `customElements.define()` in a `<script>` block at the bottom of `<body>`.
- **Comments are welcome** in the test HTML to explain why specific attributes or patterns are present — especially for non-obvious false positive setups.

---

## Case types

### Violation case
Documents a real accessibility failure. The scanner should detect and report it.
- Use `qa-error-tag` in Issues.
- `Elements with errors` row in the DL.
- Title format: `{rule-id} – {what is wrong} ({W3C ref})`

### Pass case
Documents correct implementation. The scanner should report nothing.
- Use `qa-pass-tag` in Expected result.
- `Elements under test` row in the DL.
- Title format: `{rule-id} – {what is correct} (no error)`

### False positive case
Documents a pattern the scanner may incorrectly flag despite being accessible.
- Add `qa-fp-tag` in the panel header.
- Use `qa-pass-tag` in Expected result and `qa-fp-tag` in the false-positive explanation.
- Include a `Why a scanner may false-positive` DL row explaining the scanner's reasoning and why it is wrong.
- If a real issue exists elsewhere on the same page, document it in a `Root cause of real issue (separate)` row.
- Title format: `{rule-id} – {pattern description} (no error)`

---

## QualiBooth scan config sync

Every HTML test file has a live GitHub Pages URL that must be kept in sync with the QualiBooth dev scan configs. This applies on **add**, **rename**, and **delete** — do it in the same operation as the file change, before committing.

### Reference IDs (dev environment)

| Key | Value |
|---|---|
| Environment | QualiBooth **dev** (`qbooth-dev` MCP) |
| Org | `ceco` |
| Org UUID | `a0f273d0-9765-403e-98dc-7bbb59c70c60` |
| Project | `cecotestacc.github.io` |
| Project UUID | `7bd2f8f7-66da-4b74-9f4d-bf15eb2b3050` |
| Base URL | `https://cecotestacc.github.io/test-cases-accessibility/` |

### Scan config routing

| Folder | Scan config name | Scan config UUID |
|---|---|---|
| `behaviour-feature/` | `BehaviorFeature-tests[from w3 & custom-fromAI]` | `5e3ce39d-16ca-4cec-ba0b-4f2623bc0724` |
| `ScreenReader/` | `BehaviorFeature-tests[from w3 & custom-fromAI]` | `5e3ce39d-16ca-4cec-ba0b-4f2623bc0724` |
| `Custom-HTML-Elements/` | `Custom elements-tests` | `07727068-221a-48b7-8149-3dd5bc380607` |

### URL construction

Prepend the base URL to the file's path relative to the repo root:

```
behaviour-feature/tab-order/positive-tabindex-breaks-order.html
→ https://cecotestacc.github.io/test-cases-accessibility/behaviour-feature/tab-order/positive-tabindex-breaks-order.html

Custom-HTML-Elements/CustomHTMLElements.html
→ https://cecotestacc.github.io/test-cases-accessibility/Custom-HTML-Elements/CustomHTMLElements.html
```

### Actions

**File added** — call `mcp__claude_ai_QualiBooth__add_scan_config_urls` with the new URL:
```
scanConfigUuid: <uuid from routing table above>
urls: ["https://cecotestacc.github.io/test-cases-accessibility/<file-path>"]
confirmed: true   ← all configs are ON_DEMAND, no scheduled impact
```

**File renamed** — three steps, in order:
1. `mcp__claude_ai_QualiBooth__list_scan_config_urls` — search for the old URL to get its UUID
2. `mcp__claude_ai_QualiBooth__delete_scan_config_urls` — delete by that UUID
3. `mcp__claude_ai_QualiBooth__add_scan_config_urls` — add the new URL

**File deleted** — call `mcp__claude_ai_QualiBooth__list_scan_config_urls` to find the URL UUID, then `mcp__claude_ai_QualiBooth__delete_scan_config_urls` to remove it.

### Rules

- Always use the **dev** MCP (`mcp__claude_ai_QualiBooth__*`), never prod.
- All four scan configs are `ON_DEMAND` — `confirmed: true` is always safe to pass.
- Do not add non-HTML files (assets, `.md`, `.json`) to any scan config.
- If a file moves between folders (e.g. `behaviour-feature/` → `Custom-HTML-Elements/`), delete from the old scan config and add to the new one.

---

## What NOT to do

- Do not modify the QA panel CSS — not even whitespace.
- Do not add `tabindex` values greater than 0 unless the case is specifically testing that failure.
- Do not use `role="presentation"` or `aria-hidden` to hide the panel from assistive technology — the panel is informational and must remain in the accessibility tree.
- Do not create a new folder for a rule that already has a folder.
- Do not skip case numbers or reuse them.
- Do not mix multiple failure modes in one file — one scenario per file.
