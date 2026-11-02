---
name: Palinode Loop
description: Dark, high-contrast architecture explainer for a human-governed agent feedback workflow.
colors:
  page: "#0d1117"
  surface: "#161b22"
  border: "#30363d"
  text: "#e6edf3"
  muted: "#b8c5ce"
  teal: "#7ee7c1"
  coral: "#ffa28b"
  control: "#21262d"
  control-outline: "#6e7d8a"
  code-text: "#d4e5dd"
  active-node: "#1d4039"
typography:
  display:
    fontFamily: "Fraunces, Georgia, serif"
    fontSize: "clamp(3rem, 6vw, 5.4rem)"
    fontWeight: 500
    lineHeight: 1.02
    letterSpacing: "-0.035em"
  headline:
    fontFamily: "Fraunces, Georgia, serif"
    fontSize: "clamp(2.2rem, 4vw, 3.5rem)"
    fontWeight: 500
    lineHeight: 1.08
    letterSpacing: "-0.025em"
  title:
    fontFamily: "Fraunces, Georgia, serif"
    fontSize: "1.45rem"
    fontWeight: 500
  body:
    fontFamily: "system-ui, -apple-system, sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.65
  label:
    fontFamily: "system-ui, -apple-system, sans-serif"
    fontSize: "0.86rem"
    fontWeight: 400
  code:
    fontFamily: "ui-monospace, SFMono-Regular, monospace"
    fontSize: "0.8rem"
    fontWeight: 400
    lineHeight: 1.7
rounded:
  architecture: "9px"
  canvas: "10px"
  node: "7px"
  control: "5px"
  code: "6px"
spacing:
  mobile-gutter: "16px"
  desktop-gutter: "32px"
  stage-gap: "7px"
  control-gap: "10px"
  section-space: "88px"
  mobile-section-space: "65px"
components:
  button-stage:
    backgroundColor: "{colors.control}"
    textColor: "{colors.text}"
    typography: "{typography.label}"
    rounded: "{rounded.control}"
    padding: "5px 9px"
  button-selected:
    backgroundColor: "{colors.teal}"
    textColor: "{colors.page}"
    typography: "{typography.label}"
    rounded: "{rounded.control}"
    padding: "5px 9px"
  button-primary:
    backgroundColor: "{colors.control}"
    textColor: "{colors.text}"
    typography: "{typography.body}"
    rounded: "{rounded.control}"
    padding: "8px 12px"
  architecture-panel:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    rounded: "{rounded.architecture}"
    padding: "0px"
  code-panel:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.code-text}"
    typography: "{typography.code}"
    rounded: "{rounded.code}"
    padding: "20px"
---

# Design System: Palinode Loop

## Overview

**Creative North Star: “The Revisable Ledger”**

The interface is a compact field guide to a feedback architecture. Fraunces gives the argument an editorial voice; system sans-serif keeps labels and explanations direct. Deep page and panel tones support long technical reading, while teal tracks the evidence path and coral singles out the human decision.

The architectural contribution is framed as two lifecycles—evidence and active rules—joined by approval and recorded failures. The authored SVG is the central diagram: a folded-paper evidence record moves through six stages, with its state in SVG title metadata. On narrow screens, a native progress cue summarizes the diagram's horizontal position; the code section connects the picture to the ledger. Borders and tonal changes organize the page without shadows or decorative effects. Print styles switch the surrounding page and code panels to light output while the SVG retains its literal dark canvas.

**Key Characteristics:**
- Dark page and panel surfaces with high-contrast text.
- Teal marks the process path; coral marks the approval boundary.
- Compact controls and code-shaped details support technical inspection.
- Evidence stays inspectable; approved rules stay revisable.

## Colors

The dark neutral base is interrupted by two semantic accents: teal for the path and coral for human authority.

### Primary
- **Near-black page** (`colors.page`): Full-page canvas and code excerpts.
- **Raised charcoal surface** (`colors.surface`): Architecture frame and code panels.

### Secondary
- **Mint teal** (`colors.teal`): Links, process connectors, selected stages, and active-node outlines.

### Tertiary
- **Soft coral** (`colors.coral`): Approval gate, emphasized hero word, and keyboard focus.

### Neutral
- **Cool white text** (`colors.text`): Main copy and diagram labels.
- **Blue-gray muted text** (`colors.muted`): Secondary explanations and code annotations.
- **Graphite border** (`colors.border`): Section rules and panel outlines.
- **Control charcoal** (`colors.control`): Unselected stage buttons and SVG nodes.
- **Slate outline** (`colors.control-outline`): Walkthrough controls and inactive SVG nodes.
- **Pale code text** (`colors.code-text`): Example excerpts and code.
- **Active forest fill** (`colors.active-node`): Current node in the SVG path.

**The Approval Color Rule.** Coral identifies the human decision boundary; teal identifies the process path and active stage.

## Typography

**Display Font:** Fraunces (self-hosted), with Georgia and serif fallbacks

**Body Font:** system-ui, -apple-system, sans-serif

**Label/Mono Font:** system sans-serif for navigation and controls; ui-monospace, SFMono-Regular, monospace for code details.

**Character:** Fraunces adds a literary note to the thesis and section headings. The supporting type is compact and functional, with monospace reserved for actual schema, function names, and commands.

### Hierarchy
- **Display** (500 weight, tight line-height): The hero statement.
- **Headline** (500 weight, balanced): Major section headings.
- **Title** (500 weight): Study names and the active walkthrough step.
- **Body** (400 weight, generous line-height): Explanatory prose and controls.
- **Label** (compact sans-serif): Navigation, stage selectors, and SVG labels.
- **Code** (monospace): Schema snippets, evidence excerpts, and reproducible commands.

## Layout

The centered content frame caps at 1180px. The hero is a single concise statement above the full-width architecture walkthrough. Below it, sections pair headings with supporting material on wide screens and stack into one reading column at the tablet breakpoint. The six-stage controls wrap; evidence entries remain open rows rather than cards.

At narrow widths the page gutters and section spacing tighten. At a 390px viewport, the SVG keeps its 800px drawing width inside an approximately 341px visible scroll region while the document remains 375px wide. A native progress cue reports start, middle, or end only when the diagram overflows; it is hidden when the full drawing fits. Step detail, evidence, and source layouts reflow to one column. Code blocks remain visibly distinct and scroll horizontally where a line must stay intact.

Print styles switch page and surface to white, text and accents to near-black, borders to gray, and code panels to a pale surface. They hide interactive controls and let the SVG fit the printed width; its internal dark canvas remains literal.

## Elevation & Depth

The system is flat: dark surface shifts, fine borders, and selected fills establish hierarchy. No drop shadows are used. Focus has a clear coral outline, and state changes use short fill and stroke transitions; reduced-motion settings remove those transitions and move the artifact directly.

## Shapes

The page uses lightly rounded architecture and code frames, compact rounded controls, and slightly softer SVG nodes. Borders stay fine and structural. The hold route uses a dashed coral line to distinguish a candidate that does not enter active guidance.

## Components

### Navigation
- **Character:** A quiet Fraunces wordmark with three teal text links.
- **Mobile:** Links may wrap; the reading frame narrows and the main content stacks.
- **States:** Links shift toward a brighter mint on hover; keyboard focus uses a visible coral outline.

### Buttons and Select
- **Stage selector:** Compact dark buttons wrap in a row; the current stage uses teal fill and page-color text.
- **Walkthrough controls:** One Play/Pause control and one Next stage control; disabled controls reduce opacity.
- **Decision select:** Appears only at the human-decision stage and offers Approve or Hold candidate.
- **Focus / hover:** Hover sharpens the border toward teal; focus receives a coral outline.

### Cards / Containers
- **Architecture frame:** Bordered surface containing the SVG, caption, and walkthrough; the drawing scrolls inside its own region.
- **Mobile scroll cue:** Native progress indicator with a position label; shown only when horizontal overflow exists.
- **Evidence entries:** Open rows separated by fine borders, keeping source details readable.
- **Code panel:** Surface fill, pale monospace text, and a fine border distinguish machine-readable examples from prose.

### Signature Component: Moving Evidence Record

The six-node SVG is the system's explanatory centerpiece. A folded-paper glyph moves along the teal path as the user advances; its state is held in SVG title metadata rather than a tiny visible label. Choosing Hold sends it onto the dashed coral branch, outside active guidance. Function and field labels connect each stage to the Python implementation. The footer closes with “Evidence stays inspectable” and “Approved rules stay revisable.”

## Do's and Don'ts

### Do:
- **Do** keep the background dark and body text high-contrast.
- **Do** reserve teal for flow and active state, and coral for the approval boundary and focus.
- **Do** keep the artifact moving inside the SVG rather than shifting the diagram's topology.
- **Do** reserve monospace for code, data, and function names.

### Don't:
- **Don't** add palette ramps, gradients, or new state colors that are not implemented in the page.
- **Don't** make the diagram wider than its bounded scroll region on mobile.
- **Don't** add drop shadows or extra control rows that compete with the six-stage explanation.
