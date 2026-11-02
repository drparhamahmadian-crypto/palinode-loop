# Palinode Loop

<!-- impeccable:product-schema 1 -->

## Platform

GitHub-ready open-source repository with a standalone dark HTML/SVG explainer and a local Python command-line reference implementation.

## Stack

Standalone HTML with authored SVG and local static assets; Python 3.10+ standard library. No runtime service, network dependency, or third-party Python package.

## Users

Developers and researchers inspecting agent-memory and feedback designs, and maintainers reviewing a small, reproducible implementation.

## Product Purpose

Make documented agent failures actionable through an explicit lifecycle: evidence-bearing candidate, human policy decision, active scoped rule, and visible feedback when that rule fails again. The architectural contribution is this governed evidence-to-intervention path.

## Capabilities and Constraints

The CLI validates a local version 1 ledger and renders active rules for human review. It does not capture conversations, authenticate approvals, fetch sources, run a model, change ledger states, or enforce guidance in a host. The interactive SVG walkthrough moves a synthetic evidence packet through the lifecycle and shows the hold/approval boundary without changing the CLI ledger.

The repository documents published results for related mechanisms with the studied systems and task conditions clearly attributed. Do not transfer those results to Palinode Loop or report a measured Palinode effectiveness gain. No new efficacy experiment is required for this release.

Use precise domain language, concise explanatory copy, and code examples that experts can inspect and reproduce. The architecture should remain understandable without the animation.

## Brand Commitments

Working identity: Palinode Loop. Preserve the philosophical idea of revision and corrigibility. Use a dark, high-contrast GitHub-oriented presentation with a compact type hierarchy, restrained accents, and an inspectable SVG architecture. Reduce controls to the essential walkthrough actions; make code and schema examples visually clear.

## Privacy

Use synthetic fixtures only. Do not include private source history, personal paths, account configuration, credentials, patient information, or real conversation records. The explainer uses local assets and sends no analytics or data.

## Accessibility

Keep SVG labels readable and provide a static diagram; support keyboard navigation, visible focus, reduced motion, narrow-screen reflow, and horizontal diagram scrolling within a bounded region.
