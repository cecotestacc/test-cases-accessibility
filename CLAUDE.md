# Test Case Authoring Rules

This file is read automatically by Claude Code when working in this repo.
Follow every rule here when creating or editing test cases.

---

## Repo layout

```
behaviour-feature/
  {rule-id}/
    StandardHTMLElements-A.html   ← first standard-HTML case for this rule
    StandardHTMLElements-B.html   ← second standard-HTML case
    StandardHTMLElements-C.html   ← third, and so on
    CustomHTMLElements.html       ← custom-element variant (one per rule)
Custom-HTML-Elements/             ← standalone custom-element demos
ScreenReader/                     ← screen-reader focused cases
```

---

## Filename rules

- **One concept per file.** Each file covers exactly one scenario (one failure mode, one pass, or one false positive).
- **Filename = the test case subject.** Name the file so that reading the filename alone tells you what the case tests. Use the standard series naming:
  - `StandardHTMLElements-A.html`, `StandardHTMLElements-B.html`, … — for standard HTML element cases, lettered sequentially within the rule folder.
  - `CustomHTMLElements.html` — for the custom-element variant of the same rule.
- **Letter assignment** — check the highest letter already present in the folder and use the next one. Never reuse a letter.
- **No other filename formats.** Do not invent names like `footer-false-positive.html` or `test1.html`.

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

## What NOT to do

- Do not modify the QA panel CSS — not even whitespace.
- Do not add `tabindex` values greater than 0 unless the case is specifically testing that failure.
- Do not use `role="presentation"` or `aria-hidden` to hide the panel from assistive technology — the panel is informational and must remain in the accessibility tree.
- Do not create a new folder for a rule that already has a folder.
- Do not skip case numbers or reuse them.
- Do not mix multiple failure modes in one file — one scenario per file.
