# Presentation Style Guide (Default)

Unless the user specifies otherwise, use this style for all presentations.

## Slide Types & Backgrounds

Three slide types with distinct backgrounds:

| Type | Background | Use For |
|------|-----------|---------|
| **Title/Section** | `assets/backgrounds/dark.png` (dark navy with organic waves) | Title slide, section dividers, closing slide |
| **Interlude** | `assets/backgrounds/light.png` (light blue-gray with organic waves) | Transition slides, quote slides, visual breaks |
| **Content** | Solid white `{ color: "FFFFFF" }` | All content slides (the bulk of the deck) |

**Loading backgrounds in code:**
```javascript
const fs = require("fs");
const SKILL_DIR = "${CLAUDE_PLUGIN_ROOT}/skills/presentation";
const darkBg = "image/png;base64," + fs.readFileSync(`${SKILL_DIR}/assets/backgrounds/dark.png`).toString("base64");
const lightBg = "image/png;base64," + fs.readFileSync(`${SKILL_DIR}/assets/backgrounds/light.png`).toString("base64");

// Title slide
slide.background = { data: darkBg };
// Interlude slide
slide.background = { data: lightBg };
// Content slide
slide.background = { color: "FFFFFF" };
```

## Color Palette

| Role | Hex | Usage |
|------|-----|-------|
| Primary | `1E2A5E` | Headers on white bg, cards, accents |
| Accent | `E04040` | Subtitles, highlights, key numbers |
| Text | `1E293B` | Body text on white backgrounds |
| Muted | `4A5568` | Secondary text, captions, bullets |
| Light Text | `CADCFC` | Text on dark backgrounds |
| White | `FFFFFF` | Primary text on dark backgrounds |

## Typography

Fonts chosen for Google Slides compatibility (no font substitution issues).

| Element | Font | Size | Color |
|---------|------|------|-------|
| Slide title (dark bg) | Arial Black | 44-54pt bold | `FFFFFF` |
| Slide title (white bg) | Arial Black | 36-44pt bold | `1E2A5E` |
| Subtitle / date | Arial | 20-22pt bold | `E04040` |
| Section header | Arial Black | 20-24pt bold | `1E2A5E` |
| Body text | Arial | 14-16pt | `1E293B` |
| Bullet text | Arial | 14-16pt | `4A5568` |
| Captions | Arial | 10-12pt | `4A5568` |
| Big stat number | Arial Black | 60-72pt bold | `E04040` or `CADCFC` (on dark) |
| Stat label | Arial | 14-16pt | `4A5568` or `FFFFFF` (on dark) |

## Content Slide Design

Content slides use a **clean white background**. Add visual interest through:

- **Navy accent cards** (`1E2A5E` fill) for stat callouts or key points
- **White cards with shadow** on interlude slides for contrast
- **Left-aligned text** for all body content; center only titles
- **Charts and tables** using the color palette above

**Layout options:**
- Two-column (text left, visual right)
- Icon + text rows
- 2x2 or 2x3 grid of cards
- Large stat callout with description

**Data display:**
- Big stat numbers (60-72pt) with small labels below
- Comparison columns (before/after, side-by-side)
- Timeline or process flow

## Spacing

- 0.5" minimum margins from slide edges
- 0.3-0.5" between content blocks
- Leave breathing room -- don't fill every inch

## Avoid

- **Don't repeat the same layout** -- vary columns, cards, and callouts across slides
- **Don't center body text** -- left-align paragraphs and lists; center only titles
- **Don't use accent lines under titles** -- use whitespace instead
- **Don't use low-contrast elements** -- test readability against the background
- **Don't forget text box padding** -- set `margin: 0` when aligning with shapes
- **Don't mix spacing randomly** -- pick 0.3" or 0.5" gaps and use consistently
