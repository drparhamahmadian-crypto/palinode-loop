---
name: Palinode Loop
description: Editorial evidence-ledger identity for a human-governed agent feedback workflow.
colors:
  ink: "#192e35"
  paper: "#f4f0e7"
  rust: "#a03e23"
  teal: "#21645b"
  wash: "#ebe5d9"
  active-fill: "#d2e2d8"
  selected-fill: "#d5e5dc"
  on-dark: "#e4ece5"
  dark-divider: "#637a72"
  inset: "#213c3e"
typography:
  display:
    fontFamily: "Fraunces, Georgia, serif"
    fontSize: "clamp(3.1rem, 6.7vw, 6rem)"
    fontWeight: 500
    lineHeight: 0.99
    letterSpacing: "-0.04em"
  display-mobile:
    fontFamily: "Fraunces, Georgia, serif"
    fontSize: "clamp(3.2rem, 13vw, 4.5rem)"
    fontWeight: 500
    lineHeight: 0.99
    letterSpacing: "-0.04em"
  headline:
    fontFamily: "Fraunces, Georgia, serif"
    fontSize: "clamp(2.4rem, 4.2vw, 4rem)"
    fontWeight: 500
    lineHeight: 1.05
    letterSpacing: "-0.03em"
  title:
    fontFamily: "Fraunces, Georgia, serif"
    fontSize: "1.65rem"
    fontWeight: 500
    lineHeight: 1.15
  body:
    fontFamily: "system-ui, -apple-system, sans-serif"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: 1.6
  body-mobile:
    fontFamily: "system-ui, -apple-system, sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.6
  label:
    fontFamily: "system-ui, -apple-system, sans-serif"
    fontSize: "0.86rem"
    fontWeight: 400
rounded:
  square: "0px"
  diagram-node: "6px"
spacing:
  mobile-gutter: "16px"
  tablet-gutter: "20px"
  desktop-gutter: "40px"
  control-gap: "9px"
  section-space: "110px"
  tablet-section-space: "75px"
components:
  button-stage:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.label}"
    rounded: "{rounded.square}"
    padding: "12px 14px"
    height: "59px"
  button-step:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.square}"
    padding: "6px 12px"
  button-selected:
    backgroundColor: "{colors.selected-fill}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.square}"
    padding: "9px 15px"
  diagram-frame:
    backgroundColor: "{colors.wash}"
    textColor: "{colors.ink}"
    rounded: "{rounded.square}"
    padding: "18px"
---

# Design System: Palinode Loop

## Overview

**Creative North Star: “The Revisable Ledger”**

The page pairs an editorial reading voice with a diagram that makes the workflow inspectable. Fraunces headlines carry the argument; plain sans-serif copy explains the mechanics. Warm paper and dark ink establish the reading surfaces, while teal traces the path and terracotta marks the consequential approval boundary.

The system stays quiet around its evidence: generous section spacing, thin rules, and open layouts let the loop and source details do the work. The same visual language moves into a dark walkthrough, where selected stages remain easy to distinguish. The authored SVG is the signature object; on narrow screens it scrolls inside its own frame rather than widening the page.

**Key Characteristics:**
- Editorial serif headlines with direct, readable sans-serif copy.
- Warm paper surfaces against deep ink, with teal and terracotta carrying meaning.
- Evidence and approval shown as separate stages, not interchangeable signals.

## Colors

Warm paper, blue-green ink, and restrained green and terracotta accents keep the experience calm while giving the approval boundary a clear visual signal.

### Primary
- **Deep blue-green ink** (`colors.ink`): Main text, dark walkthrough surface, and code panel.

### Secondary
- **Path teal** (`colors.teal`): Links, loop connectors, focus on active diagram nodes, and section rules.

### Tertiary
- **Decision terracotta** (`colors.rust`): The human approval gate, selected emphasis, and focus outline.

### Neutral
- **Warm paper** (`colors.paper`): Main reading canvas and the light text color on the dark walkthrough.
- **Soft parchment** (`colors.wash`): Diagram frame against the page canvas.
- **Active mint** (`colors.active-fill`): Current loop node.
- **Selected mint** (`colors.selected-fill`): Chosen walkthrough stage and simulated decision.
- **Pale on dark** (`colors.on-dark`): Stage labels on the walkthrough surface.
- **Muted green divider** (`colors.dark-divider`): Grid lines and inset-code borders on dark surfaces.
- **Deep inset green** (`colors.inset`): Walkthrough excerpt panel.

**The Gate Accent Rule.** Reserve terracotta for the approval boundary and the hero's emphasized word; it marks a consequential human decision.

## Typography

**Display Font:** Fraunces (self-hosted), with Georgia and serif fallbacks

**Body Font:** system-ui, -apple-system, sans-serif
**Label/Mono Font:** Bold Arial in the authored SVG; ui-monospace, SFMono-Regular, monospace for executable commands.

**Character:** Fraunces supplies an expressive editorial voice without making the technical explanation ornate. Sans-serif body copy and compact labels keep the steps, evidence and controls practical.

### Hierarchy
- **Display** (500 weight, tight line-height): Hero statement and major section headings.
- **Headline** (500 weight, balanced): Section titles, including the tour and evidence sections.
- **Title** (500 weight): Study headings and the current walkthrough stage.
- **Body** (400 weight, generous line-height): Explanatory copy, constrained to readable measures where specified.
- **Label** (regular sans-serif; bold in the diagram): Navigation, controls, stage names and SVG process labels.

## Layout

The page uses a centered reading frame capped at 1320px. Wide layouts pair the hero statement with the loop diagram and place section headings beside explanatory material. At the tablet breakpoint, these become single-column reading flows and section spacing tightens. At the mobile breakpoint, gutters tighten, the walkthrough selector becomes two columns, and principle items stack. The loop diagram keeps a wide minimum drawing width in a bounded horizontal scroll region, with a visible instruction to scroll it.

Spacing is deliberately open: page gutters tighten in two responsive steps, main sections reduce their vertical padding at tablet width, and controls stay compact beside generous content gaps.

## Elevation & Depth

The system is flat. It uses background tone changes, thin borders, and the dark walkthrough surface to separate regions; no drop shadows are present. Focus is shown with a visible terracotta outline rather than elevation.

## Shapes

Panels and controls are square-cornered. The loop's SVG nodes use a restrained corner radius; their fill and stroke change to show the active step, approval gate, and held candidate. Thin rules define the masthead, section endings, study entries, and code frame.

## Components

### Navigation
- **Character:** Quiet text links beside a serif wordmark.
- **Style:** Underlined teal links; hover shifts to terracotta. The wordmark uses Fraunces and remains dark ink.
- **Mobile:** Links wrap within the masthead; the reading frame narrows with the viewport.

### Buttons
- **Character:** Plain, rectangular controls with clear state changes.
- **Step selectors:** Dark background with pale labels; the selected stage switches to a pale mint surface and dark ink.
- **Decision controls:** Transparent on the dark walkthrough with a light border; the selected decision uses pale mint fill and dark text.
- **Diagram controls:** Transparent with teal borders and dark text; hover receives a pale green fill.
- **Focus / disabled:** Focus uses a 3px terracotta outline with offset. Disabled controls lower opacity and use a not-allowed cursor.

### Cards / Containers
- **Diagram frame:** Parchment fill, fine warm border, and open inset padding. The inner SVG scrolls horizontally on narrow screens.
- **Walkthrough surface:** Full-width dark ink field with pale text; selected steps and decisions use a light mint contrast.
- **Evidence entries:** Open rows divided by thin rules rather than individual filled cards.

### Signature Component: Evidence Loop

The six-stage SVG is the page's central explainer. Teal connectors show sequence; the active stage receives a mint fill; terracotta identifies the human gate and held-candidate branch. Stage controls, keyboard navigation, playback, and code mapping change the explanation without implying that the CLI changes a ledger.

## Do's and Don'ts

### Do:
- **Do** use teal for the path and navigation, and terracotta for the human approval boundary.
- **Do** keep the diagram inside its own scroll region on narrow layouts.
- **Do** preserve the difference between candidate, decision, active rule, and later feedback.
- **Do** keep playback opt-in and honor reduced-motion settings for transitions.

### Don't:
- **Don't** use terracotta as a general-purpose highlight; it carries the gate and revision meaning.
- **Don't** stretch the SVG loop to force it into a narrow viewport; keep the bounded horizontal scroll behavior.
- **Don't** add shadows or rounded card stacks; depth comes from tonal surfaces and rules.
