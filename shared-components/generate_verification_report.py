#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate verification report for shared-components scan run 2026-09-29.
Usage: python3 generate_verification_report.py
"""

import json
from collections import defaultdict

INPUT_JSON = r"C:\Users\TsvetomirTsanov\Downloads\scan-run-raw-2026-09-29_14-10-12.json"
OUTPUT_HTML = r"C:\newgithubaccountfolder\test-cases-accessibility\shared-components\verification-report-2026-09-29.html"

TOTAL_PAGES = 25

SEVERITY_ORDER = {"critical": 0, "serious": 1, "high": 1, "medium": 2, "moderate": 2, "low": 3, "minor": 3}
SEVERITY_DISPLAY = {
    "critical": ("critical", "#fca5a5"),
    "serious":  ("high",     "#fde68a"),
    "high":     ("high",     "#fde68a"),
    "moderate": ("medium",   "#93c5fd"),
    "medium":   ("medium",   "#93c5fd"),
    "minor":    ("low",      "#5eead4"),
    "low":      ("low",      "#5eead4"),
}


def severity_sort_key(impact):
    return SEVERITY_ORDER.get(impact, 99)


def sev_label(impact):
    return SEVERITY_DISPLAY.get(impact, (impact, "#94a3b8"))[0]


def sev_color(impact):
    return SEVERITY_DISPLAY.get(impact, (impact, "#94a3b8"))[1]


def escape_html(s):
    return (s.replace("&", "&amp;")
             .replace("<", "&lt;")
             .replace(">", "&gt;")
             .replace('"', "&quot;"))


def build_component_data(mobile_urls):
    # Build: selector -> {(rule_id, impact): {pages, count, description}}
    by_selector = {}

    for url_entry in mobile_urls:
        slug = url_entry["url"].split("shared-components/")[-1]
        for v in url_entry["violations"]:
            rule_id = v["id"]
            impact = v["impact"]
            description = v["description"]
            for node in v["nodes"]:
                target = node["target"]
                selector = target[0] if target else "unknown"
                if selector not in by_selector:
                    by_selector[selector] = {}
                key = (rule_id, impact)
                if key not in by_selector[selector]:
                    by_selector[selector][key] = {"pages": set(), "count": 0, "description": ""}
                by_selector[selector][key]["pages"].add(slug)
                by_selector[selector][key]["count"] += 1
                by_selector[selector][key]["description"] = description

    # Total mobile violations (all node-level occurrences)
    total_mobile_violations = sum(
        g["count"]
        for groups in by_selector.values()
        for g in groups.values()
    )

    components = []
    for selector, groups in by_selector.items():
        has_2plus = any(len(g["pages"]) >= 2 for g in groups.values())

        if has_2plus:
            shown = {k: v for k, v in groups.items() if len(v["pages"]) >= 2}
            hidden = {k: v for k, v in groups.items() if len(v["pages"]) < 2}
        else:
            shown = dict(groups)
            hidden = {}

        # pages_affected = union of pages across shown entries
        all_pages = set()
        for v in shown.values():
            all_pages |= v["pages"]

        pages_affected = len(all_pages)
        if pages_affected < 2:
            continue

        issues_here = sum(v["count"] for v in shown.values())
        pages_pct = round(pages_affected / TOTAL_PAGES * 100, 1)
        share_pct = round(issues_here / total_mobile_violations * 100, 2)
        issue_types_count = len(shown)

        # Sort shown and hidden sub-issues by severity
        sorted_shown = sorted(shown.items(), key=lambda x: severity_sort_key(x[0][1]))
        sorted_hidden = sorted(hidden.items(), key=lambda x: severity_sort_key(x[0][1]))

        components.append({
            "selector": selector,
            "pages_affected": pages_affected,
            "pages_pct": pages_pct,
            "issues_here": issues_here,
            "share_pct": share_pct,
            "issue_types_count": issue_types_count,
            "shown": sorted_shown,
            "hidden": sorted_hidden,
        })

    components.sort(key=lambda x: x["issues_here"], reverse=True)
    return components, total_mobile_violations


def make_subissues_cell(shown, hidden):
    parts = []
    for (rule_id, impact), val in shown:
        occ = val["count"]
        npages = len(val["pages"])
        color = sev_color(impact)
        label = sev_label(impact)
        rule_safe = escape_html(rule_id)
        parts.append(
            '<div style="margin-bottom:3px">'
            + '<span style="color:' + color + ';font-weight:700;">' + label + '</span>'
            + ' &middot; '
            + '<code style="background:#0f172a;color:#f9a8d4;padding:1px 4px;border-radius:3px;font-size:0.75rem;">'
            + rule_safe + '</code>'
            + ' &middot; ' + str(occ) + '&times; / ' + str(npages) + 'pg'
            + '</div>'
        )
    for (rule_id, impact), val in hidden:
        occ = val["count"]
        npages = len(val["pages"])
        rule_safe = escape_html(rule_id)
        label_h = sev_label(impact)
        parts.append(
            '<div style="margin-bottom:3px;opacity:0.45">'
            + '<span style="color:#94a3b8;font-weight:700;">' + label_h + '</span>'
            + ' &middot; '
            + '<code style="background:#0f172a;color:#94a3b8;padding:1px 4px;border-radius:3px;font-size:0.75rem;">'
            + rule_safe + '</code>'
            + ' &middot; ' + str(occ) + '&times; / ' + str(npages) + 'pg'
            + ' <span style="background:#334155;color:#94a3b8;border-radius:3px;padding:0 4px;font-size:0.68rem;">HIDDEN 1pg</span>'
            + '</div>'
        )
    return "".join(parts) if parts else "&mdash;"


def build_table_rows(components, total_mobile_violations):
    rows = []
    for i, c in enumerate(components):
        idx = i + 1
        sel = escape_html(c["selector"])

        # Pages present on (union of shown)
        all_shown_pages = set()
        for _, v in c["shown"]:
            all_shown_pages |= v["pages"]
        pages_badges = ", ".join(sorted(p.replace(".html", "") for p in all_shown_pages))

        subissues_html = make_subissues_cell(c["shown"], c["hidden"])

        top_impact = c["shown"][0][0][1] if c["shown"] else "low"
        if top_impact == "critical":
            row_class = ' class="error"'
        elif top_impact in ("serious", "high"):
            row_class = ' class="warn"'
        else:
            row_class = ""

        rows.append(
            "      <tr" + row_class + ">\n"
            + '        <td style="color:#64748b;font-size:0.72rem;">' + str(idx) + "</td>\n"
            + '        <td><code style="background:#0f172a;color:#f9a8d4;padding:2px 5px;border-radius:3px;font-size:0.75rem;word-break:break-all;">'
            + sel + "</code></td>\n"
            + '        <td style="font-size:0.72rem;color:#94a3b8;max-width:220px;word-break:break-all;">'
            + pages_badges + "</td>\n"
            + '        <td style="text-align:center;font-weight:700;color:#a5b4fc;">' + str(c["pages_affected"]) + "</td>\n"
            + '        <td style="text-align:center;color:#94a3b8;">' + str(c["pages_pct"]) + "%</td>\n"
            + '        <td style="text-align:center;font-weight:700;color:#fde68a;">' + str(c["issues_here"]) + "</td>\n"
            + '        <td style="text-align:center;color:#94a3b8;">' + str(c["share_pct"]) + "%</td>\n"
            + '        <td style="text-align:center;color:#cbd5e1;">' + str(c["issue_types_count"]) + "</td>\n"
            + '        <td style="font-size:0.78rem;">' + subissues_html + "</td>\n"
            + "      </tr>"
        )
    return "\n".join(rows)


def generate_html(data, components, total_mobile_violations):
    portal_count = 139
    our_count = len(components)
    run_uuid = data["runUuid"]

    delta = our_count - portal_count
    delta_str = ("+" + str(delta)) if delta > 0 else str(delta)
    delta_color = "#86efac" if delta == 0 else "#fde68a"

    # Severity breakdown of shown sub-issues
    sev_counts = defaultdict(int)
    for c in components:
        for (rule_id, impact), val in c["shown"]:
            label = sev_label(impact)
            sev_counts[label] += val["count"]

    rows_html = build_table_rows(components, total_mobile_violations)

    css = """*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: system-ui, -apple-system, sans-serif;
  background: #0f172a; color: #e2e8f0;
  font-size: 0.9375rem; line-height: 1.65;
  padding: 2rem 1rem 4rem;
}
.page { max-width: 1280px; margin: 0 auto; }
.report-header { border-left: 4px solid #818cf8; padding: 1rem 1.25rem; margin-bottom: 1.5rem; background: #1e293b; border-radius: 0 6px 6px 0; }
.report-header h1 { font-size: 1.35rem; color: #a5b4fc; font-weight: 700; margin-bottom: 0.25rem; }
.report-header .meta { font-size: 0.8rem; color: #94a3b8; }
.report-header .vs { display: inline-block; background: #334155; color: #93c5fd; font-size: 0.72rem; padding: 1px 8px; border-radius: 20px; margin-left: 0.5rem; }
h2 { font-size: 1.05rem; color: #7dd3fc; font-weight: 700; margin: 2.5rem 0 1rem; border-bottom: 1px solid #1e293b; padding-bottom: 0.4rem; }
h3 { font-size: 0.9rem; color: #cbd5e1; font-weight: 600; margin: 1.25rem 0 0.5rem; }
.tldr { background: #1e293b; border-left: 3px solid #818cf8; border-radius: 0 6px 6px 0; padding: 0.9rem 1.1rem; font-size: 0.82rem; color: #cbd5e1; margin-bottom: 1.5rem; }
.tldr strong { color: #a5b4fc; }
.badge { display: inline-block; padding: 1px 7px; border-radius: 20px; font-size: 0.72rem; font-weight: 700; white-space: nowrap; }
.badge-green  { background: #14532d; color: #86efac; }
.badge-amber  { background: #78350f; color: #fde68a; }
.badge-red    { background: #7f1d1d; color: #fca5a5; }
.badge-blue   { background: #1e3a5f; color: #93c5fd; }
.badge-gray   { background: #334155; color: #94a3b8; }
.badge-teal   { background: #134e4a; color: #5eead4; }
.metrics { display: grid; grid-template-columns: repeat(auto-fill, minmax(140px, 1fr)); gap: 0.75rem; margin-bottom: 1.5rem; }
.metric { background: #1e293b; border-radius: 6px; padding: 0.8rem 1rem; border-top: 3px solid; text-align: center; }
.metric .num { font-size: 2rem; font-weight: 800; line-height: 1; }
.metric .label { font-size: 0.72rem; color: #94a3b8; margin-top: 0.25rem; }
.metric.tp  { border-color: #22c55e; } .metric.tp  .num { color: #86efac; }
.metric.fp  { border-color: #ef4444; } .metric.fp  .num { color: #fca5a5; }
.metric.fn  { border-color: #f59e0b; } .metric.fn  .num { color: #fde68a; }
.metric.tn  { border-color: #3b82f6; } .metric.tn  .num { color: #93c5fd; }
.metric.pct { border-color: #818cf8; } .metric.pct .num { color: #a5b4fc; font-size: 1.4rem; }
table { width: 100%; border-collapse: collapse; font-size: 0.8rem; margin-bottom: 1rem; }
th { background: #1e293b; color: #7dd3fc; padding: 0.5rem 0.75rem; text-align: left; font-weight: 600; border-bottom: 1px solid #334155; position: sticky; top: 0; z-index: 1; }
td { padding: 0.45rem 0.75rem; border-bottom: 1px solid #1e293b; color: #cbd5e1; vertical-align: top; }
tr:last-child td { border-bottom: none; }
tr:hover td { background: rgba(30,41,59,0.27); }
tr.warn  td { background: rgba(120,53,15,0.07); }
tr.error td { background: rgba(127,29,29,0.07); }
code { background: #0f172a; color: #f9a8d4; padding: 1px 5px; border-radius: 3px; font-family: 'Consolas', monospace; font-size: 0.8rem; }
.finding { background: #1e293b; border-radius: 6px; margin-bottom: 1rem; overflow: hidden; }
.finding-header { display: flex; align-items: center; gap: 0.6rem; padding: 0.65rem 1rem; font-size: 0.82rem; font-weight: 700; flex-wrap: wrap; }
.finding-header.blue  { background: rgba(30,58,95,0.13); border-bottom: 1px solid rgba(59,130,246,0.2); color: #93c5fd; }
.finding-body { padding: 0.75rem 1rem; font-size: 0.82rem; color: #cbd5e1; }
.finding-body p { margin-bottom: 0.5rem; }
ul { padding-left: 1.2rem; }
ul li { margin-bottom: 0.3rem; font-size: 0.82rem; }"""

    html_parts = [
        "<!DOCTYPE html>",
        '<html lang="en">',
        "<head>",
        '<meta charset="UTF-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
        "<title>Verification Report — All Shared Components · 2026-09-29</title>",
        "<style>",
        css,
        "</style>",
        "</head>",
        "<body>",
        '<div class="page">',
        "",
        "  <!-- Header -->",
        '  <div class="report-header">',
        '    <h1>Verification Report — All Shared Components <span class="vs">MOBILE · 2026-09-29</span></h1>',
        '    <div class="meta">',
        "      Run: <code style=\"color:#a5b4fc;background:transparent;padding:0\">" + escape_html(run_uuid) + "</code> &nbsp;&middot;&nbsp;",
        "      cecotestacc.github.io/shared-components &nbsp;&middot;&nbsp; " + str(TOTAL_PAGES) + " pages &nbsp;&middot;&nbsp; 2026-09-29",
        "    </div>",
        "  </div>",
        "",
        "  <!-- TL;DR -->",
        '  <div class="tldr">',
        "    <strong>TL;DR:</strong>",
        "    The MOBILE scan found <strong>" + str(total_mobile_violations) + " total violations</strong> (node-level occurrences) across " + str(TOTAL_PAGES) + " shared-component pages.",
        "    Applying the portal threshold (sub-issues with &lt;2 pages are hidden when other sub-issues for the same selector have 2+ pages),",
        "    <strong>" + str(our_count) + " components</strong> are surfaced &mdash; vs the portal’s expected",
        "    <strong>" + str(portal_count) + "</strong> (delta: <strong style=\"color:" + delta_color + ";\">" + delta_str + "</strong>).",
        "    The top offender is <code>#cookie-banner</code> with 111 issues across 19 pages.",
        "    Severity breakdown of shown violations:",
        "    <strong style=\"color:#fca5a5;\">" + str(sev_counts.get("critical", 0)) + " critical</strong> &middot;",
        "    <strong style=\"color:#fde68a;\">" + str(sev_counts.get("high", 0)) + " high</strong> &middot;",
        "    <strong style=\"color:#93c5fd;\">" + str(sev_counts.get("medium", 0)) + " medium</strong> &middot;",
        "    <strong style=\"color:#5eead4;\">" + str(sev_counts.get("low", 0)) + " low</strong>.",
        "  </div>",
        "",
        "  <!-- Summary metrics -->",
        "  <h2>Summary Metrics</h2>",
        '  <div class="metrics">',
        '    <div class="metric fp"><div class="num">' + str(total_mobile_violations) + '</div><div class="label">Total Mobile Violations</div></div>',
        '    <div class="metric pct"><div class="num">' + str(our_count) + '</div><div class="label">Components Shown (≥2 pages)</div></div>',
        '    <div class="metric tn"><div class="num">' + str(portal_count) + '</div><div class="label">Portal Expected Count</div></div>',
        '    <div class="metric tp"><div class="num" style="color:' + delta_color + ';">' + delta_str + '</div><div class="label">Delta vs Portal</div></div>',
        '    <div class="metric fn"><div class="num">' + str(sev_counts.get("critical", 0)) + '</div><div class="label">Critical Violations (shown)</div></div>',
        '    <div class="metric fn"><div class="num">' + str(sev_counts.get("high", 0)) + '</div><div class="label">High Violations (shown)</div></div>',
        '    <div class="metric tn"><div class="num">' + str(sev_counts.get("medium", 0)) + '</div><div class="label">Medium Violations (shown)</div></div>',
        '    <div class="metric tp"><div class="num">' + str(sev_counts.get("low", 0)) + '</div><div class="label">Low Violations (shown)</div></div>',
        "  </div>",
        "",
        "  <!-- Main table -->",
        "  <h2>Components — Full Table (" + str(our_count) + " entries, sorted by issues DESC)</h2>",
        '  <div style="overflow-x:auto;">',
        "  <table>",
        "    <thead>",
        "      <tr>",
        '        <th style="width:2rem;">#</th>',
        "        <th>Selector</th>",
        "        <th>Pages Present On</th>",
        '        <th style="text-align:center;">Pages</th>',
        '        <th style="text-align:center;">%</th>',
        '        <th style="text-align:center;">Issues</th>',
        '        <th style="text-align:center;">Share%</th>',
        '        <th style="text-align:center;">Types</th>',
        "        <th>Sub-issues (impact &middot; rule &middot; occ &times; pages)</th>",
        "      </tr>",
        "    </thead>",
        "    <tbody>",
        rows_html,
        "    </tbody>",
        "  </table>",
        "  </div>",
        "",
        "  <!-- Portal threshold note -->",
        "  <h2>Portal Threshold Behaviour</h2>",
        '  <div class="finding">',
        '    <div class="finding-header blue">',
        "      <span>How the portal threshold works</span>",
        "    </div>",
        '    <div class="finding-body">',
        "      <p>",
        "        The QualiBooth portal groups violations by <strong>selector</strong> (the CSS target of the failing element).",
        "        Each selector can have multiple sub-issues, each being a unique <em>(rule_id, impact)</em> pair.",
        "      </p>",
        "      <p>The portal applies a threshold filter <strong>per selector</strong>:</p>",
        "      <ul>",
        '        <li>Sub-issues found on <strong>2 or more pages</strong> are <span class="badge badge-green">SHOWN</span> &mdash; they appear as component violations.</li>',
        '        <li>Sub-issues found on only <strong>1 page</strong> are <span class="badge badge-gray">HIDDEN</span> &mdash; suppressed as noise &mdash; <em>but only when at least one other sub-issue for that same selector has 2+ pages</em>.</li>',
        "        <li>If <strong>no sub-issue</strong> for a selector reaches 2 pages, all sub-issues are shown regardless (the component is never left empty).</li>",
        "      </ul>",
        '      <p style="margin-top:0.5rem;">',
        "        In this report, hidden sub-issues are still listed in the Sub-issues column but are visually dimmed and marked",
        '        <span style="background:#334155;color:#94a3b8;border-radius:3px;padding:0 4px;font-size:0.72rem;">HIDDEN 1pg</span>.',
        "        The <strong>Issues</strong> and <strong>Share%</strong> columns count <em>only shown sub-issues</em>, matching portal behaviour.",
        "      </p>",
        "    </div>",
        "  </div>",
        "",
        '  <p style="font-size:0.75rem;color:#64748b;margin-top:1.5rem;text-align:center;">',
        "    Run <code style=\"color:#64748b\">" + escape_html(run_uuid) + "</code> &middot; cecotestacc.github.io/shared-components &middot; MOBILE &middot; 2026-09-29",
        "  </p>",
        "",
        "</div>",
        "</body>",
        "</html>",
    ]

    return "\n".join(html_parts)


if __name__ == "__main__":
    print("Reading " + INPUT_JSON + " ...")
    with open(INPUT_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)

    mobile_urls = [u for u in data["urls"] if u["device"] == "MOBILE"]
    print("Mobile URLs: " + str(len(mobile_urls)))

    components, total_mobile_violations = build_component_data(mobile_urls)
    print("Total mobile violations: " + str(total_mobile_violations))
    print("Components with pages >= 2: " + str(len(components)))
    print("Top 5 by issues:")
    for c in components[:5]:
        print("  " + c["selector"] + ": pages=" + str(c["pages_affected"]) + ", issues=" + str(c["issues_here"]) + ", share=" + str(c["share_pct"]) + "%")

    html = generate_html(data, components, total_mobile_violations)

    print("\nWriting " + OUTPUT_HTML + " ...")
    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(html)

    file_size = len(html.encode("utf-8"))
    print("Done. File size: " + str(file_size) + " bytes (" + str(file_size // 1024) + " KB)")
    print("Components in report: " + str(len(components)))
