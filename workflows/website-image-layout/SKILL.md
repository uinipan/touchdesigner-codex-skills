---
name: website-image-layout
description: Arrange images for simple website and portfolio galleries. Use when adding project photos, screenshots, posters, transparent cutouts, or other media that need classification, paired or full-width layouts, scaling, cropping, and alignment.
---

# Website Image Layout

Create restrained, image-led project galleries without introducing a heavy gallery system.

## Workflow

1. Inspect every candidate image's dimensions and visual content.
2. Exclude the page cover from the body unless repetition is intentional.
3. Group images by meaning, such as exhibition documentation, process, interface, or final outcome.
4. Choose layouts by aspect ratio and importance:
   - Pair images with similar proportions.
   - Use a single full-width image for a key frame or an unpaired image.
   - Pair portrait images only when their ratios are close.
   - Avoid forcing mixed-ratio images into square crops.
5. Add bilingual section headings when the project page is bilingual.
6. Reference images from `/projects/{slug}/images/` in the project's Markdown.
7. Reuse gallery classes in `src/pages/projects/[id].astro`; add a modifier only when the existing classes cannot express the layout.
8. Build the Astro site and verify desktop and mobile wrapping.

## Layout Rules

- Use two columns on desktop and one column on narrow screens.
- Keep gaps at `1rem`.
- Use `object-fit: cover` for photos and screenshots with compatible crops.
- Use `object-fit: contain` for posters, diagrams, and transparent cutouts.
- Give paired items a stable shared aspect ratio so rows align.
- Preserve the artwork's visual center with `object-position` when needed.
- Keep captions optional and short; do not narrate obvious image content.
- Do not move, rename, delete, or overwrite source images unless explicitly requested.

## Preferred Classes

- `.project-media-grid`: base grid.
- `.project-media-grid--two`: two-column pair.
- `.project-media-grid--portrait`: portrait pair using contain.
- `.project-media-grid--landscape`: photographic landscape pair.
- `.project-media-grid--wide`: wide screenshot pair.
- `.project-media-single`: one full-width image.

Use semantic `alt` text and lazy loading for all body images.
