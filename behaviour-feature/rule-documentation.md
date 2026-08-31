{
  "focus-obscured": {
    "id": "focus-obscured",
    "impact": "serious",
    "tags": ["cat.keyboard", "wcag22aa", "wcag2411", "wcag2412"],
    "metadata": {
      "help": "Focus not obscured",
      "description": "At every tab stop, hit-tests nine points on the focused component and measures how much of it is painted over by higher-stacked content. Entirely covered fails 2.4.11 (AA); partially covered fails 2.4.12 (AAA)."
    },
    "violation": "aa"
  },
  "focus-visible": {
    "id": "focus-visible",
    "impact": "serious",
    "tags": ["cat.keyboard", "wcag2aa", "wcag247", "wcag2413"],
    "metadata": {
      "help": "Focus visible",
      "description": "Screenshots each control focused and unfocused over the same region and compares the pixels. Reports 2.4.7 when the two renderings are identical, and 2.4.13 when an indicator exists but is thinner or lower contrast than the criterion requires."
    },
    "violation": "aa"
  },
  "tab-order": {
    "id": "tab-order",
    "impact": "serious",
    "tags": ["cat.keyboard", "wcag2a", "wcag243"],
    "metadata": {
      "help": "Focus order",
      "description": "Compares the observed tab sequence against DOM order and against visual reading order. A DOM-order mismatch is reported as certain; a reading-order mismatch is reported as likely, with a screenshot of the numbered tab stops."
    },
    "violation": "a"
  },
  "keyboard-trap": {
    "id": "keyboard-trap",
    "impact": "critical",
    "tags": ["cat.keyboard", "wcag2a", "wcag212"],
    "metadata": {
      "help": "Keyboard trap",
      "description": "Tabs through the page and looks for a set of controls that keyboard focus cannot leave. A modal dialog that confines focus but releases it on Escape is correct behaviour and is not reported."
    },
    "violation": "a"
  },
  "accessible-name": {
    "id": "accessible-name",
    "impact": "serious",
    "tags": ["cat.name-role-value", "wcag2a", "wcag21a", "wcag253", "wcag412"],
    "metadata": {
      "help": "Accessible name quality",
      "description": "Reads Chrome's own accessible-name computation, including which of aria-labelledby, aria-label, native label, contents and title contributed. Reports names that hide the visible label, names duplicated by their description, and references that resolve to nothing."
    },
    "violation": "a"
  },
  "contrast-image": {
    "id": "contrast-image",
    "impact": "serious",
    "tags": ["cat.color", "wcag2aa", "wcag143"],
    "metadata": {
      "help": "Text contrast over images, gradients and video",
      "description": "Measures the contrast of text whose backdrop is not a flat colour - exactly the population a static checker has to mark as needs review. Captures the text, captures the same region with the glyphs made transparent, and compares each glyph pixel against the background actually behind it."
    },
    "violation": "aa"
  },
  "reflow": {
    "id": "reflow",
    "impact": "serious",
    "tags": ["cat.structure", "wcag21aa", "wcag1410"],
    "metadata": {
      "help": "Reflow at 320 CSS pixels",
      "description": "Renders the page at the 320 CSS pixel width the criterion names and finds the outermost elements that still force horizontal scrolling, ignoring content deliberately placed in a scrollable region."
    },
    "violation": "aa"
  },
  "text-spacing": {
    "id": "text-spacing",
    "impact": "serious",
    "tags": ["cat.structure", "wcag21aa", "wcag1412"],
    "metadata": {
      "help": "Text spacing",
      "description": "Applies the criterion's line height, letter spacing and word spacing to the whole page and compares the geometry before and after, reporting text that becomes clipped by a fixed-size box or collides with its neighbours."
    },
    "violation": "aa"
  },
  "forced-colors": {
    "id": "forced-colors",
    "impact": "serious",
    "tags": ["cat.color", "wcag21aa", "wcag1411"],
    "metadata": {
      "help": "Forced colors mode",
      "description": "Emulates Windows High Contrast and measures each small graphic against its own surroundings before and after. Reports the ones that become indistinguishable from the page - typically icons drawn with a mask and a background colour, gradients, and outlines drawn with box-shadow."
    },
    "violation": "aa"
  },
  "live-region": {
    "id": "live-region",
    "impact": "serious",
    "tags": ["cat.aria", "wcag21aa", "wcag413"],
    "metadata": {
      "help": "Live region mechanics",
      "description": "Records every DOM mutation from document start and reconstructs when each live region came into existence relative to the content it holds. Reports the updates a screen reader will not announce, with the timeline that proves it."
    },
    "violation": "aa"
  },
  "hover-focus-content": {
    "id": "hover-focus-content",
    "impact": "serious",
    "tags": ["cat.structure", "wcag21aa", "wcag1413", "wcag211"],
    "metadata": {
      "help": "Content on hover or focus",
      "description": "Hovers each tooltip trigger and scripts the three requirements of 1.4.13 in turn: the content stays while the pointer moves into it, Escape dismisses it without moving the pointer, and it does not disappear on its own. Also reports content that only hover can reveal."
    },
    "violation": "aa"
  },
  "modal-lifecycle": {
    "id": "modal-lifecycle",
    "impact": "serious",
    "tags": ["cat.aria", "wcag2a", "wcag212", "wcag243", "wcag412"],
    "metadata": {
      "help": "Modal dialog lifecycle",
      "description": "Opens each candidate dialog and walks the full contract: focus moves in, Tab stays contained, the rest of the page is removed from the accessibility tree, Escape closes it, and focus returns to the control that opened it. Each step is a separate assertion with its own finding."
    },
    "violation": "a"
  },
  "captions": {
    "id": "captions",
    "impact": "serious",
    "tags": ["cat.time-and-media", "wcag2a", "wcag122"],
    "metadata": {
      "help": "Caption accuracy and synchronisation",
      "description": "Transcribes the audio and compares the result against the supplied caption file: word error rate with a full aligned diff, median timing offset, drift over the length of the media, and the proportion of speech no cue covers."
    },
    "violation": "a"
  },
  "flash-motion": {
    "id": "flash-motion",
    "impact": "critical",
    "tags": ["cat.time-and-media", "wcag2a", "wcag231", "wcag222"],
    "metadata": {
      "help": "Flashing, motion and reduced-motion preference",
      "description": "Records the viewport frame by frame and measures luminance over time. Applies the 2.3.1 flash threshold arithmetic literally, finds motion that runs past five seconds without a pause control, and re-records under prefers-reduced-motion to see whether the preference changes anything."
    },
    "violation": "a"
  }
}
